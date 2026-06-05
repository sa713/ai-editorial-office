# Scripts

Эта папка хранит служебные скрипты проекта.

Она существует для небольших проверок и вспомогательных операций, которые
поддерживают структуру редакции, но не заменяют редакционный процесс.

Статус папки: активная служебная зона. Скрипты можно запускать по необходимости,
если задача требует проверки соответствующего участка проекта.

Читайте эту папку, когда нужно понять, какие локальные проверки уже есть, как их
запускать и что они проверяют.

Не читайте её как источник редакционных правил, ролей, статусов, пайплайнов или
governance. Скрипты должны проверять уже заданные правила, а не создавать новые.

Содержимое `scripts/` не определяет активные правила системы. Канонические
правила остаются в `ai-editorial-office/AGENTS.md` и других владельцах,
указанных в нём.

## Существующие скрипты

### `validate_task_lifecycle.py`

Назначение: локально проверяет базовые structural/governance ошибки task
package: обязательные `task-manifest.md` и `status.md`, наличие review перед
`final.md`, распознаваемый review outcome, запрет финализации без `approved`,
consistency current status между manifest/status и наличие выбранного pipeline
файла. Если в `status.md` есть previous/current status, валидатор проверяет
transition по `kb/task_statuses.md`.

Дополнительно валидатор мягко сверяет найденный current status с
`kb/task_statuses.md`: unknown status даёт warning, не blocker. Missing selected
pipeline тоже warning; selected pipeline без файла в `pipelines/` — blocker.
Missing previous status и одинаковые previous/current status дают warning.
Invalid known transition даёт blocker, а `blocked` -> `finalized` запрещён
отдельным guard.

Запуск:

```bash
python3 ai-editorial-office/scripts/validate_task_lifecycle.py PATH_TO_TASK_FOLDER
```

Скрипт выводит blockers, warnings и итоговый `PASS` или `FAIL`. Exit code `0`
означает отсутствие blockers, `1` — blockers найдены, `2` — ошибка запуска или
пути.

Скрипт только читает task folder и не меняет файлы. Он проверяет уже заданные
правила из canonical sources, но не создаёт новые правила lifecycle.

### `check_about_memory_package.sh`

Назначение: проверяет служебный пакет памяти `/about` для ChatGPT.

Когда запускать: после изменений в `/about`, после обновления файлов, копии
которых лежат в `/about`, или перед передачей изменений, связанных с memory
package.

Что делает: проверяет, что в `/about` ровно 20 файлов, и сравнивает копии
канонических файлов с их источниками в `ai-editorial-office/`.
