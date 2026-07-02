# Writer Notes

## What Was Consolidated

- The complete dashboard draft was used as the base.
- Calendar-specific details from `БТ календарь.md` were folded into event
  calendar, organizer, registration, notification, feedback, and analytics
  sections.
- Hobby-specific details from `БТ хобби.md` were folded into profile interests,
  catalog, skill level, recommendations, ZOZH challenges, and metrics.

## Key Writing Choices

- The final document uses the neutral title "Дашборд увлечений сотрудников" to
  match the user request.
- The organization name is not hard-coded throughout the document because source
  naming conflicts between "УЭК", "Банк", and Sber-related channels.
- The event author is described as an organizer scenario that may become a
  separate access role if confirmed.
- Detailed NFR from engineering were not invented; the NFR section is limited to
  business-level requirements.
- ZOZH challenges are included, but progress/rating/achievement implementation
  is conditional and carried into open questions.

## Conscious Omissions

- UI mockups, button labels, microcopy, API, database, SSO, technical
  integrations, development plan, estimates, and support regulations.
- Exact metric targets where the source used placeholders.
- Mandatory SberChat, Telegram, Google Calendar, or Outlook support.
- Legal consent rules or personal-data basis, because the sources do not define
  them.

## Review Focus

- Check that no unsupported functionality is stated as confirmed.
- Check that role descriptions and user stories are aligned.
- Check that privacy and visibility rules are not weakened.
- Check that the final open questions include all source contradictions.

## Bounded Revision 2026-06-10

User requested three local changes to the accepted BRD:

- add product boundaries to prevent drift into a corporate social network;
- rewrite user-story statements through employee life situations without
  changing scenarios or acceptance criteria;
- add 5-7 critical business requirements that define the product foundation.

Changes made:

- Added `Границы продукта`.
- Added `Критически важные бизнес-требования` with seven BR items.
- Rewrote the statement line for all 16 user stories.
- Left acceptance criteria unchanged during this revision.
- Did not change goals, roles, data structure, privacy model, open questions, or
  unrelated business requirements.
