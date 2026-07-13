# Social Task Template

## template purpose

Use for social posts, platform-specific variants, campaign captions,
announcement copy, or short-form distribution copy. This template is a working
form; platform sequence and governance live in the selected pipeline. The file
lists below are scaffolding defaults; they do not override pipeline
conditionality, compact execution, or canonical ownership.

## when to use

- Deliverable is social copy or variants.
- Platform constraints affect length, tone, CTA, or formatting.
- Draft variants need review before finalization.
- Research/evidence artifacts are created only when claims or governance require
  traceability.

## folder structure

```text
tasks/TASK-ID/
  brief.md
  task-manifest.md
  status.md
  platform-constraints.md
  draft.md
  review.md
```

Conditional files:

- `orchestration_plan.md`
- `research.md`, `sources.md`, `facts.md`, `claims_table.md`
- `claims-used.md`
- `writer-notes.md`
- `open-questions.md`
- `qa-checklist.md`
- `review-summary.md`
- `reviewer-notes.md`
- `final.md`
- `finalization-notes.md`
- `finalization-checklist.md`
- `final_decision.md`
- `handoff-*.md`

## required files

- `brief.md`
- `task-manifest.md`
- `status.md`
- `platform-constraints.md`
- `draft.md`
- `review.md`

## conditional artifact rules

- `review.md` is the primary review artifact.
- Optional review/finalization artifacts require downstream, high-governance,
  task-specific, blocker, or traceability need.
- `open-questions.md` exists only for real questions or blockers.
- Research traceability files are required when social copy contains factual,
  product, numeric, legal, policy, or sensitive claims.

## bootstrap

1. Capture campaign/post goal in `brief.md`.
2. Set current state, version pointers, and `client_profile` fields when a
   client profile is considered in `task-manifest.md`.
3. Record status.
4. Fill platform constraints before drafting.
5. Draft variants, review, then finalize only after approved review.

## brief.md scaffold

```markdown
# Brief

## task title

## user goal

## audience

## platform or channel

## deliverable

## message priority

## CTA

## constraints

## client profile

## factual sensitivity

## risk mode

## success criteria

## reader outcome, only when material

- Starting state or immediate context:
- Required understanding or action:
- Failure signal:
- Reader Review depth: compact/normal/not applicable
- Companion Pass: required/not applicable

## open questions
```

## platform-constraints.md scaffold

```markdown
## platform constraints

| Platform | Character/format limit | Tone | CTA | Hashtags/tags | Notes |
| --- | --- | --- | --- | --- | --- |
```

## research artifacts

Create only when claims need evidence.

```markdown
# Research

## key facts

## claim risks

## do-not-say list

## evidence gaps
```

```markdown
# Claims Table

| Claim | Evidence | Sensitivity | Safe for copy? |
| --- | --- | --- | --- |
```

## writing artifacts

```markdown
# Draft

## platform

## variant 1

## variant 2

## variant 3

## rationale

## review notes
```

```markdown
# Claims Used

| Claim | Variant | Evidence | Caveat |
| --- | --- | --- | --- |
```

```markdown
# Writer Notes

## assumptions

## tone choices

## CTA choices

## unresolved issues
```

## review artifacts

```markdown
# Review

## reviewed variants

## reviewer independence

## platform validation

## claim validation

## tone and CTA validation

## compact reader review, when material

- Reader understands the main transfer: pass/fail/not applicable
- Reader can take the intended action: pass/fail/not applicable
- Avoidable burden or artificial tone blocks the outcome: yes/no/not applicable
- Companion Pass: pass/fail/not applicable

## findings

## blockers

## outcome

approved / changes_requested / blocked

## next action
```

## finalization artifacts

```markdown
# Final

## approved platform copy

## selected variant

## posting notes
```

Create finalization notes/checklist only when conditional rules require them.

## handoff files

Use `handoff_template.md` for role transfer. Include current variants, platform,
claim caveats, blockers, and next action.

## completion checklist

- Platform constraints are current.
- Current active variant/version is clear.
- Claims are supported or omitted.
- Reader outcome checks are compact or explicitly not applicable.
- `review.md` exists and matches reviewed variants.
- Conditional artifacts are justified.

## restart checklist

Read:

- `AGENTS.md` or invariant summary;
- `task-manifest.md`;
- latest relevant handoff;
- current draft/final variant;
- directly relevant pipeline/KB/platform constraint.
