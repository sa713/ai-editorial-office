# Architecture Decision — minimal integration of Product Intent Review

- Decision ID: `PIR-ADR-STEP0-001`
- Date: 2026-07-29
- Status: proposed for Step 1 specification
- Scope: architecture decision only
- Implementation authorization: none

## Решение

Встроить Product Intent Review как **условно активируемую специализированную
decision lens внутри семейства Professional Analysis**, с отдельной компактной
канонической спецификацией и записью в Capability Registry.

Рабочее архитектурное определение:

> Product Intent Review — evidence-bounded analytical lens, которая до глубокой
> редакционной доработки восстанавливает продуктовый замысел, проверяет его
> ценность, соответствие, механизм и жизнеспособность и передаёт Chief Editor
> ограниченный продуктовый вывод и следующий decision.

Линза не является:

- новой ролью;
- новым pipeline;
- lifecycle stage;
- review gate;
- task status;
- закрытым классификатором;
- обязательным standalone task artifact;
- владельцем продукта или бизнес-цели.

## Почему это самостоятельная узкая линза, а не только reuse

Professional Analysis уже содержит `Business or needs analysis` и `Product
discovery analysis`. Это правильный общий дом. Но простой reuse не гарантирует:

- фиксированную семичленную модель замысла;
- четыре обязательные product checks;
- три режима активации;
- product-first ordering;
- один главный разрыв;
- minimum hypothesis validation;
- explicit right to recommend smaller intervention, pause or no-build;
- non-activation на простой редактуре.

Следовательно, новая сущность нужна на уровне **предметной линзы и её
контракта**, но не на уровне роли, lifecycle или governance.

## Минимальная новая каноническая сущность

На Step 1 рекомендуется создать один новый owner:

`ai-editorial-office/kb/product_intent_review.md`

Он должен владеть только:

- purpose и non-goals;
- activation/non-activation;
- режимами `not_needed / limited / full`;
- семичленной моделью;
- четырьмя проверками;
- правилами неполных данных;
- смысловым output contract;
- minimum hypothesis validation;
- границей с редактурой, research, domain expertise, strategy и product
  ownership;
- типовыми failure modes;
- роль-сотрудничеством без новой роли.

Он не должен повторять:

- evidence classes и confidence labels;
- analytical reasoning moves;
- общую Professional Analysis форму;
- audience/outcome framework;
- planning method;
- review outcomes;
- lifecycle stages;
- task status model.

`kb/capability_registry.md` должен получить краткую запись и role mapping,
ссылающуюся на этого owner. В `AGENTS.md` достаточно добавить owner в
Canonical ownership map и короткую entry-discipline consequence; полную
спецификацию туда копировать нельзя.

## Governance precondition

Это решение описывает архитектурную совместимость, но не даёт release
authority.

Текущий `project-state.md`:

- говорит, что future stage не активна;
- оставляет Professional Analysis в списке open release candidates;
- требует Project Lead decision по её статусу.

Поэтому Step 1 не должен молча считать Professional Analysis уже принятым
каноническим родителем. Перед спецификацией владелец инициативы должен выбрать
одно из двух:

1. отдельно принять/авторизовать Professional Analysis как parent capability
   family для этой инициативы;
2. разрешить Product Intent Review ссылаться на текущий release-candidate
   contract без изменения его статуса и с явной обратной совместимостью.

Ни одно из этих решений не принято на Step 0. Пользовательский запрос
авторизует только текущий аудит.

## Активация

Task Need Recognition даёт только advisory recommendation на основе нескольких
сигналов:

- предлагается новая активность, сервис, формат, процесс, программа или
  пользовательский сценарий;
- ожидается изменение поведения, решения, опыта или состояния аудитории;
- формат решения ещё не утверждён;
- пользователь спрашивает о целесообразности или выбранном подходе;
- качество материала нельзя отделить от качества замысла.

Chief Editor принимает одно из трёх task-local решений:

| Mode | Когда | Минимальный результат |
| --- | --- | --- |
| `not_needed` | Локальная редактура, перевод, сокращение, утверждённая концепция, product logic вне scope. | Короткая negative-evidence причина или полное опущение при очевидном случае. |
| `limited` | Один материальный product-intent вопрос влияет на полезность, но полный аудит избыточен. | Только релевантные элементы модели, один риск и bounded next decision. |
| `full` | Новая/неутверждённая концепция, существенная причинная гипотеза или решение о создании. | Полная доступная модель, четыре проверки, главный разрыв, alternatives и minimum validation. |

Эти значения — depth/mode внутри task object. Они не являются task statuses,
pipelines или review levels.

## Точка в lifecycle

Базовый lifecycle не меняется.

```text
intake
  -> Task Need Recognition signal when material
  -> Chief Editor mode decision
  -> research when evidence is needed
  -> Product Intent Review conclusion
  -> Editorial Decision Frame / production permission
  -> writing or UX writing when still justified
  -> existing independent review
  -> finalization and governance
```

Правило последовательности:

> При `limited` или `full` сначала проверяется основание решения; только затем
> подробно оценивается или производится его редакционная реализация.

Это правило не создаёт stage. Оно задаёт condition внутри существующих routing,
research и planning contracts.

## Распределение по ролям

### Chief Editor

- выбирает mode;
- определяет evidence depth;
- решает, можно ли идти в production;
- фиксирует bounded product finding перед Editorial Decision Frame;
- не принимает бизнес/product decision за владельца.

### Intake Agent / Task Need Recognition

- фиксирует наблюдаемые сигналы и negative evidence;
- не активирует линзу автоматически;
- не требует универсального расширенного брифа.

### Research Agent

- восстанавливает доступные элементы модели;
- отделяет подтверждённое от гипотез и unknowns;
- ищет diagnostic/disconfirming evidence только в назначенном scope;
- не проектирует продукт вместо владельца.

### Writer Agent / UX Writer

- получают короткий approved finding и production boundary;
- не исправляют слабый продукт только качеством текста;
- не меняют product behavior или формат решения.

### Review Agent

- проверяет корректность активации и mode;
- проверяет evidence/model/four checks/main gap/minimum test;
- убеждается, что editorial polish не скрыла слабый product finding;
- использует существующие outcomes `approved`, `changes_requested`, `blocked`;
- не становится product owner и не выбирает новый active route.

### Final Editor

- сохраняет одобренный продуктовый вывод, uncertainty и next decision;
- не добавляет новый product analysis.

## Где хранится task-local состояние

Не создавать обязательный `product-intent-review.md`.

Минимальное отображение:

- `orchestration_plan.md`: mode, activation basis, product finding, production
  consequence и reroute trigger;
- `research.md` или выбранный analytical deliverable: модель, evidence,
  checks, gaps и minimum validation, если глубина требует;
- `review.md`: independent Product Intent Review challenge;
- `task-manifest.md`: capability/mode pointer только когда активна или
  материальна для restart.

Отдельный task-local artifact допустим только когда selected deliverable прямо
является Product Intent Review report или глубина/traceability действительно
требует его. Это conditional artifact, не default.

## Product verdict и operational verdict должны быть разными

Смысловые продуктовые выводы из `brief.md` не должны становиться task statuses
или Review Pipeline outcomes.

Пример:

- Product finding: `до производства требуется проверка продуктовой гипотезы`.
- Review outcome: `approved`, если сам анализ корректен и decision-ready.
- Chief Editor consequence: production task не разрешён до решения владельца
  продукта или отдельного пилота.

Так сохраняется различие между качеством Product Intent Review и решением
создавать продукт.

## Рассмотренные альтернативы

### A. Только расширить Professional Analysis

Плюсы: минимум файлов.
Минусы: большая product-specific модель размоет общий owner, activation и
output contract останутся трудно обнаружимыми.

Вердикт: отклонить как недостаточно исполняемый вариант. Использовать
Professional Analysis как родительское семейство, но создать узкий owner.

### B. Реализовать только в Editorial Challenge Lens

Плюсы: использует существующий независимый review.
Минусы: analysis возникает после production, не создаёт ранний mode decision и
не даёт Research Agent/Chief Editor contract.

Вердикт: отклонить как слишком поздний и неполный вариант.

### C. Расширить Architecture Review

Плюсы: уже умеет drivers, tradeoffs, risks и design fitness.
Минусы: архитектурная семантика не подходит курсам, кампаниям, мероприятиям и
рабочим процессам без architecture significance.

Вердикт: отклонить как неверного владельца.

### D. Создать Product Strategist / Product Reviewer

Плюсы: заметная ответственность.
Минусы: существующие роли уже дают routing, research, analysis, independent
review и governance; новая роль дублирует их и создаёт coordination cost.

Вердикт: отклонить. Evidence необходимости новой независимой accountability
отсутствует.

### E. Создать отдельный Product Intent pipeline или pre-production gate

Плюсы: жёсткая последовательность.
Минусы: превращает условную проверку в параллельный процесс и усложняет простые
задачи.

Вердикт: отклонить. Достаточно capability mode и существующих lifecycle gates.

### F. Принять исторический Problem Hypothesis proposal как решение

Плюсы: уже предлагает компактную проблемную гипотезу.
Минусы: proposal не прошёл каноническое принятие и покрывает только один элемент
из семи.

Вердикт: не использовать как owner. На Step 1 решить, интегрировать ли его как
compact subset или формально supersede.

## Каноническая поверхность следующих шагов

Это рекомендуемая карта, а не разрешение на изменение.

### Step 1 — specification

Минимально:

- новый `kb/product_intent_review.md`;
- `kb/capability_registry.md`;
- `AGENTS.md` — только ownership pointer и global boundary, если нужен.

Проверить:

- `kb/professional_analysis.md` — короткая relationship note без дублирования;
- governance precondition выше — не превращать open release candidate в
  accepted capability неявным patch;
- `project-state.md` — не обновлять до принятого/реализованного состояния.

### Step 2 — task model and routing

Вероятно:

- `kb/task_need_recognition.md`;
- `kb/task_object_model.md`;
- `agents/intake_agent.md`;
- `agents/chief_editor.md`;
- `templates/artifacts/orchestration_plan_template.md`;
- `templates/artifacts/task_manifest_template.md` только если restart pointer
  нельзя выразить текущими полями;
- task-pack generator только если активная линза требует условной загрузки
  нового KB owner.

Не создавать universal questionnaire.

### Step 3 — Editorial Decision Frame and review integration

Вероятно:

- `AGENTS.md` entry discipline;
- `agents/chief_editor.md`;
- `agents/review_agent.md`;
- `pipelines/review_pipeline.md`;
- `templates/artifacts/orchestration_plan_template.md`;
- review task template/fixture, если текущий review artifact contract требует
  явного conditional section.

Не менять task statuses, review outcomes или базовые gates.

### Step 4 — result format

Сначала проверить reuse:

- `kb/deliverables/report.md`;
- `kb/deliverables/research-report.md`;
- `kb/deliverables/decision-memo.md`;
- `kb/professional_communication.md`.

Новый deliverable profile допустим только если тесты покажут устойчиво
отдельную читательскую задачу. По baseline он не обязателен.

### Step 5 — minimum validation

Основной owner: `kb/product_intent_review.md`, с ссылками на Evidence Framework
и Analytical Reasoning. Role consequence может потребоваться в
`research_agent.md` и `review_agent.md`; отдельная Researcher/Product Tester
роль не нужна.

### Step 6 — test suite

Новый manual/synthetic набор должен покрыть десять классов из `brief.md` и
сравнить current / with-lens / expected. Автоматизированные проверки должны
проверять conditional loading и отсутствие обязательной активации, но не
симулировать human product judgment простым string check.

### Step 7 — documentation and adoption

После принятия и реализации:

- `project-state.md`;
- соответствующие canonical docs;
- `/about` только по существующим mapping/sync rules;
- implementation report, change summary, known limitations и final decision.

## Регрессионные риски

| Риск | Что может сломаться | Обязательная проверка |
| --- | --- | --- |
| Over-activation | Copyedit, translation, tone и approved-concept work получают продуктовый аудит. | Negative cases и сохранение compact path. |
| Keyword routing | Слово «продукт», «курс» или «кампания» автоматически активирует full mode. | Multi-signal/negative-evidence tests. |
| Hidden mandatory brief | Пользователю навязывают семь полей до любой работы. | Reconstruction-from-material cases и bounded unknowns. |
| Deliverable/product conflation | Система проверяет форму отчёта вместо предлагаемого вмешательства. | Отдельные fixtures на campaign banners и approved material. |
| Review-gate duplication | Product verdict становится вторым operational verdict. | Mapping product finding vs `approved/changes_requested/blocked`. |
| Role drift | Review Agent исследует/перепроектирует, Chief Editor становится product owner. | Role-boundary cases и review findings с owner mapping. |
| Analysis after polish | Product gap появляется после длинных редакционных замечаний. | Output-order assertion/manual evaluation. |
| Generic consulting drift | Любая редакционная задача превращается в strategy audit. | Explicit non-goals и simple-task samples. |
| False certainty | Problem, market, user need или effect выдумываются. | Fact/assumption/unknown checks and low-evidence cases. |
| Architecture overreach | Architecture Review расширяется на все intervention types. | Non-architecture product fixtures. |
| Process bloat | Новые files/sections появляются даже при `not_needed`. | Task-pack and artifact-minimalism tests. |
| Weak minimum test | Один кейс объявляется доказательством эффективности; появляются выдуманные thresholds. | Minimum-validation boundary cases. |
| Product owner substitution | Редакция сама утверждает бизнес-цель или решает запуск. | Human decision boundary tests. |
| Existing test degradation | TNR, deliverable selection, reader quality и lifecycle contracts расходятся. | Полный regression set ниже. |

## Рекомендуемый regression set после реализации

- `tests/task_need_recognition_smoke_test.md`
- `tests/professional_analysis_smoke_test.md`
- `tests/outcome_first_deliverable_selection_smoke_test.md`
- `tests/deliverable-knowledge-multi-deliverable-planning-smoke-test.md`
- `tests/reader-centered-quality-smoke-test.md`
- `tests/editorial_intelligence_acceptance_smoke_test.md`
- новый `tests/product_intent_review_smoke_test.md`
- `sh ai-editorial-office/tests/test_task_pack_generator.sh`
- `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh`
- `sh ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh`
- `sh ai-editorial-office/tests/test_deliverable_knowledge_multi_deliverable_planning.sh`
- `sh ai-editorial-office/scripts/check_about_memory_package.sh` только если
  затронут mapped `/about` package.

## Нужна ли новая роль

Нет.

Требуемая ответственность уже корректно раскладывается между:

- Intake Agent / Task Need Recognition — signal;
- Chief Editor — mode, route и production decision;
- Research Agent — evidence и model reconstruction;
- Professional Analysis / Analytical Reasoning — analysis;
- Review Agent — independent challenge;
- Final Editor — controlled preservation;
- product owner/user — реальное решение о продукте.

Новая роль была бы оправдана только при подтверждённом конфликте accountability
или независимости, который нельзя устранить role boundaries и review. Такой
конфликт в текущей архитектуре не найден.

## Evidence, confidence и ограничения решения

- Evidence class: direct repository inspection, canonical documentation,
  current tests, and two bounded historical task decisions.
- Confidence: `supported` для выбранной архитектурной формы; `verified` для
  отсутствия текущего canonical Product Intent Review owner и для существующих
  role/lifecycle boundaries.
- Assumptions: одна отдельная KB-спецификация окажется достаточной и не
  размоет Professional Analysis.
- Unknowns: фактическая нагрузка на реальные задачи и качество product
  judgments до Step 6 не доказаны.
- What would change this decision: evidence, что расширение только
  `professional_analysis.md` даёт одинаково обнаружимое, тестируемое и
  restraint-safe поведение без отдельного owner; либо реальный accountability
  conflict, требующий новой роли.

## Step 0 readiness recommendation

Рекомендация: `ready_for_independent_review`.

При одобрении review Step 0 можно закрыть как завершённый аудит. Решение не
разрешает Step 1 автоматически и не утверждает, что Product Intent Review уже
реализован. Отдельный owner/Project Lead decision требуется для governance
dependency на Professional Analysis и для запуска следующего шага.
