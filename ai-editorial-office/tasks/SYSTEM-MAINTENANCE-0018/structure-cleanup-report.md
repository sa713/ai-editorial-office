# Отчёт о структурной очистке

## Правило структуры задач

- `ai-editorial-office/tasks/` — рабочие задачи редакции и их task-local артефакты.
- `retrospectives/` — исторические разборы, выводы и развитие системы.

Рабочие задачи не переносятся автоматически. Ретроспективы не удаляются.

## Найденные `TASK-*`

| `TASK-*` | Расположение | Зона | Оценка |
| --- | --- | --- | --- |
| `TASK-0001` | `ai-editorial-office/tasks/TASK-0001/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0002` | `ai-editorial-office/tasks/TASK-0002/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0003` | `ai-editorial-office/tasks/TASK-0003/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0003B` | `ai-editorial-office/tasks/TASK-0003B/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0004` | `ai-editorial-office/tasks/TASK-0004/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0004B` | `ai-editorial-office/tasks/TASK-0004B/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0005` | `ai-editorial-office/tasks/TASK-0005/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0006` | `ai-editorial-office/tasks/TASK-0006/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0007` | `ai-editorial-office/tasks/TASK-0007/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0008` | `ai-editorial-office/tasks/TASK-0008/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0009` | `ai-editorial-office/tasks/TASK-0009/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0010` | `ai-editorial-office/tasks/TASK-0010/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0011` | `ai-editorial-office/tasks/TASK-0011/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0012` | `ai-editorial-office/tasks/TASK-0012/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0013` | `ai-editorial-office/tasks/TASK-0013/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0014` | `ai-editorial-office/tasks/TASK-0014/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0015` | `ai-editorial-office/tasks/TASK-0015/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0016` | `ai-editorial-office/tasks/TASK-0016/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0017` | `ai-editorial-office/tasks/TASK-0017/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0018` | `ai-editorial-office/tasks/TASK-0018/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0019` | `ai-editorial-office/tasks/TASK-0019/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0020` | `ai-editorial-office/tasks/TASK-0020/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0021` | `ai-editorial-office/tasks/TASK-0021/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0022` | `ai-editorial-office/tasks/TASK-0022/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0023` | `ai-editorial-office/tasks/TASK-0023/` | рабочие задачи редакции | ожидаемое место |
| `TASK-0001-retrospective.md` | `retrospectives/TASK-0001-retrospective.md` | исторические разборы | ожидаемое место для retrospective |

## Задачи вне ожидаемых зон

Не обнаружены.

## Рекомендации по переносу задач

Обязательных рекомендаций по переносу нет: найденные `TASK-*` находятся в
`ai-editorial-office/tasks/` или `retrospectives/`.

Если в будущем потребуется переименовать или перенести
`retrospectives/TASK-0001-retrospective.md`, это должно быть отдельным решением
человека, потому что файл является историческим разбором и может использоваться
как ссылка на прошлую задачу.

## Placeholder / reserved / retired

### Placeholder

- `editorial_knowledge/02_editorial_intent.md` — содержит только каркас разделов, не содержит активных правил.
- `editorial_knowledge/03_usefulness_review.md` — содержит только каркас разделов, не содержит активных правил.

### Reserved

- `ai-editorial-office/README.md` — зарезервированная верхняя навигация, не активный регламент.
- `ai-editorial-office/kb/good_examples.md` — зарезервирован для будущих хороших примеров, сейчас не содержит активных правил.
- `ai-editorial-office/kb/bad_examples.md` — зарезервирован для будущих плохих примеров, сейчас не содержит активных правил.
- `editorial_knowledge/cases/CASE_TEMPLATE.md` — заготовка для будущих кейсов, не активное правило и не активный пример.

### Retired

- Не обнаружено и не помечено.

## Кандидаты на удаление

Кандидатов на удаление содержательных файлов не выделено. Пустые и каркасные
файлы сохранены с безопасной пометкой, потому что их назначение может быть
полезно в будущем.

## Служебный шум

Найдены `.DS_Store` в корне, `ai-editorial-office/`, `ai-editorial-office/tasks/`,
отдельных task-папках, `ai-editorial-office/templates/`, `editorial_knowledge/`
и `retrospectives/`.

Выполнено: `.DS_Store` удалены, `.DS_Store` добавлен в `.gitignore`.

Других очевидных служебных файлов `Thumbs.db`, `desktop.ini`, `__pycache__` или
`*.pyc` не найдено.

Также найден файл `about/editorial-structure-ordering-recommendations.md`,
который сам был помечен как read-only audit note вне 20-файлового ChatGPT memory
package, но физически лежал внутри `/about` и ломал
`check_about_memory_package.sh`.

Выполнено: файл перенесён в
`retrospectives/editorial-structure-ordering-recommendations-2026-06-03.md` как
исторический системный аудит. После переноса проверка `/about` проходит:
20 файлов, copied files match canonical sources.

## Изменённые файлы

### Созданы

- `.gitignore`
- `retrospectives/README.md`
- `ai-editorial-office/tasks/README.md`
- `ai-editorial-office/learn/README.md`
- `ai-editorial-office/tests/README.md`
- `ai-editorial-office/scripts/README.md`
- `editorial_knowledge/00_index.md`
- `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0018/task-manifest.md`
- `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0018/orchestration_plan.md`
- `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0018/status.md`
- `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0018/structure-cleanup-report.md`

### Обновлены

- `ai-editorial-office/README.md`
- `ai-editorial-office/kb/good_examples.md`
- `ai-editorial-office/kb/bad_examples.md`
- `editorial_knowledge/02_editorial_intent.md`
- `editorial_knowledge/03_usefulness_review.md`
- `editorial_knowledge/cases/CASE_TEMPLATE.md`

### Перенесены

- `about/editorial-structure-ordering-recommendations.md` -> `retrospectives/editorial-structure-ordering-recommendations-2026-06-03.md`

### Удалены как служебный шум

- `.DS_Store`
- `ai-editorial-office/.DS_Store`
- `ai-editorial-office/tasks/.DS_Store`
- `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0004/.DS_Store`
- `ai-editorial-office/tasks/TASK-0003/.DS_Store`
- `ai-editorial-office/tasks/TASK-0018/.DS_Store`
- `ai-editorial-office/tasks/TASK-0019/.DS_Store`
- `ai-editorial-office/tasks/TASK-0020/.DS_Store`
- `ai-editorial-office/templates/.DS_Store`
- `editorial_knowledge/.DS_Store`
- `retrospectives/.DS_Store`
- `retrospectives/0001/.DS_Store`
- `retrospectives/0002/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0005/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0006/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0007/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0010/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0011/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0011-1/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0012/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0013-1/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0014/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0014-1/.DS_Store`
- `retrospectives/system-maintenance-retrospective-0015/.DS_Store`

## Вопросы и решения для человека

- Заполнять ли `good_examples.md` и `bad_examples.md` реальными примерами в отдельной будущей задаче.
- Оставлять ли `editorial_knowledge/02_editorial_intent.md` и `editorial_knowledge/03_usefulness_review.md` как каркасы или позже слить/удалить их после отдельного решения.
- Добавлять ли реальные integrity checks в `ai-editorial-office/tests/` после этой структурной очистки.
- Нужно ли когда-нибудь переименовывать исторический `retrospectives/TASK-0001-retrospective.md`; сейчас перенос не требуется.
