import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProductInformationRegistryTest(unittest.TestCase):
    def setUp(self):
        self.formats = (ROOT / "app/Artifact-Data-Formats.md").read_text()
        self.information = (ROOT / "app/Product-Information-Management-Instructions.md").read_text()
        self.interview = (ROOT / "app/Product-Interview-Instructions.md").read_text()
        self.ux = (ROOT / "app/UX-Guide.md").read_text()

    def test_example_matches_both_record_schemas(self):
        registry = json.loads(self.formats.split("```json\n", 1)[1].split("```", 1)[0])
        self.assertEqual(set(registry), {"product_id", "records"})
        questions = self.formats.split("### Question Records", 1)[1].split("### Decision Records", 1)[0]
        decisions = self.formats.split("### Decision Records", 1)[1].split("### Example Registry", 1)[0]
        fields = {
            kind: set(re.findall(r"^\| `([^`]+)` \|", section, re.MULTILINE))
            for kind, section in (("question", questions), ("decision", decisions))
        }
        records = registry["records"]
        self.assertEqual({record["type"] for record in records}, {"question", "decision"})
        self.assertEqual(len({record["id"] for record in records}), len(records))
        for record in records:
            with self.subTest(record=record["id"]):
                self.assertEqual(set(record), fields[record["type"]])
        question = next(record for record in records if record["type"] == "question")
        decision = next(record for record in records if record["type"] == "decision")
        self.assertEqual(question["status"], "answered")
        self.assertIsInstance(question["proposed_answer"], str)
        self.assertNotEqual(question["user_answer"], question["proposed_answer"])
        self.assertEqual(decision["decision_status"], "proposed")
        self.assertIn(question["id"], decision["source_refs"])
        self.assertIsInstance(question["interpreted_as"], list)
        self.assertIsInstance(question["interpretation_note"], str)
        self.assertIsNone(decision["confirmation_source"])

    def test_authority_interpretation_and_migration_guards(self):
        for rule in (
            "not owner approval, a decision status, or verification",
            "Multiple labels are allowed",
            "do not force one interpretation onto the entire answer",
            "A clear decision made directly by an authorized owner does not require a second confirmation",
            "Do not infer authorization or confirmation from an answer's completeness",
            "not independently verified merely because it was answered",
            "Preserve the original files and snapshots",
            "Prepare the imported registry separately and verify it against its sources before writing it to the new location",
            "without changing IDs, owner answers, decision statuses, authority evidence, source links, or history",
            "Preserve unmapped legacy fields",
            "Preserve an unknown legacy status in `legacy_data` and ask the responsible actor how to map it",
            "If a unified registry already exists alongside legacy records",
            "ID collisions, or mappings cannot be resolved safely",
            "Legacy snapshots remain available as history",
            "Share the unified registry and snapshots only with actors authorized to access their contents",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, self.formats)
        self.assertIn("explicitly authorized delegate", self.information)
        self.assertIn("answer completeness alone does not confirm a proposal or verify a fact", self.information)
        self.assertIn("Allow the owner to provide a direct answer when no proposal exists", self.ux)
        self.assertIn('**"Submit Round"**', self.ux)
        self.assertIn("Submission alone does not confirm a proposed decision", self.ux)
        self.assertIn("Record an owner's correction to the interpretation without changing their answer", self.formats)
        self.assertIn("find related decisions from a question by searching `source_refs`", self.formats)

    def test_one_registry_rounds_handoff_and_statuses(self):
        self.assertIn("one versioned Product Information Registry per product, shared across stages", self.formats)
        self.assertIn("Other stages must use the same registry, not create stage-local copies", self.formats)
        self.assertIn("If a configured registry is missing or unreadable, report it and ask the responsible actor before creating a replacement", self.formats)
        self.assertIn("product-information-registry.json", self.information)
        self.assertIn("ProductInformationRegistry", self.interview)
        self.assertIn("#product-information-registry-record-structure", self.interview)
        handbook = (ROOT / "stages/Product-Development-Handbook.md").read_text()
        overview = handbook.split("### Stage Overview", 1)[1]
        self.assertIn("product's configured shared Product Information Registry", overview)
        self.assertIn("Do not create a separate stage-local decision registry", overview)
        self.assertIn("snapshot after registry records change outside an interview round", self.formats)
        self.assertIn("Do not claim that a snapshot was saved without a successful save", self.formats)
        self.assertIn("mark the answer `partially_answered` when required information is still missing", self.formats)
        self.assertIn("interpret legacy `unexplored`, `partially defined`, `defined`, and `not applicable` values", self.formats)
        for status in ("`unknown`", "`partial`", "`done`", "`n/a`"):
            with self.subTest(status=status):
                self.assertIn(status, self.formats.split("## Coverage Map Entry Structure", 1)[1])
