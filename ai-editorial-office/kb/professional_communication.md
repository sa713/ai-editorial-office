# Professional Communication

This file owns practical Professional Communication guidance for AI Editorial
Office. It translates professional communication practice into lightweight
lenses for message architecture, recommendation presentation, explanation
quality, technical communication, information density, and actionability.

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
- compressed summary that removes uncertainty or overstates confidence;
- multi-audience artifact that satisfies no reader because all detail is
  flattened into one layer;
- polished prose that hides weak evidence, missing action, or scope limits;
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
- whether the correct outcome is `approved`, `changes_requested`, `blocked`, or
  escalation through the existing lifecycle.

## Role Cooperation

Professional Communication is shared work, not a new role.

| Role | Communication responsibility |
| --- | --- |
| Chief Editor | Select the capability when communication transfer quality materially affects route, depth, review, or governance. |
| Intake Agent | Capture or infer early signs that reader action, decision, channel, or density will shape communication. |
| Research Agent | Preserve evidence, confidence, unknowns, and source meaning for later communication. |
| Writer Agent | Shape draft message architecture, density, explanation, recommendations, and action path inside approved scope. |
| UX Writer | Preserve product-state action path and product truth; use this capability only when broader communication transfer is material. |
| Review Agent | Challenge communication failures inside existing `review.md` when material. |
| Final Editor | Preserve approved message path, actionability, caveats, density, and reader fit during finalization. |

## Non-Goals

Professional Communication does not:

- create a Professional Communicator, Communications Strategist, Technical
  Writer, Policy Writer, Science Communicator, Consultant, Editor, or Reviewer
  role;
- create a new pipeline, lifecycle stage, review gate, checklist system,
  communication score, consulting framework, documentation framework, or
  mandatory artifact;
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
