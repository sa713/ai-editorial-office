# Rollback notes

## Full rollback

To fully rollback Step 5:

1. Remove compact review minimum, normal/full distinction, and bounded revision paragraph from `review_agent.md`.
2. Restore Review Agent outputs to the previous always-listed review artifact set if desired.
3. Remove compact review minimum and bounded revision text from `review_pipeline.md`.
4. Restore review pipeline completion conditions that required `qa-checklist.md`, `review-summary.md`, and `reviewer-notes.md` unconditionally.
5. Remove bounded revision note from `AGENTS.md`.
6. Remove Step 5 normalization note from `project-state.md`.

## Partial rollback

If compact review becomes too thin:

- keep compact review, but require separate `qa-checklist.md` for standard tasks.

If bounded revision hides deeper issues:

- keep bounded fields, but add a stronger escalation note after repeated failed repair.

If separate artifact omission causes confusion:

- keep `review-summary.md` conditional but require it whenever the next role is not Chief Editor.

## Rollback safety

Rollback does not require changing lifecycle, statuses, governance state, compact path, agent set, or existing task folders.
