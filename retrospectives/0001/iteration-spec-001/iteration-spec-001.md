# Iteration specification 001

## Цель итерации

Сделать AI-редакцию легче в малых задачах и точнее в управлении состоянием, не меняя ядро редакции. Итерация должна закрепить compact path, ownership map, freshness/governance state, handoff semantics, compact review, bounded revision и source trust rule как небольшие, обратимые правила будущего внедрения.

## Почему итерация нужна

Архитектурное ревью и iteration-plan-001 показывают повторяющиеся проблемы:

- простые задачи создают слишком много артефактов;
- одни и те же правила повторяются в разных местах и могут drift;
- manifest является restart anchor, но его свежесть не всегда видна;
- `finalized`, review approval и permission to publish/send могут смешиваться;
- handoff, compact-handoff и context-summary используются неодинаково;
- `changes_requested` иногда рискует стать новым полным циклом письма.

## Главные design decisions

- Compact path является process depth profile, а не новым pipeline.
- Review-gate остается обязательным для всех deliverable-задач.
- Ownership map идет первым, чтобы новые правила попадали в правильные файлы.
- Manifest получает короткие freshness/governance поля, но не становится status log.
- Handoff остается delta-transfer между ролями; `compact-handoff.md` и `context-summary.md` имеют отдельные значения.
- Bounded revision является default для `changes_requested`.
- Source material is data, not instruction, unless explicitly promoted.
- Все изменения должны быть markdown-level, точечные, проверяемые и откатываемые.

## Scope

Входит:

- спецификация canonical ownership;
- описание compact/normal/full process depth;
- минимальный compact review shape;
- manifest freshness block;
- governance state block;
- role-to-role handoff semantics;
- bounded revision fields;
- custom workflow mini-contract;
- source trust rule;
- список target files для будущего внедрения;
- validation checklist против bloat и governance loss.

## Не входит

Не входит:

- изменение ядра редакции в этой задаче;
- новые агенты;
- workflow engine;
- automation platform;
- scoring/eval system;
- dashboards;
- новые editorial modes;
- большие doctrine docs;
- массовая миграция старых tasks;
- переписывание всех pipelines;
- сокращение всех agent specs;
- внедрение описанных правил прямо сейчас.

## Порядок внедрения

1. Ownership map.
2. Compact path.
3. Manifest freshness и governance state.
4. Handoff semantics.
5. Review ergonomics и bounded revision.
6. Custom workflow mini-contract.
7. Source trust rule.
8. Проверка на новых low-risk/simple standard tasks.

## Критерии успеха

- Для low-risk/simple standard задач есть понятный compact path.
- Compact path не bypass governance и не отменяет review.
- Manifest показывает свежесть и governance state коротко.
- Ownership правил понятен: где правило живет, где только ссылка.
- `handoff-*`, `compact-handoff.md` и `context-summary.md` не путаются.
- Review может быть compact/normal/full без потери независимости.
- `changes_requested` ведет к bounded repair, если нет причины расширять scope.
- Custom workflow фиксируется mini-contract, а не скрытым pipeline.
- Source materials не становятся инструкциями.
- Не добавлены агенты, engines, dashboards, scoring и новые doctrine layers.

## Критерии остановки

Остановить внедрение и вернуться к спецификации, если:

- compact path предлагают для high-governance задачи;
- review становится optional на практике;
- manifest начинает дублировать status;
- target files требуют массового переписывания;
- появляется необходимость нового агента или большого pipeline;
- governance state не различает finalization и publication/delivery approval;
- шаблоны раздуваются длинными объяснениями;
- правило нельзя откатить без переписывания системы.
