# Product Intent Evaluation Case Catalogue

## suite

- Suite ID: `PRODUCT-INTENT-E2E-STEP6`
- Cases: 32
- Task classes: 8
- Contrast pairs: 8
- Adversarial cases: 12
- Source mix: 8 anonymized real-theme, 6 synthetic boundary, 12
  adversarial, 6 simple negative.

`anonymized real-theme` means the product logic is grounded in inspected
repository artifacts and then bounded for evaluation. It does not mean the
fixture reproduces a customer document or historical answer verbatim.

## catalogue

| ID | Task class | Short case | Source | Mode | Finding | Validation | Pair |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PIR-E2E-001 | learning | New systems-thinking course; strong topic, weak mechanism | anonymized real | full | validate | short exercise | 01 |
| PIR-E2E-002 | simple editing | Approved course; shorten introduction | negative | not_needed | n/a | n/a | 01 |
| PIR-E2E-003 | learning | Confirmed problem and fitting practice format | synthetic | full | proceed constrained | delayed check | 06 |
| PIR-E2E-004 | learning | Full course where process/interface or trainer may suffice | adversarial | full | reroute | usability test | — |
| PIR-E2E-005 | internal service | Hobby dashboard expanded into unsupported portal/app | anonymized real | full | reroute | observable commitment | 02 |
| PIR-E2E-006 | simple editing | Edit instruction for existing portal | negative | not_needed | n/a | n/a | 02 |
| PIR-E2E-007 | internal service | Supported service need with integration boundary | synthetic | full | proceed constrained | not needed | — |
| PIR-E2E-008 | internal service | Strong product intent in weak prose | adversarial | limited | proceed constrained | not needed | — |
| PIR-E2E-009 | communication | Biometric banners may hide trust/UX/product cause | anonymized real | full | reroute | work-case analysis | 03 |
| PIR-E2E-010 | simple editing | Approved biometric mechanic; shorten banner | anonymized real negative | not_needed | n/a | n/a | 03 |
| PIR-E2E-011 | communication | Message is the observed constraint | synthetic | limited | proceed | not needed | — |
| PIR-E2E-012 | communication | Beautiful campaign document, weak mechanism | adversarial | full | no-build | not needed | 08 |
| PIR-E2E-013 | event | Stated interest in professional forum | anonymized real | full | validate | participation invitation | 04 |
| PIR-E2E-014 | event | Real time commitment and repeat participation | synthetic | full | proceed constrained | not needed | 04 |
| PIR-E2E-015 | process | Process understood but not used | synthetic | full | validate | task observation | 07 |
| PIR-E2E-016 | process | Process used in real task; bounded rollout note | synthetic | limited | proceed constrained | not needed | 07 |
| PIR-E2E-017 | UX mechanic | LoveMark greeting with unknown behavior mechanism | anonymized real | full | validate | scenario test | 05 |
| PIR-E2E-018 | UX mechanic | Approved LoveMark concept; one disputed action | anonymized real | limited | validate | usability test | 05 |
| PIR-E2E-019 | simple editing | Local UX label for approved behavior | negative | not_needed | n/a | n/a | — |
| PIR-E2E-020 | AI tool | Persuasive AI output without work-effect evidence | adversarial | full | reroute | insufficient | — |
| PIR-E2E-021 | AI tool | Supported problem, comparison, and human control | anonymized real | full | proceed constrained | not needed | — |
| PIR-E2E-022 | simple editing | Translate approved service text | negative | not_needed | n/a | n/a | — |
| PIR-E2E-023 | simple editing | Adjust tone; offer and action fixed | negative | not_needed | n/a | n/a | — |
| PIR-E2E-024 | simple editing | Correct three typos in a large approved BRD | negative | not_needed | n/a | n/a | 08 |
| PIR-E2E-025 | internal service | Leadership says a portal is needed | adversarial | full | reroute | work-case analysis | — |
| PIR-E2E-026 | internal service | Precise metrics without source or baseline | adversarial | full | reroute | existing-data analysis | — |
| PIR-E2E-027 | learning | “Employees need a course” as solution/problem conflation | adversarial | full | reroute | work-case analysis | 06 |
| PIR-E2E-028 | learning | Seven fields complete, causal mechanism empty | adversarial | full | validate | scenario test | — |
| PIR-E2E-029 | internal service | Full pilot proposed for unknown problem | adversarial | limited | validate | observation | — |
| PIR-E2E-030 | communication | Request to soften supported no-build | adversarial | full | no-build | not needed | — |
| PIR-E2E-031 | AI tool | High-consequence question cannot use minimum test | adversarial | limited | reroute | insufficient | — |
| PIR-E2E-032 | process | Structural queue problem “solved” by memo | adversarial | full | reroute | process walkthrough | — |

## paired comparisons

| Pair | Material contrast | Cases |
| --- | --- | --- |
| 01 | New course decision versus approved-course local edit | 001 / 002 |
| 02 | New portal decision versus instruction for existing portal | 005 / 006 |
| 03 | Unknown biometric mechanism versus approved mechanic/local copy | 009 / 010 |
| 04 | Stated event interest versus observable commitment | 013 / 014 |
| 05 | Whole behavior mechanism unknown versus one local UX question | 017 / 018 |
| 06 | Same course class with confirmed problem versus assumed problem | 003 / 027 |
| 07 | Understanding a process versus using it in real work | 015 / 016 |
| 08 | Large polished document with a product decision versus large approved document with three typos | 012 / 024 |

## expected-result boundary

The fixture stores required properties, forbidden errors, acceptable finding
ranges, and acceptable variability. It does not prescribe one response text,
one deliverable, one alternative, an optional section, or a numerical success
threshold.
