# Artifact Review

## visual_concept.md

Purpose: зафиксировать, что должна означать будущая иллюстрация.

Не дублирует prompt и не дублирует artist brief. Это смысловой документ.

Информации достаточно для редакционного решения. Поля полезные: main meaning, viewer takeaway, tone, metaphor, risks.

Лишнее: `Notes for future illustration brief` может стать мусорным полем, если туда складывать ранние artist instructions. Его надо держать как вопросы и constraints, не как черновик brief.

## illustration_brief.md

Purpose: перевести смысл в задание художнику.

Отличие от `visual_concept.md` сформулировано хорошо:

- concept: что означает иллюстрация;
- brief: что должен нарисовать художник, чтобы передать смысл.

Риск дублирования высокий: большинство полей повторяют concept. Это оправдано только если brief реально добавляет "required elements", forbidden distortions и короткие пояснения художнику.

Не хватает одного практического поля: delivery context. Например: статья, обложка, inline illustration, hero image, карточка. Это не композиция и не стиль, но влияет на пригодность задания.

## image_prompt.md

Purpose: исполнительский prompt на основе `illustration_brief.md`.

Структура нормальная: source brief, prompt, required elements, forbidden distortions, text-on-image, format/aspect ratio, style only if given, unresolved questions.

Главный риск: поле `prompt` может поглотить смысловой контроль. Если prompt получается длинным и образным, он легко добавит новый смысл.

Хорошо, что style constraints ограничены "only if given". Это снижает риск превращения ветки в дизайн-систему.

## Overall

Три артефакта не лишние концептуально.

На практике их стоит держать короткими. Если каждый превращается в длинный документ, система станет тяжелее, чем задача.
