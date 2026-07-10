# Facts

| ID | Finding | Evidence | Confidence | S5.R3 implication |
| --- | --- | --- | --- | --- |
| F01 | Repository canon already defines `/about` as a derived 20-file memory package and makes repository sources authoritative. | R01, R04-R05, R11-R12 | verified | Extend current owners; do not create a memory system. |
| F02 | Knowledge Evolution already owns memory disposition, stale/correction/retirement, while Chief Editor classifies and Review Agent challenges. | R01, R05, R07-R10 | verified | No new capability, owner, role, pipeline, or gate is needed. |
| F03 | The checker validates package count and exact-copy byte identity but not summary meaning. | R11 | verified | Exact copies use deterministic comparison; summaries require human semantic review. |
| F04 | Current state surfaces contradict accepted S5.R2 evidence and active S5.R3 backlog state. | R02-R04, R14, user mission | verified | Normalize state and replace temporary/old release memory during S5.R3. |
| F05 | NIST emphasizes documentation, periodic review, clear roles, knowledge limits, human oversight, and provenance/limitation tracking. | E01-E02 | verified | Memory decisions need source, limits, owner, validation, and review. |
| F06 | W3C PROV distinguishes primary sources, derivation, revision, attribution, and invalidation. | E03 | verified | A memory fact must be traceable as exact copy or derived summary. |
| F07 | RFC 9111 treats stale derived state as requiring validation against the origin and uses invalidation after source-changing actions. | E04 | verified within cache scope | Canonical change or memory signal should trigger materiality/revalidation, not automatic reuse. |
| F08 | OpenGitOps preserves desired state in a declarative, versioned source and reconciles derived/runtime state to it. | E05 | verified | Repository canon is desired state; adopt provenance/reconciliation, reject automatic pull/write. |
| F09 | KCS treats knowledge as maintained through use and provides explicit archive/consolidation behavior for obsolete and duplicate articles. | E06-E08 | supported | Correct/consolidate/retire memory without parallel answers or silent context loss. |
| F10 | Records guidance bases retention/disposal on continuing value and documented rationale. | E09-E10 | verified | Keep externally useful context; retire content without continuing memory value and record why when material. |
| F11 | Data minimization, accuracy, storage limitation, and accountability require limiting personal data to purpose and correcting/removing inaccurate data. | E11 | verified | Sensitive/task-local content is omitted unless explicitly authorized and necessary. |
| F12 | Long-context research shows cost/performance pressure and value in high-density compressed representations. | E12-E13 | supported | Prefer compact summaries for large canon while preserving decisions, boundaries, caveats, source pointers, and current state. |
| F13 | Review systems preserve accountable approval/request-changes decisions. | E01, E14, R01 | verified | Memory update remains manual after independent review; advisory automation may only report. |
| F14 | Exact-copy files and compact summaries have different failure modes. | R11-R12, F06, F12 | verified/synthesis | Exact copies fail on byte drift; summaries fail on semantic omission, contradiction, staleness, and bloat. |
| F15 | Mandatory sync after every commit would propagate internal, temporary, sensitive, and low-value detail. | user mission, R05-R06, F10-F12 | supported synthesis | Use materiality and explicit `no-sync`/`omit` decisions. |
| F16 | Evaluation Signals may surface likely drift or maintenance burden but cannot modify memory. | R05, R14 | verified | Evaluation Signals are an intake signal only; Memory Hygiene owns disposition, not decision automation. |

## Research limitations

- Cache and GitOps are analogies for origin/derived consistency, not authority
  for automatic project-memory behavior.
- Compression papers demonstrate token/context benefits, not that a particular
  human-authored summary preserves project meaning.
- Records/privacy sources have legal scopes broader than this local project;
  this release adopts only conservative purpose, minimization, accuracy,
  retention, and rationale principles.
