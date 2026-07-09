# Sources

## Source policy

- Research date: 2026-07-10.
- Selection rule: repository canon first, then primary standards bodies,
  official security knowledge bases, provider documentation, and official
  engineering guidance.
- Product documentation supports current implementation examples and bounded
  engineering claims. It does not become universal policy.
- Living web sources are stale when their version, URL, product behavior,
  terminology, or public status changes.
- Public ISO pages support only the visible abstract and metadata; no claim is
  attributed to inaccessible standards text.
- Safety sources are used for defensive categories and mitigations only. No
  offensive procedure was collected or preserved.

## Repository canon

| ID | Source | Authority and use | Freshness / limitation |
| --- | --- | --- | --- |
| R01 | [`kb/domain_knowledge_pack_standard.md`](../../kb/domain_knowledge_pack_standard.md) | Canonical pack structure, evidence, boundary, review, update, retirement, and `/about` rules. | Repository-owned; recheck whenever the standard changes. |
| R02 | [`kb/engineering_review.md`](../../kb/engineering_review.md) | Canonical implementation/change-safety owner and review relationship. | Repository-owned. |
| R03 | [`kb/professional_analysis.md`](../../kb/professional_analysis.md) | Canonical decision-ready analysis relationship. | Repository-owned. |
| R04 | [`kb/software_architecture_domain_pack.md`](../../kb/software_architecture_domain_pack.md) | Adjacent design-boundary and architecture-tradeoff context. | Repository-owned. |
| R05 | [`kb/devsecops_domain_pack.md`](../../kb/devsecops_domain_pack.md) | Adjacent delivery, CI/CD, supply-chain, runtime, configuration, and operational-security context. | Repository-owned. |
| R06 | [`kb/cybersecurity_domain_pack.md`](../../kb/cybersecurity_domain_pack.md) | Adjacent threat, defensive control, assurance, misuse, and security-risk context. | Repository-owned. |
| R07 | [`kb/editorial_evidence_framework.md`](../../kb/editorial_evidence_framework.md) | Evidence types, confidence, uncertainty, and claim discipline. | Repository-owned. |

## External authoritative sources

| ID | Source | Authority and use | Accessed / stale-if trigger |
| --- | --- | --- | --- |
| S01 | [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Official guidance for eval-driven development, task-specific datasets, automation, human calibration, and continuous evaluation. | 2026-07-10; stale if page or evaluation guidance changes. |
| S02 | [OpenAI — Prompting](https://developers.openai.com/api/docs/guides/prompting) | Official guidance for instruction placement, examples, prompt versioning, tests, evals, and rollback-oriented prompt management. | 2026-07-10; page contains product-specific and deprecated prompt-object details, which are excluded from durable claims. |
| S03 | [OpenAI — Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Official distinction between schema adherence and semantic correctness; supports validation and function/tool boundary guidance. | 2026-07-10; stale if supported schemas or API behavior changes. |
| S04 | [OpenAI — Retrieval](https://developers.openai.com/api/docs/guides/retrieval) | Official retrieval concepts: semantic search, result scores/origin, query rewriting, filters, chunking, embedding, and indexing. | 2026-07-10; product mechanics are examples, not universal design requirements. |
| S05 | [OpenAI — File search](https://developers.openai.com/api/docs/guides/tools-file-search) | Official example of combined semantic and keyword retrieval over managed corpora. | 2026-07-10; hosted-tool behavior is volatile. |
| S06 | [OpenAI — Agent evals](https://developers.openai.com/api/docs/guides/agent-evals) | Official guidance for trace-level evaluation of tools, routing, handoffs, guardrails, and end-to-end agent behavior. | 2026-07-10; stale if agent/eval platform behavior changes. |
| S07 | [OpenAI — Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) | Official defensive guidance for moderation, adversarial testing, human oversight, constrained inputs/outputs, and source access. | 2026-07-10; product-specific safeguards are not generalized as universal controls. |
| S08 | [Anthropic — Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Official guidance for measurable, task-relevant, multidimensional success criteria; representative tests; code, human, and model grading; judge validation. | 2026-07-10; provider examples and interface details are volatile. |
| S09 | [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Official guidance to define empirical success criteria and tests before prompt optimization. | 2026-07-10; stale if guide changes. |
| S10 | [Anthropic — Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) | Official defensive guidance for separating trusted instructions from untrusted content, provenance, least privilege, screening, monitoring, and layered safeguards. | 2026-07-10; used only at defensive category level. |
| S11 | [Google Cloud Architecture Framework — Operational excellence for AI/ML](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence) | Official guidance for versioning data/model/code, task-specific evaluation, monitoring, controlled release, rollback, drift/anomaly detection, and human evaluation. | Accessed 2026-07-10; page noted last review 2025-04-28; stale on revision. |
| S12 | [Google Cloud Architecture Center — Deploy and operate generative AI applications](https://docs.cloud.google.com/architecture/deploy-operate-generative-ai-applications) | Official production guidance for continuous evaluation, monitoring, feedback/ground truth, skew/drift, and alerting. | 2026-07-10; platform examples are non-universal. |
| S13 | [Google ML Crash Course — Production ML systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems) | Official explanation that production ML quality depends on data collection/verification, serving, monitoring, and infrastructure beyond model code. | 2026-07-10; stale if curriculum changes. |
| S14 | [Google ML — Data quality](https://developers.google.com/machine-learning/guides/data-traps/quality) | Official guidance on data errors, bias, sampling, and downstream model effects. | 2026-07-10; educational source, not a complete data governance standard. |
| S15 | [Google Cloud — Evaluate a judge model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluate-judge-model) | Official guidance that model judges should be evaluated against human ratings or ground truth. | 2026-07-10; product details are volatile. |
| S16 | [Microsoft Azure Architecture Center — RAG solution design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) | Official RAG guidance for representative queries, chunking, enrichment, embeddings, indexing/search, stepwise and end-to-end evaluation, and experiment documentation. | 2026-07-10; stale if architecture guide changes. |
| S17 | [Microsoft Foundry — RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) | Official separation of retrieval-process evaluation from system-level groundedness, relevance, and completeness. | 2026-07-10; product evaluators are examples, not required tooling. |
| S18 | [Microsoft Azure Architecture Center — RAG information retrieval](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) | Official retrieval-quality context including precision, recall, reciprocal rank, positive/negative tests, and query-processing tradeoffs. | 2026-07-10; metric choice remains task-specific. |
| S19 | [Microsoft Azure Architecture Center — Secure multitenant RAG](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag) | Official security boundary: retrieval must preserve tenant/user authorization for grounding data. | 2026-07-10; architecture patterns are contextual, not universal prescriptions. |
| S20 | [AWS Bedrock — Evaluate model performance](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) | Official examples of model and RAG evaluation with custom prompt datasets, automated/model-based/human methods, and ground truth. | 2026-07-10; service behavior is volatile. |
| S21 | [AWS Generative AI Lens — Monitor generative AI applications](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf01-bp02.html) | Official guidance for application-level metrics, telemetry, golden datasets, and task-shaped quality monitoring. | 2026-07-10; stale when lens revises. |
| S22 | [AWS Generative AI Lens — Periodic evaluation](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01.html) | Official guidance for evaluation using feedback, ground truth, and sampled behavior. | 2026-07-10; stale when lens revises. |
| S23 | [AWS Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html) | Official current context for additional failure surfaces introduced by tools, memory, multi-call behavior, and handoffs. | Published 2026-06-10; new and likely to evolve; recheck before relying on specific practices. |
| S24 | [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) | Primary voluntary, use-case-agnostic AI risk-management framework and lifecycle context. | Published 2023-01-26; NIST says revision is underway, so stale upon AI RMF revision. |
| S25 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Primary Govern/Map/Measure/Manage context, continuous application, context/impact/limits, and metric fitness. | 2026-07-10; stale when revised AI RMF is published. |
| S26 | [NIST AI 600-1 — Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Primary cross-sector companion profile for generative-AI risks and actions. | Published 2024-07-26; recheck after AI RMF revision or profile update. |
| S27 | [NIST SP 800-218A — SSDF Community Profile for Generative AI and Dual-Use Foundation Models](https://www.nist.gov/publications/secure-software-development-practices-generative-ai-and-dual-use-foundation-models-ssdf) | Primary secure-development context for AI model/system producers and acquirers, used with SSDF. | Published 2024-07; stale on revision. |
| S28 | [NIST AI 100-2e2023 — Adversarial Machine Learning taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) | Primary terminology for AI attack/mitigation categories across data, models, testing, deployment, and infrastructure. | Published 2024-01; NIST continues updating this topic, so recheck current edition for security-sensitive work. |
| S29 | [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) | Official awareness taxonomy for common LLM-application risk categories. | Version 2025; use as prompts, not proof or a complete control baseline; stale on new edition. |
| S30 | [MITRE ATLAS](https://atlas.mitre.org/) | Official living knowledge base for adversary tactics/techniques and mitigations involving AI-enabled systems. | 2026-07-10; living taxonomy, so recheck current version for security tasks. |
| S31 | [ISO — ISO/IEC 5259-1:2024](https://www.iso.org/standard/81088.html) | Official public metadata/abstract establishing terminology and an overview for data quality in analytics and ML. | 2026-07-10; only public abstract inspected; no inaccessible clause is claimed. |
| S32 | [GitHub Docs — Review AI-generated code](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code) | Official practical guidance for human oversight, tests/static analysis, intent/architecture checks, dependency/license review, AI-specific mistakes, and collaborative review. | 2026-07-10; tools/examples are contextual and volatile. |
| S33 | [GitHub Docs — Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/get-started/best-practices) | Official guidance to understand, review, test, lint, scan, and inspect generated code. | 2026-07-10; provider/product source, generalized only where evidence aligns with broader engineering practice. |
| S34 | [GitHub Docs — Risks and mitigations for Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations) | Official example of constrained agent authority, branch/access boundaries, protected checks, and required human review before merge. | 2026-07-10; implementation-specific controls are illustrative, not universal. |

## Excluded or downgraded source classes

- Unattributed blog posts, SEO summaries, and listicles: excluded.
- Social posts and community anecdotes: excluded because the release needs
  durable authoritative support.
- Provider benchmark marketing: excluded as a basis for universal model choice.
- Search snippets without an inspected primary page: not used as evidence.
- Product-preview details: allowed only as clearly volatile examples and not as
  durable pack requirements.
