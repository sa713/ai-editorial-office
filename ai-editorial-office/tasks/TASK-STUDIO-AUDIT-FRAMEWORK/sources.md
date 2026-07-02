# Sources

## Scope

This research stage used only the local AI Software Studio Knowledge Base:

- `/ai-editorial-office/kb/ai-software-studio-knowledge-base/`

No current implementation audit was performed. No source outside the KB was
used to create audit criteria.

## KB Model Documents Used

| File | Used for |
| --- | --- |
| `index.md` | KB purpose, structure, durability classes, supported record types, governance notes |
| `schema.md` | required record fields, confidence, refresh requirements, application profile model |
| `navigation.md` | domain map and record inventory by type/status |
| `source-register.md` | originating external source IDs for KB records |
| `application-model.md` | working-memory model, object links, validation status values |
| `lifecycle.md` | knowledge lifecycle statuses, transitions, evidence for status changes |
| `studio-object-map.md` | canonical role/process/artifact/rule/governance object references |
| `application-register.md` | current KB record application status and validation snapshot |
| `coverage-model.md` | coverage dimensions and coverage rules |
| `development-recommendations.md` | future KB, BRD, Product Analyst, Validator, Historian usage guidance |

## KB Records Used

All 55 atomic KB records were read and classified.

| Record | Type | Main audit use |
| --- | --- | --- |
| `principle-sociotechnical-production-system` | Principle | Scope entire Studio as people/process/tools/knowledge/governance system |
| `principle-fast-feedback-loops` | Principle | Feedback, learning, review, eval, incident, discovery criteria |
| `principle-built-in-quality` | Principle | Quality embedded in work, not only final inspection |
| `principle-autonomy-with-guardrails` | Principle | Decision rights, role boundaries, escalation, AI guardrails |
| `principle-knowledge-close-to-work` | Principle | Task-local memory, source-linked artifacts, restartability |
| `pattern-small-batches` | Pattern | Work slicing, reviewability, flow, rollback |
| `pattern-continuous-delivery-pipeline` | Pattern | Build/test/security/release control and repeatability |
| `pattern-slo-error-budget` | Pattern | Reliability objectives and speed/risk tradeoffs |
| `pattern-platform-as-product` | Pattern | Internal platform/user model and capability ownership |
| `pattern-golden-paths` | Pattern | Maintained default paths with justified exceptions |
| `pattern-product-trio` | Pattern | Product/design/engineering collaboration in discovery |
| `pattern-opportunity-solution-tree` | Pattern | Outcome-opportunity-solution-experiment linkage |
| `pattern-agent-tool-loop` | Pattern | Agent reasoning/tool/action/observation loop criteria |
| `pattern-agent-computer-interface` | Pattern | Agent workspace, tools, permissions, observations |
| `pattern-human-ai-checkpoints` | Pattern | Risk-based human review/approval/steering checkpoints |
| `pattern-adr-decision-log` | Pattern | Decision memory and status/consequence traceability |
| `pattern-provenance-linked-knowledge` | Pattern | Source, claim, derivation, confidence, refresh linkage |
| `anti-pattern-single-metric-productivity` | Anti-pattern | Measurement guardrail against one-dimensional productivity |
| `anti-pattern-platform-as-ticket-queue` | Anti-pattern | Platform governance failure mode |
| `anti-pattern-portal-equals-platform` | Anti-pattern | Tool-interface mistaken for platform capability |
| `anti-pattern-agentic-overengineering` | Anti-pattern | Unjustified agency/orchestration complexity |
| `anti-pattern-checklist-theater` | Anti-pattern | Ceremonial controls and false assurance |
| `anti-pattern-feature-factory` | Anti-pattern | Output-focused product work without outcome evidence |
| `anti-pattern-knowledge-dump-kb` | Anti-pattern | Stale, weakly linked, source-free documentation |
| `anti-pattern-human-rubber-stamp-ai` | Anti-pattern | Superficial human-in-the-loop control |
| `anti-pattern-automation-without-observability` | Anti-pattern | Automation without signals, audit trail, rollback, evals |
| `practice-modern-code-review` | Practice | Change review quality and focus |
| `practice-architecture-review-by-viewpoints` | Practice | Architecture concerns/viewpoints review |
| `practice-secure-sdlc-ssdf` | Practice | Security integrated across lifecycle |
| `practice-checklists-at-pause-points` | Practice | Short critical checks at natural pause points |
| `practice-kaizen-retrospective-improvement` | Practice | Evidence-based continuous improvement cycles |
| `practice-context-and-memory-management` | Practice | Context persistence, expiry, retrieval, handoffs |
| `practice-ai-evaluation-harness` | Practice | Repeatable AI workflow evals and regressions |
| `practice-continuous-discovery` | Practice | Customer evidence, outcomes, opportunities, experiments |
| `standard-nist-ssdf` | Standard | Secure software lifecycle reference |
| `standard-iso-42010` | Standard | Architecture description concepts |
| `standard-iso-42001` | Standard | AI management-system governance |
| `standard-nist-ai-rmf` | Standard | AI risk identification, measurement, management, monitoring |
| `standard-iso-25010` | Standard | Multi-dimensional product quality model |
| `framework-space` | Framework | Balanced developer productivity measurement |
| `framework-dora-core` | Framework | Delivery system health and outcome relationship |
| `framework-diataxis` | Framework | Documentation organization by user need |
| `framework-platform-maturity` | Framework | Platform capability maturity dimensions |
| `method-a3-problem-solving` | Method | Structured problem solving and follow-up |
| `process-incident-management` | Process | Incident response, communication, learning |
| `metric-dora-four-key-metrics` | Metric | Delivery throughput/stability indicators |
| `metric-space-balanced-productivity` | Metric | Balanced productivity indicators |
| `tool-internal-developer-portal` | Tool | Portal as interface, not platform; rejected for current context |
| `tool-knowledge-graph` | Tool | Linked knowledge representation |
| `case-study-google-sre` | Case Study | Reliability/SLO/incidents reference |
| `case-study-toyota-production-system` | Case Study | Built-in quality, flow, kaizen analogy |
| `case-study-who-surgical-safety-checklist` | Case Study | Pause-point checklist analogy |
| `case-study-swe-bench-and-swe-agent` | Case Study | Coding-agent eval/interface reference |
| `decision-technique-adr` | Decision Technique | Compact decision record technique |
| `glossary-intelligent-production-system` | Glossary | Definition of Studio as intelligent production system |

## Source Limits

- The Framework may cite external source IDs only through the KB. It should not
  claim direct fresh verification of those external sources.
- KB records with `Accepted`, `Under Evaluation`, or `Rejected` status should be
  treated as audit knowledge with explicit applicability limits, not as proof
  that the Studio already implements the practice.
- Records marked Evolving or with quarterly/semiannual refresh requirements
  require freshness checks before future audit cycles rely on them.
