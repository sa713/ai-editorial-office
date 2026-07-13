# Reader-Centered Editorial Quality Backlog

Статус документа: `implementation complete / comparative promotion pending`

Дата: 2026-07-13

Основание: сравнительный разбор `final_editorial.md` и `final_chatgpt.md` для одного запроса о практическом развитии ИИ после периода ChatGPT 5.2.

Этот документ — отдельный backlog и execution ledger в `ideas/`. Он не
заменяет активный `ideas/master_backlog.md`, `ROADMAP.md` или `BACKLOG.md`.
Описанные изменения реализованы в существующих canonical owners, ролях,
pipelines, templates и tests последовательными bounded slices. При этом
заявление о достигнутом паритете с сильным одиночным ChatGPT остаётся
неподтверждённым до фактических comparative runs и решения Project Lead.

## Статус реализации

| ID | Статус | Краткий результат |
| --- | --- | --- |
| `ROQ-P0-01` | implemented | Reader Outcome Contract и неослабляемые quality/evidence guardrails закреплены в существующем каноне. |
| `ROQ-P0-02` | implemented | Chief Editor проектирует reader journey и обосновывает выбранный порядок через исходное состояние и требуемое изменение. |
| `ROQ-P0-03` | implemented | Cognitive Bridge, 3-5 Moments of Insight и Practical Transformation встроены в Editorial Decision Frame. |
| `ROQ-P0-04` | implemented | Reader Model и Learning Design распределены между существующими ролями; новых ролей нет. |
| `ROQ-P0-05` | implemented | Детерминированный Reader Review встроен в `review.md` и существующий review gate. |
| `ROQ-P0-06` | implemented | Companion Pass выполняется до approval; substantive repair остаётся у Writer Agent. |
| `ROQ-P0-07` | implemented | Chief Editor может принять только явный, ограниченный и reviewable Bounded Utility Tradeoff. |
| `ROQ-P1-01` | implemented and automated | Material reader context передаётся Writer/Review task packs без новых task artifacts; fixture и smoke test добавлены. |
| `ROQ-P1-02` | calibrated; external comparison pending | Реальный longread baseline и два synthetic cases зафиксированы; promotion gate честно оставлен `not yet proven`. |
| `ROQ-P1-03` | implemented from calibration evidence | Определены `compact`, `normal`, `full` depth и bounded re-review. |
| `ROQ-P1-04` | implemented | Добавлены восемь anti-regression cases и architecture-restraint checks. |
| `ROQ-P2-01` | implemented and automated | Planned/actual runtime topology живёт в plan/manifest; task-pack fixture проверяет передачу record. |
| `ROQ-P2-02` | implemented | Feedback/Learning Framework хранит outcome evidence и задаёт высокий evidence threshold для новой постоянной роли. |

## Цель

Сделать результат AI Editorial Office как минимум не хуже результата сильного одиночного ChatGPT по всем существенным для пользователя параметрам, сохранив преимущества Редакции в доказательности, нейтральности, независимом review и трассируемости.

Целевой результат должен одновременно:

- быть корректным, доказательным, нейтральным и трассируемым;
- отвечать исходной позиции конкретного читателя, а не только теме;
- давать понятный мост от старой модели к новой;
- оставлять 3–5 запоминающихся выводов;
- переводить понимание в практическое действие;
- быть живым, конкретным и естественным без потери точности;
- не требовать новых постоянных ролей или дополнительных служебных файлов без доказанной пользы.

## Наблюдение, из которого исходит backlog

В сравнительном кейсе Редакция была сильнее по композиционной целостности, доказательной дисциплине, нейтральности и отделению фактов от выводов. Одиночный ChatGPT был сильнее по прямому мосту от известной пользователю точки, продуктовой конкретике, числу практических примеров, педагогической последовательности и скорости перехода к вопросу «что делать теперь».

Проблема не сводится к качеству Writer Agent. Главный разрыв возникает раньше: в выбранном Chief Editor критерии оптимизации и в Editorial Decision Frame недостаточно явно спроектирован путь конкретного читателя. Поэтому изменения должны начинаться с существующих владельцев маршрута, качества, коммуникации и review, а не с добавления новой роли.

## Принципы реализации

- Сначала использовать существующие роли: `chief_editor`, `intake_agent`, `writer_agent`, `review_agent`, `final_editor`.
- Reader Model, Learning Design, Reader Review и Companion Pass реализовать как функции, линзы и task-local поля в существующих артефактах.
- Не создавать отдельный обязательный файл для Reader Model, Learning Design, Reader Review, Companion Pass или runtime execution record.
- Новые поля держать компактными и включать пропорционально типу задачи; обучающие и объяснительные материалы требуют большей глубины, чем короткий рабочий текст.
- Полезность не отменяет evidence boundary. Корректность, подтверждаемость, нейтральность, честная неопределённость и review-gate остаются обязательными ограничителями.
- Сравнительный кейс считать сильным сигналом для пилота, но не достаточным доказательством для немедленного разрастания архитектуры.

## P0 — изменения, необходимые для следующего качественного скачка

### ROQ-P0-01 — Reader Outcome Contract и новая иерархия качества

- **ID:** `ROQ-P0-01`
- **Название:** Reader Outcome Contract и новая иерархия качества.
- **Проблема:** действующий канон уже учитывает аудиторию, actionability и reader path, но допускает, что корректный и хорошо организованный документ будет признан сильным без явного изменения модели читателя или его практики. Пользовательская ценность может оказаться одним из атрибутов, а не центральным критерием маршрута.
- **Предлагаемое изменение:** закрепить компактный Reader Outcome Contract: исходное состояние читателя, требуемое изменение понимания, требуемое действие после чтения и признаки бесполезного результата. В quality priority оценивать ценность для конкретного читателя, изменение его модели мышления и практическую применимость наряду с корректностью, evidence support, нейтральностью и трассируемостью. Последние остаются обязательными guardrails и не могут быть принесены в жертву полезности.
- **Затрагиваемые файлы/компоненты:** `kb/audience_outcome_alignment.md`, `kb/editorial_quality_attributes.md`, `kb/task_object_model.md`, короткие ссылки в `AGENTS.md`, quality profile в существующих task artifacts.
- **Критерии приёмки:**
  - маршрут нельзя признать достаточным только потому, что документ корректен и полон;
  - для material reader-facing задач видны исходное состояние читателя, целевое изменение и практический результат;
  - quality profile явно сохраняет correctness, evidence support, neutrality и traceability как неослабляемые ограничения;
  - не вводится числовой универсальный score и не создаётся новый обязательный артефакт.
- **Приоритет:** `P0`.
- **Зависимости:** нет; это базовый контракт для остальных P0-задач.
- **Риски/предостережения:** субъективное слово «ценность» может превратиться в вкусовую оценку; критерии должны выводиться из запроса, reader context, intended outcome и наблюдаемого действия, а не из предпочтений агента.

### ROQ-P0-02 — Chief Editor проектирует путь читателя

- **ID:** `ROQ-P0-02`
- **Название:** Reader Journey как обязанность Chief Editor.
- **Проблема:** Chief Editor умеет выбирать pipeline, глубину, evidence boundary, структуру и quality profile, но может оптимизировать результат как корректный документ, а не как переход конкретного читателя из текущего состояния в новое.
- **Предлагаемое изменение:** обязать Chief Editor при material reader-facing задачах проектировать путь: «что читатель думает/умеет сейчас → что должно измениться → в какой последовательности это объяснить → что он сможет сделать после». Выбор concept-first, chronology-first, product-first или иной стратегии должен объясняться через этот путь. Reader Journey остаётся короткой частью существующего orchestration contract.
- **Затрагиваемые файлы/компоненты:** `agents/chief_editor.md`, `kb/editorial_planning_framework.md`, `kb/capability_registry.md`, `templates/artifacts/orchestration_plan_template.md`, при необходимости короткая governance-ссылка в `AGENTS.md`.
- **Критерии приёмки:**
  - Chief Editor называет исходную позицию читателя и целевое состояние;
  - выбранный порядок разделов объясняется потребностью читателя, а не только логикой предмета;
  - для запроса «я остановился на X» маршрут содержит явный мост от X, если источники позволяют его построить;
  - Writer получает применимый reader journey, а не расширенное эссе Chief Editor;
  - компактные и неридерские задачи не обрастают лишней секцией.
- **Приоритет:** `P0`.
- **Зависимости:** `ROQ-P0-01`.
- **Риски/предостережения:** дублирование Audience & Outcome Alignment и Professional Communication; нужно расширять их применение, а не создавать параллельный фреймворк.

### ROQ-P0-03 — Расширение Editorial Decision Frame

- **ID:** `ROQ-P0-03`
- **Название:** Cognitive Bridge, Moments of Insight и Practical Transformation.
- **Проблема:** текущий Editorial Decision Frame фиксирует маршрут, альтернативы, writer contract, review focus и reroute triggers, но не гарантирует явный педагогический мост, запоминающиеся выводы и изменение поведения.
- **Предлагаемое изменение:** добавить в существующий Editorial Decision Frame три компактных поля:
  - **Cognitive Bridge:** что читатель уже знает; какую старую или неполную модель нужно обновить; какой переход нужен;
  - **Moments of Insight:** 3–5 мыслей, которые читатель должен сохранить после материала;
  - **Practical Transformation:** что читатель начнёт делать иначе после материала.
  Поля должны быть обязательны для обучающих и объяснительных reader-facing задач и условны для остальных типов.
- **Затрагиваемые файлы/компоненты:** `AGENTS.md` в части canonical definition Editorial Decision Frame, `kb/task_object_model.md`, `templates/artifacts/orchestration_plan_template.md`, `templates/tasks/article_task_template.md`, `agents/chief_editor.md`, `agents/writer_agent.md`.
- **Критерии приёмки:**
  - все три поля находятся внутри `orchestration_plan.md`, а не в новом файле;
  - Cognitive Bridge описывает реальную исходную модель читателя, а не общий портрет аудитории;
  - Moments of Insight содержит 3–5 сформулированных мыслей, а не названия разделов;
  - Practical Transformation содержит наблюдаемое действие или изменение практики;
  - Writer и Review могут проследить эти поля до draft/review;
  - поля допускают `not applicable` с причиной для задач, где обучение не является целью.
- **Приоритет:** `P0`.
- **Зависимости:** `ROQ-P0-01`, `ROQ-P0-02`.
- **Риски/предостережения:** разрастание orchestration plan и формальное заполнение полей; ограничить каждое поле несколькими строками и проверять его влияние на результат.

### ROQ-P0-04 — Reader Model и Learning Design как общие функции

- **ID:** `ROQ-P0-04`
- **Название:** Reader Model и педагогическая логика без новых ролей.
- **Проблема:** система знает аудиторию и communication job, но недостаточно явно моделирует знания, устаревшие убеждения, ожидаемые «ага-моменты» и последовательность усвоения. В результате материал может быть академически сильным, но обучать медленнее, чем более прямой одиночный ответ.
- **Предлагаемое изменение:** определить Reader Model как обязательную функцию для задач типа `Teach`, `Understand` и сложных объяснений. Распределить её между существующими ролями: Intake фиксирует исходную позицию, Chief Editor утверждает переход, Writer реализует его, Review проверяет. В Professional Communication закрепить условный Learning Design pattern: `раньше → сейчас → почему → пример → что делать`. Паттерн является инструментом, а не обязательной структурой каждого текста.
- **Затрагиваемые файлы/компоненты:** `kb/audience_outcome_alignment.md`, `kb/professional_communication.md`, `kb/capability_registry.md`, `agents/intake_agent.md`, `agents/chief_editor.md`, `agents/writer_agent.md`, `pipelines/article_pipeline.md`.
- **Критерии приёмки:**
  - Reader Model имеет понятный trigger и распределённую ответственность существующих ролей;
  - не создаются `reader_model_agent`, `learning_designer` или отдельный обязательный файл;
  - обучающий маршрут показывает старую модель, новую модель, причину изменения, пример и действие, когда это улучшает понимание;
  - Writer использует конкретные примеры там, где абстракция иначе останется непереносимой;
  - pattern можно сократить или не применять, если он ухудшает другой тип материала.
- **Приоритет:** `P0`.
- **Зависимости:** `ROQ-P0-01`–`ROQ-P0-03`.
- **Риски/предостережения:** формульность, искусственная хронология и чрезмерное объяснение очевидного опытному читателю; глубина должна зависеть от reader context.

### ROQ-P0-05 — Reader Review внутри существующего review-gate

- **ID:** `ROQ-P0-05`
- **Название:** Детерминированный Reader Review.
- **Проблема:** текущий review хорошо проверяет brief, evidence, структуру, actionability и reader transfer, но не требует отдельно доказать, что конкретный читатель понял переход, запомнит ключевые мысли и сможет применить материал. Результат может пройти по формальным критериям и всё равно остаться тяжёлым, академичным или оторванным от исходной модели пользователя.
- **Предлагаемое изменение:** добавить Reader Review как условную линзу внутри существующего `review.md`, а не как новый gate, цикл, роль или файл. Reviewer должен ответить: что читатель понял; какие 3–5 мыслей сможет воспроизвести; что сможет сделать; где отсутствует Cognitive Bridge; где академизм, jargon density, перегрузка, абстрактность или нехватка примера мешают outcome. Каждое замечание связывается с brief, Reader Outcome Contract или конкретным фрагментом.
- **Затрагиваемые файлы/компоненты:** `agents/review_agent.md`, `pipelines/review_pipeline.md`, `templates/tasks/review_task_template.md`, `kb/professional_communication.md`, `kb/audience_outcome_alignment.md`, review section в существующем `review.md`.
- **Критерии приёмки:**
  - Reader Review использует статусы `pass`, `fail`, `not applicable`, `needs clarification`;
  - проверяются понимание, запоминание, применение, Cognitive Bridge и лишняя академичность;
  - `fail` содержит evidence, consequence и bounded repair, а не «мне не нравится»;
  - Reviewer не подменяет Writer и не предлагает вкусовой rewrite;
  - Reader Review не ослабляет factual, source, neutrality или governance checks;
  - для короткой низкорисковой задачи линза может быть компактной внутри основного checklist.
- **Приоритет:** `P0`.
- **Зависимости:** `ROQ-P0-01`–`ROQ-P0-04`.
- **Риски/предостережения:** ложная объективность и вкусовщина; требуется связь каждого finding с объявленным reader outcome и воспроизводимыми критериями.

### ROQ-P0-06 — Companion Pass перед финализацией

- **ID:** `ROQ-P0-06`
- **Название:** Companion Pass без потери точности.
- **Проблема:** доказательный текст может звучать как учебник или служебный документ, хотя пользователь ждёт живого объяснения от сильного собеседника. Простая команда «сделать человечнее» опасна: она может добавить фальшивую близость, рекламность или убрать точные оговорки.
- **Предлагаемое изменение:** добавить Companion Pass как последнюю reader-facing линзу Review перед `approved`: «можно ли объяснить это конкретному читателю живо, естественно и по-человечески, сохранив смысл, evidence boundary и терминологическую точность?». Если нужен содержательный rewrite, материал возвращается Writer Agent; Final Editor только сохраняет уже одобренный баланс и выполняет разрешённые поверхностные изменения.
- **Затрагиваемые файлы/компоненты:** `kb/professional_communication.md`, `agents/review_agent.md`, `pipelines/review_pipeline.md`, `agents/final_editor.md`, `templates/tasks/review_task_template.md`.
- **Критерии приёмки:**
  - Companion Pass выполняется до finalization и фиксируется в существующем `review.md`;
  - оцениваются естественность, конкретность, jargon burden и дистанция от читателя;
  - запрещено удалять caveats, источники, точные границы или неопределённость ради плавности;
  - запрещены fake empathy, фамильярность и искусственная разговорность;
  - substantive repair возвращается Writer Agent и проходит bounded re-review;
  - новый lifecycle stage или artifact не создаётся.
- **Приоритет:** `P0`.
- **Зависимости:** `ROQ-P0-04`, `ROQ-P0-05`.
- **Риски/предостережения:** пересечение с Professional Communication и tone of voice; Companion Pass должен быть узкой финальной проверкой reader relationship, а не новым стилевым фреймворком.

### ROQ-P0-07 — Осознанные локальные компромиссы ради полезности

- **ID:** `ROQ-P0-07`
- **Название:** Bounded Utility Tradeoff для Chief Editor.
- **Проблема:** стремление к универсальности и долговечности может убрать именно тот мост, который нужен пользователю сейчас: короткую хронологию, конкретный продуктовый срез, сравнение «тогда/сейчас» или пример из актуального интерфейса.
- **Предлагаемое изменение:** разрешить Chief Editor явные и ограниченные компромиссы ради reader outcome. Решение должно фиксировать: какую потребность читателя оно закрывает; точный scope; evidence/freshness boundary; что может устареть; какой атрибут сознательно ослаблен; какие guardrails нельзя ослаблять. Пример допустимого решения: краткая проверенная хронология или продуктовый мост от GPT-5.2, если именно так сформулирована исходная позиция пользователя.
- **Затрагиваемые файлы/компоненты:** `kb/editorial_quality_attributes.md`, `kb/editorial_planning_framework.md`, `agents/chief_editor.md`, `templates/artifacts/orchestration_plan_template.md`, Editorial Decision Frame.
- **Критерии приёмки:**
  - компромисс записан как bounded decision, а не скрытое отклонение;
  - указаны reader benefit, scope, freshness/staleness note и preservation guardrails;
  - correctness, source boundary, neutrality и review independence нельзя объявить relaxable;
  - конкретика поставщика не превращается в рекламу или необоснованный каталог возможностей;
  - Review Agent может проверить, остаётся ли компромисс оправданным.
- **Приоритет:** `P0`.
- **Зависимости:** `ROQ-P0-01`–`ROQ-P0-03`.
- **Риски/предостережения:** исключение может стать универсальным разрешением на feature dump, хрупкую хронологию или vendor bias; использовать только при прямой связи с исходной позицией читателя.

## P1 — усиление и проверка эффекта

### ROQ-P1-01 — Компактная интеграция в шаблоны и task packs

- **ID:** `ROQ-P1-01`
- **Название:** Протянуть reader-outcome contract без новых артефактов.
- **Проблема:** даже хороший канон не влияет на выполнение, если orchestration, role packets и review templates не передают нужные поля следующим ролям. Одновременно копирование полного правила во многие файлы создаст governance drift.
- **Предлагаемое изменение:** добавить только fillable fields и короткие canonical references в существующие шаблоны. Обеспечить, чтобы Writer и Review role packets получали Cognitive Bridge, Moments of Insight, Practical Transformation, quality tradeoff и reader-review focus, когда они material. Не создавать `reader-model.md`, `learning-design.md`, `reader-review.md` или `companion-pass.md`.
- **Затрагиваемые файлы/компоненты:** `templates/artifacts/orchestration_plan_template.md`, `templates/artifacts/task_manifest_template.md` при необходимости pointer/state, `templates/tasks/article_task_template.md`, `templates/tasks/review_task_template.md`, `templates/tasks/social_task_template.md`, `scripts/generate_task_pack.py`, `tests/test_task_pack_generator.sh`.
- **Критерии приёмки:**
  - поля имеют одного canonical owner и не дублируются полными инструкциями;
  - role packet включает только material context;
  - компактные задачи не получают расширенный checklist автоматически;
  - task pack generator остаётся совместим с существующими fixtures;
  - ни один новый обязательный task artifact не появляется.
- **Приоритет:** `P1`.
- **Зависимости:** все `P0`-задачи, определяющие канонический контракт.
- **Риски/предостережения:** template sprawl и увеличение context load; проверять каждый добавленный field по downstream consumer.

### ROQ-P1-02 — Пилот на трёх типах задач

- **ID:** `ROQ-P1-02`
- **Название:** Comparative pilot: longread, working document, short user text.
- **Проблема:** один сильный сравнительный кейс показывает направление, но не доказывает, что изменения улучшают разные типы материалов и не вредят компактным задачам.
- **Предлагаемое изменение:** провести одинаково поставленные сравнительные пилоты на 2–3 задачах разных типов:
  1. обучающий лонгрид с устаревшей исходной моделью читателя;
  2. рабочий документ, который должен привести к решению или выполнению;
  3. короткий пользовательский текст, где важны ясность, естественность и действие.
  Для каждой задачи сравнить результат обновлённой Редакции с сильным одиночным ChatGPT и, где возможно, с baseline Редакции до изменений. Использовать одинаковый brief, source boundary, доступные материалы и ограничения.
- **Затрагиваемые файлы/компоненты:** task-local pilot packs в `tasks/`, существующие pipelines/templates, отдельный компактный synthetic или manual trial в `tests/` на этапе реализации, Project Lead review.
- **Критерии приёмки:**
  - сравнение по каждой задаче фиксирует correctness, evidence support, neutrality, traceability, reader fit, clarity, concreteness, memory change, practical action и naturalness;
  - обновлённая Редакция не хуже comparator по каждому material criterion, а не только по средней оценке;
  - нет регрессии evidence/review discipline ни в одном пилоте;
  - judgment содержит evidence и конкретные фрагменты; numeric score не является единственным основанием;
  - отрицательный или смешанный результат сохраняется как finding, а не сглаживается.
- **Приоритет:** `P1`.
- **Зависимости:** `ROQ-P1-01`.
- **Риски/предостережения:** модель comparator и продуктовые поверхности меняются; фиксировать дату, модель/режим, source set и ограничения, не делать универсальный вывод из трёх кейсов.

### ROQ-P1-03 — Калибровка глубины и bounded repair

- **ID:** `ROQ-P1-03`
- **Название:** Разная глубина Reader Review для разных задач.
- **Проблема:** полная педагогическая проверка полезна для лонгрида, но может перегрузить короткий текст или рабочий документ. Без калибровки улучшение превратится в новый слой governance.
- **Предлагаемое изменение:** после пилотов определить компактный, нормальный и полный варианты reader-outcome checks. Для короткой задачи оставить несколько outcome-вопросов в основном checklist; для обучающего материала проверять весь Cognitive Bridge, Moments of Insight, Practical Transformation, Learning Design и Companion Pass. Любой `changes_requested` должен назначать bounded repair owner/scope/re-review scope.
- **Затрагиваемые файлы/компоненты:** `kb/shared_lifecycle_kernel.md`, `pipelines/article_pipeline.md`, `pipelines/review_pipeline.md`, при необходимости `pipelines/social_pipeline.md`, `agents/review_agent.md`, `templates/tasks/review_task_template.md`.
- **Критерии приёмки:**
  - depth trigger зависит от intended outcome, reader risk и explanation complexity;
  - low-risk short text не требует полного обучающего блока;
  - исправление reader-outcome failure не разрешает бесконтрольный rewrite;
  - повторный review ограничен изменённым scope, если другие проверки остаются валидными;
  - artifact count не увеличивается.
- **Приоритет:** `P1`.
- **Зависимости:** `ROQ-P1-02` и evidence пилотов.
- **Риски/предостережения:** слишком сложная матрица активации; использовать минимальное число чётких triggers и ручное решение Chief Editor.

### ROQ-P1-04 — Регрессионные сценарии

- **ID:** `ROQ-P1-04`
- **Название:** Reader-outcome smoke tests и anti-regression cases.
- **Проблема:** изменения могут постепенно свестись к красивым полям в шаблоне, ослабить evidence discipline или начать активироваться везде.
- **Предлагаемое изменение:** добавить небольшой набор сценариев: корректный, но бесполезный академический текст; живой, но недоказательный текст; хороший Cognitive Bridge; feature dump вместо reader bridge; обоснованный и необоснованный bounded tradeoff; Reader Review как вкусовщина; короткий текст, где full learning design не нужен.
- **Затрагиваемые файлы/компоненты:** существующая `tests/`-структура, `tests/README.md`, при необходимости новый smoke-test Markdown-файл и минимальные fixtures; существующие lifecycle/task-pack tests для anti-regression.
- **Критерии приёмки:**
  - тесты различают reader value и простую лёгкость чтения;
  - доказательный guardrail блокирует приятный, но неподтверждённый текст;
  - `not applicable` корректно работает для нерелевантных задач;
  - тесты подтверждают отсутствие новой роли, нового gate и обязательного artifact set;
  - существующие lifecycle и task-pack проверки проходят без регрессии.
- **Приоритет:** `P1`.
- **Зависимости:** `ROQ-P1-02`, `ROQ-P1-03`.
- **Риски/предостережения:** синтетические примеры могут научить систему проходить тест, а не помогать читателю; сохранять ручной pilot review.

## P2 — наблюдаемость и дальнейшее развитие

### ROQ-P2-01 — Runtime execution record в task pack

- **ID:** `ROQ-P2-01`
- **Название:** Фактическая runtime-топология без случайных nicknames.
- **Проблема:** task pack показывает канонические роли и артефакты, но не позволяет восстановить фактическое распараллеливание, назначение research-подпотоков, model/mode, входные границы и вклад отдельных subagent-сессий. Для разбора кейса пришлось обращаться к локальным `.codex/sessions`.
- **Предлагаемое изменение:** добавить компактный runtime execution record в существующие task artifacts. `orchestration_plan.md` хранит планируемую топологию, а `task-manifest.md` — фактически выполненную. Для каждого runtime instance или подпотока фиксировать стабильный task-local ID, каноническую роль/функцию, назначение и scope, parent/coordination relation, model/mode если доступны, входные границы, созданные или переданные артефакты/пакеты и границы ответственности. Случайный nickname может быть optional note, но не идентификатором процесса.
- **Затрагиваемые файлы/компоненты:** `kb/task_object_model.md`, `kb/shared_lifecycle_kernel.md`, `templates/artifacts/orchestration_plan_template.md`, `templates/artifacts/task_manifest_template.md`, `agents/chief_editor.md`, `scripts/generate_task_pack.py`, `tests/test_task_pack_generator.sh`.
- **Критерии приёмки:**
  - planned topology и actual execution не смешиваются;
  - видны все material subagent streams, включая подпотоки без прямой записи файла;
  - указаны model/mode только когда они доступны; иначе используется `unknown`/`not recorded`, без догадок;
  - вклад связывается с артефактом или межагентным пакетом;
  - случайные имена вроде Hume/Volta не требуются для воспроизводимости;
  - record живёт в существующих артефактах и не становится отдельным обязательным файлом;
  - исключены секреты, лишние session metadata и персональные/чувствительные данные.
- **Приоритет:** `P2`.
- **Зависимости:** можно реализовывать независимо от P0/P1 после согласования минимальной схемы; проверять на пилотах `ROQ-P1-02`.
- **Риски/предостережения:** stale runtime state, ручная нагрузка, привязка к конкретному runtime Codex и утечка внутренних данных; запись должна быть компактной, best-effort и privacy-bounded.

### ROQ-P2-02 — Наблюдение эффекта и порог для новых ролей

- **ID:** `ROQ-P2-02`
- **Название:** Evidence-based evolution после пилота.
- **Проблема:** успешный пилот может вызвать преждевременное желание создать Reader Model Agent, Learning Designer или отдельный reader-testing pipeline; неуспешный — преждевременно отменить полезную идею.
- **Предлагаемое изменение:** собирать повторяющиеся outcome-сигналы через существующие feedback, evaluation и learning mechanisms. Рассматривать новую постоянную роль только если несколько разных задач показывают устойчивую проблему, существующие владельцы не могут её решить без конфликта ответственности, а отдельная роль даёт проверяемую пользу выше своей стоимости. До этого функции остаются распределёнными.
- **Затрагиваемые файлы/компоненты:** `kb/feedback_patterns.md`, `kb/editorial_learning_framework.md`, существующие Evaluation Signals, task-local `feedback.md`/`review.md`, позднее `ideas/master_backlog.md` только после отдельного Project Lead решения.
- **Критерии приёмки:**
  - outcome feedback отделён от вкусового preference;
  - сохранены положительные, отрицательные и противоречивые результаты;
  - canon/backlog/role changes не происходят автоматически;
  - новая роль требует repeated evidence, ownership conflict analysis, cost/benefit и отдельного reviewed system update;
  - отсутствие новой роли считается нормальным успешным исходом, если существующие роли справляются.
- **Приоритет:** `P2`.
- **Зависимости:** `ROQ-P1-02`–`ROQ-P1-04`.
- **Риски/предостережения:** self-confirmation, метрики активности вместо результата и накопление служебных записей; сохранять только decision-useful evidence.

## Не делать

- Не создавать отдельного агента на каждую новую функцию: Reader Model, Learning Design, Reader Review и Companion Pass сначала принадлежат существующим ролям.
- Не раздувать governance и число служебных файлов без явной downstream-пользы.
- Не ослаблять evidence/review discipline, независимость review, source boundary, нейтральность или честное обозначение неопределённости.
- Не превращать Reader Review в субъективную вкусовщину без критериев, evidence и связи с reader outcome.
- Не оптимизировать текст только под лёгкость чтения в ущерб точности.
- Не превращать Learning Design pattern в обязательный шаблон для каждого материала.
- Не делать Companion Pass разрешением на fake empathy, фамильярность, рекламность или удаление caveats.
- Не считать случайные runtime nicknames каноническими именами агентов или ролей.
- Не переносить proposal автоматически в `AGENTS.md`, `ROADMAP.md`, `BACKLOG.md`, `ideas/master_backlog.md` или `/about` без отдельного reviewed update.

## Рекомендуемая последовательность реализации небольшими шагами

1. **Зафиксировать baseline.** Сохранить сравнительную матрицу по исходному кейсу: где Редакция сильнее, где одиночный ChatGPT сильнее, какие свойства нельзя потерять.
2. **Обновить канонический quality contract.** Реализовать только `ROQ-P0-01`: reader outcome + неослабляемые evidence guardrails. Провести review на отсутствие дублирования существующих canonical owners.
3. **Усилить orchestration.** Реализовать `ROQ-P0-02`, `ROQ-P0-03` и `ROQ-P0-07` в Chief Editor и существующем Editorial Decision Frame. Не трогать Review до проверки, что Writer получает полезный контракт.
4. **Добавить production-логику.** Реализовать `ROQ-P0-04`: Reader Model и Learning Design через существующие роли и Professional Communication.
5. **Добавить review-линзы.** Реализовать `ROQ-P0-05` и `ROQ-P0-06` внутри существующего review-gate; не создавать новый stage или artifact.
6. **Протянуть минимальные поля.** Выполнить `ROQ-P1-01` и проверить task pack generator и существующие tests.
7. **Провести пилоты.** Выполнить `ROQ-P1-02` на обучающем лонгриде, рабочем документе и коротком пользовательском тексте.
8. **Откалибровать и закрепить.** По результатам выполнить `ROQ-P1-03` и `ROQ-P1-04`; если улучшение не подтверждено, сузить или откатить конкретную линзу, а не наращивать процесс.
9. **Добавить наблюдаемость отдельно.** Реализовать `ROQ-P2-01` как небольшой независимый slice и проверить на тех же пилотах.
10. **Принять решение о развитии.** Использовать `ROQ-P2-02`; отдельную роль или новый pipeline рассматривать только после повторяющегося доказанного failure pattern.

## Пилотная проверка

### Общие условия

- Один и тот же raw request, brief, source set, source freshness boundary и output constraints для всех сравниваемых вариантов.
- Зафиксированные дата, модель/режим и доступные инструменты.
- Сравнение финальных пользовательских результатов отдельно от сравнения governance/task packs.
- Blind или label-neutral сравнение там, где это практически возможно.
- Project Lead judgment остаётся финальным; модельный reviewer не принимает собственный результат автоматически.

### Кейсы

| Тип | Проверяемый риск | Основной ожидаемый эффект |
| --- | --- | --- |
| Обучающий лонгрид | академичность, слабый мост от старой модели, мало практических примеров | Cognitive Bridge, 3–5 Moments of Insight, Learning Design, конкретное изменение практики |
| Рабочий документ | корректность без решения или следующего действия | ясный reader job, decision/action path, bounded detail, применимость |
| Короткий пользовательский текст | governance overhead, искусственная педагогика, неестественный тон | компактный Reader Review, естественность, ясность и действие без лишней структуры |

### Promotion gate

Изменение можно предлагать к канонизации только если:

- ни один пилот не показывает material regression в correctness, evidence support, neutrality, traceability или review independence;
- обновлённая Редакция не хуже сильного одиночного ChatGPT по каждому material criterion конкретной задачи;
- улучшение можно связать с конкретным P0-изменением, а не только с большей длиной, числом агентов или service artifacts;
- короткая задача не стала заметно тяжелее без reader benefit;
- отрицательные результаты и unresolved tradeoffs явно сохранены.

## Вероятные точки реализации в существующих файлах

Этот список не является разрешением менять все файлы сразу. Точный минимальный diff должен быть выбран отдельной implementation mission после canonical ownership review.

- `AGENTS.md`
- `agents/chief_editor.md`
- `agents/intake_agent.md`
- `agents/writer_agent.md`
- `agents/review_agent.md`
- `agents/final_editor.md`
- `kb/audience_outcome_alignment.md`
- `kb/professional_communication.md`
- `kb/editorial_quality_attributes.md`
- `kb/editorial_planning_framework.md`
- `kb/task_object_model.md`
- `kb/shared_lifecycle_kernel.md`
- `kb/capability_registry.md`
- `pipelines/article_pipeline.md`
- `pipelines/review_pipeline.md`
- `pipelines/social_pipeline.md` — только если пилот короткого текста показывает необходимость общей интеграции
- `templates/artifacts/orchestration_plan_template.md`
- `templates/artifacts/task_manifest_template.md`
- `templates/tasks/article_task_template.md`
- `templates/tasks/review_task_template.md`
- `templates/tasks/social_task_template.md` — только при подтверждённом trigger
- `scripts/generate_task_pack.py`
- `tests/test_task_pack_generator.sh`
- `tests/README.md` и один компактный reader-outcome smoke/manual trial на этапе реализации

## Definition of Done для всей инициативы

Инициатива считается доказавшей ценность, когда на разных типах задач AI Editorial Office стабильно сохраняет свою доказательность, нейтральность, независимый review и трассируемость, при этом не уступает сильному одиночному ChatGPT в reader fit, ясности, конкретике, педагогическом переходе, запоминаемости, практической применимости и естественности; достигает этого через существующие роли и артефакты; и не увеличивает governance cost без измеримой reader benefit.
