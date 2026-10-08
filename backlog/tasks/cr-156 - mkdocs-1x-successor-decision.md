---
id: CR-156
title: 'mkdocs-1x-successor-decision'
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
Our `docs/` site build depends on the MkDocs 1.x lineage, and that lineage
has an unresolved future. We need to decide, at some point before it's
forced on us, what we migrate to.

Current state, verified against this repo's own `pdm.lock`:

- `mkdocs-material` 9.7.6 (pinned `>=9.5`) hard-requires `mkdocs<2,>=1.6` —
  it cannot run on the incompatible "MkDocs 2.0" the original author is
  building in a private `encode/mkdocs` repo.
- `mkdocs-kroki-plugin` 1.6.0 (pinned `>=0.8`) unconditionally requires
  `properdocs` as a dependency — already present in our `pdm.lock` — purely
  so it can print a "switch to ProperDocs" nag during `mkdocs build`. See
  [dev-docs/security-notes.md](../../../plcc-ng/dev-docs/security-notes.md) for the full trace of
  that warning; it's legitimate, not malware.

Nothing is broken today: `mkdocs>=1.6` and `mkdocs-material`'s own
`mkdocs<2,>=1.6` constraint mean our build keeps working as long as real
MkDocs 1.x stays installable from PyPI. The decision only becomes forced if
either (a) MkDocs 1.x is pulled/broken on PyPI, or (b) we want features only
available in a successor.

The two credible successors, per dev-docs/security-notes.md:

- **ProperDocs** — community fork by a former MkDocs maintainer, positioned
  as a 1:1 drop-in replacement (`mkdocs.yml`, plugins, themes work
  unchanged; swap `mkdocs build` for `properdocs build`).
- **Zensical** — new stack built by the actual Material-for-MkDocs team,
  absorbing the theme; reads existing `mkdocs.yml` but only supports a
  subset of plugins today.

### Notes

Not urgent. Revisit when one of the following happens:
- MkDocs 1.x becomes uninstallable or unmaintained-to-the-point-of-breaking.
- `mkdocs-kroki-plugin` (or another pinned doc dependency) drops support for
  real MkDocs 1.x.
- Zensical reaches plugin parity with what we actually use
  (`mkdocs-material`, `mkdocs-kroki-plugin`, `mkdocs-include-markdown-plugin`).

Background and the full investigation trail: [dev-docs/security-notes.md](../../../plcc-ng/dev-docs/security-notes.md).

Migrated from plcc-ng #156.
<!-- SECTION:DESCRIPTION:END -->
