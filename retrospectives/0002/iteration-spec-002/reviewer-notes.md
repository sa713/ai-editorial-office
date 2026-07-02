# Reviewer notes

## Purpose

These notes are for external review of iteration-spec-002 before any implementation.

## Most debatable areas

- Whether reader-state belongs in `editorial_knowledge/02_editorial_intent.md` or only in failure/review guidance.
- Whether an optional review block should ever reach templates.
- Whether intake/orchestration prompts are needed before production trial.
- Whether workspace framing can be used without accidentally implying current activity.

## Risk of over-psychologizing

Watch for:

- emotional language;
- motivation claims;
- inferred reader feelings;
- broad behavioral explanations.

Preferred standard:

```text
first step, pressure, obligation, evidence
```

## Risk of fake softness

Watch for:

- mandatory actions made to sound optional;
- rules moved out of sight;
- blockers softened into suggestions;
- "you can just..." when the task requires more.

Human confirmation needed if obligation level is unclear.

## Risk of tone policing

Watch for review comments like:

- "make it warmer";
- "more human";
- "less formal";
- "more inviting".

These are only valid if tied to a concrete reader-action problem.

## Risk of behavioral bureaucracy

Watch for:

- required reader-state blocks in every task;
- new artifacts;
- new routing;
- new approval steps;
- template bloat;
- pipeline edits without trial evidence.

## Decisions needing human confirmation before implementation

- Exact canonical file for reader-state definitions.
- Whether review template should include an optional block or guidance is enough.
- Whether intake/orchestration prompts are needed at all.
- Whether any pipeline note is justified after production trial.
- Whether TASK-0009 examples may be referenced directly in editorial knowledge.

## Reviewer verdict focus

The review should answer:

```text
Does this spec increase editorial sensitivity without increasing behavioral ambition?
```

If not, implementation should not start.
