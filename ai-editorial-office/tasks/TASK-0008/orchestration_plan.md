# TASK-0008 orchestration plan

## task summary

Task ID: `TASK-0008`

Task title: `CYBER-LUNCHES COMMUNICATION DIAGNOSIS`

Requested output: diagnostic editorial package plus compact handoff.

Audience: task owner and future editorial users; secondary audiences are leadership, executors, and potential participants.

Primary goal: identify what is broken in the communication and what artifact architecture should replace it.

Quality bar: professional editorial-system diagnosis, not copywriting cleanup.

Current task status: `planning`

Brief source: `/tasks/TASK-0008/brief.md`

Status source: `/tasks/TASK-0008/status.md`

## task classification

Task type: `editorial-review / communication diagnosis`

Complexity: `medium`

Risk level: `standard`

Factual sensitivity: `low-medium`

Requires research: `no external research`; source diagnosis only.

Requires writing: `yes`, diagnostic and bounded revised artifacts.

Requires optional revision: `yes`, if diagnosis justifies a replacement artifact set.

Requires independent review: `yes`

Requires human approval: `yes` before any real stakeholder send-out.

Classification rationale:

- the materials are internal, but stakeholder interpretation and employee feedback sensitivity matter;
- the task is about communication architecture and operational clarity, not factual investigation.

## selected workflow

No single existing pipeline fully fits. Use a custom local editorial workflow under `AGENTS.md`:

```text
intake -> orchestration -> material diagnosis -> audience analysis -> rewrite strategy -> bounded revised artifacts -> review -> final decision
```

Pipeline constraints:

- do not collapse diagnosis into rewriting;
- do not create revised artifacts unless the diagnosis shows which artifacts should exist;
- review must verify whether the package transfers understanding, not just whether it is stylistically clean.

## required role behavior

| Stage | Role behavior | Responsibility |
| --- | --- | --- |
| intake | `intake_agent` behavior | normalize task, materials, audiences, and quality bar |
| orchestration | `chief_editor` behavior | set workflow, artifact scope, and review criteria |
| diagnosis | `writer_agent` behavior | produce structured diagnosis and rewrite strategy |
| review | `review_agent` behavior | independently test the package against the brief |
| final decision | `chief_editor` behavior | validate artifact completeness and final state |

## artifact scope

| Artifact | Class | Purpose |
| --- | --- | --- |
| `brief.md` | required | active task definition |
| `task-manifest.md` | required | compact state |
| `status.md` | required | lifecycle history |
| `orchestration_plan.md` | required | execution contract |
| `diagnosis.md` | required | main interpretation of failure |
| `audience-analysis.md` | required | audience needs and mismatch |
| `communication-failures.md` | required | failure taxonomy |
| `rewrite-strategy.md` | required | rebuild plan |
| `revised-manager-summary.md` | conditional, justified | leadership layer |
| `revised-operational-concept.md` | conditional, justified | executor operating model |
| `revised-executor-next-step.md` | conditional, justified | immediate post-meeting alignment |
| `revised-participant-announcement.md` | conditional, justified | participant-facing launch copy |
| `revised-faq.md` | conditional, justified | reusable clarification layer |
| `review.md` | required | independent review verdict |
| `final_decision.md` | required | governance decision |
| `compact-handoff.md` | required | final user-facing handoff |

## structure-before-writing plan

Expected reader usage mode: mixed quick scanning and decision support.

Proposed structure type:

- answer-first diagnosis;
- audience-by-audience analysis;
- failure taxonomy;
- artifact architecture recommendation;
- bounded revised prototypes.

Likely reader-path risks:

- mistaking diagnosis for personal criticism of the author;
- reducing the problem to length;
- over-producing artifacts instead of separating layers;
- approving attractive wording without resolving ownership and operating model.

## review criteria

Review must verify:

- usefulness;
- executive clarity;
- operational realism;
- information hierarchy;
- audience alignment;
- structure quality;
- signal-to-noise ratio;
- answer-first behavior;
- whether readers can explain the initiative after reading;
- where the old communication performs intelligence instead of transferring understanding;
- where abstraction replaces operational meaning;
- where detail replaces decision clarity;
- where audiences receive the wrong layer of information.

