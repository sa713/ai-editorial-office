# Implementation Notes

## Existing feedback loop points

Already present before P5.5:

- `ai-editorial-office/AGENTS.md` allowed optional post-delivery
  `feedback.md` and explicitly said no user reaction means no feedback artifact.
- `kb/feedback_loop.md` described a lightweight post-delivery feedback flow.
- `kb/feedback_patterns.md` owned recurring or significant feedback pattern
  tracking, not raw feedback storage.
- `templates/artifacts/feedback_template.md` existed as task-local optional
  feedback guidance.
- `chief_editor.md` already owned post-delivery feedback decisions.
- `tests/feedback_loop_*` contained synthetic/manual feedback-loop checks.

## Integration choice

P5.5 was integrated into the existing mechanism instead of creating a second
one:

- new active workflow: `kb/customer_feedback_loop.md`;
- old `kb/feedback_loop.md`: compatibility pointer for existing references and
  task-pack read sets;
- existing `feedback_template.md`: updated to the P5.5 structure and
  classification;
- existing `chief_editor` and `final_editor`: minimally updated with role
  consequences;
- existing `feedback_loop_smoke_test.md`: updated as the smoke fixture.

`engineering_watchlist.md` is connected as a decision-gated engineering
observation log. `feedback_patterns.md` remains the place for recurring feedback
patterns when Chief Editor decides that pattern tracking is useful.

## Why no new agent

The workflow has only two responsibilities:

- raw capture after a result, which can be done by `final_editor` when still in
  handoff context;
- classification and governance routing, which already belongs to
  `chief_editor`.

Adding a Feedback Agent would duplicate Chief Editor governance, add a role for
a small optional artifact, and increase the risk that feedback becomes a
parallel review or automatic system-change path.

## Production files changed

- `ai-editorial-office/kb/customer_feedback_loop.md`
- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/kb/feedback_loop.md`
- `ai-editorial-office/kb/feedback_patterns.md`
- `ai-editorial-office/templates/artifacts/feedback_template.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/final_editor.md`
- `ai-editorial-office/tests/feedback_loop_smoke_test.md`
- `ai-editorial-office/ideas/master_backlog.md`

## Non-goals preserved

- No new agent or role.
- No review-gate change.
- No lifecycle validator change.
- No task pack generator change.
- No mandatory `feedback.md`.
- No automatic watchlist/backlog mutation.
- No CRM, metrics, or satisfaction scoring.
