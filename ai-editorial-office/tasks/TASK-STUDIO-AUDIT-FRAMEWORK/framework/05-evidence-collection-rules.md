# Evidence Collection Rules

## Evidence Principle

Audit conclusions must be based on saved, inspectable evidence. Interviews and
assertions may provide context, but they cannot by themselves prove maturity
above `M1`.

KB basis:

- `pattern-provenance-linked-knowledge`
- `principle-knowledge-close-to-work`
- `anti-pattern-automation-without-observability`
- `anti-pattern-human-rubber-stamp-ai`

## Evidence Classes

| Class | Examples | Typical confidence |
| --- | --- | --- |
| Governing documents | role specs, policies, pipeline docs, decision records, standards mapping | `E2` if current, `E3` if usage is shown |
| Work artifacts | manifests, status logs, review files, final decisions, handoffs, source registers, claim tables | `E2-E3` |
| System evidence | CI logs, test results, eval results, release records, observability dashboards, incident logs | `E3-E4` |
| Product evidence | discovery notes, opportunity maps, experiment results, customer/user evidence, roadmap rationale | `E2-E4` |
| Knowledge evidence | KB records, application register, coverage snapshots, refresh logs, provenance links | `E2-E4` |
| Human evidence | interview notes, approval records, reviewer notes, calibration notes | `E1-E3` depending on corroboration |

## Admissible Sources

Future auditors may use:

- repository files;
- task-local artifacts;
- KB records and registers;
- test/eval outputs;
- CI or automation logs;
- architecture/decision records;
- product discovery artifacts;
- operational/incident records;
- approved interview notes;
- approval evidence;
- metric definitions and trend data.

## Non-Admissible as Sole Proof

These may inform questions but cannot independently prove maturity:

- memory of past work;
- unrecorded verbal claims;
- screenshots without source/context;
- demo success without repeatability;
- tool adoption claims without usage evidence;
- checklists completed after the relevant decision;
- metrics without definitions and decision context.

## Evidence Collection Steps

1. Freeze audit scope and criterion applicability.
2. Request evidence by area and criterion ID.
3. Record evidence source, owner, date, freshness, and access path.
4. Classify each item as existence, usage, effectiveness, freshness,
   ownership, or exception evidence.
5. Check evidence against KB-linked criterion questions.
6. Record missing, stale, contradictory, or insufficient evidence.
7. Preserve evidence references in the Audit Report.

## Evidence Freshness

Each evidence item must be classified:

| Freshness | Meaning |
| --- | --- |
| `current` | Still represents current practice or active artifact. |
| `recent` | Useful but may need corroboration. |
| `outdated` | Historical only; cannot prove current maturity. |
| `unknown` | Date or current relevance is unclear. |

Records with quarterly or semiannual KB refresh requirements require explicit
freshness checks before scoring.

## Evidence Confidence Rules

- A documented rule with no usage evidence normally supports `E2`.
- A documented rule plus examples of real use supports `E3`.
- Real use plus outcome/trend/improvement evidence supports `E4`.
- Contradictory evidence lowers confidence unless resolved.
- Missing evidence should be reported as missing evidence, not interpreted as
  automatic failure unless the criterion requires that evidence to be auditable.

## Sampling Rules

Use sampling when evidence volume is large.

Minimum sample design must state:

- sample period;
- selection method;
- included/excluded artifact types;
- reason sample is representative enough;
- known sampling limitations.

High-risk areas require broader samples or targeted edge-case samples.

## Interview Rules

Interviews may clarify:

- intent;
- ownership;
- decision context;
- undocumented edge cases;
- interpretation of contradictory evidence.

Interview claims must be corroborated by artifacts before they support maturity
above `M1`.

## Contradiction Handling

When evidence conflicts:

1. Identify the conflict precisely.
2. Prefer current canonical artifacts over stale or informal claims.
3. Check whether the conflict is expected exception handling or uncontrolled
   drift.
4. Record uncertainty.
5. Do not score above `M2` if contradiction affects criterion validity and is
   unresolved.

## Evidence Register Fields

Every future audit should maintain an evidence register with:

- evidence ID;
- area and criterion ID;
- source path/link;
- owner or source system;
- collection date;
- freshness;
- evidence class;
- confidence level;
- relevant excerpt or summary;
- limitation;
- auditor who inspected it.

## Privacy and Access

The Framework does not define a full privacy program. Future audits must still
avoid collecting sensitive, irrelevant, or low-value context merely because it
is available.

KB basis:

- `practice-context-and-memory-management`

