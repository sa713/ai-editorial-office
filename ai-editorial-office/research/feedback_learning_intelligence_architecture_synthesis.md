# Feedback and Learning Intelligence Architecture Synthesis

Date: 2026-07-10

Release: `S5.R1 - Feedback and Learning Intelligence`

## Decision

Implement S5.R1 as a bounded integration between two existing owners:

- `kb/customer_feedback_loop.md` continues to own classification and immediate
  routing of actual post-delivery user/customer feedback;
- `kb/editorial_learning_framework.md` continues to own reusable learning,
  evidence and applicability checks, learning disposition, pattern
  confirmation, owner-scoped canon change, rejection, deferral, correction,
  supersession, retirement, and memory disposition.

No separate Feedback and Learning Intelligence capability, framework, store,
taxonomy, role, pipeline, lifecycle stage, review gate, or mandatory artifact
is needed.

The release adds an explicit bridge:

```text
actual feedback or observed completed-work outcome
-> feedback classification when applicable
-> evidence, affected-area, and applicability check
-> existing Knowledge Evolution disposition
-> existing review
-> bounded action routed to the existing owner
-> effect evidence before wider reuse
```

## Problem Being Solved

The repository already prevents automatic canon promotion, but its two owner
contracts are connected mostly by cross-reference. That leaves five practical
questions under-specified:

1. How does a classified feedback item enter Knowledge Evolution without
   turning feedback classification into a second learning taxonomy?
2. How can the system learn from completed-work outcomes when no customer
   feedback exists?
3. What evidence and applicability boundary confirms a pattern without an
   arbitrary score?
4. How does a candidate reach the correct canonical owner with a bounded,
   testable action rather than a vague improvement request?
5. How can real Domain Pack activation produce useful or negative learning
   evidence without mandatory telemetry or assuming activation equals value?

S5.R1 answers only these questions. It does not redesign Knowledge Evolution.

## Existing Coverage And Retained Owners

### Editorial Learning Framework

Already covered and retained:

- Knowledge Evolution states;
- source-evidence chain;
- reusable-learning and canonization criteria;
- observation-to-pattern promotion;
- task-local default;
- rejection and deferral;
- owner-first canon update;
- stale/conflicting knowledge challenge;
- correction, supersession, retirement, and `/about` disposition;
- existing Review Agent challenge.

S5.R1 extends this owner with a compact intake bridge, evidence-sufficiency
test, affected-area routing, bounded improvement candidate fields, and Domain
Pack effect evidence.

### Customer Feedback Loop

Already covered and retained:

- use only for actual reaction after delivery;
- optional task-local `feedback.md`;
- Chief Editor classification;
- classifications `task_local`, `preference`, `observation`,
  `confirmed_pattern`, and `system_change_candidate`;
- task-local revision/new-task boundaries;
- pattern/watchlist/backlog candidate routing;
- no automatic rule change.

S5.R1 does not add or rename classifications. It clarifies that classification
is followed by a separate, optional learning disposition when future reuse is
claimed.

### Feedback Patterns

Already covered and retained:

- one journal for recurring/significant patterns;
- maturity labels;
- no raw feedback archive;
- no automatic system change.

S5.R1 strengthens entry evidence, applicability, owner, and non-promotion
fields. It does not create another journal.

### Domain Knowledge Pack Standard

Already covered and retained:

- activation criteria and non-activation;
- activation note fields;
- sources, confidence, boundaries, stale-if triggers, and stop conditions;
- review, update, and retirement;
- no policy/capability/role authority.

S5.R1 adds optional effect evidence for actual use: specific sections used,
affected task decision/artifact/review, observed benefit or burden, confidence,
complexity cost, and learning disposition. The standard remains the activation
owner; the Learning Framework remains the reuse/disposition owner.

### Existing roles, lifecycle, task object, and review

Already sufficient:

- Chief Editor owns feedback classification and Knowledge Evolution routing;
- Review Agent challenges learning claims inside the existing review gate;
- task object exposes optional learning candidates, reusable patterns,
  post-task learning, and memory disposition;
- memory curation already exists in the shared lifecycle;
- task-local `feedback.md`, `review.md`, `final_decision.md`, and release reports
  can carry compact evidence.

No task-object field, stage, status, gate, or role is added. Role and Review
Pipeline text need only a concise consequence for the new bridge.

## Classification And Disposition Model

The two existing label sets remain separate because they answer different
questions.

| Decision | Owner | Question | Labels |
| --- | --- | --- | --- |
| Feedback classification | Customer Feedback Loop | What kind of post-delivery reaction is this, and what immediate route is safe? | `task_local`, `preference`, `observation`, `confirmed_pattern`, `system_change_candidate` |
| Learning disposition | Editorial Learning Framework | What, if anything, should future work preserve or change? | existing Knowledge Evolution states, including task-local, candidates, rejection, deferral, accepted canon, supersession, and retirement |

Default bridge guidance:

| Feedback classification | Default learning disposition | Boundary |
| --- | --- | --- |
| `task_local` | `task_local` | Current artifact correction or no action; no future-use claim by default. |
| `preference` | `task_local` or `learning_candidate` | Scope to the user/client/context; never a global rule merely because it repeats. |
| `observation` | `learning_candidate`, `deferred`, or `rejected` | Preserve only if evidence and future value justify maintenance. |
| `confirmed_pattern` | `pattern_candidate` | Confirmation means evidence supports recurrence/applicability; canon still requires a separate owner update. |
| `system_change_candidate` | `canon_update_candidate` or `deferred` | Name affected owner, bounded hypothesis, validation, and review; no automatic implementation. |

This is routing guidance, not a deterministic conversion table. Chief Editor
may choose a smaller disposition when evidence or scope is weak.

Observed completed-work outcomes without customer reaction enter directly at
the evidence/scope check and receive only a learning disposition. They are not
relabelled as customer feedback.

## Evidence And Scope Contract

When a signal is proposed for reuse, the smallest existing artifact should make
these fields reconstructable:

- source signal: exact feedback, observed outcome, review finding, validation,
  repository conflict, or Domain Pack use;
- evidence pointer: task/artifact/section/commit/source link;
- observed outcome: what changed, succeeded, failed, or remained unknown;
- affected system area: current artifact, user/client preference, role,
  pipeline, template, KB/canonical owner, Domain Pack, validation, or memory;
- learning claim: what future work might do or understand differently;
- applicability scope: where the claim holds and explicit non-applicability;
- corroborating and contradicting signals;
- confidence and unknowns;
- classification when it is actual customer feedback;
- learning disposition;
- existing owner and proposed bounded action;
- review path and non-promotion statement.

These are conditional information fields, not mandatory task-object fields or
a new standalone artifact.

## Pattern Confirmation Without Scoring

A pattern is confirmed only when a reviewer can answer yes to all material
questions:

1. Are the source signals saved and reconstructable?
2. Do they describe the same underlying condition rather than similar wording?
3. Is the affected scope explicit and broader than one artifact, unless a
   high-impact exception applies?
4. Is there corroboration across comparable tasks, releases, reviews,
   validations, or contexts, or a single high-impact event with direct causal
   evidence and material future risk?
5. Were plausible local causes, preferences, contradictions, and alternative
   explanations considered?
6. Is the candidate useful enough to maintain?
7. Is an existing owner and review path clear?

No numeric minimum is canonical. Counts can support but cannot decide. A
single anecdote normally remains `task_local`, `deferred`, or `rejected`. The
high-impact exception still requires bounded applicability, strong evidence,
owner, and review, and still cannot auto-promote.

## Bounded Improvement Contract

When learning suggests a system change, use the existing system-change
proposal shape or a compact equivalent in a release/task artifact. The proposal
should name:

- problem signal and learning disposition;
- evidence and counterevidence;
- affected canonical owner;
- change hypothesis and expected effect;
- smallest change surface and non-goals;
- responsible owner;
- validation or comparable future-use check;
- side effects, stop condition, and correction/revert path;
- review and Project Lead boundary.

This makes a proposal executable and falsifiable without adding an improvement
pipeline. Accepted canon exists only after the reviewed owner file is actually
changed and validated.

## Domain Pack Use Evidence

### Capture trigger

Capture Domain Pack effect evidence only when:

- a pack was actually activated in a task; and
- use materially affected evidence, terminology, risk, review, output quality,
  task cost, or complexity; or
- a reviewer needs to record that activation had no demonstrated value.

No effect note is required for every activation. The absence of evidence means
`unknown`, not positive or negative.

### Compact fields

- active pack and activation reason;
- sections/sources actually used;
- affected decision, artifact, evidence depth, terminology, risk handling, or
  review finding;
- observed effect: `beneficial`, `burdensome`, `mixed`, or `unknown`;
- evidence pointer and confidence;
- unnecessary context/complexity or maintenance cost;
- alternative explanation/counterfactual limit;
- learning disposition and existing owner if action is proposed.

These are observation values, not a score or a new taxonomy. They may be plain
language in an existing task artifact.

### Routing

- A beneficial one-off use is normally a `learning_candidate` for comparable
  future testing, not a confirmed pattern.
- An unnecessary-complexity use is normally task-local or a routing/activation
  `learning_candidate`.
- Repeated comparable signals may become a `pattern_candidate`.
- A pack-content or activation-rule change becomes an owner-scoped
  `canon_update_candidate` only after evidence and review.
- Pack changes route to the specific pack or Domain Knowledge Pack Standard as
  appropriate; they do not change automatically.

## Exact Implementation Shape

### Canonical or active owner files

- `kb/editorial_learning_framework.md`
  - add the feedback/outcome intake bridge;
  - add evidence/applicability and pattern-confirmation checks;
  - add owner-scoped bounded improvement and Domain Pack use evidence.
- `kb/customer_feedback_loop.md`
  - preserve classification;
  - add evidence/scope and optional learning-disposition handoff;
  - clarify outcome-only signals route directly to the Learning Framework;
  - add rejection/deferral boundary without making them feedback labels.
- `kb/feedback_patterns.md`
  - strengthen entry fields for evidence, applicability, affected area,
    disposition, owner, contradictions, and non-promotion.
- `kb/domain_knowledge_pack_standard.md`
  - add optional actual-use effect evidence and review consequence.
- `agents/chief_editor.md`
  - add one linked classification/disposition/owner-routing responsibility.
- `agents/review_agent.md` and `pipelines/review_pipeline.md`
  - challenge feedback/outcome learning claims and Domain Pack effect claims
    inside the existing Knowledge Evolution and Domain Pack checks.
- `project-state.md`
  - represent the S5.R1 release candidate and normalization decision only.

### Templates and discoverability

- `templates/artifacts/feedback_template.md`
  - add evidence, affected-area, learning-disposition, owner, Domain Pack, and
    non-promotion fields.
- `templates/artifacts/system_change_proposal_template.md`
  - add evidence/counterevidence, owner, bounded hypothesis, validation, and
    stop/revert fields.
- `kb/00_index.md`
  - clarify the two-owner integration without defining duplicate rules.

### Non-canonical support

- required research, synthesis, release report, release pack, and task-local
  lifecycle artifacts;
- one manual smoke test covering all nine mission cases;
- `tests/README.md` registration;
- `/about` exact-copy and compact-summary synchronization.

## Files Intentionally Not Changed

- `AGENTS.md`: ownership and authority are already correct.
- `kb/capability_registry.md`: existing Memory Curation and Knowledge
  Evolution capabilities already cover the behavior.
- `kb/task_object_model.md`: existing optional learning fields are sufficient.
- `kb/shared_lifecycle_kernel.md`: existing memory curation and review touchpoints
  are sufficient.
- task statuses and pipeline set: no lifecycle change is needed.
- Domain Pack files: no real ordinary-task evidence supports pack-specific
  changes yet.
- `feedback_loop.md`: compatibility entry already points to the active workflow
  and the feedback classification remains unchanged.

## Representative Case Disposition

The nine mission cases will be validated in a manual smoke test. The test must
show classification, evidence treatment, affected owner, learning disposition,
and non-promotion for each case. Synthetic cases verify decision logic but do
not themselves confirm a reusable pattern.

Expected high-level results:

1. wording correction -> `task_local`, current artifact owner;
2. repeated user preference -> `preference`, user/client scope, candidate at
   most;
3. recurring workflow failure -> evidence-backed `confirmed_pattern` plus
   owner-scoped system-change candidate;
4. successful reusable pattern -> learning/pattern candidate before canon;
5. unsupported negative feedback -> reject or defer, no system change;
6. beneficial Domain Pack activation -> learning candidate with effect
   evidence, no automatic pack promotion;
7. burdensome Domain Pack activation -> task-local or learning candidate routed
   to activation/pack owner, no automatic removal;
8. one-anecdote system change -> deferred or rejected;
9. stale learning -> evidence-backed correction, supersession, or retirement
   candidate routed to the current owner.

## Postponed

- automated task scanning or trend detection;
- feedback dashboards, health scores, confidence scores, or pattern counters;
- mandatory post-task retrospectives or scheduled learning ceremonies;
- automatic Domain Pack use telemetry;
- automatic backlog, roadmap, canon, `/about`, or model updates;
- memory hygiene intelligence beyond S5.R1-required synchronization;
- evaluation-signal design reserved for S5.R2;
- task-need/pack activation optimization reserved for later evidence and S5.R4;
- new Domain Pack content or structure changes without real use evidence.

## Rejected

| Option | Reason |
| --- | --- |
| New `feedback_learning_intelligence.md` owner | Duplicates the Customer Feedback Loop and Editorial Learning Framework. |
| One combined classification taxonomy | Conflates immediate feedback meaning with future learning disposition. |
| New learning database or pattern store | `feedback_patterns.md`, task artifacts, and canonical owners already provide the needed storage. |
| New Feedback/Learning Agent | Existing roles already own classification, evidence support, review, and governance. |
| New review gate or lifecycle stage | Existing review and memory curation touchpoints are sufficient. |
| Mandatory retrospective for every task | Produces noise and violates artifact minimalism. |
| Score-based signal quality | Evidence volume and context do not support a valid general score. |
| Automatic canon or model adaptation | Violates human/canonical-owner authority and the mission. |
| Treat Domain Pack activation as proof of value | Confuses use with outcome and contradicts the Stage 4 evidence gap. |

## Architecture Impact

Impact: small.

The release changes guidance and templates inside existing ownership. It does
not change architecture shape, governance authority, task status, lifecycle,
role set, pipeline set, review gate, memory boundary, or Domain Pack authority.

## Release State Decision

After implementation, validation, and independent approval:

- S5.R1 moves from `Not Started` to `Review`;
- Stage 5 becomes active with S5.R1 as its current release candidate;
- S5.R2 remains `Not Started`;
- Project Lead acceptance remains pending;
- the release must not be marked `Done` in this mission.
