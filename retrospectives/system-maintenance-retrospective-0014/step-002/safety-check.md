# Safety Check

## Scope Check

Only Step 2, `Codex Entry Bootstrap`, was implemented.

## Rule Placement

The root `AGENTS.md` contains only a bootstrap rule. It does not duplicate the
full editorial charter and points to `ai-editorial-office/AGENTS.md` as the
active rule owner.

## Non-Regression Check

No changes were made to:

- visual branch rules;
- Artist Agent rules;
- review system;
- pipelines;
- existing task outputs.

## Direct Production Guard

The root bootstrap explicitly blocks direct `PDF -> SVG/PNG/MD` production for
editorial `TASK-*` work unless the user explicitly asks to bypass the editorial
process.

## Expected Next-Request Behavior

A request mentioning `TASK-0019` must trigger the root bootstrap first, then
load `ai-editorial-office/AGENTS.md`, then start the editorial entry flow before
technical work.
