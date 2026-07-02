# Brief

## task title

Problem Hypothesis Framework design refinement.

## user goal

Refine the minimal AI Editorial Office design so Chief Editor records a
professional hypothesis about the problem a request appears to address, without
claiming to know the user's true problem.

## expected artifact

- Design-only proposal.
- No production edits.
- No new roles.
- No large mandatory documents.
- Clear answer on lifecycle, artifacts, reviewer validation, hypothesis
  language, and governance boundaries.

## source boundary

Use the current production architecture:

- `AGENTS.md`
- `agents/chief_editor.md`
- `agents/review_agent.md`
- `templates/artifacts/orchestration_plan_template.md`
- `templates/artifacts/handoff_template.md`

The current Editorial Decision Frame work is relevant context because the new
problem-hypothesis step must feed it without duplicating it.

## constraints

- Preserve architecture.
- Prefer existing artifacts.
- Keep the mechanism compact.
- Do not make the editorial office argue with the user by default.
- Separate stated user intent from source-backed or editorially inferred
  problem hypotheses.
- Do not imply that the editorial office knows the user's real problem.
