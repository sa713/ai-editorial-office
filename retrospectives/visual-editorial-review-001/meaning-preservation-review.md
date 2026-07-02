# Meaning Preservation Review

## Main Loss Points

Смысл может потеряться в трёх местах:

1. Text -> `visual_concept.md`: редакция берёт тему вместо главной мысли.
2. `visual_concept.md` -> `illustration_brief.md`: смысл превращается в набор объектов.
3. `illustration_brief.md` -> `image_prompt.md`: prompt усиливает красивую второстепенную идею.

## New Meaning Points

Новый смысл может появиться здесь:

- visual metaphor слишком самостоятельная;
- required elements добавлены ради картинки, не ради смысла;
- Artist Agent выбирает execution detail, который меняет тон;
- prompt добавляет конфликт, драму, персонажа, символ или оценку, которых не было.

## Typical Errors

- "Текст про сотрудничество" превращается в "борьбу с препятствием".
- Сложная мысль превращается в одну банальную метафору.
- Серьёзный материал становится ироничным.
- Внутренний анонс получает слишком героический образ.
- Prompt добавляет людей, эмоции или конфликт без основания.

## Review Strength

Step 7 хорошо закрывает semantic continuity. Важное правило: если drift появился позже, не менять `visual_concept.md`, а чинить `illustration_brief.md` или `image_prompt.md`.

## Remaining Weakness

Нет проверки после фактического изображения. Это было намеренно исключено. Но в реальной работе изображение может нарушить смысл даже при хорошем prompt. Сейчас система это не ловит.

Это не значит, что нужен art review. Но нужен хотя бы future lightweight "image vs prompt meaning check", если ветка пойдёт в production.
