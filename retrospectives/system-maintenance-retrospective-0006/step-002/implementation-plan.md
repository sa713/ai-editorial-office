# Implementation plan

## Scope

Add one observable editorial failure pattern, `Defensive Diagnostic Drift`, to `editorial_knowledge/50_editorial_failure_patterns.md`.

## Steps

1. Inspect the existing failure pattern structure.
2. Add the new pattern after `Artificial Concept Completion`.
3. Keep the pattern short, operational, reviewable, and repair-oriented.
4. Verify that uncertainty, hypotheses, and previous diagnostic guardrails remain allowed.
5. Record changed files, decisions, safety notes, rollback notes, and the diff in this step folder.

## Non-goals

- No pipeline changes.
- No template changes.
- No review system rewrite.
- No confidence framework.
- No scoring.
- No formal evidence logic.
- No rollback of Artificial Concept Completion safeguards.
- No step 3 from `system-maintenance-retrospective-0006`.
- No tone or style discussion.
