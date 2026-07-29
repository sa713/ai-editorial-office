#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
RUNNER="$ROOT_DIR/ai-editorial-office/tests/run_product_intent_evaluation.py"
SUITE="$ROOT_DIR/ai-editorial-office/tests/fixtures/product_intent_evaluation/cases.json"

output=$(python3 "$RUNNER" "$SUITE")
printf '%s\n' "$output"

for expected in \
  'Result: PASS' \
  'coverage.cases: 32' \
  'coverage.task_classes: 8' \
  'coverage.pairs: 8' \
  'coverage.adversarial: 12' \
  'metric.routing_accuracy: 1.0' \
  'metric.critical_contract_violations: 0' \
  'metric.confirmed_production_defects: 0' \
  'metric.repair_loops: 0'
do
  if ! printf '%s\n' "$output" | grep -Fq "$expected"; then
    printf 'FAIL missing evaluation output: %s\n' "$expected" >&2
    exit 1
  fi
done

tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT

python3 -c '
import json, sys
src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
data["cases"][1]["case_id"] = data["cases"][0]["case_id"]
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
' "$SUITE" "$tmp_dir/duplicate.json"
if python3 "$RUNNER" "$tmp_dir/duplicate.json" >/dev/null 2>&1; then
  printf '%s\n' 'FAIL duplicate Case ID was accepted' >&2
  exit 1
fi

python3 -c '
import json, sys
src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
del data["cases"][0]["hidden_structure"]
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
' "$SUITE" "$tmp_dir/missing-metadata.json"
if python3 "$RUNNER" "$tmp_dir/missing-metadata.json" >/dev/null 2>&1; then
  printf '%s\n' 'FAIL missing case metadata was accepted' >&2
  exit 1
fi

python3 -c '
import json, sys
src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
data["cases"] = data["cases"][:8]
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
' "$SUITE" "$tmp_dir/coverage-gap.json"
if python3 "$RUNNER" "$tmp_dir/coverage-gap.json" >/dev/null 2>&1; then
  printf '%s\n' 'FAIL coverage gap was accepted' >&2
  exit 1
fi

python3 -c '
import json, sys
src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
data["cases"][0]["observed"]["errors"] = ["product_owner_substitution"]
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
' "$SUITE" "$tmp_dir/critical-violation.json"
if python3 "$RUNNER" "$tmp_dir/critical-violation.json" >/dev/null 2>&1; then
  printf '%s\n' 'FAIL critical contract violation was accepted' >&2
  exit 1
fi

python3 "$RUNNER" "$SUITE" --format json >/dev/null

printf '%s\n' 'Product Intent Review Step 6 evaluation runner tests passed.'
