---
id: CR-99
title: 'Add a link from the docs site to the source code repository'
status: Done
assignee: []
created_date: '2026-06-18'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The docs site has no link to the source code repository. Users who want to
browse the code, file issues, or contribute have no obvious path from the
docs to the repository.

### Desired Behavior

Add a visible link from the docs site to the GitHub repository. Common
placements include:

- A repository link in the site header or navigation bar.
- A footer link alongside any other site-wide links.

Most static-site doc frameworks (MkDocs Material, Docusaurus) have
first-class support for a repo link/icon in the header — enabling it may
be a one-line config change.

### Notes

The link should point to the canonical repository URL. If the docs
framework supports it, displaying the GitHub icon alongside the link is
a nice touch.

Migrated from plcc-ng #099.
<!-- SECTION:DESCRIPTION:END -->
