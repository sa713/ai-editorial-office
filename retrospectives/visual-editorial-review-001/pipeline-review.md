# Pipeline Review

## Chain

Текущая цепочка:

`text` -> `visual_illustration_brief` -> `visual_concept.md` -> visual concept review -> `illustration_brief.md` -> Artist Agent -> `image_prompt.md` -> meaning preservation review -> image.

## Logic

Логика в целом правильная: сначала смысл, потом задание, потом исполнение, потом контроль drift. Это защищает от типичной ошибки "сразу написать промпт по тексту".

## Extra Stages

Для простых задач цепочка может быть избыточной:

- короткий внутренний анонс;
- простая иллюстрация к новости;
- маленькая карточка для соцсети;
- материал, где визуальный смысл очевиден.

В таких случаях `visual_concept.md` и `illustration_brief.md` могут слиться по содержанию, даже если формально разные.

## Missing Stages

Не хватает не нового pipeline, а entry rule:

- когда визуальная ветка включается;
- кто решает, что нужен `visual_concept.md`;
- когда достаточно `illustration_brief.md` без отдельного полного concept;
- какой статус считается approved для `visual_concept.md` и `illustration_brief.md`.

## Cycles

Опасный цикл один: review находит drift в `image_prompt.md`, Artist Agent чинит prompt, потом снова возникает drift из-за prompt-переформулировки. Это нормальный цикл, если он короткий и bounded.

Плохой цикл: review начинает менять `visual_concept.md`, чтобы оправдать хороший prompt. В Step 7 это запрещено, и это правильно.

## Duplication

Дублирование есть между:

- main meaning;
- viewer takeaway;
- emotional tone;
- visual metaphor;
- required elements;
- distortion risks.

Оно допустимо, если артефакты реально выполняют разные функции. Если в практике `illustration_brief.md` просто копирует `visual_concept.md`, слой нужно сжимать.
