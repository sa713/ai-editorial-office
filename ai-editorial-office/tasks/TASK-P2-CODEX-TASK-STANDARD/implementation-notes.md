# Implementation notes

## Что изменено

- Добавлен `ai-editorial-office/kb/codex_task_standard.md`.
- Обновлён `ai-editorial-office/agents/chief_editor.md`.
- Обновлён `ai-editorial-office/kb/00_index.md`.
- Обновлён `ai-editorial-office/ideas/master_backlog.md`.

## Почему именно так

- Chief Editor уже владеет routing, preflight, role assignment и execution
  contract, поэтому он является production owner для перехода normalized brief
  -> Codex task/check-pack.
- KB подходит для компактного reusable standard без добавления роли, пайплайна
  или governance layer.
- `generate_task_pack.py` оставлен read-only helper, потому что он формирует
  read set, а не Codex task.

## Какие файлы затронуты

- `ai-editorial-office/kb/codex_task_standard.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/ideas/master_backlog.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/*`

## Что не делал

- Не добавлял новых агентов, ролей, пайплайнов, validators или capability packs.
- Не менял review-gate.
- Не менял intake rules P1.5.
- Не менял `generate_task_pack.py`.
- Не создавал обязательный check-pack для каждой редакционной задачи.
- Не создавал `/about`, потому что директория отсутствует в checkout.

## Как проверить

- Проверить, что `kb/codex_task_standard.md` содержит compact Codex task shape,
  check-pack shape, chain и examples.
- Проверить, что `chief_editor.md` ссылается на стандарт и не расширяет роли.
- Проверить, что backlog P2 имеет статус `implemented` и запись в журнале.
- Проверить, что `git diff --check` проходит.
