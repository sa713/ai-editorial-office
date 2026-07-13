# Deliverable Knowledge And Multi-Deliverable Planning Smoke Test

Status: manual synthetic regression. These cases are not task materials, an
automatic classifier, a bundle generator, a closed taxonomy, or a new gate.

## Contract Under Test

The test passes only when the decision:

1. retrieves relevant deliverable knowledge rather than treating a name as a
   template or pipeline;
2. checks whether one artifact satisfies all material user outcomes;
3. selects a single deliverable when one is sufficient;
4. selects the minimum sufficient ordered set when distinct outcomes remain;
5. records purpose, dependency, and production priority for every member;
6. preserves explicit user scope and does not produce companions automatically;
7. uses existing production roles and primary pipelines or bounded
   mini-contracts;
8. lets Review remove redundant members and identify necessary missing ones.

## Case 1: Longread Only Remains Single

### Synthetic request

> Write a self-contained longread explaining why our operating model changed.
> I do not need a summary, checklist, or follow-up materials.

### Expected selected deliverable set

1. Longread — primary explanatory artifact; independent; priority 1.

### Expected result

Pass. One artifact satisfies the stated understanding outcome and the user
explicitly excludes companions. A cheat sheet or FAQ may not be added merely
because the catalogue lists them as typical.

## Case 2: AI Education Needs Three Distinct Jobs

### Synthetic request

> I am an experienced AI user who needs to rebuild my mental model, remember the
> new working practices, and know what to study next. Choose the format.

### Expected selected deliverable set

1. Longread — primary mental-model update; independent; priority 1.
2. Cheat Sheet — fast recall of the new practices; depends on Longread;
   priority 2.
3. Roadmap — future learning sequence; independent from final prose but uses the
   same scope/evidence; priority 3.

### Expected result

Pass. One longread cannot serve deep learning, at-use recall, and future study
sequence equally well. Every companion has a distinct outcome and the set is
minimal.

## Case 3: Presentation Needs Speaker Notes

### Synthetic request

> Prepare material I can present to the steering committee in fifteen minutes.
> I need to deliver it myself and preserve the evidence caveats while speaking.

### Expected selected deliverable set

1. Presentation — audience-facing visual narrative; independent; priority 1.
2. Speaker Notes — delivery cues, caveats, timing, and transitions; depends on
   Presentation; priority 2.

### Expected result

Pass. Notes cover a distinct presenter outcome and prevent the deck from being
overloaded. They are not generated automatically when the request is deck-only.

## Case 4: Interview Publication Needs Announcement

### Synthetic request

> Publish this approved conversation as an interview. Make sure our Telegram
> audience can discover it, but choose the minimum sufficient artifact set.

### Expected selected deliverable set

1. Interview — primary attributed publication; independent; priority 1.
2. Announcement — distribution and action cue; depends on reviewed Interview;
   priority 2.

### Expected result

Pass. The Interview format is explicit, while the distribution artifact format
is delegated. Catalogue companion knowledge supports recommending Announcement;
Chief Editor must still select the set before production. Existing Writer
responsibilities and a bounded social mini-contract are sufficient.

## Case 5: Short Answer Stays Single

### Synthetic request

> In two sentences, tell me whether this setting affects existing projects.

### Expected selected deliverable set

1. Short answer — direct bounded response; independent; priority 1.

### Expected result

Pass. No report, FAQ, checklist, or reference is justified. Multi-deliverable
planning must not make trivial work heavier.

## Case 6: Explicit Deck-Only Scope Blocks Automatic Companion

### Synthetic request

> Create only the presentation. Do not create speaker notes or a memo.

### Expected selected deliverable set

1. Presentation — explicit sole deliverable; independent; priority 1.

### Expected result

Pass only when Speaker Notes remain an unselected catalogue possibility. A
typical companion relationship is not user consent or production authority.

## Case 7: Research Needs Executive Compression

### Synthetic request

> Research the alternatives in depth, preserve the source and uncertainty trail,
> and give our leadership a short decision-oriented entry point.

### Expected selected deliverable set

1. Research Report — evidence, method, findings, and limits; independent;
   priority 1.
2. Executive Brief — decision-relevant compression; depends on Research Report;
   priority 2.

### Expected result

Pass. The brief is not a duplicate: it serves a distinct senior-reader use case
and inherits rather than replaces the evidence base.

## Case 8: BRD Companion Is Conditional On Execution Outcome

### Synthetic request A

> Create a BRD for stakeholder approval. Implementation planning is a later task.

### Expected decision A

Single BRD.

### Synthetic request B

> Create the BRD and the executable plan the delivery team will use immediately
> after approval.

### Expected decision B

1. BRD — business alignment and approval; independent; priority 1.
2. Implementation Plan — delivery sequence; depends on approved BRD; priority 2.

### Expected result

Pass. The same catalogue relationship produces one or two artifacts depending
on the actual outcome and explicit scope, not on a default bundle.

## Regression Verdict

The capability passes only if all eight cases preserve minimum sufficient scope,
explicit intent, member purpose/dependency/priority, existing role and pipeline
boundaries, independent review, and non-automatic production.
