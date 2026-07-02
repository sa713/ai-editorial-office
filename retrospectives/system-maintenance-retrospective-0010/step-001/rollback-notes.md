# Rollback Notes

## Rollback Scope

Rollback this step by reverting changes in:

- `ai-editorial-office/AGENTS.md`;
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`;
- the five touched pipeline files;
- the five touched role spec files;
- the five touched task scaffold files.

Also remove the Step 1 retrospective folder if the implementation itself is rolled back.

## Expected Effect Of Rollback

Rollback would restore the previous heavier artifact defaults, including:

- stronger pressure to create `qa-checklist.md` and `review-summary.md` for standard review;
- stronger pressure to create `finalization-checklist.md` for standard finalization;
- scaffold pressure to create `open-questions.md` even when empty;
- less explicit warning against copying legacy heavy task folders.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, restore from the pre-step project snapshot. Do not delete task history folders or generated task artifacts during rollback.

## Post-Rollback Check

After rollback, verify:

- `review.md` is still mandatory;
- governance and human approval rules still exist;
- no partial wording remains that contradicts the restored artifact policy.
