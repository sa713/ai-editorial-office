# Forbidden Patterns

## purpose

This file prevents generic AI writing drift. Use it during drafting, UX writing, review, and finalization.

Forbidden does not always mean the exact words can never appear. It means the pattern is not allowed when it adds filler, false confidence, manipulation, or unclear behavior.

## forbidden stylistic patterns

| pattern | why it is bad | preferred replacement behavior |
| --- | --- | --- |
| `в современном мире` / `in today's world` | Generic opening that adds no task-specific value. | Start with the actual subject, decision, or user problem. |
| `важно отметить` / `it is important to note` | Usually announces importance instead of proving it. | State the point directly, or remove it. |
| `следует понимать` / `it should be understood` | Patronizing and vague. | Name the concrete constraint or implication. |
| Generic AI intros | Waste space and signal template writing. | Begin from the brief, finding, recommendation, or task output. |
| Fake transitions such as `Moreover`, `Furthermore`, `In conclusion` without logical need | Creates flow without adding meaning. | Use headings, bullets, or direct continuation. |
| Decorative wording without information value | Makes text feel polished while reducing precision. | Keep only words that change meaning, action, or tone. |
| Fake empathy | Simulates care without helping the reader. | Acknowledge concrete user friction only when relevant. |
| Corporate motivational tone | Inflates simple work into slogans. | Use practical, grounded language. |

## forbidden structural patterns

| pattern | why it is bad | preferred replacement behavior |
| --- | --- | --- |
| Empty introductions | Delay the useful answer. | Lead with the answer, scope, or decision. |
| Empty conclusions | Repeat without adding action, risk, or decision. | End when the work is complete, or state the next required action. |
| Essay structure for operational artifacts | Makes agents search for instructions. | Use checklists, tables, and short rules. |
| Overlong context before decision | Hides the operational point. | Put the decision first, then evidence. |
| Mixing facts, assumptions, and recommendations | Breaks traceability. | Separate them under explicit labels. |
| Hidden reading path in instructions | Makes the reader reconstruct where to start and what to skip. | Name the route to action, safe skip points, or section purpose. |
| Mixed section roles | Turns one block into overview, action sequence, constraints, and troubleshooting at once. | Split or relabel sections by role when the mix increases rereading cost. |
| Repeated process explanation without new value | Forces rereading and hides the shortest successful path. | Keep necessary repetition only where it supports safety, role independence, or trust. |
| Forced linear reading for reference material | Makes role-specific or repeat use inefficient. | Add navigation, section labels, tables, or checklists when selective reading is needed. |
| Explanation that should be structure | Describes the system instead of helping the reader perform the action. | Convert the explanation into steps, decision points, tables, or navigation when that reduces action friction. |
| Inherited purpose as hook | Uses the general purpose of a format, rubric, event, magazine, or product instead of the specific reason this material matters. | Return to the current topic, release, hero, issue, or change; state what would disappear if the topic were replaced. |
| Dead closing phrase | Ends with a mechanical CTA or filler close that adds no action, meaning, clarification, or useful impulse. | Give a concrete action if needed, or end on a meaning-bearing line that holds the angle. |

## forbidden confidence patterns

| pattern | why it is bad | preferred replacement behavior |
| --- | --- | --- |
| Clickbait certainty | Overstates importance or novelty. | Use evidence-matched claims. |
| Manipulative certainty | Pushes the reader toward a conclusion without proof. | Show evidence, limits, and tradeoffs. |
| `This proves...` when evidence is partial | Converts limited support into false proof. | Say `This suggests...` or state the actual evidence. |
| Unsupported superlatives | Cannot be reviewed. | Remove or source the claim. |
| Rewriting facts for dramatic effect | Damages accuracy and reviewability. | Preserve factual boundaries and caveats. |
| Hiding uncertainty | Creates fake confidence. | Mark unknowns, assumptions, and open questions. |

## forbidden UX writing patterns

| pattern | why it is bad | preferred replacement behavior |
| --- | --- | --- |
| UX copy that hides system state | Users cannot decide what to do next. | State what happened, current state, and available action. |
| Vague error messages such as `Something went wrong` | Gives no recovery path. | Explain the problem and what the user can do. |
| Ambiguous verbs such as `Continue`, `Proceed`, or `Submit` when the result is unclear | Users cannot predict the consequence. | Use action-specific verbs: `Save`, `Send invite`, `Delete file`. |
| Invented product behavior | Misleads users and breaks product trust. | Escalate missing behavior or write only from supplied product context. |
| Branding over clarity | Makes the interface harder to use. | Put user action and state first. |
| Multiple intents in one message | Increases cognitive load. | Use one intent per message. |

## forbidden review behavior

| pattern | why it is bad | preferred replacement behavior |
| --- | --- | --- |
| Reviewer rewriting instead of reviewing | Breaks role boundaries and hides findings. | Identify issue, cite artifact, recommend return path. |
| Approval without artifact checks | Weakens review-gate. | Verify required inputs, outputs, traceability, and independence. |
| `Looks good` as review rationale | Not reproducible. | Record concrete checks passed and residual risks. |
| Ignoring missing evidence | Allows unsupported claims through. | Mark `changes_requested` or `blocked` according to severity. |
| Reviewing from memory | Breaks restartability. | Review saved task artifacts. |
| Approving generic but pleasant copy | Lets tone quality hide missing relevance. | Run editorial relevance and replaceability checks before approval. |
| Approving operational instructions after local wording fixes only | Lets clean prose hide broken information architecture. | Run reading path, section role, duplication, selective reading, and navigation checks. |

## replacement guidance

When a forbidden pattern appears:

1. Remove filler before rewriting.
2. Preserve factual meaning.
3. Replace inflated claims with evidence-matched claims.
4. Replace vague UX copy with state, action, and recovery.
5. Record unresolved evidence or product gaps.
6. Route changes to the owning active role instead of crossing role boundaries.
