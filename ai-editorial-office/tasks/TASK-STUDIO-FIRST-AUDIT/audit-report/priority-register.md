# Priority Register

Task: `TASK-STUDIO-FIRST-AUDIT`
Date: 2026-07-02

Priority classes follow the approved Studio Audit Framework. This register records audit findings and impact only; it does not define implementation actions.

## Critical Problems

No Critical problems were identified under the available evidence and Framework rules.

## Important Problems

| ID | Finding | Impact | Evidence |
|---|---|---|---|
| IP-01 | The expected root `/about` memory package is absent, while project state and KB application records refer to it as part of applied context-memory management. | Reduces confidence in Studio memory integrity and in the Applied status of `practice-context-and-memory-management`. | E05, E15, E17, E25 |
| IP-02 | A finalized high-governance task fails automated lifecycle validation due to pipeline mapping and review outcome recognition. | Reduces confidence that automated governance checks consistently validate finalized task states. | E14, E22 |
| IP-03 | AI evaluation harness, agent-computer-interface criteria and AI telemetry are not operationally evidenced. | Caps AI-native maturity and limits objective assessment of agentic work quality. | E17-E19 |
| IP-04 | Security and AI-risk standards are present in KB but not evidenced as local controls. | Leaves SEC area at ad hoc maturity and limits risk-control assurance. | E17-E18 |
| IP-05 | Metrics, productivity, delivery-performance and outcome-measurement systems are not evidenced. | Prevents whole-Studio maturity from reaching Measured or Learning levels. | E17-E18 |
| IP-06 | Product Analyst, BRD and BRD Governance are not canonical Studio objects. | Limits product discovery and value-governance assessment. | E19, E21-E22 |
| IP-07 | Explicit architecture review and ADR practice are not canonical. | Limits architecture-governance scoring to implicit ownership and final decision evidence. | E19, E21, E24 |

## Desirable Improvements

| ID | Observation | Impact | Evidence |
|---|---|---|---|
| DI-01 | Delivery validators exist and pass smoke tests, but coverage is narrow. | Validation assurance is helpful but not comprehensive. | E10-E14 |
| DI-02 | Final decisions preserve governance decisions, but their relationship to architecture decisions is not formalized. | Decision memory exists but architecture decision traceability remains partial. | E21-E24 |
| DI-03 | Platform and internal developer experience are supported by templates and golden paths, not by a platform-as-product operating model. | Platform criteria are only partially applicable in the current Studio shape. | E08-E09, E17, E19 |
| DI-04 | Feedback artifacts exist through review and final decisions, but trend-based learning evidence was not found. | Learning-cycle maturity remains below Measured/Learning. | E22-E23 |

## Observations Without Need For Intervention

| ID | Observation | Evidence |
|---|---|---|
| OBS-01 | Canonical ownership map and role authority are clear. | E01, E03 |
| OBS-02 | Review before finalization is a hard invariant. | E02, E06 |
| OBS-03 | The Knowledge Base has explicit schema, lifecycle and application register. | E16-E20 |
| OBS-04 | Internal developer portal is explicitly rejected for the current local markdown context. | E17 |
| OBS-05 | Visual subsystem is explicitly bounded and does not expand the active role set. | E03 |

## Questions Requiring Additional Research

| ID | Question | Evidence basis |
|---|---|---|
| RQ-01 | Was `/about` intentionally moved, omitted or never created? | E05, E15, E25 |
| RQ-02 | Is inline-code formatting for review outcomes intended to be accepted by lifecycle validation? | E14, E22 |
| RQ-03 | Are final decision artifacts intended to substitute for ADRs in the current Studio? | E21, E24 |
| RQ-04 | Which Accepted standards and frameworks are intended as references only versus future operating practices? | E17-E21 |
| RQ-05 | What evidence would qualify AI evaluation and AI risk controls as Applied in the Studio context? | E17-E19 |
