# Criterion Scorecard

Task: `TASK-STUDIO-FIRST-AUDIT`
Date: 2026-07-02
Framework version: approved `TASK-STUDIO-AUDIT-FRAMEWORK`

Scoring uses the approved maturity model:

- M0: Not evidenced
- M1: Ad hoc
- M2: Defined
- M3: Operated
- M4: Measured
- M5: Learning

Evidence confidence uses the Framework scale:

- E0: no evidence
- E1: assertion
- E2: artifact exists
- E3: artifact plus usage evidence
- E4: usage plus effectiveness, trend or learning evidence

Priority classes: Critical, Important, Improvement, No Change, Observation.

## Scorecard

| Criterion | Maturity | Confidence | Priority | Evidence | Audit result |
|---|---:|---:|---|---|---|
| GOV-01 Governance ontology and authority boundaries | M3 | E3 | No Change | E01, E03, E05, E17 | Canonical governance, ownership and authority boundaries are defined and used in task execution. |
| GOV-02 Role accountability and human responsibility | M3 | E3 | No Change | E02, E03, E07, E23 | Role accountability and reviewer separation are explicit and visible in sampled tasks. |
| GOV-03 Governance gates and approval discipline | M3 | E3 | Improvement | E02, E04, E06, E12, E13, E14, E23, E24 | Gates are operated, but one finalized task is not machine-recognized as compliant by the lifecycle validator. |
| GOV-04 Change governance and artifact ownership | M3 | E3 | No Change | E01, E04, E08, E09, E21 | Artifact ownership and change boundaries are clear; future noncanonical objects are explicitly marked. |
| KNO-01 Knowledge record schema and provenance | M3 | E3 | No Change | E16, E18, E20 | KB records use explicit schema, lifecycle fields, confidence and object links. |
| KNO-02 Application register and knowledge traceability | M3 | E3 | No Change | E16, E17, E18 | Application status is registered across the 55-record KB. |
| KNO-03 Context and memory management | M2 | E2 | Important | E05, E15, E17, E22, E25 | Context-memory practice is registered as Applied, but the `/about` package expected by current state is absent at the repository root. |
| KNO-04 Decision memory and institutional learning | M2 | E2 | Improvement | E04, E21, E22, E24 | Decisions are recorded through final decisions and project state; canonical Historian/BRD governance records are not available. |
| AI-01 Agent autonomy boundaries | M2 | E2 | Improvement | E02, E03, E17, E19 | Human checkpoints and role boundaries are defined; agent-tool-loop patterns remain Under Evaluation. |
| AI-02 Agent-computer/tool interface governance | M1 | E2 | Important | E17, E19, E21 | Tool and computer-interface records are Under Evaluation or not canonical; operational evidence is limited. |
| AI-03 AI evaluation and feedback loops | M1 | E1 | Important | E17, E18 | No evidence of a formal AI evaluation harness, benchmark suite or trend-based evaluation loop was found. |
| AI-04 AI output traceability and observability | M2 | E2 | Important | E04, E08, E23 | Editorial traceability exists, but AI-specific observability and output-quality telemetry are not evidenced. |
| QUA-01 Built-in quality gates | M3 | E3 | No Change | E02, E04, E06, E11, E23, E24 | Review gates, final governance and validator checks are defined and used. |
| QUA-02 Independent review discipline | M3 | E3 | No Change | E02, E06, E23, E24 | Independent review is explicitly required and visible in sampled high-governance artifacts. |
| QUA-03 Evidence-based quality review | M3 | E3 | Improvement | E06, E08, E09, E14, E23 | Evidence-based review is practiced, with a tooling recognition gap in one finalized task. |
| QUA-04 Quality standards and formal quality models | M2 | E2 | Improvement | E16, E17 | Quality principles are represented in KB records; formal quality-standard operation is not evidenced. |
| DEL-01 Flow, batch size and delivery cadence | M2 | E2 | Improvement | E04, E08, E09 | Workflow stages and task artifacts support controlled flow; delivery cadence evidence is limited. |
| DEL-02 Continuous integration or automated validation | M2 | E3 | Important | E10, E11, E12, E13, E14 | Read-only validators and smoke tests exist; validation coverage is not consistently aligned with all finalized task formats. |
| DEL-03 Reliability objectives and service levels | M1 | E1 | Important | E17, E18 | SLO and reliability records are Accepted in KB but not evidenced as current Studio practices. |
| DEL-04 Incident learning and recovery | M1 | E1 | Important | E17, E18 | Incident and post-incident practices are KB knowledge, but operating artifacts were not found. |
| PLA-01 Platform-as-product operating model | M1 | E1 | Improvement | E17, E19, E21 | Platform-as-product knowledge is present; a platform operating model is not canonical in the current Studio. |
| PLA-02 Internal developer experience ownership | M2 | E2 | Improvement | E01, E04, E08, E09 | Golden paths and templates support internal experience; dedicated platform ownership evidence is limited. |
| PLA-03 Portal/tooling fit and rejection discipline | M3 | E3 | No Change | E17 | Internal developer portal knowledge is explicitly Rejected for the current Studio context. |
| PLA-04 Golden paths and reusable templates | M3 | E3 | No Change | E08, E09, E23 | Pipeline files and templates act as golden paths and are used in sampled tasks. |
| PRO-01 Product discovery and value validation | M1 | E1 | Important | E17, E19, E21 | Product discovery knowledge exists, but canonical Product Analyst and BRD practices are not available. |
| PRO-02 BRD and product decision governance | M1 | E1 | Important | E19, E21, E22 | BRD and BRD Governance are explicitly not yet available as canonical Studio objects. |
| PRO-03 Portfolio and backlog governance | M1 | E2 | Improvement | E05, E21 | Project state and ideas/backlog references exist, but formal portfolio governance evidence is limited. |
| SEC-01 Secure development and AI risk controls | M1 | E1 | Important | E17, E18 | Security and AI-risk standards are in KB but not evidenced as local controls. |
| SEC-02 Security validation and supply-chain discipline | M1 | E1 | Important | E17, E18 | No operating evidence of security validation, dependency control or supply-chain governance was found. |
| SEC-03 Governance anti-theater controls | M2 | E2 | Improvement | E01, E02, E17, E23 | Anti-checklist and anti-rubber-stamp knowledge is Applied; security-specific anti-theater controls are not separately evidenced. |
| MET-01 Metrics definitions and measurement system | M1 | E1 | Important | E17, E18 | Metrics records are in KB but no operating measurement system was found. |
| MET-02 Productivity metrics safety | M1 | E1 | Improvement | E17, E18 | No harmful single-metric mechanism was observed, but no operational productivity metric model was evidenced. |
| MET-03 Feedback loops and learning cadence | M2 | E2 | Improvement | E04, E06, E17, E22, E23 | Reviews and final decisions create feedback artifacts; trend-based learning is not evidenced. |
| MET-04 Outcome and adoption measurement | M1 | E1 | Important | E17, E18 | No evidence of adoption, outcome or effectiveness measurement for Studio practices was found. |
| ARC-01 Architecture governance and decision structure | M2 | E2 | Improvement | E01, E04, E19, E21, E24 | Architecture is implicit in canonical ownership and task governance; dedicated architecture-review practice is not evidenced. |
| ARC-02 Decision records and reversibility | M2 | E3 | Improvement | E04, E22, E23, E24 | Final decisions and project-state records preserve decisions; explicit ADR practice is not canonical. |
| ARC-03 Information architecture and knowledge taxonomy | M3 | E3 | No Change | E16, E18, E20 | KB taxonomy and schema are defined and operated through the application register. |
| ARC-04 Knowledge graph and cross-reference discipline | M2 | E2 | Improvement | E16, E18, E19 | Cross-reference discipline exists; formal knowledge graph tooling remains Under Evaluation. |

## Area Maturity Map

| Area | Area maturity | Confidence | Evidence sufficiency | Main limitation |
|---|---:|---:|---|---|
| GOV Governance and Operating Model | M3 Operated | E3 | Sufficient | Validator recognition gap in one finalized task. |
| KNO Knowledge and Organizational Memory | M3 Operated with contested memory-package evidence | E3/E2 mixed | Mostly sufficient | `/about` package absent despite current-state and KB application claims. |
| AI AI-Native Work System | M2 Defined | E2 | Limited | AI evaluation, agent-computer-interface and telemetry are not operationally evidenced. |
| QUA Quality and Review System | M3 Operated | E3 | Sufficient | Review/validator format mismatch affects automated assurance. |
| DEL Delivery, Reliability and Operations | M2 Defined | E2 | Partial | Delivery reliability and incident learning evidence is weak. |
| PLA Platform and Internal Developer Experience | M2 Defined | E2 | Partial | Platform-as-product is knowledge-level rather than operating-model evidence. |
| PRO Product, Discovery and Value Governance | M1 Ad hoc | E1/E2 | Limited | Product Analyst, BRD and BRD Governance are not canonical. |
| SEC Security, Compliance and AI Risk | M1 Ad hoc | E1/E2 | Limited | Standards exist in KB but local controls were not found. |
| MET Metrics, Feedback and Learning | M1 Ad hoc | E1/E2 | Limited | No measurement system or trend evidence found. |
| ARC Architecture and Socio-Technical Design | M2 Defined | E2 | Partial | Architecture decisions are implicit; ADR/review practice is not canonical. |

## Studio-Level Maturity

Overall maturity: **M2 Defined**

Confidence: **Medium-high**

Rationale: Governance, knowledge schema, review discipline and golden-path workflows operate at M3 in the sampled evidence. The Studio-level rating is capped at M2 because AI evaluation, security/risk controls, metrics, product discovery, delivery reliability and explicit architecture review have weak operating evidence and are often represented in KB as Accepted, Under Evaluation or not-yet-available rather than Applied.
