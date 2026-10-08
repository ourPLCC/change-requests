---
id: CR-155
title: 'test-scripts-path-filter'
status: Done
assignee: []
created_date: '2026-07-07'
labels: []
dependencies: []
type: chore
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`bin/test/units.bash` already forwards its arguments to `pdm test`
(pytest), so `bin/test/units.bash src/plcc/cmd/make_test.py` narrows to
one file — CONTRIBUTING.md documents it as the tight TDD inner loop for
exactly this reason. The bats-backed tiers don't offer the same thing:
`bin/test/commands.bash`, `bin/test/integration.bash`, and
`bin/test/e2e.bash` ignore any arguments and always run their whole
`tests/bats/<tier>/` directory via a hardcoded `bats tests/bats/<tier>/`
call, even though `bats` itself accepts a specific file or subdirectory.

Give these scripts (and `functional.bash`, which composes them) an
optional path parameter that narrows the `bats` invocation to the named
file or directory, falling back to the current whole-tier behavior when
no path is given. That turns them into a usable inner loop for
bats-covered work the way `units.bash` already is for pytest-covered
work.

### Steps to Reproduce

1. Edit a single file in `tests/bats/commands/`.
2. Run `bin/test/commands.bash tests/bats/commands/plcc-make.bats`.
3. Observe it runs the entire `tests/bats/commands/` directory instead
   of just that file — no faster than running the whole tier.

### Notes

- Already flagged as a known gap in issue CR-152's notes, called out
  there as "why cache misses are expensive and worth avoiding."
- Dev-only tooling (`bin/`), not shipped in `src/` — `chore`, not
  `feat`, so it doesn't bump the release version.
- TDD: `tests/bats/commands/` already has cache-behavior coverage for
  these scripts (see CR-152); extend it with a case asserting that a
  path argument narrows the `bats` invocation.

Migrated from plcc-ng #155.
<!-- SECTION:DESCRIPTION:END -->
