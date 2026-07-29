# Product Intent Review Adoption Guide

## what it is

Product Intent Review is an implemented and evaluated, conditionally activated
analytical lens. It checks whether a proposed product or intervention has
enough evidence-bounded value, fit, mechanism, and viability for the next
editorial or owner decision.

It is not a role, pipeline, lifecycle stage, gate, status, outcome, universal
brief, mandatory report, or product-owner replacement.

## when it activates

Intake Agent records observable signals and negative evidence. Task Need
Recognition may recommend `not_needed`, `limited`, or `full`. Chief Editor
alone makes the task-local mode decision.

- Use `not_needed` for ordinary editing, fixed/approved product logic, faithful
  conversion, or work where product analysis cannot change usefulness or the
  next decision.
- Use `limited` for one bounded product assumption that materially affects the
  artifact.
- Use `full` for a new/unapproved concept, multiple material unknowns, a
  consequential create/no-build choice, or a potentially wrong intervention
  class.

Keywords never activate the capability by themselves. Negative evidence can
keep a substantial-looking request on the compact path.

## who does what

| Owner | Responsibility |
| --- | --- |
| Intake Agent | Preserve signals, negative evidence, explicit decisions, and unknowns; do not activate or analyze. |
| Chief Editor | Decide mode/scope, assign an existing analytical owner, map the finding to production consequence, preserve owner authority. |
| Research Agent | Work with evidence and, only when explicitly assigned, form the bounded analytical finding and nearest validation. |
| Writer / UX Writer | Work inside approved boundaries; reroute new material gaps instead of polishing them away. |
| Review Agent | Independently challenge activation, judgment, validation, authority, output, and finding/verdict separation. |
| Final Editor | Preserve the approved finding and confidence; add no new analysis. |
| Product owner | Decide product direction, scope, investment, pilot, launch, intervention class, or stop. |

## what the task owner sees

For active work, the selected existing deliverable starts with:

1. direct product verdict;
2. one main product gap;
3. next owner decision or check;
4. compact evidence boundary;
5. editorial production consequence;
6. local editorial detail last.

Internal capability names, lifecycle mechanics, full model fields, and method
inventories stay hidden unless the user explicitly asks about the system.

## deliverables

Reuse:

- `report`;
- `decision memo`;
- `research report`;
- a compact embedded block.

A separate Product Intent Review report is allowed only when explicitly
selected or when independent transfer/traceability creates a real reader need.
Capability naming does not create a mandatory artifact or deliverable profile.

## minimum validation

Start with the one main gap. Either:

- define the nearest reversible check of one critical hypothesis;
- state why additional validation is `not_needed`;
- state why one bounded check is `insufficient`.

The product owner decides what to run. The capability does not authorize a
pilot, experiment, launch, or full research program.

## restart

For material `limited`/`full` work, restart from `task-manifest.md`,
`orchestration_plan.md`, the current analytical artifact, and latest handoff.
Persist only mode, bounded focus, evidence pointer, finding/consequence, and
reroute-critical state. Do not copy the full analysis into the manifest.

`not_needed` does not require heavy state or conditional owner loading.

## verification and maintenance

Run:

```bash
sh ai-editorial-office/tests/test_product_intent_evaluation.sh
```

Then run the neighboring routing, decision/review, output, validation, task-pack,
deliverable, lifecycle, task-state, and `/about` checks listed in
`tests/README.md`.

Change the capability only from a reproducible failing case or an explicitly
authorized contract change. Preserve expected semantic variability, document
defects and repair loops, patch the canonical owner minimally, and obtain
independent review.

## canonical references

- semantics and limits: `/kb/product_intent_review.md`;
- discoverability and role mapping: `/kb/capability_registry.md`;
- advisory routing signals: `/kb/task_need_recognition.md`;
- current initiative state: `project-state.md`;
- evaluation/contributor detail: `tests/README.md` and repository
  `CONTRIBUTING.md`.
