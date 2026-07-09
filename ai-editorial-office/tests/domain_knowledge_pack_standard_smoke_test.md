# Domain Knowledge Pack Standard Smoke Test

Status: manual smoke-test / synthetic examples only.

Purpose: check whether Domain Knowledge Pack activation, structure, source
requirements, boundaries, review, update, and retirement stay inside
`/kb/domain_knowledge_pack_standard.md` without creating roles, pipelines,
lifecycle stages, review gates, policy owners, capability owners, or mandatory
ordinary task artifacts.

This file is not a canonical rule owner. Canonical guidance lives in
`/kb/domain_knowledge_pack_standard.md`.

## Expected Classification Labels

- `activate_pack`: Domain context materially changes evidence depth,
  terminology, risk, review focus, or output quality.
- `do_not_activate`: Domain term is present, but ordinary task evidence is
  enough.
- `research_first`: A needed pack does not exist or is stale, so source-specific
  research is required before pack use.
- `boundary_handoff`: The task crosses domains and Chief Editor must choose
  primary pack, multiple packs, or no pack.
- `reject_pack_content`: Proposed pack content is unsourced, volatile, or
  duplicates a canonical owner.
- `update_or_retire`: Source age, supersession, contradiction, or repeated
  review finding triggers update, deprecation, or retirement review.

## Cases

| Case | Scenario | Expected | Checks |
| --- | --- | --- | --- |
| DKP-01 | A future Software Architecture pack is used to review an architecture-sensitive canon decision with quality-attribute tradeoffs. | `activate_pack` | activation reason recorded; Architecture Review ownership preserved |
| DKP-02 | A social post mentions "architecture" as a metaphor and makes no system-design claim. | `do_not_activate` | no pack activation for incidental terminology |
| DKP-03 | A proposed DevSecOps pack contains deployment mandates but no source register. | `reject_pack_content` | no policy ownership; source register required |
| DKP-04 | A task spans software architecture, secure delivery, and incident response. | `boundary_handoff` | Chief Editor chooses primary/multiple packs or source-specific research |
| DKP-05 | A pack cites a withdrawn external standard as current without a stale-if note. | `update_or_retire` | stale source challenge and retirement/update path visible |
| DKP-06 | A writer wants a new Security Reviewer role because a cybersecurity pack is active. | `reject_pack_content` | packs are context packages, not role creators |
| DKP-07 | A task needs AI evaluation guidance before any AI Engineering pack exists. | `research_first` | ordinary research proceeds; no invented pack authority |
| DKP-08 | Review uses a pack's review questions inside existing `review.md`. | `activate_pack` | no second review gate or mandatory checklist |

## Pass Criteria

- Activation is material, recorded, and bounded.
- Non-activation is allowed when a domain term is incidental.
- Sources and confidence limits are reconstructable.
- Domain boundaries and adjacent-domain handoffs are explicit.
- Pack content never overrides canonical owners.
- Review happens inside the existing review gate.
- Updates, deprecation, and retirement use source-backed Knowledge Evolution
  disposition when material.
- No case creates a new role, pipeline, lifecycle stage, review gate, policy
  owner, capability owner, client profile, task status model, or mandatory
  ordinary task artifact.
