# Orchestration Plan

## task summary

- Task ID: `SYSTEM-MAINTENANCE-UPDATE-0021`
- User goal: add a compact Preflight Gate before production activity.
- Deliverable: task-local design/review package plus minimal system-file changes.
- Audience/channel: local AI editorial office and project owner.
- Current active version: this maintenance package.

## task classification

- Task type: `editorial system update / process maintenance`
- Risk mode: `standard`
- Factual sensitivity: low
- Human approval likely required: no
- Rationale: the update changes process guidance, but it is narrow and explicitly constrained not to alter status model, governance, review-gate, roles, or pipelines.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: the task needs design, implementation, review, final decision, and a diff, but not a new system pipeline.
- Forbidden depth shortcuts: no system-file changes before `design-note.md`; no review skip; no old-task mutation.
- Expanded profile trigger, if any: conflict with role boundaries, status model, governance, or user constraints.

## selected pipeline

- Pipeline: `custom workflow mini-contract`
- Why this pipeline: no dedicated system-maintenance pipeline exists; the output is a bounded system process update.
- Pipeline exceptions or local constraints: preserve current lifecycle and review gate.

## custom workflow mini-contract

- Deviation: compact maintenance workflow rather than article/social/research/UX pipeline.
- Reason: this is a process update, not a production editorial deliverable.
- Owner: `chief_editor`
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Routing/design | `chief_editor` | yes | Create task package and design note |
| Implementation | `chief_editor` | yes | Targeted system-file changes only |
| Review | `review_agent` | yes | Verify compatibility and constraints |
| Final governance | `chief_editor` | yes | Record final decision |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart pointer |
| `orchestration_plan.md` | required | all roles | Mini-contract |
| `status.md` | required | all roles | State transitions |
| `design-note.md` | required | maintainer / reviewer | Pre-change design |
| `changed-files.md` | required | reviewer / maintainer | Change trace |
| `diff.md` | required by user | reviewer / maintainer | Diff of changed system files |
| `pilot-preflight-examples.md` | required | reviewer / maintainer | Demonstrates gate decisions |
| `review.md` | required | Chief Editor | Compatibility review |
| `final_decision.md` | required | user / archive | Governance closeout |
| New preflight artifact template | omitted | none | Gate must live in existing artifacts |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | user request, `AGENTS.md`, TASK-0024 signal | `design-note.md` | Design completed before edits |
| 2 | `chief_editor` | design note | targeted system-file changes | Gate integrated minimally |
| 3 | `chief_editor` | changed files | `changed-files.md`, `diff.md`, `pilot-preflight-examples.md` | Trace and examples complete |
| 4 | `review_agent` | implementation package | `review.md` | Verdict recorded |
| 5 | `chief_editor` | review | `final_decision.md` | Final decision recorded |

## review requirements

- Review artifact: `review.md`
- Review depth: compact but explicit against constraints.
- Reviewer independence requirement: `review_agent` evaluates saved artifacts and changed files.
- Claims/evidence checks required: check no new role, no new pipeline, no mandatory new file, no status/governance/review-gate change, compact tasks still compact.

## completion criteria

- Design note complete.
- System-file changes are minimal and listed.
- `diff.md` includes all changed system files.
- Pilot examples show ASK, CONSTRAIN, PROCEED, and BLOCK.
- Review outcome is approved.
- Final decision is recorded.

