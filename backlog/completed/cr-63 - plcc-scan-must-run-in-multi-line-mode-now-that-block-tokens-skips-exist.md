---
id: CR-63
title: 'plcc-scan must run in multi-line mode now that block tokens/skips exist'
status: Done
assignee: []
created_date: '2026-06-05'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Now that block tokens and skips exist (patterns that can span multiple lines), `plcc-scan` needs to run in multi-line mode — reading across line boundaries the way `plcc-parse` and `plcc-rep` already do. In its current single-line mode, block tokens/skips will never match input that spans more than one line.

### Notes

- `plcc-parse` and `plcc-rep` already handle multi-line input correctly; `plcc-scan` should adopt the same approach.
- This is a prerequisite for block tokens/skips to be useful end-to-end.

Migrated from plcc-ng #063.
<!-- SECTION:DESCRIPTION:END -->
