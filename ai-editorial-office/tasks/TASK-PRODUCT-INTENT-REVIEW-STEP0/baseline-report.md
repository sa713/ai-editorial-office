# Product Intent Review — baseline report

Дата аудита: 2026-07-29
Статус: Step 0 complete for review
Источник требований: `brief.md`

## Краткий вывод

AI Editorial Office уже содержит почти все общие аналитические строительные
блоки, необходимые для Product Intent Review: распознавание характера задачи,
product-discovery и needs-analysis линзы, problem framing, evidence confidence,
проверку аудитории и результата, анализ альтернатив, Editorial Decision Frame,
Editorial Challenge Lens и право остановить небезопасную работу.

При этом требуемое поведение не существует как цельная, канонически
принадлежащая и условно активируемая операция. Ни один действующий механизм не
обязан до глубокой редакционной работы:

1. восстановить цепочку
   `аудитория -> проблема -> требуемое изменение -> продукт -> механизм ->
   пользовательский опыт -> наблюдаемый результат`;
2. отдельно проверить ценность, соответствие, механизм и жизнеспособность;
3. различить режимы `не требуется`, `ограниченная проверка`, `полная проверка`;
4. вынести главный продуктовый разрыв раньше локальной оценки материала;
5. предложить минимальную проверку конкретной гипотезы;
6. дать продуктовый вывод `продолжить / уменьшить / проверить / остановить`,
   не становясь владельцем продукта.

Точный baseline: архитектура обладает общими средствами анализа, но не имеет
исполняемого контракта Product Intent Review.

## Область и метод аудита

Проверялись только текущий канонический репозиторий и непосредственно
релевантные исторические решения. Legacy-репозиторий не использовался.

Для каждого механизма проверялись четыре разных вида ответственности:

- распознать сигнал;
- принять решение об активации и глубине;
- выполнить анализ;
- независимо проверить результат.

Наличие близкого термина не считалось покрытием, если файл не владеет
наблюдаемым поведением, входом, выходом и границей ответственности.

Текущие канонические файлы считались авторитетнее старых task-предложений,
`ideas/`, тестовых примеров и `/about`.

## Изученные документы

### Архитектурные владельцы

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/project-state.md`
- `ai-editorial-office/kb/task_object_model.md`
- `ai-editorial-office/kb/capability_registry.md`
- `ai-editorial-office/kb/task_need_recognition.md`
- `ai-editorial-office/kb/shared_lifecycle_kernel.md`
- `ai-editorial-office/kb/task_statuses.md`
- `ai-editorial-office/kb/editorial_evidence_framework.md`
- `ai-editorial-office/kb/analytical_reasoning.md`
- `ai-editorial-office/kb/professional_analysis.md`
- `ai-editorial-office/kb/professional_communication.md`
- `ai-editorial-office/kb/architecture_review.md`
- `ai-editorial-office/kb/editorial_planning_framework.md`
- `ai-editorial-office/kb/audience_outcome_alignment.md`
- `ai-editorial-office/kb/editorial_quality_attributes.md`
- `ai-editorial-office/kb/editorial_failure_modes.md`

### Роли, lifecycle и рабочие контракты

- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/agents/research_agent.md`
- `ai-editorial-office/agents/writer_agent.md`
- `ai-editorial-office/agents/ux_writer.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/agents/final_editor.md`
- `ai-editorial-office/pipelines/research_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/artifacts/status_template.md`
- `ai-editorial-office/templates/artifacts/handoff_template.md`

### Deliverable knowledge и regression evidence

- `ai-editorial-office/kb/deliverables/report.md`
- `ai-editorial-office/kb/deliverables/research-report.md`
- `ai-editorial-office/kb/deliverables/decision-memo.md`
- `ai-editorial-office/kb/deliverables/comparison-matrix.md`
- `ai-editorial-office/tests/task_need_recognition_smoke_test.md`
- `ai-editorial-office/tests/professional_analysis_smoke_test.md`
- `ai-editorial-office/tests/outcome_first_deliverable_selection_smoke_test.md`
- `ai-editorial-office/tests/deliverable-knowledge-multi-deliverable-planning-smoke-test.md`
- `ai-editorial-office/tests/reader-centered-quality-smoke-test.md`
- `ai-editorial-office/tests/reader-centered-quality-pilot.md`
- `ai-editorial-office/tests/editorial_intelligence_acceptance_smoke_test.md`

### Релевантная история решений

- `ai-editorial-office/tasks/TASK-PROBLEM-FRAMING-FRAMEWORK/`
- `ai-editorial-office/tasks/TASK-EDITORIAL-CHALLENGE-FRAMEWORK/`

Эти папки прочитаны только как evidence прошлых предложений. Они не
использовались как шаблоны или текущий canon.

## Текущее архитектурное покрытие

| Механизм | Что уже делает | Степень покрытия Product Intent Review | Что не покрывает |
| --- | --- | --- | --- |
| Task Need Recognition | По evidence рекомендует вероятный тип задачи, capabilities, глубину research/review, риск, неоднозначность и decomposition; сохраняет negative evidence и compact path. | Частичное, сильное для будущей активации. | Нет product-intent сигналов и режимов `none / limited / full`; не выполняет анализ и по замыслу не принимает решение. |
| Routing and Preflight | Chief Editor выбирает deliverable set, pipeline, capabilities, глубину и `ask / constrain / proceed / block`. | Частичное, сильное для управления активацией. | Gate отвечает, можно ли безопасно начать редакционную задачу, а не стоит ли создавать предложенный продукт. |
| Professional Analysis | Имеет `Business or needs analysis` и `Product discovery analysis`; поддерживает decision-ready выводы, варианты, риски и ограниченные рекомендации. | Самое близкое общее основание. | Нет обязательной модели замысла, четырёх проверок, product-specific вердикта, минимального теста и порядка до редакционной детализации. |
| Analytical Reasoning | Problem framing, гипотезы, причинные объяснения, disconfirmation, assumptions, contradictions, sufficiency. | Сильное методическое покрытие. | Общий reasoning toolkit не задаёт предмет product intent и его output contract. |
| Editorial Evidence Framework | Отделяет fact, interpretation, assumption, hypothesis, unknown; калибрует confidence и validation needed. | Почти полное переиспользуемое основание для эпистемической дисциплины. | Не определяет, какие продуктовые элементы должны быть восстановлены и проверены. |
| Audience & Outcome Alignment / Reader Outcome Contract | Связывает артефакт с читателем, требуемым пониманием/действием и практическим результатом; Reader Model не выдумывает аудиторию. | Частичное, но относится прежде всего к воздействию материала. | Не проверяет существование исходной проблемы, необходимость самого продукта, механизм продукта и пользовательский опыт продукта. |
| Editorial Planning & Option Evaluation | Требует реальные альтернативы, tradeoffs, selected option и reconsideration triggers. | Частичное для альтернатив и меньшего решения. | Не требует сравнить классы вмешательств или проверить, нужен ли предлагаемый продукт вообще. |
| Outcome-first deliverable selection и каталог deliverables | Проверяет, какой редакционный артефакт или минимальный набор нужен для результата пользователя. | Смежное, но не эквивалентное. | `Deliverable` здесь — форма редакционного результата, а `product` в инициативе — вмешательство, сервис, курс, процесс, событие или инструмент. Выбор хорошего отчёта не доказывает состоятельность описываемого продукта. |
| Editorial Decision Frame | Фиксирует выбранный редакционный маршрут, альтернативы, production contract, review focus и reroute triggers. | Частичное как место потребления продуктового вывода. | Не обязан содержать восстановленную продуктовую логику или четыре product-intent проверки; должен оставаться коротким management block. |
| Editorial Challenge Lens | Review Agent проверяет, сохраняются ли assumptions, делавшие выбранный маршрут валидным. | Частичное для независимого давления на вывод. | Работает во время review, то есть слишком поздно для обязательного pre-production анализа; не восстанавливает замысел и не выбирает активный маршрут. |
| Architecture Review | Проверяет architecture drivers, scenarios, tradeoffs, assumptions, risks и design fitness. | Частичное только для архитектурно значимых системных решений. | Слишком узко: не покрывает курс, кампанию, мероприятие, процесс или изменение поведения без архитектурной значимости. |
| Failure Modes / weak challenge / over-polishing | Позволяет остановить косметическую работу, вернуть задачу к evidence, routing или research и не полировать слабый маршрут. | Сильная страховка. | Реактивное восстановление не заменяет положительный контракт Product Intent Review. |
| Review Agent и существующие verdicts | Может выдать `approved`, `changes_requested` или `blocked`, проверяет evidence, reasoning, analysis, audience и route assumptions. | Достаточная независимость и operational outcome model. | Нет product-intent review dimension и продуктовых смысловых вердиктов; их нельзя превращать в новые task statuses. |
| Shared Lifecycle Kernel | Разрешает условно подключать capabilities к существующим стадиям; сохраняет один review-gate. | Полностью пригодное lifecycle основание. | Не называет Product Intent Review и не задаёт его точку подключения. |

## Что реализовано сильнее всего

### 1. Эпистемическая дисциплина

`editorial_evidence_framework.md` уже задаёт необходимые классы evidence и
confidence. Недостающие данные могут быть оставлены как assumption,
hypothesis, unknown или validation needed. Создавать отдельную product-evidence
систему не нужно.

### 2. Общая профессиональная аналитика

`professional_analysis.md` уже разрешает business/needs analysis и product
discovery до solution commitment. Это наиболее близкое более общее понятие,
частью которого должен стать Product Intent Review.

### 3. Раннее распознавание без автоматики

`task_need_recognition.md` умеет учитывать outcome, work surface, consequence,
evidence state, ambiguity и negative evidence, но оставляет решение Chief
Editor. Это правильная основа для условной активации без keyword classifier.

### 4. Независимое оспаривание

Текущий Review Agent уже способен независимо оспаривать reasoning,
Professional Analysis, evidence, alternatives и route assumptions. Новая
review-role или второй gate не нужны.

### 5. Защита простого пути

Существующие smoke tests прямо требуют, чтобы copyedit, typo fix и
keyword-rich simple request оставались compact. Этот restraint должен стать
non-regression baseline для Product Intent Review.

## Частичное и проблемное покрытие

### Problem Hypothesis не является действующим общим owner

Текущий canon условно упоминает `Problem Hypothesis` как возможный вход для
Editorial Challenge Lens, однако:

- в `task_object_model.md` нет канонического поля или view mapping для него;
- в активном `orchestration_plan_template.md` нет соответствующего блока;
- в `capability_registry.md` нет capability record;
- task `TASK-PROBLEM-FRAMING-FRAMEWORK` имеет только design proposal со
  статусом `review_ready`, без `review.md` и `final_decision.md`.

Следовательно, Problem Hypothesis — релевантный предшествующий design signal,
но не действующая способность, на которую можно опереться как на готовое
решение. Даже если её позднее принять, она покрывает только формулировку
проблемной гипотезы, а не полную цепочку продуктового замысла.

### Reader-centered quality проверяет другой объект

Reader Outcome Contract полезен для механизма воздействия материала на
читателя. Product Intent Review должен проверять механизм самого предлагаемого
продукта или вмешательства. Эти проверки могут использовать общую логику
«исходное состояние -> требуемое изменение -> наблюдаемый результат», но не
должны сливаться.

### Deliverable fit не равен product fit

Текущий outcome-first выбор отвечает на вопрос, какой артефакт нужен
пользователю Редакции. Product Intent Review отвечает на вопрос, оправдан ли
курс, сервис, кампания, мероприятие, процесс или иной объект, описываемый
артефактом. Терминологическое смешение создаст ложное ощущение покрытия.

## Точный функциональный разрыв

В текущей системе нет канонического условно активируемого владельца
предпроизводственной проверки продуктового замысла, который:

- распознаётся по multi-signal evidence, а не слову «продукт»;
- восстанавливает семь элементов логики без домысливания;
- проверяет ценность, соответствие, механизм и жизнеспособность;
- выдаёт один приоритетный разрыв и следующий продуктовый decision;
- предлагает минимальную проверку конкретной гипотезы;
- выполняется до глубокой оценки реализации, когда это материально;
- остаётся выключенным для простой редактуры и утверждённых концепций;
- использует существующие роли, lifecycle, evidence и review-gate.

Это не пробел в аналитической технике. Это пробел в предметной
ответственности, активации, последовательности и output contract.

## Изменения, внесённые на шаге 0

Изменена только task-local поверхность:

- сохранён `brief.md` как канонический источник требований;
- созданы task governance artifacts;
- подготовлены три запрошенных Step 0 отчёта.

Production logic, canonical KB, роли, pipelines, templates, scripts, runtime и
tests не изменялись.

## Проверки шага 0

- Канонический brief сопоставлен с исходным attachment: содержание совпадает;
  repository-файл нормализован добавлением финального перевода строки.
- Проверено отсутствие Product Intent Review в текущих canonical owners.
- Проверены текущие role boundaries и review outcomes.
- Проверена сохранность production surface через scoped `git diff`.
- Полные lifecycle и regression checks должны быть выполнены после review
  task-пакета; в Step 0 нет поведения, которое требовало бы новых product tests.

## Открытые вопросы

1. Следует ли оставить рабочее имя `Product Intent Review`, несмотря на риск
   спутать capability с существующим Review Pipeline?
2. Нужен ли отдельный deliverable profile, или product-intent блок должен
   адаптироваться внутри report, research report и decision memo?
3. Должен ли исторический Problem Hypothesis proposal быть формально
   superseded, интегрирован как компактный поднабор или оставлен отдельным
   непринятым proposal?
4. Какие реальные paired cases будут доступны на Step 6 кроме synthetic
   fixtures?
5. `project-state.md` по-прежнему называет Professional Analysis open release
   candidate. Может ли Step 1 использовать её как родительское capability
   family, или сначала нужен отдельный Project Lead decision о её статусе?

Эти вопросы не блокируют минимальное архитектурное решение Step 0.

## Рекомендация о переходе

После независимого одобрения этого отчёта, responsibility map и architecture
decision Step 0 готов к закрытию. Переход к Step 1 допустим только как отдельное
решение пользователя/владельца инициативы; он не происходит автоматически.
До Step 1 также нужно разрешить governance dependency: текущий
`project-state.md` не активирует будущую стадию и оставляет Professional
Analysis open release candidate. Step 0 не меняет этот статус и не считается
его принятием.
