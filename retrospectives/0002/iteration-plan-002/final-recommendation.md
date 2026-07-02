# Final recommendation

## Recommendation

Принять iteration 002 как bounded plan по reader-state awareness, но внедрять его минимально.

Главный вывод TASK-0009: AI-редакции не нужен новый behavioral framework. Ей нужен короткий практический навык — замечать, когда текст делает первый шаг читателя тяжелее, чем нужно.

## What to implement now

Реализовать пять малых изменений:

1. **Reader-state intake questions**
   Добавить optional questions для задач с onboarding, participation или change communication.

2. **Low-pressure entry guidance**
   Закрепить правило: если можно честно начать с просмотра, не требовать commitment в первом шаге.

3. **Pressure audit in review**
   Научить review ловить fake obligation, unsupported urgency, social pressure и слишком ранний commitment.

4. **Failure patterns from TASK-0009**
   Добавить короткий набор practical anti-patterns для diagnosis and bounded repair.

5. **Bounded refinement shape**
   Для reader-state issues использовать точечную правку: source of friction, minimal repair, unchanged constraints, re-review target.

## What to defer

Отложить:

- rewrite core documents;
- массовое обновление всех templates;
- новые agent specs;
- новый behavioral pipeline;
- scoring/eval;
- dashboards;
- adoption metrics;
- emotional taxonomy;
- full migration старых задач;
- автоматические проверки.

Эти вещи не нужны для проверки полезности iteration 002.

## What not to do

Не делать:

- new agents;
- behavioral UX role;
- persuasion strategy;
- engagement optimization;
- social proof without sources;
- fake momentum;
- voluntary framing for mandatory actions;
- дружелюбный тон вместо ясного governance;
- reader-state analysis for every artifact.

## Recommended implementation order

1. Зафиксировать reader-state definitions and boundaries в одном canonical месте.
2. Добавить optional intake/orchestration questions.
3. Добавить pressure audit как optional review block.
4. Добавить failure patterns как repair aid.
5. Протестировать на 2-3 новых задачах похожего типа.
6. После теста решить, какие template updates действительно нужны.

## Decision

Iteration 002 должна сделать редакционное ядро чуть внимательнее к первому шагу читателя, но не шире как система.

Правильный масштаб:

- меньше лишнего давления;
- яснее безопасный вход;
- честнее уровень обязательности;
- конкретнее review;
- меньше полного rewrite там, где достаточно bounded refinement.

Этого достаточно для следующего шага. Более крупные behavioral concepts должны ждать повторных реальных failures, а не появляться заранее.
