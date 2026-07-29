# Product Intent Review — Step 1 baseline report

## Краткий вывод

Step 1 начинает работу с подтверждённой архитектурной позиции: Product Intent
Review должен стать узкой условной decision lens внутри семейства Professional
Analysis. Полного канонического владельца этой семантики сейчас нет. Текущих
capabilities достаточно как соседних опор, но ни одна из них одновременно не
владеет реконструкцией продуктового замысла, проверками value/fit/mechanism/
viability, главным продуктовым разрывом, классом альтернатив и минимальной
проверкой гипотезы.

## Авторизация и состояние родительской capability

- Step 1 имеет статус `Authorized` в `brief.md`.
- Разрешено опираться на текущий release-candidate contract Professional
  Analysis.
- Это разрешение не принимает Professional Analysis целиком, не меняет её
  статус и не разрешает новый project stage.
- `project-state.md` должен и будет оставлен без изменений.

## Что уже существует

| Механизм | Повторно используемая ответственность | Граница |
| --- | --- | --- |
| Professional Analysis | decision-ready форма анализа, синтез, варианты, implications, recommendation | не владеет полной Product Intent Review моделью |
| Analytical Reasoning | постановка вопроса, гипотезы, опровержение, достаточность | не владеет продуктовым finding и intent contract |
| Evidence Framework | классы evidence, confidence, assumptions, unknowns | Product Intent Review не создаёт свою taxonomy |
| Task Need Recognition / Preflight | сигналы входа, route/depth recommendation, решение Chief Editor | Step 1 не реализует activation behavior |
| Audience & Outcome / reader-centered quality | польза и изменение для читателя/пользователя артефакта | не доказывает ценность самой intervention |
| Planning | варианты, выбор подхода, tradeoffs, reconsideration | не реконструирует продуктовый замысел |
| Architecture Review | fitness архитектурного решения | не универсальный product-intent owner |
| Editorial Challenge Lens / Review Agent | независимый challenge и существующий review verdict | Product Intent Review не является вторым gate |
| Deliverable Knowledge | purpose/fit конкретного типа deliverable | deliverable и product/intervention не тождественны |
| Product owner | решение о запуске, изменении, пилоте или остановке | AI capability не подменяет владельца решения |

## Точный пробел

Нет единого узкого canonical contract, который до глубокой редакционной работы:

1. реконструирует семь элементов замысла без выдумывания данных;
2. разделяет confirmed, hypothesis и unknown через существующий evidence owner;
3. проверяет value, fit, mechanism и viability;
4. выделяет один главный разрыв, способный изменить класс следующего решения;
5. предлагает классы альтернатив без выбора за product owner;
6. задаёт минимальную, не псевдонаучную проверку гипотезы;
7. отделяет продуктовый finding от operational review verdict.

## Минимальная поверхность Step 1

Полный контракт должен жить только в `kb/product_intent_review.md`.
`kb/capability_registry.md` получает краткую запись и mapping.
`AGENTS.md` получает только ownership pointer.
`kb/professional_analysis.md` получает только короткую relationship note.
Изменение `AGENTS.md` требует точной синхронизации `about/AGENTS.md` по
действующему package check.

## Решение по Problem Hypothesis

Исторический Problem Hypothesis остаётся отдельным непринятым proposal.
Step 1 его не интегрирует и не объявляет superseded: первое неявно канонизировало
бы незавершённый workflow contract, второе потребовало бы нормализации текущих
ссылок и поведенческой поверхности. Элемент `problem` в новой спецификации
самостоятельно задаёт ограниченный продуктовый вопрос и не наследует
исторический proposal.

## Отрицательная граница

В Step 1 не меняются routing, task object, роли, pipelines, templates, runtime,
production behavior, review outcomes, task statuses или release state. Проверки
ограничиваются целостностью спецификации, ссылками, scoped diff, lifecycle и
регрессией уже существующего Professional Analysis contract.

## Readiness

Блокирующих пробелов для канонической спецификации нет. Evidence достаточно для
передачи Writer Agent при сохранении перечисленной отрицательной границы.
