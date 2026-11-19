import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InstructionSplitTest(unittest.TestCase):
    def test_product_development_principles_are_preserved_and_referenced(self):
        handbook = (ROOT / "stages/Product-Development-Handbook.md").read_text()
        instructions = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        self.assertIn("Product-Information-Management-Instructions.md", handbook)
        section = instructions.split("## 4. Product Development Principles", 1)[1].split("## ", 1)[0]
        for rule in (
            "Keep source information, requirements, architecture, and implementation separate. An artifact may have multiple sources.",
            "Link derived artifacts to their sources using stable identifiers, and maintain those links when changes occur.",
            "Define objective verification criteria for every output and document the justification for selected solutions.",
            "Missing information and contradictions block only activities that critically depend on them.",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, section)
                self.assertNotIn(rule, handbook)
        self.assertNotIn("Each artifact has a single authoritative source", handbook)
        self.assertIn("Product-Interview-Instructions.md", handbook)

    def test_processing_priorities_are_preserved_and_referenced(self):
        handbook = (ROOT / "stages/Product-Development-Handbook.md").read_text()
        instructions = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        self.assertIn("Product-Information-Management-Instructions.md", handbook)
        section = instructions.split("## 3. Processing Priorities", 1)[1].split("## ", 1)[0]
        for rule in (
            "Prioritize questions and requests that significantly affect dependent decisions. Record unknown parameters explicitly.",
            "Identify contradictions and costly-to-change decisions before executing dependent work.",
            "AI agents perform as much necessary work as their capabilities and authority allow. Involve humans only when their information, judgment, or authority is needed, and minimize their effort.",
            "Eliminate independently maintained duplicates and enable automatic updates of dependent artifacts.",
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
        self.assertIn("Product-Information-Management-Instructions.md#8-decision-management-and-conflict-resolution", formats)
        for rule in (
            "Follow [Artifact-Data-Formats.md](Artifact-Data-Formats.md) as the authoritative reference for Q&A registry fields, formats, statuses, and storage rules",
            "Others must not change an owned item without the owner's authorization",
            "An actor may confirm an item on another actor's behalf only with that actor's explicit delegation",
            "Store the current Q&A registry in `qa-registry.json`",
            "using a new sequential filename for each completed round",
            "without treating proposals as confirmed decisions",
            "Record each established requirement separately",
            "When the owner requests a product specification",
            "Use only confirmed input, expose gaps and conflicts, and preserve traceability",
            "The owner decides when the specification is complete",
            "provided those decisions introduce no new conflicts or other issues",
            "the actors responsible for the affected requirements must then resolve those conflicts",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, requirements)
        self.assertIn("Accept \"I don't know\" as a valid answer", interview)
        self.assertIn("Every question must influence requirements or subsequent decisions", interview)
        self.assertIn("## Minimize Human Effort", interview)
        self.assertIn("## Question Relevance", interview)
        self.assertIn("Product-Interview-Instructions.md", handbook)
        self.assertNotIn("## 2. Core Principles", handbook)
