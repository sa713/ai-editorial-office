# Domain Knowledge Pack Standard Landscape

Date: 2026-07-09

Release: `S4.R1 - Domain Knowledge Pack Standard`

Status: research artifact for architecture synthesis.

## Research Question

What should AI Editorial Office learn from knowledge management, expert
systems, domain modeling, technical documentation, architecture knowledge,
cybersecurity knowledge bases, AI risk frameworks, and documentation governance
before defining a standard for future Domain Knowledge Packs?

The goal is not to create a domain pack. The goal is to define how future packs
can be useful, bounded, sourced, reviewable, maintained, and retired without
becoming hidden policy owners, duplicate capability owners, new roles, new
pipelines, or stale fact collections.

## Evidence Basis

Primary or authoritative sources reviewed:

- ISO, [ISO 30401:2018 Knowledge management systems - Requirements](https://www.iso.org/standard/68683.html).
- W3C, [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/).
- W3C, [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/).
- ISO, [ISO/IEC/IEEE 42010:2022 Software, systems and enterprise - Architecture description](https://www.iso.org/standard/74393.html).
- Carnegie Mellon SEI, [Documenting Software Architectures: Views and Beyond, 2nd Edition](https://www.sei.cmu.edu/library/documenting-software-architectures-views-and-beyond-second-edition/).
- Carnegie Mellon SEI, [Software Architecture in Practice, 4th Edition](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/).
- Martin Fowler, [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html).
- Microsoft Azure Architecture Center, [Use domain analysis to model microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis).
- NIST, [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29).
- NIST, [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- MITRE, [ATT&CK FAQ](https://attack.mitre.org/resources/faq/).
- OWASP, [Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/).
- NIST, [Artificial Intelligence Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1).
- Google for Developers, [About the Google developer documentation style guide](https://developers.google.com/style).
- Google for Developers, [Timeless documentation](https://developers.google.com/style/timeless-documentation).
- Google for Developers, [Prescriptive documentation](https://developers.google.com/style/prescriptive-documentation).
- Diataxis, [A systematic approach to technical documentation authoring](https://diataxis.fr/).
- U.S. Army, [Center for Army Lessons Learned](https://www.army.mil/call).
- CLIPS, [A Tool for Building Expert Systems](https://www.clipsrules.net/).

Evidence confidence: `supported` to `verified` for the source observations
above. Architecture implications for AI Editorial Office are local synthesis
from these sources plus repository governing documents, and are therefore
`supported` when they align with existing canon.

## Cross-Field Findings

### 1. Useful knowledge packages are scoped around use, not around completeness.

ISO 30401 frames knowledge management as a maintained management system rather
than a one-time library. NIST CSF uses a taxonomy of outcomes and supplemental
resources, but explicitly avoids prescribing exactly how every outcome must be
achieved. Diataxis organizes documentation around user needs rather than topic
dumping.

Implication for domain packs:

- A pack should define where it helps work and where it does not.
- A pack should prefer decision support, vocabulary, common pitfalls, evidence
  sources, and review lenses over broad encyclopedic coverage.
- "Complete domain knowledge" is a false goal. The pack should be sufficient
  for routed AI Editorial Office work and explicit about gaps.

### 2. Domain boundaries prevent semantic drift.

SKOS treats knowledge organization as concept schemes with concepts, labels,
definitions, notes, semantic relations, collections, and mappings. Domain-driven
design similarly treats model language as valid inside bounded contexts;
Fowler's bounded-context guidance emphasizes that one large unified model is
not feasible or cost-effective for large domains. Microsoft domain-analysis
guidance also warns that service boundaries and domain models require careful
business-domain thinking, not mechanical decomposition.

Implication for domain packs:

- Every pack needs a domain boundary and out-of-scope boundary.
- Terms should be defined for the pack's domain context, including synonyms,
  overloaded terms, and terms that mean something different in adjacent
  domains.
- Cross-domain mappings should be explicit and cautious. A software
  architecture term, DevSecOps term, and cybersecurity term may look similar
  while carrying different consequences.

### 3. Provenance is a first-class design requirement.

PROV-O centers provenance around entities, activities, agents, derivation,
revision, quotation, and primary source relationships. NIST SP 800-53 publishes
controls with update notes, mappings, supplemental machine-readable material,
and caution against assuming equivalency from mappings alone. MITRE ATT&CK
describes itself as a knowledge base and taxonomy grounded mainly in public
threat intelligence and incident reporting. OWASP ASVS gives versioned
requirement identifiers because identifiers may change between versions.

Implication for domain packs:

- Pack claims need source pointers and evidence confidence, not just polished
  statements.
- Source freshness, source authority, version, and last-reviewed date are part
  of the pack's content.
- Mappings to other standards, frameworks, or AI Editorial Office capabilities
  must not imply equivalence unless that equivalence is actually supported.

### 4. Packs should guide activation, not silently run everywhere.

NIST CSF Profiles tailor framework outcomes to organizational mission,
stakeholder expectations, threat landscape, and requirements. NIST AI RMF uses
profiles and lifecycle actors because risk depends on context and system stage.
Domain-driven design uses bounded contexts because a model is only coherent
within a defined context.

Implication for domain packs:

- A pack should activate only when Chief Editor or a task artifact records a
  domain materiality trigger.
- Activation should state the task question the pack helps answer.
- Non-activation is as important as activation: a pack should not load just
  because a term is mentioned.

### 5. Packs must avoid becoming policy.

Policy/control sources such as NIST SP 800-53 and OWASP ASVS show how formal
requirements, controls, and verification requirements are structured and
versioned. NIST CSF is useful precisely because it separates outcomes,
profiles, and implementation examples, and does not prescribe all actions.
AI Editorial Office already has canonical policy owners in `AGENTS.md` and
named KB files.

Implication for domain packs:

- Domain packs may summarize domain practices and source-backed guidance.
- Domain packs must not override `AGENTS.md`, lifecycle, review gate, role
  behavior, task statuses, evidence standards, or capability owners.
- If a domain claim should become canonical policy, it must be routed through
  the existing owner and reviewed as canon, not smuggled into a pack.

### 6. Packs must stay separate from capabilities and roles.

CLIPS demonstrates a classic expert-system separation: a rule-based language can
represent knowledge for expert-system behavior, but that is a system with an
inference mechanism. AI Editorial Office is not introducing a rule engine in
S4.R1. Existing repository architecture treats capabilities as reusable
operations wrapped by existing roles.

Implication for domain packs:

- A domain pack is not a role, pipeline, or capability owner.
- A pack supplies domain context, terminology, evidence sources, risks, and
  review questions to existing roles and capabilities.
- Existing capabilities such as Professional Analysis, Architecture Review,
  Engineering Review, Evidence Confidence, and Knowledge Evolution decide how
  to reason, review, validate, or evolve the work. The pack supplies domain
  material for those capabilities to use.

### 7. Staleness must be designed into the standard.

Google's timeless-documentation guidance warns against time-anchored wording
that becomes inaccurate. NIST AI RMF states that the framework is a living
document with versioning and planned review. OWASP ASVS recommends versioned
requirement references. MITRE ATT&CK publishes a stated update cadence. The
U.S. Army Center for Army Lessons Learned describes collecting, analyzing,
disseminating, integrating, and archiving lessons learned.

Implication for domain packs:

- Every pack needs last-reviewed, source freshness, stale-if triggers, update
  owner, and retirement rules.
- A pack should prefer durable principles and source classes over volatile
  facts unless the volatile fact is necessary and clearly dated.
- Retirement is a normal outcome, not a failure. Packs should be retired when
  they lose source support, duplicate better canon, or impose more maintenance
  cost than value.

### 8. Review must challenge boundaries, evidence, and maintenance cost.

Architecture-description practice emphasizes stakeholders, concerns,
viewpoints, rationale, and comprehensible documentation. SEI architecture
documentation guidance emphasizes capturing architecture so others can build,
use, and maintain systems. Google documentation guidance places
project-specific guidance above general style guidance and recommends clarity
and consistency for domain readers. NIST and OWASP sources show that catalogs
and standards need versioning, mappings, and caution around applicability.

Implication for domain packs:

- Review should ask whether the pack's domain boundary, source evidence,
  activation criteria, update path, and forbidden content are valid.
- Review should reject packs that read like loose research notes, permanent
  policies, role specs, capability specs, or unchecked advice.
- Review should validate against at least representative scenarios before a
  pack is accepted.

## What A Domain Pack Should Contain

Minimum useful content:

- pack identity, purpose, intended use, and non-goals;
- activation and non-activation criteria;
- domain boundary and adjacent-domain boundaries;
- source register with authority, freshness, version/date, and relevance;
- key terminology and overloaded terms;
- durable domain principles or heuristics, each source-backed or caveated;
- common failure modes, risks, and misconceptions;
- review questions or domain challenge prompts;
- evidence expectations and confidence limits;
- update triggers, stale-if triggers, and retirement conditions;
- relation to existing AI Editorial Office capabilities and canonical owners.

Optional content:

- compact examples, only when source-backed and stable enough;
- mappings to external frameworks or standards, with equivalence caveats;
- pack-specific source-search patterns;
- scenario validation notes for future pack acceptance.

## What A Domain Pack Must Not Contain

Forbidden content:

- new roles, pipelines, lifecycle stages, review gates, or mandatory ordinary
  task artifacts;
- policy that overrides `AGENTS.md` or canonical KB owners;
- capability ownership or duplicated capability instructions;
- task status rules or lifecycle transition rules;
- client-profile rules unless the pack is explicitly a client profile, which
  domain packs are not;
- unsourced fact collections;
- volatile claims without dates, versions, or stale-if triggers;
- confidential or private source content unless the task and owner explicitly
  authorize it;
- broad "best practice" commands that hide evidence limits, context limits, or
  domain disagreement;
- automatic canon-promotion rules.

## Source-Specific Lessons

| Source area | Lesson for S4.R1 |
| --- | --- |
| ISO 30401 knowledge management | Treat domain knowledge as maintained organizational knowledge, not a static dump. |
| SKOS | Use concept, definition, scope, relation, and mapping discipline without requiring formal ontology tooling. |
| PROV-O | Preserve source/provenance chain: source, derivation, revision, quotation, and primary-source relationships where material. |
| DDD bounded context | Require domain boundaries and term validity boundaries; avoid one unified mega-pack. |
| ISO 42010 and SEI architecture docs | Tie knowledge views to stakeholder concerns, rationale, and maintainability. |
| NIST CSF | Use taxonomy, profiles, and informative references as a model for non-prescriptive, context-tailored guidance. |
| NIST SP 800-53 | Version catalogs, mapping cautions, and machine-readable supplements show how structured knowledge avoids ambiguity. |
| MITRE ATT&CK | A domain knowledge base should have taxonomy, public source basis, contribution/update model, and explicit scope. |
| OWASP ASVS | Versioned identifiers prevent stale or ambiguous requirement references. |
| NIST AI RMF | Living documents need versioning, planned review, and lifecycle/context awareness. |
| Google documentation guidance | Prefer current-state, durable language and hierarchy of guidance; avoid ambiguous prescriptions. |
| Diataxis | Organize by user need, not by topic accumulation. |
| U.S. Army CALL | Lessons become useful through collection, analysis, dissemination, integration, and archiving. |
| CLIPS/expert systems | Do not confuse a knowledge package with a rule engine or automated inference owner. |

## Implications For AI Editorial Office

1. The standard should live in `kb/domain_knowledge_pack_standard.md` as the
   canonical owner for domain-pack structure, activation, evidence, maintenance,
   and retirement.
2. `AGENTS.md` should only name the owner and governance consequence in the
   canonical ownership map and entry/routing discipline.
3. `capability_registry.md` should clarify that domain packs are not
   capabilities. Existing capabilities consume domain-pack context when active.
4. `shared_lifecycle_kernel.md` and `task_object_model.md` only need lightweight
   references for optional active domain-pack context if that improves
   discoverability.
5. `review_pipeline.md` should challenge domain-pack use when a reviewed
   artifact depends on it.
6. The standard may include a compact template, but should not create a
   separate framework, registry, validator, or required ordinary task artifact.
7. `/about` sync is required only if changed canonical files are copied into the
   memory package or summary files must mention the new standard.

## Validation Hypotheses

Software Architecture Domain Pack should pass the standard if it can:

- bound architecture concepts separately from Engineering Review;
- cite architecture sources such as ISO 42010, SEI, and local Architecture
  Review canon;
- provide source-backed architecture terminology, drivers, quality attributes,
  risks, and review prompts;
- avoid becoming an Architecture Review capability owner.

DevSecOps Domain Pack should pass the standard if it can:

- bound delivery, automation, configuration, operations, and security-in-delivery
  topics separately from Engineering Review and cybersecurity policy;
- cite sources such as NIST CSF, NIST SP 800-53 where relevant, OWASP, and
  delivery/operations sources;
- provide activation triggers for DevSecOps-sensitive work;
- avoid becoming a security policy owner, DevOps role, or engineering review
  gate.

## Research Sufficiency Judgment

The research is sufficient for S4.R1 architecture synthesis. The external
sources converge on the same design pattern: domain knowledge must be scoped,
source-backed, versioned, context-activated, reviewable, and maintainable. The
repository governing documents add the local constraint that this pattern must
fit inside existing role, lifecycle, review, capability, and `/about` boundaries
without creating new owners or process layers.
