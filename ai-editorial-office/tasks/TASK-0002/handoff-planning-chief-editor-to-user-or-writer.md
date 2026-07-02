# Handoff

## metadata

Task ID: `TASK-0002`

From role: `chief_editor`

To role: `writer_agent`

Stage: `planning`

Created at: `2026-05-18 02:15:15 MSK`

Related manifest: `/tasks/TASK-0002/task-manifest.md`

Related status: `/tasks/TASK-0002/status.md`

Related orchestration plan: `/tasks/TASK-0002/orchestration_plan.md`

## reason for handoff

Research is sufficient for a constrained first article draft. Chief Editor decided not to ask the user a questionnaire now because remaining unknowns can be safely constrained for drafting without pretending they are resolved.

## delta summary

- Created: `planning-notes.md`, `handoff-planning-chief-editor-to-user-or-writer.md`;
- Updated: `task-manifest.md`, `status.md`, `orchestration_plan.md`, `open-questions.md`;
- State changes: status moved from `planning` to `writing`; owner moved from `chief_editor` to `writer_agent`.

## artifacts created or updated

| Artifact | Action | Owner | Why it matters |
| --- | --- | --- | --- |
| `/tasks/TASK-0002/planning-notes.md` | created | `chief_editor` | Records clarification decision and constrained writing scope. |
| `/tasks/TASK-0002/task-manifest.md` | updated | `chief_editor` | Current compact routing state. |
| `/tasks/TASK-0002/status.md` | updated | `chief_editor` | Records planning to writing transition. |
| `/tasks/TASK-0002/orchestration_plan.md` | updated | `chief_editor` | Adds post-research writing constraints. |
| `/tasks/TASK-0002/open-questions.md` | updated | `chief_editor` | Marks which uncertainties are deferred vs blocking later. |

## active constraints for next role

- Write in Russian.
- Treat audience as general professional readers who work in or with teams; do not claim a specific audience or publication channel.
- Use generic hypothetical workflow scenarios only; do not invent real cases or internal examples.
- Use only allowed or caveated claims from `claims_table.md`.
- Do not use blocked claims.
- Avoid numeric claims unless tightly attributed and necessary.
- Keep tone calm, practical, non-alarmist, non-hype.
- Do not imply approval, publication readiness, finalization, or governance completion.

## blockers and open questions

- Blockers for writing: none under the constraints above.
- Deferred: publication channel, exact length, human approval, and real examples.
- Blocking later: publication/finalization approval, internal examples, vendor/legal/compliance/security/HR claims, or numeric productivity claims beyond current evidence.

## next action

Next role: `writer_agent`

Next action: Create a constrained article outline and draft from the brief, research, claims table, and this handoff.

Expected outputs:

- `/tasks/TASK-0002/outline.md`;
- `/tasks/TASK-0002/draft.md`;
- `/tasks/TASK-0002/writer-notes.md`;
- `/tasks/TASK-0002/claims-used.md`;
- updated `/tasks/TASK-0002/task-manifest.md`;
- updated `/tasks/TASK-0002/status.md`;
- writing handoff to `review_agent` or `chief_editor` as allowed by the pipeline.

Forbidden outputs:

- `review.md`;
- `final.md`;
- `final_decision.md`;
- publication approval;
- real internal examples;
- vendor/legal/compliance/security/HR claims;
- universal claims that AI harms teams.

## validation before proceeding

- Manifest is current.
- Status is consistent with manifest.
- Research artifacts and `claims_table.md` are present.
- No writing artifact existed before this handoff.
- Next role is valid under `AGENTS.md`.

## escalation conditions

Stop and escalate to `chief_editor` if:

- a necessary claim is blocked or unsupported;
- the draft requires real examples, internal context, or a specific publication channel;
- numeric productivity, ROI, legal, compliance, security, HR, vendor, or policy claims become necessary;
- the task begins to imply publication or approval rather than a draft.
