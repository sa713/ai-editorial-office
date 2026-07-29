# Handoff — Chief Editor to Research Agent

- Task: `TASK-PRODUCT-INTENT-REVIEW-STEP2`
- From: `chief_editor`
- To: `research_agent`
- Date: 2026-07-29

## assignment

Establish current Task Need Recognition, task-object, role, template,
task-pack-generator, and regression behavior. Design the smallest Step 2
integration before any implementation.

## fixed boundaries

- Three modes only: `not_needed`, `limited`, `full`.
- Recognition recommends; Chief Editor decides.
- Mode is task-local analytical depth, never task status.
- Full analysis and Step 3 remain forbidden.
- Generator changes require executable shell tests.
