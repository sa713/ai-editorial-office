# AI Engineering Domain Pack Landscape

- Release: `S4.R5 - AI Engineering Domain Pack`
- Research date: 2026-07-10
- Audience: Chief Editor, Writer Agent, Review Agent, and Project Lead
- Evidence packet: `tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/`

## Decision summary

World-class AI engineering guidance is converging on system engineering rather
than prompt craft alone. High-quality practice frames the intended task and
impact, treats prompts/data/retrieval/tools/interfaces as versioned system
components, evaluates task behavior with representative evidence, monitors
production outcomes, constrains authority, and keeps human accountability
visible. A durable editorial pack should encode those questions and evidence
expectations while leaving architecture, security, delivery, implementation
review, and approval ownership in existing canon.

## Landscape map

| Surface | Strong practice | Evidence to seek | Failure if omitted |
| --- | --- | --- | --- |
| Problem and user | Intended task, users, impact, limits, failure cost | Use cases, exclusions, affected parties, measurable criteria | Optimizes the wrong behavior |
| Model/provider | Task-shaped comparative evaluation and operational fit | Representative results, latency/cost, constraints, version | Benchmark prestige substitutes for fitness |
| Prompt/instruction | Authority separation, versioning, fixtures/evals, rollback | Prompt version, examples, negative cases, change comparison | Invisible behavioral change or instruction confusion |
| Structured output | Schema plus semantic/domain validation | Parse/schema/semantic checks and downstream error handling | Machine-valid but wrong action/data |
| RAG | Corpus-to-answer pipeline with permissions and provenance | Corpus manifest, retrieval tests, answer tests, citations/provenance | Fluent unsupported answer or access leak |
| Data | Provenance, rights, sensitivity, representativeness, freshness | Dataset/source notes, sampling/quality checks, access conditions | Biased, stale, contaminated, or unauthorized behavior |
| Evaluation | Objective, representative set, criteria, baseline, graders | Cases, rubrics, thresholds, human calibration, regression results | Demo/vibe becomes acceptance evidence |
| Reliability | Observable failure modes, continuous evaluation, fallback | Quality/safety/latency/error signals and response mapping | Silent degradation or unrecoverable change |
| Human oversight | Competence, evidence, authority, correction/stop path | Review design and accountability boundary | Ceremonial human-in-the-loop |
| Safety/misuse | Layered defense, least privilege, adversarial testing | Threat assumptions, permission map, safety cases, residual risk | Taxonomy/checklist theater |
| Tools/agents | Trace tool choice, arguments, state, handoffs, side effects | Trace/eval cases, authorization, idempotency/retry evidence | Correct text with unsafe system action |
| AI-assisted coding | Human understanding plus tests/scans/dependency review | Diff, tests, static/security checks, provenance/license review | Plausible but defective or risky change |

## Authoritative ecosystem findings

### Standards and public-interest frameworks

NIST AI RMF supplies the broadest vendor-neutral context: risks are mapped,
measured, and managed within continuous governance and use context. The
Generative AI Profile adds GenAI-specific risk considerations, while SP
800-218A connects AI development to secure software-development practice. NIST
AI 100-2 supplies defensive adversarial-ML terminology. These sources are
strong for context, lifecycle risk, evidence limits, and category awareness;
they do not provide a product acceptance verdict.

ISO/IEC 5259-1:2024 establishes a public scope for data-quality terminology in
analytics and ML. Only its public abstract was inspected, so it is a weak
supporting pointer rather than detailed normative evidence.

### Security knowledge bases

OWASP Top 10 for LLM Applications and MITRE ATLAS are current living resources
for defensive risk discovery. Their value is category coverage and shared
language. Their limitation is equally important: neither proves a specific
system vulnerable, secure, or compliant. Exact editions and entries must be
refreshed during security-sensitive tasks.

### Model/provider engineering guidance

OpenAI contributes unusually explicit guidance on eval-driven development,
prompt-as-code discipline, structured-output limits, retrieval mechanics,
trace-level agent evaluation, and layered safety. Anthropic independently
reinforces empirical success criteria, representative tests, grader selection,
and untrusted-content separation. Agreement across these providers increases
confidence in the durable principles; their product interfaces and deprecated
features remain volatile.

Google's production-ML and architecture guidance emphasizes the surrounding
system: data verification, infrastructure, serving, monitoring, versioning,
drift, controlled release, rollback, and human evaluation. Microsoft provides
the clearest official decomposition of RAG evaluation into retrieval-process
and answer/system quality. AWS adds application-level monitoring, golden data,
sampled evaluation, and current agentic-system failure-surface context.

### AI-assisted engineering

GitHub's official guidance is product-specific but its review principles are
durable: understand the suggestion, test and analyze it, verify architecture
and intent, scrutinize dependencies and licenses, catch hallucinated APIs or
deleted tests, and keep human review before merge/deployment. Current cloud
agent controls illustrate constrained authority through branch, credential,
tool, check, and merge boundaries.

## Evaluation design pattern

A reusable evaluation pattern emerges across sources:

1. Define the intended behavior, users, material impacts, and failure cost.
2. Translate them into observable criteria and unacceptable outcomes.
3. Build a representative case set with normal, edge, and material adverse
   cases.
4. Select component and end-to-end measures suited to the failure model.
5. Establish a baseline or prior-version comparison.
6. Choose deterministic, human, or model-based graders and validate their fit.
7. Run before release, on material change, and through proportionate production
   sampling.
8. Interpret results by slice and failure type; do not hide uncertainty in one
   aggregate score.

This is a reasoning pattern, not a new AI Editorial Office pipeline or gate.

## RAG design pattern

RAG evidence should remain separable across:

- corpus authority, provenance, rights, sensitivity, and freshness;
- ingestion, parsing, chunking, enrichment, and index/embedding version;
- query understanding, filtering, authorization, and ranking;
- context selection and provenance transfer;
- answer correctness, relevance, completeness, groundedness, and abstention;
- production feedback, drift, source removal, and re-index behavior.

No single citation, retrieval score, or end-to-end answer score covers every
stage. The useful minimum is to locate the failure and preserve enough evidence
to reproduce it.

## Boundary map

| Primary question | Primary context owner | AI Engineering contribution |
| --- | --- | --- |
| Does the system decomposition or quality tradeoff fit? | Software Architecture Domain Pack | AI-specific surfaces and failure modes |
| What threat, misuse, control, or assurance question exists? | Cybersecurity Domain Pack | AI-specific assets, trust inputs, and behavior categories |
| How should CI/CD, secrets, deployment, runtime, or supply chain be handled? | DevSecOps Domain Pack | AI artifacts and runtime signals that need delivery treatment |
| Is this implementation/change safe and validated? | Engineering Review | AI-specific review prompts and expected evidence |
| What decision and recommendation should the analysis present? | Professional Analysis | AI domain evidence, uncertainty, and tradeoffs |

## Recommended pack architecture

Use one canonical file with:

- identity, purpose, activation, questions, and domain boundary;
- concise vocabulary and principles;
- system-surface map;
- focused sections for prompt/instruction, RAG, data, evaluation,
  reliability/monitoring, human oversight, safety/misuse,
  integrations/workflows, and AI-assisted engineering;
- review questions, mistakes, sources, confidence, update, retirement, and
  adjacent-owner relations;
- explicit statements that all patterns are context, not mandatory workflow.

Do not add roles, capabilities, registries, frameworks, pipelines, lifecycle
stages, approval workflows, review gates, scoring systems, or ordinary-task
artifacts.

## Research limitations

- Provider documentation is current to the research date but changes rapidly.
- Sources are English-language and weighted toward major cloud/model providers
  plus public standards bodies.
- No private product terms, enterprise configurations, or paywalled standards
  text were inspected.
- The landscape does not compare model quality or recommend a vendor.
- Safety research intentionally excludes operational abuse detail.

## Source pointer

Full source metadata, fact extraction, claim mapping, contradictions, and
stale-if triggers are preserved in:

- `tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/sources.md`;
- `tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/facts.md`;
- `tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/claims_table.md`;
- `tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/research.md`.
