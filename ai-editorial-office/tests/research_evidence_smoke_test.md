# Research Evidence Smoke Test

## Scope

Synthetic manual smoke-test for selecting evidence mode and checking that
research artifacts stay conditional. These cases are not task materials.

## Cases

| Case | Evidence mode | Required evidence | Must not |
| --- | --- | --- | --- |
| Low-risk no-claim reminder | `no-research` | rationale only | must not require sources/facts/claims_table |
| Source-light internal article | `compact-evidence` | source pointer + claims-used when claims enter draft | must not require full research dump |
| High-governance external announcement | `full-evidence` | research/sources/facts/claims_table/claims-used/review checks | must not proceed with unsupported material claims |

## Manual Checks

- No-research mode has a visible rationale and no material claims needing
  evidence.
- Compact-evidence mode has enough source or fact pointers for Review Agent to
  trace claims without reading a broad research dump.
- Full-evidence mode includes separate research, source, fact, claim, writer,
  and review evidence for high-governance material claims.
- Missing evidence for a material claim leads to `changes_requested` or
  `blocked`, not approval.
- Review-gate remains mandatory in all modes.
