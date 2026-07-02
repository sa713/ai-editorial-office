# Step 5 Rollback Notes

## Rollback Scope

Rollback Step 5 by restoring only these files from the pre-Step-5 state:

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/pipelines/article_pipeline.md`
- `ai-editorial-office/pipelines/social_pipeline.md`
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/artifacts/final_decision_template.md`

The Step 5 retrospective files may be kept as historical notes or removed if the
whole step is reverted.

## Do Not Roll Back

- Do not change agent specs as part of Step 5 rollback.
- Do not change task templates.
- Do not remove Step 1 artifact-depth normalization unless a separate rollback
  asks for it.
- Do not remove Step 2 context-loading profile unless a separate rollback asks
  for it.
- Do not remove Step 3-4 compression unless a separate rollback asks for it.

## Validation After Rollback

Verify:

- `review.md` remains mandatory;
- high-governance workflow remains full/expanded;
- task manifest still has current-version pointer from Step 2;
- optional artifacts from Step 1 remain conditional;
- no new workflow, agent, pipeline, or automation remains from Step 5.
