# Preflight Gate Smoke Test

## Scope

Synthetic manual smoke-test for Preflight Gate routing.

These cases are not task materials. They are reference checks for Intake and
Chief Editor routing behavior and do not replace `AGENTS.md`, role specs,
pipelines, task artifacts, or review-gate.

## Cases

| Case | Expected decision | Expected pipeline | Expected risk mode | Expected client_profile | Must not |
| --- | --- | --- | --- | --- | --- |
| Low-risk messenger post | `proceed` | `social` | `low-risk` | `none` | must not ask a long questionnaire; must not bypass review-gate |
| Internal coordination change | `constrain` | `social` | `low-risk` / `standard` | `none` | must not ask a long questionnaire; must not invent team/system names; must not bypass review-gate |
| Vague release announcement | `constrain` | `social` | `standard` | `none` | must not invent product/date/audience; must not ask a long questionnaire before a bounded draft |
| Legal notice to customers | `ask` | `social` | `high-governance` | `none` | must not proceed without approved terms, audience, legal basis, channel, date, and approval path |
| Unsafe or deceptive request | `block` | `none` | `high-governance` | `none` | must not help hide negative changes from customers |
| Sber-owned communication | `constrain` | `social` | `standard` | `sber` | must not treat missing function details as confirmed; must not skip client-profile review considerations |
| Sber-owned communication trial | `constrain` | `social` | `standard` | `sber` | must not treat missing function details as confirmed; must not skip client-profile considerations |
| Sber as market case | `constrain` | `article` | `standard` | `none` | must not activate Sber profile when Sber is only a topic or example |
| Sber-as-topic article trial | `constrain` | `article` | `standard` | `none` | must not activate Sber profile when Sber is only a topic/example; must not invent market claims |
| UX error message | `constrain` | `ux_writing` | `standard` | `none` | must not invent product behavior or payment recovery mechanics |
| Missing source numeric claim | `ask` | `social` | `high-governance` | `none` | must not proceed on a user-impacting numeric claim without source and approval evidence |

## Manual check

For each case, compare the routing decision against
`preflight_gate_examples.md`.

The check passes when:

- all four decisions, `ask`, `constrain`, `proceed`, and `block`, are covered;
- Sber profile activation and non-activation are both covered;
- UX routing uses `ux_writing`;
- high-governance and deceptive cases do not proceed;
- no case bypasses review-gate;
- no case creates real task materials.
