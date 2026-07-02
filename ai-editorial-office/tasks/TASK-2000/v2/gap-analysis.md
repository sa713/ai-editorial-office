# Gap Analysis: Travel DOCX vs Current BRD

## Sources Checked

- `business-requirements.md`
- `БТ для путешествий.docx`

## Уже учтено

1. Purpose of the travel map.
   - The DOCX says employee travel experience should become a shared corporate
     asset and a reason for informal communication.
   - Already reflected in the BRD goal, summary, critical BRs, and travel-map
     user stories.

2. Past travel marks.
   - The DOCX describes marks in "Где были ранее" with country, city, and dates.
   - Already reflected through past trips, destination cards, dates visibility,
     and employee-added travel data.

3. Interactive map and country/city filtering.
   - The DOCX describes map viewing, scaling/moving by regions, and filtering by
     countries/cities.
   - Already reflected at business level through the travel map, countries,
     cities, direction cards, and filters. Detailed map interactions are UI
     design and do not need BRD expansion.

4. Moderation of travel content.
   - The DOCX says admin can moderate new marks and routes and hide/delete
     publications.
   - Already reflected as moderation of travel additions, routes, advice, and
     published user content.

5. Popular destinations and reports.
   - The DOCX mentions reports by popular destinations, map/profile fill rate,
     and informing colleagues about popular destinations.
   - Already reflected through aggregated analytics for popular travel
     directions and dashboard adoption. Push channel details are not included.

## Стоит добавить

1. Travel type and travel tags.
   - Why important: "пляжный", "горный", "экскурсионный" and similar travel
     types help employees find relevant travel experience, not just places.
   - Where to add: `Источники данных`, `Основные сущности раздела`, `US-05`.

2. Editing and deleting one's own travel marks.
   - Why important: employees need control over outdated or mistakenly added
     travel data; this supports trust and data freshness.
   - Where to add: `Основные пользовательские задачи`, role `Сотрудник`,
     `US-06`.

3. Admin-managed travel dictionaries.
   - Why important: if countries, cities, travel types, and tags are structured,
     someone must keep these lists usable for filtering and reporting.
   - Where to add: `Основные пользовательские задачи`, data sources,
     role `Администратор`, `US-15`.

## Не включать

1. Layer "Сейчас находится" with automatic detection from "Пульс".
   - Reason: current-location display is materially different from voluntary
     past/future travel sharing and can become employee location tracking. It
     conflicts with the BRD's product boundaries around monitoring and control.

2. Low-level map interactions: zooming, panning, moving across regions.
   - Reason: this is UI behavior, not business logic.

3. Push notifications or separate UI tiles for popular destinations.
   - Reason: channel and placement are implementation/product-design choices.
     The business need for popular-destination analytics is already covered.

4. Placeholder success metrics with unknown values.
   - Reason: the DOCX uses `?%` / `шт`; the BRD already states that target
     metric values require confirmation.

5. Employee management of global country/city/type/tag lists.
   - Reason: the DOCX phrases this under employee use cases, but global
     reference-data management is better treated as an administrator capability
     to avoid data-quality and moderation issues.

