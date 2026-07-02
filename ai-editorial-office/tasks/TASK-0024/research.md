# Research

## research scope

This research analyzes the editorial system's behavior across accumulated
task-local artifacts. It does not evaluate individual text quality as an end in
itself and does not modify the system.

Primary questions:

- how reliably the system understands work before producing;
- how Chief Editor routes pipeline, depth, research, and artifact scope;
- what writing defects recur;
- what review catches and misses;
- which mechanisms create practical value;
- which repeated failures should drive the next system improvements.

## executive synthesis

The editorial system has moved from a capable but inconsistent local writing
workflow into a usable early-production editorial operating model. Its strongest
behavior is not "better prose"; it is the ability to preserve boundaries:
source boundaries, claim boundaries, role boundaries, review boundaries, and
publication/governance boundaries.

The current mature workflow performs well when a task enters through the full
editorial gate. In `TASK-0003` through `TASK-0008` and `TASK-0021` through
`TASK-0023`, the system usually identifies audience, reader state, source
limits, process depth, review requirements, and final decision boundaries. The
best examples show real editorial intelligence: `TASK-0008` diagnoses a
communication architecture failure instead of merely rewriting; `TASK-0004B`
uses structure-before-writing to improve selective reading; `TASK-0002` keeps
unknown audience/channel information explicit and constrains writing instead of
pretending the brief is complete.

The main weakness is uneven application. The corpus contains a clear split:
formal-cycle tasks are well governed, while direct/sparse tasks (`TASK-0011` to
`TASK-0019`, parts of `TASK-0010` and `TASK-0012` to `TASK-0015`) have useful
outputs but weak restartability, weak review evidence, and little trace of how
decisions were made. The system has since added governance defenses against this,
but the historical pattern matters: without entry discipline, the editorial
system can still behave like a capable direct producer rather than an editorial
organization.

## maturity assessment

Current maturity: advanced MVP / early production.

The system is beyond prototype because it has:

- repeatable roles;
- task-local artifacts;
- review gate;
- final governance decisions;
- source-boundary and claim-boundary behavior;
- compact-mode behavior for small tasks;
- maintenance evidence showing learning from prior failures.

It is not yet mature production because:

- entry discipline has not been uniformly applied across the corpus;
- artifact depth still needs tighter budgeting;
- review sometimes checks the artifact more than the original user outcome;
- final readiness is well disclaimed, but publication/user-action readiness can
  still depend on unresolved placeholders, links, or approvals;
- some newer compact tasks reduce artifact bloat successfully, but the policy is
  still behaviorally young.

## intake findings

Strong intake behavior appears when briefs explicitly capture:

- reader state;
- task goal;
- source boundary;
- forbidden assumptions;
- success criteria;
- unknowns.

Examples:

- `TASK-0002` preserves unknown audience, channel, length, and publication scope,
  then routes research before writing.
- `TASK-0004` identifies role-based reader tasks and likely drop-off points.
- `TASK-0006` records canonical source materials and launch constraints.
- `TASK-0022` states a strict source boundary: rewrite only the answer in
  `task.md`, without new promises or commitments.

Weak intake behavior appears in two forms:

1. Sparse or absent intake in direct tasks. `TASK-0011` to `TASK-0019` often
   contain outputs without a saved brief, manifest, plan, status, or review.
2. Inferred context becomes operational. `TASK-0023` assumes an
   internal/publication-style audience from the interview context. That is
   reasonable, but the evidence shows why the newer normalized-brief contract is
   important: inferred context must remain labeled as inferred unless confirmed.

Repeated missing data:

- exact publication channel;
- actual audience segment;
- approval owner;
- live links or access paths;
- internal examples;
- exact product/process behavior;
- success criteria beyond "make it clearer".

The mature system often handles missing data safely by constraining scope, but
the direct-production layer often leaves no evidence that the missing data was
noticed.

## Chief Editor findings

Chief Editor decisions are strongest when they treat process depth as a risk
decision, not as a default template.

Good decisions:

- Require research and claim traceability for AI-workflow articles in
  `TASK-0001` and `TASK-0002`.
- Omit external research for source-contained rewrites and launch materials in
  `TASK-0004B`, `TASK-0005`, `TASK-0006`, `TASK-0021`, and `TASK-0022`.
- Use social pipeline for short announcements and launch communication.
- Use compact depth in later tasks while preserving review.
- Add structure-before-writing for operational instructions after earlier
  structure problems.
- For `TASK-0020`, use visual concept, sketchnote brief, image prompt, and
  review rather than a raw PDF-to-image path.

Weak decisions:

- Early full-cycle tasks sometimes became heavy. `TASK-0001` is valuable as a
  lifecycle validation run, but its artifact depth is too large for routine use.
- Some low-risk social tasks still carried separate QA, review summary,
  finalization notes, and many handoffs when embedded review would have been
  enough.
- Some transition tasks produced strong editorial artifacts without full routing
  evidence, especially `TASK-0009` and `TASK-0010`.
- Visual precursor tasks before `TASK-0020` show direct production without the
  semantic ownership path that later became necessary.

## research findings

Research creates high value when factual or causal claims matter. In
`TASK-0001` and `TASK-0002`, research separates facts, interpretations,
assumptions, generic scenarios, and blocked claims. Review then has something
concrete to check.

Research is correctly omitted when the source is authoritative and closed:

- rewriting supplied instructions;
- launch communication using canonical task-local sources;
- source-contained interview adaptation;
- short follow-up email with user-supplied access steps.

The risk is not "too little research" in mature tasks. The bigger risk is
research-shaped work being absent where there is no formal task package. In
direct tasks, the system may still reason well, but the evidence trail does not
prove it.

## writing findings

Recurring writing risks are stable across the corpus:

- abstract intent before operational meaning;
- answer delay;
- generic but pleasant copy;
- HR/corporate optimism;
- synthetic editorial warmth;
- unsupported certainty;
- over-explanation;
- duplicated process explanation;
- insufficient concrete examples when source material is thin.

The system has learned to counter these risks:

- `TASK-0005` rewrites values like trust, involvement, and flexibility into
  concrete work situations.
- `TASK-0006` separates email and messenger reading modes.
- `TASK-0007` treats openings as usefulness tools, not style decoration.
- `TASK-0008` refuses to create one "better text" and instead rebuilds artifact
  architecture.
- `TASK-0003B` corrects synthetic editorial tone after user feedback.

The most common writing defect that survives into review is not bad prose. It
is a small but material meaning drift: a frequency claim, a productivity
implication, a motivational phrase, an abstract benefit, or a sentence that
sounds better than the evidence allows.

## review findings

Review is strong at:

- claim discipline;
- unsupported certainty;
- source-boundary violations;
- role/channel mismatch;
- fake warmth and corporate tone;
- sequence ambiguity in instructions;
- answer delay;
- operational usefulness;
- finalization and publication boundary disclaimers.

Review is weaker at:

- catching original task misunderstanding when the brief itself is already too
  narrow or inferred;
- challenging Chief Editor's process-depth choice;
- validating whether all necessary user data was gathered before work;
- consistently distinguishing review from self-check in compact literary tasks.

`TASK-0008` is the best positive counterexample: review checks the diagnostic
package against the communication problem, not just against prose polish.
`TASK-0023` is the cautionary example: the review artifact is useful, but its
framing as "editorial self-check" makes the independence signal weaker than in
more mature review artifacts.

## finalization findings

Final decisions are one of the system's strongest mechanisms. They repeatedly
separate:

- editorial readiness from publication approval;
- local task completion from stakeholder approval;
- final artifact existence from live delivery readiness;
- link placeholders from executable communication.

This appears in `TASK-0001`, `TASK-0006`, `TASK-0009`, `TASK-0021`,
`TASK-0022`, and `TASK-0023`.

The remaining risk is practical rather than editorial: the system can deliver a
ready text with placeholders or unresolved external decisions. It usually says
so, but future task routing should make "ready to use as-is" versus
"editorially ready after human insertion/approval" more visible at intake and
review, not only final decision.

## key behavioral conclusion

The system's highest-value behavior is disciplined interpretation: it asks what
the material is for, who must act, what is known, what is inferred, what must not
be invented, and what kind of review is needed.

The highest-risk behavior is premature confidence: starting production without
enough confirmed context, choosing a plausible but synthetic editorial angle,
or treating a useful direct output as if it had the same governance reliability
as a reviewed task package.
