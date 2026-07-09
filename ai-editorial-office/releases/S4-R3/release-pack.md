# Release Pack

Release readiness rule: no release is considered ready for Project Lead review
until a completed `release-pack.md` exists.

## Release

- Release ID: `S4.R3`
- Release title: DevSecOps Domain Pack
- Status: release candidate ready for Project Lead review
- Date: 2026-07-10

## Executive Summary

S4.R3 adds the DevSecOps Domain Knowledge Pack:
`kb/devsecops_domain_pack.md`. The pack provides source-backed DevSecOps
context for secure software delivery, CI/CD, automation, configuration,
supply-chain risk, deployment boundaries, validation evidence, and
operational-security assumptions. It improves Engineering Review and
Architecture Review context without replacing them and is ready for Project
Lead review after independent review and final validation.

## Architectural Impact

Architecture impact:

- Small

Reason:

The release adds one source-backed domain context package and discoverability
references. It does not change roles, capabilities, pipelines, lifecycle
stages, review gates, task statuses, canonical governance owners, client
profiles, or mandatory ordinary artifacts.

## Goal Of The Release

Create a reusable DevSecOps Domain Knowledge Pack that helps AI Editorial
Office activate deep secure delivery context when material, while keeping
DevSecOps expertise bounded as context rather than workflow, policy, role,
capability, or review ownership.

## Architecture Decisions

- Decision: create `kb/devsecops_domain_pack.md` as a release-candidate Domain
  Knowledge Pack.
- Rationale: a single canonical pack file provides practical source-backed
  context without adding a framework, registry, role, pipeline, gate, or
  mandatory artifacts.
- Architecture preserved: the pack is subordinate to `AGENTS.md`,
  `kb/domain_knowledge_pack_standard.md`, `kb/engineering_review.md`,
  `kb/software_architecture_domain_pack.md`, evidence guidance, and existing
  task governance.
- Status decision: mark the pack `release candidate`, not `active`, until
  Project Lead review.

## Capability Decisions

- Capability shape: no new capability.
- Activation: Chief Editor or a role may activate the pack only when DevSecOps
  context materially affects evidence depth, terminology, risk, review focus,
  or output quality.
- Review: Review Agent challenges active pack use inside the existing review
  gate using the Domain Knowledge Pack Standard.
- Non-goals: no DevSecOps role, no DevSecOps pipeline, no DevSecOps review
  gate, no DevSecOps policy owner, no mandatory SBOMs/scans/attestations, no
  Engineering Review replacement.

## Scope

### Implemented

- Source-backed DevSecOps Domain Knowledge Pack.
- Activation and non-activation boundaries.
- Questions the pack can answer.
- Domain boundary and overloaded-term definitions.
- Evidence and confidence rules.
- Domain vocabulary.
- DevSecOps principles.
- Secure SDLC / SSDF concepts.
- CI/CD security.
- Supply-chain security.
- Secrets and credentials.
- Configuration and environment safety.
- Dependency and tooling risk.
- Container, runtime, and infrastructure considerations.
- Validation and evidence expectations.
- Operational security considerations.
- Review questions, common mistakes, source register, confidence notes, update
  rules, retirement rules, and relation to canon.
- Research landscape.
- Architecture synthesis.
- Release report with representative scenario validation.
- Release state updates in Backlog, Roadmap, project state, and memory
  summaries where required.

### Merged

- NIST SSDF secure SDLC framing.
- OWASP SAMM maturity and secure build/deployment/operations framing.
- OWASP ASVS verification vocabulary.
- SLSA v1.2 supply-chain, provenance, and verification vocabulary.
- OpenSSF Scorecard repository-security signal framing.
- GitHub Actions and GitLab CI/CD platform-security guidance.
- Kubernetes Pod Security, Secrets, and RBAC guidance.
- Docker build, secret, and engine-security guidance.
- CIS benchmark references for Docker and Kubernetes.
- NTIA SBOM transparency framing.
- Microsoft SDL lifecycle framing.
- Google SRE operational-readiness prompts.

### Postponed

- Cybersecurity Domain Pack.
- AI Engineering Domain Pack.
- Pack registry or index automation.
- Automated source freshness checks.
- Dedicated validator for pack section completeness.
- Cloud-provider-specific DevSecOps packs.
- Detailed CIS benchmark control reproduction.

### Rejected

- New DevSecOps, Security Reviewer, DevOps, SRE, Platform, or Release
  Engineering role.
- New DevSecOps capability.
- New DevSecOps review gate.
- New DevSecOps pipeline or lifecycle stage.
- New DevSecOps policy owner.
- Mandatory SBOM, SLSA, Scorecard, scanner, attestation, signature, or
  checklist artifacts.
- Treating CI/CD platform guidance as universal law across all providers.
- Treating SBOMs, SLSA, Scorecard, signatures, scans, or attestations as
  automatic pass/fail verdicts.
- Expanding Engineering Review into a DevSecOps encyclopedia.
- Treating `/about` as canonical pack storage.

## Canonical Files Changed

- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/kb/devsecops_domain_pack.md`
- `ai-editorial-office/project-state.md`

## Canonical Owners Updated

Updated canonical owners:

- `kb/00_index.md`: discoverability.
- `project-state.md`: current state and release-candidate visibility.

New canonical owners introduced:

- None in the governance sense. The new pack is a canonical domain-context
  package, but it does not own policy, capability, workflow, role behavior,
  review outcomes, task statuses, or mandatory artifacts.

## Non-Canonical Files

- `ai-editorial-office/BACKLOG.md`
- `ai-editorial-office/ROADMAP.md`
- `ai-editorial-office/research/devsecops_pack_landscape.md`
- `ai-editorial-office/research/devsecops_pack_architecture_synthesis.md`
- `ai-editorial-office/research/devsecops_pack_release_report.md`
- `ai-editorial-office/releases/S4-R3/release-pack.md`
- `ai-editorial-office/tasks/TASK-DEVSECOPS-DOMAIN-PACK-RELEASE/`
- `about/CHATGPT_MEMORY_EDITORIAL_STANDARDS.md`
- `about/project_tree.md`
- `about/project-state.md`

## Release Metrics

Canonical files changed: 3

Research artifacts: 3

Templates: 0

Tests: 0 new automated tests; scenario validation recorded in release report.

Memory package updated: yes

Validation scripts executed: 5

Commits: final release commit will be created after final governance; hash
delivered in handback to avoid self-referential commit-hash churn in this file.

## Validation Results

Scenario validation:

| Check | Result |
| --- | --- |
| GitHub Actions workflow with secrets and permissions | pass |
| Dependency update with supply-chain risk | pass |
| Docker/container configuration change | pass |
| Local deployment or automation script | pass |
| Security-sensitive CI/CD gate change | pass |
| Generic security mention with no delivery surface | pass |

Command validation:

| Check | Result |
| --- | --- |
| `git diff --check` | pass |
| `sh ai-editorial-office/scripts/check_about_memory_package.sh` | pass |
| `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` | pass |
| `sh ai-editorial-office/tests/test_task_pack_generator.sh` | pass |
| `python3 ai-editorial-office/scripts/validate_task_lifecycle.py ai-editorial-office/tasks/TASK-DEVSECOPS-DOMAIN-PACK-RELEASE` | pass |

## Known Risks

- Pack may be over-activated for incidental DevSecOps or security terms;
  mitigated by non-activation criteria and scenario validation.
- Platform-specific guidance may become stale quickly; mitigated by source
  register, stale-if triggers, confidence notes, and task-specific source
  refresh expectations.
- SBOMs, SLSA, Scorecard, scans, signatures, and attestations may be treated as
  verdicts; mitigated by repeated evidence-signal framing.
- Future Cybersecurity Domain Pack may require boundary tuning; update rules
  record that trigger.
- Project Lead may request different scope, source depth, or integration before
  acceptance.

## Open Questions

- None blocking for release-candidate review.

## Recommended Project Lead Decision

Recommended decision:

Changes Requested or Accepted after Project Lead architectural review.

Rationale:

The release is internally complete and review-ready. Acceptance remains a
Project Lead decision.

## Suggested Next Release

- `S4.R4 - Cybersecurity Domain Pack`

## Acceptance Checklist

- Architecture preserved
- Review gate unchanged
- No new roles
- No new pipelines
- No lifecycle changes
- Validation passed
- Memory synchronized
- Ready for Project Lead review

## Release Verdict

Project Lead: Accepted

Review Date: 2026-07-10

Reviewer: Project Lead

Notes:

- Release accepted.
- Architecture preserved.
- DevSecOps Domain Pack correctly remains a source-backed domain context package.
- Engineering Review ownership preserved.
- No new capabilities, roles, pipelines, lifecycle stages, review gates, or mandatory artifacts introduced.
- Validation passed.
- Memory synchronized.
- Future observation recorded: evaluate Domain Pack section reuse after additional packs are implemented.
