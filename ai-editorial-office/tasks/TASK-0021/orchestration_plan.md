# Orchestration Plan

## task summary

- Task ID: TASK-0021
- User goal: передать редакции задачу и получить готовый текст письма участникам встречи УЭК.
- Deliverable: короткое рабочее письмо.
- Audience/channel: сотрудники УЭК, внутреннее письмо после встречи.
- Current active version: `final.md`

## task classification

- Task type: short internal announcement / follow-up email.
- Risk mode: `low-risk`
- Factual sensitivity: low; все операционные инструкции и имена предоставлены пользователем.
- Human approval likely required: no for editorial completion; delivery/publication approval not assessed.
- Rationale: внутреннее рабочее письмо без внешней публикации, числовых, юридических или репутационно чувствительных утверждений.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: один короткий текст, источник контекста один, research не нужен, review обязателен.
- Forbidden depth shortcuts: не пропускать review; не смешивать writing, review, finalization и governance.
- Expanded profile trigger, if any: конфликт требований, спорные продуктовые инструкции, необходимость подтверждения доступа в Друге.

## selected pipeline

- Pipeline: `social_pipeline`
- Why this pipeline: задача является короткой внутренней коммуникацией / announcement copy; article pipeline слишком тяжёлый, UX pipeline не подходит, так как это не интерфейсная микрокопия.
- Pipeline exceptions or local constraints: email channel вместо соцплатформы; platform adaptation трактуется как рабочее письмо.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `intake_agent` | yes | normalized brief |
| Research | `research_agent` | no | user supplied required factual context |
| Writing | `writer_agent` | yes | short email draft |
| Review | `review_agent` | yes | `review.md` required |
| Finalization | `final_editor` | yes | final email in `final.md` |
| Final governance | `chief_editor` | yes | `final_decision.md` |

## required knowledge and evidence

- Required KB: `tone_of_voice.md`, `editorial_policy.md`, selected `social_pipeline.md`.
- Required source/evidence files: `brief.md`; user-provided prompt captured there.
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | normalized user request |
| `task-manifest.md` | required | all roles | restart and governance pointer |
| `status.md` | required | all roles | state history |
| `orchestration_plan.md` | required | all roles | routing and compact-depth rationale |
| `draft.md` | required | review/finalization | draft under review |
| `writer-notes.md` | required | review | compact rationale and constraints |
| `claims-used.md` | omitted | review | no separate claim traceability needed; claims are user-provided instructions in `brief.md` |
| `research.md` / `sources.md` / `facts.md` / `claims_table.md` | omitted | review/governance | no separate research needed |
| `review.md` | required | final_editor / chief_editor | review gate |
| `qa-checklist.md` | omitted | none | checklist embedded in `review.md` |
| `review-summary.md` | omitted | none | review handoff and `review.md` sufficient |
| `final.md` | required | user / chief_editor | final deliverable |
| `finalization-notes.md` | omitted | none | no controlled changes beyond approved polishing |
| `final_decision.md` | required | governance | final readiness decision |

## structure-before-writing plan

- Reader path: thank participants -> provide two material links -> explain access steps -> fallback if invite is missing -> Сергей as contact.
- Section roles: greeting/context, materials, access instruction, troubleshooting.
- Required structure: subject line plus short body.
- Duplication risks: do not repeat meeting content; avoid two separate long instruction lists if prose is clearer.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `intake_agent` | user request | `brief.md`, intake handoff | scope clear |
| 2 | `chief_editor` | brief, pipeline rules | plan, manifest/status update, handoff to writer | route approved |
| 3 | `writer_agent` | brief, plan, tone/policy | `draft.md`, `writer-notes.md`, writing handoff | ready for review |
| 4 | `review_agent` | draft and artifacts | `review.md`, review handoff | approved or changes requested |
| 5 | `final_editor` | approved draft/review | `final.md` | final deliverable exists |
| 6 | `chief_editor` | review/final/manifest | `final_decision.md`, status finalized | governance complete |

## review requirements

- Review artifact: `review.md`
- Review depth: compact; checklist embedded in review.
- Reviewer independence requirement: review role instance distinct from writer role instance.
- Claims/evidence checks required: validate against `brief.md`; no external research.
- Optional review artifacts justified: no; no downstream consumer.

## human approval requirements

- Required: no for producing the requested text.
- Approval owner: user, if sending the email.
- Evidence needed: not needed for editorial completion.
- Cannot proceed past: actual sending/publication not assessed.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Text becomes too instructional or long | lower usefulness | writer/reviewer | keep steps compact |
| Missing invite workflow is unclear | access friction | writer/reviewer | include exact filter instruction |
| Links are not yet available | incomplete send-ready details | user | placeholders marked for manual insertion |

## unresolved questions

- None.

## completion criteria

- Required artifacts complete: yes when `final.md`, `review.md`, `final_decision.md`, manifest and status exist.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## finalization conditions

- Finalization may start when: review outcome is `approved`.
- Finalization must stop when: new claims, new access instructions, or unreviewed scope changes are introduced.
- Compact finalization shape allowed: yes; no separate finalization notes needed if final matches approved draft.
- Conditional finalization artifacts needed: no.

## restart notes

- Minimum read set: `AGENTS.md` invariant summary, this plan, `task-manifest.md`, `final.md`, `review.md`.
- Current active version: `final.md`.
- Deprecated/previous versions: none.
- Latest relevant handoff: `handoff-review-review-agent-to-final-editor.md`.
- Directly relevant pipeline/KB: `social_pipeline.md`, `tone_of_voice.md`, `editorial_policy.md`.
