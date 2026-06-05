This is a synthetic/sanitized end-to-end case. It is not a real task folder and does not contain real methodology, real meeting records, real PSI materials, client data, or internal confidential content.

# Task Pack

Task folder: ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback
Role: writer
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
- `brief.md` — writer role input.
- `draft.md` — writer role input.

### Conditional
- `ai-editorial-office/pipelines/social_pipeline.md` — selected pipeline contract for `social`.
- `final.md` — current artifact pointer from task-manifest.md.
- `ai-editorial-office/kb/00_index.md` — KB navigation and ownership index.
- `ai-editorial-office/kb/compact_execution.md` — compact execution mentioned in task context.
- `ai-editorial-office/kb/source_provenance.md` — source/provenance terms found in task context.

## Not included
- `normalized-brief.md` — not present for `writer` role.
- `research.md` — not present for `writer` role.
- `facts.md` — not present for `writer` role.
- `claims-used.md` — not present for `writer` role.
- `sources.md` — not present for `writer` role.
- `handoff*.md` — no handoff candidate found in task folder root.
- Client-profile files — client_profile is none or not specified.
- Latest modified files — never used as source of truth.
- Whole project scan — not performed by this helper.
