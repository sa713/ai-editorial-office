# Raw Brief Normalization Decisions

## owner

The mechanism lives in:

```text
ai-editorial-office/agents/intake_agent.md
```

## implemented decision

Raw Brief is now treated as a normal editorial input form, not an error state.

Intake Agent must attempt to understand the task and create a working brief before asking clarifying questions.

## recovery rule

When reliable, Intake may infer:

- task type;
- channel;
- audience;
- goal;
- expected result;
- minimum sufficient constraints.

Allowed basis:

- user wording;
- task context;
- common sense;
- editorial templates.

## clarifying-question rule

Clarifying questions are reserved for missing information that materially blocks routing or brief creation, could lead to the wrong result, and cannot be reasonably recovered.

This means incompleteness alone is not enough to ask questions.

## safety limits

Intake must not:

- invent facts;
- invent people;
- invent events;
- turn assumptions into facts;
- change the user's goal.

Assumptions must stay labeled as assumptions.

## Chief Editor relation

Chief Editor receives the normalized working brief from Intake.

Chief Editor confirms routing, risk mode, pipeline or mode, and role assignment. Chief Editor is not responsible for reconstructing raw user context.

## non-decisions

This update does not create:

- a new pipeline;
- a new review rule;
- a new visual subsystem behavior;
- a new role;
- a new task status model.

