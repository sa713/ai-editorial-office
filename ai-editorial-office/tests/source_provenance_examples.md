# Source Provenance Synthetic Examples

These examples are synthetic. They are not task materials and do not contain
real client, source, policy, or document data.

## Purpose

Check source status classification without treating cleaned Markdown as a
magically verified source.

## Examples

### Example 1 - Pending source

Scenario:

> An external policy is expected, but the source file has not been verified and
> no source notes exist yet.

Expected source status: `pending_source`

Why:

- The source may exist, but it is not verified enough for rule use.
- Missing rules cannot be invented during cleaning or setup.
- A client profile must not be activated as source-backed from unverified
  material.

Must not:

- claim policy compliance;
- invent missing rules;
- activate client profile from unverified source.

### Example 2 - Active source

Scenario:

> Cleaned Markdown exists, source notes are complete, omissions are recorded,
> and the source import smoke-test has passed.

Expected source status: `active`

Why:

- Provenance is recorded.
- The cleaned source has defined scope and usage rules.
- The smoke-test confirms that missing rules were not invented.

Allowed:

- rules or profiles may use it within declared scope;
- compliance claims are allowed only if source notes say yes.

Must not:

- exceed declared source scope;
- treat the source as global editorial policy.

### Example 3 - Stale source

Scenario:

> Source date is old, a newer version may exist, or a review flags possible
> supersession.

Expected source status: `stale`

Why:

- The source may still be useful for comparison, but not for current compliance
  claims without review.

Must not:

- use as active;
- claim current compliance.

### Example 4 - Deprecated source

Scenario:

> Source is explicitly superseded by another policy or retired by the owner.

Expected source status: `deprecated`

Why:

- Deprecated material must not define new rules.
- It may remain useful only to explain history or compare changes.

Allowed only for:

- historical comparison.

Must not:

- use for new work;
- create new profile rules from it.
