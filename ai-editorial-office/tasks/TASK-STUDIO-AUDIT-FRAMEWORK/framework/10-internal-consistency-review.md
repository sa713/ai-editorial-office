# Internal Consistency Review

This is an internal review of the Framework draft, not an audit of AI Software
Studio.

## Review Questions

| Question | Result |
| --- | --- |
| Does the Framework conduct a current audit? | No. It defines methodology only. |
| Does it evaluate current Studio implementation? | No current maturity scores or findings are included. |
| Does every area have KB basis? | Yes. Area mappings are listed in `02-audit-areas.md` and `07-kb-traceability.md`. |
| Does every criterion have KB basis or gap status? | Yes. Criterion basis appears in `03-assessment-criteria.md` and `../claims_table.md`. |
| Does the model avoid single-score reduction? | Yes. Area profile and caps are required; single average is disallowed. |
| Does the Framework distinguish KB gaps from Studio findings? | Yes. `08-kb-gaps.md` and report rules separate these categories. |
| Does it avoid BRD/process-change/Codex-task output? | Yes. These are prohibited in summary, report rules, and first-audit guidance. |

## Contradictions Checked

### Maturity Model vs Anti-Maturity-Ladder Warning

Potential contradiction: using maturity levels could encourage ladder chasing.

Resolution: `04-maturity-model.md` states that maturity is context-relative,
uses caps, requires narrative rationale, and forbids maximizing maturity as an
objective detached from need.

KB basis: `framework-platform-maturity`,
`anti-pattern-single-metric-productivity`.

### Human Checkpoints vs Bottleneck Risk

Potential contradiction: the Framework requires human checkpoints while KB says
too many checkpoints can bottleneck work.

Resolution: criteria require risk-based, evidence-based checkpoints and permit
lighter checks for low-risk well-evaluated automation.

KB basis: `pattern-human-ai-checkpoints`,
`anti-pattern-human-rubber-stamp-ai`.

### Knowledge Graph vs Simplicity

Potential contradiction: knowledge graph appears as a tool but agentic/tooling
overengineering is an anti-pattern.

Resolution: Framework does not require graph tooling; it asks whether simple
links/IDs/metadata are sufficient.

KB basis: `tool-knowledge-graph`, `anti-pattern-agentic-overengineering`.

### Platform Area vs Rejected Developer Portal

Potential contradiction: platform area could imply requiring a portal.

Resolution: Framework explicitly says portal is not required and is rejected
for current context unless reconsideration conditions appear.

KB basis: `tool-internal-developer-portal`,
`anti-pattern-portal-equals-platform`.

### Standards vs Local Context

Potential contradiction: NIST/ISO records could be read as mandatory compliance.

Resolution: Framework treats them as references for risk/control reasoning, not
as certification or full local control requirements.

KB basis: `standard-nist-ssdf`, `standard-nist-ai-rmf`,
`standard-iso-42001`.

## Residual Risks

- Criterion cards are intentionally compact; a future audit may need
  subcriteria for high-risk areas after KB expansion.
- AI-agent criteria depend on evolving records and should be refreshed before
  each audit cycle.
- Security and AI risk areas need local control mapping before detailed control
  scoring.
- First-audit calibration is necessary because no prior maturity baseline
  exists.

## Internal Review Outcome

The Framework draft is internally consistent enough for independent review,
provided `03-assessment-criteria.md` remains aligned with `../claims_table.md`
and the final review confirms no accidental current-state audit language.

