# Software Architecture Pack Landscape

Status: research complete for S4.R2 release synthesis.

Date: 2026-07-10

Research role: `research_agent`

## Research Question

What durable, source-backed software architecture knowledge should AI Editorial
Office package so future architecture-sensitive tasks can reason about
decisions, drivers, quality attributes, tradeoffs, styles, boundaries,
coupling, risks, evidence, and first questions without creating a new role,
capability, pipeline, or policy owner?

## Source Selection

The research prioritized sources that are primary, standards-based,
institutional, or maintained by recognized architecture practitioners:

- architecture-description standards and quality models;
- SEI architecture-evaluation and quality-attribute material;
- cloud provider well-architected frameworks;
- widely used architecture documentation approaches;
- recognized architecture practitioner guidance for ADRs, C4, arc42,
  microservices, monolith-first, and bounded contexts.

Low-quality blogspam, generic listicles, unsourced pattern catalogs, and
vendor-specific implementation pages were excluded unless they provided a
maintained reference architecture or framework boundary.

## Executive Findings

Software architecture practice is not a collection of preferred styles. It is a
discipline for making and communicating high-impact design decisions under
drivers, constraints, stakeholder concerns, quality attributes, uncertainty,
and tradeoffs.

The pack should emphasize:

- whether a decision is architecturally significant;
- drivers and constraints before solution shape;
- quality-attribute scenarios instead of vague "ilities";
- explicit tradeoffs and accepted risks;
- boundaries, ownership, coupling, data, and runtime communication;
- evidence proportional to reversibility and blast radius;
- style/pattern fit by problem, not trend;
- decision records and architecture descriptions as communication aids;
- review questions that help existing roles challenge architecture claims.

The pack should not create an architect role, architecture-review gate,
architecture pipeline, framework, methodology, or mandatory architecture
artifact set. Existing Architecture Review and Engineering Review already own
review moves and change-safety lenses. The pack should supply source-backed
domain context consumed by those capabilities.

## Source Register

| Source | Class | Version/date | Last checked | Relevance | Confidence limits |
| --- | --- | --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022, "Software, systems and enterprise - Architecture description" (`https://www.iso.org/standard/74393.html`, `https://standards.ieee.org/ieee/42010/6846/`) | International standard | 2022-11 | 2026-07-10 | Architecture descriptions, architecture vs description distinction, viewpoints, model kinds, architecture description frameworks/languages | Public abstract only; do not infer paid-standard details beyond the abstract |
| ISO/IEC 25010:2023, "Systems and software Quality Requirements and Evaluation - Product quality model" (`https://www.iso.org/standard/78176.html`) | International standard | 2023-11 | 2026-07-10 | Quality model as reference for specifying and evaluating product quality | Public abstract only; pack uses broad quality-model concept, not full standard text |
| SEI, "Quality Attribute Workshops (QAWs), Third Edition" (`https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/`) | SEI technical report | 2003-10-01 | 2026-07-10 | Stakeholder workshop for early discovery and prioritization of driving quality attributes; complements ATAM | Older source but foundational; use as durable method pattern, not current tool mandate |
| SEI, "ATAM: Method for Architecture Evaluation" (`https://resources.sei.cmu.edu/asset_files/TechnicalReport/2000_005_001_13706.pdf`) | SEI technical report | 2000 | 2026-07-10 | Scenario-based architecture evaluation, tradeoffs, sensitivity points, risks, and risk themes | Direct PDF extraction was not available in this session; use as authoritative method pointer, not as precise step-by-step quotation source |
| AWS Well-Architected Framework (`https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`) | Maintained cloud architecture framework | Publication date 2024-11-06 | 2026-07-10 | Pros/cons of architecture decisions, constructive review, best-practice questions, cloud quality pillars | AWS-specific; generalize only at quality/tradeoff level |
| Google Cloud Well-Architected Framework (`https://docs.cloud.google.com/architecture/framework`) | Maintained cloud architecture framework | Last reviewed 2026-01-28 | 2026-07-10 | Secure, resilient, high-performing, cost-effective, sustainable cloud design; pillars and cross-pillar perspectives | Google Cloud-specific; useful for cross-pillar reasoning and freshness model |
| Azure Well-Architected Framework (`https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework`) | Maintained cloud architecture framework | Current Microsoft Learn page | 2026-07-10 | Five pillars: reliability, security, cost optimization, operational excellence, performance efficiency | Azure-specific; does not cover non-cloud architecture alone |
| Azure Architecture Center, Application Architecture Fundamentals (`https://learn.microsoft.com/en-us/azure/architecture/guide/`) | Maintained architecture guidance | Last updated 2026-01-30 | 2026-07-10 | Tradeoffs between pillars, architecture styles, workloads, best practices, technology choices, reference architecture review | Azure-specific examples; style reasoning is broadly useful |
| Azure Architecture Styles (`https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/`) | Maintained architecture style guidance | Last updated 2025-10-14 | 2026-07-10 | Styles as constraints; N-tier, Web-Queue-Worker, microservices, event-driven; complexity and tradeoffs | Cloud framing; still useful for style-fit heuristics |
| Azure Cloud Design Patterns (`https://learn.microsoft.com/en-us/azure/architecture/patterns/`) | Maintained pattern catalog | Last updated 2026-06-03 | 2026-07-10 | Pattern selection by problem/constraint/risk; distributed-system fallacies; tradeoffs | Pattern catalog is broad and cloud-oriented; use as examples, not exhaustive doctrine |
| C4 Model official site (`https://c4model.com/`, `https://c4model.com/introduction`) | Practitioner-authored architecture visualization model | Current official website | 2026-07-10 | System/context/container/component/code abstractions, diagrams for communication, diagram-quality problems | Visualization/documentation method, not architecture decision method |
| arc42 documentation (`https://docs.arc42.org/home/`, `https://docs.arc42.org/section-1/`) | Practitioner-maintained architecture documentation template/guidance | Current docs | 2026-07-10 | Drivers, constraints, context, solution strategy, decisions, quality scenarios, risks, glossary; lean vs thorough documentation | Documentation template, not mandatory artifact set |
| ADR GitHub organization (`https://adr.github.io/`) | ADR knowledge hub | Current site | 2026-07-10 | ADR definition, decision log, architectural decision vocabulary | Aggregator; pair with Nygard and AWS for stronger support |
| Michael Nygard, "Documenting Architecture Decisions" (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`) | Original practitioner ADR article | 2011-11-15 | 2026-07-10 | Lightweight records for significant decisions affecting structure, qualities, dependencies, interfaces, construction; context/decision/status/consequences | Practitioner article; durable but not a formal standard |
| AWS Prescriptive Guidance, ADR process (`https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html`, `https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html`) | Maintained prescriptive guidance | 2022-03 | 2026-07-10 | ADR anti-patterns, ADR process, decision log, immutable accepted ADRs and supersession | Prescriptive team guidance; adapt, do not make mandatory |
| Martin Fowler and James Lewis, "Microservices" (`https://www.martinfowler.com/articles/microservices.html`) | Recognized practitioner article | 2014-03-25 | 2026-07-10 | Microservices characteristics: independently deployable services, business capability, decentralized governance/data, infrastructure automation, failure design | Descriptive practitioner guidance; not a formal definition |
| Martin Fowler, "Monolith First" (`https://martinfowler.com/bliki/MonolithFirst.html`) | Recognized practitioner article | 2015-06-03 | 2026-07-10 | Microservice premium, boundary uncertainty, monolith-first strategy for many new systems | Practitioner view; useful as caution, not universal rule |
| Martin Fowler, "Bounded Context" (`https://martinfowler.com/bliki/BoundedContext.html`) | Recognized practitioner article | 2014-01-15 | 2026-07-10 | Domain boundaries, multiple models, language/context boundaries, context maps | DDD-focused; not every architecture task is DDD |

## What The Sources Agree On

### Architecture Is About Significant Decisions

ISO/IEC/IEEE 42010 distinguishes an architecture from an architecture
description and frames architecture descriptions around concerns, viewpoints,
model kinds, and communication. ADR sources frame architectural decisions as
significant choices whose rationale and consequences matter to future
stakeholders. Nygard gives a practical significance test: structure,
non-functional characteristics, dependencies, interfaces, and construction
techniques.

Implication for the pack: include a practical "is this architectural?" test
based on impact, reversibility, quality attributes, boundaries, interfaces,
dependencies, data ownership, operational model, and future constraint.

### Drivers Come Before Style

SEI QAW, arc42, cloud well-architected frameworks, and Microsoft architecture
style guidance all start from goals, stakeholders, requirements, constraints,
qualities, and tradeoffs before style selection. A style such as microservices,
N-tier, Web-Queue-Worker, or event-driven architecture is a constraint bundle
chosen because it fits drivers, not because it is modern.

Implication for the pack: the first architect questions should ask about
mission/business goal, users, stakeholders, constraints, quality attributes,
change profile, data boundaries, operations maturity, and risk.

### Quality Attributes Need Scenarios

SEI QAW and arc42 both push quality attributes toward concrete scenarios.
ISO/IEC 25010 supplies a formal quality-model reference. Cloud well-architected
frameworks organize architecture review around quality pillars such as
security, reliability, operational excellence, performance, cost, and
sustainability. These sources converge on the idea that vague labels such as
"scalable", "secure", or "maintainable" are insufficient without context and
evidence.

Implication for the pack: include quality-attribute prompts and require
stimulus/context/response/evidence framing before recommending architecture.

### Tradeoffs Are Central

AWS states the framework helps understand pros and cons of decisions and treats
review as a constructive conversation rather than an audit mechanism. Microsoft
style and pattern guidance explicitly warns that styles and patterns have
constraints, benefits, challenges, and strategic tradeoffs. SEI ATAM is
foundational for tradeoff/risk analysis.

Implication for the pack: strong recommendations should name what improves,
what worsens, which risks remain, and what evidence would change the decision.

### Boundaries And Coupling Drive Fitness

Fowler/Lewis emphasize services around business capabilities, independent
deployment, decentralized data, and explicit downsides of remote communication.
Fowler's bounded context guidance emphasizes that large systems often need
different coherent models with explicit interrelationships. Microsoft style
guidance treats architecture styles as constraints on elements and
relationships. C4 and arc42 both expose boundaries through context, container,
building-block, runtime, deployment, and decision views.

Implication for the pack: boundary evaluation should include business
capability cohesion, ownership, data ownership, communication mode, deployment
unit, team topology, change rate, and semantic language boundaries.

### Documentation Should Be Useful And Proportionate

ISO/IEC/IEEE 42010 covers architecture descriptions without prescribing
process, tools, or media. C4 focuses on accessible architecture diagrams and
common diagram problems. arc42 offers lean and thorough documentation modes.
ADR guidance favors small records that preserve rationale. These sources agree
that architecture documentation should help stakeholders understand and review
the architecture rather than create performative completeness.

Implication for the pack: advise evidence and documentation proportional to
risk and audience. Do not create mandatory artifacts in the pack.

## Architectural Concepts To Carry Into The Pack

| Concept | Source support | Pack consequence |
| --- | --- | --- |
| Architecture decision | ISO 42010, ADR sources, Nygard, AWS ADR | Significant design choice whose rationale and consequences matter |
| Architecturally significant requirement | ADR and architecture practice sources, SEI QAW | Requirement that measurably affects architecture shape or quality |
| Stakeholder concern | ISO 42010, arc42, SEI QAW | Architecture must answer concerns of affected stakeholders, not only developers |
| View / viewpoint | ISO 42010, C4, arc42 | Different concerns need different representations; one diagram rarely suffices |
| Quality attribute | ISO 25010, SEI QAW, cloud frameworks, arc42 | Use scenarios and evidence, not vague labels |
| Tradeoff | SEI ATAM, AWS, Microsoft style/pattern docs | Every style/pattern improves some qualities at cost to others |
| Sensitivity point | SEI ATAM | A design choice where a small change may strongly affect a quality attribute |
| Risk theme | SEI ATAM/QAW family | Repeated risks should be summarized and reviewed |
| Boundary | C4, Fowler, Microsoft styles, arc42 | Boundary choices shape coupling, ownership, data, deployment, and change |
| Coupling | ADR, microservices, patterns, styles | Evaluate semantic, runtime, data, deployment, and organizational coupling |
| Architecture style | Microsoft styles, cloud frameworks, Fowler | Constraint family; choose by driver fit |
| Architecture pattern | Microsoft patterns | Reusable solution to a recurring problem with tradeoffs |
| Decision record | Nygard, ADR GitHub, AWS ADR | Preserve context, decision, status, and consequences when the decision matters |

## Style And Pattern Landscape

### Modular Monolith

Source basis: Fowler's monolith-first caution, Microsoft N-tier style guidance,
and general boundary reasoning from C4/arc42.

Useful when:

- domain boundaries are still changing;
- team/operations maturity does not justify distributed complexity;
- one deployable unit is acceptable;
- strong internal module boundaries can preserve future extraction options;
- latency, transactionality, and local development simplicity dominate.

Watch:

- module boundaries eroding into a big ball of mud;
- shared database becoming the only integration model;
- scaling or deployment cadence forcing whole-system changes;
- internal dependencies crossing intended boundaries.

### Microservices

Source basis: Fowler/Lewis microservices article and Microsoft architecture
styles.

Useful when:

- domain is complex enough to justify service autonomy;
- business capabilities and bounded contexts are reasonably understood;
- teams need independent deployment and scaling;
- operational maturity supports observability, CI/CD, service discovery,
  distributed reliability, and incident response;
- data ownership can be decentralized without unacceptable consistency risk.

Watch:

- premature decomposition before boundaries stabilize;
- service chat and synchronous dependency chains;
- distributed data consistency surprises;
- team autonomy without platform maturity;
- using microservices as a default style rather than a response to drivers.

### Event-Driven Architecture

Source basis: Microsoft architecture styles and cloud design patterns.

Useful when:

- producers and consumers should be decoupled;
- asynchronous processing, fan-out, buffering, or event replay matters;
- real-time or near-real-time reactions are important;
- independent evolution of consumers is valuable.

Watch:

- ordering, delivery guarantees, duplicate messages, idempotency, and
  eventual consistency;
- unclear event ownership and schema evolution;
- event streams becoming hidden coupling;
- observability gaps across asynchronous flows.

### Layered / N-Tier

Source basis: Microsoft architecture styles and arc42 building block/context
views.

Useful when:

- domain is stable and conventional;
- organizational constraints favor clear horizontal responsibilities;
- migration from an existing layered application is the main driver;
- simplicity and familiar separation matter more than independent deployment.

Watch:

- cross-layer changes slowing agility;
- business capability logic spread across layers;
- data layer becoming a bottleneck or integration trap;
- layers becoming labels rather than enforceable dependency constraints.

### Web-Queue-Worker

Source basis: Microsoft architecture styles and cloud patterns.

Useful when:

- front-end request handling and background work need different scaling;
- long-running or resource-intensive tasks can run asynchronously;
- the domain is relatively simple;
- queue buffering improves reliability or throughput.

Watch:

- eventual consistency and user feedback gaps;
- worker/front-end responsibilities growing into two large monoliths;
- retry, dead-letter, and idempotency behavior left unspecified.

## Risk Themes For Pack Design

- Architecture-as-fashion: choosing microservices, event-driven architecture,
  CQRS, or serverless because they sound modern rather than because drivers
  require them.
- Vague quality attributes: "scalable", "secure", "maintainable", or
  "simple" without scenario, priority, evidence, or tradeoff.
- Missing decision rationale: future work can see what changed but not why.
- Boundary confusion: business, data, deployment, team, runtime, and code
  boundaries are treated as the same boundary.
- Coupling blindness: only code dependency is inspected while runtime calls,
  data sharing, schema evolution, operational dependencies, and semantic
  coupling remain hidden.
- Cloud framework overreach: provider well-architected guidance is treated as
  general architecture law instead of cloud/workload context.
- Diagram theater: boxes and lines look plausible but omit scope, notation,
  relationships, responsibility, or quality evidence.
- Review substitution: architecture context is treated as review outcome,
  bypassing `kb/architecture_review.md` and the existing review gate.

## Research Sufficiency Judgment

Sufficiency: enough for a release-candidate pack.

Reason:

- The source set covers architecture-description standards, quality models,
  quality-attribute elicitation, tradeoff/risk evaluation, documentation,
  decision records, architecture styles, cloud quality frameworks, visual
  communication, and key practitioner cautions.
- Sources are authoritative enough for durable domain guidance but not enough
  to create universal prescriptions for all technologies, regulated domains,
  safety-critical systems, cybersecurity, AI engineering, data platforms, or
  DevSecOps.

Confidence:

- High for general guidance: stakeholder concerns, architecture descriptions,
  quality attributes, tradeoffs, decision records, style/pattern fit by
  drivers, and documentation proportionality.
- Medium for style-specific heuristics: microservices, event-driven, modular
  monolith, N-tier, and Web-Queue-Worker because actual fit depends strongly on
  local domain, team, runtime, data, and operational context.
- Limited for exact ATAM process details because direct PDF extraction was not
  available in this session; use only ATAM's broad role as a recognized
  scenario-driven tradeoff/risk evaluation method unless the source is checked
  directly in a future update.

## Recommended Pack Shape

Create `kb/software_architecture_domain_pack.md` as a canonical candidate
domain pack with status `release candidate`.

The pack should:

- follow every required section in `kb/domain_knowledge_pack_standard.md`;
- add the user-requested "Questions This Pack Can Answer" section;
- include practical vocabulary and first questions;
- distinguish architectural decisions from implementation details;
- separate architectural principles from review authority;
- provide source-backed guidance for drivers, quality attributes, styles,
  patterns, boundaries, coupling, tradeoffs, risks, and evidence;
- explicitly subordinate itself to `AGENTS.md`,
  `kb/domain_knowledge_pack_standard.md`, `kb/architecture_review.md`, and
  `kb/engineering_review.md`;
- include stale-if, update, and retirement triggers;
- avoid mandatory artifacts and universal prescriptions.
