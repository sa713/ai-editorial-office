# Orchestration Plan

## task summary

- Task ID: TASK-0024
- User goal: understand how the editorial system behaves in practice across accumulated tasks.
- Deliverable: behavioral audit package with executive summary, stage audit, systemic error catalog, useful mechanism catalog, top three improvements, and final decision.
- Audience/channel: internal system owner; markdown artifacts in task folder.
- Current active version: this audit task package.

## task classification

- Task type: research / behavioral audit
- Risk mode: standard
- Factual sensitivity: medium
- Human approval likely required: no
- Rationale: the task analyzes internal project evidence and produces recommendations, not system changes.

## process depth

- Depth: full
- Execution profile: expanded
- Rationale: the user requested maximum practical coverage across completed tasks and multiple behavioral dimensions.
- Forbidden depth shortcuts: no direct recommendations without artifact review; no system edits; no bypass of review before final decision.
- Expanded profile trigger, if any: broad historical sample and governance impact of recommendations.

## selected pipeline

- Pipeline: `research_pipeline` with review-gate and Chief Editor final governance.
- Why this pipeline: the primary work is evidence collection and synthesis from completed task artifacts.
- Pipeline exceptions or local constraints: the final deliverables are audit reports, not production copy; review still checks evidence, reasoning, and completeness.

## custom workflow mini-contract

- Deviation: create audit-specific report artifacts after research synthesis.
- Reason: user requested multiple named audit deliverables rather than only `research.md`.
- Owner: research_agent for evidence and report drafting; review_agent for independent review; chief_editor for final decision.
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent / chief_editor | yes | Normalized in `brief.md`; no blocking open questions |
| Research | research_agent | yes | Inspect task artifacts and synthesize behavioral evidence |
| Writing/UX writing | research_agent | limited | May draft analytical audit artifacts, not editorial system changes |
| Review | review_agent | yes | `review.md` required before final decision |
| Finalization | final_editor | no | Not required; audit package can be finalized by governance after review if no prose conversion is needed |
| Final governance | chief_editor | yes | `final_decision.md` required |

## required knowledge and evidence

- Required KB: `AGENTS.md`, `task_statuses.md`, relevant pipeline/role specs as comparison baseline.
- Required source/evidence files: completed `TASK-*` folders and their task-local artifacts.
- Evidence gaps: some tasks have incomplete artifacts; mark gaps rather than infer hidden behavior.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart and current state |
| `brief.md` | required | all roles | Scope and constraints |
| `orchestration_plan.md` | required | all roles | Route and artifact scope |
| `status.md` | required | all roles | State history |
| `sources.md` | required | review_agent / chief_editor | Evidence sample traceability |
| `research.md` | required | review_agent / chief_editor | Main evidence synthesis |
| `executive-summary.md` | required | user / review_agent | Executive summary requested by user |
| `behavioral-audit.md` | required | user / review_agent | Stage-by-stage behavioral audit |
| `systemic-errors.md` | required | user / chief_editor | Error grouping requested by user |
| `useful-mechanisms.md` | required | user / chief_editor | Strong solution catalog requested by user |
| `top-3-improvements.md` | required | user / chief_editor | Prioritized recommendations |
| `review.md` | required | chief_editor | Independent validation |
| `final_decision.md` | required | user / archive | Governance conclusion |
| `qa-checklist.md` | omitted | n/a | `review.md` can carry checklist compactly |
| `review-summary.md` | omitted unless needed | chief_editor | Only create if review needs separate transfer |
| `open-questions.md` | omitted unless needed | chief_editor | No blocking questions at start |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | User request, AGENTS | Task package | Route recorded |
| 2 | research_agent | Completed task artifacts | `sources.md`, `research.md` | Evidence sample sufficient or limitations explicit |
| 3 | research_agent | Evidence synthesis | audit deliverables | Required sections complete |
| 4 | review_agent | Audit package | `review.md` | Verdict recorded |
| 5 | chief_editor | Audit package and review | `final_decision.md`, status update | Task finalized or blocked |

## status transitions

- Starting status: intake
- Next expected status: research
- Status owner: chief_editor
- Status update trigger: research complete, review begins, review outcome, final decision.

## review requirements

- Review artifact: `review.md`
- Review depth: standard, evidence-aware
- Reviewer independence requirement: reviewer did not produce the audit synthesis
- Claims/evidence checks required: yes, against saved task artifacts and declared sample limitations
- Optional review artifacts justified: no

## human approval requirements

- Required: no
- Approval owner: not applicable
- Evidence needed: not applicable
- Cannot proceed past: no explicit human approval gate

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Incomplete historical artifacts | Medium | research_agent | Mark coverage limits and avoid unsupported conclusions |
| Confusing text quality with system behavior | High | research_agent / review_agent | Keep findings tied to process stage and repeated patterns |
| Overfitting to early legacy tasks | Medium | research_agent | Separate early, mature, visual, and maintenance evidence where useful |
| Recommending system changes without evidence | High | review_agent | Require evidence-linked rationale |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if analysis requires modifying completed tasks or changing system rules.
- Stop or escalate if evidence is too incomplete to support a requested conclusion.

## completion criteria

- Required artifacts complete: yes
- Review outcome acceptable: yes
- Blockers resolved: yes
- Governance fields complete: yes

## finalization conditions

- Finalization may start when: `review.md` approves or requests only non-blocking clarifications.
- Finalization must stop when: review blocks evidence sufficiency or identifies missing required sections.
- Compact finalization shape allowed: yes, if final audit artifacts already are final-form reports and review approves.
- Conditional finalization artifacts needed: no unless review requires controlled wording changes.

## restart notes

- Minimum read set: `AGENTS.md`, `brief.md`, `task-manifest.md`, `status.md`, this plan, current audit artifacts.
- Current active version: `TASK-0024` audit package.
- Deprecated/previous versions: none.
- Latest relevant handoff: none yet.
- Directly relevant pipeline/KB: `research_pipeline`, `review_pipeline`, `task_statuses`.
