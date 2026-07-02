# Task Manifest

## task identity

Task ID: `TASK-0003`

Task title: `Announcement for internal magazine issue 13`

Task type: `social`

Active pipeline: `/pipelines/social_pipeline.md`

Risk mode: `low-risk`

Risk mode selected by: `chief_editor`

Risk mode rationale: Internal short announcement using user-supplied context only; no sensitive claims, no exact numbers invented, review gate retained.

## current state

Current status: `finalized`

Current stage: `governance`

Current owner role: `chief_editor`

Latest completed stage: `final governance`

Next required role: `none`

Next required action: compact handoff to user

Latest handoff: `/tasks/TASK-0003/handoff-governance-chief-editor-to-user.md`

Current blockers: none

## governance state

Review required: `yes`

Review outcome: `approved`

Finalization status: `complete`

Final governance status: `complete`

Human approval required: `no for local delivery`

Publication/delivery approval: `local delivery complete; publication approval not requested`

## artifact inventory

| Artifact | Owner | Stage | State | Required now | Notes |
| --- | --- | --- | --- | --- | --- |
| `brief.md` | `intake_agent` | intake | `present` | yes | Intake summary, intent, constraints. |
| `task-manifest.md` | `chief_editor` | all | `present` | yes | Compact state. |
| `status.md` | `chief_editor` | all | `present` | yes | Status history. |
| `orchestration_plan.md` | `chief_editor` | planning | `present` | yes | Pipeline and artifact scope. |
| `outline.md` | `writer_agent` | structure-from-intent | `present` | yes | Proposed structure. |
| `draft.md` | `writer_agent` | writing | `present` | yes | Three variants. |
| `writer-notes.md` | `writer_agent` | writing | `present` | yes | Writing decisions. |
| `review.md` | `review_agent` | review | `present` | yes | Variant review and approval after bounded revision. |
| `qa-checklist.md` | `review_agent` | review | `present` | yes | Tone and governance checks. |
| `review-summary.md` | `review_agent` | review | `present` | yes | Concise review transfer. |
| `bounded-revision.md` | `writer_agent` | changes_requested | `present` | yes | Selected version revision. |
| `final.md` | `final_editor` | finalization | `present` | yes | Final announcement text. |
| `finalization-notes.md` | `final_editor` | finalization | `present` | yes | Finalization validation. |
| `final_decision.md` | `chief_editor` | governance | `present` | yes | Final governance decision. |
| handoffs | stage owners | transitions | `present` | yes | Role transfers recorded. |

## active constraints

- Do not invent exact number, names, link, or contact details.
- Do not publish final text in chat; provide compact handoff only.
- Preserve role separation and review-gate evidence.
- Keep final text short and non-corporate.

## open questions

| Question | Blocks next action | Owner | Status |
| --- | --- | --- | --- |
| none | no | none | not_applicable |

## next action packet

Read first:

- `/tasks/TASK-0003/final.md`;
- `/tasks/TASK-0003/review-summary.md`;
- `/tasks/TASK-0003/final_decision.md`;
- `/tasks/TASK-0003/handoff-governance-chief-editor-to-user.md`.

Required inputs:

- none.

Expected outputs:

- compact handoff in chat.

Forbidden outputs:

- full final announcement text in chat;
- new draft variants in chat.

Validation before handoff:

- `final.md` exists.
- `review.md` verdict is approved.
- `final_decision.md` status is finalized.
