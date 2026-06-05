# Feedback Loop Acceptance Trial

This is a synthetic/sanitized manual trial. It is not a real task folder and
does not contain real working materials.

## Purpose

Check how the Feedback Loop guidance classifies a sanitized post-delivery
reaction when the user accepts the result, praises it, and gives a preference
for future work without asking to change the current artifact.

## Trial status

- Synthetic/sanitized trial only.
- Not a task artifact.
- No real tasks, teams, clients, documents, source files, or people are used.

## Raw feedback

> После финального текста пользователь говорит: "Да, теперь хорошо. В следующий
> раз давай сразу делать короче и без вводного абзаца".

This scenario is synthetic/sanitized and does not describe a real delivered
artifact.

## Compared examples

- Task-local note example: primary match, because the feedback is a single
  reaction after delivery and does not request immediate artifact changes.
- Bounded revision example: contrast, because the user does not ask to rewrite
  the current artifact.
- Possible pattern example: weak watch, because "в следующий раз" may become a
  repeated preference if similar feedback appears again.
- System change proposal example: negative contrast, because one future
  preference is not enough to propose a system update.

## Classification

Expected classification: `task-local note + future preference watch`

Why:

- The user accepts the result: "теперь хорошо".
- There is no request to revise the current artifact.
- "В следующий раз" is a future preference, not a bounded revision.
- "Сразу делать короче и без вводного абзаца" may become a pattern watch only
  if similar evidence repeats.
- One feedback item is not enough for a KB pattern or system change proposal.

## Expected next action

- Create task-local `feedback.md` only if this were a real task.
- Mark the delivered artifact as accepted if the task state supports acceptance
  recording.
- Do not revise the current artifact unless the user explicitly requests it.
- Do not update `feedback_patterns.md` from one future preference unless
  repeated evidence exists.
- Do not create `system_change_proposal.md`.
- Do not change production rules.

## What should not happen

- should not reopen task automatically;
- should not create bounded revision without explicit current-artifact change
  request;
- should not update `AGENTS.md`;
- should not update pipelines;
- should not add raw feedback to KB;
- should not create system change proposal from one future preference;
- should not create real task materials.

## Decision

Manual trial result: feedback loop is useful.

The guidance separates acceptance and future preference from a current-artifact
revision request.

## Need for validator

Lightweight validator is not needed yet.

Recommendation:

- feedback examples are enough for now to distinguish acceptance/future
  preference from bounded revision;
- run one more trial on repeated governance failure or move to a lightweight
  validator decision.
