---
id: CR-1013
title: Rename the tracker repo to ourPLCC/dev
status: To Do
assignee: []
created_date: '2026-10-10 18:33'
updated_date: '2026-10-10 18:34'
labels: []
milestone: m-0
dependencies:
  - CR-1012
references:
  - ../../dev-docs/specs/2026-10-10-org-developer-docs-design.md
type: chore
project: change-requests
ordinal: 500
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Once this repo holds the org developer guide, specs, and agent rules as well as the tracker, its name describes only half of it, and a newcomer would not look in a repo called change-requests for how we work. The name appears in every devcontainer path, so it changes before the remaining repos are set up against it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The GitHub repository is ourPLCC/dev
- [ ] #2 backlog/config.yml lists the project value dev in place of change-requests, every CR that had project change-requests has project dev, and bin/check.py passes
- [ ] #3 The repo's current docs, tooling, and CI refer to it as dev; records of past work (closed CRs, migration reports) are left as written
<!-- AC:END -->
