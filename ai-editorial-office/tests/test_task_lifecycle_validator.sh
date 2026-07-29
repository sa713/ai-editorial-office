#!/usr/bin/env bash

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
VALIDATOR="$REPO_ROOT/ai-editorial-office/scripts/validate_task_lifecycle.py"
FIXTURES_DIR="$REPO_ROOT/ai-editorial-office/tests/fixtures/task_lifecycle"
PROJECTION_FIXTURES="$REPO_ROOT/ai-editorial-office/tests/fixtures/task_state_projection"
export VALIDATOR FIXTURES_DIR PROJECTION_FIXTURES

failures=0

run_case() {
  local fixture_name="$1"
  local expected_exit="$2"
  local expected_result="$3"
  local expected_text="${4:-}"
  local output
  local exit_code

  output="$(python3 "$VALIDATOR" "$FIXTURES_DIR/$fixture_name" 2>&1)"
  exit_code=$?

  if [ "$exit_code" -ne "$expected_exit" ]; then
    echo "FAIL: $fixture_name expected exit $expected_exit, got $exit_code"
    echo "$output"
    failures=1
    return
  fi

  if ! printf '%s\n' "$output" | grep -q "Result: $expected_result"; then
    echo "FAIL: $fixture_name expected Result: $expected_result"
    echo "$output"
    failures=1
    return
  fi

  if [ -n "$expected_text" ] && ! printf '%s\n' "$output" | grep -q "$expected_text"; then
    echo "FAIL: $fixture_name expected output to contain: $expected_text"
    echo "$output"
    failures=1
    return
  fi

  echo "PASS: $fixture_name"
}

run_case "valid_minimal" 0 "PASS"
run_case "valid_with_pipeline" 0 "PASS"
run_case "invalid_missing_manifest" 1 "FAIL"
run_case "invalid_final_without_review" 1 "FAIL"
run_case "invalid_final_with_changes_requested" 1 "FAIL"
run_case "invalid_final_with_ambiguous_review" 1 "FAIL"
run_case "invalid_status_mismatch" 1 "FAIL"
run_case "invalid_unknown_pipeline" 1 "FAIL"
run_case "warning_missing_pipeline" 0 "PASS" "Selected pipeline was not found"
run_case "valid_transition_writing_to_review" 0 "PASS"
run_case "invalid_transition_writing_to_finalized" 1 "FAIL" "Invalid status transition"
run_case "warning_missing_previous_status" 0 "PASS" "previous status"
run_case "warning_same_previous_current_status" 0 "PASS" "same"
run_case "invalid_blocked_to_finalized" 1 "FAIL" "Blocked task must not move directly to finalized"

python3 - <<'PY'
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

validator = Path(os.environ["VALIDATOR"])
fixtures = Path(os.environ["PROJECTION_FIXTURES"])
failures: list[str] = []


def invoke(name: str, output_format: str = "json"):
    return subprocess.run(
        [
            sys.executable,
            str(validator),
            str(fixtures / name),
            "--format",
            output_format,
        ],
        text=True,
        capture_output=True,
    )


def data(name: str):
    result = invoke(name)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {}
    return result, payload


def codes(payload, level):
    return {item["code"] for item in payload.get(level, [])}


def check(name: str, condition: bool):
    if condition:
        print(f"PASS: validator {name}")
    else:
        failures.append(name)
        print(f"FAIL: validator {name}")


active_conflict, active_conflict_json = data("manifest_status_conflict")
check(
    "active manifest/status conflict is error",
    active_conflict.returncode == 1
    and "status_conflict" in codes(active_conflict_json, "errors"),
)

historical, historical_json = data("historical_read_only")
historical_text = invoke("historical_read_only", "text")
check(
    "historical schema gap is warning/info",
    historical.returncode == 0
    and historical_json.get("projection", {}).get("task", {}).get("compatibility_mode")
    == "historical_read_only"
    and historical_json.get("warnings")
    and historical_json.get("info"),
)
check(
    "historical task is not labeled failed",
    "task failed" not in historical_text.stdout.lower(),
)

unknown, unknown_json = data("unknown_status")
check(
    "invalid status is error",
    unknown.returncode == 1 and "unknown_status" in codes(unknown_json, "errors"),
)

transition, transition_json = data("invalid_transition")
check(
    "invalid transition is error",
    transition.returncode == 1
    and "invalid_transition" in codes(transition_json, "errors"),
)

valid, valid_json = data("valid_current")
check(
    "missing review before review stage is allowed",
    valid.returncode == 0
    and "status_requires_approved_review" not in codes(valid_json, "errors"),
)

unmarked, unmarked_json = data("unmarked_current")
check(
    "unmarked current task is compatibility non-executable",
    unmarked.returncode == 0
    and unmarked_json["projection"]["task"]["compatibility_mode"] == "compatibility"
    and not unmarked_json["projection"]["valid_for_execution"],
)

final_no_review, final_no_review_json = data("final_without_review")
check(
    "finalization without approved review is blocked",
    final_no_review.returncode == 1
    and "status_requires_approved_review"
    in codes(final_no_review_json, "errors"),
)

self_review, self_review_json = data("self_review")
check(
    "explicit self-review blocks finalization",
    self_review.returncode == 1
    and "review_self_approval" in codes(self_review_json, "errors"),
)

stale, stale_json = data("stale_review")
check(
    "provably stale review blocks finalization",
    stale.returncode == 1
    and "stale_review_evidence" in codes(stale_json, "errors"),
)

approval, approval_json = data("approval_without_evidence")
check(
    "human approval assertion requires evidence",
    approval.returncode == 1
    and "approval_without_evidence" in codes(approval_json, "errors"),
)

approved_blocker, approved_blocker_json = data("approved_with_blocker")
check(
    "approved task with active blocker is blocked",
    approved_blocker.returncode == 1
    and "approved_with_active_blocker"
    in codes(approved_blocker_json, "errors"),
)

blocked_no_evidence, blocked_no_evidence_json = data("blocked_without_blocker")
check(
    "blocked task without blocker evidence is invalid",
    blocked_no_evidence.returncode == 1
    and "blocked_without_blocker_evidence"
    in codes(blocked_no_evidence_json, "errors"),
)

strict_terminal, strict_terminal_json = data("strict_finalized_missing")
check(
    "strict finalized task requires final and review evidence",
    strict_terminal.returncode == 1
    and "finalized_without_final_artifact"
    in codes(strict_terminal_json, "errors")
    and "finalized_review_not_machine_verifiable"
    in codes(strict_terminal_json, "errors"),
)

wrong_reviewer, wrong_reviewer_json = data("strict_wrong_reviewer")
check(
    "strict approved task rejects known wrong reviewer role",
    wrong_reviewer.returncode == 1
    and "strict_contract_incomplete" in codes(wrong_reviewer_json, "errors")
    and "review_state.reviewer_role"
    in next(
        item
        for item in wrong_reviewer_json["errors"]
        if item["code"] == "strict_contract_incomplete"
    )["details"]["missing_fields"],
)

unknown_reviewer, unknown_reviewer_json = data("strict_unknown_reviewer")
check(
    "strict approved task rejects unknown reviewer role",
    unknown_reviewer.returncode == 1
    and "strict_contract_incomplete" in codes(unknown_reviewer_json, "errors")
    and "review_state.reviewer_role"
    in next(
        item
        for item in unknown_reviewer_json["errors"]
        if item["code"] == "strict_contract_incomplete"
    )["details"]["missing_fields"],
)

check(
    "compatibility does not hide contradiction",
    active_conflict_json.get("projection", {}).get("task", {}).get(
        "compatibility_mode"
    )
    in {"compatibility", "unsupported"}
    and active_conflict_json.get("errors"),
)

check(
    "unknown telemetry is not zero",
    historical_json["projection"]["task"]["last_operation"] is None
    and "operation_attempts" not in historical_json["projection"]["task"],
)

text = invoke("valid_current", "text")
blockers = int(re.search(r"Blockers: (\d+)", text.stdout).group(1))
warnings = int(re.search(r"Warnings: (\d+)", text.stdout).group(1))
info = int(re.search(r"Info: (\d+)", text.stdout).group(1))
all_messages = [
    item["message"]
    for key in ("errors", "warnings", "info")
    for item in valid_json[key]
]
check(
    "text and JSON diagnostics agree",
    blockers == len(valid_json["errors"])
    and warnings == len(valid_json["warnings"])
    and info == len(valid_json["info"])
    and all(message in text.stdout for message in all_messages),
)

check(
    "JSON schema is stable",
    valid_json.get("schema_version") == 1
    and set(valid_json)
    == {
        "schema_version",
        "task_dir",
        "result",
        "errors",
        "warnings",
        "info",
        "projection",
    },
)


def tree_hash(root: Path):
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


before = tree_hash(fixtures / "valid_current")
_ = invoke("valid_current", "json")
after = tree_hash(fixtures / "valid_current")
check("validator is read-only", before == after)

source = validator.read_text(encoding="utf-8")
check(
    "TaskStateProjection is sole normalization layer",
    "from task_state import" in source
    and "re.compile" not in source
    and "def normalize_value" not in source
    and "def extract_current_status" not in source,
)

if failures:
    sys.exit(1)
PY
projection_checks=$?
if [ "$projection_checks" -ne 0 ]; then
  failures=1
fi

if [ "$failures" -ne 0 ]; then
  echo "Task lifecycle validator smoke test failed."
  exit 1
fi

echo "All task lifecycle validator smoke tests passed."
