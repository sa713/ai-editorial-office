# Business Requirements Document (BRD)

This is a deliverable knowledge profile, not a template or pipeline.

## Purpose

Align business, product, operational, procurement, and governance stakeholders
on the problem, outcomes, scope, requirements, constraints, and acceptance.

## Best Use Cases

- multiple stakeholder groups must approve business requirements;
- rationale, scope, value, constraints, and acceptance need one shared record;
- implementation detail should remain downstream.

## Weak Use Cases

- a precise technical interface or behavior must be implemented directly;
- the need is only a small change or an already-approved execution plan.

## Typical Reader Goal

Agree on what business problem is being solved, what is in scope, and what the
solution must achieve.

## Typical Structure

Context and objectives, stakeholders, scope, business requirements,
constraints, assumptions, acceptance outcomes, dependencies, and risks.

## Strengths

- creates cross-functional alignment;
- preserves rationale and boundaries;
- separates business need from implementation choice.

## Weaknesses

- can become bureaucratic or vague;
- may duplicate specifications;
- difficult to maintain when ownership is unclear.

## Common Failure Modes

- solution design disguised as business requirement;
- untestable requirement language;
- missing out-of-scope boundaries;
- no approval or acceptance owner.

## Typical Companion Deliverables

- [Decision Memo](decision-memo.md) for the approval request;
- [Specification](specification.md) for implementable detail;
- [Implementation Plan](implementation-plan.md) after approval.

## Not This

A BRD is not a [Specification](specification.md): it defines business need and
required outcomes, not the full technical behavior or implementation contract.
