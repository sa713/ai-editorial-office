TASK — Product Intent Review: Step 3

Статус

Authorized

Основание

Step 0, Step 1 и Step 2 завершены и финализированы.

Уже реализовано:

* каноническая спецификация Product Intent Review;
* запись в Capability Registry;
* multi-signal распознавание;
* negative-evidence routing;
* advisory recommendation;
* task-local mode decision:
    * not_needed;
    * limited;
    * full;
* conditional loading канонического owner;
* restart semantics;
* сохранение compact path;
* разделение recommendation и Chief Editor decision.

На текущем этапе Product Intent Review ещё не выполняет полный анализ и не участвует в независимом review как отдельная проверяемая dimension.

⸻

Цель Step 3

Интегрировать Product Intent Review в существующий Editorial Decision Frame и Review Pipeline так, чтобы при режимах limited и full:

1. продуктовый вывод формировался до глубокой редакционной работы;
2. Chief Editor использовал его для решения о production permission;
3. Writer Agent и UX Writer получали чёткие границы допустимой работы;
4. Review Agent независимо проверял качество Product Intent Review;
5. product finding не смешивался с operational verdict;
6. слабый продуктовый замысел нельзя было скрыть качественной редакционной полировкой.

Step 3 не должен создавать новый pipeline, review-gate, task status, review outcome, роль или обязательный standalone artifact.

⸻

Целевое поведение

При not_needed

Система продолжает обычный маршрут.

Product Intent Review:

* не выполняется;
* не появляется в review;
* не создаёт дополнительных артефактов;
* не усложняет production contract.

При limited

Система должна:

* проверить только назначенный product-intent focus;
* сформировать один ограниченный product finding;
* зафиксировать product consequence;
* разрешить, ограничить или приостановить соответствующую часть production;
* передать Review Agent минимально необходимый scope проверки.

При full

Система должна:

* выполнить доступную семичленную модель;
* провести четыре проверки;
* выделить один главный продуктовый разрыв;
* сформировать альтернативы в допустимых границах;
* предложить minimum hypothesis validation, если это требуется;
* сформировать product finding;
* определить следующий decision;
* определить, разрешена ли глубокая редакционная работа.

⸻

Основной архитектурный принцип

Product Intent Review является аналитическим основанием для редакционного решения.

Она не принимает решение о продукте автоматически.

Последовательность:

Product Intent Review analysis
  -> product finding
  -> Chief Editor consequence
  -> Editorial Decision Frame
  -> production permission or constraint
  -> material production
  -> existing independent review

Product finding и operational verdict должны оставаться разными сущностями.

⸻

Область изменений

Проверить и при необходимости изменить:

* agents/chief_editor.md;
* agents/research_agent.md;
* agents/writer_agent.md;
* agents/ux_writer.md;
* agents/review_agent.md;
* agents/final_editor.md — только для сохранения одобренного вывода;
* pipelines/research_pipeline.md;
* pipelines/review_pipeline.md;
* kb/editorial_planning_framework.md;
* kb/editorial_challenge_lens.md или фактический canonical owner;
* templates/artifacts/orchestration_plan_template.md;
* review artifact template;
* research или analytical artifact templates, если без этого невозможно выразить Product Intent Review;
* связанные tests и fixtures.

Не изменять файлы только потому, что они перечислены. Каждое изменение должно иметь наблюдаемую необходимость.

⸻

1. Выполнение Product Intent Review

Analytical owner

Product Intent Review должна выполняться существующим аналитическим маршрутом.

Предпочтительно:

* Research Agent собирает и структурирует evidence, если research назначен;
* Chief Editor либо текущий analytical owner формирует decision-ready product finding;
* Writer Agent и UX Writer не выполняют Product Intent Review;
* Review Agent не выполняет первичный анализ.

Не создавать отдельного Product Analyst.

limited

Анализ ограничивается назначенным focus.

Примеры:

* только механизм воздействия;
* только подтверждённость проблемы;
* только соответствие формата;
* только жизнеспособность;
* только один разрыв между аудиторией и решением.

Нельзя механически заполнять всю семичленную модель.

full

Выполняются:

* доступная семичленная модель;
* четыре product checks;
* evidence/assumption/unknown separation;
* один главный разрыв;
* ограниченные alternatives;
* minimum validation, когда требуется;
* product finding;
* следующий decision.

⸻

2. Product finding

Product finding — это предметный вывод Product Intent Review.

Он должен отвечать на вопросы:

* насколько обоснован замысел;
* какой главный продуктовый разрыв обнаружен;
* что допустимо делать дальше;
* какое решение требуется от владельца;
* какие ограничения должны быть сохранены.

Примеры product finding:

* замысел обоснован, но механизм изменения поведения не определён;
* проблема значима, но выбранный формат не подтверждён;
* продукт перегружен и должен быть уменьшен;
* требуется короткий пилот до полной реализации;
* материал можно редактировать, но production продукта преждевременен;
* задача может быть решена меньшим вмешательством;
* создание продукта в текущем виде нецелесообразно;
* предоставленных данных недостаточно для решения о создании.

Product finding не является закрытым enum.

⸻

3. Product consequence

Chief Editor должен переводить product finding в редакционное consequence.

Минимальные типы consequence:

Proceed

Замысел достаточно обоснован для продолжения редакционной работы.

Proceed with constraints

Редакционная работа разрешена только в обозначенных границах.

Примеры:

* не расширять продукт;
* не обещать неподтверждённый эффект;
* не менять утверждённый формат;
* сохранить uncertainty;
* подготовить только пилотный материал.

Validate before production

Полная редакционная или продуктовая реализация не разрешена до проверки гипотезы.

Допустима работа над:

* прототипом;
* пилотным сценарием;
* исследовательским материалом;
* decision memo;
* тестовым артефактом.

Reroute

Нужен другой класс решения или иной deliverable.

Stop / no-build recommendation

Редакция рекомендует не создавать продукт в текущем виде.

Фактическое решение остаётся у владельца продукта.

Эти consequence не должны становиться:

* task statuses;
* review outcomes;
* lifecycle stages;
* pipeline names.

Использовать существующую Editorial Decision Frame и routing semantics.

⸻

4. Editorial Decision Frame

При limited или full Editorial Decision Frame должен содержать компактный product-intent block.

Минимально:

* mode;
* product finding;
* главный разрыв;
* evidence boundary;
* production consequence;
* owner decision required;
* reconsideration trigger.

Не помещать в Editorial Decision Frame:

* полную семичленную модель;
* длинный research narrative;
* полный список альтернатив;
* подробную minimum validation design;
* редакционные замечания.

Editorial Decision Frame остаётся коротким управленческим решением.

⸻

5. Product-first ordering

При limited или full нельзя переходить к глубокой редакционной доработке, пока не сформирован достаточный product finding.

Глубокой редакционной работой считается:

* полная переработка структуры;
* написание большого материала;
* создание серии коммуникаций;
* проектирование полного курса;
* UX-copy для неутверждённого поведения;
* полировка решения, целесообразность которого не проверена.

Допустима предварительная работа, необходимая для анализа:

* извлечение структуры;
* краткое резюме;
* evidence mapping;
* восстановление логики;
* подготовка пилотного варианта;
* создание минимального проверочного артефакта.

Product-first ordering не является новой стадией lifecycle.

⸻

6. Research Agent

При активной Product Intent Review Research Agent должен уметь:

* восстановить доступные элементы семичленной модели;
* маркировать facts, assumptions, hypotheses и unknowns;
* искать evidence, релевантное назначенному mode и focus;
* искать disconfirming evidence;
* проверять причинные основания;
* выявлять отсутствующие данные;
* не проектировать продукт вместо владельца;
* не принимать product decision;
* не превращать research в универсальное исследование рынка.

Для limited research должен быть ограниченным.

Для full depth определяется ставками, evidence state и обратимостью решения.

⸻

7. Writer Agent и UX Writer

Writer Agent и UX Writer должны получать только утверждённые границы.

Они не должны:

* исправлять слабый product intent сильным текстом;
* добавлять неподтверждённые обещания;
* расширять продукт;
* менять product behavior;
* скрывать uncertainty;
* превращать пилот в полноценный запуск;
* самостоятельно устранять product gap.

Они должны:

* следовать production consequence;
* сохранять product finding;
* соблюдать constraints;
* сигнализировать Chief Editor, если production обнаруживает новый материальный product gap.

Такой сигнал должен вызывать reroute, а не самостоятельное перепроектирование.

⸻

8. Review Agent

Review Agent должен независимо проверять Product Intent Review внутри существующего review-gate.

Обязательные проверки активации

* был ли mode выбран корректно;
* учтено ли negative evidence;
* не активирована ли линза по ключевому слову;
* не требовалась ли линза там, где она была пропущена;
* соответствует ли глубина limited или full реальному риску.

Обязательные проверки анализа

При limited:

* проверен ли назначенный focus;
* не разросся ли анализ в полный аудит;
* подтверждён ли главный вывод;
* корректно ли обозначены unknowns.

При full:

* восстановлена ли доступная семичленная модель;
* проведены ли четыре проверки;
* отделено ли подтверждённое от предположений;
* выбран ли один главный разрыв;
* обоснованы ли alternatives;
* корректна ли minimum validation;
* не подменён ли product owner.

Обязательные проверки результата

* product finding следует из evidence;
* production consequence соответствует finding;
* Editorial Decision Frame не искажает анализ;
* Writer Agent не скрыл product gap;
* качественный текст не используется как доказательство качества продукта;
* uncertainty сохранена;
* следующий decision понятен;
* фактическое решение оставлено владельцу.

⸻

9. Operational verdict

Review Agent продолжает использовать только существующие outcomes:

* approved;
* changes_requested;
* blocked.

Примеры:

Approved

Product Intent Review корректно показал, что продукт не следует запускать.

Сам продуктовый вывод отрицательный, но качество анализа одобрено.

Changes requested

Основной product finding правдоподобен, но:

* недостаточно evidence;
* не выбран главный разрыв;
* consequence не следует из вывода;
* minimum validation слишком слабая;
* не сохранена uncertainty.

Blocked

Например:

* анализ выдумывает потребность;
* продуктовый вывод представлен как бизнес-решение;
* редакционная production скрыла критический разрыв;
* высокий риск требует evidence, которого нет;
* нарушена независимость review.

Не создавать Product Intent Review verdicts в Review Pipeline.

⸻

10. Editorial Challenge Lens

Product Intent Review dimension должна быть встроена в существующую challenge-логику.

Review должен задавать вопросы:

* Какие основания делают product finding действительным?
* Какие данные могли бы его опровергнуть?
* Не спутана ли проблема с предлагаемым решением?
* Не предполагается ли эффект без механизма?
* Не является ли выбранный формат привычным, но необоснованным?
* Не существует ли меньшего вмешательства?
* Не стала ли редакционная полировка заменой продуктовой проверки?
* Не приняла ли Редакция решение вместо владельца?

Не создавать отдельную Product Challenge Lens, если существующий owner может содержать условную dimension без размывания.

⸻

11. Final Editor

Final Editor не выполняет новый Product Intent Review.

Он должен:

* сохранить approved product finding;
* сохранить uncertainty;
* сохранить production consequence;
* сохранить owner decision boundary;
* не смягчать отрицательный продуктовый вывод;
* не добавлять новые альтернативы;
* не превращать рекомендацию в факт;
* не скрывать no-build recommendation ради более позитивного финала.

Изменять final_editor.md только если существующего preservation contract недостаточно.

⸻

12. Артефакты

Не создавать обязательный product_intent_review.md в каждой task-папке.

Product Intent Review может быть представлен в:

* research.md;
* аналитическом отчёте;
* decision memo;
* отдельном Product Intent Review report, если он выбран как deliverable;
* orchestration plan в компактной форме;
* review.md как independent challenge.

Отдельный task-local artifact допустим, если:

* анализ является самостоятельным deliverable;
* глубина full требует traceability;
* материала слишком много для существующего research artifact;
* решение владельца зависит от отдельного отчёта.

Не делать его default.

⸻

13. Minimum hypothesis validation

На Step 3 необходимо реализовать аналитическое формирование minimum validation, но не отдельный исследовательский pipeline.

Minimum validation должна включать:

* конкретную гипотезу;
* целевую аудиторию или контекст;
* минимальное вмешательство;
* наблюдаемое действие или сигнал;
* условие продолжения;
* условие пересмотра;
* ограничения вывода.

Review Agent должен проверять:

* проверяется ли реальная гипотеза;
* меньше ли проверка полной реализации;
* нет ли выдуманных метрик;
* нет ли ложной статистической строгости;
* не объявляется ли один кейс доказательством;
* соответствует ли тест главному разрыву.

⸻

14. Альтернативы

Product Intent Review должна уметь обозначать альтернативный класс решения.

Допустимые типы:

* меньшее вмешательство;
* пилот;
* изменение процесса;
* изменение интерфейса;
* исследование;
* прототип;
* тренажёр;
* коммуникация;
* отказ от нового продукта;
* использование существующего инструмента.

Альтернативы должны быть:

* релевантными главному разрыву;
* ограниченными по количеству;
* явно маркированными как recommendations;
* не превращёнными в полный новый product design.

⸻

15. Reroute triggers

Нужно определить условия возврата к Chief Editor.

Примеры:

* production выявила новый product gap;
* изменился формат решения;
* появились новые данные о проблеме;
* владелец изменил аудиторию или цель;
* mechanism оказался неподтверждённым;
* minimum validation дала отрицательный или неоднозначный результат;
* product finding и requested deliverable больше не совместимы;
* Writer Agent вынужден менять product behavior для выполнения задачи.

Reroute не является новым task status.

⸻

16. Требования к review artifact

Review artifact при активной Product Intent Review должен позволять проследить:

* mode;
* scope;
* product finding;
* evidence boundary;
* главный разрыв;
* production consequence;
* review challenge;
* operational verdict;
* owner decision boundary.

Не требовать полного повторения исходного анализа.

Review должен проверять, а не пересказывать.

⸻

17. Тестовый набор

Обязательно добавить или расширить исполняемые tests.

17.1. Negative product finding, approved analysis

Вход:

* новая концепция;
* Product Intent Review рекомендует не запускать.

Ожидание:

* Review outcome approved;
* product finding остаётся отрицательным;
* operational verdict не подменяется product verdict.

17.2. Product finding скрыт полировкой

Вход:

* analysis выявил неподтверждённый механизм;
* Writer Agent подготовил убедительный материал с обещанием эффекта.

Ожидание:

* review не approved;
* обнаружено нарушение production boundary.

17.3. Limited mode overreach

Вход:

* focus только mechanism;
* analysis перепроектировал весь продукт.

Ожидание:

* changes requested.

17.4. Full mode incomplete model

Вход:

* отсутствует часть модели;
* неизвестное скрыто уверенным выводом.

Ожидание:

* changes requested или blocked в зависимости от риска.

17.5. Product owner substitution

Вход:

* Chief Editor объявил бизнес-цель и запуск утверждёнными.

Ожидание:

* review finding о нарушении authority boundary.

17.6. Weak minimum validation

Вход:

* один разговор с сотрудником объявлен доказательством эффективности курса.

Ожидание:

* review не approved.

17.7. Correct minimum validation

Вход:

* проверяется одна конкретная гипотеза;
* задан наблюдаемый сигнал;
* ограничения вывода обозначены.

Ожидание:

* анализ может быть approved.

17.8. No-build vs blocked

Проверить различие:

* корректный no-build recommendation → review может быть approved;
* некачественный анализ → changes requested или blocked.

17.9. Not-needed regression

Простая редактура не получает Product Intent Review review dimension.

17.10. Reroute

Production обнаруживает новый материальный product gap.

Ожидание:

* возврат к Chief Editor;
* Writer Agent не перепроектирует продукт сам.

⸻

18. Regression protections

Проверить сохранность:

* compact path;
* Task Need Recognition;
* conditional loading;
* task restart;
* deliverable selection;
* Professional Analysis;
* reader-centered quality;
* existing review outcomes;
* single review-gate;
* role boundaries;
* finalization semantics;
* lifecycle validation.

⸻

Запрещённые изменения на Step 3

Не создавать:

* новую роль;
* Product Reviewer;
* Product Strategist;
* новый pipeline;
* product-intent review pipeline;
* новый lifecycle stage;
* новый review-gate;
* новый task status;
* новый review outcome;
* обязательный standalone artifact;
* универсальный Product Intent Review шаблон для всех задач;
* автоматическое product decision;
* новую evidence taxonomy;
* отдельный research lifecycle;
* новый project-state release status.

Не принимать Professional Analysis как released capability.

Не начинать Step 4.

⸻

Обязательные task artifacts

Создать task-папку Step 3.

Минимально подготовить:

* brief.md;
* baseline-report.md;
* decision-integration-design.md;
* review-integration-design.md;
* implementation-report.md;
* change-summary.md;
* review.md;
* final_decision.md;
* final.md.

Допускается адаптация к действующему lifecycle contract.

⸻

Проверки

Выполнить:

* lifecycle validation;
* lifecycle validator smoke suite;
* git diff --check;
* Python и shell syntax checks для изменённых scripts;
* Product Intent Review routing tests;
* новые Product Intent Review decision/review tests;
* Task Need Recognition regressions;
* task-pack generator regressions;
* Professional Analysis smoke tests;
* Editorial Challenge regressions;
* reader-centered-quality regressions;
* outcome-first deliverable selection regressions;
* review outcome regressions;
* restart checks;
* compact-path checks;
* canonical-link checks;
* /about parity, если затронута mapped surface;
* forbidden-surface diff;
* scoped diff.

Отдельно подтвердить:

* один review-gate сохранён;
* operational verdicts не изменены;
* task statuses не изменены;
* новая роль не создана;
* новый pipeline не создан;
* Final Editor не выполняет новый анализ;
* product finding не стал task status или review outcome;
* Professional Analysis остаётся open release candidate;
* Step 4 не начат.

⸻

Критерии приёмки Step 3

Step 3 принимается, если:

1. Product Intent Review выполняется при limited и full.
2. limited остаётся сфокусированным.
3. full использует доступную семичленную модель.
4. Выполняются четыре product checks.
5. Evidence, assumptions и unknowns различаются.
6. Выделяется один главный продуктовый разрыв.
7. Формируется product finding.
8. Product finding отделён от operational verdict.
9. Chief Editor формирует production consequence.
10. Editorial Decision Frame сохраняет компактный product-intent block.
11. Product-first ordering соблюдается.
12. Writer Agent не исправляет слабый продукт сильным текстом.
13. UX Writer не меняет product behavior.
14. Research Agent не становится product owner.
15. Review Agent независимо проверяет Product Intent Review.
16. Review использует только существующие outcomes.
17. Корректный no-build finding может получить approved.
18. Некорректный анализ получает changes_requested или blocked.
19. Minimum validation имеет корректные границы.
20. Альтернативы не превращаются в полный redesign.
21. Reroute triggers работают.
22. Final Editor только сохраняет одобренный вывод.
23. not_needed не получает лишнюю review dimension.
24. Один review-gate сохранён.
25. Новые роли, pipelines, stages, statuses и outcomes не созданы.
26. Обязательный standalone artifact не создан.
27. Compact path не деградировал.
28. Professional Analysis сохранила текущий статус.
29. Regression tests проходят.
30. Step 4 не начат.

⸻

Первый запрос Кодексу

Выполни только Step 3 — интеграцию Product Intent Review в Editorial Decision Frame, production boundaries и существующий Review Pipeline.

При режимах limited и full реализуй:

* Product Intent Review analysis;
* product finding;
* один главный продуктовый разрыв;
* production consequence;
* product-first ordering;
* independent review dimension;
* minimum hypothesis validation;
* reroute triggers.

Сохрани различие между product finding и operational verdict.

Review Agent должен использовать только существующие outcomes:

* approved;
* changes_requested;
* blocked.

Корректный вывод «продукт не следует создавать» может и должен получать approved, если анализ качественный.

Не создавай новую роль, pipeline, lifecycle stage, review-gate, task status, review outcome или обязательный standalone artifact.

Не принимай Professional Analysis как released capability.

Не начинай Step 4.

После реализации проведи независимый review и верни полный task pack, canonical diff и результаты regression checks.
