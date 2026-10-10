---
id: CR-1011
title: Document the spec supersession convention
status: To Do
assignee: []
created_date: '2026-10-10 16:18'
updated_date: '2026-10-10 18:34'
labels: []
dependencies:
  - CR-1012
references:
  - ../../dev-docs/specs/2026-10-10-org-developer-docs-design.md
type: docs
project: change-requests
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Design decisions live in specs and are found by searching them, but nothing written down says how a later spec overrides an earlier one. In practice we have both edited merged specs and added ad hoc "superseded" banners, so a reader cannot tell whether a spec is still current or which parts of it were replaced.

The agreed convention: a merged spec is frozen (it may change only on its own branch, during implementation); a newer spec declares what it overrides in a `## Supersedes` section that links each older spec and states the scope (entirely, or which parts); there are no forward "superseded by" links, and readers find superseding specs by searching for the older spec's filename.

This convention is meant to apply across all ourPLCC repos. Where org-wide policy lives is still being decided, so this CR may move to another project once that is settled.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The documentation contributors read for spec guidance states that a merged spec is not edited; specs change only on their own branch during implementation
- [ ] #2 It states that a newer spec lists each spec it overrides in a `## Supersedes` section, linking the spec and stating the scope (entirely, or which parts)
- [ ] #3 It states that specs do not carry forward "superseded by" links, and tells readers to search both the repo's and the org's dev-docs/specs/ for a spec's filename to find anything that supersedes it
<!-- AC:END -->
