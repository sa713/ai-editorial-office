# Recommendations for the First Audit

This guidance prepares the first audit. It does not perform it.

## First-Audit Objectives

The first audit should establish:

- which Framework criteria are applicable;
- what evidence exists;
- which areas can be scored confidently;
- which KB gaps block scoring;
- where maturity model calibration is needed.

It should not attempt to optimize the Studio during evidence collection.

## Preparation Sequence

1. Freeze Framework version and KB snapshot.
2. Re-check KB freshness for Evolving, quarterly, and semiannual records.
3. Confirm audit scope and exclusions.
4. Confirm auditor independence and conflicts.
5. Select applicable criteria.
6. Prepare an evidence request by criterion ID.
7. Define sampling windows and evidence classes.
8. Run a scoring calibration pass on 3-5 criteria before full scoring.
9. Complete evidence collection.
10. Score criteria, synthesize areas, and draft the Audit Report.

## Recommended First-Audit Scope

Start broad but shallow:

- include all 10 audit areas;
- score all criteria that have direct KB support and accessible evidence;
- mark unsupported/gap-only criteria separately;
- avoid deep control-level scoring where KB lacks local control mapping.

This creates a baseline without pretending precision the KB cannot support.

## Evidence Request Shape

Ask for evidence by area:

- GOV: role/authority/governance docs, review gates, exception records.
- KNO: KB records, source registers, application register, task-local evidence,
  refresh records.
- AI: agent workflow descriptions, tool permissions, evals, logs, human review
  evidence.
- QUA: review artifacts, checklists, test/eval records, quality criteria.
- DEL: delivery records, pipeline/test logs, incident or failure-learning
  records, reliability indicators.
- PLA: golden paths, templates, capability ownership, support/adoption evidence.
- PRO: discovery artifacts, outcome maps, opportunity/solution/experiment
  evidence.
- SEC: security/AI risk reviews, control mapping, approval evidence.
- MET: metric definitions, dashboards, retrospectives, improvement follow-up.
- ARC: architecture views, decision records, documentation map.

## Scoring Calibration

Before scoring all criteria, the audit team should jointly score:

- one governance criterion;
- one knowledge/provenance criterion;
- one AI-agent criterion;
- one evidence-heavy criterion;
- one gap-limited criterion.

The goal is to align interpretation of `M0-M5`, `E0-E4`, priority, and KB
support levels.

## First-Audit Cautions

- Do not convert KB gaps into process-change recommendations.
- Do not require an internal developer portal; KB rejects it for current
  context unless multi-user platform needs appear.
- Do not require Product Analyst, Validator, Historian, BRD, or ADR artifacts
  as current canonical objects.
- Do not treat DORA, SPACE, ISO, NIST, or platform maturity models as checklists
  to maximize.
- Do not average all criteria into one score without caps and narrative.
- Do not accept human approval as evidence unless the reviewer had criteria,
  context, and time.

## Expected First-Audit Outputs

The first audit should produce:

- Audit Report using `06-audit-report-rules.md`;
- evidence register;
- criterion score table;
- area maturity profile;
- priority register;
- KB traceability appendix;
- KB gap appendix;
- calibration notes;
- limitations statement.

It should not produce:

- Codex tasks;
- BRD;
- implementation roadmap;
- unapproved Studio process changes.

