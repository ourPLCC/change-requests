---
id: CR-1010
title: Give the tracker its own dev-docs/specs/ with a spec of its design
status: To Do
assignee: []
created_date: '2026-10-09 13:08'
updated_date: '2026-10-10 19:14'
labels: []
dependencies:
  - CR-1012
references:
  - ../../../plcc-ng/dev-docs/specs/2026-10-08-199-central-tracker-design.md
type: docs
project: dev
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The tracker is a system built on Backlog.md: its own config, ID ranges, lifecycle rules, bin/check.py, devcontainer setup in each code repo, and migrate/ tooling. Its design and the reasons behind it are recorded only in a plcc-ng spec written as the plan for moving plcc-ng onto the tracker. Someone fixing the tracker (for example a migrate/ bug) looks in this repo and finds the workflow rules in README.md but not the decisions behind them, so fixes risk undoing a choice that was made on purpose. This repo has no dev-docs/specs/ for tracker specs to go in.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 This repo has dev-docs/specs/ containing an initial spec of the tracker's current design: configuration, IDs, lifecycle, checks, code-repo setup, and migration tooling
- [ ] #2 The spec gives the reasons for its key decisions and the alternatives that were rejected
- [ ] #3 The spec describes the system as it stands, not the plan for migrating plcc-ng
- [ ] #4 README.md points to dev-docs/specs/ and says specs for project change-requests go there
- [ ] #5 README.md says assignees are GitHub usernames (e.g. @StoneyJackson), and the spec records why
<!-- AC:END -->
