import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InformationHeadingsTest(unittest.TestCase):
    def test_lists_use_sequential_numbers(self):
        instructions = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        self.assertNotRegex(instructions, r"(?m)^[-*+] ")
        for section, expected in (("5. Interview Artifact Handling", 4), ("6. Traceability", 5)):
            content = instructions.split(f"## {section}", 1)[1].split("## ", 1)[0]
            numbers = re.findall(r"^(\d+)\. ", content, re.MULTILINE)
            self.assertEqual([int(number) for number in numbers], list(range(1, expected + 1)))

    def test_sections_and_decision_link(self):
        instructions = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        headings = re.findall(r"^## (\d+)\. (.+)$", instructions, re.MULTILINE)
        self.assertEqual([int(number) for number, _ in headings], list(range(1, 9)))
        self.assertEqual(headings[-1][1], "Decision Management and Conflict Resolution")
        formats = (ROOT / "app/Artifact-Data-Formats.md").read_text()
        self.assertIn("Product-Information-Management-Instructions.md#8-decision-management-and-conflict-resolution", formats)
