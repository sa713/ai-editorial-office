# Comparison With TASK-0004

Compared:

- `tasks/TASK-0004/final.md` requested in the task; local file was not present, so the available previous final artifact `tasks/TASK-0004/final(1).md` was used
- `tasks/TASK-0004B/final.md`

Comparison focus: system behavior and instruction quality, not style.

## Summary

`TASK-0004B` shows the effect of the structure-before-writing update. The new result is more deliberately routed: it starts with reader intent, separates action paths, and moves repeated operational details into reference sections.

## Repetition

Improved.

`TASK-0004` repeats parts of the task lifecycle in `Как проходит задача`, `Если вы Автор задачи` and `Если вы Исполнитель задачи`. `TASK-0004B` reduces that by using role paths and shared reference sections for fields, statuses and disputes.

## Selective Reading

Improved.

`TASK-0004` is readable linearly but asks the reader to move through the document structure to find their role. `TASK-0004B` adds an early "Выберите свой путь" table, so a reader can jump directly to Автор, Исполнитель, Идея or reference topics.

## Author Path

Clearer.

`TASK-0004` has a useful Author section, but it sits after a full process description. `TASK-0004B` makes the Author path self-contained: create card, wait for moderation, choose executor, agree result, close or return for revision.

## Executor Path

Clearer.

Both versions state that Исполнитель comments in `To Do` and waits for the Author. `TASK-0004B` makes the risk more visible: a comment is not an automatic assignment.

## Idea Path

Slightly clearer.

Both versions preserve the main distinction: idea has no deadline and goes to Moderators. `TASK-0004B` keeps the idea path shorter and avoids re-explaining the task form except for differences that matter.

## Path To Action

Shorter.

`TASK-0004B` puts action routes near the top. A reader does not need to read the full lifecycle before acting.

## Important Constraints

Preserved.

Both versions preserve:

- pilot on АС Taska;
- Moderators check cards;
- Author chooses one Исполнитель;
- subtask creation is forbidden;
- idea deadline is not filled;
- disputes go to curators.

`TASK-0004B` removes unresolved source term `Инициатива`, which avoids turning a source placeholder into a formal definition.

## Excess Architecture

Not introduced.

The planning artifact is more architectural than in the earlier run, but the final instruction itself does not expose that architecture heavily. It uses one routing table and two reference tables, which support action rather than adding process overhead.

## Real Usefulness

Improved.

The new version is more useful as an operational reference: a reader can choose a path, perform the next action, then consult fields, statuses or escalation guidance without rereading the whole instruction.
