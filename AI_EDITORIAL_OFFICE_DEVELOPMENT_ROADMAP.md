# Roadmap развития ИИ-редакции

Статус документа: `active roadmap`  
Дата создания: 2026-06-04  
Назначение: planning/backlog document, чтобы не терять контекст развития ИИ-редакции между чатами, Codex-задачами и локальными изменениями.

Этот файл фиксирует 10 направлений развития, которые мы восстановили после апдейта `Sber-mode`.  
Он не заменяет `AGENTS.md`, production-файлы, пайплайны, роли или task artifacts. Это навигационная карта развития, а не canonical governance source.

## Как пользоваться этим файлом

1. Перед новым системным апдейтом открывать этот файл и выбирать один раздел.
2. Не смешивать несколько больших направлений в одном PR, если это не инфраструктурно необходимо.
3. Для каждого шага заводить отдельную ветку и отдельную Codex-задачу.
4. После выполнения обновлять статус раздела: `planned`, `in_progress`, `done`, `paused`, `rejected`.
5. После каждого системного апдейта проверять:
   - production-файлы;
   - `/about` memory package;
   - роли;
   - пайплайны;
   - smoke-tests или ручные acceptance checks.
6. Не складывать этот roadmap в `/about`, если это нарушит правило 20 файлов. `/about` — compact memory package для ChatGPT, а не backlog.
7. Если roadmap расходится с `AGENTS.md` или production-файлами, приоритет у production-файлов и `AGENTS.md`.

## Текущая база

Уже сделано:

- добавлен `client_profile: sber`;
- Сбер подключён как изолированный task-scoped client profile;
- редполитика Сбера не стала глобальной политикой ИИ-редакции;
- production templates получили поля client profile;
- article/social/UX/review pipelines умеют загружать client-profile files только когда профиль активен;
- роли intake/chief/writer/ux_writer/review/final_editor знают про active client profile;
- `/about` синхронизирован и проверен;
- safe-core ИИ-редакции опубликован в repo `sa713/ai-editorial-office`;
- repo сейчас public;
- в GitHub repo попало только безопасное ядро без `tasks/`, `learn/`, `kb/clients/`, `/about`, `editorial_knowledge/`, `retrospectives/`, binary/source files и реальных рабочих материалов;
- работа с safe core идёт маленькими ветками и PR;
- ChatGPT теперь может читать публичный repo/PR через GitHub connector;
- локальные diff/review pack остаются fallback;
- добавлен `CONTRIBUTING.md` через PR #1;
- добавлен MVP task lifecycle validator через PR #2;
- добавлен compact execution guidance через PR #3;
- task lifecycle validator расширен status/pipeline checks через PR #4.

Следующая логика развития: не добавлять сразу новые клиентские режимы, а сделать редакцию удобнее, компактнее и проверяемее в ежедневной локальной работе.

---

# Приоритетный порядок

Рекомендуемый порядок работы:

1. Validation layer.
2. Compact execution tuning.
3. Task lifecycle validators.
4. Feedback loop.
5. Preflight Gate examples and tests.
6. Source/provenance framework.
7. Task pack generator.
8. Research Pipeline hardening.
9. Future roles decision.
10. Visual subsystem decision.

Статус первых направлений:

- пункт 1 уже начат через MVP validator и smoke-tests;
- пункт 2 уже начат через compact execution guidance;
- пункт 3 уже начат через status/pipeline checks в lifecycle validator.

Следующий кандидат:

- дальнейшее расширение lifecycle validator до transition checks;
- или Preflight Gate examples and tests.

Порядок можно менять, но лучше не начинать future roles и visual subsystem до того, как появятся валидаторы и compact execution.

---

# 1. Автоматические валидаторы

Статус: `in_progress`  
Приоритет: `P1`  
Тип апдейта: tooling / governance automation

## Идея

Сейчас редакция многое проверяет вручную: есть ли нужные артефакты, валидны ли статусы, не нарушен ли review-gate, не потерян ли handoff, не появились ли факты без источников.

Нужно добавить слой локальных проверок, чтобы система сама ловила структурные ошибки до review или merge.

## Почему это важно

Редакция уже стала сложной. Без автоматических проверок она может:

- пропустить обязательный `review.md`;
- забыть обновить `task-manifest.md`;
- перейти в неправильный статус;
- создать лишние артефакты;
- финализировать материал без достаточного review trail;
- потерять active client profile;
- перепутать текущую версию артефакта.

## Что хотим получить

Набор скриптов или единая команда проверки, которая валидирует task package и системные файлы.

Возможные проверки:

- artifact existence validator;
- status transition validator;
- handoff validator;
- review-gate validator;
- claim coverage checker;
- forbidden pattern scanner;
- finalization diff checker;
- source metadata checker;
- retrospective metrics collector.

## Выполнено

- добавлен read-only `ai-editorial-office/scripts/validate_task_lifecycle.py`;
- добавлен smoke-test runner `ai-editorial-office/tests/test_task_lifecycle_validator.sh`;
- добавлены synthetic fixtures в `ai-editorial-office/tests/fixtures/task_lifecycle/`;
- проверяются required files `task-manifest.md` и `status.md`;
- проверяется review-gate: `review.md` должен существовать перед `final.md`;
- проверяется review outcome: `approved`, `changes_requested` или `blocked`;
- проверяется finalization gate: `final.md` не проходит без approved review;
- ambiguous outcome вроде `not approved` не считается approved outcome;
- smoke-test проходит.

## Осталось

- handoff validator;
- claim coverage checker;
- forbidden pattern scanner;
- finalization diff checker;
- source metadata checker;
- retrospective metrics collector;
- аккуратная интеграция с `/about` check, если понадобится.

## Возможная Codex-задача

```text
Add local validation scripts for AI Editorial Office task lifecycle.
```

## Acceptance criteria

- Есть локальный валидатор task package.
- Валидатор не требует remote.
- Валидатор можно запускать локально.
- Ошибки выводятся понятным списком.
- Валидатор не меняет файлы автоматически.
- Валидатор не создаёт новые правила, а проверяет уже существующие.
- `/about` check остаётся отдельной или встроенной проверкой.

## Риски

- Не превратить валидатор в новую бюрократию.
- Не заставлять low-risk задачи создавать лишние файлы.
- Не дублировать весь `AGENTS.md` в коде.
- Не делать проверку слишком жёсткой для legacy tasks.

---

# 2. Уменьшить бюрократию в обычных задачах

Статус: `in_progress`  
Приоритет: `P1`  
Тип апдейта: workflow simplification

## Идея

Система безопасная, но иногда слишком тяжёлая. Для простых задач не всегда нужны отдельные `qa-checklist.md`, `review-summary.md`, `finalization-notes.md`, `open-questions.md` и другие поддерживающие файлы.

Нужно довести compact execution до реально удобного режима.

## Почему это важно

Если редакция создаёт слишком много файлов для простой задачи, пользователь начинает воспринимать процесс как тормоз. При этом review нельзя убирать.

Нужен баланс:

```text
меньше служебного веса
без потери review, traceability и restartability
```

## Что хотим получить

Ясное правило:

- low-risk task → минимальный набор;
- simple standard task → компактный набор;
- high-governance task → полный набор.

## Возможный минимальный набор для low-risk

```text
brief.md
task-manifest.md
status.md
orchestration_plan.md, если нужен routing
draft.md или ux-copy.md
review.md
final.md
final_decision.md
```

Некоторые handoff можно не создавать, если `task-manifest.md`, текущий артефакт и `review.md` дают достаточно delta context.

## Выполнено

- добавлен `ai-editorial-office/kb/compact_execution.md`;
- добавлены synthetic compact examples в `ai-editorial-office/tests/compact_execution_examples.md`;
- article/social/UX/review pipelines получили короткие ссылки на compact execution guidance;
- review-gate сохранён;
- `review.md` перед finalization остаётся обязательным;
- optional artifacts не стали обязательными;
- high-governance задачи не предлагается чрезмерно сокращать.

## Осталось

- проверить compact execution на реальной low-risk задаче;
- уточнить, когда rationale может жить в `task-manifest.md` или `status.md`, а когда нужен отдельный `orchestration_plan.md`;
- при необходимости добавить smoke-test/checklist для compact vs expanded.

## Возможная Codex-задача

```text
Tune compact execution rules and examples for low-risk editorial tasks.
```

## Acceptance criteria

- Compact execution не удаляет review.
- Optional artifacts не становятся обязательными.
- В пайплайнах есть понятные примеры compact vs expanded.
- Chief Editor обязан записывать rationale, если сокращает набор артефактов.
- Review Agent может проверить compact task без дополнительных файлов.
- Finalization может быть компактной, если review approved и manifest актуален.

## Риски

- Перепутать compact с “можно без проверки”.
- Слишком сильно сократить traceability.
- Сделать compact неявным и непроверяемым.

---

# 3. Task lifecycle validators вместо ручного ревью структуры

Статус: `in_progress`  
Приоритет: `P1`  
Тип апдейта: lifecycle control

## Идея

Раздел 1 — общий validation layer. Этот раздел — конкретный lifecycle-MVP: статусы, переходы, review-gate, finalization-gate.

Нужно, чтобы система могла проверить задачу как state machine.

## Что проверять

- У задачи есть `task-manifest.md`.
- У задачи есть `status.md`.
- Выбранный pipeline существует.
- Текущий статус входит в допустимые статусы.
- Переход статуса допустим.
- `review.md` существует перед finalization.
- `final.md` не создан до approved review.
- `final_decision.md` создаётся только на Chief Editor governance stage.
- `task-manifest.md` содержит актуальный current status.
- Если `client_profile` активен, указаны client-profile files.
- Если `client_profile: sber`, статус не противоречит наличию источника.

## Выполнено

- валидатор проверяет status consistency между `task-manifest.md` и `status.md`;
- missing current status в `task-manifest.md` — blocker;
- missing current status в `status.md` — warning;
- status mismatch — blocker;
- unknown status — warning;
- selected pipeline existence проверяется через `ai-editorial-office/pipelines/`;
- missing selected pipeline — warning;
- unknown selected pipeline — blocker;
- smoke-test расширен.

## Осталось

- transition validator;
- finalization-gate deep checks;
- более предсказуемый parser для `task_statuses.md` или явный источник статусов;
- проверки `client_profile` consistency;
- проверка `final_decision.md` stage/ownership;
- smoke-tests на valid/invalid transitions.

## Возможная Codex-задача

```text
Add task lifecycle validator for statuses, review gate, and finalization gate.
```

## Acceptance criteria

- Валидатор читает task folder.
- Валидатор сообщает ошибки, но не исправляет их автоматически.
- Валидатор различает blocker и warning.
- Валидатор не требует всех optional artifacts.
- Валидатор учитывает compact execution.
- Есть smoke-test на валидную и невалидную задачу.

## Риски

- Слишком жёсткая проверка legacy tasks.
- Смешивание governance rules и task-type rules.
- Дублирование `task_statuses.md` вместо чтения его как источника.

---

# 4. Feedback loop

Статус: `planned`  
Приоритет: `P2`  
Тип апдейта: learning loop / governance

## Идея

Реакции пользователя после доставки результата должны фиксироваться как сигналы, но не должны автоматически менять систему.

Системная цепочка:

```text
single feedback
↓
repeated signal
↓
validated pattern
↓
system change proposal
↓
separate reviewed system update
```

## Почему это важно

ИИ-редакция должна учиться на повторяющихся проблемах, но не должна менять правила из-за одного замечания.

## Что хотим получить

- `feedback.md` для task-local реакции пользователя;
- `/kb/feedback_patterns.md` для повторяющихся сигналов;
- шаблон `system_change_proposal.md`;
- правило: Chief Editor решает, является ли feedback:
  - task-local note;
  - bounded revision;
  - new task;
  - possible system pattern.

## Возможная Codex-задача

```text
Add feedback capture and system change proposal workflow.
```

## Acceptance criteria

- Feedback не создаётся, если реакции пользователя нет.
- Feedback не переоткрывает задачу автоматически.
- Один feedback не меняет систему.
- Repeated pattern фиксируется отдельно.
- System change proposal проходит review как системный апдейт.
- Feedback loop не создаёт новую обязательную роль.

## Риски

- Превратить каждую правку пользователя в “ошибку системы”.
- Слишком быстро менять правила.
- Засорить `/kb` сырыми отзывами.

---

# 5. Preflight Gate: меньше лишних вопросов

Статус: `in_progress`
Приоритет: `P2`  
Тип апдейта: intake/orchestration quality

## Идея

Intake не должен превращаться в анкету. Система должна сначала восстановить очевидный контекст, а потом Chief Editor выбирает стратегию:

```text
ask
constrain
proceed
block
```

Первые examples и smoke-test для Preflight Gate добавлены. Дальше их нужно
проверить на реальном intake-сценарии и при необходимости автоматизировать.

## Почему это важно

Пользователь часто даёт короткий рабочий запрос. Редакция не должна отвечать длинным списком уточнений, если можно безопасно начать с разумными ограничениями.

## Что хотим получить

Набор routing examples:

- “нужен пост про релиз” → proceed или constrain;
- “юридическое уведомление клиентам” → ask/block/high-governance;
- “пуш для Сбера” → proceed/constrain + `client_profile: sber`;
- “статья про Сбер как кейс рынка” → proceed/constrain + `client_profile: none`;
- “UX-текст для ошибки оплаты” → UX pipeline + product-context check.

## Выполнено

- добавлены synthetic Preflight Gate examples в `ai-editorial-office/tests/preflight_gate_examples.md`;
- добавлен markdown smoke-test `ai-editorial-office/tests/preflight_gate_smoke_test.md`;
- покрыты decisions `ask`, `constrain`, `proceed`, `block`;
- покрыты Sber activation и Sber non-activation examples;
- покрыты UX/high-governance examples.

## Осталось

- проверить examples на реальной intake-задаче;
- при необходимости добавить automated checker;
- уточнить связь с `task-manifest.md` и `orchestration_plan.md`;
- добавить more edge cases after real usage.

## Возможная Codex-задача

```text
Test Preflight Gate examples on a real intake task and decide whether to add an automated checker.
```

## Acceptance criteria

- Intake сначала нормализует raw brief.
- Chief Editor не задаёт вопросы автоматически.
- `ask` используется только при действительно критическом пробеле.
- `constrain` используется, когда можно безопасно ограничить задачу.
- `proceed` используется, когда данных достаточно.
- `block` используется для небезопасных или противоречивых задач.
- Есть тесты на Sber activation и non-activation.

## Риски

- Слишком много уточнений.
- Слишком смелые допущения.
- Подмена пользовательской цели “разумной реконструкцией”.

---

# 6. Future roles: решить, какие роли действительно нужны

Статус: `planned`  
Приоритет: `P3`  
Тип апдейта: role architecture

## Идея

В проекте уже упоминаются возможные будущие роли:

- `future_style_editor`;
- `future_structural_editor`;
- `future_terminology_reviewer`;
- `future_fact_checker`.

Сейчас они не являются core roles. Их нельзя включать по умолчанию.

## Почему это важно

Нельзя плодить роли без доказанной необходимости. Иначе система станет сложнее, но не качественнее.

## Что хотим понять

- Часто ли Review Agent перегружен фактчекингом?
- Часто ли Review Agent перегружен стилем?
- Часто ли тексты требуют отдельной структурной редакторской роли?
- Часто ли терминология требует отдельного reviewer?
- Достаточно ли усилить текущие role specs вместо добавления новых ролей?

## Возможная Codex-задача

```text
Evaluate future editorial extension roles based on task retrospectives.
```

## Acceptance criteria

- Есть критерии, когда новая роль нужна.
- Есть критерии, когда новая роль не нужна.
- Future roles не становятся активными без обновления `AGENTS.md`.
- Если роль добавляется, у неё есть:
  - bounded scope;
  - forbidden actions;
  - pipeline integration;
  - review-gate compatibility;
  - smoke-test.

## Риски

- Раздуть систему.
- Ввести роль, которая дублирует Review Agent.
- Сломать role separation.
- Сделать future role обязательной для обычных задач.

---

# 7. Visual subsystem

Статус: `planned`  
Приоритет: `P3`  
Тип апдейта: subsystem decision

## Идея

Визуальная подсистема сейчас frozen / experimental. Artist Agent легализован, но не активируется по умолчанию.

Нужно решить судьбу visual subsystem:

1. оставить frozen как архив знаний;
2. разморозить и сделать полноценный visual pipeline;
3. вынести в optional module.

## Почему это важно

Пока visual subsystem хранится в проекте, есть риск, что Codex или ChatGPT случайно воспримут её как активный pipeline.

## Что хотим получить

Чёткую границу:

- ordinary editorial work не использует visual branch;
- visual branch включается только явной просьбой;
- Artist Agent не становится дизайнером, писателем, reviewer или универсальным image-prompt агентом;
- визуальные задачи не обходят semantic ownership и review.

## Возможная Codex-задача

```text
Clarify frozen visual subsystem boundaries or extract it as optional module.
```

## Acceptance criteria

- Статус visual subsystem понятен.
- Ordinary text tasks не затрагивают visual docs.
- Если subsystem остаётся frozen, это видно в navigation/project-state.
- Если subsystem выносится, пути и ссылки обновлены.
- Если subsystem размораживается, нужен отдельный pipeline и smoke-tests.

## Риски

- Случайно активировать visual branch.
- Размыть роль Artist Agent.
- Превратить image generation в обход редакционного процесса.
- Потратить время на подсистему, которая сейчас не приоритетна.

---

# 8. Research Pipeline hardening

Статус: `planned`  
Приоритет: `P2`  
Тип апдейта: research quality / production test

## Идея

Research Pipeline уже есть, но его нужно проверить на реальной задаче и сделать production-grade на практике.

## Почему это важно

Research-слой чаще всего создаёт тяжёлые артефакты. Если он плохо настроен, редакция либо недособирает факты, либо создаёт слишком много служебного материала.

## Что хотим проверить

Связку:

```text
research
→ sources
→ facts
→ claims_table
→ writer claims-used
→ review claim checks
```

## Возможная Codex-задача

```text
Harden Research Pipeline with smoke tests and compact evidence rules.
```

## Acceptance criteria

- Research Pipeline работает на реальной article/social задаче.
- Claims traceability понятна Writer Agent.
- Review Agent может проверить claims без чтения всего research dump.
- Low-risk no-research rationale работает.
- High-governance research требует полный evidence set.
- Sources/facts/claims_table не создаются без необходимости.

## Риски

- Research станет слишком тяжёлым.
- Writer начнёт использовать неподтверждённые факты.
- Review Agent не сможет быстро понять, какие claims попали в draft.
- Claims-used станет формальным и бесполезным.

---

# 9. Source/provenance workflow

Статус: `planned`  
Приоритет: `P2`  
Тип апдейта: source governance / reusable import pattern

## Идея

На примере Сбера появился хороший паттерн:

```text
external source
→ cleaned Markdown
→ source-notes
→ source status
→ profile/rules
→ smoke-test
```

Нужно обобщить его для будущих внешних политик, клиентских профилей и крупных источников.

## Почему это важно

Без source/provenance workflow система может:

- использовать устаревший источник;
- выдумать правила при конвертации;
- потерять дату ревизии;
- не отличить active source от pending_source;
- заявить соответствие политике без основания.

## Что хотим получить

Общий стандарт для внешних источников:

- где хранить оригинал;
- где хранить cleaned Markdown;
- как фиксировать source status;
- как описывать omissions/uncertainties;
- когда источник считается active;
- какой smoke-test нужен после обновления.

## Возможная Codex-задача

```text
Generalize external source import workflow from Sber profile.
```

## Acceptance criteria

- Есть source import convention.
- Есть шаблон `source-notes.md`.
- Есть статусы: `active`, `pending_source`, `stale`, `deprecated`.
- Есть правило: не выдумывать missing rules.
- Есть правило: после обновления source нужен smoke-test.
- Sber profile остаётся частным случаем общего механизма.

## Риски

- Слишком бюрократизировать импорт источников.
- Потерять исходный PDF/документ.
- Смешать external source с внутренним `AGENTS.md`.
- Автоматически доверять cleaned Markdown без provenance.

---

# 10. Task pack generator

Статус: `planned`  
Приоритет: `P2`  
Тип апдейта: context management / restartability

## Идея

Нужно упростить подготовку контекста для следующей роли. Сейчас агент должен сам решать, какие файлы читать. Это правильно, но можно помочь ему локальным генератором task context.

## Что должен делать генератор

По задаче и роли выдавать минимальный read set:

```text
AGENTS invariant summary
task-manifest.md
current artifact
latest handoff
selected pipeline
active client-profile files
relevant KB
review.md, если роль final_editor
research/claims, если роль review_agent и есть factual claims
```

## Почему это важно

Это снижает риск:

- загрузить весь проект;
- прочитать старые версии;
- пропустить active client profile;
- работать по устаревшему handoff;
- забыть selected pipeline;
- потерять контекст при restart.

## Возможная Codex-задача

```text
Add task pack generator for role-specific restart context.
```

## Acceptance criteria

- Генератор не читает весь проект.
- Генератор учитывает `task-manifest.md`.
- Генератор учитывает current version pointer.
- Генератор включает client-profile files только когда профиль активен.
- Генератор различает роли:
  - writer;
  - ux_writer;
  - review_agent;
  - final_editor;
  - chief_editor.
- Генератор выводит список файлов и краткую причину включения.
- Генератор не заменяет judgment агента, а помогает собрать стартовый контекст.

## Риски

- Превратить генератор в скрытый orchestrator.
- Подменить Chief Editor routing.
- Случайно включать лишние старые файлы.
- Считать latest modified source of truth.

---

# Общий Definition of Done для любого системного апдейта

Любой будущий апдейт считается завершённым только если:

- изменён canonical production source, а не только `/about`;
- при необходимости обновлён `/about`;
- `/about` check проходит;
- роли и пайплайны не противоречат `AGENTS.md`;
- review-gate не ослаблен;
- новые optional artifacts не стали обязательными без причины;
- compact execution не превратился в bypass;
- есть smoke-test или ручной acceptance check;
- рабочее дерево чистое после commit/merge;
- статус раздела в этом roadmap обновлён.

---

# Журнал решений

## 2026-06-04

Создан roadmap из 10 направлений развития после завершения Sber-mode update.

Принято решение:

- работать по шагам;
- не полагаться только на память чата;
- использовать этот файл как сверочный backlog;
- не смешивать roadmap с `/about` memory package;
- следующим кандидатом считать validation layer.

## 2026-06-05

Выполнены первые safe-core GitHub апдейты:

- создан GitHub repo `sa713/ai-editorial-office`; после safe-core проверки repo открыт public для прямого review через GitHub connector;
- добавлен `CONTRIBUTING.md` через PR #1;
- добавлен MVP task lifecycle validator через PR #2;
- добавлен compact execution guidance через PR #3;
- lifecycle validator расширен status/pipeline checks через PR #4.

Принято решение:

- roadmap хранится в safe-core repo как planning document;
- roadmap не заменяет `AGENTS.md`, production-файлы, роли, пайплайны или task artifacts;
- GitHub repo хранит safe core;
- реальные task materials и source files не добавляются;
- ChatGPT review пока выполняется через локальные diff/review pack;
- следующие шаги выбираются по одному разделу roadmap за раз.
- repo открыт public только после safe-core очистки: `tasks/`, `learn/`, `kb/clients/`, source/binary files и реальные task materials не публиковались.
- ChatGPT может читать public repo/PR через GitHub connector; локальные diff/review pack остаются резервным способом проверки.

Дополнительно:

- repo был открыт public для прямого review через GitHub connector;
- перед публикацией в repo не попали `tasks/`, `learn/`, `kb/clients/`, source/binary files и реальные рабочие материалы.

## 2026-06-05

Добавлены Preflight Gate synthetic examples and smoke-test.

Принято решение:

- Preflight examples являются tests/reference material, не production governance;
- examples не заменяют Intake Agent, Chief Editor или `AGENTS.md`;
- Sber profile activation проверяется на activation/non-activation examples;
- unsafe/deceptive communication должен блокироваться.

---

# Следующий рекомендуемый шаг

Вариант A — продолжить раздел 3:

```text
Add transition checks to task lifecycle validator.
```

Вариант B — продолжить раздел 5:

```text
Test Preflight Gate examples on a real intake task or add an automated checker.
```

Рекомендуемый следующий шаг: real intake check или automated Preflight checker,
если цель — проверить routing на практике; transition checks, если цель —
продолжить укреплять validator layer.
