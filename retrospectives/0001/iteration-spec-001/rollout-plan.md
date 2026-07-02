# Rollout plan

## Шаг 1. Ownership map

- Какие файлы меняются: target canonical ownership location; possibly `AGENTS.md` only as short pointer.
- Зачем: решить, где живут rules before adding new ones.
- Зависимости: approved bounded scope.
- Что проверить после шага: no duplicated long rules; AGENTS did not become pipeline copy.
- Rollback condition: ownership map repeats policy instead of assigning owners.

## Шаг 2. Compact path

- Какие файлы меняются: orchestration guidance, selected pipeline notes, possibly Chief Editor guidance.
- Зачем: define compact/normal/full and compact allow/deny rules.
- Зависимости: ownership map.
- Что проверить после шага: review still required; compact forbidden for high-governance; omitted artifacts require rationale.
- Rollback condition: compact path can be read as bypass governance.

## Шаг 3. Manifest freshness and governance

- Какие файлы меняются: manifest template/guidance, final decision guidance if needed, task status guidance only if semantics conflict.
- Зачем: make restart and human approval state visible.
- Зависимости: compact path.
- Что проверить после шага: manifest remains short; finalization/publication approval are separate; status model not duplicated.
- Rollback condition: manifest becomes longer than necessary or starts carrying full review/status.

## Шаг 4. Handoff semantics

- Какие файлы меняются: handoff template/guidance, compact-handoff guidance, context-summary guidance.
- Зачем: separate role-to-role delta, final user transfer and recovery summary.
- Зависимости: manifest guidance, because handoff must not duplicate manifest.
- Что проверить после шага: `handoff-*`, `compact-handoff.md`, `context-summary.md` have distinct uses.
- Rollback condition: handoff docs become longer or more ambiguous than before.

## Шаг 5. Review ergonomics

- Какие файлы меняются: review pipeline/guidance, review template, Review Agent note.
- Зачем: define compact review, independence check and bounded revision.
- Зависимости: compact path and governance state.
- Что проверить после шага: compact review has minimum evidence; `changes_requested` has repair/re-review scope; no scoring system added.
- Rollback condition: compact review becomes checklist theater or rubber stamp.

## Шаг 6. Custom workflow and source trust

- Какие файлы меняются: orchestration guidance for mini-contract; source/context guidance for source trust rule; maybe review guidance for source-heavy check.
- Зачем: keep custom flows explicit and source materials bounded as data.
- Зависимости: ownership map, review ergonomics.
- Что проверить после шага: no new pipeline created; no source labeling bureaucracy; embedded source instructions cannot override system/user instructions.
- Rollback condition: mini-contract becomes default form for normal tasks or source trust labels bloat artifacts.

## Шаг 7. Trial on future tasks only

- Какие файлы меняются: only new task artifacts created after implementation.
- Зачем: validate compact path without migrating legacy tasks.
- Зависимости: all prior steps.
- Что проверить после шага: artifact count, restartability, review quality, governance clarity, omitted artifact rationale.
- Rollback condition: compact task loses source traceability, review independence or publication approval clarity.

## Шаг 8. Retrospective

- Какие файлы меняются: new retrospective only.
- Зачем: decide whether to keep, trim or suspend the iteration changes.
- Зависимости: at least 2-3 future compact/normal tasks.
- Что проверить после шага: which artifacts changed downstream decisions; which fields were unused; any drift introduced.
- Rollback condition: improvements reduce paperwork but also reduce quality or safety.
