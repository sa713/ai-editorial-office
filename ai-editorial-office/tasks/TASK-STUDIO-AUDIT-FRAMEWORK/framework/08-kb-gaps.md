# Knowledge Base Gaps

These gaps were discovered while deriving the Framework. They are not audit
findings about the current Studio.

## Gap Register

| Gap ID | Missing or insufficient knowledge | Affected Framework area | Current treatment |
| --- | --- | --- | --- |
| GAP-01 | Canonical BRD governance and BRD artifact model are not available. | GOV, PRO, ARC | Do not score BRD governance maturity; record as gap-only unless KB changes. |
| GAP-02 | Product Analyst, Validator, and Historian roles are reserved but not canonical. | GOV, PRO, KNO, MET | Do not require these roles; mention as future role-mapping research. |
| GAP-03 | Studio-specific AI evaluation harness design and thresholds do not exist. | AI, SEC, QUA | Score presence/quality of eval evidence if available; do not prescribe thresholds. |
| GAP-04 | Agent-computer-interface standard is under evaluation and not canonical. | AI | Use criterion cautiously; cap maturity if evidence is only informal. |
| GAP-05 | Canonical architecture review artifact and ADR process are not present in object map. | ARC | Score decision/architecture traceability generically; do not require a specific file format. |
| GAP-06 | Incident process and severity taxonomy are accepted as future references but not locally mapped. | DEL, MET | Ask evidence questions; do not require a fixed incident taxonomy. |
| GAP-07 | Delivery metrics and productivity measurement program do not exist in KB application layer. | DEL, MET | Use balanced measurement criteria; do not demand DORA/SPACE dashboard implementation. |
| GAP-08 | Exact ISO/IEC 25010 2023 mapping is not incorporated. | QUA, ARC | Use quality-attribute reasoning with refresh caveat. |
| GAP-09 | A3 Problem Solving lacks direct A3-specific source depth. | MET | Use only as optional structured problem-solving reference. |
| GAP-10 | Platform maturity is accepted but not validated in Studio context. | PLA | Avoid ladder-chasing; interpret maturity contextually. |
| GAP-11 | Security and AI risk standards lack local control mapping. | SEC | Audit evidence of risk ownership/control mapping if present; do not invent controls. |
| GAP-12 | Knowledge Graph is under evaluation; no proof simple links are insufficient. | KNO, ARC | Do not require graph tooling; allow simple links/IDs/metadata. |
| GAP-13 | Privacy/access handling for audit evidence is not defined in KB. | KNO, SEC | Treat as evidence-handling limitation; future research needed before sensitive audits. |

## How Gaps Affect Scoring

- Gap-only items are not scored.
- A gap may reduce confidence in a related active criterion only when the
  missing knowledge prevents the auditor from determining conformance.
- A gap is not a Studio failure unless the active criterion requires evidence
  that cannot be produced.
- Future audits must keep KB gaps separate from evidence gaps.

## Recommended Future Research

Future research may be useful in these areas:

1. Studio-specific AI evaluation harness and regression corpus.
2. Local security and AI risk control mapping derived from NIST SSDF, NIST AI
   RMF, and ISO/IEC 42001.
3. Architecture and decision-record governance for AI Software Studio.
4. Incident management model for AI-assisted workflows and local markdown-based
   systems.
5. Balanced metric design for a single-user or small-team AI Software Studio.
6. Product discovery evidence model for Studio improvement decisions.
7. Criteria for when a local repository-first Studio should become a
   multi-user platform.
8. Evidence privacy and retention policy for recurring audits.

These are research recommendations, not implementation tasks.

