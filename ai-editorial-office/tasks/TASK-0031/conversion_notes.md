# Conversion Notes

## Source PDF

- Source file: `Редакционная политика 05.2026.pdf`
- Candidate selection: exactly one PDF was present in `tasks/TASK-0031/`, so it
  was used.
- Source boundary: this is an external Sber document. It was not added to
  `/kb`, not treated as AI-editorial-office policy, and the original PDF was
  not modified.

## Extraction Method

- Ordinary text extraction was checked first with `pypdf`.
- Result: the PDF has an incomplete extractable text layer. `pypdf` detected 35
  pages, but ordinary extraction mostly returned the repeated date/header,
  bullets, and a few symbols rather than the full page text.
- OCR was used: yes, because ordinary extraction was incomplete.
- OCR workflow:
  - split the PDF into 35 single-page PDFs with `pypdf 6.10.0`;
  - rendered each page to high-resolution PNG with macOS Quick Look
    (`qlmanage -t -s 2400`);
  - recognized text with Apple Vision OCR (`VNRecognizeTextRequest`) using
    Russian and English recognition languages;
  - kept a page-level OCR report in temporary working files during conversion.
- No external network download or package installation was used.

## Technical Cleanup Applied

- Removed repeated page headers: `Редакция от 14.05.2026`.
- Removed temporary page delimiters from the final Markdown.
- Converted visible numbered sections into Markdown headings.
- Preserved the table of contents and body section order.
- Corrected obvious OCR artifacts where the source/context was clear, including:
  `om` -> `от`, `no` -> `по`, `muna` -> `типа`, Cyrillic/Latin OCR swaps,
  broken `AI`, `GPT4o`, `№`, `QR-код`, and selected emoji artifacts.
- After post-delivery feedback, reprocessed comparison examples with
  word-level OCR coordinates so `Нет` / `Да` and `Хороший пример` / `Хороший
  антипример` columns are separated into readable Markdown blocks.
- Did not summarize, shorten, paraphrase, or convert the Sber document into
  local editorial rules.

## Tables, Images, and Layout

- Many pages use side-by-side `Нет` / `Да` comparison tables.
- These comparison blocks are represented as separate readable Markdown blocks
  under `**Нет**` and `**Да**` markers rather than forced into Markdown tables.
- The `1.21` example block is represented as separate `**Хороший пример**` and
  `**Хороший антипример**` blocks.
- Complex reference tables were also preserved in readable text form:
  - `3.7. Сложные названия и исключения`;
  - `4.15. Сложные слова`;
  - `5. Сверяемся`;
  - `6. Редакция`.
- Decorative backgrounds, color coding, and visual highlighting were not
  reproduced in Markdown.

## Known Limitations

- The result is OCR-based because the source PDF did not expose complete text
  for ordinary extraction.
- All 35 pages were processed, but residual OCR inaccuracies may remain,
  especially in rare symbols, emoji, mixed Latin/Cyrillic tokens, and complex
  reference tables.
- For legal, brand, or publication-critical use, verify disputed wording against
  the original PDF.
