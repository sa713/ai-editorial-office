# Task Manifest

## task identity

Task ID: `TASK-0002`

Task title: `AI tools getting in the way of team work`

Task type: `article`

Active pipeline: `/pipelines/article_pipeline.md`

Risk mode: `standard`

Risk mode selected by: `chief_editor`

Risk mode rationale: Normal article request with likely factual and causal claims; unresolved audience, publication scope, examples, and factual sensitivity prevent `low-risk`, while no explicit high-governance trigger has been supplied.

Risk mode controls artifact depth and review strictness. Standard mode requires research and claim traceability before writing because factual claims are likely.

## current state

Current status: `finalized`

Current stage: `closed test run`

Current owner role: `chief_editor`

Latest completed stage: `test closure`

Next required role: `none`

Next required action: none inside TASK-0002; future system development continues separately.

Latest handoff: `/tasks/TASK-0002/handoff-rereview-review-agent-to-chief-editor-or-finalization.md`

Current blockers: none; task is closed as a successful system test run.

## governance state

Review required: `yes`

Review outcome: `approved`

Finalization status: `not_started intentionally`

Final governance status: `closed as system test, not article governance approval`

Human approval required: `not_applicable for test closure`

Publication/delivery approval: `not_granted`

## artifact inventory

| Artifact | Owner | Stage | State | Required now | Notes |
| --- | --- | --- | --- | --- | --- |
| `brief.md` | `intake_agent` | intake | `present` | yes | Normalized raw brief and uncertainties. |
| `task-manifest.md` | `chief_editor` | all | `present` | yes | Compact current state. |
| `status.md` | `chief_editor` | all | `present` | yes | Status/history updated through orchestration. |
| `open-questions.md` | `research_agent` | research | `present` | yes | Updated writing blockers and deferred questions. |
| `handoff-intake-intake-agent-to-chief-editor.md` | `intake_agent` | intake | `present` | yes | Compact transfer to Chief Editor. |
| `orchestration_plan.md` | `chief_editor` | orchestration | `present` | yes | Execution contract. |
| `handoff-orchestration-chief-editor-to-next-role.md` | `chief_editor` | orchestration | `present` | yes | Transfer to Research Agent. |
| `research.md` | `research_agent` | research | `present` | yes | Compact synthesis and use guidance. |
| `sources.md` | `research_agent` | research | `present` | yes | Source traceability. |
| `facts.md` | `research_agent` | research | `present` | yes | Fact-level evidence map. |
| `claims_table.md` | `research_agent` | research | `present` | yes | Allowed/caveated/blocked claim guidance. |
| `handoff-research-research-agent-to-chief-editor.md` | `research_agent` | research | `present` | yes | Transfer back to Chief Editor. |
| `planning-notes.md` | `chief_editor` | planning | `present` | yes | Clarification decision and writing constraints. |
| `handoff-planning-chief-editor-to-user-or-writer.md` | `chief_editor` | planning | `present` | yes | Transfer to Writer Agent. |
| `outline.md` | `writer_agent` | writing | `present` | yes | Constrained article structure. |
| `draft.md` | `writer_agent` | writing | `present` | yes | Non-final article draft. |
| `writer-notes.md` | `writer_agent` | writing | `present` | yes | Assumptions, caveats, and avoided claims. |
| `claims-used.md` | `writer_agent` | writing | `present` | yes | Maps draft claims to `claims_table.md`. |
| `handoff-writing-writer-agent-to-review-or-chief-editor.md` | `writer_agent` | writing | `present` | yes | Transfer to Review Agent. |
| `review.md` | `review_agent` | review | `present` | yes | Verdict and actionable findings. |
| `qa-checklist.md` | `review_agent` | review | `present` | yes | Standard-mode review checklist. |
| `handoff-review-review-agent-to-chief-editor-or-final-editor.md` | `review_agent` | review | `present` | yes | Transfer after review verdict. |
| `handoff-revision-writer-agent-to-review-agent.md` | `writer_agent` | revision | `present` | yes | Bounded revision transfer back to Review Agent. |
| `handoff-rereview-review-agent-to-chief-editor-or-finalization.md` | `review_agent` | review | `present` | yes | Approved re-review transfer to Chief Editor. |
| `retrospective.md` | `chief_editor` | retrospective | `present` | yes | Test-run retrospective. |
| `final.md` | `final_editor` | finalization | `intentionally_not_created` | no | Article finalization was not run. |
| `final_decision.md` | `chief_editor` | governance | `intentionally_not_created` | no | Governance/publication decision was not performed. |

## active constraints

- TASK-0002 is closed as a system test run, not as a finalized or published article.
- Approved draft remains in `draft.md`.
- `final.md` was intentionally not created.
- `final_decision.md` was intentionally not created.
- Publication approval was not granted.
- Future system development must happen outside TASK-0002.
- Do not invent audience, publication scope, examples, claims, sources, or internal context.
- Use only allowed or caveated claims from `claims_table.md`; blocked claims must not enter the draft.
- Generic workflow scenarios must be labeled hypothetical unless sourced or user-supplied.
- Draft language is Russian; audience is constrained to general professional readers who work in or with teams.
- Publication channel remains unknown and must not be implied.
- Review gate remains mandatory before any final material.

## open questions

| Question | Blocks next action | Owner | Status |
| --- | --- | --- | --- |
| Who is the target audience? | no for constrained writing | `chief_editor` or user | `deferred: general professional readers only` |
| What is the publication channel and internal/external scope? | no for draft; yes before finalization/publication approval | `chief_editor` or user | `deferred` |
| Should examples be generic scenarios or sourced/supplied real workflows? | no for generic examples; yes if real examples are required | `chief_editor` or user | `deferred: generic hypothetical only` |
| What factual claim standard is required? | no; standard traceability exists | `chief_editor` | `partly answered` |

## next action packet

No next action inside TASK-0002.

For future reading, key files are:

- `/tasks/TASK-0002/draft.md`;
- `/tasks/TASK-0002/review.md`;
- `/tasks/TASK-0002/retrospective.md`;
- `/tasks/TASK-0002/status.md`.

Expected outputs: none.

Forbidden outputs:

- `final.md`;
- `final_decision.md`;
- any invented examples or claims.

Validation before handoff:

- `draft.md` has review approval.
- `final.md` is absent intentionally.
- `final_decision.md` is absent intentionally.
- Publication approval is not granted.
- TASK-0002 is closed as a test run.

## lifecycle notes

- User explicitly requested intake only for TASK-0002.
- `intake-notes.md` was not created because the user specified the bootstrap artifact set and artifact minimalism favors the listed downstream-consumed files.
- Chief Editor completed orchestration and routed to research rather than writing to avoid unsupported claims and silent ambiguity resolution.
- Research Agent completed compact evidence base and handed back to Chief Editor; research does not approve writing readiness by itself.
- Chief Editor chose constrained writing over user clarification to avoid clarification overkill while preserving uncertainty boundaries.
- Writer Agent completed constrained writing artifacts and handed off to Review Agent; the draft is not approved or final.
- Review Agent completed independent review and requested two local wording changes; no blocker, research return, or finalization was created.
- Writer Agent completed only the requested bounded revision and handed back to Review Agent.
- Review Agent completed bounded re-review and approved the draft for next-stage routing; this is not finalization or publication approval.
- Chief Editor closed TASK-0002 as a successful test run of the system. No finalization, final governance decision, or publication approval was performed.
