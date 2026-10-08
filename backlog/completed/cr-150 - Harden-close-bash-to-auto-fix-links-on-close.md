---
id: CR-150
title: 'Harden close.bash to auto-fix links on close'
status: Done
assignee: []
created_date: '2026-07-06'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`bin/issues/close.bash` moves an issue file to `issues/done/` but
doesn't touch any links, so every future close recreates the bug
class fixed in CR-149: other `dev-docs/` files keep linking to the
issue's old `issues/<name>` path, and any upward-relative link inside
the moved file itself (e.g. to `dev-docs/v1.0-criteria.md` or
`src/...`) ends up one level short once the file is a directory
deeper.

Enhance `close.bash` to, after the existing `git mv`:

- Grep `dev-docs/` for links to the issue's old `issues/<name>` path
  (from other files) and rewrite them to `issues/done/<name>`.
- Within the moved file itself: strip any `done/` prefix from links to
  already-closed sibling issues (they're true siblings now), and
  prepend one more `../` to any link that climbs above
  `dev-docs/issues/` (it needs one more level now that the file is
  one directory deeper).

### Notes

- Filed while resolving CR-145 (mkdocs `--strict` warnings cleanup); CR-149
  is the one-time cleanup of the existing instances of this bug, this
  issue is the preventive fix so it stops recurring on every future
  close.
- TDD: extend `tests/bats/commands/issues-close.bats`, which already
  has fixture conventions for exercising `close.bash` against a
  throwaway git repo.

Migrated from plcc-ng #150.
<!-- SECTION:DESCRIPTION:END -->
