import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "build_delivery", REPO / "scripts/build-delivery.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BuildDeliveryTests(unittest.TestCase):
    def test_size_limit(self):
        self.assertIsNone(builder.size_error(builder.MAX_BYTES - 1))
        self.assertIn("menos de", builder.size_error(builder.MAX_BYTES))

    def test_annexes_ordered_without_template_or_frontmatter(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "plan/annexes"
            folder.mkdir(parents=True)
            for name in ("02-b.md", "01-a.md", "_template.md"):
                (folder / name).write_text(
                    f"---\nowner: finance\nstatus: draft\ntitle: T\n---\n# {name}\n",
                    encoding="utf-8",
                )
            markdown = builder.annexes_markdown(root, builder.load_plan_check())
        self.assertLess(markdown.index("# 01-a.md"), markdown.index("# 02-b.md"))
        self.assertNotIn("_template", markdown)
        self.assertNotIn("owner:", markdown)
        self.assertEqual(markdown.count("page-break-before"), 1)


if __name__ == "__main__":
    unittest.main()
