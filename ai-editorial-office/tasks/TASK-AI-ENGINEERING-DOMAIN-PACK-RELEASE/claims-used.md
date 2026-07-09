# Claims Used

This artifact maps material published claims to the research evidence packet.
Section names refer to `../../kb/ai_engineering_domain_pack.md` unless noted.

| Published claim / section | Claim IDs | Evidence basis | Treatment |
| --- | --- | --- | --- |
| Pack is bounded context, not architecture or approval authority | C01-C02, C27-C32 | R01-R06, F01-F04 | Repository-canonical, stated directly |
| Whole-system boundary and behavior/impact first | C03-C04 | F05, F20, F24-F26, F38 | Cross-source durable synthesis |
| Task-shaped model/provider fit | C05 | F37-F38 | Cross-source; no ranking/vendor verdict |
| Prompt authority, versioning, tests, rollback | C06-C07 | F10-F12, F22 | Durable principle; product mechanics excluded |
| Structured-output semantic limit | C08 | F13-F14 | Scoped to interface principle |
| RAG pipeline, permissions, separate/component evaluation | C09-C10, C24 | F15-F19, F42 | Cross-source; metric choice remains contextual |
| Data provenance, quality, rights, sensitivity, freshness | C11, C23 | F19-F23, F40-F41 | Rights/legal outcomes explicitly routed |
| Evaluation design and continuous evidence | C12-C14 | F05-F08, F23, F27, F38 | No universal metric or scorecard |
| Reliability signals, response paths, and fallback | C15, C26 | F23, F39, F43 | Context questions only; no operations workflow |
| Meaningful human oversight | C16, C22 | F24-F25, F36 | Proportional design principle, no new gate |
| Defensive AI safety and layered controls | C17, C19, C23 | F29-F32, F40-F41 | Category-level only; taxonomies not verdicts |
| Tools/agentic failure surfaces | C18-C19 | F09, F31, F35 | Behavior-based; no fixed agent taxonomy |
| AI-assisted engineering verification | C20-C22 | F33-F36 | GitHub guidance plus repository Engineering Review boundary |
| Product details require task-time refresh | C25 | F41, F44 | Explicit stale-if treatment |
| Adjacent-owner relations | C27-C31 | R02-R06, F03-F04 | Repository-canonical routing |
| One-pack architecture decision | C32 | F45 and architecture synthesis | Release decision, independently reviewable |

## Excluded claims

The published packet does not claim:

- universal model/provider superiority;
- proof of safety, security, compliance, fairness, or production fitness;
- universal metrics or thresholds;
- semantic correctness from schema conformance;
- groundedness from citations alone;
- risk elimination from human review or a taxonomy;
- current product/account behavior beyond the dated source register;
- authority to approve, merge, deploy, procure, process data, or release.
