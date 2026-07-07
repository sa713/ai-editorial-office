# Editorial Learning & Canon Evolution Framework

This file is the canonical owner for reusable learning, canonization criteria,
learning extraction, canon evolution, stale-canon challenge, and canon
retirement in AI Editorial Office.

It makes the system stronger after completed work without creating uncontrolled
memory sprawl. It is not a memory database, retrospective ritual, new role,
workflow engine, review gate, or automatic documentation generator.

## Purpose

Editorial work can produce knowledge that should help future tasks. Most task
details should remain task-local. This framework decides what is worth keeping,
where it belongs, and how it enters canon safely.

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
- scope: where the learning applies and where it does not;
- owner: which canonical file should own the rule;
- duplication: whether the rule already exists elsewhere;
- conflict: whether it changes lifecycle, roles, review gate, statuses, or
  authority boundaries;
- privacy: whether the learning contains private or source-only material;
- maintenance: whether future agents can use it without more process weight.

If validation is weak, keep the item task-local, mark it as a candidate, or
request a separate reviewed system-update mission.

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

## Stale Canon Challenge

Challenge stale canon when:

- a rule conflicts with current repository state;
- a client/project source is stale, missing, or contradicted;
- a repeated review finding shows the current rule is insufficient;
- a canonical owner duplicates another owner;
- a path, template, role, or lifecycle assumption no longer matches the active
  system;
- a task repeatedly needs an exception to succeed.

The recovery is not immediate deletion. Record the concern, identify the owner,
verify evidence, and update, deprecate, or retire through a reviewed change when
the evidence is sufficient.

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

Learning extraction, canon evolution, pattern reuse, and stale canon detection
are shared capabilities. They do not create a standing Historian, Memory
Manager, or Canon Manager role.

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

## Role Cooperation

Learning and canon evolution are shared work, not a new role.

| Role | Learning responsibility |
| --- | --- |
| Chief Editor | Classify reusable decisions, pattern candidates, canon updates, and stale assumptions during governance or memory curation. |
| Research Agent | Separate durable evidence/context from task-local findings; flag source freshness or provenance patterns. |
| Review Agent | Identify repeated findings, canon duplication, stale canon, or safeguards that may deserve a system update. |
| Final Editor | Preserve reusable learning cues without bloating final output or classifying feedback. |

No Historian role exists in the current core role set, and this framework does
not create one.

## Non-Goals

This framework does not:

- add new agents;
- create a Historian role;
- make every task produce a retrospective;
- turn feedback into automatic canon;
- make `/about` canonical;
- replace `customer_feedback_loop.md` or `feedback_patterns.md`;
- bypass review for system updates;
- delete historical artifacts;
- promote private source material into public memory.
