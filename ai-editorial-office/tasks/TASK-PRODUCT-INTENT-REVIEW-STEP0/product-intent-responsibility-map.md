# Product Intent Review — responsibility map

Дата: 2026-07-29
Статус: Step 0 complete for review

## Как читать карту

`Existing owner` означает текущего канонического владельца поведения.
`Proposed integration` — рекомендация для следующих шагов, не внесённое
изменение.

## Карта по жизненному циклу

| Момент | Вопрос | Existing owner | Текущее состояние | Proposed integration |
| --- | --- | --- | --- | --- |
| Intake | Есть ли на входе концепция нового вмешательства, неутверждённый формат решения или запрос о целесообразности? | Intake Agent + Task Need Recognition | Общие сигналы есть, специальных product-intent сигналов нет. | Intake фиксирует evidence signals; не активирует capability и не задаёт большой бриф. |
| Routing | Нужна ли проверка: `none`, `limited` или `full`? | Chief Editor, informed by Task Need Recognition | Chief Editor уже выбирает capabilities и depth, но product-intent режим не определён. | Chief Editor выбирает task-local mode и пишет короткое основание/negative evidence в существующий plan/manifest. |
| Research | Какие элементы цепочки подтверждены, предполагаются или неизвестны? | Research Agent + Evidence Framework + Analytical Reasoning | Общая evidence работа существует. | Research Agent восстанавливает модель только из доступных данных и маркирует gaps; отдельный обязательный research artifact не создаётся. |
| Planning / decision | Стоит ли продолжать, уменьшить, проверить, сменить класс решения или остановиться? | Chief Editor + Professional Analysis + Planning | Общие options/recommendation moves существуют, но нет product-intent decision contract. | Product Intent Review как специализированная линза Professional Analysis формирует product judgment до подробного production contract. |
| Production | Как product finding ограничивает оценку или создание материала? | Writer Agent / UX Writer по контракту Chief Editor | Roles обязаны следовать route и не выдумывать product behavior. | В handoff передаётся только компактное решение и границы; полная модель не дублируется. |
| Independent review | Корректно ли активирована линза, подтверждён ли вывод, не подменён ли product owner и не пострадал ли compact path? | Review Agent внутри существующего `review.md` | Все общие challenge moves существуют; product-intent dimension отсутствует. | Review Agent проверяет mode, модель, четыре проверки, главный разрыв, alternative/test boundary и evidence; operational verdict остаётся `approved / changes_requested / blocked`. |
| Finalization | Не исчез ли главный продуктовый вывод под редакционной полировкой? | Final Editor | Должен сохранять approved meaning и caveats. | Только preserve approved product finding; не выполнять новый анализ. |
| Governance | Можно ли закрыть редакционный task и что остаётся решением владельца продукта? | Chief Editor | Существующая governance достаточна. | Явно отделить editorial readiness от product-owner decision и production permission. |

## Карта семи элементов замысла

| Элемент Product Intent Review | Ближайшее текущее покрытие | Coverage | Точный разрыв | Рекомендуемый владелец спецификации |
| --- | --- | --- | --- | --- |
| Аудитория продукта | Audience & Outcome Alignment; Task Need Recognition; Intake | partial | Текущая модель ориентирована на аудиторию артефакта/читателя и не обязана разделять пользователя, заказчика и стейкхолдера продукта. | Product Intent Review lens с reuse Audience Alignment. |
| Проблема | Analytical Reasoning problem framing; Professional Analysis needs/product discovery; historical Problem Hypothesis proposal | partial | Нет принятого compact product-problem contract и требования показать evidence проблемы/цену бездействия. | Product Intent Review lens; evidence owned by Evidence Framework. |
| Требуемое изменение | Reader Outcome Contract; intended outcome fields | partial | Reader change материала не равен изменению поведения/состояния от продукта. | Product Intent Review lens с явным объектом изменения. |
| Предлагаемый продукт | Task object deliverable и UX product context | weak/adjacent | Task deliverable описывает результат Редакции, а не вмешательство; UX Writer получает уже заданный product behavior. | Product Intent Review lens; не расширять deliverable taxonomy значением «product». |
| Механизм воздействия | Analytical Reasoning hypotheses/causal accounts; Learning Design для материала | partial | Нет обязательной причинной цепочки `interaction -> change -> effect` и проверки информационного решения как недостаточного по умолчанию. | Product Intent Review lens. |
| Пользовательский опыт | UX Writer action/state logic; Reader Model/Companion Pass | partial | UX Writer не решает, нужен ли продукт; Reader Model относится к материалу. Нет product-experience reconstruction до production. | Product Intent Review lens; UX Writer только потребляет утверждённые границы. |
| Наблюдаемый результат | Success criterion; Reader Outcome Contract; Evidence validation needed | partial | Нет product-pilot signal, stop/reconsider rule и границ допустимого вывода. | Product Intent Review lens с reuse Evidence Framework. |

## Карта четырёх проверок

| Проверка | Что можно переиспользовать | Чего не хватает |
| --- | --- | --- |
| Ценность | Business/needs analysis; evidence confidence; consequence signals. | Обязательной проверки подтверждённости проблемы, значимости и цены бездействия. |
| Соответствие | Task/result relevance; audience/outcome alignment; deliverable fit. | Отдельного product-to-problem fit и проверки масштаба/лишних целей. |
| Механизм | Analytical Reasoning; hypotheses; disconfirmation; Reader/Learning Design analogies. | Product-specific causal mechanism, required user action, feedback/reinforcement и запрет подменять механизм декларацией. |
| Жизнеспособность | Architecture Review для систем; option evaluation; risk/reversibility; preflight. | Cross-domain feasibility и minimum viable test для курса, сервиса, кампании, события, процесса или инструмента. |

## Границы между смежными способностями

| Смежная способность | Что остаётся у неё | Что нельзя передавать ей |
| --- | --- | --- |
| Task Need Recognition | Advisory detection signals, negative evidence, ambiguity and recommended capability/depth. | Product judgment, activation decision или product model reconstruction. |
| Routing and Preflight | Chief Editor decision `ask / constrain / proceed / block`, mode selection, role/pipeline assignment. | Предметный анализ Product Intent Review. |
| Professional Analysis | Общая analytical product shape, product discovery, needs analysis, options and recommendation. | Детальный product-intent contract без отдельной узкой спецификации. |
| Analytical Reasoning | Причинные гипотезы, competing explanations, assumptions, disconfirmation, sufficiency. | Предметная модель и activation policy. |
| Evidence Framework | Evidence classes, confidence, facts/assumptions/unknowns, validation needed. | Product-specific критерии. |
| Audience & Outcome Alignment | Fit редакционного артефакта аудитории и требуемому reader outcome. | Доказательство ценности и механизма продукта. |
| Deliverable knowledge | Выбор формы редакционного результата. | Решение, нужен ли описываемый продукт. |
| Architecture Review | Fitness архитектурно значимого design decision. | Универсальная проверка неархитектурных продуктов/активностей. |
| Editorial Challenge Lens | Независимая проверка route-validity assumptions в review. | Раннее выполнение product analysis или выбор active route. |
| Review Agent | Независимый verdict по качеству сохранённых artifacts. | Product ownership, новый активный маршрут, research или реализация альтернативы. |

## Authority map для новой линзы

| Действие | Accountable | Responsible/supporting | Не уполномочен |
| --- | --- | --- | --- |
| Зафиксировать входные сигналы | Intake Agent | Task Need Recognition | Keyword classifier |
| Выбрать `none / limited / full` | Chief Editor | Intake evidence, Task Need Recognition | Intake Agent, Research Agent, Review Agent |
| Построить evidence-backed модель | Research Agent, если research назначен; иначе текущий analytical owner по плану | Evidence Framework, Analytical Reasoning, Professional Analysis | Review Agent |
| Принять редакционное routing решение по результату | Chief Editor | Product Intent Review finding | Product Intent Review capability автоматически |
| Принять бизнес/product решение | Владелец продукта / пользователь | Редакция даёт ограниченную рекомендацию | Chief Editor, Research Agent, Review Agent |
| Проверить качество Product Intent Review | Review Agent | Existing review gate | Производитель отчёта |
| Сохранить вывод в финальном наборе | Final Editor, когда он назначен | Approved review scope | Новый analysis |

## Конфликты и дублирование, которых следует избежать

1. Не называть task deliverable «product», иначе смешаются две разные
   сущности.
2. Не превращать режимы `none / limited / full` в task statuses, pipelines или
   review levels.
3. Не создавать второй review-gate: product-intent dimension живёт внутри
   существующего `review.md`.
4. Не копировать evidence taxonomy, reasoning moves, audience model или
   planning framework в новую спецификацию.
5. Не расширять Architecture Review до всех продуктов: это разрушит его
   предметную точность.
6. Не считать Professional Analysis полностью достаточной без narrow
   product-intent contract: общий lens не гарантирует требуемую
   последовательность и output.
7. Не принимать исторический Problem Hypothesis proposal за current canon.
8. Не создавать Product Strategist или Product Reviewer role: уникального
   accountability conflict не обнаружено.

## Итоговая карта ответственности

Минимальная архитектура распределена:

```text
Task Need Recognition
    -> advisory signal
Chief Editor
    -> mode and route decision
Product Intent Review lens within Professional Analysis
    -> product model + four checks + main gap + minimum validation
Existing Writer / UX Writer path
    -> material work only inside approved product finding
Review Agent
    -> independent challenge inside existing review gate
Chief Editor / product owner
    -> editorial governance / actual product decision remain separate
```

Новой роли, стадии, pipeline, task status, review outcome или обязательного
standalone task artifact эта карта не требует.
