# Манифест задачи

## Идентификация задачи

- Task ID: `SYSTEM-MAINTENANCE-0018`
- Название: безопасная структурная очистка AI-редакции.
- Тип: `editorial system update / structural maintenance`.
- Текущая роль-владелец: `chief_editor`.
- Создано: 2026-06-04.
- Последнее обновление: 2026-06-04.

## Текущее состояние

- Статус: `finalized`.
- Выбранный workflow: `custom workflow mini-contract`.
- Risk mode: `low-risk`.
- Process depth: `compact`.
- Execution profile: `compact`.
- Текущий рабочий артефакт: служебная навигация, индексы, README и отчёт по структуре.
- Последний relevant handoff: отсутствует.
- Следующее действие: нет; структурная очистка и проверка завершены.

## Свежесть

- Последняя проверка: 2026-06-04.
- Проверил: `chief_editor`.
- Станет устаревшим, если изменятся структура задач, `editorial_knowledge`, `scripts`, `tests`, `learn`, `retrospectives` или `.gitignore`.

## Governance-состояние

- Отдельный review-артефакт: не требуется для компактной структурной maintenance-задачи без финального редакционного материала.
- Review artifact/current version: not applicable.
- Review outcome: mechanical verification passed.
- Compact finalization shape allowed: yes.
- Human approval required: no for completed documentation/noise cleanup; yes for future moves, deletions or doctrine changes.
- Human approval evidence: current user instruction.
- Final decision artifact: not required.

## Инвентарь артефактов

| Артефакт | Текущий? | Обязательность | Примечание |
| --- | --- | --- | --- |
| `task-manifest.md` | yes | required | Compact restart state for this maintenance task |
| `orchestration_plan.md` | yes | required | Execution contract and forbidden changes |
| `status.md` | yes | required | Status and completion state |
| `structure-cleanup-report.md` | yes | required by user | Список `TASK-*`, маркировки, рекомендации и вопросы |
| README/index/marker files | yes | required by user | Русская служебная навигация без новых активных правил |
| `.gitignore` | yes | required by cleanup | Игнорирует `.DS_Store` |
| `retrospectives/editorial-structure-ordering-recommendations-2026-06-03.md` | yes | cleanup / preservation | Read-only audit note moved out of `/about` to keep memory package at 20 files |

## Активные ограничения

- Не менять редакционное поведение, `AGENTS.md`, пайплайны, review-gate, роли, статусы задач, governance, retrospectives или visual subsystem.
- Не выполнять массовый перенос `TASK-*`.
- Не удалять retrospectives.
- Не наполнять пустые/scaffold-only файлы содержательными правилами.
- `AGENTS.md` остаётся главным источником архитектурных правил и иерархии управления.

## Открытые вопросы

- Обязательных blocker-вопросов нет.
- Будущие человеческие решения перечислены в `structure-cleanup-report.md`.

## Пакет следующего действия

- Роль: `chief_editor`.
- Действие: передать пользователю итоговый отчёт.
- Ожидаемый output: краткое резюме изменений, найденных `TASK-*`, маркировок и оставшихся человеческих решений.
- Stop conditions: любое дальнейшее действие, требующее изменения активных правил, переносов задач, удаления исторических материалов или активации visual subsystem.
