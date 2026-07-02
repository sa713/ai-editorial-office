# Maturity Model

## Why a Custom Model

The Framework uses a custom maturity model because the KB warns against:

- reducing production-system health to a single metric;
- ranking maturity without context;
- treating maturity level as an objective detached from need;
- mistaking tool adoption for capability.

KB basis:

- `principle-sociotechnical-production-system`
- `framework-space`
- `framework-dora-core`
- `framework-platform-maturity`
- `anti-pattern-single-metric-productivity`

## Criterion Maturity Levels

| Level | Name | Definition |
| --- | --- | --- |
| `M0` | Not evidenced | No admissible evidence, or only unsupported assertion. |
| `M1` | Ad hoc | Practice appears in isolated cases, depends on individual effort, and has weak repeatability. |
| `M2` | Defined | Expected state, ownership, and basic artifacts are documented, but usage/effectiveness evidence is limited. |
| `M3` | Operated | Practice is used in real work with traceable artifacts, role ownership, and exception handling. |
| `M4` | Measured | Practice has meaningful feedback signals, review evidence, trend or outcome data, and freshness control. |
| `M5` | Learning | Practice is continuously improved through evidence, retrospectives, evals, experiments, or governance updates. |

## Evidence Confidence

Maturity score is invalid without evidence confidence.

| Level | Meaning |
| --- | --- |
| `E0` | No evidence or inaccessible evidence |
| `E1` | Assertion only |
| `E2` | Artifact exists |
| `E3` | Artifact plus usage evidence |
| `E4` | Usage plus effectiveness, trend, or learning evidence |

Evidence confidence caps maturity:

- `E0` caps at `M0`.
- `E1` caps at `M1`.
- `E2` caps at `M2`.
- `E3` caps at `M3`.
- `E4` allows `M4` or `M5`.

## KB Support Confidence

Every criterion must include one KB support level:

| Support | Meaning | Effect |
| --- | --- | --- |
| `direct` | KB directly supports the criterion | Scorable |
| `supporting` | KB supports a narrower version | Scorable only after narrowing |
| `analogical` | KB supports via case study/adjacent domain | Scorable only with conservative interpretation |
| `insufficient` | KB does not support the criterion | Not scorable; record KB gap |

## Criterion Rating Record

Each scored criterion must record:

- criterion ID;
- applicability decision;
- KB support level;
- maturity level;
- evidence confidence;
- priority classification;
- evidence references;
- limitations;
- auditor notes.

## Area Maturity

Area maturity is synthesized from its criteria using these rules:

1. Score only applicable criteria.
2. Exclude `gap-only` criteria from numeric maturity, but report them as KB
   gaps.
3. Use the median criterion maturity as the starting point.
4. Cap the area at `M2` if any Critical finding remains unresolved.
5. Cap the area at `M3` if evidence confidence is mostly `E2` or lower.
6. Cap the area at `M3` if key ownership is unclear.
7. Allow `M5` only when improvement/learning evidence exists for the area, not
   only for isolated criteria.

Area maturity must include a short rationale. Do not report only a number.

## Whole-Studio Maturity

Whole-Studio maturity should be reported as:

- a profile across all areas;
- a short synthesis of systemic strengths and risks;
- a maturity band only when useful.

Recommended bands:

| Band | Meaning |
| --- | --- |
| `Fragmented` | Many critical capabilities are not evidenced or are ad hoc. |
| `Defined` | Important practices exist in documented form, but operation/effectiveness evidence is uneven. |
| `Operated` | Core practices run in real work with traceability and basic review. |
| `Measured` | Feedback, metrics, and evidence support management of key risks and outcomes. |
| `Learning` | The Studio demonstrates repeatable evidence-based improvement across areas. |

Whole-Studio maturity must not be a simple average. A Studio cannot be rated
above `Defined` if governance, evidence traceability, or AI-risk controls have
unresolved Critical findings.

## Priority Model

| Priority | Meaning | Examples |
| --- | --- | --- |
| `Critical` | Failure may make Studio work unsafe, unauditable, unreviewable, or materially misleading. | Unsafe AI autonomy, missing review evidence, security/AI risk blind spot, source-free criteria, false approval. |
| `Important` | Weakness materially harms repeatability, decision quality, delivery reliability, product learning, or maintainability. | Stale KB, unclear ownership, unmeasured golden path, missing incident learning. |
| `Improvement` | Maturity opportunity where current evidence is adequate for safe operation. | Better trend data, stronger documentation structure, richer discovery evidence. |
| `No Change Needed` | Expected state is met with adequate evidence and no material freshness concern. | Criterion passes with current evidence. |

## Severity Caps

- Any Critical finding in GOV, KNO, AI, SEC, or evidence traceability caps
  whole-Studio maturity at `Defined`.
- Any unauditable area caps that area at `M1`.
- Any criterion whose KB support is `insufficient` must not generate a maturity
  score.
- Any criterion based mainly on `analogical` support should not exceed `M3`
  unless future KB adds direct support.

## Reassessment Rules

Reassess maturity when:

- KB records change;
- source freshness expires;
- Studio object links change;
- new AI tools/models materially change agent behavior;
- critical incidents or major failures occur;
- governance roles or artifacts become canonical.

