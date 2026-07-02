# Writer Notes

Task ID: `TASK-0001`

Owner: `writer_agent`

## writing decisions

- Used a practical article structure: thesis, use cases, limitations, team rules, conclusion.
- Kept the central frame: AI assists editorial work but does not replace editorial responsibility.
- Used generic examples only, because no internal examples or policies were supplied.
- Avoided vendor names and product comparisons.
- Kept the draft as a reviewable article draft, not final copy.

## assumptions

| Assumption | Basis | Risk | Handling |
| --- | --- | --- | --- |
| Generic workflow examples are acceptable. | Chief Editor handoff says generic examples only. | Draft may feel less specific to the organization. | Examples are framed generically and do not imply internal practice. |
| The article should discuss AI tools generally. | Brief asks for a practical internal article, not a vendor comparison. | Low. | No vendor-specific recommendations included. |
| Approximately 4000 characters allows a compact sectioned article. | Brief requests about 4000 characters. | Low. | Draft is concise and reviewable; exact length can be adjusted later. |

## tone choices

- Calm, practical, direct.
- No hype openings or broad claims that AI transforms the whole field.
- No replacement rhetoric.
- No fake certainty around productivity or quality outcomes.
- Caveats are placed near the claims they limit.

## structure choices

- The opening states the thesis directly instead of using a broad AI introduction.
- Use cases are organized around the requested scope: drafting, structure checks, adaptation, weak-spot detection.
- Limitations and responsibility appear before the conclusion so the article does not read as promotional.
- The ending returns to process and accountability rather than inspiration.

## caveats used

| Claim | Caveat in draft |
| --- | --- |
| C1 | AI can help with a first draft, but does not guarantee time savings and depends on brief quality/context. |
| C3 | AI can suggest structure options and questions, but does not choose the correct structure. |
| C4 | AI can surface possible weak spots, but does not find every problem. |
| C7 | Shared rules are recommended as a practical governance step, not claimed as an internal policy or universal proof. |

## intentionally excluded unsafe claims

| Claim ID | Excluded claim | Reason |
| --- | --- | --- |
| C8 | AI improves editorial quality by itself. | Unsupported; quality depends on human judgment, context, and review. |
| C9 | AI can replace editors or UX writers. | Unsupported and contradicts brief/governance model. |
| C10 | AI always saves time for editorial teams. | Unsupported; no audience-specific productivity evidence. |
| C11 | Organization-specific examples or policies exist. | No internal materials were supplied. |

## weak spots draft

- The draft is intentionally generic; it may need internal examples later if the organization wants a more specific portal article.
- The article avoids statistics; if stakeholders expect numbers, a new research pass is required.
- The UX examples are generic and should be checked for fit if adapted to a real product surface.
- The draft may need tightening or expansion after review depending on the target portal style.

## where review should pay extra attention

- Check that no sentence implies guaranteed productivity, quality improvement, or complete weak-spot detection.
- Check that no generic example reads as an internal practice.
- Check that all claims used in the article match `claims_table.md`.
- Check that the tone remains practical and non-hype.
- Check whether the draft length is close enough to the requested approximately 4000 characters for the internal portal.

## unresolved issues

| Issue | Blocks review | Recommended handling |
| --- | --- | --- |
| Internal policies and examples remain unavailable. | `no` | Review as generic draft; request user material only if specificity becomes required. |
| Human approval requirement remains unknown. | `no` | Reassess after review/finalization. |

## recommended next step

Route to `review_agent` for independent review. Review must not be bypassed.
