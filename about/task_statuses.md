# Task State Model

This file defines the canonical state model for local AI editorial tasks.

It is designed for markdown workflows where each task lives in:

```text
/tasks/TASK-ID/
```

Each active task should maintain its current state in:

```text
/tasks/TASK-ID/status.md
```

The model is intentionally simple. Agents must prefer explicit state changes over implicit progress hidden in chat history.

## allowed statuses

Use only these task statuses unless `AGENTS.md` is updated.

| Status | Meaning | Owner |
| --- | --- | --- |
| `intake` | Task exists, but scope, audience, format, or acceptance criteria are still being clarified. | Intake Agent or Chief Editor |
| `research` | Facts, sources, context, and open questions are being collected. | Research Agent |
| `planning` | Structure, angle, thesis, and production plan are being defined. | Chief Editor |
| `writing` | Draft or UX copy is being written from approved brief, research, product context, and plan. | Writer Agent or UX Writer |
| `ux-writing` | Optional explicit UX writing status alias when a UX pipeline needs to distinguish product-facing copy from article/social drafting. | UX Writer |
| `editing` | Optional revision checkpoint or status bridge; not required in the current operating model and not a separate Editor Agent role. | Writer Agent or UX Writer |
| `review` | Independent review is in progress. | Review Agent |
| `changes_requested` | Review found issues that must be fixed before approval. | Writer Agent, UX Writer, or Research Agent |
| `approved` | Review passed. The material may be finalized. | Review Agent |
| `human_approval_required` | A human decision is required before finalization or continuation. | User or Chief Editor |
| `finalized` | Final approved artifact exists and the task is complete. | Chief Editor |
| `blocked` | Work cannot safely continue because of missing data, conflict, or unresolved risk. | Current agent |
| `failed` | Task cannot be completed under current constraints. | Chief Editor |
| `archived` | Task is closed and no longer active. | Chief Editor or user |

## status transitions

Allowed forward transitions:

| From | Allowed next statuses |
| --- | --- |
| `intake` | `research`, `planning`, `blocked`, `failed`, `archived` |
| `research` | `planning`, `blocked`, `failed` |
| `planning` | `writing`, `ux-writing`, `research`, `blocked`, `failed` |
| `writing` | `review`, `editing`, `research`, `blocked`, `failed` |
| `ux-writing` | `review`, `editing`, `research`, `blocked`, `failed` |
| `editing` | `review`, `writing`, `blocked`, `failed` |
| `review` | `approved`, `changes_requested`, `blocked`, `human_approval_required`, `failed` |
| `changes_requested` | `writing`, `editing`, `research`, `review`, `blocked`, `failed` |
| `approved` | `human_approval_required`, `finalized`, `archived` |
| `human_approval_required` | `finalized`, `changes_requested`, `blocked`, `failed`, `archived` |
| `finalized` | `archived` |
| `blocked` | `intake`, `research`, `planning`, `writing`, `ux-writing`, `editing`, `review`, `human_approval_required`, `failed`, `archived` |
| `failed` | `archived`, `intake` |
| `archived` | none |

Backward transitions are allowed only when they are explicit and documented. Example: `review` may return to `research` if a factual gap is discovered.

## Default writing-to-review rule

In the current operating model, `writing` -> `review` is an explicitly valid direct transition. The direct transition is valid when:

- required writing artifacts exist;
- the latest handoff from `writer_agent` to `review_agent` or from `ux_writer` to `review_agent` exists;
- for article tasks, `outline.md`, `draft.md`, `writer-notes.md`, and `claims-used.md` exist when applicable;
- for social tasks, `draft.md`, `writer-notes.md`, and `claims-used.md` exist when applicable;
- for UX writing tasks, `ux-copy.md`, `content-map.md`, `states-table.md`, `terminology-notes.md`, and `ux-writer-notes.md` exist when applicable;
- `review required` is `yes` in `status.md`, `orchestration_plan.md`, or the relevant pipeline contract;
- no separate Editor Agent is used or required.

If a task uses `ux-writing` as its operational status or as a local stage label in a handoff, template, or orchestration note, `ux-writing` -> `review` has the same default validity as `writing` -> `review`, provided the required UX writing artifacts and `ux_writer` to `review_agent` handoff exist.

`editing` is optional in the current operating model. It may be used as a revision checkpoint or status bridge after review findings or before review readiness, but it must not be treated as a required stage. `editing` does not imply a separate Editor Agent in the current operating model. Writer Agent or UX Writer may hand off directly to Review Agent after required artifacts are created.

Every transition must update `status.md` with:

- previous status;
- new status;
- reason for transition;
- responsible role;
- next expected action;
- relevant artifacts.

## blocked states

Use `blocked` when continuation would create unreliable, unverifiable, or non-compliant work.

Common blocked reasons:

- missing `brief.md`;
- missing or invalid `TASK-ID`;
- conflicting instructions;
- missing required source material;
- contradictory sources on a material point;
- unavailable required KB or pipeline;
- role boundary violation;
- attempt to bypass review;
- writer asked to approve their own work;
- unresolved legal, ethical, factual, or editorial risk.

When setting `blocked`, the agent must write the blocker in `status.md`:

```markdown
Status: blocked
Blocked reason: ...
Blocking files or instructions: ...
Responsible role: ...
Smallest decision needed: ...
Recommended next status after resolution: ...
```

Blocked tasks must not move directly to `finalized`. They must return to the correct production or review state first.

## review states

Review uses `review`, `changes_requested`, and `approved`.

Review rules:

- `review` means independent evaluation is in progress.
- `changes_requested` means the material is not approved and must be revised.
- `approved` means deterministic review passed and the material may proceed to finalization.

Review verdicts inside `review.md` must be one of:

- `approved`;
- `changes_requested`;
- `blocked`.

Mapping from review verdict to task status:

| Review verdict | Task status |
| --- | --- |
| `approved` | `approved` |
| `changes_requested` | `changes_requested` |
| `blocked` | `blocked` |

The task must not enter `approved` if:

- `review.md` is missing;
- reviewer and writer are the same role instance;
- critical issues remain open;
- required inputs were not checked;
- review did not list checked artifacts.

## escalation states

Escalation is not always a separate status. Use the smallest status that accurately describes the task.

Use `blocked` when an agent cannot proceed without a decision.

Use `human_approval_required` when the next step is a human editorial, strategic, legal, reputational, or publishing decision.

Escalation must be recorded in `status.md`:

```markdown
Escalation type: user | chief-editor | reviewer | subject-matter-expert
Escalation reason: ...
Decision needed: ...
Options: ...
Risk of proceeding without decision: ...
```

Escalation examples:

- user must choose between conflicting angles;
- Chief Editor must resolve a scope conflict;
- Review Agent requires additional evidence;
- subject-matter expert must verify a high-risk factual claim.

## human approval states

Use `human_approval_required` when the system has done its work but a human must approve the next action.

Typical cases:

- final publication requires user approval;
- material contains sensitive claims;
- editorial direction affects brand, policy, or legal exposure;
- the brief requires manual approval;
- a previous human decision is ambiguous or missing.

Human approval outcomes:

| Human decision | Next status |
| --- | --- |
| Approved for finalization | `finalized` |
| Approved with changes | `changes_requested` |
| Needs more research | `research` |
| Needs rewrite | `writing` |
| Cannot decide yet | `blocked` |
| Cancel task | `failed` or `archived` |

Human approval must be documented in `status.md` or `approval.md`. If approval is verbal or external, the agent must summarize it and mark it as user-provided.

## retry policy

Retries are allowed when a failed step can be corrected without changing the task goal.

Retryable cases:

- incomplete draft;
- missing handoff;
- formatting error;
- recoverable source gap;
- review issues that can be addressed;
- context fragmentation that can be repaired with `context-summary.md`.

Non-retryable without escalation:

- unresolved instruction conflict;
- impossible factual requirement;
- missing human decision;
- request to bypass review;
- repeated failure caused by unclear brief.

Retry rules:

- after the first failure, document the issue and retry once;
- after the second failure on the same issue, set `blocked` or escalate;
- after three failed attempts on the same production stage, set `failed` unless the user or Chief Editor changes constraints;
- each retry must preserve previous artifacts or create a versioned file.

Recommended retry note:

```markdown
Retry count: 1
Failed stage: writing
Reason: ...
Change made before retry: ...
Previous artifact: draft-v1.md
New artifact: draft-v2.md
```

## failed task policy

Use `failed` only when the task cannot be completed under current constraints.

Valid failed reasons:

- task goal is impossible;
- required evidence does not exist or cannot be accessed;
- user cancels the task after work has started;
- constraints conflict and no resolution is available;
- repeated retries fail without new information;
- task would require violating `AGENTS.md`.

When setting `failed`, create or update:

```text
/tasks/TASK-ID/failure.md
```

`failure.md` must include:

- final status;
- reason for failure;
- stages completed;
- files created;
- unresolved blockers;
- what would be needed to restart;
- whether any artifacts remain reusable.

A failed task may return to `intake` only if the user or Chief Editor changes the brief, constraints, or available inputs.

## archival policy

Use `archived` when the task should no longer appear in active work.

Archival is allowed from:

- `finalized`;
- `failed`;
- `approved`, if finalization is intentionally skipped;
- `human_approval_required`, if the user cancels or defers indefinitely;
- `blocked`, if the blocker will not be resolved.

Before archiving, ensure `/tasks/TASK-ID/` contains:

- `brief.md`, if the task passed intake;
- `status.md`;
- key production artifacts;
- `review.md`, if review occurred;
- `final.md`, if finalized;
- `failure.md`, if failed;
- final handoff or archive note.

Recommended archive note:

```text
/tasks/TASK-ID/archive.md
```

`archive.md` should include:

- archive reason;
- final status before archive;
- reusable artifacts;
- unresolved risks;
- date or local timestamp, if available;
- responsible role.

Archived tasks are read-only by default. Reopening an archived task requires a new status transition to `intake` and a note explaining why the task is being reopened.

## minimal status.md format

Every task should keep `status.md` short and current:

`status.md` is the detailed status/history artifact. It must not become a duplicate of `task-manifest.md`, handoff files, orchestration plans, or stage artifacts. If an artifact is omitted because risk mode or downstream consumption does not justify it, record the rationale briefly in `status.md`, `task-manifest.md`, or `orchestration_plan.md`.

```markdown
# Status

Task ID: TASK-ID
Current status: intake | research | planning | writing | ux-writing | editing | review | changes_requested | approved | human_approval_required | finalized | blocked | failed | archived
Previous status: ...
Responsible role: ...
Last completed stage: ...
Next action: ...

## Reason for current status

...

## Key artifacts

- brief.md
- research.md
- draft.md
- review.md

## Blockers or approvals

...

## Transition log

| From | To | Role | Reason |
| --- | --- | --- | --- |
```
