# Step 4 Rollback Notes

## Rollback Scope

Rollback Step 4 by restoring only the files under:

```text
ai-editorial-office/templates/**/*.md
```

Files changed:

- `ai-editorial-office/templates/agent_template.md`
- `ai-editorial-office/templates/artifacts/final_decision_template.md`
- `ai-editorial-office/templates/artifacts/handoff_template.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `ai-editorial-office/templates/artifacts/status_template.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/tasks/article_task_template.md`
- `ai-editorial-office/templates/tasks/research_task_template.md`
- `ai-editorial-office/templates/tasks/review_task_template.md`
- `ai-editorial-office/templates/tasks/social_task_template.md`
- `ai-editorial-office/templates/tasks/ux_writing_task_template.md`

The Step 4 retrospective files may be kept as historical notes or removed if the
whole step is reverted.

## Do Not Roll Back

- Do not modify `AGENTS.md` as part of Step 4 rollback.
- Do not modify pipelines.
- Do not modify agent specs.
- Do not change governance model, review-gate, task status model, or MVP agent
  set.
- Do not reintroduce Step 1-3 changes unless a separate rollback requests them.

## Validation After Rollback

Verify:

- all original template files exist;
- no new templates or workflow layers were added;
- `review.md` remains required;
- current-version pointer remains available for version-heavy tasks;
- governance-critical fields are still present.
