# Product Intent Review — Step 2 baseline report

## Краткий вывод

Step 1 уже создал полный semantic owner, но текущая operational surface не
умеет надёжно сохранить отдельные advisory recommendation и Chief Editor mode
decision, передать product-first consequence или условно загрузить owner при
restart. Task Need Recognition содержит общий evidence-first и negative-evidence
contract, поэтому отдельный classifier не нужен.

## Текущее покрытие

| Surface | Что уже есть | Точный Step 2 gap |
| --- | --- | --- |
| `kb/task_need_recognition.md` | Evidence-first signals, negative evidence, advisory-only boundary, compact view | Нет Product Intent Review signal families и трёх рекомендаций |
| `kb/task_object_model.md` | `active_capabilities`, optional advisory view, manifest/orchestration artifact responsibilities | Нет различимых PIR recommendation и Chief decision/restart semantics |
| Intake Agent | Собирает observed evidence, negative evidence и advisory TNR | Нет явных product-intent сигналов и запретов на семь вопросов/анализ |
| Chief Editor | Принимает/override capabilities и depth | Нет отдельного PIR mode/focus/product-first permission contract |
| Orchestration template | TNR view и Chief decision, preflight, production contract | Нет компактного PIR routing block |
| Manifest template | Restart-critical active capability/current state | Нет минимального optional PIR state pointer |
| Task-pack generator | Загружает pipeline, role, reader, source, profile и status context | Не читает explicit PIR mode и не подключает owner |
| Existing tests | Manual TNR scenarios and executable generator shell test | Нет positive/negative/ambiguous PIR route and loading regressions |

## Что можно переиспользовать

- Существующая signal-family модель TNR принимает multi-signal evidence.
- `confidence and negative evidence` уже предотвращает topic-only activation.
- Chief Editor уже имеет право accept/reject/narrow/override advisory views.
- `active_capabilities` и orchestration plan уже являются правильными task
  object views.
- Generator уже читает manifest first и orchestration fallback, что подходит
  для restart-critical mode.
- Shell test architecture generator позволяет проверить реальное conditional
  read-set behavior без создания runtime classifier.

## Доказанная необходимость generator change

Registry update Step 1 сам по себе не подключает capability: generator не
читает `active_capabilities` и не имеет generic capability-file resolution.
Для Step 2 нужен узкий parser только для explicit Chief Editor
`Product Intent Review mode`.

Generator не должен выводить recommendation из request text. Он должен:

1. читать сохранённое mode decision;
2. подключать `kb/product_intent_review.md` только для `limited`/`full`;
3. не подключать owner для `not_needed` или отсутствующего mode;
4. предпочитать manifest как restart anchor, затем orchestration fallback;
5. не реагировать на слова “product”, “course”, “service” и другие keywords.

## Test baseline

- Task-pack generator tests сейчас исполняемые и проходят.
- Task Need Recognition, outcome-first, preflight и Professional Analysis smoke
  tests являются manual synthetic contracts.
- Step 2 должен сохранить эти contracts и добавить executable shell coverage
  для mode-to-read-set/restart behavior.

## Forbidden baseline

Не требуется менять Task Status Model, Shared Lifecycle Kernel, pipelines,
Review Agent, Final Editor, project state, Step 1 semantic owner или полный
Product Intent Review analysis.
