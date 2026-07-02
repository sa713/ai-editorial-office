# Artifact ownership map

## Purpose

This map prevents drift by defining which file type owns which kind of truth. It does not redesign the system. It clarifies responsibility boundaries so future edits do not duplicate rules across every document.

## Canonical ownership

| Area | Canonical owner | Owns | Must not own |
| --- | --- | --- | --- |
| System invariants | `ai-editorial-office/AGENTS.md` | role separation, review-gate, authority hierarchy, context policy, artifact minimalism, governance boundaries | detailed pipeline sequence, every role output, editorial doctrine examples |
| Current system state | `ai-editorial-office/project-state.md` | current phase, current normalization decisions, active MVP constraints, known next system task | permanent policy that should live in `AGENTS.md` |
| Status model | `ai-editorial-office/kb/task_statuses.md` | allowed statuses, transitions, blocked/human approval semantics, retry/archival state rules | pipeline-specific artifact lists |
| Pipelines | `ai-editorial-office/pipelines/*.md` | when to use, stage sequence, stage-specific artifact requirements, pipeline-specific review focus | global invariants repeated in full |
| Agent specs | `ai-editorial-office/agents/*.md` | role mission, responsibilities, forbidden role actions, inputs/outputs, decision boundaries, escalation | full lifecycle duplication, status model duplication |
| Templates | `ai-editorial-office/templates/artifacts/*.md` | fillable fields and compact usage notes | long doctrine, repeated governance theory |
| Editorial knowledge | `editorial_knowledge/*.md` | editorial quality, usefulness, modes, failure patterns, review philosophy | operational task state, status transitions |
| Task manifest | `/tasks/TASK-ID/task-manifest.md` | compact current state, governance state, artifact inventory, active constraints, next action packet | narrative history, full review findings, full handoff content |
| Status | `/tasks/TASK-ID/status.md` | transition history, blockers, escalation notes, lifecycle rationale | artifact inventory as primary source, full role handoff |
| Orchestration plan | `/tasks/TASK-ID/orchestration_plan.md` | task-specific execution contract, selected pipeline/profile, role route, artifact scope, review target | narrative status log, complete artifact contents |
| Handoff files | `/tasks/TASK-ID/handoff-*.md` | role-to-role delta transfer | restart encyclopedia, full status history, full artifact inventory |
| Compact handoff | `/tasks/TASK-ID/compact-handoff.md` | final user-facing transfer summary when needed | role-to-role transfer unless explicitly named as such |
| Context summary | `/tasks/TASK-ID/context-summary.md` | recovery after context fragmentation or long task compaction | normal status updates or final user handoff |
| Review artifact | `/tasks/TASK-ID/review.md` | verdict, findings, review scope, independence check, required changes, next action | full rewrite, finalization, governance approval |
| Final decision | `/tasks/TASK-ID/final_decision.md` | Chief Editor final governance decision and residual approval state | final text body, publication approval unless explicitly human-granted |

## AGENTS

`AGENTS.md` should remain the constitution.

It should own:

- non-negotiable workflow invariants;
- MVP role set;
- authority hierarchy;
- context loading principles;
- artifact minimalism principles;
- review-gate requirements;
- finalization vs governance boundary;
- human approval boundary.

It should not become:

- a full copy of every pipeline;
- a full copy of every role spec;
- a style guide;
- a retrospective log.

## Pipelines

Pipelines should own sequence and task-type behavior.

They should answer:

- when this pipeline applies;
- what stage order is expected;
- which artifacts are required/conditional;
- how risk mode changes artifact depth;
- what review should focus on for this task type.

They should avoid reprinting global rules except as short references.

## Templates

Templates should be fields plus concise usage guardrails.

Good template behavior:

- tell agent what to fill;
- keep placeholders clear;
- prevent common misuse;
- avoid carrying full doctrine.

Bad template behavior:

- repeating all rules from `AGENTS.md`;
- turning optional fields into implicit requirements;
- making every artifact look mandatory.

## Editorial knowledge

Editorial knowledge owns judgment, not workflow.

It should guide:

- reader task;
- useful outcome;
- editorial modes;
- structure behavior;
- context discipline;
- review criteria;
- failure patterns.

It should not define:

- task statuses;
- handoff names;
- role ownership;
- finalization stages.

## Manifests

Manifest owns compact current state.

It should contain:

- task identity;
- risk mode;
- current status/stage/owner;
- latest handoff;
- governance state;
- artifact inventory;
- active constraints;
- open questions;
- next action packet;
- freshness block.

It must not become:

- a lifecycle diary;
- a place for full review;
- a duplicate orchestration plan.

## Statuses

`status.md` owns history and transitions.

It should contain:

- previous status;
- new status;
- reason;
- role;
- next action;
- blockers;
- escalation notes.

It may be narrative enough for humans, but should not be the only operational source of truth.

## Orchestration

`orchestration_plan.md` owns task-specific execution contract.

It should contain:

- selected pipeline or custom mini-contract;
- process depth: compact, normal, full;
- risk mode and rationale;
- role route;
- artifact scope;
- review target;
- explicit omitted artifacts when compact path is used;
- stop/escalation conditions.

It should not repeat every pipeline rule.

## Rule for future edits

When adding or changing a rule, ask:

1. Which file owns this concern?
2. Is this rule already stated elsewhere?
3. Can other files reference the owner instead of repeating it?
4. Does the rule change behavior, or only add explanation?

If no canonical owner is clear, do not add the rule until ownership is decided.
