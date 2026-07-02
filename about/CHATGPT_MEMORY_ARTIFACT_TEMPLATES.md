# ChatGPT Memory: Artifact Templates

Purpose: compact memory summary of active task artifact shapes.

Canonical source files:

- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `ai-editorial-office/templates/artifacts/status_template.md`
- `ai-editorial-office/templates/artifacts/handoff_template.md`
- `ai-editorial-office/templates/artifacts/final_decision_template.md`

This file is a memory aid, not a canonical template. If it conflicts with the
source templates or `AGENTS.md`, use the canonical owner and stop if the
conflict affects production.

## Task Manifest

`task-manifest.md` is the first restart file and compact current-state pointer.
Keep it short, current, and explicit about versions.

It should contain:

- task identity: ID, title, type, current owner, dates;
- current state: status, selected pipeline, risk mode, process depth, execution
  profile, active client profile, current working artifact, latest relevant
  handoff, next action;
- freshness: last verified, verified by, stale-if condition;
- current version pointers when versions exist;
- governance state: review requirement, review artifact/outcome, human approval
  requirement, final decision artifact;
- artifact inventory;
- stale or conflicting state;
- active user, pipeline, client-profile, and governance constraints;
- real open questions only;
- next action packet: role, action, expected output, stop conditions;
- lifecycle notes for legacy folders, old versions, and safe-to-ignore material.

Do not use modified time, file order, or suffixes as current-version authority.

## Orchestration Plan

`orchestration_plan.md` is the task execution contract. It is created or updated
when role routing, process depth, high-risk traceability, or non-trivial
coordination matters.

It should contain:

- task summary: ID, goal, deliverable, audience/channel, active version;
- classification: task type, risk mode, factual sensitivity, human approval
  likelihood, rationale;
- process depth: compact, normal, or full; execution profile; active client
  profile when applicable; forbidden shortcuts;
- selected pipeline and reason;
- custom workflow mini-contract only for documented local deviations;
- required agents by stage;
- required knowledge and evidence;
- artifact scope with required, conditional, or omitted classification;
- structure-before-writing plan when relevant;
- execution order;
- status transitions;
- review requirements;
- human approval requirements;
- risks, unresolved questions, escalation conditions;
- completion, finalization, and restart conditions.

Conditional artifacts need a consumer or governance, traceability, or restart
reason.

## Status

`status.md` records task state and meaningful history. It is not the compact
manifest.

It should contain:

- task metadata and current active version;
- current status, since date, rationale, next role/action;
- status history table;
- current owner and waiting-on state;
- required and missing artifacts;
- blockers and unresolved questions;
- review state and reviewer independence;
- human approval state;
- escalation and retry state;
- risk summary;
- assumptions requiring verification;
- latest handoff;
- latest reliable checkpoint;
- completion, finalization, and archival readiness.

Use it for state changes, blockers, readiness, and restart checkpoints.

## Handoff

`handoff-*.md` transfers delta context from one role to another. It should not
repeat the full task history.

It should contain:

- metadata: task, from role, to role, date, status, risk mode, process depth,
  active version;
- reason for handoff;
- delta summary;
- artifacts created or updated;
- active constraints for the next role;
- blockers and open questions;
- required next action, expected output, and what not to change;
- validation before proceeding;
- escalation conditions.

Do not use `compact-handoff.md` automatically. It is only for final/user-facing
transfer or explicit context migration.

## Final Decision

`final_decision.md` records Chief Editor governance after review and
finalization checks. It does not create publication, delivery, or human approval
unless approval evidence is explicit.

It should contain:

- decision metadata;
- task summary;
- reviewed artifacts;
- review validation;
- required artifact validation;
- KB and policy validation;
- unresolved risks and questions;
- human approval validation;
- final readiness assessment;
- one final decision:
  - `approved_for_next_step`
  - `changes_required`
  - `blocked`
  - `requires_human_approval`
  - `not_ready`
- follow-up actions;
- escalation notes;
- archival and restart notes.

