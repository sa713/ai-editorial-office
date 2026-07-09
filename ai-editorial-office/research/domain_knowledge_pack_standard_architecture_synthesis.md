# Domain Knowledge Pack Standard Architecture Synthesis

Date: 2026-07-09

Release: `S4.R1 - Domain Knowledge Pack Standard`

Status: architecture synthesis for implementation.

## Decision Summary

Create one new canonical standard:

```text
ai-editorial-office/kb/domain_knowledge_pack_standard.md
```

This file will own Domain Knowledge Pack purpose, structure, activation,
source/evidence rules, boundaries, forbidden content, review, update,
retirement, and relation to existing roles, capabilities, canonical owners, and
`/about`.

Domain Knowledge Packs will be defined as source-backed, bounded, maintained
domain-context packages. They are not roles, pipelines, lifecycle stages,
review gates, policy owners, capability owners, task statuses, client profiles,
or mandatory ordinary task artifacts.

## What A Domain Knowledge Pack Is

A Domain Knowledge Pack is a reusable domain-context package that helps existing
AI Editorial Office roles and capabilities work with a specific domain more
accurately. It may provide:

- domain purpose and intended use;
- activation and non-activation criteria;
- boundary and adjacent-domain distinctions;
- source register and evidence expectations;
- terminology, overloaded terms, and durable concepts;
- source-backed domain principles, patterns, risks, and failure modes;
- review questions or domain challenge prompts;
- freshness, update, and retirement rules.

It is local canon only for how to use that pack's domain context. It is not a
new operational authority.

## What A Domain Knowledge Pack Is Not

A Domain Knowledge Pack is not:

- a loose fact collection;
- a policy library;
- a domain role or specialist reviewer;
- a pipeline or lifecycle overlay;
- a capability registry entry;
- a replacement for Professional Analysis, Architecture Review, Engineering
  Review, Evidence Confidence, Knowledge Evolution, or Review Agent;
- a client profile;
- a mandatory task artifact for ordinary tasks;
- an automatic canon-promotion path;
- a source conversion shortcut.

## Canonical Placement

### Selected Owner

`kb/domain_knowledge_pack_standard.md`

Rationale:

- `AGENTS.md` owns governance invariants and the ownership map, but it should
  not carry detailed pack structure and maintenance rules.
- `capability_registry.md` owns capabilities; domain packs must not become
  capabilities.
- `editorial_learning_framework.md` owns learning/canon/stale knowledge, but
  domain packs need their own pack-specific operating standard.
- `source_provenance.md` and `editorial_evidence_framework.md` own source and
  evidence mechanics, but not domain-pack purpose, activation, and retirement.

The new file is justified because no existing canonical owner cleanly owns
domain-pack structure, activation, boundaries, and maintenance.

### Integration References

Update only the files needed for discoverability and runtime behavior:

- `AGENTS.md`: canonical ownership map and Chief Editor routing consequence.
- `kb/00_index.md`: index the new canonical owner.
- `kb/capability_registry.md`: clarify packs are context packages, not
  capabilities, and roles may consume active pack context.
- `kb/shared_lifecycle_kernel.md`: allow active domain-pack context inside
  existing lifecycle stages and expansion triggers.
- `kb/task_object_model.md`: expose optional `active_domain_packs` field and
  artifact-view responsibilities without making the field mandatory when no
  pack is active.
- `agents/chief_editor.md`: select and record active domain packs when domain
  materiality is present.
- `agents/research_agent.md`: preserve domain-pack source/evidence boundaries.
- `agents/writer_agent.md`: use active pack context without adding unsupported
  claims or treating pack guidance as policy.
- `agents/review_agent.md`: challenge pack use, source basis, boundaries, and
  stale knowledge when material.
- `agents/final_editor.md`: preserve active pack caveats and avoid adding
  unreviewed domain claims.
- `pipelines/review_pipeline.md`: add domain-pack checks to the existing review
  gate.
- `project-state.md`: record S4.R1 release-candidate state after
  implementation.
- `BACKLOG.md`: move S4.R1 from `In Progress` to `Review` after successful
  validation.
- `/about`: sync copied files and summary files only if canonical changes
  require memory alignment.

No template changes are required for S4.R1. The standard may include a compact
pack template inside its own file for future pack authors.

## Architecture Boundary Decisions

### Relation To Capabilities

Domain packs are consumed by capabilities; they do not own capabilities.

Examples:

- Architecture Review may use a Software Architecture Domain Pack as source
  context, but the Architecture Review capability remains owned by
  `kb/architecture_review.md`.
- Engineering Review may use a DevSecOps Domain Pack as source context, but
  Engineering Review remains owned by `kb/engineering_review.md`.
- Evidence Confidence decides how much confidence a domain claim deserves; the
  pack supplies source and context.
- Knowledge Evolution decides whether a pack becomes stale, needs update, or
  should be retired; the pack standard defines pack-specific triggers.

### Relation To Canonical Ownership

Domain packs may reference canonical owners, but cannot override them. If a pack
identifies a rule that belongs in `AGENTS.md`, a capability file, a lifecycle
file, or a role spec, the rule must be routed as a canon-update candidate under
the existing owner and review path.

### Relation To `/about`

Domain packs remain canonical only under `ai-editorial-office/`. `/about` may
summarize the existence of domain-pack standards when memory sync is required,
but `/about` does not become a domain-pack source of truth.

### Relation To Task Artifacts

Ordinary tasks do not create domain-pack artifacts. When a pack is active, the
existing task artifacts should record:

- which pack was active;
- why it was activated;
- which sections or source evidence matter;
- what limits, caveats, or stale-if concerns apply.

This can live in `orchestration_plan.md`, `task-manifest.md`, `research.md`,
writer notes, or `review.md`, depending on stage and risk.

## Standard Structure Decision

The standard should define:

- purpose and non-goals;
- pack identity fields;
- required sections;
- activation and non-activation rules;
- source/evidence requirements;
- evidence confidence expectations;
- domain boundary rules;
- forbidden content;
- update and stale-knowledge rules;
- retirement rules;
- review and validation requirements;
- compact template.

The standard should avoid:

- a registry or database;
- scoring or maturity levels;
- automated source freshness checks;
- required pack artifact creation inside ordinary tasks;
- a separate pack review gate;
- formal ontology tooling requirements;
- a domain-pack lifecycle separate from existing lifecycle.

## Validation Design

Validate the standard against two planned packs without implementing them:

### Software Architecture Domain Pack

Expected fit:

- Uses sources such as ISO 42010, SEI architecture documentation, architecture
  quality-attribute sources, and local Architecture Review canon.
- Provides terminology, drivers, quality attribute context, architectural
  failure modes, and review questions.
- Activates for architecture-sensitive tasks.

Must not:

- replace `kb/architecture_review.md`;
- become an Architecture Reviewer role;
- create architecture approval gates;
- override `AGENTS.md` or task lifecycle.

### DevSecOps Domain Pack

Expected fit:

- Uses sources such as NIST CSF, NIST SP 800-53 where applicable, OWASP,
  delivery/operations sources, and local Engineering Review canon.
- Provides delivery, automation, configuration, secure operations, and
  risk-context guidance.
- Activates for DevSecOps-sensitive implementation, delivery, infrastructure,
  automation, or operational tasks.

Must not:

- replace Engineering Review;
- become a DevOps, Security Reviewer, or SRE role;
- become a security policy owner;
- create a delivery or security review gate.

## Rejected Architecture Options

| Option | Rejection reason |
| --- | --- |
| Domain-pack framework with registry, validators, and lifecycle | Too much architecture for S4.R1 and conflicts with minimal complexity. |
| Domain packs as Capability Registry entries | Packs are context sources, not reusable operations. |
| Domain packs as policy libraries | Would create hidden policy owners and duplicate canonical ownership. |
| Domain packs as client profiles | Client profiles are client-specific; domain packs are domain-context packages. |
| Domain packs as mandatory task artifacts | Ordinary tasks should only record active pack context when material. |
| Formal ontology requirement | SKOS informs structure, but requiring ontology tooling would be too heavy. |
| Automated stale-source scanner | Useful later, not required for the standard release. |

## Implementation Contract

Writer Agent should implement:

1. New canonical standard file:
   `kb/domain_knowledge_pack_standard.md`.
2. Minimal integration references in canonical docs and role/review files.
3. Research release report.
4. Release pack.
5. `/about` sync if changed files are copied or memory summaries need update.
6. Validation against the two scenario packs and repository validation scripts.

Writer Agent must not:

- implement Software Architecture or DevSecOps packs;
- create a new role, pipeline, lifecycle stage, or review gate;
- add mandatory ordinary task artifacts;
- make packs capability or policy owners;
- edit the legacy/private redaction path.

## Architecture Impact

Expected impact: Small.

Reason: the release adds one canonical standard owner and lightweight references
so existing roles, lifecycle, review, and task-state artifacts know how to
activate, use, review, update, and retire domain packs. It preserves existing
architecture and adds no new operational layer.

## Synthesis Verdict

Proceed to implementation. The smallest architecture-compatible release is one
canonical Domain Knowledge Pack Standard plus limited discoverability and review
integration. The release remains within the frozen architecture.
