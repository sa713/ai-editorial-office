# Audit Areas

Each area below defines what future audits should inspect. The areas are derived
from KB domains and records, not from the current repository structure.

## Area Summary

| Area | Object of assessment | Main KB basis |
| --- | --- | --- |
| GOV | System Governance and Sociotechnical Operating Model | `glossary-intelligent-production-system`, `principle-sociotechnical-production-system`, `principle-autonomy-with-guardrails` |
| KNO | Knowledge, Memory, and Provenance | `principle-knowledge-close-to-work`, `pattern-provenance-linked-knowledge`, `application-model.md` |
| AI | AI-Agent Work System and Human-AI Control | `pattern-agent-tool-loop`, `pattern-agent-computer-interface`, `practice-ai-evaluation-harness` |
| QUA | Built-in Quality, Review, and Verification | `principle-built-in-quality`, `practice-modern-code-review`, `practice-checklists-at-pause-points` |
| DEL | Delivery Flow, Reliability, and Operations | `pattern-small-batches`, `pattern-continuous-delivery-pipeline`, `pattern-slo-error-budget`, `process-incident-management` |
| PLA | Platform Capability and Golden Paths | `pattern-platform-as-product`, `pattern-golden-paths`, `framework-platform-maturity` |
| PRO | Product Discovery and Value Validation | `practice-continuous-discovery`, `pattern-product-trio`, `pattern-opportunity-solution-tree` |
| SEC | Security and AI Risk Management | `standard-nist-ssdf`, `standard-nist-ai-rmf`, `standard-iso-42001` |
| MET | Measurement, Feedback, and Continuous Improvement | `framework-space`, `framework-dora-core`, `practice-kaizen-retrospective-improvement` |
| ARC | Architecture, Decisions, and Documentation | `standard-iso-42010`, `pattern-adr-decision-log`, `framework-diataxis` |

## GOV: System Governance and Sociotechnical Operating Model

- Object: Studio operating model, decision rights, role boundaries, guardrails,
  escalation paths, review gates, and governance mechanisms.
- Goal: determine whether the Studio can operate with autonomy while preserving
  accountability, feedback, and safe escalation.
- Expected state: explicit responsibilities, boundaries, review authority,
  golden paths, exception handling, and governance evidence.
- Mature signs: decisions are owned; risk gates are evidence-based; exceptions
  are visible; roles do not silently merge; governance is connected to real
  work.
- Problem signs: hidden authority, unclear escalation, unmanaged autonomy,
  excessive approval, or human approvals without review criteria.
- Typical anti-patterns: human rubber stamp for AI, checklist theater, agentic
  overengineering, tool-centric production-system thinking.
- Limitations: KB does not prescribe exact organizational structure or role
  count.
- Possible future research: stronger governance patterns for single-user AI
  studios versus multi-user studios.

## KNO: Knowledge, Memory, and Provenance

- Object: KB, source registers, task-local memory, decision memory, context
  management, provenance, refresh and validation status.
- Goal: determine whether knowledge remains reusable, source-backed, current,
  linked to work, and protected from staleness.
- Expected state: atomic records or equivalent reusable knowledge, source
  links, confidence, refresh rules, application status, object links, and
  current-state registers.
- Mature signs: auditors can trace claims to sources and objects; stale records
  are identifiable; knowledge gaps are explicit; memory is retrieved from source
  rather than hallucinated.
- Problem signs: long undifferentiated documents, stale KB, missing ownership,
  missing source links, unclear applied/accepted distinction.
- Typical anti-patterns: knowledge dump KB, over-capture of transient detail,
  ungoverned AI memory.
- Limitations: full knowledge graph tooling is under evaluation and not required
  by current KB.
- Possible future research: when simple links become insufficient and a graph
  implementation is justified.

## AI: AI-Agent Work System and Human-AI Control

- Object: AI-agent workflows, tool loops, agent-computer interface, permissions,
  evaluations, human checkpoints, and observability.
- Goal: determine whether AI autonomy is justified, bounded, observable,
  evaluated, and reviewable.
- Expected state: agent loops are used only where useful; tools and permissions
  are explicit; evaluations and regression checks exist for risky use; human
  review is meaningful.
- Mature signs: agent failures are visible; evals represent real work; autonomy
  increases only with evidence; tool feedback is legible; stopping conditions
  exist.
- Problem signs: demos replace evals, public benchmarks are over-trusted,
  subagents/planners are added without measured benefit, humans approve without
  evidence.
- Typical anti-patterns: agentic overengineering, automation without
  observability, human rubber stamp for AI.
- Limitations: KB marks agent-computer interface and intelligent production
  vocabulary as Under Evaluation; AI tooling knowledge requires frequent
  refresh.
- Possible future research: Studio-specific AI eval harness and local benchmark
  design.

## QUA: Built-in Quality, Review, and Verification

- Object: quality controls, review practices, checklists, verification gates,
  quality attributes, and defect prevention.
- Goal: determine whether quality is created inside the work system and
  verified with useful independent evidence.
- Expected state: quality criteria are embedded in production workflows, reviews
  are timely and focused, checklists occur at real pause points, and quality is
  multi-dimensional.
- Mature signs: review catches meaningful issues; small changes are reviewable;
  checklists are short and used before irreversible steps; quality attributes
  are tailored to risk.
- Problem signs: late-only inspection, checklist paperwork, style-policing
  review, missing tests/evidence, quality reduced to one metric.
- Typical anti-patterns: checklist theater, single-metric productivity, false
  assurance from pipeline/checklist presence.
- Limitations: ISO/IEC 25010 exact 2023 mapping needs refresh in KB.
- Possible future research: Studio-specific quality attribute taxonomy.

## DEL: Delivery Flow, Reliability, and Operations

- Object: work slicing, delivery pipeline, reliability objectives, operational
  response, incident learning, release and rollback evidence.
- Goal: determine whether the Studio can deliver safely, learn quickly, and
  recover from failures.
- Expected state: work is sliced into reviewable increments; checks provide
  trustworthy feedback; reliability tradeoffs are explicit; incidents or
  high-risk failures generate learning.
- Mature signs: delivery signals balance speed and stability; failures produce
  postmortem learning; automation has logs/evals/rollback; release gates are
  meaningful.
- Problem signs: large opaque batches, brittle pipeline, hidden failures,
  subjective reliability debates, incidents without learning.
- Typical anti-patterns: automation without observability, pipeline presence as
  proof of quality, delivery speed without stability context.
- Limitations: current KB has no local incident process or delivery metric
  implementation.
- Possible future research: local incident severity model and audit-safe
  delivery telemetry definitions.

## PLA: Platform Capability and Golden Paths

- Object: reusable internal capabilities, golden paths, platform interfaces,
  support, adoption, and capability ownership.
- Goal: determine whether shared capabilities reduce cognitive load and support
  repeated work without becoming bureaucracy.
- Expected state: common needs have maintained paths; internal users and
  adoption are understood; exceptions are possible; interface does not replace
  capability.
- Mature signs: platform surfaces solve repeated needs; golden paths are
  maintained; support and ownership are clear; adoption data informs evolution.
- Problem signs: bespoke request queue, stale portal/catalog, coercive defaults,
  no user research, no ownership.
- Typical anti-patterns: platform as ticket queue, portal equals platform,
  maturity ladder chasing.
- Limitations: internal developer portal is explicitly rejected for current
  context; Framework must not require a portal.
- Possible future research: criteria for when a local Studio becomes a
  multi-user platform.

## PRO: Product Discovery and Value Validation

- Object: product decisions, roadmap reasoning, outcome evidence, user/customer
  discovery, opportunity mapping, experiments.
- Goal: determine whether Studio development is connected to validated outcomes
  rather than only feature output.
- Expected state: decisions link outcomes, opportunities, options, experiments,
  and evidence; product/design/engineering perspectives collaborate.
- Mature signs: alternatives are considered; discovery influences delivery;
  success is measured by outcomes where possible; commitments are explicit.
- Problem signs: stakeholder request lists, feature shipping as success proof,
  discovery detached from delivery, no user evidence.
- Typical anti-patterns: feature factory, static opportunity trees, closed trios
  excluding needed perspectives.
- Limitations: KB does not define a canonical Product Analyst role.
- Possible future research: Studio-specific product discovery evidence model.

## SEC: Security and AI Risk Management

- Object: secure development lifecycle, AI risk governance, risk ownership,
  controls, monitoring, human approval, and due-care evidence.
- Goal: determine whether security and AI risks are identified, managed,
  verified, and tied to actual operations.
- Expected state: security is integrated across lifecycle; AI risks are governed
  with operational evidence; management-system language is not certification
  theater.
- Mature signs: threat/risk context is explicit; controls are tailored; risk
  reviews have evidence; AI checkpoints are meaningful; responsibility is owned.
- Problem signs: late security review only, generic compliance checklist, no AI
  risk monitoring, approvals without evidence.
- Typical anti-patterns: human rubber stamp for AI, checklist theater,
  standards as paperwork.
- Limitations: KB provides high-level standards but no local control mapping.
- Possible future research: local AI/security control catalog and audit
  evidence matrix.

## MET: Measurement, Feedback, and Continuous Improvement

- Object: metrics, feedback loops, productivity/delivery measures,
  retrospectives, improvement experiments, and follow-through.
- Goal: determine whether measurement supports learning and decisions without
  distorting behavior.
- Expected state: measures are balanced, contextual, decision-linked, and paired
  with qualitative interpretation and improvement ownership.
- Mature signs: metrics combine flow, quality, reliability, satisfaction, and
  outcomes; improvement cycles have owners and follow-up; feedback is trusted.
- Problem signs: one activity metric dominates; dashboards lack decisions;
  retrospectives produce unowned action lists; feedback is invalid/noisy.
- Typical anti-patterns: single-metric productivity, Goodhart-like incentives,
  ritual retrospectives.
- Limitations: KB does not include a local productivity measurement program.
- Possible future research: Studio-specific balanced metric set and safeguards.

## ARC: Architecture, Decisions, and Documentation

- Object: architecture descriptions, stakeholder concerns, viewpoints, decision
  records, documentation organization, and link structure.
- Goal: determine whether important technical and governance choices are
  reviewable, understandable, and maintainable over time.
- Expected state: architecture decisions address relevant concerns; important
  decisions record context/status/consequences; documentation form matches user
  need.
- Mature signs: architecture reviews use relevant viewpoints; decision records
  can be found; docs separate reference/how-to/explanation where useful; links
  support navigation.
- Problem signs: one generic diagram, missing rationale, stale docs, mixed
  purpose documents, graph/tooling before need is proven.
- Typical anti-patterns: knowledge dump KB, portal/tool equals capability,
  over-formalized review for trivial changes.
- Limitations: no canonical architecture review artifact or ADR process exists
  in current KB object map.
- Possible future research: canonical architecture/decision artifact design.

