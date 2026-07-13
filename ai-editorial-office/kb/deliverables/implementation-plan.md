# Implementation Plan

This is a deliverable knowledge profile, not a template or pipeline.

## Purpose

Turn an approved change into an executable sequence of work, owners,
dependencies, validation, rollout, and rollback or recovery considerations.

## Best Use Cases

- the target behavior or decision is sufficiently defined;
- several steps, owners, dependencies, or validation paths must coordinate;
- rollout risk or sequencing matters.

## Weak Use Cases

- the problem, requirements, or architecture decision remains unresolved;
- a simple one-step change needs no coordination.

## Typical Reader Goal

Know who does what, in what order, with which evidence and stop conditions.

## Typical Structure

Scope and prerequisites, work sequence, owners, dependencies, validation,
rollout, risk controls, recovery, and completion criteria.

## Strengths

- converts decisions into coordinated action;
- exposes dependencies and validation;
- supports handoff and progress control.

## Weaknesses

- becomes false precision when requirements are unstable;
- can duplicate project tooling;
- needs active ownership to stay current.

## Common Failure Modes

- task list without dependencies or exit conditions;
- no validation or rollback;
- architecture decisions left implicit;
- plan created before scope is approved.

## Typical Companion Deliverables

- [BRD](brd.md) or [Specification](specification.md) as the approved basis;
- [Checklist](checklist.md) for execution or release control;
- [Decision Memo](decision-memo.md) for unresolved approval.

## Not This

An implementation plan is not a [Roadmap](roadmap.md): it governs an approved
execution path rather than strategic horizons or future option direction.
