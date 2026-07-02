# Rollback Notes

## Rollback Scope

Rollback this step by removing the visual branch activation block from:

- `ai-editorial-office/AGENTS.md`

Also remove the Step 2 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011-1/step-002/`

## Expected Effect Of Rollback

Rollback would keep Artist Agent legality from Step 1, but remove explicit guidance for:

- when to activate the visual branch;
- when not to activate it;
- Chief Editor activation ownership;
- compact visual path;
- Artist Agent ban outside the activated visual branch.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the activation block and the Step 2 retrospective folder. Do not edit Artist Agent, visual templates, pipelines, review system, comic files, or presentation files during rollback.

## Post-Rollback Check

After rollback, verify:

- `AGENTS.md` still contains Step 1 Artist Agent legality if Step 1 remains;
- the visual branch activation block no longer appears;
- no new pipeline, mode, workflow, comic branch, or presentation branch remains.
