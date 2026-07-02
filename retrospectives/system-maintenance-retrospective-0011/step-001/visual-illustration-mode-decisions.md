# Visual Illustration Mode Decisions

## Primary Decision

Add `visual_illustration_brief` as an editorial mode, not as a production workflow.

The mode helps the editorial system extract and structure the meaning a future illustration must carry. It does not draw, assign style systems, generate final image prompts, or create an illustrator/artist role.

## Meaning Before Image

The mode starts from the text's meaning. The expected editorial movement is:

1. meaning of the text;
2. illustration task;
3. viewer perception in 3-5 seconds;
4. visual image or metaphor;
5. required elements and constraints;
6. possible assignment for an illustrator, only after the meaning brief is clear.

## Boundary Decisions

The mode explicitly prevents these drifts:

- rewriting or improving the text;
- inventing a new authorial idea;
- making an infographic unless the user asks for one;
- choosing a banal metaphor without testing it against the text;
- turning the work into a presentation or comic;
- jumping straight to a final prompt before the semantic brief exists.

## Why This Is Not An Artist Agent

The mode defines editorial understanding, not a new executor.

It may help formulate an assignment for an illustrator, but it does not add:

- a role file;
- an agent spec;
- a pipeline stage;
- a template;
- a generation workflow;
- review heuristics.

## Anti-Pattern Coverage

The mode names the main failures directly:

- a beautiful but irrelevant image;
- a literal or banal metaphor;
- visual invention that changes the meaning;
- a picture that changes the tone of the material;
- prompt-first behavior.
