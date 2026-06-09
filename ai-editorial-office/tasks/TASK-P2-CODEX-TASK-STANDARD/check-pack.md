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
