This is a synthetic/sanitized end-to-end case. It is not a real task folder and does not contain real course source files, confidential methodology, internal training materials, participant data, client data, or restricted content.

# Review

- reviewer role: review_agent
- reviewed artifact: draft.md
- source artifact checked: source_summary.md
- reviewer independence: independent from writer_agent drafting step

outcome: approved

## Checks

- Понятность задачи: approved. Draft ясно объясняет, какой курс дорабатывается, кто нужен и какие результаты ожидаются.
- Управленческий смысл: approved. Текст пригоден для внутреннего канала или биржи задач: есть контекст, направления работы, ожидаемый output и способ отклика.
- Корректное использование `source_summary.md`: approved. Draft ссылается на вложенное описание курса и не переносит закрытые детали.
- Нет выдуманных модулей или содержания курса: approved. Draft не называет модули и не добавляет структуру сверх source boundary.
- Не звучит как “напишите весь курс с нуля”: approved. Текст прямо говорит, что задача — доработать уже описанную структуру.
- Варианты практической части понятны: approved. Указаны два допустимых формата: задачи по модулям или один сквозной кейс.
- Compact-evidence rationale: approved. Есть task-local supplied source boundary и sanitized summary.
- Source/provenance boundary: approved. Оригинальный source file не коммитится, не переносится в `kb/`, `learn/` или `tasks/`.
- Review gate: approved. Review выполняется до `final.md`, outcome записан явно.

## Findings

No blocking findings.

## Residual Risk

Основной риск — выдумать содержание курса или закрытые методологические детали. Draft контролирует этот риск: просит работать по вложенному описанию и не приводит модульную структуру внутри sanitized case.

## Next Action

Proceed to finalization.
