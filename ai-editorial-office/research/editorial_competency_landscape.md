# Editorial Competency Landscape For AI Editorial Office

Date: 2026-07-08

Status: research artifact only. This report does not modify AI Editorial Office
canon, roles, pipelines, project state, or implementation tasks. Architecture
notes are preliminary research observations, not decisions.

## 1. Executive Summary

This research reviewed professional practice across newsroom and editorial
offices, investigative journalism, book and scholarly publishing, scientific
peer review, consulting and strategy, think tanks and policy analysis,
UX/content design, technical documentation, engineering RFC and design review,
architecture review, security and risk assessment, knowledge management, and
high-reliability decision organizations.

The recurring pattern is not "better roles"; it is a layered competency stack:
clear problem framing, audience and stakeholder interpretation, disciplined
source work, explicit evidence confidence, domain modeling, synthesis,
argumentation, independent challenge, risk review, quality control, decision
documentation, and knowledge capture. Mature organizations make these
competencies visible through artifacts: briefs, source maps, evidence tables,
review reports, decision records, risk registers, style guides, publication
checklists, retrospectives, and knowledge-base patterns.

The most valuable competencies for AI Editorial Office appear to be:

- Brief interpretation that can reject or repair a weak brief before production.
- Source discovery and evidence evaluation that separates source reliability,
  claim confidence, and editorial usefulness.
- Domain modeling that turns scattered facts into reusable conceptual maps.
- Synthesis and recommendation design that converts evidence into decisions
  without hiding uncertainty.
- Independent critical review that tests reasoning, not only prose polish.
- Risk detection that treats ethical, reputational, factual, security,
  governance, and implementation risks as first-class review objects.
- Decision documentation that preserves why a path was chosen, not just what
  was produced.
- Knowledge capture and canon-evolution discipline that distinguishes reusable
  patterns from one-off task notes.
- Workflow orchestration with explicit handoff contracts.
- Publication and delivery readiness that checks truth, usefulness, format,
  accessibility, source traceability, and residual risk together.

AI Editorial Office already has a strong canonical foundation in the Task Object
Model, Capability Registry, Shared Lifecycle Kernel, Evidence and Confidence
Framework, Failure Modes Playbook, Planning Framework, Audience and Outcome
Alignment, Quality Attributes, and Learning/Canon Evolution. The likely weak
spots are therefore not absence of governance. They are the next layer of
operational competency: richer source and evidence artifacts, explicit domain
modeling, artifact-specific review rubrics, traceable decision records, stronger
implementation-task formulation, and professional-grade publication readiness
checks. These are research observations only; they should be evaluated later
against the existing architecture before any canon change.

## 2. Competency Map

### 2.1 Task Understanding And Brief Interpretation

What it means: Translating a raw request into a bounded task, intended outcome,
audience, constraints, acceptance criteria, evidence needs, and stop conditions.

Why it matters: Many professional failures begin before research or writing. A
team that accepts an ambiguous brief will often produce polished but wrong work.
GOV.UK content practice starts with user need; RAND emphasizes clear purpose,
scope, and relevance before method; consulting practice uses issue framing
before analysis. [S11, S13, S16]

How expert organizations perform it:

- Newsrooms distinguish pitch, assignment, reporting plan, story form, and
  publication slot.
- Consulting teams translate a client ask into a problem statement, hypothesis,
  issue tree, and decision question.
- Policy teams state the policy objective, option space, stakeholders, evidence
  standard, and appraisal method.
- Engineering communities require RFCs for substantial changes so stakeholders
  can see motivation, alternatives, and consequences before implementation.

Typical artifacts:

- Editorial brief.
- Pitch memo.
- Research brief.
- Problem statement.
- Issue tree.
- RFC preamble.
- Acceptance criteria.
- Stop-condition note.

Common failure modes:

- Accepting a bad brief.
- Treating format as the goal.
- Missing the decision owner.
- Starting source collection before the core question is clear.
- Hiding unknowns as assumptions.

Useful heuristics:

- If the output could be correct in form but useless in purpose, the brief is
  not ready.
- Rewrite the request as: "For whom, to decide or do what, under what
  constraints, using what evidence?"
- Ask whether the task is seeking truth, judgment, persuasion, instruction,
  governance, implementation, or publication.
- Identify the one thing that would make the work obviously wrong if assumed
  incorrectly.

Relevance to AI Editorial Office: The current Task Object Model and lifecycle
already provide a strong base. The competency opportunity is to strengthen
brief diagnosis as a repeatable capability with artifact-specific "bad brief"
signals and repair patterns.

### 2.2 Audience And Stakeholder Analysis

What it means: Understanding who must use the artifact, what they already know,
what they need to decide or do, what constraints shape their reading, and whose
interests or risks must be represented.

Why it matters: Expert organizations optimize information for use, not merely
for completeness. IPEd describes substantive editing as beginning with purpose,
readership, reader knowledge, and reading context. RAND includes engagement and
inclusion as quality pillars because research must represent relevant
perspectives fairly and be usable by stakeholders. [S6, S11]

How expert organizations perform it:

- UX/content design uses user needs, journey context, and action language.
- Think tanks map decision-makers, affected communities, funders, critics, and
  implementation actors.
- Technical documentation splits user goals into tutorials, how-to guides,
  reference, and explanation.
- News organizations consider public interest, affected parties, reader
  context, and possible harm.

Typical artifacts:

- Audience profile.
- Stakeholder map.
- User need statement.
- Reader journey.
- Use-case matrix.
- Persona only when grounded in research.
- Outcome definition.

Common failure modes:

- Writing for the approver instead of the user.
- Confusing stakeholder opinion with stakeholder need.
- Over-generalizing audience as "everyone".
- Ignoring affected but non-present stakeholders.
- Assuming expert vocabulary is shared.

Useful heuristics:

- If the reader cannot act differently after reading, the intended outcome is
  not clear.
- Separate decision-maker, end user, reviewer, affected party, and maintainer.
- Ask what the artifact should let the reader stop worrying about.
- Do not create personas where a concrete use case or stakeholder map would be
  more honest.

Relevance to AI Editorial Office: AIEO already has Audience and Outcome
Alignment. The next competency layer is stronger stakeholder-risk mapping for
research, implementation, and governance tasks.

### 2.3 Research Question Formation And Source Discovery

What it means: Turning the brief into searchable questions, evidence needs,
source classes, exclusion criteria, and a plan for discovering primary,
authoritative, dissenting, and contextual sources.

Why it matters: Source discovery determines the ceiling of evidence quality.
Investigative and verification handbooks emphasize step-by-step online search,
open-source information, UGC handling, and testing obtained information rather
than relying on plausibility. [S4, S5]

How expert organizations perform it:

- Investigative teams create source maps: documents, people, databases,
  imagery, public records, filings, technical logs, prior coverage, and affected
  communities.
- Scientific reviewers check whether the manuscript cites relevant prior work
  and whether novelty claims are grounded in the literature.
- Analysts search for evidence that could disconfirm the preferred hypothesis.
- Documentation teams inspect support tickets, user questions, API behavior,
  and existing docs.

Typical artifacts:

- Research plan.
- Source map.
- Search log.
- Evidence inventory.
- Literature map.
- Interview list.
- Data-source register.

Common failure modes:

- Starting with convenient sources.
- Source monoculture.
- Missing primary documents.
- Treating search results as evidence.
- Not recording negative search results.

Useful heuristics:

- For each material claim, name the strongest possible source class before
  searching.
- Use at least one source that could falsify the emerging interpretation.
- Record source absence when absence affects confidence.
- Separate "found source" from "usable evidence".

Relevance to AI Editorial Office: The evidence framework can be strengthened by
explicit source-discovery patterns and a source-map artifact for high-value
research tasks.

### 2.4 Source Reliability And Provenance Discipline

What it means: Assessing who produced a source, why, when, with what access,
method, incentives, conflicts, expertise, and traceability.

Why it matters: Reuters treats source credibility as central to accuracy,
prefers named sources, requires cross-checking where possible, and calls for
explicitness about what is unknown. The Trust Project makes source references,
methods, labels, journalist expertise, and feedback visible as trust signals.
[S1, S3]

How expert organizations perform it:

- Newsrooms distinguish witnessed events, named sources, anonymous sources,
  documents, pickups, handouts, rumors, and user-generated content.
- Peer review requires conflict disclosure and appropriate reviewer expertise.
- Policy research records methods, assumptions, limitations, and support.
- Security reviews treat asset, threat, vulnerability, and control evidence
  differently.

Typical artifacts:

- Source note.
- Source reliability table.
- Provenance chain.
- Interview memo.
- Document log.
- Conflict-of-interest declaration.
- Method note.

Common failure modes:

- Citing a secondary summary when a primary source exists.
- Ignoring source motive.
- Treating official as automatically true.
- Treating anonymous as automatically false.
- Losing the provenance chain for copied facts.

Useful heuristics:

- Ask: access, expertise, motive, recency, independence, and corroboration.
- Prefer the closest source to the event or decision, but test incentives.
- Keep source label and evidence value separate.
- If the source would benefit from your conclusion, lower confidence until
  corroborated.

Relevance to AI Editorial Office: AIEO can benefit from a reusable provenance
discipline that complements confidence labels: source strength is not the same
as claim confidence.

### 2.5 Evidence Evaluation And Confidence Calibration

What it means: Judging whether evidence supports a claim, with what confidence,
under what assumptions, and with what residual uncertainty.

Why it matters: Scientific peer review asks whether conclusions are robust,
valid, and reliable; policy appraisal weighs costs, benefits, risks, and
options; security risk assessment evaluates likelihood, impact, threat,
vulnerability, and controls. [S9, S13, S23]

How expert organizations perform it:

- Peer reviewers check methods, data, statistics, uncertainty, references, and
  whether conclusions exceed evidence.
- RAND expects findings and recommendations to follow logically from methods
  and data.
- Fact-checkers break text into checkable claims and evidence.
- Risk teams distinguish inherent risk, controls, residual risk, and treatment.

Typical artifacts:

- Evidence table.
- Claim table.
- Confidence note.
- Methods appendix.
- Data-quality assessment.
- Risk register.
- Limitations section.

Common failure modes:

- Confidence inflation.
- Cherry-picked support.
- Conflating correlation with cause.
- Over-interpreting weak signals.
- Treating lack of contradiction as confirmation.

Useful heuristics:

- A claim is only as strong as the weakest link in its evidence chain.
- For each conclusion, ask what evidence would make it false or narrower.
- Use confidence labels that reflect evidence quality, not narrative certainty.
- Record assumptions separately from findings.

Relevance to AI Editorial Office: The existing Evidence and Confidence
Framework is central. Future design could add stronger claim-to-evidence
traceability and residual-risk notation for recommendations.

### 2.6 Domain Modeling

What it means: Building a structured representation of the domain: actors,
concepts, relationships, workflows, constraints, incentives, data objects,
terms, failure patterns, and decision points.

Why it matters: Experts do not merely collect facts; they model systems. RAND's
rigor and relevance standards emphasize clear questions, appropriate methods,
and stakeholder context. Technical documentation frameworks organize content
around distinct user needs and forms. Engineering design docs expose system
constraints and tradeoffs. [S11, S19, S20]

How expert organizations perform it:

- Analysts create issue trees, causal maps, theory-of-change diagrams, and
  option models.
- Product teams map user journeys, service blueprints, jobs-to-be-done, and
  decision flows.
- Architects model components, quality attributes, dependencies, and tradeoffs.
- Security teams model assets, threats, attack surfaces, vulnerabilities, and
  controls.

Typical artifacts:

- Domain map.
- Concept model.
- Causal map.
- Service blueprint.
- Architecture diagram.
- Threat model.
- Glossary.
- Taxonomy.

Common failure modes:

- Flat fact lists with no relationships.
- Imported vocabulary without local definitions.
- Missing actors and incentives.
- Modeling the happy path only.
- Confusing taxonomy with understanding.

Useful heuristics:

- If you cannot draw the domain, you probably cannot govern the work.
- Model conflicts, not just categories.
- Include ownership and incentives in the model.
- Track which model elements are evidence-backed versus inferred.

Relevance to AI Editorial Office: Domain modeling looks like one of the most
valuable missing operational competencies. It could become a shared capability
or a task-local artifact trigger for complex research and implementation tasks.

### 2.7 Synthesis And Sensemaking

What it means: Converting diverse evidence into patterns, distinctions,
tradeoffs, implications, and usable conclusions.

Why it matters: Research organizations are judged by whether they help decision
makers understand what matters. RAND emphasizes relevance, rigor, transparency,
and utility; Pew emphasizes objective, methodologically grounded research for
public understanding. [S11, S12]

How expert organizations perform it:

- Think tanks summarize findings, limitations, policy options, and implications.
- Consulting teams synthesize analyses into a recommendation storyline.
- Editors identify the main point, what to foreground, what to cut, and where
  nuance belongs.
- Documentation teams separate conceptual explanation from procedural guidance.

Typical artifacts:

- Research memo.
- Findings summary.
- Insight map.
- Recommendation memo.
- Executive summary.
- Implications section.

Common failure modes:

- Summary without synthesis.
- Over-smoothing contradictions.
- Treating frequency as importance.
- Losing minority but high-risk evidence.
- Producing insight without actionability.

Useful heuristics:

- A synthesis should say what changes because of the evidence.
- Name the pattern, the exception, and the consequence.
- Separate "what we know", "what it means", and "what to do next".
- Preserve contradictions that affect decisions.

Relevance to AI Editorial Office: AIEO has strong planning and evidence
frameworks. It may need more explicit synthesis formats for design research,
implementation planning, and canon-learning candidates.

### 2.8 Narrative Design And Information Architecture

What it means: Designing the reader path: order, hierarchy, framing, section
roles, labels, transitions, examples, and what must be visible at each point.

Why it matters: Editorial and documentation organizations treat structure as a
quality mechanism. Diataxis organizes docs by user need; IPEd requires logical
structure, suitable language, navigation aids, and appropriate presentation.
[S6, S19]

How expert organizations perform it:

- Newsrooms use inverted pyramid, nut graf, explanatory structure, and visual
  hierarchy depending on story type.
- Book publishers use developmental editing to repair structure, pacing,
  chapter logic, and reader continuity.
- Documentation teams separate learning, task completion, factual lookup, and
  conceptual understanding.
- UX writers make content support user action at the moment of need.

Typical artifacts:

- Outline.
- Story map.
- Section role plan.
- Information architecture map.
- Content model.
- Table of contents.
- Wire copy map.

Common failure modes:

- Beautiful sentences in the wrong order.
- Lead that hides the decision.
- Mixed reference and tutorial content.
- Repetition caused by unclear section jobs.
- Reader path optimized for author convenience.

Useful heuristics:

- Every section needs a job.
- Put the reader's next decision before your internal process history.
- If a section mixes "learn", "do", "decide", and "verify", split or relabel it.
- Structure is an argument about importance.

Relevance to AI Editorial Office: Structure-before-writing already appears in
the operating model. Later competency design could add reusable section-role
patterns for research reports, design reviews, and implementation briefs.

### 2.9 Argumentation And Recommendation Logic

What it means: Making claims, reasons, evidence, assumptions, alternatives,
tradeoffs, and recommendation criteria explicit.

Why it matters: Consulting, policy, peer review, and architecture boards all
distinguish between a conclusion and a justified conclusion. Nature notes that
useful reviews set out arguments for and against publication; policy appraisal
requires comparing options against objectives, benefits, costs, and risks.
[S9, S13]

How expert organizations perform it:

- Consultants use top-down recommendation structures, issue trees, and "so what"
  logic.
- Policy teams use option appraisal and business cases.
- Architects use ADRs to record context, decision, considered options, and
  consequences.
- Peer reviewers require specific evidence for major criticisms.

Typical artifacts:

- Argument map.
- Recommendation memo.
- Options analysis.
- Business case.
- ADR.
- Review report.
- Decision memo.

Common failure modes:

- Unsupported recommendations.
- Hidden criteria.
- Strawman alternatives.
- Analysis dump without conclusion.
- Decision based on loudest stakeholder.

Useful heuristics:

- Every recommendation should expose: criteria, options, evidence, tradeoff,
  residual risk, and owner.
- If alternatives are not credible, the recommendation has not been tested.
- Put the decision question before the evidence inventory.
- A strong argument can survive a hostile but fair restatement.

Relevance to AI Editorial Office: The Editorial Planning and Option Evaluation
Framework already points this way. A later competency layer could make
argumentation and recommendation memos explicit artifacts for complex tasks.

### 2.10 Editorial Judgment And Prioritization

What it means: Deciding what matters, what to foreground, what to omit, what
requires caveat, what deserves escalation, and what should not be published or
delivered.

Why it matters: Reuters states that accuracy and balance take precedence over
speed; the Trust Project emphasizes labels, methods, sources, and feedback;
editors in peer review screen submissions before formal review based on fit,
interest, novelty, and technical soundness. [S1, S3, S9]

How expert organizations perform it:

- News editors weigh public interest, accuracy, harm, novelty, timeliness, and
  fairness.
- Publishers decide whether a manuscript's structure, market fit, quality, and
  author revision path justify investment.
- Peer-review editors decide when reviewer disagreement requires more evidence
  rather than vote-counting.
- Product strategists rank opportunities by user value, business value, risk,
  and feasibility.

Typical artifacts:

- Assignment note.
- Editorial rationale.
- Kill memo.
- Prioritization matrix.
- Review verdict.
- Decision log.

Common failure modes:

- Optimizing for polish over truth.
- Confusing interesting with important.
- Avoiding a hard call through process bloat.
- Publishing because work is already sunk.
- Equal-weighting unequal evidence.

Useful heuristics:

- Ask: "What would a responsible editor refuse to let pass?"
- Important beats comprehensive when attention is scarce.
- Omission is an editorial decision; record risky omissions.
- When evidence is unequal, balance is not 50/50 presentation.

Relevance to AI Editorial Office: Editorial judgment is partly encoded in
quality attributes and failure modes. The opportunity is to make prioritization
criteria more explicit in review and publication readiness.

### 2.11 Planning And Option Evaluation

What it means: Identifying credible routes, comparing them against criteria,
choosing an approach, documenting rejected alternatives, and setting reroute
triggers.

Why it matters: HM Treasury's Green Book defines appraisal as assessing costs,
benefits, and risks of different options for objectives. Rust RFCs require a
controlled path for substantial changes so stakeholders can gain confidence in
direction before implementation. [S13, S20]

How expert organizations perform it:

- Strategy teams build issue trees and workplans.
- Policy teams compare options, counterfactuals, and value for money.
- Architecture boards compare alternatives against quality attributes.
- Security teams compare treatment options: avoid, mitigate, transfer, accept.

Typical artifacts:

- Option matrix.
- Workplan.
- Evaluation criteria.
- Business case.
- RFC.
- ADR.
- Risk treatment plan.

Common failure modes:

- Single-option planning.
- False urgency.
- Criteria after conclusion.
- Over-researching every possible path.
- No reconsideration trigger.

Useful heuristics:

- Generate at least one broader, one narrower, and one different route.
- Reject alternatives with evidence, not vibes.
- Define the moment when the plan must be revisited.
- Match planning depth to risk, reversibility, and cost of being wrong.

Relevance to AI Editorial Office: AIEO already has a Planning Framework. Future
research-to-architecture work could connect planning more tightly to RFC,
decision memo, and task formulation artifacts.

### 2.12 Critical Review And Challenge

What it means: Independently testing an artifact's claims, logic, scope,
evidence, audience fit, risk, and readiness.

Why it matters: Peer review, newsroom editing, design review, security review,
and architecture review all rely on challenge by someone other than the
producer. PLOS recommends separating major from minor issues and focusing on
publication-critical improvements, not nitpicking. [S9, S10]

How expert organizations perform it:

- Peer reviewers summarize the work, identify strengths and weaknesses, and
  justify recommendations with evidence.
- Editors challenge sourcing, fairness, structure, and legal or ethical risks.
- Engineering reviewers challenge motivation, alternatives, compatibility,
  migration, and testability.
- Security reviewers challenge threat assumptions and control sufficiency.

Typical artifacts:

- Peer review report.
- Editorial review.
- Red team memo.
- Design review comments.
- Security review.
- QA checklist.

Common failure modes:

- Review theater.
- Reviewer rewrites instead of reviews.
- Preference masquerading as requirement.
- Missing independence.
- Finding only style issues while logic fails.

Useful heuristics:

- Start review by restating what the artifact claims to do.
- Classify findings as blocking, required, suggested, or informational.
- Major issue: affects truth, decision, safety, usability, or publication
  readiness.
- Do not require extra work that is merely the next study unless current
  conclusions depend on it.

Relevance to AI Editorial Office: Review separation is already canonical. The
competency opportunity is richer review rubrics by artifact type and risk class.

### 2.13 Fact-Checking And Verification

What it means: Checking specific claims, quotes, names, dates, numbers,
relationships, images, documents, links, and interpretations against reliable
evidence.

Why it matters: Reuters treats quotes, attribution, datelines, images, rumors,
and source handling as accuracy-critical. Verification handbooks teach
structured checks for UGC and open-source information. [S1, S4]

How expert organizations perform it:

- Newsrooms use line-by-line fact checks, source call-backs, document review,
  and correction workflows.
- Investigative teams geolocate, chronolocate, archive, triangulate, and
  preserve digital evidence.
- Publishers proof references, cross-references, quotations, permissions, and
  page elements.
- Technical documentation tests commands, APIs, links, examples, and version
  behavior.

Typical artifacts:

- Fact-checking log.
- Claims table.
- Quote log.
- Link check.
- Verification note.
- Correction log.
- Evidence archive.

Common failure modes:

- Plausibility check instead of verification.
- Broken provenance for copied claims.
- Unchecked numbers in summaries.
- Link rot.
- Correct fact used in wrong context.

Useful heuristics:

- Verify nouns, numbers, dates, quotes, comparisons, and causal verbs first.
- Treat screenshots and generated summaries as clues, not sources.
- Archive volatile evidence when it matters.
- If a claim is not checkable, rewrite it as interpretation or remove it.

Relevance to AI Editorial Office: Fact-checking can become a specialized
capability invoked by risk, artifact type, or claim sensitivity, without
creating a new permanent role.

### 2.14 Risk Detection And Ethical/Safety Review

What it means: Identifying possible harm, legal exposure, security risk,
privacy risk, reputational risk, misuse, bias, conflict of interest, and
governance failure before delivery.

Why it matters: Security risk frameworks treat risk as a function of threat,
vulnerability, likelihood, impact, and controls. ISO 27001 frames information
security management as a system. HRO practice keeps attention on weak signals,
failure, resilience, and deference to expertise. [S23, S24, S28]

How expert organizations perform it:

- Newsrooms weigh harm, graphic content, source protection, conflicts, and
  fairness.
- Peer review checks research ethics, conflicts, image integrity, data
  availability, and misconduct signals.
- Security teams run risk assessments, threat models, control reviews, and
  residual-risk decisions.
- Architecture boards assess quality attribute risks and operational failure
  modes.

Typical artifacts:

- Risk register.
- Threat model.
- Ethics note.
- Conflict declaration.
- Security review.
- Hazard analysis.
- Residual-risk acceptance.

Common failure modes:

- Risk treated as a final checkbox.
- Hidden conflict of interest.
- Over-indexing on obvious risks while missing operational ones.
- No named risk owner.
- Publishing sensitive details without need.

Useful heuristics:

- Ask what could go wrong if the artifact is believed, acted on, reused, or
  copied into canon.
- Separate risk detection from risk acceptance.
- Record owner, mitigation, residual risk, and escalation threshold.
- Small anomalies may be early warnings, not noise.

Relevance to AI Editorial Office: Existing failure modes and quality attributes
can be extended with professional risk-review artifacts for security,
reputation, governance, and implementation tasks.

### 2.15 Quality Control, Style, And Accessibility

What it means: Ensuring the artifact is accurate, consistent, readable,
complete, accessible, navigable, style-compliant, and fit for its intended
medium.

Why it matters: Publishing practice distinguishes substantive editing,
copyediting, and proofreading. Google and Microsoft style guides emphasize
clear, consistent technical communication and project-specific style hierarchy.
[S6, S17, S18]

How expert organizations perform it:

- Publishers use style sheets, copyedits, proofreads, reference checks, and
  production checks.
- Documentation teams use style guides, templates, link checks, code sample
  tests, accessibility checks, and versioning.
- UX teams test whether content supports action and comprehension.
- Newsrooms use copy desks, corrections, headline checks, captions, and
  standards review.

Typical artifacts:

- Style guide.
- Style sheet.
- Copyedit checklist.
- Proofread checklist.
- Accessibility checklist.
- Publication readiness checklist.
- QA report.

Common failure modes:

- Style consistency masking factual weakness.
- Copyediting too early.
- Broken links or examples.
- Inaccessible structure.
- House style applied against user need.

Useful heuristics:

- Edit structure before sentences, sentences before punctuation, punctuation
  before production proof.
- Follow project style first; deviate only for clarity and consistently.
- Check tables, captions, links, headings, and references, not only prose.
- Accessibility is a quality property, not a postscript.

Relevance to AI Editorial Office: Quality attributes already exist; later work
could add artifact-specific quality checklists and style-sheet patterns.

### 2.16 Decision Documentation

What it means: Recording decisions, context, alternatives, reasons,
consequences, owners, date, status, and revisit triggers.

Why it matters: Mature organizations preserve decision memory to prevent
relitigation, hidden authority, and knowledge decay. ADR practice records
architecture choices; RFC processes document substantial changes before action;
Bain's decision-rights practice emphasizes named roles in decisions. [S15, S20,
S21]

How expert organizations perform it:

- Architecture teams write ADRs.
- Engineering communities use RFCs, design docs, accepted/rejected states, and
  implementation tracking.
- Policy teams use decision memos and business cases.
- Editorial teams record editorial rationale, corrections, and final approval.

Typical artifacts:

- Decision memo.
- ADR.
- RFC.
- Approval note.
- Decision log.
- Revisit trigger.
- Governance note.

Common failure modes:

- Decision owner unclear.
- Rationale only in chat.
- Alternatives not recorded.
- Decision status stale.
- Consequences omitted.

Useful heuristics:

- Record decisions when reversal is costly, future readers will ask why, or the
  decision constrains later work.
- A decision note should be short enough to read and complete enough to prevent
  mythology.
- Include what was not chosen.
- Name the next review point.

Relevance to AI Editorial Office: The current lifecycle already uses manifest,
status, and orchestration artifacts. The opportunity is a sharper decision
record pattern for architectural, editorial, and implementation choices.

### 2.17 Knowledge Capture And Reuse

What it means: Converting task-local learning into findable, maintained,
trustworthy, reusable knowledge without polluting canon with unvalidated notes.

Why it matters: ISO 30401 treats knowledge management as a management system to
establish, maintain, review, and improve organizational knowledge practices.
Documentation and policy organizations also depend on versioned, discoverable,
reviewable knowledge. [S18, S19, S25]

How expert organizations perform it:

- Knowledge teams curate knowledge-base articles, taxonomies, pattern
  libraries, lessons learned, and owner metadata.
- Documentation teams retire stale pages, track version applicability, and
  separate how-to from reference.
- Engineering teams capture recurring decisions in ADRs and templates.
- High-reliability teams run after-action reviews and feed learning into
  training and controls.

Typical artifacts:

- Knowledge-base article.
- Pattern library entry.
- Retrospective.
- Lessons learned.
- Taxonomy.
- Glossary.
- Stale-content report.

Common failure modes:

- Knowledge decay.
- Duplicate truths.
- Unowned wiki pages.
- Canonizing a one-off.
- No retirement path.

Useful heuristics:

- Reuse requires owner, scope, freshness, evidence, and retrieval path.
- Do not promote a lesson until it has evidence beyond one anecdote or a clear
  governance reason.
- Mark stale knowledge as dangerous, not merely old.
- Capture decisions and patterns separately.

Relevance to AI Editorial Office: AIEO already has Canon Evolution. The next
competency question is how to operationalize knowledge capture artifacts before
canon promotion.

### 2.18 Canon Evolution And Standards Maintenance

What it means: Updating durable standards intentionally, with owner selection,
evidence, compatibility checks, review, versioning, and deprecation.

Why it matters: Standards organizations and documentation systems distinguish
current guidance, amendments, revisions, and withdrawn material. Google
developer docs use a reference hierarchy and allow deviations only when they
improve clarity and remain consistent. [S18, S25]

How expert organizations perform it:

- Standards bodies use proposal, committee, review, ballot, publication, and
  revision lifecycles.
- Engineering communities use RFCs before substantial process or language
  change.
- Documentation teams maintain style guides, changelogs, and versioned docs.
- Research organizations periodically revisit quality standards.

Typical artifacts:

- Change proposal.
- Standards changelog.
- Deprecation note.
- Migration guide.
- Review record.
- Compatibility matrix.

Common failure modes:

- Updating canon from one task.
- Duplicating rules across owners.
- No deprecation.
- Hidden compatibility break.
- Unreviewed style drift.

Useful heuristics:

- Canon changes need evidence, owner, scope, compatibility, and review.
- Prefer a reference to duplicating a rule.
- Every new standard should say what it replaces or does not replace.
- Stale canon should be challenged through a defined route, not ignored.

Relevance to AI Editorial Office: This aligns strongly with the existing
Learning and Canon Evolution Framework. Competency design should preserve this
boundary while improving evidence capture for future canon candidates.

### 2.19 Workflow Orchestration And Handoff

What it means: Coordinating stage boundaries, role/accountability boundaries,
inputs, outputs, status, blockers, handoffs, and restart context.

Why it matters: Strong organizations separate production, review, approval, and
maintenance. Nature describes editor screening, reviewer selection, reviewer
reports, author revision, and editor decisions as distinct responsibilities.
Engineering RFCs separate proposal, discussion, acceptance, implementation, and
tracking. [S9, S20]

How expert organizations perform it:

- Newsrooms use assignment desks, editors, copy desks, fact-checking, legal
  review, and publication desks.
- Journals route manuscripts through editors, reviewers, revisions, and
  publication ethics checks.
- Engineering teams use design review, implementation review, testing, launch
  review, and postmortem.
- Security teams use intake, assessment, mitigation, acceptance, and monitoring.

Typical artifacts:

- Orchestration plan.
- Status log.
- Handoff note.
- RACI/RAPID-style responsibility map.
- Review queue.
- Approval record.

Common failure modes:

- Weak handoff.
- Role confusion.
- Silent status drift.
- Producer self-approval.
- Process bloat without clearer decisions.

Useful heuristics:

- A handoff should say what changed, what is trusted, what is uncertain, and
  what the next owner must not do.
- Status should reflect operational state, not optimism.
- Add artifacts only when they reduce risk, improve restartability, or support
  review.
- The next role should not need chat history to continue safely.

Relevance to AI Editorial Office: AIEO is already workflow-conscious. The
competency opportunity is artifact-specific handoff patterns for research,
review, implementation tasks, and canon-learning candidates.

### 2.20 Implementation Task Formulation

What it means: Translating research, decisions, and design intent into a
bounded implementation request with source of truth, allowed changes, forbidden
changes, acceptance criteria, validation, and deliver-back expectations.

Why it matters: Engineering and architecture processes separate "what should be
true" from "what should be changed now." RFCs and ADRs prevent uncontrolled
implementation of substantial changes; documentation style guides prioritize
project-specific constraints; security reviews require risk treatment and
validation. [S18, S20, S21, S23]

How expert organizations perform it:

- Product and engineering teams define tickets, user stories, design docs,
  acceptance criteria, test plans, rollout plans, and rollback triggers.
- Architecture boards require decisions before build.
- Security teams require control evidence and residual-risk acceptance.
- Documentation teams define doc change scope and version applicability.

Typical artifacts:

- Implementation brief.
- Codex task prompt.
- Acceptance criteria.
- Check plan.
- Test matrix.
- Rollout note.
- Migration note.

Common failure modes:

- Research-to-implementation gap.
- Vague "improve X" task.
- Forbidden files not named.
- No validation.
- Refactor disguised as small fix.

Useful heuristics:

- A good implementation task names repository, target behavior, source of
  truth, allowed files, forbidden files, checks, and deliver-back format.
- If the task cannot be reviewed as a diff, the scope is probably too vague.
- Preserve architectural intent but avoid prescribing unnecessary mechanics.
- Include "do not change" constraints as strongly as desired changes.

Relevance to AI Editorial Office: The existing Codex Task Standard is a strong
anchor. Future competency work could connect implementation formulation to
decision records, risk notes, and artifact-specific validation.

### 2.21 Finalization And Publication Readiness

What it means: Determining whether an artifact is ready for delivery,
publication, reuse, or governance closure after content, evidence, review,
format, accessibility, and risk checks.

Why it matters: Publishing and journalism distinguish editing from release.
Proofreading checks completeness, order, amendments, house style, errors,
headings, figures, references, and production details. Newsrooms correct errors
transparently and consider harm and suitability for audience. [S1, S6]

How expert organizations perform it:

- Publishers run proofreading, production QA, metadata checks, permissions, and
  final signoff.
- Newsrooms run headline, caption, legal, standards, corrections, and audience
  suitability checks.
- Engineering teams run release readiness and rollback checks.
- Security teams require risk acceptance or mitigation before launch.

Typical artifacts:

- Publication readiness checklist.
- Final proof.
- Metadata sheet.
- Release checklist.
- Approval log.
- Correction plan.

Common failure modes:

- Premature publication.
- Last-minute evidence edits unreviewed.
- Broken formatting or links.
- Missing approval.
- No correction pathway.

Useful heuristics:

- Finalization is not polishing; it is readiness judgment.
- Check the artifact as the audience will encounter it.
- Do not let late changes bypass review.
- Publication readiness includes what happens if an error is found afterward.

Relevance to AI Editorial Office: AIEO has review-gate discipline. It may
benefit from differentiated readiness checklists for research reports,
implementation tasks, canon changes, and public-facing outputs.

### 2.22 Feedback, Correction, And Learning Loop

What it means: Receiving feedback, correcting errors, classifying learning,
updating artifacts, and deciding whether a pattern deserves reuse or canon
attention.

Why it matters: Trust Project indicators include actionable feedback and
prominent corrections. Reuters requires transparent correction of errors. High
reliability practice treats anomalies and small failures as system signals.
[S1, S3, S28]

How expert organizations perform it:

- Newsrooms maintain correction policies and update stories.
- Journals use corrections, expressions of concern, retractions, and
  post-publication commentary.
- Engineering teams use incident reviews and postmortems.
- Knowledge teams use feedback loops, stale-content review, and owner-based
  maintenance.

Typical artifacts:

- Correction log.
- Retrospective.
- Postmortem.
- Feedback note.
- Learning candidate.
- Stale-knowledge report.

Common failure modes:

- Defensive response to correction.
- Silent edits.
- Treating all feedback as canon.
- No owner for follow-up.
- Repeating the same failure without pattern capture.

Useful heuristics:

- Correct the artifact, explain the correction, and inspect the process.
- Separate task-local feedback from reusable learning.
- Treat repeated small errors as a system signal.
- Capture what changed in future work, not only what went wrong.

Relevance to AI Editorial Office: This fits the existing Learning and Canon
Evolution Framework. The competency opportunity is more precise feedback
classification and correction artifacts.

## 3. Practices By Domain

### 3.1 Newsroom / Editorial Office

Core workflow: Pitch or assignment, brief, reporting, source verification,
editorial shaping, copy editing, standards/legal review when needed,
publication, corrections, and feedback.

Strongest practices:

- Accuracy before speed.
- Named sources preferred; anonymous sources require stronger authorization.
- Clear labels for news, opinion, analysis, sponsored content, and corrections.
- Separation between reporting, editing, standards, and publication decisions.
- Transparent corrections and source attribution. [S1, S2, S3]

Quality criteria:

- Accuracy, fairness, independence, transparency, public interest, context,
  proportionality, and correction readiness.

Artifacts:

- Pitch memo, assignment brief, source list, reporting notes, fact-check log,
  copyedit, standards note, headline/caption check, correction log.

What AI Editorial Office can learn:

- Treat source discipline and correction path as part of editorial quality, not
  optional aftercare.
- Use explicit labels for artifact type and evidence status.
- Make "what we do not know" visible.

What should not be copied:

- Newsroom speed culture when the task is architectural research.
- Beat-driven assumptions that privilege novelty over system usefulness.
- Anonymous-source conventions unless real source protection is relevant.

### 3.2 Investigative Journalism

Core workflow: Hypothesis or lead, source map, document and data collection,
human sourcing, OSINT/UGC verification, triangulation, legal/ethics review,
story construction, right of reply, publication, evidence preservation.

Strongest practices:

- Build a source map before conclusions harden.
- Triangulate documents, witnesses, databases, imagery, and public records.
- Preserve volatile digital evidence.
- Try to disprove the story, not only prove it.
- Explain methods when transparency strengthens trust. [S1, S4, S5]

Quality criteria:

- Verifiability, public-interest justification, source protection, method
  transparency, legal defensibility, proportionality of claims.

Artifacts:

- Investigation plan, source map, evidence archive, chronology, entity map,
  verification log, right-of-reply log, legal review memo.

What AI Editorial Office can learn:

- Complex research tasks need source maps, chronology, entity models, and
  disconfirmation checks.
- Evidence preservation is a competency when sources may change.

What should not be copied:

- Adversarial posture for routine editorial tasks.
- Overbuilt investigation artifacts for low-risk work.

### 3.3 Publishing

Core workflow: Acquisition or project brief, developmental/substantive editing,
copyediting, permissions and references, proofreading, production, metadata,
publication, post-publication correction.

Strongest practices:

- Distinguish edit levels: substantive, copyediting, proofreading.
- Maintain style sheets and house style.
- Check references, cross-references, tables, figures, headings, pagination,
  and production details.
- Preserve authorial or institutional voice while improving reader fit. [S6,
  S7]

Quality criteria:

- Purpose fit, reader fit, completeness, clarity, consistency, accuracy,
  production integrity, style compliance.

Artifacts:

- Editorial brief, developmental edit letter, style sheet, copyedit, proofread
  checklist, permissions log, metadata sheet.

What AI Editorial Office can learn:

- Different review passes have different jobs. AIEO can benefit from explicit
  "structure pass", "evidence pass", "copy/style pass", and "readiness pass"
  patterns.

What should not be copied:

- Publishing's sometimes slow sequential process when a compact task needs only
  bounded review.
- Style-sheet fetishism that outranks truth or usefulness.

### 3.4 Scientific Peer Review

Core workflow: Editorial screen, reviewer selection, conflict checks, expert
review, author revision, editor decision, publication, correction/retraction or
post-publication commentary when needed.

Strongest practices:

- Reviewers summarize the work in their own words before critique.
- Major and minor issues are separated.
- Validity, originality, significance, data, methodology, uncertainty,
  references, clarity, and expertise boundaries are checked.
- Editors weigh arguments rather than counting votes.
- Conflicts and confidentiality are explicit. [S8, S9, S10]

Quality criteria:

- Novelty, rigor, validity, reliability, reproducibility, ethics, contribution,
  transparency, field relevance.

Artifacts:

- Peer review report, reviewer checklist, conflict declaration, editor decision
  letter, revision response, correction/retraction notice.

What AI Editorial Office can learn:

- Review artifacts should show the reviewer's interpretation, confidence
  limits, and expertise boundary.
- "Major vs minor" classification is a powerful antidote to review theater.

What should not be copied:

- Slow anonymous gatekeeping as a default.
- Overemphasis on novelty when the task values operational usefulness.

### 3.5 Consulting / Strategy

Core workflow: Problem framing, issue tree, hypothesis, workplan, analysis,
option comparison, synthesis, recommendation, decision alignment, implementation
roadmap.

Strongest practices:

- Start with a decision question.
- Break problems into mutually exclusive and collectively exhaustive issue
  trees where possible.
- Keep the recommendation storyline visible.
- Define decision roles and avoid diffuse ownership.
- Compare options against criteria, not presentation appeal. [S13, S15]

Quality criteria:

- Clear problem statement, logical structure, evidence-backed recommendation,
  decision usefulness, tradeoff clarity, implementability.

Artifacts:

- Problem statement, issue tree, workplan, analysis pack, recommendation memo,
  decision rights map, implementation roadmap.

What AI Editorial Office can learn:

- Research reports should lead to usable distinctions and decision criteria,
  even when they do not prescribe implementation.
- Decision ownership and recommendation logic should be documented.

What should not be copied:

- Slide-polish culture.
- Overconfident recommendations that understate uncertainty.
- Client-pleasing framing that distorts evidence.

### 3.6 Think Tanks / Policy Analysis

Core workflow: Policy question, stakeholder and context mapping, evidence
review, method design, option appraisal, analysis, recommendation, peer or
quality review, dissemination, evaluation.

Strongest practices:

- Relevance, rigor, transparency, legitimacy, inclusion, and engagement are
  explicit research quality dimensions.
- Methods, assumptions, limitations, support, and recommendations are
  documented.
- Policy appraisal compares options by objectives, benefits, costs, and risks.
- Evaluation is designed early, not after implementation. [S11, S12, S13, S14]

Quality criteria:

- Objectivity, method fit, stakeholder fairness, feasibility, transparency,
  uncertainty disclosure, policy usefulness.

Artifacts:

- Policy brief, research plan, methods appendix, option appraisal, theory of
  change, evaluation plan, dissemination plan.

What AI Editorial Office can learn:

- Include stakeholders and affected perspectives when research informs system
  architecture.
- Record methods and limitations in a reusable way.

What should not be copied:

- Lengthy public-policy apparatus for small editorial tasks.
- False neutrality that avoids making evidence-weighted judgments.

### 3.7 UX Writing / Content Design

Core workflow: User need discovery, journey/context mapping, content design,
interaction copy, accessibility review, content testing, iteration, governance
through style and design systems.

Strongest practices:

- Start with user needs and user action.
- Use plain language and task-oriented structure.
- Write for the moment of use, not for organizational self-description.
- Align voice, tone, accessibility, and interaction state.
- Maintain style guidance that non-specialists can apply. [S16, S17]

Quality criteria:

- Clarity, actionability, accessibility, consistency, trust, reduced cognitive
  load, fit to user state.

Artifacts:

- User need statement, content pattern, content map, UI copy table, error-state
  copy, tone guidance, content test notes.

What AI Editorial Office can learn:

- Every internal artifact should be designed around the next user's action:
  decide, review, implement, verify, or reuse.
- Error and blocker language deserves design, not improvisation.

What should not be copied:

- Over-reliance on personas without evidence.
- Microcopy-level optimization when the real problem is decision structure.

### 3.8 Technical Documentation

Core workflow: User/task analysis, information architecture, topic type
selection, drafting, technical review, editorial review, sample/link testing,
publication, version maintenance.

Strongest practices:

- Separate tutorials, how-to guides, reference, and explanation.
- Use style-guide hierarchy: project-specific guidance first, general guide
  second, external references third.
- Prioritize clarity and consistency for the specific domain and readers.
- Test examples, commands, links, and version applicability. [S18, S19]

Quality criteria:

- Findability, task success, accuracy, completeness, maintainability,
  version-fit, consistency, accessibility.

Artifacts:

- Documentation plan, IA map, style guide, example test log, reference page,
  tutorial, how-to, explanation page, changelog.

What AI Editorial Office can learn:

- Artifact types should have distinct reader needs and quality criteria.
- AIEO can borrow Diataxis-like separation for internal knowledge: tutorial,
  procedure, reference, explanation, decision record.

What should not be copied:

- Documentation taxonomy as bureaucracy.
- Reference density when the task needs guidance or decision support.

### 3.9 Engineering Design Review / RFC

Core workflow: Identify substantial change, write RFC/design doc, discuss,
revise, accept/reject/postpone, implement, track, stabilize, document.

Strongest practices:

- Reserve heavy process for substantial changes.
- Require motivation, detailed design, drawbacks, alternatives, unresolved
  questions, and impact.
- Use public discussion to build confidence and expose tradeoffs.
- Keep implementation separate from proposal acceptance. [S20]

Quality criteria:

- Clear motivation, user impact, design coherence, compatibility, alternatives,
  testability, migration path, maintainability.

Artifacts:

- RFC, design doc, review comments, accepted/rejected decision, tracking issue,
  implementation plan, test plan.

What AI Editorial Office can learn:

- Substantial canon or architecture changes should be proposed, challenged, and
  accepted before implementation.
- RFC templates are useful models for structured change proposals.

What should not be copied:

- Open-source consensus rituals for single-user local tasks.
- Infinite discussion when the owner can make a bounded decision.

### 3.10 Architecture Review Board

Core workflow: Architecture concern intake, context and constraints, option
analysis, quality attribute review, risk/tradeoff assessment, decision record,
governance follow-up.

Strongest practices:

- Evaluate quality attributes explicitly: reliability, security, performance,
  operability, maintainability, cost, usability, portability.
- Document decisions and consequences through ADRs.
- Use well-architected frameworks to structure review questions.
- Separate advisory review from decision ownership. [S21, S22]

Quality criteria:

- Fit to business and user goals, quality attribute balance, risk visibility,
  operability, evolutionary compatibility, decision traceability.

Artifacts:

- Architecture brief, ADR, quality attribute scenario, tradeoff matrix, risk
  register, review minutes.

What AI Editorial Office can learn:

- Competency-to-architecture work should preserve tradeoff context and
  consequences.
- Architecture review should focus on quality attributes and decision records,
  not generic approval.

What should not be copied:

- Heavy board governance for ordinary editorial production.
- Architecture theater that approves without evidence or owner accountability.

### 3.11 Security / Risk Review

Core workflow: Scope assets and objectives, identify threats and vulnerabilities,
assess likelihood and impact, evaluate controls, decide treatment, record
residual risk, monitor.

Strongest practices:

- Use structured risk assessment.
- Separate assets, threats, vulnerabilities, controls, likelihood, impact, and
  residual risk.
- Require named risk owners and acceptance authority.
- Treat information security as a management system, not a one-time checklist.
  [S23, S24]

Quality criteria:

- Complete scope, credible threat model, control evidence, risk prioritization,
  treatment clarity, residual-risk acceptance, monitoring.

Artifacts:

- Risk register, threat model, control matrix, security review, risk acceptance,
  mitigation plan, incident postmortem.

What AI Editorial Office can learn:

- Editorial and architecture tasks also have risk classes. Risk review should
  be structured and owner-based.
- Residual risk is often more honest than "approved".

What should not be copied:

- Compliance-only checklists without evidence.
- Security jargon for non-security risks where simpler risk language suffices.

### 3.12 Knowledge Management

Core workflow: Identify critical knowledge, capture, classify, validate, publish,
make findable, assign owners, review freshness, retire or update.

Strongest practices:

- Treat knowledge management as a maintained system.
- Define ownership, scope, metadata, retrieval paths, and review cycles.
- Separate task notes, reusable patterns, standards, and canonical rules.
- Capture lessons from incidents and repeated questions. [S18, S19, S25]

Quality criteria:

- Relevance, findability, trustworthiness, freshness, ownership, reuse value,
  deprecation clarity.

Artifacts:

- Knowledge-base article, pattern library, glossary, taxonomy, retrospective,
  ownership register, freshness report.

What AI Editorial Office can learn:

- Canon evolution should be supported by intermediate knowledge artifacts that
  are useful without being canonical.
- Staleness and duplication should be detectable as knowledge risks.

What should not be copied:

- Wiki sprawl.
- Capturing everything because storage is cheap.
- Treating knowledge-base publication as validation.

## 4. Expert Heuristics

### Brief And Task Framing

- A brief is ready when the producer can state the output, user, decision or
  action, evidence boundary, quality bar, and stop condition in one paragraph.
- If a brief names only a format, ask what job the format must do.
- The narrower the task, the more explicit the acceptance criteria should be.
- Reject "make it better" unless "better" is tied to a quality attribute.

### Source Discovery And Evidence

- Name the ideal source before accepting the available source.
- Separate source credibility from claim support.
- Find the strongest contrary evidence early.
- Use primary sources for rules, standards, dates, and official policy.
- Mark source absence when it changes confidence.

### Reliability And Verification

- Verify the boring details first: names, dates, numbers, titles, URLs, quotes,
  and version applicability.
- Do not use a claim that cannot be traced unless it is clearly labeled as
  interpretation.
- Treat screenshots, summaries, and model output as leads, not evidence.
- Archive volatile evidence when future review depends on it.

### Domain Modeling

- Make actors, objects, relationships, workflows, constraints, and incentives
  visible.
- If a domain map has no conflicts, risks, or feedback loops, it is probably
  too tidy.
- Define terms before ranking options.
- Model maintenance and ownership, not only creation.

### Synthesis

- A summary says what sources said; a synthesis says what follows.
- Preserve contradictions that change decisions.
- State confidence, assumptions, and limits near the conclusion, not only in a
  footnote.
- Do not turn every finding into a recommendation.

### Narrative And Structure

- Every section needs a job.
- Lead with what the reader must understand, not how the writer discovered it.
- Separate explanation from procedure and decision support from reference.
- Cut detail that does not improve trust, action, decision, or reuse.

### Review And Challenge

- Begin review by restating the artifact's claim and intended use.
- Classify findings by consequence: blocking, required, suggested,
  informational.
- Challenge criteria before challenging wording.
- Do not let reviewers require their preferred alternative unless the current
  alternative fails the task.

### Recommendation And Decision

- A recommendation needs options, criteria, evidence, tradeoffs, owner, and
  residual risk.
- Record the rejected alternatives that future readers are likely to revisit.
- If a decision cannot name consequences, it is not ready.
- Revisit decisions when assumptions, constraints, or risk class change.

### Risk And Readiness

- Ask what happens if the artifact is believed, reused, automated, or made
  canonical.
- Separate detection, mitigation, and acceptance.
- Publication readiness includes correction readiness.
- Late changes that affect claims need review, even if small.

### Knowledge And Canon

- A useful lesson is not automatically canon.
- Promote knowledge only with owner, scope, evidence, freshness, and review.
- Retire stale knowledge visibly.
- Capture patterns that reduce future task risk, not every anecdote.

## 5. Artifact Catalogue

| Artifact | Purpose | When used | What good looks like | Possible AI Editorial Office equivalent |
| --- | --- | --- | --- | --- |
| Editorial brief | Defines goal, audience, scope, constraints, and success | Intake / assignment | Clear task, reader, outcome, source boundary, and stop conditions | `brief.md` with stronger competency fields |
| Pitch memo | Proposes why a topic matters and how to pursue it | Before assignment | Public/user value, evidence path, risks, angle, feasibility | Research or article proposal note |
| Research memo | Summarizes findings and implications | After research | Findings, source basis, confidence, contradictions, gaps, downstream guidance | `research.md` or report |
| Source map | Identifies needed and available source classes | Research planning | Primary, secondary, dissenting, human, data, and missing sources visible | New conditional source-map section |
| Evidence table | Links claims/findings to evidence and confidence | Research and review | Each material claim has source, confidence, caveat, sensitivity | `claims_table.md` / evidence appendix |
| Fact-checking log | Records claim-level verification | Pre-publication / high-risk review | Checkable claims, evidence, checker, status, unresolved issues | Fact-check artifact or review section |
| Quote log | Protects quote accuracy and context | Journalism / interviews | Exact quote, source, context, permission/ground rules | Source notes for interviews |
| Peer review report | Independent expert critique | Scientific review / deep review | Summary, major/minor issues, evidence, recommendation, expertise limits | `review.md` extension for expert review |
| Editorial calendar | Coordinates publication timing and ownership | Newsroom / content ops | Slots, owners, dependencies, review deadlines, status | Usually no change; possible workflow view |
| Style guide | Maintains consistent language and conventions | Ongoing publication/docs | Scope, hierarchy, examples, exceptions, owner | Existing KB style guidance / future style layer |
| Style sheet | Task/project-specific style decisions | Book/docs production | Terms, capitalization, abbreviations, spellings, exceptions | Task-local style sheet for long outputs |
| Decision memo | Records decision question, options, rationale, owner | Governance / strategy | Criteria, evidence, decision, rejected options, risks, revisit trigger | Decision frame or future decision artifact |
| Recommendation memo | Converts analysis into advised action | Consulting / policy | Clear answer, evidence, tradeoffs, implementation implications | Research-to-planning memo |
| Design review document | Presents engineering design for critique | Before implementation | Motivation, design, alternatives, risks, tests, open questions | Codex task design packet |
| RFC | Structured proposal for substantial change | Before major system/process changes | Motivation, detailed design, drawbacks, alternatives, unresolved questions | Future canon/system change proposal pattern |
| ADR | Records architecture decision and consequences | After architecture choice | Context, decision, status, consequences, related decisions | Future architecture decision note |
| Risk register | Tracks risks, owners, mitigations, residual risk | Security, governance, delivery | Risk, likelihood, impact, owner, treatment, status | Risk section in plan/review or conditional artifact |
| Threat model | Models assets, threats, vulnerabilities, controls | Security-sensitive tasks | Assets, trust boundaries, attack paths, mitigations | Security review artifact for relevant tasks |
| Quality checklist | Confirms quality attributes and task fit | Review / finalization | Tailored to artifact type and risk, not generic | `qa-checklist.md` when justified |
| Publication readiness checklist | Confirms release readiness | Final pre-delivery | Evidence, review, format, links, accessibility, approvals, correction path | Future readiness section or checklist |
| Retrospective | Captures what happened and what to improve | After task/incident | Facts, causes, improvements, owners, learning candidates | `feedback.md` / learning note |
| Postmortem | Learns from incident or failure | High-impact failure | Blameless chronology, contributing factors, actions, owners | Failure recovery artifact |
| Knowledge-base article | Reusable operational knowledge | After validated pattern | Purpose, scope, owner, freshness, examples, links | KB entry after canon-evolution process |
| Pattern library entry | Reusable design/content pattern | Repeated workflows | Use case, when to use, when not, examples, risks | Editorial pattern candidate |
| Glossary | Stabilizes terms and definitions | Complex domains | Term, definition, scope, source, deprecated terms | Task-local or KB glossary |
| Taxonomy | Organizes knowledge for retrieval | KM/docs systems | Categories tied to user tasks, not internal politics | Capability/artifact taxonomy |
| Handoff note | Transfers state between roles | Stage transition | Delta, trusted artifacts, caveats, blockers, next action | Existing `handoff-*.md` |
| Correction log | Records corrections and transparency | Post-publication | Error, correction, date, impact, process note | Feedback/correction artifact |
| Methods appendix | Makes research method transparent | Research reports | Scope, sources, method limits, exclusions, assumptions | Source Notes / research methods section |
| Option matrix | Compares plausible routes | Planning | Criteria, options, evidence, tradeoffs, selected route | Planning framework artifact |
| Implementation brief | Converts decision to executable work | Before coding/system edit | Allowed/forbidden changes, files, checks, deliver-back | Codex Task Standard packet |
| Review rubric | Defines how artifact will be judged | Before review | Criteria by artifact type, risk, evidence, outcome | Future review capability support |

## 6. Failure Modes And Anti-Patterns

| Failure | Description | Warning signs | Likely cause | Prevention pattern | Relevance to AI Editorial Office |
| --- | --- | --- | --- | --- | --- |
| Accepting a bad brief | Production starts before goal, audience, evidence, or outcome is clear | "Just make a report"; no decision owner; unclear source boundary | Speed pressure; politeness; weak intake | Preflight gate; brief repair heuristics | Strengthen task-understanding competency |
| Optimizing for polished wording over truth | Prose improves while evidence remains weak | Smooth claims with no sources; style review dominates | Editorial craft detached from evidence | Evidence-first review; claim table | Protects against LLM fluency risk |
| Weak source discipline | Sources are convenient, secondary, stale, or incentive-laden | No primary sources; no provenance; overuse of summaries | Poor source map | Source reliability table; primary-source rule | Supports evidence framework |
| False balance | Unequal evidence presented as equal sides | "Some say" framing without weight | Misunderstood fairness | Evidence-weighted synthesis | Important for review and argumentation |
| Hidden assumptions | Inferences appear as facts | No assumptions section; confident recommendations | Rushed synthesis | Assumption log; confidence labels | Already aligned with AIEO evidence framework |
| Unsupported recommendations | Advice exceeds evidence | No options, criteria, tradeoffs, or residual risk | Consultant-style overconfidence | Recommendation memo structure | Relevant to architecture notes |
| Missing audience | Artifact is accurate but unusable | No reader action; wrong depth; jargon | Producer-centered work | Audience/outcome alignment | Existing framework can be operationalized |
| Unclear decision owner | No one can approve, reject, or accept risk | Endless review; circular comments | Governance not documented | Decision roles and owner field | Applies to canon and implementation tasks |
| Weak handoff | Next role lacks context or caveats | Re-reading required; chat history dependency | Artifact minimalism misunderstood | Delta handoff with trusted/uncertain items | Existing handoff discipline can deepen |
| Over-researching | Research expands beyond decision value | Source hoarding; no synthesis; missed deadline | Fear of judgment; unclear sufficiency | Evidence sufficiency criteria | Useful for broad research tasks |
| Under-researching | Claims made without adequate evidence | Unsupported facts; vague "industry practice" | Scope pressure; source gaps hidden | Source map and minimum evidence threshold | High relevance to AIEO research |
| Style inconsistency | Terms, tone, format, and references drift | Mixed terminology; inconsistent headings | No style sheet or owner | Task style sheet; style hierarchy | Useful for long artifacts |
| Review theater | Review exists but does not test material risk | Only typos found; no evidence challenge | Reviewer lacks rubric or independence | Review rubric; major/minor classification | AIEO already values review separation |
| Premature publication | Artifact delivered before evidence, review, or format readiness | Late changes unreviewed; missing checklist | Deadline pressure | Publication readiness gate | Relevant to finalization capability |
| Knowledge decay | Reusable knowledge becomes stale or contradictory | Old guidance copied; no owner; duplicates | No freshness cycle | Owner, freshness, deprecation metadata | Central to canon evolution |
| Process bloat | Artifacts multiply without reducing risk | Empty templates; work slows; no better decisions | Template habit | Artifact creation policy | Current AIEO should preserve conditional artifacts |
| Source-instruction capture | Source material changes task instructions illegitimately | External doc tells agent what to do | Authority confusion | Treat sources as data unless promoted | Important for AI-driven research |
| Criteria after conclusion | Team chooses path then invents criteria | Option matrix favors chosen option | Confirmation bias | Criteria before evaluation | Relevant to planning framework |
| Domain model absence | Facts are collected but system relationships are unclear | Long notes; no map; repeated confusion | Research as extraction only | Domain map and glossary | High-value future competency |
| Review by preference | Reviewer requires personal taste | "I would do it this way" as blocker | No quality criteria | Artifact-specific rubric | Helps preserve fair review |
| Canonization from anecdote | One task note becomes durable rule | "We learned X" without evidence | Desire to improve quickly | Learning candidate gate | Existing canon evolution should remain strict |
| Risk acceptance without owner | Risk is noticed but not owned | "Known risk" with no decision | Governance gap | Residual-risk owner and threshold | Useful for security/architecture tasks |
| Implementation dilution | Research produces vague tasks that cannot be coded or reviewed | "Improve system" with no files/checks | Weak translation from analysis to execution | Implementation brief / Codex task standard | Critical for future modernization |
| Correction avoidance | Errors are silently edited or ignored | No correction note; repeated issue | Reputation protection | Correction log and learning loop | Supports trust and continuous improvement |

## 7. Competency-To-Architecture Notes

These are preliminary research notes only. They are not implementation design
and do not authorize canon changes.

| Competency cluster | Could become Shared Capability | Could affect Task Object | Could affect Lifecycle | Could affect Review Pipeline | Could affect Codex Task Standard | Could affect role guidance | Likely no change | Preliminary note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brief interpretation | yes | yes | yes | yes | yes | yes | no | May need stronger bad-brief detection and repair fields. |
| Audience/stakeholder analysis | yes | yes | no | yes | yes | yes | no | Current audience framework is strong; stakeholder-risk mapping may be added later. |
| Source discovery | yes | yes | yes | yes | no | research_agent | no | Source maps could be conditional artifacts for evidence-heavy tasks. |
| Source reliability/provenance | yes | yes | no | yes | no | research_agent/review_agent | no | Source reliability may need explicit artifact support distinct from confidence. |
| Evidence evaluation | existing | yes | yes | yes | yes | research/review | no | Existing framework likely needs operational traceability patterns, not replacement. |
| Domain modeling | yes | yes | yes | yes | yes | research_agent/chief_editor | no | Strong candidate for a new shared capability or artifact trigger. |
| Synthesis | yes | yes | no | yes | yes | research_agent/writer_agent | no | Could define synthesis shapes for research, recommendations, and design notes. |
| Narrative/information architecture | yes | no | no | yes | no | writer/ux/review | no | Might affect artifact templates more than lifecycle. |
| Argumentation/recommendation | yes | yes | yes | yes | yes | chief_editor/review | no | Could strengthen decision and recommendation artifacts. |
| Editorial judgment | existing | no | yes | yes | no | chief_editor/review | no | More likely rubric/heuristic improvement than new architecture. |
| Planning/option evaluation | existing | yes | yes | yes | yes | chief_editor | no | Current planning framework can absorb RFC/ADR-inspired patterns. |
| Critical review | existing | no | no | yes | yes | review_agent | no | Artifact-specific review rubrics are likely high value. |
| Fact-checking/verification | yes | yes | yes | yes | no | research/review | no | Could be a conditional capability, not a new role. |
| Risk detection | yes | yes | yes | yes | yes | chief/review | no | Risk register and residual-risk patterns may be useful. |
| Quality control/style | yes | no | no | yes | no | review/final_editor | no | Likely template/checklist improvement. |
| Decision documentation | yes | yes | yes | yes | yes | chief_editor | no | ADR/RFC/decision memo patterns may complement existing plan/status. |
| Knowledge capture | existing | yes | yes | yes | no | chief/review | no | Add intermediate knowledge artifacts before canon promotion. |
| Canon evolution | existing | yes | yes | yes | yes | chief/review | no | Preserve strict owner/evidence/review boundaries. |
| Workflow orchestration | existing | yes | yes | yes | yes | chief_editor | no | Current architecture already strong; refine handoff patterns. |
| Implementation task formulation | yes | yes | yes | yes | yes | chief_editor | no | High-value bridge from research to executable Codex tasks. |
| Publication readiness | yes | yes | yes | yes | no | final_editor/review | no | Could become differentiated readiness gates by artifact type. |
| Feedback/correction loop | existing | yes | yes | yes | no | chief/review | no | Correction and learning loops can be more explicit without canon churn. |
| High-reliability weak-signal detection | yes | no | yes | yes | yes | all roles | no | Could enrich failure-mode recovery and review challenge. |

## 8. Source Notes

Source quality summary: The strongest sources are primary professional standards
and official guidance: Reuters, AP, Trust Project, ICMJE, Nature, PLOS, RAND,
Pew, HM Treasury, GOV.UK, Microsoft, Google, Rust RFCs, AWS, NIST, ISO. Some
consulting and architecture practices are partially based on public firm
guidance plus established professional practice and book-derived methods; those
claims are used as design heuristics, not as formal standards.

### Source Index

- S1. Reuters, "Standards and Values." Reuters publishes hallmarks of
  journalism including accuracy, fair comment, transparent corrections, balance,
  conflict disclosure, attribution, source handling, quote integrity, and
  disproving as well as proving a story. URL:
  https://reutersagency.com/about/standards-values/

- S2. Associated Press, "News values and principles." AP presents itself as
  setting journalism ethics standards and describes safeguards against bias and
  inaccuracies plus conflicts-of-interest guidance. URL:
  https://www.ap.org/about/news-values-and-principles/

- S3. The Trust Project, "The 8 Trust Indicators." Identifies best practices,
  journalist expertise, labels, references, methods, local sourcing, diverse
  voices, and actionable feedback as trust signals for journalism. URL:
  https://thetrustproject.org/trust-indicators/

- S4. DataJournalism.com / European Journalism Centre, "Verification Handbook
  2." Covers online search, open-source information, UGC, data quality,
  documentation verification, ethics, and organizing newsrooms for accurate
  investigative reporting. URL:
  https://datajournalism.com/read/handbook/verification-2

- S5. Bellingcat, "Guides." Bellingcat's public guides demonstrate OSINT
  practice: geolocation, imagery, open-source tools, evidence preservation,
  conflict monitoring, and misinformation verification. URL:
  https://www.bellingcat.com/resources/how-tos/

- S6. Institute of Professional Editors, "Types of editing." Distinguishes
  substantive editing, copyediting, and proofreading; emphasizes intended
  purpose, readership, structure, language, consistency, accuracy, references,
  integrity checks, and publication readiness. URL:
  https://www.iped-editors.org/about-editing/types-of-editing/

- S7. Chartered Institute of Editing and Proofreading, "Suggested minimum
  rates" and competency/professional framing. Useful for distinguishing
  proofreading, copyediting, substantial editing, development editing, project
  management, CPD, specialization, and job-specific complexity. URL:
  https://www.ciep.uk/knowledge-hub/suggested-minimum-rates.html

- S8. International Committee of Medical Journal Editors, "Recommendations for
  the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical
  Journals." Updated January 2026; covers responsibilities, conflicts,
  peer-review process, corrections, misconduct, reporting, and AI use in
  publishing. URL: https://www.icmje.org/recommendations/

- S9. Nature Portfolio, "Peer Review." Defines publication criteria, editorial
  screening, reviewer selection, review process, disagreement handling, and
  review questions covering validity, originality, data, methods, statistics,
  conclusions, references, clarity, and expertise limits. URL:
  https://www.nature.com/nature-portfolio/editorial-policies/peer-review

- S10. PLOS, "How to Write a Peer Review." Recommends summary, overall
  impression, major/minor issue separation, concrete evidence, constructive
  feedback, professionalism, and avoiding out-of-scope demands or reviewer
  self-promotion. URL: https://plos.org/resource/how-to-write-a-peer-review/

- S11. RAND, "Standards for High-Quality and Objective Research and Analysis."
  Frames research quality through engagement, inclusion, relevance, rigor,
  transparency, and legitimacy, with documentation of purpose, scope, support,
  assumptions, activities, data, methods, results, limitations, findings, and
  recommendations. URL: https://www.rand.org/about/standards.html

- S12. Pew Research Center, "Our Methods." Describes objective, nonpartisan
  research methods, surveys, demographic analysis, data science, methodological
  standards, data quality, representativeness, and public-facing explanation.
  URL: https://www.pewresearch.org/our-methods/

- S13. HM Treasury, "The Green Book." UK government guidance on appraisal:
  assessing costs, benefits, and risks of different options for achieving
  government objectives. Page last updated 2026-02-05. URL:
  https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government

- S14. HM Treasury, "The Magenta Book." UK government guidance on evaluation:
  scoping, design, conduct, use, dissemination, analytical capabilities, and
  building evaluation into policy design and delivery. Page last updated
  2026-05-15. URL:
  https://www.gov.uk/government/publications/the-magenta-book

- S15. Bain & Company, "Great decisions - Not a solo performance" and related
  decision-rights writing. Used as a public source for decision roles and
  responsibility clarity in major decisions. URL:
  https://www.bain.com/insights/decision-insights-10-great-decisions-not-a-solo-performance/

- S16. GOV.UK content design and service design guidance. Used for user needs,
  plain language, task orientation, and content shaped around user action. URL:
  https://www.gov.uk/service-manual

- S17. Microsoft Writing Style Guide. Emphasizes simple, straightforward,
  technology-focused style: warm, relaxed, crisp, clear, bias-aware, and usable
  by many roles. URL: https://learn.microsoft.com/en-us/style-guide/welcome/

- S18. Google Developer Documentation Style Guide. Provides a reference
  hierarchy, clear and consistent technical documentation guidance, project
  specific style precedence, and permission to depart from guidance when clarity
  improves if consistency is preserved. URL: https://developers.google.com/style

- S19. Diataxis documentation framework. Organizes documentation around four
  user needs and forms: tutorials, how-to guides, reference, and explanation;
  emphasizes content, architecture, and form. URL: https://diataxis.fr/

- S20. Rust RFCs repository. Defines RFCs as a consistent and controlled path
  for substantial changes so stakeholders can be confident about project
  direction; distinguishes substantial changes from normal pull requests. URL:
  https://github.com/rust-lang/rfcs

- S21. Architecture Decision Records references and templates, including common
  ADR structures for context, decision, status, and consequences. URL:
  https://github.com/architecture-decision-record/architecture-decision-record

- S22. AWS Well-Architected Framework. Used as an architecture-review example
  emphasizing structured review across quality domains such as operational
  excellence, security, reliability, performance efficiency, cost optimization,
  and sustainability. URL:
  https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

- S23. NIST SP 800-30 Rev. 1, "Guide for Conducting Risk Assessments." Used for
  structured risk concepts: threat, vulnerability, likelihood, impact, controls,
  and risk determination. URL:
  https://csrc.nist.gov/pubs/sp/800/30/r1/final

- S24. ISO/IEC 27001:2022, "Information security management systems." Used as
  authoritative context for information security management systems and control
  governance. URL: https://www.iso.org/standard/27001

- S25. ISO 30401:2018, "Knowledge management systems - Requirements." Defines
  requirements and guidelines for establishing, implementing, maintaining,
  reviewing, and improving knowledge management systems in organizations. URL:
  https://www.iso.org/standard/68683.html

- S26. U.S. Government Accountability Office, "Yellow Book: Government Auditing
  Standards." Used as an authoritative source for evidence, independence,
  professional judgment, documentation, and quality control in audit/review
  contexts. URL: https://www.gao.gov/yellowbook

- S27. Barbara Minto, "The Pyramid Principle"; Charles Conn and Robert McLean,
  "Bulletproof Problem Solving"; and related consulting-method literature. Used
  as professional background for issue structuring, top-down recommendations,
  and problem-solving discipline. These are book sources, not web standards.

- S28. Karl Weick and Kathleen Sutcliffe, "Managing the Unexpected," and the
  high-reliability organization literature. Used for preoccupation with failure,
  reluctance to simplify, sensitivity to operations, commitment to resilience,
  and deference to expertise. This is research-literature context rather than a
  task-specific implementation standard.

### Source Use And Limitations

- Journalism and peer-review claims rely mainly on primary standards and
  guidance from Reuters, AP, Trust Project, ICMJE, Nature, and PLOS.
- Publishing claims rely on professional editing bodies and style guidance;
  some book-publishing workflow details are generalized from professional
  practice rather than a single publisher's internal process.
- Consulting claims are partly public and partly book-derived. They are treated
  as heuristics for structured thinking, not as authoritative universal rules.
- Policy and think-tank claims rely on RAND, Pew, HM Treasury Green Book, and
  Magenta Book, which are strong public sources for research quality, appraisal,
  and evaluation.
- Documentation and UX/content claims rely on GOV.UK, Microsoft, Google, and
  Diataxis, all strong public practice sources.
- Engineering and architecture claims rely on Rust RFCs, ADR references, and
  AWS Well-Architected; these are strong examples but not universal governance
  mandates.
- Security and risk claims rely on NIST and ISO; these are authoritative but
  should be scaled carefully for editorial tasks.
- Knowledge-management claims rely on ISO 30401 and documentation practice.
  ISO text is paywalled beyond the public abstract, so the report uses only the
  public abstract-level context plus general KM practice.
