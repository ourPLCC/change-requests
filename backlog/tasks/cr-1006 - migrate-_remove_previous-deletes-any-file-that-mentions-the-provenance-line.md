---
id: CR-1006
title: migrate _remove_previous deletes any file that mentions the provenance line
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
`_remove_previous` in [plcc_ng.py](../../migrate/plcc_ng.py) deletes every tracker file that contains `Migrated from <project> #` anywhere. Migrated CRs end with that line, but other CRs may quote it in their text (CR-199's description does). Re-running a migration would then delete CRs it never created. The match must be anchored to the last line of the file.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Only files whose last non-blank line is the provenance line are removed
- [ ] #2 A test shows a CR that quotes the provenance line in its body survives a re-run
- [ ] #3 A test shows a previously migrated CR is still removed on a re-run
<!-- AC:END -->
