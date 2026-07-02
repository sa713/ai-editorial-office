# Manifest freshness decisions

## Decisions implemented

- Added compact freshness block:
  - `Last updated by`;
  - `Last updated stage`;
  - `Latest artifact changes`;
  - `Known stale risk`.
- Freshness exists to tell the next role whether manifest can be trusted for restart.
- Freshness block must stay operational and short.
- Stale/conflicting state response is explicit: stop production work and route to Chief Editor.
- Conflict summary and smallest repair needed are short fields, not an investigation log.

## Decisions intentionally not implemented

- No automatic validator.
- No audit log.
- No timestamp requirements beyond existing placeholder style.
- No event store.
- No full artifact history inside manifest.
- No status history duplication.

## Boundary

Freshness should help restart. If a note explains how the task got here in detail, it belongs in `status.md`, handoff, orchestration, or final decision, not in the manifest.
