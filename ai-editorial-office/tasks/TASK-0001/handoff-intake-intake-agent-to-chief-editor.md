# Handoff

## handoff metadata

Task ID: `TASK-0001`

Handoff file: `handoff-intake-intake-agent-to-chief-editor.md`

Handoff type: `stage-specific`

Stage: `intake`

Created by: `intake_agent`

Created for: `chief_editor`

Created at: `2026-05-15 23:27:14 MSK`

Related status file: `/tasks/TASK-0001/status.md`

Related orchestration plan: `/tasks/TASK-0001/orchestration_plan.md`

Authority source: `AGENTS.md`

State model source: `/kb/task_statuses.md`

## sending role

Role: `intake_agent`

Agent spec: `/agents/intake_agent.md`

Work completed by this role:

- Normalized raw user request into an Article Pipeline task brief;
- Created initial bootstrap artifacts only;
- Documented non-blocking questions and assumptions;
- Prepared handoff to Chief Editor.

Decision boundaries reached:

- Intake recommendation is complete;
- Final pipeline approval, research routing, writing, review, finalization, and governance remain outside Intake Agent authority.

## receiving role

Role: `chief_editor`

Agent spec: `/agents/chief_editor.md`

Expected responsibility:

- Confirm and record Article Pipeline orchestration;
- Decide whether research is required before writing;
- Create `orchestration_plan.md`;
- Update `status.md`;
- Create the next handoff when routing to another role.

The receiving role must not assume any work is complete unless it is listed in this handoff or present in the referenced artifacts.

## current status

Current task status: `intake`

Previous task status: `none`

Status transition reason:

- Task package was created from the raw user request and is ready for Chief Editor orchestration.

Next expected status: `planning` or `research`

Status source of truth: `/tasks/TASK-0001/status.md`

If this handoff conflicts with `status.md`, the receiving role must stop and escalate.

## completed work

Summary of completed work:

- Task folder created at `/tasks/TASK-0001/`;
- `brief.md` created with goal, audience, tone, scope, constraints, and acceptance criteria;
- `status.md` created with operational status `intake`;
- `open-questions.md` created with non-blocking planning questions;
- No writing, review, finalization, approval, or governance artifacts were created.

Completed checklist:

| Item | Status | Evidence |
| --- | --- | --- |
| Task folder created | `done` | `/tasks/TASK-0001/` |
| Brief created | `done` | `/tasks/TASK-0001/brief.md` |
| Status created | `done` | `/tasks/TASK-0001/status.md` |
| Open questions created | `done` | `/tasks/TASK-0001/open-questions.md` |
| Intake handoff created | `done` | `/tasks/TASK-0001/handoff-intake-intake-agent-to-chief-editor.md` |
| Writing started | `not_done` | User explicitly forbade writing at bootstrap. |
| Review started | `not_done` | User explicitly forbade review at bootstrap. |

## artifacts created

| Artifact | Owner | Purpose | Ready for next role |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/brief.md` | `intake_agent` | Intake brief for Article Pipeline orchestration. | `yes` |
| `/tasks/TASK-0001/status.md` | `intake_agent` | Operational status source of truth. | `yes` |
| `/tasks/TASK-0001/open-questions.md` | `intake_agent` | Non-blocking questions and intake assumptions. | `yes` |
| `/tasks/TASK-0001/handoff-intake-intake-agent-to-chief-editor.md` | `intake_agent` | Transfer context from Intake Agent to Chief Editor. | `yes` |

## artifacts updated

None.

## selected pipeline

Pipeline file: `/pipelines/article_pipeline.md`

Pipeline stage completed: `intake`

Next pipeline stage: `chief_editor orchestration`

Pipeline constraints relevant to next role:

- User explicitly requested Article Pipeline;
- `orchestration_plan.md` must be created by `chief_editor`, not Intake Agent in this bootstrap;
- Review is mandatory before finalization;
- `final.md`, `final_decision.md`, `review.md`, and `approval.md` must not exist at bootstrap.

Pipeline conflicts:

- None identified at intake.

If a pipeline conflict exists, the next role must not proceed until it is resolved.

## required KB

KB already used:

| KB file | Used for | Notes |
| --- | --- | --- |
| `/kb/task_statuses.md` | Status selection and transition expectations. | Current status set to `intake`. |

KB required before next action:

| KB file | Required for | Must be loaded by |
| --- | --- | --- |
| `/kb/task_statuses.md` | Status transition and owner validation. | `chief_editor` |
| `/kb/editorial_policy.md` | Editorial risk and production constraints. | `chief_editor` |
| `/kb/tone_of_voice.md` | Tone guidance for calm, practical internal article. | `chief_editor` |

The receiving role must not rely on remembered KB content. Required KB must be read from disk.

## required next inputs

The receiving role must load:

- `AGENTS.md`;
- `/kb/task_statuses.md`;
- `/pipelines/article_pipeline.md`;
- `/tasks/TASK-0001/brief.md`;
- `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/open-questions.md`;
- this handoff file.

Optional but useful inputs:

- `/kb/editorial_policy.md`;
- `/kb/tone_of_voice.md`;
- `/kb/ux_writing_guidelines.md`, because the article concerns UX writers and product-team text work.

## assumptions

| Assumption | Reason | Risk | Needs verification |
| --- | --- | --- | --- |
| The task is ready for Chief Editor orchestration. | Goal, audience, tone, output, and constraints are sufficiently clear. | Low. | `no` |
| Research need is not settled at intake. | The article may use practical claims but no external facts or sources were supplied. | Medium. | `yes` |
| No human approval is required at bootstrap. | User did not request approval artifact or approval gate now. | Low. | Chief Editor should reassess before finalization or delivery. |

Assumptions must not be treated as facts by the receiving role.

## next required action

Next action owner: `chief_editor`

Next action:

```text
Create orchestration_plan.md, confirm Article Pipeline routing, decide whether research is required, update status.md, and route the task to the next role without starting writing or review in this bootstrap step.
```

Required before action:

- Verify current status is still `intake`;
- Confirm no forbidden bootstrap artifacts were created;
- Read the required inputs listed above.

Expected output:

- `/tasks/TASK-0001/orchestration_plan.md`;
- updated `/tasks/TASK-0001/status.md`;
- next handoff file appropriate to the selected route.

Expected status after action: `planning` or `research`

## success criteria for next role

The next role succeeds when:

- Article Pipeline orchestration is recorded;
- MVP roles are assigned only within Article Pipeline constraints;
- research requirement is explicitly decided;
- status transition is recorded in `status.md`;
- a new handoff is created if another role must continue.

The next role must not mark the stage complete if any blocking question remains open.

## escalation notes

Escalate if:

- Article Pipeline no longer fits the task;
- required KB is unavailable;
- the user asks to bypass writing, review, finalization, or governance rules;
- internal policy or examples are required but unavailable.

Escalation target: `chief_editor`

Smallest decision needed:

```text
Decide whether to route to research first or proceed to planning with a no-research rationale.
```

Risk of proceeding without escalation:

```text
The eventual draft may rely on generic assumptions or unsupported claims about AI-assisted editorial workflows.
```

Recommended status if escalation is needed: `blocked`

## restart notes

Minimum restart checklist for the receiving role:

- read `AGENTS.md`;
- read `/kb/task_statuses.md`;
- read `/pipelines/article_pipeline.md`;
- read `/tasks/TASK-0001/status.md`;
- read `/tasks/TASK-0001/brief.md`;
- read `/tasks/TASK-0001/open-questions.md`;
- read this handoff file;
- verify current status still matches this handoff;
- continue only from `next required action`.

Last known reliable state:

- Current status: `intake`
- Completed stage: `intake`
- Last completed artifact: `/tasks/TASK-0001/handoff-intake-intake-agent-to-chief-editor.md`
- Next role: `chief_editor`
- Next action: create orchestration plan and route the task
- Blocking issue, if any: `none`
