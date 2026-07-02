# Rollback notes

Rollback scope:

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/project-state.md`
- `ai-editorial-office/agents/chief_editor.md`
- changed `ai-editorial-office/pipelines/*.md`
- changed `ai-editorial-office/kb/*.md`
- `ai-editorial-office/templates/agent_template.md`
- Step 2 report files under `retrospectives/system-maintenance-retrospective-0012/step-002/`

Safe rollback approach:

1. Restore the changed active policy files from the pre-Step-2 version or apply a reverse patch from the Step 2 diff.
2. Remove the Step 2 report directory only if the Step 2 audit trail should also be rolled back.
3. Re-run the active-policy search for the old `MVP` terminology if the rollback is intended to return to the previous state.

Behavioral rollback impact:

- No data migration is involved.
- No task artifacts need migration.
- No role files other than `chief_editor.md` changed.
- No pipeline stage order changed, so rollback is terminology-only.

Important caution:

- Do not partially roll back only `AGENTS.md` or only pipelines. The role-admissibility vocabulary must remain consistent across governance, Chief Editor, pipelines, KB, and the agent template.
