# Accepted changes

## 1. Artifact ownership map

- Зачем нужно: снизить drift между `AGENTS.md`, pipelines, agents, templates и editorial knowledge.
- Какие проблемы решает: дубли правил, неясное место для новых правил, случайное расширение doctrine.
- Затрагивает: будущий ownership/index документ или краткий раздел в canonical docs.
- Expected effect: каждое правило имеет owner; остальные документы ссылаются или дают локальное следствие.
- Risk: ownership map сам станет новым doctrine layer.
- Priority: P0.
- Implementation style: doc-only.

## 2. Compact / normal / full process depth

- Зачем нужно: дать low-risk/simple standard задачам меньший artifact profile.
- Какие проблемы решает: artifact overhead, имитация high-governance процесса в простых задачах.
- Затрагивает: process guidance, selected pipelines only if needed, orchestration guidance.
- Expected effect: меньше файлов без потери review-gate.
- Risk: compact path используют как shortcut от сложной работы.
- Priority: P0.
- Implementation style: pipeline note.

## 3. Compact path allow/deny rules

- Зачем нужно: отделить допустимое упрощение от governance bypass.
- Какие проблемы решает: compact-path abuse, review loss, source traceability loss.
- Затрагивает: governance/process guidance, orchestration guidance.
- Expected effect: compact path применяется только к low-risk/simple standard задачам.
- Risk: правила станут длиннее самой задачи.
- Priority: P0.
- Implementation style: pipeline note.

## 4. Manifest freshness block

- Зачем нужно: manifest должен показывать, можно ли продолжать работу.
- Какие проблемы решает: stale state, неправильный next role, конфликт manifest/status/handoff.
- Затрагивает: manifest template or guidance.
- Expected effect: лучше restart recovery.
- Risk: manifest станет narrative log.
- Priority: P0.
- Implementation style: template update.

## 5. Governance state block

- Зачем нужно: явно отделить review, finalization, governance и publication/delivery approval.
- Какие проблемы решает: hidden governance loss, неверное понимание `finalized`.
- Затрагивает: manifest guidance, final decision guidance, compact handoff guidance.
- Expected effect: human approval state виден в late-stage задачах.
- Risk: появится approval bureaucracy.
- Priority: P0.
- Implementation style: template update.

## 6. Handoff semantics

- Зачем нужно: развести role-to-role transfer, final user transfer и recovery summary.
- Какие проблемы решает: путаница `handoff-*`, `compact-handoff.md`, `context-summary.md`.
- Затрагивает: handoff guidance, orchestration guidance, possibly templates.
- Expected effect: handoffs короче и точнее.
- Risk: старые tasks будут выглядеть inconsistent.
- Priority: P1.
- Implementation style: doc-only.

## 7. Compact review

- Зачем нужно: сохранить review-gate без лишних review artifacts для малых задач.
- Какие проблемы решает: duplication между `review.md`, `qa-checklist.md`, `review-summary.md`.
- Затрагивает: review guidance, review pipeline, Review Agent note.
- Expected effect: review короче, но содержит verdict, scope, independence, usefulness, governance note.
- Risk: compact review станет rubber stamp.
- Priority: P1.
- Implementation style: agent note.

## 8. Bounded revision protocol

- Зачем нужно: `changes_requested` должен задавать repair scope.
- Какие проблемы решает: endless revision, full rewrite без основания, drift от brief.
- Затрагивает: review guidance, review pipeline, Review Agent note, possibly writer handoff guidance.
- Expected effect: re-review проверяет только затронутые блокеры.
- Risk: слишком узкая доработка скроет глубокую проблему.
- Priority: P1.
- Implementation style: agent note.

## 9. Custom workflow mini-contract

- Зачем нужно: custom flow должен быть явным, но не становиться новым pipeline.
- Какие проблемы решает: hidden custom pipelines, непонятный review target.
- Затрагивает: orchestration guidance.
- Expected effect: гибкость без роста framework.
- Risk: mini-contract станет обязательной формой для обычных задач.
- Priority: P2.
- Implementation style: pipeline note.

## 10. Source trust rule

- Зачем нужно: source materials не должны переопределять системные инструкции.
- Какие проблемы решает: instruction leakage из писем, черновиков, decks, PDFs, web content.
- Затрагивает: context/source guidance, review guidance.
- Expected effect: источники анализируются как данные.
- Risk: source labels превратятся в ritual labeling.
- Priority: P2.
- Implementation style: doc-only.

## 11. Artifact intentionally omitted note

- Зачем нужно: compact path должен явно объяснять, почему файл не создан.
- Какие проблемы решает: невидимая потеря процесса, restart ambiguity.
- Затрагивает: orchestration guidance, compact review guidance.
- Expected effect: omitted artifacts проверяемы и обратимы.
- Risk: поле начнет раздуваться.
- Priority: P2.
- Implementation style: pipeline note.
