"""Lifecycle, compatibility and Review Gate rules for Task State projection."""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from task_state_io import (
    EDITORIAL_ROOT,
    APPROVAL_EVIDENCE_RE,
    CREATED_RE,
    CURRENT_STATUS_RE,
    CURRENT_ARTIFACT_RE,
    HISTORICAL_STATUSES,
    HUMAN_APPROVAL_REQUIRED_RE,
    HUMAN_APPROVAL_STATE_RE,
    INDEPENDENCE_RE,
    LIFECYCLE_CONTRACT_RE,
    NEXT_ACTION_RE,
    OWNER_RE,
    PAUSED_STATUSES,
    PIPELINES_DIR,
    PREVIOUS_STATUS_RE,
    PRODUCER_ID_RE,
    REVIEWER_ID_RE,
    PRODUCER_ROLE_RE,
    PROJECTION_VERSION,
    REQUIRED_INPUTS,
    REVIEWED_ARTIFACT_RE,
    REVIEWED_SHA_RE,
    REVIEWER_ROLE_RE,
    SELECTED_PIPELINE_RE,
    SINCE_RE,
    STATUSES_PATH,
    TASK_ID_RE,
    TASK_TYPE_RE,
    TASKS_ROOT,
    TERMINAL_STATUSES,
    UPDATED_RE,
    clean_field_value,
    extract_capabilities,
    extract_review_outcomes,
    extract_section_bullets,
    extract_located,
    load_allowed_transitions,
    load_capability_ids,
    load_known_statuses,
    load_role_ids,
    normalize_pipeline,
    normalize_value,
    resolve_pipeline_id,
    resolve_task_directory,
    safe_relative_file,
    sha256_bytes,
)
from task_state_types import Diagnostic, LocatedValue, SourceLocation, utc_now


def resolve_role(raw: str | None, known_roles: set[str]) -> str | None:
    if not raw:
        return None
    normalized = normalize_value(raw)
    aliases = {
        "chief_editor_orchestrator": "chief_editor",
        "chief_editor": "chief_editor",
        "writer": "writer_agent",
        "reviewer": "review_agent",
        "review": "review_agent",
        "ux_writer": "ux_writer",
        "final_editor": "final_editor",
        "researcher": "research_agent",
        "research_agent": "research_agent",
        "intake": "intake_agent",
    }
    if normalized in known_roles:
        return normalized
    if normalized in aliases:
        return aliases[normalized]
    matches = [
        role
        for role in sorted(known_roles, key=len, reverse=True)
        if re.search(rf"(?<![a-z0-9]){re.escape(role)}(?![a-z0-9])", normalized)
    ]
    return matches[0] if len(matches) == 1 else normalized


def derive_stage(status: str | None) -> str:
    mapping = {
        "intake": "intake",
        "planning": "routing",
        "research": "research",
        "writing": "drafting",
        "editing": "drafting",
        "ux_writing": "ux_writing",
        "review": "review",
        "changes_requested": "repair",
        "approved": "finalization",
        "human_approval_required": "governance",
        "finalized": "governance",
        "archived": "governance",
        "blocked": "unknown",
        "failed": "unknown",
    }
    return mapping.get(status or "", "unknown")


def derive_terminal_state(status: str | None) -> str:
    if status in TERMINAL_STATUSES:
        return "terminal"
    if status == "failed":
        return "terminal_under_current_constraints"
    if status in PAUSED_STATUSES:
        return "paused"
    return "active" if status else "unknown"


def approval_value(raw: str | None) -> str:
    if raw is None:
        return "unknown"
    value = normalize_value(raw)
    if value in {"no", "none", "not_required", "not_applicable", "false"}:
        return "not_required"
    if value in {"approved", "granted", "yes_approved"}:
        return "approved"
    if value in {"rejected", "denied"}:
        return "rejected"
    if value in {"requested", "pending", "required", "yes", "true"} or value.startswith(
        "yes_"
    ):
        return "required"
    return "unknown"



def append_conflict(
    diagnostics: list[Diagnostic],
    code: str,
    message: str,
    left: LocatedValue,
    right: LocatedValue,
    *,
    historical: bool = False,
) -> None:
    diagnostics.append(
        Diagnostic(
            "warning" if historical else "error",
            code,
            message,
            left.source,
            {
                "values": [
                    {"value": left.value, "source": asdict(left.source)},
                    {"value": right.value, "source": asdict(right.source)},
                ]
            },
        )
    )


@dataclass(frozen=True)
class _TaskViews:
    manifest: str
    status: str
    brief: str
    plan: str
    review: str
    approval: str


@dataclass(frozen=True)
class _LifecycleEvaluation:
    task_id: str | None
    task_type: str | None
    current_status: str | None
    previous_status: str | None
    current_stage: str
    terminal_state: str
    strict_opt_in: bool
    contract_loc: LocatedValue | None
    status_status: LocatedValue | None
    known_statuses: set[str] | None


@dataclass(frozen=True)
class _RoutingEvaluation:
    active_pipeline: str | None
    active_capabilities: list[str]
    current_owner: str | None
    next_action: str | None
    pipeline_loc: LocatedValue | None
    known_roles: set[str]


@dataclass(frozen=True)
class _ReviewGovernanceEvaluation:
    review_state: dict[str, Any]
    blockers: list[str]
    human_state: str
    current_artifact: str | None
    current_artifact_current: bool
    timestamps: dict[str, str | None]
    strict_missing: list[str]


@dataclass(frozen=True)
class _ExecutionClassification:
    compatibility_mode: str
    valid_for_execution: bool


def _assemble_invalid_projection(
    diagnostics: list[Diagnostic], generated_at: str | None
) -> dict[str, Any]:
    return {
        "projection_version": PROJECTION_VERSION,
        "generated_at": generated_at or utc_now(),
        "source_fingerprints": {},
        "valid_for_execution": False,
        "diagnostics": [item.to_dict() for item in diagnostics],
        "task": {
            "compatibility_mode": "unsupported",
            "terminal_state": "unknown",
        },
    }


def _collect_task_views(
    texts: dict[str, str], diagnostics: list[Diagnostic]
) -> _TaskViews:
    for required in REQUIRED_INPUTS:
        if required not in texts:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "required_file_missing",
                    f"{required} is missing.",
                    SourceLocation(required),
                )
            )
        elif not texts[required].strip():
            diagnostics.append(
                Diagnostic(
                    "error",
                    "required_file_empty",
                    f"{required} is empty.",
                    SourceLocation(required),
                )
            )

    manifest = texts.get("task-manifest.md", "")
    status = texts.get("status.md", "")
    brief = texts.get("brief.md", "")
    plan = texts.get("orchestration_plan.md", "")
    review = texts.get("review.md", "")
    approval = texts.get("approval.md", "")

    return _TaskViews(
        manifest=manifest,
        status=status,
        brief=brief,
        plan=plan,
        review=review,
        approval=approval,
    )


def _evaluate_identity_and_lifecycle(
    views: _TaskViews, diagnostics: list[Diagnostic]
) -> _LifecycleEvaluation:
    manifest = views.manifest
    status = views.status
    brief = views.brief

    contract_loc = extract_located(
        manifest, LIFECYCLE_CONTRACT_RE, "task-manifest.md"
    )
    contract_version = (
        normalize_value(contract_loc.value) if contract_loc is not None else None
    )
    strict_opt_in = contract_version == "1"
    if contract_loc is not None and not strict_opt_in:
        diagnostics.append(
            Diagnostic(
                "error",
                "lifecycle_contract_version_unknown",
                f"Lifecycle contract version `{contract_loc.value}` is unsupported.",
                contract_loc.source,
                {"normalized_value": contract_version},
            )
        )

    task_id_values = [
        item
        for item in (
            extract_located(manifest, TASK_ID_RE, "task-manifest.md"),
            extract_located(status, TASK_ID_RE, "status.md"),
            extract_located(brief, TASK_ID_RE, "brief.md"),
        )
        if item is not None
    ]
    task_id = task_id_values[0].value if task_id_values else None
    for other in task_id_values[1:]:
        if normalize_value(other.value) != normalize_value(task_id_values[0].value):
            append_conflict(
                diagnostics,
                "task_id_conflict",
                "Task ID differs across canonical task views.",
                task_id_values[0],
                other,
            )

    task_type_loc = extract_located(manifest, TASK_TYPE_RE, "task-manifest.md")
    if task_type_loc is None:
        task_type_loc = extract_located(brief, TASK_TYPE_RE, "brief.md")
    task_type = task_type_loc.value if task_type_loc else None

    manifest_status = extract_located(manifest, CURRENT_STATUS_RE, "task-manifest.md")
    status_status = extract_located(status, CURRENT_STATUS_RE, "status.md")
    status_candidates = [item for item in (status_status, manifest_status) if item]
    current_raw = status_candidates[0].value if status_candidates else None
    current_status = normalize_value(current_raw) if current_raw else None
    historical_hint = current_status in HISTORICAL_STATUSES
    if manifest_status and status_status:
        if normalize_value(manifest_status.value) != normalize_value(status_status.value):
            both_historical = {
                normalize_value(manifest_status.value),
                normalize_value(status_status.value),
            }.issubset(HISTORICAL_STATUSES)
            append_conflict(
                diagnostics,
                "status_conflict",
                "task-manifest.md current status "
                f"`{manifest_status.value}` differs from status.md current status "
                f"`{status_status.value}`.",
                manifest_status,
                status_status,
                historical=both_historical,
            )
    if manifest and manifest_status is None:
        diagnostics.append(
            Diagnostic(
                "error",
                "manifest_status_missing",
                "task-manifest.md does not contain a recognizable current status.",
                SourceLocation("task-manifest.md"),
            )
        )
    if status and status_status is None:
        diagnostics.append(
            Diagnostic(
                "warning",
                "status_status_missing",
                "status.md does not contain a recognizable current status.",
                SourceLocation("status.md"),
            )
        )

    previous_loc = extract_located(status, PREVIOUS_STATUS_RE, "status.md")
    previous_status = normalize_value(previous_loc.value) if previous_loc else None
    if status and previous_loc is None:
        diagnostics.append(
            Diagnostic(
                "warning",
                "previous_status_missing",
                "status.md does not contain a recognizable previous status.",
                SourceLocation("status.md"),
            )
        )

    known_statuses = load_known_statuses()
    transitions = load_allowed_transitions()
    if known_statuses is None:
        diagnostics.append(
            Diagnostic(
                "warning",
                "status_canon_unavailable",
                "Could not verify current status against known task statuses.",
                SourceLocation(str(STATUSES_PATH.relative_to(EDITORIAL_ROOT))),
            )
        )
    else:
        for label, value, loc in (
            ("current status", current_status, status_status or manifest_status),
            ("previous status", previous_status, previous_loc),
        ):
            if value and value != "none" and value not in known_statuses:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unknown_status",
                        f"{label.capitalize()} `{loc.value if loc else value}` is not "
                        "listed in kb/task_statuses.md.",
                        loc.source if loc else None,
                        {"normalized_value": value},
                    )
                )
    if transitions is None:
        diagnostics.append(
            Diagnostic(
                "warning",
                "transition_canon_unavailable",
                "Could not verify status transitions against kb/task_statuses.md.",
            )
        )
    if previous_status and current_status:
        if previous_status == current_status:
            diagnostics.append(
                Diagnostic(
                    "warning",
                    "same_previous_current_status",
                    "status.md previous status and current status are the same; "
                    "transition was not validated.",
                    previous_loc.source if previous_loc else None,
                )
            )
        elif previous_status == "blocked" and current_status == "finalized":
            diagnostics.append(
                Diagnostic(
                    "error",
                    "blocked_directly_finalized",
                    "Blocked task must not move directly to finalized.",
                    previous_loc.source if previous_loc else None,
                )
            )
        elif (
            previous_status != "none"
            and known_statuses is not None
            and transitions is not None
            and previous_status in known_statuses
            and current_status in known_statuses
            and current_status not in transitions.get(previous_status, set())
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_transition",
                    f"Invalid status transition: `{previous_loc.value}` -> "
                    f"`{current_raw}` is not allowed by kb/task_statuses.md.",
                    previous_loc.source,
                    {"from": previous_status, "to": current_status},
                )
            )

    return _LifecycleEvaluation(
        task_id=task_id,
        task_type=task_type,
        current_status=current_status,
        previous_status=previous_status,
        current_stage=derive_stage(current_status),
        terminal_state=derive_terminal_state(current_status),
        strict_opt_in=strict_opt_in,
        contract_loc=contract_loc,
        status_status=status_status,
        known_statuses=known_statuses,
    )


def _evaluate_routing_metadata(
    views: _TaskViews,
    lifecycle: _LifecycleEvaluation,
    diagnostics: list[Diagnostic],
) -> _RoutingEvaluation:
    manifest = views.manifest
    status = views.status
    plan = views.plan
    historical_hint = lifecycle.current_status in HISTORICAL_STATUSES

    manifest_pipeline = extract_located(
        manifest, SELECTED_PIPELINE_RE, "task-manifest.md"
    )
    plan_pipeline = extract_located(plan, SELECTED_PIPELINE_RE, "orchestration_plan.md")
    pipeline_loc = manifest_pipeline or plan_pipeline
    active_pipeline = resolve_pipeline_id(pipeline_loc.value) if pipeline_loc else None
    if pipeline_loc and active_pipeline is None:
        active_pipeline = pipeline_loc.value
    if manifest_pipeline and plan_pipeline:
        manifest_pipeline_id = resolve_pipeline_id(manifest_pipeline.value)
        plan_pipeline_id = resolve_pipeline_id(plan_pipeline.value)
        if (manifest_pipeline_id or normalize_pipeline(manifest_pipeline.value)) != (
            plan_pipeline_id or normalize_pipeline(plan_pipeline.value)
        ):
            append_conflict(
                diagnostics,
                "pipeline_conflict",
                "Selected pipeline differs between manifest and orchestration plan.",
                manifest_pipeline,
                plan_pipeline,
                historical=True,
            )
    if pipeline_loc is None:
        diagnostics.append(
            Diagnostic(
                "warning",
                "pipeline_missing",
                "Selected pipeline was not found in task-manifest.md or "
                "orchestration_plan.md.",
            )
        )
    else:
        pipeline_id = resolve_pipeline_id(pipeline_loc.value)
        pipeline_path = (
            PIPELINES_DIR / f"{pipeline_id}_pipeline.md"
            if pipeline_id
            else PIPELINES_DIR / "__unresolved__.md"
        )
        if not pipeline_path.is_file():
            diagnostics.append(
                Diagnostic(
                    "error",
                    "pipeline_unknown",
                    f"Selected pipeline `{active_pipeline}` does not map to an "
                    "existing pipeline file.",
                    pipeline_loc.source,
                )
            )

    known_roles = load_role_ids()
    manifest_owner = extract_located(manifest, OWNER_RE, "task-manifest.md")
    status_owner = extract_located(status, OWNER_RE, "status.md")
    owner_loc = manifest_owner or status_owner
    current_owner = resolve_role(owner_loc.value if owner_loc else None, known_roles)
    if manifest_owner and status_owner:
        left = resolve_role(manifest_owner.value, known_roles)
        right = resolve_role(status_owner.value, known_roles)
        if left != right:
            diagnostics.append(
                Diagnostic(
                    "warning" if historical_hint else "error",
                    "owner_conflict",
                    "Current owner differs between manifest and status.",
                    manifest_owner.source,
                    {
                        "values": [
                            {"value": manifest_owner.value, "normalized": left},
                            {"value": status_owner.value, "normalized": right},
                        ]
                    },
                )
            )
    if owner_loc and current_owner not in known_roles:
        diagnostics.append(
            Diagnostic(
                "error" if not historical_hint else "warning",
                "owner_unknown",
                f"Current owner `{owner_loc.value}` does not map to an existing role.",
                owner_loc.source,
                {"normalized_value": current_owner},
            )
        )
    elif owner_loc is None:
        diagnostics.append(
            Diagnostic("warning", "owner_missing", "Current owner was not found.")
        )

    next_loc = extract_located(manifest, NEXT_ACTION_RE, "task-manifest.md")
    if next_loc is None:
        next_loc = extract_located(status, NEXT_ACTION_RE, "status.md")
    next_action = next_loc.value if next_loc else None

    known_capabilities = load_capability_ids()
    active_capabilities = extract_capabilities((manifest, plan))
    if known_capabilities is None:
        diagnostics.append(
            Diagnostic(
                "warning",
                "capability_canon_unavailable",
                "Could not resolve capabilities from kb/capability_registry.md.",
            )
        )
    else:
        for capability in active_capabilities:
            if capability not in known_capabilities:
                diagnostics.append(
                    Diagnostic(
                        "warning",
                        "capability_unknown",
                        f"Active capability `{capability}` does not resolve to a "
                        "Capability Registry heading.",
                        details={"capability_id": capability},
                    )
                )


    return _RoutingEvaluation(
        active_pipeline=active_pipeline,
        active_capabilities=active_capabilities,
        current_owner=current_owner,
        next_action=next_action,
        pipeline_loc=pipeline_loc,
        known_roles=known_roles,
    )


def _evaluate_review_and_governance(
    resolved_task: Path,
    views: _TaskViews,
    lifecycle: _LifecycleEvaluation,
    routing: _RoutingEvaluation,
    raw_inputs: dict[str, bytes],
    fingerprints: dict[str, str],
    diagnostics: list[Diagnostic],
) -> _ReviewGovernanceEvaluation:
    manifest = views.manifest
    status = views.status
    review = views.review
    approval = views.approval
    current_status = lifecycle.current_status
    status_status = lifecycle.status_status
    strict_opt_in = lifecycle.strict_opt_in
    task_type = lifecycle.task_type
    previous_status = lifecycle.previous_status
    contract_loc = lifecycle.contract_loc
    active_pipeline = routing.active_pipeline
    active_capabilities = routing.active_capabilities
    current_owner = routing.current_owner
    next_action = routing.next_action
    pipeline_loc = routing.pipeline_loc
    known_roles = routing.known_roles

    blockers = extract_section_bullets(status, "active blockers")
    if not blockers:
        blockers = extract_section_bullets(status, "blockers or approvals")

    review_state: dict[str, Any] = {
        "present": bool(review),
        "outcome": None,
        "reviewer_role": None,
        "producer_role": None,
        "reviewer_identity": None,
        "producer_identity": None,
        "independence": "unknown",
        "technical_evidence": "not_present",
    }
    if review:
        outcomes = extract_review_outcomes(review)
        distinct_outcomes = list(dict.fromkeys(normalize_value(item.value) for item in outcomes))
        if len(distinct_outcomes) == 1:
            review_state["outcome"] = distinct_outcomes[0]
        elif len(distinct_outcomes) > 1:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "review_outcome_conflict",
                    "review.md contains contradictory recognized outcomes.",
                    outcomes[0].source,
                    {"values": distinct_outcomes},
                )
            )
        else:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "review_outcome_missing",
                    "review.md does not contain a recognized outcome.",
                    SourceLocation("review.md"),
                )
            )
        reviewer_role_loc = extract_located(review, REVIEWER_ROLE_RE, "review.md")
        producer_role_loc = extract_located(review, PRODUCER_ROLE_RE, "review.md")
        reviewer_id_loc = extract_located(review, REVIEWER_ID_RE, "review.md")
        producer_id_loc = extract_located(review, PRODUCER_ID_RE, "review.md")
        independence_loc = extract_located(review, INDEPENDENCE_RE, "review.md")
        review_state.update(
            {
                "reviewer_role": resolve_role(
                    reviewer_role_loc.value if reviewer_role_loc else None, known_roles
                ),
                "producer_role": resolve_role(
                    producer_role_loc.value if producer_role_loc else None, known_roles
                ),
                "reviewer_identity": reviewer_id_loc.value if reviewer_id_loc else None,
                "producer_identity": producer_id_loc.value if producer_id_loc else None,
                "independence": normalize_value(independence_loc.value)
                if independence_loc
                else "unknown",
            }
        )
        same_role = (
            review_state["reviewer_role"]
            and review_state["producer_role"]
            and review_state["reviewer_role"] == review_state["producer_role"]
        )
        same_identity = (
            review_state["reviewer_identity"]
            and review_state["producer_identity"]
            and normalize_value(review_state["reviewer_identity"])
            == normalize_value(review_state["producer_identity"])
        )
        explicit_no = review_state["independence"] in {"no", "false", "not_confirmed"}
        if same_role or same_identity or explicit_no:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "review_self_approval",
                    "Producer/reviewer evidence explicitly violates review independence.",
                    reviewer_role_loc.source if reviewer_role_loc else SourceLocation("review.md"),
                    {
                        "same_role": bool(same_role),
                        "same_identity": bool(same_identity),
                        "independence": review_state["independence"],
                    },
                )
            )

    has_final = (resolved_task / "final.md").is_file()
    if current_status == "approved" and blockers:
        diagnostics.append(
            Diagnostic(
                "error",
                "approved_with_active_blocker",
                "Current status `approved` conflicts with active blocker evidence.",
                status_status.source if status_status else SourceLocation("status.md"),
                {"blockers": blockers},
            )
        )
    if current_status == "blocked" and not blockers:
        diagnostics.append(
            Diagnostic(
                "error",
                "blocked_without_blocker_evidence",
                "Current status `blocked` requires at least one active blocker.",
                status_status.source if status_status else SourceLocation("status.md"),
            )
        )
    if current_status == "finalized" and not has_final:
        diagnostics.append(
            Diagnostic(
                "error" if strict_opt_in else "warning",
                "finalized_without_final_artifact",
                "Current status `finalized` has no final.md artifact.",
                status_status.source if status_status else SourceLocation("status.md"),
            )
        )
    if (
        current_status == "finalized"
        and not has_final
        and review_state["outcome"] != "approved"
    ):
        diagnostics.append(
            Diagnostic(
                "error" if strict_opt_in else "warning",
                "finalized_review_not_machine_verifiable",
                "Current status `finalized` has no machine-verifiable approved "
                "Review Gate evidence.",
                SourceLocation("review.md" if review else "status.md"),
            )
        )
    if has_final and not review:
        diagnostics.append(
            Diagnostic(
                "error",
                "final_without_review",
                "final.md exists but review.md is missing.",
                SourceLocation("final.md"),
            )
        )
    if has_final and review_state["outcome"] != "approved":
        if review_state["outcome"] is None:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "final_review_outcome_missing",
                    "final.md exists but review outcome is missing.",
                    SourceLocation("review.md" if review else "final.md"),
                )
            )
        else:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "final_review_not_approved",
                    f"final.md exists but review outcome is "
                    f"{review_state['outcome']}, not approved.",
                    SourceLocation("review.md"),
                )
            )
    if current_status == "approved" and review_state["outcome"] != "approved":
        diagnostics.append(
            Diagnostic(
                "error",
                "status_requires_approved_review",
                f"Current status `{current_status}` requires an approved Review Gate.",
                status_status.source if status_status else None,
            )
        )
    if current_status == "changes_requested" and review_state["outcome"] not in {
        None,
        "changes_requested",
    }:
        diagnostics.append(
            Diagnostic(
                "error",
                "status_review_outcome_conflict",
                "Current status `changes_requested` conflicts with the recognized "
                f"review outcome `{review_state['outcome']}`.",
                SourceLocation("review.md"),
            )
        )

    reviewed_artifact_loc = extract_located(review, REVIEWED_ARTIFACT_RE, "review.md")
    reviewed_sha_loc = extract_located(review, REVIEWED_SHA_RE, "review.md")
    if reviewed_artifact_loc and reviewed_sha_loc:
        reviewed_path = safe_relative_file(
            resolved_task,
            reviewed_artifact_loc.value,
            diagnostics,
            "reviewed_artifact_path_invalid",
        )
        if reviewed_path:
            relative = reviewed_path.relative_to(resolved_task).as_posix()
            data = reviewed_path.read_bytes()
            raw_inputs.setdefault(relative, data)
            fingerprints.setdefault(relative, sha256_bytes(data))
            expected = clean_field_value(reviewed_sha_loc.value).removeprefix("sha256:")
            actual = hashlib.sha256(data).hexdigest()
            review_state["technical_evidence"] = "current" if expected == actual else "stale"
            if expected != actual:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "stale_review_evidence",
                        f"Reviewed artifact `{relative}` no longer matches the "
                        "recorded SHA-256.",
                        reviewed_sha_loc.source,
                        {
                            "artifact": relative,
                            "expected": f"sha256:{expected}",
                            "actual": f"sha256:{actual}",
                        },
                    )
                )

    required_loc = extract_located(status, HUMAN_APPROVAL_REQUIRED_RE, "status.md")
    if required_loc is None:
        required_loc = extract_located(
            manifest, HUMAN_APPROVAL_REQUIRED_RE, "task-manifest.md"
        )
    state_loc = extract_located(status, HUMAN_APPROVAL_STATE_RE, "status.md")
    if state_loc is None:
        state_loc = extract_located(approval, HUMAN_APPROVAL_STATE_RE, "approval.md")
    evidence_loc = extract_located(status, APPROVAL_EVIDENCE_RE, "status.md")
    if evidence_loc is None:
        evidence_loc = extract_located(approval, APPROVAL_EVIDENCE_RE, "approval.md")
    human_state = approval_value(state_loc.value if state_loc else None)
    required_state = approval_value(required_loc.value if required_loc else None)
    if current_status == "human_approval_required":
        human_state = "requested"
    elif human_state == "unknown" and required_state != "unknown":
        human_state = required_state
    evidence_value = normalize_value(evidence_loc.value) if evidence_loc else "none"
    evidence_present = evidence_value not in {
        "",
        "none",
        "not_present",
        "not_provided",
        "pending",
        "unknown",
    }
    if human_state in {"approved", "rejected"} and not evidence_present:
        diagnostics.append(
            Diagnostic(
                "error",
                "approval_without_evidence",
                f"Human approval is asserted as `{human_state}` without canonical evidence.",
                state_loc.source if state_loc else None,
            )
        )
    if (
        current_status == "finalized"
        and required_state == "required"
        and not evidence_present
    ):
        diagnostics.append(
            Diagnostic(
                "warning",
                "finalized_without_human_approval_evidence",
                "Task is finalized although human approval is required and no "
                "canonical approval evidence is present.",
                required_loc.source if required_loc else None,
            )
        )

    current_artifact_loc = extract_located(
        manifest, CURRENT_ARTIFACT_RE, "task-manifest.md"
    )
    current_artifact = current_artifact_loc.value if current_artifact_loc else None
    current_artifact_current = False
    if current_artifact_loc:
        current_path = safe_relative_file(
            resolved_task,
            current_artifact_loc.value,
            diagnostics,
            "current_artifact_path_invalid",
            unsafe_level="warning",
        )
        if current_path:
            relative = current_path.relative_to(resolved_task).as_posix()
            data = current_path.read_bytes()
            raw_inputs.setdefault(relative, data)
            fingerprints.setdefault(relative, sha256_bytes(data))
            current_artifact_current = True

    timestamps: dict[str, str | None] = {}
    for key, pattern, text, source in (
        ("created", CREATED_RE, manifest, "task-manifest.md"),
        ("updated", UPDATED_RE, manifest, "task-manifest.md"),
        ("since", SINCE_RE, status, "status.md"),
    ):
        value = extract_located(text, pattern, source)
        timestamps[key] = value.value if value else None

    strict_missing: list[str] = []
    if strict_opt_in:
        strict_requirements = {
            "task_type": bool(task_type),
            "previous_status": bool(previous_status),
            "active_pipeline": bool(
                pipeline_loc and resolve_pipeline_id(pipeline_loc.value)
            ),
            "active_capabilities": bool(active_capabilities),
            "current_owner": current_owner in known_roles,
            "next_action": bool(next_action),
            "current_artifact": bool(
                current_artifact and current_artifact_current
            ),
            "human_approval_state": human_state != "unknown",
        }
        strict_missing.extend(
            name for name, present in strict_requirements.items() if not present
        )
        if current_status in {"review", "approved"} and not review_state["outcome"]:
            strict_missing.append("review_state.outcome")
        if current_status == "approved":
            independence_confirmed = review_state["independence"] in {
                "yes",
                "true",
                "confirmed",
            }
            strict_review_requirements = {
                "review_state.reviewer_role": (
                    review_state["reviewer_role"] == "review_agent"
                ),
                "review_state.producer_role": (
                    review_state["producer_role"] in known_roles
                    and review_state["producer_role"] != "review_agent"
                ),
                "review_state.reviewer_identity": bool(
                    review_state["reviewer_identity"]
                ),
                "review_state.producer_identity": bool(
                    review_state["producer_identity"]
                ),
                "review_state.independence_confirmed": independence_confirmed,
                "review_state.current_fingerprint": (
                    review_state["technical_evidence"] == "current"
                ),
                "blockers.empty": not blockers,
            }
            strict_missing.extend(
                name
                for name, present in strict_review_requirements.items()
                if not present
            )
        if strict_missing:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "strict_contract_incomplete",
                    "Lifecycle contract v1 is opted in, but required Slice 2 "
                    "execution-safety fields are incomplete.",
                    contract_loc.source if contract_loc else None,
                    {"missing_fields": sorted(set(strict_missing))},
                )
            )

    return _ReviewGovernanceEvaluation(
        review_state=review_state,
        blockers=blockers,
        human_state=human_state,
        current_artifact=current_artifact,
        current_artifact_current=current_artifact_current,
        timestamps=timestamps,
        strict_missing=strict_missing,
    )


def _classify_execution_mode(
    lifecycle: _LifecycleEvaluation,
    routing: _RoutingEvaluation,
    governance: _ReviewGovernanceEvaluation,
    diagnostics: list[Diagnostic],
) -> _ExecutionClassification:
    task_id = lifecycle.task_id
    task_type = lifecycle.task_type
    current_status = lifecycle.current_status
    previous_status = lifecycle.previous_status
    known_statuses = lifecycle.known_statuses
    strict_opt_in = lifecycle.strict_opt_in
    active_pipeline = routing.active_pipeline
    active_capabilities = routing.active_capabilities
    current_owner = routing.current_owner
    next_action = routing.next_action
    known_roles = routing.known_roles
    review_state = governance.review_state
    human_state = governance.human_state
    current_artifact_current = governance.current_artifact_current
    strict_missing = governance.strict_missing

    basic_unrecoverable = (
        task_id is None
        or current_status is None
        or known_statuses is None
        or (known_statuses is not None and current_status not in known_statuses)
    )
    if basic_unrecoverable:
        compatibility_mode = "unsupported"
    elif current_status in HISTORICAL_STATUSES:
        compatibility_mode = "historical_read_only"
    else:
        has_projection_conflict = any(
            item.code
            in {
                "task_id_conflict",
                "status_conflict",
                "pipeline_conflict",
                "owner_conflict",
            }
            for item in diagnostics
        )
        complete_for_strict = strict_opt_in and not strict_missing and all(
            (
                task_type,
                previous_status,
                active_pipeline,
                active_capabilities,
                current_owner in known_roles,
                next_action,
                current_artifact_current,
                human_state != "unknown",
            )
        ) and not has_projection_conflict
        if current_status in {"review", "approved"}:
            complete_for_strict = complete_for_strict and bool(review_state["outcome"])
        compatibility_mode = "strict" if complete_for_strict else "compatibility"

    if compatibility_mode == "historical_read_only":
        diagnostics.append(
            Diagnostic(
                "info",
                "historical_read_only",
                "Historical task is readable but not executable; schema gaps do "
                "not assess editorial quality.",
            )
        )
    elif compatibility_mode == "compatibility":
        diagnostics.append(
            Diagnostic(
                "info",
                "compatibility_mode",
                "Task is readable through compatibility projection; current "
                "Markdown does not provide every strict execution field.",
            )
        )
    elif compatibility_mode == "unsupported":
        diagnostics.append(
            Diagnostic(
                "info",
                "unsupported_mode",
                "Task state cannot be reconstructed safely for execution.",
            )
        )
    else:
        diagnostics.append(
            Diagnostic("info", "strict_mode", "Task has a complete unambiguous state view.")
        )
    diagnostics.append(
        Diagnostic(
            "info",
            "last_operation_unknown",
            "Last operation is unknown because lifecycle events are outside Slices 0-2.",
        )
    )

    errors = [item for item in diagnostics if item.level == "error"]
    return _ExecutionClassification(
        compatibility_mode=compatibility_mode,
        valid_for_execution=compatibility_mode == "strict" and not errors,
    )


def _assemble_projection(
    lifecycle: _LifecycleEvaluation,
    routing: _RoutingEvaluation,
    governance: _ReviewGovernanceEvaluation,
    classification: _ExecutionClassification,
    diagnostics: list[Diagnostic],
    fingerprints: dict[str, str],
    generated_at: str | None,
) -> dict[str, Any]:
    task = {
        "task_id": lifecycle.task_id,
        "task_type": lifecycle.task_type,
        "current_status": lifecycle.current_status,
        "previous_status": lifecycle.previous_status,
        "current_stage": lifecycle.current_stage,
        "active_pipeline": routing.active_pipeline,
        "active_capabilities": routing.active_capabilities,
        "current_owner": routing.current_owner,
        "next_action": routing.next_action,
        "current_artifact": governance.current_artifact,
        "review_state": governance.review_state,
        "blockers": governance.blockers,
        "human_approval_state": governance.human_state,
        "last_operation": None,
        "timestamps": governance.timestamps,
        "terminal_state": lifecycle.terminal_state,
        "compatibility_mode": classification.compatibility_mode,
    }
    return {
        "projection_version": PROJECTION_VERSION,
        "generated_at": generated_at or utc_now(),
        "source_fingerprints": dict(sorted(fingerprints.items())),
        "valid_for_execution": classification.valid_for_execution,
        "diagnostics": [item.to_dict() for item in diagnostics],
        "task": task,
    }


def _build_task_state_projection(
    task_dir: str | Path,
    *,
    allowed_root: str | Path | None = None,
    generated_at: str | None = None,
    read_inputs: Any,
    revalidate: Any,
) -> dict[str, Any]:
    """Coordinate the established read-only Task State projection stages."""

    diagnostics: list[Diagnostic] = []
    try:
        resolved_task = resolve_task_directory(
            Path(task_dir), Path(allowed_root) if allowed_root else TASKS_ROOT
        )
    except (OSError, ValueError) as exc:
        diagnostics.append(Diagnostic("error", "invalid_task_path", str(exc)))
        return _assemble_invalid_projection(diagnostics, generated_at)

    texts, raw_inputs, initial_presence = read_inputs(resolved_task, diagnostics)
    fingerprints = {
        name: sha256_bytes(data) for name, data in sorted(raw_inputs.items())
    }
    views = _collect_task_views(texts, diagnostics)
    lifecycle = _evaluate_identity_and_lifecycle(views, diagnostics)
    routing = _evaluate_routing_metadata(views, lifecycle, diagnostics)
    governance = _evaluate_review_and_governance(
        resolved_task,
        views,
        lifecycle,
        routing,
        raw_inputs,
        fingerprints,
        diagnostics,
    )
    revalidate(resolved_task, fingerprints, initial_presence, diagnostics)
    classification = _classify_execution_mode(
        lifecycle, routing, governance, diagnostics
    )
    return _assemble_projection(
        lifecycle,
        routing,
        governance,
        classification,
        diagnostics,
        fingerprints,
        generated_at,
    )
