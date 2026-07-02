# Framework Architecture

## Design Goals

Studio Audit Framework must be:

- repeatable across audit cycles;
- independent from current Studio implementation details;
- grounded in the Knowledge Base;
- evidence-based rather than opinion-based;
- able to expose strengths, risks, technical debt, organizational debt, and
  knowledge gaps;
- explicit about applicability limits and unsupported areas.

## Core Components

| Component | Purpose | Main file |
| --- | --- | --- |
| Audit scope model | Defines the Studio as a sociotechnical production system | `02-audit-areas.md` |
| Criteria catalog | Defines what is checked and why | `03-assessment-criteria.md` |
| Maturity model | Defines criterion, area, and whole-Studio maturity | `04-maturity-model.md` |
| Evidence model | Defines admissible evidence and confidence | `05-evidence-collection-rules.md` |
| Priority model | Classifies findings by risk and action urgency | `04-maturity-model.md` |
| Report model | Defines future Audit Report structure | `06-audit-report-rules.md` |
| KB traceability model | Proves criteria are KB-grounded | `07-kb-traceability.md` |
| KB gap model | Records missing knowledge without inventing criteria | `08-kb-gaps.md` |

## Audit Workflow

```text
scope and independence
  -> KB freshness check
  -> criterion applicability selection
  -> evidence request and collection
  -> criterion scoring
  -> area maturity synthesis
  -> whole-Studio maturity synthesis
  -> priority classification
  -> Audit Report drafting
  -> evidence and KB traceability review
```

## Auditor Roles

The Framework defines audit responsibilities, not new Studio production roles.

| Audit responsibility | Purpose |
| --- | --- |
| Lead auditor | Maintains scope, independence, scoring consistency, and report integrity |
| Evidence collector | Collects artifacts, logs, documents, and interview notes without scoring alone |
| Domain reviewer | Reviews criteria in a specialized domain when expertise is needed |
| KB traceability reviewer | Checks that criteria and findings cite KB records correctly |

If future Studio rules canonicalize Validator, Historian, Product Analyst, or
other roles, future Framework revisions may map audit responsibilities to those
roles. Current KB reserves those roles but does not canonicalize them.

## Independence Rules

An auditor should not be the sole scorer for an area they directly designed,
implemented, or recently approved. When independence cannot be achieved, the
Audit Report must mark the affected findings as independence-limited.

Human review must be meaningful: reviewers need access to the evidence,
criteria, scoring rules, and enough time to challenge conclusions.

KB basis:

- `pattern-human-ai-checkpoints`
- `anti-pattern-human-rubber-stamp-ai`
- `principle-autonomy-with-guardrails`

## Criterion Lifecycle

Criteria can have these states:

| State | Meaning |
| --- | --- |
| `active` | Supported by KB and available for scoring |
| `applicability-limited` | Supported by KB but only in certain contexts |
| `gap-only` | KB is insufficient; record as knowledge gap, do not score |
| `deprecated` | Replaced by later Framework version or KB update |

Criterion state is not the same as KB record lifecycle status. KB record status
describes current application inside AI Software Studio; criterion state
describes whether this Framework can use the knowledge for audit methodology.

## KB Support Levels

| Level | Meaning | Scoring rule |
| --- | --- | --- |
| `direct` | KB directly supports the criterion | May be scored |
| `supporting` | KB supports part of the criterion | May be scored if the unsupported portion is removed or limited |
| `analogical` | KB case study or adjacent discipline supports an analogy | May be used as context; scoring must be conservative |
| `insufficient` | KB does not support the criterion | Do not score; record gap |

## Framework Governance

Before each audit cycle:

1. Confirm KB freshness for records used by active criteria.
2. Re-check records marked Evolving, Under Evaluation, or requiring quarterly
   refresh.
3. Confirm no new KB records supersede existing criteria.
4. Move unsupported candidate criteria to the KB gap register.
5. Record any Framework changes as methodology changes, not audit findings.

KB basis:

- `schema.md`
- `lifecycle.md`
- `coverage-model.md`
- `development-recommendations.md`

## Hard Boundaries

The Framework must not:

- score current Studio maturity inside methodology files;
- require tools that KB marks as rejected for current context;
- treat Accepted KB knowledge as already implemented;
- treat Under Evaluation knowledge as validated;
- turn external source IDs into direct citations without KB review;
- use one metric as total Studio maturity.

