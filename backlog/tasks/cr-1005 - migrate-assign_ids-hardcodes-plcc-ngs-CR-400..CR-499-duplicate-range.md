---
id: CR-1005
title: migrate assign_ids hardcodes plcc-ng's CR-400..CR-499 duplicate range
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
`assign_ids` in [plcc_ng.py](../../migrate/plcc_ng.py) takes `offset` as a parameter, but its range guard for the second file of a duplicated legacy number is hard-coded to `400 <= cr <= 499` and its message names plcc-ng's range. Reusing it for languages-ng (+500) or plcc-ng-demo (+800) would reject every duplicate number even though the ID it assigns is valid for that repo, which blocks CR-1000 and CR-1001 from sharing the tooling.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The duplicate-ID range guard is derived from the repo being migrated, not fixed at 400..499
- [ ] #2 A test shows a duplicate legacy number migrated with a non-plcc-ng offset gets an ID inside that repo's reserved range
- [ ] #3 A test shows an ID outside the repo's reserved range is still rejected
- [ ] #4 Re-running the plcc-ng migration produces the same IDs as before
<!-- AC:END -->
