# Editorial Intelligence Acceptance Landscape

Date: 2026-07-10

Release: `S5.R5 - Editorial Intelligence Acceptance`

## Executive conclusion

Authoritative practice converges on a claim-centered, context-sensitive
acceptance model rather than a universal score. A credible improvement claim
needs evidence connected to intended use, a meaningful comparison when one
exists, explicit limits on what synthetic or pre-deployment evidence can prove,
and follow-up evidence from operation when the claim is operational. Human
authority must be designed as an effective control, not represented by a
nominal approval label. Architecture, maintenance, reversibility, failure
containment, unintended effects, and residual uncertainty remain part of the
decision because a locally useful mechanism can still make the wider system
harder, less safe, or less governable.

For AI Editorial Office, these findings support a bounded qualitative contract:
each Stage 5 intelligence release must demonstrate both value and restraint,
and the Project Lead must remain the person who decides the disposition.

## Research question and method

The research asked what evidence is sufficient to judge a self-improvement
mechanism before human acceptance, with particular attention to:

- claims and evidence;
- intended versus observed benefit;
- false-positive and false-negative effects;
- human judgment and automation;
- architecture and maintenance cost;
- reversibility, containment, and retirement;
- uncertainty, contradiction, and unintended consequences;
- operational proof and post-implementation learning.

The source set prioritizes current government frameworks and guidance, agency
engineering handbooks, an FFRDC architecture method, and foundational
peer-reviewed human-factors research. Management scorecards and generic
maturity models were excluded. Repository-specific owner decisions are treated
as synthesis, not external fact.

The task-local source register is
[`sources.md`](../tasks/TASK-EDITORIAL-INTELLIGENCE-ACCEPTANCE-RELEASE/sources.md).

## Practice landscape

### 1. AI system evaluation: behavior is not impact

[NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) separates context,
measurement, and management. It asks organizations to describe intended
benefits and costs, use appropriate benchmarks, define human oversight,
evaluate under conditions similar to deployment, monitor production behavior,
document generalization limits, and decide whether development or deployment
should proceed. Its risk-measurement discussion also warns that controlled
results may differ from real-world results and that a baseline is needed when
AI augments or replaces human activity.

[NIST's Measure Playbook](https://airc.nist.gov/airmf-resources/playbook/measure/)
makes the validity distinction more operational: the test must measure the
concept claimed, causal interpretation must consider other factors, and results
must not be generalized outside supported conditions. Production drift and new
ground truth can change conclusions after deployment.

Acceptance consequence:

- prove mechanism conformance separately from outcome value;
- name evidence origin and context;
- cap the claim at what the evidence actually covers;
- require operational evidence for operational improvement claims;
- leave the claim narrower or deferred when only synthetic evidence exists.

### 2. Impact evaluation: intended benefit is a testable proposition

[HM Treasury's AI intervention guidance](https://www.gov.uk/government/publications/the-magenta-book/guidance-on-the-impact-evaluation-of-ai-interventions-html)
defines impact evaluation around whether, to what extent, how, and why an
intervention produced intended impacts. It distinguishes technical capability
testing from wider impact, calls for a clearly described baseline or
business-as-usual comparator, makes unintended outcomes and variation across
contexts explicit, and asks evaluators to state what can be learned at each
stage of rollout.

The [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html)
adds a practical distinction between process and impact evaluation. A mechanism
can be delivered as intended without causing the desired outcome. Impact claims
need a credible comparison or other proportionate causal reasoning; before,
during, and after evidence answer different questions.

Acceptance consequence:

- record the intended beneficiary, decision, or system outcome;
- distinguish planned benefit, observed outcome, and causal attribution;
- use comparison only when populations, tasks, or time periods are meaningfully
  comparable;
- record alternative explanations and missing cases;
- do not convert absence of evidence into evidence of no risk or no value.

### 3. False positives and false negatives are decision costs

[NIST trustworthiness guidance](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/)
places false-positive and false-negative measures inside realistic conditions,
human-AI teaming, representative tests, and failure harm. The measure alone is
not the decision.

[Parasuraman and Riley](https://doi.org/10.1518/001872097778543886) show the
paired human-factors problem: over-reliance can create monitoring and decision
failures, while frequent false alarms can cause disuse and missed true cases.
Automating a function without deliberately designing the human role can itself
degrade performance.

Acceptance consequence:

- inspect both unnecessary activation/bureaucracy and missed useful action;
- consider workload, salience, trust, review capacity, and consequence;
- do not optimize one error direction while hiding the other;
- keep disagreements and contradictory cases visible.

### 4. Human-in-the-loop must mean effective authority

NIST requires human oversight processes to be defined and assessed, not merely
named. Its human-AI interaction guidance distinguishes autonomous action,
human-deferred decisions, and advice to a human decision maker; different
configurations produce different risks. NIST also includes appeal, override,
recovery, change management, and decommissioning in post-deployment management.

The human-factors evidence adds a practical test: a human is not meaningfully in
control if automation determines the choice, hides relevant evidence, overloads
the reviewer, or makes correction and disengagement impractical.

Acceptance consequence:

Evidence for preserved human judgment should answer:

- What decision remains human?
- What evidence reaches the person before the decision?
- Does the person have competence, time, and authority to disagree?
- Can the person correct, override, stop, narrow, or retire the mechanism?
- Is accountability still assigned to the human owner?
- Could interface, defaults, workload, or timing turn review into rubber-stamping?

### 5. Assurance cases: connect evidence to the claim

The [NCSC Principles Based Assurance method](https://www.ncsc.gov.uk/information/principles-based-assurance)
separates a claim, the reasoning that links evidence to it, and evidence that
supports or rebuts it. It also varies assessment independence with the impact
of failure and emphasizes that assurance output must enable a human decision.

S5.R5 does not need formal assurance-case notation or a new assurance process.
The transferable discipline is smaller:

- state the improvement claim precisely;
- point to supporting and contradicting evidence;
- explain why that evidence bears on the claim;
- name assumptions, gaps, context, and residual uncertainty;
- state explicit non-claims;
- let the accountable human decide.

### 6. Engineering release acceptance: verify and validate

The [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/system-engineering-handbook-appendix/)
distinguishes verification—conformance to specified requirements—from
validation—fitness for intended use in the intended environment. Analysis,
inspection, demonstration, and testing may all contribute, and test-article
pedigree affects what the evidence proves.

NASA's [System Acceptance Review guidance](https://swehb.nasa.gov/pages/viewpage.action?pageId=19661899)
expects acceptance criteria, verification and validation results, operational-
environment evidence, risk and mitigation updates, unresolved actions,
deviations, and a human review-panel decision.

Acceptance consequence:

- repository validators and scenario tests prove specified behavior only;
- practical usefulness needs intended-use or operational evidence;
- open actions and deviations stay visible rather than being averaged away;
- human review closes acceptance only after inspecting the package.

### 7. Architecture fitness: value can move between qualities

The [SEI Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/steps-in-an-architecture-tradeoff-analysis-method-quality-attribute-models-and-analysis/)
evaluates architecture against several interacting quality attributes. An
improvement in one can degrade another, so scenarios, risks, sensitivity
points, and tradeoffs matter more than one aggregate result.

Acceptance consequence:

- identify the existing owner and changed surface;
- compare practical benefit with new coupling, artifacts, rules, maintenance,
  review effort, and cognitive load;
- inspect whether simple work becomes heavier;
- record which quality improves and which may degrade;
- reject or narrow a mechanism whose local value creates disproportionate
  system cost.

### 8. Control effectiveness: presence is not operation

The [GAO Green Book](https://www.gao.gov/greenbook) treats internal control as
something management designs, implements, operates, monitors, and periodically
reviews to achieve objectives. A documented control that is not implemented or
operating is not equivalent to effective control.

For intelligence automation, evidence should therefore match authority and
consequence. A proposal, rule, checker, or approval field is design evidence;
real decisions, overrides, failures, maintenance, and observed outcomes are
operating evidence.

Acceptance consequence:

- automation with write, routing, activation, or governance authority requires
  stronger operational proof than advisory text;
- monitoring must connect to a human response;
- failure containment, recovery, and disengagement must be practicable;
- absence of incidents in a small or unrepresentative window is weak proof.

### 9. Continuous improvement and organizational learning

The [UK Lessons Management guidance](https://www.gov.uk/government/publications/lessons-management-best-practice-guidance/lessons-management-best-practice-guidance-html)
distinguishes an observed lesson from an implemented and evaluated improvement
in practice. Monitoring asks whether delivery is on track and whether desired
changes occur; evaluation supports the conclusion that implementation
succeeded; retention over time is a further claim.

Acceptance consequence:

- a documented mechanism is not yet a learned improvement;
- actual use can reveal benefit, burden, or mixed effects;
- recurring evidence can support later confirmation, narrowing, correction, or
  retirement;
- implementation cost and continuing value remain relevant after release.

### 10. Post-implementation review

The [regulatory post-implementation review guidance](https://www.gov.uk/government/publications/the-magenta-book/supplementary-guide-guidance-for-conducting-regulatory-post-implementation-review-html)
uses planned baseline monitoring, post-implementation evidence, stakeholder
input, and proportionate process/impact evaluation. Monitoring often covers
anticipated indicators; stakeholder and evaluation evidence help find
unintended effects and explain why outcomes occurred.

Acceptance consequence:

- define what later evidence would change the disposition;
- treat `defer` as an evidence decision with an owner and observation need, not
  as indefinite limbo;
- use later evidence to retain, narrow, supersede, or retire intelligence;
- do not create mandatory telemetry when ordinary saved evidence is sufficient.

## Evidence origin and claim boundaries

These evidence origins are not scores or maturity levels. They identify what a
claim can and cannot safely say.

| Evidence origin | Can support | Cannot establish alone |
| --- | --- | --- |
| Repository inspection and deterministic checks | file presence, owner placement, forbidden-pattern absence, validator conformance | human usefulness, operating effectiveness, long-term maintenance value |
| Synthetic scenarios or simulation | documented behavior across designed cases, boundary handling, failure hypotheses | real task distribution, real false-positive/negative rates, operational value |
| Controlled pilot or user trial | behavior and user effects in the tested population/context | scaled, durable, or cross-context impact without further evidence |
| Comparable real-use observation | practical benefit/burden in named tasks and conditions | broad causal attribution when alternatives and selection effects remain |
| Longitudinal operational evidence | persistence, maintenance burden, drift, recurring value or harm in the observed scope | universal applicability outside the observed scope |
| Expert or stakeholder judgment | contextual meaning, feasibility, qualitative usefulness, risk interpretation | objective frequency or causal effect without supporting evidence |

An evidence origin should not be treated as universally superior. The decision
question determines what evidence is fit. Qualitative judgment remains
necessary for architecture fit, governance burden, authority, usability,
meaningful restraint, and residual uncertainty.

## What should remain qualitative

- whether the mechanism materially helps human judgment;
- whether its scope and owner fit are proportionate;
- whether maintenance and cognitive burden are acceptable;
- whether human authority is meaningful in context;
- whether one quality improvement justifies degradation elsewhere;
- whether uncertainty is acceptable for the recommended disposition;
- whether observations are blocking or safely non-blocking.

Qualitative does not mean unsupported. Each judgment still needs reconstructable
evidence, reasoning, alternatives, and uncertainty.

## What may be comparative

- before/after task behavior for comparable work;
- with/without mechanism on a bounded task set;
- mechanism versus existing owner or simpler alternative;
- false-positive versus false-negative consequences;
- maintenance/review effort versus observed decision benefit;
- pilot evidence versus later operational evidence;
- current mechanism versus proposed retirement or superseding mechanism.

Comparison is optional when no valid comparator exists. The evidence gap and
reason must then be explicit.

## What should remain optional

- quantitative metrics when the decision can be supported qualitatively;
- controlled trials when lower-risk real-use evidence is sufficient;
- Evaluation Signal views when no material decision question exists;
- post-implementation monitoring beyond evidence already captured in tasks,
  reviews, incidents, feedback, and release artifacts;
- formal assurance-case diagrams or external independent assessment for this
  small single-user repository.

## What should be postponed

- dashboards, telemetry, automatic scanning, or universal comparison datasets;
- acceptance thresholds, health scores, maturity bands, or weighted models;
- automated acceptance, rejection, rollback, retirement, or canon/state action;
- mandatory evidence capture for every ordinary release;
- broad causal claims until comparable real-use evidence exists;
- tool automation until advisory use has operating evidence, a clear failure
  model, and a separately reviewed authority decision.

## Contract implications

The acceptance record should make one line of reasoning reconstructable:

```text
improvement claim
-> intended beneficiary and outcome
-> evidence and meaningful comparison
-> observed limits, counterevidence, and uncertainty
-> value judgment
-> restraint judgment
-> Project Lead disposition
```

Value requires material benefit to human judgment, system quality, safety, or
operational clarity. Restraint requires preserved human authority, no hidden
governance, proportionate architecture and maintenance cost, and a practical
reversal/containment path.

Both are necessary. Neither should be converted to a score, and the record must
never make the disposition automatically.
