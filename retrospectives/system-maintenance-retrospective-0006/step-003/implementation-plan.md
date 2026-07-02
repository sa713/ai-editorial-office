# Implementation plan

## Scope

Add minimal review heuristics for detecting `Defensive Diagnostic Drift` to `editorial_knowledge/40_editorial_review_system.md`.

## Steps

1. Inspect the existing review-system guidance for `diagnostic_analysis`.
2. Add compact bounded heuristics inside the existing diagnostic pass.
3. Keep the guidance mode-specific and limited to relevant diagnostic-analysis tasks.
4. Verify that no new review stage, workflow, scoring, confidence matrix, or formal audit was introduced.
5. Record changed files, decisions, safety notes, rollback notes, and the diff in this step folder.

## Non-goals

- No new review stage.
- No separate diagnostic workflow.
- No pipeline changes.
- No template changes.
- No scoring.
- No confidence matrix.
- No formal evidence logic.
- No full review-system rewrite.
- No rollback of Artificial Concept Completion safeguards.
- No weakening of diagnostic discipline.
