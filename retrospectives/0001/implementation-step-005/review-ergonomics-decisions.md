# Review ergonomics decisions

## Decisions implemented

- Compact review has minimum evidence:
  - verdict;
  - reviewed artifact or artifact set;
  - lightweight independence check;
  - usefulness/pass rationale or blocking issues;
  - governance note when relevant;
  - one clear next action.
- Normal review may use separate `qa-checklist.md` or `review-summary.md` when downstream routing, risk, or review depth needs them.
- Full review is reserved for high-governance or source-heavy work.
- Separate `qa-checklist.md`, `review-summary.md`, and `reviewer-notes.md` are conditional, not always required.
- Review remains mandatory before finalization.
- Review Agent remains reviewer, not final authority.

## Decisions intentionally not implemented

- No numeric scoring.
- No eval system.
- No automatic QA.
- No review engine.
- No approval workflow.
- No new verdicts.
- No new agents.
