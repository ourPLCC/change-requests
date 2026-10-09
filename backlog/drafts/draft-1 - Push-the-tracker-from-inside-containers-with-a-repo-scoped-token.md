---
id: DRAFT-1
title: Push the tracker from inside containers with a repo-scoped token
status: Draft
assignee: []
created_date: '2026-10-09 01:55'
labels: []
dependencies: []
project: plcc-ng-devcontainer
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Pushes happen from the host because the container gets no credentials. A fine-grained token limited to ourPLCC/change-requests, passed only to ourPLCC devcontainers via ${localEnv:…}, would let containers push the tracker but not code. Needs: URL-scoped credential helper via containerEnv, and core.hooksPath moved into containerEnv so the host never runs tracker hooks.
<!-- SECTION:DESCRIPTION:END -->
