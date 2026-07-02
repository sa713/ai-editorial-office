# Design Note: User Feedback Loop

## lifecycle placement

Feedback appears after `chief_editor final governance decision` as an optional post-delivery capture step:

```text
final decision -> optional post-delivery feedback capture
```

This step does not reopen a task automatically, does not downgrade the completed result retroactively, and does not change the canonical task status model.

## owner and timing

- Owner: `chief_editor`, because feedback routing touches lifecycle, task-local governance evidence, and system-change boundaries.
- Timing: only after the user reacts to a delivered result.
- Optionality: feedback capture is optional. No reaction means no `feedback.md`.

## storage

- Task-local feedback lives in `/tasks/TASK-ID/feedback.md`.
- `feedback.md` is created only when post-delivery user reaction exists.
- A reusable scaffold lives in `ai-editorial-office/templates/artifacts/feedback_template.md`.
- Repeating/systemic patterns live in `ai-editorial-office/kb/feedback_patterns.md`.

`ai-editorial-office/kb/feedback_patterns.md` is preferred over `editorial_knowledge/feedback_patterns.md` because the file is operational process knowledge: it governs how feedback signals accumulate before system changes. `editorial_knowledge/` remains better suited to writing quality, usefulness, modes, and failure examples.

## task feedback vs system signal

Task feedback records what the user said about one result: acceptance, praise, revision need, rejection, unclear reaction, or mixed reaction.

System signal is only a cautious classification that the feedback might reveal a recurring quality issue. A single item may be marked as a possible signal, but it does not become policy.

Required principle:

```text
Один feedback не меняет систему автоматически.
One feedback does not change the system automatically.
```

## pattern threshold

The escalation ladder is:

```text
single feedback ↓ repeated signal ↓ validated pattern ↓ system change proposal ↓ separate reviewed system update
```

- Single feedback: recorded in `feedback.md` only.
- Repeated signal: similar feedback appears across more than one task, or one severe issue is clearly process-relevant.
- Validated pattern: review confirms it is not merely taste, one-off preference, or task-specific misunderstanding.
- System change proposal: recorded as a proposed future update, not applied directly.
- Separate reviewed system update: any rule/process change requires its own task, review, and final decision.

## revision boundary

If the user asks for changes after delivery, the system distinguishes:

- feedback as quality evidence;
- a new task for a new request or broadened scope;
- bounded revision of the current task only when existing rules allow it.

## files proposed to change

- `ai-editorial-office/AGENTS.md`: minimal lifecycle principle only.
- `ai-editorial-office/agents/chief_editor.md`: role-specific responsibility to capture optional feedback and route patterns.
- `ai-editorial-office/agents/review_agent.md`: review check that feedback loop did not bypass review or mutate governance.
- `ai-editorial-office/templates/artifacts/feedback_template.md`: new optional task-local artifact scaffold.
- `ai-editorial-office/kb/feedback_patterns.md`: new system journal for recurring/significant patterns only.
- `ai-editorial-office/kb/00_index.md`: short index entry for the new KB file.

## files not to change

- `ai-editorial-office/kb/task_statuses.md`
- `ai-editorial-office/pipelines/*.md`
- `ai-editorial-office/templates/tasks/*.md`
- old `TASK-*` folders
- visual subsystem files and prompts
- governance model or review-gate definitions beyond a short post-delivery note
