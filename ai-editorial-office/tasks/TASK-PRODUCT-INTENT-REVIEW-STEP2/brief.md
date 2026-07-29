TASK — Product Intent Review: Step 2

Статус

Authorized

Основание

Step 0 и Step 1 завершены и финализированы.

Приняты следующие решения:

* Product Intent Review является условно активируемой специализированной линзой внутри семейства Professional Analysis.
* Полный канонический контракт принадлежит kb/product_intent_review.md.
* Новая роль, pipeline, lifecycle stage, review-gate, task status и review outcome не создаются.
* Professional Analysis остаётся open release candidate.
* Исторический Problem Hypothesis остаётся отдельным непринятым proposal.
* Step 1 зафиксировал спецификацию, но не реализовал маршрутизацию и исполняемое поведение.

⸻

Цель Step 2

Научить AI Editorial Office распознавать задачи, в которых Product Intent Review может быть полезна, и фиксировать task-local решение о глубине проверки:

* not_needed;
* limited;
* full.

На этом шаге необходимо встроить сигналы, режим и последствия режима в существующие Task Need Recognition, task object и orchestration contracts.

Step 2 не должен реализовывать полный Product Intent Review analysis, независимый product-intent review или финальный формат отчёта.

⸻

Целевое поведение

После Step 2 система должна уметь:

1. Обнаружить наблюдаемые сигналы продуктового замысла.
2. Не активировать линзу по одному ключевому слову.
3. Сохранить negative evidence.
4. Рекомендовать глубину Product Intent Review.
5. Передать recommendation Chief Editor.
6. Позволить Chief Editor принять task-local mode decision.
7. Зафиксировать mode и его основание в существующем task state.
8. Не создавать обязательный расширенный бриф.
9. Не усложнять простые редакционные задачи.
10. Не выполнять сам Product Intent Review analysis на этапе intake.

⸻

Основной архитектурный принцип

Task Need Recognition:

* распознаёт сигналы;
* формирует advisory recommendation;
* сохраняет negative evidence;
* не активирует Product Intent Review самостоятельно.

Chief Editor:

* принимает mode decision;
* определяет глубину;
* определяет необходимость research;
* определяет consequence для production route.

Capability:

* не активирует сама себя;
* не создаёт новый pipeline;
* не создаёт новый task status.

⸻

Обязательная последовательность

Input
  -> Task Need Recognition signals
  -> advisory Product Intent Review recommendation
  -> Chief Editor mode decision
  -> task-local state
  -> existing routing and planning

На Step 2 не требуется выполнять модель из семи элементов и четыре проверки.

⸻

Область изменений

Необходимо проверить и при необходимости изменить:

* kb/task_need_recognition.md;
* kb/task_object_model.md;
* agents/intake_agent.md;
* agents/chief_editor.md;
* templates/artifacts/orchestration_plan_template.md;
* templates/artifacts/task_manifest_template.md;
* task-pack generator — только если без этого новый канонический owner нельзя условно подключить;
* связанные tests и fixtures.

Дополнительные файлы разрешены только при доказанной необходимости.

⸻

1. Product Intent Review signals

Task Need Recognition должен уметь фиксировать несколько классов сигналов.

1.1. Новый объект или вмешательство

Примеры:

* новая обучающая активность;
* новый сервис;
* новая программа;
* новый рабочий процесс;
* новое мероприятие;
* новая коммуникационная механика;
* новый пользовательский сценарий;
* новый инструмент;
* существенное изменение существующего продукта.

Само наличие объекта не означает автоматическую активацию.

1.2. Требуемое изменение аудитории

Материальным сигналом является ожидание, что продукт должен изменить:

* поведение;
* решение;
* опыт;
* способность;
* состояние;
* привычку;
* результат деятельности пользователя.

1.3. Неутверждённый формат решения

Примеры:

* предлагаемый формат ещё обсуждается;
* владелец просит мнение о концепции;
* пользователь спрашивает, стоит ли делать продукт;
* требуется сравнить классы решений;
* неизвестно, является ли курс, портал, кампания или сервис правильной формой.

1.4. Причинная гипотеза

Сигнал возникает, если полезность материала зависит от предположения:

предложенное взаимодействие приведёт к требуемому изменению.

1.5. Неразделимость материала и замысла

Продуктовая проверка материальна, если нельзя содержательно оценить документ, не оценивая описываемое вмешательство.

⸻

2. Negative evidence

Task Need Recognition должен учитывать признаки, при которых Product Intent Review не требуется или должна оставаться ограниченной.

Примеры:

* пользователь явно просит только корректуру;
* концепция уже утверждена;
* формат продукта находится вне scope;
* работа касается локального текста;
* изменение product behavior запрещено;
* пользователь просит сохранить существующее решение;
* продуктовый анализ не повлияет на полезность результата;
* объект упомянут только как контекст;
* задача является переводом, сокращением или изменением тона.

Negative evidence должно иметь реальный вес.

Слово курс, продукт, сервис, кампания или мероприятие не должно перевешивать явное ограничение scope.

⸻

3. Advisory recommendation

Task Need Recognition должен возвращать рекомендацию:

* not_needed;
* limited;
* full.

Допустима и рекомендация uncertain, только если существующая архитектура уже поддерживает подобную форму неопределённости и она не создаёт скрытый четвёртый mode.

Предпочтительный вариант:

* recommendation остаётся одним из трёх modes;
* uncertainty описывается в rationale и confidence;
* Chief Editor может изменить recommendation.

⸻

4. Логика рекомендации

not_needed

Рекомендуется, если:

* задача локальная;
* продуктовая концепция утверждена;
* анализ замысла находится вне scope;
* material/product distinction не влияет на результат;
* negative evidence сильнее product-intent signals.

limited

Рекомендуется, если:

* есть один материальный продуктовый вопрос;
* полный анализ не нужен;
* продуктовая логика в основном задана;
* локальное противоречие может изменить редакционное решение;
* требуется проверить одно основание, механизм или соответствие.

full

Рекомендуется, если:

* пользователь принёс новую или неутверждённую концепцию;
* просит решить, стоит ли создавать продукт;
* несколько элементов замысла не определены;
* причинный механизм является существенной гипотезой;
* выбранный формат может быть неверным;
* решение требует сравнения с альтернативными классами вмешательства.

⸻

5. Multi-signal principle

Нельзя реализовывать активацию через:

* поиск одного слова;
* простой список типов документов;
* обязательную активацию для всех курсов, сервисов или кампаний;
* единственный boolean is_product;
* название deliverable;
* предположение, что большой документ требует полного анализа.

Рекомендация должна учитывать совокупность:

* intended outcome;
* work surface;
* decision state;
* scope;
* consequence;
* ambiguity;
* evidence state;
* negative evidence.

Использовать существующую модель Task Need Recognition, а не создавать параллельный классификатор.

⸻

6. Chief Editor mode decision

Chief Editor должен:

* получить advisory recommendation;
* принять окончательное task-local решение;
* при необходимости изменить recommendation;
* зафиксировать краткое основание;
* определить research depth;
* определить consequence для production.

Пример consequence:

not_needed

Продолжить обычный маршрут.

limited

Проверить конкретный product-intent вопрос до глубокой редакционной работы.

full

Не разрешать подробный production contract до получения bounded Product Intent Review finding.

На Step 2 допустимо зафиксировать consequence, но не реализовывать полный Product Intent Review output.

⸻

7. Task object model

Проверить, как минимально представить Product Intent Review state.

Предпочтительная семантика:

product_intent_review:
  mode: not_needed | limited | full
  basis: ...
  confidence: ...
  focus: ...
  production_consequence: ...

Это иллюстрация, а не обязательная схема.

Необходимо следовать существующей структуре task object model.

Обязательные требования:

* mode является task-local analytical depth;
* mode не является task status;
* recommendation и Chief Editor decision различимы, если это необходимо для traceability;
* rationale остаётся коротким;
* not_needed не должен создавать тяжёлый обязательный объект во всех артефактах;
* restart должен сохранять mode, если он материален;
* unknowns не заполняются автоматически.

⸻

8. Orchestration plan

При limited или full orchestration plan должен уметь сохранять:

* mode;
* activation basis;
* focus;
* required evidence depth;
* product-first consequence;
* reroute trigger.

При not_needed:

* блок может быть опущен в очевидных случаях;
* либо фиксируется короткое negative-evidence rationale, если задача потенциально неоднозначна.

Не выводить полную семичленную модель в orchestration plan.

⸻

9. Task manifest

Task manifest должен содержать только минимальные restart-critical данные.

Допустимо сохранить:

* active capability pointer;
* mode;
* canonical owner reference;
* task-local consequence.

Не хранить:

* полный продуктовый анализ;
* подробную модель;
* четыре проверки;
* alternatives;
* minimum validation.

Если существующая структура manifest уже позволяет восстановить состояние по orchestration plan, не добавлять новые поля без необходимости.

⸻

10. Intake Agent

Intake Agent должен:

* фиксировать наблюдаемые сигналы;
* сохранять negative evidence;
* не спрашивать универсальные семь вопросов;
* не требовать заполнения Product Intent Review brief;
* не выбирать окончательный mode;
* не выполнять продуктовый анализ;
* не предлагать продуктовые альтернативы;
* не становиться product owner.

Если материала достаточно, Intake должен передать его дальше без дополнительных вопросов.

⸻

11. Chief Editor

Chief Editor должен:

* принять mode decision;
* задать scope;
* определить, нужен ли Research Agent;
* определить, что блокирует production;
* не принимать бизнес-решение;
* не выполнять полный анализ вместо аналитического owner;
* сохранить compact path.

Необходимо чётко отличить:

* решение активировать capability;
* результат capability;
* решение разрешить производство;
* фактическое решение владельца продукта.

⸻

12. Conditional capability loading

Проверить task-pack generator.

Цель:

* kb/product_intent_review.md подключается при limited или full;
* не подключается по умолчанию в простые задачи;
* не загружается только из-за ключевого слова;
* может быть подключён Chief Editor даже вопреки первоначальному not_needed, если выявлен материальный разрыв;
* mode сохраняется при restart.

Не менять generator, если существующий механизм capability loading уже полностью решает задачу после registry update.

Любое изменение generator должно быть минимальным и сопровождаться shell tests.

⸻

13. Product-first ordering

На Step 2 необходимо реализовать только routing consequence:

При limited или full материальный product-intent вопрос должен быть разрешён до глубокой редакционной доработки.

Это не новая lifecycle stage.

Это условие планирования и production permission.

На Step 2 не требуется реализовывать:

* полный Product Intent Review report;
* четыре проверки;
* minimum validation;
* product verdict catalogue;
* независимый review dimension.

⸻

14. Поведение при неполных данных

Система должна:

* рекомендовать доступный mode;
* сохранять неизвестное;
* не требовать всех семи полей;
* определить, какой product-intent вопрос материален;
* при необходимости назначить ограниченный research;
* не выдумывать потребность или аудиторию;
* не блокировать задачу автоматически только из-за неполноты.

Пример:

Концепция утверждена, но механизм изменения поведения не определён.

Возможный mode: limited, focus — mechanism.

⸻

15. Regression protections

Обязательно защитить следующие сценарии.

15.1. Простая корректура

Вход:

Исправь ошибки в уведомлении о новом сервисе.

Ожидание:

* not_needed;
* обычный compact path;
* Product Intent Review owner не загружается.

15.2. Перевод

Вход:

Переведи описание обучающей программы на английский.

Ожидание:

* not_needed, если анализ концепции не запрошен;
* отсутствие продуктового аудита.

15.3. Утверждённая концепция

Вход:

Концепция курса утверждена. Сократи введение.

Ожидание:

* not_needed;
* explicit negative evidence имеет приоритет.

15.4. Новый курс

Вход:

Мы хотим создать курс для развития системного мышления. Оцени концепцию и скажи, стоит ли запускать.

Ожидание:

* recommendation full;
* Chief Editor mode full;
* capability loading;
* product-first consequence.

15.5. Один материальный вопрос

Вход:

Формат мероприятия утверждён, но непонятно, почему участники после него начнут применять практику.

Ожидание:

* limited;
* focus — mechanism;
* отсутствие полного обязательного аудита.

15.6. Keyword trap

Вход:

Исправь опечатку в слове «продукт».

Ожидание:

* not_needed.

15.7. Approved product material

Вход:

Подготовь текст баннера для уже утверждённой механики.

Ожидание:

* not_needed, если product logic не является предметом задачи.

15.8. Product decision

Вход:

Нужен ли нам новый внутренний портал или проблему лучше решить иначе?

Ожидание:

* full.

15.9. Неясный scope

Вход:

Посмотри описание новой активности и дай мнение.

Ожидание:

* вероятный full или limited на основе материала;
* отсутствие требования заполнить бриф;
* rationale по evidence.

15.10. Большой, но утверждённый документ

Ожидание:

* размер не активирует Product Intent Review сам по себе.

⸻

Обязательные изменения tests

Создать или обновить тесты так, чтобы они проверяли исполняемое routing behavior.

Минимально:

* расширить task_need_recognition_smoke_test.md;
* создать product_intent_review_routing_smoke_test.md либо эквивалентный canonical test;
* обновить task-pack generator tests, если generator изменён;
* проверить restart-state representation;
* проверить compact path;
* проверить keyword traps;
* проверить negative evidence;
* проверить limited;
* проверить full;
* проверить отсутствие новой стадии и статуса.

String-only tests недостаточны, если они проверяют лишь наличие слов в документации.

Тест должен проверять контракт поведения существующим для репозитория способом.

⸻

Запрещённые изменения на Step 2

Не реализовывать:

* полный Product Intent Review analysis;
* семичленную модель как обязательный runtime output;
* четыре проверки как review logic;
* minimum hypothesis validation;
* формат итогового Product Intent Review report;
* новые product findings;
* независимый Product Intent Review challenge;
* изменения Review Agent;
* изменения Final Editor;
* новые deliverables;
* новый pipeline;
* новый lifecycle stage;
* новый review-gate;
* новый task status;
* новый review outcome;
* новую роль;
* принятие Professional Analysis;
* обновление project-state до статуса «реализовано».

Не начинать Step 3.

⸻

Обязательные task artifacts

Создать task-папку Step 2.

Минимально подготовить:

* brief.md;
* baseline-report.md;
* routing-design.md;
* implementation-report.md;
* change-summary.md;
* review.md;
* final_decision.md;
* final.md.

Допускается адаптация имён под lifecycle contract репозитория.

⸻

Проверки

Выполнить:

* lifecycle validation;
* lifecycle validator smoke tests;
* git diff --check;
* Task Need Recognition smoke tests;
* Product Intent Review routing tests;
* task-pack generator shell tests, если затронут generator;
* restart-state tests, если существуют;
* capability registry checks;
* canonical link checks;
* compact-path regression;
* outcome-first deliverable selection regression;
* Professional Analysis smoke tests;
* forbidden-surface diff;
* scoped diff.

Отдельно подтвердить:

* новая роль не создана;
* новый pipeline не создан;
* новая stage не создана;
* новый task status не создан;
* новый review outcome не создан;
* Review Agent не изменён;
* Final Editor не изменён;
* полный Product Intent Review analysis не реализован.

⸻

Критерии приёмки Step 2

Step 2 принимается, если:

1. Task Need Recognition распознаёт product-intent signals.
2. Negative evidence влияет на recommendation.
3. Keyword-only activation исключена.
4. Поддерживаются рекомендации not_needed / limited / full.
5. Chief Editor принимает task-local mode decision.
6. Recommendation и decision не смешиваются с task status.
7. limited имеет ограниченный focus.
8. full задаёт product-first consequence.
9. Простая редактура сохраняет compact path.
10. Универсальный product brief не требуется.
11. Семь элементов не превращены в обязательные intake fields.
12. Mode сохраняется в task-local state.
13. Restart может восстановить материальный mode.
14. Capability owner условно подключается.
15. not_needed не создаёт лишние artifacts.
16. Intake Agent не выполняет продуктовый анализ.
17. Chief Editor не становится product owner.
18. Полный Product Intent Review analysis не реализован.
19. Новые роли, pipelines, stages, statuses, gates и outcomes не созданы.
20. Существующие routing и editorial сценарии не деградировали.
21. Тесты покрывают positive, negative и ambiguous cases.
22. Professional Analysis сохраняет текущий статус.
23. Step 3 не начат.

⸻

Первый запрос Кодексу

Выполни только Step 2 — интеграцию Product Intent Review в Task Need Recognition, task-local state и routing.

Используй утверждённый kb/product_intent_review.md как канонический owner.

Реализуй multi-signal advisory recommendation и task-local mode decision:

* not_needed;
* limited;
* full.

Сохрани Chief Editor как владельца решения об активации.

Не создавай новую роль, pipeline, lifecycle stage, review-gate, task status или review outcome.

Не реализуй полный Product Intent Review analysis, четыре проверки, minimum validation, итоговый формат и независимый review dimension.

Защити compact path, negative evidence и отсутствие keyword-only activation.

После реализации проведи независимый review и верни полный task pack, canonical diff и результаты regression checks.
