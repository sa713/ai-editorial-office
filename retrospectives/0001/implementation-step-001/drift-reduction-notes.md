# Drift reduction notes

## Reduced duplication

- `project-state.md` no longer restates the full architecture principles list.
- `project-state.md` no longer restates full risk-mode definitions.
- `project-state.md` no longer carries a separate primary responsibility map for artifacts.
- `kb/00_index.md` now clarifies KB scope instead of leaving it implicit.

## Kept unchanged to avoid behavior drift

- `AGENTS.md` existing invariants.
- Review-gate requirements.
- Status names and transitions.
- Pipelines.
- Agent specs.
- Artifact templates.
- Editorial knowledge.

## Redesign risks avoided

- Did not create a new ownership framework outside `AGENTS.md`.
- Did not create a new workflow behavior.
- Did not add new statuses or new task artifacts.
- Did not convert templates into policy documents.

## Remaining known drift risk

Existing pipelines, task templates, and agent specs still contain repeated lifecycle and artifact guidance. This step did not clean those because doing so broadly would risk Step 2+ behavior changes or pipeline rewrite.
