# Architecture Review

This file owns practical Architecture Review guidance for AI Editorial Office.
It distills professional architecture review practice into lightweight review
moves for architecture-sensitive work.

It is not a new role, framework, pipeline, lifecycle stage, review gate,
workflow engine, scoring model, or mandatory artifact set. Use it only when
architectural significance justifies making design drivers, tradeoffs, risks,
and rationale reviewable.

## Purpose

Architecture Review checks whether a proposed or existing architecture is fit
for its drivers, constraints, quality attributes, tradeoffs, risks, operating
context, and decision rationale.

It helps agents:

- distinguish architecture decisions from implementation details;
- identify the drivers and constraints that make a design matter;
- turn vague quality attributes into reviewable scenarios;
- compare credible design alternatives and accepted tradeoffs;
- expose architectural assumptions and accepted risks;
- evaluate architecture evidence rather than preference;
- communicate findings without turning review into redesign.

## When To Use

Use Architecture Review when any of these are material:

- the task evaluates, changes, or recommends system architecture, canon
  architecture, repository structure, lifecycle design, integration boundaries,
  governance structure, or capability/role separation;
- the decision affects quality attributes such as reliability, security,
  maintainability, operability, scalability, performance, cost, traceability,
  reviewability, or evolution;
- the change crosses ownership, interface, data, dependency, pipeline,
  lifecycle, role, or canonical-owner boundaries;
- the decision is hard to reverse or may constrain future work;
- a recommendation depends on rejected alternatives, accepted risk, or
  architectural assumptions;
- Review Agent needs to challenge design fitness, not only code, wording,
  evidence, or product desirability.

Do not use Architecture Review for ordinary small implementation tasks,
wording changes, formatting changes, low-impact bug fixes, or local choices
that do not affect system shape, boundaries, quality attributes, or future
decision space.

## Review Scope

Architecture Review asks:

- What architecture decision or design commitment is being reviewed?
- What drivers and constraints make the decision architectural?
- Which stakeholders, owners, or future maintainers are affected?
- Which quality attributes are materially shaped by the decision?
- Which credible alternatives were considered or rejected?
- What tradeoffs, risks, assumptions, and residual risks are accepted?
- What evidence supports the claimed fitness of the design?
- What would require re-review or revision?

Architecture Review is distinct from:

- code review, which checks implementation quality and change safety;
- security review, which may be one architecture lens but does not cover every
  architecture quality;
- product review, which checks desirability, value, and product direction;
- general editorial review, which checks whether the artifact passes the
  existing review gate.

## Architectural Drivers

Architectural drivers are the reasons the architecture takes its shape.

Common driver classes:

| Driver | Review question |
| --- | --- |
| Business or mission | What outcome makes this architecture matter? |
| User or reader | What workflow, use case, or future user action must the design support? |
| Quality attribute | Which qualities materially shape the design? |
| Constraint | What cannot change: policy, platform, compatibility, deadline, team capacity, source boundary, or governance rule? |
| Integration | Which systems, artifacts, interfaces, owners, or canonical files are affected? |
| Lifecycle | How will the design be operated, reviewed, evolved, retired, or recovered? |
| Risk | What failure would be expensive, unsafe, confusing, or hard to unwind? |

Weak review often starts from a diagram, patch, or preferred solution. Strong
review starts from drivers.

## Quality Attribute Scenarios

Vague quality labels are not enough. Convert material quality attributes into
short scenarios.

```markdown
- quality attribute:
- stimulus or change:
- affected artifact/system part:
- expected response:
- response measure or review evidence:
```

Examples:

- Maintainability: if a new capability is added later, which owner file changes
  and which files only reference it?
- Reviewability: can Review Agent reconstruct the decision from saved
  artifacts without chat memory?
- Operability: if the process restarts after context loss, which artifact tells
  the next owner what to do?
- Security or privacy: which source boundaries, permissions, or private paths
  are protected?

Use only scenarios that affect the decision. Do not create a broad checklist
for every task.

## Tradeoff Analysis

Architecture Review should make real tradeoffs visible.

Compact pattern:

```markdown
## architecture review
- decision:
- drivers:
- quality attributes:
- alternatives considered:
- selected approach:
- tradeoffs accepted:
- architecture risks:
- assumptions:
- evidence:
- completion judgment:
```

Tradeoff review should distinguish:

- selected option vs credible alternatives;
- architectural tradeoff vs personal preference;
- accepted risk vs unresolved blocker;
- architecture decision vs implementation detail;
- current decision vs future revision trigger.

If no meaningful tradeoff exists, the task may not need Architecture Review.

## Architecture-Specific Risks

Common architecture risks:

| Risk | Signal |
| --- | --- |
| Missing drivers | Review cannot say what the architecture is optimizing for. |
| Vague quality attribute | "Scalable", "secure", or "maintainable" has no scenario or evidence. |
| Architecture/implementation confusion | Review debates code details while design commitments, boundaries, or tradeoffs stay hidden. |
| First-plausible design | No credible rejected alternatives are recorded for a significant decision. |
| Hidden architectural assumption | The design relies on an unstated platform, source, workload, owner, or future behavior. |
| Undocumented accepted risk | A known risk is neither mitigated nor explicitly accepted by the right owner. |
| Decision without rationale | Future maintainers can see what changed but not why. |
| Local optimization | One area improves while lifecycle, governance, reviewability, or another owner gets worse. |
| View/evidence mismatch | Diagrams, notes, or artifacts do not support the decision being claimed. |

## Completion Criteria

Architecture Review is complete when the existing review or decision artifact
can support a bounded judgment:

- the reviewed architecture decision is clear;
- architectural significance is explained or ruled out;
- drivers and constraints are visible enough for the task risk;
- material quality attributes have scenarios or concrete evidence;
- credible alternatives and rejected options are visible when meaningful;
- tradeoffs, assumptions, architecture risks, and accepted residual risks are
  recorded at the needed depth;
- architecture evidence supports the conclusion;
- Review Agent can decide `approved`, `changes_requested`, or `blocked` without
  inventing a new review gate.

Do not create a standalone architecture-review artifact by default. Keep the
review note inside the existing artifact that owns the route, research,
implementation task, review, or governance decision.
