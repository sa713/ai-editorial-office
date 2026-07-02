# Implementation plan

## Step

Iteration 002 implementation step 001: Behavioral boundaries and honesty rule.

## Files changed

Only one canonical file was changed:

- `editorial_knowledge/01_principles.md`

## Why this file

`editorial_knowledge/01_principles.md` owns durable editorial principles. Step 1 is not a review change, pipeline change, template change, or orchestration change. It is a boundary statement, so it belongs in principles.

## What changed

Added a short `Reader-state boundaries` section:

- reader-state awareness is bounded editorial sensitivity;
- use only when a task involves entry, first step, participation, workspace use, or similar reader action;
- allowed purpose is limited to honest first step, less unnecessary pressure, observation before commitment, and human operational language;
- explicitly forbidden: persuasion, emotional editing, engagement/adoption optimization, tone policing, new workflow/stage/role/score/review requirement;
- honesty rule: mandatory stays mandatory, optional stays optional, unknown stays unknown.

## Why this is bounded and safe

- No workflow changes.
- No review heuristics.
- No pressure audit.
- No prompts.
- No templates.
- No pipelines.
- No agents.
- No new artifacts.

The change only constrains future iteration-002 work before Step 2.

## Why intentionally minimal

Step 1 exists to prevent behavioral sprawl before adding any diagnosis or review guidance. A larger edit here would create the same risk the iteration is meant to avoid.
