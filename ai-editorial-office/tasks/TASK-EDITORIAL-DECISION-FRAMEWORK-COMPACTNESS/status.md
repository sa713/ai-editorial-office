# Status

## current state

Status: `review_ready`

The compactness normalization was applied to production instructions. Writer
Agent and UX Writer were not edited in this pass.

## changed in production

- `AGENTS.md`: added compactness norm and lifecycle wording.
- `agents/chief_editor.md`: tightened Chief Editor ownership, handoff, and
  quality checks.
- `agents/review_agent.md`: added bloated/duplicative frame checks.
- `templates/artifacts/orchestration_plan_template.md`: specified short
  alternative format and long-rationale boundary.
- `templates/artifacts/handoff_template.md`: kept planning transfer short and
  limited rejected alternatives to names or one-line reasons.

## not changed in this pass

- `agents/writer_agent.md`
- `agents/ux_writer.md`

These files remain modified in the worktree from the earlier implementation
step, but this compactness pass did not edit them.

## validation

- Full requested diff saved to `production-diff.md`.
- `git status --short` captured for final response.
