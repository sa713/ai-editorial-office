# Annotated Source Register

Task ID: `GLOBAL_RESEARCH_INTELLIGENT_PRODUCTION_SYSTEMS`
Owner role: `research_agent`
Status: v1 source register
Last updated: 2026-07-02

## Selection Rules

- Prefer books, standards, peer-reviewed papers, official documentation, and primary engineering publications.
- Use company blogs when they describe concrete engineering practice or current product guidance.
- Treat vendor and consulting sources as useful but potentially biased.
- Mark rapidly changing AI and tooling sources for recurring refresh.

## Sources

### S01 - DORA Research Program

- Title: DORA Research Program and archive
- Author/organization: Google Cloud / DORA
- Year: ongoing, archive through 2025
- Type: longitudinal research program
- Link: https://dora.dev/research/
- Description: Multi-year research on software delivery, operational performance, capabilities, and organizational outcomes.
- Reason included: Canonical source for engineering performance research and the balance between throughput, stability, and organizational capability.
- Trust level: high
- Limitations: Survey and model-based research; correlations need local interpretation and should not be treated as deterministic laws.

### S02 - 2025 DORA AI-assisted Software Development Report

- Title: 2025 DORA Report: AI-assisted software development
- Author/organization: Google Cloud / DORA
- Year: 2025
- Type: research report
- Link: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report
- Description: Recent DORA research on AI use in software delivery, AI capabilities, value-stream management, and systems effects.
- Reason included: Current evidence that AI adoption is a sociotechnical change, not merely tool installation.
- Trust level: high for current trend direction
- Limitations: Very current; conclusions may shift as tools and practices mature.

### S03 - Accelerate

- Title: Accelerate: The Science of Lean Software and DevOps
- Author/organization: Nicole Forsgren, Jez Humble, Gene Kim
- Year: 2018
- Type: book / research synthesis
- Link: https://itrevolution.com/product/accelerate/
- Description: Research-backed model connecting technical practices, lean management, culture, and software delivery performance.
- Reason included: Foundational source for modern DevOps, continuous delivery, and measurement.
- Trust level: high
- Limitations: Based on a particular research program and period; metrics can be abused if detached from context.

### S04 - Site Reliability Engineering

- Title: Site Reliability Engineering
- Author/organization: Google
- Year: 2016
- Type: engineering book
- Link: https://sre.google/sre-book/table-of-contents/
- Description: Google's public account of reliability practices including SLOs, toil, automation, release engineering, incident response, and postmortems.
- Reason included: Mature model of production operations as engineering discipline.
- Trust level: high
- Limitations: Google-scale practices require adaptation for smaller or different organizations.

### S05 - Service Level Objectives

- Title: Service Level Objectives
- Author/organization: Google SRE
- Year: 2016
- Type: book chapter
- Link: https://sre.google/sre-book/service-level-objectives/
- Description: Defines SLIs, SLOs, error budgets, and user-centered reliability targets.
- Reason included: Core decision mechanism for reliability tradeoffs.
- Trust level: high
- Limitations: Requires measurable services and disciplined product-engineering negotiation.

### S06 - Secure Software Development Framework

- Title: NIST SP 800-218 Secure Software Development Framework
- Author/organization: NIST
- Year: 2022
- Type: official standard/guidance
- Link: https://csrc.nist.gov/pubs/sp/800/218/final
- Description: High-level secure software development practices integrated across the SDLC.
- Reason included: Authoritative secure-by-design reference.
- Trust level: very high
- Limitations: Framework-level guidance; implementation needs domain-specific controls and threat models.

### S07 - Architecture Description

- Title: ISO/IEC/IEEE 42010:2022
- Author/organization: ISO/IEC/IEEE
- Year: 2022
- Type: international standard
- Link: https://www.iso.org/standard/74393.html
- Description: Standard for architecture descriptions, stakeholders, concerns, viewpoints, and views.
- Reason included: Stable foundation for architecture review and decision traceability.
- Trust level: very high
- Limitations: Standard is abstract and can become documentation-heavy if applied mechanically.

### S08 - SPACE of Developer Productivity

- Title: The SPACE of Developer Productivity
- Author/organization: Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, Jenna Butler
- Year: 2021
- Type: peer-reviewed/ACM article
- Link: https://queue.acm.org/detail.cfm?id=3454124
- Description: Framework with Satisfaction, Performance, Activity, Communication/collaboration, and Efficiency/flow dimensions.
- Reason included: Strong corrective to single-metric productivity measurement.
- Trust level: high
- Limitations: Measurement still requires local construct validity and qualitative interpretation.

### S09 - Software Engineering at Google

- Title: Software Engineering at Google
- Author/organization: Titus Winters, Tom Manshreck, Hyrum Wright / Google
- Year: 2020
- Type: engineering book
- Link: https://abseil.io/resources/swe-book/html/toc.html
- Description: Lessons on sustainable engineering, code review, documentation, testing, tooling, and scale.
- Reason included: Practical reference for long-lived software organizations.
- Trust level: high
- Limitations: Many examples come from Google's scale and culture.

### S10 - Modern Code Review at Google

- Title: Modern Code Review: A Case Study at Google
- Author/organization: Caitlin Sadowski et al. / Google
- Year: 2018
- Type: empirical case study
- Link: https://research.google/pubs/modern-code-review-a-case-study-at-google/
- Description: Empirical description of review motivations, workflow, effects, and developer perceptions at Google.
- Reason included: Evidence-based view of code review as quality, knowledge-sharing, and ownership practice.
- Trust level: high
- Limitations: Single-company case study.

### S11 - Platforms White Paper

- Title: Platforms White Paper
- Author/organization: CNCF TAG App Delivery
- Year: 2023
- Type: industry white paper
- Link: https://tag-app-delivery.cncf.io/whitepapers/platforms/
- Description: Defines internal platforms, platform capabilities, users, benefits, and reduction of cognitive load.
- Reason included: Strong current reference for internal developer platforms and platform engineering.
- Trust level: high
- Limitations: Cloud-native community perspective; not all organizations need the same platform shape.

### S12 - Platform Engineering Maturity Model

- Title: Platform Engineering Maturity Model
- Author/organization: CNCF TAG App Delivery
- Year: 2024
- Type: maturity model
- Link: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
- Description: Reflective maturity model across investment, adoption, interfaces, operations, and measurement.
- Reason included: Useful for separating platform capability from cargo-cult adoption.
- Trust level: medium-high
- Limitations: Maturity models can be misused as ladder-chasing.

### S13 - Common Myths About Platform Engineering

- Title: Common myths about platform engineering
- Author/organization: Google Cloud
- Year: 2023
- Type: engineering blog
- Link: https://cloud.google.com/blog/products/application-development/common-myths-about-platform-engineering
- Description: Clarifies platform engineering misconceptions, including developer portal versus platform and platform-as-product thinking.
- Reason included: Helps identify anti-patterns in IDP adoption.
- Trust level: medium-high
- Limitations: Vendor blog; examples may align with cloud platform interests.

### S14 - Continuous Discovery

- Title: Continuous Discovery Habits
- Author/organization: Teresa Torres / Product Talk
- Year: 2021 and ongoing site material
- Type: product method/book-derived guidance
- Link: https://www.producttalk.org/continuous-discovery/
- Description: Continuous customer connection, product trio collaboration, and outcome-oriented discovery.
- Reason included: Strong product counterweight to feature-factory delivery.
- Trust level: medium-high
- Limitations: Method guidance with less formal evidence than standards or peer-reviewed research.

### S15 - Opportunity Solution Trees

- Title: Opportunity Solution Trees
- Author/organization: Teresa Torres / Product Talk
- Year: 2016 and updated guidance
- Type: product discovery method
- Link: https://www.producttalk.org/opportunity-solution-trees/
- Description: Visual structure linking desired outcomes, customer opportunities, solution ideas, and experiments.
- Reason included: Concrete decision technique for discovery and option management.
- Trust level: medium-high
- Limitations: Requires real customer evidence; can become decorative if not updated.

### S16 - Product vs Feature Teams

- Title: Product vs Feature Teams
- Author/organization: Marty Cagan / Silicon Valley Product Group
- Year: 2017
- Type: product leadership article
- Link: https://www.svpg.com/product-vs-feature-teams/
- Description: Contrasts empowered product teams with teams that mainly implement stakeholder feature requests.
- Reason included: Useful source for feature-factory anti-pattern and product operating model design.
- Trust level: medium
- Limitations: Strong practitioner viewpoint; not a neutral empirical study.

### S17 - A Practical Guide to Building Agents

- Title: A Practical Guide to Building Agents
- Author/organization: OpenAI
- Year: 2025
- Type: official guide
- Link: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- Description: Agent definition, when to build agents, tools, instructions, orchestration, guardrails, evals, and multi-agent guidance.
- Reason included: Primary current AI-agent engineering guidance.
- Trust level: high for OpenAI stack and general agent design heuristics
- Limitations: Vendor guidance; AI tooling evolves quickly.

### S18 - OpenAI Agents SDK Guide

- Title: Agents SDK documentation
- Author/organization: OpenAI
- Year: current as of 2026-07-02
- Type: official documentation
- Link: https://platform.openai.com/docs/guides/agents
- Description: Current platform documentation for agent orchestration, tools, context, guardrails, and evaluations.
- Reason included: Current operational reference for AI-first engineering systems.
- Trust level: high for product behavior
- Limitations: Rapidly changing documentation and API surface.

### S19 - Building Effective Agents

- Title: Building Effective Agents
- Author/organization: Anthropic
- Year: 2024
- Type: AI lab engineering article
- Link: https://www.anthropic.com/research/building-effective-agents
- Description: Practical patterns for workflows and agents, emphasizing simple designs, tool feedback, evaluation, and complexity control.
- Reason included: Strong counterbalance to over-complex multi-agent designs.
- Trust level: high for modern AI engineering practice
- Limitations: Vendor perspective; examples reflect model capabilities at publication time.

### S20 - Claude Code Overview

- Title: Claude Code overview
- Author/organization: Anthropic
- Year: current as of 2026-07-02
- Type: official documentation
- Link: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview
- Description: Documentation for an agentic coding tool that reads codebases, edits files, and runs commands.
- Reason included: Current reference for coding-agent interaction model, permissions, memory, and context.
- Trust level: high for product behavior
- Limitations: Product-specific and rapidly changing.

### S21 - SWE-bench

- Title: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- Author/organization: Jimenez et al.
- Year: 2023
- Type: arXiv research paper / benchmark
- Link: https://arxiv.org/abs/2310.06770
- Description: Benchmark of real GitHub issues requiring repository understanding, long context, and environment interaction.
- Reason included: Important evidence about the gap between coding demos and real software maintenance.
- Trust level: high as benchmark source
- Limitations: Benchmark may not represent all engineering work and is subject to saturation over time.

### S22 - SWE-agent

- Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- Author/organization: Yang et al.
- Year: 2024
- Type: arXiv research paper
- Link: https://arxiv.org/abs/2405.15793
- Description: Demonstrates that agent-computer interface design materially affects coding-agent performance.
- Reason included: Supports treating agent environment design as core engineering work.
- Trust level: medium-high
- Limitations: Results age quickly as models, benchmarks, and tools evolve.

### S23 - AI Risk Management Framework

- Title: Artificial Intelligence Risk Management Framework
- Author/organization: NIST
- Year: 2023
- Type: official framework
- Link: https://www.nist.gov/itl/ai-risk-management-framework
- Description: Voluntary framework for trustworthy and responsible AI risk management.
- Reason included: Authoritative governance vocabulary for AI systems.
- Trust level: very high
- Limitations: Voluntary framework; not a full implementation manual.

### S24 - AI Management System

- Title: ISO/IEC 42001:2023
- Author/organization: ISO/IEC
- Year: 2023
- Type: international management-system standard
- Link: https://www.iso.org/standard/42001
- Description: Standard for establishing, implementing, maintaining, and improving an AI management system.
- Reason included: Stable governance reference for organizations using or providing AI.
- Trust level: very high
- Limitations: Certification-oriented systems can become compliance theater if detached from real risk.

### S25 - Toyota Production System

- Title: Toyota Production System
- Author/organization: Toyota
- Year: current public description, based on long-running operating system
- Type: official company practice description
- Link: https://global.toyota/en/company/vision-and-philosophy/production-system/
- Description: Production philosophy based on waste elimination, jidoka, just-in-time, kaizen, and human-centered automation.
- Reason included: Foundational adjacent discipline for intelligent production systems.
- Trust level: high for stated Toyota principles
- Limitations: Direct transfer to software can be misleading without abstraction.

### S26 - The Checklist Manifesto

- Title: The Checklist Manifesto
- Author/organization: Atul Gawande
- Year: 2009
- Type: book
- Link: https://atulgawande.com/book/the-checklist-manifesto/
- Description: Cross-domain argument that well-designed checklists improve reliability in complex work.
- Reason included: Adjacent practice for quality gates, review, and high-stakes workflows.
- Trust level: medium-high
- Limitations: Book-level synthesis; implementation details need domain-specific validation.

### S27 - WHO Surgical Safety Checklist

- Title: WHO Surgical Safety Checklist and implementation resources
- Author/organization: World Health Organization
- Year: 2009 and updates
- Type: official checklist and implementation guidance
- Link: https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery/tool-and-resources
- Description: Nineteen-item checklist designed to reduce surgical errors and improve team communication.
- Reason included: Concrete example of checklist as pause point, not paperwork.
- Trust level: high
- Limitations: Clinical context; software adoption requires careful translation.

### S28 - Documenting Architecture Decisions

- Title: Documenting Architecture Decisions
- Author/organization: Michael Nygard
- Year: 2011
- Type: practitioner article
- Link: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Description: Introduces short architecture decision records with context, decision, status, and consequences.
- Reason included: Foundational practical source for decision logs.
- Trust level: medium-high
- Limitations: Practitioner format, not a formal standard.

### S29 - ADR GitHub Organization

- Title: Architecture Decision Records
- Author/organization: ADR GitHub community
- Year: ongoing
- Type: community resource
- Link: https://adr.github.io/
- Description: Hub for ADR templates, tools, and related practices.
- Reason included: Shows broad adoption and variants of decision-record practice.
- Trust level: medium
- Limitations: Community-curated; quality varies by linked resource.

### S30 - Diataxis

- Title: Diataxis
- Author/organization: Daniele Procida
- Year: ongoing
- Type: documentation framework
- Link: https://diataxis.fr/
- Description: Classifies documentation into tutorials, how-to guides, explanation, and reference.
- Reason included: Useful structure for knowledge-base navigation and reducing documentation ambiguity.
- Trust level: medium-high
- Limitations: Framework is conceptual; does not replace content governance.

### S31 - PROV Overview

- Title: PROV Overview
- Author/organization: W3C
- Year: 2013
- Type: W3C standard overview
- Link: https://www.w3.org/TR/prov-overview/
- Description: Provenance model for representing entities, activities, agents, and derivations.
- Reason included: Stable vocabulary for source traceability and knowledge trust.
- Trust level: very high
- Limitations: Full provenance modeling may be too heavy for a first KB version.

### S32 - RDF 1.1 Concepts

- Title: RDF 1.1 Concepts and Abstract Syntax
- Author/organization: W3C
- Year: 2014
- Type: W3C recommendation
- Link: https://www.w3.org/TR/rdf11-concepts/
- Description: Core graph data model based on triples and linked resources.
- Reason included: Conceptual foundation for knowledge graphs and linked KB entries.
- Trust level: very high
- Limitations: RDF implementation is optional; graph discipline can be applied without full semantic-web stack.

### S33 - ISO/IEC 25010

- Title: ISO/IEC 25010 product quality model
- Author/organization: ISO/IEC
- Year: 2011, revised by 2023 standards
- Type: international standard / quality model
- Link: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
- Description: Quality model covering functional suitability, performance, compatibility, usability, reliability, security, maintainability, and portability.
- Reason included: Stable multidimensional language for quality engineering.
- Trust level: high
- Limitations: ISO site notes 2011 version has been revised; exact model version should be refreshed.

### S34 - ISO/IEC/IEEE 29119

- Title: ISO/IEC/IEEE 29119 Software and systems engineering - Software testing
- Author/organization: ISO/IEC/IEEE
- Year: 2022
- Type: international testing standard
- Link: https://www.iso.org/standard/45142.html
- Description: Standard vocabulary and concepts for software testing.
- Reason included: Useful reference point for test process and terminology.
- Trust level: high
- Limitations: Standards can encourage ceremony if not fitted to product risk.

### S35 - Backstage Documentation

- Title: What is Backstage?
- Author/organization: Backstage project
- Year: current as of 2026-07-02
- Type: tool documentation
- Link: https://backstage.io/docs/overview/what-is-backstage/
- Description: Developer portal for software catalogs, templates, docs, and plugin-based developer experience.
- Reason included: Concrete example of an internal developer portal tool.
- Trust level: high for tool behavior
- Limitations: A portal is not itself a complete platform operating model.

