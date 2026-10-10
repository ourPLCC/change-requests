---
id: CR-1006
title: migrate _remove_previous deletes any file that contains the provenance text
status: To Do
assignee: []
created_date: '2026-10-09 12:35'
updated_date: '2026-10-10 19:14'
labels: []
milestone: m-0
dependencies: []
type: chore
project: dev
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`_remove_previous` in [plcc_ng.py](../../migrate/plcc_ng.py) deletes every tracker file whose text contains `Migrated from <project> #` anywhere. Migrated CRs carry that line as the last line of their description (just before the description end marker), but nothing stops a later CR or a hand-edited note from quoting it, and a re-run of the migration would then delete a CR it never created. No file is affected today; the risk grows once more repos are migrated and their CRs are discussed.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Only files whose description ends with the provenance line are removed on a re-run
- [ ] #2 A test shows a CR that quotes the provenance line elsewhere in its text survives a re-run
- [ ] #3 A test shows a previously migrated CR is still removed on a re-run
<!-- AC:END -->
