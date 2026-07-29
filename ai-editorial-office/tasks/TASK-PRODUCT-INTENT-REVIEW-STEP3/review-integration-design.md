# Review Integration Design

## One existing gate

Product Intent Review is a conditional dimension inside the existing Review
Pipeline and Editorial Challenge Lens. It introduces no Product Reviewer,
pipeline, lifecycle stage, gate, status, or outcome.

## Trace contract

When mode is `limited` or `full`, `review.md` must allow a reviewer to trace:

- mode and scope;
- product finding;
- evidence boundary;
- one main product gap;
- production consequence;
- independent challenge;
- operational verdict;
- owner decision boundary.

The review checks rather than repeats the full analysis.

## Independent checks

Activation checks challenge multi-signal basis, negative evidence, keyword-only
activation, missed material activation, and proportional depth.

For `limited`, review checks assigned focus, bounded scope, evidence support,
and visible unknowns. For `full`, it checks the available seven-element model,
all four checks, evidence separation, one main gap, bounded alternatives,
minimum validation, and product-owner boundary.

Result checks challenge whether the finding follows from evidence, consequence
follows from the finding, the compact frame preserves the analysis, production
did not hide the gap, uncertainty remains visible, the next decision is clear,
and the product owner retains authority.

## Operational outcome separation

Only `approved`, `changes_requested`, and `blocked` are valid operational
outcomes. A well-supported no-build recommendation is an acceptable product
finding and can receive `approved`. A plausible finding with repairable
evidence, prioritization, consequence, validation, or uncertainty defects gets
`changes_requested`. Fabricated need/effect, owner substitution, hidden
critical gap, or independence failure may get `blocked`.

## Challenge questions

The existing Editorial Challenge Lens asks what supports or could disconfirm
the finding; whether problem and solution, exposure and effect, or familiar
format and justified fit were conflated; whether a smaller intervention exists;
whether polish substituted for product evidence; and whether the editorial
system made the owner's decision.

## Scenario test model

Executable fixtures use a small review-record vocabulary for the ten authorized
cases. The checker validates relationships rather than inventing a product
verdict enum: mode/scope, required analysis evidence, production-boundary
violations, validation quality, authority boundary, reroute, and the existing
operational outcome.
