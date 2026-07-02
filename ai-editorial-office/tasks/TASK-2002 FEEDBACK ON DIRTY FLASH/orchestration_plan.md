# Orchestration Plan

## task summary

- Task ID: `TASK-2002 FEEDBACK ON DIRTY FLASH`
- User goal: classify customer feedback on `TASK-2001 DIRTY FLASH` and decide whether it implies task-local action, preference tracking, observation, confirmed pattern, or system change.
- Deliverable: feedback classification and governance decision.
- Audience/channel: internal editorial process.
- Current active version: first feedback classification.

## task classification

- Task type: post-delivery feedback classification.
- Risk mode: standard.
- Factual sensitivity: low; the task evaluates saved editorial artifacts and explicit customer feedback.
- Human approval likely required: no.
- Rationale: feedback is meaningful but does not contain legal, factual, or publication-sensitive claims.

## process depth

- Depth: compact.
- Execution profile: compact.
- Rationale: the feedback is specific, source artifacts are available, and the user explicitly forbids premature system updates.
- Forbidden depth shortcuts: do not create `system_change_proposal.md`; do not update `feedback_patterns.md`, `engineering_watchlist.md`, backlog, or global rules from this single signal.
- Expanded profile trigger, if any: repeated similar feedback across tasks or explicit user request for a system-change analysis.

## selected pipeline

- Pipeline: `review_pipeline`.
- Why this pipeline: the task reviews a delivered artifact set and records a deterministic governance decision about feedback handling.
- Pipeline exceptions or local constraints: `feedback.md` is the reviewed material instead of a production `draft.md`.

## client profile

- Client profile: none.
- Client profile status: not_applicable.
- Activation reason: none.
- Non-activation reason, if considered and rejected: the task is not a client-owned communication.
- Client-profile files: none.
- Stop condition: not applicable.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | confirmed |
| Channel or context | confirmed |
| Deliverable | defined |
| Source boundary | defined |
| Success criterion | defined |
| Approval boundary | defined |
| Missing data strategy | proceed |

- Rationale: the feedback and source artifacts are explicit enough for classification.
- Production may start: yes.
- If `constrain`: decide only feedback handling, not a rewrite of TASK-2001.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/routing | Chief Editor | yes | Apply customer feedback loop |
| Analysis | Chief Editor | yes | Classify feedback and system-change boundary |
| Review | Review Agent | yes | Validate classification and guardrails |
| Final governance | Chief Editor | yes | Record no-system-change decision |

## required knowledge and evidence

- Required KB: `kb/customer_feedback_loop.md`, `kb/feedback_patterns.md`.
- Required source/evidence files: TASK-2001 `photo_concept.md`, `model_brief.md`, `photographer_cheatsheet.md`, `editorial_decision.md`; current user feedback.
- Evidence gaps: no cross-task recurrence evidence.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Defines feedback scope |
| `task-manifest.md` | required | all roles | Restart pointer |
| `orchestration_plan.md` | required | all roles | Feedback-loop contract |
| `status.md` | required | all roles | Lifecycle trace |
| `feedback.md` | required | Chief Editor / user | Main classification |
| `review.md` | required | Chief Editor | Review gate |
| `final_decision.md` | required | Chief Editor / user | Governance closure |
| `system_change_proposal.md` | omitted | n/a | Insufficient evidence by rule |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user feedback, TASK-2001 artifacts | routing artifacts | feedback classification may start |
| 2 | Chief Editor | feedback-loop KB, source artifacts | `feedback.md` | classification complete |
| 3 | Review Agent | `feedback.md`, rules, source artifacts | `review.md` | approved/blocked/changes requested |
| 4 | Chief Editor | approved review | `final_decision.md`, finalized status | task closed |

## review requirements

- Review artifact: `review.md`
- Review depth: compact standard review.
- Reviewer independence requirement: Review Agent validates Chief Editor classification.
- Claims/evidence checks required: verify no system update is proposed from insufficient evidence.
- Optional review artifacts justified: no.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Treating useful feedback as a system flaw | Premature system change | Chief Editor / Review | Classify as task-local observation unless recurrence appears |
| Losing useful nuance | Future similar tasks may repeat drift | Chief Editor | Record specific lesson in task-local `feedback.md` |
| Silently rewriting TASK-2001 | Scope creep | Chief Editor | Mark bounded revision as optional future action only |

## completion criteria

- Required artifacts complete: yes.
- Feedback type and significance recorded: yes.
- System-change decision recorded: yes.
- Review outcome acceptable: yes.
- No forbidden system update created: yes.

## restart notes

- Minimum read set: `brief.md`, `feedback.md`, `review.md`, `final_decision.md`, TASK-2001 source artifacts.
- Current active version: first classification.
- Deprecated/previous versions: none.
- Latest relevant handoff: not applicable.
- Directly relevant pipeline/KB: `review_pipeline`, `customer_feedback_loop.md`, `feedback_patterns.md`.
