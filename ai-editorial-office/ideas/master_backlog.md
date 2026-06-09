# Master backlog ИИ-редакции

Статус документа: `active draft / placed in repo`  
Версия: `v0.2`  
Дата сборки: 2026-06-09  
Назначение: единый рабочий файл для планирования доработок ИИ-редакции, контроля прогресса и ретроспективы уже сделанных системных апдейтов.

Этот файл собирает важное из трёх дорожных карт и наших обсуждений:

- `DEVELOPMENT_ROADMAP.md` — основной roadmap развития safe-core, lifecycle, validators, compact execution, source/provenance и task pack generator.
- `SKILLS_ROADMAP.md` — идеи про capability packs, governance, artifact QA, reader testing, evals и scripted validators.
- `token_economy_improvements.md` — практический стандарт постановки задач для Codex, чтобы не расходовать контекст на шум и не раздувать изменения.

Файл не заменяет `AGENTS.md`, production-роли, пайплайны и шаблоны. Если этот backlog конфликтует с `AGENTS.md` или production-файлами, приоритет у production-файлов.

Текущий статус: файл собран как master backlog v0.2, но ещё должен быть размещён в repo и признан рабочим planning artifact. До этого он является сильной проектной сводкой, но не production source of truth.

---

## 1. Текущее состояние редакции

Редакция уже не находится на стадии сборки архитектуры. Safe-core собран и проверяется на реальных и синтетических задачах. Текущий этап — сделать ежедневную работу компактной, проверяемой, воспроизводимой и устойчивой к расползанию.

Ключевой сдвиг:

```text
от “добавим ещё роли и документы”
к “минимальный task pack → компактное выполнение → проверяемый diff → обязательный review”
```

Главные инварианты:

- `AGENTS.md` остаётся главным источником системных правил.
- Review-gate обязателен: финализация без review не допускается.
- Новые роли не добавляются без отдельного решения.
- Новые обязательные артефакты не добавляются без причины.
- `/about` — compact memory package для ChatGPT, а не backlog и не governance source.
- Safe-core может жить в GitHub; реальные task materials, клиентские профили, бинарные/source-файлы и чувствительные материалы не публикуются.
- Client profile, включая Sber-mode, активируется только task-scoped и только при явных условиях.
- Capabilities рассматриваются как optional helpers, а не как новые роли и не как обход пайплайнов.
- Сырой пользовательский запрос должен уметь превращаться в рабочий brief/task внутри редакции, без ручного перевода через ChatGPT на каждом шаге.

---

## 2. Что уже сделано

### 2.1. Safe-core и базовая архитектура

Сделано:

- собраны ключевые роли: `chief_editor`, `intake_agent`, `research_agent`, `writer_agent`, `ux_writer`, `review_agent`, `final_editor`;
- закреплён task lifecycle;
- закреплены базовые task artifacts: `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, `review.md`, `final_decision.md`, итоговый артефакт;
- закреплён review-gate;
- добавлен compact handoff;
- добавлен compact execution guidance;
- `/about` используется как компактный memory package для ChatGPT;
- safe-core опубликован в GitHub repo `sa713/ai-editorial-office`;
- repo открыт public только после safe-core очистки;
- в repo не попали `tasks/`, `learn/`, `kb/clients/`, source/binary files и реальные рабочие материалы;
- ChatGPT может читать public repo/PR через GitHub connector;
- локальные diff/review pack остаются резервным способом проверки.

### 2.2. Sber-mode

Сделано:

- добавлен `client_profile: sber`;
- Сбер подключён как изолированный task-scoped client profile;
- редполитика Сбера не стала глобальной политикой редакции;
- production templates получили поля client profile;
- article/social/UX/review pipelines умеют загружать client-profile files только когда профиль активен;
- роли intake/chief/writer/ux_writer/review/final_editor знают про active client profile;
- `/about` синхронизирован и проверен.

Принцип на будущее:

```text
клиентский профиль — не новая редакция и не глобальная политика;
это task-scoped слой, включаемый только по явным условиям.
```

### 2.3. Validation layer

Сделано:

- добавлен read-only `scripts/validate_task_lifecycle.py`;
- добавлен smoke-test runner `tests/test_task_lifecycle_validator.sh`;
- добавлены synthetic fixtures для task lifecycle;
- проверяются required files `task-manifest.md` и `status.md`;
- проверяется review-gate: `review.md` должен существовать перед `final.md`;
- проверяется review outcome: `approved`, `changes_requested`, `blocked`;
- ambiguous outcome вроде `not approved` не считается approved;
- finalization gate не пропускает `final.md` без approved review;
- добавлены status/pipeline checks;
- добавлены transition checks;
- `blocked -> finalized` запрещён отдельным guard;
- missing previous status пока warning, не blocker.

### 2.4. Compact execution

Сделано:

- добавлен `kb/compact_execution.md`;
- добавлены synthetic compact examples;
- article/social/UX/review pipelines получили ссылки на compact execution guidance;
- review-gate сохранён;
- `review.md` перед finalization остаётся обязательным;
- optional artifacts не стали обязательными;
- high-governance задачи не предлагается чрезмерно сокращать.

Главный смысл:

```text
меньше служебного веса
без потери review, traceability и restartability
```

### 2.5. Preflight Gate

Сделано:

- добавлены synthetic examples and smoke-test;
- проведены manual trials;
- проверены сценарии:
  - Sber-owned vs Sber-as-topic;
  - UX/context scenario;
  - unsafe/deceptive communication;
- после трёх manual trials решено пока не добавлять automated checker.

Решение:

```text
manual examples сейчас полезнее, чем ранняя автоматизация routing.
checker вернётся в roadmap только при повторяющихся routing failures.
```

### 2.6. Feedback loop

Сделано:

- добавлен Feedback loop workflow;
- проведены sanitized manual trials;
- зафиксировано различие между:
  - bounded revision;
  - task-local note;
  - future preference watch;
  - repeated signal;
  - system change proposal.

Решение:

```text
один feedback не меняет систему;
повторяющийся сигнал может стать pattern;
production changes проходят отдельный reviewed system update.
```

### 2.7. Source/provenance workflow

Сделано:

- добавлен source/provenance workflow;
- source status должен быть явным;
- missing rules нельзя выдумывать при чистке источника;
- compliance claims разрешены только если source status и source-notes это позволяют;
- source import smoke-test нужен до признания imported source активным.

### 2.8. Research Pipeline hardening

Сделано:

- research artifacts стали conditional, not automatic;
- low-risk no-claim tasks могут использовать no-research rationale;
- compact-evidence разрешён для source-light задач;
- full-evidence требуется для high-governance material claims;
- Review Agent должен проверять material claims без чтения полного research dump.

### 2.9. Task pack generator MVP

Сделано:

- добавлен MVP task pack generator;
- generator является read-only context helper;
- generator не является orchestrator;
- generator не заменяет Chief Editor routing;
- generator не использует latest modified как source of truth;
- generator включает client-profile files только если они явно указаны и существуют.

### 2.10. End-to-end sanitized cases

Проведены первые три sanitized cases.

Зафиксировано:

- security-adjacent employee task должен использовать `constrain`, а не `proceed`;
- exploit wording нужно переписывать как sanctioned internal security testing;
- no-research mode достаточен для editorial tasks без внешних factual claims;
- clear internal feedback request может использовать `proceed`, если raw brief достаточен;
- редактор не должен выдумывать toolkit functions или methodology content;
- source-based internal course task должен использовать `constrain`;
- compact-evidence подходит, если user-provided source используется как task-local source;
- original source files не должны коммититься в safe-core repo;
- source summary достаточно для sanitized editorial case review;
- task pack generator требует follow-up check для task-local source summaries в source-based compact-evidence cases.

---

## 3. Главные рабочие принципы дальше

### 3.1. Не добавлять слой ради слоя

Сейчас редакции нужен не новый агент, а более короткий и надёжный путь:

```text
нормальная постановка задачи
→ минимальный task pack
→ компактное выполнение
→ проверяемый diff
→ review без чтения всего проекта
```

### 3.2. Capabilities, not roles

Идеи из NVIDIA Skills и Anthropic Skills полезны не как готовые скилы, а как модель controlled adoption.

Берём:

```text
узкое назначение
→ явная активация
→ границы применения
→ риски
→ evals
→ review
→ controlled adoption
```

Две обязательные идеи для capability-подхода:

- **Progressive disclosure**: capability должна быть короткой на входе; детали подтягиваются только при активации, чтобы не раздувать контекст каждой задачи.
- **Activation contract**: у каждой capability должно быть понятно, когда она включается, когда не включается, какие файлы/артефакты она может трогать и какие действия ей запрещены.

Не берём:

- новые роли по умолчанию;
- отдельные `docx_agent`, `pdf_agent`, `slides_agent`, `spreadsheet_agent`;
- обязательные QA-документы для каждой markdown-задачи;
- governance-слои, дублирующие `AGENTS.md`;
- автоматическое создание новых артефактов ради красоты архитектуры.

### 3.3. Markdown remains canonical

Capabilities, scripts и validators могут помогать, но canonical rules остаются в markdown-файлах проекта.

### 3.4. External artifacts require QA

DOCX, PDF, PPTX, XLSX и другие внешние артефакты не считаются готовыми, пока они не проверены визуально/структурно.

Это будущий кандидат для первой настоящей capability: `artifact-quality-gates`.

### 3.5. Экономия токенов — это дисциплина постановки задачи

Главная потеря контекста возникает не из-за длинных файлов, а из-за размытой задачи, после которой Codex сам читает лишнее, строит неверный контекст и чинит не то.

Стандарт:

```text
цель → границы → source of truth → список файлов → запреты → acceptance criteria → check-pack
```

### 3.6. Что сейчас не делаем

Чтобы не раздувать систему, сейчас не делаем:

- новые роли;
- большой рефакторинг пайплайнов;
- обязательные capability packs;
- автоматизацию preflight checker без повторяющихся routing failures;
- визуальную подсистему как production default;
- external artifact generation как базовое поведение редакции;
- перенос всех идей из skills-репозиториев;
- новые обязательные артефакты ради аккуратной архитектуры;
- переписывание всего safe-core ради одной точечной проблемы.

---

## 4. Приоритеты

### P0 — единый master backlog

Статус: `draft created / needs repo placement`

Задача: свести `DEVELOPMENT_ROADMAP.md`, `SKILLS_ROADMAP.md` и `token_economy_improvements.md` в один управляющий артефакт.

Результат: этот файл должен стать основным планом контроля. Исходные roadmap-файлы остаются источниками деталей, но не должны жить как три равноправных плана.

Что ещё нужно сделать:

- перенести этот файл в repo;
- определить постоянное место, например `ai-editorial-office/roadmaps/master_backlog.md` или `ai-editorial-office/project-management/master_backlog.md`;
- явно указать в `project-state.md`, что этот файл используется для планирования системных доработок;
- после переноса обновлять его при каждом системном апдейте.

### P1 — сравнить первые три end-to-end case report

Статус: `next recommended step`

Задача: сравнить первые три `case_report.md` и решить, где нужен маленький fix.

Возможные зоны фикса:

- compact execution;
- source/provenance;
- task pack generator;
- case conventions;
- research evidence modes.

Ожидаемый результат:

- краткое сравнение кейсов;
- список повторяющихся поломок;
- один точечный fix, если он реально нужен;
- без большого рефакторинга.


### P1.5 — raw brief normalization

Статус: `planned`

Задача: научить редакцию принимать сырой пользовательский запрос и превращать его в рабочий `brief.md` / task definition без ручного перевода через ChatGPT.

Почему важно:

- пользователь должен иметь возможность давать задачу естественным языком;
- intake/chief editor должны сами выделять цель, аудиторию, ограничения, source status, expected artifacts и acceptance criteria;
- система должна отличать рабочий бриф от переписки, эмоций, примеров и шума;
- это снижает зависимость от ручной формулировки Codex-задач.

Минимальный результат:

- правило в `intake_agent.md` или связанном workflow;
- шаблон нормализации сырого брифа;
- examples: плохой сырой запрос → нормальный task brief;
- ограничение: normalization не должна выдумывать цели, источники и требования, которых нет в запросе.

### P2 — внедрить стандарт Codex-задачи и check-pack

Статус: `planned`

Задача: превратить правила экономии токенов в рабочий шаблон для всех новых Codex-задач.

Должно появиться:

- шаблон задания для Codex;
- блок `source of truth`;
- блок `рабочая зона`;
- блок жёстких запретов;
- acceptance criteria;
- `implementation-notes.md`;
- `check-pack.md`.

Польза:

- меньше лишнего чтения repo;
- меньше расползания изменений;
- проще присылать ChatGPT результат на проверку;
- меньше длинных отчётов в чате;
- выше качество ревью.

### P3 — дорастить lifecycle validator

Статус: `in_progress`

Задача: расширить validator вокруг тех ошибок, которые реально могут ломать редакцию.

Кандидаты:

- handoff validator;
- finalization-gate deep checks;
- `client_profile` consistency;
- `final_decision.md` ownership/stage checks;
- source metadata checker;
- forbidden pattern scanner;
- claim coverage checker;
- retrospective metrics collector.

Правило:

```text
валидатор должен ловить структурные ошибки,
но не превращать low-risk задачи в бюрократию.
```

### P4 — проверить compact execution на реальной low-risk задаче

Статус: `planned`

Задача: подтвердить, что compact execution работает не только на synthetic examples.

Проверить:

- не создаёт ли редакция лишних файлов;
- не теряется ли restartability;
- не ослабляется ли review-gate;
- понятно ли ChatGPT проверять результат;
- достаточно ли `task-manifest.md`, `status.md`, рабочего артефакта и `review.md` без отдельного handoff.

### P5 — донастроить task pack generator

Статус: `planned`

Задача: проверить и улучшить generator для source-based compact-evidence cases.

Особое внимание:

- task-local source summaries;
- явный source status;
- client-profile files only when active;
- отсутствие зависимости от latest modified;
- компактный набор контекста для writer/review.

### P6 — capability governance skeleton

Статус: `proposal / planned after P1-P5`

Задача: создать минимальный governance-скелет для capabilities без новых ролей.

Минимальный набор:

```text
kb/capability_governance.md
templates/capability-card.md
```

Правила:

- capability не может override `AGENTS.md`, выбранный pipeline, role separation или review-gate;
- capability активируется явно;
- capability имеет owner из существующих ролей;
- capability имеет when_to_use / when_not_to_use;
- capability имеет activation contract;
- capability использует progressive disclosure и не грузит детали без активации;
- capability имеет risks, forbidden actions и eval scenarios;
- capability остаётся optional helper.

### P7 — первая capability: artifact-quality-gates

Статус: `proposal`

Задача: сделать первый практический capability pack для проверки внешних артефактов.

Почему первый именно он:

- польза понятная;
- риск ошибок в DOCX/PDF/PPTX/XLSX высокий;
- проверка артефактов плохо держится только на reasoning;
- часть проверок можно вынести в scripts.

Минимальный формат:

```text
capabilities/artifact-quality-gates/SKILL.md
capabilities/artifact-quality-gates/evals/activation_positive.jsonl
capabilities/artifact-quality-gates/evals/activation_negative.jsonl
```

Не делать mandatory для обычных markdown-задач.

### P8 — reader-testing capability

Статус: `proposal`

Задача: добавить optional QA-проход свежим читателем без контекста переписки.

Использовать для:

- важных статей;
- стратегических документов;
- UX-writing specs;
- клиентских отчётов;
- decision memos;
- текстов, где непонимание читателя дорого стоит.

Проверяет:

- может ли свежий читатель понять документ сам по себе;
- что документ предполагает, но не говорит;
- где есть двусмысленность;
- где не хватает контекста;
- что выглядит общим или неподкреплённым.

Не делать обязательным для каждой мелкой задачи.

### P9 — review-gate-linter / source-traceability-check

Статус: `proposal`

Задача: добавить capabilities/scripts, которые помогают Review Agent не пропускать governance drift.

Кандидаты:

- `review-gate-linter`;
- `source-traceability-check`;
- `claim coverage checker`;
- `forbidden pattern scanner`.

Сначала лучше делать scripts для стабильных проверок, а editorial judgment оставлять Review Agent.

### P10 — future roles и visual subsystem

Статус: `defer`

Решение:

- future roles пока не развивать;
- visual subsystem не включать по умолчанию;
- визуальные задачи рассматривать как experimental/isolated workflow;
- возвращаться к ним после стабилизации validators, compact execution и task pack generator.

Known problems по visual subsystem:

- короткая постановка “визуальный конспект” не всегда запускала правильный sketchnote pipeline;
- Codex иногда делал SVG/инфографику вместо живого hand-drawn sketchnote;
- итоговый результат должен быть PNG, без лишних HTML и служебных файлов, если пользователь не просит иначе;
- русский текст на картинке нужно проверять на фантазии, читаемость и соответствие статье;
- visual pipeline должен отличать sketchnote, инфографику, мем, комикс и презентационный визуал;
- визуальные задачи требуют отдельного visual brief и image prompt, но не должны ломать обычный editorial task lifecycle.

---

## 5. Практический стандарт задачи для Codex

Этот стандарт нужно использовать для большинства новых задач по доработке редакции.

Операционное правило для ChatGPT:

```text
Если пользователь просит задачу для Codex, ответ должен быть одним цельным md-сообщением, удобным для копирования, без псевдо-слайдов, без длинной преамбулы и без отдельного пересказа вокруг задания.
```

```md
# Задача для Codex

## Цель
Коротко: что должно измениться и какой результат нужен.

## Контекст
Зачем это делаем. Какое поведение редакции улучшаем.

## Рабочая зона
Работай только в указанных папках и файлах.

## Source of truth
1. AGENTS.md — системные правила, роли, review-gate.
2. project-state.md — текущее состояние системы.
3. Нужный pipeline — если задача про конкретный процесс.
4. Нужный agent — если задача про роль.
5. Нужные templates/kb — если задача про артефакты или справочник.

Не искать альтернативные правила в других файлах без необходимости.

## Что можно менять
Список разрешённых файлов или областей.

## Что нельзя менять
- Не добавлять новых агентов, pipeline и обязательных артефактов без прямой необходимости.
- Не менять review-gate.
- Не переписывать соседние файлы ради стилистического улучшения.
- Не читать весь проект без необходимости.
- Любое изменение вне списка файлов сначала обосновать.

## Глубина работы
Например: точечный patch, не архитектурный рефакторинг.

## Acceptance criteria
Как понять, что задача выполнена правильно.

## Формат результата
- Минимальный patch.
- Короткий implementation-notes.md.
- check-pack.md для проверки в ChatGPT.
- Без длинного отчёта в чате.

## Что прислать на проверку
- git diff summary;
- список изменённых файлов;
- ключевые фрагменты;
- implementation-notes.md;
- check-pack.md;
- результаты smoke-test/manual check.
```

### implementation-notes.md

```md
# Implementation notes

## Что изменено

## Почему именно так

## Какие файлы затронуты

## Что не делал

## Как проверить
```

### check-pack.md

```md
# Check pack

## Краткая суть изменения

## Список изменённых файлов

## Git diff summary

## Ключевые фрагменты изменённых файлов

## Риски

## Что нужно прислать ChatGPT на ревью
```

---

## 6. Definition of Done для системного апдейта

Любой системный апдейт считается завершённым только если:

- изменён canonical production source, а не только `/about`;
- при необходимости обновлён `/about`;
- `/about` check проходит;
- роли и пайплайны не противоречат `AGENTS.md`;
- review-gate не ослаблен;
- новые optional artifacts не стали обязательными без причины;
- compact execution не превратился в bypass;
- есть smoke-test или ручной acceptance check;
- рабочее дерево чистое после commit/merge;
- статус в этом backlog обновлён.

Для апдейтов intake/chief editor отдельно проверять:

- сырой пользовательский запрос не превращается в фантазийный brief;
- неявные ограничения помечаются как assumptions/questions, а не как факты;
- task definition остаётся пригодным для Codex и review.

---

## 7. Журнал решений и ретроспектива

### 2026-06-04

Создан roadmap из 10 направлений развития после Sber-mode update.

Решения:

- работать по шагам;
- не полагаться только на память чата;
- использовать roadmap как сверочный backlog;
- не смешивать roadmap с `/about` memory package;
- следующим кандидатом считать validation layer.

### 2026-06-05

Выполнены первые safe-core GitHub апдейты.

Сделано:

- создан GitHub repo `sa713/ai-editorial-office`;
- добавлен `CONTRIBUTING.md` через PR #1;
- добавлен MVP task lifecycle validator через PR #2;
- добавлен compact execution guidance через PR #3;
- lifecycle validator расширен status/pipeline checks через PR #4.

Решения:

- repo хранит safe core;
- реальные task materials и source files не добавляются;
- ChatGPT review возможен через GitHub connector;
- локальные diff/review pack остаются fallback;
- следующие шаги выбираются по одному разделу roadmap за раз.

### 2026-06-05 — Preflight Gate

Сделано:

- synthetic examples and smoke-test;
- три manual trials;
- проверка Sber activation/non-activation;
- проверка UX/context scenario;
- проверка unsafe/deceptive communication.

Решение:

- automated checker пока не добавлять;
- manual examples оставить как reference material.

### 2026-06-05 — Feedback loop

Сделано:

- добавлен workflow;
- проведены manual trials;
- уточнены bounded revision, future preference watch и system change proposal.

Решение:

- single feedback остаётся task-local;
- repeated signal может стать feedback pattern;
- production changes только через reviewed system update.

### 2026-06-05 — Source/provenance

Сделано:

- добавлен workflow;
- source status стал явным;
- compliance claims ограничены source status и source-notes;
- source import требует smoke-test.

### 2026-06-05 — Research Pipeline hardening

Сделано:

- введены `no-research`, `compact-evidence`, `full-evidence`;
- research artifacts стали conditional;
- full-evidence закреплён для high-governance material claims.

### 2026-06-05 — Task pack generator MVP

Сделано:

- read-only context helper;
- не orchestrator;
- не заменяет Chief Editor;
- не использует latest modified как source of truth;
- client-profile files включаются только явно.

### 2026-06-05 — первые end-to-end cases

Сделано:

- проведены три sanitized cases;
- зафиксированы решения по `proceed/constrain`, no-research, compact-evidence и source summaries.

Следующий вывод:

```text
нужно сравнить три case_report.md и понять, нужен ли точечный fix.
```

### 2026-06-09 — master backlog

Сделано:

- сведения из `DEVELOPMENT_ROADMAP.md`, `SKILLS_ROADMAP.md`, `token_economy_improvements.md` сведены в один план;
- приоритеты уточнены: сначала реальные case reports и компактный Codex/check-pack стандарт, потом validators, затем capabilities;
- capabilities оставлены как proposal, не как активная архитектура.

### 2026-06-09 — master backlog v0.2

Сделано:

- статус P0 изменён с `done` на `draft created / needs repo placement`;
- добавлен пункт raw brief normalization;
- добавлено правило: задачи для Codex выдавать одним цельным md-сообщением;
- добавлены progressive disclosure и activation contract для capabilities;
- добавлен anti-roadmap “что сейчас не делаем”;
- visual subsystem дополнен known problems и оставлен в `defer`.

---

## 8. Следующий лучший шаг

Рекомендуемый следующий шаг:

```text
Сначала перенести master_backlog.md в repo и закрепить его как planning artifact. Затем сравнить первые три end-to-end case_report.md и решить, нужен ли один маленький fix в compact execution, source/provenance, task pack generator или case conventions.
```

Формат следующей Codex-задачи:

```md
# Задача для Codex

## Цель
Сравнить первые три end-to-end sanitized editorial case_report.md и предложить один точечный fix, если он действительно нужен.

## Контекст
Мы стабилизируем ИИ-редакцию после внедрения validation layer, compact execution, source/provenance, research hardening и task pack generator MVP. Нужно понять, какие проблемы повторяются на реальных sanitized cases, а не добавлять новую архитектуру заранее.

## Рабочая зона
Работай только с папками/файлами end-to-end sanitized cases и связанными notes/check-pack, если они есть.
Production-файлы не меняй на первом шаге.

## Source of truth
- AGENTS.md
- project-state.md
- DEVELOPMENT_ROADMAP.md или master_backlog.md, если он уже перенесён в repo
- case_report.md по первым трём end-to-end cases

## Что сделать
1. Найди первые три end-to-end case_report.md.
2. Кратко сравни их по routing, research mode, source handling, compact execution, task pack usefulness и review readiness.
3. Выдели повторяющиеся проблемы.
4. Предложи не больше одного маленького fix.
5. Ничего не меняй в production files без отдельного подтверждения.

## Acceptance criteria
- Есть короткое сравнение трёх кейсов.
- Есть список повторяющихся проблем или вывод, что их недостаточно для системного изменения.
- Есть рекомендация: fix / no fix / collect more cases.
- Нет большого рефакторинга.
- Нет новых ролей, pipeline или обязательных артефактов.

## Формат результата
- case-comparison.md
- краткий implementation-notes.md, если были изменения
- check-pack.md для проверки в ChatGPT
```

---

## 9. Как обновлять этот файл

После каждого системного апдейта обновлять:

1. `Что уже сделано` — если апдейт завершён.
2. `Приоритеты` — если изменился порядок работ.
3. `Журнал решений` — коротко, дата + решение + причина.
4. `Следующий лучший шаг` — один конкретный шаг, а не список желаний.
5. Статусы backlog-пунктов: `planned`, `in_progress`, `done`, `defer`, `rejected`.

Правило:

```text
Этот файл должен помогать выбирать следующий шаг,
а не превращаться в склад всех идей.
```
