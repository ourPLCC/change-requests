---
id: CR-131
title: 'Make `LanguageError` accessible from Haskell user code'
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
`LanguageError` is defined inline in the generated `Main.hs`, but user-authored semantics code lives in separate module files (`Prog.hs`, `Exp.hs`, etc.) that `Main.hs` imports — not the other way around. There is currently no way for a Haskell user to import or construct a `LanguageError` value from their semantics code.

The other three languages (Python, Java, JavaScript) all provide `LanguageError` in a `runtime/` module that user class files can import via an `import` fragment. Haskell needs equivalent access.

### Notes

- The fix is to move `LanguageError` out of the inline `Main.hs` template and into a dedicated `runtime/LanguageError.hs` module (similar to `Token.hs`). `Main.hs` and user modules would then both import it.
- Until this is done, the Haskell language-guide page should note that `LanguageError` is not yet accessible from user semantics code (documented in issue 127).
- Related: issue 127 — document `plcc-rep` protocol, `specification_error`, and `LanguageError` per language.

Migrated from plcc-ng #131.
<!-- SECTION:DESCRIPTION:END -->
