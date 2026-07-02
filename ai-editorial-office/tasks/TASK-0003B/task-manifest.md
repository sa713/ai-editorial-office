# Task Manifest

## task identity

Task ID: `TASK-0003B`

Task title: `Depth revision for internal magazine announcement`

Task type: `social`

Active pipeline: `/pipelines/social_pipeline.md`

Risk mode: `low-risk`

Risk mode selected by: `chief_editor`

Risk mode rationale: Follow-up bounded revision of internal announcement using supplied facts only; main risk is tonal, not factual.

Follow-up to: `/tasks/TASK-0003/`

## current state

Current status: `finalized`

Current stage: `governance`

Current owner role: `chief_editor`

Latest completed stage: `final governance`

Next required role: `none`

Next required action: compact handoff to user

Latest handoff: `/tasks/TASK-0003B/handoff-governance-chief-editor-to-user.md`

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
| `brief.md` | `intake_agent` | intake | `present` | yes | Follow-up feedback and quality task. |
| `task-manifest.md` | `chief_editor` | all | `present` | yes | Compact state. |
| `status.md` | `chief_editor` | all | `present` | yes | Status history. |
| `orchestration_plan.md` | `chief_editor` | planning | `present` | yes | TASK-0003 pipeline preserved. |
| `outline.md` | `writer_agent` | structure-from-intent | `present` | yes | New restrained-based structure. |
| `draft.md` | `writer_agent` | writing | `present` | yes | Three variants. |
| `writer-notes.md` | `writer_agent` | writing | `present` | yes | Writing decisions. |
| `review.md` | `review_agent` | review | `present` | yes | Expanded review and bounded re-review. |
| `qa-checklist.md` | `review_agent` | review | `present` | yes | Tone and governance checks. |
| `review-summary.md` | `review_agent` | review | `present` | yes | Review transfer. |
| `bounded-revision.md` | `writer_agent` | changes_requested | `present` | yes | Selected version revision. |
| `final.md` | `final_editor` | finalization | `present` | yes | Final announcement text. |
| `finalization-notes.md` | `final_editor` | finalization | `present` | yes | Finalization validation. |
| `final_decision.md` | `chief_editor` | governance | `present` | yes | Final governance decision. |
| handoffs | stage owners | transitions | `present` | yes | Role transfers recorded. |

## active constraints

- Use the restrained TASK-0003 version as the base.
- Do not write final text in chat.
- Do not add facts, names, exact number, links, or interview details.
- Preserve low synthetic tone over polished editorial beauty.

## open questions

| Question | Blocks next action | Owner | Status |
| --- | --- | --- | --- |
| none | no | none | not_applicable |

## next action packet

Read first:

- `/tasks/TASK-0003B/final.md`;
- `/tasks/TASK-0003B/review-summary.md`;
- `/tasks/TASK-0003B/final_decision.md`;
- `/tasks/TASK-0003B/handoff-governance-chief-editor-to-user.md`.

Required inputs:

- none.

Expected outputs:

- compact handoff in chat.

Forbidden outputs:

- full final announcement text in chat;
- new versions in chat.

Validation before handoff:

- `final.md` exists.
- `review.md` verdict is approved.
- `final_decision.md` status is finalized.
