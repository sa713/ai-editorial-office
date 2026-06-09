# ChatGPT P2 Report

## git diff summary

Tracked diff:

```text
ai-editorial-office/agents/chief_editor.md  | 35 +++++++++++++++++++++++++++++
ai-editorial-office/ideas/master_backlog.md | 30 ++++++++++++++++++++++++-
ai-editorial-office/kb/00_index.md          |  3 +++
3 files changed, 67 insertions(+), 1 deletion(-)
```

New production file, still untracked:

```text
ai-editorial-office/kb/codex_task_standard.md | 198 +++++++++++++++++++++
1 file changed, 198 insertions(+)
```

## changed files

Production files:

- `ai-editorial-office/kb/codex_task_standard.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/ideas/master_backlog.md`

Task-local review packet:

- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/brief.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/task-manifest.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/orchestration_plan.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/status.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/implementation-notes.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/check-pack.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/chatgpt_p2.md`

## key fragments

### `kb/codex_task_standard.md`

Owner and chain:

```md
raw request -> normalized brief -> Codex task -> implementation -> check-pack -> review
```

```md
- Intake Agent owns raw request -> normalized brief.
- Chief Editor owns normalized brief -> Codex task and check-pack contract.
- Codex executes only within the task boundaries.
- Review remains separate when the result requires review.
```

Task shape:

```md
# Задача для Codex

## Цель
## Контекст
## Рабочая зона
## Source of truth
## Что можно менять
## Что нельзя менять
## Глубина работы
## Acceptance criteria
## Формат результата
## Что прислать на проверку
```

Check-pack shape:

```md
# Check pack

## Краткая суть изменения
## Список изменённых файлов
## Git diff summary
## Ключевые фрагменты изменённых файлов
## Риски
## Что нужно прислать ChatGPT на ревью
```

Boundary:

```md
Do not turn check-pack into a duplicate of the full diff, a long report, a
review verdict, or a replacement for `review.md` when review is required by the
selected pipeline.
```

### `chief_editor.md`

```md
When the next step is to ask Codex to inspect files, modify files, implement a
system patch, or prepare a reviewable local change, Chief Editor owns the
conversion from normalized brief to Codex task.
```

```md
This standard extends the normalized brief into an execution request. It must
not invent requirements, source files, implementation strategy, roles,
pipelines, validators, capabilities, or review outcomes. It does not replace
task-local routing, selected pipelines, `review.md`, or final governance.
```

### `kb/00_index.md`

```md
- `codex_task_standard.md` gives practical guidance for turning a normalized
  brief into a compact Codex task and check-pack. It does not create a new role,
  pipeline, capability pack, validator, or mandatory artifact.
```

### `master_backlog.md`

```md
Статус: `implemented`
```

```md
- добавлен `kb/codex_task_standard.md` как компактный reusable standard;
- `chief_editor` закреплён как владелец перехода normalized brief -> Codex
  task / check-pack contract;
- `generate_task_pack.py` оставлен read-only context helper, не orchestrator и
  не генератор Codex-задач;
- цепочка зафиксирована как
  `raw request -> normalized brief -> Codex task -> implementation -> check-pack -> review`;
```

## implementation-notes.md

````md
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
````

## check-pack.md

````md
# Check pack

## Краткая суть изменения

P2 реализован как compact production standard: normalized brief теперь имеет
явный путь в Codex task, а результат изменений — в короткий check-pack для
ревью.

## Список изменённых файлов

- `ai-editorial-office/kb/codex_task_standard.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/ideas/master_backlog.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/brief.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/task-manifest.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/orchestration_plan.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/status.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/implementation-notes.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/check-pack.md`
- `ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD/chatgpt_p2.md`

## Git diff summary

```text
ai-editorial-office/agents/chief_editor.md  |  35 +++++++
ai-editorial-office/ideas/master_backlog.md |  30 +++++-
ai-editorial-office/kb/00_index.md          |   3 +
3 tracked files changed, 67 insertions(+), 1 deletion(-)

ai-editorial-office/kb/codex_task_standard.md | 198 +++++++++++++++++++++
1 untracked production file, 198 insertions(+)
```

## Ключевые фрагменты изменённых файлов

- `kb/codex_task_standard.md`: defines chain, owner, Codex task shape,
  check-pack shape, rules, and examples.
- `chief_editor.md`: Chief Editor owns normalized brief -> Codex task/check-pack
  contract and must use the KB standard.
- `kb/00_index.md`: indexes the new reusable standard and its boundaries.
- `master_backlog.md`: P2 is `implemented`, with result and decision-log entry.

## Риски

- Check-pack could be misread as a replacement for `review.md`; KB and Chief
  Editor explicitly forbid that.
- The standard could be overused for ordinary editorial tasks; it is scoped to
  Codex-ready execution requests and review support.
- `/about` sync cannot pass because `/about` is absent in this checkout.

## Manual check / smoke-test results

- `rg` confirmed Codex task shape, Check Pack shape, chain, owner, and examples
  in `kb/codex_task_standard.md`.
- `rg` confirmed Chief Editor, KB index, and backlog references.
- `git diff --check` passed for tracked changes.
- trailing-whitespace scan passed for the new KB file and P2 task-local files.
- `/about` check failed because `/about` is absent in this checkout:
  `FAIL: /about contains 0 files; expected 20.`

## Что нужно прислать ChatGPT на ревью

- production diff for the four changed production files;
- this `check-pack.md`;
- `implementation-notes.md`;
- `chatgpt_p2.md`;
- manual check results.
````

## manual check results

Commands run:

```text
rg -n 'Codex task shape|Check Pack shape|raw request -> normalized brief -> Codex task|brief -> Codex task|brief -> Check Pack|generate_task_pack.py' ai-editorial-office/kb/codex_task_standard.md
rg -n 'Codex Task Standard|codex_task_standard.md|P2 —|Статус: `implemented`|P2 Codex Task Standard' ai-editorial-office/agents/chief_editor.md ai-editorial-office/kb/00_index.md ai-editorial-office/ideas/master_backlog.md
git diff --check
rg -n '[ \t]+$' ai-editorial-office/kb/codex_task_standard.md ai-editorial-office/tasks/TASK-P2-CODEX-TASK-STANDARD || true
ai-editorial-office/scripts/check_about_memory_package.sh
```

Results:

- Standard sections found: chain, owner, Codex task shape, Check Pack shape,
  and examples.
- Chief Editor, KB index, and backlog references found.
- `git diff --check` passed for tracked changes.
- trailing-whitespace scan passed for the new KB and P2 task-local files.
- `/about` check failed because `/about` is absent in this checkout:

```text
find: /Users/sa/Projects/ai-editorial-office-github/about: No such file or directory
FAIL: /about contains 0 files; expected 20.
```

## git status --short

```text
 M ai-editorial-office/agents/chief_editor.md
 M ai-editorial-office/ideas/master_backlog.md
 M ai-editorial-office/kb/00_index.md
?? ai-editorial-office/kb/codex_task_standard.md
?? ai-editorial-office/tasks/
?? diff_intake.md
```
