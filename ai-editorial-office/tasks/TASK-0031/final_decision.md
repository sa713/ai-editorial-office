# Final Decision

## Decision

Finalize TASK-0031.

## Basis

- `sber-editorial-policy.md` was created from the selected source PDF.
- `conversion_notes.md` documents the extraction method, OCR use, technical
  cleanup, and limitations.
- `review.md` approved the conversion with documented OCR/layout limitations.
- The original PDF was not modified.
- No content was added to `/kb`.

## Final State

The converted Markdown is accepted as a task-local text source. For
publication-critical, legal, or brand-critical use, disputed wording should be
checked against the original PDF because the final artifact is OCR-based.

## Post-Delivery Revision

User feedback after delivery identified unreadable mixed two-column example
blocks. A bounded revision reparsed comparison blocks with word-level OCR
coordinates and refreshed `conversion_notes.md`, `review.md`, and `status.md`.
