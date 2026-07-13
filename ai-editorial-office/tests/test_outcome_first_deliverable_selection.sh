#!/usr/bin/env sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
office="$repo_root/ai-editorial-office"

require_text() {
  file="$1"
  text="$2"
  if ! grep -Fq "$text" "$file"; then
    echo "FAIL: $file is missing required contract text: $text"
    exit 1
  fi
}

require_text "$office/kb/task_need_recognition.md" "## Outcome-First Deliverable Recommendation"
require_text "$office/kb/task_need_recognition.md" "Requested deliverable"
require_text "$office/kb/task_need_recognition.md" "Recommended deliverable"
require_text "$office/kb/task_need_recognition.md" "Selected deliverable"
require_text "$office/kb/task_need_recognition.md" "silently override"
require_text "$office/agents/chief_editor.md" "then select or confirm the appropriate pipeline"
require_text "$office/agents/review_agent.md" "pipeline selection followed the selected deliverable"
require_text "$office/templates/artifacts/orchestration_plan_template.md" "## outcome-first deliverable decision"
require_text "$office/templates/artifacts/orchestration_plan_template.md" "## selected pipeline"
require_text "$office/tests/outcome_first_deliverable_selection_smoke_test.md" "Bare Explain Request Cannot Become A Checklist"
require_text "$office/tests/outcome_first_deliverable_selection_smoke_test.md" 'Fail. `Explain` requires'

if grep -Fq "Outcome-first deliverable gate" \
  "$office/pipelines/review_pipeline.md"; then
  echo "FAIL: outcome-first checks must stay inside the existing Task Need Recognition gate."
  exit 1
fi

decision_line=$(awk '/^## outcome-first deliverable decision$/ { print NR; exit }' \
  "$office/templates/artifacts/orchestration_plan_template.md")
pipeline_line=$(awk '/^## selected pipeline$/ { print NR; exit }' \
  "$office/templates/artifacts/orchestration_plan_template.md")

if [ -z "$decision_line" ] || [ -z "$pipeline_line" ] || \
  [ "$decision_line" -ge "$pipeline_line" ]; then
  echo "FAIL: deliverable decision must appear before selected pipeline in orchestration template."
  exit 1
fi

case_count=$(grep -c '^## Case ' \
  "$office/tests/outcome_first_deliverable_selection_smoke_test.md")
if [ "$case_count" -ne 10 ]; then
  echo "FAIL: expected 10 synthetic cases, found $case_count."
  exit 1
fi

for forbidden in \
  "$office/agents/deliverable_agent.md" \
  "$office/agents/format_agent.md" \
  "$office/pipelines/deliverable_pipeline.md" \
  "$office/pipelines/format_pipeline.md"
do
  if [ -e "$forbidden" ]; then
    echo "FAIL: forbidden architecture element exists: $forbidden"
    exit 1
  fi
done

echo "PASS: outcome-first deliverable selection contract and 10 synthetic cases are present."
