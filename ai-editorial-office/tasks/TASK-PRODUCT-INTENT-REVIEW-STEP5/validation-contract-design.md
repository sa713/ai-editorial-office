# Validation Contract Design

## design objective

Strengthen the existing minimum hypothesis validation into a reliable Minimum
Product Validation decision without creating a new stage, pipeline, role, or
required artifact.

Core question:

> What is the cheapest, fastest, and most reversible way to obtain the evidence
> needed for the next decision?

The check reduces one material uncertainty. It does not prove that the whole
product will succeed.

## decision sequence

1. Start from the one main product gap.
2. Decide whether more validation is needed for the next decision.
3. If needed, select one critical hypothesis or a tightly related minimum set.
4. State why the next costly or hard-to-reverse decision depends on it.
5. Classify the primary hypothesis.
6. Choose a method that can observe the uncertainty in its real context.
7. remove every feature, artifact, audience segment, and production-quality
   element not needed to test that hypothesis.
8. Define the observable signal.
9. Define evidence-grounded continue and reconsider conditions.
10. State what the check cannot prove.
11. Name the next decision and its owner.

## validation disposition

The analysis records one semantic disposition:

- `minimum_test`: one bounded check can materially reduce the uncertainty;
- `not_needed`: current evidence or decision economics make another check
  unnecessary;
- `insufficient`: one minimum check cannot responsibly answer the decision
  because risk, heterogeneity, dependencies, conflicts, duration, or
  observability require deeper evidence.

These are analytical dispositions, not lifecycle stages, task statuses, review
outcomes, or owner decisions.

## minimum-test record

When disposition is `minimum_test`, the selected analytical artifact contains:

- critical hypothesis;
- why it is critical for the next decision;
- primary hypothesis class;
- bounded audience/context;
- selected method;
- minimum intervention;
- observable signal and signal kind;
- continue condition;
- reconsider condition;
- inference limits;
- next product-owner decision.

The checker also verifies that the design:

- is linked to the main gap;
- keeps one critical assumption;
- costs less than full implementation;
- is stoppable and reversible;
- excludes non-hypothesis features;
- recommends only the nearest check;
- does not use automatic surveys, A/B tests, or pilots;
- does not claim general proof;
- does not invent a threshold without a recorded basis.

## not-needed record

When disposition is `not_needed`, the analysis states why another check cannot
materially improve the next decision. It must not create a validation record as
ritual service weight.

## insufficient record

When disposition is `insufficient`, the analysis states:

- why a minimum check cannot answer the material question;
- the deeper evidence or specialist route required;
- the next owner decision.

It does not silently create a research program or a new pipeline.

## signal and threshold rules

Prefer observed action, choice, task completion, decision quality, repeat use,
transfer, error reduction, refusal, obstacle, or process change. Stated liking,
interest, clarity, approval, or intent may be supporting evidence but cannot
alone prove demand, mechanism, behavior, transfer, or durable effect.

Qualitative conditions are valid when observable and decision-linked. A
numeric threshold is allowed only when its basis is recorded; the checker does
not impose a universal percentage, sample size, or significance claim.

## sequential checks

A complex product may eventually need several checks, but the result recommends
only the closest check needed for the next decision. A complete discovery or
research program requires separate user or owner authority.

## AI-specific boundary

For an AI intervention, method and signal must consider decision quality and
work effect, not merely persuasive output. The design makes material data
quality, model limits, variability, human control, confidentiality, and
permitted data use explicit. A successful demonstration does not prove a
stable operating effect.

## reader-facing compression

When validation is material, the selected existing deliverable may compress it
to:

- What to test — critical hypothesis.
- How to test — method, minimum intervention, and context.
- What to observe — real signal.
- How to decide — continue and reconsider conditions plus next decision.
- Limit — what the check does not prove.

Internal field names, role names, capability names, and pipeline mechanics do
not appear unless the user explicitly requests implementation detail.
