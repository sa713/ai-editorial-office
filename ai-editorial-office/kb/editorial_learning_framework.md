# Editorial Learning & Knowledge Evolution Framework

This file is the canonical owner for reusable learning, canonization criteria,
learning extraction, Knowledge Evolution, canon evolution, stale-knowledge
challenge, and canon retirement in AI Editorial Office.

It makes the system stronger after completed work without creating uncontrolled
memory sprawl. It is not a memory database, retrospective ritual, new role,
workflow engine, review gate, or automatic documentation generator.

## Purpose

Editorial work can produce knowledge that should help future tasks. Most task
details should remain task-local. This framework decides what is worth keeping,
where it belongs, whether it has become a reusable pattern, how stale guidance
is challenged, and how canon is updated or retired safely.

Good learning answers:

- what pattern, decision, context, failure, or correction should be reusable;
- what evidence proves it is durable enough to preserve;
- what should stay task-local;
- what existing canonical owner should change, if any;
- what duplicated, stale, or obsolete assumption should be challenged;
- how future agents will know when to use or ignore the learning.

Learning is extracted after work is grounded in artifacts, review, feedback,
or repeated evidence. It is not inferred from model memory or one attractive
example.

## Knowledge Evolution Capability

Knowledge Evolution is the bounded capability for moving saved experience
through deliberate knowledge states:

```text
task-local observation
->
learning candidate
->
pattern candidate
->
canon-update candidate
->
reviewed owner update, deferral, rejection, correction, or retirement
```

It strengthens the existing Learning Framework. It does not create a separate
knowledge base, separate canon owner, new lifecycle stage, new role, mandatory
artifact, or automatic promotion path.

Use Knowledge Evolution when work produces a material signal such as:

- a completed task or release exposes reusable learning;
- multiple tasks show the same pattern, failure, exception, or safeguard;
- review identifies a repeated or high-risk finding;
- repository state contradicts current guidance;
- a canonical owner is duplicated, stale, missing, or ambiguous;
- source freshness, provenance, or client-profile status affects future work;
- `/about` needs synchronization after canonical changes;
- outdated guidance should be corrected, deprecated, superseded, or retired.

The default result is no canon change. A useful task-local note remains useful
even when it never becomes canon.

## Knowledge Disposition States

When learning disposition is material, classify it with the smallest useful
state:

| State | Meaning | Default location |
| --- | --- | --- |
| `task_local` | Useful only for the current task, artifact, or user exchange. | Current task artifact, `feedback.md`, `final_decision.md`, or `status.md` |
| `learning_candidate` | May be reusable, but evidence or scope is not yet strong enough. | Review, final decision, feedback, implementation report, or release report |
| `pattern_candidate` | Repeated or high-likelihood signal worth watching across tasks. | `kb/feedback_patterns.md`, release report, or task-local note |
| `canon_update_candidate` | A clear owner file may need a reviewed change. | System update task, release report, or final decision |
| `accepted_canon` | Reviewed owner-file change has been made and validated. | Canonical owner file |
| `superseded` | Old guidance is replaced by newer guidance and should point to it when future readers may encounter the old path. | Canonical owner or task-local version pointer |
| `retired` | Guidance should no longer be used and no replacement is needed or available. | Canonical owner, final decision, or release report |
| `rejected` | Candidate failed evidence, owner, scope, privacy, duplication, or maintenance checks. | Existing task/review/release artifact |
| `deferred` | Candidate may matter later, but current evidence or release scope is insufficient. | Existing task/review/release artifact |

These states are labels for decision clarity, not operational task statuses.
They do not change `/kb/task_statuses.md`.

## Feedback And Outcome Intake

Feedback and observed outcomes enter this framework through existing owners;
they do not create a second feedback workflow.

- Actual user or customer reaction after delivery is first classified through
  `/kb/customer_feedback_loop.md`.
- A completed-task or release outcome without customer reaction enters this
  framework directly as an observed outcome. Do not relabel it as customer
  feedback.
- Review findings, validation results, repository conflicts, and real Domain
  Knowledge Pack use may also be source signals when future use is material.

Use two linked decisions when actual feedback may matter beyond the current
exchange:

1. Feedback classification: what kind of reaction is this and what immediate
   route is safe?
2. Learning disposition: what, if anything, should future work preserve,
   test, reject, defer, correct, retire, or route to an existing owner?

Feedback classification remains owned by the Customer Feedback Loop. Knowledge
disposition remains owned here. Do not merge the two label sets.

Default bridge guidance:

| Feedback classification | Default learning disposition | Boundary |
| --- | --- | --- |
| `task_local` | `task_local` | Correct the current artifact, clarify, open a new task when scope changed, or take no action. |
| `preference` | `task_local` or `learning_candidate` | Keep user, customer, and context scope explicit; repetition does not make it global policy. |
| `observation` | `learning_candidate`, `deferred`, or `rejected` | Preserve only when evidence and future value justify maintenance. |
| `confirmed_pattern` | `pattern_candidate` | Confirmation supports recurrence and applicability, not automatic canon. |
| `system_change_candidate` | `canon_update_candidate` or `deferred` | Name the existing owner, bounded hypothesis, validation, and review path. |

This table is routing guidance, not automatic conversion. Chief Editor should
choose the smallest safe disposition supported by the evidence.

### Compact Signal Record

When a future-use or system-change claim is material, make these facts
reconstructable in the smallest existing task, review, feedback, implementation,
or release artifact:

- source signal: feedback, observed outcome, review finding, validation,
  repository conflict, or Domain Pack use;
- evidence pointer: task, artifact, section, commit, validation output, or
  source link;
- observed outcome: what improved, failed, changed, or remained unknown;
- affected system area: current artifact, user/client preference, role,
  pipeline, template, KB/canonical owner, Domain Pack, validation, or memory;
- learning claim and applicability scope, including where it does not apply;
- corroborating, contradicting, or alternative explanations;
- confidence, unknowns, and validation still needed;
- feedback classification when the source is actual customer feedback;
- learning disposition, existing owner, proposed bounded action, and review
  path;
- explicit non-promotion state: what does not change automatically.

These are conditional information fields, not new required task-object fields,
a mandatory learning artifact, or a retrospective form.

### Evidence And Scope Check

Before any disposition beyond `task_local`, ask:

- Can the source signal and observed outcome be reconstructed?
- Does the evidence support the learning claim rather than only the reaction?
- Is the affected area and applicability boundary explicit?
- Are similar signals genuinely comparable?
- Were contradictions, local causes, preference-only explanations, and
  alternative explanations considered?
- Is the future value or risk high enough to justify maintenance?
- Is an existing owner and review path clear?

Do not compute a general signal score. Counts, ratings, and sentiment may
support judgment but cannot replace evidence, context, applicability, owner, or
review. If the check is weak, keep the signal local, reject it, or defer it.

## Advisory Evaluation Signal View

Evaluation Signals make selected evidence visible for a material Project Lead,
review, governance, or canonical-owner decision. They are an optional view over
saved evidence, not a new evaluation framework, capability, taxonomy, store,
dashboard, telemetry layer, task status, artifact, review gate, or promotion
path.

The view preserves three separate layers:

```text
saved observation or measurement
-> contextual interpretation
-> accountable human decision
```

It may raise a question, support an investigation, or expose a pattern. It
never accepts or rejects a release, changes canon, reprioritizes backlog or
roadmap, modifies memory, retires a capability or Domain Pack, or changes any
owner automatically.

### When A View Is Useful

Create the view inside the smallest existing task, review, pattern, release, or
governance artifact only when:

- a real decision question exists;
- material saved evidence exists;
- the view adds decision value beyond the source artifacts;
- the interpretation can be bounded and reviewed;
- expected value exceeds capture and maintenance cost.

No view is required for every task or release. Absence means no material signal
was recorded for that decision, not that the system is healthy, improving, or
free of risk.

### Compact Evaluation Signal Record

When material, make these facts reconstructable:

- decision question: which human judgment this may inform;
- observation: what was seen, without decision language;
- evidence pointers: exact tasks, findings, validations, verdicts, use records,
  sections, or commits;
- scope and comparison window: which tasks, releases, or contexts are included;
- denominator or exposure opportunity when a count or frequency is used;
- missing, excluded, or ambiguous cases;
- interpretation: what the evidence may indicate;
- contradicting evidence and plausible alternative explanations;
- confidence, unknowns, and evidence still needed;
- existing affected owner;
- optional human consideration: investigate, compare, verify, request evidence,
  consider an owner-scoped reviewed change, or take no action;
- explicit non-decision: what does not happen automatically.

These are conditional information fields, not required task-object fields or a
mandatory `evaluation-signals.md` artifact.

### Existing Signal Owners

The view does not redefine the underlying evidence:

| Signal question | Existing owner or evidence surface |
| --- | --- |
| Capability activation frequency | Task manifests and orchestration plans for activation evidence; `capability_registry.md` for capability meaning |
| Domain Pack usefulness | `domain_knowledge_pack_standard.md`, the active pack, and actual-use effect evidence |
| Recurring review findings | Review Agent and Review Pipeline for findings; this framework and `feedback_patterns.md` for reusable recurrence |
| Recurring architecture issues | `architecture_review.md` for drivers, quality scenarios, tradeoffs, and risks |
| Evidence quality trends | `editorial_evidence_framework.md` for evidence classes, confidence, assumptions, and unknowns |
| Learning promotion trends and stale knowledge | this framework for disposition, pattern confirmation, correction, supersession, retirement, and owner routing |
| Release quality observations | review, validation, final decision, release report, Release Pack, and Project Lead verdict |
| Maintenance-cost observations | saved task/release evidence and the affected canonical owner; this framework when reuse or change is proposed |

### Count And Frequency Safety

Counts and frequencies may be descriptive evidence only. Use a bounded window,
comparable population, and denominator or exposure opportunity when those
affect interpretation. Preserve missing cases and task mix.

Do not convert counts into:

- targets, thresholds, KPIs, or OKRs;
- composite or weighted scores;
- ranks, league tables, or individual performance measures;
- maturity bands or capability levels;
- automatic acceptance, rejection, prioritization, retirement, promotion, or
  owner changes.

Capability or Domain Pack activation frequency does not prove usefulness.
Frequent activation may be beneficial, burdensome, mixed, or unnecessary. Rare
activation may reflect low value, limited opportunity, correct non-activation,
or a rare high-risk need. Actual effect and task context remain necessary.

### Qualitative Judgments

Keep these judgments qualitative even when supporting counts exist:

- Domain Pack usefulness or maintenance justification;
- evidence sufficiency for a material decision;
- architecture drift and tradeoff significance;
- release value and realized improvement;
- whether repeated rejection indicates weak production or a strong gate;
- whether maintenance burden lacks enduring value;
- whether a learning candidate deserves canon;
- how contradictory signals affect a decision;
- release acceptance or changes requested.

### Noise And Contradiction

Keep the proposed signal local, reject it, or defer it when it is only an
activity count, lacks comparable scope, cannot be reconstructed, hides missing
cases or selection bias, duplicates an owner record without adding decision
value, ignores a plausible alternative explanation, costs more to maintain than
it can inform, or seeks a forbidden score or automatic action.

When signals conflict, preserve each supported observation separately. Compare
scope, time window, exposure opportunity, source strength, task mix, and
outcome. Record what additional evidence could distinguish the explanations.
Do not average contradictions, vote between them, or choose the convenient
signal. Unresolved contradiction reduces confidence and usually supports
further evidence, deferral, rejection, or no action.

### Project Lead And Review Boundary

Chief Editor may assemble a material view from saved evidence and route it to
the existing owner. Review Agent challenges evidence, comparability,
denominator, missing cases, alternatives, contradictions, confidence,
proportionality, and non-decision language inside the existing review gate.

Project Lead or the existing canonical owner decides whether to investigate,
request evidence, make a separate reviewed change, or take no action. An
Evaluation Signal never supplies or performs that decision.

If a signal is proposed for reuse, apply the existing Knowledge Evolution
disposition and pattern-confirmation rules. Appearance in a Release Pack does
not promote it to a pattern or canon.

## Source-Evidence Chain

Reusable learning should remain traceable to saved evidence. Before promotion,
identify:

- source signal: task, release, feedback pattern, review finding, repository
  inspection, source-freshness issue, validation result, or governance decision;
- evidence pointer: file path, section, review finding, commit, validation
  output, or source link;
- learning claim: what future work should know or do differently;
- scope: where it applies and where it does not;
- owner: existing canonical owner or reason no owner exists;
- disposition: keep local, watch, update canon, correct, retire, reject, or
  defer;
- review path: where independent review or governance approval happens.

If the source-evidence chain cannot be reconstructed, the learning must remain
task-local or be rejected until evidence is available.

## What Counts As Reusable Learning

Reusable learning is worth preserving when it can improve future decisions,
reduce risk, prevent repeated failures, improve implementation quality, or save
future agents from rediscovering the same pattern.

| Learning type | Preserve when |
| --- | --- |
| Task pattern | A recurring task shape, artifact packet, or handoff pattern appears likely to repeat. |
| Client/project context | A verified client, project, repository, or domain constraint will matter in future tasks. |
| Successful workflow | A compact or expanded route worked well and can guide similar future tasks. |
| Failure pattern | A mistake, near miss, or repeated blocker should become a safeguard or warning sign. |
| Decision precedent | A route, tradeoff, or governance decision is likely to recur under similar conditions. |
| Evidence pattern | A source class, validation method, or evidence limit should guide future confidence decisions. |
| Quality pattern | A quality attribute or tradeoff repeatedly affects task success. |
| Implementation pattern | A repository-aware implementation slice, validation pattern, or file-boundary decision should be reused. |
| Review finding | A repeated or high-risk review finding should become a prevention rule or review focus. |
| Prompt/process improvement | A Codex or role instruction improves execution enough to reuse, without becoming process noise. |
| Canon correction | Existing canon is wrong, duplicated, stale, ambiguous, or missing an owner. |

## From Observation To Pattern

Temporary observations become reusable patterns only after one of these
thresholds is met:

- repeated signal across tasks, reviews, feedback, releases, or validations;
- one high-impact finding that would materially reduce future risk;
- clear repository-state evidence that makes old guidance unsafe;
- clear source/provenance evidence that changes future confidence;
- Project Lead or Chief Editor decision that a pattern should be watched or
  promoted through reviewed owner update.

Pattern confirmation also requires that saved signals describe the same
underlying condition rather than only similar wording, that applicability and
non-applicability are visible, and that contradictions or plausible local
causes were considered.

No numeric minimum confirms a pattern. Repeated comparable evidence is the
normal path. One high-impact event may justify a reviewed exception only when
causal evidence, material future risk, bounded applicability, owner, and review
are explicit. The exception still produces a candidate, not automatic canon.

Pattern candidates should name applicability boundaries. Do not generalize from
one task merely because the reaction is strong or the proposed improvement is
attractive.

## What Should Not Be Canonized

Do not promote:

- one-off task details;
- unverified assumptions;
- temporary preferences;
- obsolete project state;
- duplicate wording already owned by another canonical file;
- low-value process narration;
- private source material or sensitive client content without explicit scope;
- old task-folder structure as a template;
- model memory, chat impressions, or unsaved notes;
- a single user reaction as a global rule.

If the learning is useful only for the current task, keep it in `feedback.md`,
`final_decision.md`, `status.md`, or the relevant task artifact instead of
changing canon.

## Canonization Criteria

Learning may become canonical knowledge when most of these are true:

- repeated usefulness or strong future likelihood;
- high future value;
- verified by saved evidence, reviewed artifacts, repository inspection, or
  confirmed feedback pattern;
- applies beyond one artifact or one task-local draft;
- reduces future risk;
- improves decision quality;
- prevents a known failure mode;
- has a clear canonical owner;
- can be stated concisely without duplicating existing canon.

Reject canonization when the candidate is:

- one-off detail;
- unverified assumption;
- temporary preference;
- obsolete state;
- duplicate of existing canon;
- lower value than the maintenance cost;
- process noise;
- too broad to review;
- not traceable to artifacts or evidence.

## Learning Extraction Pattern

Use this lightweight pattern at governance closure, memory curation, feedback
classification, review of a system update, or after a Codex implementation when
learning is material.

1. What worked?
2. What failed or nearly failed?
3. What decision should be reusable?
4. What context should persist?
5. What pattern should future agents recognize?
6. What canon should be updated, if any?
7. What should remain task-local?
8. What assumption, source, pattern, or rule became stale?
9. What evidence supports promotion, deferral, or rejection?

Record the answer in the smallest existing artifact. A compact final decision,
feedback note, review finding, or implementation report is enough unless a
separate reviewed canon update is required.

## Validation Before Promotion

Before learning changes canon, check:

- source: which artifact, review, feedback pattern, commit, or repository
  inspection supports it;
- evidence chain: whether future reviewers can trace the learning back to the
  saved source signal;
- scope: where the learning applies and where it does not;
- owner: which canonical file should own the rule;
- duplication: whether the rule already exists elsewhere;
- conflict: whether it changes lifecycle, roles, review gate, statuses, or
  authority boundaries;
- privacy: whether the learning contains private or source-only material;
- maintenance: whether future agents can use it without more process weight.

If validation is weak, keep the item task-local, mark it as a candidate, or
request a separate reviewed system-update mission.

## Owner-Scoped Improvement Candidates

When learning suggests a system change, use the existing
`system_change_proposal_template.md` or a compact equivalent in an existing
task/release artifact. Name:

- problem signal and learning disposition;
- evidence, counterevidence, and applicability;
- affected canonical owner;
- change hypothesis and expected effect;
- smallest change surface and explicit non-goals;
- responsible owner;
- validation or comparable future-use check;
- side effects, stop condition, and correction or revert path;
- review path and Project Lead boundary when applicable.

The proposal is not implementation authority. Canon is `accepted_canon` only
after the correct owner file is reviewed, changed, and validated. A backlog,
roadmap, `/about`, Domain Pack, role, pipeline, template, or model behavior does
not change merely because a candidate exists.

## Canon Evolution Rules

Canon changes should be deliberate, small, and owned.

### Adding New Canon

- Choose the canonical owner first.
- Prefer updating an existing owner over creating a new file.
- Create a new canonical file only when no existing owner fits.
- State the rule concisely and link to related owners instead of copying their
  content.
- Preserve traceability to the reason for the update when the change is not
  self-evident.

### Updating Existing Canon

- Patch the owner file, not every file that mentions the topic.
- Update references only where discoverability or role behavior requires it.
- Keep task-local examples task-local unless they are generalized.
- Run the relevant validation checks before committing.

### Deprecating Or Retiring Canon

- Mark stale assumptions, retired paths, or deprecated patterns explicitly.
- Replace outdated guidance with the current owner or stop condition.
- Do not delete historical artifacts merely to clean the narrative.
- Preserve enough context for future agents to understand why the rule changed.
- Prefer `superseded` when newer guidance replaces old guidance.
- Prefer `retired` when the guidance should no longer be used and no replacement
  is needed.
- Prefer `correction` when the guidance remains valid but factual, path,
  source, owner, or scope details were wrong.
- Prefer `deferred` when the concern is plausible but not yet evidenced enough
  for canon change.

### Avoiding Duplication

- Do not copy checklists across files.
- Do not create parallel owners for lifecycle, roles, statuses, evidence,
  planning, audience, quality, or review.
- If two files appear to own the same rule, stop and route the conflict through
  Chief Editor or a reviewed system update.

### Keeping Canon Concise

- Durable principle belongs in canon.
- Task-specific evidence belongs in the task folder.
- Raw feedback belongs in `feedback.md`.
- Repeated feedback patterns belong in `/kb/feedback_patterns.md`.
- Public memory export belongs in `/about`; `/about` is not canon.

## Stale Or Conflicting Knowledge Challenge

Challenge stale or conflicting knowledge when:

- a rule conflicts with current repository state;
- a client/project source is stale, missing, or contradicted;
- a repeated review finding shows the current rule is insufficient;
- a canonical owner duplicates another owner;
- a path, template, role, or lifecycle assumption no longer matches the active
  system;
- a task repeatedly needs an exception to succeed;
- `/about` diverges from canonical files or compact summaries;
- a rule depends on words such as `new`, `latest`, `current`, or `temporary`
  without a date, version, or current-version pointer;
- source links, file paths, role names, statuses, or validation commands no
  longer resolve.

The recovery is not immediate deletion. Record the concern, identify the owner,
verify evidence, and update, deprecate, or retire through a reviewed change when
the evidence is sufficient.

### Triage Outcomes

| Outcome | Use when |
| --- | --- |
| `no_change` | Concern was checked and current canon still holds. |
| `task_local_caveat` | Concern affects only the current task. |
| `watch_pattern` | Concern is plausible and should be tracked but not promoted yet. |
| `owner_patch` | Existing canonical owner needs a bounded reviewed update. |
| `supersede` | Old guidance should point to replacement guidance. |
| `retire` | Guidance should stop being used. |
| `block` | Safe continuation depends on resolving the stale/conflicting rule. |

Use the smallest outcome that protects future work.

## Learning From Actual Domain Pack Use

Domain Knowledge Pack activation remains owned by
`/kb/domain_knowledge_pack_standard.md`. This framework owns any reusable
learning disposition produced by actual pack use.

Capture a compact effect note only when a pack was actually activated and its
use materially affected evidence depth, terminology, risk handling, review,
output quality, task cost, or complexity, or when a reviewer needs to record
that no value was demonstrated. Use an existing task artifact.

When material, record:

- active pack, activation reason, and sections or sources actually used;
- affected decision, artifact, evidence, terminology, risk treatment, or
  review finding;
- observed effect: beneficial, burdensome, mixed, or unknown;
- evidence pointer, confidence, and alternative explanation;
- unnecessary context, complexity, or maintenance cost;
- learning disposition and existing owner if action is proposed.

These are plain-language observations, not a score or a new taxonomy. No note
is mandatory for every activation. Absence of effect evidence means `unknown`,
not success.

A useful one-off activation normally becomes a `learning_candidate` for a
comparable future task. Unnecessary complexity normally stays task-local or
becomes a routing/activation learning candidate. Repeated comparable evidence
may become a `pattern_candidate`. Pack content or activation rules change only
through a reviewed update to the specific pack or Domain Knowledge Pack
Standard; use does not modify a pack automatically.

## Memory Hygiene Intelligence And `/about` Disposition

Memory Hygiene Intelligence is the bounded Knowledge Evolution behavior for
keeping external project memory accurate, compact, useful, synchronized, and
non-canonical. It refines the existing Memory Curation, stale-knowledge, and
Integrity Checking capabilities. It is not a new capability, owner, role,
pipeline, lifecycle stage, review gate, memory store, synchronization engine,
or automatic documentation process.

`/about` is the external memory package. Repository canon remains
authoritative. A memory fact is valid only as an exact copy or reviewed compact
summary derived from current canonical sources. If memory and canon conflict,
stop relying on the memory fact and repair memory from canon. Never change
canon merely to match memory.

### Bounded Flow

```text
canonical change or saved memory-hygiene signal
-> identify canonical source and evidence
-> materiality, purpose, sensitivity, and continuing-value check
-> exact-copy | compact-summary | correct | compress | retire |
   omit | defer | no-sync
-> branch-appropriate validation
-> independent review
-> explicit manual memory update or preserved no-change
```

A canonical change is a reason to check disposition, not permission to write
memory. Most commits do not require memory synchronization.

### Sync Triggers

Apply the disposition check when material evidence shows one of these:

- a canonical file mapped as an exact copy changes;
- accepted or current release state, active phase, next action, or approval
  state changes and external memory represents it;
- canonical roles, authority, lifecycle, supported features, memory-package
  usage, or critical constraints change in a way external memory users need;
- the package mapping, file-count contract, or validation contract changes
  through a reviewed update;
- the memory-package checker reports a mismatch or missing package file;
- repository inspection, review, saved feedback/outcome evidence, or a material
  Evaluation Signal reports stale, contradictory, duplicated, bloated,
  sensitive, or misleading memory;
- temporary Release Candidate or transition state becomes accepted, rejected,
  superseded, or obsolete;
- a source path, role, status, validator, current-version statement, or summary
  boundary no longer resolves or remains accurate.

Time alone is a review signal, not proof that a fact is stale. Repository
contradiction, changed source meaning, or expired purpose establishes the need
for repair.

### No-Sync And Omission Triggers

Choose `no-sync` or `omit` when:

- the change is internal research, task evidence, test detail, draft history,
  implementation narration, or another repository-only artifact;
- no fact represented in external memory changed;
- an existing summary remains accurate and sufficient for external use;
- temporary detail would create churn without durable external-memory value;
- content is private, sensitive, client-specific, credential-bearing,
  source-restricted, security-sensitive, or task-local;
- the proposed fact duplicates existing memory or canon without adding useful
  orientation;
- maintenance, bloat, privacy, or misuse risk exceeds continuing external
  value;
- evidence, canonical state, authorization, or safe summary wording is not yet
  sufficient, in which case `defer` may be safer than a final omission.

`no-sync` is an explicit disposition after a materiality check, not a skipped
check. Record it in an existing `final_decision.md`, release report, Release
Pack, review, or implementation report only when the decision matters for
governance, auditability, or restart. Do not create a per-commit memory log.

### Memory Dispositions

Use the smallest supported disposition:

| Disposition | Use when | Evidence and result |
| --- | --- | --- |
| `exact-copy` | The active package intentionally exposes an operational file whose wording must match canon. | Name the canonical path and copy mapping; replace the package copy from the source and verify byte identity. |
| `compact-summary` | External memory needs durable orientation, state, or boundaries but not the full owner file. | Name the canonical source set; preserve material meaning in an existing summary and verify it semantically. |
| `correct` | Memory is factually wrong, stale, contradictory, or misstates scope, authority, certainty, or status. | Cite current canon; remove the wrong claim and replace it only with source-supported meaning. |
| `compress` | Useful memory is verbose, repeated, fragmented, or crowded by lower-value detail. | Consolidate at the strongest existing location; preserve unique scope, caveats, and source pointers while reducing repetition. |
| `retire` | Content is obsolete, superseded, misleading, or has no continuing external-memory value. | Remove or replace it from active memory; keep meaningful history and rationale in repository artifacts. |
| `omit` | Content is repository-only, raw, temporary, task-local, sensitive, private, or externally unnecessary. | Keep it out of memory; verify that no required external context is lost. |
| `defer` | Source, evidence, approval, accepted state, safe wording, or contradiction resolution is incomplete. | Make no speculative change; record the unresolved issue and next verification when material. |
| `no-sync` | Canon changed but external facts and the package contract remain accurate and sufficient. | Leave memory unchanged after checking the affected representation; record rationale only when material. |

These labels improve decision clarity. They are not task statuses, lifecycle
states, scoring categories, mandatory fields, or a second knowledge taxonomy.
A release may use different dispositions for different facts.

### Exact Copies

Use exact copies only for files deliberately included in the package mapping
because external operation needs their current wording. The repository file is
the only content owner. Do not independently edit the copy.

Exact-copy validation requires:

- current canonical path and mapped package name;
- byte-for-byte identity after the authorized copy;
- package file-count validation;
- independent review of the changed scope when the release/task requires it.

The package checker may report mismatch, but it must not write or select a
disposition automatically.

### Compact Summaries

Use compact summaries for durable orientation rather than full operational
instruction. A summary must remain reconstructable from its canonical sources
and preserve, when material:

- current decision or state and the next action;
- source and authority, including `/about` non-canonical status;
- scope, applicability, and non-applicability;
- role, review, approval, and automation boundaries;
- meaningful caveats, exceptions, risk, uncertainty, and stop conditions;
- replacement or supersession state when old memory would mislead.

Omit raw evidence, task-local history, draft debate, implementation narration,
repeated prose, and details whose only durable home should be the repository.
Compression fails when the summary becomes broader, more certain, more
permanent, or more authoritative than canon.

Summary validation is semantic and human-reviewed. The exact-copy checker
cannot establish that omissions, phrasing, or compression preserve meaning.

### Stale Or Contradictory Memory Repair

Treat these as material indicators:

- exact-copy mismatch;
- current state, status, approval, or next-action conflict;
- missing or renamed source, role, path, status, or validator;
- words such as `current`, `latest`, `temporary`, `next`, or `pending` without
  a surviving current-state basis;
- summary language broader, narrower, or more certain than canon;
- duplicate memory facts that disagree or obscure scope;
- deprecated or retired behavior still described as active;
- sensitive detail retained after its external purpose ends;
- package growth without new durable external value.

Repair in this order:

1. Stop using the disputed memory fact as evidence.
2. Identify the canonical owner and current reviewed state.
3. If canon is clear, `correct`, `compress`, replace, or `retire` memory from
   that source.
4. If canonical sources conflict, route the owner conflict through Chief
   Editor, repair canon first, and `defer` or block the memory change.
5. Run exact-copy or semantic validation as applicable.
6. Independently review authority, meaning, privacy, growth, and potential
   context loss.
7. Record material correction, consolidation, retirement, deferral, or
   no-sync evidence in the smallest existing governance artifact.

Do not average contradictions into vague wording, choose a convenient source,
silently delete meaningful context, or let memory override repository files.

### Consolidation, Compression, And Retirement

Before adding a fact, search current memory summaries and mapped copies. When
duplicates exist, consolidate them into the strongest existing summary
location, merge only unique useful meaning, retain necessary source pointers
and caveats, and remove redundant statements.

Retirement removes obsolete content from active external memory; it does not
delete repository history. Use replacement wording when new guidance
supersedes the old fact. Use removal when no replacement is needed. Preserve a
repository pointer or disposition rationale when future readers may need to
understand why context changed.

No memory size score, completeness metric, growth target, or fact quota is
used. Growth is bounded by continuing external value, the package contract,
deduplication, omission, compression, and independent review.

### Evidence And Auditability

When disposition is material, make these reconstructable in the smallest
existing release, review, final-decision, or implementation artifact:

- source signal and canonical source path(s);
- memory fact/location currently affected;
- materiality, purpose, sensitivity, and continuing-value judgment;
- chosen disposition and non-obvious rejected alternatives;
- exact-copy or summary validation performed;
- context preserved during correction, consolidation, or retirement;
- reviewer outcome;
- explicit canonical-authority and non-automation boundary.

These are conditional evidence fields. They do not create a mandatory memory
artifact, task-object field, audit log, or review gate.

### Evaluation Signals And Advisory Automation

An Evaluation Signal may report likely drift, duplication, contradiction,
maintenance burden, repeated validation failure, or memory bloat. It remains
an input to Chief Editor judgment. It cannot choose a disposition, write or
delete memory, change canon, prove completeness, or trigger synchronization
automatically.

Advisory automation may count package files, compare mapped exact copies,
check paths/references, and report likely drift for review. It must not write,
summarize, correct, consolidate, omit, or retire content; change canon to fit
memory; infer sensitive-data disposition; propagate raw feedback or task-local
content; or record release acceptance.

### Ownership And Review

| Role or check | Memory-hygiene responsibility |
| --- | --- |
| Chief Editor | Identify canonical source, decide materiality and disposition, record material no-sync/deferral, authorize bounded manual change, and preserve Project Lead authority. |
| Research Agent | Verify source freshness, provenance, conflict, privacy, or summary evidence when assigned; do not decide disposition. |
| Writer Agent | Apply the authorized exact-copy or compact-summary change from named sources; do not add memory-only rules. |
| Review Agent | Challenge source fidelity, summary semantics, authority, privacy, omission, duplication, growth, context preservation, validation, and non-automation inside the existing review gate. |
| Final Editor | Preserve reviewed memory-disposition meaning during controlled finalization; do not reclassify it. |
| Integrity check/script | Report file-count, exact-copy, path, reference, or likely-drift failures; never write or become an owner. |
| Project Lead | Accept or request changes to a release; no memory state supplies acceptance automatically. |

Run `ai-editorial-office/scripts/check_about_memory_package.sh` whenever
`/about` is updated. Passing the checker proves only the fixed package count and
mapped exact-copy identity; review must still validate compact-summary meaning,
omissions, contradictions, and growth.

## Integration Points

### Task Object

Task state may expose learning candidates, canon updates needed, reusable
patterns, deprecated assumptions, and post-task learning when they materially
affect closure or future work.

### Shared Lifecycle

Learning is normally considered during governance and memory curation. It may
also appear during review or repair when a repeated issue should become a
safeguard.

### Capability Registry

Knowledge Evolution includes learning extraction, canon evolution, pattern
reuse, stale knowledge detection, correction, retirement, and memory
disposition, including the bounded Memory Hygiene Intelligence contract, as
shared capabilities. They do not create a standing Historian, Memory Manager,
Canon Manager, or Knowledge Curator role.

### Failure Modes

Canon duplication, stale assumptions, repeated failures, and implementation-task
dilution can produce learning candidates. Use `/kb/editorial_failure_modes.md`
to recover first, then decide whether canon should change.

### Quality Attributes

Maintainability, reviewability, traceability, evidence support, and
implementation readiness help decide whether learning deserves promotion.

### Codex Task Standard

Codex completion notes may surface reusable patterns, canon updates needed, or
obsolete assumptions when relevant. This should stay compact and should not turn
every implementation into a retrospective.

### Review Gate

Review Agent challenges Knowledge Evolution claims inside the existing
`review.md` when reviewed work proposes reusable learning, pattern promotion,
canon updates, stale/conflicting knowledge, or `/about` synchronization.
Review checks evidence, scope, owner, duplication, privacy, maintenance cost,
and whether task-local disposition is safer than canon change.

## Role Cooperation

Learning and canon evolution are shared work, not a new role.

| Role | Learning responsibility |
| --- | --- |
| Chief Editor | Classify reusable decisions, learning disposition, pattern candidates, canon updates, stale assumptions, correction/retirement needs, and `/about` materiality/disposition during governance or memory curation. |
| Research Agent | Separate durable evidence/context from task-local findings; flag source freshness, provenance, or evidence-pattern signals. |
| Review Agent | Challenge Knowledge Evolution claims; identify repeated findings, canon duplication, stale/conflicting canon, unsupported promotion, or safeguards that may deserve a system update. |
| Final Editor | Preserve reviewed reusable learning cues without bloating final output or classifying feedback/canon disposition. |

No Historian role exists in the current core role set, and this framework does
not create one.

## Non-Goals

This framework does not:

- add new agents;
- create a Historian role;
- create a Knowledge Curator or Canon Manager role;
- make every task produce a retrospective;
- turn feedback into automatic canon;
- make `/about` canonical;
- create a second memory system, autonomous synchronization mechanism, or
  mandatory per-commit sync;
- use memory completeness, health, growth, or scoring metrics;
- propagate unreviewed, task-local, temporary, private, or sensitive content;
- replace `customer_feedback_loop.md` or `feedback_patterns.md`;
- bypass review for system updates;
- delete historical artifacts;
- promote private source material into public memory;
- require a new learning artifact for every task.
- make Domain Pack telemetry or effect notes mandatory for every activation;
- treat Domain Pack activation as proof of usefulness;
- invent feedback, learning, or evaluation scores without evidence.
