# Knowledge Extraction Report

Task ID: `GLOBAL_RESEARCH_INTELLIGENT_PRODUCTION_SYSTEMS`
Status: v1
Date: 2026-07-02

## Purpose

This report explains how the research corpus was converted into the first permanent AI Software Studio Knowledge Base.

Permanent KB path:

`/ai-editorial-office/kb/ai-software-studio-knowledge-base/`

## Extraction Method

1. Extract facts from source material into `facts.md`.
2. Convert facts into traceable claims in `claims_table.md`.
3. Identify recurring principles, patterns, practices, standards, metrics, anti-patterns, tools, methods, processes, case studies, decision techniques, and glossary terms.
4. Create one atomic KB record per reusable knowledge unit.
5. Add source IDs, confidence, limitations, related knowledge, and refresh requirements to every record.

## Full Knowledge Inventory

| ID | Type | Why included | Key related knowledge |
| --- | --- | --- | --- |
| `principle-sociotechnical-production-system` | Principle | Foundational explanation of why tools/processes alone do not create system quality. | fast feedback, autonomy with guardrails, DORA |
| `principle-fast-feedback-loops` | Principle | Repeated across engineering, product, SRE, AI evals, and knowledge systems. | small batches, continuous delivery, AI evals |
| `principle-built-in-quality` | Principle | Durable cross-domain pattern from TPS, DevOps, security, review, and testing. | secure SDLC, code review, continuous delivery |
| `principle-autonomy-with-guardrails` | Principle | Resolves central governance tension between speed and control. | golden paths, human-AI checkpoints, SSDF |
| `principle-knowledge-close-to-work` | Principle | Required for organizational memory and AI context reliability. | ADRs, provenance, knowledge graph |
| `pattern-small-batches` | Pattern | Recurring mechanism for reducing risk and improving feedback. | continuous delivery, code review |
| `pattern-continuous-delivery-pipeline` | Pattern | Core production-system mechanism for repeatable release flow. | DORA metrics, secure SDLC |
| `pattern-slo-error-budget` | Pattern | Converts reliability tradeoffs into explicit decisions. | Google SRE, DORA metrics |
| `pattern-platform-as-product` | Pattern | Core platform-engineering operating model. | golden paths, platform maturity |
| `pattern-golden-paths` | Pattern | Provides bounded autonomy and cognitive-load reduction. | platform as product, autonomy with guardrails |
| `pattern-product-trio` | Pattern | Reduces handoff loss in product discovery. | continuous discovery, opportunity tree |
| `pattern-opportunity-solution-tree` | Pattern | Makes product evidence and options visible. | continuous discovery, feature factory |
| `pattern-agent-tool-loop` | Pattern | Central model for modern AI agents. | AI eval harness, agentic overengineering |
| `pattern-agent-computer-interface` | Pattern | Evidence-backed factor in coding-agent performance. | SWE-bench/SWE-agent, context management |
| `pattern-human-ai-checkpoints` | Pattern | Governs AI autonomy where risk is material. | human rubber stamp, AI RMF |
| `pattern-adr-decision-log` | Pattern | Captures rationale for future reuse and review. | ADR technique, provenance |
| `pattern-provenance-linked-knowledge` | Pattern | Makes KB entries auditable and maintainable. | knowledge graph, Diataxis |
| `anti-pattern-single-metric-productivity` | Anti-pattern | Strong evidence against one-dimensional productivity metrics. | SPACE, DORA |
| `anti-pattern-platform-as-ticket-queue` | Anti-pattern | Common platform failure mode. | platform as product, golden paths |
| `anti-pattern-portal-equals-platform` | Anti-pattern | Prevents confusing a tool interface with operating capability. | internal developer portal |
| `anti-pattern-agentic-overengineering` | Anti-pattern | Strong current AI-agent warning from multiple labs. | agent tool loop, AI eval harness |
| `anti-pattern-checklist-theater` | Anti-pattern | Critical adjacent-domain translation warning. | pause-point checklists |
| `anti-pattern-feature-factory` | Anti-pattern | Product operating-model risk. | continuous discovery, product trio |
| `anti-pattern-knowledge-dump-kb` | Anti-pattern | Prevents long-document accumulation from replacing memory. | provenance, Diataxis |
| `anti-pattern-human-rubber-stamp-ai` | Anti-pattern | Exposes weak human-in-the-loop control design. | human-AI checkpoints, AI RMF |
| `anti-pattern-automation-without-observability` | Anti-pattern | Prevents hidden failure in automated production systems. | SRE, continuous delivery |
| `practice-modern-code-review` | Practice | Empirical case study supports review as quality and knowledge practice. | small batches, built-in quality |
| `practice-architecture-review-by-viewpoints` | Practice | Operationalizes ISO 42010 for review. | ISO 42010, ADRs |
| `practice-secure-sdlc-ssdf` | Practice | Turns secure-by-design into lifecycle practice. | NIST SSDF, built-in quality |
| `practice-checklists-at-pause-points` | Practice | Transferable high-reliability coordination mechanism. | WHO checklist, checklist theater |
| `practice-kaizen-retrospective-improvement` | Practice | Continuous improvement practice from Lean/TPS and DevOps lineage. | TPS, A3 |
| `practice-context-and-memory-management` | Practice | Necessary for AI agents and KB reliability. | agent-computer interface, provenance |
| `practice-ai-evaluation-harness` | Practice | Core requirement for AI-first engineering systems. | agent tool loop, SWE-bench |
| `practice-continuous-discovery` | Practice | Product practice for outcome evidence. | product trio, opportunity tree |
| `standard-nist-ssdf` | Standard | Authoritative secure software development reference. | secure SDLC |
| `standard-iso-42010` | Standard | Authoritative architecture-description reference. | architecture review |
| `standard-iso-42001` | Standard | AI management-system governance reference. | AI RMF, human-AI checkpoints |
| `standard-nist-ai-rmf` | Standard | Authoritative AI risk-management framework. | ISO 42001, AI evals |
| `standard-iso-25010` | Standard | Stable multidimensional software quality model. | built-in quality |
| `framework-space` | Framework | Balanced productivity measurement framework. | single-metric anti-pattern |
| `framework-dora-core` | Framework | Delivery performance and capability model. | DORA metrics |
| `framework-diataxis` | Framework | Documentation navigation model. | knowledge dump anti-pattern |
| `framework-platform-maturity` | Framework | Structured platform capability reflection. | platform as product |
| `method-a3-problem-solving` | Method | Adds structured problem-solving method from Lean/TPS lineage. | kaizen, TPS |
| `process-incident-management` | Process | Converts failures into response and learning. | SRE, SLOs |
| `metric-dora-four-key-metrics` | Metric | Balanced delivery throughput/stability metric set. | DORA core, SPACE |
| `metric-space-balanced-productivity` | Metric | Measurement implementation of SPACE principle. | single-metric anti-pattern |
| `tool-internal-developer-portal` | Tool | Concrete platform interface category. | portal-not-platform |
| `tool-knowledge-graph` | Tool | Enables linked, traceable KB structure. | provenance, RDF |
| `case-study-google-sre` | Case Study | Mature reliability engineering public case. | SLOs, incident management |
| `case-study-toyota-production-system` | Case Study | Adjacent production-system foundation. | built-in quality, kaizen |
| `case-study-who-surgical-safety-checklist` | Case Study | Concrete high-reliability checklist case. | pause-point checklists |
| `case-study-swe-bench-and-swe-agent` | Case Study | Evidence base for coding-agent evaluation and interfaces. | AI eval harness |
| `decision-technique-adr` | Decision Technique | Compact method for recording important decisions. | ADR decision log |
| `glossary-intelligent-production-system` | Glossary | Shared definition for the research object. | sociotechnical production system |

## Detected Contradictions

| Contradiction | KB response |
| --- | --- |
| Tool adoption versus system design | `principle-sociotechnical-production-system` makes tooling subordinate to operating system design. |
| Speed versus reliability | `pattern-slo-error-budget` and DORA metrics balance flow and stability. |
| Productivity metrics versus trust | `framework-space` and `anti-pattern-single-metric-productivity` prevent one-dimensional measurement. |
| Standardization versus autonomy | `principle-autonomy-with-guardrails`, `pattern-golden-paths`, and `pattern-platform-as-product` preserve bounded autonomy. |
| Agent autonomy versus safety | `practice-ai-evaluation-harness`, `pattern-human-ai-checkpoints`, and `anti-pattern-human-rubber-stamp-ai` define controls. |
| Checklists versus bureaucracy | `practice-checklists-at-pause-points` and `anti-pattern-checklist-theater` separate useful checklists from ritual. |
| Standards versus learning | Standards records include explicit limitations and contradiction notes. |

## Knowledge Requiring Regular Refresh

### Quarterly

- `pattern-agent-tool-loop`
- `pattern-agent-computer-interface`
- `practice-ai-evaluation-harness`
- `practice-context-and-memory-management`
- `case-study-swe-bench-and-swe-agent`
- AI-specific parts of `anti-pattern-agentic-overengineering`
- AI-specific parts of `anti-pattern-automation-without-observability`

### Semiannual

- `standard-nist-ssdf`
- `standard-iso-42001`
- `standard-nist-ai-rmf`
- `standard-iso-25010`
- `framework-platform-maturity`
- `tool-internal-developer-portal`
- `pattern-platform-as-product`
- `pattern-golden-paths`

### Annual

- Stable principles, patterns, practices, case studies, metrics, Diataxis, ADR, provenance, and glossary records.

## Fundamental Knowledge

- `principle-sociotechnical-production-system`
- `principle-fast-feedback-loops`
- `principle-built-in-quality`
- `principle-autonomy-with-guardrails`
- `principle-knowledge-close-to-work`
- `case-study-toyota-production-system`

## Fast-Aging Knowledge

- AI-agent design and orchestration records.
- Coding-agent benchmark records.
- AI eval harness design.
- AI memory and context management.
- Developer portal/tool ecosystem records.
- AI governance standards and regulatory guidance.

## Areas Requiring Additional Research

- Modern AI lab internal operating models beyond public agent guidance.
- Empirical comparison of product operating models across organization sizes.
- Engineering leadership and decision-authority frameworks.
- Research-lab knowledge management and scientific collaboration practices.
- Aviation incident/checklist practices beyond first v1 checklist sources.
- DevSecOps supply-chain practices in more depth.
- Release engineering and progressive delivery practices as their own source cluster.

## Conclusion

The KB is ready as a v1 reusable foundation. It should be treated as a living asset: useful now for future analysis and framework design, but explicitly not exhaustive and not a substitute for later targeted research.

