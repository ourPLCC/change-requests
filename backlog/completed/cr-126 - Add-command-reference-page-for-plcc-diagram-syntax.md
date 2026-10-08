---
id: CR-126
title: 'Add command reference page for `plcc-diagram-syntax`'
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
Issue 123 renamed `plcc-diagram-syntactic` to `plcc-diagram-syntax`, but no command reference page was created or updated for the new name. There is no `docs/cli/commands/plcc-diagram-syntax.md` file, and no user-facing docs reference `plcc-diagram-syntax` by name.

### Notes

- Add `docs/cli/commands/plcc-diagram-syntax.md` modeled after the other `plcc-diagram-*` command pages.
- Wire it into `mkdocs.yml` nav.
- Check whether `plcc-diagram-syntactic` appears anywhere in user-facing docs and remove/replace it.

Migrated from plcc-ng #126.
<!-- SECTION:DESCRIPTION:END -->
