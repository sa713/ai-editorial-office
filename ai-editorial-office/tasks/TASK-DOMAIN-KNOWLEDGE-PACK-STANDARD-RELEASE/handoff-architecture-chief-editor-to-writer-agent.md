# Handoff: Chief Editor To Writer Agent

## Transfer

- From role: `chief_editor`
- To role: `writer_agent`
- Reason: architecture synthesis approved the smallest compatible standard
  shape and implementation can begin.

## What Changed

- Created
  `../../research/domain_knowledge_pack_standard_architecture_synthesis.md`.
- Selected `../../kb/domain_knowledge_pack_standard.md` as the new canonical
  owner for the Domain Knowledge Pack Standard.
- Approved only lightweight integration references in routing, role, task,
  lifecycle, review, state, and memory files as needed.

## Writer Contract

Create the standard and release documentation. Keep domain packs as
source-backed context packages consumed by existing roles and capabilities.

Must include:

- pack purpose and structure;
- activation and non-activation criteria;
- source, evidence, freshness, update, and retirement rules;
- relation to roles, capabilities, canonical owners, and `/about`;
- forbidden content and anti-patterns;
- review and validation expectations;
- compact template.

Must not include:

- Software Architecture or DevSecOps pack implementation;
- new roles, pipelines, lifecycle stages, review gates, or mandatory ordinary
  task artifacts;
- packs as policy owners or capability owners;
- automatic canon promotion.

## Next Action

Writer Agent should patch canonical files, write the release report and release
pack, synchronize `/about` if required, and prepare validation evidence for
review.

## Stop Conditions

Stop if implementation requires a forbidden architecture change, duplicate
canonical owner, or source claim that cannot be supported.
