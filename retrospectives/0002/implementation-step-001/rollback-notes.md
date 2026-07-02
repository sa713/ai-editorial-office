# Rollback notes

## What to rollback

Rollback only the `Reader-state boundaries` section added to:

- `editorial_knowledge/01_principles.md`

## How to rollback

Remove the section starting with:

```markdown
## Reader-state boundaries
```

through the final sentence:

```markdown
Reader-state edits must not hide rules, soften real obligations into suggestions, make optional actions sound required, or imply activity and social proof without evidence.
```

No other core file rollback is needed because no other core files were changed.

## Rollback triggers

Rollback or revise if this change starts to:

- blur governance;
- make mandatory actions sound optional;
- make optional actions sound mandatory;
- create vague behavioral language;
- trigger tone-policing comments;
- expand into broad editorial doctrine;
- cause future steps to add prompts, templates, or pipelines by default.

## Safer fallback

If the section feels too broad, replace it with only the honesty rule:

```text
Mandatory stays mandatory.
Optional stays optional.
Unknown stays unknown.
```
