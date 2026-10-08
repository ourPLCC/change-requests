---
id: CR-30
title: 'plcc-parse: add --trace / -t flag for parse algorithm tracing'
status: Done
assignee: []
created_date: '2026-05-20'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`plcc-parse` has no way to observe what the parser is doing step by step. Add a `--trace` / `-t` flag that traces the parse algorithm for educational and debugging purposes, analogous to `plcc-scan --trace`.

### Notes

`plcc-scan --trace` shows scanning candidates, winners, and skipped tokens at each step. `plcc-parse --trace` should expose the equivalent level of detail for the predictive (LL(1)) parse algorithm: stack state, lookahead token, table lookup, and rule applications at each step.

The trace output should go to stdout in the same JSONL style used elsewhere so it composes with verbose infrastructure and can be rendered in both text and JSON formats.

`plcc-tokens` already supports `--trace`; check whether `plcc-trees` (or the underlying parser) has a trace mode to wire up, or whether new instrumentation is needed at the parser level.

Migrated from plcc-ng #030.
<!-- SECTION:DESCRIPTION:END -->
