# Knowledge Evolution Landscape

Date: 2026-07-09

## Research Question

What should a bounded Knowledge Evolution capability learn from mature
knowledge-management, organizational-learning, postmortem, decision-record,
documentation-governance, stale-knowledge, and correction practices?

## Executive Finding

World-class knowledge evolution is not a larger memory bucket. It is a governed
conversion path from situated experience into reusable, reviewed, owned, and
maintainable knowledge. The common pattern across strong systems is:

```text
capture locally -> validate evidence -> detect reuse or risk pattern ->
choose owner -> review change -> update, correct, retire, or defer ->
preserve traceability
```

The implication for AI Editorial Office is that Knowledge Evolution should
strengthen deliberate learning and canon hygiene inside the existing Learning
Framework, not create a new role, repository, memory database, or automatic
canon-promotion mechanism.

## Source Base

### Knowledge Management Systems

ISO 30401 frames knowledge management as a management system that must be
established, maintained, reviewed, and improved, and applies across
organization types and sizes. The ISO page also exposes standards lifecycle
thinking: the standard is reviewed periodically, may receive amendments, and
may include editorial or technical corrections. Source:
[ISO 30401:2018](https://www.iso.org/standard/68683.html).

Implications:

- Knowledge work needs an operating system, not just storage.
- Review and improvement are part of the system, not exceptional cleanup.
- Stale knowledge handling should be normal: review cycles, amendments,
  corrections, and replacements are expected parts of knowledge governance.

### Lessons Learned Systems

NASA's Lessons Learned system is described as a database of official, reviewed
lessons from NASA programs and projects. It is managed by a steering committee
and curator; approved lessons are indexed for retrieval; lesson records include
the driving event and recommendations, and those recommendations feed continual
improvement through training, best practices, policies, and procedures. Source:
[NASA Lessons Learned](https://www.nasa.gov/nasa-lessons-learned/).

Implications:

- A lesson is not just an observation. It becomes reusable after review,
  approval, indexing, and recommendation shaping.
- Traceability matters: the lesson points back to the event that produced it.
- Reuse requires retrieval design, not only preservation.
- Lessons may inform policy, but only after they have passed through a reviewed
  path.

### After Action Reviews

WHO's AAR guidance presents After Action Review as a methodology for planning
and implementing review of actions after public-health events and also as a
routine management tool for continuous learning and improvement. It names
multiple formats and includes designing, preparing, conducting, and following
up on each format. Source:
[WHO Guidance for After Action Review](https://www.who.int/publications/i/item/WHO-WHE-CPI-2019.4).

Implications:

- Retrospective work is bounded by a specific event, purpose, and follow-up
  path.
- The value is in learning that changes future practice, not in producing a
  ceremonial artifact.
- Different task shapes can use different review depths without inventing a new
  lifecycle.

### Engineering Incident Learning

Google SRE's postmortem culture treats postmortems as written records of
incidents, impacts, mitigation, root causes, and follow-up actions. Google
emphasizes pre-defined triggers, blamelessness, review before publication,
sharing to the widest useful audience, action items, postmortem repositories,
and metadata/trend analysis across postmortems. Sources:
[Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) and
[SRE Book table of contents](https://sre.google/sre-book/table-of-contents/).

Implications:

- Decide in advance what events deserve deeper learning extraction.
- Blamelessness improves reporting quality by reducing concealment.
- Review is not optional: an unreviewed learning artifact has little practical
  value.
- Patterns emerge across records; the system should allow trend detection
  without requiring every record to become canon.
- Metadata is useful only when it enables retrieval, comparison, or trend
  analysis.

### Knowledge-Centered Service

KCS treats knowledge as part of the work, not a separate after-the-fact
publishing department. It includes capture, structure, reuse, improvement, an
Evolve Loop, content health, and closed-loop feedback. KCS's "reuse is review"
practice says article use is a natural moment to improve knowledge. Its content
health indicators include uniqueness, completeness, clarity, valid links, and
correct metadata. Its archiving guidance warns against deleting old content
only because it is old; relevance, findability, structure, and domain analysis
matter more than age alone. Sources:
[KCS v6 Practices Guide](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide),
[Reuse is Review](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030/040/020),
[Archiving Old Articles](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010/044),
[Content Health Indicators](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010/065),
and
[Closed Loop Feedback](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/020/050).

Implications:

- Reuse is a quality signal: knowledge that future work touches should be
  checked, improved, or challenged then.
- A knowledge base becomes a junk drawer when uniqueness, completeness,
  metadata, link health, relevance, and owner boundaries are not managed.
- Low-use knowledge is not automatically obsolete; obsolete means contradicted,
  harmful, unreachable, duplicated, ownerless, or no longer applicable.
- Pattern analysis should happen across related records, not from one
  attractive case.

### Decision Record Maintenance

Michael Nygard's ADR pattern favors small modular decision records that capture
context, decision, status, and consequences. ADRs are kept even when reversed,
but marked deprecated or superseded with a replacement reference. Source:
[Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

MADR similarly treats decision records as structured records of significant
decisions, options, outcomes, and status. Source:
[Markdown Architectural Decision Records](https://adr.github.io/madr/).

Implications:

- Canon changes should preserve rationale, status, consequences, and
  replacement links when relevant.
- Retiring outdated guidance should not erase why it once existed.
- Small modular records are easier to maintain than large synthesized
  documents.
- "Superseded" and "deprecated" are legitimate knowledge states.

### Documentation Governance And Staleness

Google's developer documentation style guide explicitly defines a reference
hierarchy: project-specific guidance first, then the shared guide, then
third-party references. It also captures page freshness through "last updated"
metadata and lets readers report "out of date" issues. Its timeless
documentation guidance says time-sensitive terms like "new", "currently", and
"latest" can quickly become inaccurate; durable documentation should describe
the current state or give an explicit date/version reference when needed.
Sources:
[Google developer documentation style guide](https://developers.google.com/style)
and
[Timeless documentation](https://developers.google.com/style/timeless-documentation).

Implications:

- A knowledge system needs an authority hierarchy so local guidance does not
  override canon by accident.
- Staleness can be reduced by avoiding temporal language unless the date or
  version is explicit.
- Feedback channels should include "out of date" as a first-class signal.
- Metadata helps only when it supports freshness, ownership, or routing.

### Scientific Correction And Retraction Norms

ICMJE distinguishes correction, debate, evolving science, retraction, and
retraction with republication. Corrections should describe changes, cite the
original, preserve prior versions, mark older electronic versions, and point to
the most recent version. For serious concerns, expressions of concern and
retractions should be clearly labeled, linked in both directions with the
original, explain the reason, and keep retracted articles in the public domain
where possible. Sources:
[Corrections and Version Control](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html)
and
[Scientific Misconduct, Expressions of Concern, and Retraction](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/scientific-misconduct-expressions-of-concern-and-retraction.html).

Implications:

- Correction is not the same as deletion.
- Retired knowledge should remain traceable when future readers might encounter
  it or need the rationale.
- Uncertain concerns can be marked as concerns pending review; they should not
  be silently promoted or silently erased.
- Replacement and current-version pointers prevent stale knowledge from
  masquerading as current guidance.

## Cross-Disciplinary Patterns

| Pattern | Strong practice | Risk if missing |
| --- | --- | --- |
| Source-grounded capture | Learning points back to event, task, evidence, review, feedback, or repository inspection. | Attractive anecdotes become policy. |
| Promotion threshold | Reuse, future value, risk reduction, owner fit, and evidence decide promotion. | Canon bloats with task-local noise. |
| Owner-first updates | A single canonical owner is chosen before changing durable guidance. | Duplicate rules and conflicting documents. |
| Reviewed canon change | Learning may propose canon; review approves the change. | Automatic promotion bypasses governance. |
| Pattern confirmation | Repeated or high-impact signals are separated from one-off observations. | Every task becomes a precedent. |
| Stale knowledge challenge | Contradiction, broken links, stale source, owner mismatch, repeated exceptions, or old assumptions trigger review. | Old guidance remains active by inertia. |
| Correction/retirement visibility | Deprecated or superseded guidance keeps replacement and rationale. | Future agents cannot reconstruct why rules changed. |
| Demand-driven hygiene | Reuse, review, failed retrieval, and out-of-date feedback point to maintenance work. | Knowledge cleanup becomes arbitrary pruning. |
| Minimal metadata | Metadata exists for retrieval, freshness, ownership, status, and traceability. | The system creates bureaucratic fields no one uses. |
| Non-canonical memory boundary | Public/export memory mirrors canon but does not decide canon. | Memory becomes a second source of truth. |

## What Becomes Reusable

Knowledge is reusable when it has enough of the following:

- repeatable task shape or decision context;
- source evidence or reviewed artifact trail;
- clear applicability and non-applicability;
- future risk reduction or quality gain;
- named owner or destination;
- concise expression;
- discoverability where future agents will look;
- known retirement or challenge trigger.

Knowledge should remain task-local when it is:

- a one-off preference;
- an unreviewed interpretation;
- a context detail that matters only to one artifact;
- a weak observation without source evidence;
- a useful example but not yet a pattern;
- private/source-only material without explicit promotion scope;
- already covered by an existing canonical owner.

## Stale Knowledge Signals

Stale knowledge is not merely old. It is suspect when:

- repository state contradicts the rule;
- validation or review repeatedly needs an exception;
- an owner file duplicates or conflicts with another owner;
- source material is missing, unverified, or replaced;
- links, paths, role names, statuses, or template references no longer resolve;
- a rule says "current", "new", "latest", or "temporary" without date/version;
- a prior decision has been superseded without clear replacement pointer;
- `/about` diverges from canonical source files;
- repeated task-local notes point to the same weakness in canon.

## Junk-Drawer Failure Modes

Knowledge bases become junk drawers when they:

- preserve every observation with the same authority;
- lack owner boundaries;
- confuse source material, memory, research notes, feedback, and canon;
- do not distinguish candidate, accepted, superseded, retired, and rejected
  knowledge states;
- use cleanup as deletion rather than correction, replacement, or owner repair;
- create too much metadata for small tasks;
- hide stale guidance instead of marking it;
- lack review before policy/canon changes;
- optimize for collection volume instead of future retrieval and action.

## Design Implications For AI Editorial Office

1. Knowledge Evolution should be a bounded capability integrated into
   `editorial_learning_framework.md`, not a new canonical owner unless synthesis
   proves the existing owner cannot hold it.
2. The capability should make promotion states explicit: task-local,
   candidate, pattern, canon update candidate, accepted canon, superseded,
   retired, rejected.
3. It should add a compact evidence trail expectation: source artifact,
   evidence type, owner, decision, and disposition.
4. It should treat stale knowledge challenge as a reviewed correction path,
   not as immediate deletion.
5. It should preserve `/about` as external memory export and check drift after
   canonical changes.
6. It should reject mandatory new artifacts; existing `final_decision.md`,
   `feedback.md`, `review.md`, release reports, and implementation reports are
   sufficient places to record learning disposition.
7. Review Agent should challenge promotion criteria, source support,
   duplication, owner choice, stale guidance, and `/about` drift inside the
   normal review gate.

## Research Conclusion

The smallest architecture-compatible release is to clarify Knowledge Evolution
as the deliberate evolution layer already implied by the Learning Framework:
learning extraction, evidence-backed pattern confirmation, canon promotion
decision, stale knowledge challenge, correction/retirement, and memory sync
disposition. This should strengthen the existing learning/canon owner, add
discoverability in registry/lifecycle/role/review references, and avoid a new
role, pipeline, lifecycle stage, or knowledge database.
