# Specification

This is a deliverable knowledge profile, not a template or pipeline.

## Purpose

Define behavior, interfaces, constraints, requirements, edge cases, and
acceptance precisely enough for implementation and verification.

## Best Use Cases

- engineering or product behavior must be built consistently;
- ambiguity creates implementation or validation risk;
- interfaces, states, rules, and acceptance criteria matter.

## Weak Use Cases

- business alignment, exploratory research, or executive persuasion;
- the problem and outcome are not yet agreed.

## Typical Reader Goal

Know exactly what must be implemented or verified and where judgment remains.

## Typical Structure

Scope, definitions, required behavior, interfaces or states, constraints, edge
cases, acceptance criteria, dependencies, and unresolved decisions.

## Strengths

- reduces implementation ambiguity;
- supports validation and handoff;
- exposes edge cases and constraints.

## Weaknesses

- can freeze premature decisions;
- costly to keep synchronized;
- often weak on business rationale.

## Common Failure Modes

- vague requirements presented as precision;
- no acceptance criteria;
- hidden assumptions or undefined terms;
- implementation detail mixed with unresolved product decisions.

## Typical Companion Deliverables

- [BRD](brd.md) for business context;
- [Implementation Plan](implementation-plan.md) for sequencing and ownership;
- [Checklist](checklist.md) for verification.

## Not This

A specification is not a [BRD](brd.md) or [Implementation Plan](implementation-plan.md):
it defines required behavior, not business justification or delivery sequence.
