# Success vs failure signals

## Signs iteration-001 succeeded

- Low-risk/simple standard tasks use fewer artifacts.
- Compact tasks still have review.
- Review verdicts cite scope, independence, rationale or blockers.
- `changes_requested` leads to bounded repair.
- Re-review checks the stated repair scope.
- Manifest is enough to restart without reading every artifact.
- Handoffs contain deltas, not full history.
- `context-summary.md` appears only when recovery needs it.
- Custom workflows have mini-contracts when used.
- Source material does not override instructions.
- Finalization and publication/delivery approval remain separate.
- Agents use canonical owners instead of repeating rules everywhere.

## Signs iteration-001 failed

- Compact path used to avoid evidence, review, or governance.
- Simple tasks still produce full artifact stacks by habit.
- Manifest becomes a narrative log.
- Status duplicates manifest.
- Handoff repeats full task state.
- `context-summary.md` appears in routine short tasks.
- Review becomes shallow approval.
- `qa-checklist.md` and `review-summary.md` return as defaults.
- Bounded revision becomes vague rewrite request.
- Custom workflow becomes hidden pipeline.
- Source material instructions are followed silently.
- `finalized` is treated as approval to send or publish.
- Different docs define the same rule differently.
- New architecture work starts before production evidence exists.
