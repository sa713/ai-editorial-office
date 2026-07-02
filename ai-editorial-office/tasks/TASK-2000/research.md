# Research Summary

## Research Scope

Read and consolidate the three source drafts in `TASK-2000`:

- `БТ дашборд хобби.md`
- `БТ календарь.md`
- `БТ хобби.md`

No external research was performed. The sources are treated as draft
requirements, not final policy.

## Main Synthesis

The requested section should be described as one employee-hobbies dashboard with
three connected modules:

- travel map;
- hobbies and interests;
- event calendar.

The main business value is to make employee interests visible enough for
colleagues to find each other, exchange experience, join activities, and form
communities, while keeping employees in control of what they disclose.

The dashboard should also give HR, managers, and internal communications
aggregated insight into interests, events, communities, and adoption. Analytics
must stay aggregated and must not reveal hidden individual choices.

## Key Source Additions To Preserve

- S1 contributes the full dashboard logic: modules, privacy, moderation,
  travel map, hobbies, calendar, analytics, out-of-scope boundaries, and open
  questions.
- S2 adds useful event-calendar details: event author/organizer rights,
  registration management, notifications, reviews, reporting, attendance, event
  statistics, copying events, and reports.
- S3 adds useful hobbies-module details: profile fill target, catalog tree,
  skill level, recommendations, messaging to colleagues, ZOZH challenges,
  achievement sharing, and calendar integration.

## Consolidation Decisions

1. Use one title: "Дашборд увлечений сотрудников".
2. Treat travel, hobbies, and calendar as modules of the same section, not as
   three separate products.
3. Separate roles into:
   - employee;
   - event organizer/author;
   - moderator;
   - administrator;
   - analytics user: HR, manager, internal communications.
4. Treat event organizer as an extended employee scenario rather than a separate
   access class unless the business owner confirms otherwise.
5. Keep "contacts-only visibility", SberChat/Telegram, legal consent,
   detailed data refresh rules, and approval for high-responsibility events as
   open questions.
6. Include business-level nonfunctional requirements because the user explicitly
   requested them, while excluding technical architecture and implementation
   details.

## Open Questions For Final Document

- Which organization/product terminology should be used: УЭК, Банк, Sber, or a
  neutral portal term?
- Is the travel map definitely in scope for "Дашборд увлечений сотрудников"?
- Who owns the interest/category catalog and final content disputes?
- What is the exact split between moderator and administrator rights?
- Is "visibility only for contacts" required, and what is a "contact" in this
  portal?
- What legal basis or consent model applies to HR/profile data shown in the
  dashboard?
- Which communication and calendar channels are allowed?
- Are ZOZH challenges and achievement feeds part of this module or external
  channels?
- Are Excel exports, manual participant changes, and attendance tracking allowed
  for event organizers?
- How should small groups be handled in analytics to avoid re-identification?

## Sufficiency For Writing

Research is sufficient to draft `business-requirements.md` because all three
source files were readable and the main contradictions can be handled through
conservative wording plus an explicit "Открытые вопросы" section.

