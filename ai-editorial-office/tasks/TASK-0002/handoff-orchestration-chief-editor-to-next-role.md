# Handoff

## metadata

Task ID: `TASK-0002`

From role: `chief_editor`

To role: `research_agent`

Stage: `orchestration`

Created at: `2026-05-18 02:10:00 MSK`

Related manifest: `/tasks/TASK-0002/task-manifest.md`

Related status: `/tasks/TASK-0002/status.md`

Related orchestration plan: `/tasks/TASK-0002/orchestration_plan.md`

## reason for handoff

Orchestration is complete. Article Pipeline is selected, `standard` risk mode is confirmed, and research is required before writing because the topic invites factual and causal claims about AI tools and team workflows.

## delta summary

- Created: `orchestration_plan.md`, `handoff-orchestration-chief-editor-to-next-role.md`;
- Updated: `task-manifest.md`, `status.md`;
- State changes: status moved from `intake` to `research`; owner moved from `intake_agent` to `research_agent`; next route is research, not writing.

## artifacts created or updated

| Artifact | Action | Owner | Why it matters |
| --- | --- | --- | --- |
| `/tasks/TASK-0002/orchestration_plan.md` | created | `chief_editor` | Records pipeline, risk mode, artifact scope, and research assignment. |
| `/tasks/TASK-0002/task-manifest.md` | updated | `chief_editor` | Keeps compact state current for research restart. |
| `/tasks/TASK-0002/status.md` | updated | `chief_editor` | Records `intake` to `research` transition. |
| `/tasks/TASK-0002/handoff-orchestration-chief-editor-to-next-role.md` | created | `chief_editor` | Transfers only the delta to Research Agent. |

## active constraints for next role

- Do not write the article, outline, review, final, or governance decision.
- Do not invent audience, publication scope, internal examples, sources, claims, or numeric productivity claims.
- Treat examples as either sourced/supplied real cases or clearly generic scenario patterns.
- Keep research artifacts compact but traceable; standard mode requires normal research artifacts because factual claims are likely.
- Hand off back to `chief_editor` after research for sufficiency and unresolved-scope decisions.

## blockers and open questions

- Blockers: none for research.
- Blocks writing: unresolved audience, publication channel, final language/length, example type, and claim boundaries.
- May remain uncertain during research: final audience, publication channel, exact length, final thesis, and final example choice.

## next action

Next role: `research_agent`

Next action: Create a compact evidence base and claim-use map for the article topic, then hand off to Chief Editor for routing.

Expected outputs:

- `/tasks/TASK-0002/research.md`;
- `/tasks/TASK-0002/sources.md`;
- `/tasks/TASK-0002/facts.md`;
- `/tasks/TASK-0002/claims_table.md`;
- updated `/tasks/TASK-0002/open-questions.md`, if needed;
- updated `/tasks/TASK-0002/task-manifest.md`;
- updated `/tasks/TASK-0002/status.md`;
- research handoff to `chief_editor`.

Forbidden outputs:

- `outline.md`;
- `draft.md`;
- `review.md`;
- `final.md`;
- `final_decision.md`;
- publication approval or final audience/publication assumptions.

## validation before proceeding

- Manifest is current.
- Status is consistent with manifest.
- Orchestration plan exists and selects Article Pipeline with Research Pipeline upstream.
- Required previous-stage artifacts are present.
- No forbidden production artifacts were created.
- Next role is valid under `AGENTS.md`.

## escalation conditions

Stop and escalate to `chief_editor` if:

- research scope cannot be completed without choosing audience, publication scope, or real examples;
- sources are insufficient for the causal claims the article appears to require;
- evidence suggests `high-governance` risk mode is needed;
- the next action would cross into writing, review, finalization, publication, or approval;
- manifest, status, orchestration plan, or this handoff conflict.
