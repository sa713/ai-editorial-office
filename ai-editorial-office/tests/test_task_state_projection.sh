#!/usr/bin/env bash

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
export REPO_ROOT

python3 - <<'PY'
from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

repo = Path(os.environ["REPO_ROOT"])
scripts = repo / "ai-editorial-office" / "scripts"
fixtures = repo / "ai-editorial-office" / "tests" / "fixtures" / "task_state_projection"
sys.path.insert(0, str(scripts))

import task_state  # noqa: E402

build_task_state = task_state.build_task_state


failures: list[str] = []


def project(name: str):
    return build_task_state(fixtures / name, allowed_root=fixtures)


def codes(result, level=None):
    return {
        item["code"]
        for item in result["diagnostics"]
        if level is None or item["level"] == level
    }


def check(name: str, condition: bool, detail: str = ""):
    if condition:
        print(f"PASS: {name}")
    else:
        failures.append(name)
        print(f"FAIL: {name} {detail}".rstrip())


valid = project("valid_current")
check(
    "valid current task",
    not codes(valid, "error")
    and valid["task"]["task_id"] == "PROJECTION-VALID-CURRENT"
    and valid["task"]["current_stage"] == "drafting"
    and valid["task"]["compatibility_mode"] == "strict"
    and valid["valid_for_execution"],
)

unmarked = project("unmarked_current")
check(
    "unmarked current task is compatibility non-executable",
    not codes(unmarked, "error")
    and unmarked["task"]["compatibility_mode"] == "compatibility"
    and not unmarked["valid_for_execution"],
)

conflict = project("manifest_status_conflict")
conflict_diag = next(
    (item for item in conflict["diagnostics"] if item["code"] == "status_conflict"),
    None,
)
check(
    "manifest/status conflict",
    conflict_diag is not None
    and conflict_diag["level"] == "error"
    and len(conflict_diag["details"].get("values", [])) == 2
    and not conflict["valid_for_execution"],
)

unknown = project("unknown_status")
check(
    "unknown status",
    "unknown_status" in codes(unknown, "error")
    and unknown["task"]["compatibility_mode"] == "unsupported",
)

transition = project("invalid_transition")
check("invalid previous-to-current transition", "invalid_transition" in codes(transition, "error"))

compat = project("compat_missing_optional")
check(
    "missing optional field compatibility",
    compat["task"]["compatibility_mode"] == "compatibility"
    and "previous_status_missing" in codes(compat, "warning"),
)

historical = project("historical_read_only")
check(
    "historical read-only task",
    historical["task"]["compatibility_mode"] == "historical_read_only"
    and not historical["valid_for_execution"]
    and "historical_read_only" in codes(historical, "info"),
)

unsupported = project("unsupported")
check(
    "unsupported unrecoverable task",
    unsupported["task"]["compatibility_mode"] == "unsupported"
    and not unsupported["valid_for_execution"],
)

pipeline = project("pipeline_reference_missing")
check("pipeline reference missing", "pipeline_unknown" in codes(pipeline, "error"))

owner = project("unknown_owner")
check("unknown role owner", "owner_unknown" in codes(owner, "error"))

check(
    "missing review for non-final task",
    valid["task"]["review_state"]["present"] is False
    and "status_requires_approved_review" not in codes(valid, "error"),
)

final_no_review = project("final_without_review")
check(
    "approved task without Review Gate evidence",
    "status_requires_approved_review" in codes(final_no_review, "error"),
)

self_review = project("self_review")
check("explicit self-review", "review_self_approval" in codes(self_review, "error"))

stale = project("stale_review")
check("stale review evidence", "stale_review_evidence" in codes(stale, "error"))

approval = project("approval_without_evidence")
check(
    "human approval assertion without evidence",
    "approval_without_evidence" in codes(approval, "error")
    and "finalized_without_human_approval_evidence" in codes(approval, "warning"),
)

approved_blocker = project("approved_with_blocker")
check(
    "approved task with active blocker is rejected",
    "approved_with_active_blocker" in codes(approved_blocker, "error")
    and not approved_blocker["valid_for_execution"],
)

blocked_without_evidence = project("blocked_without_blocker")
check(
    "blocked task requires blocker evidence",
    "blocked_without_blocker_evidence"
    in codes(blocked_without_evidence, "error"),
)

strict_terminal = project("strict_finalized_missing")
check(
    "strict finalized task requires final and review evidence",
    "finalized_without_final_artifact" in codes(strict_terminal, "error")
    and "finalized_review_not_machine_verifiable"
    in codes(strict_terminal, "error")
    and not strict_terminal["valid_for_execution"],
)

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    allowed = tmp_path / "tasks"
    task = allowed / "strict-approved-incomplete"
    shutil.copytree(fixtures / "approved_with_blocker", task)
    manifest_path = task / "task-manifest.md"
    manifest_path.write_text(
        manifest_path.read_text(encoding="utf-8").replace(
            "- Task type:", "- Lifecycle contract version: 1\n- Task type:"
        ),
        encoding="utf-8",
    )
    status_path = task / "status.md"
    status_path.write_text(
        status_path.read_text(encoding="utf-8").replace(
            "- Unresolved security defect.", "- None."
        ),
        encoding="utf-8",
    )
    strict_incomplete = build_task_state(task, allowed_root=allowed)
    strict_diag = next(
        (
            item
            for item in strict_incomplete["diagnostics"]
            if item["code"] == "strict_contract_incomplete"
        ),
        None,
    )
    missing_fields = set(
        strict_diag["details"].get("missing_fields", []) if strict_diag else []
    )
    check(
        "strict approved task requires normalized independence and fingerprint",
        strict_diag is not None
        and {
            "review_state.reviewer_identity",
            "review_state.producer_identity",
            "review_state.independence_confirmed",
            "review_state.current_fingerprint",
        }.issubset(missing_fields)
        and not strict_incomplete["valid_for_execution"],
    )

wrong_reviewer = project("strict_wrong_reviewer")
wrong_reviewer_diag = next(
    (
        item
        for item in wrong_reviewer["diagnostics"]
        if item["code"] == "strict_contract_incomplete"
    ),
    None,
)
check(
    "strict approved task rejects known wrong reviewer role",
    wrong_reviewer_diag is not None
    and "review_state.reviewer_role"
    in wrong_reviewer_diag["details"].get("missing_fields", [])
    and not wrong_reviewer["valid_for_execution"],
)

unknown_reviewer = project("strict_unknown_reviewer")
unknown_reviewer_diag = next(
    (
        item
        for item in unknown_reviewer["diagnostics"]
        if item["code"] == "strict_contract_incomplete"
    ),
    None,
)
check(
    "strict approved task rejects unknown reviewer role",
    unknown_reviewer_diag is not None
    and "review_state.reviewer_role"
    in unknown_reviewer_diag["details"].get("missing_fields", [])
    and not unknown_reviewer["valid_for_execution"],
)

traversal = build_task_state(
    fixtures / ".." / "task_state_projection" / "valid_current",
    allowed_root=fixtures,
)
check("path traversal rejection", "invalid_task_path" in codes(traversal, "error"))

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    allowed = tmp_path / "tasks"
    task = allowed / "external-symlink"
    shutil.copytree(fixtures / "valid_current", task)
    outside = tmp_path / "outside-status.md"
    outside.write_text("# Status\n\nStatus: writing\n", encoding="utf-8")
    (task / "status.md").unlink()
    (task / "status.md").symlink_to(outside)
    symlink_result = build_task_state(task, allowed_root=allowed)
    check(
        "external symlink rejection",
        "external_symlink" in codes(symlink_result, "error"),
    )

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    allowed = tmp_path / "tasks"
    task = allowed / "changed-source"
    shutil.copytree(fixtures / "valid_current", task)

    original_read = task_state.read_initial_inputs

    def read_then_mutate(root: Path, diagnostics):
        result = original_read(root, diagnostics)
        path = root / "status.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        return result

    task_state.read_initial_inputs = read_then_mutate
    try:
        changed = build_task_state(task, allowed_root=allowed)
    finally:
        task_state.read_initial_inputs = original_read
    check(
        "source input changed during parse",
        "source_changed_during_parse" in codes(changed, "error")
        and not changed["valid_for_execution"],
    )

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    allowed = tmp_path / "tasks"
    task = allowed / "changed-dynamic-source"
    shutil.copytree(fixtures / "stale_review", task)
    draft_path = task / "draft.md"
    review_path = task / "review.md"
    current_sha = hashlib.sha256(draft_path.read_bytes()).hexdigest()
    review_path.write_text(
        review_path.read_text(encoding="utf-8").replace("0" * 64, current_sha),
        encoding="utf-8",
    )

    original_revalidate = task_state.revalidate_inputs

    def mutate_then_revalidate(root, fingerprints, initial_presence, diagnostics):
        path = root / "draft.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\nchanged after first read\n",
            encoding="utf-8",
        )
        return original_revalidate(root, fingerprints, initial_presence, diagnostics)

    task_state.revalidate_inputs = mutate_then_revalidate
    try:
        dynamic_changed = build_task_state(task, allowed_root=allowed)
    finally:
        task_state.revalidate_inputs = original_revalidate
    check(
        "dynamic reviewed artifact changed during parse",
        "source_changed_during_parse" in codes(dynamic_changed, "error")
        and not dynamic_changed["valid_for_execution"],
    )

first = project("valid_current")
second = project("valid_current")
first_without_time = copy.deepcopy(first)
second_without_time = copy.deepcopy(second)
first_without_time.pop("generated_at", None)
second_without_time.pop("generated_at", None)
check(
    "deterministic JSON excluding generated_at",
    json.dumps(first_without_time, sort_keys=True)
    == json.dumps(second_without_time, sort_keys=True),
)


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file() and not item.is_symlink()):
        rel = path.relative_to(root).as_posix().encode()
        data = path.read_bytes()
        digest.update(rel)
        digest.update(data)
    return digest.hexdigest()


before = tree_hash(fixtures / "valid_current")
_ = project("valid_current")
after = tree_hash(fixtures / "valid_current")
check("parser does not modify files", before == after)

check(
    "unknown historical values are not zero",
    historical["task"]["last_operation"] is None
    and historical["task"]["timestamps"]["created"] is None
    and "operation_attempts" not in historical["task"],
)

check(
    "task without new structured blocks remains readable",
    compat["task"]["task_id"] == "PROJECTION-COMPAT"
    and compat["task"]["compatibility_mode"] == "compatibility",
)

check(
    "projection envelope",
    valid["projection_version"] == 1
    and isinstance(valid["source_fingerprints"], dict)
    and isinstance(valid["diagnostics"], list)
    and isinstance(valid["task"], dict),
)

if failures:
    print(f"Task State projection tests failed: {len(failures)}.")
    sys.exit(1)
print("All task state projection tests passed.")
PY
