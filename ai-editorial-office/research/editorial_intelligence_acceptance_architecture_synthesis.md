# Editorial Intelligence Acceptance Architecture Synthesis

Date: 2026-07-10

Release: `S5.R5 - Editorial Intelligence Acceptance`

## Decision

Implement Editorial Intelligence Acceptance as a conditional section of the
existing Release Pack standard.

Do not create a new canonical KB owner, capability, role, pipeline, lifecycle
stage, review gate, approval board, artifact type, score, dashboard, or
automation authority.

The Release Pack already owns the required Project Lead decision packet and the
readiness rule. S5.R5 adds one Stage 5-specific contract within that packet so
improvement evidence, value, restraint, uncertainty, and recommended
disposition are assessed together. Evaluation Signals, Knowledge Evolution,
the Editorial Evidence Framework, Architecture Review, and relevant Domain
Packs continue to supply or interpret evidence within their existing ownership;
none becomes the acceptance decision owner.

Architecture impact: small.

Confidence: `supported`. Repository owner fit is directly inspectable, and
external practice supports the evidence dimensions. Operational usefulness of
the new section remains unproven until future releases use it.

## Architecture drivers

The selected shape must:

- preserve the Roadmap sequence from release mission to Release Candidate to
  Project Lead review and human acceptance;
- add the smallest decision-support surface that closes the Stage 5 evidence
  gap;
- require both value and restraint without aggregating them into a score;
- distinguish mechanism conformance from intended-use and operational impact;
- expose human authority, automation, architecture, maintenance, reversibility,
  containment, and uncertainty;
- support acceptance, observation, repair, deferral, narrowing, rejection, and
  retirement/supersession;
- remain conditional so ordinary releases do not acquire Stage 5 process weight;
- stay reviewable with existing roles and validators.

## Existing owner coverage

| Question | Current owner | Already covered | What S5.R5 must not duplicate |
| --- | --- | --- | --- |
| Is a release packet ready for Project Lead review? | [`templates/release-pack.md`](../templates/release-pack.md) | readiness rule; goal, architecture, scope, canonical changes, validation, risks, open questions, recommendation | a second release or acceptance packet |
| Who accepts a release? | [`ROADMAP.md`](../ROADMAP.md) and Project Lead operating model | Project Lead accepts after architectural review; Codex creates RCs | an automatic or agent-owned verdict |
| What evidence class and confidence are justified? | [`editorial_evidence_framework.md`](../kb/editorial_evidence_framework.md) | evidence classes, confidence, assumptions, unknowns, validation, residual risk | a new evidence taxonomy or confidence scale |
| How are saved observations exposed for a decision? | [`editorial_learning_framework.md`](../kb/editorial_learning_framework.md), Evaluation Signals section | optional decision question, observation, comparison, contradictions, confidence, owner, human consideration, non-decision | an evaluation store, dashboard, KPI, score, or automatic action |
| How does feedback or observed outcome become reusable learning? | [`customer_feedback_loop.md`](../kb/customer_feedback_loop.md) and [`editorial_learning_framework.md`](../kb/editorial_learning_framework.md) | classification, evidence/scope, disposition, owner, correction, retirement, non-promotion | release acceptance or automatic canon change |
| How are task needs recognized before routing? | [`task_need_recognition.md`](../kb/task_need_recognition.md) | advisory request evidence, uncertainty, negative evidence, recommendation/decision split | post-release value judgment or disposition |
| How are architecture fitness and tradeoffs evaluated? | [`architecture_review.md`](../kb/architecture_review.md) | drivers, quality scenarios, tradeoffs, risks, assumptions, rationale | a duplicate architecture method |
| How are AI evaluation and oversight assessed when AI is material? | [`ai_engineering_domain_pack.md`](../kb/ai_engineering_domain_pack.md) | task-shaped cases, baselines, regressions, human oversight, fallback/rollback, operational evidence | global policy or acceptance authority |
| How are releases independently checked? | [`review_pipeline.md`](../pipelines/review_pipeline.md) and Review Agent | existing review gate, evidence/architecture/learning/signal challenge | a new review gate or role |
| How is external memory changed? | Memory Hygiene Intelligence in [`editorial_learning_framework.md`](../kb/editorial_learning_framework.md) | exact-copy/summary, correct/compress/retire/omit/defer/no-sync, review and checker boundary | automatic memory action or a new memory owner |

## Missing Stage 5 acceptance evidence

The existing Release Pack sections are individually useful but do not require a
single, explicit argument that a self-improvement release has both practical
value and architectural restraint. Specifically missing are:

1. A precise improvement claim and explicit non-claims.
2. Intended beneficiary, decision, or system outcome.
3. Evidence origin and the limit it places on claim strength.
4. Intended versus observed benefit.
5. Real-use versus synthetic evidence distinction.
6. Meaningful comparison or an explicit reason no valid baseline exists.
7. False-positive, false-negative, contradiction, and cross-effect risk.
8. Architecture cost, duplicate-owner risk, and simple-task burden.
9. Governance impact and an explicit hidden-governance inspection.
10. Human evidence, competence, time, authority, override, correction, stop,
    and accountability.
11. Automation authority plus evidence proportionate to consequence.
12. Reversibility, failure containment, rollback/disablement where relevant,
    and retirement/supersession.
13. Maintenance burden and the owner of continuing evidence.
14. Evidence gaps, residual uncertainty, and what would change the conclusion.
15. A Stage 5 disposition vocabulary broader than accepted/changes requested.

These fields are related only for the Project Lead acceptance decision. They do
not require a new general evaluation or learning owner.

## Options considered

### Option A - Conditional Release Pack contract

Decision: selected.

Why:

- uses the already mandatory Project Lead packet;
- keeps evidence and recommendation next to architecture, validation, and risk;
- adds no artifact or lifecycle transition;
- can be explicitly omitted for ordinary releases;
- permits concise references to current evidence owners;
- makes missing information visible without generating a score.

### Option B - New `kb/editorial_intelligence_acceptance.md` owner

Decision: rejected.

Why:

- the stable system already has an acceptance packet and human boundary;
- a separate KB owner would invite a second workflow and duplicated release
  rules;
- no unique reusable capability remains after current owners are mapped;
- the complete contract fits coherently inside the Release Pack standard.

Reconsider only if repeated real use shows the Release Pack section cannot stay
compact or needs reusable guidance that would otherwise be duplicated across
several canonical owners.

### Option C - Put acceptance in Evaluation Signals

Decision: rejected.

Why:

Evaluation Signals intentionally stop before the decision. They may provide
saved observation, comparison, contradiction, confidence, and non-decision
evidence to the Release Pack, but accepting or rejecting there would violate
the accepted S5.R2 boundary.

### Option D - Put acceptance in Knowledge Evolution

Decision: rejected.

Why:

Knowledge Evolution owns learning disposition, pattern confirmation, canon
correction/retirement, and memory disposition. It can supply actual-use and
maintenance evidence, including a candidate to retire stale intelligence, but
it does not own Project Lead release acceptance.

### Option E - New acceptance pipeline, review gate, board, or automated score

Decision: rejected.

Why:

The mission forbids these forms, and the evidence shows that context,
tradeoffs, qualitative judgment, and uncertainty cannot be safely collapsed
into a universal mechanism.

## Bounded contract

### Applicability

Complete the contract for:

- Stage 5 Editorial Intelligence releases;
- later advisory or self-improvement releases only when the Project Lead or
  governing release scope explicitly applies the contract.

Omit it for ordinary releases. Refer to an existing S5 record when a release
only consumes accepted intelligence and does not change it.

### Core decision rule

An accept recommendation requires evidence for both:

1. **Value** — material improvement to human judgment, system quality, safety,
   or operational clarity within the stated scope.
2. **Restraint** — preserved human authority, no hidden governance,
   proportionate architecture and maintenance cost, and a practical path to
   contain, reverse, narrow, supersede, or retire the mechanism.

If value is unsupported, do not recommend acceptance merely because control is
preserved. If restraint is unsupported, do not recommend acceptance merely
because the mechanism appears useful. No averaging, weighting, or score can
offset a failure of either principle.

### Claim and evidence rule

The record must separate:

```text
claim
-> supporting and contradicting evidence
-> reasoning and scope
-> gaps, uncertainty, and non-claims
-> human disposition
```

Evidence origin sets a boundary on the claim:

- repository checks prove implementation state and conformance;
- synthetic scenarios prove behavior only for designed cases;
- pilots prove results only in their tested population and context;
- real-use observations prove effects only in named tasks/conditions;
- longitudinal evidence may support persistence, drift, maintenance, or
  retirement within the observed scope;
- expert judgment can support qualitative interpretation but must expose its
  basis and uncertainty.

Synthetic-only evidence cannot prove an operational improvement. It may support
a narrower contract-conformance claim, a bounded trial, an observation, or a
defer/narrow recommendation.

### Human authority rule

`Human in the loop` is not sufficient language. The record must state:

- the exact human decision;
- evidence available before that decision;
- required competence and realistic review capacity;
- authority to disagree, correct, override, stop, narrow, or retire;
- accountability after the decision;
- any default, interface, timing, or workload condition that could create
  rubber-stamping.

The Project Lead remains the acceptance authority. The contract supplies a
recommendation only.

### Automation rule

Automation evidence must be proportionate to:

- the authority or side effect it receives;
- consequence and blast radius of error;
- reversibility and containment;
- detectability of failure;
- false-positive and false-negative consequences;
- operating context and affected people/systems;
- availability of non-automated or lower-authority alternatives.

Any proposal that removes human review, changes canon/state, or performs
release disposition automatically fails restraint under the current
architecture.

### Hidden governance rule

Inspect behavior, not labels. Hidden governance exists if the mechanism can,
without the current accountable owner deliberately deciding:

- route or activate work;
- require ordinary-task artifacts or dashboards;
- create a new de facto approval or rejection gate;
- change task/release state;
- write canon, memory, backlog, roadmap, capability, or Domain Pack state;
- select learning, memory, or retirement disposition;
- make a recommendation effectively mandatory through defaults, unavailable
  evidence, time pressure, or impractical override.

The release must name the actual decision and write paths inspected.

### Dispositions

These are recommendations for Project Lead judgment, not task statuses or
automatic actions.

| Disposition | Use when |
| --- | --- |
| `accept` | value and restraint are supported; no blocking evidence gap remains |
| `accept with observations` | value and restraint are supported; remaining non-blocking uncertainty or follow-up has a named owner and does not undermine the current claim |
| `changes requested` | the goal remains sound but a bounded repair is required before acceptance |
| `defer` | potential value exists but evidence, timing, comparison, or operational observation is not yet sufficient |
| `narrow scope` | a smaller claim, audience, authority, or use case is supported while the broader proposal is not |
| `reject` | value is absent/unsupported, restraint fails, risk is unacceptable, or the mechanism is fundamentally misfit |
| `retire or supersede` | existing intelligence is stale, harmful, duplicative, uneconomic, or replaced by a better owner/mechanism; change remains a separate reviewed human action |

`Accept with observations` cannot hide a blocking gap. `Defer` must name the
needed evidence or trigger. `Retire or supersede` does not delete history or
change canon automatically.

## Qualitative, comparative, optional, and postponed evidence

### Must remain qualitative

- material human benefit;
- architecture and governance proportionality;
- authority quality and realistic override;
- maintenance/cognitive burden;
- cross-quality tradeoffs;
- acceptability of residual uncertainty.

These judgments still require evidence and reasoning.

### May be comparative

- before/after or with/without behavior for comparable tasks;
- current owner versus proposed mechanism;
- practical benefit versus maintenance and review cost;
- false-positive versus false-negative consequence;
- one release/version versus a superseding mechanism.

Comparison is required only when meaningful. If no valid baseline exists, name
the gap and limit the claim.

### Optional

- quantitative metrics;
- Evaluation Signal section beyond the material decision question;
- controlled pilots for low-authority advisory mechanisms;
- separate post-implementation evidence collection when existing task/review/
  feedback records are sufficient;
- external independent assessment for ordinary low-consequence intelligence.

### Postponed until real-use evidence exists

- dashboards, telemetry, automatic evidence collection, or release scanning;
- automation beyond read-only advisory checks;
- universal baselines or acceptance datasets;
- any broader application of the contract to ordinary releases;
- formal tooling for disposition or retirement.

## Implementation surface

Canonical change:

- `templates/release-pack.md`: add the conditional contract and expand the
  recommendation field for Stage 5 dispositions.

Non-canonical release evidence:

- twelve-case markdown smoke test and test index entry;
- three required research/release reports;
- S5.R5 Release Pack;
- task lifecycle artifacts;
- Roadmap, Backlog, and project-state RC normalization;
- `/about` exact copies and compact summaries only if the current memory-package
  checker and Memory Hygiene contract require them.

Explicitly unchanged:

- `AGENTS.md`;
- roles and role specs;
- pipelines and review gate;
- task status model and lifecycle;
- capability registry and Domain Packs;
- Evaluation Signals and Knowledge Evolution ownership;
- automatic actions of every kind.

## Architecture scenarios

| Scenario | Expected response |
| --- | --- |
| Synthetic proof without real use | cap claim; defer or narrow rather than claim operational improvement |
| High practical value and high maintenance | compare benefit/cost; narrow, request repair, or reject if disproportionate |
| Better routing but heavier simple tasks | expose false positives and simple-task degradation; narrow scope |
| Automation removes human review | restraint fails; reject under current authority model |
| Useful mechanism with weak source evidence | request evidence or defer; do not accept the broad claim |
| Low-cost clear human benefit | accept if evidence and authority are sufficient |
| Duplicate owner | reject or merge into existing owner; no second mechanism |
| Unclear value | defer with named evidence need |
| Existing intelligence is stale or harmful | retire/supersede recommendation with separate reviewed action |
| Positive and negative evidence conflict | preserve contradiction; narrow/defer/request repair depending materiality |
| One quality improves while another degrades | explicit tradeoff; accept only if value and restraint both survive |
| Supported value with non-blocking uncertainty | accept with observations and named owner/follow-up |

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| The section becomes a checklist ritual | require claim/evidence reasoning, non-claims, and disposition rationale |
| Release authors overstate synthetic validation | evidence-origin rule and explicit operational-proof limitation |
| Ordinary releases inherit bureaucracy | strict applicability and omission instruction |
| Observations conceal blockers | disposition definition forbids it |
| Template becomes a second evidence owner | references to Evidence Framework, Evaluation Signals, Architecture Review, Knowledge Evolution, and packs |
| Future tooling automates disposition | explicit non-automation and Project Lead boundary |

## Sufficiency judgment

The selected solution is sufficient for Release Candidate implementation. The
existing Release Pack can hold the contract coherently, all supporting evidence
owners remain intact, and the twelve mission scenarios can validate behavior
without new architecture.

Remaining uncertainty is operational: future use must show whether the section
actually improves Project Lead judgment without adding disproportionate release
work. That uncertainty belongs as an explicit S5.R5 non-claim and future
Evaluation Signal, not as a reason to create tooling or a second owner now.
