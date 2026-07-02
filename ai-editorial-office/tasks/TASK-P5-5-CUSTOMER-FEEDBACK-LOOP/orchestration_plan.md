# Orchestration Plan

## task summary

- Task ID: `TASK-P5-5-CUSTOMER-FEEDBACK-LOOP`
- User goal: implement P5.5 Customer Feedback Loop.
- Deliverable: compact production patch plus local review packet.
- Audience/channel: local editorial office system maintainers.
- Current active version: this P5.5 patch.

## task classification

- Task type: system update / workflow refinement.
- Risk mode: `standard`.
- Factual sensitivity: low; governance sensitivity is moderate because role and
  artifact rules are touched.
- Human approval likely required: yes.
- Rationale: changes production guidance, but no external factual claims.

## selected pipeline

- Pipeline: compact governed system-update mode.
- Why this pipeline: existing content pipelines create deliverables; this task
  changes editorial workflow guidance and must preserve governance.
- Pipeline exceptions or local constraints: no new pipeline, role, validator, or
  required artifact.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: user supplied explicit source files, allowed changes, forbidden
  changes, acceptance criteria, and review packet format.
- Production may start: yes.
- If `constrain`: keep changes inside P5.5 files and do not modify validators or
  task pack generator.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | `chief_editor` | yes | Routing, classification owner, backlog decision. |
| Capture | `final_editor` | conditional | Records raw post-result feedback when it appears in finalization context. |
| Review | user / external review | yes | User requested no commit/push before review. |

No Feedback Agent is added.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | restart / review | Required by editorial entry flow. |
| `orchestration_plan.md` | required | restart / review | Records compact system-update routing. |
| `status.md` | required | restart / review | Records state changes. |
| `implementation-notes.md` | required | user review | Requested implementation notes. |
| `check-pack.md` | required | user review | Requested checks. |
| `feedback.md` | omitted | none | No post-delivery customer feedback exists for this task yet. |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | Sources and existing feedback files | Integration decision | Existing mechanism understood. |
| 2 | `chief_editor` | KB/template/roles/backlog | Minimal patch | No parallel mechanism or new role. |
| 3 | `chief_editor` | Patch | Check-pack | Acceptance cases covered. |

## review requirements

- Review artifact: user-visible diff summary and check-pack.
- Review depth: focused on P5.5 governance, optionality, and role boundaries.
- Reviewer independence requirement: user review before commit/push.
- Claims/evidence checks required: source-of-truth files inspected.
- Optional review artifacts justified: no separate `review.md`; user asked for
  check-pack and no commit before review.

## completion criteria

- Required local artifacts complete: yes.
- Production patch is compact and limited to P5.5.
- Feedback classification and guardrails are explicit.
- Backlog P5.5 is implemented.
- Manual/smoke checks are recorded.
