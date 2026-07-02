# Compact path decisions

## Decisions implemented

- `compact`, `normal`, and `full` are process depth values, not pipelines.
- Process depth operates inside the selected pipeline.
- `normal` is the default when compact is not clearly safe and full is not required.
- `full` is required for high-governance, source-heavy, sensitive, multi-audience, or high factual sensitivity work.
- Compact path is allowed only for low-risk or simple standard source-light tasks.
- Compact path is explicitly forbidden for high-governance.
- Compact path never removes review-gate.
- Compact path may reduce or combine supporting artifacts only with recorded rationale.
- Intentionally omitted artifacts must be named with one-line rationale.
- Chief Editor selects process depth during orchestration.
- Orchestration plan records depth, rationale, compact allow check, review target, and omitted artifacts.

## Decisions intentionally not implemented

- No compact pipeline.
- No compact review redesign.
- No manifest freshness.
- No governance state block.
- No status transitions.
- No changes to review verdicts.
- No new task artifacts.
- No bulk pipeline updates.

## Pipeline decision

Only `article_pipeline.md` was touched because it had stale wording that would conflict with Step 2. Other pipelines already had low-risk artifact-depth notes and did not require a Step 2 change.
