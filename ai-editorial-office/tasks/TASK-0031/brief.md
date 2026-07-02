# TASK-0031 Brief

## Goal

Technically convert the external Sber editorial policy PDF in this task folder
into a usable Markdown text source.

## Source Boundary

- Source PDF: `Редакционная политика 05.2026.pdf`.
- The PDF is an external source.
- Do not turn the Sber policy into AI-editorial-office rules.
- Do not add the source or its converted content to `/kb`.
- Do not change the original PDF.

## Required Output

- `sber-editorial-policy.md`
- `conversion_notes.md`
- `review.md`
- updated `status.md`

## Conversion Rules

- Do not summarize, shorten, paraphrase, or rewrite the source.
- Preserve source meaning, wording, section order, headings, numbering, lists,
  examples, notes, disclaimers, important footnotes, service blocks, and tables.
- Only technical cleanup is allowed: broken line wraps, duplicate spaces,
  repeated headers/footers, page numbers, and PDF extraction artifacts.
- Use OCR only if ordinary text extraction fails or is incomplete.
- If a table cannot be safely converted to Markdown, keep it readable as text
  and note the limitation in `conversion_notes.md`.
