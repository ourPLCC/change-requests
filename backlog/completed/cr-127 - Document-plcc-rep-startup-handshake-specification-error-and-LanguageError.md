---
id: CR-127
title: 'Document `plcc-rep` startup handshake, `specification_error`, and `LanguageError`'
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
`plcc-rep` gained a startup handshake (ready signal) and structured `specification_error` handling, and each language runtime gained a `LanguageError` mechanism for signaling errors from generated code. None of this is documented in `docs/cli/commands/plcc-rep.md` or the per-language extension pages.

### Notes

- `docs/cli/commands/plcc-rep.md` should describe the JSONL protocol: the ready record emitted on startup, and the `specification_error` record emitted when the generated code fails to load.
- Each language extension page (`docs/language-guide/languages/python.md`, `java.md`, `javascript.md`, `haskell.md`) should explain how to raise a `LanguageError` from semantics blocks and what effect it has at runtime (e.g. `plcc-rep` reports it as a `specification_error`).
- `LanguageError` is the intended way for user-written semantics code to signal domain errors; it should be discoverable from the language extension pages, not just the source code.

Migrated from plcc-ng #127.
<!-- SECTION:DESCRIPTION:END -->
