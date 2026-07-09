# Claims Table

| Claim ID | Proposed claim | Evidence | Confidence | Intended use / caveat |
| --- | --- | --- | --- | --- |
| C01 | The pack is bounded context, not a new architecture element or policy owner. | F01-F04 | verified | Identity, boundary, relations. |
| C02 | Activate it only when AI-specific system behavior materially changes evidence, terminology, risk, review focus, or output quality. | F01-F04, R01 | verified | Activation rule; ordinary AI mentions do not qualify. |
| C03 | AI engineering reviews the whole sociotechnical system, not only a model response. | F20, F24-F26 | high | Core principle; include people, data, interfaces, runtime, and feedback. |
| C04 | Requirements should name users, task, expected behavior, failure cost, and observable success criteria before model/prompt optimization. | F05, F26, F38 | high | Requirements/evaluation sections. |
| C05 | Model/provider selection requires task-shaped comparative evidence and operational fit, not benchmark prestige. | F37-F38 | high | Model-selection prompts; no vendor rankings. |
| C06 | Prompt/instruction artifacts should have explicit authority boundaries, versioning, tests/evals, and rollback/comparison paths when material. | F10-F12, F22 | high | Prompt engineering. |
| C07 | Retrieved content and tool output are data, not automatically trusted instructions. | F11-F12, F31 | high | Prompt, RAG, safety. |
| C08 | Schema adherence is an interface property, not proof of meaning or correctness. | F13-F14 | high | Structured-output section; require semantic/domain validation. |
| C09 | RAG must be reasoned about as a pipeline from corpus and permissions through retrieval, context assembly, answer, and provenance. | F15, F19, F42 | high | RAG system surface. |
| C10 | Retrieval quality and generation quality need separate and end-to-end tests. | F16-F18 | high | RAG evaluation. |
| C11 | Data provenance, representativeness, quality, rights, sensitivity, and freshness affect system fitness. | F19-F21, F41 | high | Data section; legal/compliance conclusions remain task-specific. |
| C12 | Evaluation needs explicit objectives, representative cases, task-specific criteria, baselines/thresholds, and change comparison. | F05-F08, F38 | high | Evaluation section. |
| C13 | Automated judges are useful only with validation/calibration and cannot silently define quality. | F07, F27 | high | Evaluation limits. |
| C14 | Production evaluation and monitoring should continue after launch and include user/ground-truth feedback when available. | F08, F23, F43 | high | Reliability/monitoring. |
| C15 | Monitoring signals must be tied to failure modes and response options. | F23, F39, F43 | high | Reliability; no new incident workflow. |
| C16 | Human oversight must be meaningful, with competence, evidence, authority, and a correction/stop path proportionate to impact. | F24-F25 | high | HITL section; not a new approval gate. |
| C17 | AI safety and misuse analysis should use layered defenses and system-specific evidence, not taxonomy completion as proof. | F29-F32 | high | Safety; defensive only. |
| C18 | Tool-using/agentic systems add authorization, tool-choice, argument, state, handoff, and multi-step failure surfaces. | F09, F31, F35 | high | Integration/workflows; route security and delivery details. |
| C19 | Least privilege and constrained authority are useful design principles for AI integrations. | F31, F35 | high | Defensive design; exact controls belong to architecture/security/DevSecOps. |
| C20 | AI-generated code remains subject to ordinary engineering standards plus AI-specific plausibility and provenance checks. | F33-F36 | high | AI-assisted engineering. |
| C21 | Generated dependencies/APIs, skipped tests, secrets, licensing, and suspicious changes require explicit review. | F34 | high | Review prompts, not a fixed checklist. |
| C22 | Accountability for accepting, merging, deploying, or publishing AI-assisted work remains with authorized humans/teams. | F24, F36 | high | Human boundary; not a new approval workflow. |
| C23 | Logs, traces, corpora, prompts, and eval datasets can be sensitive assets. | F40-F41 | high | Safety/data; route control detail to Cybersecurity/DevSecOps. |
| C24 | A citation or grounded-looking answer is not enough; source provenance and claim support must be inspectable. | F42 | high | RAG/review. |
| C25 | Volatile product features must be refreshed at task time and not encoded as durable canon. | F44 | verified | Source/confidence/update rules. |
| C26 | Fallback, refusal, escalation, degraded operation, and disablement are legitimate reliability options when proportional to failure impact. | F39 | medium-high | System design questions; no mandatory workflow. |
| C27 | Security-sensitive AI questions that primarily concern threats, exploitability, access, or control assurance route to Cybersecurity. | F04, F29-F32 | verified/high | Boundary routing. |
| C28 | Questions primarily about CI/CD, secrets handling, deployment, runtime configuration, artifact provenance, or supply chain route to DevSecOps. | F04, F40-F41 | verified/high | Boundary routing. |
| C29 | Questions primarily about system decomposition, boundaries, quality-attribute tradeoffs, and style/pattern choice route to Software Architecture. | F04 | verified | Boundary routing. |
| C30 | Implementation/change findings and acceptance judgments remain with Engineering Review and the existing review gate. | F03, F33-F36 | verified | Relation to review. |
| C31 | Decision-ready interpretation and recommendations may activate Professional Analysis, while the pack supplies domain evidence and questions only. | R03, F37-F38 | verified/high | Relation to analysis. |
| C32 | One bounded cross-surface pack is architecturally preferable to new prompt/RAG/eval roles, pipelines, or approval systems for this release. | F45 | high | Release architecture decision; reviewer must challenge. |

## Claims not authorized for the pack

- Any named model or provider is universally best, safest, or compliant.
- Passing an eval suite proves production quality or safety.
- Schema-valid output is semantically correct.
- RAG citations prove grounding.
- Human review eliminates AI risk.
- OWASP, MITRE, NIST, a scanner, or a checklist supplies an automatic verdict.
- A prompt technique reliably defeats all instruction-confusion attacks.
- The pack grants authority to approve models, data, security, deployment,
  procurement, legal compliance, or production release.
