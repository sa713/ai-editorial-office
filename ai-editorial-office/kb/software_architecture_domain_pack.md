# Software Architecture Domain Knowledge Pack

Status: active

Pack name: Software Architecture Domain Knowledge Pack

Domain: software architecture

Maintainer context: AI Editorial Office canonical KB, created for release
`S4.R2`.

Created: 2026-07-10

Last reviewed: 2026-07-10

Stale if:

- ISO/IEC/IEEE 42010 or ISO/IEC 25010 is revised, superseded, or withdrawn;
- AWS, Google Cloud, or Azure Well-Architected guidance changes materially;
- repeated Architecture Review or Engineering Review tasks expose missing
  architecture terms, risks, or activation boundaries;
- a future accepted Domain Knowledge Pack Standard adds required sections;
- this pack causes confusion with a role, capability, pipeline, review gate, or
  policy owner;
- the pack is not reviewed for 12 months after acceptance.

## Purpose

This pack helps AI Editorial Office apply source-backed software architecture
knowledge when architecture context materially affects task quality.

It helps existing roles and capabilities reason about:

- whether a choice is architecturally significant;
- which drivers and constraints matter;
- which quality attributes dominate;
- which architectural styles or patterns may fit;
- which tradeoffs, risks, assumptions, and evidence should be visible;
- how boundaries, coupling, data, ownership, and runtime communication shape a
  system;
- what an architecture recommendation can and cannot claim.

This pack is not a role, capability, framework, pipeline, lifecycle stage,
review gate, policy owner, client profile, task status model, or mandatory
ordinary task artifact.

## Intended Use

Use this pack as domain context for architecture-sensitive work. It may support:

- Chief Editor routing and activation decisions;
- Research Agent source framing;
- Writer Agent drafting of architecture-sensitive recommendations, briefs, or
  task instructions;
- Review Agent challenge inside the existing review gate;
- Final Editor preservation of reviewed architecture caveats;
- Architecture Review and Engineering Review when software architecture domain
  knowledge improves their evidence and questions.

The pack does not decide review outcomes, final governance, task status, or
whether a design is accepted.

## When To Activate

Activate this pack only when software architecture context materially changes
evidence depth, terminology, risk handling, review focus, or output quality.

Typical activation triggers:

- the task evaluates, changes, recommends, or explains system architecture;
- the task asks whether a decision is architectural;
- a recommendation depends on architectural drivers, constraints, quality
  attributes, alternatives, or tradeoffs;
- the work crosses service, module, data, API, ownership, deployment,
  lifecycle, runtime, or canonical system boundaries;
- a design choice is hard to reverse or constrains future evolution;
- architecture styles or patterns such as microservices, modular monolith,
  event-driven architecture, N-tier/layered architecture, CQRS, event sourcing,
  circuit breaker, saga, strangler fig, or anti-corruption layer are material;
- Review Agent must challenge architecture rationale, not only prose quality,
  factual support, or code change safety;
- Engineering Review identifies an implementation change with design-fitness
  implications.

Record activation in the smallest existing task artifact that keeps the next
role safe:

- `orchestration_plan.md`;
- `task-manifest.md`;
- `research.md`;
- writer or UX notes;
- `review.md`;
- `final_decision.md`.

Activation note should name:

- active pack: `Software Architecture Domain Knowledge Pack`;
- activation reason;
- relevant sections or sources;
- evidence confidence;
- boundary limits and stale-if triggers;
- stop conditions.

## When Not To Activate

Do not activate this pack when:

- "architecture" is used metaphorically or incidentally;
- the task is ordinary writing, copyediting, formatting, or summarization with
  no architecture-sensitive claim;
- the work is a small local implementation change with no design-fitness,
  boundary, quality-attribute, or future-evolution impact;
- Engineering Review alone can handle code/config/change safety;
- the task is primarily DevSecOps, cybersecurity, AI engineering, data
  architecture, enterprise architecture, product strategy, or compliance and
  no software architecture context is material;
- the only need is to cite a vendor implementation detail from a specific
  platform;
- source-specific research is required because the pack is stale, insufficient,
  or outside scope;
- activation would create a new role, capability, workflow, gate, or mandatory
  artifact.

Do not activate merely because a source mentions microservices, cloud, system,
platform, API, service, module, or architecture.

## Questions This Pack Can Answer

This pack can help answer:

- Is this an architectural decision or a local implementation choice?
- Which stakeholders, concerns, drivers, and constraints shape this decision?
- Which requirements are architecturally significant?
- Which quality attributes dominate, and how can they be expressed as
  scenarios?
- Which architecture styles fit the drivers, and which styles are poor fits?
- Which patterns may address the problem, and what tradeoffs do they introduce?
- Which system, module, service, data, API, deployment, team, or runtime
  boundaries should exist?
- How should coupling be evaluated beyond source-code dependencies?
- What evidence supports an architecture recommendation?
- Which risks, assumptions, sensitivity points, and future-change triggers
  should be examined?
- What should an architect ask first before recommending a design?
- When is a microservice recommendation premature?
- When is a modular monolith or N-tier design sufficient?
- When does event-driven architecture fit, and what hidden risks follow?
- What should be captured in an architecture decision record?

This pack cannot answer:

- which exact technology, cloud service, database, library, or framework must
  be used without task-specific research;
- whether code/config changes are safe without Engineering Review evidence;
- whether a security-sensitive design is safe without cybersecurity-specific
  evidence;
- whether regulated, safety-critical, medical, financial, or legal architecture
  claims are acceptable without domain-specific sources;
- whether Project Lead should accept a release.

## Domain Boundary

In scope:

- architecture significance;
- architecture descriptions, views, viewpoints, diagrams, and decision records;
- stakeholders, concerns, drivers, constraints, and architecturally significant
  requirements;
- quality attributes and quality-attribute scenarios;
- architectural styles, patterns, tradeoffs, and risks;
- boundaries, coupling, modularity, data ownership, service ownership,
  communication modes, deployment units, and operational implications;
- architecture recommendation evidence and confidence limits.

Out of scope:

- implementation-level code review;
- DevSecOps as delivery, automation, platform, and secure operations domain;
- cybersecurity threat modeling or control selection as a full domain;
- AI engineering, model evaluation, prompt/data architecture, or agent-system
  architecture as a full domain;
- data architecture as a full domain;
- enterprise architecture governance and portfolio management;
- legal, regulatory, safety-critical, medical, financial, or compliance
  architecture obligations without task-specific sources;
- cloud-provider service selection beyond architecture-quality framing.

Adjacent domains:

- Architecture Review: use this pack for domain context; review moves remain
  owned by `kb/architecture_review.md`.
- Engineering Review: use this pack when implementation work has architecture
  significance; change safety remains owned by `kb/engineering_review.md`.
- DevSecOps Domain Pack: use or research separately for CI/CD, platform,
  infrastructure automation, environment management, and secure operations.
- Cybersecurity Domain Pack: use or research separately for threats, controls,
  vulnerabilities, incident risk, identity, cryptography, or abuse cases.
- AI Engineering Domain Pack: use or research separately for model, evaluation,
  data, prompt, retrieval, agent, or AI reliability concerns.

Overloaded terms:

- `architecture`: in this pack, high-impact structure and design rationale of
  a software-intensive system, not presentation layout or generic organization.
- `service`: can mean business service, software service, cloud service, or OO
  service object. Clarify before using it as a boundary.
- `component`: can mean C4 component, deployable component, code module, or
  runtime process. Clarify abstraction level.
- `container`: in C4, an application or data store boundary; not necessarily a
  Docker container.
- `domain`: can mean business domain, technical domain, DDD bounded context, or
  knowledge-pack domain.
- `quality`: can mean product quality, architecture quality, review quality, or
  editorial quality. Name the quality attribute.
- `coupling`: can be code, semantic, data, runtime, deployment, operational,
  temporal, or organizational coupling.

## Domain Vocabulary

| Term | Meaning in this pack | Notes |
| --- | --- | --- |
| Architecture decision | A significant design choice whose rationale and consequences affect system structure, quality, dependencies, interfaces, construction, deployment, operations, or future evolution. | ADR sources and Nygard support this decision-rationale framing. |
| Architecturally significant requirement | A requirement, constraint, quality, or scenario that measurably shapes architecture. | Often includes both functional and quality requirements. |
| Driver | A force that causes architecture to take a particular shape: mission, business goal, user need, quality attribute, constraint, risk, integration, team, lifecycle, or platform. | Strong architecture starts from drivers, not diagrams. |
| Stakeholder concern | Something an affected stakeholder needs the architecture to address. | ISO 42010 and arc42 emphasize stakeholder concerns. |
| View | A representation of architecture from a perspective. | C4, arc42, and ISO 42010 all support multi-view thinking. |
| Viewpoint | The conventions and concerns for a view. | Use to avoid one diagram pretending to answer every concern. |
| Quality attribute | A property used to judge fitness, such as reliability, security, performance, modifiability, maintainability, operability, scalability, cost, or sustainability. | Express as scenario when material. |
| Quality-attribute scenario | A concrete stimulus/context/response/evidence expression of a quality need. | Supported by SEI QAW and arc42. |
| Architecture style | A family of architectures with characteristic constraints on elements and relationships. | Examples: microservices, event-driven, N-tier. |
| Architecture pattern | A reusable solution to a recurring architecture problem with tradeoffs. | Examples: circuit breaker, saga, strangler fig, anti-corruption layer. |
| Boundary | A separation line around responsibilities, data, runtime, ownership, deployment, language/model, or change cadence. | Boundaries should be explicit and evidence-backed. |
| Coupling | Degree and type of dependency between parts. | Evaluate more than imports or function calls. |
| Cohesion | How strongly responsibilities within a unit belong together. | Weak cohesion often signals wrong boundary. |
| Tradeoff | A design choice that improves some qualities while worsening or risking others. | Architecture recommendations should name tradeoffs. |
| Sensitivity point | A design decision where a small change may strongly affect a quality attribute. | ATAM vocabulary; use with source caution. |
| Risk theme | A recurring or clustered risk pattern across scenarios or decisions. | Useful for review and governance. |
| ADR | Architecture Decision Record: a short record of a significant decision, its context, status, and consequences. | Use when rationale matters later. |
| Bounded context | A domain boundary where a model/language is internally coherent and explicit relationships to other contexts are needed. | DDD-focused; not identical to service boundary. |

## Architectural Principles

These principles are guidance, not policy. Use only when the task is
architecture-sensitive and evidence supports the claim.

### Start With Drivers

Source basis: SEI QAW, arc42, AWS/Google/Azure Well-Architected guidance.

Ask what outcome, stakeholder concern, quality attribute, constraint, risk, and
future change make the architecture matter before selecting a style or pattern.

### Architecture Is Tradeoff Management

Source basis: SEI ATAM, AWS Well-Architected, Microsoft architecture styles and
patterns.

A recommendation that names only benefits is not an architecture
recommendation. It should name costs, risks, degraded qualities, assumptions,
and evidence that would change the decision.

### Make Quality Attributes Concrete

Source basis: SEI QAW, ISO/IEC 25010, arc42, cloud well-architected pillars.

Convert vague qualities into scenarios:

```markdown
- quality attribute:
- stimulus or change:
- affected part:
- expected response:
- response evidence or measure:
```

### Boundaries Are Design Commitments

Source basis: C4, Fowler/Lewis microservices, Fowler bounded context,
Microsoft architecture styles.

Module, service, data, team, deployment, runtime, and model boundaries are not
interchangeable. A good boundary usually aligns several forces; a weak boundary
optimizes one and ignores the others.

### Prefer Reversible Simplicity Until Drivers Demand Complexity

Source basis: Fowler "Monolith First", Microsoft style guidance, arc42 lean
documentation.

Distributed designs can improve independent deployment and scaling, but they
also add operational, consistency, observability, and coordination costs. Do
not pay that premium without drivers.

### Document Rationale Proportionally

Source basis: ISO 42010, C4, arc42, Nygard ADR, AWS ADR.

Architecture evidence should be useful to future maintainers and reviewers.
Use diagrams, ADRs, or written descriptions when they help answer stakeholder
concerns, not to produce performative completeness.

## Architectural Drivers

Use these driver classes when framing an architecture-sensitive task.

| Driver class | First questions | Evidence to seek |
| --- | --- | --- |
| Mission/business | What outcome must the system enable? What fails if the architecture is wrong? | Business goal, user journey, service level, cost/risk framing |
| Stakeholders | Who builds, uses, operates, pays for, audits, reviews, or is harmed by the system? | Stakeholder map, concern list, ownership notes |
| Functional shape | Which core capabilities must the system provide? Which functions cross boundaries? | Use cases, domain model, workflows |
| Quality attributes | Which qualities dominate and conflict? | Quality scenarios and priority |
| Constraints | What cannot change? | Platform, team, budget, time, legal, data, compatibility, governance constraints |
| Change profile | Which parts change often or independently? | Release cadence, roadmap volatility, ownership model |
| Data | Who owns data? What consistency, privacy, retention, migration, and reporting constraints exist? | Data lifecycle, schema ownership, consistency needs |
| Integration | Which external systems, APIs, protocols, or contracts shape the design? | Interface inventory, contract stability, failure modes |
| Operations | Who runs it? What observability, incident, deployment, scaling, and recovery maturity exists? | SLOs, runbooks, monitoring, CI/CD maturity |
| Risk | Which failure is expensive, unsafe, confusing, or hard to reverse? | Risk scenarios, impact, mitigations, residual risk |

## Quality Attributes

Quality attributes should be prioritized, made concrete, and tied to evidence.

Common architecture-relevant attributes:

- reliability and availability;
- security and privacy;
- performance and latency;
- scalability and elasticity;
- modifiability and maintainability;
- deployability and operability;
- observability and diagnosability;
- interoperability and compatibility;
- data consistency and integrity;
- cost efficiency;
- sustainability;
- usability/interaction impact when architecture affects user experience;
- auditability and traceability when governance matters.

Use ISO/IEC 25010 as a quality-model reference, but do not treat it as the only
possible attribute list. Use cloud-provider pillars when the workload is cloud
or platform-oriented. Use task-specific sources for regulated or
safety-critical domains.

Quality scenario prompt:

```markdown
- Attribute:
- Stakeholder:
- Stimulus:
- Environment/context:
- Artifact or system part affected:
- Expected response:
- Response measure or review evidence:
- Tradeoff:
- Confidence/source:
```

Warning signs:

- quality attribute appears only as an adjective;
- no stakeholder is named;
- no stimulus or expected response is visible;
- no tradeoff is acknowledged;
- evidence is a preference or trend rather than source/task context.

## Architectural Styles

Styles are constraint families. Choose them by driver fit.

### Modular Monolith

Source basis: Fowler "Monolith First", C4/arc42 boundary documentation,
Microsoft N-tier/layering guidance.

Consider when:

- domain boundaries are still being discovered;
- one deployable unit is acceptable;
- local transactions, simple debugging, and low operational overhead matter;
- team size and operational maturity do not justify distributed services;
- future extraction is possible if internal boundaries stay explicit.

Risks:

- weak module boundaries decay into a big ball of mud;
- shared database becomes the integration mechanism;
- all changes deploy together even when parts need different cadence;
- hidden coupling prevents later extraction.

Architect questions:

- Which modules represent business capabilities or coherent domains?
- How are module boundaries enforced?
- Which dependencies are forbidden?
- What evidence would justify extracting a module into a separate service?

### Layered / N-Tier

Source basis: Azure Architecture Styles.

Consider when:

- the domain is stable and conventional;
- the organization benefits from clear horizontal responsibilities;
- the task is migration of an existing layered application;
- simplicity and familiarity dominate over independent service deployment.

Risks:

- changes cut through many layers;
- business logic spreads across layers;
- data tier becomes the real coupling point;
- layer names exist but dependency constraints are not enforced.

### Microservices

Source basis: Fowler/Lewis microservices and Azure Architecture Styles.

Consider when:

- the domain is complex and boundaries are reasonably understood;
- services can align with business capabilities or bounded contexts;
- independent deployment, scaling, and team ownership materially matter;
- operations can support observability, service discovery, incident response,
  CI/CD, and distributed reliability;
- data ownership can be decentralized with acceptable consistency tradeoffs.

Risks:

- premature decomposition before boundaries stabilize;
- network latency, failure, and interservice communication overhead;
- distributed data consistency and reporting complexity;
- duplicated platform work and operational burden;
- synchronous call chains that turn services into a distributed monolith.

Architect questions:

- What business capability does each service own?
- What data does each service own exclusively?
- Which calls are synchronous, asynchronous, or avoided?
- What happens when a dependency is slow, unavailable, or returns stale data?
- What is the minimum operational maturity required?

### Event-Driven Architecture

Source basis: Azure Architecture Styles and Cloud Design Patterns.

Consider when:

- producers and consumers should evolve independently;
- asynchronous fan-out, buffering, real-time reaction, or event replay matters;
- consumers need to react to business facts without direct producer knowledge;
- loose runtime coupling is worth eventual consistency.

Risks:

- event ordering and delivery guarantees are unclear;
- consumers are not idempotent;
- duplicate messages and replay behavior are unhandled;
- event schema evolution creates hidden coupling;
- observability across asynchronous flows is weak.

Architect questions:

- What is an event: fact, command, notification, or data snapshot?
- Who owns event schema and compatibility?
- Are consumers idempotent?
- What are ordering, retry, dead-letter, replay, and retention rules?
- How will traces connect producer, broker, and consumers?

### Web-Queue-Worker

Source basis: Azure Architecture Styles and Cloud Design Patterns.

Consider when:

- a web-facing path and background work scale differently;
- long-running or resource-heavy work should be asynchronous;
- queue buffering improves reliability and user responsiveness;
- the domain is relatively simple.

Risks:

- background and foreground components each grow into large monoliths;
- user feedback and consistency expectations are unclear;
- retries create duplicate work;
- queue depth hides downstream failure.

## Architectural Patterns

Patterns solve recurring problems but introduce tradeoffs. Choose by problem,
constraint, or risk, not by technology preference.

Pattern examples from maintained cloud architecture guidance:

| Pattern | Use when | Key tradeoff |
| --- | --- | --- |
| Anti-corruption layer | A new model must integrate with a legacy or external model. | Extra translation layer and maintenance cost. |
| Backends for Frontends | Different clients need different backend experiences. | Duplicated backend logic risk. |
| Bulkhead | Failures should be isolated between resource pools or workloads. | More partitioning and capacity planning complexity. |
| Cache-aside | Reads can benefit from caching. | Staleness and invalidation complexity. |
| Circuit breaker | A dependency may fail or become slow. | Requires fallback behavior and threshold tuning. |
| CQRS | Reads and writes have different models, scale, or consistency needs. | More models, eventual consistency, and operational complexity. |
| Event sourcing | State history must be reconstructed from events. | Event schema evolution and query complexity. |
| Gateway routing/aggregation/offloading | A single entry point should route, combine, or offload cross-cutting behavior. | Gateway can become bottleneck or central coupling point. |
| Queue-based load leveling | Producers and consumers have bursty or mismatched load. | Latency and queue management. |
| Retry | Transient failures are expected. | Can amplify load without backoff and circuit breaking. |
| Saga / compensating transaction | Distributed work needs consistency without a single transaction. | Compensation logic and partial failure complexity. |
| Strangler fig | Legacy replacement should be incremental. | Transitional routing and coexistence complexity. |

Documentation and decision patterns:

- C4 diagrams: use when stakeholders need maps at system context, container,
  component, code, dynamic, or deployment levels.
- arc42 structure: use as a reference for compact or thorough architecture
  documentation when drivers, constraints, context, decisions, qualities, and
  risks need to be organized.
- ADRs: use when a significant decision's context, decision, status, and
  consequences must remain understandable later.

No pattern is mandatory merely because this pack mentions it.

## Boundary And Coupling Evaluation

Evaluate boundaries across several dimensions:

| Dimension | Questions |
| --- | --- |
| Business capability | Does the unit own a coherent business responsibility? |
| Domain language | Does the same term mean the same thing inside the boundary? |
| Data ownership | Who writes, reads, migrates, retains, and protects the data? |
| API contract | Is the interface explicit, stable enough, versioned, and observable? |
| Runtime communication | Is communication synchronous, asynchronous, batch, streaming, or local? |
| Deployment | Can this unit be built, tested, deployed, scaled, and rolled back independently if needed? |
| Team ownership | Does one team own outcomes and operations for the boundary? |
| Change cadence | Do parts inside the boundary change together? |
| Failure isolation | Can failure be contained without cascading? |
| Governance | Which canonical owner, compliance rule, or review owner is affected? |

Coupling types to inspect:

- code dependency;
- semantic coupling through shared terms and models;
- data coupling through shared databases or schemas;
- temporal coupling through synchronous request chains;
- deployment coupling through shared release units;
- operational coupling through shared monitoring, queues, secrets, or runtime;
- organizational coupling through cross-team coordination;
- governance coupling through shared canonical owners or review responsibility.

Architectural concern rises when multiple coupling types point in different
directions, for example separate services sharing one database or one module
owned by several teams with incompatible change cadences.

## Trade-off Thinking

Use this compact pattern for architecture-sensitive recommendations:

```markdown
## architecture tradeoff
- Decision or recommendation:
- Drivers:
- Quality attributes improved:
- Quality attributes weakened or at risk:
- Alternatives considered:
- Why selected:
- Why rejected alternatives were not selected:
- Assumptions:
- Sensitivity points:
- Risks and mitigations:
- Evidence:
- Revisit trigger:
```

Common tradeoffs:

- simplicity vs independent deployment;
- consistency vs availability/latency;
- performance vs modifiability;
- security isolation vs usability/operability;
- autonomy vs duplication;
- local transactionality vs distributed scalability;
- standardization vs team autonomy;
- cost efficiency vs resilience headroom;
- time-to-market vs future evolvability;
- detailed documentation vs maintenance burden.

Strong recommendation language:

- "Given these drivers..."
- "This improves..."
- "This worsens or risks..."
- "This assumes..."
- "Revisit if..."

Weak recommendation language:

- "Best practice says..."
- "Modern architecture uses..."
- "This is scalable" without scenario.
- "Microservices will solve..." without boundary/operations evidence.

## Evidence Rules

Claims this pack can support:

- general software architecture reasoning about drivers, concerns, views,
  quality attributes, styles, patterns, boundaries, tradeoffs, decision
  records, and architecture-risk review;
- cautious style-fit heuristics for modular monolith, N-tier, microservices,
  event-driven architecture, and Web-Queue-Worker;
- pattern tradeoff prompts from maintained cloud design pattern catalogs;
- documentation and diagramming guidance from C4, arc42, ISO 42010, and ADR
  sources.

Claims this pack cannot support by itself:

- precise vendor service selection;
- benchmark, capacity, reliability, availability, or cost claims;
- security-control sufficiency;
- compliance or legal claims;
- safety-critical design sufficiency;
- AI/model/data-engineering architecture sufficiency;
- exact ATAM procedural compliance without direct source review.

Evidence expectations:

- High-governance architecture recommendation: source register, drivers,
  quality scenarios, alternatives, tradeoffs, risks, and confidence limits.
- Standard architecture advice: source-backed principles, task-specific
  assumptions, and visible caveats.
- Low-risk explanation: pack source references and caveats may be enough.

Confidence labels:

- High: supported by ISO/IEEE standard abstracts, SEI report abstracts, or
  maintained official cloud/provider documentation for general concepts.
- Medium: supported by recognized practitioner sources or provider-specific
  guidance generalized cautiously.
- Limited: exact method steps, technology selection, regulated-domain claims,
  or current vendor-specific facts not checked in task-specific sources.

## Risk Checklist

Use inside existing planning, research, writing, review, or governance
artifacts when architecture risk is material.

- Architectural decision is unclear.
- Drivers are missing or solution-first.
- Stakeholder concerns are not identified.
- Quality attributes are vague, unprioritized, or unmeasured.
- Style is selected by trend, preference, or vendor default.
- Tradeoffs and rejected alternatives are hidden.
- Boundaries confuse module, service, data, deployment, team, and domain model.
- Coupling is assessed only as code dependency.
- Data ownership, consistency, retention, or migration risk is unresolved.
- Synchronous dependencies create cascading failure risk.
- Asynchronous events lack ordering, idempotency, retry, replay, and schema
  rules.
- Microservices are proposed without operational maturity.
- Monolith is proposed without module-boundary enforcement.
- Event-driven design is proposed without observability.
- Cloud framework guidance is treated as universal law.
- Diagrams omit scope, notation, relationships, responsibilities, or
  abstraction level.
- ADRs or rationale are missing for high-impact decisions.
- Review cannot reconstruct evidence or confidence.
- Pack guidance is being treated as policy or review verdict.

## Review Questions

Review Agent may use these questions inside the existing review gate when this
pack is active:

- Was pack activation justified by material architecture context?
- Is the architecture decision or recommendation clearly named?
- Are drivers and constraints visible before the selected solution?
- Are stakeholder concerns identified at the necessary depth?
- Are quality attributes concrete enough to review?
- Are scenarios or evidence provided for material quality claims?
- Are credible alternatives considered without strawman rejection?
- Are tradeoffs, assumptions, and residual risks explicit?
- Is the style or pattern fit explained by drivers?
- Are boundaries described across business, data, API, runtime, deployment,
  team, and governance dimensions where material?
- Is coupling evaluated beyond code dependencies?
- Are cloud-provider sources kept within their scope?
- Does the work preserve Architecture Review and Engineering Review ownership?
- Are stale-if triggers, source limits, and confidence notes visible when
  material?
- Does the artifact avoid creating roles, pipelines, gates, policies, or
  mandatory artifacts?

## Common Mistakes

- Starting with "microservices vs monolith" before drivers.
- Treating "scalable" or "secure" as self-evident.
- Assuming service boundary equals domain boundary.
- Assuming bounded context equals deployable service.
- Treating event-driven architecture as automatically decoupled while event
  schemas and shared meanings create coupling.
- Ignoring operational maturity when recommending distributed systems.
- Treating database separation as optional in microservices while claiming
  service autonomy.
- Using cloud well-architected pillars as a checklist detached from workload
  context.
- Creating diagrams that mix abstraction levels.
- Recording decisions without consequences.
- Recording consequences without revisit triggers.
- Treating a pattern catalog as a menu rather than a problem/constraint match.
- Confusing Architecture Review with Engineering Review.
- Letting this pack act as a review verdict.

## Source Register

| Source | Class | Version/date | Last checked | Supports | Confidence limits |
| --- | --- | --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 (`https://www.iso.org/standard/74393.html`, `https://standards.ieee.org/ieee/42010/6846/`) | International standard | 2022-11 | 2026-07-10 | Architecture descriptions, viewpoints, model kinds, architecture vs description distinction | Public abstract only |
| ISO/IEC 25010:2023 (`https://www.iso.org/standard/78176.html`) | International standard | 2023-11 | 2026-07-10 | Product quality model and quality characteristics as reference model | Public abstract only |
| SEI QAW Third Edition (`https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/`) | SEI report | 2003-10-01 | 2026-07-10 | Stakeholder discovery and prioritization of driving quality attributes | Foundational but older |
| SEI ATAM report (`https://resources.sei.cmu.edu/asset_files/TechnicalReport/2000_005_001_13706.pdf`) | SEI report | 2000 | 2026-07-10 | Scenario-driven tradeoff/risk evaluation method pointer | Direct PDF extraction unavailable; avoid precise step claims |
| AWS Well-Architected Framework (`https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`) | Maintained cloud framework | 2024-11-06 | 2026-07-10 | Pros/cons of decisions, constructive review, cloud quality pillars | AWS-specific |
| Google Cloud Well-Architected Framework (`https://docs.cloud.google.com/architecture/framework`) | Maintained cloud framework | Last reviewed 2026-01-28 | 2026-07-10 | Secure, efficient, resilient, high-performing, cost-effective, sustainable design; pillars and perspectives | Google Cloud-specific |
| Azure Well-Architected Framework (`https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework`) | Maintained cloud framework | Current page | 2026-07-10 | Reliability, security, cost, operational excellence, performance pillars | Azure-specific |
| Azure Application Architecture Fundamentals (`https://learn.microsoft.com/en-us/azure/architecture/guide/`) | Maintained architecture guidance | Last updated 2026-01-30 | 2026-07-10 | Tradeoffs, style choice, technology choice, reference architecture review | Azure-specific examples |
| Azure Architecture Styles (`https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/`) | Maintained style guidance | Last updated 2025-10-14 | 2026-07-10 | Style constraints and tradeoffs; N-tier, Web-Queue-Worker, microservices, event-driven | Cloud framing |
| Azure Cloud Design Patterns (`https://learn.microsoft.com/en-us/azure/architecture/patterns/`) | Maintained pattern catalog | Last updated 2026-06-03 | 2026-07-10 | Pattern selection by problem/constraint/risk and pattern tradeoffs | Cloud/distributed-system focus |
| C4 Model official site (`https://c4model.com/`, `https://c4model.com/introduction`) | Practitioner-authored official method site | Current site | 2026-07-10 | System/context/container/component/code abstractions and diagram communication | Visualization method, not decision method |
| arc42 docs (`https://docs.arc42.org/home/`, `https://docs.arc42.org/section-1/`) | Practitioner-maintained documentation guidance | Current docs | 2026-07-10 | Drivers, constraints, context, decisions, quality scenarios, risks, lean/thorough docs | Documentation template, not mandatory artifact set |
| ADR GitHub organization (`https://adr.github.io/`) | ADR knowledge hub | Current site | 2026-07-10 | ADR vocabulary and decision log concept | Aggregator |
| Nygard, "Documenting Architecture Decisions" (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`) | Practitioner article | 2011-11-15 | 2026-07-10 | Significant decision test; context/decision/status/consequences | Practitioner source |
| AWS ADR Prescriptive Guidance (`https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html`, `https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html`) | Maintained guidance | 2022-03 | 2026-07-10 | ADR anti-patterns, process, decision log, supersession | Prescriptive guidance, not AI Editorial Office process |
| Fowler/Lewis, "Microservices" (`https://www.martinfowler.com/articles/microservices.html`) | Practitioner article | 2014-03-25 | 2026-07-10 | Microservice characteristics and tradeoffs | Descriptive, not formal definition |
| Fowler, "Monolith First" (`https://martinfowler.com/bliki/MonolithFirst.html`) | Practitioner article | 2015-06-03 | 2026-07-10 | Microservice premium and monolith-first caution | Practitioner view |
| Fowler, "Bounded Context" (`https://martinfowler.com/bliki/BoundedContext.html`) | Practitioner article | 2014-01-15 | 2026-07-10 | Domain model/language boundaries and context maps | DDD-focused |

## Confidence Notes

- High confidence: general framing that architecture work should expose
  stakeholders, concerns, drivers, quality attributes, views, tradeoffs,
  decisions, and rationale.
- High confidence: activation should be material and bounded because this is
  required by `kb/domain_knowledge_pack_standard.md`.
- Medium confidence: style-fit guidance for modular monolith, microservices,
  event-driven, N-tier, and Web-Queue-Worker. These are durable heuristics, but
  actual fit depends on local context.
- Medium confidence: pattern list and tradeoff prompts from Microsoft cloud
  patterns. They are useful beyond Azure, but examples are cloud-oriented.
- Limited confidence: exact ATAM procedure claims. This pack uses ATAM only as
  a recognized tradeoff/risk evaluation reference unless the source is checked
  directly in a future task.
- Limited confidence: any current vendor-service recommendation. Use
  task-specific research.

## Update Rules

Update this pack when:

- a source in the register changes materially, is withdrawn, or is superseded;
- a new accepted Domain Knowledge Pack Standard requirement applies;
- repeated tasks show a missing activation boundary, vocabulary item, risk,
  source, style, pattern, or review question;
- Review Agent finds unsupported, misleading, stale, or over-broad guidance;
- Project Lead accepts a source-backed improvement;
- a related future pack changes adjacent-domain boundaries.

For small updates, change this pack and record the source/date in the source
register or confidence notes. For high-governance, disputed, or source-heavy
updates, use a reviewed system task or release.

## Retirement Rules

Deprecate or retire this pack when:

- software architecture domain context is no longer used by AI Editorial
  Office;
- source support becomes stale or too weak to maintain confidence;
- the pack repeatedly causes role, capability, policy, lifecycle, or review
  confusion;
- another accepted pack or canonical owner supersedes it;
- maintenance cost exceeds future value;
- Project Lead accepts a replacement pack.

Retirement must preserve enough context for future readers to know why the
pack should no longer be used. Do not delete historical task artifacts merely
to clean the narrative.

## Relation To Existing Canon

Capabilities supported:

- Architecture Review;
- Engineering Review when architecture significance is material;
- Professional Analysis;
- Professional Communication;
- Evidence Confidence Assessment;
- Knowledge Evolution.

Canonical owners not overridden:

- `AGENTS.md` for governance, role separation, review gate, artifact
  minimalism, and canonical ownership map;
- `kb/domain_knowledge_pack_standard.md` for pack purpose, activation,
  structure, source/evidence requirements, review, update, and retirement;
- `kb/architecture_review.md` for Architecture Review moves;
- `kb/engineering_review.md` for Engineering Review moves;
- `kb/editorial_evidence_framework.md` for evidence classes and confidence;
- `kb/editorial_learning_framework.md` for Knowledge Evolution;
- `pipelines/*.md` for task-type workflow overlays;
- `agents/*.md` for role behavior.

`/about` disposition:

- `/about` may mention this pack as a memory aid after S4.R2 synchronization.
- `/about` is not canonical and must not be treated as pack storage.
