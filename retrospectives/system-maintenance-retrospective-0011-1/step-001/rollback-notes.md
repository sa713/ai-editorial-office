# Rollback Notes

## Rollback Scope

Rollback this step by reverting changes in:

- `ai-editorial-office/AGENTS.md`;
- `ai-editorial-office/pipelines/article_pipeline.md`;
- `ai-editorial-office/pipelines/social_pipeline.md`;
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`;
- `ai-editorial-office/pipelines/research_pipeline.md`;
- `ai-editorial-office/pipelines/review_pipeline.md`.

Also remove the Step 1 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011-1/step-001/`

## Expected Effect Of Rollback

Rollback would restore the previous conflict:

- `artist_agent.md` would still exist;
- `AGENTS.md` and pipelines would again treat non-MVP roles as fully forbidden;
- Artist Agent would no longer be clearly legal for illustration-to-text tasks.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually restore only the previous role-policy and pipeline guardrail wording. Do not delete `artist_agent.md`, visual templates, review-system guidance, comic files, or presentation files as part of this rollback.

## Post-Rollback Check

After rollback, verify:

- `AGENTS.md` no longer contains the Artist Agent extension legalization;
- pipelines no longer contain the explicitly legalized extension-role exception;
- `artist_agent.md` remains unchanged if Step 6 of update 0011 remains;
- no new agents, pipelines, comics, or presentations were created.
