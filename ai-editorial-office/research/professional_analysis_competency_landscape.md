# Professional Analysis Competency Landscape

Date: 2026-07-08

Status: research artifact only. This file does not modify canon, roles,
pipelines, lifecycle, review gate, `/about`, or implementation behavior.

## Executive Summary

Professional analytical practice converges on a stable pattern: define the
decision need, structure the problem, inspect evidence, synthesize what matters,
compare options or interpretations, state implications and risks, and present a
recommendation or judgment calibrated to confidence.

For AI Editorial Office, this should not become a new Analyst role or a bundle
of separate consulting, business analysis, policy analysis, product discovery,
intelligence, decision analysis, and technology assessment capabilities. Those
areas are better represented as lenses inside one Professional Analysis
capability.

The capability should complement existing architecture:

- Analytical Reasoning owns reasoning moves and inspectability.
- Professional Analysis owns the shape of decision-ready analytical products.
- Evidence, planning, audience/outcome alignment, quality attributes,
  Architecture Review, and Engineering Review keep their current ownership.
- Chief Editor activates Professional Analysis when a task needs structured
  interpretation, synthesis, recommendation, or decision support.
- Review Agent challenges the analysis inside the existing review gate.

## Source Basis

Primary and authoritative external sources used:

| Source | Used for |
| --- | --- |
| IIBA BABOK overview, `https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/` | Business analysis as needs, value, stakeholders, requirements, and solution context. |
| HM Treasury Green Book, `https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government` | Appraisal, options, value, evaluation, and decision support in public-sector analysis. |
| UK Aqua Book, `https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government` | Analytical quality assurance, models, evidence, assumptions, and proportionate assurance. |
| CIA Tradecraft Primer, `https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf` | Structured analytic techniques, assumptions, alternatives, indicators, and bias reduction. |
| NASA Decision Analysis, `https://www.nasa.gov/reference/6-8-decision-analysis/` | Alternatives, decision criteria, uncertainty, and decision quality for technical programs. |
| GAO Technology Assessment Design Handbook, `https://www.gao.gov/products/gao-20-246g` | Technology assessment structure, policy context, stakeholder effects, and implications. |
| GOV.UK Service Manual discovery guidance, `https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works` | Product/service discovery before solution commitment. |

Internal sources reused:

- `kb/analytical_reasoning.md`;
- `kb/editorial_evidence_framework.md`;
- `kb/editorial_planning_framework.md`;
- `kb/audience_outcome_alignment.md`;
- `kb/editorial_quality_attributes.md`;
- `kb/architecture_review.md`;
- `kb/engineering_review.md`;
- `kb/capability_registry.md`;
- `ROADMAP.md`;
- `BACKLOG.md`;
- `project-state.md`.

## Domain Findings

### Management Consulting And Strategic Analysis

Professional signal: consulting-style analysis is decision-led. It frames the
business problem, identifies drivers and constraints, synthesizes evidence into
insights, compares options, and communicates a recommendation, risks, and next
steps to a decision-maker.

AI Editorial Office relevance:

- The office increasingly handles strategy, roadmap, system, product, and
  implementation decisions.
- The useful reusable capability is not a consulting framework; it is a
  disciplined analytical product shape.
- This should improve recommendation quality without creating a consultant
  role or mandatory slide-deck style artifact.

Decision: include as Professional Analysis lenses for situation assessment,
options/recommendation, and executive decision brief.

### Business Analysis

Professional signal: business analysis connects stakeholder needs, value,
requirements, constraints, change, and solution fit. It separates the need or
problem from the proposed solution.

AI Editorial Office relevance:

- Many project tasks require understanding what a requested change is for,
  whether it serves a user or project need, and what outcome would count as
  useful.
- Existing audience/outcome and planning canon already cover part of this.
  Professional Analysis should add a bounded business/needs-analysis lens
  rather than duplicate those owners.

Decision: include as a lens. Do not create a separate Business Analysis
capability or role.

### Policy Analysis

Professional signal: policy analysis and appraisal compare options, impacts,
constraints, risks, evidence strength, and value. The Green Book and Aqua Book
emphasize proportionate analysis, quality assurance, assumptions, and
decision-support evidence.

AI Editorial Office relevance:

- Some future tasks may involve policy, governance, operational rules, or
  organizational impact.
- The office should be able to produce impact-aware analysis without becoming a
  legal, regulatory, or public-policy authority.

Decision: include policy/impact analysis as a lens. Postpone deep regulatory or
legal-domain analysis to future domain packs or source-backed tasks.

### Intelligence Products And Structured Analytic Techniques

Professional signal: intelligence analysis uses structured techniques to reduce
bias, expose assumptions, compare alternatives, preserve uncertainty, and
communicate confidence.

AI Editorial Office relevance:

- The reasoning techniques are already owned by Analytical Reasoning.
- Professional Analysis should use those moves to produce usable assessments,
  judgments, indicators, and decision briefs when the task calls for them.

Decision: do not duplicate Analytical Reasoning. Include intelligence-product
style situation assessment and uncertainty communication as Professional
Analysis product lenses.

### Product Discovery

Professional signal: discovery clarifies user needs, service context,
constraints, risks, and whether a solution should be built before committing to
delivery.

AI Editorial Office relevance:

- Product and UX tasks often fail when they jump from a prompt to a solution.
- Existing audience/outcome alignment and planning already support this.
  Professional Analysis can add a product-discovery lens that structures the
  problem, users, constraints, opportunity, and success signals.

Decision: include as a lens. Do not create a new discovery pipeline.

### Technology Assessment

Professional signal: technology assessment evaluates a technology's purpose,
readiness, benefits, limitations, risks, alternatives, stakeholder effects, and
policy or operational implications.

AI Editorial Office relevance:

- Future AI, software, cybersecurity, and DevSecOps domain packs will need
  deeper technical knowledge.
- Professional Analysis can provide the assessment product shape, while domain
  expertise supplies specialized evidence.

Decision: include a technology-assessment lens. Postpone deep technology-domain
expertise to Stage 4 domain packs.

### Decision Analysis

Professional signal: decision analysis defines alternatives, criteria,
uncertainty, tradeoffs, and decision quality. It is strongest when the decision
is consequential, ambiguous, or evidence-limited.

AI Editorial Office relevance:

- Existing planning canon owns option generation and evaluation.
- Professional Analysis should package decision analysis into recommendation
  products without replacing the planning owner.

Decision: include as options/recommendation and executive decision brief
lenses. Keep option-generation rules in the planning framework.

### Executive Analytical Communication

Professional signal: strong analytical communication leads with the decision
need, bottom line, evidence level, recommendation, risk, and next action.
Supporting detail exists to make the conclusion reviewable, not to bury it.

AI Editorial Office relevance:

- Many outputs must be useful to a Project Lead, reviewer, implementer,
  stakeholder, or public reader.
- Audience/outcome alignment owns reader fit; Professional Analysis should
  make analytical artifacts decision-ready for that reader.

Decision: include executive decision brief as a lens. Do not create a new
communication capability here; Professional Communication remains a later
roadmap release.

## Candidate Capability Disposition

| Candidate area | Disposition | Rationale |
| --- | --- | --- |
| Management consulting analysis | Merged lens | Valuable for problem framing, synthesis, options, recommendation, and executive brief; a standalone capability would add framework sprawl. |
| Business analysis | Merged lens | Needs/value/stakeholder analysis fits Professional Analysis but should not duplicate audience/outcome or planning owners. |
| Strategic analysis | Merged lens | Strategy products are decision-support outputs, not a separate role or pipeline. |
| Policy analysis | Merged lens | Impact and option appraisal fit; legal/regulatory depth remains source- and domain-dependent. |
| Intelligence products | Partially merged | Product shape and uncertainty communication fit; cognitive methods remain Analytical Reasoning. |
| Product discovery | Merged lens | Problem/user/constraint discovery fits; no new pipeline needed. |
| Technology assessment | Trigger-based lens | Product shape fits; deep domain evidence is postponed to domain packs. |
| Decision analysis | Partially merged | Recommendations and decision briefs fit; option evaluation remains owned by planning canon. |
| Executive analytical communication | Merged lens | Decision-ready presentation fits; broader communication capability remains future roadmap work. |

## Postponed Or Rejected Items

Postponed:

- deep domain packs for software architecture, DevSecOps, cybersecurity, and AI
  engineering;
- quantitative financial modeling, market sizing, statistical modeling, and
  economic modeling unless a task supplies evidence and scope;
- legal, regulatory, and compliance-specific analysis without authoritative
  source grounding;
- competitive intelligence as a standalone capability;
- automated scoring, templates, or analysis checklists.

Rejected for this release:

- a new Analyst, Consultant, Business Analyst, Policy Analyst, Product
  Strategist, Intelligence Analyst, or Technology Analyst role;
- separate capabilities for every analytical domain;
- a mandatory professional-analysis artifact;
- a consulting framework owner;
- duplicating Analytical Reasoning, planning, evidence, audience/outcome,
  Architecture Review, or Engineering Review.

## Architecture Implication

Professional Analysis should be implemented as one shared capability with
optional lenses:

- situation assessment;
- synthesis brief;
- options and recommendation;
- business or needs analysis;
- policy or impact analysis;
- product discovery analysis;
- technology assessment;
- executive decision brief.

This gives AI Editorial Office stronger professional analytical output without
changing the architecture.
