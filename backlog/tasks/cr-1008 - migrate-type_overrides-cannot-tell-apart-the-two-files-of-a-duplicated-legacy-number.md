---
id: CR-1008
title: >-
  migrate type_overrides cannot tell apart the two files of a duplicated legacy
  number
status: To Do
assignee: []
created_date: '2026-10-09 12:35'
labels: []
milestone: m-0
dependencies: []
type: chore
project: change-requests
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`type_overrides` in the triage file is keyed by legacy issue number ([plcc_ng.py](../../migrate/plcc_ng.py), `_validate` and `convert`). When two legacy issues share a number (plcc-ng had three such pairs), an override meant for one file is also applied to the other, so the wrong type can be assigned silently.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A type override can target one file of a duplicated legacy number without affecting the other
- [ ] #2 Overrides keyed by a plain number keep working for numbers that are not duplicated
- [ ] #3 A test covers an override applied to only one file of a duplicate pair
<!-- AC:END -->
