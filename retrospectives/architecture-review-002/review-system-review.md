# Review system review

## Стал ли review слишком тяжёлым

Местами да. Проблема не в обязательности проверки, а в объёме вокруг неё.

Тяжесть создают:

- отдельный `review.md`;
- отдельный `qa-checklist.md`;
- отдельный `review-summary.md`;
- иногда `reviewer-notes.md`;
- handoff после review;
- повтор проверки в `final_decision.md`.

Для high-governance это оправдано. Для low-risk это часто больше, чем нужно.

## Где review реально повышает качество

- Ловит неподтверждённые факты, обещания, продуктовые утверждения.
- Проверяет, что текст отвечает brief, а не просто звучит лучше.
- Защищает от essay-mode, fake usefulness, context inflation.
- Сохраняет channel roles в многоартефактных задачах.
- Отлично сработал в diagnostic tasks: не дал v1-подходу в `TASK-0010` достроить сырой концепт в готовый продукт.
- Защищает последние обновления: `diagnostic_analysis`, `author_concept_diagnosis`, Artificial Concept Completion, Premature Solution Substitution.

## Где review создаёт лишние циклы

- Полная повторная проверка после локальной правки.
- Review всех каналов после изменения одного канала.
- Требование отдельного summary без следующего потребителя.
- Проверка template compliance вместо качества результата.
- Финальное governance-повторение всех review checks.

## Как сохранить usefulness-first review

- Review должен начинаться с reader task и useful outcome.
- Проверять структуру по режиму текста, а не по вкусу.
- Разделять blocking issue и non-blocking note.
- Не требовать "полноты", если текст уже выполняет задачу.
- Не превращать diagnostic analysis в consulting или solution design.
- Не ослаблять сильные выводы там, где материал их поддерживает.

## Как не потерять bounded revision

В `changes_requested` всегда указывать:

- blocking issue;
- owner of repair;
- repair scope;
- re-review scope;
- what must not be reopened.

Если проблема локальная, revision должна быть локальной. Полный rewrite только при сломанном reader outcome, evidence gap, instruction conflict или неверном формате.

## Как избежать review bureaucracy

- Для low-risk: один `review.md`.
- Для standard: отдельный checklist только если есть сложные проверки.
- Для high-governance: полный review сохраняется.
- Review не переписывает текст, а возвращает owner и scope.
- Review output должен быть короче объекта проверки, если задача простая.
- Review не должен проверять все правила проекта, если риск и объект узкие.

## Что не делать

- Не делать review optional.
- Не заменять review финальным решением Chief Editor.
- Не давать writer self-approval.
- Не вводить scoring.
- Не создавать reviewer dashboard.
- Не превращать review в формальную сертификацию каждого поля шаблона.

