# Memory Hygiene Intelligence Landscape

## Executive conclusion

Authoritative practice supports a small, source-first, human-reviewed memory
hygiene discipline rather than an autonomous memory system. External memory is
most reliable when it is explicitly derived from an authoritative origin,
revalidated after material source changes or drift signals, limited to a clear
purpose, consolidated when duplicated, compressed without losing governing
meaning, and retired when it no longer has continuing external-memory value.

For AI Editorial Office this means `/about` should behave as a curated derived
view: exact copies when operational fidelity is required, compact summaries
when navigation and persistent context are enough, omission for repository-
only or sensitive detail, and explicit no-sync when canon changed without a
meaningful external-memory effect.

## Research question

What bounded practices can keep external project memory accurate, compact,
useful, synchronized, and non-canonical without automatically propagating
unreviewed repository content or turning maintenance into continuous growth?

## Method and evidence boundary

Research covered:

- knowledge-base maintenance and content health;
- documentation/review hygiene;
- AI context and memory compression;
- configuration and derived-state reconciliation;
- stale-state detection and cache validation;
- records appraisal, retention, disposal, and auditability;
- provenance and primary-source/derived-view relationships;
- privacy, minimization, and omission;
- human oversight and accountable review.

Primary and authoritative sources were preferred: NIST, W3C, IETF, CNCF/
OpenGitOps, the Consortium for Service Innovation, The National Archives,
EUR-Lex, ACL research, Google Research, and GitHub documentation. External
mechanisms are not copied wholesale. Cache and GitOps are consistency analogies;
records and privacy rules are used only for conservative lifecycle/minimization
principles; compression studies motivate compactness but cannot validate this
project's summaries.

## Practice landscape

### 1. Source of truth and provenance

W3C PROV provides distinct relations for primary source, derivation, revision,
quotation, attribution, and invalidation. NIST's Generative AI Profile likewise
emphasizes tracking origin, modifications, dates/versions, sources, provenance
limitations, and human authentication.

Transfer to project memory:

- every external-memory fact must have a repository source;
- a copied file and a summary are different forms of derivation;
- source path and current canonical meaning must remain reconstructable;
- memory cannot introduce a rule or resolve a repository ambiguity by itself;
- if source and memory conflict, the source wins and the memory becomes a
  repair target.

### 2. Synchronization triggers are not automatic writes

RFC 9111 distinguishes fresh from stale cached representations and validates a
stale representation against its origin before reuse. It also treats state-
changing operations as invalidation signals. OpenGitOps places desired state in
a declarative, versioned source and reconciles other state to it.

The transferable principle is source-first revalidation. The non-transferable
part is automatic reconciliation: this mission explicitly requires manual,
reviewable memory changes.

Useful triggers:

- an exact-copy source changes;
- accepted release state or active next action changes;
- canonical roles, lifecycle, authority, supported features, or memory usage
  rules change materially;
- a checker reports mismatch or package-boundary failure;
- review, Evaluation Signals, or repository inspection exposes stale,
  duplicated, contradictory, sensitive, or bloated memory;
- a temporary state becomes accepted, rejected, superseded, or obsolete;
- a summary no longer gives enough current context for safe use.

Each trigger opens a materiality check. It does not authorize a write.

### 3. Knowledge-base content health

KCS treats knowledge as evolving through use and focuses on timely, findable,
usable content. Its article-state practice distinguishes active confidence from
archived content. Its duplicate guidance recommends merging overlapping
answers and archiving the redundant article while preserving useful history
and links.

Transfer to project memory:

- search existing summary locations before adding a fact;
- consolidate duplicate facts instead of adding a third copy;
- preserve unique scope, caveats, source pointers, and still-useful context;
- retire obsolete memory from the active package rather than presenting it as
  an equal answer;
- keep detailed history in versioned repository artifacts, not in the compact
  external package.

### 4. Information lifecycle and retirement

The National Archives defines appraisal as distinguishing records of continuing
value from those without continuing value. Its guidance stresses early
appraisal, documented rationale, stakeholder context, and retention tied to
business, legal, or historical need. Disposal is an accountable lifecycle
decision, not casual cleanup.

Transfer to project memory:

- include a fact only while it has continuing external-memory value;
- retire obsolete or misleading facts when canon and current use no longer need
  them;
- do not delete repository history merely to shorten `/about`;
- when removal could hide meaningful context, record the disposition in the
  release report, final decision, or review artifact and point to the surviving
  canonical/history source.

### 5. Omission, privacy, and purpose limitation

GDPR Article 5 states purpose limitation, accuracy, data minimization, storage
limitation, integrity/confidentiality, and accountability for personal data.
NIST AI 600-1 also connects provenance tracking with privacy/security and
recommends removing personally identifiable information where appropriate.

Conservative project rule:

- omit private, sensitive, client, credential, personal, source-restricted,
  task-local, or security-sensitive detail unless explicit authorization,
  external-memory purpose, and safe wording all exist;
- omit internal research notes, raw findings, draft debate, and temporary
  implementation detail when canon or a compact conclusion is enough;
- do not interpret omission as deletion from repository records;
- correct inaccurate external personal/sensitive facts promptly and use the
  minimum detail necessary.

### 6. Compression and context usefulness

LongLLMLingua reports that long context can raise cost, reduce performance, and
create position bias, while higher information density can improve long-context
use. ReadTwice demonstrates a model architecture that summarizes segments into
a smaller memory table for later use.

The project-specific synthesis is not token-level compression. It is semantic
selection:

- retain current decision/state and next action;
- retain the authoritative source and whether the memory is an exact copy or
  summary;
- retain scope, applicability, non-applicability, and authority boundaries;
- retain material caveats, exceptions, risk, and human-approval state;
- remove raw evidence, implementation narration, repeated prose, temporary
  detail, and already-discoverable repository-only material;
- replace several overlapping facts with one stronger statement and source
  pointer.

Compression fails when it makes a statement broader, more certain, more
permanent, or more authoritative than canon.

### 7. Human-in-the-loop governance

NIST AI RMF ties documentation to transparency, human review, accountability,
clear roles, periodic review, knowledge limits, and human oversight. GitHub's
review model provides explicit approve/request-changes outcomes and a saved
review trail.

Transfer to project memory:

- Chief Editor classifies materiality and disposition;
- Writer Agent performs authorized content changes from canonical sources;
- Review Agent independently checks source fidelity, semantic preservation,
  privacy, growth, and non-automation;
- checkers may report exact-copy/package drift but may not write content;
- Project Lead remains release acceptance authority;
- no model memory, chat impression, or unsaved note is change evidence.

## Disposition model supported by research

| Disposition | Use when | Required evidence | Validation |
| --- | --- | --- | --- |
| `exact-copy` | The package intentionally exposes an active operational file whose wording must match canon | canonical source path and package mapping | byte comparison plus package check |
| `compact-summary` | External memory needs durable orientation but not the full owner file | canonical source set, material facts, boundaries, caveats | semantic comparison and independent review |
| `correct` | Memory is factually wrong, stale, or narrower/broader than canon | current canonical evidence and conflict description | old claim absent; replacement matches source |
| `compress` | Content is useful but duplicated, verbose, or too detailed | continuing-value judgment and source pointers | meaning/caveats preserved; size/repetition reduced |
| `retire` | Content is obsolete, superseded, misleading, or lacks continuing external value | current owner/state and retirement rationale | active memory no longer presents it; meaningful history remains in repo |
| `omit` | Content is internal, task-local, raw, sensitive, temporary, or not useful externally | classification and purpose check | prohibited detail absent; no required context lost |
| `defer` | Signal is plausible but canon, evidence, authorization, or replacement state is incomplete | unresolved source/evidence/approval note | no speculative write; next verification named |
| `no-sync` | Canon changed but no externally useful fact or package contract changed | affected source and materiality rationale | package remains accurate; decision recorded when material |

`compress` is the action form of `compact-summary` maintenance. A single
decision may combine dispositions at fact level, but one fact must not be both
copied and summarized in competing locations without a clear reason.

## Stale-memory indicators

- exact-copy mismatch;
- release/status/next-action conflict with accepted repository evidence;
- unresolved path, role, status, validator, or file-count statement;
- words such as current, latest, temporary, next, pending, or active without a
  surviving current-state basis;
- summary contradicts its named source or omits a boundary that changes meaning;
- duplicate facts disagree or use different scope;
- deprecated/retired feature remains described as active;
- sensitive/task-local data remains after its external purpose ends;
- package growth occurs without a new durable external-memory need;
- checker or reviewer reports drift, missing source, or package-contract failure.

Time alone is only a review signal. Repository contradiction or expired
purpose establishes the repair need.

## Contradiction handling

1. Stop using memory as evidence for the disputed fact.
2. Identify the canonical owner and current reviewed state.
3. If canon is clear, correct/replace/retire the memory from canon.
4. If canonical files conflict, route to Chief Editor and repair canon first;
   defer or block the memory write.
5. Re-run exact-copy or semantic validation.
6. Preserve a disposition note when the correction or retirement is material.

Never merge contradictory statements into a vague compromise and never update
canon to match external memory merely to remove the difference.

## No-sync decision

No-sync is correct when:

- changed content is internal research, task evidence, draft history, release
  implementation detail, or a task-local artifact;
- the canonical change does not alter any fact currently represented in
  external memory;
- external readers do not need the detail to understand current architecture,
  operation, status, constraints, or next action;
- an existing summary remains accurate and sufficient;
- the change is temporary and exporting it would create avoidable churn;
- content is sensitive, private, or source-restricted;
- evidence or approval is insufficient, so defer is safer.

A no-sync decision should be recorded in an existing release report,
`final_decision.md`, or Release Pack only when the disposition is material to
governance or future restart. No per-commit log is required.

## Architecture implications

- Existing owners are sufficient.
- `editorial_learning_framework.md` should own the exact disposition contract.
- Capability Registry should refine existing Memory Curation and Integrity
  Checking, not name a new capability.
- Chief Editor should own materiality/disposition and Review Agent the
  independent semantic/fidelity challenge.
- Review Pipeline should include memory hygiene in its existing Knowledge
  Evolution gate.
- The existing checker should remain read-only and exact-copy/package focused.
- Summary validation must remain human because the current package contains
  deliberately compact synthesized files.
- Evaluation Signals may surface a problem but cannot choose or execute a
  memory action.

## Source register

See task-local [`sources.md`](../tasks/TASK-MEMORY-HYGIENE-INTELLIGENCE-RELEASE/sources.md)
for authority, freshness, use, and transfer limitations. Facts and downstream
claims are separated in [`facts.md`](../tasks/TASK-MEMORY-HYGIENE-INTELLIGENCE-RELEASE/facts.md)
and [`claims_table.md`](../tasks/TASK-MEMORY-HYGIENE-INTELLIGENCE-RELEASE/claims_table.md).

## Research sufficiency

The evidence is sufficient to choose an existing-owner architecture. The
remaining uncertainty is empirical: future use must show whether the compact
disposition contract prevents drift and growth in real releases. That
uncertainty does not justify automation, scoring, or a new owner in S5.R3.
