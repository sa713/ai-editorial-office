# Domain Knowledge Pack Standard

This file is the canonical owner for Domain Knowledge Pack purpose, structure,
activation, source/evidence requirements, domain boundaries, forbidden content,
review, update, retirement, and relation to existing AI Editorial Office roles,
capabilities, canonical owners, and `/about`.

It is a standard for future domain packs. It is not itself a domain pack.

## Purpose

Domain Knowledge Packs help AI Editorial Office apply source-backed domain
context without turning domain expertise into loose fact dumps, hidden policy,
duplicate capability ownership, new roles, new pipelines, new lifecycle stages,
or mandatory ordinary task artifacts.

A domain pack should make future work better by answering:

- when the domain context should be activated;
- what domain boundary applies;
- which sources support the pack;
- which concepts, risks, and failure modes matter;
- what evidence confidence is justified;
- when the pack is stale, needs update, or should be retired;
- how existing roles and capabilities should use it without giving the pack
  operational authority.

## Definition

A Domain Knowledge Pack is a reusable, source-backed, bounded, maintained
domain-context package.

It may provide domain terminology, durable principles, source maps, evidence
expectations, review questions, common risks, and failure modes for a named
domain.

It does not decide workflow, policy, role authority, review outcome, task
status, final governance, or canon promotion.

## Non-Goals

A Domain Knowledge Pack is not:

- a policy owner;
- a capability owner;
- a role spec;
- a pipeline;
- a lifecycle stage;
- a review gate;
- a client profile;
- a task status model;
- an expert-system rule engine;
- a mandatory ordinary task artifact;
- a permanent fact database;
- an automatic path for canon updates.

## Required Pack Structure

Each accepted pack must include these sections, with compact content preferred:

1. Pack identity
   - pack name;
   - domain;
   - current status: draft, release candidate, active, deprecated, retired;
   - owner or maintainer context;
   - created and last reviewed dates;
   - stale-if triggers.
2. Purpose and intended use
   - what work the pack improves;
   - which readers or roles consume it;
   - what decisions or artifacts it supports.
3. Activation criteria
   - material task triggers;
   - non-activation criteria;
   - where activation must be recorded.
4. Domain boundary
   - in-scope topics;
   - out-of-scope topics;
   - adjacent domains and handoff boundaries;
   - overloaded terms and context-specific meanings.
5. Source register
   - source title and link or repository path;
   - source class;
   - authority;
   - version or publication date;
   - last checked date;
   - relevance;
   - confidence limits.
6. Evidence and confidence rules
   - claims the pack supports;
   - claims the pack cannot support;
   - evidence class and confidence expectations;
   - source freshness requirements.
7. Domain concepts and terminology
   - durable terms;
   - definitions;
   - synonyms or alternate labels when useful;
   - scope notes for terms that are often misused.
8. Domain guidance
   - durable principles, heuristics, risks, and failure modes;
   - each material item source-backed or explicitly caveated.
9. Review questions
   - domain-specific checks Review Agent can apply inside the existing review
     gate.
10. Update and retirement rules
    - update triggers;
    - stale knowledge triggers;
    - retirement triggers;
    - disposition path through Knowledge Evolution when needed.
11. Relation to existing canon
    - capabilities the pack may support;
    - canonical owners it must not override;
    - `/about` memory disposition when relevant.

## Activation

A domain pack activates only when domain context is material to the task.

Activation can be selected by Chief Editor during routing, or requested by a
role when evidence shows domain context is necessary for safe continuation.

Activation should be recorded in the smallest existing task artifact that makes
the next role safe:

- `orchestration_plan.md`;
- `task-manifest.md`;
- `research.md`;
- writer or UX notes;
- `review.md`;
- `final_decision.md`.

The activation note should name:

- active pack;
- activation reason;
- relevant pack sections or sources;
- evidence confidence;
- limits, stale-if triggers, or stop conditions.

Do not activate a pack merely because a domain term is mentioned. Activate it
only when the pack materially changes evidence depth, terminology, review
focus, risk handling, or output quality.

## Source And Evidence Requirements

Packs must be source-backed. Sources should be primary, authoritative, current,
or clearly marked when they are secondary, historical, or illustrative.

Every pack must include a source register. The register should make it possible
for Review Agent to reconstruct:

- what sources were checked;
- why those sources are authoritative enough for the pack;
- what each source supports;
- what source age or version limits apply;
- what important gaps remain.

Evidence confidence follows `/kb/editorial_evidence_framework.md`. A pack may
not raise confidence above what its sources justify.

Mappings to external standards, frameworks, methods, or AI Editorial Office
canon must not imply equivalence unless equivalence is source-backed. When in
doubt, use weaker language such as related, overlaps with, informs, or may
support.

## Domain Boundary Rules

Each pack must define where its domain model applies and where it stops.

Boundary sections should identify:

- in-scope work surfaces;
- adjacent domains;
- terms that change meaning across domains;
- conditions requiring another pack, another capability, or Chief Editor
  rerouting;
- source classes that are acceptable for the domain;
- source classes that are insufficient for high-governance claims.

When a task spans multiple domains, Chief Editor decides whether one pack is
primary, multiple packs are active, or the task should proceed with only
source-specific research.

## Forbidden Content

Domain packs must not contain:

- operational policy that overrides a canonical owner;
- task status transitions;
- lifecycle gates;
- role duties beyond short role-specific consequences;
- pipeline steps;
- review verdict rules;
- final governance rules;
- client-specific policy unless explicitly routed as a client profile instead;
- unsourced claims;
- copied source material without provenance or permission;
- volatile facts without version/date and stale-if trigger;
- broad best-practice commands without evidence limits;
- automatic canon-promotion instructions;
- mandatory ordinary task artifacts.

If a pack discovers a needed canonical rule, record it as a canon-update
candidate and route it through the existing canonical owner and review path.

## Relation To Capabilities And Roles

Domain packs are context packages. Capabilities remain reusable operations.
Roles remain accountability wrappers.

Examples:

- Architecture Review may use an active Software Architecture Domain Pack as
  context, but Architecture Review remains owned by
  `/kb/architecture_review.md`.
- Engineering Review may use an active DevSecOps Domain Pack as context, but
  Engineering Review remains owned by `/kb/engineering_review.md`.
- Evidence Confidence assesses source quality; the pack provides source
  pointers and confidence limits.
- Knowledge Evolution handles stale, superseded, corrected, deferred, or
  retired pack knowledge through `/kb/editorial_learning_framework.md`.

No pack creates a Specialist, Analyst, Architect, Security Reviewer, DevOps,
SRE, Fact Checker, Knowledge Curator, or Domain Owner role.

## Review Requirements

Domain-pack review happens inside the existing Review Gate. No second gate is
created.

When a reviewed artifact depends on an active domain pack, Review Agent checks:

- activation was justified;
- boundary and adjacent-domain limits were respected;
- source register supports material claims;
- stale-if triggers were considered;
- pack guidance did not override canonical policy;
- pack context did not replace a needed capability;
- unsupported or volatile facts were caveated, omitted, or returned to
  research;
- maintenance or retirement concerns were recorded when material.

When reviewing a proposed pack or pack update, Review Agent also checks that
all required pack sections exist and that maintenance cost is justified by
future value.

## Update Rules

A pack should be updated when:

- a source it depends on changes materially;
- a source becomes stale, withdrawn, superseded, or contradicted;
- repeated tasks show a pack boundary, term, risk, or review question is
  missing;
- Review Agent finds unsupported or misleading guidance;
- Project Lead or Chief Editor approves a source-backed improvement;
- a future release accepts a new domain pack standard requirement.

Updates must preserve provenance and record what changed. For small updates,
the pack itself may carry the change note. For high-governance, source-heavy,
or disputed updates, use a reviewed system task or release.

## Retirement Rules

Retire or deprecate a pack when:

- the domain is no longer used by AI Editorial Office;
- source support is too stale or weak to maintain confidence;
- the pack duplicates a better canonical owner;
- the pack repeatedly causes policy, role, capability, or lifecycle confusion;
- maintenance cost exceeds future value;
- a replacement pack supersedes it.

Retirement must preserve enough context for future readers to know why the pack
should no longer be used. Do not delete historical task artifacts merely to
clean the narrative.

## Validation Expectations

Before a new pack is accepted, validate it against at least two plausible task
scenarios for that domain. Scenario validation should test:

- activation;
- non-activation;
- source sufficiency;
- boundary clarity;
- relation to capabilities;
- review usefulness;
- stale/update/retirement triggers;
- absence of forbidden content.

Validation may be recorded in the pack, a release report, `review.md`, or a
task-local validation note. Do not create a separate validation artifact unless
review, governance, or release scope needs it.

## `/about` Boundary

Canonical domain pack standards and packs live under `ai-editorial-office/`.
The `/about` folder may contain copied files or compact memory summaries, but it
is not canonical.

Synchronize `/about` only when canonical changes require external memory
alignment. If a `/about` summary mentions domain packs, it must clearly state
that production files remain canonical.

## Compact Pack Template

Use this template only when creating a future domain pack. Remove unused
placeholder notes before review.

```markdown
# DOMAIN Domain Knowledge Pack

Status:
Created:
Last reviewed:
Stale if:

## Purpose

## Activation

- Activate when:
- Do not activate when:
- Record activation in:

## Domain Boundary

- In scope:
- Out of scope:
- Adjacent domains:
- Overloaded terms:

## Source Register

| Source | Class | Version/date | Last checked | Supports | Confidence limits |
| --- | --- | --- | --- | --- | --- |

## Evidence Rules

## Concepts And Terminology

| Term | Meaning in this pack | Notes |
| --- | --- | --- |

## Domain Guidance

## Risks And Failure Modes

## Review Questions

## Update And Retirement

- Update when:
- Retire when:
- Knowledge Evolution disposition:

## Relation To Existing Canon

- Capabilities supported:
- Canonical owners not overridden:
- `/about` disposition:
```

## Stop Conditions

Stop, reroute, or request repair when:

- source evidence is insufficient for a material domain claim;
- pack guidance conflicts with a canonical owner;
- activation reason is weak or missing;
- pack context is being treated as policy or capability ownership;
- stale source concerns cannot be resolved;
- review cannot reconstruct the source path;
- the task requires a domain pack that does not exist and ordinary research is
  not enough.
