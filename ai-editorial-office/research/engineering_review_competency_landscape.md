# Engineering Review Competency Landscape

Date: 2026-07-08

Status: research artifact only. This file does not modify canon, roles,
pipelines, lifecycle, review gate, `/about`, or implementation behavior.

## Executive Summary

Professional engineering review is not one checklist. It is a family of review
lenses that protect implementation quality, security, configuration safety,
delivery automation, infrastructure assumptions, interface contracts,
operability, data integrity, performance, and reliability.

For AI Editorial Office, the important architecture lesson is that these areas
should not become separate default roles or many disconnected capabilities.
They are best represented as one Engineering Review capability with selectable
lenses. Chief Editor activates the capability for engineering-sensitive work;
Review Agent challenges it during independent review; existing Architecture
Review still owns system-shape decisions; existing quality, evidence,
planning, and Codex-task frameworks remain in place.

The professional sources converge on a stable pattern:

- start from the changed surface and risk;
- review against evidence, not preference;
- make threats, assumptions, contracts, and failure modes explicit;
- keep automation, configuration, and supply chain review close to security;
- require observability before strong reliability or performance claims;
- treat database and performance review as trigger-based, not always-on;
- preserve remediation owner, validation, and residual risk.

## Source Basis

Primary external sources used:

| Source | Used for |
| --- | --- |
| Google Engineering Practices, Code Review Developer Guide, `https://google.github.io/eng-practices/review/` | Code review standard, change safety, reviewer focus. |
| NIST SP 800-218 Secure Software Development Framework, `https://csrc.nist.gov/pubs/sp/800/218/final` | Secure development practices, vulnerability response, verification. |
| OWASP SAMM, `https://owasp.org/www-project-samm/` | Software assurance governance, design, implementation, verification, operations. |
| OWASP API Security Top 10 2023, `https://owasp.org/API-Security/editions/2023/en/0x11-t10/` | API/interface security risk classes. |
| The Twelve-Factor App, Config, `https://12factor.net/config` | Configuration separation and environment-specific config risk. |
| GitHub Actions Security Hardening, `https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions` | CI/CD workflow hardening, tokens, scripts, untrusted input. |
| SLSA v1.0 specification, `https://slsa.dev/spec/v1.0/` | Supply-chain integrity, provenance, build levels. |
| OpenTelemetry Observability Primer, `https://opentelemetry.io/docs/concepts/observability-primer/` | Observability signals and inspectability. |
| Google SRE, Service Level Objectives, `https://sre.google/sre-book/service-level-objectives/` | Reliability targets, SLO thinking, error budgets. |
| Google SRE, Monitoring Distributed Systems, `https://sre.google/sre-book/monitoring-distributed-systems/` | Monitoring signals and operational evidence. |
| PostgreSQL documentation, transaction isolation and constraints, `https://www.postgresql.org/docs/current/transaction-iso.html`, `https://www.postgresql.org/docs/current/ddl-constraints.html` | Database integrity, isolation, constraint thinking. |
| web.dev Core Web Vitals, `https://web.dev/articles/vitals` | User-centered performance measures and measurement discipline. |

Internal sources reused:

- `architecture_review_landscape.md`;
- `editorial_competency_landscape.md`;
- `editorial_deliverables_landscape.md`;
- `engineering_review_execution_plan.md`;
- `kb/architecture_review.md`;
- `kb/codex_task_standard.md`;
- `kb/editorial_quality_attributes.md`;
- `kb/capability_registry.md`.

## Competency Findings

### Code Review

Professional signal: Code review checks correctness, understandability,
maintainability, test adequacy, and consistency with local standards. Strong
reviewers evaluate the changed code and its system effects rather than only
format or personal style.

AI Editorial Office relevance:

- Codex regularly changes scripts, markdown rules, generated task packs, tests,
  and repository structure.
- Review Agent already checks implementation tasks for repository inspection,
  validation, deliver-back clarity, and canon integration.
- Code Review should become the baseline Engineering Review lens, not a new
  role.

Decision: implement as the default Engineering Review lens for code/script
changes.

### Security Review

Professional signal: NIST SSDF and OWASP SAMM treat security as part of the
software lifecycle: define requirements, secure implementation, verify
security properties, manage vulnerable dependencies, and respond to findings.

AI Editorial Office relevance:

- The project has publication boundaries, private path exclusions, local source
  files, GitHub publication risks, scripts, and potential future connectors.
- Security review must cover secrets, unsafe source disclosure, dependency and
  supply-chain risk, injection/abuse paths, and permission assumptions.
- Some security concerns are architectural, but not every security finding is
  an Architecture Review.

Decision: implement as an Engineering Review lens. Split internally into code
security, threat/abuse modeling, secret/publication safety, dependency risk,
and permission/data handling.

### Configuration Review

Professional signal: configuration should be separated from code and reviewed
as a first-class source of behavior. Environment variables, feature flags,
defaults, ignored files, and permissions can change system behavior without a
normal code diff.

AI Editorial Office relevance:

- `.gitignore`, service files, scripts, environment assumptions, deployment
  helpers, and memory-package sync rules can all create configuration drift.
- Configuration review protects safe-core publication and local/private file
  boundaries.

Decision: merge into Engineering Review as a foundational lens, tightly linked
to security and CI/CD.

### CI/CD Review

Professional signal: workflow security and reliability depend on triggers,
token permissions, secrets, script injection risk, artifact handling, and
whether automated checks actually protect the release.

AI Editorial Office relevance:

- The project already uses local validation scripts and may use GitHub checks.
- CI/CD Review should protect workflow changes, test coverage expectations, and
  release gates without becoming a new pipeline.

Decision: merge into Engineering Review as the delivery automation lens.

### Infrastructure Review

Professional signal: infrastructure review checks runtime assumptions,
deployment environment, permissions, dependencies, operational ownership, and
environment drift. Cloud review models often use pillars such as operational
excellence, security, reliability, performance, and cost.

AI Editorial Office relevance:

- Current infrastructure is mostly repository-local: scripts, tests, generated
  files, services, deployment helpers, and local runtime assumptions.
- Cloud/hosting review is premature unless a real deployment surface appears.

Decision: merge local/tooling infrastructure into Engineering Review. Postpone
cloud/hosting infrastructure review until a deployment surface exists.

### API Review

Professional signal: API review protects contract clarity, compatibility,
authentication, authorization, error behavior, rate/limit behavior, data
exposure, and versioning. OWASP API risks show that interface security is a
specialized surface, not only implementation style.

AI Editorial Office relevance:

- The project may not expose HTTP APIs, but it has interfaces: scripts,
  command-line behavior, generated task pack shapes, markdown schemas,
  templates, and future connectors.
- API Review should be called Interface Review inside the system unless a true
  API surface exists.

Decision: merge as Interface/API lens. Use for contract-affecting changes.

### Observability Review

Professional signal: Observability makes system behavior inspectable through
signals such as logs, metrics, traces, events, diagnostics, and failure output.
Without observability, reviewers cannot validate reliability or performance
claims.

AI Editorial Office relevance:

- Script output, validator messages, task-pack reports, smoke-test evidence,
  and error messages are the project equivalent of operational signals.
- Review Agent needs inspectable validation output.

Decision: merge as Observability lens and make it a prerequisite for strong
reliability/performance claims.

### Reliability Review

Professional signal: Reliability review uses SLOs, failure modes, recovery
behavior, dependency failure, incident readiness, and monitoring evidence. It
requires concrete expectations and signals, not vague "robustness".

AI Editorial Office relevance:

- The system already values restartability, recovery, status consistency,
  validation, and not losing task state.
- Reliability Review should focus on failure modes, idempotency, recovery,
  data loss, validation repeatability, and restart safety.

Decision: merge as Reliability lens. Use after or alongside Observability
when behavior evidence exists.

### Database Review

Professional signal: database review protects schema integrity, migrations,
constraints, isolation, consistency, backups, query safety, retention, and
privacy.

AI Editorial Office relevance:

- The current system is markdown-first and does not have an active database as
  a core architectural surface.
- Database competence matters if a future task introduces SQLite, external
  storage, migrations, persistent state, or structured data stores.

Decision: postpone as a standalone active lens. Keep as a trigger-based
sub-lens inside Engineering Review for storage/persistence tasks.

### Performance Review

Professional signal: performance review requires baselines, workload
assumptions, measurement method, bottleneck evidence, resource use, and
user/system impact. User-centered performance guidance emphasizes measuring
what affects the user experience.

AI Editorial Office relevance:

- Most current tasks are markdown and script oriented. Premature performance
  capability would be speculative.
- Performance matters for slow validators, large task-pack generation,
  rendering, conversion, or future services.

Decision: postpone as standalone active capability. Keep as trigger-based
Performance lens when measurable performance risk exists.

### DevSecOps Review

Professional signal: DevSecOps integrates security into delivery automation,
configuration, dependency management, release gates, monitoring, and operations.
It is a synthesis across security and delivery disciplines.

AI Editorial Office relevance:

- A standalone DevSecOps capability would duplicate Security, Configuration,
  CI/CD, Infrastructure, Observability, and Reliability review.
- The useful local behavior is secure delivery synthesis when several of those
  lenses are active.

Decision: reject as standalone capability. Merge into Engineering Review as a
secure-delivery synthesis when CI/CD, security, and operational surfaces
overlap.

## Cross-Competency Patterns

### Evidence Pattern

Engineering Review should ask for evidence proportional to risk:

- inspected diff or files;
- tests or validation output;
- affected interface or contract;
- configuration/dependency changes;
- security-sensitive data, permission, or secret boundary;
- operational signal or diagnostic output;
- failure mode and recovery behavior;
- residual risk and owner when risk is accepted.

### Activation Pattern

Activate Engineering Review when a task changes or reviews:

- code, scripts, validators, automation, or generated outputs;
- dependency, config, environment, permissions, or publication boundary;
- CI/CD, service files, deployment helper, or runtime assumption;
- API/interface/schema/task-pack/template contract;
- persistent data, migrations, retention, or structured storage;
- performance, reliability, observability, recovery, or diagnostics;
- security-sensitive behavior, secrets, source exposure, or abuse paths.

Do not activate it for ordinary editorial drafting, copyediting, formatting,
low-risk markdown navigation, or text-only strategy unless engineering change
safety is material.

### Completion Pattern

Engineering Review is complete for a task when Review Agent can state:

- which lenses were used or ruled out;
- which evidence was checked;
- which findings are blocking vs non-blocking;
- what validation passed or is missing;
- what residual risk remains and who owns it;
- whether approval, bounded repair, or block is the correct outcome.

## Recommended Competency Disposition

| Competency | Release disposition | Notes |
| --- | --- | --- |
| Code Review | Implemented lens | Default for code/script changes. |
| Security Review | Implemented lens | Includes abuse, secret, dependency, permission, and data exposure checks. |
| Configuration Review | Merged lens | Linked to security, publication safety, and environment behavior. |
| CI/CD Review | Merged lens | Delivery automation and workflow safety. |
| Infrastructure Review | Merged lens / partial postpone | Local/tooling infra active; cloud/hosting postponed. |
| API Review | Merged lens | Named Interface/API for scripts, schemas, task-pack contracts, connectors. |
| Observability | Merged lens | Validation output, logs, diagnostics, telemetry where applicable. |
| Reliability | Merged lens | Failure modes, recovery, idempotency, restart safety. |
| Database | Postponed standalone | Trigger sub-lens only when persistence/storage appears. |
| Performance | Postponed standalone | Trigger sub-lens only when measurable performance risk appears. |
| DevSecOps | Rejected standalone / merged synthesis | Secure delivery synthesis across other lenses. |

## Research Conclusion

AI Editorial Office should implement one Engineering Review capability. It
should not implement separate Code Review, Security Review, CI/CD Review,
Infrastructure Review, API Review, Observability Review, Reliability Review,
Database Review, Performance Review, or DevSecOps capabilities.

The capability should be:

- optional and explicitly activated;
- owned as reusable guidance in KB;
- selected by Chief Editor when engineering sensitivity is material;
- challenged by Review Agent during independent review;
- integrated with Codex task standard for implementation tasks;
- distinct from Architecture Review but able to feed it when engineering
  concerns become architectural.
