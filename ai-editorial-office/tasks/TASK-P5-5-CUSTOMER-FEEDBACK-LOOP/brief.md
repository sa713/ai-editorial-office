# Brief

## task

Implement P5.5 - Customer Feedback Loop as a compact system update for the
editorial office.

## goal

Add a lightweight workflow for customer feedback after a task result so feedback
is not lost in chat and does not automatically become a system change.

## scope

- Add `kb/customer_feedback_loop.md`.
- Update existing feedback guidance/template instead of creating a parallel
  mechanism.
- Update `chief_editor` and `final_editor` minimally.
- Update `kb/00_index.md` and P5.5 in `ideas/master_backlog.md`.
- Add or update a lightweight smoke/manual check.

## constraints

- Do not add new agents or roles.
- Do not change review-gate, lifecycle validator, or task pack generator.
- Do not make `feedback.md` mandatory for every task.
- Do not automatically update watchlist or backlog from feedback.
- Do not turn a single feedback item or user preference into a global rule.
- Do not touch unrelated backlog items.

## acceptance

- Workflow covers classification:
  `task_local`, `preference`, `observation`, `confirmed_pattern`,
  `system_change_candidate`.
- Task-local `feedback.md` guidance exists and remains optional.
- Feedback loop is owned by existing roles.
- Engineering watchlist connection is explicit and decision-gated.
- Guardrails and sanitized examples are present.
- Backlog P5.5 is marked implemented.
- Implementation notes and check-pack are created.
