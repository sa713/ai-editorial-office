# Facts

## external evidence findings

| ID | Finding | Evidence | Confidence | Release implication |
| --- | --- | --- | --- | --- |
| F01 | AI/system effects are socio-technical: benefits and risks can emerge from technical behavior, people, organizational use, and context together. | E01, E07 | verified | Evaluate operational context and human effects, not mechanism internals alone. |
| F02 | Controlled or laboratory evidence can differ from operational evidence; validity beyond tested conditions must be explicit. | E01, E02, E04 | verified | Synthetic scenarios may prove documented behavior but not real-use benefit. |
| F03 | Intended benefits, monetary and non-monetary costs, scope, meaningful benchmarks, and human oversight should be documented before proceeding. | E01 | verified | Acceptance needs intended value, costs, comparison, and authority fields. |
| F04 | Performance or assurance evidence can be qualitative or quantitative, but should reflect deployment-like conditions, document methods, and expose generalization limits. | E01, E02, E07 | verified | Keep qualitative evidence valid; do not force a universal metric or score. |
| F05 | False-positive and false-negative rates are context-dependent evidence; representative conditions, human-AI teaming, and failure harm affect interpretation. | E03, E14 | verified | Acceptance must consider both over-triggering and missed-need risk without reducing them to one number. |
| F06 | Human oversight must be defined, assessed, and connected to real authority; override, appeal, recovery, and decommissioning are operational concerns. | E01, E02 | verified | An approval button or nominal reviewer is insufficient evidence of preserved judgment. |
| F07 | Systems or mechanisms that produce outcomes inconsistent with intended use need assigned responsibilities and a safe supersede, disengage, deactivate, or recovery path. | E01, E03 | verified | Reversibility, containment, retirement, and supersession belong in the contract. |
| F08 | Robust AI-intervention impact evaluation distinguishes capability/technical testing from the wider question of whether intended outcomes occurred and why. | E04 | verified | A functioning mechanism is not by itself proof that the system improved. |
| F09 | Baselines and comparison groups clarify what the intervention changed; business-as-usual must be described precisely when it is the comparator. | E04, E05, E06 | verified | Comparison is required when meaningful, but infeasible counterfactuals must be acknowledged rather than invented. |
| F10 | Early/formative evaluation should state what can and cannot be inferred before scale or long-term use, and repeated evaluation is needed as the intervention evolves. | E04 | verified | Strong synthetic or pilot evidence can justify narrower claims, observations, or deferral, not broad operational proof. |
| F11 | Impact evaluation must examine unintended outcomes and differences across tasks, contexts, or affected groups. | E04, E05, E06 | verified | Cross-effects and degradation of one area while another improves must be visible. |
| F12 | Assurance cases separate claims, the reasoning connecting them, and evidence; evidence is useful only insofar as it supports or rebuts a claim. | E08 | verified | The contract needs an explicit improvement claim, evidence link, counterevidence, gaps, and non-claims. |
| F13 | Assurance depth should be proportionate to criticality and may justify independent assessment when consequences are higher. | E07, E08 | verified | Keep the contract conditional and proportional; do not impose it on ordinary releases. |
| F14 | Verification establishes conformance to specified requirements, while validation establishes fitness for intended use in the intended environment. | E09 | verified | Repository checks prove implementation conformance, not practical value. |
| F15 | Engineering acceptance reviews inspect criteria, verification and validation results, expected operational performance, risks, open actions, deviations, and a human panel decision. | E10 | verified | Release acceptance needs a complete evidence packet and explicit unresolved evidence, not automated closure. |
| F16 | Architecture fitness involves competing quality attributes and tradeoffs; improving one attribute may degrade another. | E11 | verified | Architecture and maintenance value/cost cannot be represented by a single acceptance score. |
| F17 | Effective controls are designed, implemented, operated, and periodically reviewed against objectives; policy presence alone is not operating effectiveness. | E12 | verified | Automation/control proposals need operational proof appropriate to their authority and risk. |
| F18 | Organizational learning is not implemented merely because a lesson is documented; measurable, evaluated improvement in practice and retention over time are distinct claims. | E13 | verified | Canon addition or release completion is not proof of learned improvement. |
| F19 | Monitoring helps identify whether delivery is on track and whether desired impacts occur, while evaluation supports conclusions about success and future action. | E06, E13 | verified | Maintenance and post-implementation evidence can support later accept, narrow, or retire decisions. |
| F20 | Automation over-reliance can cause monitoring and decision failures; false alarms can produce disuse, and automating without designing the human role can degrade performance. | E14 | verified | Acceptance must test authority, workload, evidence access, override, and false-positive/negative consequences. |

## repository findings

| ID | Finding | Evidence | Confidence | Release implication |
| --- | --- | --- | --- | --- |
| F21 | Project Lead alone accepts releases; Codex produces Release Candidates. | R02, R08 | verified | S5.R5 can recommend a disposition but cannot record acceptance. |
| F22 | A completed Release Pack is already mandatory before Project Lead review and includes architecture, scope, validation, risks, signals, open questions, and a recommended decision. | R09 | verified | The Release Pack is the strongest existing owner candidate. |
| F23 | Evaluation Signals expose saved evidence, comparisons, contradictions, confidence, existing owner, and explicit non-decision, but never accept/reject or change owners automatically. | R06, R10 | verified | Reuse signals as evidence input; do not move acceptance into Evaluation Signals. |
| F24 | Knowledge Evolution owns feedback/outcome learning disposition, pattern confirmation, canon correction/retirement, and non-promotion. | R05, R07, R10, R11 | verified | Reuse its evidence and retirement state; do not make it release acceptance. |
| F25 | Task Need Recognition is a pre-routing advisory capability and cannot make route, activation, or governance decisions. | R08, R12 | verified | It is in scope as a release under assessment, not as the acceptance owner. |
| F26 | The Editorial Evidence Framework already owns evidence classes, confidence, assumptions, unknowns, validation, and residual risk. | R13 | verified | The contract should reference these concepts, not create a second evidence taxonomy. |
| F27 | Architecture Review already owns quality-attribute scenarios, tradeoffs, architectural risks, and rationale. | R14 | verified | The contract records architecture impact/cost evidence without duplicating the method. |
| F28 | The accepted AI Engineering pack already distinguishes task-shaped evaluation, baseline, regressions, human oversight, rollback/disablement, and residual risk. | R15 | verified | Reuse as domain context when material; do not promote it to a global acceptance owner. |
| F29 | Accepted S5 Release Packs consistently state that synthetic cases validate contracts but do not prove operational improvement. | R06, R07, R08 | verified | S5.R5 should make this recurring limitation an explicit acceptance rule. |
| F30 | Current `ROADMAP.md` and `project-state.md` lag the accepted S5.R4 Release Verdict and `BACKLOG.md`. | R02, R03, R04, R08 | verified | Normalize S5.R4 accepted and S5.R5 Review during RC state sync. |

## interpretations and gaps

- Interpretation: the missing element is not a new evaluation capability or
  approval process. It is a conditional, decision-ready claim/evidence/value/
  restraint record inside the existing Release Pack.
- Gap: no operational evidence yet shows that the S5.R5 contract improves
  future Project Lead decisions. This release can prove bounded design,
  scenario behavior, architecture fit, and validator conformance only.
- Gap: not every qualitative benefit has a valid counterfactual. The contract
  should require a meaningful comparison when available and an explicit reason
  when it is not.
- Gap: no evidence supports dashboards, acceptance scores, mandatory telemetry,
  or automatic disposition.
