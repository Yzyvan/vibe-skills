from pathlib import Path
import unittest


SKILL = Path(__file__).with_name("SKILL.md")


class BrainstormingSkillContractTests(unittest.TestCase):
    def test_one_owner_approval_starts_implementation_planning(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("One Approval Rule", text)
        self.assertIn("Do not ask the user to approve the written spec again", text)
        self.assertNotIn("User reviews spec?", text)
        self.assertNotIn("User Review Gate", text)


if __name__ == "__main__":
    unittest.main()
