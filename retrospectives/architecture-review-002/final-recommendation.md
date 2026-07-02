# Final recommendation

## Что улучшать первым

Первым улучшать не роли и не пайплайны, а артефактную нагрузку.

Начать с правила:

- low-risk и simple standard используют один `review.md`;
- `qa-checklist.md`, `review-summary.md`, `finalization-checklist.md` создаются только при явном потребителе;
- handoff остаётся короткой передачей изменений;
- старые task folders не копируются как шаблон.

Это даст быстрый выигрыш без риска для качества.

## Что не трогать

- `AGENTS.md` как устав.
- MVP agent set.
- Review-gate.
- Research/writing separation.
- Finalization vs publication approval.
- Bounded revision.
- Source material as data.
- Diagnostic-analysis and author-facing diagnosis updates.
- Запрет Artificial Concept Completion и Premature Solution Substitution.

## Главный выигрыш по скорости

Главный выигрыш — сократить количество служебных файлов на простых задачах.

Реальные задачи показывают, что редакция умеет производить хороший результат. Но часть времени уходит на обслуживание артефактов: статусы, handoff, summary, checklist, final notes. Сокращение этого слоя даст больше скорости, чем новый инструмент.

## Главный выигрыш по лимитам

Главный выигрыш — короткий путь чтения:

1. `AGENTS.md` или краткая ссылка на инварианты.
2. `task-manifest.md`.
3. Последний handoff или объект работы.
4. Только нужный пайплайн / KB.

Не читать весь проект, все ретроспективы и все старые артефакты без причины.

## Опасные изменения

- Новые агенты.
- Автоматический движок маршрутизации.
- Scoring review.
- Обязательная проверка всех полей шаблона.
- Новый режим на каждый тип текста.
- Поведенческая система вокруг reader-state.
- Ослабление review под видом скорости.
- Откат diagnostic guardrails под видом "меньше осторожности".

## Следующий bounded update

Сделать один узкий update:

**Artifact depth normalization for compact and standard tasks.**

Scope:

- условность `qa-checklist.md`, `review-summary.md`, `finalization-checklist.md`, `open-questions.md`;
- compact review shape;
- short handoff rule;
- current-version pointer for versioned tasks;
- note that legacy tasks are historical evidence, not templates.

Не включать:

- переписывание всех ролей;
- новый пайплайн;
- новые агенты;
- автоматизацию;
- изменение diagnostic/author-facing diagnosis.

Это самый безопасный следующий шаг: меньше трения, меньше лимитов, review и governance остаются на месте.

