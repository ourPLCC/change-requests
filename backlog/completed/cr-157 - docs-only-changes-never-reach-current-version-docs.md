---
id: CR-157
title: 'docs-only-changes-never-reach-current-version-docs'
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
Our published docs are versioned with `mike` (see
[.github/workflows/docs.yml](../../../plcc-ng/.github/workflows/docs.yml)):

- Every push to `main` redeploys the `dev` alias.
- Only a GitHub `release` event redeploys a version alias (e.g. `1.0`)
  and moves `latest`.

Since `docs`-only commits never bump the version (by design — see the
classification note in [issues/TEMPLATE.md](../../TEMPLATE.md)), a
docs-only PR merged to `main` updates `dev` but never touches `1.0` or
`latest`. That was fine as an assumption when docs shipped in lockstep
with the release that introduced them, but in practice docs regularly
lag behind — we fix or clarify documentation for features that already
shipped, in PRs with no code change. Right now those fixes are
invisible to anyone pinned to `1.0`/`latest` until we happen to cut a
new release for an unrelated reason.

Discovered while discussing issue CR-147 (heading capitalization): the
fix merged to `main` and appeared on the `dev` docs preview, but users
on the `1.0` docs won't see it until the next release.

### Notes

Proposed direction: add a workflow step, triggered on push to `main`
with a `docs/` path filter, that looks up whatever version `mike list`
currently reports as newest (not `dev`) and re-runs `mike deploy
<that-version>` — no `--update-aliases`, so it doesn't create a new
version or move `latest`, just refreshes that version's already-live
content.

Open question worth resolving before implementing: should this
sync unconditionally on every docs-only merge, or only for changes
judged worth backporting (e.g. broken instructions, wrong commands)
versus purely cosmetic changes (e.g. heading capitalization) that
don't need to disturb an already-published snapshot? Auto-syncing
everything is simplest but means a version's docs silently drift from
"what shipped with that release" toward "whatever main says now," even
for non-functional edits.

Migrated from plcc-ng #157.
<!-- SECTION:DESCRIPTION:END -->
