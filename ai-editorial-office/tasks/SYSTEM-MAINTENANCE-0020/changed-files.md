# Changed Files

## task-local artifacts

| File | Change | Reason |
| --- | --- | --- |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/task-manifest.md` | Created | Current-state pointer for this system task |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/orchestration_plan.md` | Created | Compact maintenance mini-contract |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/status.md` | Created and updated | Status and transition history |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/design-note.md` | Created | Required pre-change design note |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/changed-files.md` | Created | Traceability for this update |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/diff.md` | Created | Requested task-local diff for selected system files |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/pilot-feedback-examples.md` | Created | Demonstration of old-task feedback handling without old-task mutation |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/review.md` | Created | Review gate for this system update |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0020/final_decision.md` | Created | Chief Editor final governance decision |

## system files

| File | Change | Reason |
| --- | --- | --- |
| `ai-editorial-office/AGENTS.md` | Minimal update | Added optional post-delivery feedback capture, artifact ownership, and anti-self-modification ladder |
| `ai-editorial-office/agents/chief_editor.md` | Minimal update | Added Chief Editor responsibility and boundaries for optional feedback capture |
| `ai-editorial-office/agents/review_agent.md` | Minimal update | Added review checks for feedback-loop system updates |
| `ai-editorial-office/templates/artifacts/feedback_template.md` | Created | Optional task-local `feedback.md` scaffold |
| `ai-editorial-office/kb/feedback_patterns.md` | Created | System journal for recurring/significant feedback patterns only |
| `ai-editorial-office/kb/00_index.md` | Minimal update | Indexed `feedback_patterns.md` ownership |

## files intentionally not changed

- `ai-editorial-office/kb/task_statuses.md`
- `ai-editorial-office/pipelines/*.md`
- `ai-editorial-office/templates/tasks/*.md`
- old `TASK-*` folders
- visual subsystem files and prompts
- governance model beyond the narrow post-delivery principle

## implementation notes

- No new roles were created.
- No new pipeline was created.
- `feedback.md` is optional, not a required lifecycle artifact.
- `feedback_patterns.md` is not a raw feedback archive.
- One feedback item does not change system rules automatically.
