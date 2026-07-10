# Claims Table

| ID | Claim | Status | Evidence | Confidence | Sensitivity | Allowed downstream use | Reviewer note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | Memory Hygiene Intelligence should be a bounded refinement of existing Knowledge Evolution/Memory Curation/Integrity Checking, not a new capability or system. | confirmed synthesis | F01-F03 | verified | critical | yes | Validate exact owner fit. |
| C02 | Repository canon must win every canonical-memory contradiction. | confirmed | R01, R04-R05, R12 | verified | critical | yes | No memory override. |
| C03 | Exact copies require source identity; compact summaries require provenance and semantic validation. | confirmed synthesis | F03, F06, F12, F14 | supported | high | yes | Different validation branches. |
| C04 | A canonical change is a sync signal, not an automatic sync command. | confirmed synthesis | F07-F08, F15 | supported | high | yes | Apply materiality and evidence. |
| C05 | Internal research, task-local evidence, temporary detail, and sensitive content should normally be omitted. | confirmed | F10-F12, F15 | supported | high | yes | Exceptions need purpose and authorization. |
| C06 | Explicit no-sync is correct when no externally useful fact changes and should be recorded when material. | confirmed synthesis | F10, F15 | supported | high | yes | No per-commit record requirement. |
| C07 | Stale/contradictory memory should be corrected from canon, with ambiguity deferred or blocked rather than guessed. | confirmed | F05-F07 | verified | critical | yes | Preserve source pointer and review. |
| C08 | Duplicate memory facts should be consolidated at one useful summary location without losing unique meaning or provenance. | confirmed synthesis | F09-F10 | supported | high | yes | Avoid silent deletion. |
| C09 | Obsolete external memory should be retired or replaced when it has no continuing use; meaningful history stays in repository artifacts. | confirmed synthesis | F09-F10 | supported | high | yes | `/about` need not preserve repository history. |
| C10 | Compression must preserve current decision/state, canonical source, scope, boundaries, exceptions/caveats, and next action where material. | confirmed synthesis | F06, F12, F14 | supported | high | yes | Review semantic preservation. |
| C11 | Temporary RC memory should be superseded after acceptance or changes requested. | confirmed synthesis | F04, F07, R14 | supported | high | yes | State transition is a sync trigger. |
| C12 | Evaluation Signals may report a memory-hygiene signal but cannot write, delete, or choose disposition automatically. | confirmed | F13, F16 | verified | critical | yes | Preserve S5.R2 boundary. |
| C13 | Advisory automation may compare files or report drift but all content changes remain explicit and reviewable. | confirmed | R11, F03, F13 | verified | critical | yes | No sync engine. |
| C14 | No memory score, completeness metric, or mandatory inclusion model is required. | confirmed synthesis | user mission, F10-F12, F15 | supported | critical | yes | Quality is disposition correctness, not volume. |
| C15 | S5.R3 must normalize S5.R2 accepted/S5.R3 Review state and synchronize `/about` for the RC. | confirmed | F04, user mission | verified | high | yes | Do not record S5.R3 acceptance or start S5.R4. |
