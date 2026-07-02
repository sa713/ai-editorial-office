# Task Manifest

## task identity

Task ID: `TASK-0004`

Task title: `Task Exchange Instruction Review`

Task type: `editorial-review`

Active pipeline: `/pipelines/review_pipeline.md`

Risk mode: `standard`

Risk mode selected by: `chief_editor`

Risk mode rationale: Internal operational instruction with process rules, role ownership, and possible user-action misunderstanding. No external publication or sensitive factual claims.

## current state

Current status: `finalized`

Current stage: `governance`

Current owner role: `chief_editor`

Latest completed stage: `final governance decision`

Next required role: `none`

Next required action: `deliver compact handoff`

Latest handoff: `/tasks/TASK-0004/compact-handoff.md`

Current blockers: `none`

## governance state

Review required: `yes`

Review outcome: `approved`

Finalization status: `complete`

Final governance status: `complete`

Human approval required: `no`

Publication/delivery approval: `not_required`

## artifact inventory

| Artifact | Owner | Stage | State | Required now | Notes |
| --- | --- | --- | --- | --- | --- |
| `brief.md` | `intake_agent` | intake | present | yes | task normalized from user request |
| `status.md` | `chief_editor` | all | present | yes | detailed state history |
| `orchestration_plan.md` | `chief_editor` | planning | present | yes | review/revision path |
| `draft.md` | `writer_agent` | writing | present | yes | revised instruction candidate |
| `review.md` | `review_agent` | review | present | yes | approved with residual friction noted |
| `qa-checklist.md` | `review_agent` | review | present | yes | required by user and standard review depth |
| `review-summary.md` | `review_agent` | review | present | yes | concise outcome |
| `final.md` | `final_editor` | finalization | present | yes | final revised instruction |
| `final_decision.md` | `chief_editor` | governance | present | yes | governance closure |
| `compact-handoff.md` | `chief_editor` | governance | present | yes | user-facing handoff source |

## active constraints

- Do not answer the instruction task directly in chat; deliver only compact handoff after completion.
- Preserve operational clarity, sequence integrity, and action hierarchy.
- Do not turn the instruction into HR, marketing, motivational, or editorialized communication.
- Use `/tasks/TASK-0004/source-draft.md` as the primary source.

## open questions

| Question | Blocks next action | Owner | Status |
| --- | --- | --- | --- |
| Exact platform UI labels and workflow statuses beyond the supplied draft | no | product owner | deferred |
| Definition of `Инициатива` as separate from `Идея` | no | product owner | deferred; removed from final terms to avoid unsupported distinction |

## next action packet

Read first:

- `/tasks/TASK-0004/final.md`;
- `/tasks/TASK-0004/review-summary.md`;
- `/tasks/TASK-0004/final_decision.md`.

Required inputs:

- none.

Expected outputs:

- compact handoff only.

Forbidden outputs:

- full revised instruction in chat;
- essay-style review in chat.

Validation before handoff:

- final instruction exists;
- review verdict is approved;
- final decision is finalized.

## lifecycle notes

- Source file has docx/zip structure despite `.md` extension; text was extracted with `pandoc -f docx -t markdown`.
- Current structure was not critically broken; revision kept the main source structure and repaired local usefulness issues.
