import shutil
import dataclasses
import tempfile
import textwrap
import unittest
from pathlib import Path

from migrate import plcc_ng


def legacy(number, title, type_="fix", status="", body="Body."):
    status_line = f"**Status:** {status}\n" if status else ""
    return textwrap.dedent(f"""\
        # {number:03d} - {title}

        **Type:** {type_}
        **Date:** 2026-07-01
        """) + status_line + f"\n## Description\n\n{body}\n\n## Notes\n\nN.\n"


class ConvertTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        self.repo, self.tracker = base / "plcc-ng", base / "issues"
        issues = self.repo / "dev-docs" / "issues"
        (issues / "done").mkdir(parents=True)
        files = {
            issues / "done" / "035-plcc-diagram-hangs.md": legacy(35, "Diagram hangs", "bug"),
            issues / "done" / "035-python-emitter-blocks.md": legacy(35, "Emitter: blocks", "feature"),
            issues / "done" / "111-mermaid.md": legacy(111, "Mermaid", "feat", "abandoned — superseded by #160"),
            issues / "160-race.md": legacy(160, "Race", "fix", body="Like #035 and [#111](done/111-mermaid.md)."),
            issues / "161-rename.md": legacy(161, "Rename?", "enhancement"),
        }
        for path, text in files.items():
            path.write_text(text)
        for folder in ("tasks", "completed", "drafts"):
            (self.tracker / "backlog" / folder).mkdir(parents=True)
        self.triage = {"open": {"160": {"as": "cr", "status": "In Progress", "reason": "r"},
                                "161": {"as": "draft", "reason": "r"}}}

    def tearDown(self):
        self._tmp.cleanup()

    def files(self, folder):
        return sorted(p.name for p in (self.tracker / "backlog" / folder).glob("*.md"))

    def test_assign_ids_remaps_second_duplicate(self):
        issues = plcc_ng.load_issues(self.repo)
        ids, remaps = plcc_ng.assign_ids(issues)
        self.assertEqual(ids["dev-docs/issues/done/035-plcc-diagram-hangs.md"], 35)
        self.assertEqual(ids["dev-docs/issues/done/035-python-emitter-blocks.md"], 435)
        self.assertEqual(len(remaps), 1)

    def test_assign_ids_guards_remap_range(self):
        issues = plcc_ng.load_issues(self.repo)[:2]
        issues = [dataclasses.replace(issues[0], number=150),
                  dataclasses.replace(issues[1], number=150)]
        with self.assertRaises(SystemExit) as cm:
            plcc_ng.assign_ids(issues)
        self.assertIn("499", str(cm.exception))

    def test_assign_ids_remaps_duplicate_into_other_repos_range(self):
        issues = plcc_ng.load_issues(self.repo)[:2]
        issues = [dataclasses.replace(i, number=12) for i in issues]
        ids, remaps = plcc_ng.assign_ids(issues, offset=500, dup_offset=100,
                                         dup_range=range(600, 700))
        self.assertEqual(sorted(ids.values()), [512, 612])
        self.assertIn("CR-612", remaps[0])

    def test_assign_ids_guards_other_repos_range(self):
        issues = plcc_ng.load_issues(self.repo)[:2]
        issues = [dataclasses.replace(i, number=150) for i in issues]
        with self.assertRaises(SystemExit) as cm:
            plcc_ng.assign_ids(issues, offset=500, dup_offset=100, dup_range=range(600, 700))
        self.assertIn("CR-750", str(cm.exception))
        self.assertIn("CR-600..CR-699", str(cm.exception))

    def test_convert_places_files_by_state(self):
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertEqual(self.files("completed"),
                         ["cr-111 - Mermaid.md", "cr-35 - Diagram-hangs.md", "cr-435 - Emitter-blocks.md"])
        self.assertEqual(self.files("tasks"), ["cr-160 - Race.md"])
        self.assertEqual(self.files("drafts"), ["draft-1 - Rename.md"])

    def test_convert_content(self):
        report = plcc_ng.convert(self.repo, self.tracker, self.triage)
        race = (self.tracker / "backlog" / "tasks" / "cr-160 - Race.md").read_text()
        self.assertIn("status: In Progress", race)
        self.assertIn("type: fix", race)
        self.assertIn("project: plcc-ng", race)
        self.assertIn("Like CR-35 and CR-111.", race)
        self.assertIn("### Notes", race)
        self.assertIn("Migrated from plcc-ng #160.", race)
        mermaid = (self.tracker / "backlog" / "completed" / "cr-111 - Mermaid.md").read_text()
        self.assertIn("  - wontdo", mermaid)
        self.assertIn("Abandoned before migration: abandoned — superseded by CR-160", mermaid)
        emitter = (self.tracker / "backlog" / "completed" / "cr-435 - Emitter-blocks.md").read_text()
        self.assertIn("type: feat", emitter)
        self.assertIn("CR-435", report)
        self.assertIn("ambiguous", report)

    def test_untriaged_open_issue_is_an_error(self):
        with self.assertRaises(SystemExit):
            plcc_ng.convert(self.repo, self.tracker, {"open": {"160": {"as": "cr"}}})

    def test_unmapped_type_needs_override(self):
        (self.repo / "dev-docs/issues/done/050-w.md").write_text(legacy(50, "W", "warning"))
        with self.assertRaises(SystemExit):
            plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.triage["type_overrides"] = {"50": "chore"}
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertIn("cr-50 - W.md", self.files("completed"))

    def test_type_override_by_stem_targets_one_duplicate(self):
        self.triage["type_overrides"] = {"035-plcc-diagram-hangs": "chore"}
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        completed = self.tracker / "backlog" / "completed"
        self.assertIn("type: chore", (completed / "cr-35 - Diagram-hangs.md").read_text())
        self.assertIn("type: feat", (completed / "cr-435 - Emitter-blocks.md").read_text())

    def test_number_key_for_duplicated_number_is_an_error(self):
        self.triage["type_overrides"] = {"35": "chore"}
        with self.assertRaises(SystemExit) as cm:
            plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertIn("035-plcc-diagram-hangs", str(cm.exception))

    def add_open_duplicates(self):
        issues = self.repo / "dev-docs" / "issues"
        (issues / "070-alpha.md").write_text(legacy(70, "Alpha"))
        (issues / "070-beta.md").write_text(legacy(70, "Beta"))

    def test_open_entry_by_stem_targets_one_duplicate(self):
        self.add_open_duplicates()
        self.triage["open"].update({"070-alpha": {"as": "cr", "status": "In Progress", "reason": "r"},
                                    "070-beta": {"as": "draft", "reason": "r"}})
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertEqual(self.files("tasks"), ["cr-160 - Race.md", "cr-70 - Alpha.md"])
        self.assertEqual(self.files("drafts"), ["draft-1 - Beta.md", "draft-2 - Rename.md"])
        alpha = (self.tracker / "backlog" / "tasks" / "cr-70 - Alpha.md").read_text()
        self.assertIn("status: In Progress", alpha)

    def test_open_number_key_for_duplicated_number_is_an_error(self):
        self.add_open_duplicates()
        self.triage["open"]["70"] = {"as": "cr", "reason": "r"}
        with self.assertRaises(SystemExit) as cm:
            plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertIn("070-alpha", str(cm.exception))

    def test_rerun_replaces_previous_output_only(self):
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        other = self.tracker / "backlog" / "tasks" / "cr-1000 - New.md"
        other.write_text("---\nid: CR-1000\ntitle: New\n---\n")
        (self.repo / "dev-docs/issues/161-rename.md").unlink()
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertEqual(self.files("tasks"), ["cr-1000 - New.md", "cr-160 - Race.md"])
        self.assertEqual(self.files("drafts"), [])
        self.assertTrue(other.exists())

    def test_rerun_keeps_cr_that_quotes_provenance_line(self):
        quoting = self.tracker / "backlog" / "tasks" / "cr-1001 - Quote.md"
        quoting.write_text(
            "---\nid: CR-1001\ntitle: Quote\n---\n\n## Description\n\n"
            "<!-- SECTION:DESCRIPTION:BEGIN -->\nCR-160 ends with \"Migrated from plcc-ng #160.\"\n"
            "Migrated from plcc-ng #160.\n\nMore text.\n<!-- SECTION:DESCRIPTION:END -->\n\n"
            "## Implementation Notes\n\n<!-- SECTION:NOTES:BEGIN -->\nMigrated from plcc-ng #160.\n"
            "<!-- SECTION:NOTES:END -->\n")
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertTrue(quoting.exists())

    def test_rerun_removes_previously_migrated_cr(self):
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        race = self.tracker / "backlog" / "tasks" / "cr-160 - Race.md"
        moved = race.with_name("cr-160 - Old-title.md")
        race.rename(moved)
        plcc_ng.convert(self.repo, self.tracker, self.triage)
        self.assertFalse(moved.exists())
        self.assertEqual(self.files("tasks"), ["cr-160 - Race.md"])

    def test_expected_counts(self):
        issues = plcc_ng.load_issues(self.repo)
        self.assertEqual(plcc_ng.expected_counts(issues, self.triage),
                         {"tasks": 1, "completed": 3, "drafts": 1})


if __name__ == "__main__":
    unittest.main()
