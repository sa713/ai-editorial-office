# Orchestration Plan

Task ID: `TASK-0004`

Owner: `chief_editor`

Stage: `planning`

## task summary

Requested output: revised operational instruction, review summary, QA checklist, final decision, compact handoff.

Audience: employees using an internal task exchange.

Primary goal: make the instruction actionable, sequential, and low-friction.

Quality bar: practical usefulness over friendliness, style, or editorial polish.

Current task status at planning: `planning`

Brief source: `/tasks/TASK-0004/brief.md`

## task classification

Task type: `editorial-review`

Complexity: `medium`

Risk level: `medium`

Factual sensitivity: `low`

Requires research: `no`

Requires writing: `yes`

Requires independent review: `yes`

Requires human approval: `no`

Classification rationale:

- The task is internal and operational, not external publication.
- The draft contains process rules and action ownership, so unclear wording can cause incorrect use.
- No external factual claims require research; the source draft is the authoritative supplied material.

## selected pipeline

Pipeline file: `/pipelines/review_pipeline.md`

Supporting governance: `/tasks/SYSTEM-MAINTENANCE-0001/final_decision.md`, `editorial_knowledge/50_editorial_failure_patterns.md`

Reason selected:

- The user requested instruction review and improvement, not creation of product UI copy.
- The key risk is usefulness failure: buried action, sequence ambiguity, operational overload, and fake usefulness.

Pipeline constraints:

- Review gate required before finalization.
- Writing/revision and review must remain separate stages.
- Do not add unsupported product behavior or new frameworks.
- Do not rewrite from scratch unless source structure is critically broken.

Pipeline conflicts: none.

## required agents

| Stage | Required agent | Responsibility |
| --- | --- | --- |
| intake | `intake_agent` | normalize task, reader state, success criteria |
| planning | `chief_editor` | select path and artifact scope |
| writing | `writer_agent` | revise source into operational instruction |
| review | `review_agent` | validate usefulness, clarity, sequence, and risks |
| finalization | `final_editor` | produce final deliverable from approved draft |
| governance | `chief_editor` | final decision and compact handoff |

## artifact scope

| Artifact | Class | Owner | Status | Rationale |
| --- | --- | --- | --- | --- |
| `brief.md` | required | `intake_agent` | present | defines reader task and risks |
| `task-manifest.md` | required | current owner | present | restart anchor |
| `status.md` | required | current owner | present | state history |
| `orchestration_plan.md` | required | `chief_editor` | present | execution contract |
| `draft.md` | required | `writer_agent` | present | revised instruction candidate |
| `review.md` | required | `review_agent` | present | verdict and findings |
| `qa-checklist.md` | required | `review_agent` | present | user explicitly requested QA checks |
| `review-summary.md` | required | `review_agent` | present | concise transfer |
| `final.md` | required | `final_editor` | present | final revised instruction |
| `final_decision.md` | required | `chief_editor` | present | governance closure |
| `compact-handoff.md` | required | `chief_editor` | present | final chat output source |

Research artifacts omitted: no external factual research required; the supplied source is the source of truth.

## execution order

1. Intake: define reader task, reader state, operational goal, misunderstanding risks, drop-off points.
2. Structure analysis: identify answer delay, buried actions, context inflation, sequence breaks, unclear ownership, overload.
3. Revision: preserve usable structure and revise locally for action hierarchy and clarity.
4. Review: check usefulness, cognitive load, action discoverability, sequence integrity, fake usefulness, replaceability, and residual friction.
5. Finalization: create final instruction from approved draft.
6. Governance: confirm artifacts and provide compact handoff only.

## review requirements

Review must answer separately:

- where instruction is still friction-heavy;
- which actions remain non-obvious;
- where text sounds correct but is operationally weak;
- which parts are likely to be skipped;
- where text explains the system instead of helping the reader act;
- whether unnecessary editorialization remains.
