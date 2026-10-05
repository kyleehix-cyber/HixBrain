"""Guards for the account-brief workflow wiring: every file the skill relies on
exists, and the deck prompt template keeps its 8-slide agenda."""
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


class PackageWiringTest(unittest.TestCase):
    def test_skill_references_existing_files(self):
        skill = read(".claude/skills/account-brief/SKILL.md")
        for rel in set(re.findall(r"`((?:templates|playbooks)/[\w./-]+\.md|seller_profile\.yaml)`", skill)):
            with self.subTest(rel=rel):
                self.assertTrue(os.path.exists(os.path.join(ROOT, rel)), rel)

    def test_deck_prompt_is_a_default_deliverable(self):
        skill = read(".claude/skills/account-brief/SKILL.md")
        self.assertIn("--no-deck", skill)
        self.assertIn("discovery-deck-prompt.md", skill)
        self.assertNotIn("Discovery deck prompt (when asked)", skill)

    def test_deck_template_has_eight_slides(self):
        tpl = read("templates/discovery_deck_prompt.md")
        self.assertEqual(re.findall(r"^### Slide (\d)", tpl, re.M), [str(i) for i in range(1, 9)])

    def test_seller_profile_has_deepgram_facts(self):
        try:
            import yaml
        except ImportError:
            self.skipTest("pip install pyyaml")
        profile = yaml.safe_load(read("seller_profile.yaml"))
        facts = profile["deepgram_facts"]
        self.assertIn("as_of", facts)
        self.assertTrue(all(s.get("source", "").startswith("https://") for s in facts["stats"]))


if __name__ == "__main__":
    unittest.main()
