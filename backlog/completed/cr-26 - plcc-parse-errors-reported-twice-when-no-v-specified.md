---
id: CR-26
title: 'plcc-parse: errors reported twice when no `-v` specified'
status: Done
assignee: []
created_date: '2026-05-18'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
When `plcc-parse` encounters an error without `-v`, the error is emitted twice: once as plain
text and once as a JSONL verbose event. The JSONL line should be suppressed when verbose mode
is not active.

### Steps to Reproduce

```bash
echo "bad input" | plcc-parse
```

Observe the error message appears as plain text followed by a `{"event":...}` JSONL line on
stderr.

### Notes

The two `verbose.emit_error()` calls in `table_cli.py` that wrote parse result errors to
stderr were removed entirely. Parse result errors (unexpected token, `ParseError`) are data
and belong on stdout as JSONL records, not on stderr as tool diagnostics. The two
`verbose.emit_error()` calls that guard genuine tool failures (cannot load `ll1.json`,
grammar is not LL(1)) were left intact.

Migrated from plcc-ng #026.
<!-- SECTION:DESCRIPTION:END -->
