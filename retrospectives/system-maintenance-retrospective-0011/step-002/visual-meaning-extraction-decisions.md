# Visual Meaning Extraction Decisions

## Primary Decision

Step 2 adds guidance to the existing `visual_illustration_brief` mode rather than creating a new role, workflow, artifact, or prompt format.

The guidance defines how editors extract visual meaning from a text before there is an illustrator or image prompt.

## Meaning Is Not Topic

The main meaning is the idea the illustration must carry.

It is not:

- the topic of the text;
- a summary of the text;
- a literal list of scenes from the text;
- a new idea invented by the editorial system.

## Viewer Takeaway

The mode now asks for the understanding a viewer should get in 3-5 seconds.

This keeps the work semantic: the editor clarifies what should be understood, not how an image should be composed.

## Emotional Tone

Tone is extracted only when grounded in the text.

Examples include anxiety, hope, absurdity, tension, irony, calm, inquiry, and awe. The list is illustrative, not a style palette.

## Visual Metaphor

The mode allows visual metaphor as a way to carry meaning, but requires a check against the text before accepting it.

The first obvious metaphor can be wrong when it flattens complexity, changes tone, or shifts the conclusion.

## Distortion Risks

The guidance names common risks:

- simplifying a complex idea;
- turning serious material into a joke;
- using aggression where the text is about cooperation;
- adding meaning absent from the text.

## Explicit Boundary

This is not:

- an instruction to an artist;
- composition guidance;
- color guidance;
- style guidance;
- prompt writing;
- a design methodology.
