---
id: CR-107
title: 'Add documentation for the Haskell language extension'
status: Done
assignee: []
created_date: '2026-06-23'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
plcc-ng can now emit Haskell, but there is no user-facing documentation for it. Users have no way to know the feature exists, how to invoke it, or how to write Haskell semantic sections.

### Notes

- Model the page on the existing Java and Python language guide pages.
- Cover: how to invoke `plcc-haskell-emit`, the supported fragment kinds (`top`, `import`, `body`, `file`), and a minimal end-to-end example.
- Note Haskell-specific requirements (GHC version, cabal).
- Mention the concrete-vs-abstract class name gotcha (see issue 105) until that is fixed.

Migrated from plcc-ng #107.
<!-- SECTION:DESCRIPTION:END -->
