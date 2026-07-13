# Outcome-First Deliverable Selection Smoke Test

Status: manual synthetic regression test. These cases are not task materials,
real user evidence, an automatic classifier, or a new review gate.

## Contract Under Test

The test passes only when the record:

1. separates requested, recommended, and selected deliverables;
2. labels format authority as `explicit`, `delegated`, `inferred`, or `unknown`;
3. recommends the smallest artifact that is still sufficient for the actual
   outcome and use context;
4. preserves explicit user format intent unless the user agrees to change it;
5. explains alternatives or unresolved mismatches rather than silently
   overriding the request;
6. selects the pipeline, mode, or task-local mini-contract after and for the
   selected deliverable;
7. creates no Deliverable Agent, Format Agent, pipeline, lifecycle stage, gate,
   score, or mandatory standalone artifact.

## Case 1: Explicit Article Stays Article

### Synthetic request

> Write an article that helps experienced managers understand our new incident
> response policy.

### Expected decision

- Requested deliverable: article.
- Format authority: `explicit`.
- Recommended deliverable: article; an executive checklist may be suggested as
  an optional appendix, not a replacement.
- Decision: `respect_requested`.
- Selected deliverable: article.
- Pipeline consequence: Article Pipeline is selected after the deliverable.

### Expected result

Pass. The office may improve the article shape but may not silently turn it into
a checklist, memo, or slide deck.

## Case 2: Delegated Format Produces A Learning Roadmap

### Synthetic request

> I need to catch up on modern AI practice. Format and structure are up to you.

### Expected decision

- Requested deliverable: `not specified`.
- Format authority: `delegated`.
- Recommended deliverable: learning roadmap with reading order and practical
  checkpoints.
- Decision: `select_recommended`.
- Selected deliverable: learning roadmap.
- Pipeline consequence: use the existing Article Pipeline only if its
  knowledge-content contract fits; otherwise use a bounded task-local
  mini-contract with current Writer, Review, and governance owners. Do not add a
  roadmap pipeline.

### Expected result

Pass. Delegation authorizes format choice, and the recommendation is tied to
the learning outcome rather than to the first familiar document type.

## Case 3: Bare Explain Request Cannot Become A Checklist

### Synthetic request

> Explain how the new access model works.

### Invalid decision

- Recommended deliverable: checklist.
- Reason: shorter and easier to scan.

### Expected result

Fail. `Explain` requires a communication artifact capable of building the
model. A checklist may support later application, but brevity alone does not
make it sufficient. Recommend an explainer/tutorial or ask about the use case if
the required depth is materially ambiguous.

## Case 4: Presentable Outcome Selects Presentation

### Synthetic request

> I need something I can present to the steering committee in fifteen minutes.

### Expected decision

- Requested deliverable: `not specified`.
- Format authority: `inferred` from the explicit presentation use context.
- Recommended deliverable: presentation with a concise decision summary.
- Decision: `select_recommended` when no competing format changes the outcome;
  otherwise ask one bounded question.
- Selected deliverable: presentation.
- Pipeline consequence: select an existing compatible mode or bounded
  mini-contract after the presentation decision; do not create a presentation
  pipeline merely for this case.

### Expected result

Pass. The use situation supports the artifact shape.

## Case 5: Compare Outcome Selects Comparison Matrix

### Synthetic request

> Help me compare three onboarding platforms for a purchase decision.

### Expected decision

- Requested deliverable: `not specified`.
- Format authority: `delegated` or safely `inferred`, depending on surrounding
  context.
- Recommended deliverable: comparison matrix with criteria, evidence notes,
  tradeoffs, and a bounded recommendation if requested.
- Decision: `select_recommended`.
- Selected deliverable: comparison matrix.
- Pipeline consequence: research depth follows claim/evidence need; the writing
  or analytical mini-contract follows the selected matrix.

### Expected result

Pass. A matrix directly enables comparison and is more outcome-fit than an
unstructured essay without weakening evidence.

## Case 6: Management Persuasion Selects Decision Memo

### Synthetic request

> I need to convince management to fund the migration. Give me the strongest
> format.

### Expected decision

- Requested deliverable: `not specified`.
- Format authority: `delegated`.
- Recommended deliverable: decision memo with recommendation, evidence,
  alternatives, costs, risks, and explicit ask.
- Decision: `select_recommended`.
- Selected deliverable: decision memo.
- Pipeline consequence: Professional Communication and Professional Analysis
  may be activated; no new memo role or pipeline is created.

### Expected result

Pass. The deliverable supports a management decision rather than merely
describing the technical topic.

## Case 7: Requirements Need Selects BRD

### Synthetic request

> I need requirements that product, engineering, and procurement can approve.

### Expected decision

- Requested deliverable: requirements, format not fully specified.
- Format authority: `inferred`.
- Recommended deliverable: BRD or specification, with the choice tied to the
  approval and downstream-use context.
- Decision: `select_recommended` if the context clearly supports BRD;
  `ask_before_change` if BRD versus technical specification changes ownership
  or acceptance materially.
- Selected deliverable: recorded before the pipeline or mini-contract.

### Expected result

Pass only when the recommendation basis and ambiguity handling are visible.

## Case 8: Explicit Presentation Is Not Replaced By A Memo

### Synthetic request

> Create a presentation for the board. A memo might be easier for you, but I
> need slides for the meeting.

### Expected decision

- Requested deliverable: presentation.
- Format authority: `explicit`.
- Recommended deliverable: presentation; an executive memo may be an optional
  companion only if useful and in scope.
- Decision: `respect_requested`.
- Selected deliverable: presentation.

### Expected result

Pass. Production convenience cannot override explicit meeting needs.

## Case 9: Material Format Mismatch Routes Through Preflight

### Synthetic request

> Write a one-page memo that fully trains new operators to perform a complex
> recovery procedure without supervision.

### Expected decision

- Requested deliverable: one-page memo.
- Format authority: `explicit`.
- Recommended deliverable: tutorial/runbook or staged training package.
- Decision: `ask_before_change` or `constrain_with_explanation`.
- Selected deliverable: not changed silently; production does not start until
  preflight resolves the mismatch or records a safe bounded scope.

### Expected result

Pass. Respect for intent does not require pretending the requested artifact can
meet an impossible outcome.

## Case 10: Trivial Obvious Work Stays Compact

### Synthetic request

> Fix the typo in this email and return the corrected email.

### Expected decision

- Requested deliverable: corrected email.
- Format authority: `explicit`.
- Recommended deliverable: corrected email.
- Decision: `respect_requested`.
- Selected deliverable: corrected email.
- Pipeline consequence: compact existing route; no expanded recognition block
  or new artifact is required.

### Expected result

Pass. Outcome-first selection does not make obvious work heavier.

## Regression Verdict

The capability passes this smoke test only if Cases 1, 2, 4, 5, 6, 8, 9, and
10 produce the expected pass behavior, Case 3 is rejected, and Case 7 preserves
the stated conditional ambiguity handling. Synthetic success does not prove
real-world improvement; it demonstrates contract coverage and restraint.
