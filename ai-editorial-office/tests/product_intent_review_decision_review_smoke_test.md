# Product Intent Review Decision/Review Smoke Test

Executable entry point:

```sh
sh ai-editorial-office/tests/test_product_intent_review_decision_review.sh
```

The fixture records are test-only contract examples. They do not define a
product finding enum, task status, pipeline, lifecycle stage, or additional
review outcome. The checker accepts only the existing operational outcomes:
`approved`, `changes_requested`, and `blocked`.

Covered cases:

1. a sound negative/no-build finding receives `approved`;
2. polished copy hiding an unsupported mechanism receives
   `changes_requested`;
3. `limited` overreach receives `changes_requested`;
4. an incomplete `full` model with hidden unknowns receives
   `changes_requested`;
5. product-owner substitution receives `blocked`;
6. weak minimum validation receives `changes_requested`;
7. correct bounded minimum validation receives `approved`;
8. fabricated need/effect receives `blocked`, distinct from no-build;
9. `not_needed` omits the review dimension and stays approved;
10. a new production-stage product gap reroutes to Chief Editor and prevents
    approval without Writer/UX Writer redesign.
