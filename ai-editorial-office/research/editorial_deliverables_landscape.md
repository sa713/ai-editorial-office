# Editorial Deliverables Landscape For AI Editorial Office

Date: 2026-07-08

Status: research artifact only. This report does not modify AI Editorial Office
canon, roles, agents, pipelines, project state, or architecture. Any notes about
AI Editorial Office are preliminary observations for later evaluation, not
implementation recommendations.

## 1. Executive Summary

This study examined professional deliverables used by mature editorial,
investigative, publishing, scientific, consulting, policy, UX/content,
technical documentation, architecture, engineering, security, risk, product,
knowledge-management, and high-reliability organizations.

The strongest recurring pattern is that excellent organizations do not rely
only on expert thinking. They externalize thinking into work products that make
intent, evidence, judgment, risk, review, decision, and memory inspectable.
Deliverables exist because collaboration creates failure modes that individual
competence alone cannot solve: ambiguous goals, weak evidence, hidden
assumptions, unreviewed tradeoffs, stale decisions, invisible risk, forgotten
context, inconsistent style, and post-failure amnesia.

Across domains, mature deliverables fall into several recurring categories:

- Planning and framing artifacts define what work is being done, for whom, why
  it matters, and where the boundaries are.
- Research and evidence artifacts preserve source discovery, claim support,
  uncertainty, and verification status.
- Analysis and synthesis artifacts convert raw material into findings,
  options, implications, and recommendations.
- Review and challenge artifacts give independent reviewers a structured way to
  test accuracy, reasoning, originality, quality, feasibility, and risk.
- Decision and governance artifacts record what was decided, by whom, under
  what constraints, and with what consequences.
- Risk and security artifacts make uncertainty, threats, controls, mitigations,
  and residual exposure visible before harm occurs.
- Implementation and coordination artifacts translate decisions into usable
  work without forcing every reader to reconstruct rationale.
- Publication and quality artifacts protect consistency, readiness,
  accessibility, legal/ethical safety, and reader trust.
- Learning and knowledge artifacts turn completed work, incidents, and repeated
  questions into organizational memory.

The reason these artifacts recur across unrelated professions is practical.
They reduce ambiguity, permit independent review, coordinate specialists,
enable audit, preserve rationale, lower onboarding cost, and prevent the same
mistake from being rediscovered as if it were new.

AI Editorial Office appears strongest today in editorial governance, task
routing, role separation, review gates, evidence awareness, audience/outcome
alignment, quality attributes, failure-mode recognition, and learning/canon
discipline. Its existing foundation already resembles the professional pattern
of using artifacts as views over task state.

Where professional deliverables could significantly enrich future design is not
by adding more intellectual competencies, but by making the right intermediate
work products explicit when risk, novelty, coordination, evidence burden, or
future reuse justify them. The most promising areas for later evaluation are
source maps, evidence tables, fact-checking and verification logs, decision
records, RFC-like proposal records, risk registers, threat models, publication
readiness checklists, pattern-library entries, and postmortems. These are
research notes only.

## 2. Deliverable Taxonomy

The taxonomy below focuses on the work each deliverable performs, not merely
its name. Many organizations use different names for the same professional
function.

| Category | Core need | Typical deliverables | Mature-use signal |
| --- | --- | --- | --- |
| Intake and planning | Bound the task before production | Editorial brief, research brief, terms of reference, problem statement, stakeholder map | Work can be accepted, declined, constrained, or re-scoped before effort is wasted |
| Inquiry and source discovery | Find the right evidence, not only available evidence | Source map, search log, interview plan, data inventory, literature map | The team can explain what was searched, why, and what is missing |
| Evidence and verification | Make claim support inspectable | Evidence table, fact-checking log, verification log, citation audit | Claims can be traced to source classes and confidence levels |
| Analysis and synthesis | Convert raw material into meaning | Issue tree, analytical memo, research memo, findings report, options analysis | Readers can see reasoning, alternatives, implications, and uncertainty |
| Recommendation and decision | Move from knowledge to accountable choice | Recommendation memo, decision memo, ADR, RFC, decision log | The decision has owner, rationale, alternatives, consequences, and review trail |
| Review and challenge | Test work independently | Peer review report, review letter, design review, architecture assessment, red-team report | Critique is specific, actionable, scoped, and separate from production |
| Governance and assurance | Protect standards, accountability, compliance, and escalation | Architecture board review, publication readiness checklist, quality checklist, risk acceptance note | Approval is tied to evidence and known residual risk |
| Risk and security | Surface uncertainty before harm | Risk register, threat model, control assessment, incident risk memo | Risks have owners, likelihood/impact, treatment, and review cadence |
| Implementation and coordination | Translate approved thinking into coordinated work | Requirements/PRD, design specification, acceptance criteria, test plan, runbook | Implementers can act without re-litigating the whole analysis |
| Publication and editorial consistency | Make output trustworthy and usable | Style sheet, editorial checklist, corrections log, release notes, accessibility checklist | Published work is consistent, accurate, accessible, and maintainable |
| Knowledge management | Preserve reusable knowledge | Knowledge-base article, pattern-library entry, decision index, glossary, source dossier | Future teams can reuse the artifact without rereading the original project |
| Learning and improvement | Convert completion or failure into learning | Lessons learned, retrospective, postmortem, after-action report | The organization changes future behavior rather than only assigning blame |
| Lifecycle and retirement | Prevent stale artifacts from becoming false authority | archive note, supersession notice, deprecation note, version history | Readers know what is current, obsolete, or replaced |

Important taxonomy distinctions:

- A brief is not a plan. A brief defines intent and boundary; a plan sequences
  work.
- A source map is not evidence. It identifies possible evidence classes; an
  evidence table records evidence actually used.
- A finding is not a recommendation. Findings state what the evidence supports;
  recommendations state what action follows.
- A review is not approval. Review tests quality; approval accepts the residual
  state.
- A decision record is not a design document. It preserves why one path was
  chosen among alternatives.
- A checklist is not governance by itself. It is useful only when it triggers
  action, escalation, or explicit acceptance.
- A knowledge-base article is not an archive. It distills reusable knowledge;
  archives preserve historical record.

## 3. Deliverable Catalogue

Each catalogue entry describes the professional job the deliverable performs.
The exact format varies by organization, but the underlying need is stable.

### 3.1 Editorial Brief

- Purpose: Defines an editorial assignment before research or writing begins.
- Problem it solves: Prevents polished work on the wrong audience, angle,
  format, standard, or deadline.
- When created: At commissioning or intake; revised when the assignment changes
  materially.
- Creator: Commissioning editor, chief editor, assigning editor, or project
  lead.
- Consumer: Reporter, researcher, writer, editor, reviewer, producer, and
  publication owner.
- Mandatory information: goal, audience, channel, scope, angle, source
  expectations, constraints, deadline, quality bar, review path, forbidden
  territory.
- Optional information: comparable examples, SEO/social needs, visuals, legal
  sensitivity, stakeholder notes, tone guidance.
- Quality criteria: specific enough to guide work, bounded enough to prevent
  drift, explicit about evidence and review, honest about unknowns.
- Common mistakes: treating the headline as the brief; omitting audience;
  hiding legal or reputational risk; changing the assignment without updating
  the brief.
- Lifecycle: proposed -> accepted -> active -> revised if scope changes ->
  closed after delivery.
- Retirement conditions: output delivered, assignment cancelled, or replaced by
  a new brief.
- AIEO note: Potentially valuable; overlaps existing brief/intake and audience
  concepts; future evaluation could examine whether artifact-specific
  editorial briefs deserve stronger task-local shape.

### 3.2 Research Brief

- Purpose: Converts a broad question into research questions, evidence needs,
  source boundaries, and synthesis expectations.
- Problem it solves: Stops research from becoming endless source collection or
  opportunistic search.
- When created: Before substantial research begins, especially when the report
  will influence decisions.
- Creator: Research lead, editor, analyst, policy lead, or principal
  investigator.
- Consumer: Researchers, analysts, reviewers, decision-makers, and downstream
  writers.
- Mandatory information: research objective, decision context, key questions,
  inclusion/exclusion rules, source hierarchy, evidence standard, expected
  outputs, confidence needs.
- Optional information: search strategy, known prior work, interview targets,
  data constraints, ethical concerns, dissenting views to test.
- Quality criteria: answerable, bounded, explicit about source quality, clear
  about what would change the conclusion.
- Common mistakes: asking too many questions; failing to state exclusion
  criteria; confusing desk research with evidence; omitting uncertainty.
- Lifecycle: drafted -> reviewed for sufficiency -> active -> amended as
  evidence gaps emerge -> closed with research memo/report.
- Retirement conditions: research cancelled, question reframed, or report
  delivered and archived.
- AIEO note: Potentially valuable; overlaps research pipeline and evidence
  framework; future evaluation needed for when it should be mandatory.

### 3.3 Terms Of Reference / Scope Note

- Purpose: Defines remit, authority, scope, constraints, roles, outputs, and
  review/approval boundaries.
- Problem it solves: Prevents mandate confusion in investigations,
  committees, reviews, audits, and cross-functional work.
- When created: At start of a formal review, investigation, policy study,
  committee, or architecture assessment.
- Creator: Sponsor, chief editor, governance owner, committee chair, audit
  lead, or project lead.
- Consumer: Participants, reviewers, decision bodies, and affected
  stakeholders.
- Mandatory information: mandate, scope in/out, authority, deliverables,
  timeline, evidence standard, decision rights, escalation path.
- Optional information: budget, confidentiality rules, stakeholder engagement,
  reporting cadence, dependencies.
- Quality criteria: unambiguous boundaries, named accountable parties,
  realistic timeline, explicit approval authority.
- Common mistakes: vague authority; no out-of-scope list; no decision owner;
  scope expansion without sponsor acceptance.
- Lifecycle: proposed -> approved -> active -> amended under change control ->
  closed.
- Retirement conditions: mandate fulfilled, superseded, or terminated.
- AIEO note: Potentially valuable for high-governance work; overlaps task
  manifest/orchestration plan; could be redundant for ordinary tasks.

### 3.4 Problem Statement

- Purpose: States the problem to be solved, why it matters, who is affected,
  and what success means.
- Problem it solves: Prevents teams from solving symptoms, requests, or
  preferred solutions instead of the underlying problem.
- When created: Early in consulting, product, policy, design, research, and
  engineering work.
- Creator: Analyst, product manager, researcher, editor, architect, or sponsor
  with team input.
- Consumer: Researchers, designers, engineers, decision-makers, reviewers, and
  stakeholders.
- Mandatory information: current state, desired state, gap, affected audience,
  evidence of problem, constraints, success criteria.
- Optional information: non-goals, assumptions, hypotheses, business impact,
  user stories, policy context.
- Quality criteria: solution-neutral, evidence-aware, narrow enough to act on,
  broad enough to avoid local optimization.
- Common mistakes: embedding the preferred solution; using abstract language;
  ignoring whose problem it is; missing measurable success.
- Lifecycle: drafted -> tested against evidence/stakeholders -> accepted ->
  updated if discovery changes the problem.
- Retirement conditions: problem resolved, reframed, or superseded by a
  decision or project charter.
- AIEO note: Highly valuable; overlaps planning and task understanding; likely
  important for future architectural evaluation.

### 3.5 Issue Tree

- Purpose: Decomposes a complex question into mutually useful analytical
  branches.
- Problem it solves: Organizes inquiry, prevents duplicated analysis, and makes
  implicit hypotheses visible.
- When created: Early in consulting, investigations, policy analysis, product
  discovery, and research synthesis.
- Creator: Analyst or research lead, often with team challenge.
- Consumer: Research team, reviewers, decision-makers, writers, and clients.
- Mandatory information: root question, major branches, sub-questions,
  dependencies, evidence needs.
- Optional information: hypotheses, confidence by branch, owners, priority,
  data availability.
- Quality criteria: branches cover the decision space, are non-overlapping
  where possible, and connect to evidence collection.
- Common mistakes: confusing a topic outline with an issue tree; creating too
  many branches; ignoring dependencies; treating the tree as fixed after new
  evidence.
- Lifecycle: draft -> challenged -> used to guide research -> pruned or
  revised -> summarized in findings.
- Retirement conditions: replaced by findings/report, or abandoned if framing
  changes.
- AIEO note: Potentially valuable; overlaps planning framework; future
  evaluation should test whether it helps complex research without adding
  bureaucracy.

### 3.6 Stakeholder / Audience Map

- Purpose: Identifies who is affected, who decides, who uses the output, who
  can block it, and whose perspective is missing.
- Problem it solves: Prevents work from being optimized for the loudest or
  nearest reader while ignoring real users or affected parties.
- When created: During intake, policy analysis, UX/content design, risk review,
  and governance work.
- Creator: Editor, researcher, product manager, UX/content designer, analyst,
  or project lead.
- Consumer: Researchers, writers, reviewers, decision-makers, and
  implementation teams.
- Mandatory information: stakeholder groups, relationship to work, needs,
  risks, influence, decision role, information needs.
- Optional information: communication channel, resistance points, accessibility
  needs, equity considerations, legal/ethical sensitivity.
- Quality criteria: concrete, not generic; distinguishes user, decision-maker,
  reviewer, subject, sponsor, and affected party.
- Common mistakes: treating stakeholders as personas without evidence; missing
  non-present affected groups; over-weighting executive readers.
- Lifecycle: created in planning -> updated during discovery -> used in review
  and readiness checks -> archived with task.
- Retirement conditions: no longer relevant after project closure or replaced
  by a more current map.
- AIEO note: Potentially valuable; overlaps audience/outcome alignment; useful
  for high-impact research, policy, and product tasks.

### 3.7 Source Map

- Purpose: Maps possible source classes and known sources against research
  questions and claim types.
- Problem it solves: Prevents source monoculture, missing primary evidence,
  and over-reliance on convenient secondary summaries.
- When created: Before or during research discovery; updated as new source
  classes appear.
- Creator: Researcher, investigator, analyst, fact-checker, or editor.
- Consumer: Research team, reviewer, fact-checker, writer, and decision-maker.
- Mandatory information: research question, source class, source owner, access
  path, expected evidentiary value, limitations, confidence concerns.
- Optional information: contact plan, FOIA/public-record status, data format,
  provenance, language, cost, legal/ethical constraints.
- Quality criteria: includes primary, secondary, dissenting, expert,
  documentary, data, and human source classes as applicable.
- Common mistakes: listing links without source-class logic; omitting sources
  that could disconfirm the angle; not recording inaccessible sources.
- Lifecycle: drafted with research brief -> expanded during discovery -> used
  to build evidence table -> archived or distilled.
- Retirement conditions: research complete, replaced by evidence table, or
  source landscape becomes stale.
- AIEO note: Highly valuable; overlaps evidence framework but is more
  pre-evidence; requires future architectural evaluation.

### 3.8 Search Log / Research Log

- Purpose: Records search queries, databases, repositories, people contacted,
  dates, results, and dead ends.
- Problem it solves: Makes research reproducible and prevents repeated failed
  searches or hidden selection bias.
- When created: During source discovery, systematic reviews, investigations,
  audits, and high-stakes research.
- Creator: Researcher, librarian, analyst, investigator, or fact-checker.
- Consumer: Research team, reviewer, auditor, editor, and future maintainer.
- Mandatory information: date, search location, query/method, filters, result,
  relevance judgment, follow-up.
- Optional information: screenshots, exported citations, search rationale,
  excluded results, language/region limits.
- Quality criteria: enough detail for another person to understand what was
  tried and why evidence was included or excluded.
- Common mistakes: logging only successful finds; leaving out dates; failing to
  connect searches to research questions.
- Lifecycle: active during research -> summarized in methods/source notes ->
  archived with evidence.
- Retirement conditions: research closed; log retained only if auditability or
  reproducibility matters.
- AIEO note: Valuable for high-evidence tasks; likely redundant for lightweight
  work; future evaluation should be risk-based.

### 3.9 Evidence Table

- Purpose: Connects claims, evidence, source quality, confidence, and
  interpretation in one inspectable structure.
- Problem it solves: Prevents unsupported synthesis and makes review possible
  without rereading every source from scratch.
- When created: During research synthesis and fact review.
- Creator: Researcher, analyst, fact-checker, reviewer, or evidence lead.
- Consumer: Writer, reviewer, editor, decision-maker, and future maintainer.
- Mandatory information: claim/question, evidence summary, source link or
  citation, source type, reliability, relevance, confidence, limitations.
- Optional information: counter-evidence, quote location, date accessed,
  alternative interpretations, owner, status.
- Quality criteria: claims are granular; evidence is traceable; confidence is
  explicit; conflicts are visible.
- Common mistakes: turning the table into a bibliography; hiding weak evidence;
  copying long quotes instead of summarizing support; no confidence labels.
- Lifecycle: built during synthesis -> reviewed -> used in report/checking ->
  archived or distilled into source notes.
- Retirement conditions: superseded by updated evidence, report withdrawn, or
  source state becomes obsolete.
- AIEO note: Highly valuable; overlaps evidence/confidence framework; strong
  candidate for future evaluation in research-heavy tasks.

### 3.10 Fact-Checking Log

- Purpose: Tracks factual claims, checks performed, source support,
  corrections, and unresolved issues.
- Problem it solves: Separates editorial confidence from writer confidence and
  gives reviewers a claim-by-claim trail.
- When created: Before publication, especially for journalism, research
  reports, policy memos, and public claims.
- Creator: Fact-checker, editor, research assistant, reviewer, or writer under
  independent check.
- Consumer: Editor, legal reviewer, publication owner, writer, and future
  corrections process.
- Mandatory information: claim, source checked, check result, correction
  needed, status, checker, date.
- Optional information: risk level, source quote/location, contact notes,
  unresolved ambiguity, legal sensitivity.
- Quality criteria: checks material claims, numbers, names, dates, quotations,
  attributions, and causal claims; unresolved items are visible.
- Common mistakes: checking only obvious facts; not checking paraphrase
  accuracy; marking "verified" without source; ignoring context.
- Lifecycle: opened during review -> resolved before publication or escalated
  -> archived with final artifact.
- Retirement conditions: publication complete and correction window handled;
  retained when audit trail matters.
- AIEO note: Potentially valuable; overlaps review/evidence concepts; future
  evaluation needed for risk thresholds.

### 3.11 Verification Log

- Purpose: Records verification of media, source identity, document
  provenance, technical claims, or event evidence.
- Problem it solves: Prevents false material from being accepted because it is
  vivid, viral, plausible, or repeated.
- When created: During investigative journalism, OSINT, emergency reporting,
  security review, and source-sensitive research.
- Creator: Verification specialist, reporter, investigator, OSINT analyst, or
  fact-checker.
- Consumer: Editor, reviewer, legal/security reviewer, writer, and publication
  owner.
- Mandatory information: item verified, provenance, method, tools used,
  corroboration, result, uncertainty, verifier, date.
- Optional information: geolocation, metadata, reverse-image/video checks,
  contact with original source, chain of custody.
- Quality criteria: distinguishes source verification from content
  verification; records uncertainty; uses triangulation where possible.
- Common mistakes: treating metadata as decisive; not contacting original
  source when needed; omitting failed checks; over-trusting tools.
- Lifecycle: opened when questionable evidence appears -> updated through
  verification -> resolved, escalated, or excluded.
- Retirement conditions: evidence excluded, published with confidence note, or
  superseded by stronger verification.
- AIEO note: Valuable for source-sensitive work; overlaps evidence framework
  but is more operational; future evaluation required.

### 3.12 Interview / Source Notes

- Purpose: Preserves what a human source said, under what ground rules, and how
  the information may be used.
- Problem it solves: Prevents memory drift, quote misuse, source ambiguity, and
  disputes about attribution.
- When created: During reporting, investigations, research, policy work, UX
  research, and expert interviews.
- Creator: Reporter, researcher, analyst, interviewer, or investigator.
- Consumer: Writer, editor, fact-checker, reviewer, legal reviewer.
- Mandatory information: source identity or protected status, date, context,
  ground rules, notes, usable claims, attribution limits.
- Optional information: recording location, consent, follow-up questions,
  source reliability assessment, conflicts of interest.
- Quality criteria: clearly separates direct quote, paraphrase, inference, and
  interviewer interpretation.
- Common mistakes: unclear on/off-record status; selective notes; missing date;
  quote cleanup that changes meaning.
- Lifecycle: captured during interview -> clarified with source if appropriate
  -> used in evidence table/fact check -> archived securely.
- Retirement conditions: source withdrawn, material no longer needed, or
  retention limit reached.
- AIEO note: Potentially valuable for tasks using interviews; not generally
  needed for desk-only work.

### 3.13 Research Memo

- Purpose: Synthesizes research into an internal analytical explanation before
  final publication or decision.
- Problem it solves: Gives teams a place to reason, compare evidence, and state
  uncertainty without premature final form.
- When created: After evidence collection and before report, recommendation, or
  decision.
- Creator: Researcher, analyst, investigator, or policy analyst.
- Consumer: Editor, writer, reviewer, project lead, decision-maker.
- Mandatory information: question, method/source basis, findings, evidence,
  uncertainty, implications, open questions.
- Optional information: alternative interpretations, source limitations,
  appendix of evidence, next research needs.
- Quality criteria: separates findings from recommendations, evidence from
  inference, and confidence from certainty.
- Common mistakes: becoming a source dump; hiding contradictions; writing for
  polish instead of reasoning; no conclusion.
- Lifecycle: drafted -> reviewed -> revised -> feeds report/recommendation ->
  archived as working memory.
- Retirement conditions: superseded by final report or new evidence.
- AIEO note: Strongly overlaps existing research artifacts; valuable but may be
  redundant unless shaped by task type.

### 3.14 Findings Report

- Purpose: Presents what the research or assessment found, with evidence and
  implications.
- Problem it solves: Allows readers to understand the state of knowledge before
  deciding what to do.
- When created: At the end of research, audit, review, investigation, or
  assessment.
- Creator: Researcher, analyst, auditor, investigator, reviewer, or assessment
  lead.
- Consumer: Decision-makers, editors, clients, public readers, implementation
  teams.
- Mandatory information: scope, method, key findings, evidence, limitations,
  confidence, implications.
- Optional information: recommendations, appendices, visualizations, detailed
  methods, source tables.
- Quality criteria: claims are supported; limitations are visible; structure
  lets readers distinguish major from minor findings.
- Common mistakes: mixing findings and advocacy; omitting negative findings;
  overclaiming; hiding weak evidence in appendices.
- Lifecycle: outline -> draft -> reviewed -> approved/published -> archived.
- Retirement conditions: superseded, corrected, withdrawn, or made obsolete by
  new evidence.
- AIEO note: Already central to research work; future evaluation may focus on
  evidence traceability rather than new artifact names.

### 3.15 Recommendation Memo

- Purpose: Converts findings into an advised course of action.
- Problem it solves: Makes the reasoning from evidence to action explicit
  enough for decision-makers to accept, reject, or revise.
- When created: After research and options analysis, before decision.
- Creator: Analyst, consultant, policy adviser, product lead, editor, or
  architecture/security reviewer.
- Consumer: Decision-maker, sponsor, governance board, implementation owner.
- Mandatory information: decision question, recommendation, evidence basis,
  options considered, tradeoffs, risks, implementation implications,
  confidence.
- Optional information: cost/benefit, sequencing, dependencies, dissenting
  view, decision deadline.
- Quality criteria: actionable, not merely descriptive; alternatives are fair;
  residual risk is visible.
- Common mistakes: recommendation without options; advocacy detached from
  evidence; ignoring feasibility; burying risks.
- Lifecycle: drafted -> challenged -> revised -> accepted/rejected/deferred ->
  archived with decision.
- Retirement conditions: decision made, recommendation superseded, or context
  changes.
- AIEO note: Potentially valuable; overlaps planning/synthesis; requires future
  architectural evaluation to keep recommendations distinct from decisions.

### 3.16 Decision Memo

- Purpose: Records the decision request, options, analysis, decision, rationale,
  owner, and consequences.
- Problem it solves: Prevents decisions from becoming oral folklore or being
  reopened without new evidence.
- When created: Before or at the decision point for consequential choices.
- Creator: Decision owner, analyst, chief editor, product lead, policy adviser,
  or committee secretary.
- Consumer: Decision-maker, implementers, reviewers, auditors, future teams.
- Mandatory information: decision to make, context, options, criteria,
  recommendation or selected option, rationale, owner, date, consequences.
- Optional information: dissent, risk acceptance, review comments, constraints,
  implementation next steps.
- Quality criteria: explains why, not only what; names alternatives; records
  decision rights; states what would trigger reconsideration.
- Common mistakes: documenting after the fact with sanitized rationale; no
  alternatives; no owner; no link to evidence.
- Lifecycle: proposed -> reviewed -> decided -> active -> revisited if trigger
  occurs -> archived/superseded.
- Retirement conditions: decision expires, is reversed, superseded, or no
  longer relevant.
- AIEO note: Highly valuable; overlaps orchestration/final decision concepts;
  future evaluation needed for scope and thresholds.

### 3.17 Architecture Decision Record (ADR)

- Purpose: Captures an architecturally significant decision in concise,
  durable form.
- Problem it solves: Preserves rationale for hard-to-change technical choices
  so future maintainers understand context and consequences.
- When created: When choosing a technology, interface, pattern, constraint, or
  architecture direction with lasting consequences.
- Creator: Architect, senior engineer, technical lead, or team collectively.
- Consumer: Engineers, architects, reviewers, operators, auditors, future
  maintainers.
- Mandatory information: status, context, decision, consequences, date, owner.
- Optional information: options considered, links to RFC/design doc, risk,
  related decisions, supersession.
- Quality criteria: concise, discoverable, decision-focused, updated when
  superseded, linked to implementation context.
- Common mistakes: recording every minor choice; omitting consequences;
  treating ADRs as implementation specs; never marking superseded decisions.
- Lifecycle: proposed -> accepted/rejected -> active -> amended only by new
  ADR or status change -> superseded/deprecated.
- Retirement conditions: decision superseded, system retired, or artifact
  archived with historical value.
- AIEO note: Potentially valuable for future technical governance; overlaps
  decision documentation; requires architectural evaluation before adoption.

### 3.18 RFC / Proposal Record

- Purpose: Opens a substantial change proposal for structured community or
  stakeholder review before acceptance.
- Problem it solves: Prevents large changes from being implemented before
  motivation, design, alternatives, compatibility, and objections are tested.
- When created: For significant protocol, platform, product, policy, workflow,
  or system changes.
- Creator: Proposer or working group; reviewed by maintainers, stakeholders,
  or standards body.
- Consumer: Reviewers, implementers, maintainers, governance group, affected
  users.
- Mandatory information: summary, motivation, design, alternatives, drawbacks,
  compatibility, unresolved questions, status.
- Optional information: reference implementation, migration plan, security
  considerations, operational impact, examples.
- Quality criteria: public enough for relevant challenge; specific enough to
  implement later; explicit about open issues and consensus status.
- Common mistakes: using an RFC as a sales pitch; hiding tradeoffs; accepting
  without review; failing to update status.
- Lifecycle: draft -> discussion -> revision -> accepted/rejected/deferred ->
  implemented or archived -> superseded.
- Retirement conditions: rejected, withdrawn, implemented and preserved as
  rationale, or superseded by later RFC.
- AIEO note: Highly valuable as a professional pattern; overlaps design-change
  governance; future evaluation needed, not implementation advice.

### 3.19 Design Review Packet

- Purpose: Presents a design and its evidence, requirements, tradeoffs, risks,
  and open questions for structured critique.
- Problem it solves: Finds defects in reasoning before production or
  implementation cost rises.
- When created: Before committing to significant product, engineering,
  editorial, service, or content-system design.
- Creator: Designer, engineer, architect, UX/content lead, product lead.
- Consumer: Review panel, peers, stakeholders, implementers, governance owner.
- Mandatory information: problem, goals/non-goals, requirements, design,
  alternatives, risks, test/validation plan, open questions.
- Optional information: prototypes, diagrams, metrics, user research, security
  notes, rollout plan.
- Quality criteria: reviewable at the right abstraction level; key decisions
  and tradeoffs are visible; asks reviewers for specific judgments.
- Common mistakes: showing only final solution; no alternatives; reviewer
  feedback too late; confusing review with presentation.
- Lifecycle: draft -> review -> revision -> approval/changes requested ->
  implementation handoff or archive.
- Retirement conditions: design replaced, implemented and documented, or
  abandoned.
- AIEO note: Potentially valuable for complex production/design tasks; overlaps
  review and planning; future evaluation required.

### 3.20 Architecture Assessment

- Purpose: Evaluates an architecture against agreed principles, qualities,
  constraints, standards, and risks.
- Problem it solves: Makes architecture quality explicit instead of relying on
  personal taste or authority.
- When created: During major design, modernization, governance review, cloud
  review, or portfolio assessment.
- Creator: Architect, architecture review board, external reviewer, senior
  engineering reviewer.
- Consumer: Technology leaders, implementation teams, risk/security owners,
  governance board.
- Mandatory information: assessment scope, criteria, evidence, findings,
  risks, recommendations or required changes, residual concerns.
- Optional information: maturity model, scoring, diagrams, dependency map,
  roadmap implications, exceptions.
- Quality criteria: criteria-based, evidence-backed, distinguishes required
  changes from advisory observations.
- Common mistakes: style policing; no explicit criteria; no risk owner;
  producing a score without actionable findings.
- Lifecycle: scoped -> assessed -> reviewed -> findings accepted or disputed ->
  follow-up tracked -> archived.
- Retirement conditions: architecture superseded, issues resolved, or
  assessment expires.
- AIEO note: Valuable as research pattern; may overlap future governance; not
  relevant to ordinary editorial tasks without future evaluation.

### 3.21 Peer Review Report

- Purpose: Provides independent expert critique of scholarly, analytical, or
  technical work.
- Problem it solves: Tests validity, originality, method, evidence, clarity,
  and contribution before publication or acceptance.
- When created: After submission/draft and before publication, funding, or
  formal acceptance.
- Creator: Peer reviewer or expert panel independent from author.
- Consumer: Editor, author, program committee, journal, funder, or governance
  body.
- Mandatory information: summary, major issues, minor issues, evidence/method
  concerns, recommendation/verdict, confidentiality/COI compliance.
- Optional information: line comments, suggested literature, ethical concerns,
  reproducibility comments, reviewer confidence.
- Quality criteria: specific, constructive, scoped, fair, evidence-aware,
  separates fatal issues from improvements.
- Common mistakes: vague criticism; gatekeeping by preference; conflict of
  interest; abusive tone; ungrounded demands.
- Lifecycle: assigned -> completed -> editor decision -> author response ->
  further review if needed -> archived.
- Retirement conditions: manuscript rejected/accepted, review round closed, or
  replaced by updated review.
- AIEO note: Strongly overlaps review agent practice; professional peer-review
  structure may enrich future review rubrics.

### 3.22 Review Letter / Response Letter

- Purpose: Communicates review decisions and required revisions, or documents
  how authors responded to review.
- Problem it solves: Turns critique into an accountable revision conversation.
- When created: After peer/editorial review and during revision cycles.
- Creator: Editor/reviewer for review letter; author/team for response letter.
- Consumer: Author, editor, reviewer, committee, final approver.
- Mandatory information: decision/verdict, major required changes, rationale,
  deadline; for response: each comment, response, change made or reason
  declined.
- Optional information: annotated manuscript links, appeal path, editorial
  guidance, residual concerns.
- Quality criteria: complete mapping from comment to action; respectful;
  transparent about disagreements.
- Common mistakes: cherry-picking comments; vague "fixed" responses; reviewer
  scope creep; no link to revised text.
- Lifecycle: review -> letter -> revision -> response -> re-review or final
  decision -> archive.
- Retirement conditions: review cycle closed or work withdrawn.
- AIEO note: Potentially valuable; overlaps handoff/review artifacts; useful
  where revision traceability matters.

### 3.23 Risk Register

- Purpose: Maintains an active inventory of risks, owners, likelihood/impact,
  treatment, status, and review cadence.
- Problem it solves: Prevents risk from being discussed once and then forgotten
  until it becomes an incident.
- When created: At project/program start and updated continuously.
- Creator: Risk owner, project manager, security lead, governance lead, audit
  lead, or team.
- Consumer: Leadership, project team, reviewers, auditors, safety/security
  owners.
- Mandatory information: risk statement, cause/event/consequence, likelihood,
  impact, owner, treatment, residual risk, status, review date.
- Optional information: triggers, controls, dependencies, risk appetite,
  escalation threshold, evidence links.
- Quality criteria: risks are specific, owned, current, connected to decisions,
  and reviewed at meaningful intervals.
- Common mistakes: generic risks; no owner; no treatment; stale status; using
  color scores without judgment.
- Lifecycle: identified -> assessed -> treated/accepted/escalated -> monitored
  -> closed or converted to issue/incident.
- Retirement conditions: risk no longer possible/relevant, accepted and
  expired, transferred, or materialized as an issue.
- AIEO note: Highly valuable for high-risk editorial and system tasks; overlaps
  failure modes/quality; future evaluation needed.

### 3.24 Threat Model

- Purpose: Models assets, actors, trust boundaries, threats, attack paths, and
  mitigations.
- Problem it solves: Finds security and abuse risks before systems or content
  processes are deployed.
- When created: During design, major change, security review, AI/tool
  integration, and before launch for sensitive systems.
- Creator: Security engineer, architect, development team, privacy/safety
  reviewer, red team.
- Consumer: Engineers, security reviewers, product owners, risk owners,
  auditors.
- Mandatory information: system/context model, assets, entry points, trust
  boundaries, threat scenarios, mitigations, residual risks.
- Optional information: abuse cases, data-flow diagrams, STRIDE-style
  categories, control mapping, test cases.
- Quality criteria: specific to system and actors; actionable mitigations;
  residual risk visible; updated when design changes.
- Common mistakes: generic checklist threat model; no diagram/context;
  ignoring abuse cases; no owner for mitigations.
- Lifecycle: scoped -> modeled -> reviewed -> mitigations tracked -> updated
  with changes -> archived/superseded.
- Retirement conditions: system retired, model superseded, or risk context
  materially changed.
- AIEO note: Potentially valuable for future AI/tool/security work; not
  ordinary editorial architecture; requires future evaluation.

### 3.25 Security Review Report

- Purpose: Evaluates security posture, vulnerabilities, controls, and residual
  risk for a system, process, or release.
- Problem it solves: Turns security concerns into reviewed findings and
  accountable remediation.
- When created: Before release, after major change, during audit, or after
  security testing.
- Creator: Security reviewer, application security engineer, auditor, red team,
  or assessor.
- Consumer: Engineering owner, product owner, risk owner, leadership,
  compliance body.
- Mandatory information: scope, method, findings, severity, evidence,
  affected assets, remediation, owner, residual risk.
- Optional information: threat model links, test logs, exploitability notes,
  compensating controls, acceptance rationale.
- Quality criteria: severity is justified; findings are reproducible; fixes are
  actionable; false positives handled.
- Common mistakes: vulnerability dump without context; severity inflation; no
  risk acceptance; no retest.
- Lifecycle: planned -> tested/reviewed -> reported -> remediated/accepted ->
  retested -> closed.
- Retirement conditions: findings closed, system changed, or report superseded.
- AIEO note: Potentially valuable only for technical/security scope; future
  architectural evaluation required.

### 3.26 Quality Checklist

- Purpose: Gives reviewers a consistent set of quality checks for a specific
  output type.
- Problem it solves: Reduces omissions and variability in repeated review
  workflows.
- When created: Before repeated production or when quality failures show a
  pattern.
- Creator: Editor, quality lead, standards owner, process owner, reviewer.
- Consumer: Producers, reviewers, approvers, trainers.
- Mandatory information: check item, pass/fail or evidence expectation,
  escalation condition, owner or stage.
- Optional information: examples, severity, references, automation hooks,
  review notes.
- Quality criteria: short enough to use; specific enough to catch real failure;
  tied to action, not ritual.
- Common mistakes: oversized checklist; vague items; no owner; no retirement of
  obsolete checks; checking everything equally.
- Lifecycle: drafted -> trialed -> adopted -> updated from failures -> pruned
  when stale.
- Retirement conditions: output type retired, risk removed, or checklist no
  longer improves quality.
- AIEO note: Potentially valuable; overlaps quality attributes/review; future
  evaluation should prevent checklist theater.

### 3.27 Publication Readiness Checklist

- Purpose: Confirms that work is ready for release to its intended audience.
- Problem it solves: Prevents publication with unresolved factual, legal,
  ethical, accessibility, formatting, or approval issues.
- When created: Before publication, delivery, launch, or external release.
- Creator: Editor, publication manager, release manager, final reviewer.
- Consumer: Publisher, editor, author, legal/compliance reviewer, delivery
  owner.
- Mandatory information: factual checks, source/citation status, rights,
  accessibility, style, format, approvals, corrections path, residual issues.
- Optional information: SEO/social metadata, distribution plan, localization,
  stakeholder notifications, embargo.
- Quality criteria: tied to release decision; includes stop conditions; checks
  audience usability, not only internal process.
- Common mistakes: using it as decoration after approval; omitting source
  readiness; no blocker category; no owner for fixes.
- Lifecycle: prepared -> checked -> blockers resolved/accepted -> release ->
  archived with final artifact.
- Retirement conditions: publication complete, withdrawn, or superseded by a
  later release checklist.
- AIEO note: Highly valuable for publication-grade tasks; overlaps review/final
  delivery; future evaluation required.

### 3.28 Style Sheet / Editorial Style Guide

- Purpose: Records style, spelling, terminology, capitalization, formatting,
  and usage decisions for consistent text.
- Problem it solves: Prevents inconsistent editorial choices and repeated
  low-value debates.
- When created: For publications, brands, clients, journals, books, teams, or
  repeated content types.
- Creator: Editor, copyeditor, style lead, documentation lead, brand/content
  lead.
- Consumer: Writers, editors, reviewers, translators, designers,
  documentation teams.
- Mandatory information: terms, spelling, capitalization, numbers/dates,
  punctuation, naming, source/citation conventions.
- Optional information: voice/tone, forbidden terms, examples, client-specific
  rules, localization notes.
- Quality criteria: current, searchable, scoped, example-rich, consistent with
  higher authority.
- Common mistakes: mixing universal rules with task-specific choices; no owner;
  style rule sprawl; conflicts with canonical standards.
- Lifecycle: created -> used -> updated through editorial decisions -> versioned
  -> archived/superseded.
- Retirement conditions: publication/client/team retired, guide superseded, or
  rules merged into canonical source.
- AIEO note: Potentially valuable; overlaps style/client profile concepts; can
  be redundant without clear ownership.

### 3.29 Pattern Library Entry

- Purpose: Documents a reusable pattern: when to use it, how it works, examples,
  constraints, and known pitfalls.
- Problem it solves: Prevents teams from reinventing solutions or applying
  patterns without context.
- When created: After a pattern recurs or after a design system/content system
  standardizes it.
- Creator: Design system team, documentation lead, UX/content designer,
  architect, knowledge owner.
- Consumer: Designers, writers, engineers, editors, product teams, reviewers.
- Mandatory information: pattern name, purpose, use cases, anatomy, rules,
  examples, accessibility/quality constraints.
- Optional information: variants, anti-patterns, code/content snippets,
  research evidence, related patterns, ownership.
- Quality criteria: practical, example-based, scoped, maintained, connected to
  real use and user need.
- Common mistakes: pattern without evidence; too abstract; stale screenshots;
  no distinction between pattern and one-off example.
- Lifecycle: proposed -> reviewed -> published -> maintained -> deprecated or
  superseded.
- Retirement conditions: pattern no longer supported, harmful, obsolete, or
  replaced.
- AIEO note: Highly relevant to knowledge reuse; overlaps learning/canon
  evolution; future evaluation required.

### 3.30 Knowledge Base Article

- Purpose: Provides reusable answer, procedure, explanation, or reference for a
  known information need.
- Problem it solves: Reduces repeated support, preserves operational knowledge,
  and accelerates onboarding.
- When created: When a question recurs, a process stabilizes, or support
  tickets reveal a knowledge gap.
- Creator: Subject-matter expert, support/documentation writer, knowledge
  manager, engineer, editor.
- Consumer: Internal users, customers, support teams, operators, future
  contributors.
- Mandatory information: title, problem/question, audience, answer/procedure,
  prerequisites, date/owner, related links.
- Optional information: screenshots, examples, troubleshooting, warnings,
  decision context, tags.
- Quality criteria: findable, current, task-oriented, concise, tested against
  real user need.
- Common mistakes: dumping project notes; no owner; stale instructions; no
  feedback path; writing for experts only.
- Lifecycle: draft -> review -> publish -> monitor usage/feedback -> update ->
  archive.
- Retirement conditions: answer obsolete, product/process retired, or content
  merged into better article.
- AIEO note: Valuable for organizational memory; overlaps KB/learning; future
  evaluation could focus on article selection criteria.

### 3.31 Documentation Page / How-To / Reference Entry

- Purpose: Helps a user understand, perform, or look up something with minimal
  ambiguity.
- Problem it solves: Converts system behavior and domain knowledge into usable
  instructions and reference.
- When created: During product/service delivery, API release, process
  stabilization, or support improvement.
- Creator: Technical writer, content designer, engineer, product expert,
  editor.
- Consumer: Users, developers, operators, support teams, maintainers.
- Mandatory information: audience/task, prerequisites, steps or reference,
  expected result, warnings, examples, last updated.
- Optional information: conceptual explanation, troubleshooting, diagrams,
  related pages, version notes.
- Quality criteria: matches user intent; separates tutorial/how-to/reference/
  explanation when useful; tested for accuracy.
- Common mistakes: mixing goals; stale screenshots; missing prerequisites;
  product behavior not verified.
- Lifecycle: draft -> technical review -> editorial review -> publish -> update
  with product changes -> archive.
- Retirement conditions: feature/process retired, page superseded, or merged.
- AIEO note: Potentially useful for docs-style outputs; overlaps writing/review
  processes; future evaluation depends on task types.

### 3.32 Requirements / Product Requirements Document (PRD)

- Purpose: Defines what a product, feature, system, or service must achieve and
  how success will be judged.
- Problem it solves: Aligns product, design, engineering, research, and
  stakeholders before implementation.
- When created: Before design/implementation commitment; updated through
  discovery and decision.
- Creator: Product manager, business analyst, systems engineer, policy owner,
  or project lead.
- Consumer: Designers, engineers, QA, stakeholders, reviewers, support,
  decision-makers.
- Mandatory information: problem, users, goals, non-goals, requirements,
  constraints, success metrics, acceptance criteria.
- Optional information: market context, risks, dependencies, rollout,
  analytics, open questions, links to research.
- Quality criteria: solution-aware but not over-prescriptive where discovery is
  needed; testable; traceable to user/business need.
- Common mistakes: requirements as wish list; no non-goals; no priority; no
  acceptance criteria; hidden assumptions.
- Lifecycle: draft -> review -> approved -> implemented/changed -> closed or
  superseded.
- Retirement conditions: feature delivered, cancelled, or requirements replaced.
- AIEO note: Potentially valuable for implementation tasks; overlaps task
  object and planning; future evaluation required.

### 3.33 Acceptance Criteria / Definition Of Done

- Purpose: Defines observable conditions that must be true for work to be
  accepted.
- Problem it solves: Prevents subjective completion and late disagreement over
  whether work satisfies intent.
- When created: During planning or before execution begins.
- Creator: Product owner, editor, reviewer, QA lead, project lead, team.
- Consumer: Producer, implementer, reviewer, approver, tester.
- Mandatory information: outcome conditions, quality conditions, evidence
  required, exclusions, review/approval criteria.
- Optional information: examples, edge cases, test cases, performance targets,
  accessibility/legal checks.
- Quality criteria: testable, specific, tied to user/value, not merely a task
  list.
- Common mistakes: too vague; too implementation-heavy; no negative examples;
  missing quality attributes.
- Lifecycle: drafted -> reviewed -> used during work/review -> updated only
  through explicit scope change -> closed.
- Retirement conditions: work accepted, cancelled, or criteria superseded.
- AIEO note: Valuable; overlaps quality/outcome alignment; future evaluation
  could clarify artifact vs field.

### 3.34 Test / Validation Plan

- Purpose: Defines how claims, requirements, behavior, design assumptions, or
  readiness will be tested.
- Problem it solves: Prevents teams from discovering too late that success was
  never verifiable.
- When created: Before implementation, publication, experiment, launch, or
  high-risk decision.
- Creator: QA lead, researcher, engineer, systems engineer, editor, reviewer.
- Consumer: Implementers, reviewers, decision-makers, auditors, operators.
- Mandatory information: objectives, test subjects, method, acceptance
  criteria, data/evidence, responsibilities, schedule.
- Optional information: edge cases, risk-based priorities, automation,
  environment, rollback criteria.
- Quality criteria: tests material risks; connects to requirements; feasible;
  records evidence.
- Common mistakes: only happy-path testing; no owner; untestable criteria;
  validation after launch only.
- Lifecycle: planned -> executed -> results reviewed -> defects handled ->
  archived with release/report.
- Retirement conditions: validation complete, plan superseded, or system/report
  retired.
- AIEO note: Potentially useful for factual, technical, or publication
  validation; future evaluation needed.

### 3.35 Runbook / Playbook

- Purpose: Provides operational steps for repeated execution, response, or
  coordination under known conditions.
- Problem it solves: Reduces reliance on memory during routine work or
  high-pressure events.
- When created: When a process recurs, has risk, needs handoff, or must be
  executed reliably.
- Creator: Operations lead, engineer, editor, incident manager, project owner,
  knowledge manager.
- Consumer: Operators, editors, support teams, on-call engineers, coordinators.
- Mandatory information: trigger, prerequisites, steps, decision points,
  escalation, verification, rollback/stop condition, owner.
- Optional information: screenshots, commands, contact list, templates,
  examples, common failures.
- Quality criteria: executable by intended user, current, tested, specific,
  clear under pressure.
- Common mistakes: stale steps; no escalation; too much explanation; no test of
  usability.
- Lifecycle: drafted -> tested -> published -> used -> updated from incidents
  -> retired.
- Retirement conditions: process changed, risk removed, or playbook replaced.
- AIEO note: Potentially valuable for operating AIEO processes; overlaps
  pipelines; future evaluation required to avoid duplicating canon.

### 3.36 Lessons Learned

- Purpose: Captures reusable lessons after work completes.
- Problem it solves: Converts experience into organizational memory before it
  disappears into individual recollection.
- When created: After projects, launches, publications, investigations, audits,
  or major reviews.
- Creator: Project lead, facilitator, reviewer, participants, knowledge
  manager.
- Consumer: Future teams, process owners, governance bodies, training
  materials.
- Mandatory information: context, what happened, what worked, what failed,
  causes, reusable lesson, future trigger.
- Optional information: evidence, examples, recommended canon candidates,
  responsible owner, follow-up date.
- Quality criteria: specific, evidence-based, reusable, not blame-centered, not
  overgeneralized from one case.
- Common mistakes: inspirational slogans; no cause analysis; no owner; lessons
  never revisited.
- Lifecycle: collected -> reviewed -> distilled -> stored or canon-candidate
  marked -> revisited.
- Retirement conditions: lesson obsolete, incorporated into canon, or disproven
  by later evidence.
- AIEO note: Strong overlap with learning framework; valuable as research
  pattern; future evaluation can focus on selection and retirement.

### 3.37 Retrospective

- Purpose: Facilitates team reflection on process, collaboration, quality, and
  improvement after a cycle.
- Problem it solves: Gives teams a non-punitive structure to improve how they
  work.
- When created: At sprint/cycle/project end or after significant collaboration
  friction.
- Creator: Team facilitator, project lead, scrum master, editor, team.
- Consumer: Team, process owner, future participants.
- Mandatory information: what went well, what did not, root causes, decisions,
  action items, owners, due dates.
- Optional information: metrics, sentiment, experiments, unresolved tensions,
  follow-up review.
- Quality criteria: actionable, psychologically safe, focused on process and
  system conditions, not only individual performance.
- Common mistakes: venting without action; action items with no owner; ritual
  repetition; ignoring repeated issues.
- Lifecycle: prepare -> hold -> document actions -> follow up -> close or
  carry forward.
- Retirement conditions: action items completed/closed or cycle superseded.
- AIEO note: Potentially valuable; overlaps feedback/learning; future
  evaluation needed for when it is worth the overhead.

### 3.38 Postmortem / Incident Report

- Purpose: Explains what happened in an incident, why it happened, impact,
  detection, response, and prevention.
- Problem it solves: Creates blameless, evidence-based learning from failure
  and makes remediation accountable.
- When created: After incident, serious error, publication failure, outage,
  security event, or major process failure.
- Creator: Incident lead, responder, editor, reliability engineer, reviewer,
  safety/risk owner.
- Consumer: Team, leadership, affected stakeholders, future responders,
  auditors.
- Mandatory information: summary, timeline, impact, causes/contributing
  factors, detection, response, corrective actions, owners.
- Optional information: customer communications, metrics, screenshots/logs,
  near misses, what went well, unresolved questions.
- Quality criteria: blameless but accountable; cause-focused; action items are
  specific; evidence is preserved.
- Common mistakes: scapegoating; vague "human error"; no timeline; action items
  not tracked; hiding uncomfortable causes.
- Lifecycle: incident -> draft -> review -> publish internally/externally as
  appropriate -> action tracking -> close.
- Retirement conditions: actions closed and report archived; never erased when
  it serves safety memory.
- AIEO note: Highly valuable for future learning/failure-mode maturity; overlaps
  existing failure and learning frameworks.

### 3.39 Decision Log

- Purpose: Maintains an index of decisions, dates, owners, status, and links to
  detailed rationale.
- Problem it solves: Prevents teams from losing track of which decisions are
  active, superseded, or unresolved.
- When created: For projects with many decisions, long lifecycles, or repeated
  governance checkpoints.
- Creator: Project lead, architect, secretary, chief editor, product manager.
- Consumer: Team, reviewers, auditors, future maintainers, governance owners.
- Mandatory information: decision title, status, date, owner, short rationale,
  link to record/source, supersession status.
- Optional information: affected artifacts, dependencies, review trigger,
  related risks, version.
- Quality criteria: current, concise, linked, status-aware, not a duplicate of
  every decision record.
- Common mistakes: becoming a dumping ground; no status; decisions without
  rationale link; not marking superseded items.
- Lifecycle: opened early -> updated as decisions occur -> checked at review ->
  archived with project.
- Retirement conditions: project closed and archive complete, or migrated into
  permanent decision index.
- AIEO note: Potentially valuable for complex tasks; overlaps manifest/status;
  future evaluation needed to avoid duplication.

### 3.40 Archive / Supersession / Deprecation Notice

- Purpose: Tells readers that an artifact is obsolete, replaced, deprecated, or
  preserved only for history.
- Problem it solves: Prevents stale documents from becoming false authority.
- When created: When a document, rule, decision, pattern, report, or process is
  replaced or retired.
- Creator: Document owner, editor, architect, knowledge manager, governance
  owner.
- Consumer: Future readers, maintainers, auditors, search users, reviewers.
- Mandatory information: artifact status, replacement link, date, reason,
  owner, what not to use.
- Optional information: migration guidance, affected artifacts, retention
  period, historical note.
- Quality criteria: visible at point of use, unambiguous, linked to current
  authority.
- Common mistakes: deleting without trace; archiving without replacement;
  leaving stale documents searchable as current.
- Lifecycle: proposed -> applied -> maintained while artifact remains
  discoverable -> removed only when safe.
- Retirement conditions: artifact deleted from active corpus or all consumers
  migrated.
- AIEO note: Highly relevant to canon hygiene; overlaps current-version
  discipline; future evaluation may strengthen stale-artifact handling.

## 4. Deliverable Relationships

Professional deliverables are most useful when they form a dependency model.
The mature pattern is not "more documents"; it is "the smallest chain of
artifacts needed to preserve intent, evidence, decision, action, and memory."

### 4.1 Core Dependency Chain

1. Intake and framing:
   Editorial brief, research brief, terms of reference, problem statement,
   stakeholder map.

2. Inquiry design:
   Issue tree, source map, search log, interview plan, research plan.

3. Evidence capture:
   Evidence table, fact-checking log, verification log, interview/source notes,
   data inventory.

4. Analysis:
   Research memo, analytical memo, findings report, options analysis.

5. Recommendation and decision:
   Recommendation memo, decision memo, ADR, RFC, decision log.

6. Review and challenge:
   Peer review report, review letter, design review packet, architecture
   assessment, security review.

7. Action and release:
   Requirements/PRD, acceptance criteria, test/validation plan, runbook,
   publication readiness checklist.

8. Memory:
   Knowledge-base article, pattern-library entry, lessons learned,
   retrospective, postmortem, archive/supersession notice.

### 4.2 Dependency Rules

- Briefs feed every later artifact. If the brief changes, all downstream
  artifacts may need reassessment.
- Problem statements and issue trees decide what evidence is relevant.
- Source maps feed search logs and evidence tables.
- Evidence tables feed research memos, findings reports, fact-checking, and
  review.
- Fact-checking logs verify final claims, not the entire source universe.
- Verification logs are specialized evidence artifacts for contested,
  source-sensitive, media, OSINT, or provenance-heavy claims.
- Research memos feed findings reports and recommendation memos.
- Findings reports can exist without recommendations; recommendations should
  not exist without findings or equivalent evidence.
- Decision memos summarize research, options, recommendation, and risk.
- ADRs and RFCs preserve technical or system change decisions; they may depend
  on design reviews, threat models, and architecture assessments.
- Risk registers and threat models feed design review, security review,
  publication readiness, and decision acceptance.
- Quality and publication checklists consume prior artifacts; they should not
  invent missing evidence at the end.
- Knowledge-base and pattern-library entries distill reusable content from
  completed work; they should not copy entire project artifacts.
- Postmortems and lessons learned feed future checklists, patterns, training,
  and canon candidates.
- Archive/supersession notices protect the whole system from stale authority.

### 4.3 Replace, Summarize, Feed, Preserve

| Relationship | Pattern | Example |
| --- | --- | --- |
| Depends on | Later artifact requires earlier context | Recommendation memo depends on findings/evidence |
| Summarizes | Higher-level artifact compresses evidence | Findings report summarizes evidence table |
| Replaces | New artifact becomes current authority | New ADR supersedes old ADR |
| Feeds | Artifact drives next production step | PRD feeds design and test plan |
| Governs | Artifact sets decision/quality standard | Style guide governs article editing |
| Audits | Artifact checks another artifact | Fact-checking log checks final draft |
| Distills | Artifact extracts reusable knowledge | Pattern entry distills lessons from repeated work |
| Retires | Artifact prevents stale use | Supersession notice retires old guidance |

### 4.4 Common Professional Workflows

Research workflow:

Brief -> research brief -> source map -> search log -> evidence table ->
research memo -> findings report -> peer/editorial review -> published report
or archived research.

Decision workflow:

Problem statement -> issue tree/options -> evidence table -> recommendation
memo -> decision memo -> decision log -> implementation artifacts -> lessons
learned.

Engineering change workflow:

Problem statement -> RFC/design review packet -> threat model/architecture
assessment as needed -> accepted decision/ADR -> implementation plan -> test
plan -> release readiness -> postmortem/retro if warranted.

Publication workflow:

Editorial brief -> reporting/research artifacts -> draft -> fact-checking log
and review -> style/accessibility/legal checks -> publication readiness
checklist -> publication -> corrections/updates/knowledge capture.

Incident learning workflow:

Incident record -> timeline -> postmortem -> corrective actions -> risk
register/checklist/pattern update -> action closure.

## 5. Deliverable Evolution

Professional organizations treat artifacts as living work products with status,
owner, review, and retirement. Stale artifacts are a recognized risk.

### 5.1 Common Lifecycle States

| State | Meaning | Typical artifacts |
| --- | --- | --- |
| Proposed | Artifact or decision is suggested but not accepted | RFC, ADR, problem statement, risk |
| Draft | Work is being authored and is not yet authoritative | brief, memo, report, checklist |
| Review | Artifact is open for critique or validation | peer review, design review, fact check |
| Revision | Author/team is responding to critique | review letter response, draft report |
| Approved | Authorized for use, publication, or implementation | decision memo, PRD, checklist |
| Published | Released to intended audience | report, KB article, pattern entry |
| Active | Current authority for work or operation | runbook, style guide, risk register |
| Monitored | Requires periodic review | risk register, threat model, KB article |
| Superseded | Replaced by newer artifact | ADR, style guide, report, pattern |
| Deprecated | Still visible but discouraged or scheduled for removal | pattern, API docs, process note |
| Archived | Preserved for history, not active use | old brief, closed report, incident record |
| Withdrawn | Removed from authority due to error or invalidity | report, recommendation, guidance |

### 5.2 Lifecycle Patterns By Artifact Type

Planning artifacts:

- Drafted early.
- Reviewed for sufficiency.
- Updated only when scope changes.
- Retired when final output closes or scope is replaced.

Evidence artifacts:

- Built incrementally.
- Reviewed for source quality and confidence.
- Linked to outputs.
- Marked stale when sources, facts, or dates change.

Decision artifacts:

- Proposed before decision.
- Accepted, rejected, deferred, or superseded.
- Kept as rationale even after implementation.
- Retired only by explicit supersession or system closure.

Review artifacts:

- Created against a specific version.
- Actioned through revision or decision.
- Closed when comments are resolved, rejected with rationale, or accepted as
  residual risk.

Quality/checklist artifacts:

- Piloted before becoming standard.
- Revised from recurring failures.
- Pruned to avoid ritual overload.
- Retired when risks or output type change.

Knowledge artifacts:

- Published only after reusable value is clear.
- Assigned owner and review cadence.
- Updated from use, feedback, and incidents.
- Archived when obsolete.

Incident-learning artifacts:

- Drafted soon after event.
- Reviewed for accuracy and blamelessness.
- Action items tracked.
- Retained as safety memory.

### 5.3 Professional Status Discipline

Mature organizations usually make at least five things visible:

- Current status: draft, active, approved, superseded, archived.
- Owner: who can update or retire the artifact.
- Scope: where the artifact applies and where it does not.
- Version/date: when it was last made true.
- Replacement path: what to use instead if stale.

This matters because old artifacts often look authoritative in search results.
The professional antidote is not deletion alone; it is visible lifecycle
metadata and replacement links.

## 6. Deliverable Selection

Experts do not create every possible artifact. Professional judgment is largely
the art of choosing the minimum useful artifact set for the risk, complexity,
novelty, reversibility, and memory burden of the work.

### 6.1 Lightweight Versus Heavyweight Artifacts

Lightweight artifacts are appropriate when:

- The task is low-risk.
- The decision is reversible.
- The audience is small and known.
- Evidence burden is low.
- The work will not become long-term authority.
- Coordination is simple.
- The cost of misunderstanding is low.

Heavyweight artifacts are justified when:

- The work affects public trust, safety, money, law, security, reputation, or
  system architecture.
- The decision is hard to reverse.
- Multiple roles must coordinate.
- Evidence quality is contested.
- The output will be reused or cited later.
- Reviewers need a trail.
- Failure would teach future teams something important.

### 6.2 Mandatory Versus Conditional Artifacts

Professional organizations often define a small mandatory core and a larger
conditional set.

Mandatory core for most serious work:

- Brief or equivalent task frame.
- Evidence/source notes appropriate to risk.
- Review artifact or review record.
- Final deliverable.
- Status/owner/version metadata.

Conditional artifacts:

- Source map when source discovery is complex.
- Evidence table when claims are numerous or consequential.
- Fact-checking log when public factual claims matter.
- Verification log when source provenance is uncertain.
- Decision memo when a consequential choice is being made.
- ADR/RFC when a durable system decision or change is proposed.
- Risk register when uncertainty must be monitored over time.
- Threat model when adversarial misuse or security boundaries matter.
- Publication readiness checklist when release failure would be costly.
- Postmortem when failure, near miss, or incident creates reusable learning.

### 6.3 Cost Versus Value

Artifact value comes from one or more of these functions:

- Preventing wrong work.
- Improving evidence quality.
- Enabling independent review.
- Coordinating specialists.
- Making decisions accountable.
- Reducing future maintenance cost.
- Protecting public/user trust.
- Supporting audit or compliance.
- Creating reusable memory.

Artifact cost includes:

- Authoring time.
- Review time.
- Maintenance burden.
- Search/noise burden.
- Process friction.
- Risk of false confidence.
- Risk that the artifact becomes stale authority.

The selection question is: "What failure would this artifact prevent, and is
that failure plausible and costly enough to justify the artifact?"

### 6.4 Risk-Based Creation

Create more explicit artifacts when risk rises along these dimensions:

- Factual risk: claims may be wrong, contested, or time-sensitive.
- Ethical risk: people may be harmed or misrepresented.
- Legal/compliance risk: rights, privacy, regulated claims, or auditability
  matter.
- Reputational risk: publication or decision affects trust.
- Security risk: adversarial behavior or sensitive systems/data are involved.
- Operational risk: failure interrupts service or repeatable process.
- Architectural risk: decisions are hard to reverse.
- Knowledge risk: future teams will need rationale.

### 6.5 Complexity-Based Creation

Create more structure when complexity rises:

- Many sources -> source map and evidence table.
- Many claims -> fact-checking log.
- Many stakeholders -> stakeholder map and terms of reference.
- Many options -> issue tree and options analysis.
- Many reviewers -> review letter/response matrix.
- Many decisions -> decision log.
- Many future users -> KB article or pattern-library entry.
- Many failure pathways -> risk register, threat model, or postmortem.

### 6.6 Professional Judgment Heuristics

- If the task can be restarted safely from memory, keep artifacts light.
- If the task must be restarted by another person, preserve frame, status, and
  evidence.
- If the work changes a system, preserve decision rationale.
- If the work makes factual claims to a public audience, preserve checking.
- If the work affects security, preserve threat reasoning.
- If the work will recur, distill it into a pattern or playbook.
- If an artifact has no consumer, do not create it.
- If an artifact has a consumer but no owner, redesign or avoid it.
- If a checklist does not change behavior, retire or rewrite it.

## 7. Anti-Patterns

### 7.1 Documentation Theater

Documents are created because a process requires them, but no one uses them to
think, review, decide, act, or learn.

Why it happens:

- Governance rewards visible compliance over useful judgment.
- Templates become proxies for quality.
- Reviewers check presence, not substance.
- Teams are afraid to delete inherited artifacts.

Damage:

- Creates false confidence.
- Consumes attention.
- Hides real uncertainty behind completed forms.

### 7.2 Duplicated Information

The same rule, decision, or evidence is copied across many artifacts.

Why it happens:

- No canonical owner.
- Fear that readers will not follow links.
- Templates demand the same fields repeatedly.
- Teams confuse traceability with copying.

Damage:

- Inconsistency.
- Stale fragments.
- Expensive updates.
- Conflicting authority.

### 7.3 Stale Documents As False Authority

Old artifacts remain discoverable and look current.

Why it happens:

- No lifecycle metadata.
- No owner.
- Search favors old pages.
- Supersession is not recorded.

Damage:

- Future work follows obsolete decisions.
- Review debates already-settled issues.
- Trust in documentation declines.

### 7.4 Oversized Templates

Templates demand more information than the task needs.

Why it happens:

- Past failures are patched by adding fields.
- One template is used for all risk levels.
- Governance optimizes for completeness over judgment.

Damage:

- People fill fields mechanically.
- Important signals are buried.
- Lightweight work becomes slow without becoming safer.

### 7.5 Missing Ownership

Artifacts exist without an accountable owner for updates, retirement, or
quality.

Why it happens:

- Artifact creation is assigned; maintenance is not.
- Ownership changes after project closure.
- Shared documents become "everyone's" responsibility.

Damage:

- Artifacts decay.
- Decisions cannot be challenged cleanly.
- Consumers stop trusting the corpus.

### 7.6 No Consumer

An artifact is produced but no role uses it.

Why it happens:

- Process imported from another organization.
- Artifact has symbolic status.
- Producer assumes future usefulness without evidence.

Damage:

- Waste.
- Artifact pile-up.
- Cynicism about process.

### 7.7 Premature Formalization

Teams formalize a pattern before they understand it.

Why it happens:

- Desire for control.
- One successful case is treated as universal.
- Leaders want repeatability before variation is understood.

Damage:

- Bad patterns become canon.
- Local context is erased.
- Teams route around the process.

### 7.8 Document Explosion

Every problem receives a new artifact type.

Why it happens:

- Each failure triggers a new document.
- No retirement discipline.
- Teams prefer adding artifacts to improving existing ones.

Damage:

- Harder onboarding.
- Fragmented context.
- More process without more quality.

### 7.9 Evidence Laundering

Weak evidence becomes authoritative after being summarized repeatedly.

Why it happens:

- Secondary summaries cite each other.
- Evidence tables are absent.
- Confidence labels are omitted.
- Review checks prose rather than source support.

Damage:

- Unsupported claims look established.
- Decisions rest on narrative momentum.
- Corrections become difficult.

### 7.10 Checklist Theater

Checklists are completed after the real decision has already been made.

Why it happens:

- Readiness checks are placed too late.
- Blockers have no authority.
- Teams fear delaying release.

Damage:

- Readiness process cannot stop harm.
- Repeated failures survive.
- Review becomes ritual.

### 7.11 Review Without Response

Comments are gathered, but no one records whether they were accepted,
rejected, or resolved.

Why it happens:

- Review is treated as conversation, not decision input.
- No response letter or comment matrix.
- Time pressure.

Damage:

- Same issues recur.
- Reviewers lose trust.
- Final artifact has unresolved defects.

### 7.12 Knowledge Base As Dumping Ground

Project notes, old decisions, drafts, and reusable guidance are all stored
together.

Why it happens:

- Archiving is easier than distillation.
- Knowledge managers lack authority to prune.
- Search replaces taxonomy.

Damage:

- Readers cannot tell current from historical.
- Good guidance is buried.
- Maintenance becomes impossible.

## 8. AI Editorial Office Notes

These notes are preliminary research observations only. They do not recommend
implementation and do not redesign AI Editorial Office.

| Deliverable | Potentially valuable | Potentially redundant | Overlaps existing AIEO concepts | Requires future architectural evaluation |
| --- | --- | --- | --- | --- |
| Editorial Brief | Yes | Sometimes | Intake, brief, audience/outcome, task object | Yes |
| Research Brief | Yes | Sometimes | Research pipeline, evidence framework | Yes |
| Terms of Reference / Scope Note | Yes for formal reviews | Yes for ordinary tasks | Orchestration plan, manifest, governance | Yes |
| Problem Statement | Yes | Low | Planning framework, task understanding | Yes |
| Issue Tree | Yes for complex analysis | Yes for simple tasks | Planning framework, research structure | Yes |
| Stakeholder / Audience Map | Yes | Sometimes | Audience/outcome alignment | Yes |
| Source Map | Yes | Low | Evidence framework, research artifacts | Yes |
| Search / Research Log | Yes for high-evidence tasks | Yes for light tasks | Evidence/source notes | Yes |
| Evidence Table | Yes | Low | Evidence/confidence framework | Yes |
| Fact-Checking Log | Yes for public factual output | Yes for low-risk internal notes | Review, evidence framework | Yes |
| Verification Log | Yes for provenance-heavy tasks | Yes for ordinary desk research | Evidence framework | Yes |
| Interview / Source Notes | Yes when human sources used | Yes otherwise | Research artifacts | Conditional |
| Research Memo | Yes | Sometimes | Research report, handoff | Yes |
| Findings Report | Yes | Low | Research output | Yes |
| Recommendation Memo | Yes | Sometimes | Planning/synthesis/decision frame | Yes |
| Decision Memo | Yes | Sometimes | Orchestration, final decision, status | Yes |
| ADR | Yes for technical decisions | Yes for editorial-only tasks | Decision records | Yes |
| RFC / Proposal Record | Yes for major system changes | Yes for small changes | Governance and planning | Yes |
| Design Review Packet | Yes for complex design | Yes for text-only tasks | Review/orchestration | Yes |
| Architecture Assessment | Yes for architecture work | Yes for ordinary tasks | Review/governance | Yes |
| Peer Review Report | Yes | Low | Review artifact | Yes |
| Review Letter / Response Letter | Yes where revisions matter | Sometimes | Review and handoff | Yes |
| Risk Register | Yes for ongoing risk | Yes for simple tasks | Failure modes, quality, status | Yes |
| Threat Model | Yes for security/AI-tool work | Yes for ordinary writing | Risk/security review | Yes |
| Security Review Report | Yes for technical scope | Yes for editorial-only scope | Review/risk | Yes |
| Quality Checklist | Yes | High if generic | Quality attributes, review | Yes |
| Publication Readiness Checklist | Yes | Low for publication-grade work | Review/final delivery | Yes |
| Style Sheet / Style Guide | Yes | Sometimes | Client profile, style standards | Yes |
| Pattern Library Entry | Yes | Low if pattern proven | Learning/canon evolution | Yes |
| Knowledge Base Article | Yes | Sometimes | KB, learning framework | Yes |
| Documentation Page / How-To / Reference | Yes for docs outputs | Sometimes | Writing/review | Conditional |
| Requirements / PRD | Yes for implementation tasks | Yes for editorial-only tasks | Task object, planning | Yes |
| Acceptance Criteria / Definition Of Done | Yes | Sometimes | Quality/outcome, review | Yes |
| Test / Validation Plan | Yes for verifiable systems/claims | Yes for low-risk prose | Review, quality, evidence | Yes |
| Runbook / Playbook | Yes for repeatable operations | Yes if duplicating pipelines | Pipelines, scripts, KB | Yes |
| Lessons Learned | Yes | Low | Learning framework | Yes |
| Retrospective | Yes conditionally | Yes if ritual | Feedback/learning | Yes |
| Postmortem / Incident Report | Yes | Low after serious failure | Failure modes, learning | Yes |
| Decision Log | Yes for complex tasks | Yes if duplicating status | Manifest/status/current-version discipline | Yes |
| Archive / Supersession Notice | Yes | Low | Current-version discipline, canon hygiene | Yes |

### 8.1 Where AIEO Appears Strong Today

- Governance boundaries and role separation.
- Review gate awareness.
- Task-state thinking through manifest/status/orchestration concepts.
- Evidence and confidence vocabulary.
- Audience and outcome alignment.
- Quality attributes and accepted tradeoffs.
- Failure-mode detection and recovery.
- Canon evolution and learning discipline.
- Current-version discipline.

### 8.2 Where Professional Deliverables Could Improve Future Design

Preliminary areas for later evaluation:

- Stronger source discovery artifacts before evidence exists.
- More explicit evidence tables for claim-heavy research.
- Fact-checking and verification logs for public or high-risk outputs.
- Decision records for consequential choices.
- RFC-like proposal records for system changes.
- Risk registers and threat models for ongoing or adversarial risk.
- Publication readiness checks that combine evidence, style, accessibility,
  and residual risk.
- Pattern-library entries for reusable task solutions.
- Postmortems for serious process failures.

### 8.3 Boundary Note

This report does not say AI Editorial Office should adopt these artifacts. The
professional lesson is conditionality: mature organizations create artifacts
when they reduce real risk, clarify real decisions, enable real review, or
preserve reusable knowledge. The future architecture question is not "which
documents can be added?" It is "which professional work products deserve to
exist as task-local views under specific risk and complexity conditions?"

## 9. Sources

Source quality was assessed by authority type:

- Standards and official guidance: strongest for norms, lifecycle, governance,
  risk, security, peer review, and public-sector appraisal.
- Professional handbooks and organizational guidance: strong for newsroom,
  documentation, engineering, and reliability practice, though often
  organization-specific.
- Public open-source processes: useful evidence of modern engineering
  deliverable practice, but not universal standards.
- Books and industry methods: useful for consulting/product practice, but often
  proprietary or less publicly inspectable; treated as practice synthesis, not
  standards.
- Generic blogs were avoided except where a practice originated in a recognized
  practitioner source and no formal standard exists.

### 9.1 Editorial, Journalism, Fact-Checking, And Verification

- Reuters, "Standards and Values." Official newsroom standards. Source type:
  professional editorial standard. https://reutersagency.com/about/standards-values/
- Society of Professional Journalists, "SPJ Code of Ethics." Source type:
  professional ethics standard. https://www.spj.org/ethicscode.asp
- BBC Editorial Guidelines, especially accuracy, fairness, harm, and
  accountability guidance. Source type: organizational editorial standard.
  https://www.bbc.co.uk/editorialguidelines/guidelines/
- International Fact-Checking Network, "Code of Principles." Source type:
  professional fact-checking standard. https://ifcncodeofprinciples.poynter.org/
- European Journalism Centre / DataJournalism.com, "Verification Handbook."
  Source type: professional verification handbook. https://verificationhandbook.com/
- Reporters Without Borders / Journalism Trust Initiative. Source type:
  journalism trust and transparency standard/practice.
  https://www.journalismtrustinitiative.org/
- Associated Press, "News Values and Principles." Source type: professional
  newsroom standard. https://www.ap.org/about/news-values-and-principles/

### 9.2 Publishing, Scientific Journals, And Peer Review

- International Committee of Medical Journal Editors, "Recommendations for the
  Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical
  Journals." Source type: official scholarly publishing guidance, updated
  January 2026. https://www.icmje.org/recommendations/
- Committee on Publication Ethics, "Ethical Guidelines for Peer Reviewers."
  Source type: publication ethics guidance. https://publicationethics.org/
- Council of Science Editors, "White Paper on Publication Ethics." Source type:
  professional publishing guidance. https://www.councilscienceeditors.org/
- EQUATOR Network, reporting guidelines library. Source type: research
  reporting guideline infrastructure. https://www.equator-network.org/
- Open Access Scholarly Publishing Association, "Principles of Transparency and
  Best Practice in Scholarly Publishing." Source type: publishing transparency
  standard. https://oaspa.org/principles-of-transparency-and-best-practice-in-scholarly-publishing/

### 9.3 Consulting, Policy Analysis, Audit, And Public Decision Practice

- U.S. Government Accountability Office, "Yellow Book: Government Auditing
  Standards." Source type: official audit standard. https://www.gao.gov/yellowbook
- HM Treasury, "The Green Book." Source type: official appraisal and
  evaluation guidance. https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government
- U.S. Office of Management and Budget, "Circular A-4." Source type: official
  regulatory analysis guidance. https://www.whitehouse.gov/omb/information-for-agencies/circulars/
- RAND Corporation, research brief publication series. Source type: think-tank
  publication practice. https://www.rand.org/pubs/research_briefs.html
- National Academies, report review process and study reports. Source type:
  formal expert consensus/review practice. https://www.nationalacademies.org/

### 9.4 Engineering, RFCs, Architecture, And Design Review

- RFC Editor, RFC 2026, "The Internet Standards Process." Source type: official
  Internet standards process. https://www.rfc-editor.org/rfc/rfc2026
- RFC Editor, RFC 8729, "The RFC Series and RFC Editor." Source type: official
  RFC governance. https://www.rfc-editor.org/rfc/rfc8729
- Rust RFCs repository. Source type: open-source engineering process.
  https://github.com/rust-lang/rfcs
- Kubernetes Enhancements / KEP process. Source type: open-source engineering
  governance process. https://github.com/kubernetes/enhancements/tree/master/keps
- AWS Well-Architected Framework. Source type: official cloud architecture
  review framework. https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- NASA Systems Engineering Handbook. Source type: official high-reliability
  systems engineering guidance.
  https://www.nasa.gov/reference/systems-engineering-handbook/
- The Open Group, TOGAF Standard. Source type: enterprise architecture standard.
  https://pubs.opengroup.org/togaf-standard/
- Titus Winters, Tom Manshreck, Hyrum Wright, eds., "Software Engineering at
  Google", design documents and review practice. Source type: organizational
  engineering practice. https://abseil.io/resources/swe-book/

### 9.5 Security And Risk Management

- NIST SP 800-30 Rev. 1, "Guide for Conducting Risk Assessments." Source type:
  official risk assessment guidance. https://csrc.nist.gov/pubs/sp/800/30/r1/final
- NIST SP 800-218, "Secure Software Development Framework." Source type:
  official secure software development guidance.
  https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP, "Threat Modeling Cheat Sheet." Source type: professional security
  practice guidance. https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- ISO 31000:2018, "Risk management - Guidelines." Source type: international
  risk-management standard. https://www.iso.org/standard/65694.html
- MITRE ATT&CK. Source type: adversary behavior knowledge base.
  https://attack.mitre.org/

### 9.6 UX, Content Design, Documentation, And Pattern Libraries

- GOV.UK Service Manual. Source type: official service/content design guidance.
  https://www.gov.uk/service-manual
- GOV.UK Design System. Source type: official pattern/component library.
  https://design-system.service.gov.uk/
- Google Developer Documentation Style Guide. Source type: official technical
  documentation style guidance. https://developers.google.com/style
- Microsoft Writing Style Guide. Source type: official technical/editorial
  style guidance. https://learn.microsoft.com/en-us/style-guide/welcome/
- W3C Web Content Accessibility Guidelines 2.2. Source type: web accessibility
  standard. https://www.w3.org/TR/WCAG22/
- Diataxis documentation framework. Source type: widely used documentation
  practice framework. https://diataxis.fr/

### 9.7 Knowledge Management, Learning, And Reliability

- Google Site Reliability Engineering, "Postmortem Culture." Source type:
  organizational reliability practice. https://sre.google/sre-book/postmortem-culture/
- NASA Lessons Learned Information System. Source type: high-reliability
  lessons-learned practice. https://llis.nasa.gov/
- U.S. Army / Center for Army Lessons Learned, after-action review practice.
  Source type: high-reliability learning practice. https://www.army.mil/call/
- Atlassian Incident Management and postmortem guidance. Source type: industry
  practice guidance. https://www.atlassian.com/incident-management

### 9.8 Source Quality Assessment

The strongest sources for this report are official standards and public
professional guidance: Reuters, SPJ, ICMJE, COPE, GAO, HM Treasury, OMB, IETF,
NASA, NIST, OWASP, ISO, W3C, AWS, and GOV.UK. These sources are appropriate for
identifying durable artifact functions such as evidence, review, decision,
risk, readiness, and lifecycle control.

The weaker but still useful source class is public practice from open-source
and product organizations: Rust RFCs, Kubernetes KEPs, Google engineering/SRE,
Atlassian, Diataxis, and design systems. These are valuable as examples of how
professional organizations operationalize deliverables, but they should not be
treated as universal standards.

Consulting deliverables such as issue trees, recommendation memos, and problem
statements are widely used but less often specified in open standards. This
report treats them as professional practice synthesis rather than standards.
