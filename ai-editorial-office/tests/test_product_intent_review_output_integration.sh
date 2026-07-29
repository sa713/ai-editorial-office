#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
OFFICE="$ROOT_DIR/ai-editorial-office"

require_text() {
  file=$1
  text=$2
  message=$3
  if ! grep -Fq -- "$text" "$file"; then
    printf 'FAIL %s\n' "$message" >&2
    exit 1
  fi
}

require_text "$OFFICE/kb/product_intent_review.md" '### Reader-Facing Result' 'canonical output contract missing'
require_text "$OFFICE/kb/product_intent_review.md" 'Source length must not mechanically determine result length.' 'source-size boundary missing'
require_text "$OFFICE/kb/deliverables/report.md" 'When Product Intent Review is active' 'report adaptation missing'
require_text "$OFFICE/kb/deliverables/research-report.md" 'When Product Intent Review is active' 'research-report adaptation missing'
require_text "$OFFICE/kb/deliverables/decision-memo.md" 'When Product Intent Review is active' 'decision-memo adaptation missing'
require_text "$OFFICE/kb/professional_communication.md" '### Product-Decision Result' 'communication lens missing'
require_text "$OFFICE/agents/writer_agent.md" 'verdict first, one main gap, next owner decision' 'Writer output order missing'
require_text "$OFFICE/agents/review_agent.md" 'Output challenge:' 'Review output challenge missing'
require_text "$OFFICE/agents/final_editor.md" 'preserve the approved Product Intent Review reader order' 'Final preservation missing'
require_text "$OFFICE/templates/tasks/review_task_template.md" 'Internal architecture is absent from user-facing output' 'conditional review field missing'

profile_count=$(find "$OFFICE/kb/deliverables" -maxdepth 1 -type f -name '*.md' | wc -l | tr -d ' ')
if [ "$profile_count" -ne 21 ]; then
  printf 'FAIL expected 20 profiles plus index, found %s\n' "$profile_count" >&2
  exit 1
fi

for forbidden in \
  "$OFFICE/kb/deliverables/product-intent-review.md" \
  "$OFFICE/templates/product_intent_review_template.md" \
  "$OFFICE/pipelines/product_intent_output_pipeline.md" \
  "$OFFICE/pipelines/product_intent_review_pipeline.md"
do
  if [ -e "$forbidden" ]; then
    printf 'FAIL forbidden output surface exists: %s\n' "$forbidden" >&2
    exit 1
  fi
done

sh "$OFFICE/tests/test_product_intent_review_output.sh"

printf '%s\n' 'Product Intent Review Step 4 output integration contract passed.'
