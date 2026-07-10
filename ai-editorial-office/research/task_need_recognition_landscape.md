# Task Need Recognition Landscape

Date: 2026-07-10

Release: `S5.R4 - Task Need Recognition`

## Executive finding

Authoritative practice does not support a single keyword classifier for the
work AI Editorial Office performs. Strong intake and triage instead combine
several kinds of evidence: intended outcome, user/stakeholder context,
deliverable, current versus expected state, constraints, impact, uncertainty,
required expertise, affected surface, and evidence gaps. Classification,
priority, effort, and impact are kept distinct. AI-assisted classification is
most reliable when it can expose unsupported or out-of-scope cases and when a
human reviews the recommendation.

For S5.R4, the defensible transfer is a compact advisory recognition view, not
an automatic router. The view should make observed request signals,
recommendations, negative evidence, ambiguity, and uncertainty inspectable so
Chief Editor can make the existing routing, activation, depth, and preflight
decisions.

## Research questions

- What professional intake signals are durable across requirements, issue,
  architecture, incident, consulting/discovery, and AI-routing contexts?
- Which signals help distinguish task type, capability need, Domain Pack need,
  research/review depth, risk, significance, and decomposition?
- Where does automation fail or lose context?
- What must remain a human/Chief Editor decision?

## Method and source boundary

The research used 15 external source groups: NASA systems engineering, SEI
architecture intake, government service discovery/problem framing, GitHub
issue intake and AI triage, NIST and Google incident/risk practice, two primary
intent/model-routing studies, Microsoft human-AI interaction research, and
NIST AI RMF human-oversight guidance. Repository findings were checked against
current canonical owners, accepted Stage 3 capabilities, all accepted Stage 4
Domain Packs, and accepted Stage 5 releases.

The detailed source register, limitations, and repository evidence are in
`tasks/TASK-TASK-NEED-RECOGNITION-RELEASE/sources.md`.

## Practice landscape

### Stakeholder and requirements intake

NASA treats stakeholder expectations as the foundation for later engineering:
identify stakeholders, intended use, desired end state, constraints, operating
context, assumptions, and measurable expectations. Its requirements guidance
also warns against designing from received requirements alone; iteration is
needed to avoid building the wrong interpretation.

Transferable signals:

- intended user/stakeholder and affected party;
- desired outcome or end state;
- deliverable and acceptance evidence;
- explicit constraints and external interfaces;
- assumptions, missing information, and conflicting interpretations;
- whether a large request has separable lower-level requirements.

Non-transferable mechanism: formal “shall” requirements for every editorial
request. Ordinary tasks need proportional recognition, not systems-engineering
ceremony.

### Issue triage and engineering intake

GitHub issue forms separate issue type from actual behavior, expected behavior,
reproduction, environment, and context. Organization issue fields also keep
priority and effort separate from type. GitHub's AI intake feature is described
as suggesting whether an issue is actionable or needs more information, after
which a person reviews the suggestions and takes action.

Transferable signals:

- work-item/task type is not the same as priority, effort, or impact;
- observable changed or failed surface indicates engineering significance;
- missing reproduction, environment, or expected state increases uncertainty;
- actionability and needs-more-information are advisory states;
- structured evidence improves routing but does not prove the route.

Non-transferable mechanism: automatic labels, assignees, types, and project
routing. S5.R4 forbids automatic activation or routing.

### Consulting and service problem framing

GOV.UK discovery guidance says to understand the problem before committing to a
solution, challenge solution-shaped briefs, name what is outside scope, learn
about users/context/constraints, and recognize when the apparent task is part
of a wider journey spanning teams. Digital.gov adds a compact who/what/why/goal
frame and treats narrower reframing as a way to preserve research resources.

Transferable signals:

- distinguish requested output from underlying need;
- detect solution-first framing and hidden assumptions;
- identify wider journeys, multiple owners, and likely decomposition;
- recommend research from novelty, uncertainty, and decision value;
- define explicit exclusions;
- protect simple work by narrowing research to what can change the decision.

Non-transferable mechanism: a multi-week discovery phase. Recognition recommends
depth; Chief Editor chooses the existing task route.

### Architecture decision intake

SEI QAW identifies architecture-driving quality attributes through early
stakeholder engagement and scenarios before an architecture exists. The
accepted Architecture Review and Software Architecture Domain Pack add current
repository boundaries: architecture significance comes from drivers,
cross-owner/boundary effects, quality attributes, tradeoffs, risk, and
hard-to-reverse consequences.

Transferable signals:

- named architecture/design commitment;
- cross-owner, interface, data, dependency, lifecycle, role, or canon boundary;
- material quality-attribute effect;
- hard-to-reverse or future-constraining consequence;
- credible alternative/tradeoff requirement;
- need for Software Architecture Domain Pack context.

Negative evidence matters: the word “architecture” in a copyedit or a local
implementation detail is not architectural significance.

### Incident classification

NIST frames incident response inside risk management and impact reduction.
Google SRE makes severity product-specific and tied to user-visible impact and
critical objectives; it explicitly warns that applying one method everywhere
can create unjustified instrumentation and maintenance cost. Google also uses
automated impact analysis and suggested mitigations as support for people with
clear incident roles.

Transferable signals:

- impact, exposure, reversibility, affected users/systems, urgency, and
  recoverability shape risk/review depth;
- classification can change as evidence changes;
- domain context matters to severity;
- a high-risk keyword without a material affected asset or consequence should
  not force maximum depth;
- automation can surface facts and suggestions while humans retain control.

Non-transferable mechanism: external incident-severity ladders. AI Editorial
Office keeps its own risk modes and Chief Editor decision.

### Intent recognition

The CLINC/OOS study demonstrates a durable failure pattern: classifiers can do
well on known intent classes while struggling to detect plausible out-of-scope
queries. Rich editorial requests also differ from short, single-intent
utterances: they can contain multiple deliverables, domains, and significance
surfaces.

Transferable signals:

- never force every request into one known type;
- preserve `uncertain`, `mixed`, and unsupported recognition;
- distinguish dominant task from secondary material needs;
- treat out-of-scope/domain gaps as a research, constrain, or escalation
  signal rather than a guessed label;
- validate negative and near-neighbor cases, not only obvious positive cases.

Non-transferable mechanism: a fixed exhaustive intent taxonomy and classifier
confidence percentage.

### AI task/model routing

RouteLLM is explicitly designed to select a stronger or weaker model during
inference to optimize cost and response quality. It is useful here mainly as a
boundary contrast: model routers need training data, objective functions,
comparisons, and automatic selection authority. S5.R4 has none of those goals
and forbids that authority.

Transferable idea:

- expected quality, cost, and task difficulty can be relevant evidence.

Rejected transfer:

- a learned router, score, threshold, model choice, automatic action, or claim
  that synthetic cases optimize the system.

### Human decision support

Microsoft's validated human-AI guidelines emphasize making capabilities and
likely error limits clear, supporting verification/correction/control, and
recognizing that inference under uncertainty can create harmful hidden routing.
NIST AI RMF separates context mapping and technical categorization from
governance, calls for differentiated human-AI roles, and warns that converting
complex human phenomena into measurable quantities can remove needed context.

Transferable signals and boundaries:

- show what recognition can and cannot infer;
- show confidence limits and missing evidence;
- distinguish recommendation from decision;
- let the accountable human correct, override, constrain, or request evidence;
- avoid scores that conceal context;
- scale risk-management/review effort to the use context.

## Cross-practice recognition signals

The following signal families recur across the sources and map cleanly to
existing repository owners:

| Signal family | Evidence to inspect | Recognition use | Existing decision owner |
| --- | --- | --- | --- |
| Outcome and deliverable | requested action, reader outcome, artifact, acceptance cue | dominant task type and communication job | Chief Editor routing; audience/outcome canon |
| Work surface | prose, analysis, code/config, architecture boundary, operational incident, product/UI, domain decision | capability significance | Chief Editor; relevant capability owner |
| Consequence and exposure | affected users/assets, publication, sensitivity, reversibility, blast radius | risk and review-depth recommendation | AGENTS risk mode; Chief Editor |
| Evidence state | supplied sources, novelty, volatility, factual claims, contradictions, missing data | research/evidence recommendation | Evidence Framework; Chief Editor |
| Change/significance | cross-owner/boundary, implementation behavior, quality attributes, hard-to-reverse commitment | Architecture/Engineering Review recommendation | respective capability owners; Chief Editor |
| Domain materiality | domain-specific assets, terms, risks, controls, models, delivery surfaces | likely primary/adjacent Domain Packs | Domain Pack Standard; Chief Editor |
| Communication transfer | executive decision, recommendation/ask, technical explanation, stakeholder memo, dense evidence | Professional Communication recommendation | Chief Editor and capability owner |
| Analytical product | synthesis, assessment, options, judgment, recommendation | Professional Analysis recommendation | Chief Editor and capability owner |
| Ambiguity and conflict | missing audience/output, incompatible constraints, mixed intents, contradictory evidence | ask/constrain/decompose/uncertainty recommendation | Chief Editor and Preflight |
| Decomposition | divergent deliverables, owners, evidence, risk, domains, or validation paths | split/sequence/keep-coherent recommendation | Chief Editor |

## Depth recommendations

Recognition should recommend qualitative depth with a reason, never select the
actual process value.

### Research depth signals

- `none or source-light`: transformation/editing task; no material factual,
  product, policy, numeric, domain, or current-state claim.
- `compact`: bounded source verification or repository inspection can answer
  the material question.
- `full`: conflicting/multiple evidence streams, high-governance claim,
  volatile product behavior, domain-specific recommendation, architecture
  decision, or high uncertainty.

### Review depth signals

- `focused`: simple, low-risk, source-light change with one clear deliverable.
- `standard`: factual or implementation surface with bounded evidence and
  ordinary consequence.
- `deep`: high-governance, architecture-significant, cross-domain,
  security-sensitive, source-conflicted, hard-to-reverse, or multi-deliverable
  work.

These labels are recommendation language only. Repository `risk_mode`,
`process_depth`, selected capabilities, and review scope remain Chief Editor
decisions through existing canon.

## Decomposition recognition

Recommend decomposition when two or more parts of a request have materially
different:

- deliverables or audiences;
- primary owners or active roles;
- evidence bases or source boundaries;
- risk/approval requirements;
- lifecycle/validation paths;
- primary Domain Packs whose concerns cannot be handled coherently in one
  artifact;
- sequencing dependencies that make one part a prerequisite for another.

Do not recommend decomposition merely because the request lists several
bullets, mentions multiple technologies, or activates more than one capability
or Domain Pack. A coherent decision packet may legitimately stay one task.

## Anti-patterns rejected

- fixed exhaustive task taxonomy;
- keyword-to-capability or keyword-to-pack mapping;
- numeric likelihood, severity, complexity, or routing score;
- strongest-keyword-wins classification;
- automatic pipeline, capability, pack, risk, depth, role, or review choice;
- treating every ambiguous request as blocked;
- treating every complex-looking request as research-heavy;
- hiding multiple tasks inside one confident label;
- duplicating Professional Analysis, Evaluation Signals, Preflight, Domain
  Pack activation, Architecture Review, Engineering Review, or evidence owners.

## Implications for S5.R4

S5.R4 should add one shared advisory capability with a concise owner contract:

```text
raw request and available evidence
-> observed recognition signals
-> advisory need recommendations plus negative evidence and uncertainty
-> Chief Editor challenge and decision
-> existing routing, preflight, capability, Domain Pack, depth, and review owners
```

The capability should be visible primarily in Intake Agent and Chief Editor
behavior, recorded conditionally in `brief.md`, `orchestration_plan.md`, or
`task-manifest.md`, and challenged by Review Agent only when downstream work
depends materially on the view. It should not create a standalone artifact,
new task-object field set, new role, pipeline, stage, gate, or automation.

## Confidence and residual risk

- High confidence: multi-signal context, impact, constraints, evidence,
  uncertainty, and human ownership are durable intake patterns.
- High confidence: repository owners already make every actual route decision.
- Supported synthesis: one bounded shared capability owner is the smallest
  clear home for the cross-owner advisory contract.
- Residual risk: prose guidance can still be applied as a rigid checklist or
  keyword router; representative negative cases and independent review must
  challenge that misuse.
