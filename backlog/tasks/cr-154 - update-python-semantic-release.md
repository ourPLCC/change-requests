---
id: CR-154
title: 'update-python-semantic-release'
status: To Do
assignee: []
created_date: '2026-07-07'
labels: []
dependencies: []
type: chore
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`pyproject.toml` pins `python-semantic-release>=9.0.0,<10.0.0`
(`pdm.lock` currently resolves 9.21.2). The latest release is 10.5.3 —
a major version bump, likely with breaking changes to config or CLI
behavior given semantic-release's own versioning conventions. Consider
updating the constraint and adapting `[tool.semantic_release]` in
`pyproject.toml` plus the release workflow/scripts as needed.

### Notes

- Dev-only dependency (used by `bin/release/` and the release CI job,
  not shipped in `src/`), so this is `chore`, not `feat`/`fix` — it
  doesn't affect the published package and shouldn't bump the release
  version.
- Check the [v10 changelog](https://python-semantic-release.readthedocs.io/en/latest/misc/psr_changelog.html)
  for breaking changes before bumping the constraint; run a real
  release dry run (`--noop` / `bin/release/verify.bash`) to confirm
  the config still behaves as expected.

Migrated from plcc-ng #154.
<!-- SECTION:DESCRIPTION:END -->
