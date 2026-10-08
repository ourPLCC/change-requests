---
id: CR-116
title: 'docopts gives a cryptic error for unrecognized command-line options'
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
When a user passes an unrecognized or malformed option to any `plcc-*` command, docopts emits a confusing internal representation instead of a clear usage error. Example observed:

```text
Warning: found unmatched (duplicate?) arguments [Option('-t', None, 0, True)]
```

This message is opaque to users — it exposes docopts internals rather than saying what was wrong.

### Notes

- Affects any command that uses docopts for argument parsing.
- The fix likely involves catching the docopts exception and printing the command's usage string with a short "unrecognized option" prefix, then exiting non-zero.
- Goal: replace the internal warning with something like `error: unrecognized option '-t'\n<usage string>`.

Migrated from plcc-ng #116.
<!-- SECTION:DESCRIPTION:END -->
