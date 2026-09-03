import unittest

from scripts.update_recently_shipped import (
    item_from_commit,
    item_from_release,
    render_items,
    replace_block,
)

SAMPLE = """before
<!-- RECENTLY-SHIPPED:START -->
old
<!-- RECENTLY-SHIPPED:END -->
after
"""


class UpdateRecentlyShippedTests(unittest.TestCase):
    def test_replace_block_preserves_outside_exactly(self):
        updated = replace_block(SAMPLE, "new")
        self.assertEqual(
            updated,
            "before\n<!-- RECENTLY-SHIPPED:START -->\nnew\n<!-- RECENTLY-SHIPPED:END -->\nafter\n",
        )

    def test_replace_block_requires_markers(self):
        with self.assertRaises(ValueError):
            replace_block("no markers here\n", "new")

    def test_replace_block_is_idempotent(self):
        once = replace_block(SAMPLE, "new")
        twice = replace_block(once, "new")
        self.assertEqual(twice, once)

    def test_item_from_release(self):
        item = item_from_release(
            "ShapArt/tessa-matrix-studio",
            {
                "tag_name": "v1.9.51",
                "name": "TESSA Matrix Studio v1.9.51\nextra",
                "html_url": "https://github.com/ShapArt/tessa-matrix-studio/releases/tag/v1.9.51",
                "published_at": "2026-09-02T19:13:28Z",
            },
        )
        self.assertEqual(item["label"], "v1.9.51")
        self.assertEqual(item["date"], "2026-09-02")
        self.assertEqual(item["title"], "TESSA Matrix Studio v1.9.51")

    def test_item_from_commit(self):
        item = item_from_commit(
            "ShapArt/eyegate-l-luckfox-scud",
            {
                "sha": "1234567890abcdef",
                "html_url": "https://github.com/ShapArt/eyegate-l-luckfox-scud/commit/1234567890abcdef",
                "commit": {
                    "message": "Fix camera lifecycle\nlong body",
                    "committer": {"date": "2026-08-30T10:20:30Z"},
                },
            },
        )
        self.assertEqual(item["label"], "1234567")
        self.assertEqual(item["date"], "2026-08-30")
        self.assertEqual(item["title"], "Fix camera lifecycle")

    def test_render_items_newest_first(self):
        items = [
            {
                "name": "Older",
                "url": "https://github.com/x/older",
                "label": "v1",
                "date": "2026-08-01",
                "title": "old",
                "sort_key": "2026-08-01T00:00:00Z",
            },
            {
                "name": "Newer",
                "url": "https://github.com/x/newer",
                "label": "v2",
                "date": "2026-09-01",
                "title": "new",
                "sort_key": "2026-09-01T00:00:00Z",
            },
        ]
        rendered = render_items(items)
        self.assertLess(rendered.index("Newer"), rendered.index("Older"))


if __name__ == "__main__":
    unittest.main()
