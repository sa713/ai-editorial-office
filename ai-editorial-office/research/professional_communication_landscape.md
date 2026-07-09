# Professional Communication Landscape

Date: 2026-07-09

## Purpose

This research landscape identifies professional communication practices that
can strengthen AI Editorial Office without duplicating Writer Agent, UX Writer,
Audience and Outcome Alignment, Quality Attributes, Analytical Reasoning, or
Professional Analysis.

The release question is not "how do we make prose nicer?" It is:

```text
How should the system help intellectual work transfer to a reader so the
reader can understand, decide, review, implement, recommend, or act without
meaning loss, evidence loss, or decision-quality loss?
```

## Source Base

The research used primary or authoritative sources where possible:

| Source | Domain | Why it matters |
| --- | --- | --- |
| [Digital.gov Plain Language Guide Series](https://digital.gov/guides/plain-language) | plain language / government communication | Connects public-facing communication to audience-specific understanding and the Plain Writing Act. |
| [CDC Clear Communication Index](https://www.cdc.gov/ccindex/index.html) | public health / risk communication | Research-based tool with scored items for main message, action, numbers, risk, and unknowns. |
| [GOV.UK content design: understand content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/) | content design / public service communication | Defines content around user need, format, publication place, accessibility, and maintenance. |
| [GOV.UK content design: identify user needs](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/) | user-need communication | Gives a task/action-oriented model for defining the reader need and acceptance criteria. |
| [GOV.UK plan new content](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/plan-new-govuk-content/) | policy and service communication | Separates mainstream and specialist guidance, campaign communication, and task-focused content. |
| [Google Developer Documentation Style Guide](https://developers.google.com/style) | technical documentation | Establishes project-specific hierarchy, clarity, consistency, audience fit, and style as reference rather than universal truth. |
| [Google Technical Writing One: Audience](https://developers.google.com/tech-writing/one/audience) | technical writing | Defines documentation as the gap between what a reader needs to do a task and what they already know. |
| [Google Technical Writing One](https://developers.google.com/tech-writing/one) | technical writing | Teaches scope, audience, key points first, sectioning, clear sentences, and terminology consistency. |
| [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) and [Top 10 tips](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice) | technology communication | Emphasizes simple, direct, reader-helpful technology communication and fast next-step visibility. |
| [MIT Communication Lab policy memo](https://mitcommlab.mit.edu/broad/commkit/policy-memo/) | policy / executive communication | Provides a decision-reader memo pattern: bottom line, concise background, evidence, recommendation, implementation. |
| [MIT Communication Lab scientific writing tips](https://mitcommlab.mit.edu/broad/commkit/general-tips/) | scientific communication | Emphasizes main message, logical structure, expert/novice adaptation, and jargon control. |
| [MIT Communication Lab coding mindset](https://mitcommlab.mit.edu/broad/commkit/coding-mindset/) | engineering communication / documentation | Connects code documentation to problem statement, methodology, rationale, and maintainability. |
| [Diataxis](https://diataxis.fr/) and [Diataxis quality](https://diataxis.fr/quality/) | documentation architecture | Separates tutorials, how-to, reference, and explanation by user need, and distinguishes functional quality from deeper human fit. |
| [RFC 2119](https://www.rfc-editor.org/info/rfc2119/) and [RFC 8174](https://www.rfc-editor.org/info/rfc8174/) | standards communication | Shows how requirement language reduces ambiguity when used carefully and sparingly. |
| [ICMJE Recommendations](https://www.icmje.org/recommendations/) | scholarly communication | Defines reporting, editing, authorship, publication, corrections, and responsible communication norms for medical journals. |
| [EQUATOR reporting-guideline toolkit](https://www.equator-network.org/toolkits/developing-a-reporting-guideline/) | scientific reporting transparency | Treats reporting guidance as structured tools that help work be understood, replicated, used for decisions, and included in review. |
| [Nature reporting standards](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards) | scientific reproducibility / transparency | Requires disclosure of data, materials, code, protocols, and restrictions so readers can replicate and build on claims. |

## Cross-Domain Findings

### 1. Professional communication is transfer design

Across sources, strong communication starts from the reader's use of the
information. Plain language sources tie success to a specific audience's ability
to understand and use content. GOV.UK content design starts with user needs and
publishing context. Google technical writing defines useful documentation by
what the audience needs to know or do minus what they already know. Diataxis
organizes documentation around distinct user needs.

Implication:

Professional Communication should help agents design the transfer from
intellectual work to reader use. It should answer:

- What must be transferred?
- To whom?
- For what decision, action, review, implementation, or understanding?
- At what level of detail and evidence?
- In what order, density, and form?

It should not own the audience definition itself. That remains Audience and
Outcome Alignment.

### 2. Decision readers need the answer early

MIT policy memo guidance is explicit: start with the most important
recommendations, provide concise background, prioritize evidence that supports
the recommendation, and include implementation. Microsoft's guidance similarly
pushes "get to the point fast", front-load keywords for scanning, and make next
steps obvious. CDC's index includes main message location and call to action as
core communication features.

Implication:

Professional Communication should include a decision-first or message-first
lens for executive summaries, recommendations, memos, release reports, reviews,
and governance decisions. This is not the same as Professional Analysis making
the recommendation. It is the way the justified recommendation is presented so
the reader can act on it.

### 3. Structure carries meaning

GOV.UK separates guidance for mainstream users, specialist users, policy
information, and campaign communication. Diataxis separates tutorials, how-to,
reference, and explanation. Google technical writing asks writers to define
document scope and break long topics into appropriate sections. MIT scientific
writing emphasizes logical order based on conclusions and reader path, not only
the chronology of work.

Implication:

Professional Communication should own message architecture and reading path:
summary first when needed, evidence after conclusion when the reader must
decide, procedural order when the reader must act, conceptual order when the
reader must understand, and layered detail for mixed audiences.

This complements, but does not replace, Writer Agent. Writer Agent drafts;
Professional Communication provides a shared capability for preserving
reader-useful structure across roles and artifacts.

### 4. Information density is a professional choice

CDC's index emphasizes one main message, chunking, headings, summarized
important information, and separate communication of what is known and unknown.
MIT policy memo guidance warns that excessive numerical detail can overwhelm or
obscure the take-away. Microsoft emphasizes brief, useful wording. Google
technical writing warns against the curse of knowledge and asks writers to
calibrate vocabulary and detail to the audience's current knowledge.

Implication:

Professional Communication should help agents tune density:

- compact enough for the reader's time and task;
- detailed enough for trust, review, implementation, or decision quality;
- layered enough when multiple readers need different depths;
- not simplified so far that caveats, uncertainty, or evidence disappear.

This complements Quality Attributes, which owns tradeoff vocabulary.
Professional Communication owns the practical communication move of layering,
ordering, and compressing without meaning loss.

### 5. Recommendations need an action path

MIT policy memo guidance links recommendations to implementation. CDC's index
separates main message from behavioral recommendation and specific direction.
GOV.UK user needs are action/task oriented, and acceptance criteria define when
the need is met. Microsoft calls for visible choices and next steps.

Implication:

Professional Communication should include recommendation presentation:

- recommendation or ask;
- why now;
- evidence level;
- decision owner or reader action;
- implementation or next step;
- risks, caveats, and alternatives only at the level the reader needs.

Professional Analysis still owns whether the recommendation is justified.
Professional Communication owns whether the recommendation can be understood,
trusted, and acted on.

### 6. Explanations must match expertise and task

Google's audience guidance treats role as a first approximation and then adds
proximity to the subject. It warns experts against hidden assumptions and
unexplained concepts. MIT scientific writing distinguishes expert and novice
readers: experts can handle less background and more nuance; novices need
motivation, definitions, and accessible framing. Diataxis distinguishes
explanation from how-to and tutorial.

Implication:

Professional Communication should include explanation quality:

- what concept, decision, mechanism, or rationale must be explained;
- what prior knowledge can be assumed;
- what must be defined;
- what sequence makes the mental model stable;
- what detail would distract from the reader's task.

This does not duplicate Analytical Reasoning. Analytical Reasoning owns the
reasoning moves. Professional Communication owns making the explanation
usable by the intended reader.

### 7. Technical communication needs precision without local jargon

Google and Microsoft both stress clear, consistent terminology and
reader-appropriate vocabulary. RFC 2119/8174 show a mature example of
normative words carrying exact requirement levels only when defined and used
with care. MIT coding mindset connects documentation to the problem solved,
methodology, rationale, and where to inspect relevant code. Nature and EQUATOR
show that scientific and technical claims need enough reporting detail for
review, reuse, replication, or downstream decision-making.

Implication:

Professional Communication should include technical communication as a lens:

- define terms, abbreviations, and requirement levels;
- distinguish fact, requirement, recommendation, option, risk, and rationale;
- preserve exact boundaries while reducing unnecessary jargon;
- point implementers or reviewers to the evidence, file, method, or validation
  that lets them act.

This complements Engineering Review. Engineering Review owns change safety.
Professional Communication owns how implementation-relevant meaning is
communicated.

### 8. Scientific and evidence-heavy communication depends on transparency

ICMJE, EQUATOR, and Nature focus on transparent reporting, reproducibility,
availability of data/materials/code/protocols, and disclosure of restrictions.
CDC includes "what we know and don't know" among clear communication items.

Implication:

Professional Communication should preserve evidence visibility, uncertainty,
and limitations when communicating research or recommendations. It should never
compress away confidence, unknowns, validation need, or residual risk when the
reader's decision depends on them.

This complements the Evidence Framework. The Evidence Framework owns evidence
classes and confidence labels. Professional Communication owns how those
evidence cues are exposed to the reader.

## Domain-Specific Practice Patterns

### Executive communication

Professional pattern:

- Lead with the decision, recommendation, ask, or bottom line.
- Explain significance quickly.
- Give only the evidence needed to decide, with confidence and risk visible.
- Separate decision from implementation detail.
- Make the required action, approval, or next decision explicit.

Best fit in AI Editorial Office:

- release reports;
- executive summaries;
- recommendation memos;
- governance decisions;
- review summaries;
- user-facing delivery notes when the user is a decision-maker.

### Technical and engineering communication

Professional pattern:

- State the problem or task boundary before the mechanism.
- Define terms and requirement levels.
- Put commands, paths, interfaces, states, validation, and constraints where
  implementers can find them.
- Explain non-obvious rationale, not obvious mechanics.
- Preserve exactness while using reader-appropriate language.

Best fit in AI Editorial Office:

- Codex tasks;
- implementation reports;
- engineering review notes;
- documentation;
- architecture or configuration explanations;
- handoffs to implementers or reviewers.

### Consulting and recommendation communication

Professional pattern:

- Make the answer or recommendation visible early.
- Connect recommendation to issue, evidence, criteria, tradeoffs, risks, and
  implementation.
- Show alternatives only to the depth needed for trust and choice.
- Explain implications and next steps.

Best fit in AI Editorial Office:

- recommendation sections;
- options memos;
- product or operating-model advice;
- Project Lead review packets;
- decision support artifacts.

### Policy communication

Professional pattern:

- State the policy question or decision context.
- Separate background from evidence.
- Prioritize the evidence that changes the decision.
- Show implementation consequences and caveats.
- Keep specialist detail available without making the main memo unreadable.

Best fit in AI Editorial Office:

- policy notes;
- governance decisions;
- high-governance communication;
- public-facing or stakeholder-sensitive explanations.

### Scientific communication

Professional pattern:

- State the main finding and its significance.
- Match background and terminology to expert/novice mix.
- Preserve methods, data, limitations, uncertainty, and reproducibility signals
  when material.
- Do not make a claim stronger than the reporting basis supports.

Best fit in AI Editorial Office:

- research summaries;
- evidence reviews;
- source-backed claims;
- high-sensitivity factual communication.

### Documentation practice

Professional pattern:

- Choose content type by user need: learn, do, look up, understand.
- Keep explanation from interrupting procedural work unless needed.
- Keep reference precise and navigable.
- Treat quality as both functional correctness and human fit.

Best fit in AI Editorial Office:

- KB files;
- templates;
- user instructions;
- reusable process docs;
- system documentation.

### UX writing

Professional pattern:

- User action, product state, accessibility, terminology, and product truth
  drive copy.
- Content should help the user do the next thing without unsupported product
  promises.

Best fit in AI Editorial Office:

- Professional Communication may support message structure and evidence
  preservation for product copy, but UX Writer and UX writing canon remain the
  owners of product-facing UI copy.

## Candidate Capability Boundaries

Professional Communication should own:

- message architecture;
- reader path and information hierarchy;
- decision-first and recommendation presentation;
- explanation fit;
- technical communication clarity and precision;
- information density and layering;
- actionability of communication;
- preservation of evidence, uncertainty, caveats, assumptions, and decision
  cues during communication;
- communication review challenge when an artifact is correct but does not
  transfer understanding or action reliably.

Professional Communication should not own:

- audience identification and intended outcome, owned by
  `audience_outcome_alignment.md`;
- quality vocabulary and tradeoffs, owned by
  `editorial_quality_attributes.md`;
- cognitive reasoning moves, owned by `analytical_reasoning.md`;
- analytical product shape and whether a recommendation is justified, owned by
  `professional_analysis.md`;
- drafting responsibility, owned by Writer Agent or UX Writer;
- product-facing copy rules, owned by UX Writer and UX writing canon;
- evidence classes and confidence labels, owned by
  `editorial_evidence_framework.md`;
- review gate authority, owned by `AGENTS.md` and `review_pipeline.md`.

## Synthesis For S3.R5

The smallest architecture-compatible release is one shared capability:

```text
Professional Communication = the capability for shaping and reviewing how
meaning, evidence, recommendations, explanations, decisions, and next actions
are transferred to a specific professional reader.
```

It should be activated only when communication quality is material to the
reader's ability to decide, act, implement, review, approve, understand, or
reuse the work.

It should not be activated for ordinary grammar cleanup, cosmetic editing,
simple rewriting, standard drafting, or low-risk text polish.

## Open Research Limits

- Public sources vary in depth. Consulting communication practice is often
  proprietary, so the release should use public executive, policy, technical,
  documentation, and scientific communication practices rather than importing a
  branded consulting methodology.
- Sources are strongest for written artifacts. Oral presentation, facilitation,
  negotiation, crisis communication, and media relations should remain
  postponed unless a future release explicitly targets them.
- Professional Communication should remain a capability lens, not a universal
  template. Mandatory forms would conflict with the current artifact-minimalism
  architecture.
