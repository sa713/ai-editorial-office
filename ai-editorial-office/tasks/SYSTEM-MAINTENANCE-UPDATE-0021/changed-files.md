# Changed Files

## task-local artifacts

| File | Change | Reason |
| --- | --- | --- |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/task-manifest.md` | Created | Current-state pointer |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/orchestration_plan.md` | Created | Compact maintenance contract |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/status.md` | Created and updated | State history |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/design-note.md` | Created | Required pre-change design note |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/changed-files.md` | Created | Traceability for this update |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/diff.md` | Created | Diff of changed system files |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/pilot-preflight-examples.md` | Created | Demonstrates ASK/CONSTRAIN/PROCEED/BLOCK |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/review.md` | Created | Compatibility review |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-UPDATE-0021/final_decision.md` | Created | Chief Editor final decision |

## system files

| File | Change | Reason |
| --- | --- | --- |
| `ai-editorial-office/AGENTS.md` | Minimal update | Added compact Preflight Gate principle before production |
| `ai-editorial-office/agents/chief_editor.md` | Minimal update | Added Chief Editor preflight responsibility and boundaries |
| `ai-editorial-office/agents/intake_agent.md` | Minimal update | Added intake support for preflight inputs without making Intake the gate owner |
| `ai-editorial-office/templates/artifacts/orchestration_plan_template.md` | Minimal update | Added compact preflight block to an existing artifact template |

## files intentionally not changed

- `ai-editorial-office/kb/task_statuses.md`
- `ai-editorial-office/pipelines/*.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/agents/final_editor.md`
- `ai-editorial-office/templates/tasks/*.md`
- visual subsystem files
- old `TASK-*` folders

## implementation notes

- No new role was created.
- No new pipeline was created.
- No new mandatory standalone artifact was created.
- Preflight records a decision; it does not force a user question.
- Review-gate, governance, and task status model were not changed.
