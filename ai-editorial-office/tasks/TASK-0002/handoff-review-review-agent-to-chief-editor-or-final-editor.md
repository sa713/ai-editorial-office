# Handoff

## metadata

Task ID: `TASK-0002`

From role: `review_agent`

To role: `chief_editor`

Stage: `review`

Created at: `2026-05-18 02:30:40 MSK`

Related manifest: `/tasks/TASK-0002/task-manifest.md`

Related status: `/tasks/TASK-0002/status.md`

Review artifact: `/tasks/TASK-0002/review.md`

QA checklist: `/tasks/TASK-0002/qa-checklist.md`

## reason for handoff

Independent review is complete with verdict `changes_requested`. The draft should not move to finalization yet.

## delta summary

- Created: `review.md`, `qa-checklist.md`, `handoff-review-review-agent-to-chief-editor-or-final-editor.md`.
- Updated: `task-manifest.md`, `status.md`.
- State change: `review` -> `changes_requested`.

## required next action

Chief Editor should route the task to `writer_agent` for a limited revision.

Required fixes:

- Soften `Самый частый сбой...` because frequency is unsupported.
- Soften `Такие правила не делают работу медленнее.` because it implies an unsupported general speed/productivity effect.

No new research, user clarification, or finalization is required before this limited revision.

## residual constraints

- Keep examples generic/hypothetical.
- Do not add real cases, vendors, numeric productivity claims, legal/HR/security/compliance claims, or publication approval language.
- After revision, return to `review_agent` for re-review.
