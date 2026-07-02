# Simplification Opportunities

## Keep As Is

- `visual_illustration_brief` mode.
- `visual_concept.md` for non-trivial materials.
- Meaning preservation review for prompt-producing work.

## Simplify In Practice

Для low-risk задач можно объединять concept и brief в один короткий document shape, если:

- главный смысл очевиден;
- нет сложной метафоры;
- нет высокого риска искажения;
- нет внешнего художника;
- prompt нужен быстро.

Формально это может быть один `illustration_brief.md` с compact concept block.

## Questionable Weight

`visual concept review` и `meaning preservation review` как два отдельных review stages могут быть тяжелыми.

В пилоте стоит проверить, можно ли:

- review concept делать только для medium/high-risk иллюстраций;
- meaning preservation review делать только когда есть `image_prompt.md`;
- для простых задач использовать один review pass.

## Avoid Simplifying

Не стоит убирать `visual_concept.md` полностью. Без него Artist Agent и prompt быстро станут владельцами смысла.

Не стоит разрешать prompt-first поведение. Это уничтожит главную ценность ветки.

## Practical Test

Проверить на 10 задачах:

- сколько минут занимает каждый слой;
- сколько раз brief реально отличается от concept;
- сколько drift-находок ловит review;
- сколько задач можно было решить compact path без потери качества.
