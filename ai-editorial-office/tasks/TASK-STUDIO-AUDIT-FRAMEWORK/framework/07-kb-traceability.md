# Knowledge Base Traceability

## Traceability Rule

Every Framework section and criterion must trace to Knowledge Base records or
KB model documents. If support is insufficient, the Framework must say so and
avoid scoring the unsupported requirement.

## Framework Section Traceability

| Framework section | KB entries used | Insufficient knowledge | Future research need |
| --- | --- | --- | --- |
| Executive Summary | `index.md`, `navigation.md`, `glossary-intelligent-production-system`, `principle-sociotechnical-production-system` | None for high-level purpose | Refresh if KB purpose changes |
| Framework Architecture | `schema.md`, `application-model.md`, `lifecycle.md`, `coverage-model.md`, `development-recommendations.md` | No canonical audit role model | Define audit role mapping if Validator becomes canonical |
| Audit Areas | `navigation.md`, all domain records | None for high-level area set | Revisit when KB domains change |
| Criteria Catalog | `claims_table.md`, all 55 records | Some detailed controls unsupported | Add control-level records where needed |
| Maturity Model | `framework-space`, `framework-dora-core`, `framework-platform-maturity`, `anti-pattern-single-metric-productivity` | No Studio-specific maturity history | Calibrate after first audit |
| Evidence Rules | `pattern-provenance-linked-knowledge`, `practice-context-and-memory-management`, `anti-pattern-automation-without-observability` | No privacy/access evidence policy | Add evidence-handling policy if needed |
| Audit Report Rules | `pattern-provenance-linked-knowledge`, `principle-knowledge-close-to-work`, `decision-technique-adr` | No report archive lifecycle | Add future Historian guidance |
| KB Gaps | `application-register.md`, `studio-object-map.md`, `development-recommendations.md` | n/a | Convert gaps into KB research tasks only outside this Framework |
| First Audit Guidance | all model documents and criteria records | No first-audit calibration data | Calibrate scoring rubric during first audit |

## Area-to-KB Map

| Area | Primary KB records | Supporting records |
| --- | --- | --- |
| GOV | `principle-sociotechnical-production-system`, `principle-autonomy-with-guardrails`, `pattern-human-ai-checkpoints` | `pattern-golden-paths`, `anti-pattern-human-rubber-stamp-ai`, `anti-pattern-checklist-theater` |
| KNO | `principle-knowledge-close-to-work`, `pattern-provenance-linked-knowledge`, `practice-context-and-memory-management` | `anti-pattern-knowledge-dump-kb`, `tool-knowledge-graph`, `framework-diataxis` |
| AI | `pattern-agent-tool-loop`, `pattern-agent-computer-interface`, `practice-ai-evaluation-harness` | `anti-pattern-agentic-overengineering`, `case-study-swe-bench-and-swe-agent`, `standard-nist-ai-rmf` |
| QUA | `principle-built-in-quality`, `practice-modern-code-review`, `practice-checklists-at-pause-points` | `standard-iso-25010`, `case-study-who-surgical-safety-checklist`, `anti-pattern-checklist-theater` |
| DEL | `pattern-small-batches`, `pattern-continuous-delivery-pipeline`, `pattern-slo-error-budget`, `process-incident-management` | `case-study-google-sre`, `metric-dora-four-key-metrics`, `anti-pattern-automation-without-observability` |
| PLA | `pattern-platform-as-product`, `pattern-golden-paths`, `framework-platform-maturity` | `tool-internal-developer-portal`, `anti-pattern-platform-as-ticket-queue`, `anti-pattern-portal-equals-platform` |
| PRO | `practice-continuous-discovery`, `pattern-product-trio`, `pattern-opportunity-solution-tree` | `anti-pattern-feature-factory` |
| SEC | `practice-secure-sdlc-ssdf`, `standard-nist-ssdf`, `standard-nist-ai-rmf`, `standard-iso-42001` | `pattern-human-ai-checkpoints`, `anti-pattern-human-rubber-stamp-ai` |
| MET | `framework-space`, `metric-space-balanced-productivity`, `framework-dora-core`, `metric-dora-four-key-metrics` | `principle-fast-feedback-loops`, `practice-kaizen-retrospective-improvement`, `anti-pattern-single-metric-productivity` |
| ARC | `standard-iso-42010`, `practice-architecture-review-by-viewpoints`, `pattern-adr-decision-log`, `decision-technique-adr` | `framework-diataxis`, `tool-knowledge-graph`, `principle-knowledge-close-to-work` |

## Criteria Traceability

Criterion-level traceability is maintained in:

- `../claims_table.md`
- `03-assessment-criteria.md`

Future Framework revisions must update both when criteria are added, removed,
or narrowed.

## Records by KB Application Status

The Framework may use all statuses as methodology knowledge, but must interpret
them carefully:

| KB status | Use in Framework |
| --- | --- |
| Applied | Strong evidence that the concept is already represented in some active Studio object; still not an audit result. |
| Accepted | Valid external knowledge for methodology; not proof of current implementation. |
| Under Evaluation | Use with caution and refresh; do not treat as stable local practice. |
| Rejected | May support "do not require this" or "test reconsideration condition"; do not turn into a requirement. |
| Deprecated | Exclude unless historical comparison is needed. |

## External Source Boundary

The Framework cites KB records and source IDs through the KB. It does not claim
fresh direct verification of external standards or reports. Future audits that
need current regulatory or standard precision must refresh the KB first.

