import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AppReadmeTest(unittest.TestCase):
    def test_template_covers_scope_and_existing_workflows(self):
        readme = (ROOT / "app/README.md").read_text()
        for expected in (
            "specific product, a product sub-module, or an individual product development stage",
            "README.md` at the root",
            "**Scope type:**",
        ):
            self.assertIn(expected, readme)
        for expected in (
            "app/Product-Interview-Instructions.md",
            "app/Product-Information-Management-Instructions.md",
            "app/Artifact-Data-Formats.md",
            "app/UX-Guide.md",
        ):
            with self.subTest(path=expected):
                self.assertIn(expected, readme)
                self.assertTrue((ROOT / expected).is_file())
        for expected in (
            "explicitly authorized delegate",
            "without the owner's authorization",
            "how relative paths are resolved",
            "project's development stages and their resources are separate from the add-on",
            "project's own process descriptions and resources",
            "resume existing artifacts instead of overwriting them",
            "do not treat verification alone as acceptance",
            "do not automatically modify confirmed decisions",
        ):
            with self.subTest(rule=expected):
                self.assertIn(expected.lower(), readme.lower())
        self.assertNotIn("stages/", readme)
        self.assertNotIn("Product-Development-Handbook.md", readme)
