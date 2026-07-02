# Orchestration Plan

## task summary

- Task ID: `VIBE-VISION`
- User goal: содержательно проверить зрелость vision-документа сообщества.
- Deliverable: `review.md`, `improvement_proposals.md`, `final_decision.md`.
- Audience/channel: владелец концепции и участники дальнейшего проектирования сообщества.
- Current active version: `Vibe Coding Community Vision.md`

## task classification

- Task type: editorial review.
- Risk mode: `standard`.
- Factual sensitivity: low; проверяется внутренняя логика и концептуальная достаточность, а не внешние факты.
- Human approval likely required: yes, для принятия или отклонения предложенных правок.
- Rationale: документ задаёт концептуальную рамку сообщества, поэтому нужна внимательная проверка связности, но без внешнего ресёрча.

## process depth

- Depth: `normal`.
- Execution profile: `compact`.
- Rationale: исходный документ короткий и самодостаточный; дополнительных исследовательских артефактов не требуется.
- Forbidden depth shortcuts: нельзя обходить редакционную маршрутизацию и независимый review artifact.
- Expanded profile trigger, if any: появление внешних источников, спорной стратегии или запроса на переписывание vision.

## selected pipeline

- Pipeline: `review_pipeline`.
- Why this pipeline: задача состоит в независимой проверке уже существующего материала.
- Pipeline exceptions or local constraints: вместо проверки `draft.md` проверяется task-local source artifact `Vibe Coding Community Vision.md`; это зафиксировано как текущая активная версия.

## client profile

- Client profile: `none`.
- Client profile status: `not_applicable`.
- Activation reason: not applicable.
- Non-activation reason, if considered and rejected: задача не относится к Sber-owned/Sber-policy материалам.
- Client-profile files: none.
- Stop condition: обнаружение скрытого клиентского требования, меняющего критерии ревью.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `inferred` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: пользователь дал источник, папку, цель, критерии проверки, ограничения и ожидаемые артефакты.
- Production may start: yes.
- If `ask`: not applicable.
- If `constrain`: проверять только существующую концепцию, не проектировать новую.
- If `block`: not applicable.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Select review route, maintain governance artifacts |
| Review | Review Agent | yes | Produce `review.md` and improvement findings |
| Final governance | Chief Editor | yes | Record `final_decision.md` |

## required knowledge and evidence

- Required KB: `AGENTS.md`, `review_pipeline.md`, `task_statuses.md`.
- Required source/evidence files: `Vibe Coding Community Vision.md`.
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | Review Agent / Chief Editor | Scope and acceptance criteria |
| `task-manifest.md` | required | all roles | Current state pointer |
| `status.md` | required | all roles | State history and review outcome |
| `orchestration_plan.md` | required | Review Agent / Chief Editor | Execution contract |
| `review.md` | required | Chief Editor / user | Main detailed review |
| `improvement_proposals.md` | required by user | user / future Writer Agent | Specific change list |
| `final_decision.md` | required by user | user / Chief Editor | Final governance verdict |
| `qa-checklist.md` | omitted | none | Checklist embedded in `review.md` |
| `review-summary.md` | omitted | none | `final_decision.md` provides concise conclusion |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | User request, AGENTS.md | `brief.md`, `task-manifest.md`, `orchestration_plan.md`, `status.md` | Review route recorded |
| 2 | Review Agent | Source document and scope | `review.md`, `improvement_proposals.md` | Findings and improvement proposals complete |
| 3 | Chief Editor | Review artifacts | `final_decision.md`, updated `status.md`, updated `task-manifest.md` | Final verdict recorded |

## review requirements

- Review artifact: `review.md`.
- Review depth: normal conceptual review.
- Reviewer independence requirement: Review Agent must review the source document, not its own rewrite.
- Claims/evidence checks required: internal consistency and source-boundary check only.
- Optional review artifacts justified: yes, `improvement_proposals.md` is explicitly required by the user.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Review expands into new strategy | Would violate user constraints | Review Agent | Frame all proposals as small clarifications of existing model |
| Literary editing displaces conceptual review | Lowers usefulness | Review Agent | Do not propose wording polish unless it affects meaning |
| Operational model becomes too heavy | Contradicts practical-realizability criterion | Review Agent | Recommend lightweight clarification, not new governance |

## unresolved questions

- None.

## completion criteria

- Required artifacts complete: yes when `review.md`, `improvement_proposals.md`, and `final_decision.md` exist.
- Review outcome acceptable: final verdict recorded.
- Blockers resolved: no blockers.
- Governance fields complete: yes after final status update.
