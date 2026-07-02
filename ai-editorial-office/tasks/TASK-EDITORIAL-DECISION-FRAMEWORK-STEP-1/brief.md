# Brief

## task title

Editorial Decision Framework, step 1.

## user goal

Design the smallest architecture-compatible change that makes editorial
reasoning visible before the main deliverable is written.

## expected output

- Proposed change description.
- Files that would be changed in a future implementation.
- New files proposed, if any.
- Lifecycle change.
- Rationale for why the proposal is better than current behavior.
- Final `git status --short`.

## constraints

- Do not change existing production agents, pipelines, templates, or processes in
  this step.
- Preserve AI Editorial Office philosophy: minimum entities, no duplication,
  existing architecture, compatibility with all task types.
- Prefer existing artifacts unless a new artifact is clearly necessary.

## source boundary

Use the current repository architecture as source material:

- `AGENTS.md`;
- active agent specs under `agents/`;
- pipeline contracts under `pipelines/`;
- artifact templates under `templates/artifacts/`;
- relevant KB and project state files.

## success criteria

- The proposal identifies where the editorial decision should happen.
- The responsible role is clear.
- Artifact choice is justified.
- Inputs and outputs of the decision step are explicit.
- Writer and Reviewer integration are clear.
- The proposal avoids unnecessary new entities.
