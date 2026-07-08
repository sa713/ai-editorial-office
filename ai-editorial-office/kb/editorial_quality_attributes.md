# Editorial Quality Attributes Framework

This file is the canonical owner for editorial quality attributes, quality
tradeoffs, task-specific quality priorities, evaluation guidance, and quality
preservation across the AI Editorial Office lifecycle.

It defines shared quality vocabulary. It is not a scoring framework, mandatory
checklist, new review process, role, workflow engine, or replacement for the
Review Pipeline.

## Purpose

Quality is not one thing. A strong artifact may need correctness, clarity,
actionability, traceability, audience fit, implementation readiness, or
maintainability in different proportions.

This framework helps agents:

- name the qualities that matter for the task;
- avoid optimizing for the wrong quality;
- make tradeoffs visible instead of pretending they disappear;
- preserve intended quality across handoffs;
- give Review Agent a shared vocabulary for findings;
- keep compact tasks compact and high-risk tasks explicit.

Use the smallest quality profile that makes the task reviewable. Do not create
a quality artifact unless risk, restartability, review, or governance needs it.

## Quality Attribute Model

A task may select priority attributes from the table below. Not every attribute
is required for every task.

| Attribute | Meaning | Typical evidence or signal |
| --- | --- | --- |
| Correctness | The artifact is true to source, repo state, user request, product behavior, and canon. | Direct source/repo inspection, tests, reviewed facts, no contradicted claims. |
| Completeness | The artifact covers the required scope without important omissions. | Acceptance criteria covered, required states/claims/files addressed. |
| Relevance | The artifact answers the actual task rather than a generic adjacent task. | Objective, audience, outcome, and deliverable match the brief. |
| Actionability | The reader can decide, implement, review, approve, publish, or proceed. | Clear next action, owner, boundaries, acceptance criteria, or decision point. |
| Clarity | The artifact is understandable at the intended reader's expertise level. | Plain structure, defined terms, no avoidable ambiguity. |
| Precision | Claims, instructions, boundaries, and terminology are specific enough to act on. | Concrete file paths, exact constraints, scoped claims, no vague absolutes. |
| Consistency | The artifact does not conflict with itself, canon, active task state, or related artifacts. | Manifest/status/plan alignment, terminology consistency, no route contradictions. |
| Traceability | Important claims, decisions, and changes can be followed back to evidence or artifacts. | Source pointers, diff references, claims-used, review findings, decision frame. |
| Evidence support | Material conclusions have evidence and confidence appropriate to the output type. | Evidence class, confidence label, assumptions, unknowns, validation needed. |
| Analytical rigor | Reasoning from question to conclusion is inspectable when complexity, ambiguity, or decision impact is material. | Analytical question, hypotheses, key assumptions, contradiction handling, disconfirmation checks, sufficiency judgment. |
| Audience fit | Detail, tone, format, and evidence depth match the intended reader and outcome. | Alignment note, reader context, useful omissions, action path. |
| Structural coherence | Sections have distinct jobs and create a usable reading path. | Logical order, no duplicate sections, navigable layers for mixed audiences. |
| Maintainability | The artifact or system change remains easy to update, review, and extend. | One canonical owner, low duplication, stable terms, bounded scope. |
| Implementation readiness | Codex or an implementer can perform the work without guessing. | Repo path, files to inspect, allowed/forbidden changes, validation commands. |
| Reviewability | Review Agent can validate the artifact without excessive reconstruction. | Current artifact pointer, scope, evidence, quality priorities, open blockers. |

Local tasks may add a temporary quality attribute when the domain requires it,
but local additions must not create permanent canon unless a separate reviewed
system update promotes them.

## Quality Profile Pattern

Use this compact pattern when quality priorities are material:

```markdown
## quality profile
- priority attributes:
- accepted tradeoffs:
- must preserve:
- may relax:
- review focus:
```

The profile can live inside `brief.md`, `orchestration_plan.md`, production
notes, `review.md`, or `final_decision.md`. A one-line note is enough for simple
tasks. High-governance or multi-stage tasks may need more detail.

## Quality Tradeoffs

Quality tradeoffs should be handled deliberately, not hidden.

| Tradeoff | Handle by |
| --- | --- |
| Completeness vs brevity | Keep required scope; move optional detail to appendix, notes, or omit it. |
| Speed vs confidence | Ship only claims supported by available evidence; mark uncertainty or block high-risk claims. |
| Precision vs accessibility | Preserve exact meaning, then translate into reader-appropriate language. |
| Flexibility vs consistency | Allow task-local variation only when it does not create parallel canon or unclear terminology. |
| Exploration vs execution | Explore enough credible options, then commit to the smallest useful next action. |
| Elegance vs implementation value | Prefer a validated, bounded change over a beautiful abstraction with little task value. |
| Traceability vs readability | Keep reader-facing text clean while preserving evidence pointers where review/governance needs them. |
| Maintainability vs local optimization | Avoid local shortcuts that create duplicated rules, hidden dependencies, or future confusion. |
| Audience fit vs technical depth | Layer the artifact so decision-makers can act and implementers can still inspect detail. |

When a tradeoff matters, record the accepted tradeoff in the smallest existing
artifact that the next owner or reviewer will read.

## Task-Specific Priorities

Different task types emphasize different attributes. These are defaults, not a
rigid matrix.

| Task type | Usually highest priority | Commonly relaxed |
| --- | --- | --- |
| Codex implementation task | Implementation readiness, precision, actionability, validation readiness, repository awareness, reviewability. | Broad strategy, polish, exhaustive background. |
| Architecture recommendation | Correctness, maintainability, canon compatibility, evidence support, tradeoff visibility. | Brevity, immediate implementation detail when not requested. |
| Code review | Correctness, evidence support, precision, traceability, reviewability. | Completeness outside changed scope, stylistic preference. |
| Research summary | Evidence support, traceability, completeness of material findings, uncertainty visibility. | Persuasion, decorative structure. |
| Executive brief | Relevance, actionability, clarity, audience fit, tradeoff visibility. | Low-level technical detail unless it changes the decision. |
| Editorial article | Audience fit, clarity, structural coherence, evidence support, tone, relevance. | Exhaustive traceability in reader-facing copy when review artifacts preserve it. |
| Canonical documentation | Correctness, maintainability, consistency, precision, reviewability. | Narrative polish, task-local examples that duplicate canon. |

If priorities conflict, Chief Editor or the active owner should name the tradeoff
and choose the attribute that best serves the task outcome, evidence boundary,
and review need.

## Evaluation Guidance

Evaluate quality by asking:

1. Which attributes matter most for this task and audience?
2. Which attributes are explicitly less important?
3. What tradeoff was accepted, and why?
4. What evidence proves or weakens the priority attributes?
5. What quality loss could happen during the next handoff?
6. Can Review Agent validate the selected attributes from saved artifacts?

Do not assign numeric scores. Use findings such as `sufficient`, `weak`,
`missing`, `over-optimized`, or `blocked` when a label helps review or repair.

## Lifecycle Usage

- Intake: capture success cues, constraints, audience/outcome, and obvious
  quality priorities or conflicts.
- Planning: choose quality priorities and tradeoffs when they affect route,
  implementation slice, evidence depth, or artifact shape.
- Research: protect correctness, evidence support, traceability, and uncertainty
  visibility.
- Writing and UX writing: preserve the selected quality profile while shaping
  structure, language, detail, and actionability.
- Review: challenge whether the artifact optimized for the right attributes and
  whether any quality loss blocks approval.
- Finalization: preserve approved quality attributes; do not improve polish by
  removing precision, caveats, traceability, or actionability.

Quality preservation is especially important at handoff. Each handoff should
make visible any priority attribute that could be lost by the next role.

## Integration Points

### Task Object

Task state may expose quality priorities and accepted quality tradeoffs when
they materially affect routing, production, review, or finalization.

### Audience And Outcome Alignment

Audience fit is a quality attribute. `/kb/audience_outcome_alignment.md` owns
reader and outcome fit; this file owns the broader vocabulary for weighing it
against correctness, completeness, traceability, and other attributes.

### Evidence Framework

Evidence support and traceability are quality attributes. Evidence quality and
confidence labels remain owned by `/kb/editorial_evidence_framework.md`.

### Analytical Reasoning

Analytical rigor is a quality attribute when the artifact depends on problem
framing, decomposition, competing explanations, disconfirmation, contradiction
handling, or sufficiency judgment. `/kb/analytical_reasoning.md` owns the
practical reasoning moves; this file only names analytical rigor as a quality
that may matter for review and handoff.

### Planning And Option Evaluation

Planning should consider quality attributes when options optimize for different
things. The chosen option should make important quality tradeoffs visible.

### Failure Modes

When work is polished but unsupported, too complete to be usable, too elegant to
implement, or optimized for the wrong reader, use
`/kb/editorial_failure_modes.md` to recover at the smallest stage.

### Learning And Canon Evolution

Maintainability, reviewability, traceability, evidence support, and
implementation readiness help decide whether a task finding is worth preserving
as reusable learning. `/kb/editorial_learning_framework.md` owns the decision
to keep learning task-local, promote a pattern, update canon, or challenge stale
canon.

### Review Pipeline

The Review Pipeline remains the review gate. This framework gives Review Agent
shared vocabulary for quality findings; it does not create a second review
process.

## Codex Implementation Quality

A high-quality Codex implementation task is:

- repository-aware: active repo, forbidden paths, and source-of-truth files are
  explicit;
- implementation-focused: it asks for useful file changes or inspection, not
  process performance;
- appropriately scoped: the slice is small enough to validate and large enough
  to matter;
- technically precise: likely files, constraints, and non-goals are concrete;
- validation-ready: commands or manual checks are named;
- actionable: Codex knows the next step without inventing requirements;
- low ambiguity: assumptions, unknowns, and user-decision points are visible;
- high value: the change improves the repository more than it increases
  documentation or process weight;
- reviewable: deliver-back and diff expectations make review possible.

## Non-Goals

This framework does not:

- make every quality attribute mandatory;
- require numeric scoring;
- add a quality reviewer role;
- add a mandatory quality checklist;
- replace audience, evidence, planning, failure recovery, lifecycle, or review
  canon;
- justify polishing when the task needs evidence, implementation, repair, or
  review.
