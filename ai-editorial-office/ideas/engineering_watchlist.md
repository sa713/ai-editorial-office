# Engineering Watchlist

Статус документа: `engineering observation log`
Дата создания: 2026-06-09

Этот файл фиксирует слабые инженерные сигналы, риски и наблюдения по развитию
ИИ-редакции.

Это не backlog, не roadmap, не список задач и не production source of truth.
Файл не переопределяет `AGENTS.md`, `ai-editorial-office/AGENTS.md`,
production-роли, пайплайны, review-gate, шаблоны или task lifecycle.

Назначение:

```text
наблюдение -> watchlist -> если повторяется, confirmed pattern
-> если требует действия, backlog -> если исправлено, resolved
```

Наблюдение попадает в backlog только после подтверждения, повторения или
отдельного решения о действии. Пока наблюдение находится здесь, оно не является
обязательством на разработку.

Допустимые статусы:

- `observation`
- `watch`
- `confirmed pattern`
- `moved to backlog`
- `resolved`

## Формат записи

```md
## OBS-000X — короткое название

Дата:
Статус:

Контекст:

Наблюдение:

Почему важно:

Подтверждения:

Следующее действие:
```

## OBS-0001 — Hardcoded evidence-mode detection in task pack generator

Дата: 2026-06-09
Статус: watch

Контекст:
P5 task pack generator.

Наблюдение:
В `generate_task_pack.py` используется `SOURCE_EVIDENCE_MODE_RE` со списком
жёстко заданных evidence/source keywords.

Почему важно:
Если позже появится новый evidence mode или новое обозначение source-bound
задачи, generator может не включить нужный task-local evidence artifact.

Подтверждения:
Пока это не баг. P5 тесты проходят. Это риск расширяемости.

Следующее действие:
Наблюдать. Вернуться, если появятся новые evidence modes или повторится
проблема с source artifacts.

## OBS-0002 — Missing handoff warnings may be compact-case noise

Дата: 2026-06-09
Статус: watch

Контекст:
P1 сравнение первых трёх end-to-end cases.

Наблюдение:
Во всех трёх compact cases task pack generator предупреждал о missing handoff
files.

Почему важно:
Warning повторяется, но не ломает выполнение. Есть риск, что такие
предупреждения будут создавать шум и снижать доверие к проверкам.

Подтверждения:
В P1 это признано repeated but non-blocking pattern.

Следующее действие:
Не фиксить сейчас. Вернуться, если warning начнёт мешать ревью или скрывать
настоящие проблемы.

## OBS-0003 — Chief Editor can accumulate too much execution responsibility

Дата: 2026-06-09
Статус: watch

Контекст:
P2 Codex Task Standard.

Наблюдение:
Chief Editor теперь владеет не только routing/preflight, но и переходом
normalized brief -> Codex task / check-pack contract.

Почему важно:
Это логично сейчас, но со временем Chief Editor может начать разрастаться и
смешивать routing, planning, execution contract и review-support.

Подтверждения:
Пока проблемы нет. P2 не добавил новых ролей и не ослабил review-gate.

Следующее действие:
Наблюдать за ростом `chief_editor.md`. Вернуться, если файл начнёт превращаться
в большой operational manual.

## OBS-0004 — KB standards can become too long to be useful

Дата: 2026-06-09
Статус: watch

Контекст:
P2 `kb/codex_task_standard.md`.

Наблюдение:
Файл оказался приемлемым, но было подозрение, что reusable KB standards могут
разрастаться в мини-книги.

Почему важно:
Если KB-файлы станут слишком длинными, агенты будут хуже удерживать их в
контексте, а пользователю будет сложнее проверять изменения.

Подтверждения:
Для P2 проблема не подтвердилась: файл компактный, значительная часть —
шаблоны и примеры.

Следующее действие:
Использовать как watchpoint для будущих KB standards. При добавлении новых KB
проверять компактность.

## OBS-0005 — Borderline inference should remain visible

Дата: 2026-06-09
Статус: watch

Контекст:
P1.5 validation trials.

Наблюдение:
В некоторых тестах Intake делал допустимые, но близкие к границе inference,
например “likely internal communication task”.

Почему важно:
Такие inference полезны, но при накоплении могут начать превращаться в скрытые
фантазии.

Подтверждения:
P1.5 validation прошла успешно, фантазии не выявлены.

Следующее действие:
Наблюдать в будущих real-world tasks. Если borderline inference начнёт повторно
искажать brief, перенести в backlog как refinement для intake guidance.

## OBS-0006 — /about sync/check is repeatedly unavailable in current checkout

Дата: 2026-06-09
Статус: watch

Контекст:
Несколько последних system updates.

Наблюдение:
`/about` check повторно падает, потому что `/about` отсутствует в текущем
checkout.

Почему важно:
Backlog говорит, что `/about` — compact memory package для ChatGPT, но текущая
рабочая копия не позволяет выполнить sync/check. Это может создавать ложные
failed checks и неясность, когда `/about` реально должен обновляться.

Подтверждения:
P1.5 и P2 отчёты фиксировали `/about` check failure из-за отсутствующей
директории.

Следующее действие:
Не чинить в этом апдейте. Вернуться отдельно, если `/about` снова станет
обязательной частью system update workflow.

## OBS-0007 — Task-local packets can accidentally enter public repo

Дата: 2026-06-09
Статус: confirmed pattern

Контекст:
P2 cleanup.

Наблюдение:
Task-local packet `TASK-P2-CODEX-TASK-STANDARD` случайно попал в commit и был
удалён отдельным cleanup-коммитом.

Почему важно:
Safe-core repo не должен публиковать реальные task materials. Даже sanitized
task-local packets лучше держать локально, если они не являются production
tests/fixtures.

Подтверждения:
P2 потребовал cleanup commit `Remove P2 task-local packet from repository`.

Следующее действие:
Наблюдать. Если повторится, добавить guard/check или обновить Codex task
standard с явным commit-scope предупреждением.

## OBS-0008 — Backlog updates can become too verbose

Дата: 2026-06-09
Статус: watch

Контекст:
P1 и P5 backlog updates.

Наблюдение:
Некоторые backlog updates получаются заметно больше, чем сам управленческий
вывод.

Почему важно:
Master backlog должен оставаться planning artifact, а не архивом подробных
отчётов. Иначе он станет тяжёлым и менее полезным для выбора следующего шага.

Подтверждения:
P1 diff выглядел относительно крупным для диагностического вывода; P5 backlog
update тоже может быть объёмным.

Следующее действие:
Наблюдать. При следующем backlog update просить Codex писать компактный result
+ decision log, без переноса полного анализа.
