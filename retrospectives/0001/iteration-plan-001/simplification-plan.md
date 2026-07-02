# Simplification plan

## Simplification principle

Simplify only where the system keeps:

- review integrity;
- role separation;
- restartability;
- source discipline;
- governance clarity.

The aim is not less process everywhere. The aim is less process where it does not change the outcome.

## What can be shortened

## 1. Late-stage next action packets

Current risk:

Late-stage manifests can start resembling mini-status files.

Plan:

Keep only:

- files the next role truly needs;
- one next action;
- blockers;
- forbidden outputs.

Expected effect:

- less repeated reading;
- clearer routing.

## 2. Handoffs

Current risk:

Handoffs repeat full task state, KB lists and artifact inventories.

Plan:

Handoff contains only:

- reason for transfer;
- delta summary;
- artifacts created/updated;
- active constraints for next role;
- blockers/open questions;
- next action;
- escalation conditions.

Expected effect:

- less context bloat;
- better handoff semantics.

## 3. Review outputs for compact tasks

Current risk:

`review.md`, `qa-checklist.md`, `review-summary.md`, `reviewer-notes.md` may overlap.

Plan:

Compact tasks use `review.md` only, unless separate checklist or summary has a downstream consumer.

Expected effect:

- fewer review artifacts;
- clearer verdict.

## 4. Finalization outputs for compact tasks

Current risk:

Separate finalization notes/checklist may be excessive.

Plan:

For compact tasks:

- final artifact;
- `final_decision.md`;
- optional short finalization note only if meaning changed or residual risk exists.

Expected effect:

- less post-review paperwork.

## What can be combined

## 1. Review summary into review

If next action is clear inside `review.md`, omit `review-summary.md`.

Do not combine when:

- high-governance;
- complex changes_requested;
- next role needs separate transfer summary.

## 2. QA checklist into review

Compact review may embed checklist as a short section.

Do not combine when:

- standard/high-governance review requires detailed checks;
- factual traceability is complex;
- human approval depends on checklist evidence.

## 3. Finalization checklist into final decision

For low-risk tasks, Chief Editor final decision may include compact finalization validation.

Do not combine when:

- finalization materially changed the reviewed text;
- finalization has residual risks;
- human approval requires detailed proof.

## What can be removed from active use

## 1. Ambiguous legacy handoff naming

Do not imitate filenames with multiple possible receivers:

- `to-next-role`;
- `to-user-or-writer`;
- `to-chief-editor-or-final-editor`.

Route ambiguity belongs inside the handoff body.

## 2. Placeholder/scaffold knowledge files in retrieval path

If a file contains only headings or incomplete doctrine, do not treat it as active source of truth.

Options:

- mark as placeholder;
- convert into short index;
- remove from default retrieval.

## 3. Repeated global rules in local artifacts

Local artifacts should not reprint:

- full AGENTS rules;
- full status transition model;
- full pipeline doctrine;
- full KB list.

They should cite the relevant file and record task-specific implications.

## What to stop duplicating

Stop duplicating:

- risk mode definitions in every file;
- review-gate explanation in every pipeline section;
- artifact minimalism language in every template;
- role separation paragraphs inside every artifact;
- full source constraints across manifest, status, handoff and review.

Keep the rule in canonical owner and mention only local consequence.

## What not to simplify

Do not simplify away:

- `brief.md` for active tasks;
- independent review;
- high-governance research requirements;
- source traceability when claims matter;
- human approval state;
- final governance decision;
- blocker escalation.

## Simplification guardrail

Before omitting an artifact, record one line:

```text
Omitted because: [risk mode / no downstream consumer / no factual claims / equivalent info in X].
```

This prevents compact path from becoming invisible process loss.

## Expected result

After simplification:

- simple tasks have fewer files;
- handoff is shorter;
- review output is clearer;
- status does not balloon;
- manifest stays useful;
- high-risk tasks still get full depth.
