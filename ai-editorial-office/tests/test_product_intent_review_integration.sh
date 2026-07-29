#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
OFFICE="$ROOT_DIR/ai-editorial-office"

assert_contains() {
  file=$1
  pattern=$2
  message=$3
  if ! grep -Fq -- "$pattern" "$file"; then
    printf 'FAIL %s\n' "$message" >&2
    exit 1
  fi
}

assert_contains "$OFFICE/kb/product_intent_review.md" 'Proceed with constraints' 'canonical consequence contract missing'
assert_contains "$OFFICE/kb/product_intent_review.md" 'Stop / no-build recommendation' 'canonical no-build consequence missing'
assert_contains "$OFFICE/kb/product_intent_review.md" '## Minimum Product Validation' 'Step 5 canonical contract missing'
assert_contains "$OFFICE/kb/product_intent_review.md" '`minimum_test`' 'validation disposition contract missing'
assert_contains "$OFFICE/kb/product_intent_review.md" '| Problem |' 'problem hypothesis class missing'
assert_contains "$OFFICE/kb/product_intent_review.md" '| Demand |' 'demand hypothesis class missing'
assert_contains "$OFFICE/kb/product_intent_review.md" 'Do not produce a complete discovery or research program' 'nearest-check boundary missing'
assert_contains "$OFFICE/agents/research_agent.md" 'keep `limited` research confined' 'limited research boundary missing'
assert_contains "$OFFICE/agents/research_agent.md" 'explicitly assigns Research Agent as the task-local' 'analytical owner assignment missing'
assert_contains "$OFFICE/agents/research_agent.md" 'distinguish its problem/demand/mechanism/behavior/' 'Research validation method fit missing'
assert_contains "$OFFICE/agents/writer_agent.md" 'return to Chief Editor rather than redesigning the product' 'Writer reroute missing'
assert_contains "$OFFICE/agents/writer_agent.md" 'create only the minimum intervention' 'Writer minimum-artifact boundary missing'
assert_contains "$OFFICE/agents/ux_writer.md" 'return to Chief Editor rather than redesigning the flow' 'UX Writer reroute missing'
assert_contains "$OFFICE/agents/review_agent.md" 'A product finding may be negative' 'negative finding review rule missing'
assert_contains "$OFFICE/agents/review_agent.md" 'accept observable qualitative decision conditions' 'qualitative threshold review rule missing'
assert_contains "$OFFICE/agents/final_editor.md" 'including a negative or no-build recommendation' 'Final Editor preservation missing'
assert_contains "$OFFICE/agents/final_editor.md" 'preserve approved validation criticality' 'Final Editor validation preservation missing'
assert_contains "$OFFICE/pipelines/research_pipeline.md" 'not a Product Intent Review pipeline' 'research pipeline boundary missing'
assert_contains "$OFFICE/pipelines/review_pipeline.md" 'No Product Intent Review verdict' 'review outcome separation missing'
assert_contains "$OFFICE/templates/tasks/review_task_template.md" 'Finding/verdict separation: pass/fail' 'review trace field missing'
assert_contains "$OFFICE/templates/artifacts/orchestration_plan_template.md" 'Product-owner decision required:' 'decision frame owner boundary missing'

for forbidden in \
  "$OFFICE/agents/product_reviewer.md" \
  "$OFFICE/agents/product_analyst.md" \
  "$OFFICE/agents/product_strategist.md" \
  "$OFFICE/agents/product_researcher.md" \
  "$OFFICE/pipelines/minimum_product_validation_pipeline.md" \
  "$OFFICE/pipelines/validation_pipeline.md" \
  "$OFFICE/pipelines/product_intent_review_pipeline.md"
do
  if [ -e "$forbidden" ]; then
    printf 'FAIL forbidden surface exists: %s\n' "$forbidden" >&2
    exit 1
  fi
done

sh "$OFFICE/tests/test_product_intent_review_decision_review.sh"

printf '%s\n' 'Product Intent Review Step 3 integration contract passed.'
