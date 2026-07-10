# Evaluation Signals Landscape

Date: 2026-07-10

Release: `S5.R2 - Evaluation Signals`

## Executive finding

Professional practice does not support one general score for whether an
engineering or editorial system is improving. It supports a bounded set of
signals that answer specific questions, preserve context and uncertainty, and
are used by accountable humans alongside qualitative evidence.

The strongest transfer to AI Editorial Office is therefore not a KPI system or
dashboard. It is an optional, evidence-backed view over observations the
repository already knows how to save: activation, actual use effect, review
findings, architecture risks, evidence confidence, learning disposition,
staleness, release outcomes, and maintenance burden.

Counts may be evidence. They are not judgments. A useful Evaluation Signal
must say what question it informs, what evidence and comparison window support
it, what context or denominator matters, what alternative explanation or
contradiction exists, how confident the interpretation is, which existing owner
is affected, and what remains a Project Lead decision.

## Research question

What is the smallest Evaluation Signals mechanism that helps the Project Lead
judge system improvement, release value, capability and Domain Pack use,
recurring findings, architecture drift, learning movement, stale knowledge,
and maintenance cost without creating scores, KPIs, rankings, automatic
governance, or a parallel observability system?

## Method and source boundary

The research combined:

- current repository owners and Stage 5 release evidence;
- primary research on engineering and product measurement;
- current standards and public-sector evaluation guidance;
- authoritative engineering practice for monitoring, architecture evaluation,
  quality, continuous improvement, process capability, and AI evaluation.

Professional sources were selected for transferable principles, not copied as
ready-made metrics. AI Editorial Office is a local markdown-first editorial
operating system, not a production service, enterprise engineering department,
or policy programme. Any transfer must fit its low event volume, qualitative
work, existing review gate, and single Project Lead authority.

## Repository baseline

The repository already saves most of the evidence S5.R2 needs:

- `task-manifest.md` and `orchestration_plan.md` can show selected capabilities
  and Domain Pack activation;
- `review.md` saves findings, verdict, scope, evidence, and repeatable checks;
- `architecture_review.md` provides drivers, quality-attribute scenarios,
  tradeoffs, architecture risks, and decision rationale;
- `editorial_evidence_framework.md` owns evidence classes, confidence,
  assumptions, unknowns, validation, and residual risk;
- `editorial_learning_framework.md` owns source-evidence chains, pattern
  confirmation, learning disposition, stale knowledge, owner routing, and
  non-promotion;
- `domain_knowledge_pack_standard.md` distinguishes activation from actual-use
  benefit, burden, mixed effect, or unknown effect;
- `feedback_patterns.md` can hold recurring comparable patterns;
- release packs, release reports, final decisions, validation outputs, and
  Project Lead verdicts save release-level evidence.

The missing layer is a compact way to assemble selected observations for a
specific human decision without treating the assembled view as a verdict.

## Professional practice

### Engineering performance and productivity

[DORA's current software delivery metrics guide](https://dora.dev/guides/dora-metrics/)
uses several measures in tension, applies them at an application or service
level, and warns against setting metrics as goals, comparing unlike systems,
using one metric for a complex system, competing on metrics, or spending more
on measurement than improvement. Transfer: a count must remain scoped to a
comparable release/task set and cannot become a target, rank, or standalone
decision.

The peer-reviewed [SPACE framework](https://queue.acm.org/detail.cfm?id=3454124)
shows why activity alone cannot represent productivity. It uses multiple
dimensions and explicitly warns that commit, pull-request, review, or other
activity counts can have opposite explanations. Transfer: capability
activation frequency can identify a question, but it cannot establish value,
quality, individual performance, or retirement need.

### Software quality and architecture fitness

[ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) defines a
multi-characteristic product quality model for specifying, measuring, and
evaluating software quality. Transfer: quality is plural; release observations
should name the quality or risk affected instead of compressing correctness,
maintainability, reviewability, traceability, and usability into a scalar.

The [SEI Architecture Tradeoff Analysis Method collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)
frames architecture evaluation against quality-attribute goals and exposes
risks and tradeoffs rather than assigning a universal architecture grade.
Transfer: recurring architecture warnings should retain driver, affected
quality attribute, scenario, tradeoff, and risk context.

Thoughtworks' description of an
[architectural fitness function](https://www.thoughtworks.com/en-us/radar/techniques/architectural-fitness-function)
shows that some architecture characteristics can be checked objectively and
continually. It is an older practice note and is not sufficient authority for
automating governance here. Transfer: reuse deterministic repository checks
where they already exist; keep qualitative architecture drift in Architecture
Review and human judgment.

### Monitoring and organizational observability

Google SRE's chapter on
[monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
distinguishes trends, comparisons, alerting, dashboards, and retrospective
analysis. It emphasizes high signal, low noise, simple human-facing rules, and
the non-trivial cost of monitoring itself. Transfer: Evaluation Signals should
surface only material questions, not collect everything or require someone to
watch a dashboard.

DORA's guidance on
[monitoring systems for business decisions](https://dora.dev/capabilities/monitoring-systems/)
warns against monitoring everything and local optimization, and emphasizes
making meaningful data available in a form suited to the decision. Transfer:
an existing markdown artifact is sufficient; a dashboard is unnecessary.

Google SRE's definition of
[toil](https://sre.google/sre-book/eliminating-toil/) identifies manual,
repetitive, tactical, automatable work with little enduring value and work that
scales with system growth. Transfer: maintenance-cost signals should describe
observed repeated burden and enduring value, not equate every difficult or
unpleasant task with waste.

### Evaluation and continuous improvement

The 2026 UK Government
[Magenta Book](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html)
distinguishes design, implementation, outcome, process, impact, and value-for-
money questions. It emphasizes proportionality, usefulness to decision-makers,
triangulation, alternative explanations, limitations, and evidence robustness
matched to the size of the decision. Transfer: a signal record should begin
with the decision question and use stronger evidence for broader conclusions.

The Institute for Healthcare Improvement's
[PDSA guidance](https://www.ihi.org/library/model-for-improvement/testing-changes)
uses planned local tests, observation, and action on learning to build knowledge
across repeated cycles. Transfer: a proposed improvement remains a hypothesis;
future comparable use should confirm, contradict, constrain, or reject it.

### Capability maturity

[ISO/IEC 33020:2019](https://www.iso.org/standard/78526.html), confirmed current
in 2026, shows that formal process-capability assessment requires a defined
measurement framework and produces attribute ratings and capability levels.
Transfer: AI Editorial Office does not have the evidence volume, assessor
contract, or mission authority for maturity levels. Consistency of behavior may
be observed qualitatively, but no maturity score or level should be introduced.

### Product health

The Google Research
[HEART framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/)
maps product goals to user-centered measures rather than beginning with easily
available data. Transfer: Domain Pack usefulness and release value must start
from intended effect and observed use, not activation volume.

### AI evaluation

The [NIST AI RMF Measure function](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
uses quantitative, qualitative, or mixed methods; requires context,
uncertainty, documented limitations, regular reassessment, and independent
review; and treats measurement as input to management decisions. Transfer:
AI-related evaluations must be context-bound, reviewable, and explicit about
what cannot be measured. The separation between measuring and managing also
supports S5.R2's separation between signals and Project Lead decisions.

## Synthesis: signal, evidence, and decision

The professional sources repeatedly separate three layers:

```text
saved observation or measurement
-> contextual interpretation
-> accountable human decision
```

AI Editorial Office should preserve the same separation:

```text
task, review, validation, release, or learning evidence
-> optional Evaluation Signal view
-> Review Agent challenge and Project Lead judgment
```

An Evaluation Signal is therefore not a raw count and not a decision. It is a
reviewable claim that selected evidence may matter to a named human question.

## Useful signal families

| Signal family | Useful evidence | Question it may raise | Why it cannot decide |
| --- | --- | --- | --- |
| Capability activation | Comparable task manifests/plans, relevant capability, bounded window, non-activation context | Is a capability understood, needed, or over/under-activated? | Frequency does not show value, omission cost, task mix, or correct routing. |
| Domain Pack usefulness | Actual sections/sources used, affected decision or artifact, benefit/burden/mixed/unknown, confidence | Which packs materially help or burden comparable work? | Activation is not value; rare packs may cover rare high-risk tasks. |
| Recurring review findings | Comparable findings, issue type, severity/context, repair outcome, affected owner | Is a prevention or owner update worth considering? | Repeated wording may hide different causes; rejected releases may show a strong gate working. |
| Architecture issues | Drivers, quality scenarios, tradeoffs, repeated risk, accepted/residual risk | Where is drift or cross-owner friction beginning? | Architecture significance and tradeoffs remain qualitative and context-specific. |
| Evidence quality | Evidence classes/confidence, recurring gaps, contradictions, validation outcomes | Are decisions becoming better supported or repeatedly relying on weak evidence? | Confidence labels are claim-specific and cannot be averaged into system quality. |
| Learning promotion | Candidate sources, disposition changes, acceptance/rejection/deferral, owner update evidence | Which candidates repeatedly mature, stall, or fail? | More promotion can mean useful learning or harmful canon growth; less can mean discipline. |
| Stale knowledge | Repeated freshness warnings, unresolved owner conflict, correction/retirement outcomes | Which knowledge deserves verification or bounded owner repair? | A stale warning may be false, local, or already mitigated. |
| Release quality | Acceptance/rejection reasons, validation, review repairs, realized effect, residual risk | Which releases delivered evidence-backed value and which assumptions failed? | Acceptance is Project Lead authority; successful validation does not prove real-world value. |
| Maintenance burden | Repeated manual work, duplicated updates, validator failures, context load, no enduring value | Which areas create avoidable recurring cost? | Effort is not automatically waste; some high-cost work protects high-value quality. |

## Signals that may use counts

Counts or frequencies can be descriptive evidence for:

- capability activation within a named comparable task set;
- Domain Pack activation within a named comparable task set;
- occurrences of the same review or architecture condition;
- learning dispositions across a named release/task window;
- repeated stale-knowledge or maintenance-burden events.

A count is usable only when the record preserves:

- bounded comparison window;
- comparable population and denominator when it matters;
- source artifact pointers;
- missing or ambiguous cases;
- task mix and exposure opportunity;
- interpretation limits and alternative explanations.

The system should not define target values, thresholds, maturity bands,
percentile ranks, weighted totals, or composite scores.

## Signals that must remain qualitative

These judgments should not be reduced to numeric proxies:

- whether a Domain Pack was useful enough to justify its maintenance;
- whether evidence was sufficient for a material decision;
- whether an architecture warning indicates drift or a legitimate tradeoff;
- whether a release delivered meaningful value;
- whether a repeated review finding reflects weak production, stronger review,
  a changed task mix, or another cause;
- whether a maintenance burden has enduring protective value;
- how contradictory signals should be reconciled;
- whether a learning candidate belongs in canon;
- whether a release should be accepted, rejected, or reprioritized.

Numbers may accompany these judgments but cannot replace the evidence and
rationale.

## Task-local versus reusable

Default to task-local when:

- one task or release provides the only evidence;
- the observation depends on local scope, preference, or unusual risk;
- comparability or denominator is unknown;
- an alternative explanation remains plausible;
- future decision value is lower than maintenance cost.

An observation may become a reusable pattern candidate only when the existing
Knowledge Evolution checks are satisfied: saved comparable evidence, explicit
scope, contradictions and alternatives considered, an existing owner, future
value, review, and non-promotion.

Evaluation Signals do not create a new promotion path. They use the existing
learning disposition path when future reuse is proposed.

## Dangerous uses

Reject or ignore a proposed signal when it:

- counts activity without an outcome or decision question;
- treats capability or Domain Pack activation as proof of usefulness;
- treats rare activation as proof of irrelevance;
- treats review rejection as failure without examining whether the gate worked;
- compares unlike tasks, releases, packs, or time windows;
- hides missing cases, selection bias, or changed exposure;
- collapses contradictory signals into an average or score;
- turns a descriptive count into a target, KPI, ranking, incentive, or
  acceptance threshold;
- uses precision that the evidence cannot support;
- creates collection or dashboard maintenance burden greater than its decision
  value;
- requests automatic canon, backlog, roadmap, memory, release, or capability
  action;
- monitors individuals or evaluates role performance from activity traces.

## Interaction with existing owners

### Learning Framework

The Learning Framework continues to own source-evidence chains, pattern
confirmation, learning disposition, stale knowledge, owner-scoped changes, and
non-promotion. An Evaluation Signal can expose a question to that framework but
cannot add a new disposition or bypass its evidence test.

### Review

Review Agent should challenge whether a signal is comparable, evidenced,
contextualized, proportionate, and genuinely useful to a named decision. Review
must preserve contradictions and reject target, score, ranking, or automatic-
action language. This is part of existing review, not a new gate.

### Project Lead

The Project Lead remains the only release acceptance and strategy owner. A
signal can support questions such as "investigate", "compare", "verify", or
"consider an owner-scoped change". It cannot output `accept`, `reject`,
`reprioritize`, `retire`, or `change canon` as an automatic action.

## Minimal architecture implications

The evidence does not justify:

- a new Evaluation capability or framework;
- a dashboard, database, telemetry layer, or scanner;
- a scorecard or health index;
- mandatory signal capture for every task;
- a new role, pipeline, stage, review gate, or status;
- changes to task-object fields or Domain Pack activation rules;
- automatic trend detection or governance actions.

The evidence supports:

- one optional compact signal record inside existing task, review, release,
  pattern, or governance artifacts;
- release-pack visibility when a signal is material to Project Lead review;
- existing Chief Editor assembly and Review Agent challenge;
- current evidence, learning, architecture, Domain Pack, and Project Lead
  owners remaining authoritative;
- one representative scenario test that includes noise and contradictions.

## Evidence confidence and limitations

- Professional-practice findings: `supported` to `verified` within the cited
  source scope.
- Transfer to AI Editorial Office: `supported`; it is an architecture synthesis
  from professional practice and repository inspection, not an externally
  validated causal claim.
- Main limitation: the repository has little accumulated ordinary-task signal
  volume. S5.R2 can make future evidence legible; it cannot prove current
  capability, pack, or release value from synthetic scenarios.
- Residual risk: future users may still treat counts as targets. Explicit
  non-decision fields and independent review are required safeguards.

## Research conclusion

S5.R2 should implement Evaluation Signals as a small advisory view over saved
evidence, not as a measurement system. The useful unit is a decision question
with evidence and limits, not a number. The mechanism should make important
signals visible and make unsafe inferences harder, while leaving every release,
canon, roadmap, backlog, memory, and capability decision with the existing
human and canonical owners.
