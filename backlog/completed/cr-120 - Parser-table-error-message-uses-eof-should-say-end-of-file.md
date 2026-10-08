---
id: CR-120
title: 'Parser-table error message uses `''eof''` — should say `end of file`'
status: Done
assignee: []
created_date: '2026-06-25'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The parser-table error message for unexpected end-of-input reads:

```text
plcc-parser-table: -:1:1: error: unexpected 'eof', no production for 'Expr'
```

The token name `'eof'` is an internal implementation detail. A student or new user is unlikely to know what it means. `end of file` (unquoted, plain English) would be clearer.

### Notes

- Replace the quoted `'eof'` token name with `end of file` in the error message.
- Check all parser-table error paths for similar internal token names that would confuse users.
- Desired output: `plcc-parser-table: -:1:1: error: unexpected end of file, no production for 'Expr'`

Migrated from plcc-ng #120.
<!-- SECTION:DESCRIPTION:END -->
