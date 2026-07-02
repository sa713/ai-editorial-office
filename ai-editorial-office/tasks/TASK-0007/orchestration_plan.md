# Orchestration Plan

Task ID: `TASK-0007`

Pipeline: custom article/reference guidance flow based on `/pipelines/article_pipeline.md`

Risk mode: `low-risk`

## Execution Model

This task produces a reusable editorial guide. It needs structure-before-writing because readers will use it selectively when drafting or reviewing internal communications.

Separate external research is not required. The work is based on the user brief and local editorial standards: usefulness-first structure, information priority behavior, launch/onboarding communication learnings, and tone rules against fake warmth and corporate sludge.

Sequence:

1. Intake and brief.
2. Structure-before-writing planning.
3. Writing: outline, draft, writer notes.
4. Independent review.
5. Finalization.
6. Chief Editor final decision.

## Roles

| Stage | Role | Output |
| --- | --- | --- |
| Intake | `intake_agent` | `brief.md`, status framing |
| Orchestration | `chief_editor` | `orchestration_plan.md` |
| Writing | `writer_agent` | `outline.md`, `draft.md`, `writer-notes.md` |
| Review | `review_agent` | `review.md`, `qa-checklist.md`, `review-summary.md` |
| Finalization | `final_editor` | `final.md`, finalization notes |
| Governance | `chief_editor` | `final_decision.md`, `compact-handoff.md` |

## Intake Findings

### why an opening exists

An opening should earn its place by doing at least one job:

- orienting the reader to what changed, when, or why now;
- naming the situation the message helps with;
- setting the level of importance or required attention;
- reducing friction when the message interrupts work;
- making the first action or decision easier to find.

A greeting alone only performs social politeness. It is not enough when the reader needs relevance, context, or action.

### when greeting is useless

A greeting is useless when:

- the subject line or channel already establishes the audience;
- the first line repeats the subject without adding meaning;
- the message is short and operational;
- the reader needs a deadline, link, decision, or change first;
- politeness delays the only useful information.

### when opening helps

An opening helps when it carries useful context:

- what is new;
- what requires attention;
- who is affected;
- why the message appears now;
- what kind of reading is expected: awareness, decision, action, calendar check.

### openings that only occupy space

Space-filling openings include:

- ceremonial greetings with no context;
- generic enthusiasm;
- phrases that announce communication rather than deliver information;
- broad corporate rationale before the specific signal;
- playful lines that create tone work without reader benefit.

## Structure-Before-Writing

### Email reading behavior

Expected mode: subject-line triage, preview scan, then selective reading.

Email can tolerate one orienting sentence before details if that sentence changes interpretation. It should not tolerate a politeness-only line followed by a generic intro.

First useful signal should usually be:

- the change;
- the decision;
- the affected group;
- the deadline;
- the event date;
- the reader situation.

Opening should orient when:

- the message has several details and needs a frame;
- the announcement could be mistaken for routine noise;
- the reader needs to know whether the message affects them;
- the calendar item needs timing or priority.

Opening should disappear when:

- the email is a short operational notice;
- the subject line plus first sentence can carry the full signal;
- the main value is a deadline, link, or action;
- any greeting creates delay before usefulness.

### Messenger reading behavior

Expected mode: fast feed scan, interruption-aware reading, low patience for ceremonial setup.

Messenger openings should be shorter than email openings. The first line should almost always carry the signal. A greeting is rarely needed in channel posts unless the post is conversational and low-stakes.

First useful signal should usually be:

- `Сегодня...`;
- `С [даты]...`;
- `Открыта регистрация...`;
- `В календаре...`;
- `Изменился...`;
- `Если вы...`.

Opening should orient when:

- the post interrupts people with a real update;
- the message needs quick filtering by relevance;
- the event or news has timing;
- the reader must decide whether to open details.

Opening should disappear when:

- the channel already has a title and audience;
- the post is a link card, deadline reminder, or operational update;
- the first line can be the headline;
- the greeting would push the useful part below the fold.

### Key editorial checks

- Greeting creates delay when it uses the first line without adding relevance.
- Opening can carry context instead of politeness when it names change, timing, affected reader, or expected action.
- Zero-opening is better than any greeting when the first useful signal is short, clear, and enough.

## Draft Contract

The guide should be curated, not exhaustive. It should group patterns by:

- platform;
- communication type;
- intensity/formality level.

Each pattern needs:

- an example opening;
- when to use it;
- why it works;
- reader-state supported.

The guide must include a bad patterns list with reasons.
