# Implementation plan

Step 005 scope: add minimal review heuristics for author-facing diagnosis to `editorial_knowledge/40_editorial_review_system.md`.

Plan:

1. Review the existing `author_concept_diagnosis` conceptual block.
2. Add a compact authorship check for reviewing author-facing diagnosis output.
3. Keep the check mode-specific and bounded.
4. Preserve guardrails against `Premature Solution Substitution`.
5. Do not create a review stage, workflow, pipeline change, template change, scoring, maturity review, or coaching session.
6. Record changed files, decisions, safety checks, rollback notes, and the local diff.

Out of scope:

- New review stage.
- Separate workflow.
- Pipeline or template changes.
- Scoring.
- Maturity review.
- Coaching or ideation methodology.
- Steps 006-007 of `system-maintenance-retrospective-0007`.
