# Step 5 Compact Execution Decisions

## Canonical Rule

`AGENTS.md` now owns compact execution profile as a global operating rule.

Compact execution is an official bounded operating mode inside the selected
pipeline. It is not a new pipeline, workflow, agent, status model, automation,
or governance model.

## What Compact Execution Allows

For low-risk and simple source-light standard tasks, compact execution may use:

- short context read path;
- minimum task-appropriate artifact set;
- one primary `review.md`;
- short handoff only when the next role needs delta context;
- compact final decision evidence;
- no conditional artifacts without explicit reason.

## What Compact Execution Does Not Mean

Compact execution does not mean:

- lower quality;
- weaker review;
- skipped evidence;
- skipped review;
- skipped governance;
- missing artifacts;
- minimalism at any cost.

It means:

- less service weight;
- less duplication;
- less restart friction.

## Non-Automatic Scope

Compact execution is not applied automatically to:

- high-governance tasks;
- conflict-heavy tasks;
- source-sensitive tasks;
- externally risky tasks;
- evidence-heavy tasks;
- unresolved diagnostic tasks;
- restart-unclear tasks;
- tasks with material human approval complexity.

## Expansion Triggers

Switch from `compact` to `expanded` when any of these appears:

- blockers;
- traceability need;
- governance escalation;
- unresolved contradictions;
- version conflict;
- evidence dispute;
- reviewer uncertainty;
- human approval complexity.

## Compact Finalization Shape

For compact execution, finalization can be sufficient with:

- approved `review.md`;
- final artifact;
- current `task-manifest.md` with governance/current-state fields updated;
- optional short handoff only if the next owner needs it.

Do not create extra summary, checklist, or duplicated final notes unless a
conditional artifact rule requires them.

## Pipeline Decision

Pipelines were not redesigned. Only wording that made finalization handoff or
finalization proof artifacts appear unconditionally required was adjusted.

## Template Decision

Execution profile is now explicit in:

- orchestration plan;
- task manifest;
- final decision.

This makes compact execution auditable without creating a new workflow layer.
