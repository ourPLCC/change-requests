# Organization-wide developer docs (`ourPLCC/dev`) — design

Date: 2026-10-10

## Problem

Material that applies to every ourPLCC repo has no home:

- Workflow rules are restated in each repo's `CONTRIBUTING.md` and
  `CLAUDE.md` and in the tracker README, and the copies drift.
- A decision that binds several repos has nowhere to go. The tracker's own
  design spec lives in plcc-ng, and the spec supersession convention below
  had no obvious place either.
- A new repo starts by copying another repo's docs, or by reinventing them.
- Agent instruction files (`CLAUDE.md`) mix rules every developer needs with
  rules that apply only to agents, so humans miss rules they should follow
  and agents load duplicates.

The tracker repo (`ourPLCC/change-requests`) is already cloned beside every
code repo and mounted in every devcontainer, and its README already carries
workflow policy beyond tracker mechanics.

## Decision summary

Rename `ourPLCC/change-requests` to **`ourPLCC/dev`** and make it the home of
the organization's shared development material: the org developer guide,
org-wide specs, agent rules, and the change-request tracker. Each code repo
keeps only what is specific to it, says so explicitly where it deviates, and
loads the org material into agent sessions by import rather than by copy.

## Audience and scope

`dev` is for people who build and run ourPLCC: maintainers, their agents,
and new developers. Two needs drive the design:

- **Maintainers and agents** need the shared rules loaded in every session,
  consistent across repos, and reusable when starting a new repo.
- **New developers** must reach the shared rules from GitHub without cloning
  anything: any repo's `CONTRIBUTING.md` is one link away from them.

Out of scope: the user-facing front door (a GitHub Pages site, the org
profile README, community-health files). Those serve a different audience
and would give this repo too many responsibilities.

## The `dev` repo

```text
dev/
  README.md          what this repo is; where to start
  CONTRIBUTING.md    the org developer guide
  AGENTS.md          agent-only rules for every ourPLCC repo
  dev-docs/
    tracker.md       the full tracker guide
    specs/           org-wide specs
  backlog/           tracker data
  bin/  migrate/     tracker tooling
```

- **`CONTRIBUTING.md`** holds only what every developer in every repo needs.
  It is imported into every agent session, so it stays short:
  - how work flows (issue → CR → spec → branch → PR), branch naming, and
    commit style;
  - spec conventions, including supersession (below);
  - the precedence rule (below);
  - a short summary of tracking, linking to `dev-docs/tracker.md`.
- **`dev-docs/tracker.md`** takes the tracker-specific content of today's
  README: filing, lifecycle, statuses, drafts, types and projects, IDs,
  references, searching, pushing, checks, upgrading Backlog.md, and notes on
  working on the tracker tooling itself. Tooling notes go here rather than in
  `CONTRIBUTING.md` so they are not imported into every repo's sessions.
- **`README.md`** says what the repo is and sends readers to
  `CONTRIBUTING.md`.
- **`dev-docs/specs/`** holds specs for decisions that bind more than one
  repo, including the tracker's own design.

## What each code repo keeps

- **`CONTRIBUTING.md`** opens with: "This builds on the
  [ourPLCC developer guide](https://github.com/ourPLCC/dev/blob/main/CONTRIBUTING.md);
  read that first. Below is what's specific to this repo, and where it
  differs." The rest is repo-specific: commands, test tiers, `bin/`
  conventions, documentation rules, commit scopes, CI behavior.
- **`dev-docs/`** holds the repo's architecture, release procedure, security
  notes, and `specs/` for changes to that repo.
- **`AGENTS.md`** (see Agent instructions).

A repo's docs do not restate the org guide, even to agree with it; they link
to it.

### Precedence

The org guide applies unless a repo's `CONTRIBUTING.md` or `dev-docs/`
deviates **explicitly and with a reason** ("Unlike the org guide, this
repo … because …"). An unexplained difference is drift and is fixed in
whichever copy is wrong.

Readers are told what wins; they never infer it from reading order.

### Where a spec goes

A spec lives in the repo whose code it changes. A decision that binds more
than one repo has its spec in `dev/dev-docs/specs/`; the work is still one
CR per repo, and each CR references that spec.

## Spec supersession

Design decisions live in specs and are found by searching them. A spec
records decisions at the time it was written, so later specs may override
it, wholly or in part.

- **A merged spec is frozen.** It changes only on its own branch, during its
  implementation, when the course changes.
- **A newer spec declares what it overrides** in a `## Supersedes` section
  that links each older spec and states the scope: entirely, or which parts.
- **No forward links.** Older specs do not get "superseded by" banners. To
  check whether a spec still holds, search both the repo's and `dev`'s
  `dev-docs/specs/` for its filename. Banners already in place stay; removing
  them would be an edit to a merged spec.

## Agent instructions

### What goes in `AGENTS.md`

The first rule in `dev/AGENTS.md`, applying everywhere:

> If a human contributor would need to know it, it goes in `CONTRIBUTING.md`
> or `dev-docs/`, even if agents need it too. `AGENTS.md` holds only what
> exists because the reader is an agent.

The same test applies to agent memory: general knowledge belongs in the
docs, not in memory files.

### `dev/AGENTS.md`

- The rule above.
- **Agent mechanics:** run `backlog` as a single plain command, never
  wrapped in other shell code (permission rules match the command's start);
  never edit tracker files by hand; where memory goes and what belongs in it.
- **Limits on autonomy:** create CRs or drafts only with the human's
  approval; during automated runs, record discovered work in the CR's notes;
  triage those notes with the human when closing the CR.

### Each code repo's `AGENTS.md`

```markdown
Read @../dev/AGENTS.md, @../dev/CONTRIBUTING.md, then @CONTRIBUTING.md before making changes.

## Agent rules for this repo

- …rules specific both to this repo and to agents, if any…
```

- **Imports, not pointers.** A link inside an imported file is a suggestion
  an agent may skip; an import is always loaded. Importing the human docs
  gives agents the same rules humans read, from one source.
- **Order** runs general to specific: org agent rules, org guide, repo guide.
- **Relative paths** work on the host and in the container, since the repos
  are siblings in both. To an agent without import support, the line reads as
  an instruction.
- **Long references** (`dev-docs/tracker.md`, release procedures) are linked
  from `CONTRIBUTING.md`, not imported.

No repo has a `CLAUDE.md`: Claude Code loads `AGENTS.md` when a project has
no `CLAUDE.md`, and other agents read `AGENTS.md` natively. Claude-specific
configuration (`.claude/settings.json`) stays where it is.

**To verify during implementation:** that `@` imports inside `AGENTS.md`
resolve, and how relative imports outside the repo are handled, including any
one-time approval prompt. Setup instructions mention what is found.

## Changes and order

One CR per repo, linked by dependencies:

1. **Restructure the tracker repo into the `dev` layout.** Split the README
   into `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, and
   `dev-docs/tracker.md`; add `dev-docs/specs/` holding this spec. Recording
   the tracker's own design spec there and adding the supersession
   convention to `CONTRIBUTING.md` are separate changes that follow this
   one.
2. **Rename the repo to `dev`** (depends on 1): the GitHub rename, the
   project value `change-requests` → `dev` in `backlog/config.yml` with
   existing CRs re-tagged, and self-references in the repo.
3. **plcc-ng adopts the layout** (depends on 2): the devcontainer clones and
   mounts `../dev` and updates `BACKLOG_CWD` and `safe.directory`;
   `CLAUDE.md` becomes `AGENTS.md`; `CONTRIBUTING.md` drops the org
   material ("Tracking work", branch naming, commit style) and gains the
   opening line; the PR template is updated.
4. **The remaining repos** (languages-ng, plcc-ng-demo,
   plcc-ng-devcontainer) are set up against `dev` directly, following
   plcc-ng's layout from step 3; their migrations depend on step 2.

No window is broken during the rename: GitHub redirects the old URL, and
plcc-ng's devcontainer keeps mounting the host's existing
`../change-requests` folder until step 3 merges. Each maintainer then
renames that host folder to `../dev` before rebuilding; step 3's PR says
so. Relative links from CRs into sibling repos (`../../../plcc-ng/…`) do not
depend on the tracker's name.

## Alternatives considered

- **A separate handbook repo** beside the tracker. Rejected: a second clone
  and mount for every developer, a rule for which repo each piece belongs in,
  and the tracker README is already part developer guide.
- **GitHub's org `.github` repo.** Its inherited community-health files suit
  outside visitors, but devcontainers and agents do not see it without
  another mount. It may still serve the out-of-scope front door later.
- **Names.** `planning` fits the tracker but not the guides; `handbook` the
  reverse; `meta` has confused people elsewhere. `dev` is short and names
  the audience.
- **Precedence by binding org guide** (repos only add). Too strict for real,
  rare deviations. **Precedence by silent repo override.** Indistinguishable
  from drift.
- **Pointers instead of imports** for agents. Nothing ensures the agent
  follows them.
- **Org material in `CLAUDE.md`.** Claude-only; `AGENTS.md` serves every
  agent and Claude reads it.
- **Backlog.md decisions and documents.** Decisions have no update command,
  so recording a status change means editing tracker files by hand; documents
  would compete with specs kept beside the code they describe.
- **A decision index, and forward "superseded by" links.** Searching specs
  already finds both the decision and anything overriding it; an index or
  banner is a second copy that can disagree.

## Supersedes

- [2026-10-08-199-central-tracker-design.md](../../../plcc-ng/dev-docs/specs/2026-10-08-199-central-tracker-design.md),
  in part: the repository's name, and the README as the single workflow
  guide. The tracker's model, IDs, lifecycle, and checks stand.
