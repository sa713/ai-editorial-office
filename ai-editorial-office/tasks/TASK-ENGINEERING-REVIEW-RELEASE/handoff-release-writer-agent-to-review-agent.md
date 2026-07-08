# Handoff: Release Writer To Review Agent

## Transfer

- From: `writer_agent`
- To: `review_agent`
- Status: `review`
- Risk mode: `standard`
- Process depth: `full`

## Release Candidate Artifacts

- `../../research/engineering_review_competency_landscape.md`
- `../../research/engineering_review_architecture_synthesis.md`
- `../../kb/engineering_review.md`
- `../../research/engineering_review_release_report.md`
- canonical integration updates in `AGENTS.md`, role specs, KB, review
  pipeline, Codex task standard, and project state
- `/about` sync updates
- `../../tests/engineering_review_smoke_test.md`

## Delta Summary

Engineering Review is implemented as one shared capability with selectable
lenses. The release intentionally avoids new roles, pipelines, lifecycle
stages, review gates, mandatory artifacts, or one capability per competency.

## Review Focus

- Architecture preservation.
- Capability minimalism.
- Correct competency disposition: implemented, merged, postponed, rejected.
- Engineering Review vs Architecture Review boundary.
- Review-gate preservation.
- `/about` sync correctness.
- Validation evidence.

## Stop Conditions

Stop if the release:

- redesigns frozen architecture;
- creates specialist default roles;
- creates a new review gate or mandatory artifact;
- treats postponed database/performance work as implemented standalone
  capability;
- leaves `/about` copied files out of sync;
- lacks validation evidence.
