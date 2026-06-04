# Agent Specification Template

Use this form only when defining an approved role. Do not use it to create a new
role unless the governance owner has explicitly added that role to the core role
set or legalized it as an extension role. Global rules live in `AGENTS.md`,
pipelines, and artifact templates; this file captures role-local behavior.

## role

- Agent name:
- Role type:
- Primary stage:
- One-line boundary:

## mission

Short statement of what this role is responsible for and what it must preserve.

## primary responsibilities

- ...

## inputs

Required:

- ...

Conditional:

- ...

## outputs

Required:

- ...

Conditional:

- ...

## forbidden actions

- ...

## decision boundaries

Can decide:

- ...

Must not decide:

- ...

## stop conditions

Stop, block, or escalate when:

- ...

## handoff expectations

State what the next role needs, changed artifacts, blockers, required next
action, and what must not be changed.

## role-specific quality checks

- ...

## canonical references

- Global authority, governance, review-gate, artifact depth, context loading:
  `AGENTS.md`
- Sequence and stage conditions: selected pipeline
- Artifact shape: artifact templates
