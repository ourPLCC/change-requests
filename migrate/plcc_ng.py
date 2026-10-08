"""Convert plcc-ng's legacy dev-docs/issues/ tracker into Backlog.md files.

Usage: python3 -m migrate.plcc_ng --repo PLCC_NG --tracker ISSUES --triage FILE --report OUT
"""
import argparse
import json
import posixpath
import sys
from pathlib import Path

from migrate.emit import (CORE_TYPES, TYPE_MAP, WONTDO_RE, assemble_description, filename_for,
                          render_task)
from migrate.legacy import parse_issue
from migrate.links import IssueRef, LinkContext, rewrite_issue_body

PROJECT = "plcc-ng"
OFFSET = 0
DUP_OFFSET = 400
OTHER_OFFSETS = {"languages-ng": 500, "plcc-ng-demo": 800}
GITHUB = "https://github.com/ourPLCC/plcc-ng"
PROVENANCE_PREFIX = f"Migrated from {PROJECT} #"
FOLDERS = ("tasks", "completed", "drafts")


def load_issues(repo_root):
    repo_root = Path(repo_root)
    base = repo_root / "dev-docs" / "issues"
    paths = sorted(base.glob("[0-9]*.md")) + sorted((base / "done").glob("[0-9]*.md"))
    issues = [parse_issue(p, repo_root) for p in paths]
    return sorted(issues, key=lambda i: (i.number, posixpath.basename(i.rel_path)))


def assign_ids(issues, offset=OFFSET):
    by_number = {}
    for issue in issues:
        by_number.setdefault(issue.number, []).append(issue)
    ids, remaps = {}, []
    for number, group in by_number.items():
        if len(group) > 2:
            raise SystemExit(f"#{number:03d} is used by {len(group)} files; extend the remap rule")
        ids[group[0].rel_path] = number + offset
        if len(group) == 2:
            cr = number + offset + DUP_OFFSET
            if not 400 <= cr <= 499:
                raise SystemExit(f"duplicate #{number:03d} remaps to CR-{cr}, outside the "
                                 f"reserved CR-400..CR-499 range (500+ is languages-ng)")
            ids[group[1].rel_path] = cr
            remaps.append(f"#{number:03d} {group[1].slug} -> CR-{cr} "
                          f"(#{number:03d} {group[0].slug} keeps CR-{number + offset})")
    return ids, remaps


def build_refs(issues, ids):
    refs = {}
    for issue in issues:
        refs.setdefault(issue.number, []).append(IssueRef(issue.slug, ids[issue.rel_path]))
    return refs


def _placement(issue, triage):
    if issue.closed:
        return "completed"
    return "drafts" if triage["open"][str(issue.number)]["as"] == "draft" else "tasks"


def expected_counts(issues, triage):
    counts = {folder: 0 for folder in FOLDERS}
    for issue in issues:
        counts[_placement(issue, triage)] += 1
    return counts


def _validate(issues, triage):
    errors = []
    open_triage = triage.get("open", {})
    overrides = triage.get("type_overrides", {})
    for issue in issues:
        if not issue.closed:
            entry = open_triage.get(str(issue.number))
            if not entry or entry.get("as") not in ("cr", "draft"):
                errors.append(f"#{issue.number:03d} is open but has no valid triage entry")
        mapped = overrides.get(str(issue.number)) or TYPE_MAP.get(issue.type)
        if mapped not in CORE_TYPES:
            errors.append(f"#{issue.number:03d} has type {issue.type!r}; add a type_overrides entry")
    if errors:
        raise SystemExit("cannot convert:\n  " + "\n  ".join(errors))


def _remove_previous(backlog):
    for folder in FOLDERS:
        for path in (backlog / folder).glob("*.md"):
            if PROVENANCE_PREFIX in path.read_text(encoding="utf-8"):
                path.unlink()


def convert(repo_root, tracker_root, triage):
    repo_root, backlog = Path(repo_root), Path(tracker_root) / "backlog"
    issues = load_issues(repo_root)
    _validate(issues, triage)
    ids, remaps = assign_ids(issues)
    ctx = LinkContext(PROJECT, repo_root, build_refs(issues, ids), OTHER_OFFSETS, GITHUB)
    overrides = triage.get("type_overrides", {})
    _remove_previous(backlog)

    type_notes, wontdo, drafts, draft_number = [], [], [], 0
    for issue in issues:
        folder = _placement(issue, triage)
        cr_type = overrides.get(str(issue.number)) or TYPE_MAP[issue.type]
        if cr_type != issue.type:
            type_notes.append(f"#{issue.number:03d}: {issue.type!r} -> {cr_type}")
        labels, final_summary, status = [], None, "To Do"
        if folder == "completed":
            task_id, status = f"CR-{ids[issue.rel_path]}", "Done"
            if WONTDO_RE.match(issue.status_note):
                labels = ["wontdo"]
                note = rewrite_issue_body(issue.status_note, posixpath.dirname(issue.rel_path), ctx)
                final_summary = f"Abandoned before migration: {note}"
                wontdo.append(f"#{issue.number:03d} -> {task_id}: {issue.status_note}")
        elif folder == "drafts":
            draft_number += 1
            task_id = f"DRAFT-{draft_number}"
            drafts.append(f"#{issue.number:03d} -> {task_id}: {issue.title}")
        else:
            task_id = f"CR-{ids[issue.rel_path]}"
            status = triage["open"][str(issue.number)].get("status", "To Do")
        body = rewrite_issue_body(assemble_description(issue), posixpath.dirname(issue.rel_path), ctx)
        description = f"{body}\n\n{PROVENANCE_PREFIX}{issue.number:03d}."
        text = render_task(task_id=task_id, title=issue.title, status=status, created=issue.date,
                           labels=labels, description=description, type_=cr_type,
                           project=PROJECT, final_summary=final_summary)
        (backlog / folder / filename_for(task_id, issue.title)).write_text(text, encoding="utf-8")

    counts = expected_counts(issues, triage)
    sections = [
        ("Duplicate-number remaps", remaps),
        ("Type mappings (non-identity)", type_notes),
        ("Won't-do (abandoned or superseded)", wontdo),
        ("Drafts (lose their number; provenance line keeps it greppable)", drafts),
        ("Link findings", ctx.findings),
    ]
    lines = [f"# {PROJECT} migration report", "",
             f"Converted {len(issues)} files: {counts['completed']} -> completed/, "
             f"{counts['tasks']} -> tasks/, {counts['drafts']} -> drafts/.", ""]
    for title, items in sections:
        lines += [f"## {title}", ""] + ([f"- {item}" for item in items] or ["(none)"]) + [""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--tracker", required=True, type=Path)
    parser.add_argument("--triage", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args(argv)
    triage = json.loads(args.triage.read_text(encoding="utf-8"))
    report = convert(args.repo, args.tracker, triage)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report, encoding="utf-8")
    print(report.splitlines()[2])
    return 0


if __name__ == "__main__":
    sys.exit(main())
