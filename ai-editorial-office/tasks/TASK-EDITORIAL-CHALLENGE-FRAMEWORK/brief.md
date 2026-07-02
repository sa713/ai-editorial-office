# Brief

## task title

Editorial Challenge Framework design.

## user goal

Refine the Editorial Challenge design so Review Agent tests the assumptions
behind Chief Editor and Writer Agent decisions, without rewriting, re-routing,
or becoming a second Chief Editor.

## expected artifact

- Design-only proposal.
- No production edits.
- No new roles.
- No new mandatory production artifacts.
- Clear mechanism for assumptions-based, evidence-backed challenge inside
  existing review.

## source boundary

Use the current AI Editorial Office architecture:

- `AGENTS.md`;
- `agents/chief_editor.md`;
- `agents/review_agent.md`;
- `agents/writer_agent.md`;
- `pipelines/review_pipeline.md`;
- `templates/tasks/review_task_template.md`;
- `kb/forbidden_patterns.md`.

## constraints

- Preserve role separation.
- Preserve review-gate and deterministic outcomes.
- Do not make Reviewer a Writer or Chief Editor.
- Do not increase review cycles by default.
- Do not allow preference-only objections.
- Challenge must test whether route-validity assumptions still hold.
