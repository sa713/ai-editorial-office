# Limit usage review

## Где тратится слишком много токенов

- Полные agent specs по 400-600 строк читаются ради короткого действия.
- Пайплайны по 300-660 строк повторяют общие инварианты.
- Task templates доходят до 700-1000 строк и содержат много политики.
- `final_decision_template.md` и `status_template.md` слишком подробны для обычных задач.
- Старые задачи содержат handoff по 100-300 строк, которые соблазняют читать историю вместо короткого состояния.
- Ретроспективы уже больше активной редакционной базы и требуют выборочного чтения.

## Где контекст читается повторно

- `AGENTS.md` + роль + пайплайн + шаблон повторяют review-gate и role separation.
- `kb/editorial_policy.md` и `AGENTS.md` повторяют factual discipline, review, artifact minimalism.
- `editorial_knowledge/40_editorial_review_system.md` и `review_agent.md` частично пересекаются по review behavior.
- `project_tree.md` и `AGENTS.md` повторяют ownership map.
- Task-local `status.md`, `orchestration_plan.md`, `handoff-*` повторяют artifact inventory.

## Какие файлы слишком часто подтягиваются без необходимости

- Полный `project_tree.md` нужен для архитектурных ревью, но не для обычного выполнения.
- Полные task templates нужны при создании задачи, но не на каждом этапе.
- Полный `status.md` не нужен, если `task-manifest.md` свежий и задача не спорная.
- Все `editorial_knowledge` файлы не нужны для каждой задачи. Достаточно выбранного режима, operational rules и review system по необходимости.
- Ретроспективы нужны только при системных изменениях или проверке истории решения.

## Какие этапы можно делать короче

- Intake: использовать компактный brief из 5-7 сигналов, не полную форму.
- Orchestration: записывать только pipeline, depth, next role, required artifacts, omissions.
- Writing: не делать отдельные notes, если нет допущений, рисков или фактов.
- Review: в low-risk держать verdict, checked scope, findings, next action в одном файле.
- Final decision: проверять только неснятые governance-вопросы, не повторять весь review.

## Где использовать summaries вместо полного чтения

- Для длинных источников: `source-summary.md` или краткий блок в research.
- Для длинной истории задачи: свежий `task-manifest.md`.
- Для повторного review: `re-review scope`.
- Для версии v2/v3: `current-version.md` или короткий блок в манифесте.
- Для ретроспектив: короткий `implemented / deferred / do not do` вместо чтения всех diff-файлов.

## Где уменьшить output volume

- Handoff: максимум 10-15 строк, если нет blocker.
- Review: не больше одного review artifact для low-risk.
- Final decision: короткий verdict + blockers + required before sending.
- Orchestration: не копировать таблицу всех возможных артефактов.
- Status: держать историю, но не повторять план и review.

## Целевое состояние

Для обычной задачи следующая роль должна читать:

1. `AGENTS.md` по необходимости или короткую ссылку на инварианты.
2. `task-manifest.md`.
3. Последний handoff или объект работы.
4. Только один релевантный пайплайн или его краткий профиль.

Остальное читать только при риске, конфликте, source-heavy задаче или high-governance.

