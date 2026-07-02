# Studio Audit Framework

Version: v0.1 methodology draft
Status: methodology package, not an audit report
Source boundary: AI Software Studio Knowledge Base

## Purpose

Studio Audit Framework defines how to conduct an independent audit of AI
Software Studio maturity. It does not audit the current Studio and does not
contain findings about the current implementation.

Every criterion in this package must be either:

- explicitly supported by Knowledge Base records; or
- marked as a Knowledge Base gap and excluded from scoring until support exists.

## Package Contents

| File | Role |
| --- | --- |
| `00-executive-summary.md` | Executive summary and core principles |
| `01-framework-architecture.md` | Framework structure, roles, workflow, and governance |
| `02-audit-areas.md` | Audit area catalog with objects, goals, maturity signs, problem signs, and anti-patterns |
| `03-assessment-criteria.md` | Criterion catalog with rationale, KB links, questions, evidence, and conformance signals |
| `04-maturity-model.md` | Criterion, area, and whole-Studio maturity model |
| `05-evidence-collection-rules.md` | Evidence sources, confidence, sampling, and admissibility rules |
| `06-audit-report-rules.md` | Required structure of future Audit Reports |
| `07-kb-traceability.md` | How the Framework maps to Knowledge Base records and sections |
| `08-kb-gaps.md` | Knowledge gaps discovered while building the Framework |
| `09-first-audit-guidance.md` | Recommendations for preparing the first audit without performing it here |
| `10-internal-consistency-review.md` | Internal contradiction and constraint review of this Framework draft |

## Non-Goals

- Evaluate the current AI Software Studio.
- Produce current maturity scores.
- Produce a BRD.
- Propose Studio process changes.
- Write Codex implementation tasks.
- Treat external source IDs as freshly verified outside the KB.

## Canonical Use

Future auditors should start with this order:

1. Read `00-executive-summary.md`.
2. Confirm scope and independence using `01-framework-architecture.md`.
3. Select applicable areas from `02-audit-areas.md`.
4. Score criteria using `03-assessment-criteria.md`,
   `04-maturity-model.md`, and `05-evidence-collection-rules.md`.
5. Produce the future report using `06-audit-report-rules.md`.
6. Attach traceability and gaps using `07-kb-traceability.md` and
   `08-kb-gaps.md`.

