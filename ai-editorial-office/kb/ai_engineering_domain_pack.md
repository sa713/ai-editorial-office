# AI Engineering Domain Knowledge Pack

## Pack Identity

- Pack name: AI Engineering Domain Knowledge Pack
- Domain: AI engineering for AI-enabled systems
- Current status: active
- Owner / maintainer context: AI Editorial Office canonical KB; maintained
  through the Domain Knowledge Pack Standard, current authoritative sources,
  independent review, and Chief Editor governance. The pack creates no Domain
  Owner role.
- Created: 2026-07-10
- Last reviewed: 2026-07-10, independent review round 2 approved
- Stale if:
  - the Domain Knowledge Pack Standard or an adjacent canonical owner changes;
  - NIST revises AI RMF or related GenAI/secure-AI publications;
  - OWASP or MITRE materially revises AI/LLM risk taxonomies;
  - provider guidance materially changes model, prompt, retrieval, structured
    output, evaluation, tool/agent, data-use, or safety behavior;
  - repeated tasks expose a missing surface, misleading term, unsafe detail, or
    owner-boundary conflict;
  - the current source register can no longer support a material claim.

This pack is an accepted, active source-backed context package under
`kb/domain_knowledge_pack_standard.md` following Project Lead acceptance.

It does not create an AI Engineer role, AI Reviewer role, capability, framework,
pipeline, lifecycle stage, governance layer, policy owner, model owner, data
owner, approval workflow, review gate, scoring system, client profile, or
mandatory ordinary task artifact.

## Purpose

This pack helps AI Editorial Office reason accurately about the engineering of
AI-enabled systems: systems in which model behavior interacts with users,
instructions, data, retrieval, tools, interfaces, runtime conditions,
monitoring, feedback, and human responsibility.

It provides vocabulary, principles, evidence expectations, failure questions,
review prompts, source limits, and adjacent-owner routing for work involving:

- model or provider fit;
- prompt and instruction behavior;
- structured outputs and AI-facing interfaces;
- retrieval-augmented generation and internal knowledge;
- AI data quality and provenance;
- evaluation design and interpretation;
- reliability, observability, monitoring, and change;
- meaningful human oversight;
- defensive AI safety and misuse risk;
- tool-using, agentic, or multi-step AI workflows;
- AI-assisted software engineering.

The pack should improve domain depth without turning guidance into hidden
process or authority.

## Intended Use

Use this pack to improve:

- research and evidence plans for AI-enabled products or features;
- technical and architecture analysis involving AI-specific behavior;
- evaluation plans, result interpretation, and release reasoning;
- prompt, retrieval, structured-output, tool, or model-change review context;
- reliability and monitoring recommendations for AI behavior;
- safety-aware, defensive analysis of model-integrated systems;
- implementation/change review when AI-specific surfaces are material;
- decision-ready recommendations whose tradeoffs depend on AI behavior;
- explanations and handoffs that must preserve AI-specific uncertainty.

Use only the sections and sources material to the task. This is reference
context, not a mandatory sequence or checklist.

## When To Activate

Activate the pack when AI-specific domain context materially changes evidence
depth, terminology, risk handling, review focus, or output quality.

Typical activation signals include:

- selecting or changing a model, provider, embedding, reranker, or AI service;
- designing or reviewing prompts, instruction hierarchies, examples, context
  assembly, or structured outputs;
- building or evaluating RAG, search-grounded answers, citations, or an
  internal-knowledge assistant;
- defining an AI-system evaluation plan, dataset, rubric, grader, threshold,
  benchmark, or production quality signal;
- working with fine-tuning, labeled data, synthetic data, data quality, data
  provenance, or training/serving differences;
- changing a tool-using, multi-step, agentic, or human-in-the-loop workflow;
- making claims about AI reliability, safety, hallucination, groundedness,
  monitoring, drift, fallback, or refusal;
- using AI to generate, modify, test, review, or explain code where the AI
  origin affects verification or risk;
- handling sensitive data, consequential decisions, or external side effects
  through an AI-enabled system;
- reviewing current product/provider behavior that can change over time.

Record activation in existing task artifacts with:

- activation reason;
- relevant sections and source IDs;
- confidence and evidence limits;
- adjacent packs or capabilities also active;
- product/version/account assumptions and stale-if triggers;
- stop or escalation conditions.

## When Not To Activate

Do not activate merely because:

- the text mentions AI, machine learning, automation, a model name, or a vendor;
- AI is a background topic with no material effect on the requested judgment;
- the task is ordinary copyediting, translation, summarization, or layout work;
- the primary question is a general software design decision with no AI-specific
  behavior;
- the primary question concerns application security, access control,
  vulnerability, threat, or control assurance and belongs to Cybersecurity;
- the primary question concerns CI/CD, secrets, deployment, configuration,
  artifact provenance, supply chain, or runtime operations and belongs to
  DevSecOps;
- the primary question is whether an implementation change is safe and correct,
  which remains Engineering Review ownership;
- a current legal, privacy, procurement, employment, medical, financial, or
  compliance conclusion is required without the proper task-specific sources
  and authority.

Stop using the pack when AI-specific context no longer changes the evidence,
risk, or output. Keep only the primary owner active.

## Questions This Pack Can Answer

The pack can help answer:

- What is the AI-enabled system boundary, not just the model boundary?
- Which behavior, user outcome, impact, and failure cost should drive design and
  evaluation?
- What evidence is needed to compare models or providers for this task?
- How should prompt and instruction changes be specified, versioned, tested,
  and interpreted?
- What must be validated beyond a structured-output schema?
- Where can a RAG system fail between corpus selection and answer use?
- How should retrieval quality and answer quality be tested separately and end
  to end?
- Which data-quality, provenance, rights, sensitivity, and freshness questions
  matter?
- What makes an evaluation representative, repeatable, and decision-useful?
- How should automated or model-based graders be calibrated?
- Which production signals provide evidence of quality, safety, reliability,
  drift, or degradation?
- When is human oversight meaningful rather than ceremonial?
- What AI-specific safety categories and defensive evidence should be examined?
- What additional failure surfaces appear when models use tools, state, memory,
  routing, or handoffs?
- How should AI-generated code or review suggestions be verified?
- Which adjacent pack or capability owns the next judgment?

It cannot determine by itself:

- that a system, model, provider, prompt, dataset, or workflow is safe;
- that a model is universally best or fit for every population;
- that an evaluation suite proves production quality;
- that a schema-valid output is semantically correct;
- that a cited answer is grounded or authorized;
- that a system is secure, compliant, private, lawful, fair, or approved;
- that a deployment, merge, procurement, data use, or production release should
  be authorized;
- that an OWASP, MITRE, NIST, vendor, benchmark, scanner, or checklist result is
  an automatic pass/fail verdict.

## Domain Boundary

AI engineering is the evidence-driven design, integration, evaluation,
operation, and change reasoning for AI-enabled system behavior. Its object is
the whole system:

```text
people and intended use
+ instructions and context
+ models/providers
+ data and retrieval
+ interfaces, tools, state, and side effects
+ validation and evaluation
+ runtime, monitoring, and feedback
+ human accountability
```

The pack owns none of these components operationally. It supplies shared domain
context for roles and capabilities already authorized by repository canon.

Boundary routing:

- use the Software Architecture Domain Pack for decomposition, architectural
  boundaries, style/pattern choice, and quality-attribute tradeoffs;
- use the Cybersecurity Domain Pack for threats, abuse, access control,
  exploitability, security controls, assurance, and residual security risk;
- use the DevSecOps Domain Pack for CI/CD, secrets, configuration, artifacts,
  supply chain, deployment, runtime operations, and operational evidence;
- use Engineering Review for implementation/change findings, severity,
  validation sufficiency, and residual implementation risk;
- use Professional Analysis for decision-ready synthesis, options,
  recommendations, implications, and uncertainty presentation;
- use current task-specific legal, privacy, compliance, procurement, or domain
  expertise when those conclusions are material.

When concerns overlap, name a primary context and use this pack only for the
AI-specific surface. Do not merge owner responsibilities.

## Evidence And Confidence Rules

Use evidence that matches the claim and decision. The pack supports bounded
engineering claims about AI-system surfaces, common failure modes, evidence
questions, evaluation design, source limits, and adjacent-owner routing. It
does not support universal product, safety, security, privacy, legal,
compliance, fairness, or approval claims.

Acceptable source classes include:

- repository canonical owners for AI Editorial Office architecture, roles,
  capabilities, pack boundaries, evidence, review, and governance;
- primary standards-body and government publications for their stated scope;
- official living security knowledge bases for defensive category discovery;
- first-party provider documentation for current behavior of that provider's
  products, with date/version/account limits;
- official engineering documentation from major platforms for contextual
  practices, corroborated before being generalized;
- peer-reviewed or primary technical research when a material technical claim
  requires it;
- task-specific empirical evidence such as representative evaluations, tests,
  traces, logs, user/ground-truth feedback, and observed production behavior.

Insufficient evidence for high-governance claims includes:

- model memory, search snippets, unattributed summaries, SEO content, or
  unsaved conversation claims;
- provider marketing or benchmark claims without task-shaped comparison;
- one demo, anecdote, prompt example, or average score;
- community posts without reconstructable primary evidence;
- an uncalibrated model judge or undocumented rubric;
- a citation, schema pass, scanner result, taxonomy match, checklist, or human
  approval label used as automatic proof;
- stale product documentation or an edition/version that no longer matches the
  system under review.

Confidence rules:

- `verified` is appropriate for inspected repository canon and directly
  observed validation results within their scope;
- `supported` is appropriate for durable engineering synthesis corroborated by
  authoritative sources;
- `inferred` must expose the reasoning, assumptions, and validation still
  needed;
- product/provider claims must name current version or observation date and a
  stale-if trigger;
- conflicting or unavailable evidence must lower confidence, narrow the claim,
  return the task to research, or trigger an owner escalation;
- no evaluation can establish the absence of all unknown failures.

The Source Register below is canonical for this pack and uses the same stable
`R01-R07` and `S01-S34` namespace as the release task evidence. Future updates
must preserve IDs for unchanged sources or record an explicit replacement map.

## Domain Vocabulary

| Term | Meaning in this pack | Boundary note |
| --- | --- | --- |
| AI-enabled system | A system whose behavior materially depends on a trained model or AI service plus surrounding components and people. | Not synonymous with the model. |
| Model | A learned computational component that maps input/context to output or decisions. | Exact capabilities are version-specific. |
| Provider | A party or platform supplying model/API/runtime behavior. | Terms, retention, regions, limits, and versions require current verification. |
| Inference | Running a model to produce scores, representations, text, structured values, or actions. | Does not imply correctness. |
| Prompt | Input and contextual material used to elicit model behavior. | May include instructions, examples, retrieved context, and user data with different authority. |
| Instruction | A directive intended to shape behavior. | Authority and provenance matter; content can contain instruction-like text without being trusted. |
| Context window | The finite input state available to a model invocation. | Size, truncation, and attention behavior are model/version-specific. |
| Structured output | Output expected to conform to a machine-readable schema or contract. | Schema conformance is not semantic correctness. |
| Embedding | A numerical representation used for similarity or downstream ML tasks. | Fit depends on data, task, version, and evaluation. |
| Retrieval-augmented generation (RAG) | Use of retrieved external content as context for model output. | Retrieval, authorization, context use, and answer behavior are separable. |
| Chunk | A unit created from source content for indexing or retrieval. | Chunking changes recall, context, provenance, and answer behavior. |
| Groundedness | Degree to which an output's material claims are supported by supplied evidence. | Terminology and measures vary; citations alone do not prove it. |
| Hallucination | A fluent output that is unsupported, false, inconsistent with evidence, or otherwise fabricated in the relevant context. | Too broad for diagnosis; name the observable failure. |
| Evaluation case | A defined input/context with expected behavior, criteria, or reference evidence. | It may be deterministic, rubric-based, comparative, or exploratory. |
| Evaluation set | A collection of cases intended to represent material behavior and failure conditions. | Representativeness and leakage matter more than size alone. |
| Golden set | A curated evaluation set with trusted references or judgments. | It can age, contain bias, and require versioning. |
| Grader / judge | A deterministic rule, human, or model used to evaluate outputs or traces. | A model judge must itself be evaluated for the intended use. |
| Baseline | A prior system/version, simple method, or established result used for comparison. | Not automatically an acceptance threshold. |
| Drift | A material change in input, data, behavior, or performance distribution over time. | Diagnose the type before prescribing response. |
| Trace | A record of relevant steps, model calls, tool use, routing, state, and outputs. | May contain sensitive data; trace completeness varies. |
| Tool | An interface through which an AI-enabled system reads data, computes, or causes external effects. | Tool authority and output trust require explicit boundaries. |
| Agentic behavior | Model-influenced selection and sequencing of actions, tools, state, or handoffs toward a goal. | Avoid treating `agent` as a stable universal product taxonomy. |
| Human-in-the-loop (HITL) | A design in which human judgment or action is intentionally placed in system behavior. | A label does not prove effective oversight. |
| Guardrail | A bounded measure intended to constrain, detect, or respond to undesirable behavior. | No single guardrail proves safety. |
| Fallback | An alternate behavior when confidence, availability, safety, or quality conditions are not met. | Can include refusal, human escalation, degraded mode, or disablement. |
| AI-assisted engineering | Use of AI to support software planning, generation, modification, testing, review, or explanation. | Generated work remains subject to ordinary engineering accountability. |

## AI Engineering Principles

### Engineer The System, Not The Demo

A compelling output demonstrates possibility, not dependable system behavior.
Include users, data, instructions, interfaces, tools, runtime conditions,
monitoring, feedback, and human responsibility in the system boundary.

### Start From Behavior And Impact

Define intended users, task, acceptable behavior, unacceptable outcomes,
failure cost, and observable success before optimizing a prompt or selecting a
model. Requirements that cannot be observed cannot be evaluated directly; name
their uncertainty instead of inventing precision.

### Separate Component Quality From End-To-End Quality

A model, retriever, prompt, schema, tool, or grader can perform well in
isolation while the system fails. Test material components and their
interactions, then test the outcome experienced by the user or downstream
system.

### Evidence Must Match The Decision

A benchmark may help shortlist models. A schema test may validate an interface.
A retrieval metric may diagnose search. A red-team case may expose one failure.
None alone answers whether the whole system is fit to release. Choose evidence
for the actual decision and failure cost.

### Treat Change As A Behavioral Change Until Shown Otherwise

Model versions, provider configuration, prompts, tools, data, corpora,
chunking, embeddings, routing, libraries, and downstream interfaces can change
behavior. Preserve versions, comparison evidence, and recovery options
proportionate to impact.

### Keep Authority And Trust Explicit

System/developer instructions, user requests, retrieved documents, tool
outputs, memory, and model-generated content do not have equal authority.
Separate trusted directions from untrusted data and constrain the authority of
tools and identities.

### Prefer Observable Failure Over Vague Labels

Replace “the AI hallucinated” with the smallest supported diagnosis: wrong
retrieval, missing context, unsupported claim, invalid tool argument, stale
source, schema-valid wrong value, unsafe instruction following, or failed
handoff. Specific failures lead to specific evidence and owners.

### Human Oversight Must Be Operable

A human is not a safety control merely by being present. Oversight should give
the person adequate evidence, context, competence, time, authority, and a way
to correct, refuse, stop, or escalate proportionate to impact.

### Defense Is Layered And Residual Risk Remains

Instruction design, filtering, least privilege, validation, sandboxing,
monitoring, evaluation, and human oversight cover different failure paths.
Combine relevant layers and state what risk remains. Route security judgment to
Cybersecurity context.

### Reproducibility Has Limits But Still Matters

AI outputs can be nondeterministic and providers can change. Preserve the
inputs, versions, configuration, data/corpus state, tool results, evaluation
logic, and observation time needed to reconstruct the decision as far as the
system permits.

### Production Feedback Completes Evaluation

Pre-release tests cannot represent every real interaction. Use proportionate
production sampling, user/ground-truth feedback, failure monitoring, and
change-triggered re-evaluation while respecting privacy and security limits.

## AI System Surfaces

Use this map to identify material surfaces. It is not a required architecture
or artifact list.

| Surface | Questions | Typical evidence | Primary adjacent owner when deeper |
| --- | --- | --- | --- |
| Intended use and users | What task, user, decision, impact, and exclusion define fitness? | Use cases, exclusions, affected parties, acceptance rationale | Professional Analysis / domain expert |
| Model/provider | Why this version/provider for this task and constraints? | Comparative evals, version/config record, latency/cost and limitation evidence | Software Architecture / procurement as applicable |
| Instructions/context | Which directions are authoritative? What can be untrusted? | Versioned prompts, examples, negative cases, change diff | Cybersecurity for instruction-confusion risk |
| Input interface | What forms, sizes, languages, modalities, or invalid cases occur? | Schemas, validators, representative inputs, error behavior | Engineering Review |
| Output interface | What consumes the output and what if it is wrong? | Schema and semantic tests, downstream contract, fallback | Software Architecture / Engineering Review |
| Data | Where did it come from; is it representative, permitted, sensitive, and fresh? | Provenance, quality checks, rights/access notes, version | Cybersecurity / data/legal authority |
| Retrieval | Can the right authorized evidence be found and preserved? | Corpus/index version, query set, ranked results, provenance | Cybersecurity for access; Architecture for design |
| Tools and side effects | What can the system read/change; under which identity and limits? | Tool contract, permission map, trace, adverse cases | Cybersecurity / DevSecOps / Engineering Review |
| State and memory | What persists, for whom, for how long, and how is it corrected? | State model, retention/access evidence, reset/correction behavior | Software Architecture / Cybersecurity |
| Evaluation | Which cases, criteria, graders, thresholds, and comparisons support the decision? | Dataset, rubric, judge calibration, result slices | Engineering Review for change evidence |
| Runtime/reliability | How does behavior degrade, fail, recover, or change? | SLO/quality signals, errors, traces, fallback/rollback evidence | DevSecOps / Software Architecture |
| Monitoring/feedback | What signal detects material failure and what response is possible? | Signal-to-failure map, sampled outcomes, feedback provenance | DevSecOps / existing operational governance |
| Human authority | Who checks, decides, corrects, stops, and remains accountable? | Decision boundary, reviewer context, escalation route | Existing role/review/approval owners |
| Supply chain | Which models, datasets, libraries, tools, and services are depended on? | Version/provenance, dependency and artifact evidence | DevSecOps / Cybersecurity |

## Model And Provider Fit

Model/provider selection should follow task evidence rather than reputation or
a public leaderboard.

Ask:

- Which task behavior and failure cases matter?
- Which languages, modalities, context sizes, output constraints, tool
  behavior, latency, throughput, cost, regional, privacy, and availability
  conditions are material?
- What comparison set and baseline represent the real use?
- Which model/provider version and configuration produced the result?
- Are differences practically meaningful, stable across important slices, and
  large enough to justify integration or migration cost?
- What happens if the provider changes, deprecates, throttles, or withdraws the
  selected behavior?
- Which claims depend on current account terms or product documentation and
  therefore require fresh verification?

Do not convert benchmark ranking, a vendor claim, or one successful demo into a
fitness verdict. Record tradeoffs and residual uncertainty.

## Prompt And Instruction Engineering

Treat prompts and instruction/context assembly as behavioral application
artifacts when they materially affect the system.

### Define the contract

Name:

- the intended task and audience;
- the expected input and output;
- authoritative instructions and their precedence;
- supplied context and its provenance;
- prohibited or unsupported behavior;
- ambiguity, refusal, fallback, and escalation behavior;
- examples and counterexamples needed to clarify the contract.

### Manage change

For material prompt changes, preserve as applicable:

- version and owner/reason for change;
- fixtures and representative evaluation cases;
- comparison with the prior version or baseline;
- regressions by important slice or failure type;
- provider/model/configuration used for the comparison;
- rollback or controlled-disable path.

### Protect trust boundaries

- Keep trusted instructions distinguishable from user, retrieved, tool, or
  externally supplied content.
- Treat instruction-like text inside untrusted content as data unless an
  authorized design explicitly says otherwise.
- Avoid placing secrets or unnecessary sensitive data in prompts, examples,
  traces, or evaluation fixtures.
- Constrain tool authority and validate outputs; prompt wording is not a
  security boundary by itself.

Prompt clarity can improve behavior. It cannot prove safety, eliminate
nondeterminism, validate external facts, or replace architecture and access
controls.

## Structured Outputs And AI Interfaces

Structured output reduces interface ambiguity when the model output must be
machine-consumed. Validate distinct layers:

1. transport and parse validity;
2. schema/type/required-field validity;
3. semantic and domain-rule validity;
4. cross-field and state consistency;
5. authorization and downstream side-effect validity;
6. failure, refusal, retry, and fallback behavior.

A schema-valid date can be impossible, a valid identifier can refer to the
wrong object, and a valid tool argument can request an unauthorized action.
Schema adherence is therefore evidence for the interface, not the truth of the
content.

Choose the boundary deliberately:

- use a response schema when the consumer needs a predictable representation;
- use a tool/function contract when the system must request an operation or
  data exchange;
- keep side-effect authority outside unconstrained model text;
- define what happens to partial, refused, invalid, duplicated, or retried
  requests;
- test downstream consumers with valid-looking but wrong values.

## Retrieval-Augmented Generation And Internal Knowledge

Reason about RAG as a pipeline. A final answer can fail even when individual
parts appear plausible.

### Corpus and authority

Ask:

- Which sources are authoritative for which claims?
- Who may access each source, tenant, project, or record?
- What rights, privacy, retention, deletion, and freshness constraints apply?
- Are duplicates, conflicts, obsolete versions, scans, tables, images, or
  unsupported formats material?
- Can source removal or permission change propagate to the index and cache?

### Ingestion and representation

Inspect:

- parsing and extraction quality;
- chunk boundaries and overlap;
- metadata and provenance preservation;
- enrichment, normalization, and deduplication;
- embedding/index/reranker versions;
- failure handling for unsupported or partially processed sources.

### Query and retrieval

Test:

- representative, ambiguous, multilingual, short, long, and negative queries;
- filters and caller authorization before evidence reaches the model;
- relevant-result recall and irrelevant-result precision at useful ranks;
- query rewriting or expansion effects;
- missing-source and conflicting-source behavior;
- result provenance and reproducibility.

Metric names such as precision, recall, or reciprocal rank can help diagnose
retrieval. Select them for the actual failure model; no one retrieval metric
establishes answer quality.

### Context and answer

Check:

- whether the selected evidence supports the requested claim;
- whether the model uses, ignores, distorts, or overgeneralizes it;
- completeness, relevance, and unsupported additions;
- handling of conflicts, insufficient evidence, and abstention;
- source citation/provenance accuracy;
- leakage across authorization or tenant boundaries;
- end-to-end user outcome.

A citation is useful only when it points to real evidence that supports the
claim and was authorized for the user. Citation presence alone does not prove
groundedness.

### RAG evaluation evidence

Preserve as applicable:

- corpus/index version and evaluation time;
- representative query set and source expectations;
- retrieval results and ranked-retrieval measures;
- answer-level rubrics or references;
- component and end-to-end results;
- error categories and slices;
- permission and negative-access tests;
- experiment configuration and material changes.

## AI Data Quality

Data can affect training, fine-tuning, retrieval, evaluation, monitoring, and
human feedback. For each material dataset or corpus, ask:

- provenance: where did it come from and can that be reconstructed?
- purpose: was it collected or created for a compatible use?
- rights: may it be used, transformed, retained, and shared in this context?
- sensitivity: does it contain personal, confidential, regulated, secret, or
  security-sensitive information?
- representativeness: which users, languages, conditions, and failure cases are
  present or absent?
- integrity: are there missing, duplicated, corrupted, poisoned, mislabeled, or
  inconsistent records?
- leakage/contamination: do evaluation cases or answers appear in training,
  examples, or retrieval context?
- freshness: what changed since collection or indexing?
- labels/feedback: who produced them, with which rubric and disagreement
  process?
- transformation: which parsing, cleaning, filtering, synthetic generation,
  enrichment, sampling, or aggregation changed the data?
- version: which data state produced the observed result?

Data quality is fitness for the intended use, not a universal property. A large
dataset can be unrepresentative; a clean dataset can be unauthorized; synthetic
data can preserve or amplify assumptions; user feedback can be sparse,
strategic, or biased.

Route detailed access/control/privacy questions to Cybersecurity and authorized
data/privacy owners. Route ingestion/deployment/runtime mechanics to DevSecOps
or Software Architecture as primary. Do not infer legal permission from
technical access.

## Evaluation Design

Evaluation should support a concrete decision: select, change, release, monitor,
diagnose, or retire.

### 1. Define the decision and behavior

State:

- intended use, user, and context;
- behavior to preserve or improve;
- unacceptable outcomes and failure cost;
- component versus end-to-end scope;
- quality, safety, latency, cost, reliability, and operational constraints that
  matter;
- uncertainty that cannot be measured reliably.

### 2. Build representative cases

Use a task-shaped set with:

- frequent normal cases;
- high-impact and boundary cases;
- known regressions and historical failures;
- relevant languages, formats, populations, and usage conditions;
- positive and negative cases;
- benign adversarial or misuse-resistance cases when authorized;
- enough metadata to analyze important slices;
- separation from prompt examples/training data when leakage would invalidate
  results.

Volume does not repair biased coverage. Preserve the origin and intended role
of each case.

### 3. Select criteria and measures

Combine evidence appropriate to the output:

- deterministic checks for schema, exact rules, executable behavior, or known
  invariants;
- reference-based comparisons where trusted answers exist;
- rubrics for relevance, completeness, groundedness, style, or policy fit;
- retrieval measures for ranked evidence;
- code/test/security evidence for engineering outputs;
- human expert judgment for ambiguous, novel, or high-impact questions;
- operational measures such as latency, error, availability, and cost when
  material.

Do not hide multiple failure dimensions inside one aggregate score. State the
accepted tradeoff and minimum evidence for the decision.

### 4. Validate graders

For model-based or heuristic graders:

- define a clear rubric and scale;
- compare with qualified human judgments or ground truth;
- inspect disagreement, bias, position/order effects, and unstable cases;
- verify performance on the errors the grader is expected to detect;
- preserve grader model/version/prompt/configuration;
- require human review where grader uncertainty or impact warrants it.

An automated judge increases coverage; it does not silently become the
definition of quality.

### 5. Compare and interpret

Use a relevant baseline or prior version. Analyze:

- improvement and regression by criterion and slice;
- practical significance, not only numerical difference;
- variance or repeated-run stability where nondeterminism matters;
- newly introduced failure modes;
- uncertainty, missing coverage, and conflicts between measures;
- whether a gain is worth cost, latency, complexity, or risk tradeoffs.

### 6. Continue after release

Re-evaluate on material changes and use proportionate production evidence such
as sampled outputs, verified user feedback, ground truth, incident/failure
signals, and drift. Protect sensitive data in logs and evaluation sets.

### Evaluation anti-patterns

- “looks good” or demo-only acceptance;
- generic public benchmark as the release case;
- test cases written only after seeing the candidate output;
- one aggregate score with hidden critical failures;
- an unrepresentative or contaminated golden set;
- a model judge with no human/ground-truth calibration;
- only average results with no important slices;
- changing prompt, model, data, and evaluator simultaneously without a
  reconstructable comparison;
- treating a pass as proof that unknown failures do not exist.

## Reliability, Monitoring, And Change

AI reliability is sustained behavior within defined operating conditions, not
the absence of one visible error.

### Identify failure modes

Examples include:

- provider/model unavailable, throttled, changed, or deprecated;
- input/context too large, malformed, truncated, or outside expected language
  or modality;
- retrieval empty, stale, unauthorized, conflicting, or irrelevant;
- output invalid, unsupported, inconsistent, unsafe, or unusable downstream;
- tool call duplicated, partial, timed out, or non-idempotent;
- state/memory stale, cross-user, corrupt, or impossible to correct;
- judge/monitor blind to the relevant failure;
- latency/cost/resource behavior outside operating constraints;
- user behavior or data distribution drifting beyond evaluation coverage.

### Connect signals to behavior

Choose proportionate evidence such as:

- task success or verified outcome;
- groundedness/answer-quality samples;
- safety or refusal outcomes;
- retrieval empty/low-quality rates;
- invalid or semantically rejected structured outputs;
- tool errors, retries, side effects, and trace failures;
- latency, availability, errors, tokens/resources, and cost;
- drift, language/user/segment changes, and new unsupported conditions;
- human override, correction, escalation, complaint, and feedback signals.

For each signal ask what failure it can and cannot detect, how it is sampled,
what sensitive data it contains, and what response is possible.

### Preserve change evidence

Version as applicable:

- model/provider and configuration;
- prompts/instructions/examples;
- code, dependencies, schemas, tools, and routing;
- corpus, parsing, chunks, embeddings, indexes, rerankers, and filters;
- data, labels, evaluation cases, rubrics, graders, and thresholds;
- monitoring definitions and dashboards.

Use controlled comparison and recovery proportionate to impact. Fallback can
mean a simpler method, prior version, human handling, restricted function,
refusal, degraded mode, or disablement. Detailed release, rollback, alerting,
and incident operation remains DevSecOps/existing governance territory.

## Human Oversight

Design oversight around a real decision or intervention.

Ask:

- What judgment or action remains human-owned?
- At what point can the human meaningfully change the outcome?
- Does the person see the input, source evidence, model output, uncertainty,
  relevant trace, and downstream effect needed to judge?
- Does the person have the competence and time for the case volume?
- Can they correct, reject, stop, retry, reroute, or escalate safely?
- Is automation bias, rubber-stamping, fatigue, or incentive conflict likely?
- Are disagreements and overrides captured without turning sensitive material
  into uncontrolled logs?
- Who remains accountable when the AI suggestion is accepted?

Use stronger human involvement when failure is consequential, evidence is
ambiguous, domain judgment is required, the system can cause external effects,
or evaluation coverage is weak. This guidance does not create a new approval
gate or assign authority; existing owners decide the review/approval shape.

## Safety And Misuse

This section is defensive context only.

### Defensive risk categories

Consider where relevant:

- conflicting or untrusted instructions, including retrieved/tool-supplied
  content;
- sensitive-information disclosure through prompts, outputs, logs, memory,
  retrieval, tools, or training/evaluation data;
- poisoned, manipulated, untrusted, or compromised data/model/dependency
  supply;
- unsafe use of model output by downstream code or people;
- excessive tool, identity, data, network, financial, or change authority;
- retrieval, embedding, index, cache, or tenant-isolation weaknesses;
- unsupported or misleading content used for consequential decisions;
- resource/cost exhaustion and uncontrolled loops/retries;
- model/provider behavior that does not match the assumed safety boundary.

Use NIST, OWASP, and MITRE sources as discovery vocabularies. A category match
is not a finding, and category completion is not assurance.

### Defensive engineering questions

- Which inputs and content are untrusted?
- What identities, data, tools, destinations, and side effects can the system
  reach?
- Are permissions narrower than the maximum possible request?
- Is authorization enforced outside model judgment at every relevant boundary?
- Are structured/model outputs validated before use?
- Can sensitive material be minimized, redacted, segmented, or kept out of the
  model path?
- What benign adverse cases test the actual threat assumptions?
- What monitoring can detect harmful or anomalous outcomes?
- What fallback or stop behavior limits impact?
- What residual risk and unknown coverage remain?

### Safe alternative pattern

If a request asks for jailbreak construction, prompt-injection exploitation,
exfiltration, evasion, malware/phishing, credential theft, unauthorized access,
or other operational abuse:

1. do not provide the procedure, payload, or optimization advice;
2. name the defensive risk category at a high level;
3. restate a benign assessment objective;
4. request authorized, non-destructive test conditions and observable evidence;
5. recommend proportionate trust separation, least privilege, validation,
   monitoring, and human controls;
6. route the security judgment to the Cybersecurity Domain Pack and authorized
   security/review owners.

## Integration, Tool, And Agentic Workflows

When a model can use tools, state, memory, routing, or handoffs, review the
observable behavior rather than relying on the product label `agent`.

### Boundaries to expose

- goal and stop conditions;
- identities and permissions used by each action;
- tool names, contracts, allowed arguments, and destinations;
- trusted versus untrusted tool outputs;
- state/memory scope, persistence, ownership, and correction;
- routing and handoff conditions;
- retry, timeout, duplication, idempotency, and partial-success behavior;
- external side effects and reversibility;
- human decision/intervention points;
- trace and audit evidence within privacy/security limits.

### Evaluate steps and outcomes

Include cases for:

- correct and incorrect tool choice;
- valid and invalid arguments;
- denied permissions and missing data;
- misleading, malformed, or incomplete tool output;
- handoff/routing errors;
- repeated, delayed, partial, or conflicting results;
- long sequences and error recovery;
- final user outcome and unintended side effects.

Trace evidence can locate a failure but does not prove every hidden action or
provider behavior. Route architectural decomposition to Software Architecture,
permissions/threat assurance to Cybersecurity, runtime/deployment to DevSecOps,
and implementation findings to Engineering Review.

## AI-Assisted Engineering

AI-generated code, tests, documentation, reviews, commands, and implementation
plans are proposals. Their fluency and apparent completeness are not evidence
of correctness.

### Before accepting a change

- Confirm the requirement, intended behavior, and architecture fit.
- Understand the generated change and its assumptions; do not merge code no
  responsible human can explain or maintain.
- Inspect the complete diff, not only the generated summary.
- Compile/build and run relevant deterministic, unit, integration, end-to-end,
  regression, and adverse tests in proportion to risk.
- Apply applicable formatting, linting, type, static, security, secret,
  dependency, license, and artifact checks.
- Verify generated APIs, packages, versions, commands, configuration keys, and
  documentation against authoritative/current sources.
- Look for deleted, skipped, weakened, or rewritten tests that conceal failure.
- Check error handling, concurrency, data loss, authorization, privacy,
  observability, performance, rollback, and compatibility where material.
- Inspect for secrets, sensitive data, copied/public-code similarity, licensing,
  and suspicious dependencies.
- Preserve independent review and existing branch/release protections for
  material changes.

### Constrain coding-agent authority

Use context-appropriate boundaries such as:

- least-privilege repository, branch, file, tool, credential, network, and
  environment access;
- isolated/sandboxed execution for untrusted changes;
- protected checks and separate authorization for consequential actions;
- human review before merge, deployment, publication, or destructive effects;
- visible logs/diffs and a recoverable change path.

These are engineering principles, not a new repository approval workflow.
Engineering Review owns findings and validation sufficiency. DevSecOps owns
delivery/runtime mechanics. Cybersecurity owns threats and control assurance.

## AI Engineering Evidence Expectations

Evidence should be proportional to the claim and consequence. A useful packet
may include:

- intended use, users, exclusions, and failure-cost assumptions;
- system boundary and material AI surfaces;
- model/provider/version/configuration record;
- prompt/instruction/version diff and representative fixtures;
- data/corpus provenance, rights/access, quality, sensitivity, and version;
- schema/tool contracts and semantic/downstream validation;
- evaluation objective, cases, criteria, graders, calibration, baselines,
  thresholds, slices, and results;
- component and end-to-end RAG evidence;
- trace/tool/handoff evidence for multi-step behavior;
- production quality, safety, reliability, latency/error, drift, and feedback
  signals;
- human-oversight boundary and available evidence/action;
- validation commands, environment, date, and limitations;
- residual risk, unknowns, stale-if triggers, and next validation.

Evidence strength examples:

| Claim | Weak evidence | Stronger evidence |
| --- | --- | --- |
| “Model B is better” | public leaderboard | task-shaped paired comparison across material slices and constraints |
| “Prompt change is safe” | several good outputs | versioned regression/adverse cases plus relevant system controls and residual risk |
| “Output is reliable” | schema conformance | schema, semantic, downstream, failure, and production evidence |
| “RAG is grounded” | citations are present | retrieval and answer evidence with real provenance and conflict/missing-source cases |
| “Judge is accurate” | judge score looks plausible | calibration against qualified human/ground truth with disagreement analysis |
| “Human review handles risk” | approval button exists | reviewer has evidence, competence, capacity, authority, and correction/stop path |
| “AI-generated code works” | generated explanation | understood diff plus tests, analysis/scans, dependency/provenance review, and independent review |

## Review Questions

Select only the questions material to the task.

### Activation and boundary

- Is AI Engineering material, or is AI merely mentioned?
- What is the primary context owner?
- Are adjacent Cybersecurity, DevSecOps, Software Architecture, Engineering
  Review, or Professional Analysis boundaries explicit?
- Has the pack created hidden policy, workflow, scoring, or approval authority?

### Intended behavior

- Are users, task, outcome, exclusions, failure cost, and affected parties
  visible?
- Is the system boundary wider than the model call where necessary?
- Which assumptions are observed, inferred, or unknown?

### Model, prompt, and interface

- Is model/provider choice supported by representative task evidence?
- Are version/configuration and volatile provider assumptions recorded?
- Are instruction authority and untrusted content separated?
- Are prompt changes versioned and compared against relevant cases?
- Does structured-output validation include semantic and downstream rules?

### RAG and data

- Are corpus authority, permissions, provenance, rights, freshness, and removal
  behavior known?
- Are ingestion/chunking/index versions and failures inspectable?
- Are retrieval and answer quality evaluated separately and end to end?
- Do citations actually support the claims and preserve real provenance?
- Are data representativeness, leakage, labels, sensitivity, and transformations
  addressed?

### Evaluation

- What decision does the evaluation support?
- Does the set represent normal, boundary, high-impact, and negative cases?
- Do criteria map to observable behavior and failure cost?
- Is the baseline meaningful?
- Are graders validated, versioned, and reviewed where necessary?
- Are important slices, disagreements, regressions, and uncertainty visible?
- Is a single score hiding a critical failure?

### Reliability and operation

- Which failures can be detected, and which remain invisible?
- Do monitoring signals map to user/system impact and a possible response?
- Are logs/traces minimized and protected as potentially sensitive data?
- Are fallback, rollback, refusal, degraded mode, or disablement considered where
  proportionate?
- Will material model, prompt, data, retrieval, tool, or evaluator changes
  trigger re-evaluation?

### Human oversight

- What decision can the human actually change?
- Does the human have sufficient evidence, competence, time, and authority?
- Can the person correct or stop the system safely?
- Is automation bias or rubber-stamping likely?
- Does accountability remain explicit?

### Safety and tools

- What is untrusted, sensitive, externally controlled, or capable of side
  effects?
- Are tool/data/identity permissions least-privilege and enforced outside model
  judgment?
- Are output validation, adverse testing, monitoring, and residual risk
  proportionate?
- Has any unsafe operational procedure entered the artifact?
- Is a taxonomy/checklist being mistaken for a verdict?

### AI-assisted engineering

- Does the change satisfy the real requirement and architecture?
- Has a responsible human understood the full diff?
- Were relevant tests and static/security/dependency/license checks run?
- Were hallucinated APIs/packages, weakened tests, secrets, and suspicious
  changes examined?
- Is agent authority constrained and the change path recoverable?
- Has independent Engineering Review remained intact?

## Common Mistakes

- Treating the model as the whole system.
- Choosing a model from a leaderboard without task-shaped evidence.
- Optimizing a prompt before defining success and failure.
- Treating prompt wording as an access-control boundary.
- Treating schema-valid output as correct or safe.
- Treating a citation as proof of groundedness.
- Evaluating only the final answer and hiding retrieval/tool failures.
- Using a large but unrepresentative or contaminated evaluation set.
- Letting an uncalibrated model judge define quality.
- Collapsing quality, safety, latency, cost, and reliability into one score.
- Reporting averages without important slices or error categories.
- Calling monitoring complete because logs exist.
- Storing sensitive prompts, corpora, traces, or eval cases without controls.
- Using “human-in-the-loop” as a safety claim without meaningful authority.
- Giving a tool-using model broader permissions than the task requires.
- Assuming refusal, a filter, or a taxonomy eliminates residual risk.
- Accepting AI-generated code from its explanation instead of verification.
- Failing to verify generated packages, APIs, commands, licenses, or versions.
- Allowing AI review to replace independent human/authorized review.
- Encoding current preview/product behavior as stable canon.
- Activating this pack when Cybersecurity or DevSecOps is clearly primary.
- Turning these questions into a mandatory workflow or checklist regime.

## Source Register

Last checked for every source in this release: 2026-07-10. `Version / date`
means the inspected publication version when one is declared; `living` means
the page can change without a new edition. The IDs match the task evidence
register exactly.

### Repository canon

| ID | Source | Source class | Authority | Version / date | Relevance | Confidence limit |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | `kb/domain_knowledge_pack_standard.md` | Repository canon | Canonical owner | Current repository version | Pack identity, structure, evidence, boundary, review, update, retirement | Recheck on repository change. |
| R02 | `kb/engineering_review.md` | Repository canon | Canonical owner | Current repository version | Implementation/change-safety ownership | Does not supply AI product facts. |
| R03 | `kb/professional_analysis.md` | Repository canon | Canonical owner | Current repository version | Decision-ready analysis ownership | Does not decide AI technical fitness. |
| R04 | `kb/software_architecture_domain_pack.md` | Repository domain pack | Canonical context owner | Current repository version | Architecture boundary and tradeoff context | Pack status and source freshness still apply. |
| R05 | `kb/devsecops_domain_pack.md` | Repository domain pack | Canonical context owner | Current repository version | Delivery, runtime, supply-chain boundary | Does not establish product behavior. |
| R06 | `kb/cybersecurity_domain_pack.md` | Repository domain pack | Canonical context owner | Current repository version | Threat, control, assurance, and misuse boundary | Security conclusions remain task-specific. |
| R07 | `kb/editorial_evidence_framework.md` | Repository canon | Canonical owner | Current repository version | Evidence classes, confidence, uncertainty | Does not replace domain evidence. |

### Provider and platform engineering guidance

| ID | Source | Source class | Authority | Version / date | Relevance | Confidence limit |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Official provider documentation | OpenAI, first party | Living | Task-specific, continuous evaluation and human calibration | Product terminology can change; generalize only corroborated principles. |
| S02 | [OpenAI — Prompting](https://developers.openai.com/api/docs/guides/prompting) | Official provider documentation | OpenAI, first party | Living | Prompt/instruction versioning, examples, tests, evals | Product prompt objects and deprecated features are not durable canon. |
| S03 | [OpenAI — Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Official provider documentation | OpenAI, first party | Living | Schema adherence versus semantic correctness | Supported schemas and API behavior are version-specific. |
| S04 | [OpenAI — Retrieval](https://developers.openai.com/api/docs/guides/retrieval) | Official provider documentation | OpenAI, first party | Living | Semantic retrieval, filters, scores, chunk/index concepts | Hosted mechanics are examples, not universal requirements. |
| S05 | [OpenAI — File search](https://developers.openai.com/api/docs/guides/tools-file-search) | Official provider documentation | OpenAI, first party | Living | Example of semantic plus keyword retrieval | Hosted-tool behavior is volatile. |
| S06 | [OpenAI — Agent evals](https://developers.openai.com/api/docs/guides/agent-evals) | Official provider documentation | OpenAI, first party | Living | Trace-level tool, routing, handoff, guardrail evaluation | Agent/eval platform behavior is volatile. |
| S07 | [OpenAI — Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) | Official provider documentation | OpenAI, first party | Living | Defensive testing, oversight, input/output constraints | Product safeguards are not universal controls. |
| S08 | [Anthropic — Develop tests and evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Official provider documentation | Anthropic, first party | Living | Measurable criteria, representative tests, graders, rubrics | Provider tooling and examples are volatile. |
| S09 | [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Official provider documentation | Anthropic, first party | Living | Empirical criteria and tests before prompt optimization | Does not prove a specific prompt is fit. |
| S10 | [Anthropic — Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) | Official provider safety guidance | Anthropic, first party | Living | Defensive trust separation, least privilege, screening, monitoring | Used only for defensive categories; provider controls are contextual. |
| S11 | [Google — Operational excellence for AI/ML](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence) | Official cloud architecture guidance | Google Cloud, first party | Page noted last review 2025-04-28 | Versioning, evaluation, monitoring, rollback, drift | Platform examples are non-universal. |
| S12 | [Google — Deploy and operate generative AI applications](https://docs.cloud.google.com/architecture/deploy-operate-generative-ai-applications) | Official cloud architecture guidance | Google Cloud, first party | Living | Continuous evaluation, feedback, drift, alerting | Platform implementation details are contextual. |
| S13 | [Google — Production ML systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems) | Official engineering education | Google, first party | Living curriculum | Data, serving, monitoring, infrastructure beyond model code | Educational overview, not a complete standard. |
| S14 | [Google — Data quality](https://developers.google.com/machine-learning/guides/data-traps/quality) | Official engineering guidance | Google, first party | Living | Data error, bias, and sampling risks | Not a complete data governance or legal standard. |
| S15 | [Google — Evaluate a judge model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluate-judge-model) | Official provider documentation | Google Cloud, first party | Living | Judge comparison with human ratings or ground truth | Product behavior and evaluator implementations are volatile. |
| S16 | [Microsoft — RAG design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) | Official cloud architecture guidance | Microsoft, first party | Living | Representative RAG tests, components, end-to-end evaluation | Product patterns are contextual. |
| S17 | [Microsoft — RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) | Official provider documentation | Microsoft, first party | Living | Retrieval-process versus answer/system evaluation | Named evaluators and tooling are product-specific. |
| S18 | [Microsoft — RAG information retrieval](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) | Official cloud architecture guidance | Microsoft, first party | Living | Ranked-retrieval metrics and positive/negative tests | Metric choice remains task-specific. |
| S19 | [Microsoft — Secure multitenant RAG](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag) | Official cloud security architecture guidance | Microsoft, first party | Living | Tenant/user authorization for grounding data | Architecture pattern is contextual; not proof of security. |
| S20 | [AWS Bedrock — Evaluate model performance](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) | Official provider documentation | AWS, first party | Living | Model/RAG evaluation, custom data, automated/model/human methods | Service behavior is volatile. |
| S21 | [AWS Generative AI Lens — Monitoring](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf01-bp02.html) | Official cloud architecture guidance | AWS, first party | Living lens | Application metrics, telemetry, golden data | Lens guidance is contextual, not a universal gate. |
| S22 | [AWS Generative AI Lens — Periodic evaluation](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01.html) | Official cloud architecture guidance | AWS, first party | Living lens | Feedback, ground truth, sampled evaluation | Exact cadence and methods are use-case-specific. |
| S23 | [AWS Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html) | Official cloud architecture guidance | AWS, first party | Published 2026-06-10 | Tool, memory, multi-call, and handoff failure surfaces | New, fast-evolving guidance; recheck before specific use. |

### Standards, government, and public security resources

| ID | Source | Source class | Authority | Version / date | Relevance | Confidence limit |
| --- | --- | --- | --- | --- | --- | --- |
| S24 | [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) | Primary government framework publication | NIST | Published 2023-01-26 | Voluntary use-case-agnostic AI risk context | NIST says revision is underway; stale on replacement. |
| S25 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Primary government guidance | NIST | Living AI RMF resource | Govern/Map/Measure/Manage, context, impact, limits, metric fitness | Stale when revised AI RMF is published. |
| S26 | [NIST AI 600-1 — Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Primary government profile | NIST | Published 2024-07-26 | Cross-sector GenAI risk companion | Recheck after AI RMF/profile revision. |
| S27 | [NIST SP 800-218A](https://www.nist.gov/publications/secure-software-development-practices-generative-ai-and-dual-use-foundation-models-ssdf) | Primary government secure-development publication | NIST | Published 2024-07 | AI model/system producer and acquirer secure-development context | Must be used with applicable SSDF context; stale on revision. |
| S28 | [NIST AI 100-2e2023](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) | Primary government taxonomy | NIST | Published 2024-01 | Defensive adversarial-ML terminology | NIST continues updates; recheck current edition for security work. |
| S29 | [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) | Official community security knowledge base | OWASP Foundation | 2025 edition | LLM-application risk-category discovery | Awareness taxonomy, not proof or complete control baseline. |
| S30 | [MITRE ATLAS](https://atlas.mitre.org/) | Official living security knowledge base | MITRE | Living | AI adversary tactics/techniques and mitigation discovery | Taxonomy changes; not proof of system vulnerability or safety. |
| S31 | [ISO — ISO/IEC 5259-1:2024](https://www.iso.org/standard/81088.html) | Official public standards catalog | ISO | 2024 edition | Public scope/terminology for analytics/ML data quality | Only public abstract inspected; no inaccessible clause is claimed. |

### AI-assisted engineering

| ID | Source | Source class | Authority | Version / date | Relevance | Confidence limit |
| --- | --- | --- | --- | --- | --- | --- |
| S32 | [GitHub — Review AI-generated code](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code) | Official platform engineering guidance | GitHub, first party | Living | Human oversight, tests/static analysis, intent, dependencies, licenses, AI-specific errors | Product examples are contextual; general principles align with Engineering Review. |
| S33 | [GitHub — Copilot best practices](https://docs.github.com/en/copilot/get-started/best-practices) | Official provider documentation | GitHub, first party | Living | Understand, review, test, lint, and scan suggestions | Provider-specific guidance, not universal product proof. |
| S34 | [GitHub — Cloud agent risks and mitigations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations) | Official provider security guidance | GitHub, first party | Living | Constrained branch, credential, tool, check, and merge authority example | Implementation-specific controls are illustrative. |

The full task evidence register preserves the same IDs plus research selection
policy, access/freshness notes, exclusions, facts, claims, and contradictions at
`tasks/TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE/sources.md`.

## Confidence Notes

### High confidence

- AI system quality depends on the surrounding data, interfaces, evaluation,
  runtime, feedback, and human boundary, not only the model.
- Task-specific representative evaluation, comparison, and continuous evidence
  are stronger than demos or generic benchmarks.
- Retrieval and answer quality are separable.
- Schema conformance does not guarantee semantic correctness.
- Automated/model graders require fit validation or human/ground-truth
  calibration.
- Tool authority should be constrained and enforced outside model judgment.
- AI-generated engineering work requires ordinary verification and accountable
  human review.
- Domain packs cannot create workflow, capability, role, gate, or approval
  authority.

### Medium or context-dependent confidence

- Exact metrics, thresholds, sampling, observability, fallback, and oversight
  designs depend on the use case and impact.
- `Agent`, `groundedness`, `hallucination`, `guardrail`, and related terms are
  used inconsistently across providers and teams.
- Public provider and cloud guidance is authoritative for its own products but
  becomes general guidance only where multiple sources and engineering logic
  align.

### Task-time verification required

- model names, versions, context/tool behavior, limits, pricing, availability,
  latency, benchmark claims, safety behavior, and deprecation;
- provider data retention, training use, regional processing, privacy,
  contractual, and account-specific behavior;
- current OWASP, MITRE, NIST, ISO, legal, regulatory, and industry guidance;
- exact API schemas, product features, preview status, and evaluation tooling;
- dataset rights, provenance, sensitivity, and permission;
- any claim of security, compliance, fairness, safety, or production fitness.

## Update Rules

Review this pack when:

- Domain Knowledge Pack Standard or an adjacent canonical owner changes;
- NIST publishes the revised AI RMF or updates GenAI/secure-AI guidance;
- OWASP or MITRE publishes a materially revised AI/LLM taxonomy;
- major providers materially change prompt, retrieval, structured-output,
  evaluation, agent/tool, data-use, or safety guidance;
- repeated tasks expose missing AI system surfaces or unclear routing;
- review finds a claim encoded too universally or a source no longer supports
  it;
- terms such as agent, groundedness, or guardrail become misleading;
- the pack is repeatedly over-activated or mistaken for a workflow/checklist.

For each update:

1. verify the current canonical owner and pack boundary;
2. refresh primary sources and record date/version;
3. distinguish durable principle from product implementation;
4. update claims, confidence, examples, and stale triggers;
5. check adjacent packs for duplication or conflict;
6. run representative activation/non-activation scenarios;
7. use independent review before acceptance.

Do not silently replace source-backed claims with model memory or current
marketing language.

## Retirement Rules

Retire or supersede the pack when:

- an accepted canonical owner replaces it;
- the pack becomes structurally incompatible with the Domain Knowledge Pack
  Standard;
- the content fragments into stale provider notes that cannot be maintained;
- its useful material is fully absorbed by clearer existing owners;
- it repeatedly creates architecture ambiguity or unsafe guidance that cannot
  be repaired;
- evidence cannot be refreshed enough to support future use.

Retirement should record:

- replacement or reason no replacement exists;
- sections and claims affected;
- source-freshness state;
- references that must be updated;
- a clear instruction not to activate the retired pack.

Retirement is a reviewed canon change, not an ad hoc deletion.

## Relation To Engineering Review

AI Engineering supplies domain questions and expected evidence for
AI-specific changes. Engineering Review remains the owner of implementation and
change-safety challenge, finding severity, validation sufficiency, and residual
implementation risk.

Examples:

- this pack asks how a prompt, retriever, tool, or grader can fail;
- Engineering Review determines whether the changed implementation handles
  those failures and whether evidence is sufficient;
- this pack identifies AI-generated-code risks;
- Engineering Review records actionable findings inside the existing review
  gate.

The pack cannot approve code, waive tests, resolve findings, or replace
independent review.

## Relation To Cybersecurity Domain Pack

AI Engineering identifies AI-specific assets, trust inputs, tool/identity
surfaces, sensitive-data paths, misuse categories, and evidence questions.
Cybersecurity owns threat analysis, abuse cases, access/control reasoning,
security assurance, exploitability, and residual security risk.

Use Cybersecurity as primary when the question is mainly:

- prompt injection or instruction-confusion security risk;
- unauthorized data/tool/tenant access;
- sensitive-information disclosure;
- poisoning, malicious dependency, or adversarial manipulation;
- excessive privilege/agency or unsafe side effects;
- security control design/effectiveness;
- a claim that a system is secure or acceptably exposed.

Keep all joint work defensive and authorized. This pack does not contain
offensive procedures.

## Relation To DevSecOps Domain Pack

AI Engineering names AI artifacts and runtime signals that may require delivery
and operational treatment: model/provider versions, prompts, datasets, corpora,
indexes, embeddings, evaluation assets, tool configurations, traces, and
quality/safety signals.

DevSecOps owns the deeper questions about:

- CI/CD and release automation;
- secrets and environment configuration;
- dependency, model, dataset, container, and artifact provenance;
- deployment, rollback, runtime permissions, and operational boundaries;
- monitoring implementation, alerting, and operational response;
- supply-chain and secure-delivery evidence.

This pack does not define an AI release pipeline or mandatory evaluation gate.

## Relation To Software Architecture Domain Pack

AI Engineering supplies AI-specific surfaces, failure modes, evidence
expectations, and volatile constraints. Software Architecture owns system
decomposition, component and trust boundaries, coupling, style/pattern choice,
quality-attribute scenarios, tradeoffs, and architecture decisions.

Use both when model/provider abstraction, RAG topology, tool integration,
state/memory, fallback, human boundary, observability, or provider dependency is
architecturally significant. The AI Engineering Pack does not prescribe a
reference architecture.

## Relation To Professional Analysis

AI Engineering supplies source-backed domain interpretation: what was measured,
which tradeoffs and failure modes matter, where evidence is weak, and what must
be refreshed. Professional Analysis owns the decision-ready product shape:
problem framing, synthesis, options, recommendation, implications, risks, and
uncertainty.

The pack cannot decide business priorities or recommend a model/provider from
domain evidence alone. A recommendation should connect task evidence to the
actual decision, constraints, and consequences.

## Relation To Existing Canon

- `AGENTS.md` remains the governance and authority owner.
- `kb/domain_knowledge_pack_standard.md` owns pack rules.
- `kb/editorial_evidence_framework.md` owns evidence/confidence discipline.
- `kb/analytical_reasoning.md` owns reusable reasoning moves.
- `kb/architecture_review.md` owns architecture-specific challenge.
- `kb/engineering_review.md` owns implementation/change-safety challenge.
- `kb/professional_analysis.md` owns decision-ready analytical product quality.
- `kb/professional_communication.md` owns reader transfer without losing
  evidence, caveats, or actionability.
- `kb/software_architecture_domain_pack.md`,
  `kb/cybersecurity_domain_pack.md`, and `kb/devsecops_domain_pack.md` own their
  adjacent domain context.
- selected role specs and pipelines still own stage behavior and artifact
  responsibility.

If this pack conflicts with a canonical owner, the canonical owner wins and the
conflict should be escalated through Chief Editor rather than resolved by
inventing local policy.

## Safety Boundaries

This pack supports defensive engineering, evaluation, review, and risk
reduction. It must not be used to provide:

- jailbreak or prompt-injection payloads and exploitation steps;
- data-exfiltration, credential-theft, unauthorized-access, or privilege-abuse
  instructions;
- evasion or safeguard-bypass optimization;
- malware, phishing, persistence, destructive, or stealth procedures;
- operational targeting of people, systems, tenants, providers, or models;
- fabricated claims of security, safety, compliance, approval, or authorization.

For a suspicious or dual-use request, keep only the benign defensive objective,
use non-destructive evidence, remove operational attack detail, state the
authorization boundary, and activate the Cybersecurity Domain Pack as primary.
