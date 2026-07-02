# Orchestration Plan

Task ID: `TASK-0005`

Owner: `chief_editor`

Selected pipeline: `article_pipeline`

Review required: yes

## Routing

1. Intake: normalize reader state, skepticism risks and source limits in `brief.md`.
2. Structure-before-writing planning: fix reading mode, section roles, hierarchy and dilution risks in this plan.
3. Writing: create `outline.md`, `draft.md`, `writer-notes.md`.
4. Review: check usefulness, onboarding clarity, reader trust, information priority, skepticism handling, signal dilution and explanation/detail balance.
5. Finalization: create `final.md` after approved review.
6. Governance: create `final_decision.md` and `compact-handoff.md`.

## Research Decision

Separate research stage is omitted.

Reason: task is based on supplied internal source material and user-provided context. No external factual claims, metrics, dates or policy details are required. Any mechanics in the text must stay at orientation level and avoid unsupported implementation details.

## Intake Findings

### Likely Reader State

- “Мне ещё один инструмент добавляют, зачем?”
- “Это обязательно или можно использовать, когда реально нужно?”
- “Чем это отличается от обычной просьбы в чате?”
- “Если я откликнусь, меня автоматически назначат?”
- “Идея — это тоже задача или нет?”

### Skepticism Risks

- Words like `доверие`, `вовлечённость`, `инициатива` can sound like HR framing if they appear before the concrete problem.
- “Биржа” can sound like marketplace rhetoric unless explained as visible place for work that needs an owner.
- “Помощь командам” can sound like hidden extra workload unless the text clarifies voluntary matching and agreement.
- Too much process detail will confirm the bureaucracy fear.

### What The Reader Wants First

1. What is this in plain terms?
2. Why should I care?
3. When would I use it?
4. What is expected from me?
5. What is a task, and what is only an idea?

### Vague Or Corporate Traps

- “Повышение эффективности распределения задач”.
- “Поддержка культуры инициативы”.
- “Горизонтальное взаимодействие”.
- “Инструмент вовлечённости”.

These meanings may appear only after translation into operational language.

## Structure-Before-Writing Planning

### Expected Reading Mode

Mixed, but primarily one-time onboarding with quick scanning.

The reader will likely read the opening and the headings first, then stop once they understand whether the system is useful to them. The opening must not bury the practical promise.

### Structure Type

Overview plus practical scenarios.

Recommended flow:

1. plain definition;
2. problem solved;
3. personal use cases;
4. task vs idea distinction;
5. basic interaction model;
6. participation rationale;
7. pointer to detailed instruction.

### Importance Hierarchy

Must be understood first:

- Биржа задач is a shared place for work that needs help or an owner;
- it exists to make available work and available capacity visible;
- it is used when a task can be picked up by another employee or when an idea needs consideration;
- a task has expected result and agreement; an idea is a proposal that still needs assessment.

Secondary:

- examples of usage;
- who interacts with whom;
- why participation helps the organization.

Lowest detail:

- fields, statuses, moderation, platform-specific paths, exception handling.

### Reader-Path Risks

- Reader may stop after the first paragraph if it starts with values instead of use.
- Reader may reject the material if participation sounds like mandatory volunteering.
- Reader may misunderstand ideas as tasks and expect immediate execution.
- Reader may think the exchange replaces normal management, planning or direct conversation.
- Reader may miss that interaction requires agreement, not just posting or commenting.

### Section Role Map

| Future section | Role |
| --- | --- |
| Что такое Биржа задач | Direct definition and anti-bureaucracy framing |
| Зачем она нужна | Problem solved and scope |
| Когда ей пользоваться | Scenario overview |
| Задача или идея | Core distinction with examples |
| Как устроено взаимодействие | Basic model of Author, potential Executor, agreement and result |
| Зачем участвовать | Personal usefulness, not motivation slogan |
| Где подробности | Boundary: this is orientation, instruction lives separately |

### Duplication Risks

- Do not repeat the purpose in every section.
- Do not explain task lifecycle twice: once as mechanics is enough.
- Do not repeat the task/idea distinction inside every scenario; centralize it.
- Do not end with a motivational summary that repeats the opening in softer words.

### Signal Dilution Risks

- Too many examples may make the text look like a manual.
- Too many value words may make the text look like an HR announcement.
- Too many caveats may make the system feel fragile.
- Too much detail about interaction may hide the simpler message: visible work, visible availability, agreed result.

## Artifact Scope

Required by user:

- `brief.md`
- `orchestration_plan.md`
- `outline.md`
- `draft.md`
- `writer-notes.md`
- `review.md`
- `qa-checklist.md`
- `review-summary.md`
- `final.md`
- `final_decision.md`
- `compact-handoff.md`

Required by local governance:

- `task-manifest.md`
- `status.md`

Omitted:

- `research.md`, `sources.md`, `facts.md`, `claims_table.md`, `claims-used.md`: no external claims or factual evidence set used.

