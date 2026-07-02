# Orchestration Plan

## task summary

- Task ID: TASK-UEK-TRAVEL-HOBBY-DASHBOARD-BR
- User goal: подготовить БТ к дашборду "Путешествия и хобби сотрудников УЭК"
- Deliverable: `business_requirements.md`
- Audience/channel: внутренняя продуктовая и разработческая документация
- Current active version: `business_requirements.md`

## task classification

- Task type: business requirements / article-style knowledge document
- Risk mode: `low-risk`
- Factual sensitivity: low; all substantive inputs provided by user
- Human approval likely required: no
- Rationale: задача не требует внешних источников, политик или технических решений; основная ценность в структурировании требований.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: low-risk source-light task with clear input, while review-gate remains mandatory.
- Forbidden depth shortcuts: no bypass of review, no production outside task folder, no creation of new pipeline or roles.
- Expanded profile trigger, if any: conflicting requirements, demand for technical architecture, or need for external facts.

## selected pipeline

- Pipeline: article_pipeline
- Why this pipeline: existing project has no dedicated business-requirements pipeline; article_pipeline is the nearest existing markdown-first flow for structured deliverables requiring writing and review.
- Pipeline exceptions or local constraints: `business_requirements.md` is the main deliverable; `draft.md` is kept as a pointer to avoid duplicating the full document.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: n/a
- Non-activation reason, if considered and rejected: task is about УЭК and not a Sber-owned or explicit Sber-policy task.
- Client-profile files: none
- Stop condition: if user later states that Sber editorial policy must apply.

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

- Rationale: user supplied detailed business context, functional scope, required roles, format, exclusions, and readiness criteria.
- Production may start: yes
- If `ask`: n/a
- If `constrain`: stay within business requirements, not technical design.
- If `block`: n/a

## custom workflow mini-contract

- Deviation: main deliverable is named `business_requirements.md`, while `draft.md` points to it.
- Reason: user explicitly requested a main BT document and project pipeline expects a draft artifact.
- Owner: chief_editor
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | chief_editor | yes | Compact intake from user prompt |
| Research | research_agent | no | External research not required |
| Writing | writer_agent | yes | Prepare main BT document |
| Review | review_agent | yes | `review.md` required |
| Finalization | final_editor | no | No separate `final.md`; main artifact is approved as final deliverable |
| Final governance | chief_editor | yes | `final_decision.md` after approved review |

## required knowledge and evidence

- Required KB: `AGENTS.md`, `kb/task_statuses.md`, selected pipeline and templates.
- Required source/evidence files: user prompt captured in `brief.md`.
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Normalize task goal and constraints |
| `task-manifest.md` | required | all roles | Restart anchor |
| `status.md` | required | all roles | State and transition evidence |
| `orchestration_plan.md` | required | all roles | Entry routing and role assignment |
| `business_requirements.md` | required | user / development team | Main deliverable |
| `draft.md` | required | review_agent | Pipeline compatibility pointer |
| `review.md` | required before final decision | chief_editor | Review-gate evidence |
| `final_decision.md` | conditional | user / chief_editor | Governance closure after approved review |
| `final.md` | omitted | n/a | Would duplicate main deliverable; review-gate is preserved through `business_requirements.md` and `final_decision.md` |

## structure-before-writing plan

- Reader path: context -> purpose -> users -> cross-cutting rules -> module stories -> analytics -> exclusions -> open questions.
- Section roles: separate business intent from checkable requirements.
- Required structure: match user-requested outline.
- Duplication risks: avoid repeating every visibility or moderation rule inside every module unless needed for acceptance criteria.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | user prompt, AGENTS, templates | task folder, brief, manifest, status, plan | preflight allows proceed |
| 2 | writer_agent | brief, plan | `business_requirements.md`, `draft.md` | all required sections and stories exist |
| 3 | review_agent | brief, plan, document | `review.md` | deterministic outcome recorded |
| 4 | chief_editor | approved review | `final_decision.md`, updated manifest/status | task ready for user review |

## status transitions

- Starting status: intake
- Next expected status: finalized
- Status owner: chief_editor
- Status update trigger: artifact creation, review outcome, final decision

## review requirements

- Review artifact: `review.md`
- Review depth: compact deterministic review against user criteria and exclusions.
- Reviewer independence requirement: review role is separate from writer role.
- Claims/evidence checks required: validate against user-provided brief; no external source claims.
- Optional review artifacts justified: no; embedded checklist in `review.md` is sufficient.

## human approval requirements

- Required: no
- Approval owner: n/a
- Evidence needed: n/a
- Cannot proceed past: n/a

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Документ станет похож на ТЗ | Размывание бизнес-уровня | writer_agent / review_agent | Exclude API, DB, architecture, UI layouts, estimates |
| Открытые вопросы превратятся в скрытые требования | Неясность scope | writer_agent / review_agent | Phrase them as questions |
| Final artifact duplication | Confusing current version | chief_editor | Keep `business_requirements.md` as main artifact and `draft.md` as pointer |

## unresolved questions

- None blocking. Product open questions are part of the deliverable.

## escalation conditions

- Stop or escalate if the user requests changes to AGENTS, roles, review-gate, pipelines, or production project rules.

## completion criteria

- Required artifacts complete: yes when listed artifacts exist.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## finalization conditions

- Finalization may start when: `review.md` outcome is approved.
- Finalization must stop when: review is missing, blocked, or changes requested.
- Compact finalization shape allowed: yes; main deliverable is already the named business artifact.
- Conditional finalization artifacts needed: `final_decision.md` only.

## restart notes

- Minimum read set: `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, `business_requirements.md`, `review.md`.
- Current active version: `business_requirements.md`.
- Deprecated/previous versions: none.
- Latest relevant handoff: not created under compact execution.
- Directly relevant pipeline/KB: `article_pipeline.md`, `kb/task_statuses.md`.
