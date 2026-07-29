# Deliverable Catalogue

This directory stores reusable knowledge about deliverable types. It helps
Task Need Recognition compare plausible artifact shapes and helps Chief Editor
choose a single deliverable or a minimal coordinated set.

The catalogue is not a template library, closed taxonomy, pipeline registry,
document generator, role, classifier, or automatic packaging rule. A catalogue
entry describes editorial fitness; it does not authorize production. Missing
catalogue coverage does not forbid a task-specific deliverable.

Capability names do not create deliverable profiles. Product Intent Review, for
example, should normally use `Report`, `Research Report`, `Decision Memo`, or an
embedded block according to the reader's job. A separately named task-local
report may be selected when needed without adding a catalogue profile.

## Ownership And Use

- This directory owns deliverable-type knowledge: purpose, fit, limitations,
  failure modes, companion relationships, and nearby-type distinctions.
- `/kb/task_need_recognition.md` owns advisory outcome-first recommendation and
  minimal-set reasoning.
- Chief Editor owns the selected deliverable set and production order.
- Existing Writers own production under the selected route.
- Review Agent owns independent minimality, sufficiency, and artifact-purpose
  checks.

Load only the profiles needed to compare material candidates or companions. Do
not load the whole catalogue for an obvious single-format request.

## Profile Schema

Every entry answers:

- Purpose;
- Best Use Cases;
- Weak Use Cases;
- Typical Reader Goal;
- Typical Structure at a high level, never as a fillable template;
- Strengths;
- Weaknesses;
- Common Failure Modes;
- Typical Companion Deliverables;
- Not This, distinguishing nearby deliverables.

## Catalogue

| Deliverable | Primary communication job | Common nearby distinction |
| --- | --- | --- |
| [Article](article.md) | explain or argue one editorial idea | shorter and less instructional than a longread |
| [Longread](longread.md) | build a substantial mental model | deeper synthesis than an article; not step-by-step by default |
| [Tutorial](tutorial.md) | teach a reproducible procedure or skill | guided learning, not reference lookup |
| [Roadmap](roadmap.md) | sequence future progress and checkpoints | direction and order, not an immediate checklist |
| [Checklist](checklist.md) | prevent omissions during known work | execution control, not conceptual explanation |
| [Cheat Sheet](cheat-sheet.md) | support fast recall during use | compressed memory aid, not a learning path |
| [FAQ](faq.md) | resolve recurring audience questions | question-led access, not a coherent argument |
| [Comparison Matrix](comparison-matrix.md) | compare options on shared criteria | evidence-backed comparison, not a decorative table |
| [Executive Brief](executive-brief.md) | transfer decision-relevant context quickly | informs an executive reader; may not ask for one decision |
| [Decision Memo](decision-memo.md) | secure a bounded decision or approval | recommendation and ask, not neutral reporting |
| [Presentation](presentation.md) | support a live or asynchronous visual narrative | audience-facing visual sequence, not speaker notes |
| [Speaker Notes](speaker-notes.md) | help a presenter deliver the approved narrative | delivery support, not the audience deck |
| [Report](report.md) | document findings, analysis, and implications | general analytical record, not necessarily source-heavy research |
| [Research Report](research-report.md) | preserve method, evidence, findings, and limits | evidence product, not only an executive digest |
| [BRD](brd.md) | align stakeholders on business need and requirements | business agreement, not implementation detail |
| [Specification](specification.md) | define implementable behavior and acceptance | precise build contract, not business rationale |
| [Implementation Plan](implementation-plan.md) | sequence delivery work, owners, dependencies, and validation | execution plan, not a product roadmap or specification |
| [Interview](interview.md) | publish an expert or participant voice through questions | attributed conversation, not an anonymous article |
| [Announcement](announcement.md) | make a bounded change, event, or release known | notification and action cue, not full explanation |
| [Reference](reference.md) | support repeated lookup of stable facts or rules | non-linear lookup, not guided teaching |

## Catalogue Maintenance

Add or revise a profile only through a reviewed canonical update. Prefer a new
entry when the reader goal and failure modes are materially distinct; prefer a
cross-reference when the difference is only naming or channel convention.
