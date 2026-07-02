# План оркестрации

## Краткое описание задачи

- Task ID: `SYSTEM-MAINTENANCE-0018`.
- Цель пользователя: безопасно навести порядок в структуре проекта AI-редакции без изменения поведения системы.
- Deliverable: README для крупных папок, индекс `editorial_knowledge`, пометки пустых/scaffold-only файлов, список `TASK-*`, рекомендации по переносам и очистка служебного шума.
- Аудитория: локальная AI-редакция, Codex, ChatGPT и русскоязычный человек-владелец проекта.
- Текущая активная версия: current repository files.

## Классификация задачи

- Тип: `editorial system update / structural maintenance`.
- Risk mode: `low-risk`.
- Factual sensitivity: low; задача проверяет локальные файлы, а не внешние факты.
- Human approval likely required: no for documentation and noise cleanup; yes for future task moves or deletions.
- Обоснование: изменения улучшают навигацию и маркировку, не меняя редакционную логику.

## Выбранный workflow

- Workflow: `custom workflow mini-contract`.
- Почему так: стандартные production-пайплайны предназначены для материалов; эта задача обслуживает структуру проекта.
- Локальные ограничения: не менять `AGENTS.md`, `/pipelines`, `/agents`, `/kb/task_statuses.md`, review-gate или governance model.

## Назначенные роли

| Этап | Роль | Обязательна? | Примечание |
| --- | --- | --- | --- |
| Оркестрация | `chief_editor` | yes | Route maintenance work and preserve boundaries |
| Инвентаризация | `chief_editor` | yes | Local structural inspection only |
| Служебная документация | `chief_editor` | yes | Russian service docs; no new active rules |
| Проверка | `chief_editor` | yes | Check files, `.DS_Store`, `.gitignore`, and forbidden scope |

Новые роли не создавались. Visual subsystem не активировалась.

## Границы артефактов

| Артефакт | Статус | Потребитель | Обоснование |
| --- | --- | --- | --- |
| `task-manifest.md` | required | restart | Editorial entry discipline |
| `orchestration_plan.md` | required | governance | Compact execution contract |
| `status.md` | required | restart | State and completion record |
| `structure-cleanup-report.md` | required by user | user / restart | Итоговая инвентаризация и решения |
| `review.md` | omitted | none | No editorial material is finalized; verification is mechanical and scope-bound |
| `final.md` | omitted | none | This task is maintenance, not publication content |

## Порядок выполнения

| Шаг | Роль | Input | Output | Условие выхода |
| --- | --- | --- | --- | --- |
| Route | `chief_editor` | user request, `AGENTS.md`, `project-state.md` | task-local route | constraints recorded |
| Inventory `TASK-*` | `chief_editor` | filesystem | task location report | all paths with `TASK-*` found |
| Inspect folders | `chief_editor` | target directories | README scope decisions | no behavior owner changed |
| Mark placeholders | `chief_editor` | empty/scaffold-only files | placeholder/reserved notes | no substantive content added |
| Create knowledge index | `chief_editor` | `editorial_knowledge` file list | `00_index.md` | categories recorded, `AGENTS.md` authority stated |
| Clean noise | `chief_editor` | service files | removed `.DS_Store`, updated `.gitignore` | no valuable files removed |
| Verify | `chief_editor` | changed files and reports | final status | scope matches constraints |

## Проверка

- Отдельный `review.md`: не создаётся для компактной maintenance-задачи.
- Проверка: механическая сверка наличия README, индекса, placeholder/reserved markers, списка `TASK-*`, отсутствия `.DS_Store` и неизменности запретных зон.
- Claims/evidence: только локальная файловая система.
- Optional review artifacts: не нужны.

## Риски

| Риск | Влияние | Владелец | Смягчение |
| --- | --- | --- | --- |
| README случайно становится новым rule source | Может изменить интерпретацию governance | `chief_editor` | Явно указать, что folder docs не определяют активные правила |
| Placeholder marker превращается в hidden guidance | Может создать ложный активный контекст | `chief_editor` | Пометить как non-authoritative и не заполнять содержанием |
| Автоматический перенос задач | Может сломать restart/history assumptions | `chief_editor` | Только inventory и recommendations; no moves |
| Reactivation of visual knowledge | Может нарушить frozen visual subsystem | `chief_editor` | Категория frozen visual-related knowledge only |

## Условия остановки

- Остановиться, если cleanup требует менять `AGENTS.md`, pipelines, roles, statuses, review-gate, governance или visual subsystem state.
- Остановиться, если нужен перенос `TASK-*` или удаление содержательного файла.
- Остановиться, если статус файла active/retired неоднозначен и влияет на активное поведение.

## Критерии завершения

- Required README files exist and are in Russian.
- `editorial_knowledge/00_index.md` exists and states `AGENTS.md` authority.
- `TASK-*` inventory and recommendations are recorded.
- Empty/scaffold-only files are marked or listed.
- `.DS_Store` files are removed and ignored.
- No active editorial behavior, pipelines, roles, statuses, review-gate, governance, retrospectives, or visual subsystem activation changed.
