# План оркестрации

## Краткое описание задачи

- Task ID: `SYSTEM-MAINTENANCE-0019`.
- Цель пользователя: переименовать update-папки, чтобы не путать рабочие system-maintenance задачи и исторические разборы.
- Deliverable: новые имена папок, mapping, точечные обновления ссылок и проверка.
- Аудитория: человек-владелец проекта, Codex и ChatGPT.

## Выбранная схема имён

- Рабочие записи в `ai-editorial-office/tasks/`: `SYSTEM-MAINTENANCE-0001`.
- Исторические разборы в `retrospectives/`: `system-maintenance-retrospective-0005`.

Эта схема разделяет вопрос "где выполнялась maintenance-задача" и вопрос "где лежит разбор после maintenance-задачи".

## Границы

- Новые роли не создаются.
- Visual subsystem не активируется.
- `AGENTS.md`, pipelines, review-gate, role specs, task status model и governance не меняются.
- Исторические материалы не удаляются.

## Порядок выполнения

| Шаг | Роль | Output |
| --- | --- | --- |
| Inventory | `chief_editor` | Список старых папок |
| Rename | `chief_editor` | Новые folder names |
| Reference update | `chief_editor` | Точечные актуальные ссылки на новые пути |
| Verify | `chief_editor` | `rg`, `find`, memory package check |

## Проверка

- Старых top-level folder names больше нет.
- Новые папки существуют.
- Актуальные навигационные документы используют новую схему.
- `/about` memory package check проходит.
- `.DS_Store` не возвращается.
