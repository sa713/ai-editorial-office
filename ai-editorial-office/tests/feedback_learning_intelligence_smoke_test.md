# Feedback and Learning Intelligence Smoke Test

Status: manual smoke test; synthetic decision cases only.

Purpose: validate the S5.R1 bridge between
`/kb/customer_feedback_loop.md` and
`/kb/editorial_learning_framework.md` without creating a new taxonomy, store,
role, pipeline, lifecycle stage, review gate, scoring model, or automatic
promotion path.

These cases test decision logic. They are not real feedback, real Domain Pack
use evidence, or evidence that any pattern is confirmed in production.

## Required fields for each case

- feedback classification when actual post-delivery feedback exists;
- source signal and evidence pointer;
- observed outcome and affected system area;
- applicability and counterevidence;
- learning disposition;
- existing owner and bounded action or explicit no-action;
- non-promotion statement.

## Cases

### FLI-01 - One-off wording correction

- Signal: after delivery, the user asks to replace one misleading heading in
  the current artifact.
- Feedback classification: `task_local`.
- Evidence and scope: exact user request plus the delivered heading; affects
  one artifact and no other task.
- Learning disposition: `task_local`.
- Owner/action: current task's Writer or UX Writer makes a bounded revision if
  requested; existing review rules decide re-review scope.
- Non-promotion: no pattern entry, canon update, backlog, roadmap, memory, or
  model change.
- Verdict: pass.

### FLI-02 - Repeated user preference

- Signal: the same user says across three saved tasks that future executive
  briefs should be shorter and avoid promotional tone.
- Feedback classification: `preference`.
- Evidence and scope: three task-local feedback pointers; consistent wording
  and comparable deliverable type; scope is this user and executive briefs,
  not all customers, formats, or editorial work.
- Learning disposition: scoped `learning_candidate` or task-local preference.
- Owner/action: Chief Editor reuses the preference when relevant; a verified
  client/profile owner may be considered only if the existing profile rules
  apply.
- Counterevidence: long analytical reports may still need depth.
- Non-promotion: repetition does not make the preference global canon.
- Verdict: pass.

### FLI-03 - Recurring workflow failure across tasks

- Signal: three comparable task reviews show that a required source-status
  caveat was lost at the same handoff boundary and caused review blockers.
- Feedback classification: `confirmed_pattern` if the repeated signal came
  through post-delivery feedback; not applicable if identified only through
  review outcomes.
- Evidence and scope: saved handoffs and review findings identify the same
  boundary failure; unrelated tasks without the boundary are excluded.
- Learning disposition: `pattern_candidate`, then
  `canon_update_candidate` only if a bounded owner patch is proposed.
- Owner/action: route a small prevention/test proposal to the existing handoff,
  source-provenance, or pipeline owner selected by Chief Editor; define
  expected effect and re-test on a comparable task.
- Non-promotion: no production rule changes until separate owner review and
  validation.
- Verdict: pass.

### FLI-04 - Successful pattern worth reusing

- Signal: a compact source-summary handoff was used in several comparable
  source-heavy tasks and independent review found fewer provenance gaps without
  loss of necessary evidence.
- Feedback classification: not applicable unless a user reaction is one of the
  source signals.
- Evidence and scope: comparable task artifacts, review findings, and explicit
  source-depth context; alternative explanations such as simpler source sets
  are considered.
- Learning disposition: `pattern_candidate`.
- Owner/action: Chief Editor may authorize a bounded future-use test or propose
  a concise patch to the existing source/handoff owner.
- Non-promotion: successful use is not `accepted_canon` until owner-file review,
  implementation, and validation occur.
- Verdict: pass.

### FLI-05 - Negative feedback unsupported by evidence

- Signal: one user says the delivered artifact is factually wrong but gives no
  example; the cited claims and sources are rechecked and no contradiction is
  found.
- Feedback classification: `observation` or `task_local` clarification signal,
  depending on whether the user asks for a current-task check.
- Evidence and scope: raw comment is preserved; claim/source recheck is saved;
  the alleged error remains unidentified.
- Learning disposition: `rejected` for reusable/system learning, or `deferred`
  if the user may provide concrete evidence later.
- Owner/action: Chief Editor may ask for the disputed claim or retain a task-
  local caveat; no system action.
- Non-promotion: negative sentiment alone does not prove a system failure.
- Verdict: pass.

### FLI-06 - Domain Pack activation improved a result

- Signal: an actually activated Software Architecture Domain Pack supplied a
  specific quality-attribute scenario and source pointer used in the draft;
  independent review shows that the scenario exposed a previously hidden
  tradeoff.
- Feedback classification: not applicable unless the user also comments after
  delivery.
- Evidence and scope: activation note, sections/sources actually used, draft
  delta or decision record, and review finding; effect is `beneficial` with
  bounded confidence because one comparable task is available.
- Learning disposition: `learning_candidate` for future comparable tasks.
- Owner/action: Chief Editor may test the same activation signal on another
  architecture-sensitive task; pack owner receives a candidate only if content
  or activation guidance is implicated.
- Non-promotion: one beneficial activation does not confirm pack value, change
  activation rules, or update the pack automatically.
- Verdict: pass.

### FLI-07 - Domain Pack activation added unnecessary complexity

- Signal: an actually activated AI Engineering Domain Pack added sections that
  were not used in the result, increased context cost, and caused Review Agent
  to request removal of domain detail unrelated to the task outcome.
- Feedback classification: not applicable unless post-delivery feedback also
  exists.
- Evidence and scope: activation reason, unused sections, writer/review notes,
  and bounded context-cost evidence; effect is `burdensome` for this task type,
  not proof that the pack is generally harmful.
- Learning disposition: `task_local` or routing `learning_candidate`.
- Owner/action: Chief Editor narrows future activation in a comparable test;
  repeated evidence may route to the pack or Domain Pack Standard owner.
- Non-promotion: one over-activation does not retire, rewrite, or deactivate the
  pack automatically.
- Verdict: pass.

### FLI-08 - System change proposed from one anecdote

- Signal: one post-delivery complaint proposes changing every pipeline.
- Feedback classification: `system_change_candidate` records the requested
  route without endorsing it.
- Evidence and scope: one task and no comparable evidence; broad applicability
  is unsupported and maintenance/risk cost is high.
- Learning disposition: `deferred` pending comparable evidence or `rejected`
  if the proposal conflicts with known boundaries.
- Owner/action: no owner patch; Chief Editor may record what evidence would be
  needed to reconsider.
- Non-promotion: no backlog, roadmap, pipeline, canon, or model change.
- Verdict: pass.

### FLI-09 - Stale learning should be corrected or retired

- Signal: a saved reusable rule points to a removed path and contradicts the
  current canonical owner.
- Feedback classification: not applicable unless a user reported the stale
  rule after delivery.
- Evidence and scope: current repository inspection, the stale rule, current
  owner, and affected read path; historical artifacts remain historical.
- Learning disposition: `canon_update_candidate` with correction or
  supersession; `retired` when no replacement is needed.
- Owner/action: patch only the existing canonical owner through reviewed work,
  preserve replacement/rationale, validate references, then sync `/about` only
  if its exported memory is affected.
- Non-promotion: stale detection does not authorize silent deletion or broad
  rewrite.
- Verdict: pass.

## Cross-Case Results

| Requirement | Result | Evidence |
| --- | --- | --- |
| One-off feedback stays local | pass | FLI-01, FLI-05, FLI-08 |
| Preferences remain scoped | pass | FLI-02 |
| Pattern confirmation requires comparable evidence and applicability | pass | FLI-03, FLI-04 |
| Positive and negative outcomes are both learnable | pass | FLI-04, FLI-05, FLI-06, FLI-07 |
| Rejection and deferral are explicit | pass | FLI-05, FLI-08 |
| Existing owner is named before action | pass | all cases |
| Domain Pack activation and effect evidence are distinct | pass | FLI-06, FLI-07 |
| No automatic canon, backlog, roadmap, memory, pack, or model change | pass | all cases |
| Stale learning is corrected, superseded, or retired with traceability | pass | FLI-09 |

## Overall Verdict

Pass. All nine representative cases produce a bounded classification or
learning disposition, evidence treatment, affected owner, and explicit non-
promotion result. The cases require no new governance structure and do not
claim that synthetic validation is real pattern or Domain Pack outcome
evidence.
