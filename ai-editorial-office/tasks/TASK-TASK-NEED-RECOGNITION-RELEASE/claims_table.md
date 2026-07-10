# Claims Table

| ID | Claim | Status | Evidence | Confidence | Sensitivity | Use downstream | Reviewer note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | Task Need Recognition can be implemented as advisory decision support before Chief Editor routing. | confirmed | F08, F14, F16-F18 | supported | high | yes | verify no decision verbs or hidden activation |
| C02 | Intake Agent should produce request-level recognition signals and recommendations. | confirmed | F01-F08, F17 | verified | high | yes | Intake must not confirm route, depth, capability, or pack activation |
| C03 | Chief Editor should challenge the view and make all routing decisions. | confirmed | F14-F18 | verified | high | yes | preserve existing authority and preflight |
| C04 | Recognition must be multi-signal and may be multi-label. | confirmed | F01-F07, F11, F21 | supported | medium | yes | avoid fixed exhaustive taxonomy claim |
| C05 | Recognition must allow ambiguity, contradiction, uncertainty, and unsupported/out-of-scope results. | confirmed | F02, F11, F13-F15 | supported | high | yes | no forced classification |
| C06 | Keyword presence alone cannot justify capability or Domain Pack recommendations. | confirmed | F01, F03-F05, F21 | verified for repository rule | high | yes | test simple keyword-rich case |
| C07 | Research depth should be recommended from novelty, evidence gaps, consequence, volatility, and decision need. | confirmed | F02, F04-F05, F09-F10, R03 | supported | high | yes | Chief Editor retains depth decision |
| C08 | Review depth should be recommended from risk, consequence, change surface, ambiguity, evidence, architecture, and domain sensitivity. | confirmed | F03, F09-F10, F22 | supported | high | yes | never add a new gate or automatic level |
| C09 | Architectural significance should reuse Architecture Review drivers and scenarios. | confirmed | F03, F22 | verified | high | yes | recognition only identifies likely materiality |
| C10 | Engineering significance should reuse Engineering Review changed-surface triggers. | confirmed | F06, F22 | verified | high | yes | markdown-only changes stay simple unless implementation contract changes |
| C11 | Communication significance should reuse Professional Communication materiality. | confirmed | F01, R03 | verified | medium | yes | distinguish communication job from ordinary copyediting |
| C12 | Likely Domain Packs should be recommended only when domain context could materially change work; one primary pack and adjacent packs may be named. | confirmed | F21, R04 | verified | high | yes | activation remains Chief Editor decision |
| C13 | Decomposition should be advised when deliverables, owners, evidence, risks, or validation paths diverge. | confirmed | F04, F23, R02 | supported | medium | yes | recommendation only; coherent bundles may stay one task |
| C14 | Existing task artifacts can carry recognition; no standalone artifact or new required task-object field is needed. | confirmed | F23 | verified | high | yes | template section must be explicitly conditional |
| C15 | A new bounded capability owner file is justified because current owners define decisions and component capabilities but not the shared request-to-need signal contract. | likely | F16-F24 | supported | high | with caveat | architecture synthesis must prove owner boundaries and minimum surface |
| C16 | Numeric scores, thresholds, and automatic routing should be rejected. | confirmed | F11-F15, user mission | verified | high | yes | scan canon/test for forbidden language |
| C17 | Representative synthetic cases can validate contract behavior but cannot prove real-world routing improvement. | confirmed | R05, evidence framework | verified | medium | yes | release signals must preserve limitation |

## Claim use rules

- `confirmed` claims may be used within the stated scope and confidence.
- C15 requires explicit architecture rationale because creating a canonical
  owner is a repository synthesis decision, not an external fact.
- No claim supports autonomous routing, auto-activation, a score, or a promise
  of real-world improvement.
