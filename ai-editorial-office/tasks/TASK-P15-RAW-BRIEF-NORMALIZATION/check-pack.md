# Check pack

## Краткая суть изменения

P1.5 реализован как точечный update Intake Agent: сырой пользовательский запрос
теперь нормализуется в рабочий `brief.md` / task definition через явное
разделение фактов, assumptions, questions, unknown, source status и noise.

## Список изменённых файлов

- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/ideas/master_backlog.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/brief.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/task-manifest.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/orchestration_plan.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/status.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/implementation-notes.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/check-pack.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/chatgpt_report.md`

## Git diff summary

```text
ai-editorial-office/agents/intake_agent.md  | 242 +++++++++++++++++++++++-----
ai-editorial-office/ideas/master_backlog.md |  31 +++-
2 files changed, 231 insertions(+), 42 deletions(-)
```

Task-local files are untracked because `ai-editorial-office/tasks/` already
contains untracked local task materials.

## Ключевые фрагменты изменённых файлов

`intake_agent.md`:

- adds `Normalization pass` with task signal / background context / noise;
- adds conservative field labels: `confirmed`, `inferred`, `unknown`,
  `assumption`, `question`;
- adds explicit source status labels and active-source guard;
- adds working normalization shape for `brief.md`, `task-manifest.md`, or
  intake handoff;
- adds ask-vs-proceed rules;
- adds hard limits against invented goals, audiences, sources, requirements,
  roles, pipelines, validators, and mandatory artifacts;
- adds three sanitized examples.

`master_backlog.md`:

- P1.5 status changed from `planned` to `implemented`;
- added implementation result;
- added decision/retrospective entry dated 2026-06-09.

## Риски

- Intake guidance became longer; reviewer should confirm it remains readable.
- Examples must remain guidance, not mandatory artifact shape.
- `/about` sync check fails because `/about` is absent in this checkout.

## Manual check

- `rg` confirmed the new Raw Brief Normalization sections and source-status
  examples exist in `intake_agent.md`.
- `rg` confirmed P1.5 is `implemented` and journal entry exists in
  `master_backlog.md`.
- `git diff --check` passed with no whitespace errors.
- `/about` check failed before comparison because `/about` directory is absent:
  `FAIL: /about contains 0 files; expected 20.`

## Что нужно прислать ChatGPT на ревью

- `git diff -- ai-editorial-office/agents/intake_agent.md ai-editorial-office/ideas/master_backlog.md`
- this `check-pack.md`
- `implementation-notes.md`
- `chatgpt_report.md`
