import importlib.util
import unittest
from pathlib import Path

from migrate.emit import (TYPE_MAP, WONTDO_RE, assemble_description, demote_headings,
                          filename_for, render_task, slugify, yaml_quote)
from migrate.legacy import LegacyIssue

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("check", ROOT / "bin" / "check.py")
check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check)


def issue(**kw):
    base = dict(number=160, slug="race", rel_path="dev-docs/issues/160-race.md", title="Race",
                type="fix", date="2026-07-01", status_note="", closed=False, preamble="",
                sections=(("Description", "It races."),))
    base.update(kw)
    return LegacyIssue(**base)


class EmitTest(unittest.TestCase):
    def test_type_map(self):
        self.assertEqual(TYPE_MAP["bug"], "fix")
        self.assertEqual(TYPE_MAP["enhancement"], "feat")
        self.assertEqual(TYPE_MAP["feature"], "feat")
        self.assertEqual(TYPE_MAP["perf"], "fix")
        for t in ("fix", "feat", "docs", "test", "refactor", "chore"):
            self.assertEqual(TYPE_MAP[t], t)
        self.assertNotIn("warning", TYPE_MAP)

    def test_wontdo_re(self):
        self.assertTrue(WONTDO_RE.match("abandoned — not a priority"))
        self.assertTrue(WONTDO_RE.match("Superseded by #124"))
        self.assertFalse(WONTDO_RE.match(""))

    def test_slugify_and_filename(self):
        self.assertEqual(slugify("plcc-diagram: `x/y` (LL(1))"), "plcc-diagram-x-y-LL-1")
        self.assertEqual(filename_for("CR-160", "Race!"), "cr-160 - Race.md")
        self.assertEqual(filename_for("DRAFT-2", "Idea"), "draft-2 - Idea.md")

    def test_demote_headings_outside_fences_only(self):
        md = "### A\ntext\n```\n## code\n```\n#### B"
        self.assertEqual(demote_headings(md), "#### A\ntext\n```\n## code\n```\n##### B")

    def test_assemble_description_order_and_demotion(self):
        i = issue(preamble="**Supersedes:** #012",
                  sections=(("Description", "It races."),
                            ("Steps to Reproduce", "1. Go.\n\n### Detail\n\nX."),
                            ("Notes", "N.")))
        self.assertEqual(
            assemble_description(i),
            "**Supersedes:** #012\n\nIt races.\n\n### Steps to Reproduce\n\n1. Go.\n\n"
            "#### Detail\n\nX.\n\n### Notes\n\nN.")

    def test_render_done_wontdo_task(self):
        text = render_task(task_id="CR-111", title="Old", status="Done", created="2026-06-01",
                           labels=["wontdo"], description="D.", type_="feat", project="plcc-ng",
                           final_summary="Abandoned before migration: abandoned — x")
        fm = check.parse_frontmatter(text)
        self.assertEqual(fm["id"], "CR-111")
        self.assertEqual(fm["labels"], ["wontdo"])
        self.assertEqual(fm["type"], "feat")
        self.assertEqual(fm["project"], "plcc-ng")
        self.assertIn("<!-- SECTION:DESCRIPTION:BEGIN -->\nD.\n<!-- SECTION:DESCRIPTION:END -->", text)
        self.assertIn("## Final Summary\n\n<!-- SECTION:FINAL_SUMMARY:BEGIN -->\n"
                      "Abandoned before migration: abandoned — x\n"
                      "<!-- SECTION:FINAL_SUMMARY:END -->", text)

    def test_title_with_yaml_specials_round_trips(self):
        title = "plcc-diagram: `x` isn't #1 — 'quoted'"
        text = render_task(task_id="CR-5", title=title, status="To Do", created="2026-01-01",
                           labels=[], description="D.", type_="fix", project="plcc-ng")
        self.assertEqual(check.parse_frontmatter(text)["title"], title)
        self.assertEqual(yaml_quote("a'b"), "'a''b'")

    def test_render_omits_absent_optional_fields(self):
        text = render_task(task_id="DRAFT-1", title="Idea", status="To Do", created="2026-01-01",
                           labels=[], description="D.")
        fm = check.parse_frontmatter(text)
        self.assertNotIn("type", fm)
        self.assertNotIn("project", fm)
        self.assertNotIn("Final Summary", text)


if __name__ == "__main__":
    unittest.main()
