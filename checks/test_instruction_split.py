import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InstructionSplitTest(unittest.TestCase):
    def test_processing_priorities_are_preserved_and_referenced(self):
        handbook = (ROOT / "stages/Product-Development-Handbook.md").read_text()
        instructions = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        self.assertIn("Product-Information-Management-Instructions.md#processing-priorities", handbook)
        section = instructions.split("## Processing Priorities", 1)[1].split("## ", 1)[0]
        for rule in (
            "Prioritize questions and requests that significantly affect dependent decisions. Record unknown parameters explicitly.",
            "Identify contradictions and costly-to-change decisions before executing dependent work.",
            "AI Agents take on the largest possible share of necessary work within their capabilities and authority. Involve Human Actors only when their information, judgment, or authority is needed, while minimizing the effort required from them.",
            "Eliminate independently maintained duplicates of information. Enable automatic updates of dependent artifacts.",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, section)
                self.assertNotIn(rule, handbook)

    def test_moved_rules_remain_reachable_and_keep_their_guards(self):
        interview = (ROOT / "app/Product-Interview-Instructions.md").read_text()
        handbook = (ROOT / "stages/Product-Development-Handbook.md").read_text()
        requirements = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        formats = (ROOT / "app/Artifact-Data-Formats.md").read_text()
        for entry in (interview, handbook):
            self.assertIn("Product-Information-Management-Instructions.md", entry)
        self.assertIn("Product-Information-Management-Instructions.md#decision-management-and-conflict-resolution", formats)
        for rule in (
            "can't be changed by others without the owner’s authorization",
            "No actor may confirm an item in another actor's name without explicit delegation",
            "Store the current Q&A registry in `qa-registry.json`",
            "using a new sequential filename for each completed round",
            "without treating proposals as confirmed decisions",
            "Record each established requirement as a separate entry",
            "When the owner requests a product specification",
            "Use confirmed input only; expose gaps and conflicts; ensure traceability",
            "The owner decides when it is complete",
            "provided those decisions introduce no new conflicts or other issues",
            "The Actors responsible for the affected requirements must then resolve those conflicts",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, requirements)
        self.assertIn("Accept \"I don't know\" as a valid answer", interview)
        self.assertIn("Every question must influence requirements or subsequent decisions", interview)
        self.assertIn("#minimize-human-effort", handbook)
        self.assertIn("#question-relevance", handbook)
