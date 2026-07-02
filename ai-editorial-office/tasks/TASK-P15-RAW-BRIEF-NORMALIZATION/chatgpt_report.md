# ChatGPT report

## git diff summary

```text
ai-editorial-office/agents/intake_agent.md  | 242 +++++++++++++++++++++++-----
ai-editorial-office/ideas/master_backlog.md |  31 +++-
2 files changed, 231 insertions(+), 42 deletions(-)
```

## changed files

Production files:

- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/ideas/master_backlog.md`

Task-local review packet:

- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/brief.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/task-manifest.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/orchestration_plan.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/status.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/implementation-notes.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/check-pack.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/chatgpt_report.md`

Note: `ai-editorial-office/tasks/` already contains unrelated untracked local
task folders. They were not modified intentionally.

## key fragments from changed production files

### `ai-editorial-office/agents/intake_agent.md`

Raw Brief now covers noisy natural-language input:

```md
A Raw Brief is a natural-language user request that may contain task signal,
emotion, incomplete context, examples, corrections, chat history, and noise.
```

Normalization separates signal from context and noise:

```md
Intake Agent separates the raw request into:

- task signal: requested action, deliverable, audience, channel/context,
  supplied source material, constraints, examples, acceptance cues, and
  explicit exclusions;
- background context: why the user needs the task, prior attempts, process
  comments, deadline pressure, or surrounding conversation;
- noise: repeated wording, frustration, jokes, side comments, abandoned ideas,
  and unrelated chat fragments.
```

Brief fields must be classified:

```md
- `confirmed` — explicitly stated by the user or present in supplied material;
- `inferred` — safely recovered from wording or immediate task context without
  changing the task;
- `unknown` — not provided and not safely recoverable;
- `assumption` — a bounded, reviewable working choice needed to continue;
- `question` — missing information that can materially change routing or output.
```

Source status is explicit and conservative:

```md
Source status must be explicit. Use the narrowest truthful label, such as:

- `provided/attached and available`;
- `linked but not yet reviewed`;
- `mentioned but not provided`;
- `expected later`;
- `unavailable`;
- `unknown`.
```

The guidance is not a new mandatory artifact:

```md
Use this shape as guidance for `brief.md`, `task-manifest.md`, or the intake
handoff. It is not a new mandatory standalone artifact.
```

Hard limits preserve scope:

```md
- Do not invent goals, audiences, sources, facts, events, requirements, product
  behavior, approval needs, or acceptance criteria.
- Do not turn user emotion into a requirement without explicit support.
- Do not treat a mentioned, linked, or attached source as active until source
  status is clear.
- Do not expand the task beyond the user's request to make the brief look
  complete.
- Do not create new roles, pipelines, capabilities, validators, or mandatory
  artifacts for normalization.
- Do not weaken review-gate or Chief Editor routing.
- Do not turn assumptions into facts.
```

Three sanitized examples were added:

- noisy follow-up email request;
- incomplete urgent post request with questions/assumptions;
- source-bound FAQ request with explicit source status.

### `ai-editorial-office/ideas/master_backlog.md`

P1.5 status changed:

```md
### P1.5 — raw brief normalization

Статус: `implemented`
```

Implementation result added:

```md
- `intake_agent.md` расширен правилом raw brief normalization;
- закреплено различение task signal, background context, noise, facts,
  assumptions, questions и unknown;
- добавлен guidance-шаблон нормализации без нового обязательного артефакта;
- добавлены sanitized examples для noisy, incomplete и source-bound requests;
- source status должен фиксироваться явно до source-dependent production.
```

Decision log entry added:

```md
### 2026-06-09 — P1.5 raw brief normalization

Сделано:

- усилен `intake_agent.md`: сырой пользовательский запрос теперь
  нормализуется в рабочий `brief.md` / task definition через явное разделение
  task signal, background context и noise;
- добавлены статусы `confirmed`, `inferred`, `unknown`, `assumption` и
  `question` для полей brief;
- source status закреплён как обязательная явная часть нормализации;
- добавлен compact guidance-шаблон и три sanitized examples;
- новые роли, пайплайны, capabilities, validators и обязательные артефакты не
  добавлялись.
```

## implementation-notes.md

```md
# Implementation notes

## Что изменено

- В `ai-editorial-office/agents/intake_agent.md` расширен раздел
  `Raw Brief Normalization`.
- В `ai-editorial-office/ideas/master_backlog.md` статус P1.5 обновлён на
  `implemented`, добавлен результат и запись в журнал решений.

## Почему именно так

- `intake_agent.md` уже является ближайшим production owner для превращения
  сырого запроса в рабочий brief/task definition.
- Новый блок сделан guidance/example, а не новым обязательным standalone
  artifact.
- Backlog обновлён как planning/status artifact, но не становится production
  source of truth.

## Какие файлы затронуты

- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/ideas/master_backlog.md`
- `ai-editorial-office/tasks/TASK-P15-RAW-BRIEF-NORMALIZATION/*`

## Что не делал

- Не добавлял новых агентов, пайплайнов, capabilities или validators.
- Не менял review-gate.
- Не менял клиентские профили, включая Sber-mode.
- Не трогал visual subsystem.
- Не создавал новый обязательный артефакт для каждой задачи.
- Не создавал `/about`, потому что директория отсутствует в checkout и её
  восстановление было бы более широким memory-package изменением.

## Как проверить

- Проверить, что `Raw Brief Normalization` в `intake_agent.md` описывает
  разделение task signal / background context / noise.
- Проверить, что поля brief могут быть `confirmed`, `inferred`, `unknown`,
  `assumption` или `question`.
- Проверить, что source status фиксируется явно.
- Проверить, что hard limits запрещают выдумывать цели, аудитории, источники и
  требования.
- Проверить, что P1.5 в backlog имеет статус `implemented` и журнал решений.
```

## check-pack.md

````md
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
````

## manual check / smoke-test results

Commands run:

```text
rg -n "Raw Brief Normalization|Normalization pass|Working normalization shape|Sanitized examples|Do not invent goals|source status" ai-editorial-office/agents/intake_agent.md
rg -n 'P1\.5|Статус: `implemented`|2026-06-09 — P1\.5 raw brief normalization|source status' ai-editorial-office/ideas/master_backlog.md
ai-editorial-office/scripts/check_about_memory_package.sh
git diff --stat
git diff --check
git status --short
```

Results:

- Intake check passed: key normalization sections, hard limits, examples, and
  source-status references are present.
- Backlog check passed: P1.5 is `implemented`; decision log entry exists.
- Diff summary generated successfully.
- `git diff --check` passed with no whitespace errors.
- `/about` check failed because `/about` is absent in this checkout:

```text
find: /Users/sa/Projects/ai-editorial-office-github/about: No such file or directory
FAIL: /about contains 0 files; expected 20.
```

Interpretation: production patch is complete; memory-package sync/check cannot
be completed without restoring or providing `/about`. This report does not
invent or recreate the missing memory package.

## current git status --short

```text
 M ai-editorial-office/agents/intake_agent.md
 M ai-editorial-office/ideas/master_backlog.md
?? ai-editorial-office/tasks/
```
