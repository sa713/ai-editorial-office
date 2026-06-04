#!/usr/bin/env sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
about_dir="$repo_root/about"

expected_count=20
actual_count=$(find "$about_dir" -maxdepth 1 -type f | wc -l | tr -d ' ')

if [ "$actual_count" != "$expected_count" ]; then
  echo "FAIL: /about contains $actual_count files; expected $expected_count."
  exit 1
fi

check_pair() {
  source_path="$1"
  about_name="$2"

  if ! cmp -s "$repo_root/$source_path" "$about_dir/$about_name"; then
    echo "FAIL: about/$about_name differs from $source_path"
    exit 1
  fi
}

check_pair "ai-editorial-office/AGENTS.md" "AGENTS.md"
check_pair "ai-editorial-office/project-state.md" "project-state.md"
check_pair "ai-editorial-office/kb/task_statuses.md" "task_statuses.md"
check_pair "ai-editorial-office/agents/chief_editor.md" "chief_editor.md"
check_pair "ai-editorial-office/agents/intake_agent.md" "intake_agent.md"
check_pair "ai-editorial-office/agents/research_agent.md" "research_agent.md"
check_pair "ai-editorial-office/agents/writer_agent.md" "writer_agent.md"
check_pair "ai-editorial-office/agents/ux_writer.md" "ux_writer.md"
check_pair "ai-editorial-office/agents/review_agent.md" "review_agent.md"
check_pair "ai-editorial-office/agents/final_editor.md" "final_editor.md"
check_pair "ai-editorial-office/pipelines/article_pipeline.md" "article_pipeline.md"
check_pair "ai-editorial-office/pipelines/research_pipeline.md" "research_pipeline.md"
check_pair "ai-editorial-office/pipelines/review_pipeline.md" "review_pipeline.md"
check_pair "ai-editorial-office/pipelines/social_pipeline.md" "social_pipeline.md"
check_pair "ai-editorial-office/pipelines/ux_writing_pipeline.md" "ux_writing_pipeline.md"

echo "OK: /about has $expected_count files and copied files match canonical sources."
