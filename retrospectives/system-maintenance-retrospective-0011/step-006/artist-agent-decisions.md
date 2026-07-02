# Artist Agent Decisions

## Primary Decision

Add Artist Agent as an execution role.

The role receives approved editorial artifacts and prepares `image_prompt.md`
or an image when the environment allows. It does not own, reinterpret, or
revise meaning.

## Ownership Chain

Meaning remains owned by:

- `visual_concept.md`;
- `illustration_brief.md`.

Execution is owned by:

- Artist Agent;
- `image_prompt.md`.

## Required Inputs

Artist Agent requires:

- approved `visual_concept.md`;
- approved `illustration_brief.md`;
- task constraints;
- requested image format or aspect ratio when provided.

## Allowed Outputs

Artist Agent may produce:

- `image_prompt.md`;
- an image, only if the environment supports image creation and the task allows
  it;
- blocker notes when the brief is insufficient.

## Boundary Decisions

Artist Agent must not:

- analyze the source text as the primary input;
- replace `visual_concept.md`;
- change `illustration_brief.md`;
- invent new meaning;
- change tone;
- complete the author's idea;
- turn the work into an infographic, comic, or presentation without explicit
  request;
- create a new pipeline;
- change the review system.

## Image Prompt Template Decision

`image_prompt.md` is an execution artifact built on `illustration_brief.md`.

Its template includes:

- source brief;
- illustration goal;
- prompt;
- required elements;
- forbidden distortions;
- text-on-image rules;
- format/aspect ratio;
- style constraints only if given;
- unresolved questions.

## Deferred Work

Still deferred:

- pipeline integration;
- review-system changes;
- comic workflows;
- presentation workflows;
- Step 7.
