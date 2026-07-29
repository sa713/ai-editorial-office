# Evaluation Coverage Report

## coverage result

Runner result: `PASS`.

| Requirement | Actual | Minimum | Result |
| --- | ---: | ---: | --- |
| End-to-end cases | 32 | 30 | pass |
| Task classes | 8 | 8 | pass |
| Contrast pairs | 8 | 8 | pass |
| Adversarial cases | 12 | 10 | pass |
| `not_needed` | 7 | 5 | pass |
| `limited` | 6 | 5 | pass |
| `full` | 19 | 10 | pass |
| No-build or reroute | 11 | 5 | pass |
| Proceed / proceed constrained | 7 | 5 | pass |
| Minimum-validation methods | 11 | 5 | pass |
| Validation `not_needed` | 8 | 2 | pass |
| Validation `insufficient` | 2 | 2 | pass |
| Anonymized real-theme cases | 8 | 5 internal suite minimum | pass |
| Cases with manual judgment | 32 | 32 | pass |

## task-class distribution

| Class | Cases |
| --- | ---: |
| Learning activity | 5 |
| Internal service | 6 |
| Communication campaign | 4 |
| Event | 2 |
| Work process | 3 |
| UX mechanic | 2 |
| AI tool | 3 |
| Simple editing | 7 |

## source distribution

| Source kind | Cases |
| --- | ---: |
| Anonymized real-theme | 8 |
| Synthetic boundary | 6 |
| Adversarial | 12 |
| Simple negative | 6 |

## validation-method coverage

Eleven distinct methods appear:

- delayed check;
- existing-data analysis;
- observable commitment;
- observation;
- participation invitation;
- process walkthrough;
- scenario test;
- short exercise;
- task-based usability test;
- task observation;
- work-case analysis.

## mandatory metrics

| Metric | Result |
| --- | ---: |
| Routing accuracy | 32/32 = 100% |
| Over-activation | 0 |
| Missed activation | 0 |
| Mode mismatch | 0 |
| Critical contract violations | 0 |
| Main-gap failures | 0 |
| Unsupported product findings | 0 |
| Validation-method mismatch | 0 |
| Authority-boundary violations | 0 |
| Compact-path regressions | 0 |
| Cases requiring manual judgment | 32 |
| Manual judgment failures | 0 |
| Confirmed production defects | 0 |
| Repair loops | 0 |

## interpretation

The distribution exercises both caution and action. Eleven no-build/reroute
findings show the system can reject or redirect unsupported concepts; seven
proceed findings show it does not treat every unknown as a blocker. Seven
`not_needed` cases protect ordinary editing. Eight validation-not-needed cases
protect against ritual pilots, while two `insufficient` cases protect against
false confidence in a minimum check.

These counts are coverage evidence, not a universal product-quality score.
