# Handoff

## metadata

Task ID: `TASK-0002`

From role: `research_agent`

To role: `chief_editor`

Stage: `research`

Created at: `2026-05-18 02:12:09 MSK`

Related manifest: `/tasks/TASK-0002/task-manifest.md`

Related status: `/tasks/TASK-0002/status.md`

Related orchestration plan: `/tasks/TASK-0002/orchestration_plan.md`

## reason for handoff

Research scope is complete enough for Chief Editor planning. The evidence base supports conditional claims about task fit, overreliance, workslop/rework, adoption gaps, and workflow governance, but writing still needs audience, publication, language/length, and example-scope decisions.

## delta summary

- Created: `research.md`, `sources.md`, `facts.md`, `claims_table.md`, `handoff-research-research-agent-to-chief-editor.md`;
- Updated: `open-questions.md`, `task-manifest.md`, `status.md`;
- State changes: recommended next status is `planning`; next role is `chief_editor`.

## artifacts created or updated

| Artifact | Action | Owner | Why it matters |
| --- | --- | --- | --- |
| `/tasks/TASK-0002/research.md` | created | `research_agent` | Compact synthesis, gaps, interpretations, generic workflow patterns, and writing implications. |
| `/tasks/TASK-0002/sources.md` | created | `research_agent` | Source traceability for factual claims. |
| `/tasks/TASK-0002/facts.md` | created | `research_agent` | Fact-level evidence map. |
| `/tasks/TASK-0002/claims_table.md` | created | `research_agent` | Allowed, caveated, and blocked claim guidance. |
| `/tasks/TASK-0002/open-questions.md` | updated | `research_agent` | Marks what still blocks writing rather than research. |
| `/tasks/TASK-0002/task-manifest.md` | updated | `research_agent` | Current compact state. |
| `/tasks/TASK-0002/status.md` | updated | `research_agent` | Research completion and next routing recommendation. |

## active constraints for next role

- Do not route directly to writing until audience, publication scope, language/length, and example policy are resolved or explicitly constrained.
- Do not use blocked claims from `claims_table.md`.
- Generic workflow scenarios must be labeled as generic/hypothetical.
- Numeric productivity or ROI claims need Chief Editor approval and precise source limits.
- Research does not grant review, finalization, governance, or publication approval.

## blockers and open questions

- Blockers for research: none.
- Blockers for writing: audience, publication channel, final language/length, example policy.
- Risk-mode watch: external publication, internal examples, legal/compliance/security/HR framing, vendor claims, or numeric productivity claims may require elevated governance or clarification.

## next action

Next role: `chief_editor`

Next action: Decide whether to ask the user for clarification or constrain the writing brief; then route to `writer_agent` or back to research if scope changes.

Expected outputs:

- updated `/tasks/TASK-0002/orchestration_plan.md` or status notes if Chief Editor changes route;
- updated `/tasks/TASK-0002/task-manifest.md`;
- updated `/tasks/TASK-0002/status.md`;
- next handoff, likely to `writer_agent` if writing blockers are resolved or constrained.

Forbidden outputs:

- article outline;
- draft;
- review;
- final deliverable;
- final governance decision;
- publication approval.

## validation before proceeding

- Manifest is current.
- Status is consistent with manifest.
- Required research artifacts are present.
- No writing, review, or finalization artifacts were created.
- Next role is valid under `AGENTS.md`.

## escalation conditions

Stop and escalate to user if:

- Chief Editor cannot select or constrain audience before writing;
- publication scope is external or official and approval requirements are unclear;
- real internal examples are required but not supplied;
- the article must include numeric productivity, ROI, vendor, legal, compliance, security, or HR claims beyond the current evidence base.
