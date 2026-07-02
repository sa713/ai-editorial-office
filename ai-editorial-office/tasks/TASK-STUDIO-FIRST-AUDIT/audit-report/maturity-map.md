# Maturity Map

Task: `TASK-STUDIO-FIRST-AUDIT`
Date: 2026-07-02

## Studio-Level Maturity

| Scope | Maturity | Confidence | Evidence sufficiency | Basis |
|---|---:|---:|---|---|
| AI Software Studio overall | M2 Defined | Medium-high | Mixed | M3 evidence in governance/quality/KB core; M1-M2 evidence in AI evaluation, security, metrics, product, delivery and architecture review. |

## Area Map

| Area | Maturity | Confidence | Evidence sufficiency | Main evidence | Main limitation |
|---|---:|---:|---|---|---|
| GOV Governance and Operating Model | M3 Operated | E3 | Sufficient | E01-E06, E12-E14, E23-E24 | Validator recognition gap in one finalized task. |
| KNO Knowledge and Organizational Memory | M3 Operated with contested sub-area | E3/E2 | Mostly sufficient | E16-E20, E22, E25 | `/about` package contradiction limits context-memory confidence. |
| AI AI-Native Work System | M2 Defined | E2 | Limited | E02-E04, E17-E19 | AI eval, interface governance and telemetry not evidenced. |
| QUA Quality and Review System | M3 Operated | E3 | Sufficient | E06, E10-E14, E23-E24 | Automated validator mismatch affects assurance consistency. |
| DEL Delivery, Reliability and Operations | M2 Defined | E2 | Partial | E08-E11, E17-E18 | CD/SLO/incident operation not evidenced. |
| PLA Platform and Internal Developer Experience | M2 Defined | E2 | Partial | E08-E09, E17, E19 | Platform-as-product not current operating model. |
| PRO Product, Discovery and Value Governance | M1 Ad hoc | E1/E2 | Limited | E19, E21-E22 | Product Analyst, BRD, BRD Governance not canonical. |
| SEC Security, Compliance and AI Risk | M1 Ad hoc | E1/E2 | Limited | E17-E18 | Standards not evidenced as local controls. |
| MET Metrics, Feedback and Learning | M1 Ad hoc | E1/E2 | Limited | E17-E18, E22-E23 | No measurement system or trend evidence. |
| ARC Architecture and Socio-Technical Design | M2 Defined | E2 | Partial | E01, E04, E19, E21-E24 | ADR and architecture-review practices not canonical. |

## Criterion Distribution

| Maturity level | Criteria count | Criteria |
|---|---:|---|
| M3 Operated | 12 | GOV-01, GOV-02, GOV-03, GOV-04, KNO-01, KNO-02, QUA-01, QUA-02, QUA-03, PLA-03, PLA-04, ARC-03 |
| M2 Defined | 13 | KNO-03, KNO-04, AI-01, AI-04, QUA-04, DEL-01, DEL-02, PLA-02, SEC-03, MET-03, ARC-01, ARC-02, ARC-04 |
| M1 Ad hoc | 13 | AI-02, AI-03, DEL-03, DEL-04, PLA-01, PRO-01, PRO-02, PRO-03, SEC-01, SEC-02, MET-01, MET-02, MET-04 |
| M0 Not evidenced | 0 | None scored as M0 because each criterion had at least minimal KB or artifact evidence. |

Note: criterion distribution is descriptive. Overall maturity is not calculated by averaging.
