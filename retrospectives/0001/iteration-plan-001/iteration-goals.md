# Iteration goals

## Назначение итерации

Эта итерация развивает AI-редакцию как рабочую редакционную систему, а не как agent framework. Ее задача — снизить операционное трение, drift и artifact overhead, сохранив уже работающие сильные стороны:

- repository-first memory;
- role separation;
- review-gate;
- source traceability;
- governance clarity;
- usefulness-first editorial core.

Это bounded improvement iteration. Она не должна менять философию системы, добавлять новые роли или строить платформу автоматизации.

## Главные цели

1. **Сделать compact execution допустимым и управляемым.**
   Нужен легкий путь для low-risk и simple standard задач, чтобы простая работа не оплачивала полный audit cost high-governance задач.

2. **Укрепить restartability без раздувания файлов.**
   Manifest должен лучше показывать актуальное состояние, next action и governance state, но не становиться вторым `status.md`.

3. **Снизить drift между документами.**
   Нужно ясно определить, какие файлы являются canonical owners для invariants, statuses, pipeline sequence, role behavior, templates и editorial doctrine.

4. **Сделать review более эргономичным.**
   Review должен оставаться обязательным, но его depth должен соответствовать risk mode. Compact review не должен превращаться в bypass review.

5. **Закрепить bounded revision.**
   `changes_requested` должен по умолчанию вести к точечной доработке, а не к новому writing cycle.

6. **Прояснить handoff semantics.**
   Role-to-role handoff, compact final handoff и context-summary не должны смешиваться.

7. **Усилить governance clarity.**
   `finalized` не должно читаться как approval to send/publish. Human approval state должен быть виден в late-stage tasks.

8. **Защититься от bloat.**
   Система должна явно запрещать создавать artifacts, fields, checks и rules, которые не меняют writing, review, governance или restartability.

## Anti-goals

В рамках этой итерации не делать:

- redesign AI-редакции;
- новых агентов;
- отдельного Editor Agent;
- fact-checker, style editor, structure reviewer или terminology reviewer;
- workflow engine;
- automation platform;
- scoring system;
- eval system;
- dashboards;
- numeric quality metrics;
- full event store;
- expansion of editorial modes;
- новые editorial doctrine documents без repeated real failures;
- enterprise approval framework;
- multi-agent runtime;
- connector/tool permission platform.

## Constraints

- Review-gate остается обязательным.
- Research, writing, review, finalization и governance остаются разделенными, когда задача требует этих стадий.
- Compact path не применяется к high-governance задачам.
- Source traceability для factual/product/policy claims не ослабляется.
- Human approval must remain explicit when required.
- Existing tasks не переписываются и не мигрируются массово.
- Legacy artifacts можно пометить как historical patterns, но не надо чистить их в этой итерации.
- Любое новое правило должно уменьшать ambiguity или overhead; если оно добавляет процедуру без явной пользы, оно не входит в scope.

## Success criteria

Итерация успешна, если после нее:

- low-risk/simple standard task имеет понятный compact path;
- manifest содержит freshness/governance state без превращения в narrative log;
- ownership of rules между `AGENTS.md`, pipelines, templates, agent specs и editorial knowledge ясно описан;
- `compact-handoff.md`, role handoff и `context-summary.md` не путаются;
- review artifacts могут быть compact/normal/full без потери review-gate;
- `changes_requested` имеет bounded default behavior;
- custom workflows получают mini-contract, но не новый большой pipeline;
- source materials clearly treated as data, not instructions;
- число обязательных artifacts для простых задач уменьшается;
- система не добавляет новых agents, engines, scoring или doctrine layers.

## Non-success signals

Итерация считается неудачной, если:

- compact path начинает использоваться для high-governance задач;
- review becomes optional in practice;
- manifest становится длиннее status;
- появляются новые agents или псевдо-агенты;
- создается новый большой pipeline вместо compact rule;
- templates становятся еще более доктринальными;
- появляется scoring/eval/dashboard work;
- old duplication просто переносится в новый документ.
