# Поведенческий аудит редакции

## Intake

### сильные стороны

- В зрелых задачах intake фиксирует не только тему, но и reader state,
  operational goal, source boundary, constraints и success criteria.
- Система научилась явно сохранять неизвестное. В `TASK-0002` аудитория,
  канал, реальные примеры и approval остаются unknown, а не додумываются.
- В operational tasks intake хорошо описывает читательскую задачу:
  `TASK-0004`, `TASK-0004B`, `TASK-0005`, `TASK-0006`, `TASK-0021`.
- Source boundary в поздних задачах стал сильнее: `TASK-0022` прямо запрещает
  добавлять новые обещания и факты; `TASK-0023` ограничивает работу исходной
  расшифровкой.

### слабые стороны

- В части корпуса intake отсутствует как доказуемый этап: `TASK-0011` -
  `TASK-0019`, части `TASK-0010`, `TASK-0012` - `TASK-0015`.
- В некоторых задачах контекст использования остаётся inferred:
  например, `TASK-0023` предполагает внутреннюю/корпоративную аудиторию, но не
  имеет явного подтверждения канала.
- Успех часто описан через качество текста, а не через проверяемое действие
  читателя: что он должен понять, сделать, выбрать или не перепутать.
- Human approval и publication/delivery approval часто выясняются поздно:
  final decision хорошо это проговаривает, но intake не всегда заранее
  фиксирует approval owner.

### повторяющиеся паттерны

- Если задача короткая и кажется очевидной, система склонна сокращать intake
  сильнее, чем нужно.
- При source-contained задачах система иногда уверенно пропускает research,
  что обычно верно, но требует особенно ясного source boundary.
- Недостающие live links, access paths и имена ответственных часто остаются
  человеческим follow-up, а не blocking input.

### риски

- Неподтверждённая аудитория может привести к правильному тексту для
  неправильного канала.
- Неявный approval owner может превратить editorial-ready материал в
  practically-not-ready material.
- Слабый intake делает review зависимым от уже суженной постановки.

## Chief Editor

### сильные стороны

- Обычно верно выбирает research для AI/claims-sensitive тем (`TASK-0001`,
  `TASK-0002`) и пропускает external research для source-contained работ.
- Хорошо отделяет social, article/reference, compact rewrite и visual branch
  задачи.
- В поздних задачах стал лучше выбирать compact depth без потери review.
- Накапливает системные выводы: после проблем с relevance, structure и
  redundancy появляются maintenance-изменения.

### слабые стороны

- Ранний full lifecycle был слишком тяжёлым для повторного применения:
  `TASK-0001` полезен как validation run, но не как обычный шаблон.
- Иногда отдельные review-summary, qa-checklist, finalization-notes и handoffs
  создавались по инерции.
- В transition tasks есть сильные редакционные результаты без полного
  governance evidence.
- Chief Editor не всегда явно фиксирует, какие пользовательские данные были
  подтверждены, какие выведены, а какие неизвестны. Это как раз стало причиной
  появления Normalized Brief Contract.

### повторяющиеся паттерны

- При высоком смысловом риске Chief Editor усиливает трассировку.
- При коротких задачах позже появляется хороший compact режим.
- При operational materials Chief Editor постепенно смещает внимание от стиля
  к reader path и section roles.

### риски

- Если Chief Editor ошибся на входе, Review Agent может проверять уже
  неправильно суженную задачу.
- Без artifact budget Chief Editor может платить контекстом и временем за
  артефакты, которые downstream не использует.

## Research

### сильные стороны

- В claims-sensitive задачах research создаёт реальную защиту: facts,
  claims_table, claims-used, do-not-say и blocked claims.
- Research не превращается в writing в зрелых задачах.
- Система умеет честно ограничивать: generic examples only, no vendor claims,
  no numeric productivity claims.

### слабые стороны

- В прямых задачах невозможно доказать, что исследовательская логика была
  выполнена, даже если результат выглядит осмысленным.
- Иногда research-образная аналитика (`TASK-0010`, `TASK-0014`, `TASK-0015`)
  существует как сильный документ, но без review и lifecycle.

### повторяющиеся паттерны

- Research нужен, когда материал содержит причинные утверждения, claims about
  AI/workflows, security, policy, product behavior или публичные обобщения.
- Research не нужен, когда пользователь дал замкнутый источник фактов и задача
  не требует новых утверждений.

### риски

- Пропуск research безопасен только при явном source boundary.
- Без claims_table Review Agent хуже ловит маленькие, но важные обобщения.

## Writing

### сильные стороны

- Writer Agent хорошо переводит абстрактные исходники в рабочие ситуации.
- Система научилась избегать corporate excitement, HR tone, fake warmth и
  маркетинговой бодрости.
- В operational tasks Writer Agent всё чаще строит путь читателя: сначала
  выбрать роль/действие, потом читать детали.
- Writer notes полезны: они объясняют omissions, assumptions, claims control и
  review focus.

### слабые стороны

- При неполном контексте текст становится generic. Иногда это безопасно, но
  снижает практическую силу.
- Есть склонность к «чуть более редакторскому» варианту, который может звучать
  лучше, но быть менее честным. Это видно в связке `TASK-0003` -> `TASK-0003B`.
- Мелкая unsupported certainty проскакивает в drafting: `TASK-0002` ловит
  "самый частый сбой" и общий productivity/speed implication.
- При сложных operational topics текст может начать объяснять систему вместо
  того, чтобы помогать действовать.

### повторяющиеся дефекты

- answer delay;
- abstraction before action;
- duplicated process explanation;
- too generic examples;
- synthetic warmth;
- HR/corporate framing;
- over-explanation;
- unsupported frequency/productivity/impact claims;
- weak next step when links or access paths are placeholders.

### риски

- Хороший стиль может скрыть слабую задачу.
- Конкретика без подтверждения может создать ложную операционную инструкцию.
- Без early structure planning writer вынужден чинить архитектуру уже внутри
  prose draft.

## Review

### сильные стороны

- Хорошо ловит неподдержанные claims, overconfident wording и hidden factual
  claims.
- Хорошо проверяет operational usefulness: sequence, action ownership,
  selective reading, role routes, reference usability.
- Хорошо держит tone discipline: no fake warmth, no HR motivation, no
  corporate sludge.
- Хорошо отделяет editorial readiness от publication approval.

### слабые стороны

- Review чаще проверяет draft against brief, чем raw user goal against actual
  outcome.
- Если brief неполный или слишком уверенно inferred, review может пройти
  неправильно понятую задачу.
- В compact literary/adaptation tasks review может становиться похожим на
  self-check, если не фиксирует независимость и проверенный scope достаточно
  жёстко.
- Review редко прямо оценивает, был ли выбран правильный process depth.

### повторяющиеся паттерны

- На уровне текста review ловит больше, чем на уровне task-understanding.
- Лучшие review-артефакты имеют checked scope, independence basis, findings,
  residual risks и next action.
- Отдельные QA checklist полезны для operational tasks, но не всегда нужны как
  отдельный файл.

### риски

- Review может стать "проходным approval", если нет исходного success test.
- Review может не заметить, что материал полезен только после human action
  (вставить ссылки, подтвердить доступ, выбрать канал).

## Finalization

### сильные стороны

- Final decision стабильно фиксирует границы: не publication approval, не legal
  approval, не stakeholder approval.
- В mature tasks finalization не добавляет новых фактов.
- Final decisions помогают закрывать lifecycle и не выдавать редакционный
  результат за опубликованный.

### слабые стороны

- Иногда именно final decision впервые ясно говорит о human approval и
  practical send-out conditions.
- В ранних/прямых задачах final decision отсутствует, поэтому готовность
  результата менее доказуема.

### повторяющиеся паттерны

- "Editorially ready after link insertion / human approval" встречается часто.
- Finalization хорошо сохраняет source and review boundaries.

### риски

- Пользователь может воспринять finalized как "можно отправлять сейчас", хотя
  в файле есть placeholders или approvals outside system.
- Если finalization compact, review must remain precise enough to carry all
  unresolved risks.
