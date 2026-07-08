# Engineering Review Architecture Synthesis

Date: 2026-07-08

Status: architecture synthesis for Engineering Review release. This file is
task/release evidence, not a canonical rule owner.

## Decision

Implement Engineering Review as one shared capability with selectable review
lenses.

Do not implement separate capabilities for Code Review, Security Review,
Configuration Review, CI/CD Review, Infrastructure Review, API Review,
Observability, Reliability, Database, Performance, or DevSecOps.

## Architectural Rationale

The current AI Editorial Office architecture is:

```text
task object first;
capability map second;
roles as accountability wrappers;
workflows and pipelines as execution guidance;
artifacts as views over task state.
```

Engineering Review fits this architecture as a shared capability:

- Chief Editor selects it during routing or implementation planning.
- Research Agent may support evidence when an engineering question needs
  external or repository research.
- Writer Agent or Codex produces implementation or documentation changes inside
  the selected route.
- Review Agent applies the selected Engineering Review lenses during
  independent review.
- Final Editor preserves approved risk, validation, and caveats when a final
  artifact is produced.

No new role, lifecycle stage, pipeline, review gate, mandatory artifact, or
framework owner is needed.

## Relationship To Existing Capabilities

### Architecture Review

Architecture Review owns design fitness: drivers, quality-attribute scenarios,
tradeoffs, architecture risks, assumptions, alternatives, and rationale.

Engineering Review owns implementation and operational change safety: code,
security, configuration, delivery automation, infrastructure assumptions,
interfaces, observability, reliability, data, performance, and secure delivery.

When an engineering issue affects system shape, ownership boundaries, hard to
reverse design decisions, lifecycle, or quality-attribute architecture,
Architecture Review should also be activated.

### Editorial Quality Attributes

Engineering Review uses existing quality vocabulary such as correctness,
maintainability, traceability, implementation readiness, reviewability,
security, reliability, operability, and performance. It does not create a
second quality framework.

### Codex Task Standard

Codex implementation tasks should name Engineering Review triggers when change
safety depends on code, config, security, automation, interfaces, storage,
observability, reliability, or performance. This is a task-shaping requirement,
not a new Codex workflow.

### Review Agent

Review Agent already owns independent review. Engineering Review gives Review
Agent engineering-specific lenses and evidence expectations. It does not
replace `review.md` or create a second review gate.

## Capability Shape

Create:

- `kb/engineering_review.md`

Update:

- `kb/capability_registry.md`
- `kb/00_index.md`
- `kb/codex_task_standard.md`
- `agents/chief_editor.md`
- `agents/review_agent.md`
- `project-state.md`
- `/about` package copies/summaries as needed

Do not update:

- `AGENTS.md`, unless a future architectural acceptance requires making
  Engineering Review a named canonical owner in the charter;
- pipelines;
- task object model;
- shared lifecycle kernel;
- role set;
- roadmap;
- lifecycle validator behavior.

## Lens Model

Engineering Review has these lenses:

| Lens | Covers | Status |
| --- | --- | --- |
| Code/change safety | implementation quality, maintainability, tests, diff clarity | active |
| Security and abuse | secrets, permissions, dependency risk, unsafe disclosure, abuse paths | active |
| Configuration | defaults, env assumptions, ignored files, flags, config drift | active |
| Delivery automation | CI/CD, local checks, workflow triggers, release gates | active |
| Infrastructure/runtime | local tooling, runtime assumptions, service/deploy helpers | active for local scope |
| Interface/API | scripts, CLI, file contracts, schemas, connectors, HTTP APIs if introduced | active |
| Observability | logs, diagnostics, validation output, telemetry, failure messages | active |
| Reliability/recovery | failure modes, idempotency, restartability, data loss, dependency failure | active |
| Data/database | persistence, migrations, constraints, retention, integrity | trigger-based/postponed |
| Performance | baselines, resource use, latency, throughput, measurable bottlenecks | trigger-based/postponed |
| Secure delivery synthesis | overlap of security, CI/CD, config, infra, observability | merged DevSecOps lens |

## Competency Decisions

### Implemented As Active Lenses

- Code Review.
- Security Review.
- Configuration Review.
- CI/CD Review.
- local Infrastructure Review.
- Interface/API Review.
- Observability Review.
- Reliability Review.

### Merged

- Configuration Review merges into Engineering Review as configuration lens.
- CI/CD Review merges as delivery automation lens.
- Infrastructure Review merges as local/runtime lens; cloud/hosting remains a
  future trigger.
- API Review merges as Interface/API lens.
- Observability and Reliability stay separate lenses inside one capability
  because reliability depends on observability evidence.
- DevSecOps merges as secure delivery synthesis.

### Postponed

- Database Review as a standalone competency until persistent storage,
  database schema, migration, or storage-heavy task exists.
- Performance Review as a standalone competency until measurable performance
  risk, baselines, workload assumptions, or service/user-performance surface
  exists.
- Cloud/hosting Infrastructure Review until deployment surface exists.

### Rejected

- Standalone DevSecOps capability is rejected because it would duplicate and
  blur Security, Configuration, CI/CD, Infrastructure, Observability, and
  Reliability lenses.
- One-capability-per-competency implementation is rejected because it adds
  capability sprawl without improving current review quality.

## Activation Rules

Engineering Review should be activated when a task changes or evaluates:

- code, scripts, tests, validators, or generated outputs;
- dependency, configuration, environment, permission, or publication boundary;
- CI/CD workflow, local validation, deployment helper, or service file;
- API, CLI, file schema, template, task-pack, or connector contract;
- persistent data, database, migrations, retention, or structured storage;
- reliability, restartability, idempotency, recovery, observability,
  diagnostics, or performance;
- security-sensitive behavior, secrets, source exposure, or abuse paths.

Engineering Review should not be activated for:

- ordinary editorial drafting;
- copyediting and tone work;
- low-risk markdown formatting;
- strategic planning text with no implementation surface;
- visual work unless scripts, generated assets, security, storage, or
  automation risks are material.

## Evidence Requirements

Engineering Review evidence should be proportional:

- low-risk code/doc-support change: changed files, relevant diff, validation
  command or explicit no-test rationale;
- security/config/delivery change: affected boundary, permission or secret
  handling, validation, residual risk;
- interface change: contract before/after, compatibility impact, error or
  failure behavior;
- observability/reliability change: failure mode, diagnostic output, restart or
  recovery evidence;
- data/performance change: data integrity or measurement evidence, baseline or
  clear no-baseline limitation.

No separate artifact is mandatory. Evidence can live in a Codex task, research
artifact, implementation notes, check-pack, `review.md`, or
`final_decision.md`.

## Validation Strategy

Validation for this release should include:

- existing task lifecycle validator smoke test;
- task pack generator smoke test;
- `/about` memory package sync check;
- `git diff --check`;
- `git diff --cached --check`;
- manual activation examples for Engineering Review:
  - positive code/script change;
  - positive security/config/CI change;
  - positive interface/reliability change;
  - negative ordinary editorial markdown task;
  - negative strategic planning doc with no implementation surface.

## Architecture Risks

| Risk | Mitigation |
| --- | --- |
| Engineering Review becomes a second review gate | State explicitly that `review.md` remains the review gate. |
| Too many lenses become mandatory | Use activation triggers and proportional evidence. |
| Engineering Review duplicates Architecture Review | Keep design-fitness decisions in Architecture Review and implementation/change safety in Engineering Review. |
| Security review becomes a catch-all | Make security a lens selected by risk, not a default for every text task. |
| Database/performance work becomes speculative | Postpone standalone review until real surfaces and evidence exist. |
| `/about` drift | Sync copied canonical files and summary memory after implementation. |

## Completion Judgment

Engineering Review can be considered internally complete for release when:

- one canonical Engineering Review guidance file exists;
- capability registry includes it as a shared non-role capability;
- Chief Editor and Review Agent know when to select/challenge it;
- Codex task standard includes Engineering Review triggers for implementation
  tasks;
- KB index exposes the guidance;
- research and synthesis artifacts explain merge/postpone/reject decisions;
- validation passes;
- `/about` is synchronized;
- release report records final decisions and remaining risks.
