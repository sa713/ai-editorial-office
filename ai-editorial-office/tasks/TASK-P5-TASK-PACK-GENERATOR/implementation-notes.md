This is a task-local system-update packet for P5. It does not contain real task
materials.

# Implementation Notes

## Owner

Task pack generation is owned by
`ai-editorial-office/scripts/generate_task_pack.py`.

The smoke-test owner is
`ai-editorial-office/tests/test_task_pack_generator.sh`, with fixtures under
`ai-editorial-office/tests/fixtures/task_pack/`.

## Root Cause

The generator uses role-specific file allowlists such as `brief.md`, `draft.md`,
`claims-used.md`, `facts.md`, and `sources.md`. Task-local evidence summaries
like `source_summary.md` were not part of the writer or review_agent read-set
candidates, so the source-based compact-evidence case could mention the source
summary without the pack including it.

## What Changed

- Added an allowlist for task-local source/evidence summary names:
  `source_summary.md`, `source_notes.md`, `source-notes.md`,
  `source-summary.md`, `source_evidence.md`, `evidence_summary.md`.
- Added source/evidence context detection for compact-evidence, source-based,
  source-bound, task-local supplied source, task-local evidence, and source
  summary references.
- Added inclusion only for writer and review_agent.
- Included the artifact only when it exists and is explicitly declared in
  known task context.
- Marked the read-set reason as task-local evidence summary, not original
  source.

## Tests Added

- Positive: `source_summary_compact_evidence` includes `source_summary.md` for
  writer and review_agent.
- Negative: `writer_minimal` does not include `source_summary.md` or
  `source_notes.md`.
- Guard: `client_profile_pending` does not include client-profile files without
  active profile status.

## What Did Not Change

- No broad task folder dump.
- No latest-modified logic.
- No client-profile auto-activation.
- No review-gate, roles, pipelines, lifecycle, or validator changes.
- Historical E2E case reports were not rewritten.

## Verification

- `python3 -m py_compile ai-editorial-office/scripts/generate_task_pack.py`
  passed.
- `bash ai-editorial-office/tests/test_task_pack_generator.sh` passed.
- `git diff --check` passed.
- Manual generator runs for `system_thinking_course_task` now include
  `source_summary.md` for writer and review_agent.
