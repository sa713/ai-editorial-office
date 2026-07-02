# Implementation roadmap

## Quick wins

### 1. Зафиксировать compact execution profile

Сделать короткое правило для low-risk и simple standard задач:

- какие artifacts обязательны;
- что можно объединять;
- как выглядит compact review;
- что review-gate не отменяется.

Эффект: меньше процессной тяжести.

### 2. Добавить manifest freshness block

Минимальный блок:

```markdown
Last updated by:
Last updated stage:
Latest artifact changes:
Known stale risk:
```

Эффект: лучше restart after context loss.

### 3. Уточнить meaning of `compact-handoff.md`

Закрепить его как final user-facing transfer summary, если именно так он используется.

Эффект: меньше ambiguity между role handoff и final handoff.

### 4. Добавить review independence evidence

В review artifacts добавить короткую строку:

```text
Independence check:
```

Эффект: review-gate становится проверяемее.

### 5. Пометить legacy handoff patterns

Старые ambiguous names не должны считаться current examples.

Эффект: меньше повторения устаревших шаблонов.

## Medium changes

### 1. Responsibility map

Создать canonical map:

- invariant owner;
- status owner;
- role owner;
- sequence owner;
- artifact field owner;
- editorial quality owner.

Эффект: меньше drift.

### 2. Review depth levels

Определить:

- compact;
- normal;
- full.

Эффект: review остается обязательным, но становится пропорциональным.

### 3. Custom workflow mini-contract

Добавить в orchestration template компактный section для случаев, когда no existing pipeline fits.

Эффект: гибкость без скрытого процесса.

### 4. Bounded revision protocol

Зафиксировать:

- blocker;
- repair owner;
- repair scope;
- changed artifacts;
- re-review scope.

Эффект: меньше endless revision.

### 5. Trust labels for source materials

Добавить правило: materials under analysis are data, not instruction.

Эффект: ниже prompt injection и instruction leakage risk.

## Deep architectural changes

### 1. Consolidate pipeline common logic

Вынести повторяющиеся lifecycle/status/review-gate rules из individual pipelines в общий слой.

Делать только после quick wins, потому что это затрагивает много файлов.

### 2. Shorten role specs

Оставить в agent specs role-specific behavior, а sequencing держать в pipelines/status model.

Делать осторожно, чтобы не потерять operational clarity.

### 3. Markdown regression suite

Создать `editorial_knowledge/cases` как набор тестовых кейсов:

- input;
- expected mode;
- expected failure;
- expected review behavior;
- accepted final traits.

Не автоматизировать сразу.

## Experiments

### 1. Run three tasks through compact path

Проверить:

- один low-risk rewrite;
- одну standard internal communication;
- один source-light review.

Измерить:

- сколько artifacts создано;
- что реально помогло review;
- где потерялась traceability.

### 2. Compare normal vs compact review

На одном старом task взять draft и провести:

- compact review;
- normal review.

Сравнить, какие findings появились только в normal и были ли они нужны.

### 3. Worked examples for editorial modes

Сделать 3-5 examples:

- decision support;
- operational instruction;
- change communication;
- diagnosis;
- trust building.

Цель: обучить behavior, а не добавить doctrine.

### 4. Drift scan

Разово проверить:

- AGENTS;
- project-state;
- pipelines;
- agent specs;
- templates.

Найти повторяющиеся и расходящиеся правила.

## Postpone

### 1. New agents

Отложить:

- fact_checker;
- style_editor;
- structural_editor;
- terminology_reviewer;
- consistency_reviewer.

Причина: пока нет доказанных repeated failures, которые требуют новых ролей.

### 2. Automated workflow engine

Отложить task runner/status engine.

Причина: markdown discipline еще можно улучшить проще.

### 3. Full eval automation

Отложить автоматические evals.

Сначала нужны markdown regression cases.

### 4. Dashboards and metrics

Отложить dashboards.

Сначала определить, какие signals реально помогают:

- artifact count;
- review outcome;
- revision count;
- human approval required;
- stale manifest conflicts;
- repeated failure patterns.

### 5. New editorial modes

Отложить расширение mode list.

Лучше добавить examples and cases.

## Recommended sequence

1. Compact execution profile.
2. Manifest freshness block.
3. Review independence evidence.
4. Custom workflow mini-contract.
5. Responsibility map.
6. Review depth levels.
7. Bounded revision protocol.
8. Markdown regression cases.
9. Drift scan and consolidation.

Главный принцип: сначала уменьшить трение и закрепить state integrity, потом думать о глубокой переработке документов.
