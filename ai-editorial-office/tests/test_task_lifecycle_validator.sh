#!/usr/bin/env bash

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
VALIDATOR="$REPO_ROOT/ai-editorial-office/scripts/validate_task_lifecycle.py"
FIXTURES_DIR="$REPO_ROOT/ai-editorial-office/tests/fixtures/task_lifecycle"

failures=0

run_case() {
  local fixture_name="$1"
  local expected_exit="$2"
  local expected_result="$3"
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

  echo "PASS: $fixture_name"
}

run_case "valid_minimal" 0 "PASS"
run_case "invalid_missing_manifest" 1 "FAIL"
run_case "invalid_final_without_review" 1 "FAIL"
run_case "invalid_final_with_changes_requested" 1 "FAIL"
run_case "invalid_final_with_ambiguous_review" 1 "FAIL"

if [ "$failures" -ne 0 ]; then
  echo "Task lifecycle validator smoke test failed."
  exit 1
fi

echo "All task lifecycle validator smoke tests passed."
