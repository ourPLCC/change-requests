---
id: CR-129
title: 'Update docs for "end of file" parser error message change'
status: Done
assignee: []
created_date: '2026-06-30'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A recent fix changed parser error messages from `eof` to `end of file`. Any documentation that shows example parser error output containing the old `eof` wording is now stale.

### Notes

- Search docs for `eof` in error message examples and update to `end of file`.
- Also check quickstart guides, language guide, and CLI command pages for any copy-pasted error output.

Migrated from plcc-ng #129.
<!-- SECTION:DESCRIPTION:END -->
