---
id: CR-67
title: 'Version header should print before anything else'
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
The plcc-ng version number should be printed before any other output, including error messages. Currently, an invocation that fails early produces no version information:

```
$ plcc-scan
plcc-make: grammar file not found: grammar.plcc
$
```

This means bug reports often arrive without a version number, making them harder to diagnose.

### Notes

- The version line should be emitted with minimal dependencies and logic — it must print even if something later in startup fails
- Currently the version and grammar lines may be emitted together; they may need to be separated so the version can fire unconditionally first
- This applies to all plcc-ng CLI entry points (plcc-scan, plcc-parse, etc.)
- Consider stderr vs stdout: version info on stderr ensures it is not mixed into piped output

Migrated from plcc-ng #067.
<!-- SECTION:DESCRIPTION:END -->
