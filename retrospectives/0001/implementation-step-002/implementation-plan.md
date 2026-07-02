# Implementation plan

Step executed: Step 2 only, Compact path implementation.

## Changed files

## `ai-editorial-office/AGENTS.md`

- Why: canonical owner for process-level invariants and review-gate boundaries.
- What changed: added `Process depth` section defining `compact`, `normal`, and `full`; added compact allow/deny rules; stated compact path is not a new pipeline and never removes review.
- Why safe: lifecycle, statuses, roles, review-gate, and governance semantics were not changed.

## `ai-editorial-office/agents/chief_editor.md`

- Why: Chief Editor selects risk mode and orchestration depth.
- What changed: added short note that Chief Editor selects process depth inside selected pipeline; compact is forbidden for high-governance and requires rationale, review target, and intentionally omitted artifacts.
- Why safe: this clarifies an existing orchestration responsibility without adding a new role or workflow.

## `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

- Why: orchestration plan is where process depth should be recorded.
- What changed: added compact `process depth` section with depth, rationale, compact allow check, review target, and intentionally omitted artifacts.
- Why safe: template remains a planning scaffold; no manifest freshness, governance block, status changes, or review behavior were added.

## `ai-editorial-office/pipelines/article_pipeline.md`

- Why: it contained a stale note saying compact artifact path was future/not automatic.
- What changed: replaced that line with a compact process depth note tied to Chief Editor rationale, review target, and omitted artifacts.
- Why safe: no article lifecycle, required stages, or review requirements changed.

## `ai-editorial-office/project-state.md`

- Why: current normalization decisions had the same stale future/not automatic note.
- What changed: updated it to reflect compact process depth as available only inside a selected pipeline with Chief Editor rationale and no review-gate removal.
- Why safe: current state note only; no permanent policy moved out of `AGENTS.md`.

## Explicit non-changes

- No new compact pipeline.
- No manifest freshness block.
- No governance block.
- No review behavior expansion.
- No status model changes.
- No new agents.
- No broad pipeline rewrite.
