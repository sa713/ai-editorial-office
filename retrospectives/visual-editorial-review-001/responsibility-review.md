# Responsibility Review

## visual_illustration_brief mode

Отвечает за поведение редакции: как читать текст как источник визуального смысла.

Граница выдержана: mode не рисует, не пишет prompt, не делает style guidance.

## visual_concept.md

Отвечает за ownership смысла.

Это правильный центр ветки. Если смысл спорный, спор должен решаться здесь, а не в prompt.

## Review

Review разделён на два уровня:

- review самого `visual_concept.md`;
- review сохранности смысла в chain.

Это логично. Риск в том, что review guidance находится в общем review-system, но текущий Review Agent spec не знает явно, что он может проверять visual artifacts. Это может потребовать ручного назначения.

## illustration_brief.md

Отвечает за перевод смысла в задание художнику.

Роль нормальная, но граница тонкая: brief уже спрашивает "what should the illustrator draw", но запрещает composition/style/technique. Это реалистично, если brief говорит о смысловых объектах и запретах, а не о художественном решении.

## Artist Agent

Отвечает за execution.

Граница прописана хорошо: не анализировать исходный текст, не спорить с concept, не менять brief, не добавлять meaning.

Главный конфликт: `AGENTS.md` всё ещё говорит, что активные production roles только MVP-роли. Artist Agent существует как spec, но не легализован как active role.

## Mixed Responsibilities

Смешение пока умеренное.

Самое опасное место: Artist Agent может "execution details" принять за право выбирать новый образ. Это ограничено текстом роли, но на практике надо проверять.
