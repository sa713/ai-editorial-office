# Audit Report Rules

This file defines the structure of future Audit Reports. It does not fill a
report and does not audit the current Studio.

## Report Principles

A future Audit Report must be:

- evidence-backed;
- criterion-linked;
- KB-traceable;
- explicit about scope and limits;
- clear about priority;
- careful not to turn KB gaps into Studio failures.

## Required Report Structure

1. Title and audit metadata.
2. Executive summary.
3. Scope and exclusions.
4. Independence statement.
5. Methodology used.
6. Evidence inventory summary.
7. KB freshness and traceability summary.
8. Maturity profile by area.
9. Criterion-level results.
10. Priority register.
11. Strengths and risks.
12. Technical and organizational debt themes.
13. KB gaps discovered during the audit.
14. Limitations and confidence.
15. Appendices.

## Audit Metadata

Required fields:

- audit ID;
- audit period;
- auditor(s);
- audited Studio version/scope;
- Framework version;
- KB snapshot/version/date;
- evidence collection window;
- report status.

## Scope and Exclusions

Must state:

- included systems, workflows, artifacts, roles, and time period;
- excluded areas;
- reason for each exclusion;
- whether exclusions affect maturity interpretation.

## Independence Statement

Must state:

- who performed the audit;
- relationship to audited work;
- conflicts of interest;
- areas with independence limitations;
- mitigation used.

## Evidence Inventory Summary

Must summarize:

- number of evidence items;
- evidence classes;
- freshness distribution;
- confidence distribution;
- inaccessible or missing evidence;
- sampling method.

## Criterion Result Format

Each criterion result must include:

- criterion ID and title;
- applicability decision;
- KB support level;
- evidence IDs;
- maturity level;
- evidence confidence;
- finding summary;
- conformance signs;
- nonconformance signs;
- priority;
- limitations;
- recommended audit follow-up, if any.

Do not include implementation tasks. If future action is needed, describe it as
an audit finding or follow-up question, not as a Codex task or BRD.

## Area Summary Format

Each area summary must include:

- area maturity;
- evidence confidence;
- strongest mature capabilities;
- most important risks;
- critical/important findings;
- KB gaps affecting the area;
- applicability limits.

## Priority Register

The priority register must include:

| Field | Required |
| --- | --- |
| Finding ID | yes |
| Area / Criterion | yes |
| Priority | yes |
| Evidence IDs | yes |
| Risk statement | yes |
| Maturity effect | yes |
| Owner for response | optional, only if audit scope includes response planning |
| Status | optional, for follow-up audits |

## Maturity Profile

The report should show:

- criterion ratings;
- area ratings;
- whole-Studio maturity synthesis;
- evidence confidence;
- severity caps applied.

It must not present a single overall score without the area profile and caps.

## KB Traceability Appendix

Must list:

- KB records used;
- records excluded and why;
- records stale or requiring refresh;
- criteria with direct/supporting/analogical support;
- gap-only candidate criteria.

## KB Gap Appendix

Must distinguish:

- methodology gaps found while applying the Framework;
- KB gaps already known before the audit;
- audit evidence gaps caused by inaccessible or missing Studio artifacts.

Do not label a KB gap as a Studio nonconformance unless the criterion itself is
active and applicable.

## Language Rules

Use:

- "Evidence indicates..."
- "No admissible evidence was provided..."
- "KB support is insufficient to score..."
- "This criterion is not applicable because..."

Avoid:

- "The Studio obviously..."
- "Best practice requires..." without KB link;
- "must implement..." when the Framework only found a gap;
- prescriptive tasks or BRD language.

