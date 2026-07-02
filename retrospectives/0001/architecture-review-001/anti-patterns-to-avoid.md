# Anti-patterns to avoid

## 1. Избыточная агентность

Не стоит добавлять агента на каждый тип редакционного суждения.

Опасные идеи:

- `style_editor`;
- `fact_checker`;
- `terminology_reviewer`;
- `structure_reviewer`;
- `mode_classifier`;
- `usefulness_reviewer`;
- отдельный агент на каждый editorial mode.

Почему опасно:

- больше handoff;
- больше coordination overhead;
- больше возможностей потерять состояние;
- меньше ответственности у ядра review;
- качество может снизиться из-за фрагментации.

Лучший путь: добавить check, example или bounded rule внутри существующей роли.

## 2. Бюрократия вместо редакционной пользы

Опасный паттерн: считать заполненность artifacts доказательством качества.

Признаки:

- brief заполнен, но не изменил структуру;
- review checklist полный, но reader outcome не проверен;
- handoff пересказывает всю задачу;
- manifest становится narrative log;
- low-risk задача имеет full artifact set без причины.

Правило:

```text
Если поле или артефакт не меняет writing, review, governance или restartability, он не должен быть обязательным.
```

## 3. Чрезмерная формализация compact brief

Compact editorial brief силен именно потому, что это editorial thinking made visible, not administration.

Не стоит превращать его в форму с обязательными полями:

- audience segment;
- stakeholder map;
- channel;
- tone;
- risk;
- evidence status;
- reader state;
- dominant mode;
- supporting mode;
- context limit;
- review target;
- examples;
- constraints;
- length;
- owner.

Для некоторых задач это нужно. Для многих — нет.

## 4. Enterprise theatre

Для single-user AI-редакции опасны имитации корпоративных платформ:

- сложные approval matrices;
- RACI-таблицы для каждого текста;
- многоуровневые sign-off states;
- workflow engine до появления реального volume;
- dashboards вместо better artifacts;
- "policy compliance" вместо reader usefulness.

Главный критерий: помогает ли это выпускать более полезный, проверяемый и безопасный текст?

## 5. Multi-agent framework ради модности

Система уже multi-role. Это не значит, что ей нужен multi-agent runtime.

Не стоит:

- строить автономных агентов, которые сами вызывают друг друга;
- добавлять goal loops для обычных текстов;
- делать параллельные subagents без явной независимости задач;
- автоматизировать orchestration до стабилизации compact path.

Best-practices ориентир: сначала простой loop и надежные boundaries, потом расширение по измеренным провалам.

## 6. Full automation of editorial judgment

Редакционное качество не нужно полностью механизировать.

Опасные идеи:

- numeric usefulness score;
- automatic approval if checklist passes;
- fixed thresholds for all texts;
- model-generated confidence as review evidence;
- automatic publication after finalized.

Review должен поддерживать judgment, а не заменять его fake metrics.

## 7. Checklist inflation

Failure patterns полезны как diagnostic vocabulary. Они станут вредны, если каждый pattern станет обязательным пунктом review.

Опасный симптом:

```text
Review passed all 48 checks.
```

Но текст все равно не помогает читателю.

Лучше:

```text
Dominant failure: answer delay.
Repair: move reader-facing change into opening.
```

## 8. Treating old tasks as perfect templates

Старые task folders содержат и сильные решения, и legacy artifacts:

- ambiguous handoff names;
- `final(1).md`;
- varying manifest formats;
- custom compact handoffs.

Не стоит копировать старую структуру без проверки against current AGENTS/project-state.

## 9. More modes instead of better examples

Editorial modes уже покрывают основные interaction behaviors. Новые micro-modes могут ухудшить систему.

Не добавлять:

- "announcement mode";
- "leadership mode";
- "employee communication mode";
- "internal magazine mode";
- "launch mode";
- "FAQ mode".

Это форматы или situations, а не обязательно interaction modes.

## 10. Context allergy

Система правильно борется с context inflation. Но нельзя превращать это в запрет на объяснение.

Опасный паттерн:

- удалить rationale, который нужен для trust;
- убрать emotional acknowledgment в change communication;
- сократить educational scaffolding до инструкции;
- убрать nuance, который меняет risk.

Правило:

```text
Context is allowed when it changes action, interpretation, risk, trust, acceptance or transfer.
```

## 11. Prompt-only safety

Не стоит считать, что запреты в markdown сами обеспечивают безопасность.

Для текущей файловой редакции достаточно lightweight checks, но high-governance side effects требуют:

- explicit human approval;
- visible final decision;
- publication/delivery approval state;
- source traceability;
- review evidence.

## 12. Hidden custom pipelines

Если custom flow повторился два-три раза, он уже не custom. Его нужно описать минимально.

Но не надо сразу делать большой pipeline. Сначала:

- name;
- stages;
- required artifacts;
- review target;
- stop conditions.

## 13. Unbounded revision

Опасный паттерн:

- review просит изменения;
- writer меняет шире, чем нужно;
- review находит новые мелкие проблемы;
- цикл повторяется.

Лучше:

- bounded findings;
- repair scope;
- re-review scope;
- escalation after repeated failure.

## 14. Governance language without governance evidence

Не стоит писать "approved", "finalized", "human approval not required" без artifacts.

Для редакционной системы эти слова являются state transitions, а не риторикой.

## 15. Tooling before proof of pain

Не стоит сейчас строить:

- автоматический статус-валидатор;
- web dashboard;
- full eval harness;
- task database;
- agent runtime;
- permission engine.

Сначала нужны простые markdown-level improvements и несколько regression cases.
