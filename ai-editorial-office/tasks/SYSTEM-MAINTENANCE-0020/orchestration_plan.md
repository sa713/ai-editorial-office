# Orchestration Plan

## task summary

- Task ID: `SYSTEM-MAINTENANCE-0020`
- User goal: add a light post-delivery user feedback loop to the editorial system.
- Deliverable: task-local design/review package plus minimal system files or references needed to support optional feedback capture and pattern accumulation.
- Audience/channel: AI editorial office agents and the single project owner.
- Current active version: this maintenance package.

## task classification

- Task type: `editorial system update / process maintenance`
- Risk mode: `standard`
- Factual sensitivity: low
- Human approval likely required: no
- Rationale: this changes editorial process guidance, but the requested change is narrow, non-visual, non-public, and does not alter governance/status model.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: the task needs design, implementation, review, and final decision, but not research depth or a new pipeline.
- Forbidden depth shortcuts: no skipped review, no direct system-file changes before `design-note.md`, no old-task mutation.
- Expanded profile trigger, if any: conflict with `AGENTS.md`, status model, governance, or role ownership.

## selected pipeline

- Pipeline: `custom workflow mini-contract`
- Why this pipeline: no dedicated system-maintenance pipeline exists; this is a bounded process update.
- Pipeline exceptions or local constraints: standard lifecycle is preserved conceptually as planning -> implementation -> review -> final governance decision.

## custom workflow mini-contract

- Deviation: use a compact maintenance workflow rather than article/social/UX/research pipeline.
- Reason: the output is a process change, not an editorial content deliverable.
- Owner: `chief_editor`
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/routing | `chief_editor` | yes | Determine task type and constraints |
| Design | `chief_editor` | yes | Create `design-note.md` before system changes |
| Implementation | `chief_editor` | yes | Apply targeted file changes only |
| Review | `review_agent` | yes | Produce `review.md` |
| Final governance | `chief_editor` | yes | Produce `final_decision.md` |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart pointer |
| `orchestration_plan.md` | required | all roles | Route and scope control |
| `design-note.md` | required | user / system maintainer | Pre-change mechanism design |
| `changed-files.md` | required | reviewer / maintainer | Traceability of edited files |
| `pilot-feedback-examples.md` | required | reviewer / maintainer | Demonstrates old-task behavior without mutation |
| `review.md` | required | Chief Editor | Checks constraints and review gate |
| `final_decision.md` | required | user / archive | Final governance decision |
| handoffs | omitted | none | Compact package is self-contained |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | user request, `AGENTS.md` | task package and `design-note.md` | design note complete |
| 2 | `chief_editor` | `design-note.md` | targeted system file changes | files updated and listed |
| 3 | `chief_editor` | old task references only as examples | `pilot-feedback-examples.md` | no old task folders changed |
| 4 | `review_agent` | task package and changed files | `review.md` | verdict recorded |
| 5 | `chief_editor` | `review.md` | `final_decision.md` | governance decision recorded |

## status transitions

- Starting status: `planning`
- Next expected status: `writing` for implementation, then `review`, `approved`, `finalized`
- Status owner: `chief_editor`, then `review_agent` during review
- Status update trigger: completion of design, implementation, review, and final decision

## review requirements

- Review artifact: `review.md`
- Review depth: compact but explicit against user constraints
- Reviewer independence requirement: `review_agent` must evaluate implementation artifacts, not create them
- Claims/evidence checks required: check file placement, optionality, anti-self-modification guardrail, old-task non-mutation
- Optional review artifacts justified: no

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Feedback becomes routine bureaucracy | Bloats lifecycle | `chief_editor` / `review_agent` | Make `feedback.md` optional and only post-reaction |
| Single feedback changes system rules | Chaotic self-modification | `chief_editor` / `review_agent` | Add escalation ladder and pattern log |
| Old tasks are rewritten | Historical drift | `chief_editor` | Pilot examples live only in current task |
| New role or pipeline appears | Architecture drift | `review_agent` | Use existing roles and mini-contract only |

## completion criteria

- Required task-local artifacts complete.
- Minimal system files updated.
- Optional `feedback.md` template exists.
- Feedback pattern log exists in chosen canonical location.
- Review confirms constraints.
- Final decision records readiness.
