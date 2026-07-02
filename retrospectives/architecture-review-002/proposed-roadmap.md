# Proposed roadmap

## Принцип

Сначала trimming и упрощение. Потом скорость. Автоматизация только если ручные правила не выдержат практики.

## Шаг 1. Условные артефакты

Scope:

- `review-summary.md`;
- `qa-checklist.md`;
- `finalization-checklist.md`;
- `open-questions.md`;
- `compact-handoff.md`.

Изменение:

- закрепить, когда файл нужен;
- для low-risk встроить checklist и summary в `review.md`;
- не создавать пустые файлы.

Граница:

- review остаётся обязательным;
- high-governance не сокращается.

## Шаг 2. Короткое чтение контекста

Scope:

- context loading rules;
- task restart path;
- use of manifest.

Изменение:

- описать минимальный набор чтения по risk/depth;
- запретить чтение старых task folders как шаблонов;
- добавить current-version pointer для версионных задач.

Граница:

- при конфликте или high-governance читать полный набор.

## Шаг 3. Сократить шаблоны

Scope:

- `templates/tasks/*`;
- `status_template.md`;
- `final_decision_template.md`;
- `orchestration_plan_template.md`.

Изменение:

- оставить поля и короткие guardrails;
- убрать повтор устава и пайплайнов;
- сделать compact final decision shape.

Граница:

- не менять активные pipeline semantics;
- не удалять обязательные governance fields.

## Шаг 4. Сжать роли

Scope:

- `agents/*.md`.

Изменение:

- оставить mission, responsibilities, forbidden actions, inputs, outputs, decision boundaries, stop conditions;
- убрать повтор полного lifecycle;
- сослаться на canonical owners.

Граница:

- не менять MVP agent set;
- не добавлять Editor Agent.

## Шаг 5. Optional validation только после теста

Scope:

- ручная проверка freshness и artifact omissions.

Условие:

- делать только если после шагов 1-4 остаются частые ошибки свежести или пропуска нужных артефактов.

Граница:

- не делать engine;
- не делать dashboard;
- не делать автоматическое routing.

