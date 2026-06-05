# Feedback Loop Synthetic Examples

These examples are synthetic. They are not task materials and do not contain
real user, client, source, or task data.

## Purpose

Check whether post-delivery feedback is classified without turning one reaction
into a system rule.

## Examples

### Example 1 - Task-local note

User says:

> Финальный текст норм, только заголовок был слабоват.

Expected classification: `task-local note`

Why:

- This is a single minor reaction.
- It can be recorded in task-local `feedback.md` if useful.
- It does not justify a system change.

Must not:

- change `AGENTS.md`;
- update pipelines;
- create a feedback pattern from one comment.

### Example 2 - Bounded revision

User says:

> Перепиши второй абзац, он слишком канцелярский.

Expected classification: `bounded revision`

Why:

- The user asks for a concrete change to the delivered artifact.
- The follow-up is task-local and bounded.
- It does not become a new system rule.

Must not:

- treat the request as a global tone policy;
- reopen unrelated tasks;
- skip review if revised material needs review.

### Example 3 - Possible pattern

User says repeatedly across multiple tasks:

> Ты снова начал с лишнего корпоративного вступления.

Expected classification: `possible system pattern`

Why:

- The signal repeats across tasks.
- It may be summarized in `feedback_patterns.md`.
- It still needs validation before a system update.

Must not:

- dump raw feedback into KB;
- change writing rules immediately;
- create a new required role.

### Example 4 - System change proposal

Multiple reviews show:

> Review Agent repeatedly misses that final.md was created before approved review.

Expected classification: `system change proposal`

Why:

- This is a repeated governance failure.
- It may require a proposal and separate reviewed system update.
- The proposal itself does not change production files.

Must not:

- patch production rules without review;
- weaken review-gate;
- treat the proposal as accepted by default.
