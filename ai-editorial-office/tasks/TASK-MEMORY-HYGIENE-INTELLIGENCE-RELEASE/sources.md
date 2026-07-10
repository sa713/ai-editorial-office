# Sources

Checked: 2026-07-10

## Repository sources

| ID | Source | Type / proximity | Freshness | Reliability | Used for | Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | [`AGENTS.md`](../../AGENTS.md) | canonical governance / primary | current | high | Authority, owners, roles, review, artifact boundaries | Does not define the S5.R3 mechanism |
| R02 | [`ROADMAP.md`](../../ROADMAP.md) | strategy / primary | state text stale | high for strategy | Stable architecture, Stage 5 purpose, memory as export | State predates S5.R2 acceptance |
| R03 | [`BACKLOG.md`](../../BACKLOG.md) | operational plan / primary | current | high | S5.R3 goal and active state | Not architecture canon |
| R04 | [`project-state.md`](../../project-state.md) | current-state owner / primary | partially stale | high | Current architecture/state and `/about` contract | State predates S5.R2 acceptance |
| R05 | [`kb/editorial_learning_framework.md`](../../kb/editorial_learning_framework.md) | canonical KB / primary | current | high | Knowledge Evolution, stale/correction/retirement, memory disposition | Current memory rules are too compact for S5.R3 scenarios |
| R06 | [`kb/customer_feedback_loop.md`](../../kb/customer_feedback_loop.md) | canonical feedback owner / primary | current | high | No automatic propagation from feedback | Actual customer feedback only |
| R07 | [`kb/capability_registry.md`](../../kb/capability_registry.md) | canonical capability map / primary | current | high | Memory Curation, Knowledge Evolution, stale detection, Integrity Checking | Needs only bounded refinements if owner synthesis supports them |
| R08 | [`agents/chief_editor.md`](../../agents/chief_editor.md) | canonical role / primary | current | high | Memory classification and governance owner | Current sync behavior lacks exact disposition model |
| R09 | [`agents/review_agent.md`](../../agents/review_agent.md) | canonical role / primary | current | high | Independent challenge | Current memory checks lack exact-copy/summary detail |
| R10 | [`pipelines/review_pipeline.md`](../../pipelines/review_pipeline.md) | review sequencing owner / primary | current | high | Existing Knowledge Evolution review gate | Must not become a new gate |
| R11 | [`scripts/check_about_memory_package.sh`](../../scripts/check_about_memory_package.sh) | executable contract / primary | current | high | 20-file limit and exact-copy validation | Cannot validate summary semantics automatically |
| R12 | [`about/CHATGPT_MEMORY_USAGE_RULES.md`](../../../about/CHATGPT_MEMORY_USAGE_RULES.md) | derived memory guidance | current before S5.R3 | medium-high | Existing `/about` boundary and copy precedence | Non-canonical by design |
| R13 | [`releases/S5-R1/release-pack.md`](../../releases/S5-R1/release-pack.md) | accepted release evidence | current | high | Feedback/learning integration and non-promotion | S5.R1-specific |
| R14 | [`releases/S5-R2/release-pack.md`](../../releases/S5-R2/release-pack.md) | accepted release evidence | current | high | Evaluation Signals, no automatic memory action, accepted verdict | S5.R2-specific |
| R15 | [`templates/release-pack.md`](../../templates/release-pack.md) | active release standard | current | high | Project Lead packet | No mandatory memory-disposition section |

## External authoritative sources

| ID | Source | Authority / date | Used for | Transfer limitation |
| --- | --- | --- | --- | --- |
| E01 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | NIST consensus framework, AI RMF 1.0; current page checked 2026-07-10 | Documentation, periodic review, role accountability, knowledge limits, human oversight | AI risk scope; adapted only as governance principle |
| E02 | [NIST AI 600-1 Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | NIST, 2024 | Provenance, origin/modification tracking, limitations, privacy and human authentication | Broader GAI risk profile, not a project-memory specification |
| E03 | [W3C PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation, 2013 | Derived-from, primary-source, revision, invalidation, and attribution concepts | Formal ontology is not implemented; principles only |
| E04 | [RFC 9111 HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) | IETF Internet Standard, 2022 | Origin validation, freshness/staleness, invalidation, most-restrictive conflict treatment | Cache analogy only; `/about` is not an HTTP cache |
| E05 | [OpenGitOps Principles v1.0](https://opengitops.dev/) | CNCF/OpenGitOps principles | Declarative, versioned desired-state source and reconciliation pattern | Automatic pull/reconcile is explicitly not adopted here |
| E06 | [KCS v6 Practices Guide](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide) | Consortium for Service Innovation, living v6 guide | Knowledge maintenance through use; timely/findable/usable content | Service knowledge-base context |
| E07 | [KCS Article State](https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/301-Evolve_Loop/Practice_5_Content_Health/Technique_5.2) | Consortium practice | Validated/archived lifecycle; preserve snapshots/history when required | Article lifecycle is not imported as task statuses |
| E08 | [KCS Flag It or Fix It](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030/040/030) | Consortium practice | Duplicate consolidation and archive rather than parallel answers | Project memory is smaller and owner-controlled |
| E09 | [The National Archives: Appraisal and Selection](https://www.nationalarchives.gov.uk/information-management/manage-information/planning/guiding-principles/appraisal-and-selection/) | UK National Archives guidance | Continuing value, early appraisal, documented rationale, stakeholder context | Public-record obligations are not transferred wholesale |
| E10 | [The National Archives: Disposing of Records](https://www.nationalarchives.gov.uk/information-management/manage-information/policy-process/disposal/) | UK National Archives guidance | Retain by business/legal/historical value; explain disposal | Legal retention rules vary; use value/rationale principle only |
| E11 | [EUR-Lex GDPR Article 5](https://eur-lex.europa.eu/eli/reg/2016/679/art_5/oj/eng) | EU regulation, 2016 | Accuracy, data minimization, purpose/storage limitation, accountability | Applies to personal data; supports strict sensitive-data omission |
| E12 | [LongLLMLingua](https://aclanthology.org/2024.acl-long.91/) | ACL 2024 primary research | Long-context cost/performance and importance-density rationale for compression | Prompt-compression results do not prove summary correctness here |
| E13 | [ReadTwice](https://research.google/pubs/readtwice-reading-very-large-documents-with-memories/) | NAACL 2021 primary research | Segment-to-summary memory as a compact second-pass representation | Model research, not project governance |
| E14 | [GitHub pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-a-pull-request/about-pull-request-reviews) | GitHub official documentation | Review, approval/request-changes, reviewer trace | Platform mechanics are not added to the local workflow |

## Source sufficiency

- Coverage is sufficient across knowledge maintenance, documentation hygiene,
  AI context/memory, state synchronization, staleness, lifecycle/retention,
  compression, canonical/derived views, cache consistency, organizational
  memory, provenance, privacy, and human review.
- Sources converge on traceable origin, bounded purpose, periodic or trigger-
  based review, explicit lifecycle/disposition, consolidation, and accountable
  human judgment.
- No source justifies autonomous writes or making a derived summary
  authoritative.
- External evidence cannot prove which project facts deserve external memory;
  that remains a repository-specific materiality judgment.
