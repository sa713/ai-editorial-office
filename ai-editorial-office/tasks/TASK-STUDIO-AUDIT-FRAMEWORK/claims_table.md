# Claims Table

This table maps planned Framework criteria to KB support. It is not an audit of
the current Studio.

Support labels:

- `direct`: KB record directly supports the criterion.
- `supporting`: KB record supports part of the criterion.
- `analogical`: KB case study or adjacent-domain record supports the criterion
  only as an analogy.
- `gap`: KB is insufficient for a strong criterion; the Framework may only name
  the gap or define an audit question.

| Criterion ID | Planned criterion | Support | KB basis | Applicability limits |
| --- | --- | --- | --- | --- |
| GOV-01 | Studio is treated as a sociotechnical production system with people, process, tools, knowledge, feedback, and governance in scope. | direct | `glossary-intelligent-production-system`, `principle-sociotechnical-production-system` | Does not prescribe exact roles/tools. |
| GOV-02 | Decision rights, role boundaries, guardrails, escalation, and review authority are explicit. | direct | `principle-autonomy-with-guardrails`, `pattern-human-ai-checkpoints`, `anti-pattern-human-rubber-stamp-ai` | Guardrail depth depends on risk/reversibility. |
| GOV-03 | Human checkpoints are meaningful, evidence-based, and not rubber-stamp approvals. | direct | `pattern-human-ai-checkpoints`, `anti-pattern-human-rubber-stamp-ai`, `practice-ai-evaluation-harness` | Human review may be lighter for low-risk/evaluated automation. |
| GOV-04 | Common work has maintained golden paths with justified exceptions. | direct | `pattern-golden-paths`, `principle-autonomy-with-guardrails`, `anti-pattern-checklist-theater` | Novel work may require escape hatches. |
| KNO-01 | Reusable knowledge is source-linked, atomic enough to reuse, and governed for freshness. | direct | `principle-knowledge-close-to-work`, `pattern-provenance-linked-knowledge`, `anti-pattern-knowledge-dump-kb`, `schema.md` | Do not split records so far that meaning is lost. |
| KNO-02 | Knowledge application status, validation status, and object links are maintained. | direct | `application-model.md`, `lifecycle.md`, `application-register.md`, `coverage-model.md`, `studio-object-map.md` | Status indicates Studio application, not universal truth. |
| KNO-03 | Context and memory are intentionally persisted, expired, retrieved, and protected against stale/hallucinated memory. | direct | `practice-context-and-memory-management`, `principle-knowledge-close-to-work` | AI memory practice is evolving; refresh quarterly. |
| KNO-04 | Decision rationale is preserved for consequential architecture, process, platform, AI, and governance decisions. | direct | `pattern-adr-decision-log`, `decision-technique-adr`, `standard-iso-42010` | No canonical ADR artifact currently exists; may be a KB gap. |
| AI-01 | Agentic workflows are justified by task ambiguity/tool needs and not used where deterministic workflows suffice. | direct | `pattern-agent-tool-loop`, `anti-pattern-agentic-overengineering` | Threshold changes as models/tools improve. |
| AI-02 | Agent workspace/tool interface exposes actions, observations, permissions, and stopping conditions. | direct | `pattern-agent-computer-interface`, `case-study-swe-bench-and-swe-agent` | Under Evaluation in KB; implementation-specific. |
| AI-03 | AI-assisted workflows have repeatable evals, benchmark tasks, human rubrics, and regression checks before autonomy expands. | direct | `practice-ai-evaluation-harness`, `case-study-swe-bench-and-swe-agent`, `standard-nist-ai-rmf` | Local eval design is a KB gap. |
| AI-04 | AI outputs and actions are auditable through provenance, logs, review trails, or equivalent evidence. | direct | `anti-pattern-automation-without-observability`, `pattern-provenance-linked-knowledge`, `pattern-human-ai-checkpoints` | Low-risk visible automation can use lighter evidence. |
| QUA-01 | Quality controls are embedded in work, not only applied as final inspection. | direct | `principle-built-in-quality`, `practice-secure-sdlc-ssdf`, `pattern-continuous-delivery-pipeline` | Built-in quality does not remove independent review. |
| QUA-02 | Review practices are timely, focused, independent where needed, and not style-policing bottlenecks. | direct | `practice-modern-code-review`, `principle-built-in-quality`, `pattern-small-batches` | Code-review record is accepted, not fully mapped to Studio code practice. |
| QUA-03 | Checklists are short pause-point coordination aids, not ceremonial paperwork. | direct/analogical | `practice-checklists-at-pause-points`, `anti-pattern-checklist-theater`, `case-study-who-surgical-safety-checklist` | Clinical checklist evidence is analogical for software. |
| QUA-04 | Product/system quality is evaluated across relevant quality attributes, not one defect/speed dimension. | direct | `standard-iso-25010`, `framework-space`, `principle-built-in-quality` | Exact ISO 25010 2023 mapping needs refresh. |
| DEL-01 | Work is sliced into small reviewable increments without losing coherent value or architecture context. | direct | `pattern-small-batches`, `principle-fast-feedback-loops`, `practice-modern-code-review` | Some changes need coordinated release plans. |
| DEL-02 | Build/test/security/release checks create trustworthy feedback and deployable/releasable state. | direct | `pattern-continuous-delivery-pipeline`, `principle-built-in-quality`, `standard-nist-ssdf` | Pipeline presence alone is not proof of quality. |
| DEL-03 | Reliability and delivery tradeoffs use user-centered objectives and explicit risk budget thinking where applicable. | direct | `pattern-slo-error-budget`, `case-study-google-sre`, `metric-dora-four-key-metrics` | SLOs require measurable user impact and authority to act. |
| DEL-04 | Incidents and high-risk workflow failures are detected, coordinated, resolved, and converted into learning. | direct | `process-incident-management`, `case-study-google-sre`, `practice-kaizen-retrospective-improvement` | No local incident process exists; framework must allow gap finding. |
| PLA-01 | Shared capabilities are operated as product-like platform services with users, ownership, support, adoption, and improvement. | direct | `pattern-platform-as-product`, `framework-platform-maturity` | Avoid creating platform model if no repeated internal-user need exists. |
| PLA-02 | Platform work avoids becoming a bespoke ticket queue and reduces cognitive load through reusable capabilities. | direct | `anti-pattern-platform-as-ticket-queue`, `pattern-golden-paths`, `pattern-platform-as-product` | Some high-risk work may legitimately require requests. |
| PLA-03 | Portals/catalogs are assessed as interfaces to capability, not as the platform itself. | direct | `anti-pattern-portal-equals-platform`, `tool-internal-developer-portal` | Developer portal is Rejected for current context; criterion should test assumptions, not require a portal. |
| PLA-04 | Golden paths are maintained, adopted, measured, and paired with exception handling. | direct | `pattern-golden-paths`, `framework-platform-maturity`, `pattern-platform-as-product` | Path maturity is context-relative. |
| PRO-01 | Product decisions connect outcomes, user/customer evidence, opportunities, solution options, and experiments. | direct | `practice-continuous-discovery`, `pattern-opportunity-solution-tree` | Requires access to relevant users/customers. |
| PRO-02 | Product/design/engineering perspectives collaborate in discovery and delivery decisions. | direct | `pattern-product-trio`, `practice-continuous-discovery` | Trio must not exclude relevant security/support/data/stakeholders. |
| PRO-03 | Roadmaps and success measures avoid output-only feature-factory logic. | direct | `anti-pattern-feature-factory`, `practice-continuous-discovery`, `framework-dora-core` | Some commitments legitimately require features. |
| SEC-01 | Security practices are integrated across planning, implementation, verification, release, and response. | direct | `practice-secure-sdlc-ssdf`, `standard-nist-ssdf`, `principle-built-in-quality` | SSDF is high-level and requires local threat tailoring. |
| SEC-02 | AI risk governance identifies, measures, manages, and monitors risk with real operational evidence. | direct | `standard-nist-ai-rmf`, `standard-iso-42001`, `pattern-human-ai-checkpoints` | Standards are abstract; local controls are a KB gap. |
| SEC-03 | AI governance avoids certification/compliance theater and ties responsibilities to actual system operation. | direct | `standard-iso-42001`, `standard-nist-ai-rmf`, `anti-pattern-human-rubber-stamp-ai` | Does not prescribe certification. |
| MET-01 | Delivery and productivity measurement is balanced, contextual, and system-level. | direct | `framework-dora-core`, `framework-space`, `metric-dora-four-key-metrics`, `metric-space-balanced-productivity` | Not for individual performance ranking. |
| MET-02 | Single activity metrics are not used as complete productivity truth. | direct | `anti-pattern-single-metric-productivity`, `framework-space`, `metric-space-balanced-productivity` | Activity metrics can be diagnostics if contextualized. |
| MET-03 | Feedback loops produce trustworthy evidence tied to decisions, not only activity signals. | direct | `principle-fast-feedback-loops`, `framework-dora-core`, `practice-continuous-discovery` | Feedback can be slow-cycle if explicitly designed. |
| MET-04 | Improvement cycles have ownership, evidence, experiments/countermeasures, and follow-through. | direct/analogical | `practice-kaizen-retrospective-improvement`, `method-a3-problem-solving`, `case-study-toyota-production-system` | A3-specific source depth is insufficient for mandatory A3 use. |
| ARC-01 | Architecture review addresses explicit stakeholders, concerns, viewpoints, and views. | direct | `standard-iso-42010`, `practice-architecture-review-by-viewpoints` | Avoid heavyweight review for trivial/reversible changes. |
| ARC-02 | Consequential decisions record context, decision, status, consequences, and review/reversal conditions. | direct | `decision-technique-adr`, `pattern-adr-decision-log`, `principle-knowledge-close-to-work` | ADRs do not prove decision quality. |
| ARC-03 | Documentation and knowledge surfaces match user needs and separate tutorials/how-to/explanation/reference where useful. | direct | `framework-diataxis`, `anti-pattern-knowledge-dump-kb`, `principle-knowledge-close-to-work` | Diataxis should not override more useful KB taxonomy. |
| ARC-04 | Knowledge graph or link structure is used only when simple links/IDs/metadata are insufficient. | direct | `tool-knowledge-graph`, `pattern-provenance-linked-knowledge`, `anti-pattern-agentic-overengineering` | Full graph tooling is Under Evaluation, not mandatory. |

## Unsupported or Gap-Limited Candidate Criteria

| Candidate criterion | KB status | Treatment in Framework |
| --- | --- | --- |
| BRD governance maturity | `artifact:brd.md` and `governance:brd-governance` are `not_yet_available` | Include as KB gap and optional audit question, not a scored requirement unless future KB adds governance. |
| Product Analyst / Validator / Historian operating maturity | Roles are reserved but not canonical | Include as possible evidence gap/future research, not current required role criteria. |
| Exact AI eval thresholds | No local eval harness or thresholds exist | Require evidence of eval design where autonomy/risk warrants it; do not prescribe thresholds. |
| Exact incident severity taxonomy | Incident process accepted but not mapped locally | Define evidence questions, not fixed taxonomy. |
| Exact ISO 25010 2023 characteristics mapping | KB says mapping needs refresh | Use quality-attribute principle with refresh caveat. |
