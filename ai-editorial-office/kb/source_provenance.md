# Source Provenance

## Purpose

Provide practical guidance for importing, cleaning, summarizing, activating,
reviewing, and updating external or client-specific source material.

This guidance does not override `AGENTS.md`, role specs, pipelines, task
artifacts, review-gate, or client-profile activation rules.

## Source chain

```text
external source
-> cleaned Markdown
-> source notes
-> source status
-> profile/rules
-> smoke-test
```

Cleaned Markdown is not automatically trustworthy. It can be used only within
the provenance, status, scope, and usage boundaries recorded for that source.

## Source statuses

- `pending_source`
- `active`
- `stale`
- `deprecated`

## Status meanings

### pending_source

Source exists or is expected, but has not been verified enough for rule use.

Agents must not claim policy compliance, activate a source-backed profile as
verified, or fill gaps by inventing missing rules.

### active

Source is verified, converted or cleaned, source notes exist, omissions and
uncertainties are recorded, and the relevant smoke-test has passed.

Rules or profiles may use the source only within the declared scope.

### stale

Source may be outdated or superseded. Do not claim current policy compliance
from it without review.

### deprecated

Source must not be used for new work except historical comparison.

## Import rules

- Keep original/source material outside safe-core unless explicitly approved.
- Do not commit PDF, DOCX, PPTX, binary, or source files to safe-core.
- Use cleaned Markdown only when redistribution and sensitivity allow it.
- Record source date, import date, owner, conversion method, omissions,
  uncertainties, sensitivity, and redistribution status.
- Never invent missing policy, client, compliance, or source rules during
  cleaning.
- If source status is not `active`, agents must not claim source or policy
  compliance.

## Cleaned Markdown rules

Cleaned Markdown should preserve the meaning of the source while removing
formatting noise. It must not silently add rules, conclusions, examples,
definitions, or compliance claims that are absent from the source.

When information is omitted or normalized, record it in source notes.

## Source-notes rules

Use `templates/artifacts/source_notes_template.md` to document:

- source metadata;
- conversion and cleaning method;
- omitted or uncertain content;
- provenance paths;
- verification boundaries;
- usage rules;
- update and staleness triggers.

Source notes should make it clear what the cleaned source can and cannot be used
for.

## Smoke-test rules

Use `templates/artifacts/source_import_smoke_test_template.md` after source
import or source update.

A source should not be treated as `active` until the smoke-test passes or an
equivalent reviewed check is recorded.

Smoke-tests should confirm that:

- source notes exist;
- source status is explicit;
- omissions and uncertainties are recorded;
- missing rules were not invented;
- compliance claims are allowed only when source status and source notes permit;
- stale or deprecated sources are not used as active.

## Update rules

Recheck source status when:

- a newer source appears;
- the source owner changes the policy, rules, or document;
- the source date becomes too old for the intended use;
- a review finds an unsupported compliance claim;
- a client profile or reusable rule depends on the source.

If the source cannot be reverified, set status to `stale` or `pending_source`
instead of continuing to treat it as active.

## Client profile relation

Client profiles are task-scoped. A client profile can point to source
provenance artifacts, but it does not become global editorial policy.

Sber profile handling is a specific case of this general mechanism: if the
client source is missing, stale, or unverified, use `pending_source`, rely only
on explicitly provided task constraints, and do not claim client-policy
compliance.
