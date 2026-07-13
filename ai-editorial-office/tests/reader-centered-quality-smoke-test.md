# Reader-Centered Quality Smoke Test

Purpose: manually verify activation, restraint, evidence guardrails, bounded
tradeoffs, Reader Review determinism, Companion Pass, and depth calibration.
These synthetic cases are not task materials, production evidence, or proof of
real-world improvement.

Canonical owners:

- `/kb/audience_outcome_alignment.md`
- `/kb/professional_communication.md`
- `/kb/editorial_quality_attributes.md`
- `/kb/shared_lifecycle_kernel.md`
- `/agents/review_agent.md`
- `/pipelines/review_pipeline.md`

For every case record activation, depth, finding, evidence pointer, outcome,
repair owner/scope when needed, and which non-relaxable guardrails remain.

## Case 1 — Correct But Academically Useless

Input: a source-backed article for an experienced practitioner defines twelve
current concepts accurately, but never connects them to the reader's recorded
old workflow, provides no supported example, and ends without an action.

Expected:

- Reader Review: material, `full`;
- Cognitive Bridge: `fail`;
- Application: `fail`;
- Reader burden: `fail` only with exact dense passages and the blocked outcome;
- Companion Pass: `fail` for avoidable academic distance;
- outcome: `changes_requested`;
- repair: Writer Agent adds the approved bridge, example, and action without
  changing claims or source boundaries; re-review is bounded to those changes
  plus affected traceability.

## Case 2 — Pleasant But Unsupported

Input: a lively short answer says a product is safer, faster, and easier than
alternatives without supplied evidence. The selection advice is memorable.

Expected:

- Reader Review and Companion Pass cannot compensate for unsupported claims;
- factual/evidence gate: `fail`;
- outcome: `changes_requested` or `blocked` according to evidence availability;
- repair: remove or research the claims through the existing owner;
- forbidden result: `approved` because the answer is easy to read.

## Case 3 — Usable Cognitive Bridge

Input: the brief records “reader still treats a prompt as the whole control
surface.” The artifact says that prompt quality still matters, then shows how
contract, selected context, tools, permissions, and verification now surround
it, with one source-backed before/after example and a tomorrow-morning action.

Expected:

- Cognitive Bridge: `pass`;
- Understanding, retention, and application: `pass` when exact sections support
  them;
- Learning sequence may differ from five literal headings;
- evidence and Companion Pass remain independently checked;
- outcome may be `approved` if all other gates pass.

## Case 4 — Feature Dump Instead Of Bridge

Input: a reader names an old product/version stopping point. The response lists
twenty current features by provider but never explains which working model
changed, which features matter to the reader's tasks, or what to do.

Expected:

- Reader fit, Cognitive Bridge, retention, and application: `fail`;
- more features are not a valid repair by themselves;
- vendor neutrality and freshness are reviewed separately;
- bounded repair selects only evidenced examples that serve the recorded
  transition.

## Case 5 — Justified Bounded Utility Tradeoff

Input: a reader explicitly asks what changed since a named dated practice. Chief
Editor records a six-item chronology limited to verified provider sources as of
a named date, marks availability limits, states that durability is relaxed, and
keeps correctness, evidence, neutrality, traceability, caveats, and review.

Expected:

- Bounded Utility Tradeoff: `pass` if the chronology materially improves the
  bridge;
- stale-if trigger is present;
- product specificity does not become promotion or exhaustive catalog;
- full Reader Review challenges claimed reader benefit as well as guardrails.

## Case 6 — Unjustified Bounded Utility Tradeoff

Input: Chief Editor says “current products are more engaging” and permits a
feature catalog with no date, evidence boundary, scope, relaxed attribute, or
stale-if trigger.

Expected:

- Bounded Utility Tradeoff: `fail`;
- correctness and neutrality cannot be declared relaxable;
- outcome: `changes_requested` or `blocked`;
- repair owner: Chief Editor for route/contract, Research Agent for missing
  evidence only if the route remains justified.

## Case 7 — Reader Review As Taste

Input: Reviewer writes “I prefer shorter sentences and a warmer opening” but
cannot connect either preference to the Reader Outcome Contract, a criterion,
or an exact blocked passage.

Expected:

- finding is rejected as preference-only;
- Reviewer may record a non-blocking suggestion only if task conventions allow;
- no rewrite, new persona, or fake empathy is required;
- another valid route is not a blocker when the approved route works.

## Case 8 — Short Text With Full Learning Design Not Applicable

Input: answer in at most 50 words whether to use a fixed workflow or an agent,
using two supplied definitions and one practical selection rule.

Expected:

- Reader Review depth: `compact`;
- checks: main transfer understood, intended action possible, no avoidable
  burden/artificial tone;
- full Cognitive Bridge/Moments/Learning Design table: `not applicable`;
- evidence and independent review still apply;
- no new role, stage, gate, or standalone reader artifact appears.

## Architecture Restraint Checks

All cases must preserve these invariants:

- no Reader Model Agent, Learning Designer, Companion Agent, or separate reader
  testing role;
- no `reader-model.md`, `learning-design.md`, `reader-review.md`, or
  `companion-pass.md` requirement;
- Reader Review and Companion Pass remain inside the existing review gate and
  `review.md`;
- depth changes evidence volume, not the existence of review;
- synthetic results do not update canon, backlog, roles, or promotion status
  automatically.

## Evolution Restraint Cases

### One Positive Pilot

A longread improves after adding a Cognitive Bridge, while working-document and
short-text evidence is missing. Expected disposition: `learning_candidate` or
`deferred`; no permanent role, master backlog change, or canon claim.

### Repeated Cross-Task Failure

Several comparable task types fail Reader Review after bounded changes to
existing owners. Evidence identifies a genuine accountability/independence
conflict and estimates coordination cost. Expected disposition: at most
`canon_update_candidate` for a separate reviewed system update and Project Lead
decision. No count or Evaluation Signal creates the role automatically; a
smaller owner patch, rejection, deferral, or `no role change` remains valid.

## Pass Condition

The smoke test passes only when cases 1-8 produce the expected distinctions:
reader value is not mere readability, pleasant unsupported copy fails evidence,
good bridges are reviewable, feature dumps do not substitute for transitions,
utility tradeoffs remain bounded, taste does not become a blocker, and compact
tasks remain compact. Existing lifecycle and task-pack automated smoke tests
must also pass.
