# Handoff

## metadata

Task ID: `TASK-0002`

From role: `intake_agent`

To role: `chief_editor`

Stage: `intake`

Created at: `2026-05-18 01:57:51 MSK`

Related manifest: `/tasks/TASK-0002/task-manifest.md`

Related status: `/tasks/TASK-0002/status.md`

Related orchestration plan: `not_created`

## reason for handoff

Intake bootstrap is complete for a raw article request about AI tools hindering teams. The task now needs Chief Editor orchestration, including final pipeline selection, risk-mode confirmation, and research/clarification routing.

## delta summary

- Created: `brief.md`, `task-manifest.md`, `status.md`, `open-questions.md`, `handoff-intake-intake-agent-to-chief-editor.md`;
- Updated: none;
- State changes: new task created with operational status `intake`, preliminary risk mode `standard`, likely task type `article`, likely pipeline `/pipelines/article_pipeline.md` but not selected.

## artifacts created or updated

| Artifact | Action | Owner | Why it matters |
| --- | --- | --- | --- |
| `/tasks/TASK-0002/brief.md` | created | `intake_agent` | Captures raw request, uncertainties, constraints, preliminary risk mode, and success criteria. |
| `/tasks/TASK-0002/task-manifest.md` | created | `intake_agent` | Compact restart anchor and current state. |
| `/tasks/TASK-0002/status.md` | created | `intake_agent` | Records intake status, blockers, and next role. |
| `/tasks/TASK-0002/open-questions.md` | created | `intake_agent` | Lists questions that should not be silently answered by downstream roles. |
| `/tasks/TASK-0002/handoff-intake-intake-agent-to-chief-editor.md` | created | `intake_agent` | Transfers the task to Chief Editor without duplicating full task state. |

## active constraints for next role

- User requested intake only; do not treat this handoff as permission to start research, writing, review, finalization, or publication.
- Final pipeline is not selected; `/pipelines/article_pipeline.md` is only likely.
- Audience, publication scope, example type, and factual sensitivity are unresolved.
- Do not invent examples, claims, sources, internal practices, or audience.
- Review gate remains mandatory before any final material.

## blockers and open questions

- Blockers: none for Chief Editor orchestration.
- Open questions: audience, publication channel, final language/length, article job, AI tool scope, meaning of "мешать", example type, internal examples, numeric claims, and human approval.

See `/tasks/TASK-0002/open-questions.md` for the compact question table.

## next action

Next role: `chief_editor`

Next action: Confirm or override likely article routing and preliminary `standard` risk mode; decide whether to request clarification or route research before writing; create `orchestration_plan.md` only if orchestration proceeds.

Expected outputs:

- `/tasks/TASK-0002/orchestration_plan.md`, if proceeding with orchestration;
- updated `/tasks/TASK-0002/task-manifest.md`;
- updated `/tasks/TASK-0002/status.md`;
- next handoff selected by Chief Editor.

Forbidden outputs:

- research artifacts;
- writing artifacts;
- review artifacts;
- finalization or governance artifacts;
- invented examples, claims, sources, audience, or publication context.

## validation before proceeding

- Manifest is current.
- Status is consistent with manifest.
- Required intake-stage artifacts are present.
- No forbidden downstream artifacts were created.
- Next role is valid under `AGENTS.md`.

## escalation conditions

Stop and escalate to `chief_editor` if:

- manifest, status, brief, open questions, or this handoff conflict;
- orchestration would require silently choosing audience, publication scope, or examples;
- risk mode cannot be safely confirmed without user clarification;
- the next action would cross role boundaries;
- review-gate, role separation, finalization boundary, or final governance integrity is at risk.
