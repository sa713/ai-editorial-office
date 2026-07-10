# Task Need Recognition Smoke Test

Date: 2026-07-10

Release: `S5.R4 - Task Need Recognition`

Status: passed

## Purpose

Validate the bounded advisory recognition contract against ten representative
synthetic requests. The cases test task type, likely capabilities and Domain
Packs, research/evidence/review recommendations, significance, ambiguity,
decomposition, uncertainty, negative evidence, and Chief Editor authority.

They validate documented behavior only. They do not prove real-world routing
improvement, classifier accuracy, capability value, or Domain Pack value.

## Pass contract

Every case must expose:

- observed request evidence;
- likely primary task type and material secondary aspects;
- likely capabilities and Domain Packs with reasons;
- qualitative research/evidence, risk/consequence, and review recommendations;
- architecture, engineering, communication, and analytical significance where
  material;
- ambiguity, decomposition, uncertainty, and negative evidence;
- explicit non-decision;
- a separate Chief Editor decision or next question.

A case fails if a keyword, label, score, threshold, or recommendation performs
automatic routing, capability/pack activation, risk/depth selection, planning,
decomposition, lifecycle transition, or review outcome.

## Case 1: Simple editing request

### Synthetic request

> Fix grammar and shorten this two-paragraph internal note. Do not change its
> meaning.

### Advisory recognition

- Observed signals: bounded existing text; grammar/length transformation; one
  internal deliverable; source boundary is the supplied note.
- Likely primary task type: simple editing/transformation.
- Material secondary aspects: none.
- Likely capabilities: ordinary drafting/editing behavior only; Professional
  Communication is not material because the message job is already defined and
  only local clarity/length repair is requested.
- Likely Domain Packs: none.
- Research/evidence recommendation: `none or source-light`; inspect only the
  supplied note and preserve meaning.
- Risk/consequence recommendation: ordinary low exposure; internal, reversible,
  source-bounded wording work with no sensitive or external consequence.
- Review recommendation: `focused` review of meaning preservation, grammar,
  length, and source boundary.
- Significance: no architecture or engineering significance; no material
  analytical significance.
- Ambiguity/decomposition: none; one coherent deliverable.
- Confidence/negative evidence: `verified` from the request; no factual claim,
  domain decision, code/config, recommendation, or external publication.
- Explicit non-decision: no pipeline, depth, role, or review selection occurs.

### Chief Editor decision

Confirm a compact low-risk editing route, no Domain Pack, no research stage,
and mandatory focused independent review.

### Result

Pass. Recognition protects the compact path.

## Case 2: Architecture review request

### Synthetic request

> Review whether splitting our modular monolith into services is justified.
> Compare alternatives, reliability and operability tradeoffs, and record the
> risks for a decision meeting.

### Advisory recognition

- Observed signals: explicit design commitment, system boundaries,
  alternatives, quality attributes, future consequences, decision audience.
- Likely primary task type: architecture review / decision analysis.
- Material secondary aspects: Professional Analysis and decision communication.
- Likely capabilities: Architecture Review, Analytical Reasoning, Professional
  Analysis, Professional Communication; Engineering Review only if an actual
  implementation change is included later.
- Likely Domain Packs: Software Architecture primary; DevSecOps adjacent only
  if deployment/operational automation becomes material.
- Research/evidence recommendation: `full`; system drivers, current boundary,
  change profile, reliability/operability evidence, credible alternatives, and
  tradeoffs.
- Risk/consequence recommendation: elevated consideration because a potentially
  hard-to-reverse boundary decision affects reliability and operability; Chief
  Editor confirms the repository risk mode.
- Review recommendation: `deep` architecture/evidence/recommendation review.
- Significance: architecture high; engineering not yet material;
  communication material for the decision meeting.
- Ambiguity/decomposition: one coherent architecture decision; no split needed
  unless implementation planning becomes a separate deliverable.
- Confidence/negative evidence: `supported`; the task is solution-shaped but
  explicitly asks whether the split is justified, so the recommendation must
  remain open to keeping the monolith.
- Explicit non-decision: no architecture option or pack is accepted/activated.

### Chief Editor decision

Activate Architecture Review and Software Architecture Domain Pack, select
full research and deep review, and keep Engineering Review inactive until an
implementation surface appears.

### Result

Pass. Drivers and tradeoffs, not the word “services,” determine significance.

## Case 3: Engineering implementation request

### Synthetic request

> Add a `--dry-run` flag to the existing local migration script, update tests,
> and report validation. Do not change the database schema.

### Advisory recognition

- Observed signals: script/interface behavior change, tests, validation,
  explicit schema prohibition, bounded repository surface.
- Likely primary task type: engineering implementation.
- Material secondary aspects: technical implementation handoff/report.
- Likely capabilities: Engineering Review with code/change safety,
  interface/CLI, validation, and reliability/recovery lenses; Professional
  Communication only for precise deliver-back.
- Likely Domain Packs: none from current evidence.
- Research/evidence recommendation: `compact`; repository inspection, current
  CLI contract, tests, diff, dry-run behavior, and validation output.
- Risk/consequence recommendation: ordinary bounded engineering risk; script
  behavior changes, but schema change is prohibited and validation is local.
- Review recommendation: `standard` engineering review.
- Significance: engineering material; architecture ruled out because schema,
  ownership, and system boundaries are unchanged.
- Ambiguity/decomposition: one coherent implementation task.
- Confidence/negative evidence: `verified` from the request; no CI/CD,
  deployment, security-sensitive secret, architecture, or domain-specific
  surface justifies a pack.
- Explicit non-decision: no implementation plan or Engineering Review lenses
  are activated automatically.

### Chief Editor decision

Select the repository implementation mini-contract, Engineering Review lenses
named above, compact evidence, standard review, and no Domain Pack.

### Result

Pass. Local engineering significance does not become architecture or DevSecOps
by default.

## Case 4: AI engineering request

### Synthetic request

> Compare two model/provider options for a customer-support RAG assistant,
> propose an evaluation set and human escalation behavior, and recommend a
> migration path.

### Advisory recognition

- Observed signals: model/provider fit, RAG, evaluation, human oversight,
  recommendation, migration/change, current provider behavior.
- Likely primary task type: AI engineering assessment and recommendation.
- Material secondary aspects: Professional Analysis, Architecture Review if
  provider/RAG boundaries are hard to reverse, Engineering Review for a later
  implementation, Professional Communication for the recommendation.
- Likely capabilities: Analytical Reasoning, Professional Analysis,
  Professional Communication, Architecture Review; Engineering Review becomes
  material for changed implementation/evaluation code.
- Likely Domain Packs: AI Engineering primary; Software Architecture adjacent
  for system/provider/RAG boundaries; Cybersecurity adjacent if customer data,
  retrieval authorization, or tool authority is material.
- Research/evidence recommendation: `full`; current provider/model evidence,
  task-shaped cases, corpus/data boundary, component/end-to-end evaluation,
  human-oversight evidence, tradeoffs, and stale-if triggers.
- Risk/consequence recommendation: elevated consideration because provider,
  customer-support behavior, retrieval/data, migration, and human escalation
  may create consequential and hard-to-reverse exposure; exact risk is unknown.
- Review recommendation: `deep` AI-domain, evidence, architecture, and
  recommendation review.
- Significance: analytical and communication material; architecture plausible;
  engineering dependent on implementation scope.
- Ambiguity/decomposition: keep assessment/evaluation/recommendation coherent;
  split implementation into a later task after decision.
- Confidence/negative evidence: `supported`; exact provider fit remains unknown
  before current primary-source and task evaluation evidence.
- Explicit non-decision: no model/provider, pack, threshold, or migration path
  is chosen automatically.

### Chief Editor decision

Activate AI Engineering and Software Architecture packs, activate the named
analysis/architecture/communication capabilities, require full research and
deep review, and defer implementation to a separately confirmed task.

### Result

Pass. AI mention is backed by material AI-system surfaces and current evidence
needs.

## Case 5: DevSecOps request

### Synthetic request

> Review and repair the release workflow so untrusted pull requests cannot
> reach publishing credentials. Pin third-party actions and validate package
> provenance.

### Advisory recognition

- Observed signals: CI/CD workflow, untrusted/privileged boundary, credentials,
  third-party actions, artifact publication, provenance, implementation change.
- Likely primary task type: DevSecOps-sensitive engineering review and repair.
- Material secondary aspects: defensive cybersecurity context.
- Likely capabilities: Engineering Review with secure delivery, automation,
  configuration/permissions, dependency, and validation lenses; Architecture
  Review only if trust/deployment boundaries change structurally.
- Likely Domain Packs: DevSecOps primary; Cybersecurity adjacent for trust,
  credential, authorization, and residual security risk.
- Research/evidence recommendation: `full`; current platform docs, workflow
  diff, trigger/permission/secret boundaries, action pinning, artifact identity,
  provenance verification, tests, and residual risk.
- Risk/consequence recommendation: elevated because untrusted input can reach
  publishing credentials and artifact provenance; Chief Editor selects the
  actual high-governance boundary.
- Review recommendation: `deep` engineering and defensive security review.
- Significance: engineering and security high; architecture conditional.
- Ambiguity/decomposition: one coherent secure-delivery repair; separate broad
  application-security assessment if requested later.
- Confidence/negative evidence: `verified` for DevSecOps materiality; no claim
  that provenance or pinning alone proves safety.
- Explicit non-decision: no workflow edit, credential policy, pack activation,
  or approval occurs automatically.

### Chief Editor decision

Activate DevSecOps primary and Cybersecurity adjacent, select full evidence,
deep review, and Engineering Review; keep work defensive and bounded.

### Result

Pass. Primary/adjacent pack boundaries remain clear.

## Case 6: Cybersecurity request

### Synthetic request

> Assess the authorization design for a multi-tenant export API. Identify
> trust boundaries, abuse cases, control evidence, and residual risk; do not
> provide exploit steps.

### Advisory recognition

- Observed signals: authorization, tenant boundary, sensitive export, abuse
  cases, controls, assurance, residual risk, explicit defensive boundary.
- Likely primary task type: defensive cybersecurity assessment.
- Material secondary aspects: Architecture Review, Professional Analysis, and
  Professional Communication.
- Likely capabilities: Architecture Review, Analytical Reasoning, Professional
  Analysis, Professional Communication; Engineering Review if code/config is
  inspected or changed.
- Likely Domain Packs: Cybersecurity primary; Software Architecture adjacent
  for tenant/API/data boundaries.
- Research/evidence recommendation: `full`; authorization model, API/data-flow
  evidence, assets/actors/trust boundaries, abuse cases, controls/tests/logs,
  authoritative current sources, assumptions, and residual risk.
- Risk/consequence recommendation: elevated because tenant isolation,
  authorization, and sensitive exports have material confidentiality and
  wrong-result consequences.
- Review recommendation: `deep` defensive security, architecture, and evidence
  review.
- Significance: security and architecture high; engineering conditional.
- Ambiguity/decomposition: one coherent design assessment; implementation
  repairs should be separately scoped if findings arise.
- Confidence/negative evidence: `supported`; no vulnerability or compliance
  conclusion is justified without task-specific evidence.
- Explicit non-decision: no security approval, vulnerability finding, control
  mandate, or pack activation occurs automatically.

### Chief Editor decision

Activate Cybersecurity and Software Architecture packs, the named capabilities,
full research, deep review, and the defensive safety boundary.

### Result

Pass. Recognition preserves evidence and safety limits without issuing a
security verdict.

## Case 7: Ambiguous mixed request

### Synthetic request

> Fix the onboarding problems, rewrite the help, review the architecture, and
> ship it next week. The source notes and product states are not attached.

### Advisory recognition

- Observed signals: at least UX/product, communication, architecture, and
  engineering/delivery intents; missing sources/product states; fixed schedule;
  unclear “problems” and success.
- Likely primary task type: mixed / decomposition candidate; no safe dominant
  type yet.
- Material secondary aspects: UX writing, Professional Communication,
  Architecture Review, possible Engineering Review, planning.
- Likely capabilities: only provisional until deliverables and current product
  behavior are separated.
- Likely Domain Packs: none supported yet; “architecture” alone does not prove
  Software Architecture materiality.
- Research/evidence recommendation: inspect/ask before selecting depth; product
  states, source notes, actual problem evidence, architecture scope, repository,
  and release authority are missing.
- Risk/consequence recommendation: indeterminate; schedule pressure and several
  possible work surfaces exist, but affected users, systems, reversibility,
  authority, and consequence are missing.
- Review recommendation: cannot recommend final scope yet; each resulting work
  package keeps mandatory review.
- Significance: plausible across several surfaces but unsupported in detail.
- Ambiguity/decomposition: recommend split or sequence discovery/product-state
  clarification, help-content work, architecture review, and implementation/
  release only after dependencies are known.
- Confidence/negative evidence: `plausible`; no source, affected system,
  architecture decision, or shippable definition is available.
- Explicit non-decision: recognition does not split scope or block/start work.

### Chief Editor decision

Use Preflight `ask` for the smallest material clarification and source/product
state request; do not activate packs or start production. Decide decomposition
after the reply.

### Result

Pass. Ambiguity is preserved instead of hidden by a confident mixed label.

## Case 8: Multi-domain request

### Synthetic request

> Review one proposed AI support service release: RAG authorization, model
> evaluation, CI/CD secrets, deployment provenance, and fallback architecture.
> Deliver one go/no-go evidence brief, not separate reports.

### Advisory recognition

- Observed signals: one decision/deliverable with AI, cybersecurity, DevSecOps,
  software architecture, evaluation, release, and human decision evidence.
- Likely primary task type: multi-domain architecture/engineering release
  assessment.
- Material secondary aspects: Professional Analysis and Professional
  Communication.
- Likely capabilities: Architecture Review, Engineering Review, Analytical
  Reasoning, Professional Analysis, Professional Communication.
- Likely Domain Packs: AI Engineering primary for AI-system behavior;
  Cybersecurity for authorization/trust/residual risk; DevSecOps for secrets,
  delivery/provenance/deployment; Software Architecture for fallback and
  boundaries.
- Research/evidence recommendation: `full` coordinated evidence packet with
  pack-specific source limits and one integrated decision question.
- Risk/consequence recommendation: elevated because authorization, secrets,
  provenance, AI behavior, deployment, and a go/no-go release decision create
  interacting user, data, security, and operational exposure.
- Review recommendation: `deep` multi-domain review with owner-boundary checks.
- Significance: architecture, engineering, security, AI, and communication all
  material.
- Ambiguity/decomposition: do not split the requested decision brief; sequence
  evidence work by domain and separate later repairs only if the review finds
  actionable changes.
- Confidence/negative evidence: `supported`; many packs do not automatically
  mean several tasks because one go/no-go decision unifies the work.
- Explicit non-decision: no pack activation, go/no-go verdict, or release
  approval occurs automatically.

### Chief Editor decision

Keep one high-governance coordinated assessment, activate all four packs with
AI Engineering primary, select full evidence/deep review, and record pack and
capability owner boundaries.

### Result

Pass. Multi-domain context remains coherent without mandatory decomposition.

## Case 9: Research-heavy request

### Synthetic request

> Compare authoritative evidence on three approaches to reducing editorial
> review time, explain contradictions and implementation implications, and
> recommend whether any approach should be piloted.

### Advisory recognition

- Observed signals: authoritative multi-source research, comparison,
  contradiction, implications, recommendation, pilot decision.
- Likely primary task type: research synthesis and professional analysis.
- Material secondary aspects: decision communication and planning.
- Likely capabilities: Research/Evidence Classification, Analytical Reasoning,
  Professional Analysis, Professional Communication, Planning/Option
  Evaluation.
- Likely Domain Packs: none unless the approaches introduce a material accepted
  domain surface.
- Research/evidence recommendation: `full`; primary/authoritative sources,
  comparable evidence, contradictions, assumptions, disconfirmation,
  sufficiency, and implementation evidence.
- Risk/consequence recommendation: standard decision-support risk at current
  scope; a pilot may affect process and effort, but no sensitive, safety,
  security, or irreversible implementation surface is yet established.
- Review recommendation: `deep` evidence, synthesis, recommendation, and
  communication review.
- Significance: analytical and communication high; architecture/engineering
  not assumed before approaches are known.
- Ambiguity/decomposition: one coherent comparison; a pilot implementation is
  a later task after the decision.
- Confidence/negative evidence: `verified` that research is required;
  recommendation confidence remains unknown until sources are inspected.
- Explicit non-decision: no approach, pilot, pack, or implementation plan is
  selected automatically.

### Chief Editor decision

Select full research, the named capabilities, no Domain Pack initially, deep
review, and a decision brief; defer implementation.

### Result

Pass. Research depth follows the decision/evidence problem, not topic volume.

## Case 10: Many keywords but intentionally simple

### Synthetic request

> Copyedit this sentence only: “Our architecture team mentions microservices,
> Kubernetes CI/CD, zero trust, RAG, LLM evaluation, and incident severity in
> the glossary.” Keep every technical term and do not fact-check the glossary.

### Advisory recognition

- Observed signals: one supplied sentence, copyedit only, preserve terms,
  explicit no fact-check/source expansion.
- Likely primary task type: simple editing/transformation.
- Material secondary aspects: none.
- Likely capabilities: ordinary drafting/editing behavior only.
- Likely Domain Packs: none. Software Architecture, DevSecOps, Cybersecurity,
  and AI Engineering terms are mentioned but no domain claim, decision, risk,
  behavior, evidence, or review question is in scope.
- Research/evidence recommendation: `none or source-light`; source boundary is
  the supplied sentence.
- Risk/consequence recommendation: ordinary low exposure; one reversible
  sentence edit with explicit term-preservation and no fact-checking scope.
- Review recommendation: `focused` check for grammar and exact preservation of
  technical terms/scope.
- Significance: no architecture, engineering, security, AI-engineering, or
  incident significance.
- Ambiguity/decomposition: none.
- Confidence/negative evidence: `verified`; the request explicitly constrains
  output and excludes fact-checking.
- Explicit non-decision: keywords do not activate capabilities, packs, research,
  or deep review.

### Chief Editor decision

Confirm compact low-risk editing, no packs, no research stage, and focused
independent review.

### Result

Pass. Outcome and work surface override keyword density.

## Overall result

Passed: 10 of 10 cases.

- Appropriate capabilities and Domain Packs were recommended when material.
- Keyword-only cases did not trigger activation.
- Multi-domain work could remain coherent; ambiguous mixed work could be
  clarified/decomposed.
- Research/evidence and review recommendations remained qualitative and
  proportional.
- Every route/activation/depth/decomposition decision remained Chief
  Editor-owned.
- No score, threshold, classifier, automatic routing, automatic activation,
  new role, pipeline, lifecycle stage, review gate, status, or autonomous
  planning appeared.
