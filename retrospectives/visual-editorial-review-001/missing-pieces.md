# Missing Pieces

## Activation Rule

Не хватает правила включения визуальной ветки.

Сейчас не ясно:

- кто решает, что тексту нужна иллюстрация;
- когда достаточно обычного текстового pipeline;
- когда нужен full visual chain;
- когда можно compact path.

## Role Legitimacy

`artist_agent.md` есть, но `AGENTS.md` всё ещё говорит, что активные production roles только MVP-роли. Это самый важный gap.

Пока это не исправлено, Artist Agent может считаться неактивной ролью.

## Task Scaffold

Нет task template для visual illustration tasks.

Без него пользователи будут вручную собирать:

- `visual_concept.md`;
- review;
- `illustration_brief.md`;
- `image_prompt.md`.

Это повышает шанс пропусков.

## Status And Handoff

Нет явных lifecycle statuses для visual branch.

Минимально нужны понятные переходы:

- concept drafting;
- concept review;
- brief drafting;
- prompt execution;
- meaning preservation review.

Это не обязательно новый pipeline, но нужен task-local orchestration pattern.

## Post-Image Meaning Check

Сейчас намеренно нет проверки изображения.

Для production это риск: картинка может исказить смысл даже при корректном prompt.

Нужен не art review, а ограниченный future check: "готовое изображение сохраняет смысл prompt/brief или нет". Сейчас это отсутствует.
