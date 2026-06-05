# Preflight Gate Checker Decision

## Status

Decision: do not add automated Preflight checker yet.

This is a decision note for test/reference material. It is not production
governance and does not replace `AGENTS.md`, Intake Agent, Chief Editor, task
artifacts, or review-gate.

## Context

The decision follows three sanitized manual trials:

- internal coordination scenario;
- Sber-owned vs Sber-as-topic scenario;
- UX/context scenario.

## Why

- manual examples already help choose `ask`, `constrain`, `proceed`, or
  `block`;
- the main current value is shared judgment, not automation;
- automated checker may become too rigid too early;
- more real usage is needed before encoding rules;
- current manual smoke-test is enough for now.

## What remains manual

- compare raw request with examples;
- choose `ask`, `constrain`, `proceed`, or `block`;
- decide pipeline, risk mode, and client profile;
- document rationale in `task-manifest.md` or `orchestration_plan.md` when a
  task is created.

## Revisit trigger

Return to automated checker if:

- routing mistakes repeat;
- Sber profile activation/non-activation gets confused again;
- intake starts asking long questionnaires without need again;
- risky tasks proceed without critical source or approval;
- review repeatedly catches Preflight mistakes.

## Current recommendation

Continue with manual smoke-test and add edge cases only after real usage.
