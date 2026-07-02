# Step 6 Rollback Notes

## Rollback Scope

Rollback Step 6 by restoring only these files from the pre-Step-6 state:

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `about/project_tree.md`
- `ai-editorial-office/pipelines/article_pipeline.md`
- `ai-editorial-office/pipelines/social_pipeline.md`
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/pipelines/research_pipeline.md`

The Step 6 retrospective files may be kept as historical notes or removed if the
whole step is reverted.

## Do Not Roll Back

- Do not change Step 1 artifact-depth normalization unless separately requested.
- Do not change Step 2 context-loading profile unless separately requested.
- Do not change Step 3 role compression unless separately requested.
- Do not change Step 4 template compression unless separately requested.
- Do not change Step 5 compact execution unless separately requested.

## Validation After Rollback

Verify:

- `review.md` remains mandatory;
- task manifest still has any pre-existing current-version pointer fields from
  Step 2 if Step 6 alone is rolled back selectively;
- no version registry, automation, database, sync engine, or document-management
  framework remains;
- pipelines still use the short restart path.
