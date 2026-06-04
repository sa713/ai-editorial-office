# Article Task Template

## template purpose

Use for article, post, guide, explainer, editorial page, or long-form content
that needs drafting and review. This template is a working folder form, not a
mini-pipeline. Follow `AGENTS.md`, the selected pipeline, and artifact templates
for canonical rules.

## when to use

- Article or editorial draft is the main deliverable.
- Writer produces draft material from brief, KB, and evidence.
- Review is required before finalization.
- Research artifacts are created only when factual claims or governance needs
  require traceability.

## folder structure

```text
tasks/TASK-ID/
  brief.md
  task-manifest.md
  status.md
  orchestration_plan.md
  draft.md
  review.md
```

Conditional files:

- `research.md`, `sources.md`, `facts.md`, `claims_table.md`
- `outline.md`
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
- `draft.md`
- `review.md`

`orchestration_plan.md` is required when role routing, process depth,
governance, or non-trivial coordination must be recorded.

## conditional artifact rules

- `review.md` is the primary review artifact for low-risk and simple standard
  tasks.
- `qa-checklist.md` and `review-summary.md` are created only for downstream,
  high-governance, task-specific, blocker, or traceability need.
- `open-questions.md` is created only for real open questions, blockers, or
  traceability gaps.
- `finalization-notes.md` and `finalization-checklist.md` are created only for
  high-governance, downstream governance, controlled changes, blockers, or
  traceability need.

## bootstrap

1. Create `brief.md`.
2. Create `task-manifest.md` with current-version pointers when versions exist
   and `client_profile` fields when a client profile is considered.
3. Create `status.md`.
4. Add `orchestration_plan.md` only when coordination requires it.
5. Create only the production and review artifacts needed by the selected depth.

## brief.md scaffold

```markdown
# Brief

## task title

## user goal

## audience

## deliverable

## channel or publication context

## scope

## constraints

## client profile

## source materials

## factual sensitivity

## risk mode

## success criteria

## open questions
```

## research artifacts

Create only when factual claims, evidence gaps, or governance require them.

```markdown
# Research

## scope

## key findings

## confirmed facts

## interpretations

## contradictions

## gaps

## do-not-say list
```

```markdown
# Sources

| Source | Type | Date | Reliability | Used for | Notes |
| --- | --- | --- | --- | --- | --- |
```

```markdown
# Claims Table

| Claim | Evidence | Confidence | Sensitivity | Safe for drafting? |
| --- | --- | --- | --- | --- |
```

## writing artifacts

```markdown
# Outline

## working title

## audience

## structure

## key points

## evidence dependencies

## open writing questions
```

```markdown
# Draft

## title

## body

## notes for review
```

```markdown
# Claims Used

| Claim | Source/evidence | Location in draft | Caveat |
| --- | --- | --- | --- |
```

```markdown
# Writer Notes

## assumptions

## tone and structure choices

## caveats

## unresolved issues
```

## review artifacts

```markdown
# Review

## reviewed artifacts

## reviewer independence

## validation summary

## findings

## blockers

## required changes

## outcome

approved / changes_requested / blocked

## next action
```

## finalization artifacts

```markdown
# Final

## final title

## final body
```

Create finalization notes/checklist only when conditional rules require them.

## handoff files

Use `handoff_template.md` for role transfer. Keep handoffs to delta, blockers,
current artifacts, and next action.

## completion checklist

- Brief and manifest are current.
- Current active version is clear.
- Required evidence is present or explicitly not applicable.
- `review.md` exists and matches the reviewed artifact.
- Blockers and open questions are resolved or escalated.
- Conditional artifacts are justified, not automatic.

## restart checklist

Read:

- `AGENTS.md` or invariant summary;
- `task-manifest.md`;
- latest relevant handoff;
- current working artifact;
- directly relevant pipeline/KB.
