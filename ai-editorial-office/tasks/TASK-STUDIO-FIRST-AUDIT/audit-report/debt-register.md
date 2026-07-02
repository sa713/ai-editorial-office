# Debt Register

Task: `TASK-STUDIO-FIRST-AUDIT`
Date: 2026-07-02

This register records organizational and process debt observed by the audit. It does not prescribe changes.

## Organizational Debt

| ID | Debt item | Affected areas | Impact | Evidence |
|---|---|---|---|---|
| OD-01 | Product Analyst is not a canonical role. | PRO, PLA, MET | Product discovery and value-validation criteria have weak evidence. | E19, E21 |
| OD-02 | Historian is not a canonical owner. | KNO, MET, ARC | Institutional learning and historical decision traceability depend on general artifacts rather than dedicated ownership. | E19, E21 |
| OD-03 | Validator is not a canonical role. | QUA, DEL, SEC | Validation ownership is distributed across scripts/review rather than a named operating role. | E19, E21 |
| OD-04 | BRD and BRD Governance are not canonical objects. | PRO, GOV, ARC | Product decision governance cannot be assessed as implemented. | E19, E21, E22 |
| OD-05 | Platform ownership is not a current operating model. | PLA, DEL, MET | Platform-as-product and adoption-measurement criteria have limited applicability. | E17, E19 |

## Process Debt

| ID | Debt item | Affected areas | Impact | Evidence |
|---|---|---|---|---|
| PD-01 | Lifecycle validator does not recognize one finalized task as valid. | GOV, QUA, DEL | Automated governance assurance is inconsistent across sampled tasks. | E14, E22 |
| PD-02 | Expected `/about` memory-package check fails. | KNO | Context-memory implementation is contested. | E15, E25 |
| PD-03 | AI evaluation process is not evidenced. | AI, MET, SEC | AI-native maturity cannot advance beyond Defined under current evidence. | E17-E19 |
| PD-04 | Security/risk control process is not evidenced. | SEC, GOV | Security and AI-risk maturity remain ad hoc. | E17-E18 |
| PD-05 | Metrics and trend-review process is not evidenced. | MET, DEL, PRO | Whole-Studio maturity cannot be measured or learning-oriented. | E17-E18 |
| PD-06 | Incident-management process is not evidenced. | DEL, SEC | Operational learning from failures cannot be assessed. | E17-E18 |
| PD-07 | Explicit architecture-review process is not evidenced. | ARC | Architecture maturity is inferred from governance rather than directly evidenced. | E19, E21-E24 |

## Debt Classification Notes

- Debt classification is based on audit impact, not on a prescribed fix.
- Some debt items correspond to KB-known future extensions rather than defects in existing implemented practice.
- Absence of a practice is treated as debt only when the Framework has a criterion for it and current evidence cannot satisfy that criterion.
