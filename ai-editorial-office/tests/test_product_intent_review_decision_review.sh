#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
CHECKER="$ROOT_DIR/ai-editorial-office/scripts/check_product_intent_review.py"
FIXTURES="$ROOT_DIR/ai-editorial-office/tests/fixtures/product_intent_review"

run_case() {
  case_name=$1
  expected=$2
  python3 "$CHECKER" "$FIXTURES/$case_name.json" --expect "$expected" >/dev/null
  printf 'PASS %s -> %s\n' "$case_name" "$expected"
}

run_case negative_no_build_approved approved
run_case polished_boundary_violation changes_requested
run_case limited_overreach changes_requested
run_case full_incomplete_model changes_requested
run_case product_owner_substitution blocked
run_case weak_minimum_validation changes_requested
run_case correct_minimum_validation approved
run_case bad_analysis_blocked blocked
run_case not_needed_regression approved
run_case production_reroute changes_requested

python3 "$CHECKER" "$FIXTURES/minimum_product_validation_cases.json"

printf '%s\n' 'All Product Intent Review decision/review scenarios passed.'
