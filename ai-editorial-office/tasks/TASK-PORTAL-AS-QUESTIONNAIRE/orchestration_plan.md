# Orchestration Plan

## Task Summary

- Task ID: `TASK-PORTAL-AS-QUESTIONNAIRE`
- User goal: провести полный редакционный цикл и подготовить публикацию для портала задач.
- Deliverable: `portal_task_draft.md`, плюс обязательные артефакты анализа, review и финального решения.
- Audience/channel: портал задач; сотрудники, которые выбирают задачи для участия.
- Current active version: `portal_task_draft.md`

## Task Classification

- Task type: editorial publication / article-like task card.
- Risk mode: `standard`
- Factual sensitivity: moderate; тема связана с защищённостью архитектуры, но публикация не должна добавлять технические утверждения сверх исходника.
- Human approval likely required: yes, before actual portal publication.
- Rationale: задача готовит внешний для команды текст на внутренний портал; есть потенциально чувствительная терминология, поэтому нужны явные ограничения и review.

## Process Depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: источник один, фактов мало, задача source-light; review обязателен, но отдельные evidence-файлы не нужны, потому что все исходные данные сохранены в `brief.md` и разобраны в `task_analysis.md`.
- Forbidden depth shortcuts: нельзя выпускать текст без review; нельзя добавлять факты, роли, метрики или техническую методику, которых нет в исходнике.
- Expanded profile trigger: появление дополнительных источников, требований к методике оценки защищённости, согласованию с владельцами модели или публикации от имени конкретного клиента.

## Selected Pipeline

- Pipeline: `article_pipeline`
- Why this pipeline: результат является публикацией/карточкой для портала задач, а не интерфейсной копией.
- Pipeline exceptions or local constraints: пользователь задал имена обязательных артефактов. Поэтому `task_analysis.md` выполняет функцию анализа и структуры, а `portal_task_draft.md` является draft/final deliverable under review.

## Client Profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: none.
- Non-activation reason: задача не просит писать от имени Сбера или по редполитике Сбера.
- Stop condition: если позднее потребуется публикация от имени конкретной организации с отдельной редполитикой, нужен новый routing decision.

## Preflight Gate

| Field | Decision |
| --- | --- |
| Audience | `inferred` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `constrain` |

- Rationale: данных достаточно для подготовки понятной карточки, если не расширять содержание за пределы исходника. Неподтверждённые детали выносятся в вопросы.
- Production may start: yes.
- If `constrain`: карточка не утверждает состав математической модели, расшифровку CIA(T), формат существующих наработок и полномочия КА ФО.

## Required Agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `intake_agent` | yes | Нормализует задачу в `brief.md`. |
| Orchestration | `chief_editor` | yes | Выбирает pipeline, risk mode, artifact scope. |
| Analysis | `research_agent` / `writer_agent` bounded | yes | Анализирует проблему и структуру без внешних источников. |
| Writing | `writer_agent` | yes | Готовит `portal_task_draft.md`. |
| Review | `review_agent` | yes | Независимо проверяет карточку в `review.md`. |
| Finalization | `final_editor` | yes | Создаёт `final.md` после approved review. |
| Final governance | `chief_editor` | yes | Создаёт `final_decision.md`. |

## Artifact Scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Фиксирует исходник и критерии готовности. |
| `task-manifest.md` | required | all roles | Restart anchor. |
| `status.md` | required | all roles | Статус и governance state. |
| `orchestration_plan.md` | required | all roles | Execution contract. |
| `task_analysis.md` | required by user | writer/reviewer | Анализ реальной проблемы, результата, компетенций и вопросов. |
| `portal_task_draft.md` | required by user | reviewer/final editor/user | Готовая публикация для портала задач. |
| `review.md` | required | final editor/chief editor | Review gate. |
| `final.md` | required by pipeline | chief editor/user | Controlled final deliverable after review. |
| `final_decision.md` | required | user/chief editor | Final governance decision. |
| `sources.md` / `facts.md` / `claims_table.md` | omitted | none | Внешние источники не используются; source boundary полностью в `brief.md`. |
| `qa-checklist.md` | omitted | none | Компактный чеклист включён в `review.md`. |

## Structure-Before-Writing Plan

- Reader path: проблема -> зачем участвовать -> что нужно сделать -> ожидаемый результат -> кому подходит -> что уже есть -> вопросы.
- Section roles: заголовок должен быстро объяснять задачу; тело должно снять неясность исходника; финальный блок должен показать вклад участника.
- Required structure: краткий лид, проблема, результат, задачи участника, компетенции, исходные данные, ожидаемая польза, вопросы.
- Duplication risks: не повторять математическую модель и уровень защищённости в каждом разделе.

## Review Requirements

- Review artifact: `review.md`
- Review depth: compact standard.
- Reviewer independence requirement: `review_agent` не является writer/final editor.
- Claims/evidence checks required: проверить, что все утверждения выводятся из `brief.md` или явно отмечены как вопросы.
- Optional review artifacts justified: no.

## Human Approval Requirements

- Required: yes, before publishing on the portal.
- Approval owner: task requester or portal/content owner.
- Evidence needed: explicit approval of final text and answers to optional open questions if they are material.
- Cannot proceed past: actual publication.

## Known Risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Неясна расшифровка `CIA(T)` | Возможна терминологическая ошибка | Human owner | Вынести в вопросы; не расшифровывать самовольно. |
| Неясно, что означает `КА ФО` | Внутренний жаргон может быть непонятен | Human owner | В публикации заменить на понятное описание роли. |
| Неясен формат существующих наработок | Участник может неверно оценить объём работы | Human owner | Сформулировать осторожно: "есть предварительные материалы". |

## Completion Criteria

- Required artifacts complete: yes when `task_analysis.md`, `portal_task_draft.md`, `review.md`, `final.md`, `final_decision.md` exist.
- Review outcome acceptable: `approved`.
- Blockers resolved: no blockers for editorial delivery; publication approval remains external.
- Governance fields complete: yes.
