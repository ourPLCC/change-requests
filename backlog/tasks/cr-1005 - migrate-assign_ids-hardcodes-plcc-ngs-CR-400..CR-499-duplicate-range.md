---
id: CR-1005
title: migrate assign_ids hardcodes plcc-ng's CR-400..CR-499 duplicate range
status: In Progress
assignee:
  - '@StoneyJackson'
created_date: '2026-10-09 12:35'
updated_date: '2026-10-10 20:51'
labels: []
milestone: m-0
dependencies: []
type: chore
project: dev
ordinal: 2000
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

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
assign_ids now takes dup_offset and dup_range (defaults: plcc-ng's 400 and CR-400..CR-499). Verified on branch cr-1005-derive-duplicate-id-range: plcc-ng's 197 legacy issues (from plcc-ng a9959188^) get identical IDs and remaps before and after. Open question for CR-1000/CR-1001: the ID table reserves no duplicate range for languages-ng (CR-501..CR-699) or plcc-ng-demo (CR-801..CR-899); whoever migrates them picks dup_offset/dup_range inside those ranges and records it in dev-docs/tracker.md.
<!-- SECTION:NOTES:END -->
