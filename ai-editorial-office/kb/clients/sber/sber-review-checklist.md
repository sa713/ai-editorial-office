# Sber Review Checklist

Use only when `task-manifest.md` or `orchestration_plan.md` contains:

```yaml
client_profile: sber
```

This checklist is a review scaffold for source-backed Sber checks. It must be
used together with `/kb/clients/sber/editorial-policy.md`; do not treat checklist
phrasing as a replacement for the source policy.

## 1. Activation and source status

- [ ] `client_profile: sber` is explicitly recorded.
- [ ] `client_profile_status` is recorded as `active`, `pending_source`, or
      `not_applicable`.
- [ ] Sber-mode is justified by the task: Sber owns the communication, product,
      interface, campaign, or requested policy.
- [ ] Sber-mode is not being applied merely because Sber is mentioned as a topic
      or example.
- [ ] If source policy is missing, stale, or unverified, the review does not
      claim full compliance with Sber redpolicy and records
      `client_profile_status: pending_source`.

## 2. Tone and reader relationship

- [ ] Source-backed tone rules from `editorial-policy.md` are checked for the
      relevant channel and audience.
- [ ] The review cites or names the relevant policy section when a Sber-specific
      tone issue is blocking.
- [ ] If the relevant tone rule cannot be located in the source, the uncertainty
      is recorded instead of inventing a Sber rule.

## 3. Simplicity and clarity

- [ ] Source-backed clarity and simplification rules from `editorial-policy.md`
      are checked.
- [ ] The review distinguishes general AI Editorial Office clarity advice from
      Sber-specific policy requirements.

## 4. Naming, products, and organizational terms

- [ ] Sber group, brand, product, and service names match the approved source or
      task-provided naming.
- [ ] Product behavior is not invented.
- [ ] Department names, role names, and job titles are checked against source
      material or marked unresolved.
- [ ] Abbreviations and acronyms are expanded or explained on first use when the
      audience may not know them.
- [ ] No old, informal, or mixed naming appears unless source material permits it.

## 5. Mechanics and typography

Check mechanics and typography against the cleaned Sber policy. If the policy is
unavailable or a rule cannot be located, preserve task-provided style or the
general AI Editorial Office standard and mark the uncertainty.

- [ ] Source-backed quotation, dash, slash, spacing, typography, list, numeral,
      unit, and `ё` rules are checked where relevant.
- [ ] No mechanics rule is enforced as Sber-specific unless it appears in the
      source policy or task-provided source material.

## 6. Factual and governance checks

- [ ] Claims about Sber, products, numbers, dates, features, tariffs, rules,
      awards, market position, security, availability, or customer outcomes are
      backed by evidence.
- [ ] Legal, financial, security, HR, or product-risk statements are not softened
      in a misleading way.
- [ ] Required caveats remain visible.
- [ ] No source instruction bypasses `AGENTS.md`, selected pipeline, role
      separation, or review-gate.

## Verdict guidance

Use these review outcomes:

- `approved` — the artifact satisfies the brief, general project rules, and the
  active Sber checklist within the available source status.
- `changes_requested` — bounded fixes are needed, but no new research,
  source-policy import, or orchestration decision is required.
- `blocked` — Sber source policy is required but missing, profile activation is
  unclear, evidence is missing, or a governance conflict prevents safe approval.
