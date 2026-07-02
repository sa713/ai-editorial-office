# Rollback notes

## Full rollback

To fully rollback Step 2:

1. Remove `Process depth` from `ai-editorial-office/AGENTS.md`.
2. Remove the process-depth note and decision-boundary bullet from `ai-editorial-office/agents/chief_editor.md`.
3. Remove the `process depth` section from `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`.
4. Restore the prior low-risk line in `ai-editorial-office/pipelines/article_pipeline.md`.
5. Restore the prior current normalization decision in `ai-editorial-office/project-state.md`.

## Partial rollback

If compact path causes governance or review confusion:

- keep `normal` and `full`;
- suspend `compact` by changing AGENTS to say compact is not available until a later iteration;
- keep omitted-artifact rationale as a general artifact minimalism rule.

If orchestration plans become too long:

- reduce the template section to:
  - Depth;
  - Rationale;
  - Artifacts intentionally omitted.

If article pipeline wording drifts:

- replace the article-specific compact note with a reference to `AGENTS.md` and the orchestration template.

## Rollback safety

Rollback does not require changing task folders, statuses, agent set, review verdicts, or templates outside `orchestration_plan_template.md`.
