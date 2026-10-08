---
id: CR-121
title: '`plcc-rep` continues waiting for input after Python syntax errors in semantics'
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
When there are Python syntax errors in the semantics file, `plcc-rep` shows the errors but then continues to display the `...` continuation prompt as if the build had succeeded and it is waiting for more input.

### Steps to Reproduce

1. Write a spec file with a Python semantics block containing a syntax error.
2. Run `plcc-rep`.
3. Observe: syntax errors are printed, but the REPL then shows `...` and waits for input rather than exiting or aborting the build.

### Notes

- The build should be considered failed if the semantics contain syntax errors.
- `plcc-rep` should not enter the input loop if the build failed.
- Desired behavior: print the syntax errors and exit with a non-zero status, or at minimum print a clear "build failed — fix errors and re-run" message before exiting the REPL.

Migrated from plcc-ng #121.
<!-- SECTION:DESCRIPTION:END -->
