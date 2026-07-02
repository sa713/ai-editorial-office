# Handoff: Research Agent To Writer Agent

## From / To

- From role: `research_agent`
- To role: `writer_agent`
- Reason: all three source drafts were read and classified; writing can start.

## Artifacts Created

- `sources.md`
- `facts.md`
- `research.md`
- `claims_table.md`

## Key Guidance

- Use S1 as the base structure and S2/S3 as enrichment sources.
- Keep the final document self-contained and business-readable.
- Preserve the required 14-section structure from `brief.md`.
- Describe functionality through both roles and user stories.
- Do not merge moderator and administrator unless phrased as a possible local
  configuration or open question.
- Do not assert unresolved privacy, consent, channel, or analytics rules as
  confirmed.
- Include business-level nonfunctional requirements despite S1 listing detailed
  NFR as out of scope, because the user explicitly requested this section.

## Open Questions To Carry Forward

Carry unresolved source issues into the final document:

- naming: УЭК vs Банк/Sber-related wording;
- travel-map scope;
- role split between moderator and administrator;
- consent/legal basis for HR/profile data;
- "contacts-only" visibility;
- notification, calendar, chat, and Telegram channels;
- ZOZH challenge/achievement scope;
- organizer export/manual participant/attendance rights;
- small-group analytics privacy;
- ownership of catalog and disputed content decisions.

## Expected Output

- `outline.md`
- `business-requirements.md`
- `writer-notes.md`
- `claims-used.md`

## Stop Conditions

- Stop if writing requires new functionality not supported by sources.
- Stop if a requirement cannot be stated without deciding a legal, privacy, or
  HR policy question.

