# Architecture risks

## Risk 1: Artifact bloat despite artifact minimalism

**Описание**

Система декларирует минимализм, но реальные задачи создают много файлов: TASK-0001 имеет 27 файлов, TASK-0002 — 25, TASK-0003 — 22, TASK-0008 — 18. Для сложных задач это нормально, но для стандартных задач может стать привычкой.

**Где проявляется**

- `ai-editorial-office/tasks/TASK-*`;
- article/review/social/UX pipelines;
- обязательные outputs в agent specs;
- templates with many fields.

**Возможные последствия**

- рост cognitive load;
- агент тратит усилия на lifecycle paperwork вместо редакционной работы;
- reviewer читает слишком много служебных документов;
- low-risk задачи становятся непропорционально дорогими;
- система начинает нарушать собственный принцип "artifacts are operational tools".

**Критичность**

High для масштабирования и ежедневного использования.

**Рекомендации**

- Ввести compact path для low-risk и simple standard задач.
- Разрешить объединять `review-summary.md` и handoff, если это не ухудшает route clarity.
- Зафиксировать "minimum viable task package" для каждого risk mode.
- В review добавить вопрос: какие artifacts можно было не создавать без потери качества?

## Risk 2: Rule duplication and policy drift

**Описание**

Одни и те же правила повторяются в `AGENTS.md`, `project-state.md`, agent specs, pipelines, templates и editorial knowledge. Пока они согласованы, но при правках могут разойтись.

**Где проявляется**

- role boundaries;
- status transitions;
- artifact minimalism;
- review requirements;
- risk mode behavior;
- finalization/governance separation.

**Возможные последствия**

- разные агенты читают разные версии правила;
- старый pipeline начинает противоречить обновленному `AGENTS.md`;
- reviewer блокирует задачу по устаревшему требованию;
- будущие изменения становятся дорогими.

**Критичность**

High.

**Рекомендации**

- Создать один canonical responsibility map для artifact/status/role rules.
- В остальных файлах оставлять короткие ссылки на canonical rule.
- Раз в несколько задач делать drift scan: AGENTS vs pipelines vs agent specs.

## Risk 3: Manifest freshness depends on discipline, not mechanism

**Описание**

`task-manifest.md` является restart anchor, но актуальность manifest поддерживается вручную. Система говорит "stale manifest blocks work", но нет механического способа проверить stale state.

**Где проявляется**

- stage transitions;
- handoff creation;
- review outcome changes;
- finalization status changes;
- custom workflows.

**Возможные последствия**

- агент восстанавливается из устаревшего next action packet;
- review читает не тот набор artifacts;
- status и manifest конфликтуют;
- после compaction система делает повторную или неверную работу.

**Критичность**

Medium-high.

**Рекомендации**

- Добавить lightweight freshness section: last updated by role, stage, related artifact changes.
- Не строить автоматический engine; достаточно checklist-проверки в начале роли.
- Для finalized задач фиксировать immutable final state summary.

## Risk 4: Review independence is declarative

**Описание**

Система запрещает reviewer быть тем же role instance, который писал материал. Но role instance не идентифицируется явно.

**Где проявляется**

- `review_agent.md`;
- `review.md`;
- handoff files;
- tasks with compact custom flow.

**Возможные последствия**

- review independence нельзя доказать;
- при single-user local use reviewer может фактически быть тем же model session без явной self-check boundary;
- governance выглядит сильнее, чем его evidence.

**Критичность**

Medium.

**Рекомендации**

- Добавить в review artifacts поле `Reviewed independently from writing: yes/no/unknown` и `Basis`.
- Для high-governance задач фиксировать writer role instance и reviewer role instance хотя бы текстово.
- Не вводить сложную identity system до реальной необходимости.

## Risk 5: Custom workflows can become hidden pipelines

**Описание**

TASK-0008 использует custom editorial diagnosis flow. Это правильно для задачи, но если custom flows будут повторяться без формализации, они станут скрытыми пайплайнами.

**Где проявляется**

- TASK-0008;
- future diagnostic, advisory, audit, retrospective tasks;
- tasks outside article/social/UX/review categories.

**Возможные последствия**

- Chief Editor каждый раз изобретает orchestration заново;
- artifact scope зависит от интуиции;
- review criteria непредсказуемы;
- сложнее обучать систему на повторяемых кейсах.

**Критичность**

Medium.

**Рекомендации**

- Добавить "custom workflow contract" как компактное правило, а не новый большой pipeline.
- Зафиксировать минимальные поля: task type, why no pipeline fits, stages, artifacts, review target, stop conditions.

## Risk 6: Context compression exists conceptually but not operationally

**Описание**

Система говорит о context-summary и compact handoff, но нет явного compaction protocol для long tasks: что именно сохранять, что удалять, как rehydrate.

**Где проявляется**

- long tasks с 20+ artifacts;
- repeated review/revision loops;
- tasks after context loss.

**Возможные последствия**

- потеря решений;
- повторное чтение лишних файлов;
- prompt drift;
- review по старой версии artifacts;
- handoff начинает раздуваться, чтобы компенсировать слабый manifest.

**Критичность**

Medium.

**Рекомендации**

- Описать compact-handoff vs context-summary vs task-manifest boundaries.
- Добавить compaction trigger: after major stage, after review, after finalization, after context fragmentation.
- Не делать summary для каждой задачи автоматически.

## Risk 7: Editorial doctrine inflation

**Описание**

Редакционная теория сильна, но может расти быстрее, чем проверяется практикой. Уже есть scaffold files с заголовками и большие documents с перекрывающимися правилами.

**Где проявляется**

- `editorial_knowledge`;
- `90_system_review.md`;
- future additions of modes, dimensions, patterns.

**Возможные последствия**

- агенты начинают классифицировать вместо писать;
- review превращается в checklist;
- brief становится формой;
- новые правила повторяют старые другими словами;
- полезность уступает compliance theater.

**Критичность**

Medium-high.

**Рекомендации**

- Добавлять новое правило только после repeated failure on real tasks.
- Поддерживать small golden set of editorial principles.
- Заполнять или удалить пустые scaffold files.
- Вместо новых правил добавлять worked examples.

## Risk 8: Pipeline complexity may exceed single-user needs

**Описание**

Пайплайны production-grade, но система single-user. Есть риск, что процесс начнет имитировать enterprise workflow без соответствующей пользы.

**Где проявляется**

- multiple role handoffs;
- mandatory templates;
- full lifecycle statuses;
- governance language.

**Возможные последствия**

- медленное выполнение простых задач;
- пользователь перестает использовать систему для малых работ;
- агенты создают artifacts "потому что pipeline";
- editorial judgment заменяется процедурой.

**Критичность**

Medium.

**Рекомендации**

- Сохранить governance для high-risk.
- Для low-risk разрешить один compact production packet плюс review.
- Ввести правило: process depth must be justified by risk or downstream consumption.

## Risk 9: Instruction leakage and prompt injection handling is underdeveloped

**Описание**

Система хорошо говорит о authority hierarchy, но почти не описывает, как обращаться с untrusted source content, emails, PDFs, decks и user-provided drafts, которые могут содержать инструкции.

**Где проявляется**

- research over web/docs;
- user-provided source drafts;
- email and messenger materials;
- `.pptx`, `.docx`, PDFs in `learn` and tasks.

**Возможные последствия**

- source material может стать instruction accidentally;
- агент может выполнить embedded request из документа;
- reviewer может считать source rhetoric authoritative.

**Критичность**

Medium.

**Рекомендации**

- Добавить trust labels для source materials: authoritative task instruction vs material under analysis.
- В research/review artifacts явно отделять source content from system instruction.
- Для high-governance задач фиксировать "untrusted content treated as data".

## Risk 10: Lack of evals and regression checks

**Описание**

Система имеет хорошие правила, но нет набора проверочных кейсов, который доказывает, что правила работают.

**Где проявляется**

- new pipeline changes;
- new editorial knowledge updates;
- repeated tasks TASK-0003/TASK-0003B, TASK-0004/TASK-0004B;
- review and finalization quality.

**Возможные последствия**

- улучшения нельзя измерить;
- repeated failures становятся новыми prompt instructions, а не evals;
- regression после правок незаметен.

**Критичность**

Medium.

**Рекомендации**

- Сделать 5-7 regression cases на базе уже выполненных задач.
- Для каждого: input, expected failure caught, expected artifact path, acceptable output traits.
- Не строить full automated eval harness сейчас.
