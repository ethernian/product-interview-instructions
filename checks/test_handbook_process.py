import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HandbookProcessTest(unittest.TestCase):
    def test_cross_stage_rules_are_preserved_in_process(self):
        handbook = (ROOT / "stages/Product-Development-Handbook.md").read_text()
        process = handbook.split("## 2. How the Process Works", 1)[1].split("## 3. Development Stages", 1)[0]
        for rule in (
            "Verify each stage's outputs against its inputs, applicable patterns, and completion criteria; return defects to the responsible stage for correction.",
            "An actor with the necessary authority accepts outputs against defined criteria. Verification does not confer acceptance authority, and acceptance on another actor's behalf requires explicit delegation.",
            "When an artifact changes, identify affected dependencies, regenerate necessary outputs, and repeat verification. Do not automatically modify confirmed decisions.",
            "Maintain bidirectional links between sources, requirements, decisions, tasks, implementation, and tests.",
            "Record the patterns used and the rationale for their selection.",
            "Version artifacts, instructions, and resources so that the input and rule versions used to produce each output can be determined.",
            "Release only accepted outputs.",
            "Route operational data, defects, and new needs to the appropriate stages through change management.",
            "A sub-project stage inherits inputs from the corresponding stage at the parent level, if one exists. If there is no corresponding parent stage, define its inputs explicitly in the sub-project's stage description.",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, process)
        self.assertNotIn("Rules Applied Across Stages", handbook)
        self.assertIn("#3-development-stages", process)
