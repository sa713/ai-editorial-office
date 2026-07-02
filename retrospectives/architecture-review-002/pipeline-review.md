# Pipeline review

## Article pipeline

Что работает:

- хорошо подходит для статей, объяснений, аналитики;
- держит исследование, письмо, проверку и финализацию раздельно;
- защищает фактические утверждения через `sources.md`, `facts.md`, `claims_table.md`, `claims-used.md`.

Что тормозит:

- много обязательных на практике файлов;
- полная цепочка тяжела для короткой статьи без спорных фактов;
- repeated governance sections увеличивают чтение.

Compact:

- для source-light low-risk: `brief`, `manifest/status`, `draft`, `review`, `final_decision`;
- checklist и summary внутрь `review.md`.

Оставить:

- traceability для фактов;
- independent review;
- запрет на final до approved review.

## Review pipeline

Что работает:

- хорошо формализует проверку как отдельный объект;
- различает review-only задачи и проверку внутри производства;
- сохраняет allowed verdict.

Что тормозит:

- может стать отдельной бюрократией;
- пересекается с `review_agent.md` и `editorial_knowledge/40_editorial_review_system.md`.

Compact:

- один `review.md` с verdict, scope, findings, blockers, re-review scope.

Оставить:

- независимость;
- список проверенных файлов;
- bounded revision.

## Research pipeline

Что работает:

- полезен для источников, фактов, claim-level проверки;
- хорошо отделяет facts, interpretations, assumptions, open questions.

Что тормозит:

- может запускаться там, где пользователь уже дал весь источник и новые факты не создаются;
- `sources.md`, `facts.md`, `claims_table.md` могут быть избыточны для простых внутренних текстов.

Compact:

- source-light: один `research.md` с source notes и open questions;
- full depth только при материальных claims.

Оставить:

- запрет на неподтверждённые факты;
- явную пометку uncertainty;
- открытые вопросы.

## Social pipeline

Что работает:

- хорошо держит короткие объявления, запуск, посты;
- проверяет канал, тон, действие и обещания;
- реальные задачи `TASK-0006`, `TASK-0009`, `TASK-0012` показывают пользу.

Что тормозит:

- для короткого поста слишком много lifecycle-файлов;
- email + messenger могут порождать отдельные draft/final/review artifacts.

Compact:

- один `draft.md` с вариантами каналов;
- один `review.md`;
- `final.md` или финальные channel files только если нужны для отдачи.

Оставить:

- проверку обещаний;
- роль каналов;
- human approval before sending.

## UX writing pipeline

Что работает:

- защищает продуктовую правду;
- требует контекст, состояния, терминологию;
- не даёт UX copy придумывать поведение.

Что тормозит:

- `content-map.md`, `states-table.md`, `terminology-notes.md`, `ux-writer-notes.md` могут быть тяжёлыми для малой правки.

Compact:

- для одной кнопки, ошибки или пустого состояния: `ux-copy.md` + встроенные notes;
- отдельные таблицы только когда есть несколько состояний, терминов или риск.

Оставить:

- запрет на invented product behavior;
- terminology consistency;
- accessibility and state clarity review.

## Нестандартные workflow

Что работает:

- `TASK-0008`, `TASK-0010`, `TASK-0013` доказывают, что редакция умеет работать вне пяти базовых пайплайнов.
- Custom mini-contract уже есть как правильная защита от скрытого процесса.

Что тормозит:

- каждый раз приходится заново описывать workflow;
- легко создать слишком много диагностических артефактов.

Compact:

- один блок в `orchestration_plan.md`: why no pipeline fits, stages, artifacts, review target, stop conditions.
- не превращать повторяющийся custom flow в новый пайплайн без 3-5 повторов.

Оставить:

- review-gate;
- explicit boundary diagnosis vs design;
- запрет на Artificial Concept Completion.

