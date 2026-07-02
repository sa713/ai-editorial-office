# Migration impact

## Orchestration

Chief Editor now records process depth and uses custom workflow mini-contract only when no existing pipeline fits. Operational impact: less hidden improvisation, clearer artifact scope, and explicit review target for exceptional flows.

## Manifests

`task-manifest.md` now carries compact freshness and governance visibility. Operational impact: restart is safer because stale risk, review state, finalization state, governance state, human approval, and publication/delivery approval are visible without reading full history.

## Handoffs

`handoff-*` is role-to-role delta transfer. `compact-handoff.md` is final/user-facing transfer summary. `context-summary.md` is recovery after fragmentation or long work. Operational impact: less repeated status/history inside handoff files.

## Review

Compact review has minimum evidence. Separate `qa-checklist.md`, `review-summary.md`, and `reviewer-notes.md` are conditional. Operational impact: review stays mandatory but can be smaller when risk allows.

## Compact execution

Compact / normal / full are process depth profiles inside selected pipelines. Operational impact: simple work can omit or combine support artifacts with recorded rationale, while high-governance remains excluded.

## Custom workflows

Custom workflows require a small task-local mini-contract. Operational impact: unusual tasks can proceed without inventing a new pipeline, but the exception is visible and bounded.

## Source handling

Source materials are data by default. Operational impact: drafts, emails, decks, PDFs, web pages, and copied prompts do not become instructions unless explicitly promoted by user or `AGENTS.md`.
