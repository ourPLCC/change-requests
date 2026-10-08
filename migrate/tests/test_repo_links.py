import tempfile
import unittest
from pathlib import Path

from migrate import repo_links


class RepoLinksTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        issues = self.repo / "dev-docs" / "issues"
        (issues / "done").mkdir(parents=True)
        (issues / "160-race.md").write_text("# 160 - Race\n\n**Type:** fix\n**Date:** 2026-07-01\n\n## Description\n\nX [#161](161-x.md).\n")
        (self.repo / "dev-docs" / "specs").mkdir()
        self.spec = self.repo / "dev-docs" / "specs" / "s.md"
        self.spec.write_text("Issue: [#160](../issues/160-race.md)\nSee [conv](../issue-conventions.md).\n")
        (self.repo / "CHANGELOG.md").write_text("[#160](dev-docs/issues/160-race.md)\n")
        (self.repo / "CONTRIBUTING.md").write_text("[roadmap](dev-docs/roadmap.md)\n")

    def tearDown(self):
        self._tmp.cleanup()

    def test_target_files_exclude_tracker_and_changelog(self):
        names = sorted(p.relative_to(self.repo).as_posix() for p in repo_links.target_files(self.repo))
        self.assertEqual(names, ["CONTRIBUTING.md", "dev-docs/specs/s.md"])

    def test_rewrite_repo(self):
        changed, findings = repo_links.rewrite_repo(self.repo, "plcc-ng")
        self.assertEqual(sorted(changed), ["CONTRIBUTING.md", "dev-docs/specs/s.md"])
        self.assertEqual(self.spec.read_text(), "Issue: CR-160\nSee conv.\n")
        self.assertEqual((self.repo / "CONTRIBUTING.md").read_text(), "roadmap\n")
        self.assertIn("[#160]", (self.repo / "CHANGELOG.md").read_text())
        self.assertTrue(findings)

    def test_check_mode_writes_nothing(self):
        changed, _ = repo_links.rewrite_repo(self.repo, "plcc-ng", write=False)
        self.assertTrue(changed)
        self.assertIn("[#160]", self.spec.read_text())


if __name__ == "__main__":
    unittest.main()
