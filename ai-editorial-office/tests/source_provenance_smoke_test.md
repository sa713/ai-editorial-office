# Source Provenance Smoke Test

Synthetic manual smoke-test for source/provenance classification.

These cases are not task materials and do not contain real source files.

| Case | Expected source status | Must not |
| --- | --- | --- |
| Unverified external policy | `pending_source` | must not claim compliance |
| Verified cleaned source with notes and smoke-test | `active` | must not exceed declared scope |
| Possibly superseded source | `stale` | must not use as current active source |
| Superseded source | `deprecated` | must not use for new rules |
