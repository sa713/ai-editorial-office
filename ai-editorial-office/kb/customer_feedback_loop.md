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

Observed completed-work outcomes without a user/customer reaction are not
customer feedback. Route material future-use outcomes directly through
`editorial_learning_framework.md`.

Create task-local `feedback.md` only when feedback actually exists. No feedback
means no feedback artifact.

## Processing Chain

```text
task result
-> customer feedback
-> optional task-local feedback.md
-> Chief Editor classification
-> evidence and scope check when future use is claimed
-> task-local action / preference signal / Knowledge Evolution disposition /
   watchlist proposal / backlog or system-change candidate
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

## Classification And Learning Disposition

Feedback classification answers what the reaction means and what immediate
route is safe. It does not decide what becomes reusable learning.

When a feedback item has a material future-use claim, apply
`editorial_learning_framework.md` after classification. Record the smallest
supported Knowledge Evolution disposition. `rejected` and `deferred` are
learning dispositions, not new feedback classifications.

Default bridge:

| Feedback classification | Usual learning disposition |
| --- | --- |
| `task_local` | `task_local` |
| `preference` | `task_local` or scoped `learning_candidate` |
| `observation` | `learning_candidate`, `deferred`, or `rejected` |
| `confirmed_pattern` | `pattern_candidate` |
| `system_change_candidate` | `canon_update_candidate` or `deferred` |

Chief Editor may choose a smaller disposition. No mapping is automatic.

## Evidence And Scope Check

Before routing feedback beyond the current task or scoped preference, identify:

- exact or faithfully paraphrased source signal;
- evidence pointer and actual observed outcome, if any;
- affected artifact, user/client preference, role, pipeline, template,
  KB/canonical owner, Domain Pack, validation, or memory area;
- applicability and non-applicability;
- corroborating, contradicting, or similar known signals;
- confidence, unknowns, and evidence still needed;
- proposed owner, bounded action, and review path.

Strong sentiment is not pattern evidence. Repetition is useful only when the
signals are comparable and indicate the same underlying condition. One
anecdote normally remains task-local, is rejected, or is deferred. A high-
impact exception still needs strong evidence, bounded applicability, owner,
and review and cannot promote itself.

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

System-change candidates should be bounded through the existing
`system_change_proposal_template.md` or a compact equivalent. Name the affected
canonical owner, evidence and counterevidence, expected effect, smallest change,
validation, side effects, and stop or correction path. The proposal is not
implementation or prioritization authority.

## Guardrails

- One feedback item does not change the system.
- Negative feedback is not automatically a system failure.
- A user preference does not become a global rule automatically.
- Feedback loop does not bypass review-gate.
- Feedback loop does not replace review.
- Feedback loop does not rewrite production rules.
- System changes require a separate reviewed system update.
- Raw feedback stays task-local; KB/watchlist entries must be summarized.
- Feedback classification does not automatically select learning disposition.
- `rejected` and `deferred` signals do not enter pattern or canon stores unless
  new evidence causes a reviewed reclassification.
- Feedback does not change a Domain Pack, `/about`, model behavior, roadmap, or
  backlog automatically.

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
