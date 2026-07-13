# Отчёт о реализации Outcome-First Deliverable Selection

Дата: 2026-07-13
Task: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`

## Результат

AI Editorial Office теперь различает решение о том, **что произвести**, и
решение о том, **как это произвести**.

Рабочий порядок зафиксирован так:

```text
запрос и реальная цель
-> requested / recommended / selected deliverable
-> pipeline, mode или task-local mini-contract
-> production
-> independent review
```

Изменение расширяет существующую архитектуру. Новые постоянные роли, pipelines,
lifecycle stages, gates, scores и обязательные отдельные артефакты не созданы.

## Архитектурные решения

### 1. Canonical owner — Task Need Recognition

`kb/task_need_recognition.md` уже отвечает за advisory interpretation запроса до
Chief Editor routing. Поэтому в него добавлена `Outcome-First Deliverable
Recommendation`, а не новый Deliverable/Format Agent или отдельный framework.

Capability оценивает:

- реальную проблему и нужный outcome;
- действие, решение, понимание, сравнение, approval или implementation, которые
  должен поддержать результат;
- audience, channel, use context и достаточную глубину;
- минимальный достаточный artifact shape;
- reader/user effort, maintenance burden и лишний production bulk;
- степень свободы выбора формата.

Список возможных deliverables остаётся иллюстративным и не становится закрытой
taxonomy или списком pipelines.

### 2. Четыре раздельных значения

Task object и orchestration теперь различают:

- `requested_deliverable` — что запросил или обозначил пользователь;
- `deliverable_format_authority` — `explicit`, `delegated`, `inferred` или
  `unknown`;
- `recommended_deliverable` — advisory recommendation smallest sufficient
  artifact;
- `selected_deliverable` — решение Chief Editor, которое используется в
  production и предшествует pipeline selection.

Для старых task packs оставлена совместимость: одно поле `deliverable` можно
читать как requested+selected только для очевидной explicit-format задачи без
материальной альтернативы.

### 3. Explicit user intent не переопределяется молча

Добавлены четыре Chief Editor decisions:

- `respect_requested`;
- `select_recommended`;
- `ask_before_change`;
- `constrain_with_explanation`.

Explicit requested deliverable сохраняется по умолчанию. Альтернативу можно
предложить, но нельзя незаметно подменить. Если формат не способен выполнить
заявленный outcome, задача возвращается в существующий Preflight Gate через
`ask` или `constrain`, а не получает скрытый override.

### 4. Pipeline следует за selected deliverable

В `orchestration_plan_template.md` блок `outcome-first deliverable decision`
физически расположен перед `selected pipeline`. Article, Social, UX Writing и
Research Pipeline теперь опираются на уже выбранный deliverable или его
evidence need, а не на первое упоминание формата в запросе.

Если подходящего специального pipeline нет, Chief Editor использует существующий
mode или ограниченный task-local mini-contract. Новый pipeline только ради memo,
roadmap, presentation или matrix не создаётся.

### 5. Ответственность существующих ролей

- Intake Agent фиксирует requested deliverable, format authority и advisory
  recommendation, но не выбирает результат.
- Chief Editor выбирает deliverable, затем pipeline и фиксирует решение в
  `orchestration_plan.md`.
- Writer Agent и UX Writer производят selected deliverable и останавливаются при
  конфликте request/recommendation/selection/pipeline.
- Review Agent проверяет outcome fit, sufficiency, explicit-intent preservation,
  объяснение alternative/override и правильный порядок pipeline selection.
- Final Editor сохраняет reviewed selected deliverable и не решает конфликт
  форматов во время cleanup.

## Изменённые канонические компоненты

### Entry и governance

- `/AGENTS.md`
- `ai-editorial-office/AGENTS.md`

### Canonical knowledge owners

- `kb/task_need_recognition.md`
- `kb/task_object_model.md`
- `kb/capability_registry.md`
- `kb/shared_lifecycle_kernel.md`

### Существующие роли

- `agents/intake_agent.md`
- `agents/chief_editor.md`
- `agents/writer_agent.md`
- `agents/ux_writer.md`
- `agents/review_agent.md`
- `agents/final_editor.md`

### Существующие pipelines

- `pipelines/article_pipeline.md`
- `pipelines/social_pipeline.md`
- `pipelines/ux_writing_pipeline.md`
- `pipelines/research_pipeline.md`
- `pipelines/review_pipeline.md`

### Existing templates

- `templates/artifacts/orchestration_plan_template.md`
- `templates/artifacts/task_manifest_template.md`
- `templates/tasks/article_task_template.md`
- `templates/tasks/social_task_template.md`
- `templates/tasks/ux_writing_task_template.md`
- `templates/tasks/review_task_template.md`

### Tests и documentation

- `tests/outcome_first_deliverable_selection_smoke_test.md`
- `tests/test_outcome_first_deliverable_selection.sh`
- `tests/README.md`

### Exact-copy memory package

Синхронизированы 12 существующих `/about` mirrors: `AGENTS.md`, шесть role
specs и пять pipeline specs. Новые `/about`-файлы не создавались; размер пакета
остался 20 файлов.

## Synthetic test coverage

Десять кейсов проверяют:

1. explicit article остаётся article;
2. delegated learning request получает learning roadmap;
3. bare `explain` не может быть заменён checklist только ради краткости;
4. presentation use context поддерживает presentation;
5. compare outcome поддерживает comparison matrix;
6. management persuasion поддерживает decision memo;
7. requirements request различает BRD и specification ambiguity;
8. explicit presentation не заменяется memo;
9. невозможный format/outcome mismatch возвращается в preflight;
10. trivial typo repair остаётся compact и не получает лишний governance.

Executable static regression дополнительно проверяет canonical contract,
физический порядок блоков orchestration template, наличие ровно десяти кейсов и
отсутствие запрещённых Deliverable/Format Agent или pipeline files.

## Проверки

На текущем implementation snapshot успешно выполнены:

- `git diff --check`;
- `sh ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh`;
- `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` — 14/14;
- `sh ai-editorial-office/tests/test_task_pack_generator.sh` — 13/13;
- `sh ai-editorial-office/scripts/check_about_memory_package.sh` — 20/20;
- lifecycle validation текущего task pack — 0 blockers, 0 warnings.

## Ограничения доказательства

Synthetic tests доказывают coverage контракта и отсутствие архитектурного
drift, но не доказывают real-world improvement. Практический эффект следует
проверять на будущих задачах с explicit, delegated и ambiguous format authority
и сопоставлять выбранный artifact с фактическим пользовательским outcome.

## Review state

Independent Review Agent: `approved` after one bounded repair, `OFD-001`.
Bounded re-review confirmed the finding resolved; blocking findings: none.
