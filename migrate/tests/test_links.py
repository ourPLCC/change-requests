import tempfile
import unittest
from pathlib import Path

from migrate.links import IssueRef, LinkContext, rewrite_issue_body, rewrite_repo_doc


class LinksTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        (self.repo / "src" / "plcc").mkdir(parents=True)
        (self.repo / "src" / "plcc" / "emit.py").write_text("")
        (self.repo / "dev-docs" / "specs").mkdir(parents=True)
        (self.repo / "dev-docs" / "specs" / "2026-07-01-x-design.md").write_text("")
        self.ctx = LinkContext(
            repo="plcc-ng", repo_root=self.repo,
            issues={
                160: [IssueRef("race", 160)],
                35: [IssueRef("plcc-diagram-hangs", 35), IssueRef("python-emitter-blocks", 435)],
                165: [IssueRef("real-165", 165)],
            },
            other_offsets={"languages-ng": 500, "plcc-ng-demo": 800},
            github="https://github.com/ourPLCC/plcc-ng",
        )

    def tearDown(self):
        self._tmp.cleanup()

    def body(self, text, file_dir="dev-docs/issues/done"):
        return rewrite_issue_body(text, file_dir, self.ctx)

    def test_issue_link_with_number_text_becomes_bare_id(self):
        self.assertEqual(self.body("See [#160](../160-race.md)."), "See CR-160.")

    def test_issue_link_with_prose_text_keeps_text(self):
        self.assertEqual(self.body("See [the race](../160-race.md)."), "See the race (CR-160).")

    def test_duplicate_number_resolved_by_slug(self):
        self.assertEqual(self.body("[#035](035-python-emitter-blocks.md)"), "CR-435")

    def test_slug_mismatch_still_rewritten_and_reported(self):
        self.assertEqual(self.body("[#165](../165-other-thing.md)"), "CR-165")
        self.assertTrue(any("slug mismatch" in f for f in self.ctx.findings))

    def test_broken_issue_link_left_and_reported(self):
        self.assertEqual(self.body("[#170](../170-gone.md)"), "[#170](../170-gone.md)")
        self.assertTrue(any("broken issue link" in f for f in self.ctx.findings))

    def test_code_link_rewritten_to_sibling_layout(self):
        self.assertEqual(self.body("[emit](../../../src/plcc/emit.py#L3)"),
                         "[emit](../../../plcc-ng/src/plcc/emit.py#L3)")

    def test_spec_link_is_not_mistaken_for_issue(self):
        self.assertEqual(self.body("[s](../../specs/2026-07-01-x-design.md)"),
                         "[s](../../../plcc-ng/dev-docs/specs/2026-07-01-x-design.md)")

    def test_link_written_before_move_to_done_resolves_best_effort(self):
        self.assertEqual(self.body("[emit](../../src/plcc/emit.py)"),
                         "[emit](../../../plcc-ng/src/plcc/emit.py)")

    def test_unresolved_code_link_left_and_reported(self):
        self.assertEqual(self.body("[x](../../nope.py)"), "[x](../../nope.py)")
        self.assertTrue(any("unresolved link" in f for f in self.ctx.findings))

    def test_retired_tracker_file_link_becomes_text(self):
        self.assertEqual(self.body("see [the roadmap](../../roadmap.md)"), "see the roadmap")
        self.assertTrue(any("retired" in f for f in self.ctx.findings))

    def test_external_and_anchor_links_untouched(self):
        text = "[a](https://x.org/#160) and [b](#notes)"
        self.assertEqual(self.body(text), text)

    def test_bare_number_rewritten_zero_padding_stripped(self):
        self.assertEqual(self.body("Fixed by #160 and #0160."), "Fixed by CR-160 and CR-160.")

    def test_bare_ambiguous_number_reported(self):
        self.assertEqual(self.body("Like #035."), "Like CR-35.")
        self.assertTrue(any("ambiguous" in f for f in self.ctx.findings))

    def test_unknown_bare_number_becomes_github_link(self):
        self.assertEqual(self.body("PR #284 merged."),
                         "PR [#284](https://github.com/ourPLCC/plcc-ng/issues/284) merged.")

    def test_qualified_cross_repo_mention_uses_that_offset(self):
        self.assertEqual(self.body("Originally filed as issue #3 in `ourPLCC/languages-ng`."),
                         "Originally filed as issue CR-503 in `ourPLCC/languages-ng`.")
        self.assertEqual(self.body("plcc-ng-demo's #2 too"), "plcc-ng-demo's CR-802 too")

    def test_github_qualified_reference_untouched(self):
        self.assertEqual(self.body("See ourPLCC/plcc-ng#284."), "See ourPLCC/plcc-ng#284.")

    def test_fenced_code_untouched(self):
        text = "Before #160.\n```text\n#160 [x](../160-race.md)\n```\nAfter."
        self.assertEqual(self.body(text), "Before CR-160.\n```text\n#160 [x](../160-race.md)\n```\nAfter.")

    def test_inline_code_untouched(self):
        self.assertEqual(self.body("but `#160's link` and #160"), "but `#160's link` and CR-160")

    def test_html_entity_untouched(self):
        self.assertEqual(self.body("&#160;"), "&#160;")

    def test_repo_doc_rewrites_only_issue_and_retired_links(self):
        text = ("Issue: [#160](../issues/160-race.md)\n"
                "[conv](../issue-conventions.md) [emit](../../src/plcc/emit.py) #160")
        out = rewrite_repo_doc(text, "dev-docs/specs", self.ctx)
        self.assertEqual(out, "Issue: CR-160\nconv [emit](../../src/plcc/emit.py) #160")


if __name__ == "__main__":
    unittest.main()
