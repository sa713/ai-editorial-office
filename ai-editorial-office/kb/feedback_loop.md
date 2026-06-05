# Feedback Loop

## Purpose

Provide practical guidance for handling post-delivery user feedback without
turning one reaction into a system rule.

This guidance does not override `AGENTS.md`, role specs, pipelines, task
artifacts, review-gate, or final governance decisions.

## Signal ladder

```text
single feedback
↓
repeated signal
↓
validated pattern
↓
system change proposal
↓
reviewed system update
```

## What feedback can become

- task-local note;
- bounded revision;
- new task;
- possible system pattern.

Chief Editor classifies the feedback before any follow-up starts.

## What feedback must not do

- automatically reopen a task;
- automatically change `AGENTS.md`, pipelines, roles, templates, or KB;
- become a new rule after one comment;
- pollute KB with raw feedback;
- bypass review-gate or final governance.

## When to record feedback.md

Create task-local `feedback.md` only when the user actually responds to a
delivered result.

Use it to capture:

- what the user said;
- whether the reaction is acceptance, praise, revision request, rejection,
  mixed, or unclear;
- whether follow-up is none, bounded revision, clarification, new task, or
  possible system-pattern watch;
- why the feedback does not automatically reopen the task or change the system.

Do not create `feedback.md` for every internal note, ordinary status update, or
anticipated reaction.

## When to update feedback_patterns.md

Update `/kb/feedback_patterns.md` only when feedback suggests a repeated or
significant signal worth tracking across tasks.

Examples:

- similar user reactions appear across multiple tasks;
- review repeatedly catches the same process failure;
- a task-local note appears to reflect a broader editorial habit;
- the signal is important enough to watch even before it is validated.

Do not copy raw feedback dumps into KB. Summarize the pattern, sources, why it
may be system-relevant, and the next review needed.

## When to create system_change_proposal.md

Create a system change proposal only when a pattern is repeated, significant, or
validated enough to justify a separate system update discussion.

Use `templates/artifacts/system_change_proposal_template.md`.

A proposal may recommend changing rules, roles, pipelines, templates, KB, tests,
or validators, but it does not change them by itself.

## Review and governance

Production changes happen only through a separate reviewed system update.

Before changing production files:

- confirm the pattern is not a one-off preference;
- define the proposed change and non-goals;
- list files and roles likely affected;
- review risks and possible regressions;
- preserve review-gate and role boundaries;
- keep optional artifacts optional unless a reviewed system update says
  otherwise.
