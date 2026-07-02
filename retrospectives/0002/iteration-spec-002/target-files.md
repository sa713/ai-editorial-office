# Target files

## Purpose

This file lists potential implementation targets only. It does not authorize implementation now.

Preferred order:

1. `editorial_knowledge` first.
2. Review guidance second.
3. Intake/orchestration prompts only if needed.
4. Pipelines last and minimally.

## Primary target: `editorial_knowledge/01_principles.md`

**Why it may be touched**
To add the honesty boundary if principles currently own editorial invariants.

**Possible change**
Short rule: mandatory stays mandatory, optional stays optional, unknown stays unknown.

**Canonical ownership**
Editorial quality principles and durable editorial boundaries.

**Do not add**
Behavioral theory, metrics, emotional language, new lifecycle rules.

**Drift risk**
Medium. This could duplicate governance rules if written too broadly.

## Primary target: `editorial_knowledge/02_editorial_intent.md`

**Why it may be touched**
To mention reader-state as a task-dependent modifier to intent.

**Possible change**
Small note: for onboarding/change tasks, intent may include safe first step and low-pressure entry.

**Canonical ownership**
Editorial intent and reader outcome.

**Do not add**
Large intent taxonomy or behavioral modes.

**Drift risk**
High if reader-state becomes a new intent family.

## Primary target: `editorial_knowledge/40_editorial_review_system.md`

**Why it may be touched**
To add optional pressure audit for relevant tasks.

**Possible change**
Optional review questions: fake obligation, unsupported urgency, too-early commitment, safe first step.

**Canonical ownership**
Review criteria, review depth and review findings.

**Do not add**
Tone scoring, mandatory behavioral review, new verdicts.

**Drift risk**
Medium. Review could become subjective if questions are not tied to reader action.

## Primary target: `editorial_knowledge/50_editorial_failure_patterns.md`

**Why it may be touched**
To add TASK-0009 failure patterns.

**Possible change**
Small pattern entries for mandatory-process framing, pressure-first onboarding, fake adoption momentum, overexplaining before entry.

**Canonical ownership**
Reusable editorial failure patterns.

**Do not add**
Exhaustive taxonomy, psychological labels, campaign strategy.

**Drift risk**
Low-medium if each pattern includes repair direction.

## Secondary target: `editorial_knowledge/03_usefulness_review.md`

**Why it may be touched**
If usefulness review currently owns first-step clarity.

**Possible change**
Add a sentence that useful communication may include a safe first step when action is requested.

**Canonical ownership**
Usefulness and reader-facing practical value.

**Do not add**
Engagement/adoption goals.

**Drift risk**
Medium. Usefulness must not become persuasion.

## Secondary target: review template, if one exists under `templates/artifacts/`

**Why it may be touched**
Only if production trial shows reviewers need a visible optional block.

**Possible change**
Optional section for relevant tasks.

**Canonical ownership**
Fillable artifact shape.

**Do not add**
Required reader-state block for every review.

**Drift risk**
High. Templates can turn optional checks into default bureaucracy.

## Secondary target: orchestration template, if one exists under `templates/tasks/` or task setup scaffolds

**Why it may be touched**
Only if production trial shows reader-state must be decided before writing.

**Possible change**
Optional prompt: "Does this task require reader-state checks?"

**Canonical ownership**
Task setup scaffolding, not policy.

**Do not add**
New task type, new workflow, mandatory field set.

**Drift risk**
High. Orchestration can bloat quickly.

## Last-resort target: `pipelines/*.md`

**Why it may be touched**
Only if repeated production use shows a pipeline-level ambiguity.

**Possible change**
One conditional note in the relevant pipeline, not all pipelines.

**Canonical ownership**
Pipeline sequence and task-type artifact depth.

**Do not add**
New behavioral stage, new review gate, new artifacts.

**Drift risk**
Very high. Avoid unless evidence is repeated.

## Explicit non-targets for iteration 002 implementation

Do not edit by default:

- `AGENTS.md`;
- `/agents/*.md`;
- all pipelines;
- all templates;
- old task artifacts;
- `editorial_knowledge/cases/*` unless adding a clearly bounded case note later.
