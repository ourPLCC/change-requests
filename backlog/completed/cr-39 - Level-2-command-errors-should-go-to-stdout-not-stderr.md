---
id: CR-39
title: 'Level-2 command errors should go to stdout, not stderr'
status: Done
assignee: []
created_date: '2026-05-28'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`plcc-parse` and `plcc-rep` print user-facing error messages (parse errors, scan errors) to stderr. `plcc-scan` already prints its errors to stdout. The three commands should be consistent.

When a student redirects stdout to capture the results of their experiment, they should get errors alongside the output — not lose them to an unredirected stderr. Students should not need to understand stream redirection to use these tools effectively.

### Steps to Reproduce

```bash
plcc-parse <<< "bad input" > out.txt
# out.txt is empty; error only visible on terminal
```

### Notes

- `plcc-scan` already does the right thing: `_render_record()` in `scan.py` prints errors with a plain `print()` (stdout).
- `plcc-parse` and `plcc-rep` both call `print_parse_error()` in `cmd/pipeline.py`, which writes to `sys.stderr`. Fixing that function fixes both commands.
- Check `rep.py` for any other error prints that belong on stdout (interpreter errors, etc.).
- stderr should be reserved for tool-level diagnostics: grammar file not found, internal failures, verbose/debug events.
- This fix is a prerequisite for issue 030 (parse trace), which assumes all user-facing output — including the failure trace — lives on stdout.

Migrated from plcc-ng #039.
<!-- SECTION:DESCRIPTION:END -->
