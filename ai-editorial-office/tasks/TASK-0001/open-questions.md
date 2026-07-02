# Open Questions

Task ID: `TASK-0001`

Owner: `research_agent`

| Question | Why it matters | Blocks writing | Suggested resolution | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| Are internal AI/editorial policies, examples, or product-team practices available? | Internal context would make the article more specific and reduce generic examples. | `no` | Proceed with generic examples unless Chief Editor asks user for internal material before writing. | `chief_editor` or user | `open` |
| Should workflow examples be organization-specific or generic? | Specific examples require source material; generic examples can still support the requested draft. | `no` | Use generic examples and clearly avoid claims that they describe this organization. | `chief_editor`, then `writer_agent` | `deferred: generic examples acceptable unless changed by Chief Editor` |
| Is human approval required before internal publication or delivery? | Approval may affect final governance, not research. | `no` | Reassess after review and before finalization/governance. | `chief_editor` | `open for later stage` |
| Should the draft include numeric productivity claims? | Numeric claims would need stronger, audience-specific evidence. | `yes, if numeric claims are desired` | Do not include numeric productivity claims unless Chief Editor assigns additional research. | `chief_editor` | `resolved for current path: avoid numeric claims` |

## research assumptions

| Assumption | Reason | Risk | Needs verification |
| --- | --- | --- | --- |
| The article may use generic examples about editorial workflows. | No internal examples were supplied; Chief Editor deferred generic examples. | Medium. | `yes`, only if internal specificity becomes required. |
| The draft should discuss AI tools generally, not compare vendors. | Brief asks for practical internal article, not a product comparison. | Low. | `no` |
| Writer Agent can proceed after Chief Editor routing if it uses only safe and caveated claims from `claims_table.md`. | Research artifacts now classify usable and unsafe claims. | Low. | `no` |
