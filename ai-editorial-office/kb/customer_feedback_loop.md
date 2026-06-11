# Customer Feedback Loop

## Purpose

Handle customer feedback after a task result without losing it in chat and
without turning it into an automatic system change.

This workflow does not replace review, final governance, production rules,
`feedback_patterns.md`, `engineering_watchlist.md`, or any selected pipeline.

## When to Use

Use this workflow when a user or customer reacts to a delivered task result and
the reaction may need task-local action, future preference tracking, engineering
observation, or backlog consideration.

Do not use it for internal review findings, anticipated reactions, ordinary
status updates, pre-delivery comments, or general roadmap ideas unrelated to a
delivered task.

Create task-local `feedback.md` only when feedback actually exists. No feedback
means no feedback artifact.

## Processing Chain

```text
task result
-> customer feedback
-> optional task-local feedback.md
-> Chief Editor classification
-> task-local action / preference signal / watchlist proposal / backlog candidate
```

## Roles

- `final_editor` may capture raw post-result feedback when it appears in the
  finalization or delivery context, then route it to `chief_editor`.
- `chief_editor` owns classification, decision boundaries, and whether any
  follow-up is task-local, a preference, a watchlist proposal, or a backlog
  candidate.

No Feedback Agent is added.

## Classification

- `task_local` - affects only the current task. It may mean no action, a
  bounded revision, clarification, or a new task if scope changed.
- `preference` - a customer preference. It may inform future task handling when
  relevant, but it is not a global rule.
- `observation` - a weak signal. It may justify proposing an
  `engineering_watchlist.md` entry after a decision.
- `confirmed_pattern` - a repeated or validated signal. It may become a backlog
  candidate.
- `system_change_candidate` - a candidate for a separate reviewed system update.
  It does not change production by itself.

## Watchlist and Backlog

```text
observation -> propose watchlist entry
confirmed_pattern -> may become backlog candidate
system_change_candidate -> separate reviewed system update
```

Do not write automatically to `engineering_watchlist.md`. Chief Editor must
decide that the signal is useful as an engineering observation.

Use `feedback_patterns.md` when the decision is to track a recurring feedback
pattern across tasks. Use `engineering_watchlist.md` when the signal is an
engineering or system-process observation. Neither file is a raw feedback
archive.

Do not move everything to backlog. `engineering_watchlist.md` is an observation
log, not a task list. A backlog candidate needs repeated evidence, significance,
or a separate explicit decision.

## Guardrails

- One feedback item does not change the system.
- Negative feedback is not automatically a system failure.
- A user preference does not become a global rule automatically.
- Feedback loop does not bypass review-gate.
- Feedback loop does not replace review.
- Feedback loop does not rewrite production rules.
- System changes require a separate reviewed system update.
- Raw feedback stays task-local; KB/watchlist entries must be summarized.

## Examples

### Too long

Feedback: "Too long."

Classification: `task_local`.

Decision: shorten only the current artifact if the user asks for revision, or
record the note with no system change.

### Always shorter

Feedback: "I always want this shorter and without hype."

Classification: `preference`.

Decision: record as a customer preference, not a global editorial rule.

### Source status missed again

Feedback: "This is the third time source status was not accounted for."

Classification: `confirmed_pattern`, possibly `system_change_candidate`.

Decision: consider a watchlist/backlog candidate, then use a separate reviewed
system update before changing production rules.
