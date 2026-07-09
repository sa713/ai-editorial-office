# Facts

Facts below are extracted or conservative syntheses of the inspected sources.
They are inputs to editorial claims, not automatic policy.

| ID | Fact | Source | Confidence / limit |
| --- | --- | --- | --- |
| F01 | A Domain Knowledge Pack supplies bounded context and does not create a role, capability, pipeline, lifecycle stage, gate, policy owner, or mandatory ordinary artifact. | R01 | Verified repository canon. |
| F02 | Active pack use must expose activation reason, relevant sections/sources, confidence, boundary limits, stale-if triggers, and stop conditions in existing task artifacts. | R01 | Verified repository canon. |
| F03 | Engineering Review owns implementation/change-safety challenge; a domain pack may inform it but cannot replace it. | R01, R02 | Verified repository canon. |
| F04 | Software Architecture owns design fitness and architecture tradeoffs; DevSecOps owns delivery/automation/runtime context; Cybersecurity owns threat/control/assurance context. | R04, R05, R06 | Verified repository canon. |
| F05 | Effective evaluation begins with an explicit objective, representative data, and task-specific success criteria rather than a generic score. | S01, S08, S09 | Supported across providers. |
| F06 | Evaluation should include normal, edge, adversarial, and production-representative cases when those conditions are material. | S01, S07, S08, S22 | Supported; exact distribution is task-specific. |
| F07 | Automated graders can scale evaluation, but their judgments should be calibrated or checked against human ratings, rubrics, or ground truth. | S01, S08, S15, S20 | Supported across providers. |
| F08 | Evaluation is a continuing engineering activity across changes and production sampling, not a one-time launch exercise. | S01, S11, S12, S21, S22 | Strongly supported. |
| F09 | Agentic behavior adds observable decision boundaries such as tool selection, arguments, routing, handoffs, guardrail behavior, and multi-step traces. | S06, S23 | Supported; product implementations differ. |
| F10 | Prompt and instruction changes can be versioned and tested like application changes, with fixtures/evals and a rollback or comparison path. | S02, S09 | Supported; exact tooling is contextual. |
| F11 | System/developer instructions, user requests, retrieved content, tool output, and examples do not have equal trust or authority. | S02, S10, R06 | Supported defensive principle; implementation-specific precedence differs. |
| F12 | Clear separation between trusted instructions and untrusted content reduces instruction-confusion risk. | S10, S29 | Supported defensive category-level guidance. |
| F13 | Structured-output schema conformance does not guarantee semantic correctness. | S03 | Verified for cited product; durable inference is strong but still requires task validation. |
| F14 | Tool/function interfaces and user-facing structured responses serve different integration purposes and should be selected deliberately. | S03 | Supported product example; generalized cautiously. |
| F15 | Retrieval systems include a corpus, ingestion/indexing, chunking, representation, query processing, filtering/ranking, context assembly, and answer behavior. | S04, S16, S18 | Supported synthesis. |
| F16 | Retrieval quality and answer quality are separable; a system may retrieve the wrong evidence or misuse good evidence. | S16, S17, S18 | Strongly supported. |
| F17 | Retrieval evaluation can use ranked-retrieval measures and end-to-end measures such as groundedness, relevance, completeness, or answer correctness, selected for the task. | S17, S18 | Supported; no metric is universally sufficient. |
| F18 | Representative queries, positive and negative cases, and documented experiments improve RAG evaluation. | S16, S18 | Supported. |
| F19 | Retrieval authorization must remain aligned with tenant/user access to grounding data. | S19 | Supported architecture/security boundary. |
| F20 | Production AI quality depends on data, serving, monitoring, infrastructure, and integration, not only on model behavior. | S11, S12, S13 | Strongly supported. |
| F21 | Data errors, sampling problems, bias, weak provenance, and training/serving differences can degrade AI behavior. | S11, S12, S14, S31 | Supported; ISO detail limited to public abstract. |
| F22 | Versioning relevant data, code, model/provider configuration, prompts, and evaluation assets improves reproducibility and rollback. | S02, S11 | Supported. |
| F23 | Useful production signals may include task quality, safety outcomes, latency, errors, resource/cost behavior, drift, feedback, and trace data. | S11, S12, S21 | Supported; selection must follow system risk and observability limits. |
| F24 | Human oversight is especially important for high-stakes outputs and code generation, and reviewers need enough source/context access to judge outputs. | S07, S24, S26, S32 | Supported; oversight design remains use-case-specific. |
| F25 | Human review is not meaningful if the reviewer lacks authority, time, domain competence, evidence, or a safe way to correct/stop the system. | S07, S24, S25 | Supported synthesis; phrasing is an inference from oversight and risk-management guidance. |
| F26 | AI risk management is contextual and continuous; intended users, affected parties, impacts, limitations, and metric fitness matter. | S24, S25, S26 | Strongly supported. |
| F27 | Risks that cannot be measured reliably should be documented rather than converted into fake precision. | S25 | Strongly supported. |
| F28 | NIST extends secure-development practices to AI model/system producers and acquirers through SP 800-218A. | S27 | Verified metadata/abstract claim. |
| F29 | OWASP's LLM Top 10 and MITRE ATLAS are living awareness/taxonomy resources, not proof that a system is vulnerable or safe. | S29, S30 | Supported by source type; verdict limitation is analytical. |
| F30 | Defensive AI-system review should consider prompt injection/instruction confusion, sensitive-information disclosure, supply chain, data/model poisoning, output handling, excessive agency, retrieval/vector weaknesses, misinformation, and resource consumption where relevant. | S28, S29, S30 | Supported category-level synthesis; no exploit detail retained. |
| F31 | Least privilege, narrow tool permissions, untrusted-data separation, output screening, adversarial testing, and monitoring are layered defensive measures for tool-using AI systems. | S07, S10, S29, S34 | Supported; control fit is contextual. |
| F32 | A safety taxonomy or checklist cannot substitute for system-specific threat analysis, validation evidence, and residual-risk judgment. | S24, S25, S28, S29, S30, R06 | Supported synthesis. |
| F33 | AI-generated code should be understood, reviewed for intent and architecture, compiled/tested, and checked with applicable static/security/dependency tooling before reliance. | S32, S33 | Strong provider guidance; consistent with R02. |
| F34 | Generated-code review should scrutinize hallucinated APIs/packages, suspicious or incompatible dependencies, licensing, deleted/skipped tests, hidden assumptions, and code that only appears plausible. | S32 | Supported official guidance. |
| F35 | An AI coding agent's authority can be constrained by repository/branch permissions, protected checks, restricted credentials/tools, and human review before merge. | S34 | Verified provider implementation; use as design example, not mandatory architecture. |
| F36 | AI-generated review or code suggestions do not transfer accountability away from the human/team responsible for acceptance and deployment. | S32, S33, S34, R02 | Supported synthesis. |
| F37 | Model/provider choice should be based on task-shaped evaluation, constraints, risk, latency/cost, integration, and operational fit rather than public benchmark ranking alone. | S01, S08, S11, S20, S21 | Supported synthesis; exact dimensions vary. |
| F38 | Quality thresholds and acceptable tradeoffs depend on user impact and failure cost; one number rarely captures all relevant dimensions. | S01, S08, S24, S25 | Supported. |
| F39 | Fallback, refusal, escalation, degraded-mode, or disablement behavior should be designed when failure has material impact. | S07, S11, S12, S24, S26 | Supported synthesis; exact mechanisms are system-specific. |
| F40 | Logs and traces may themselves contain sensitive data and therefore need minimization, access control, retention, and security review. | R06, R05, S21 | Supported boundary synthesis; detailed control design belongs to adjacent owners. |
| F41 | Provider retention, training use, regional processing, legal terms, and privacy behavior are product/account-specific and must be checked at task time. | R06, R05 | Verified boundary logic; no universal provider claim made. |
| F42 | RAG citations or source links improve inspectability only when they preserve real provenance and support the claim; citation presence alone does not prove groundedness. | S04, S16, S17, R07 | Supported synthesis. |
| F43 | Monitoring should connect signals to intended behavior, user impact, and response options; collecting telemetry without interpretation does not establish reliability. | S11, S12, S21, S24 | Supported synthesis. |
| F44 | Product preview features and current API behavior can change quickly and should not anchor durable repository canon. | R01, R07, source limitations | Verified editorial rule plus observed source volatility. |
| F45 | A single broad AI Engineering Pack can cover shared system surfaces while routing security, delivery, architecture, review, and analytical ownership to existing canon. | R01-R06 and full synthesis | High-confidence architecture judgment, subject to review. |

## Contradictions and reconciliations

- Provider docs differ in terminology, tooling, and preferred evaluation
  interfaces. Reconciliation: preserve common engineering principles; keep
  provider mechanics as examples requiring task-time verification.
- Sources sometimes promote automated/model grading while also requiring human
  evaluation. Reconciliation: automation increases coverage; calibrated human
  judgment remains necessary for ambiguous, high-impact, or judge-quality
  questions.
- Security taxonomies organize risks differently. Reconciliation: use them as
  complementary category prompts, not a merged pass/fail checklist.
- RAG sources use different end-to-end metric names. Reconciliation: distinguish
  retrieval from generation and select observable criteria from the failure
  model rather than standardizing one vocabulary.
