# Normalization Check

## test metadata

- Test ID: P1.5-03
- Task ID: TASK-P15-03-EXTERNAL-SOURCE-RAW-BRIEF
- Role applied: intake_agent
- Rule tested: Raw Brief Normalization
- Raw request type: external-source request
- External source opened: no
- Research performed: no
- Explanation/summary created: no
- Production files changed: no

## raw request

```text
Посмотри сайт roadmap.sh и разберись что такое vibe coding.

Коротко объясни суть документа.
```

## task signal

- Requested action: look at roadmap.sh.
- Requested action: understand what "vibe coding" is.
- Requested output: short explanation of the document's essence.
- Source cue: roadmap.sh external site.
- Source dependency: output depends on external source review.

## background context

- None supplied beyond the user's desire to understand a source/document.

## noise

- None. The request is short and source-dependent, not noisy.

## confirmed

- The user names roadmap.sh as the source area.
- The user asks about "vibe coding".
- The user wants a short explanation of the document's essence.
- No exact page URL is provided.
- The source has not been opened or reviewed in this test.

## inferred

- The future task is source-bound and likely requires research before writing.
- The final output is likely explanatory rather than promotional or creative.
- The exact document cannot be safely identified from the normalized request
  alone.

## unknown

- What "vibe coding" means in the roadmap.sh source.
- What roadmap.sh says about the topic.
- Which exact page/document the user means.
- What sections the document contains.
- The author's position or framing.
- Which technologies, tools, examples, benefits, risks, or conclusions are
  discussed.
- Citation/link requirements.
- Intended audience beyond the user.
- Required length for "short".

## assumptions

- The future task should not use general memory or unsourced knowledge; it
  should use the named external source after source access is allowed.
- If the exact document cannot be identified from roadmap.sh, the next role
  should ask for a URL or constrain the search.
- No assumption is safe enough to explain source content.

## open questions

- What exact roadmap.sh URL or document should be reviewed?
- Is roadmap.sh the only allowed source?
- Should the future output include source links or citations?
- How short should the explanation be?
- Is the output for the user only or for publication/reuse?
- Should the future explanation focus on definition, practical use, critique,
  risks, or takeaways?

## source status

- Source status: `mentioned external source, not opened or reviewed`.
- Source materials present: none in the task folder.
- Active source: none.
- Source boundary: roadmap.sh is named, but no page content has been accessed.
- Required next source action: Chief Editor must route to research/source review
  or ask for the exact URL before any explanation is written.

## acceptance criteria

- Future explanation acceptance criteria: `unknown` beyond being short,
  source-bound, and based on roadmap.sh.
- Normalization acceptance criteria:
  - do not open the source;
  - do not research or summarize source content;
  - do not explain vibe coding;
  - do not invent roadmap.sh content, document structure, author position,
    technologies, tools, or conclusions;
  - mark source status explicitly.

## fantasy check

| Check | Result | Notes |
| --- | --- | --- |
| Invented vibe coding definition | pass | No definition was added. |
| Invented roadmap.sh content | pass | No source content was described. |
| Invented future research conclusions | pass | No conclusions were projected. |
| Invented document sections | pass | Sections remain unknown. |
| Invented author position | pass | Author stance remains unknown. |
| Invented technologies/tools | pass | No technologies or tools were named. |
| Treated source as active | pass | Source is explicitly not opened/reviewed. |
| Created summary or explanation | pass | Only brief/task definition and check were created. |

## editorial conclusion

passed

Raw Brief Normalization handled the external-source request correctly. It
captured the source dependency and future output request while refusing to
describe vibe coding, roadmap.sh content, document structure, author position,
technologies, tools, or conclusions before source review.
