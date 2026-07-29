#!/usr/bin/env bash

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
GENERATOR="$REPO_ROOT/ai-editorial-office/scripts/generate_task_pack.py"
FIXTURES_DIR="$REPO_ROOT/ai-editorial-office/tests/fixtures/task_pack"
OWNER_MARKER="conditional capability owner"
failures=0

run_pack() {
  local fixture_name="$1"
  python3 "$GENERATOR" "$FIXTURES_DIR/$fixture_name" writer 2>&1
}

expect_loaded() {
  local fixture_name="$1"
  local expected_mode="$2"
  local output
  output="$(run_pack "$fixture_name")"
  if ! printf '%s\n' "$output" | grep -q "$OWNER_MARKER"; then
    echo "FAIL: $fixture_name expected Product Intent Review owner loading"
    echo "$output"
    failures=1
    return
  fi
  if ! printf '%s\n' "$output" | grep -q "\`$expected_mode\`"; then
    echo "FAIL: $fixture_name expected mode $expected_mode"
    echo "$output"
    failures=1
    return
  fi
  echo "PASS: $fixture_name loads owner for $expected_mode"
}

expect_not_loaded() {
  local fixture_name="$1"
  local output
  output="$(run_pack "$fixture_name")"
  if printf '%s\n' "$output" | grep -q "$OWNER_MARKER"; then
    echo "FAIL: $fixture_name loaded Product Intent Review owner"
    echo "$output"
    failures=1
    return
  fi
  echo "PASS: $fixture_name preserves compact path"
}

expect_not_loaded "product_intent_not_needed"
expect_not_loaded "writer_minimal"
expect_loaded "product_intent_limited" "limited"
expect_loaded "product_intent_full" "full"
expect_loaded "product_intent_override" "full"

restart_dir="$(mktemp -d)"
trap 'rm -rf "$restart_dir"' EXIT
cp -R "$FIXTURES_DIR/product_intent_limited/." "$restart_dir/"
sed '/Chief Editor Product Intent Review mode decision:/d' \
  "$restart_dir/orchestration_plan.md" > "$restart_dir/orchestration_plan.tmp"
mv "$restart_dir/orchestration_plan.tmp" "$restart_dir/orchestration_plan.md"
restart_output="$(python3 "$GENERATOR" "$restart_dir" writer 2>&1)"
if ! printf '%s\n' "$restart_output" | grep -q "$OWNER_MARKER"; then
  echo "FAIL: manifest-only restart state did not load Product Intent Review owner"
  echo "$restart_output"
  failures=1
else
  echo "PASS: manifest-only restart state preserves limited mode"
fi

if grep -Eq '^\| `(not_needed|limited|full)` \|' \
  "$REPO_ROOT/ai-editorial-office/kb/task_statuses.md"; then
  echo "FAIL: Product Intent Review modes appeared in task statuses"
  failures=1
else
  echo "PASS: Product Intent Review modes are not task statuses"
fi

if [ -e "$REPO_ROOT/ai-editorial-office/pipelines/product_intent_review_pipeline.md" ]; then
  echo "FAIL: Product Intent Review pipeline must not exist"
  failures=1
else
  echo "PASS: no Product Intent Review pipeline exists"
fi

if [ "$failures" -ne 0 ]; then
  echo "Product Intent Review routing smoke test failed."
  exit 1
fi

echo "All Product Intent Review routing smoke tests passed."
