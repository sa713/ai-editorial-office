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

## `/about` Memory Disposition

`/about` is an external memory package, not canon. Knowledge Evolution may
trigger `/about` sync only after canonical source files or compact summaries
change in a way that should be visible outside the repository.

Memory sync rules:

- update `/about` only from canonical source or approved compact summaries;
- do not let `/about` introduce new rules;
- if `/about` diverges, treat the repository source as authoritative;
- run the memory package check when `/about` is updated;
- record memory disposition in `final_decision.md`, release report, or release
  pack when material.

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
disposition as shared capabilities. They do not create a standing Historian,
Memory Manager, Canon Manager, or Knowledge Curator role.

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
| Chief Editor | Classify reusable decisions, learning disposition, pattern candidates, canon updates, stale assumptions, correction/retirement needs, and `/about` sync disposition during governance or memory curation. |
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
- replace `customer_feedback_loop.md` or `feedback_patterns.md`;
- bypass review for system updates;
- delete historical artifacts;
- promote private source material into public memory;
- require a new learning artifact for every task.
- make Domain Pack telemetry or effect notes mandatory for every activation;
- treat Domain Pack activation as proof of usefulness;
- invent feedback, learning, or evaluation scores without evidence.
