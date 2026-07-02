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
