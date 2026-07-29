#!/usr/bin/env python3
"""Validate a task-local Product Intent Review decision/review record.

This checker exists for executable contract tests. It does not activate the
capability, decide a product finding, or create a new review outcome.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


MODES = {"not_needed", "limited", "full"}
OUTCOMES = {"approved", "changes_requested", "blocked"}
CONSEQUENCES = {
    "Proceed",
    "Proceed with constraints",
    "Validate before production",
    "Reroute",
    "Stop / no-build recommendation",
}
MODEL_ELEMENTS = {
    "audience",
    "problem",
    "required_change",
    "proposed_intervention",
    "mechanism",
    "ux",
    "observable_result",
}
PRODUCT_CHECKS = {"value", "fit", "mechanism", "viability"}
VALIDATION_FIELDS = {
    "hypothesis",
    "why_critical",
    "hypothesis_type",
    "audience_context",
    "method",
    "minimum_intervention",
    "observable_signal",
    "signal_kind",
    "continue_condition",
    "reconsider_condition",
    "inference_limits",
    "next_decision",
}
VALIDATION_DISPOSITIONS = {"not_needed", "minimum_test", "insufficient"}
HYPOTHESIS_METHODS = {
    "problem": {
        "interview",
        "observation",
        "existing_data_analysis",
        "work_case_analysis",
        "incident_review",
        "workaround_study",
    },
    "demand": {
        "participation_invitation",
        "registration",
        "alternative_choice",
        "application",
        "access_request",
        "pre_enrollment",
        "observable_commitment",
    },
    "mechanism": {
        "scenario_test",
        "short_exercise",
        "controlled_walkthrough",
        "test_fragment",
        "simulation",
        "key_interaction_prototype",
        "pre_post_decision_comparison",
    },
    "behavior": {
        "task_observation",
        "repeat_task",
        "delayed_check",
        "actual_usage_analysis",
        "work_decision_comparison",
        "limited_field_pilot",
    },
    "usability": {
        "prototype_test",
        "task_based_usability_test",
        "observation",
        "think_aloud",
        "scenario_walkthrough",
    },
    "feasibility": {
        "technical_spike",
        "process_walkthrough",
        "limited_integration",
        "expert_review",
        "dependency_audit",
        "proof_of_concept",
    },
    "viability": {
        "owner_operating_model_check",
        "operating_cost_review",
        "process_impact_review",
        "bounded_viability_review",
    },
}
SIGNAL_KINDS = {
    "real_action",
    "choice",
    "task_completion",
    "decision_quality",
    "repeat_use",
    "skill_transfer",
    "error_reduction",
    "refusal",
    "observed_barrier",
    "process_change",
    "implementation_result",
    "operating_commitment",
    "stated_reaction",
    "stated_intent",
    "perceived_clarity",
    "approval",
}
WEAK_SIGNAL_KINDS = {
    "stated_reaction",
    "stated_intent",
    "perceived_clarity",
    "approval",
}
AI_CONTROL_FIELDS = {
    "data_quality",
    "model_limits",
    "variability",
    "human_control",
    "confidentiality",
    "permitted_data_use",
    "evaluates_work_effect",
}


def _present(value: Any) -> bool:
    return value not in (None, "", [], {})


def evaluate(record: dict[str, Any]) -> tuple[str, list[str]]:
    mode = record.get("mode")
    if mode not in MODES:
        return "blocked", ["mode must be not_needed, limited, or full"]

    review = record.get("review", {})
    if mode == "not_needed":
        issues = []
        if review.get("dimension_present", False):
            issues.append("not_needed must not add Product Intent Review dimension")
        outcome = "changes_requested" if issues else "approved"
        return outcome, issues

    analysis = record.get("analysis", {})
    production = record.get("production", {})
    issues: list[str] = []
    blockers: list[str] = []

    if not _present(record.get("analytical_owner")):
        issues.append("active mode requires an explicitly assigned existing analytical owner")
    if not review.get("dimension_present", False):
        issues.append("active mode requires independent review dimension")
    if not _present(analysis.get("product_finding")):
        issues.append("product finding is missing")
    if analysis.get("product_finding") in OUTCOMES:
        issues.append("product finding is conflated with operational outcome")
    if not _present(analysis.get("evidence_boundary")):
        issues.append("evidence boundary is missing")
    if not _present(analysis.get("main_gap")):
        issues.append("one main product gap is missing")
    if analysis.get("unknowns_hidden", False):
        issues.append("material unknowns are hidden")
    if production.get("consequence") not in CONSEQUENCES:
        issues.append("production consequence is missing or unsupported")
    if not production.get("permission_recorded", False):
        issues.append("production permission is not recorded")
    if not production.get("owner_decision_boundary", False):
        issues.append("product-owner decision boundary is missing")

    if mode == "limited":
        if not _present(record.get("focus")):
            issues.append("limited focus is missing")
        if not analysis.get("focus_checked", False):
            issues.append("limited focus was not checked")
        if analysis.get("scope_overreach", False):
            issues.append("limited analysis overreached into redesign/full audit")
    else:
        model = analysis.get("model", {})
        if set(model) != MODEL_ELEMENTS:
            issues.append("full analysis does not expose the available seven-element model")
        elif any(not _present(value) for value in model.values()):
            issues.append("full model contains an unmarked empty element")
        checks = set(analysis.get("product_checks", []))
        if checks != PRODUCT_CHECKS:
            issues.append("full analysis does not cover all four product checks")
        if not analysis.get("alternatives_bounded", False):
            issues.append("full alternatives are missing or unbounded")

    validation_disposition = analysis.get("validation_disposition")
    if validation_disposition not in VALIDATION_DISPOSITIONS:
        issues.append(
            "validation disposition must be not_needed, minimum_test, or insufficient"
        )
    validation = analysis.get("minimum_validation")
    if validation_disposition == "minimum_test":
        if not isinstance(validation, dict):
            issues.append("required minimum validation is missing")
        else:
            missing = sorted(field for field in VALIDATION_FIELDS if not _present(validation.get(field)))
            if missing:
                issues.append("minimum validation misses: " + ", ".join(missing))
            hypothesis_type = validation.get("hypothesis_type")
            method = validation.get("method")
            if hypothesis_type not in HYPOTHESIS_METHODS:
                issues.append("minimum validation has an unsupported hypothesis type")
            elif method not in HYPOTHESIS_METHODS[hypothesis_type]:
                issues.append("validation method does not fit the primary hypothesis type")
            if validation.get("signal_kind") not in SIGNAL_KINDS:
                issues.append("minimum validation has an unsupported signal kind")
            if not validation.get("main_gap_linked", False):
                issues.append("critical hypothesis is not linked to the main product gap")
            if not validation.get("single_critical_assumption", False):
                issues.append("minimum validation does not isolate one critical assumption")
            if not validation.get("cost_below_full_implementation", False):
                issues.append("minimum validation is not cheaper than full implementation")
            if not validation.get("stoppable", False):
                issues.append("minimum validation cannot be stopped")
            if not validation.get("reversible", False):
                issues.append("minimum validation is not reversible")
            if validation.get("non_hypothesis_features", False):
                issues.append("minimum validation includes features unrelated to the hypothesis")
            if validation.get("full_product_build", False):
                issues.append("minimum validation requires the full product")
            if not validation.get("nearest_test_only", False):
                issues.append("minimum validation does not stop at the nearest decision-relevant check")
            if validation.get("sequential_program_overreach", False):
                issues.append("minimum validation expands into a full research program")
            if validation.get("automatic_survey", False):
                issues.append("survey is used as an automatic validation method")
            if validation.get("automatic_pilot", False):
                issues.append("pilot is recommended automatically")
            if validation.get("automatic_ab_test", False):
                issues.append("A/B test is recommended automatically")
            if validation.get("weak_signal_used_as_proof", False):
                issues.append("weak attitudinal signal is used as proof")
            if (
                validation.get("signal_kind") in WEAK_SIGNAL_KINDS
                and validation.get("hypothesis_type")
                in {"demand", "mechanism", "behavior"}
            ):
                issues.append(
                    "weak attitudinal signal cannot confirm demand, mechanism, or behavior"
                )
            if _present(validation.get("numeric_threshold")) and not _present(
                validation.get("threshold_basis")
            ):
                issues.append("numeric threshold has no evidence basis")
            if validation.get("cannot_answer_core_question", False):
                issues.append(
                    "minimum validation cannot answer the core question; use insufficient"
                )
            if mode == "limited" and not validation.get("limited_focus_fit", False):
                issues.append("minimum validation exceeds the assigned limited focus")
            if validation.get("claims_general_proof", False):
                issues.append("minimum validation overclaims general proof")
            if validation.get("fabricated_metrics", False):
                issues.append("minimum validation invents metrics or false rigor")
            if validation.get("ai_related", False):
                ai_controls = validation.get("ai_controls", {})
                missing_ai = sorted(
                    field
                    for field in AI_CONTROL_FIELDS
                    if not ai_controls.get(field, False)
                )
                if missing_ai:
                    issues.append("AI validation misses: " + ", ".join(missing_ai))
    elif validation_disposition == "not_needed":
        if not _present(analysis.get("validation_not_needed_reason")):
            issues.append("validation not-needed reason is missing")
        if _present(validation):
            issues.append("not_needed must not create a minimum validation")
    elif validation_disposition == "insufficient":
        if not _present(analysis.get("validation_insufficient_reason")):
            issues.append("validation insufficiency reason is missing")
        if not _present(analysis.get("deeper_evidence_route")):
            issues.append("deeper evidence route is missing")
        if not _present(analysis.get("validation_next_owner_decision")):
            issues.append("next owner decision after insufficiency is missing")
        if _present(validation):
            issues.append("insufficient must not present a minimum check as sufficient")

    if production.get("boundary_violation", False):
        issues.append("production violated the approved product boundary")
    if production.get("new_material_gap", False):
        issues.append("production found a new material product gap and requires reroute")
        if not production.get("reroute_to_chief_editor", False):
            issues.append("new material product gap was not rerouted")
        if production.get("writer_redesigned_product", False):
            issues.append("production role redesigned the product instead of rerouting")

    if analysis.get("fabricated_need_or_effect", False):
        blockers.append("analysis fabricates need or effect")
    if analysis.get("owner_substitution", False):
        blockers.append("editorial role substituted for product owner")
    if review.get("independence_failed", False):
        blockers.append("reviewer independence failed")
    if analysis.get("critical_evidence_missing", False):
        blockers.append("critical evidence is missing for deterministic high-risk review")

    if blockers:
        return "blocked", blockers + issues
    if issues:
        return "changes_requested", issues
    return "approved", []


def _matrix_record(case: dict[str, Any]) -> dict[str, Any]:
    """Expand a compact Step 5 matrix case into the existing review record."""

    disposition = case.get("validation_disposition", "minimum_test")
    validation: dict[str, Any] | None = None
    if disposition == "minimum_test":
        validation = {
            "hypothesis": "The critical assumption can be observed in one bounded check.",
            "why_critical": "The next costly step depends on this assumption.",
            "hypothesis_type": "problem",
            "audience_context": "One bounded relevant context.",
            "method": "observation",
            "minimum_intervention": "One bounded, non-production check.",
            "observable_signal": "A real obstacle or action is observed.",
            "signal_kind": "observed_barrier",
            "continue_condition": "The expected signal appears without unsupported prompting.",
            "reconsider_condition": "The signal is absent, ambiguous, or caused by another constraint.",
            "inference_limits": "The check does not prove general success, scale, or persistence.",
            "next_decision": "The product owner decides whether the next bounded step is justified.",
            "main_gap_linked": True,
            "single_critical_assumption": True,
            "cost_below_full_implementation": True,
            "stoppable": True,
            "reversible": True,
            "non_hypothesis_features": False,
            "full_product_build": False,
            "nearest_test_only": True,
            "sequential_program_overreach": False,
            "automatic_survey": False,
            "automatic_pilot": False,
            "automatic_ab_test": False,
            "weak_signal_used_as_proof": False,
            "limited_focus_fit": True,
            "claims_general_proof": False,
            "fabricated_metrics": False,
        }
        validation.update(case.get("validation", {}))

    analysis: dict[str, Any] = {
        "product_finding": case.get(
            "product_finding",
            "Resolve the critical uncertainty before a larger investment.",
        ),
        "evidence_boundary": case.get(
            "evidence_boundary",
            "The fixture covers validation-design behavior, not product success.",
        ),
        "main_gap": case.get("main_gap", "The critical assumption remains untested."),
        "unknowns_hidden": False,
        "focus_checked": True,
        "scope_overreach": False,
        "validation_disposition": disposition,
    }
    if validation is not None:
        analysis["minimum_validation"] = validation
    if disposition == "not_needed":
        analysis["validation_not_needed_reason"] = case.get(
            "validation_not_needed_reason"
        )
    if disposition == "insufficient":
        analysis["validation_insufficient_reason"] = case.get(
            "validation_insufficient_reason"
        )
        analysis["deeper_evidence_route"] = case.get("deeper_evidence_route")
        analysis["validation_next_owner_decision"] = case.get(
            "validation_next_owner_decision"
        )

    return {
        "mode": "limited",
        "analytical_owner": "research_agent",
        "focus": case.get("focus", "the one main product gap"),
        "analysis": analysis,
        "production": {
            "consequence": case.get(
                "consequence",
                "Proceed"
                if disposition == "not_needed"
                else "Reroute"
                if disposition == "insufficient"
                else "Validate before production",
            ),
            "permission_recorded": True,
            "owner_decision_boundary": True,
            "boundary_violation": False,
        },
        "review": {
            "dimension_present": True,
            "outcome": case.get("expected_outcome"),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--expect", choices=sorted(OUTCOMES))
    args = parser.parse_args()

    data = json.loads(args.record.read_text(encoding="utf-8"))
    records = data if isinstance(data, list) else [data]
    failed = False
    for index, source_record in enumerate(records, start=1):
        if not isinstance(source_record, dict):
            print(f"error: record {index} is not an object")
            failed = True
            continue
        record = (
            _matrix_record(source_record)
            if source_record.get("matrix_case", False)
            else source_record
        )
        outcome, findings = evaluate(record)
        name = source_record.get("name", args.record.stem)
        print(f"{name}: {outcome}")
        for finding in findings:
            print(f"- {finding}")

        recorded = record.get("review", {}).get("outcome")
        if recorded not in OUTCOMES:
            print(
                "error: recorded operational outcome must be approved, "
                "changes_requested, or blocked"
            )
            failed = True
        elif recorded != outcome:
            print(
                f"error: recorded outcome {recorded} does not match "
                f"evaluated outcome {outcome}"
            )
            failed = True
        if args.expect and args.expect != outcome:
            print(f"error: expected {args.expect}, got {outcome}")
            failed = True
    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
