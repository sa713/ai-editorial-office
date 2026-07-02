# Knowledge Base Coverage Map

Task: `TASK-STUDIO-FIRST-AUDIT`
Date: 2026-07-02

Source: `../kb-implementation-map.md`

## Coverage Snapshot

| KB category | Count | Audit result |
|---|---:|---|
| Total KB records | 55 | All records reviewed. |
| Audit-confirmed implemented | 13 | Visible in current Studio evidence. |
| Partially implemented or contested | 7 | Some evidence exists, but full implementation is limited or contradicted. |
| Not implemented / reference only | 30 | Present as KB knowledge, not current operating practice. |
| Under Evaluation | 4 | Not counted as implemented. |
| Rejected | 1 | Current-context rejection confirmed. |

## Implemented Coverage By Area

| Area | Implemented KB signal | Coverage strength | Evidence |
|---|---|---|---|
| Governance | sociotechnical system, autonomy with guardrails, human-AI checkpoints | Strong | E01-E04, E23-E24 |
| Knowledge | provenance-linked knowledge, anti-knowledge-dump KB, knowledge close to work | Strong | E16-E20 |
| Quality | built-in quality, review gates, pause-point checklists | Strong | E06, E11, E23-E24 |
| Platform/Flow | golden paths and reusable templates | Moderate-strong | E08-E09 |
| AI | human checkpoints and role boundaries | Partial | E02-E04, E17-E19 |
| Delivery/Reliability | validator tooling | Partial | E10-E14 |
| Product | product knowledge retained in KB | Weak | E19, E21 |
| Security/Risk | security and AI-risk standards retained in KB | Weak | E17-E18 |
| Metrics/Learning | feedback artifacts through review/final decisions | Weak-partial | E22-E23 |
| Architecture | final decisions and ownership map | Partial | E01, E19, E21-E24 |

## Contested Coverage

| KB record | KB claim | Audit observation | Evidence |
|---|---|---|---|
| `practice-context-and-memory-management` | Applied | Task manifests and project-state restart guidance exist, but expected `/about` package is absent. | E05, E15, E17, E22, E25 |
| `pattern-adr-decision-log` | Accepted | Final decisions exist, but ADR is not canonical. | E21, E24 |
| `practice-modern-code-review` | Accepted | Review-gate practice exists; code-review-specific practice is not defined. | E06, E23 |

## Non-Implemented Knowledge Clusters

| Cluster | Records | Evidence |
|---|---|---|
| Delivery and reliability | CD pipeline, SLO/error budget, incident management, DORA metrics | E17-E18 |
| Product discovery | product trio, opportunity-solution tree, continuous discovery, BRD-related objects | E19, E21-E22 |
| AI evaluation and risk | AI evaluation harness, agent interface patterns, NIST AI RMF, ISO 42001 | E17-E19 |
| Security | NIST SSDF, secure SDLC, supply-chain/security validation | E17-E18 |
| Metrics | SPACE, DORA, balanced productivity and outcome/adoption metrics | E17-E18 |
| Architecture | ISO 42010, architecture review by viewpoints, ADR technique | E17, E19, E21-E24 |

## Not Evaluable Beyond Reference Status

The external standards, frameworks and case studies in KB are evaluable as retained knowledge. They are not fully evaluable as Studio practices unless linked to operating artifacts, controls, workflows, metrics or decisions.
