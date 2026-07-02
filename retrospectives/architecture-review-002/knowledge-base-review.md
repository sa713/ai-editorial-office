# Knowledge base review

## editorial_knowledge

Сильные части:

- `10_operational_rules.md` даёт рабочие редакционные эвристики.
- `20_editorial_modes.md` помогает выбирать структуру по задаче читателя.
- `30_compact_editorial_brief.md` хорошо держит короткий мост между запросом и письмом.
- `40_editorial_review_system.md` делает проверку полезности, а не вкуса.
- `50_editorial_failure_patterns.md` практично называет типовые провалы.
- Новые блоки про `diagnostic_analysis`, `author_concept_diagnosis`, Artificial Concept Completion, Premature Solution Substitution и Defensive Diagnostic Drift нужны и не должны откатываться.

Слабые части:

- `02_editorial_intent.md` и `03_usefulness_review.md` почти пустые.
- `01_principles.md` содержит сильные новые принципы, но рядом есть старые пустые заголовки.
- Режимов уже много. Добавлять новые рискованно.
- Failure patterns полезны, но файл растёт и может стать словарём на каждый случай.

## kb

Сильные части:

- `task_statuses.md` чётко владеет статусной моделью.
- `forbidden_patterns.md` хорошо работает как защита от AI-текста.
- `ux_writing_guidelines.md` полезен для продуктового текста.
- `glossary.md` помогает общему языку.

Слабые части:

- `good_examples.md` и `bad_examples.md` пустые.
- `editorial_policy.md` частично повторяет `AGENTS.md` и root `editorial_knowledge`.
- `/kb` и root `editorial_knowledge` имеют разные уровни зрелости. Нужно явно помнить: `/kb` — операционная поддержка, root `editorial_knowledge` — редакционная доктрина.

## Пересечения

- Artifact minimalism: `AGENTS.md`, `editorial_policy.md`, agent specs, pipelines, templates.
- Review-gate: `AGENTS.md`, `editorial_policy.md`, `review_agent.md`, pipelines.
- Forbidden patterns: `/kb/forbidden_patterns.md` и `editorial_knowledge/50_editorial_failure_patterns.md`.
- Usefulness review: `03_usefulness_review.md`, `30_compact_editorial_brief.md`, `40_editorial_review_system.md`.
- Diagnostic boundaries: `01_principles.md`, `10_operational_rules.md`, `20_editorial_modes.md`, `40_editorial_review_system.md`, `50_editorial_failure_patterns.md`.

## Устаревшие или слабые правила

- Пустые scaffold-файлы лучше не читать как активные источники.
- `project-state.md` всё ещё говорит, что current focus — materialization of pipelines. По факту система уже ушла дальше.
- Старые task artifacts до нормализации не должны быть образцом.
- Полные template checklists не должны становиться обязательными для каждого случая.

## Слишком похожие понятия

- Diagnostic analysis и author concept diagnosis различаются полезно, но требуют короткой подсказки выбора.
- Artificial Concept Completion и Premature Solution Substitution близки; первое про зрелость идеи, второе про подмену авторской работы готовым решением.
- Usefulness, reader outcome, reader task, reader state могут распухать, если каждый термин требовать в каждом brief.
- Review target и quality bar иногда пересекаются.

## Риск doctrine growth

Риск высокий, но управляемый.

Не добавлять новый термин, если он:

- не меняет структуру текста;
- не меняет проверку;
- не предотвращает повторяющийся реальный провал;
- может быть выражен существующим failure pattern.

Лучший путь развития базы знаний — больше коротких case notes, меньше новых правил.

