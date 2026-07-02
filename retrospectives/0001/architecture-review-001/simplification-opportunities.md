# Simplification opportunities

## Принцип упрощения

Упрощать стоит только то, что:

- не снижает review-gate integrity;
- не ухудшает restartability;
- не разрушает role separation;
- не скрывает human approval;
- не ослабляет usefulness review.

Цель — не сделать систему "легкой" любой ценой. Цель — убрать трение, которое не добавляет редакционной надежности.

## 1. Compact path для low-risk задач

### Сейчас

Даже low-risk задачи теоретически проходят через тот же conceptual lifecycle: brief, manifest, status, orchestration, writing, review, finalization, decision, handoff.

### Упростить

Разрешить compact path:

```text
brief + compact manifest/status -> draft -> compact review -> final -> final note
```

### Что сохранить

- review required;
- writer/reviewer separation;
- finalization vs sending boundary;
- no unsupported claims.

### Польза

Меньше файлов, меньше overhead, выше вероятность, что система будет использоваться для малых задач.

## 2. Common lifecycle вместо повторов в pipelines

### Сейчас

Article, social, UX и review pipelines повторяют:

- role separation;
- allowed statuses;
- review-gate;
- artifact minimalism;
- handoff requirements;
- risk modes.

### Упростить

Оставить common lifecycle в одном canonical месте. В pipelines оставить только различия:

- when to use;
- artifact deltas;
- review focus;
- stage-specific outputs.

### Польза

Меньше drift, легче менять правила.

## 3. Role specs короче

### Сейчас

Agent specs длинные и содержат много governance/pipeline повторов.

### Упростить

Сделать role specs более компактными:

- mission;
- responsibilities;
- forbidden actions;
- inputs;
- outputs;
- decisions;
- escalations.

Sequencing оставить pipelines.

### Польза

Роль быстрее загружается в контекст и меньше конкурирует с task-specific information.

## 4. Templates as fields, not doctrine

### Сейчас

Некоторые templates содержат не только поля, но и много правил.

### Упростить

Templates должны быть fillable scaffolds. Doctrine должна жить в canonical docs.

### Польза

Агент не получает одну и ту же инструкцию из template, pipeline и AGENTS.

## 5. Clarify scaffold files in editorial_knowledge

### Сейчас

`01_principles.md`, `02_editorial_intent.md`, `03_usefulness_review.md` почти пустые, а содержательная логика уже есть в других файлах.

### Упростить

Либо:

- заполнить их как короткий index/summary;

либо:

- явно пометить как placeholders;

либо:

- убрать из активного retrieval path.

### Польза

Меньше ложных источников правды.

## 6. One meaning for compact-handoff

### Сейчас

`compact-handoff.md` используется как финальный user-facing handoff в нескольких задачах. Handoff template при этом описывает role-to-role delta-transfer.

### Упростить

Определить:

- `handoff-*` = role-to-role delta;
- `compact-handoff.md` = final/user-facing transfer summary или compaction artifact, но не оба.

### Рекомендация

Для текущих задач лучше закрепить `compact-handoff.md` как final user-facing handoff.

## 7. Review-summary optional by default

### Сейчас

`review.md`, `qa-checklist.md`, `review-summary.md` и review handoff могут частично повторять outcome/next action.

### Упростить

Для low-risk и simple standard:

- `review.md` содержит verdict, findings, next action;
- отдельный `review-summary.md` создается только если next role needs concise transfer.

### Польза

Меньше повторения без потери review-gate.

## 8. Bounded re-review protocol instead of new artifacts

### Сейчас

Для revisions могут появляться отдельные bounded-revision, review-summary, review-round files.

### Упростить

В `review.md` добавить section:

```markdown
## Re-review scope
```

и обновлять только при необходимости.

### Польза

Меньше файлов, яснее границы повторной проверки.

## 9. Custom workflow mini-contract

### Сейчас

Custom workflows описываются внутри orchestration_plan.

### Упростить

Добавить один мини-контракт:

```text
No existing pipeline fits because:
Custom stages:
Required artifacts:
Review target:
Stop conditions:
```

### Польза

Гибкость сохраняется, но custom flow не становится скрытым процессом.

## 10. Use examples instead of more rules

### Сейчас

Редакционная теория уже достаточно богата.

### Упростить дальнейшее развитие

Следующие additions делать через examples:

- source;
- compact brief;
- selected mode;
- structure decision;
- review finding;
- final repair.

### Польза

Агенты учатся на concrete behavior, а не на новых абстрактных правилах.

## Что не упрощать

Не стоит убирать:

- review-gate;
- role separation;
- source traceability for factual claims;
- human approval boundary;
- task-local artifacts;
- risk modes;
- editorial modes как thinking tool.

Именно они делают систему устойчивой.
