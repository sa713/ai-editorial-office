# Audience & Outcome Alignment Framework

This file is the canonical owner for audience identification, intended
outcome, reader context, Reader Outcome Contract, required action or decision,
required depth, tone and language fit, artifact success criteria, mismatch
warning signs, and correction patterns in AI Editorial Office.

It prevents generic good text by forcing each artifact to serve a specific
reader and outcome. It is not a persona system, marketing framework, new role,
workflow engine, review gate, scoring rubric, or mandatory standalone artifact.

## Core Principle

An editorial artifact is successful only when the intended audience can use it
for the intended decision, action, understanding, or publication context.

Good alignment answers:

- who the output is for;
- what they already know or need assumed away;
- what they must decide, do, approve, understand, challenge, or publish;
- what evidence depth and detail level they need;
- what tone, structure, language, and format help them act;
- what should be omitted because it distracts, overburdens, or misleads them;
- what would make the artifact useful, and what would make it useless.

Audience and outcome may be explicit, inferred, unknown, or task-specific. When
missing or uncertain audience/outcome can materially change the artifact, record
it as a question, assumption, constraint, or blocker instead of filling it with
a generic reader.

## Reader Outcome Contract

For material reader-facing work, audience identification is not enough. Record
the smallest contract that makes the intended reader change reviewable:

```markdown
## reader outcome contract
- reader starting state:
- required change in understanding, decision, or practice:
- practical result after use:
- failure signal:
- evidence and precision guardrails:
```

The contract answers four different questions:

1. What does this reader already know, believe, use, or misunderstand?
2. What must be different after the artifact is used?
3. What observable decision, action, explanation, or working habit should the
   artifact enable?
4. What result would be correct in content but still useless for this reader?

Use the contract for teaching, explanation, change communication, decision
support, implementation guidance, or other work where a generic audience label
does not make success reviewable. Keep it compact for short or low-risk work.
Use `not applicable` with a reason when the task has no material reader change.

Reader value is bounded by evidence. The contract may change structure,
examples, detail, product bridge, chronology, or action path, but it may not
weaken correctness, source boundaries, neutrality, traceability, uncertainty,
review independence, or required caveats.

The Reader Outcome Contract normally lives in `brief.md`,
`orchestration_plan.md`, production notes, or `review.md`. It is not a new role,
pipeline, review gate, score, persona document, or mandatory standalone file.

## Reader Model Function

Reader Model is a shared process function for `Teach`, `Understand`, complex
explanation, change communication, and other tasks where prior knowledge or an
old mental model materially affects success. It is not a standing role.

Use the smallest useful model:

- known starting knowledge or practice;
- old, incomplete, or misleading model to update;
- terms, examples, or assumptions the reader already has;
- likely point of confusion or overload;
- target model or action after the artifact.

The model must be grounded in the request, supplied context, prior task
evidence, or an explicit bounded assumption. Do not invent demographic,
psychological, motivational, emotional, or proficiency details. If uncertainty
could materially change the artifact, ask, constrain, or mark the assumption.

Responsibility stays distributed:

- Intake Agent captures or conservatively infers the starting state;
- Chief Editor confirms the transition and route;
- Writer Agent realizes the transition in structure, examples, and action;
- Review Agent challenges whether the intended reader can make the transition;
- Final Editor preserves the approved transition during controlled
  finalization.

Record Reader Model only in existing task artifacts. A separate reader-model
file requires a distinct downstream or governance need and is never the
default.

## Alignment Pattern

Use this pattern at intake, routing, production, review, and finalization when
audience fit affects the result. Record it only as deeply as the task requires.
When reader change is material, use it together with the Reader Outcome
Contract.

1. Who is this for?
2. What do they already know?
3. What must they decide, do, approve, challenge, publish, or understand?
4. What constraints matter to them: time, expertise, risk, authority, channel,
   accessibility, governance, or implementation boundary?
5. What evidence do they need to trust or act on the artifact?
6. What format, structure, and level of detail helps them act?
7. What tone and language fit their context without hiding uncertainty?
8. What should be omitted because it is noise, premature, too technical, too
   shallow, too abstract, or outside scope?
9. What would make the output successful or useless?

The pattern usually lives inside `brief.md`, `orchestration_plan.md`, production
notes, `review.md`, or `final_decision.md`. Create a separate artifact only
when downstream review, restartability, governance, or a multi-audience task
needs it.

## Audience Classes

Audience classes are reusable defaults, not rigid personas. A task may define a
custom audience when these classes are too broad.

| Audience class | Typical needs | Common risks | Output implications |
| --- | --- | --- | --- |
| Executive decision-maker | Decision, risk, options, recommendation, business impact, approval boundary. | Too much implementation detail; hidden caveats; no clear ask. | Lead with decision context, recommendation, evidence level, tradeoffs, and next decision. |
| Product owner | User value, scope, constraints, tradeoffs, acceptance criteria, sequencing. | Abstract strategy without implementable shape; missing product risk. | Connect recommendation to user outcome, release slice, dependencies, and success criteria. |
| Engineering team | Repository facts, implementation boundary, files, interfaces, validation, risks. | Vague direction; missing edge cases; hidden architectural assumptions. | Use concrete paths, current state, constraints, acceptance criteria, and validation commands. |
| Security team | Threat model, evidence, severity, controls, compliance, residual risk. | Understated risk; unsupported assurances; missing scope. | State evidence, confidence, affected surface, mitigations, unknowns, and approval needs. |
| Reviewer | Review target, scope, evidence, blockers, decision criteria, allowed outcome. | Missing artifact pointer; unclear version; findings become rewriting. | Provide checked artifacts, assumptions, evidence basis, and exact review questions. |
| Implementer / Codex | Goal, repository, context, files to inspect, allowed/forbidden changes, validation, deliver-back. | Strategy without executable boundary; missing success criteria; touching wrong path. | Use bounded instructions, source of truth, validation commands, exclusions, and expected value. |
| End user | Task completion, clarity, accessibility, product behavior, next action. | Internal terminology; unsupported promises; unclear state/action. | Use plain language, state-aware copy, helpful structure, and no invented product behavior. |
| Public reader | Accurate claims, context, relevance, credibility, readable structure. | Overclaiming; jargon; missing source basis; reputational risk. | Use source-backed claims, readable structure, caveats, and publication-safe tone. |
| Internal team | Alignment, shared context, decision record, responsibilities, next action. | Too polished but not operational; unclear ownership. | Make state, rationale, owner, blockers, and next action visible. |
| Mixed audience | Layered detail for readers with different needs. | One-size-fits-none; excessive length; contradictions between summaries and details. | Use layered structure: summary first, role-specific detail later, clear navigation. |

When the audience is mixed, choose the primary reader and define what secondary
readers need. Do not satisfy every reader by making the artifact longer unless
layered structure is the right answer.

## Outcome Types

Outcome types define what the artifact must enable. A task may combine outcomes,
but the primary outcome should stay visible.

| Outcome type | Artifact must enable |
| --- | --- |
| Decide | Choose between options with enough evidence, tradeoffs, and uncertainty visible. |
| Approve | Confirm readiness, risk, authority, and conditions for continuation, delivery, or closure. |
| Implement | Make a bounded change with clear files, constraints, acceptance criteria, and validation. |
| Review | Independently validate a named artifact or decision against clear criteria. |
| Understand | Build accurate mental model without requiring immediate action. |
| Align stakeholders | Create shared direction, vocabulary, constraints, and next ownership. |
| Challenge a proposal | Test assumptions, evidence, alternatives, and risks without becoming a new route owner. |
| Brief quickly | Convey the minimum useful context for a time-limited reader. |
| Publish | Produce public or external-facing material with source-backed claims and appropriate tone. |
| Teach | Help a reader learn or perform a repeatable task. |
| Persuade | Make a case while preserving evidence quality, caveats, and trust. |
| Document canon | Record durable system truth in the canonical owner without duplicating other canon. |

If the requested outcome is unclear, infer only when the task context makes the
outcome low-risk and reviewable. Otherwise ask, constrain, or state the working
assumption.

## Depth, Tone, And Format Fit

Detail level should follow the reader's decision burden, not the writer's desire
to be complete.

Use compact detail when the reader needs orientation, approval, or a next step.
Use standard detail when the reader must compare tradeoffs or perform work. Use
deep detail when review, governance, implementation, source traceability, or
high-risk decision-making requires reconstruction.

Tone should fit the reader's context and evidence quality:

- use direct, decision-ready language for executives and approvers;
- use precise, operational language for implementers, reviewers, and internal
  teams;
- use plain, accessible language for end users and public readers;
- preserve caveats when evidence is limited;
- avoid polish that hides uncertainty, missing action, weak evidence, or scope
  drift.

Format constraints may include length, section order, language, channel, code or
non-code output, copyability, accessibility, and whether the user needs a final
artifact or a decision packet.

## Mismatch Warning Signs

Use `/kb/editorial_failure_modes.md` when these warning signs appear:

- correct facts but wrong reader;
- no visible decision, action, or next step;
- too long for a decision-maker or too shallow for an implementer;
- too technical for a non-technical reader;
- too abstract for Codex or another executor;
- generic summary that could fit any task;
- polished prose that does not help the reader act;
- evidence depth lower than the audience's risk or authority requires;
- missing repository, file, validation, or boundary details for implementation;
- omitted caveats needed for trust;
- mixed-audience artifact with no layered reading path.

## Correction Patterns

Choose the smallest correction that restores usefulness:

- restate audience and intended outcome in the task object;
- select a primary reader when the audience is mixed;
- narrow the outcome from broad understanding to a specific decision or action;
- adjust detail level: shorten for decision, expand for implementation or
  review;
- move background below the recommendation or next action;
- add evidence, caveat, or validation only where the reader needs it;
- remove theory, future roadmap, or internal process that does not support the
  outcome;
- split artifact layers: summary, decision, implementation detail, appendix;
- return to intake or routing if the audience/outcome assumption could change
  the deliverable;
- request missing audience/outcome information only when it materially changes
  the result.

## Integration Points

### Task Object

Audience alignment may appear in optional task-object fields: audience,
intended outcome, reader context, required action or decision, format
constraints, detail level, tone requirements, and artifact success criteria.

### Editorial Decision Frame

When audience or outcome changes route choice, the Editorial Decision Frame
should record the reader/outcome assumption, selected route, rejected
alternatives, and reroute trigger.

### Evidence Framework

Evidence depth should match the audience's decision burden. A business or public
reader may need caveats and confidence; an implementer may need repository
inspection and validation; an end user may need product truth and no invented
behavior.

### Quality Attributes

Audience fit is one quality attribute among others. Use
`/kb/editorial_quality_attributes.md` when audience fit must be balanced against
correctness, completeness, brevity, traceability, implementation readiness, or
maintainability.

### Planning And Option Evaluation

Option evaluation should include audience/outcome fit when it affects the
selected approach. A technically elegant option can lose if it does not serve
the reader's decision or action.

### Failure Modes

Audience mismatch, outcome ambiguity, over-polishing, under-execution, and
implementation-task dilution should recover through
`/kb/editorial_failure_modes.md`.

### Shared Lifecycle

Intake captures or infers audience/outcome, Chief Editor routes by it, Writer
and UX Writer shape artifacts around it, Review Agent challenges mismatch, and
Final Editor preserves actionability and fit inside the approved scope.
When a Reader Outcome Contract is material, Review Agent records the
deterministic Reader Review Lens inside `review.md`; this does not create a new
role or artifact.

## Codex Audience Guidance

Codex is an implementer and executor audience. A good Codex task makes the next
repository action obvious and reviewable.

For Codex tasks, include:

- repository and forbidden paths;
- goal and expected value of the slice;
- current context and source of truth;
- implementation boundaries and non-goals;
- files or directories likely to inspect;
- validation commands;
- what to deliver back;
- what not to touch;
- assumptions, unknowns, or user-decision points that affect implementation.

Avoid vague strategy language, excessive theory, broad future roadmaps, missing
validation, hidden assumptions, unclear success criteria, and prompts that point
Codex at Studio or legacy paths when the canonical Editorial Office repository
is the active workspace.

## Role Cooperation

Audience and outcome alignment is shared work, not a new role.

| Role | Alignment responsibility |
| --- | --- |
| Intake Agent | Capture or conservatively infer audience, intended outcome, reader starting state, reader context, constraints, and success criteria. |
| Chief Editor | Confirm the Reader Model transition, route by intended outcome, choose depth, and require audience/outcome fit before production. |
| Writer Agent | Shape structure, examples, detail, tone, evidence, and next action so the approved reader transition is usable. |
| UX Writer | Shape product copy around user action, UI state, accessibility, and product truth. |
| Review Agent | Flag audience mismatch, broken reader transition, wrong depth, missing actionability, and generic useful-looking text. |
| Final Editor | Preserve the approved reader transition, audience fit, actionability, caveats, and format constraints during finalization. |

## Non-Goals

This framework does not:

- create personas for every task;
- create a Reader Model Agent or require a standalone reader-model file;
- require a Reader Outcome Contract when no material reader change is expected;
- require a separate audience brief artifact;
- replace the Task Object Model, Decision Frame, Evidence Framework, Planning
  Framework, Failure Modes Playbook, or Review Pipeline;
- make every output longer;
- let audience preference override evidence, source boundary, role separation,
  or review-gate;
- turn style work into proof of usefulness.
