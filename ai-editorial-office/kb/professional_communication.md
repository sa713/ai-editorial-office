# Professional Communication

This file owns practical Professional Communication guidance for AI Editorial
Office. It translates professional communication practice into lightweight
lenses for message architecture, recommendation presentation, explanation
quality, learning design, technical communication, information density, and
actionability.

It is not a new role, grammar/style checklist, framework, pipeline, lifecycle
stage, review gate, workflow engine, scoring model, consulting methodology,
content-design system, UX-writing system, or mandatory artifact set. Use it
only when an artifact must transfer meaning, evidence, recommendation,
explanation, decision, or next action to a professional reader without meaning
loss or evidence loss.

## Purpose

Professional Communication helps agents make intellectual work usable by its
intended reader.

It helps agents:

- shape the message architecture and reading path;
- decide what goes first, what can be layered, and what can be omitted;
- present recommendations, asks, approvals, decisions, and next steps clearly;
- adapt explanations to reader expertise without flattening meaning;
- sequence teaching and explanation from the reader's current model to a usable
  new model or practice;
- communicate technical, policy, research, implementation, or governance work
  with appropriate precision;
- preserve evidence, confidence, caveats, assumptions, uncertainty, and
  residual risk when communication is compressed;
- keep communication strength inside the existing role, lifecycle, and review
  architecture.

## Relationship To Existing Capabilities

- Audience and Outcome Alignment owns who the reader is, what the artifact must
  enable, and the required detail/tone/format fit.
- Quality Attributes own quality vocabulary, priorities, accepted tradeoffs,
  and lifecycle quality preservation.
- Evidence Framework owns evidence classes, confidence labels, assumptions,
  unknowns, validation needed, and residual risk.
- Analytical Reasoning owns the reasoning moves behind conclusions.
- Professional Analysis owns analytical product shape, synthesis,
  recommendation justification, implications, and analytical judgment.
- Planning owns option generation, option evaluation, selected approach, and
  reconsideration triggers.
- Writer Agent and UX Writer own production within the approved route.
- Review Agent owns independent challenge through the existing review gate.

Professional Communication may consume these capabilities, but it does not
replace or become their owner.

## When To Use

Use Professional Communication when a task asks for or materially depends on:

- executive communication, briefing, release reporting, governance summary, or
  decision-maker communication;
- a recommendation, ask, approval request, decision memo, policy memo, or
  options communication where presentation affects action;
- technical explanation, engineering handoff, implementation note, system
  documentation, or Codex-ready instruction where precision and reader path
  matter;
- research or evidence communication where confidence, unknowns, limitations,
  and implications must survive compression;
- multi-audience or layered communication where readers need different depths;
- explanation of a complex concept, mechanism, rationale, tradeoff, risk, or
  decision;
- review of an artifact that is factually correct but hard to use, too dense,
  too shallow, poorly sequenced, missing action, or likely to mislead by
  omission.

Do not use Professional Communication for ordinary grammar cleanup, cosmetic
style polish, simple copyediting, low-risk rewriting, routine drafting,
Audience Alignment by itself, Quality Attribute selection by itself, Analytical
Reasoning by itself, Professional Analysis by itself, UX microcopy when UX
writing guidance is sufficient, or evidence assessment without a
communication-transfer problem.

## Communication Lenses

Select only the lenses that fit the task.

| Lens | Use when | Core questions |
| --- | --- | --- |
| Message architecture | The artifact needs a deliberate reading path. | What must come first, what can be layered, and what must not be buried? |
| Executive brief | A time-limited decision-maker needs the answer quickly. | What is the bottom line, ask, evidence level, risk, and next decision? |
| Recommendation or ask | The reader must approve, choose, fund, prioritize, or act. | What is recommended, why now, on what evidence, with what caveats, and what action follows? |
| Technical explanation | Technical work must be understood, implemented, or reviewed. | What problem, mechanism, boundary, requirement, validation, or rationale must be clear? |
| Implementation handoff | Another owner must continue work safely. | What changed, what matters now, what is next, what must not change, and where is the evidence? |
| Research or evidence communication | Evidence-heavy work must be compressed without overclaiming. | What is known, how confident are we, what is unknown, and what would change the view? |
| Policy or stakeholder memo | A policy, governance, or stakeholder reader needs decision context. | What issue, decision, evidence, tradeoff, implication, and implementation path matter? |
| Layered communication | Multiple readers need different depth. | What does every reader need first, and where does specialist detail belong? |
| Explanation fit | A concept, mechanism, or rationale must be learned or trusted. | What does the reader already know, what must be defined, and what sequence stabilizes understanding? |
| Learning design | The artifact must update a mental model or teach a repeatable practice. | What was true or believed before, what is true now, why did it change, which example makes it concrete, and what should the reader do? |
| Product-decision result | Active Product Intent Review must become a user-facing decision aid. | Is the verdict first, one main gap visible, next owner decision explicit, evidence boundary compact, consequence actionable, and internal methodology hidden? |

### Product-Decision Result

When Product Intent Review mode is `limited` or `full`, apply its reader-facing
contract from `/kb/product_intent_review.md` inside the selected deliverable.
Message architecture must put verdict, one main gap, and next owner decision
before analytical detail; production consequence must be visible; editorial
remarks follow the product decision.

Choose density from the reader job and decision stakes, not source length or
internal analysis depth. Preserve confirmed/hypothesis/unknown distinctions
without repeating the same disclaimer. Use direct language for no-build, stop,
reroute, and validate-first findings. Do not expose role names, pipelines,
task-state mechanics, canonical owners, or an internal method inventory unless
the reader explicitly needs system documentation.

This is a conditional communication lens, not a new deliverable, template,
pipeline, review gate, or mandatory standalone artifact.

## Professional Communication Pattern

Use this compact pattern inside the smallest existing artifact when
Professional Communication is material:

```markdown
## professional communication
- communication job:
- reader and use context:
- message architecture:
- bottom line or primary transfer:
- required evidence and confidence cues:
- detail and density choice:
- recommendation, ask, or next action:
- caveats, assumptions, or uncertainty to preserve:
- reader path or layering:
- stop/review concern:
```

For compact tasks, this may be one paragraph or a few bullets. Do not create a
standalone Professional Communication artifact unless the selected task depth,
review need, or governance need justifies it.

## Reader Model And Learning Design

Audience & Outcome Alignment owns the Reader Model and Reader Outcome Contract.
Professional Communication owns the explanation sequence used to realize them.

For teaching, understanding, and complex explanation, consider this conditional
pattern:

```text
раньше -> сейчас -> почему -> пример -> что делать
```

- `раньше`: name the reader's prior model or practice without caricaturing it;
- `сейчас`: state the updated model or current practice;
- `почему`: explain the change, mechanism, evidence, or tradeoff;
- `пример`: make the difference concrete with a supported example;
- `что делать`: translate the new model into an action, decision, or habit.

The pattern is not a mandatory five-part outline. Combine, reorder, or omit
parts when another sequence better serves the reader. Do not force chronology
into a task that needs an action-first, problem-first, reference, decision, or
implementation structure. Examples must stay inside the source boundary; an
illustrative example must be labeled and must not invent product behavior.

Learning Design is complete only when the Cognitive Bridge is usable, the
Moments of Insight are actually expressed, and Practical Transformation is
specific enough to review. It does not create a Learning Designer role,
pipeline, score, stage, or standalone artifact.

## Companion Pass

Companion Pass is the last communication check inside the existing review
before reader-facing material can receive `approved`. It asks:

> Could a knowledgeable colleague explain this to the intended reader in this
> way, naturally and directly, without losing precision?

Use `pass`, `fail`, `not applicable`, or `needs clarification` for:

- naturalness: sentences sound like purposeful explanation rather than a
  template, taxonomy dump, or performance of expertise;
- concreteness: abstractions are connected to supported examples, decisions,
  actions, or consequences when needed;
- distance: jargon, nominalization, formalism, and academic framing do not
  create avoidable distance from the intended reader;
- precision preservation: simplification retains evidence, boundaries,
  caveats, uncertainty, technical meaning, and traceability.

This is not an invitation to add fake empathy, invented familiarity, jokes,
sales language, or an ungrounded conversational persona. It cannot authorize
new facts or meaning changes. If passing it requires substantive rewriting,
Review Agent returns bounded repair to Writer Agent; Final Editor must not use
finalization to perform that rewrite.

## Good Professional Communication Criteria

Good Professional Communication is:

- reader-useful rather than writer-centered;
- message-led rather than chronology-led when a decision or action is needed;
- clear about what the reader must decide, do, approve, review, or understand;
- structured so the main point, evidence, caveats, and action are findable;
- dense enough to preserve meaning and sparse enough to avoid overload;
- precise about technical, policy, product, or governance boundaries;
- honest about evidence confidence, assumptions, unknowns, and residual risk;
- layered when audiences differ;
- specific about next action, owner, decision, implementation, or review need;
- aligned with existing evidence, analysis, quality, audience, and role
  boundaries.

## Common Communication Failures

Use `/kb/editorial_failure_modes.md` when these warning signs appear:

- correct facts but no usable message path;
- conclusion or recommendation buried below background;
- executive summary that has no decision, ask, risk, or next step;
- recommendation without evidence level, implementation path, or caveat;
- technical explanation that assumes hidden knowledge or uses local jargon
  without defining it;
- documentation that mixes tutorial, how-to, reference, and explanation in a
  way that interrupts the reader's task;
- explanation that presents only the new model and makes the reader infer why
  the old model no longer works;
- abstract teaching with no supported example or usable next practice;
- compressed summary that removes uncertainty or overstates confidence;
- multi-audience artifact that satisfies no reader because all detail is
  flattened into one layer;
- polished prose that hides weak evidence, missing action, or scope limits;
- reader-facing prose that is correct but sounds like an academic checklist,
  taxonomy dump, or synthetic expert performance instead of a direct
  explanation;
- handoff that is pleasant to read but does not let the next owner proceed.

## Stop Conditions

Stop, route repair, or block when:

- the reader, use context, or required action is unclear enough to change the
  communication path;
- the artifact communicates a different decision, recommendation, or task from
  the approved route;
- the main point, ask, recommendation, or next action is missing or buried when
  action is required;
- compression hides evidence limits, assumptions, uncertainty, residual risk, or
  material caveats;
- a recommendation is presented more strongly than Professional Analysis or
  available evidence supports;
- technical terms, requirement levels, product behavior, file paths, validation,
  or implementation boundaries are ambiguous enough to mislead;
- the communication is being polished instead of repaired for evidence,
  structure, actionability, or reader fit;
- UX copy needs product-state or accessibility decisions owned by UX Writer;
- Review Agent cannot reconstruct what the reader is supposed to understand,
  decide, trust, or do.

## Completion Criteria

Professional Communication is complete for a task when the reviewing role can
state:

- what communication job was material;
- who needed to use the artifact and for what action, decision, review,
  implementation, approval, or understanding;
- what message architecture and density choices were made;
- where the bottom line, evidence level, caveats, and next action are visible;
- whether recommendations or asks stay within the evidence and approved
  analysis;
- whether technical or specialist detail is precise enough for its reader;
- whether uncertainty, assumptions, and residual risk survived compression;
- whether material teaching connects the old/current model to the updated
  model, makes the transition concrete, and enables the approved practical
  transformation;
- whether Companion Pass is complete for reader-facing material without
  trading precision for warmth or ease;
- whether the correct outcome is `approved`, `changes_requested`, `blocked`, or
  escalation through the existing lifecycle.

## Role Cooperation

Professional Communication is shared work, not a new role.

| Role | Communication responsibility |
| --- | --- |
| Chief Editor | Select the capability and Learning Design lens when communication transfer or reader change materially affects route, depth, review, or governance. |
| Intake Agent | Capture or infer early signs that reader starting state, action, decision, channel, or density will shape communication. |
| Research Agent | Preserve evidence, confidence, unknowns, and source meaning for later communication. |
| Writer Agent | Shape draft message architecture, density, explanation, supported examples, reader transition, recommendations, and action path inside approved scope. |
| UX Writer | Preserve product-state action path and product truth; use this capability only when broader communication transfer is material. |
| Review Agent | Challenge communication failures, apply Reader Review when material, and run Companion Pass for reader-facing material inside existing `review.md`; taste alone is not a finding. |
| Final Editor | Preserve approved message path, Companion Pass balance, actionability, caveats, density, and reader fit during finalization; do not perform substantive companion rewriting. |

## Non-Goals

Professional Communication does not:

- create a Professional Communicator, Communications Strategist, Technical
  Writer, Policy Writer, Science Communicator, Consultant, Editor, or Reviewer
  role;
- create a new pipeline, lifecycle stage, review gate, checklist system,
  communication score, consulting framework, documentation framework, or
  mandatory artifact;
- create a Learning Designer role or force the learning pattern onto every
  artifact;
- create a Companion Agent, stage, gate, score, or standalone artifact;
- replace Writer Agent, UX Writer, Review Agent, Audience Alignment, Quality
  Attributes, Evidence Framework, Analytical Reasoning, Professional Analysis,
  Planning, Architecture Review, Engineering Review, or Failure Modes;
- make every output executive-style, short, persuasive, polished, or
  recommendation-led;
- make recommendations when the evidence supports only caveats, options, or a
  request for more information;
- turn communication into brand voice, PR, marketing, campaign, media, crisis,
  oral presentation, negotiation, facilitation, localization, or accessibility
  strategy;
- remove caveats, uncertainty, technical precision, source boundaries, or
  reviewability for the sake of smoother prose.
