# Facts And Source-Backed Requirements

## Confirmed From Sources

1. The section is intended for employees and supports non-formal interaction
   around hobbies, travel, activities, and communities. Sources: S1, S2, S3.
2. The dashboard has three connected functional modules: travel map, hobbies and
   interests, and event calendar. Source: S1.
3. The dashboard should help employees find colleagues with similar interests,
   exchange experience, find company for activities or trips, and discover
   events. Sources: S1, S2, S3.
4. HR, managers, and internal communications need aggregated analytics about
   interests, events, registrations, communities, engagement, and dashboard use.
   Sources: S1, S2, S3.
5. Data comes from HR/profile data and employee-created content. Source: S1.
6. Employee-created public content requires moderation before publication.
   Sources: S1, S2, S3.
7. Employees must be able to manage visibility of their profile/dashboard data
   and individual objects such as trips, dates, interests, event participation,
   and marks. Sources: S1, S3.
8. Hidden data must not appear in public lists, filters, search results, cards,
   or person-level analytics. Source: S1.
9. The travel module uses city as the main display unit and supports past trips,
   future plans, marks "хочу туда", "могу посоветовать", "ищу компанию",
   advice, routes, comments, and filters. Source: S1.
10. The hobbies module supports interest categories, free-text interests,
    employee skill/engagement level, finding like-minded colleagues, groups,
    subscriptions, recommendations, and links to events. Sources: S1, S3.
11. The event calendar supports event viewing, filtering, search, event cards,
    registration/cancellation, reminders, calendar integration, recurring
    events, employee-proposed events, and event moderation. Sources: S1, S2.
12. Event organizers/authors may need to create drafts, edit events, manage
    participants, communicate changes, track attendance, copy events, and see
    event statistics. Source: S2.
13. Administrators manage categories/tags/catalogs, visibility defaults or
    global settings, and possibly challenge templates and role/permission
    settings. Sources: S1, S2, S3.
14. ZOZH challenges and achievement sharing are desired but partially uncertain:
    one draft suggests they may happen in the module or in Telegram. Source: S3.
15. Success metrics are proposed around profile fill rate, event participation,
    author-created activities, satisfaction, repeat participation, new
    interests, and ZOZH activity creation. Sources: S2, S3.

## Contradictions And Ambiguities

1. Organization naming is inconsistent: S1 and S2 use "УЭК"; S3 mentions
   "Банк" and "СберЧат". The final document should avoid overcommitting to a
   specific communication channel unless confirmed.
2. Role boundaries are inconsistent: S1 separates moderator and administrator;
   S2 gives moderator rights to manage roles and categories; S3 makes
   administrator responsible for moderating new hobbies. The final document
   should separate the roles and ask who owns final role boundaries.
3. S1 says detailed nonfunctional requirements are out of scope, while the user
   explicitly requires a nonfunctional requirements section. The final document
   should include business-level nonfunctional requirements and avoid technical
   architecture depth.
4. S1 says HR data is shown automatically unless hidden, while no consent or
   legal basis flow is described. This must remain an open question.
5. S3 proposes visibility "показывать всем / только контактам / скрыть"; S1
   mainly describes visible/hidden and object-level visibility. "Только
   контактам" needs confirmation.
6. S2 includes export to Excel, manual participant management, and attendance
   tracking. These are useful organizer needs, but privacy and access limits are
   not defined.
7. S2 includes events requiring budget or high responsibility, but the approval
   process and owner are not defined.
8. Some metrics in S2 are placeholders without target values; only the 70%
   profile-fill metric in S3 is explicit.

## Do-Not-Say Constraints

- Do not state that detailed API, database, SSO, or integration design is in
  scope.
- Do not state that legal consent rules are resolved.
- Do not state that SberChat, Telegram, Google Calendar, Outlook, or any channel
  is mandatory; use business-level wording unless a source-supported caveat is
  included.
- Do not let analytics reveal a specific employee's hidden choice.
- Do not merge moderator and administrator into one role without flagging the
  role-boundary question.

