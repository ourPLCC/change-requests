---
id: CR-1007
title: 'migrate verify crashes when a migrated file has no id: line'
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
[verify.py](../../migrate/verify.py) calls `ID_RE.search(...).group(1)` on every task and draft file. A file without an `id:` line makes `search` return `None`, and verify dies with `AttributeError` instead of reporting which file is broken, which is the case it most needs to explain.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A file without an id: line is reported as a verification failure that names the file
- [ ] #2 verify exits non-zero in that case and still checks the remaining files
- [ ] #3 A test covers a task file and a draft file without an id: line
<!-- AC:END -->
