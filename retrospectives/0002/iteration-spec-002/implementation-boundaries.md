# Implementation boundaries

## Allowed changes

Future implementation may include:

- short editorial knowledge updates;
- reader-state definitions and boundaries;
- governance honesty rule;
- optional review heuristic;
- optional intake/orchestration prompts for relevant tasks;
- small failure-pattern additions;
- bounded reader-state refinement shape;
- narrow examples from TASK-0009.

## Allowed only after trial evidence

- review template optional block;
- orchestration template optional prompt;
- one narrow pipeline note for a specific task type.

## Forbidden changes

Do not implement:

- new agent;
- new pipeline;
- mandatory behavioral layer;
- behavioral approval stage;
- scoring;
- metrics;
- dashboards;
- automatic pressure detector;
- broad template rewrites;
- lifecycle changes;
- governance weakening;
- emotional taxonomy;
- adoption funnel;
- engagement optimization.

## Semantic prohibitions

Do not:

- treat optional action as mandatory;
- treat mandatory action as optional;
- use soft language to hide rules;
- use workspace framing to invent activity;
- add social proof without evidence;
- turn review into tone preference;
- make reader-state checks universal.

## File-change boundaries

Prefer:

1. `editorial_knowledge`;
2. review guidance;
3. optional prompt owners only if needed;
4. pipelines last.

Avoid:

- `AGENTS.md` unless repeated drift proves ownership issue;
- `/agents/*.md`;
- broad `/pipelines/*.md` edits;
- all-template updates.

## Stop rule

If an implementation step requires a new role, new stage, new metric or broad rewrite, stop. The proposal has exceeded iteration 002.
