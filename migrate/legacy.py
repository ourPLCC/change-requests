"""Parse one issue file in plcc-ng's legacy dev-docs/issues/ format."""
import re
from dataclasses import dataclass
from pathlib import Path

TITLE_RE = re.compile(r"^# (\d+) - (.+?)\s*$")
FILE_RE = re.compile(r"^(\d+)-(.+)\.md$")
FIELD_RE = re.compile(r"^\*\*(Type|Date|Status):\*\*\s*(.*?)\s*$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
TEMPLATE_COMMENT_RE = re.compile(r"<!--(?:(?!-->).)*Classify by user-facing impact.*?-->\n?", re.S)


@dataclass(frozen=True)
class LegacyIssue:
    number: int
    slug: str
    rel_path: str
    title: str
    type: str
    date: str
    status_note: str
    closed: bool
    preamble: str
    sections: tuple


def parse_issue(path, repo_root):
    path, repo_root = Path(path), Path(repo_root)
    text = TEMPLATE_COMMENT_RE.sub("", path.read_text(encoding="utf-8"), count=1)
    lines = text.splitlines()
    title_match = TITLE_RE.match(lines[0]) if lines else None
    file_match = FILE_RE.match(path.name)
    if not title_match or not file_match:
        raise ValueError(f"{path}: expected '# NNN - Title' and a NNN-slug.md filename")

    fields, preamble, sections = {}, [], []
    heading, buf, in_fence = None, [], False
    for line in lines[1:]:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            if heading is None:
                preamble = buf
            else:
                sections.append((heading, "\n".join(buf).strip("\n")))
            heading, buf = line[3:].strip(), []
            continue
        if heading is None and not in_fence:
            field = FIELD_RE.match(line)
            if field:
                fields[field.group(1)] = field.group(2)
                continue
        buf.append(line)
    if heading is None:
        preamble = buf
    else:
        sections.append((heading, "\n".join(buf).strip("\n")))

    raw_type = fields.get("Type", "").split()
    date = DATE_RE.search(fields.get("Date", ""))
    return LegacyIssue(
        number=int(file_match.group(1)),
        slug=file_match.group(2),
        rel_path=path.relative_to(repo_root).as_posix(),
        title=title_match.group(2),
        type=raw_type[0].lower().strip("`,.:;") if raw_type else "",
        date=date.group(0) if date else "",
        status_note=fields.get("Status", ""),
        closed="done" in path.relative_to(repo_root).parts,
        preamble="\n".join(preamble).strip("\n"),
        sections=tuple(sections),
    )
