# Engineering Review Execution Plan

Status: planning artifact / non-canonical
Roadmap stage: Professional Competency Model -> Engineering Review
Created: 2026-07-08

This document plans the Engineering Review stage for AI Editorial Office. It is
not a capability implementation, research report, architecture specification,
governance source, workflow owner, or operational rule owner.

Canonical behavior remains owned by the files named in `AGENTS.md`. If this
plan conflicts with canonical architecture, lifecycle, roles, pipelines,
frameworks, or review-gate rules, the canonical files win and this plan should
be corrected later.

## Scope

Engineering Review means the project stage that turns professional engineering
review disciplines into a deliberate execution backlog for future AI Editorial
Office capabilities.

Inside AI Editorial Office, Engineering Review should help future Codex/system
work answer questions such as:

- Is the implementation change safe, understandable, and reviewable?
- Are security, configuration, deployment, data, API, performance, reliability,
  and observability risks visible before the change is accepted?
- Which engineering concerns need a dedicated future capability, and which
  should remain part of an existing review or architecture-review path?
- What evidence must exist before Review Agent or Chief Editor can trust an
  engineering change?

This stage does not implement the capabilities. It creates the backlog,
dependencies, sequencing, deliverables, and completion criteria for future
implementation tasks.

## Stage Boundaries

In scope:

- evaluate Engineering Review competencies;
- decide which competencies should merge, split, move, or postpone;
- define expected research artifacts and future capability implementation
  targets;
- recommend execution order and dependencies;
- define completion criteria for the Engineering Review stage.

Out of scope:

- editing `AGENTS.md`, role specs, pipelines, frameworks, capability registry,
  `ROADMAP.md`, `project-state.md`, or `/about`;
- designing capability internals;
- writing implementation prompts for every capability;
- creating eval files, templates, scripts, or KB entries;
- changing task lifecycle, review-gate behavior, or role boundaries.

## Evaluation Basis

The candidate list is evaluated against:

- roadmap strategy: compact, reviewable, capability-aware evolution without new
  default roles;
- current architecture: task object first, capability map second, roles as
  accountability wrappers;
- existing architecture-review knowledge: quality attributes, tradeoffs,
  risks, assumptions, stakeholder concerns, operability, and decision
  rationale;
- practical AI Editorial Office needs: Codex implementation review,
  repository/publication safety, local scripts, markdown-first workflows,
  future capability adoption, and validation readiness.

No external research is required for this execution plan. Future competency
research artifacts may use external primary sources when their own tasks are
opened.

## Recommended Engineering Review Structure

Use three layers:

1. Foundational engineering change review.
2. Delivery and operational review.
3. Specialized system-quality review.

### Layer 1 - Foundational Engineering Change Review

These competencies should come first because most future implementation tasks
need them:

- Code Review;
- Security Review;
- Configuration Review.

### Layer 2 - Delivery and Operational Review

These competencies depend on the foundation and shape how changes move through
automation, environments, and operations:

- CI/CD Review;
- Infrastructure Review;
- Observability Review;
- Reliability Review.

### Layer 3 - Specialized System-Quality Review

These competencies are important but need specific system surfaces or evidence
before they are useful:

- API Review;
- Database Review;
- Performance Review;
- DevSecOps Review as a cross-cutting synthesis layer.

## Merge, Split, Move, Or Postpone Decisions

| Candidate | Decision | Justification |
| --- | --- | --- |
| Code Review | Keep as foundational | Most future Codex tasks change code, scripts, tests, docs-as-behavior, or repo structure. Code Review creates the baseline implementation-quality lens. |
| Security Review | Keep, with research split | Security belongs in Engineering Review, but research should distinguish application security, threat/abuse modeling, secret/publication safety, and dependency risk. |
| Infrastructure Review | Keep, with scope split | Local/repository/tooling infrastructure is relevant now. Cloud/deployment infrastructure should be postponed unless an actual deployment surface appears. |
| API Review | Keep, but interpret broadly | AI Editorial Office may not expose HTTP APIs, but it has interfaces: scripts, CLI behavior, task-pack contracts, file schemas, and future connectors. |
| DevSecOps Review | Postpone as synthesis | It depends on Security, Configuration, CI/CD, and Infrastructure Review. Implementing it first would duplicate or blur those competencies. |
| Configuration Review | Keep as foundational | Configuration drift, unsafe defaults, ignored files, publication boundaries, environment assumptions, and tool settings are high-leverage repo risks. |
| CI/CD Review | Keep, but merge evidence with delivery automation | It should not merge fully into DevSecOps yet; it needs its own review surface for automated checks, workflow triggers, secrets, permissions, and release gates. |
| Database Review | Postpone until data/storage scope exists | The project is markdown-first. Database Review belongs in Engineering Review, but should activate when a database, persistent store, migration, or schema appears. |
| Performance Review | Postpone until baselines and observability exist | Performance review without measurement evidence is speculative. It should follow Code, Infrastructure, Observability, and relevant API/Database work. |
| Reliability Review | Keep after Observability | Reliability needs failure modes, recovery expectations, and operational evidence. Observability should come first so reliability has evidence. |
| Observability Review | Keep before Reliability and Performance | Future reliability and performance reviews need logs, metrics, traces, run evidence, or equivalent inspection hooks. |

## Competency Backlog

### 1. Code Review

- Objective: define how AI Editorial Office evaluates implementation quality,
  change safety, maintainability, tests, local conventions, and reviewable
  diffs.
- Why it belongs: it is the default engineering gate for Codex-produced code
  and script changes.
- Expected research artifact:
  `ai-editorial-office/research/code_review_landscape.md`.
- Expected capability implementation:
  future optional Code Review capability or review rubric used by Review Agent
  for implementation tasks.
- Dependencies: current `AGENTS.md`, Codex task standard, lifecycle validator,
  representative past implementation diffs.
- Estimated implementation priority: P0 / first.

### 2. Security Review

- Objective: define how engineering changes expose security, abuse,
  publication, secret, dependency, permission, and data-handling risk.
- Why it belongs: safe-core publication, local files, automation, dependencies,
  and future connectors require explicit security review boundaries.
- Expected research artifact:
  `ai-editorial-office/research/security_review_landscape.md`.
- Expected capability implementation:
  future optional Security Review capability with activation criteria,
  risk-evidence expectations, and required reviewer outputs.
- Dependencies: Code Review, existing source/provenance policy, publication
  boundary rules, any dependency or automation surfaces present at the time.
- Estimated implementation priority: P1 / second.

Research split:

- application and code security;
- threat/abuse modeling;
- dependency and supply-chain risk;
- secret/publication safety;
- local-data and repository-boundary safety.

### 3. Configuration Review

- Objective: define how configuration, defaults, ignored files, environment
  assumptions, permissions, feature flags, and tool settings are reviewed.
- Why it belongs: configuration mistakes can change behavior without obvious
  code changes and can break publication safety.
- Expected research artifact:
  `ai-editorial-office/research/configuration_review_landscape.md`.
- Expected capability implementation:
  future optional Configuration Review checklist/capability for repo and
  environment-affecting changes.
- Dependencies: Code Review and Security Review.
- Estimated implementation priority: P2 / third.

### 4. CI/CD Review

- Objective: define review of automated checks, workflow triggers, permissions,
  secrets use, artifacts, gates, and release confidence.
- Why it belongs: validation discipline and reviewability depend on reliable
  automation when GitHub or local runners are used.
- Expected research artifact:
  `ai-editorial-office/research/ci_cd_review_landscape.md`.
- Expected capability implementation:
  future optional CI/CD Review capability for workflow and automation changes.
- Dependencies: Code Review, Security Review, Configuration Review.
- Estimated implementation priority: P3 / fourth.

### 5. Infrastructure Review

- Objective: define review of local tooling, repository infrastructure,
  runtime assumptions, environment boundaries, deployment surfaces, and
  operational dependencies.
- Why it belongs: engineering changes often depend on local infrastructure even
  when the product remains markdown-first.
- Expected research artifact:
  `ai-editorial-office/research/infrastructure_review_landscape.md`.
- Expected capability implementation:
  future optional Infrastructure Review capability for tooling and environment
  changes.
- Dependencies: Configuration Review and CI/CD Review.
- Estimated implementation priority: P4 / fifth.

Scope split:

- active now: local repo/tooling/test infrastructure;
- postponed: cloud, hosting, network, and production deployment review until
  those surfaces exist.

### 6. API Review

- Objective: define review of interfaces, contracts, compatibility, error
  behavior, schemas, CLI/API boundaries, task-pack inputs, and connector
  surfaces.
- Why it belongs: AI Editorial Office has interface contracts even without a
  web service, especially scripts, generated packs, templates, and future
  connectors.
- Expected research artifact:
  `ai-editorial-office/research/api_review_landscape.md`.
- Expected capability implementation:
  future optional API/Interface Review capability for contract-affecting
  changes.
- Dependencies: Code Review, Configuration Review, Infrastructure Review.
- Estimated implementation priority: P5 / sixth.

### 7. Observability Review

- Objective: define what evidence makes system behavior inspectable: logs,
  metrics, traces, validation output, diagnostics, failure messages, and audit
  signals.
- Why it belongs: Reliability and Performance Review require behavior evidence;
  Review Agent also needs inspectable validation output.
- Expected research artifact:
  `ai-editorial-office/research/observability_review_landscape.md`.
- Expected capability implementation:
  future optional Observability Review capability for automation, scripts,
  services, and diagnostic outputs.
- Dependencies: Infrastructure Review and CI/CD Review.
- Estimated implementation priority: P6 / seventh.

### 8. Reliability Review

- Objective: define review of failure modes, recovery behavior, idempotency,
  restartability, data-loss risk, dependency failure, and operational readiness.
- Why it belongs: AI Editorial Office already values restartability and
  recovery; engineering changes should preserve that quality.
- Expected research artifact:
  `ai-editorial-office/research/reliability_review_landscape.md`.
- Expected capability implementation:
  future optional Reliability Review capability for changes with operational,
  data, automation, or restart risk.
- Dependencies: Observability Review, Infrastructure Review, Code Review.
- Estimated implementation priority: P7 / eighth.

### 9. Database Review

- Objective: define review of schemas, migrations, persistence boundaries,
  data integrity, query safety, backups, privacy, and retention.
- Why it belongs: it is part of Engineering Review, but only when persistent
  storage exists or a task introduces it.
- Expected research artifact:
  `ai-editorial-office/research/database_review_landscape.md`.
- Expected capability implementation:
  future optional Database Review capability activated only for database or
  persistent-storage tasks.
- Dependencies: Code Review, Security Review, Reliability Review, and any
  concrete storage surface.
- Estimated implementation priority: P8 / postponed until storage scope.

### 10. Performance Review

- Objective: define review of latency, throughput, resource use, scaling
  assumptions, bottlenecks, measurement quality, and performance tradeoffs.
- Why it belongs: performance is a standard engineering review competency, but
  useful review needs baselines and evidence.
- Expected research artifact:
  `ai-editorial-office/research/performance_review_landscape.md`.
- Expected capability implementation:
  future optional Performance Review capability for performance-sensitive
  scripts, services, automation, or data flows.
- Dependencies: Observability Review, Infrastructure Review, API Review,
  Database Review when storage is involved.
- Estimated implementation priority: P9 / postponed until metrics or
  performance-sensitive scope.

### 11. DevSecOps Review

- Objective: synthesize secure delivery, automation, configuration,
  dependency, release, and operations review into one cross-cutting lens.
- Why it belongs: it connects security to delivery and operations, but should
  not become an umbrella that hides concrete review surfaces.
- Expected research artifact:
  `ai-editorial-office/research/devsecops_review_landscape.md`.
- Expected capability implementation:
  future synthesis capability or routing guide that composes Security,
  Configuration, CI/CD, Infrastructure, Observability, and Reliability Review.
- Dependencies: Security Review, Configuration Review, CI/CD Review,
  Infrastructure Review, Observability Review, Reliability Review.
- Estimated implementation priority: P10 / last synthesis.

## Recommended Execution Order

Use the same execution loop for each competency:

```text
Stage calibration
-> competency research
-> architecture synthesis
-> capability implementation task
-> capability validation
-> independent review
-> roadmap/backlog status update if requested
-> /about sync only if canonical or memory-package files changed
```

For this Engineering Review stage, run competencies in this order:

1. Code Review.
2. Security Review.
3. Configuration Review.
4. CI/CD Review.
5. Infrastructure Review.
6. API Review.
7. Observability Review.
8. Reliability Review.
9. Database Review.
10. Performance Review.
11. DevSecOps Review.

Rationale:

- Code Review creates the baseline engineering-review vocabulary.
- Security follows early because repository/publication safety and dependency
  risk can affect every later competency.
- Configuration and CI/CD come before infrastructure synthesis because
  automated checks and environment assumptions shape infrastructure evidence.
- API Review comes before observability/reliability for interface-sensitive
  tasks, but after infrastructure because interface review needs boundaries.
- Observability precedes Reliability and Performance because both need
  behavior evidence.
- Database and Performance are postponed until concrete storage or measurement
  surfaces exist.
- DevSecOps is last because it is a composition of earlier delivery, security,
  and operations competencies.

## Per-Competency Execution Sequence

Each competency should complete these steps before the next implementation
task begins. Research steps may overlap only when Chief Editor explicitly
approves that parallelism.

| Step | Output | Completion condition |
| --- | --- | --- |
| 1. Scope the competency | task-local brief and plan | Objective, non-goals, source boundary, and activation trigger are explicit. |
| 2. Research professional practice | `research/*_review_landscape.md` | Research artifact names sources, review objects, common workflows, evidence, failure modes, and relevance to AI Editorial Office. |
| 3. Synthesize architecture fit | task-local synthesis or proposal | Synthesis says whether this should become capability, checklist, KB guidance, script, validator, or postponed item. |
| 4. Create implementation task | future Codex task/check-pack | Task names allowed files, forbidden files, acceptance criteria, validation, and review requirements. |
| 5. Implement capability or record no-build decision | future changed files or no-build artifact | Implementation remains optional/helper and does not create roles or bypass review. |
| 6. Validate | smoke tests, examples, or manual trials | At least two positive and two negative activation examples pass, unless Chief Editor records why a smaller validation set is sufficient. |
| 7. Review | `review.md` | Review Agent approves the capability or requests bounded changes. |
| 8. Final governance | `final_decision.md` | Chief Editor records whether the competency is complete, postponed, merged, or needs another iteration. |
| 9. Sync memory package if required | `/about` sync task, only when requested/needed | `/about` is updated only when canonical or memory-package files changed and a separate sync is in scope. |

## Dependencies

```text
Code Review
  -> Security Review
  -> Configuration Review
  -> CI/CD Review
  -> Infrastructure Review
  -> API Review
  -> Observability Review
  -> Reliability Review
  -> Database Review
  -> Performance Review
  -> DevSecOps Review
```

Dependency notes:

- Security may feed back into Code, Configuration, CI/CD, and Infrastructure
  Review after its initial research.
- Observability is a prerequisite for credible Reliability and Performance
  Review.
- Database Review should not begin until there is a database, persistent store,
  migration, schema, or storage-heavy task.
- DevSecOps Review should not begin until the underlying security, delivery,
  and operations competencies have at least approved research artifacts.

## Expected Stage Deliverables

Engineering Review is complete only after it produces a reviewed set of
planning and capability-readiness artifacts, not after this plan alone.

Expected deliverables:

- this execution plan;
- one research landscape artifact for each active competency;
- merge/postpone notes for competencies that do not become standalone
  capabilities;
- one architecture synthesis artifact for each active competency;
- future capability implementation tasks for competencies approved for build;
- validation examples or smoke checks for implemented capabilities;
- review artifacts and final decisions for each competency implementation;
- a final Engineering Review stage closure note summarizing completed,
  merged, postponed, and rejected competencies.

## Completion Criteria

Engineering Review can be considered complete when all of the following are
true:

1. Every candidate competency in this plan has one final stage outcome:
   `implemented`, `merged`, `postponed`, or `rejected`.
2. Every `implemented` competency has:
   - an approved research artifact;
   - an architecture synthesis decision;
   - a capability implementation or explicit non-build decision;
   - validation evidence;
   - independent review with outcome `approved`;
   - Chief Editor final decision.
3. Every `merged` competency names the parent competency that covers it and the
   exact review concerns that were absorbed.
4. Every `postponed` competency has a concrete revisit trigger, such as
   "database introduced", "deployment surface exists", or "performance baseline
   needed".
5. Every `rejected` competency states why it does not fit AI Editorial Office
   strategy or current architecture.
6. No completed competency adds a new role, bypasses review, changes lifecycle,
   or makes optional capability use mandatory without a separate reviewed
   canonical update.
7. Validation for each implemented capability includes positive and negative
   activation examples, or a Chief Editor-approved narrower validation reason.
8. The final stage closure note lists:
   - completed competencies;
   - merged competencies;
   - postponed competencies and triggers;
   - rejected competencies;
   - remaining risks;
   - whether `/about` sync is needed.
9. `git diff --check` and `git diff --cached --check` pass for each committed
   implementation slice.
10. The working tree contains no accidental changes outside the approved scope
    for the final Engineering Review stage closure commit.

## Immediate Next Backlog Item

Open the first competency task:

```text
Engineering Review / Code Review
```

The next task should create `research/code_review_landscape.md` and should not
implement a Code Review capability until the research and architecture
synthesis are reviewed.
