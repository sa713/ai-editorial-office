# Reader-Centered Quality Pilot

Status: `synthetic calibration complete; external comparative promotion check pending`

Date: 2026-07-13

## Purpose And Limits

This manual trial calibrates the proposed reader-outcome controls across three
different artifact types before they become routine. It does not claim that the
initiative has passed its promotion gate. A strong single-model comparator was
available only as a prior human comparison for the longread, not as a saved
artifact in this repository. No equivalent comparator outputs exist here for
the working document or short text. Project Lead must therefore run or accept a
label-neutral comparative review before claiming parity on every material
criterion.

The trial uses no numeric score. Each case records observable evidence,
regressions to block, the smallest useful Reader Review depth, and the remaining
human decision.

## Shared Comparison Conditions

- same raw request, brief, source boundary, freshness date, and output
  constraint for every pair;
- final user-facing output evaluated separately from governance artifacts;
- correctness, evidence support, neutrality, traceability, and independent
  review are non-relaxable;
- labels are hidden from the human evaluator where practical;
- model, mode, tools, source set, and date are recorded for every real rerun;
- a mixed or negative result remains a finding;
- Project Lead judgment is final; a producing model cannot approve its own
  comparative result.

## Evaluation Matrix

For each material criterion use `not worse`, `regressed`, `not applicable`, or
`not yet evidenced`, with exact output fragments or artifact pointers.

| Criterion | Evidence question |
| --- | --- |
| Correctness | Are material statements true within the allowed source boundary? |
| Evidence support | Are material claims supported at the required confidence? |
| Neutrality | Is the result free of unsupported vendor, product, or editorial bias? |
| Traceability | Can material claims and decisions be followed to evidence? |
| Reader fit | Does the result meet the recorded starting state and intended use? |
| Clarity | Can the reader reconstruct the main transfer without unnecessary work? |
| Concreteness | Are abstractions connected to supported examples, actions, or decisions? |
| Model change | Does the Cognitive Bridge move the reader from the old model to the new one? |
| Retention | Are 3-5 intended ideas expressed as memorable ideas rather than headings? |
| Practical action | Can the reader perform the Practical Transformation? |
| Naturalness | Does the material pass Companion Pass without precision loss? |
| Governance cost | Did the reader benefit justify any extra process or context? |

## Pilot 1 — Educational Longread

### Controlled Input

- Task source: `tasks/TASK-0001-AI-PRACTICE-CATCHUP/brief.md`.
- Available baseline: `tasks/TASK-0001-AI-PRACTICE-CATCHUP/final_editorial.md`.
- Reader starting state: experienced AI user whose working model stopped around
  prompt craft, early projects, and early skills.
- Required change: adopt a current, practical model for choosing and governing
  AI work.
- Source boundary: dated primary sources, no rumors, financial coverage, or
  OpenAI promotion.

### Baseline Evidence

The baseline preserves strong evidence discipline, neutrality, a dated source
boundary, a practical four-sprint plan, and an explicit shift from prompt craft
to a managed work system. It already contains a useful old/new transition in
`Главный сдвиг: управлять не разговором, а контуром работы` and practical paths
for research, writing, and applications.

The prior human comparison nevertheless found a reader-fit gap: the user's
named stopping point was treated mainly as an imprecise date marker. The text
did not provide a compact, concrete bridge titled or organized around “what
changed from the practice you remember”, and its high density of terms such as
Task Contract, provenance, deterministic checks, semantic validation, and
workflow decomposition could create academic distance.

### Revised Reader Contract To Test

- Cognitive Bridge: “golden prompt formula is still useful, but it now lives
  inside a larger contract/context/tools/verification system.”
- Moments of Insight:
  1. prompt quality is one controllable surface, not the whole system;
  2. context must be selected and governed, not merely enlarged;
  3. workflow is the default when the route is known; autonomy is earned;
  4. product surfaces are interfaces to practices, not the organizing theory;
  5. evals and human acceptance are part of execution, not postscript.
- Practical Transformation: tomorrow the reader rewrites one recurring task as
  a contract, separates stable knowledge from step context, chooses workflow or
  agent deliberately, and adds a verification loop.
- Bounded Utility Tradeoff: allow a short dated “then/current practice” bridge
  with provider-specific examples only when primary sources and availability
  notes support it; do not turn the material into a release catalog.
- Reader Review depth: `full`.

### Calibration Result

| Criterion | Result | Evidence or required proof |
| --- | --- | --- |
| Correctness, evidence, neutrality, traceability | not worse required | Existing evidence chain remains the preservation baseline. |
| Reader fit and model change | likely improved by contract; not yet evidenced in a rerun | Revised bridge directly uses the recorded starting point; final output is still required. |
| Clarity, concreteness, retention, action | not yet evidenced | Full rerun must show the bridge, five ideas, examples, and tomorrow-morning practice in final copy. |
| Naturalness | not yet evidenced | Companion Pass must cite exact dense or academic passages and preserve technical precision. |
| Governance cost | acceptable at full depth if output improves | Longread is source-heavy and explicitly educational. |

Human decision still required: label-neutral comparison of the revised final
output, saved baseline, and a current strong single-model comparator.

## Pilot 2 — Working Document

### Synthetic Controlled Input

Request: prepare a one-page decision memo for a project owner choosing whether
to automate a recurring source check now. Supplied evidence says the task occurs
weekly, takes two hours, has two known edge cases, and lacks a stable upstream
API. Do not invent cost, reliability, or security facts. The reader must choose
`pilot`, `defer`, or `reject` and assign the next action.

### Failure Baseline

A correct but weak memo can restate workflow options, risks, and automation
principles without placing the decision first. It may be factually safe yet
leave the owner to reconstruct the recommendation, evidence boundary, owner,
and next step.

### Revised Reader Contract To Test

- Starting state: owner knows the recurring pain but not whether evidence is
  sufficient for automation.
- Cognitive Bridge: move from “automation saves two hours” to “a bounded pilot
  is justified only if the unstable input and two edge cases are observable and
  reversible.”
- Moments of Insight: decision; evidence basis; key uncertainty; pilot boundary.
- Practical Transformation: choose one of three outcomes and assign a named
  validation action.
- Learning Design: decision-first rather than the five-part educational pattern.
- Reader Review depth: `normal`.

### Representative Acceptance Evidence

The improved memo must make these elements findable without inference:

1. recommendation: bounded pilot, defer, or reject;
2. why the available evidence supports only that strength of decision;
3. explicit unknowns about the upstream source;
4. two edge cases as validation slices;
5. owner, next action, stop condition, and reconsideration trigger.

### Calibration Result

| Criterion | Result | Evidence or required proof |
| --- | --- | --- |
| Correctness and evidence | not worse by design | No new facts are permitted; recommendation strength is bounded by supplied evidence. |
| Reader fit, clarity, practical action | improved in the acceptance contract | Decision and next action must be above background. |
| Model change and retention | material but lighter than longread | Four decision ideas are enough; full teaching sequence would add overhead. |
| Naturalness | Companion Pass required | Memo must be direct without fake informality. |
| Governance cost | normal depth justified | The artifact drives a decision; a full pedagogical review is unnecessary. |

Human decision still required: compare actual paired outputs against the five
representative acceptance elements and the shared matrix.

## Pilot 3 — Short User Text

### Synthetic Controlled Input

Request: reply in at most 80 words to an experienced colleague asking whether
an agent is always better than a fixed workflow. Use only this supplied fact:
an agent selects steps dynamically; a workflow follows a defined route. Give a
practical selection rule and no product claims.

### Failure Baselines

- Academic failure: defines orchestration, autonomy, and control planes but does
  not answer the selection question inside 80 words.
- Pleasant unsupported failure: claims agents are smarter, faster, or more
  modern without evidence.
- Governance failure: forces a five-part learning outline and a full six-row
  Reader Review onto a simple low-risk answer.

### Representative Passing Shape

The answer should state that neither is universally better, use a workflow when
the route is known and repeatable, use an agent when choosing the next step is
part of the task, and verify the result in either case. It must not add product
behavior, performance claims, or fake familiarity.

### Calibration Result

| Criterion | Result | Evidence or required proof |
| --- | --- | --- |
| Correctness and evidence | preserved | Every statement stays within the two supplied definitions or is a labeled selection rule. |
| Reader fit, clarity, concreteness, action | satisfiable with compact checks | Reader receives a direct rule inside the word limit. |
| Model change and retention | compact | One contrast and one action rule are sufficient. |
| Naturalness | compact Companion Pass | Direct professional language; no artificial pedagogical scaffolding. |
| Governance cost | must remain minimal | No new artifacts; three outcome questions inside normal review are enough. |

Human decision still required: compare actual paired outputs if promotion is
claimed. The synthetic case is sufficient only to calibrate `compact` depth and
anti-regression expectations.

## Cross-Pilot Findings

1. Reader Review depth should depend on intended outcome, reader risk, and
   explanation complexity, not artifact length alone.
2. `full` is justified for source-heavy teaching that must update a mental
   model; `normal` fits decision documents; `compact` fits short low-risk text.
3. Cognitive Bridge is not always chronology. It may be a contrast, decision
   rule, or old-assumption/new-boundary transition.
4. Companion Pass belongs before approval, but it cannot authorize unsupported
   warmth, simplification, or substantive finalization rewrite.
5. The longread supplies real baseline evidence; the other cases are synthetic
   calibration. None of the three proves comparator parity until actual outputs
   receive Project Lead review.

## Promotion Status

`not yet proven`

Reasons:

- no saved strong single-model comparator is available in this repository;
- two cases are calibration trials rather than completed production runs;
- the revised longread has not been generated and reviewed under the new
  contract;
- Project Lead has not issued a label-neutral comparative judgment.

This honest non-promotion is a passing governance result. It allows depth
calibration and regression tests to proceed while preventing synthetic evidence
from becoming a claim that the initiative already meets its Definition of Done.
