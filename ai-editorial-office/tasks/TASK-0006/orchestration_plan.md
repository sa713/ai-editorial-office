# Orchestration Plan

Task ID: `TASK-0006`

Pipeline: `/pipelines/social_pipeline.md`

Risk mode: `standard`

## Execution model

This task uses the Social Pipeline with a launch/onboarding communication scope. Research is not a separate stage because canonical task-local source materials are supplied and no external factual claims are needed.

Sequence:

1. Intake and brief.
2. Structure-before-writing planning.
3. Writing: outline, email draft, messenger draft, writer notes.
4. Independent review.
5. Finalization.
6. Chief Editor final decision.

## Roles

| Stage | Role | Output |
| --- | --- | --- |
| Intake | `intake_agent` | `brief.md`, status framing |
| Orchestration | `chief_editor` | `orchestration_plan.md` |
| Writing | `writer_agent` | `outline.md`, `draft-email.md`, `draft-messenger.md`, `writer-notes.md` |
| Review | `review_agent` | `review.md`, `qa-checklist.md`, `review-summary.md` |
| Finalization | `final_editor` | `final-email.md`, `final-messenger.md` |
| Governance | `chief_editor` | `final_decision.md`, `compact-handoff.md` |

## Source boundary

Allowed content basis:

- Task Exchange is a common place to publish a task, respond to colleagues' tasks, or propose an idea.
- It helps make visible work that can be transferred and people who can help.
- It is not a separate reporting contour and not a replacement for team agreements.
- It is useful when work should be shown beyond the nearest circle, unit, or habitual list of performers.
- Pilot works on АС Taska.
- A task has expected result, Author, potential Executor, agreement about result, deadline, and transfer format.
- A response is not automatic assignment; Author chooses an Executor.
- An idea is a proposal or observation that first needs consideration.
- Detailed instruction exists separately.

Forbidden additions:

- new statuses, roles, escalation paths, rules, restrictions, governance, promises, metrics, guarantees, or policy logic;
- broad claims about efficiency, culture, engagement, transparency, or transformation unless anchored in practical use.

## Intake Findings

### likely reader skepticism

- "Another initiative from above."
- "Will this create extra reporting?"
- "Is this now mandatory?"
- "Why should I open another system?"
- "What happens if I respond to a task?"

### what employees will think first

- Is this relevant to my work today?
- Does it help me solve a real situation?
- Will it take time to understand?
- Am I being asked to do more work?
- Where is the system and what is the first action?

### launch-stage information priority

1. What launched and where.
2. What personal work situation it helps with.
3. What it is not.
4. Task vs idea distinction.
5. Basic interaction model.
6. Where to find instructions.
7. Immediate next step.

### likely corporate/manipulative signals

- "We are pleased to announce."
- "Improve efficiency."
- "Develop initiative culture."
- "New level of interaction."
- "Everyone should actively participate."
- "This will solve workload distribution."

### what readers need before deciding whether they care

- A concrete personal use case.
- A reassurance that it is not extra reporting.
- A quick distinction between task and idea.
- A low-friction first step.
- Link to details without forcing full onboarding in the announcement.

## Structure-before-writing: Email

Expected reading mode: mixed. Many readers skim first paragraph and bullets; some continue for orientation.

Attention window: 45-90 seconds before deciding whether to open the system or ignore.

Signal hierarchy:

1. Pilot launch in АС Taska.
2. Practical usefulness in personal situations.
3. Non-bureaucratic boundary.
4. When to use.
5. Task vs idea.
6. Basic interaction.
7. Instruction and next step.

What must appear first:

- "Запущен пилот Биржи задач в АС Taska."
- "Она может пригодиться, если есть задача вне ближайшего круга, возможность помочь, or idea."

What can be omitted:

- full field-by-field instruction;
- complete status table;
- curator list;
- detailed moderation logic;
- process philosophy.

What belongs in instruction instead:

- how to create a card;
- which fields to fill;
- statuses and columns;
- disputed situations;
- detailed constraints such as no subtasks.

Likely stop points:

- after first paragraph if it sounds ceremonial;
- after "зачем" if usefulness is too abstract;
- inside task/idea explanation if it becomes a manual.

Signal dilution risks:

- too many examples;
- explaining platform details before use cases;
- using institutional goal language from source draft.

Tone supporting trust:

- direct, calm, concrete;
- no celebration;
- no demand to participate;
- no inflated benefit claims.

Personal usefulness check:

- must appear in paragraph 2, before process detail.

## Structure-before-writing: Messenger

Expected reading mode: fast scan in feed.

Attention window: 10-20 seconds.

Signal hierarchy:

1. Pilot is live.
2. Three personal entry points.
3. Task vs idea in one distinction.
4. Next step with links.

What must appear first:

- launch signal plus why a reader might use it.

What can be omitted:

- full interaction model;
- examples of work types;
- detailed moderation/review;
- long reassurance.

What belongs in instruction instead:

- fields, statuses, where to comment, how moderation works.

Likely stop points:

- after first two lines if it reads like an announcement slogan;
- after bullets if no action is visible.

Signal dilution risks:

- copying email intro;
- playful chat tone;
- slogan-style ending.

Tone supporting trust:

- short, plain, useful;
- "можно использовать" instead of "присоединяйтесь";
- operational next step.

Personal usefulness check:

- must appear in the first block as "если у вас есть / если хотите / если есть идея".

## Artifact scope

Required by user:

- `brief.md`;
- `orchestration_plan.md`;
- `outline.md`;
- `draft-email.md`;
- `draft-messenger.md`;
- `writer-notes.md`;
- `review.md`;
- `qa-checklist.md`;
- `review-summary.md`;
- `final-email.md`;
- `final-messenger.md`;
- `final_decision.md`;
- `compact handoff`.

Additional required by local governance:

- `task-manifest.md`;
- `status.md`.

Omitted:

- `research.md`, `sources.md`, `facts.md`, `claims_table.md`, `claims-used.md`; rationale: canonical task-local sources are directly supplied, no external research or new factual claims are introduced.
