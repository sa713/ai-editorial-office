# UX Writing Guidelines

## purpose

This file is the operational UX writing authority for `ux_writer` and `review_agent`.

It governs product-facing copy: labels, buttons, helper text, empty states, validation, errors, notifications, onboarding, and flow guidance.

## core UX writing principles

- Clarity over branding.
- User action first.
- One intent per message.
- Product truth over pleasing phrasing.
- State must be visible when it affects user action.
- Terminology consistency is required.
- Short copy still needs evidence and review.

## clarity rules

UX copy must:

- say what the user can do;
- use specific verbs;
- avoid ambiguous verbs when consequence matters;
- keep the main action close to the beginning;
- avoid internal system language unless the user already sees or needs it;
- remove decorative words that do not change meaning.

Button and command copy should usually be verb-led:

- `Save changes`
- `Send invite`
- `Reset password`
- `Delete file`

Avoid vague commands when the result is unclear:

- `Continue`
- `Proceed`
- `Submit`
- `Confirm`

## terminology rules

Use terminology from:

- the brief;
- product context;
- existing UI copy;
- `/kb/glossary.md`;
- task-specific terminology notes.

Do not rename product concepts for variety. If two terms appear to mean the same thing, record the conflict in `terminology-notes.md` and escalate if the correct term is unclear.

## state communication

UX copy must not hide system state.

When state affects user action, communicate:

- what happened;
- what is happening now;
- what the user can do next;
- what is blocked, if anything;
- whether the system will retry, wait, save, send, cancel, or discard.

Examples:

- `Saving changes...`
- `Changes saved`
- `Invite sent`
- `Payment failed. Check the card details or try another card.`

## error message guidance

Error messages must help recovery.

A useful error message includes:

- the problem in plain language;
- the recovery action, if known;
- the affected object or field, when helpful;
- a safe next step when recovery is not available.

Do not expose technical detail unless the user needs it to act.

Bad:

- `Error`
- `Something went wrong`
- `Invalid input`

Better:

- `Enter a valid email address.`
- `We could not save changes. Try again.`
- `The file is too large. Upload a file under 10 MB.`

## accessibility guidance

UX copy must support accessibility:

- do not rely on color, position, or icon alone to convey meaning;
- write labels that make sense out of visual context;
- keep link text specific;
- avoid time pressure unless required by product behavior;
- make destructive actions explicit;
- use consistent names for the same action or object.

## cognitive load guidance

Reduce decision effort:

- one message, one intent;
- one primary action per state when possible;
- short labels for repeated UI elements;
- progressive detail for complex states;
- no unnecessary explanation of obvious UI behavior;
- no competing terms for the same object.

If copy needs a paragraph to explain the state, the flow or product context may need review.

## prohibited UX writing behavior

`ux_writer` must not:

- invent product behavior;
- invent feature availability;
- change business rules;
- hide uncertainty about system behavior;
- use brand voice to obscure action or state;
- write vague errors without recovery guidance;
- introduce new terminology without a reason;
- collapse multiple states into one ambiguous message;
- imply that an action succeeded before product context confirms it.

`review_agent` must not approve UX copy when:

- product behavior is unsupported;
- required UX artifacts are missing;
- terminology conflicts are unresolved;
- system state is hidden;
- error recovery is missing where recoverability matters;
- the copy violates `/kb/forbidden_patterns.md`.

## escalation rules

Escalate to `chief_editor` or return to `research_agent` when:

- product behavior is unknown;
- a UI state is missing;
- feature availability is unclear;
- terminology conflicts with product context;
- recovery behavior for an error is unknown;
- a factual or product claim lacks support;
- UX copy would require a product decision rather than a wording decision.
