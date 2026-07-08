# UX Writing Task Template

## template purpose

Use for interface copy, onboarding text, microcopy, labels, helper text,
validation messages, notifications, empty states, and flow-state language. This
template supports UX copy production without turning UX Writer into product
manager, designer, reviewer, or final approver. The file lists below are
scaffolding defaults; they do not override pipeline conditionality, compact
execution, or canonical ownership.

## when to use

- Deliverable is product/interface language.
- Product context, user state, terminology, accessibility, or edge cases affect
  wording.
- UX copy needs independent review before finalization.
- Evidence artifacts are created only when factual or product-behavior claims
  require traceability.

## folder structure

```text
tasks/TASK-ID/
  brief.md
  task-manifest.md
  status.md
  product-context.md
  ux-copy.md
  review.md
```

Conditional files:

- `orchestration_plan.md`
- `terminology.md`
- `content-map.md`
- `states-table.md`
- `terminology-notes.md`
- `ux-writer-notes.md`
- `research.md`, `sources.md`, `facts.md`, `claims_table.md`
- `open-questions.md`
- `qa-checklist.md`
- `review-summary.md`
- `final.md`
- `finalization-notes.md`
- `finalization-checklist.md`
- `final_decision.md`
- `handoff-*.md`

## required files

- `brief.md`
- `task-manifest.md`
- `status.md`
- `product-context.md`
- `ux-copy.md`
- `review.md`

## conditional artifact rules

- `content-map.md`, `states-table.md`, and terminology notes are created only
  when state coverage, review, product traceability, or task requirements need
  them.
- `review.md` is the primary review artifact.
- Optional review/finalization artifacts require downstream, high-governance,
  task-specific, blocker, or traceability need.
- `open-questions.md` exists only for real product, flow, terminology, or
  blocker questions.

## bootstrap

1. Capture UX goal in `brief.md`.
2. Set current state, version pointers, and `client_profile` fields when a
   client profile is considered in `task-manifest.md`.
3. Record status.
4. Fill product context before writing copy.
5. Create UX copy and any needed state/terminology support.
6. Review before finalization.

## brief.md scaffold

```markdown
# Brief

## task title

## user goal

## product area

## user state or journey moment

## deliverable

## constraints

## client profile

## tone and terminology requirements

## accessibility concerns

## factual or product-behavior sensitivity

## risk mode

## success criteria

## open questions
```

## product-context.md scaffold

```markdown
## product context

## user problem

## flow or screen

## user action

## system response

## known product rules

## unavailable or unknown behavior

## evidence/source for behavior
```

## terminology.md scaffold

```markdown
## terminology

| Term | Approved wording | Avoid | Notes |
| --- | --- | --- | --- |
```

## ux-copy.md scaffold

```markdown
# UX Copy

| Location/state | Copy | Purpose | Notes |
| --- | --- | --- | --- |
```

## content-map.md scaffold

Create only when the flow or page needs mapped content.

```markdown
# Content Map

| Area | User need | Copy element | Dependency |
| --- | --- | --- | --- |
```

## states-table.md scaffold

Create only when state coverage matters.

```markdown
# States Table

| State | Trigger | User need | Copy | Edge cases |
| --- | --- | --- | --- | --- |
```

## ux-writer-notes.md scaffold

```markdown
# UX Writer Notes

## assumptions

## terminology decisions

## accessibility concerns

## edge cases

## unresolved UX questions
```

## research artifacts

Create only when factual or product-behavior claims need evidence.

```markdown
# Claims Table

| Claim or product behavior | Evidence | Confidence | Safe for UX copy? |
| --- | --- | --- | --- |
```

## review artifacts

```markdown
# Review

## reviewed artifacts

## reviewer independence

## product behavior validation

## terminology validation

## accessibility and clarity validation

## findings

## blockers

## outcome

approved / changes_requested / blocked

## next action
```

## finalization artifacts

```markdown
# Final

## final UX copy

## implementation notes
```

Create finalization notes/checklist only when conditional rules require them.

## handoff files

Use `handoff_template.md`. Include produced copy, states covered, product
assumptions, terminology decisions, blockers, and review focus.

## completion checklist

- Product behavior is known or uncertainty is visible.
- Current active version is clear.
- UX copy maps to real states.
- Terminology and accessibility concerns are addressed.
- `review.md` exists and matches reviewed copy.
- Conditional artifacts are justified.

## restart checklist

Read:

- `AGENTS.md` or invariant summary;
- `task-manifest.md`;
- latest relevant handoff;
- current UX copy or product context;
- directly relevant pipeline/KB/product evidence.
