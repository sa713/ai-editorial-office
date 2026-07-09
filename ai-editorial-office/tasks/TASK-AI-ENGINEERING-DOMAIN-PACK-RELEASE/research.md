# Research Synthesis

## Research question

What durable, source-backed AI engineering context will improve analysis,
writing, design discussion, implementation review, and release reasoning in AI
Editorial Office without creating new architecture, policy, workflow, or unsafe
operational guidance?

## Executive finding

Research supports one bounded AI Engineering Domain Knowledge Pack. The common
engineering object is not a prompt or model in isolation but an AI-enabled
system composed of users, instructions, model/provider behavior, data,
retrieval, tools, interfaces, validation, runtime, monitoring, feedback, and
human accountability. Authoritative sources converge on task-shaped evaluation,
data and provenance quality, continuous monitoring, meaningful oversight,
constrained authority, and change evidence. They diverge mainly in product
terminology and tooling.

The durable pack should therefore:

- begin with intended user, task, impact, failure cost, and observable success;
- separate model behavior from system behavior;
- treat prompt/instruction, RAG, structured output, tools/agents, data, evals,
  monitoring, and AI-assisted coding as connected but separately testable
  surfaces;
- distinguish retrieval quality from answer quality;
- require calibrated evidence rather than benchmark, demo, citation, schema, or
  checklist theater;
- keep human responsibility and system authority explicit;
- route threat/control questions to Cybersecurity, delivery/runtime/supply-chain
  questions to DevSecOps, design tradeoffs to Software Architecture,
  implementation findings to Engineering Review, and decision-product shaping
  to Professional Analysis;
- carry current provider details only as task-time evidence, never stable canon.

## Landscape synthesis by system surface

### 1. Problem framing and system boundary

NIST AI RMF and provider engineering guides consistently make context primary:
intended use, users, impacts, limitations, success criteria, and operational
conditions determine what should be measured and controlled. This rejects
model-only reasoning. The pack should ask what decision or action the system
enables, who can be harmed by error, what is outside scope, and where humans or
external systems change the outcome.

### 2. Model and provider selection

No inspected source supports choosing a model by a general leaderboard alone.
The defensible pattern is comparative task evidence across material quality,
safety, latency, cost, context, integration, operational, and governance
constraints. Public benchmarks can be discovery evidence, not acceptance
evidence. Version and provider behavior are volatile, so exact claims need
task-time refresh.

### 3. Prompt and instruction engineering

OpenAI and Anthropic both connect prompt work to explicit success criteria and
empirical tests. OpenAI further treats prompts as versionable application
artifacts with fixtures, evals, comparison, and rollback. Safety guidance adds
an authority distinction: trusted instructions should be separated from user,
retrieved, or tool-supplied content. The pack should not promise that phrasing
alone provides security; it should frame prompts as one layer in a system.

### 4. Structured outputs and interfaces

Structured-output guarantees can reduce syntactic/interface ambiguity, but the
official source explicitly warns that schema-conforming values can still be
wrong. Therefore the pack should distinguish parsing, schema validation,
semantic validation, domain/business-rule validation, and downstream side
effects. Tool/function boundaries and user-response schemas should be chosen by
integration purpose, not because both are JSON-shaped.

### 5. RAG and internal knowledge

OpenAI and Microsoft sources support a pipeline view: corpus selection,
ingestion, chunking, representation, query processing, filtering/ranking,
context construction, response behavior, and provenance. Microsoft explicitly
separates retrieval-process quality from system-level answer quality. Secure
multitenant guidance adds a non-negotiable boundary: grounding retrieval must
not bypass the caller's authorization. Metrics depend on the failure model;
ranked retrieval and groundedness/completeness are examples, not mandatory
universal scores.

### 6. Data quality

Google production/data guidance and the public ISO abstract establish data
quality as an engineering concern rather than an upstream assumption. Useful
questions cover provenance, representativeness, missingness, duplication,
label quality, contamination, freshness, rights, sensitivity, and
training/serving differences. The pack may prompt these questions but cannot
make privacy, legal, or compliance determinations without current task-specific
sources and appropriate authority.

### 7. Evaluation

Across OpenAI, Anthropic, Google, Microsoft, and AWS, the strongest convergence
is:

- define objective and criteria before optimization;
- build representative cases, including important edges;
- select task-specific measures and qualitative rubrics;
- compare against a baseline or prior version;
- use automated, model-based, and human grading according to the question;
- validate graders against human or ground-truth judgments;
- keep evaluation continuous through changes and production sampling.

The sources also expose common anti-patterns: generic metrics, biased or
unrepresentative sets, vibe-based judgment, uncalibrated judges, and ignoring
human feedback. The pack should not prescribe one metric suite or release
threshold.

### 8. Reliability, monitoring, and change

Google and AWS guidance treats production quality as an application/system
property. Relevant observability can include task outcomes, safety events,
latency, errors, resource/cost behavior, drift, traces, and feedback. Signals
must map to failure modes and response options; telemetry accumulation is not
reliability evidence by itself. Versioning prompts, code, model/provider
configuration, data, and evaluation assets helps reconstruct changes and
supports rollback. Exact alerting or incident mechanics belong to DevSecOps and
existing operational governance.

### 9. Human oversight

OpenAI and NIST sources support proportional human oversight, especially for
high-impact or code-generating uses. The synthesis adds a practical test:
oversight is meaningful only when the reviewer has suitable evidence, context,
competence, time, authority, and a correction or stop path. This is a design
question, not a new repository approval gate. The pack must not imply that a
nominal human-in-the-loop makes a system safe.

### 10. Safety, misuse, and agent/tool boundaries

NIST, OWASP, MITRE, Anthropic, OpenAI, and current provider agent guidance
support a layered defensive view. Relevant categories include instruction
confusion, sensitive-data exposure, poisoned or untrusted inputs, unsafe output
handling, excessive agency, retrieval weaknesses, misinformation, supply-chain
risk, and resource abuse. Mitigation themes include trust separation, least
privilege, narrow permissions, output validation, adversarial evaluation,
monitoring, and controlled human authority.

The pack must stay category-level and defensive. It must not explain how to
construct jailbreaks, evade controls, exfiltrate data, gain unauthorized access,
or operationalize abuse. Taxonomies prompt analysis; they do not produce a
safety verdict.

### 11. Integration and AI workflows

Tool-using and multi-step systems add decision surfaces beyond the final text:
tool choice, arguments, identity/authorization, state, memory, routing,
handoffs, retry behavior, and external side effects. Trace-level evaluation can
help locate failures. Detailed architecture belongs to Software Architecture;
permissions and threat assurance to Cybersecurity; deployment and runtime
controls to DevSecOps; implementation findings to Engineering Review.

### 12. AI-assisted engineering

GitHub's official guidance supports a simple durable boundary: generated code
is a proposal, not evidence of correctness. Review should establish intent and
architecture fit, understand the change, compile/run tests, apply suitable
linting/static/security/dependency checks, inspect generated APIs/packages,
licenses, secrets, skipped tests, and suspicious changes, and preserve human
accountability. Agent authority can be constrained with narrow repository,
branch, credential, tool, and merge permissions. Specific GitHub controls are
examples; the reusable principle is constrained authority plus ordinary
engineering verification.

## Source convergence and divergence

| Topic | Convergence | Divergence / editorial treatment |
| --- | --- | --- |
| Evaluation | Task-specific, representative, repeatable, continuous | Metric names and product tooling differ; pack supplies selection questions, not one scorecard. |
| RAG | Evaluate retrieval and answer behavior; preserve provenance | Pipeline products and metric vocabularies differ; use conceptual stages. |
| Prompting | Start from criteria, test changes, provide clear context | Instruction APIs and versioning features differ; retain artifact/change principle only. |
| Monitoring | Observe quality, safety, latency/errors, feedback, drift | Available telemetry differs; require failure-to-signal reasoning. |
| Human oversight | Proportion to impact and retain human judgment | Exact approval mechanisms differ; pack creates no gate. |
| Safety | Layered defenses and continuous testing | Taxonomies organize risks differently; use complementary category prompts. |
| Agents | Tools/state/handoffs add failure surfaces | Agent definitions and products evolve quickly; avoid fixed taxonomy. |
| AI coding | Understand, review, test, scan, constrain | Product controls differ; preserve normal engineering accountability. |

## Architecture implications

1. A single pack is coherent because the surfaces share one evidence logic:
   specify behavior, identify failure modes, validate components and end to
   end, observe production, and preserve human/accountability boundaries.
2. The pack must be layered and reference-oriented, not a mandatory checklist.
3. Relations to adjacent canonical owners must be explicit at both the main
   boundary and the relevant subject sections.
4. Source notes must separate durable principles from current product examples.
5. Safety content must use safe alternative patterns: describe the defensive
   question, evidence to request, and owner to involve, without abuse detail.

## Gaps and residual uncertainty

- There is no universal, stable metric set for AI system quality. The pack must
  guide selection and evidence interpretation rather than declare one.
- “Agent” remains an unstable product term. The pack should describe observable
  tool/state/handoff behavior instead of enforcing a taxonomy.
- Provider privacy, retention, training use, regional processing, and contract
  terms change and are account-specific. Every sensitive-data task requires
  current primary-source verification.
- Public ISO access was limited to the standard abstract. It supports the
  existence/scope of data-quality terminology, not detailed requirements.
- OWASP and MITRE are living taxonomies. Security-sensitive claims require
  current edition checks and Cybersecurity context.
- Evaluation can reveal risk but cannot prove absence of unknown failure.

## Research sufficiency judgment

Status: `sufficient for architecture synthesis and pack writing`.

Basis:

- all user-required subject areas have authoritative support;
- the material claims are traceable through `facts.md` and
  `claims_table.md`;
- source disagreements can be reconciled without hiding uncertainty;
- the architecture and safety boundaries are clear;
- seven required validation scenarios can be evaluated using the resulting
  activation, surface, evidence, and escalation rules.

Stop conditions for downstream work remain:

- do not write an unsupported universal claim;
- do not make product-specific behavior durable canon;
- do not convert context into a role, gate, workflow, or approval authority;
- do not include actionable abuse procedures;
- route unresolved security, delivery, architecture, implementation, legal, or
  compliance conclusions to their proper owners.
