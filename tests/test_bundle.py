from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

EXPECTED_SKILLS = {
    "agent-harness-construction",
    "brainstorming",
    "brand-voice",
    "content-engine",
    "data-analyst",
    "emil-design-eng",
    "grilling",
    "handoff",
    "impeccable",
    "loop-design-check",
    "meeting-insights",
    "review-animations",
    "safety-guard",
    "slide-craft",
    "strategic-advisor",
    "teach",
    "to-questionnaire",
    "ui-ux-pro-max",
    "using-superpowers",
    "verification-before-completion",
    "wizard",
}

PRIVATE_MARKERS = (
    "/home/aegis",
    "agent-sveta",
    "vibe-aegis",
    "Светлан",
    "Лемана",
)


class BundleContractTest(unittest.TestCase):
    def test_exact_skill_manifest(self):
        actual = {
            path.name
            for path in SKILLS.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }
        self.assertEqual(EXPECTED_SKILLS, actual)
        self.assertEqual(21, len(actual))

    def test_every_skill_has_discoverable_frontmatter(self):
        for name in sorted(EXPECTED_SKILLS):
            skill_file = SKILLS / name / "SKILL.md"
            self.assertTrue(skill_file.is_file(), name)
            text = skill_file.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), name)
            frontmatter = text.split("---", 2)[1]
            self.assertRegex(frontmatter, rf"(?m)^name:\s*[\"']?{re.escape(name)}[\"']?\s*$")
            self.assertRegex(frontmatter, r"(?m)^description:\s*\S.+$")

    def test_router_lists_every_skill_once(self):
        index = (SKILLS / "_INDEX.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"^\| `([^`]+)` \|", index, flags=re.MULTILINE))
        self.assertEqual(EXPECTED_SKILLS, listed)

    def test_agent_architecture_is_complete(self):
        architecture = (ROOT / "AGENTS.template.md").read_text(encoding="utf-8")
        for required in (
            "## Шаг 0",
            "PDCA",
            "HANDOFF.md",
            "Уровень 1",
            "Уровень 2",
            "Уровень 3",
            "явного подтверждения",
            "провер",
        ):
            self.assertIn(required, architecture)

        setup = (ROOT / "AGENT-SETUP.md").read_text(encoding="utf-8")
        self.assertIn("21", setup)
        self.assertIn("AGENTS.template.md", setup)
        self.assertIn("не перезаписывай", setup.lower())

    def test_distributable_files_contain_no_private_markers(self):
        files = list(SKILLS.rglob("*")) + [
            ROOT / "AGENTS.template.md",
            ROOT / "AGENT-SETUP.md",
            ROOT / "README.md",
            ROOT / "THIRD_PARTY_NOTICES.md",
        ]
        for path in files:
            if not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".py", ".js", ".json", ".csv"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for marker in PRIVATE_MARKERS:
                self.assertNotIn(marker, text, f"{marker!r} found in {path.relative_to(ROOT)}")

    def test_proprietary_anthropic_material_is_not_bundled(self):
        for path in SKILLS.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            self.assertNotIn("Extract these materials from the Services", text, str(path))
            self.assertNotIn("Distribute, sublicense, or transfer these materials", text, str(path))

    def test_relative_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for markdown in SKILLS.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for raw_target in link_pattern.findall(text):
                target = raw_target.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:", "skill:", "/")):
                    continue
                target = target.strip("<>").replace("%20", " ")
                self.assertTrue(
                    (markdown.parent / target).exists(),
                    f"broken link in {markdown.relative_to(ROOT)}: {raw_target}",
                )


if __name__ == "__main__":
    unittest.main()
