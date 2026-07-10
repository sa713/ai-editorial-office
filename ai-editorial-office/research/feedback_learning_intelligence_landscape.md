# Feedback and Learning Intelligence Landscape

Date: 2026-07-10

Release: `S5.R1 - Feedback and Learning Intelligence`

## Executive Conclusion

Authoritative practice does not support a direct path from feedback to policy.
Across organizational lessons learned, continuous improvement, customer
research, incident postmortems, product feedback, and human-AI evaluation, a
stable sequence recurs:

```text
captured signal
-> separated observation and interpretation
-> evidence and applicability validation
-> bounded disposition
-> responsible-owner review
-> small action or explicit no-action
-> follow-up on actual effect
```

AI Editorial Office already owns almost all of this behavior in two places:

- `kb/customer_feedback_loop.md` classifies actual post-delivery feedback;
- `kb/editorial_learning_framework.md` decides whether a saved signal remains
  local, becomes a learning or pattern candidate, reaches an owner-scoped canon
  update, or is rejected, deferred, corrected, superseded, or retired.

S5.R1 therefore needs an explicit bridge, not a new feedback system. The bridge
must also accept observed completed-work outcomes when no customer comment
exists, because successful and unsuccessful task behavior can produce learning
evidence without becoming “customer feedback.”

## Research Question And Method

The research asked how a small, single-user AI editorial system should:

- distinguish useful signals from anecdotes and noise;
- connect feedback and outcomes to evidence and applicability scope;
- confirm patterns without arbitrary scoring;
- route proposed action to an existing owner;
- learn from successes as well as failures;
- use human feedback around AI-assisted work without silent adaptation;
- learn from real Domain Pack activation without making pack telemetry
  mandatory;
- reject, defer, correct, or retire learning safely.

The evidence base combines the current repository owners with official
government guidance, first-party operational handbooks, an improvement-method
owner, and peer-reviewed human-AI interaction research. Full source metadata
and claim traceability are in
`tasks/TASK-FEEDBACK-LEARNING-INTELLIGENCE-RELEASE/sources.md` and
`claims_table.md`.

## Current Repository Baseline

### Customer feedback is already classified

The Customer Feedback Loop applies only after a delivered result receives a
real customer/user reaction. Its current classifications are:

- `task_local`;
- `preference`;
- `observation`;
- `confirmed_pattern`;
- `system_change_candidate`.

The workflow already prevents a single reaction from changing production
rules, requires Chief Editor classification, and keeps raw feedback in the task
folder. It also distinguishes task-local action, preference, pattern tracking,
and a separate reviewed system update.

### Reusable learning already has disposition states

The Editorial Learning Framework already provides:

- a Knowledge Evolution path from task-local observation through candidates to
  a reviewed owner update;
- disposition states including `task_local`, `learning_candidate`,
  `pattern_candidate`, `canon_update_candidate`, `accepted_canon`,
  `superseded`, `retired`, `rejected`, and `deferred`;
- a source-evidence chain;
- pattern confirmation criteria;
- canonization checks;
- stale/conflicting knowledge challenge;
- correction, supersession, retirement, and memory disposition.

These states are not operational task statuses. They solve a different problem
from customer-feedback classification: feedback classification explains what a
reaction means now; learning disposition explains what the system may safely do
with a saved signal beyond the current exchange.

### Pattern and task-object support already exists

`kb/feedback_patterns.md` is already the recurring-pattern journal, and the
task object already permits optional reusable-pattern, post-task-learning, and
memory-disposition views. Chief Editor and Review Agent already point to the
two canonical owners. No new role, store, status, or lifecycle stage is needed.

### Domain Pack activation is recorded, but effect is not

The Domain Knowledge Pack Standard already asks an activation note to name the
pack, activation reason, relevant sections or sources, confidence, limits,
stale-if triggers, and stop conditions. Review checks activation, boundaries,
sources, and maintenance concerns.

What is missing is a compact way to say what happened because the pack was
used: which part actually influenced the work, what evidence supports a useful
or burdensome effect, whether the effect is uncertain, and whether any pack
change is merely a candidate.

The Stage 4 Strategic Review explicitly says the pack layer is validated by
release scenarios but not yet by unrelated ordinary tasks. A repository scan
for active-pack task evidence found release construction and state-maintenance
references, not enough ordinary-task activation/outcome evidence to confirm
pack value. S5.R1 must preserve that gap rather than manufacture a success
claim.

## External Practice Landscape

| Practice area | Authoritative signal | Transfer to S5.R1 |
| --- | --- | --- |
| Organizational lessons learned | [GAO](https://files.gao.gov/reports/GAO-26-107863/index.html) separates collection, analysis, validation, archiving, and sharing; validation checks that the lesson is correct and determines applicability. | Do not equate capture with learning. Require an evidence pointer, a learning claim, and applicability scope before promotion. |
| Institutional learning | [NASA](https://www.nasa.gov/nasa-lessons-learned/) describes official, reviewed lessons that link a driving event to recommendations and feed existing policies, practices, procedures, and training. | A learning item needs a source event and recommendation; improvements enter existing owners, not a parallel system. |
| Continuous improvement | [IHI](https://www.ihi.org/library/model-for-improvement/testing-changes) recommends small tests with an objective, prediction, collected data, study against the prediction, and refinement before scale. | A system-change candidate should be bounded and testable; wider reuse depends on observed effect, not confidence rhetoric. |
| Postmortems | [Google SRE](https://sre.google/workbook/postmortem-culture/) and [AWS COE](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.coe.en.html) emphasize factual impact, root cause, concrete preventative/mitigating actions, ownership, review, and follow-through. | Recurring workflow failures need causal evidence and an owner-scoped action. Vague blame or “improve process” is not reusable learning. |
| Customer feedback and qualitative research | [GOV.UK research analysis](https://www.gov.uk/service-manual/user-research/analyse-a-research-session) separates observations from interpretation, clusters matching evidence, and permits irrelevant isolated notes to be discarded before findings and actions. | Preserve raw signal separately; isolated or unsupported feedback may be rejected without becoming a pattern. |
| Product/service improvement | [GOV.UK satisfaction guidance](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) asks services to combine feedback sources, identify significant patterns, test changes, and monitor whether the expected effect occurred. | Pattern confirmation needs corroboration and outcome evidence. Proposed changes remain candidates until tested. |
| Outcome focus | [GOV.UK user-research guidance](https://www.gov.uk/service-manual/user-research/how-user-research-improves-service-design) warns against learning only what people like or prefer and focuses on whether users achieve the right outcome. | Preference remains preference unless outcome evidence shows broader system relevance. Capture meaningful outcomes, not sentiment alone. |
| Human-in-the-loop AI | [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) calls for continuous governance, clear human oversight, deployment-context measurement, and adjudicated feedback rather than unreviewed incorporation. | Project Lead, Chief Editor, Review Agent, and canonical owners retain authority. Feedback cannot silently change AI/editorial behavior. |
| Generative AI evaluation | [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) recommends ground-truth comparison, multiple evaluation methods, human oversight, and documented provenance/assumptions. | AI-assisted work should link the observed outcome to task evidence and acknowledge alternative explanations and generalization limits. |
| AI monitoring limits | [NIST AI 800-4](https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems) reports unresolved human-AI feedback-loop methods, beneficial-impact metrics, feedback burden, and drift-monitoring challenges. | Do not invent a score, dashboard, or mandatory telemetry. Use risk- and materiality-based qualitative evidence until stronger measures exist. |
| Human-AI correction and adaptation | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) supports efficient correction, uncertainty scoping, cautious adaptation, granular feedback, and user control. | Task-local corrections should be easy; durable adaptation should remain explicit, cautious, and owner-reviewed. |
| Feedback semantics | [Google PAIR](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/) distinguishes implicit and explicit feedback and notes that user intent may not align with what a system can validly learn. | Record what the feedback actually evidences. Do not infer a reusable preference, model lesson, or policy from ambiguous behavior. |
| Product feedback triage | [GitLab](https://handbook.gitlab.com/handbook/product/product-processes/customer-issues-prioritization-framework/) uses multi-channel context and timely review while leaving final prioritization with the responsible product team. | Timely consideration does not mandate action. Backlog and roadmap authority remain unchanged. |
| Retrospectives | The [Agile principle](https://agilemanifesto.org/principles.html) supports reflection and adjustment; [Atlassian](https://www.atlassian.com/agile/scrum/retrospectives) emphasizes a few owned actions and follow-through. | Learning may be extracted after material work, but S5.R1 should not make a retrospective mandatory for every task. |

## Cross-Practice Findings

### 1. Preserve signal, interpretation, and action as separate claims

A user statement, observed task outcome, reviewer finding, and repository
conflict are different source signals. Each may justify an interpretation, but
the interpretation is not part of the raw signal. A proposed change is a third
claim that needs its own owner and evidence.

A compact item should therefore be reconstructable as:

```text
source signal + evidence pointer
-> interpreted learning claim
-> applicability scope
-> disposition and owner-scoped action
```

### 2. Keep feedback classification and learning disposition distinct

Replacing the two existing label sets with a single taxonomy would lose useful
meaning. A repeated preference can be classified as `preference` while its
learning disposition is `learning_candidate`, `pattern_candidate`, or
`task_local`. A strong workflow failure may be `confirmed_pattern` in the
feedback loop and still only a `canon_update_candidate` until the correct owner
is reviewed and patched.

The integration should ask two linked questions:

1. What kind of feedback or outcome signal is this?
2. What is the smallest safe learning disposition, if any?

### 3. Evidence sufficiency is qualitative, not a score

This system has too little volume and too many context-sensitive tasks for a
general scoring model. Evidence is sufficient for pattern confirmation when a
reviewer can reconstruct the source signals, see that they describe the same
underlying condition, understand the affected scope, rule out a merely local
cause or preference, and judge the future value or risk material.

Useful corroboration may include:

- similar evidence across multiple tasks, releases, reviews, or contexts;
- a high-impact or safety-critical event with direct causal evidence;
- a controlled comparison or bounded change test;
- a repository-state contradiction;
- direct Project Lead confirmation of applicability;
- a successful outcome repeated under comparable conditions.

Counts may support a judgment but cannot make it. One anecdote is normally
task-local, rejected, or deferred. A one-event exception needs a documented
high-impact rationale, strong evidence, bounded applicability, owner, and
review; it still does not auto-promote.

### 4. Rejection and deferral protect intelligence quality

`rejected` is correct when the signal is irrelevant, contradicted, duplicate,
private beyond allowed scope, unsupported, misclassified, or less valuable
than its maintenance cost. `deferred` is correct when the signal may matter but
evidence, comparability, owner, timing, or release scope is insufficient.

Neither outcome is a failure to learn. Both preserve the decision and prevent
noise from entering recurring guidance.

### 5. Owner-scoped action is the end of triage, not automatic execution

A learning item should name the affected system area and existing canonical
owner. Possible bounded actions include:

- correct the current task or record a scoped user preference;
- watch for comparable evidence in `feedback_patterns.md`;
- propose a small test in a future comparable task;
- request a separate reviewed owner patch;
- correct, supersede, or retire stale guidance;
- take no action, reject, or defer.

The disposition cannot write automatically to canon, backlog, roadmap,
`/about`, a Domain Pack, or model behavior.

### 6. Learn from positive outcomes without success bias

A successful result may produce reusable learning, but “worked once” is not a
confirmed pattern. Record what was different, which evidence connects the
practice to the result, what alternative explanations remain, and where the
pattern is expected to apply. Reuse can begin as a candidate or bounded future
test before canonization.

### 7. Ordinary tasks and releases use the same intelligence with different depth

Releases may justify a full evidence trail. Ordinary tasks should use the
smallest existing artifact: `feedback.md`, `review.md`, `final_decision.md`,
implementation report, or a compact task note. Learning extraction is
triggered when a material signal exists, not at every closure.

Material triggers include repeated friction, a high-impact near miss,
unexpected outcome, successful method with plausible future value, stale canon,
meaningful Project Lead correction, or Domain Pack effect worth checking.

### 8. Domain Pack use needs activation evidence plus effect evidence

When a pack was actually activated and its effect is material, the smallest
existing task artifact should be able to record:

- active pack and activation reason;
- relevant sections or sources actually used;
- task decision, artifact, evidence depth, terminology, risk handling, or
  review finding affected;
- observed benefit, burden, mixed effect, or unknown effect;
- evidence pointer and confidence;
- added context or maintenance cost, including unnecessary complexity;
- alternative explanation or counterfactual limit;
- learning disposition and owner, if action is proposed.

This is not mandatory telemetry. Absence of evidence is `unknown`, not success.
A useful activation may become a bounded reuse candidate. An over-activation
may stay task-local, become a routing learning candidate, or—after repeated
evidence—propose a pack/activation-owner patch. Neither changes a pack
automatically.

### 9. AI-assisted work needs human adjudication and cautious generalization

Feedback about AI-assisted work should identify the human-visible outcome and
saved artifact evidence. It should avoid inferring model quality, prompt
quality, role performance, or system capability from one output without a
comparable basis. Project Lead and existing review/canonical owners decide any
durable change.

## Research-Derived Bounded Flow

The evidence supports this architecture-compatible flow:

```text
actual feedback or observed completed-work outcome
-> classify the source signal when applicable
-> record evidence pointer, affected area, and applicability scope
-> choose the smallest learning disposition
-> review only when reusable or system action is proposed
-> route a bounded action to the existing owner
-> verify effect before wider reuse or canon change
```

Expected dispositions cover the mission cases without a new taxonomy:

- task-local correction or preference;
- `learning_candidate`;
- `pattern_candidate`, with `confirmed_pattern` only after sufficiency review;
- `canon_update_candidate` / feedback `system_change_candidate`;
- `rejected`;
- `deferred`;
- correction, supersession, or retirement for stale learning;
- accepted owner update only after separate review and validation.

## What The Evidence Does Not Support

- automatic canon or model adaptation;
- automatic backlog or roadmap changes;
- a universal feedback score;
- a pattern threshold based only on item count;
- a second feedback taxonomy or learning store;
- a mandatory retrospective or Domain Pack telemetry form for every task;
- a claim that Stage 4 Domain Packs already improve ordinary tasks;
- a new Feedback Agent, Learning Owner, review gate, or lifecycle stage;
- optimization of Domain Pack activation before real usage evidence exists.

## Research Sufficiency And Limits

Confidence is high that existing-owner integration is the correct architecture
shape. The conclusion is supported independently by the repository ownership
map and by external practices that separate capture, validation, ownership,
and action.

The largest evidence limit is intentional: AI Editorial Office does not yet
have enough unrelated ordinary-task Domain Pack activation evidence to confirm
pack value or cost patterns. S5.R1 should make future evidence legible and
reviewable, then defer pack optimization until real signals accumulate.
