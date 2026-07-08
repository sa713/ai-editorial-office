# Engineering Review

This file owns practical Engineering Review guidance for AI Editorial Office.
It distills professional engineering review practice into lightweight review
lenses for implementation-sensitive work.

It is not a new role, framework, pipeline, lifecycle stage, review gate,
workflow engine, scoring model, or mandatory artifact set. Use it only when
engineering change safety is material.

## Purpose

Engineering Review checks whether an implementation, automation, configuration,
interface, runtime, data, security, reliability, observability, or performance
change is safe, understandable, validated, and reviewable.

It helps agents:

- evaluate implementation quality without creating a separate Code Reviewer
  role;
- select the engineering concerns that matter for a task;
- distinguish engineering change safety from architecture design fitness;
- make security, configuration, delivery, interface, and operational risks
  visible;
- require evidence proportional to risk;
- keep engineering review inside the existing review gate.

## Relationship To Architecture Review

Architecture Review checks design fitness: architectural drivers,
quality-attribute scenarios, tradeoffs, architecture risks, assumptions,
alternatives, accepted risk, and decision rationale.

Engineering Review checks change safety: code, scripts, configuration,
dependencies, CI/CD, local infrastructure, interfaces, observability,
reliability, data, performance, and secure delivery.

Use both when an engineering change has architectural significance, crosses
canonical or ownership boundaries, affects hard-to-reverse design commitments,
or materially changes quality attributes.

## When To Use

Use Engineering Review when a task changes, reviews, or depends on any of
these:

- code, scripts, tests, validators, generators, or generated outputs;
- dependencies, configuration, environment assumptions, permissions, ignored
  files, or publication boundaries;
- CI/CD workflows, local validation automation, release gates, service files,
  deployment helpers, or runtime assumptions;
- API, CLI, file schema, template, task-pack, connector, or other interface
  contract;
- persistent data, database, migration, retention, backup, or structured
  storage behavior;
- logs, diagnostics, validation output, telemetry, observability, reliability,
  recovery, idempotency, restartability, or performance;
- security-sensitive behavior, secrets, source exposure, abuse paths,
  dependency risk, or permission boundaries.

Do not use Engineering Review for ordinary editorial drafting, copyediting,
tone work, low-risk markdown formatting, strategic planning text with no
implementation surface, or purely visual work unless an engineering surface is
material.

## Review Lenses

Select only the lenses that fit the task.

| Lens | Use when | Core questions |
| --- | --- | --- |
| Code/change safety | Code, scripts, tests, validators, or generators change. | Is the change correct, maintainable, scoped, tested, and easy to review? |
| Security and abuse | Secrets, permissions, source exposure, dependencies, untrusted input, or abuse paths are involved. | What can go wrong, what boundary protects it, and what residual risk remains? |
| Configuration | Defaults, environment variables, ignored files, flags, service files, or tool settings change. | Could config drift or unsafe defaults change behavior or expose private material? |
| Delivery automation | CI/CD, local checks, release gates, workflow triggers, or generated artifacts change. | Do automated checks run at the right time with safe permissions and useful output? |
| Infrastructure/runtime | Local tooling, runtime assumptions, deployment helpers, or operational dependencies change. | What environment must exist, what fails if it is absent, and how is that visible? |
| Interface/API | CLI, scripts, file shapes, templates, schemas, task-pack contracts, connectors, or HTTP APIs change. | Is the contract clear, compatible, validated, and safe on error? |
| Observability | Logs, diagnostics, validator output, telemetry, or failure messages matter. | Can a reviewer or maintainer inspect behavior without guessing? |
| Reliability/recovery | Restartability, idempotency, dependency failure, data loss, or recovery behavior matters. | What failure modes exist, how does the system recover, and what proves it? |
| Data/database | Persistence, schema, migration, retention, constraints, or structured storage appears. | Are integrity, privacy, migration, isolation, and recovery risks handled? |
| Performance | Runtime, latency, throughput, resource use, or large input size is material. | What baseline or measurement supports the performance claim? |
| Secure delivery synthesis | Security, config, CI/CD, infrastructure, and operations overlap. | Is the release path secure end to end, or do separate lenses leave a gap? |

## Competency Disposition

Engineering Review intentionally uses one capability with lenses.

| Competency | Disposition |
| --- | --- |
| Code Review | Active lens. |
| Security Review | Active lens, split internally into code security, threat/abuse, dependency, secret/publication, permission, and data exposure concerns. |
| Configuration Review | Merged active lens. |
| CI/CD Review | Merged active lens for delivery automation. |
| Infrastructure Review | Merged active lens for local/tooling/runtime scope; cloud or hosting scope is postponed until such a surface exists. |
| API Review | Merged active lens as Interface/API Review. |
| Observability Review | Merged active lens and prerequisite for strong reliability/performance claims. |
| Reliability Review | Merged active lens. |
| Database Review | Trigger-based lens only; standalone capability postponed until persistent storage exists. |
| Performance Review | Trigger-based lens only; standalone capability postponed until measurable performance risk exists. |
| DevSecOps Review | Rejected as standalone capability; merged as secure delivery synthesis. |

## Evidence Pattern

Use evidence proportional to risk. Engineering Review may rely on:

- inspected files or diff;
- validation command output;
- tests, smoke checks, or manual trial;
- affected contract before and after the change;
- dependency, permission, secret, or config boundary;
- failure mode and recovery behavior;
- diagnostic, log, or validator output;
- data integrity or migration evidence;
- performance baseline or explicit no-baseline limitation;
- residual risk and owner when risk is accepted.

No separate Engineering Review artifact is mandatory. Evidence may live in the
Codex task, implementation notes, check-pack, research, `review.md`, or
`final_decision.md`.

## Compact Review Pattern

Use this inside an existing artifact when Engineering Review is material:

```markdown
## engineering review
- changed surface:
- lenses used:
- lenses ruled out:
- evidence checked:
- validation:
- findings:
- residual risk:
- completion judgment:
```

For simple tasks, one or two lines in `review.md` are enough.

## Stop Conditions

Stop, request changes, or escalate when:

- changed files or behavior cannot be identified;
- validation is missing and no no-validation rationale is given;
- security-sensitive data, secrets, private paths, permissions, or dependency
  risk are unresolved;
- configuration or environment assumptions are hidden;
- workflow or automation permissions are unclear;
- interface contract changes are undocumented;
- reliability or performance claims lack evidence;
- data integrity, migration, retention, or recovery risk is unresolved;
- the change has architectural significance but Architecture Review was not
  activated;
- review would require inventing evidence from plausibility.

## Completion Criteria

Engineering Review is complete for a task when the reviewing role can state:

- which engineering surface changed or was evaluated;
- which lenses were used and which were explicitly ruled out when material;
- what evidence was checked;
- what validation passed or why validation was not applicable;
- which findings are blocking, non-blocking, or informational;
- what residual risk remains and who owns it when material;
- whether the correct outcome is `approved`, `changes_requested`, `blocked`,
  or escalation through the existing lifecycle.

## Non-Goals

Engineering Review does not:

- create a Code Reviewer, Security Reviewer, DevOps Reviewer, SRE, DBA, or
  Performance Reviewer role;
- create a new pipeline, lifecycle stage, review gate, checklist system, or
  mandatory artifact;
- replace Architecture Review, quality attributes, evidence confidence,
  planning, Codex task standard, or Review Agent;
- require every small documentation or markdown change to use engineering
  lenses;
- require database or performance review without a concrete data or performance
  surface.
