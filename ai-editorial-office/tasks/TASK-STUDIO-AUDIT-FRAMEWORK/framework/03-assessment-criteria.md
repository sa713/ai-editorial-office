# Assessment Criteria

This catalog defines how future auditors should evaluate criteria. It does not
score the current Studio.

Every criterion includes:

- object and expected state;
- rationale and KB links;
- applicability limits;
- verification questions;
- necessary evidence and admissible sources;
- signs of conformance and nonconformance.

Use maturity rules from `04-maturity-model.md` and evidence rules from
`05-evidence-collection-rules.md`.

## GOV: System Governance and Sociotechnical Operating Model

### GOV-01: Sociotechnical System Scope

- Object: whole Studio operating model.
- Expected state: audit scope covers people, process, tools, knowledge,
  feedback, governance, and improvement.
- Why it matters: KB defines intelligent production systems as sociotechnical,
  not merely automated tooling.
- KB links: `glossary-intelligent-production-system`,
  `principle-sociotechnical-production-system`.
- Questions: Does audit scope include all sociotechnical dimensions? Are tool,
  process, knowledge, and governance interactions visible?
- Evidence: scope statement, operating model docs, role/process/artifact maps,
  governance docs.
- Conformance signs: system interactions are explicit; local practices are tied
  to outcomes and governance.
- Nonconformance signs: audit treats Studio only as toolchain, repository, or
  document set.
- Limits: criterion does not prescribe exact organization design.

### GOV-02: Decision Rights and Guardrails

- Object: role boundaries, decision authority, escalation, review gates.
- Expected state: autonomy exists inside explicit guardrails with accountability
  and escalation.
- Why it matters: KB says guardrails prevent both central bottlenecks and hidden
  unmanaged decisions.
- KB links: `principle-autonomy-with-guardrails`,
  `pattern-human-ai-checkpoints`, `anti-pattern-human-rubber-stamp-ai`.
- Questions: Who can decide, approve, block, or escalate? What boundaries apply
  by risk level?
- Evidence: role specs, pipeline docs, approval records, exception logs,
  final-governance records.
- Conformance signs: authority is documented and used; exceptions are traceable.
- Nonconformance signs: authority is implicit, merged, bypassed, or dependent on
  memory.
- Limits: low-risk work may use lighter guardrails if boundaries are explicit.

### GOV-03: Meaningful Human Checkpoints

- Object: human review, approval, and steering checkpoints.
- Expected state: checkpoints occur where risk/ambiguity warrants them and are
  supported by evidence and criteria.
- Why it matters: KB warns that human-in-the-loop controls become false safety
  when reviewers lack context, time, authority, or criteria.
- KB links: `pattern-human-ai-checkpoints`,
  `anti-pattern-human-rubber-stamp-ai`, `practice-ai-evaluation-harness`.
- Questions: What decisions require human checkpoint? Can the human reviewer
  make an informed decision?
- Evidence: review artifacts, approval records, criteria/rubrics, evidence
  packets, reviewer notes.
- Conformance signs: reviewers cite evidence; approval can be challenged;
  review depth matches risk.
- Nonconformance signs: approvals are perfunctory, context-free, or always
  granted.
- Limits: negligible-risk well-evaluated automation may not need heavy human
  checkpoints.

### GOV-04: Golden Paths with Exceptions

- Object: default workflows, templates, pipelines, and exception routes.
- Expected state: common work has maintained default paths; atypical work has
  justified escape hatches.
- Why it matters: KB treats golden paths as useful only when maintained and not
  coercive.
- KB links: `pattern-golden-paths`,
  `principle-autonomy-with-guardrails`, `anti-pattern-checklist-theater`.
- Questions: What work has default paths? How are exceptions approved and
  documented?
- Evidence: templates, pipelines, usage examples, exception records, maintenance
  notes.
- Conformance signs: defaults reduce setup cost and preserve risk controls.
- Nonconformance signs: defaults are stale, ignored, mandatory in inappropriate
  cases, or undocumented.
- Limits: novel work may not have a sensible golden path.

## KNO: Knowledge, Memory, and Provenance

### KNO-01: Source-Linked Reusable Knowledge

- Object: KB records, source registers, reusable guidance.
- Expected state: knowledge is source-linked, atomic enough to reuse, and
  governed for confidence and refresh.
- Why it matters: KB warns against anonymous assertion and knowledge dump
  documentation.
- KB links: `principle-knowledge-close-to-work`,
  `pattern-provenance-linked-knowledge`, `anti-pattern-knowledge-dump-kb`,
  `schema.md`.
- Questions: Can key claims be traced to sources? Are confidence, limits, and
  refresh rules visible?
- Evidence: KB records, source registers, schema compliance checks, refresh
  records.
- Conformance signs: claims have sources and limitations; records are findable
  and reusable.
- Nonconformance signs: long source-free documents, duplicated claims, stale
  guidance, unclear ownership.
- Limits: long research documents may remain useful as source material, not as
  the only reusable memory format.

### KNO-02: Knowledge Application and Coverage

- Object: application register, lifecycle statuses, object links, coverage
  snapshots.
- Expected state: accepted/applied/under-evaluation/rejected knowledge is
  distinguished and linked to Studio objects where applicable.
- Why it matters: KB separates external knowledge value from current Studio
  application.
- KB links: `application-model.md`, `lifecycle.md`,
  `application-register.md`, `coverage-model.md`, `studio-object-map.md`.
- Questions: Are Applied records backed by active object links? Are rejected and
  under-evaluation records explained?
- Evidence: application register, coverage model, object map, record profiles.
- Conformance signs: status counts are current; applied status is not inflated;
  reconsideration and review triggers exist.
- Nonconformance signs: accepted knowledge treated as implemented; rejected
  records lack conditions; missing object links.
- Limits: status is current Studio application, not universal truth.

### KNO-03: Context and Memory Management

- Object: task memory, persistent context, retrieval, retention, freshness.
- Expected state: important context persists near work; stale, sensitive, or
  low-value memory is not retained blindly.
- Why it matters: KB says useful memory is relevant, trusted, current, and
  governed.
- KB links: `practice-context-and-memory-management`,
  `principle-knowledge-close-to-work`.
- Questions: What must persist? What expires or is retrieved from source? How
  are restarts protected from hallucinated memory?
- Evidence: task manifests, status files, handoffs, context summaries, retention
  rules, source references.
- Conformance signs: restart artifacts point to current source; stale context is
  visible; handoffs preserve necessary deltas.
- Nonconformance signs: reliance on chat memory, stale assumptions, noisy
  over-capture, sensitive low-value persistence.
- Limits: AI memory practices are evolving and require frequent refresh.

### KNO-04: Consequential Decision Memory

- Object: decisions about architecture, process, platform, AI, governance, and
  knowledge structure.
- Expected state: important decisions record context, status, decision, and
  consequences.
- Why it matters: KB says decision records prevent re-litigation and loss of
  rationale.
- KB links: `pattern-adr-decision-log`, `decision-technique-adr`,
  `standard-iso-42010`.
- Questions: Which decisions are consequential? Can future auditors find the
  rationale and status?
- Evidence: ADRs or equivalent records, final decisions, architecture notes,
  governance records.
- Conformance signs: decisions are compact, current, and linked to consequences.
- Nonconformance signs: rationale exists only in memory; decisions are repeated
  or reversed without trace.
- Limits: no canonical ADR artifact exists in KB; equivalent evidence is
  acceptable.

## AI: AI-Agent Work System and Human-AI Control

### AI-01: Justified Agentic Workflow

- Object: agent loops, planners, routers, subagents, tool use.
- Expected state: agency is used when ambiguity, tool feedback, and multi-step
  adaptation justify it.
- Why it matters: KB warns against complex agent systems where deterministic
  workflows would be better.
- KB links: `pattern-agent-tool-loop`, `anti-pattern-agentic-overengineering`.
- Questions: Why is an agent loop needed? What simpler workflow was considered?
- Evidence: workflow design notes, eval comparisons, failure analysis,
  operating constraints.
- Conformance signs: complexity is justified by evidence and task nature.
- Nonconformance signs: agents added for novelty, cost/latency/failure surface
  rises without measured benefit.
- Limits: threshold changes as models and tools evolve.

### AI-02: Agent-Computer Interface

- Object: agent tools, commands, permissions, observations, environment.
- Expected state: interface makes actions, observations, permissions, and
  stopping conditions legible and auditable.
- Why it matters: KB links coding-agent effectiveness to environment and
  interface design.
- KB links: `pattern-agent-computer-interface`,
  `case-study-swe-bench-and-swe-agent`.
- Questions: What can agents do? What can they observe? What actions require
  approval?
- Evidence: tool permission docs, execution logs, sandbox policy, interface
  specs, agent traces.
- Conformance signs: tool actions are visible; permissions match risk; failures
  can be diagnosed.
- Nonconformance signs: opaque actions, hidden environment assumptions,
  uncontrolled permissions.
- Limits: KB status is Under Evaluation; score conservatively without local
  validation.

### AI-03: AI Evaluation Harness

- Object: eval datasets, benchmark tasks, rubrics, regression checks.
- Expected state: AI workflow changes and autonomy expansion are evaluated with
  repeatable tests and human rubrics.
- Why it matters: KB says demos, anecdotes, and public benchmark scores are
  insufficient for production confidence.
- KB links: `practice-ai-evaluation-harness`,
  `case-study-swe-bench-and-swe-agent`, `standard-nist-ai-rmf`.
- Questions: What tasks represent real work? How are regressions detected? What
  thresholds gate autonomy?
- Evidence: eval suites, benchmark tasks, rubric results, regression logs,
  model/tool change records.
- Conformance signs: evals map to real workflows and are refreshed.
- Nonconformance signs: only demos, one-off successes, or public benchmark
  claims.
- Limits: KB lacks Studio-specific thresholds; auditors must not invent them.

### AI-04: AI Observability and Audit Trail

- Object: AI actions, outputs, logs, provenance, review trails.
- Expected state: AI-assisted work is reviewable through logs, provenance, evals
  or equivalent evidence.
- Why it matters: KB warns automation without observability creates hidden
  failure modes.
- KB links: `anti-pattern-automation-without-observability`,
  `pattern-provenance-linked-knowledge`, `pattern-human-ai-checkpoints`.
- Questions: Can auditors reconstruct what AI did and why? Are failures visible?
- Evidence: run logs, prompts/inputs when appropriate, tool traces, review
  artifacts, provenance links.
- Conformance signs: material AI outputs and actions can be traced and reviewed.
- Nonconformance signs: no logs, no provenance, no rollback/diagnosis path for
  risky automation.
- Limits: low-risk visible automation may need lighter evidence.

## QUA: Built-in Quality, Review, and Verification

### QUA-01: Built-in Quality Controls

- Object: quality gates embedded across work lifecycle.
- Expected state: quality is designed into workflow, not inspected only at the
  end.
- Why it matters: KB says late inspection alone is weaker than built-in quality.
- KB links: `principle-built-in-quality`, `practice-secure-sdlc-ssdf`,
  `pattern-continuous-delivery-pipeline`.
- Questions: Where is quality checked before final review? Which defects are
  prevented rather than detected late?
- Evidence: workflow docs, tests, review gates, security checks, validation
  artifacts.
- Conformance signs: quality criteria affect work before finalization.
- Nonconformance signs: review is the only quality mechanism; recurring defects
  are accepted.
- Limits: built-in quality does not remove independent review.

### QUA-02: Review Quality

- Object: code/content/system review practices.
- Expected state: review is timely, focused, independent where needed, and
  supports correctness, maintainability, and knowledge sharing.
- Why it matters: KB treats review as quality and context-sharing mechanism, not
  style theater.
- KB links: `practice-modern-code-review`, `principle-built-in-quality`,
  `pattern-small-batches`.
- Questions: What is review expected to catch? Are changes reviewable in size
  and context?
- Evidence: review artifacts, PR/review logs, reviewer notes, change samples,
  re-review records.
- Conformance signs: findings are substantive; review is proportional to risk.
- Nonconformance signs: review is skipped, purely stylistic, blocking without
  value, or non-independent where independence is required.
- Limits: record is accepted but not fully mapped to a Studio code-review
  practice.

### QUA-03: Checklists at Pause Points

- Object: release, publication, review, safety, incident, or AI-action
  checklists.
- Expected state: checklists are short coordination aids used at natural pause
  points before consequential actions.
- Why it matters: KB distinguishes useful checklists from checklist theater.
- KB links: `practice-checklists-at-pause-points`,
  `anti-pattern-checklist-theater`,
  `case-study-who-surgical-safety-checklist`.
- Questions: Is the checklist short, timed correctly, and used before action?
  Does it coordinate attention?
- Evidence: checklist templates, completed checklists, timing records, reviewer
  notes.
- Conformance signs: checks are concise, risk-focused, and used in the workflow.
- Nonconformance signs: long generic lists, after-the-fact completion, ignored
  items, false assurance.
- Limits: WHO case study is analogical for software/AI.

### QUA-04: Multi-Dimensional Quality

- Object: product/system quality attributes and verification criteria.
- Expected state: quality is evaluated across relevant attributes such as
  reliability, usability, security, maintainability, and functional suitability.
- Why it matters: KB warns against reducing quality to speed or one defect
  dimension.
- KB links: `standard-iso-25010`, `framework-space`,
  `principle-built-in-quality`.
- Questions: Which quality attributes matter for this Studio scope? Are they
  weighted by risk and user context?
- Evidence: quality model, review criteria, architecture concerns, test/eval
  plans.
- Conformance signs: quality attributes are explicit and tailored.
- Nonconformance signs: all attributes treated equally, or quality reduced to
  one number.
- Limits: exact ISO/IEC 25010 2023 mapping needs KB refresh.

## DEL: Delivery Flow, Reliability, and Operations

### DEL-01: Small Reviewable Batches

- Object: work slicing and change size.
- Expected state: work is split into small, coherent, independently reviewable
  increments.
- Why it matters: KB says large batches hide defects and delay learning.
- KB links: `pattern-small-batches`, `principle-fast-feedback-loops`,
  `practice-modern-code-review`.
- Questions: Can reviewers understand each increment? Does slicing preserve
  coherent value?
- Evidence: change history, task records, release notes, review samples.
- Conformance signs: changes are reviewable and integrate safely.
- Nonconformance signs: large opaque batches, excessive fragmentation, missing
  integration context.
- Limits: coordinated release plans may still be necessary.

### DEL-02: Trustworthy Delivery Pipeline

- Object: build, test, security, deployment/release checks.
- Expected state: automated or repeatable checks keep work in a releasable state
  and provide valid feedback.
- Why it matters: KB treats pipelines as feedback and control systems, not proof
  of quality by presence alone.
- KB links: `pattern-continuous-delivery-pipeline`,
  `principle-built-in-quality`, `standard-nist-ssdf`.
- Questions: Which checks gate release? Are tests/security checks meaningful?
- Evidence: CI logs, test results, release records, security checks, rollback
  evidence.
- Conformance signs: pipeline failures are actionable; checks map to risks.
- Nonconformance signs: brittle checks, ignored failures, shallow tests,
  pipeline theater.
- Limits: not every Studio artifact may require deployment pipeline evidence.

### DEL-03: Reliability Objectives and Tradeoffs

- Object: reliability goals, service/workflow objectives, error budget thinking.
- Expected state: reliability/speed tradeoffs are explicit and user-impact
  centered where measurable.
- Why it matters: KB says SLOs and error budgets make tradeoffs less subjective.
- KB links: `pattern-slo-error-budget`, `case-study-google-sre`,
  `metric-dora-four-key-metrics`.
- Questions: What reliability/user-impact objectives exist? Who can act on
  reliability signals?
- Evidence: SLO/SLI definitions, incident data, release decisions, user-impact
  metrics.
- Conformance signs: objectives inform release or pause decisions.
- Nonconformance signs: no reliability signals, subjective debates, indicators
  detached from user impact.
- Limits: do not apply mechanically where user impact cannot be measured.

### DEL-04: Incident and Failure Learning

- Object: incidents, high-risk workflow failures, response and learning.
- Expected state: failures are detected, coordinated, resolved, communicated,
  and converted into system learning.
- Why it matters: KB treats incident management as reliability learning, not
  blame.
- KB links: `process-incident-management`, `case-study-google-sre`,
  `practice-kaizen-retrospective-improvement`.
- Questions: How are significant failures declared and learned from? Are actions
  owned and followed up?
- Evidence: incident records, postmortems, status logs, improvement follow-up,
  communication records.
- Conformance signs: response roles and learning loops are visible.
- Nonconformance signs: repeated failures without analysis, blame focus, no
  follow-up.
- Limits: KB lacks a local incident severity taxonomy.

## PLA: Platform Capability and Golden Paths

### PLA-01: Platform as Product

- Object: shared internal capabilities and their operating model.
- Expected state: shared capabilities have users, ownership, support, adoption
  understanding, and improvement path.
- Why it matters: KB says platforms should be product-like, not passive request
  services.
- KB links: `pattern-platform-as-product`, `framework-platform-maturity`.
- Questions: Who are the internal users? What repeated needs are served? How is
  adoption understood?
- Evidence: capability docs, user research, support records, adoption data,
  roadmap/rationale.
- Conformance signs: capabilities reduce cognitive load and evolve with user
  evidence.
- Nonconformance signs: unclear users, no support, no adoption signal, platform
  exists by declaration only.
- Limits: avoid platform model if repeated internal-user needs do not exist.

### PLA-02: Avoid Platform Ticket Queue

- Object: platform request and support workflow.
- Expected state: support exists but does not replace reusable self-service
  capability.
- Why it matters: KB identifies platform-as-ticket-queue as a scaling failure.
- KB links: `anti-pattern-platform-as-ticket-queue`,
  `pattern-golden-paths`, `pattern-platform-as-product`.
- Questions: Is work dominated by bespoke requests? Do repeated requests become
  reusable capabilities?
- Evidence: request logs, support patterns, golden paths, capability backlog,
  adoption evidence.
- Conformance signs: repeated needs are productized; support informs platform
  evolution.
- Nonconformance signs: manual approvals and bespoke work dominate.
- Limits: high-risk operations may legitimately require request workflows.

### PLA-03: Portal Is Not Platform

- Object: portals, catalogs, templates, platform interfaces.
- Expected state: portals/catalogs are evaluated as interfaces to real
  capability, not as the platform itself.
- Why it matters: KB rejects portal-only thinking and marks internal developer
  portal rejected for current context.
- KB links: `anti-pattern-portal-equals-platform`,
  `tool-internal-developer-portal`.
- Questions: What capability sits behind any portal/interface? Does the portal
  have ownership and automation?
- Evidence: portal/catalog docs if present, capability links, ownership records,
  automation/support evidence.
- Conformance signs: interface improves access to real maintained capability.
- Nonconformance signs: stale catalog, no capability, portal treated as proof of
  platform maturity.
- Limits: do not require a portal for current local repository-first context.

### PLA-04: Maintained Golden Paths

- Object: platform/default paths for common work.
- Expected state: golden paths are maintained, adopted, measured, and paired
  with exception handling.
- Why it matters: KB says default paths reduce cognitive load only when treated
  as maintained product surfaces.
- KB links: `pattern-golden-paths`, `framework-platform-maturity`,
  `pattern-platform-as-product`.
- Questions: Are paths current? Who maintains them? How are adoption and
  exceptions known?
- Evidence: templates, path docs, usage records, maintenance logs, exception
  examples.
- Conformance signs: users can follow paths reliably; stale paths are updated.
- Nonconformance signs: outdated templates, hidden exceptions, forced defaults.
- Limits: maturity is context-relative; higher maturity is not always better.

## PRO: Product Discovery and Value Validation

### PRO-01: Outcome-to-Opportunity Trace

- Object: product/problem decisions and discovery evidence.
- Expected state: outcomes connect to user/customer evidence, opportunities,
  solution options, and experiments.
- Why it matters: KB says discovery reduces feature work that lacks value
  evidence.
- KB links: `practice-continuous-discovery`,
  `pattern-opportunity-solution-tree`.
- Questions: What outcome is targeted? What evidence supports the opportunity?
  What alternatives were considered?
- Evidence: discovery notes, opportunity maps, experiment plans/results,
  customer/user research.
- Conformance signs: decisions trace from outcomes to options and tests.
- Nonconformance signs: solution chosen before problem evidence; static maps
  without discovery.
- Limits: requires access to relevant users/customers or suitable proxy
  evidence.

### PRO-02: Cross-Functional Product Decision Unit

- Object: product/design/engineering collaboration and stakeholder inclusion.
- Expected state: product, design, and engineering perspectives collaborate;
  relevant security/support/data/stakeholders are included when needed.
- Why it matters: KB says product trio reduces late discovery of value,
  usability, feasibility, and viability risks.
- KB links: `pattern-product-trio`, `practice-continuous-discovery`.
- Questions: Which perspectives shaped the decision? Were relevant risks
  represented early?
- Evidence: decision notes, discovery sessions, review records, stakeholder
  input, option evaluation.
- Conformance signs: tradeoffs across value/usability/feasibility/viability are
  explicit.
- Nonconformance signs: handoff-only decisions, closed trio excluding necessary
  expertise.
- Limits: exact roles may differ; the criterion checks perspectives, not titles.

### PRO-03: Avoid Feature Factory

- Object: roadmap, success measures, product output/value logic.
- Expected state: shipped features are not treated as proof of value without
  outcome evidence or justified commitment.
- Why it matters: KB identifies feature factory as output optimization without
  validated outcomes.
- KB links: `anti-pattern-feature-factory`,
  `practice-continuous-discovery`, `framework-dora-core`.
- Questions: How is success defined? Are outcomes measured or deliberately
  deferred?
- Evidence: roadmap rationale, outcome metrics, discovery artifacts, experiment
  results, commitment records.
- Conformance signs: value/risk evidence influences priorities.
- Nonconformance signs: roadmap is mainly request list; success equals feature
  count.
- Limits: some contractual/compliance commitments legitimately require feature
  delivery.

## SEC: Security and AI Risk Management

### SEC-01: Secure Lifecycle Integration

- Object: secure software/AI development practices across lifecycle.
- Expected state: security is integrated into planning, implementation,
  verification, release, and response.
- Why it matters: KB says security should not be late inspection or compliance
  paperwork only.
- KB links: `practice-secure-sdlc-ssdf`, `standard-nist-ssdf`,
  `principle-built-in-quality`.
- Questions: Where are security risks identified and verified? Are controls
  tailored to threat context?
- Evidence: threat/risk notes, security checks, code review evidence, release
  gates, response records.
- Conformance signs: controls affect actual engineering behavior.
- Nonconformance signs: generic checklist, late-only security review, no threat
  context.
- Limits: SSDF is high-level and requires local tailoring.

### SEC-02: AI Risk Governance

- Object: AI risk identification, measurement, management, monitoring.
- Expected state: AI risks have explicit ownership, evidence, monitoring, and
  decision paths.
- Why it matters: KB uses NIST AI RMF and ISO/IEC 42001 as governance language
  for AI risk.
- KB links: `standard-nist-ai-rmf`, `standard-iso-42001`,
  `pattern-human-ai-checkpoints`.
- Questions: What AI risks are known? How are they measured or monitored? Who
  can accept or block risk?
- Evidence: risk register, eval results, monitoring, approval records,
  incident/failure records.
- Conformance signs: risk evidence affects autonomy, release, or approval.
- Nonconformance signs: AI risk is implicit; no monitoring; approvals have no
  criteria.
- Limits: KB lacks local AI control mapping.

### SEC-03: No Governance Theater

- Object: AI/security governance controls and certification/compliance claims.
- Expected state: governance mechanisms connect to real operational evidence,
  responsibility, and follow-up.
- Why it matters: KB warns management systems and human controls fail when they
  become paperwork or rubber stamps.
- KB links: `standard-iso-42001`, `standard-nist-ai-rmf`,
  `anti-pattern-human-rubber-stamp-ai`.
- Questions: What decision does each control support? What evidence shows it
  changes operation?
- Evidence: control mapping, review records, action follow-up, risk decisions,
  monitoring reports.
- Conformance signs: governance controls are used and produce decisions.
- Nonconformance signs: certification labels, unchecked boxes, no operational
  effect.
- Limits: criterion does not require certification.

## MET: Measurement, Feedback, and Continuous Improvement

### MET-01: Balanced System-Level Measurement

- Object: delivery, productivity, flow, satisfaction, quality, outcomes.
- Expected state: measurement is balanced, contextual, and system-level.
- Why it matters: KB warns against single-metric productivity and context-free
  ranking.
- KB links: `framework-dora-core`, `framework-space`,
  `metric-dora-four-key-metrics`, `metric-space-balanced-productivity`.
- Questions: What decisions do metrics support? Are throughput and stability
  balanced with human/product signals?
- Evidence: metric definitions, dashboards, survey/research summaries, decision
  records.
- Conformance signs: metrics are interpreted with context and used for system
  improvement.
- Nonconformance signs: one metric drives behavior; individual ranking; unclear
  metric definitions.
- Limits: no metric set is universal.

### MET-02: Single-Metric Guardrail

- Object: productivity and performance indicators.
- Expected state: no single activity metric is treated as complete productivity
  truth.
- Why it matters: KB identifies single-metric productivity as a harmful
  simplification.
- KB links: `anti-pattern-single-metric-productivity`, `framework-space`,
  `metric-space-balanced-productivity`.
- Questions: Are activity metrics used diagnostically or as total performance
  proxies?
- Evidence: KPI definitions, dashboard explanations, review/decision records,
  incentive policy.
- Conformance signs: activity data is contextualized and not punitive alone.
- Nonconformance signs: commits/tickets/prompts used as productivity proof.
- Limits: activity metrics can be useful diagnostics.

### MET-03: Trustworthy Feedback Loops

- Object: feedback mechanisms across delivery, product, AI, operations, and KB.
- Expected state: feedback produces valid signals tied to decisions.
- Why it matters: KB says fast feedback is valuable only when signal is valid
  and connected to outcomes.
- KB links: `principle-fast-feedback-loops`, `framework-dora-core`,
  `practice-continuous-discovery`.
- Questions: What feedback arrives when? What decision changes because of it?
- Evidence: review cycles, eval results, discovery findings, incident learning,
  metric trends.
- Conformance signs: feedback leads to small corrections and risk detection.
- Nonconformance signs: feedback is invalid, noisy, delayed, or ignored.
- Limits: deep research may use longer-cycle feedback if explicit.

### MET-04: Improvement Follow-Through

- Object: retrospectives, problem-solving, improvement experiments.
- Expected state: improvement cycles have evidence, ownership, countermeasures,
  and follow-up.
- Why it matters: KB says continuous improvement without ownership becomes
  ceremony.
- KB links: `practice-kaizen-retrospective-improvement`,
  `method-a3-problem-solving`, `case-study-toyota-production-system`.
- Questions: Are recurring problems analyzed? Are actions owned and validated?
- Evidence: retro notes, A3-like records, improvement experiments, follow-up
  status, outcome checks.
- Conformance signs: problems recur less or learning is institutionalized.
- Nonconformance signs: unowned action lists, repeated issues, no validation.
- Limits: A3 source support is incomplete; do not mandate A3 format.

## ARC: Architecture, Decisions, and Documentation

### ARC-01: Architecture by Viewpoints

- Object: architecture descriptions and reviews.
- Expected state: significant architecture is reviewed through stakeholder
  concerns, viewpoints, and views.
- Why it matters: KB says one generic diagram is insufficient for complex
  architecture decisions.
- KB links: `standard-iso-42010`,
  `practice-architecture-review-by-viewpoints`.
- Questions: Whose concerns are represented? Which views answer which concerns?
- Evidence: architecture docs, viewpoint list, review records, decision records.
- Conformance signs: security, operations, maintainability, users, and business
  concerns are considered when relevant.
- Nonconformance signs: diagrams without concerns, opinion-only review,
  over-formality for trivial changes.
- Limits: avoid heavyweight review for low-risk reversible changes.

### ARC-02: Decision Records

- Object: consequential technical/process/governance decisions.
- Expected state: context, decision, status, consequences, and reversal/review
  conditions are recorded.
- Why it matters: KB says decision records preserve rationale and aid future
  review.
- KB links: `decision-technique-adr`, `pattern-adr-decision-log`,
  `principle-knowledge-close-to-work`.
- Questions: Which decisions matter later? Can consequences and status be
  inspected?
- Evidence: ADRs or equivalent, final decisions, governance records,
  architecture notes.
- Conformance signs: records are compact, findable, and maintained.
- Nonconformance signs: repeated re-litigation, lost rationale, stale status.
- Limits: ADRs document decisions; they do not prove decision quality.

### ARC-03: Documentation by User Need

- Object: documentation and knowledge surfaces.
- Expected state: documentation form matches user need, separating reference,
  how-to, explanation, and tutorial where useful.
- Why it matters: KB says mixed-purpose documentation reduces findability and
  reuse.
- KB links: `framework-diataxis`, `anti-pattern-knowledge-dump-kb`,
  `principle-knowledge-close-to-work`.
- Questions: What user need does each document serve? Are reference and
  narrative mixed in harmful ways?
- Evidence: documentation map, navigation, docs samples, user feedback,
  maintenance records.
- Conformance signs: docs are findable and purpose-clear.
- Nonconformance signs: stale catch-all documents, duplicated guidance, unclear
  audience.
- Limits: Diataxis should not override better local taxonomy for KB records.

### ARC-04: Link Structure Before Graph Tooling

- Object: knowledge links, IDs, metadata, graph/tooling.
- Expected state: links and IDs support navigation; graph tooling is introduced
  only if simple structure is insufficient.
- Why it matters: KB values linked knowledge but warns against unnecessary
  tooling complexity.
- KB links: `tool-knowledge-graph`,
  `pattern-provenance-linked-knowledge`,
  `anti-pattern-agentic-overengineering`.
- Questions: Are relationships findable? Is graph tooling justified by actual
  navigation/traceability needs?
- Evidence: link maps, source registers, graph/schema docs if present, user
  navigation evidence.
- Conformance signs: simple links work or graph need is evidenced.
- Nonconformance signs: heavy graph stack without content quality or use case.
- Limits: full graph implementation is not mandatory.

