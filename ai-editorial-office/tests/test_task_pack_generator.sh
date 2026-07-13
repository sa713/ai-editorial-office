#!/usr/bin/env bash

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
GENERATOR="$REPO_ROOT/ai-editorial-office/scripts/generate_task_pack.py"
FIXTURES_DIR="$REPO_ROOT/ai-editorial-office/tests/fixtures/task_pack"

failures=0

run_case() {
  local fixture_name="$1"
  local role="$2"
  local expected_exit="$3"
  shift 3
  local output
  local exit_code
  local expected_text

  output="$(python3 "$GENERATOR" "$FIXTURES_DIR/$fixture_name" "$role" 2>&1)"
  exit_code=$?

  if [ "$exit_code" -ne "$expected_exit" ]; then
    echo "FAIL: $fixture_name/$role expected exit $expected_exit, got $exit_code"
    echo "$output"
    failures=1
    return
  fi

  for expected_text in "$@"; do
    if ! printf '%s\n' "$output" | grep -q "$expected_text"; then
      echo "FAIL: $fixture_name/$role expected output to contain: $expected_text"
      echo "$output"
      failures=1
      return
    fi
  done

  echo "PASS: $fixture_name/$role"
}

run_case_absent() {
  local fixture_name="$1"
  local role="$2"
  local expected_exit="$3"
  shift 3
  local output
  local exit_code
  local unexpected_text

  output="$(python3 "$GENERATOR" "$FIXTURES_DIR/$fixture_name" "$role" 2>&1)"
  exit_code=$?

  if [ "$exit_code" -ne "$expected_exit" ]; then
    echo "FAIL: $fixture_name/$role expected exit $expected_exit, got $exit_code"
    echo "$output"
    failures=1
    return
  fi

  for unexpected_text in "$@"; do
    if printf '%s\n' "$output" | grep -q "$unexpected_text"; then
      echo "FAIL: $fixture_name/$role expected output not to contain: $unexpected_text"
      echo "$output"
      failures=1
      return
    fi
  done

  echo "PASS: $fixture_name/$role absent checks"
}

run_case "writer_minimal" "writer" 0 "draft.md" "article_pipeline.md"
run_case "review_with_claims" "review_agent" 0 "claims-used.md" "facts.md" "sources.md"
run_case "final_editor_missing_review" "final_editor" 1 "review.md is missing"
run_case "chief_editor_feedback" "chief_editor" 0 "feedback.md" "feedback_loop.md"
run_case "source_summary_compact_evidence" "writer" 0 "source_summary.md" "task-local evidence summary"
run_case "source_summary_compact_evidence" "review_agent" 0 "source_summary.md" "task-local evidence summary"
run_case_absent "writer_minimal" "writer" 0 "source_summary.md" "source_notes.md"
run_case "client_profile_pending" "writer" 0 "client-profile files were not included"
run_case_absent "client_profile_pending" "writer" 0 "explicit active client-profile file"
run_case "reader_outcome_material" "writer" 0 "audience_outcome_alignment.md" "professional_communication.md" "editorial_quality_attributes.md"
run_case "reader_outcome_material" "review_agent" 0 "audience_outcome_alignment.md" "professional_communication.md" "editorial_quality_attributes.md"
run_case_absent "writer_minimal" "writer" 0 "audience_outcome_alignment.md" "professional_communication.md" "editorial_quality_attributes.md"
run_case "runtime_execution_record" "writer" 0 "planned runtime topology" "actual runtime execution record"

if [ "$failures" -ne 0 ]; then
  echo "Task pack generator smoke test failed."
  exit 1
fi

echo "All task pack generator smoke tests passed."
