# Implementation plan

Step executed: Step 5 only, Review ergonomics and bounded revision.

## Changed files

## `ai-editorial-office/agents/review_agent.md`

- Why: Review Agent owns detailed review behavior and artifact content.
- What changed: added compact review minimum, normal/full distinction, bounded revision fields, and conditional review artifact guidance.
- Why safe: review remains mandatory; verdict model and lifecycle are unchanged.

## `ai-editorial-office/pipelines/review_pipeline.md`

- Why: Review Pipeline owns sequencing, artifact depth, and quality gates.
- What changed: added compact review minimum at pipeline level; made `qa-checklist.md`, `review-summary.md`, and `reviewer-notes.md` conditional in completion conditions; added bounded revision requirement for `changes_requested`.
- Why safe: no new review workflow, no scoring, no status changes.

## `ai-editorial-office/AGENTS.md`

- Why: AGENTS owns review-gate invariants.
- What changed: added a short bounded revision note under Review-gate.
- Why safe: keeps review mandatory and prevents unbounded rewrite from `changes_requested`.

## `ai-editorial-office/project-state.md`

- Why: current normalization decisions should reflect Step 5.
- What changed: added note that compact review may keep checklist/summary inside `review.md` when minimum evidence exists.
- Why safe: current-state note only.

## Explicit non-changes

- No lifecycle change.
- No compact path semantic change.
- No governance model change.
- No scoring/eval system.
- No new agents.
- No approval workflow.
- No review engine.
- No automatic QA.
