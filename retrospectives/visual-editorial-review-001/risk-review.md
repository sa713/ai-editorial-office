# Risk Review

## High Risk

Artist Agent не легализован в `AGENTS.md` как active production role.

Impact: ветка может конфликтовать с системным уставом и pipelines, которые разрешают только MVP-роли.

## High Risk

Prompt drift.

Impact: `image_prompt.md` может добавить драму, стиль, конфликт, персонажей или символы, которых не было в meaning artifacts.

## Medium Risk

Process weight.

Impact: для простых задач пользователи будут обходить систему вручную, потому что full chain кажется слишком длинной.

## Medium Risk

Concept/brief duplication.

Impact: два артефакта могут стать копиями друг друга. Тогда review будет проверять форму, а не реальную передачу смысла.

## Medium Risk

No post-image semantic check.

Impact: ветка может сохранить смысл до prompt, но потерять его на картинке.

## Low Risk

Art-direction drift в текущих текстах.

Impact: правила многократно запрещают style/composition/color/taste. Пока риск контролируемый.

## Low Risk

Comic/presentation drift.

Impact: явно запрещено почти на каждом уровне. Риск низкий, если пользователь не просит такие форматы отдельно.
