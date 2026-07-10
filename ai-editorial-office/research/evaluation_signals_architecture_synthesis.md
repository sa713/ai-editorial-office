# Evaluation Signals Architecture Synthesis

Date: 2026-07-10

Release: `S5.R2 - Evaluation Signals`

## Decision

Implement Evaluation Signals as an optional advisory view over saved evidence
already owned by AI Editorial Office.

Do not create a new Evaluation capability, framework, taxonomy, store,
dashboard, telemetry layer, role, pipeline, lifecycle stage, task status,
review gate, mandatory artifact, score, KPI, rank, target, maturity level, or
automatic action.

The mechanism is:

```text
saved task/review/validation/release/learning evidence
-> optional compact Evaluation Signal view
-> existing Review Agent challenge
-> Project Lead or existing canonical-owner judgment
```

The view may raise a question or expose a pattern. It never supplies the
governance decision.

## Problem being solved

Current canon saves many useful observations but does not give the Project Lead
a stable, bounded way to see them together for a release or system decision.
This makes important evidence discoverable only by reading multiple task,
review, pack, learning, validation, and release artifacts.

S5.R2 closes five gaps:

1. distinguish a useful signal from a raw count or metric;
2. preserve comparison scope, missing cases, uncertainty, contradictions, and
   alternative explanations;
3. route each observation to its existing evidence and canonical owner;
4. make release-level signals visible in the current Project Lead packet;
5. state explicitly that the view cannot accept, reject, rank, reprioritize,
   retire, or modify anything automatically.

## Architectural drivers

- Human judgment: Project Lead review and existing canonical owners retain
  every decision.
- Evidence support: signal claims must be reconstructable from saved artifacts.
- Reviewability: Review Agent must be able to challenge comparison,
  interpretation, uncertainty, and non-decision boundaries.
- Maintainability: no parallel store, new artifact family, or mandatory data
  collection.
- Proportionality: create a view only when a real decision question and material
  evidence exist.
- Architectural stability: reuse the role set, lifecycle, review gate,
  capability map, and owner boundaries.
- Low noise: no collect-everything behavior or dashboard maintenance.

## Quality-attribute scenarios

### Reviewability

- Stimulus: a Release Pack claims repeated architecture warnings.
- Affected surface: release pack, saved review findings, Architecture Review.
- Expected response: Review Agent can trace comparable evidence, see
  contradictions and scope, and determine whether the signal is supportable.
- Evidence: pointers and context in the compact signal record.

### Maintainability

- Stimulus: a new signal family is proposed later.
- Affected surface: existing canonical owner and Learning Framework.
- Expected response: the observation remains with its owner; no new dashboard,
  taxonomy, store, or role is required unless separately reviewed evidence
  proves the current shape inadequate.
- Evidence: one owner, one optional view, no duplicate rules.

### Governance safety

- Stimulus: a signal shows a Domain Pack was rarely activated.
- Affected surface: Domain Pack evidence and Project Lead review.
- Expected response: the view raises a routing/usefulness question, records
  unknown exposure and effect, and forbids automatic retirement.
- Evidence: non-decision field and Review Agent challenge.

### Proportionality

- Stimulus: a task has no material system/release decision signal.
- Affected surface: task artifacts.
- Expected response: no signal record is created.
- Evidence: optionality rule; absence means no material recorded signal, not
  system health.

## Existing owners retained

No signal family receives a new canonical owner.

| Signal family | Evidence/meaning owner retained | Assembly and decision boundary |
| --- | --- | --- |
| Capability activation frequency | Task manifest/orchestration evidence; `capability_registry.md` for capability meaning | Chief Editor may assemble; frequency alone cannot determine value or retirement. |
| Domain Pack usefulness | `domain_knowledge_pack_standard.md` for activation/use effect; specific pack for content; Learning Framework for reuse | Project Lead or reviewed owner update decides; activation is not benefit. |
| Recurring review findings | `review_agent.md` and Review Pipeline for findings; Learning Framework and `feedback_patterns.md` for recurrence/reuse | Review Agent challenges comparability; no automatic prevention rule. |
| Recurring architecture issues | `architecture_review.md` for drivers, scenarios, tradeoffs, and risks | Project Lead/current architecture owner judges significance and response. |
| Evidence quality trends | `editorial_evidence_framework.md` for evidence classes and confidence | Claim-specific confidence cannot be averaged into a system score. |
| Learning promotion trends | `editorial_learning_framework.md` for disposition and owner-scoped canon evolution | More or fewer promotions are not inherently better. |
| Stale knowledge indicators | `editorial_learning_framework.md` for challenge, correction, supersession, and retirement | Verification and reviewed owner action remain required. |
| Release quality observations | Review/final decision/release report/Release Pack and Project Lead verdict | Signal informs the Project Lead; it cannot accept or reject a release. |
| Maintenance-cost observations | Saved task/release evidence plus the affected canonical owner; Learning Framework for reuse | Burden must be weighed against enduring value and quality protection. |

## Why the Learning Framework is the integration point

The optional view does not redefine evidence, architecture, Domain Pack,
review, or release meaning. Its only cross-family behavior is deciding whether
a saved observation remains local or is worth showing as a reusable decision
signal. That behavior already belongs to Knowledge Evolution:

- source-evidence chain;
- comparable-pattern check;
- applicability and non-applicability;
- contradictions and alternatives;
- confidence and unknowns;
- existing owner;
- rejection, deferral, or candidate disposition;
- non-promotion.

Therefore `editorial_learning_framework.md` should define the compact advisory
view and its safety rules. It must explicitly defer each signal's technical
meaning to the current owner.

This is not a new Learning Framework state or a new promotion route.

## Compact Evaluation Signal view

When a material task, release, or system decision would benefit, record the
smallest useful view inside an existing task, review, pattern, release, or
governance artifact.

Required information when material:

- decision question: what human judgment could this inform;
- observation: what was seen, without decision language;
- evidence pointers: exact saved artifacts, findings, validations, verdicts,
  or use records;
- scope and comparison window: which tasks/releases/contexts are included;
- denominator or exposure opportunity when a count/frequency is used;
- missing, excluded, or ambiguous cases;
- interpretation: what the evidence may indicate;
- contradictions and plausible alternative explanations;
- evidence confidence and unknowns;
- existing affected owner;
- optional human consideration: investigate, compare, verify, or consider an
  owner-scoped reviewed change;
- explicit non-decision: what does not happen automatically.

No standalone `evaluation-signals.md` artifact is required or introduced.

## Count and frequency safety

Counts and frequencies may appear only as descriptive evidence. They need a
bounded window, comparable population, and denominator/exposure opportunity
when those affect interpretation.

Allowed examples:

- "The pack was activated in 2 of 6 comparable security-sensitive tasks; use
  effect was beneficial once and unknown once."
- "The same owner-conflict warning appeared in three reviewed releases; one
  local cause was ruled out and one contradictory case remains."

Forbidden transformations:

- targets or thresholds;
- KPI or OKR use;
- composite or weighted scores;
- ranks or league tables;
- maturity bands or capability levels;
- individual/role performance measures;
- automatic acceptance, rejection, prioritization, retirement, or owner edits.

## Qualitative-only judgments

These may use supporting numbers but must stay evidence-backed qualitative
judgments:

- Domain Pack usefulness or maintenance justification;
- evidence sufficiency for a material decision;
- architecture drift and tradeoff significance;
- release value and realized improvement;
- whether repeated rejection indicates weak production or a strong gate;
- whether maintenance burden lacks enduring value;
- whether a learning candidate deserves canon;
- how contradictory signals affect the decision;
- release acceptance or changes requested.

## Materiality and optionality

Create a signal view only when all are true:

- a real Project Lead, review, governance, or owner decision question exists;
- material saved evidence exists;
- the view adds meaning beyond the source artifacts;
- interpretation can be bounded and reviewed;
- expected decision value exceeds capture and maintenance cost.

Otherwise do not create it. Absence of a view means no material signal was
recorded for that decision, not that the system is healthy, improving, or free
of risk.

## Noise rejection

Keep the proposed signal task-local, reject it, or defer it when:

- it is only an activity count;
- it lacks a comparison window or comparable population;
- task mix or exposure opportunity explains the apparent difference;
- source evidence cannot be reconstructed;
- it duplicates an existing owner record without adding decision value;
- missing cases or selection bias are material;
- an alternative explanation remains unexamined;
- the collection burden exceeds likely decision value;
- it seeks a score, target, rank, or automatic action.

## Contradictory signals

Do not average, vote, or select the convenient signal.

Record:

- each supported observation separately;
- whether the evidence applies to the same scope and decision question;
- differences in task mix, time window, exposure, source strength, or outcome;
- what remains unknown;
- what additional evidence would distinguish the explanations;
- whether the safest current disposition is local, deferred, rejected, or a
  bounded investigation.

Contradiction reduces decision confidence unless the difference is explained.
It does not create an automatic tie-break rule.

## Interaction with Learning

- A task-local signal stays task-local by default.
- A reusable claim uses existing Knowledge Evolution disposition.
- A repeated signal becomes a pattern candidate only after comparable evidence,
  scope, contradiction, owner, and review checks.
- A signal never becomes accepted canon by appearing in a Release Pack.
- A signal does not create a new learning state.
- `feedback_patterns.md` remains the only existing recurring pattern journal;
  it is not converted into a general telemetry database.

## Interaction with Review

Review Agent uses the existing review gate to check:

- decision question and affected owner are explicit;
- observation and interpretation are separated;
- counts have a comparable scope and denominator when material;
- source evidence is reconstructable;
- missing cases, selection bias, and alternative explanations are addressed;
- contradictions are preserved;
- confidence matches evidence;
- collection is proportionate;
- no score, KPI, target, rank, maturity level, or automatic action appears;
- signal language does not imply Project Lead or canonical-owner decisions.

This is one more material Knowledge Evolution/release review lens, not a new
gate or review cycle.

## Interaction with Project Lead decisions

The Release Pack gains an optional `Evaluation Signals` section because it is
the existing mandatory Project Lead review packet.

Allowed human considerations:

- investigate;
- compare with a bounded set;
- verify a stale or contradictory assumption;
- request more evidence;
- consider a separate owner-scoped reviewed change;
- take no action.

The view must not prescribe or perform:

- release acceptance or rejection;
- backlog or roadmap reprioritization;
- canon, memory, role, pipeline, template, Domain Pack, or capability change;
- capability or pack retirement;
- new review requirements.

## Exact implementation shape

### Canonical or active owner files

- `kb/editorial_learning_framework.md`
  - define the optional Evaluation Signal view, materiality, count safety,
    qualitative judgments, noise rejection, contradictions, owner routing, and
    Project Lead non-decision boundary;
  - connect signals to existing Knowledge Evolution disposition without new
    states.
- `agents/chief_editor.md`
  - add material signal-view assembly and existing-owner routing responsibility;
  - forbid automatic actions and mandatory signal production.
- `agents/review_agent.md`
  - add signal evidence, comparison, contradiction, proportionality, and
    non-decision challenge.
- `pipelines/review_pipeline.md`
  - add Evaluation Signal checks inside the existing Knowledge Evolution gate
    and compact review expectations; no new gate.
- `kb/feedback_patterns.md`
  - add bounded comparison window/denominator and Project Lead question fields
    to recurring pattern entries.
- `templates/release-pack.md`
  - add an optional material `Evaluation Signals` table for Project Lead review.
- `kb/00_index.md`
  - make the existing-owner integration discoverable without declaring a new
    framework or owner.
- `project-state.md`
  - record S5.R2 Release Candidate and the advisory-signal normalization.

### Strategic and operational state

- `ROADMAP.md`
  - normalize S5.R1 accepted and S5.R2 current Release Candidate.
- `BACKLOG.md`
  - move S5.R2 from `In Progress` to `Review`; keep S5.R3-S5.R5 not started.

### Validation and release support

- `tests/evaluation_signals_smoke_test.md`
  - validate the eight required scenarios and prove non-decision behavior.
- `tests/README.md`
  - register the manual smoke test.
- three required research/release artifacts;
- completed S5.R2 Release Pack;
- full task lifecycle artifacts;
- `/about` exact-copy and compact memory updates only as required by the memory
  package contract.

## Files intentionally not changed

- `AGENTS.md`: governance, role set, authority, and review gate are unchanged.
- `kb/capability_registry.md`: no new capability is introduced; existing
  evidence, Architecture Review, Knowledge Evolution, memory curation, and
  integrity checking are sufficient.
- `kb/editorial_evidence_framework.md`: evidence classes and confidence already
  support signal claims.
- `kb/architecture_review.md`: architecture risk and scenario guidance already
  supports drift observations.
- `kb/domain_knowledge_pack_standard.md`: S5.R1 already added activation versus
  actual-use effect evidence and explicit non-automation.
- `kb/task_object_model.md`: no new task-object field is needed.
- `kb/shared_lifecycle_kernel.md`: existing governance and memory curation
  touchpoints are sufficient.
- task statuses, pipelines, role set, and ordinary task templates: unchanged.
- Domain Pack files: no real use evidence justifies pack-specific edits.

## Representative scenario decisions

| Scenario | Valid signal treatment | Forbidden inference/action |
| --- | --- | --- |
| Repeated successful release | Compare accepted verdicts, validation, realized effects, and repairs; report supported reliability/value question | Auto-accept the next release or claim improvement from acceptance count alone |
| Repeated rejected release | Compare rejection reasons and repair outcomes; preserve strong-gate alternative | Auto-reject future work or infer declining quality from rejection count |
| Rare Domain Pack activation | Report bounded frequency, opportunity/task mix, effect evidence or unknown | Retire, downgrade, or rewrite activation rules automatically |
| Frequent Domain Pack activation | Report frequency plus actual benefit/burden/mixed/unknown effects | Declare the pack useful or mandatory from volume |
| Repeated architecture warning | Preserve drivers, scenarios, owner, comparable recurrence, contradictions | Change canon, create a gate, or assert drift without architecture context |
| Repeated stale knowledge | Verify source/owner and propose bounded correction investigation | Delete, retire, or sync memory automatically |
| Noisy metric | Reject activity count lacking outcome, denominator, comparability, or decision value | Put it in a scorecard, KPI, or release verdict |
| Contradictory signals | Keep both, compare scope/evidence, lower confidence, request distinguishing evidence | Average them, choose the convenient one, or automate a tie-break |

Synthetic cases validate contract behavior only. They do not confirm actual
system improvement, pack value, capability value, or architecture drift.

## Postponed

- automatic repository/task scanning;
- event collection or telemetry;
- trend computation;
- dashboarding;
- statistical inference or benchmarking;
- per-role or individual activity measurement;
- maturity assessment;
- automatic signal-to-proposal conversion;
- automatic action on canon, backlog, roadmap, memory, packs, or capabilities;
- broader Stage 5 task-need recognition reserved for S5.R4.

## Rejected

| Option | Reason |
| --- | --- |
| Evaluation score or health index | Collapses unlike evidence, hides tradeoffs, and invites target gaming. |
| KPI/OKR layer | Converts advisory evidence into incentives and targets forbidden by the mission. |
| Dashboard | Adds collection and maintenance cost without current evidence volume or decision need. |
| New Evaluation framework or canonical owner | Duplicates evidence, learning, architecture, Domain Pack, review, and release owners. |
| New Evaluation Agent | Existing roles already own assembly, evidence, challenge, and decisions. |
| New pipeline/stage/gate | Existing lifecycle and review gate are sufficient. |
| Mandatory signal artifact | Violates proportionality and artifact minimalism. |
| Maturity levels | Require a formal assessment model and ratings outside mission scope. |
| Automatic release/canon/backlog/roadmap/memory action | Violates Project Lead and canonical-owner authority. |

## Architecture impact

Impact: small.

The release adds one optional cross-owner view and associated role/review
consequences. It does not change architecture shape, authority, owner meaning,
capability registry, lifecycle, task status, role set, pipeline set, review
gate, task object, memory boundary, or Domain Pack authority.

## Evidence confidence

- Decision basis: repository inspection plus current primary/authoritative
  sources across engineering metrics, quality, architecture, observability,
  evaluation, improvement, maturity, product health, and AI evaluation.
- Confidence: `supported` for the architecture transfer; `verified` for current
  repository owner and mission constraints.
- Assumption: an optional view in existing artifacts will be sufficient for the
  Project Lead's near-term decision volume.
- Disconfirmation trigger: repeated real use shows critical signals cannot be
  reconstructed or reviewed without a dedicated owner or artifact.
- Residual risk: counts may still be misread as targets; explicit guardrails and
  review challenge mitigate but cannot eliminate human misuse.

## Release state decision

After implementation, validation, independent approval, and finalization:

- S5.R1 remains `Done` and accepted;
- S5.R2 moves from `In Progress` to `Review`;
- S5.R3 through S5.R5 remain `Not Started`;
- Project Lead acceptance for S5.R2 remains pending;
- the release must not be marked `Done` in this mission.
