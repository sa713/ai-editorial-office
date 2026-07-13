#!/usr/bin/env sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
office="$repo_root/ai-editorial-office"
catalogue="$office/kb/deliverables"

require_text() {
  file="$1"
  text="$2"
  if ! grep -Fq "$text" "$file"; then
    echo "FAIL: $file is missing required contract text: $text"
    exit 1
  fi
}

require_absent() {
  file="$1"
  text="$2"
  if grep -Fq "$text" "$file"; then
    echo "FAIL: $file contains forbidden contract text: $text"
    exit 1
  fi
}

require_text "$catalogue/00_index.md" "not a template library"
require_text "$office/kb/task_need_recognition.md" "## Selected Deliverable Set"
require_text "$office/kb/task_need_recognition.md" "minimum sufficient artifact family"
require_text "$office/kb/task_object_model.md" '`selected_deliverable_set`'
require_text "$office/agents/chief_editor.md" "one-artifact sufficiency"
require_text "$office/agents/review_agent.md" "removable or missing companions"
require_text "$office/templates/artifacts/orchestration_plan_template.md" "| Order | Deliverable | Purpose in this task | Dependency | Production priority |"
require_text "$office/pipelines/review_pipeline.md" "automatic routing/activation/depth/production"
require_absent "$office/kb/task_need_recognition.md" "recommend and select"
require_text "$office/tests/deliverable-knowledge-multi-deliverable-planning-smoke-test.md" \
  "audience can discover it, but choose the minimum sufficient artifact set."

profile_count=$(find "$catalogue" -maxdepth 1 -type f -name '*.md' | wc -l | tr -d ' ')
if [ "$profile_count" -ne 21 ]; then
  echo "FAIL: expected 20 deliverable profiles plus index, found $profile_count files."
  exit 1
fi

for profile in "$catalogue"/*.md; do
  if [ "$(basename "$profile")" = "00_index.md" ]; then
    continue
  fi
  for heading in \
    "## Purpose" \
    "## Best Use Cases" \
    "## Weak Use Cases" \
    "## Typical Reader Goal" \
    "## Typical Structure" \
    "## Strengths" \
    "## Weaknesses" \
    "## Common Failure Modes" \
    "## Typical Companion Deliverables" \
    "## Not This"
  do
    require_text "$profile" "$heading"
  done
  require_text "$profile" "not a template or pipeline"
done

decision_line=$(awk '/^## outcome-first deliverable decision$/ { print NR; exit }' \
  "$office/templates/artifacts/orchestration_plan_template.md")
pipeline_line=$(awk '/^## selected pipeline$/ { print NR; exit }' \
  "$office/templates/artifacts/orchestration_plan_template.md")

if [ -z "$decision_line" ] || [ -z "$pipeline_line" ] || \
  [ "$decision_line" -ge "$pipeline_line" ]; then
  echo "FAIL: selected deliverable set must be decided before pipeline selection."
  exit 1
fi

case_count=$(grep -c '^## Case ' \
  "$office/tests/deliverable-knowledge-multi-deliverable-planning-smoke-test.md")
if [ "$case_count" -ne 8 ]; then
  echo "FAIL: expected 8 synthetic cases, found $case_count."
  exit 1
fi

for forbidden in \
  "$office/agents/deliverable_agent.md" \
  "$office/agents/catalogue_agent.md" \
  "$office/agents/package_agent.md" \
  "$office/agents/bundle_agent.md" \
  "$office/pipelines/deliverable_pipeline.md" \
  "$office/pipelines/catalogue_pipeline.md" \
  "$office/pipelines/package_pipeline.md" \
  "$office/pipelines/bundle_pipeline.md" \
  "$office/templates/deliverables"
do
  if [ -e "$forbidden" ]; then
    echo "FAIL: forbidden architecture element exists: $forbidden"
    exit 1
  fi
done

echo "PASS: deliverable catalogue, minimal selected sets, 20 profiles, and 8 synthetic cases are present."
