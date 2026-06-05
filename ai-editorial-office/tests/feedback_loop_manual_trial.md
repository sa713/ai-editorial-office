# Feedback Loop Manual Trial

This is a synthetic/sanitized manual trial. It is not a real task folder and
does not contain real working materials.

## Purpose

Check how the Feedback Loop guidance classifies a sanitized post-delivery
reaction when it contains both a concrete revision request and a possible
repeated style signal.

## Trial status

- Synthetic/sanitized trial only.
- Not a task artifact.
- No real tasks, teams, clients, documents, source files, or people are used.

## Raw feedback

> После финального текста пользователь говорит: "В целом нормально, но ты опять
> начал слишком официально. Убери первый абзац и начни сразу с сути".

This scenario is synthetic/sanitized and does not describe a real delivered
artifact.

## Compared examples

- Bounded revision example: primary match, because the user asks for a concrete
  change to the delivered artifact.
- Possible pattern example: useful comparison, because "опять" suggests a
  possible repeated style signal.
- Task-local note example: partial contrast, because this is more than a minor
  observation; it asks for a specific edit.
- System change proposal example: negative contrast, because one sanitized
  feedback signal is not enough to propose a system update.

## Classification

Expected classification: `bounded revision + possible pattern watch`

Why:

- The request to remove the first paragraph and start with the substance is a
  concrete bounded revision.
- The word "опять" may indicate a repeated style issue, so it is worth watching
  as a possible pattern.
- One sanitized feedback signal is not enough to create a system change
  proposal.
- This feedback must not automatically change `AGENTS.md`, pipelines, templates,
  or KB.

## Expected next action

- Create task-local `feedback.md` only if this were a real task.
- Perform the bounded revision if the task is still in revision scope.
- Do not update `feedback_patterns.md` from one case unless repeated evidence
  exists.
- Do not create `system_change_proposal.md` yet.
- Do not change production rules.

## What should not happen

- should not change `AGENTS.md`;
- should not update pipelines;
- should not add raw feedback to KB;
- should not create system change proposal from one signal;
- should not bypass review if revised artifact needs review;
- should not create real task materials.

## Decision

Manual trial result: feedback loop is useful.

The guidance separates the task-local revision from the possible system signal
without turning one comment into a rule.

## Need for validator

Lightweight validator is not needed yet.

Recommendation:

- run 1-2 more sanitized feedback trials;
- return to a lightweight validator only if feedback files, feedback patterns,
  and system change proposals start getting confused.
