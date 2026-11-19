import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StageLayoutTest(unittest.TestCase):
    def test_discovery_invocation_and_resources(self):
        stage = ROOT / "stages/01-discovery"
        readme = (stage / "README.md").read_text()
        for argument in ("Input Documents: `inputs/`", "Solution Library: `resources/`", "OutputDocuments: `outputs/`"):
            with self.subTest(argument=argument):
                self.assertIn(argument, readme)
        self.assertTrue((stage / "resources/Product-Discovery-Catalog.md").is_file())
        self.assertTrue((ROOT / "stages/02-requirements/resources/Requirements-Management-Resources.md").is_file())
        self.assertIn("stages/01-discovery/resources/Product-Discovery-Catalog.md", (ROOT / "README.md").read_text())

    def test_inputs_are_ignored(self):
        self.assertIn("inputs/", (ROOT / "stages/.gitignore").read_text().splitlines())
        result = subprocess.run(
            ["git", "check-ignore", "stages/01-discovery/inputs/example.txt"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
