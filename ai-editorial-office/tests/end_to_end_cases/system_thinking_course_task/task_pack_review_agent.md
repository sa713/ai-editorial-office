This is a synthetic/sanitized end-to-end case. It is not a real task folder and does not contain real course source files, confidential methodology, internal training materials, participant data, client data, or restricted content.

# Task Pack

Task folder: ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task
Role: review_agent
Result: PASS

## Blockers
- none

## Warnings
- No handoff file found in task folder root.

## Read set

### Required
- `task-manifest.md` — task restart anchor and current state.
- `status.md` — current lifecycle state.
- `orchestration_plan.md` — selected pipeline, process depth, and routing context.

### Role-specific
- `brief.md` — review_agent role input.
- `draft.md` — review_agent role input.
- `final.md` — review_agent role input; current artifact pointer from task-manifest.md.
- `review.md` — review_agent role input.

### Conditional
- `ai-editorial-office/pipelines/social_pipeline.md` — selected pipeline contract for `social`.
- `ai-editorial-office/kb/00_index.md` — KB navigation and ownership index.
- `ai-editorial-office/kb/compact_execution.md` — compact execution mentioned in task context.
- `ai-editorial-office/kb/source_provenance.md` — source/provenance terms found in task context.
- `ai-editorial-office/kb/task_statuses.md` — status model context for `review_agent`.

## Not included
- `normalized-brief.md` — not present for `review_agent` role.
- `ux-copy.md` — not present for `review_agent` role.
- `research.md` — not present for `review_agent` role.
- `facts.md` — not present for `review_agent` role.
- `claims_table.md` — not present for `review_agent` role.
- `claims-used.md` — not present for `review_agent` role.
- `sources.md` — not present for `review_agent` role.
- `handoff*.md` — no handoff candidate found in task folder root.
- Client-profile files — client_profile is none or not specified.
- Latest modified files — never used as source of truth.
- Whole project scan — not performed by this helper.
