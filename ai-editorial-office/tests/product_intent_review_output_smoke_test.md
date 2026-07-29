# Product Intent Review Output Smoke Test

Executable entry point:

```sh
sh ai-editorial-office/tests/test_product_intent_review_output.sh
```

The twelve test-only fixture records cover:

1. compact `limited` mechanism output;
2. decision-ready `full` learning-intervention output;
3. direct no-build language;
4. validate-before-production action boundaries;
5. embedded Product Intent Review inside a broader review;
6. decision-memo selection and tradeoffs;
7. research-report selection and evidence calibration;
8. silent `not_needed`;
9. large-source output overexpansion;
10. internal architecture leakage;
11. editorial polish masking the product gap;
12. uncertainty/disclaimer overload.

The checker validates reader-facing order, existing deliverable fit, semantic
presence, directness, uncertainty density, conditionality, and leakage. It does
not generate prose, activate Product Intent Review, create a profile, define a
product finding enum, or make a product decision.
