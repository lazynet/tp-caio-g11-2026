"""Regresiones de portabilidad, ownership y vigencia de los adaptadores."""

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = Path(os.environ.get("HARNESS_CHECK_SCRIPT", REPO / "scripts/harness-check.py"))
spec = importlib.util.spec_from_file_location("harness_check", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(REPO / ".claude/agents", self.root / ".claude/agents")
        shutil.copytree(REPO / ".agents/skills", self.root / ".agents/skills")
        (self.root / ".claude/skills").symlink_to("../.agents/skills")
        for name, owner in (
            ("01-diagnostico", "caio"),
            ("02-arquitectura", "architect"),
            ("03-gobierno-seguridad", "governance"),
            ("04-personas-cultura", "people"),
            ("05-business-case", "finance"),
            ("06-roadmap-riesgo", "caio"),
            ("07-resoluciones", "caio"),
        ):
            self.write(f"plan/annexes/{name}.md", f"---\nowner: {owner}\n---\n")
        for name in ("plan/slides.md", "defense/storyline.md", "defense/objeciones.md"):
            self.write(name, "# Ejemplo\n")
        (self.root / "defense/evidence").mkdir()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_adapters_are_valid_toml_with_shared_role_instructions(self):
        self.assertEqual(checker.check(self.root, write=True), [])
        self.assertEqual(checker.check(self.root), [])
        files = list((self.root / ".codex/agents").glob("*.toml"))
        self.assertEqual(len(files), 6)
        for path in files:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            body = (
                (self.root / f".claude/agents/{path.stem}.md")
                .read_text()
                .split("---", 2)[2]
                .strip()
            )
            self.assertEqual(data["name"], path.stem)
            self.assertIn(body, data["developer_instructions"])
            self.assertNotIn("tools", data)

    def test_stale_adapter_rejected_and_regeneration_repairs_it(self):
        self.assertEqual(checker.check(self.root, write=True), [])
        self.write(".codex/agents/board.toml", 'name = "obsolete"\n')
        self.assertTrue(
            any("desactualizado" in error for error in checker.check(self.root))
        )
        self.assertEqual(checker.check(self.root, write=True), [])

    def test_missing_role_target_is_rejected_before_generation(self):
        (self.root / "plan/annexes/05-business-case.md").unlink()
        errors = checker.check(self.root, write=True)
        self.assertTrue(
            any(
                "ruta inexistente" in error and "05-business-case" in error
                for error in errors
            ),
            errors,
        )
        self.assertFalse((self.root / ".codex").exists())

    def test_owner_cannot_claim_another_roles_annex(self):
        self.write("plan/annexes/05-business-case.md", "---\nowner: people\n---\n")
        errors = checker.check(self.root, write=True)
        self.assertTrue(any("people no declara" in error for error in errors), errors)

    def test_orphan_adapter_is_reported_without_deleting_it(self):
        extra = self.write(".codex/agents/obsolete.toml", 'name = "obsolete"\n')
        errors = checker.check(self.root, write=True)
        self.assertTrue(any("sin rol fuente" in error for error in errors), errors)
        self.assertTrue(extra.exists())

    def test_plain_windows_symlink_checkout_is_rejected(self):
        (self.root / ".claude/skills").unlink()
        self.write(".claude/skills", "../.agents/skills")
        errors = checker.check(self.root, write=True)
        self.assertTrue(any("core.symlinks" in error for error in errors), errors)

    def test_two_roles_cannot_claim_the_same_annex(self):
        path = self.root / ".claude/agents/people.md"
        path.write_text(
            path.read_text().replace(
                "## Sos dueño de",
                "## Sos dueño de\n\n- `plan/annexes/05-business-case.md`",
            )
        )
        errors = checker.check(self.root, write=True)
        self.assertTrue(any("más de un rol" in error for error in errors), errors)

    def claim_as(self, role, target):
        path = self.root / f".claude/agents/{role}.md"
        path.write_text(
            path.read_text().replace(
                "## Sos dueño de", f"## Sos dueño de\n\n- `{target}`"
            )
        )

    def test_two_roles_cannot_claim_the_deck_or_the_defense(self):
        for target in (
            "plan/slides.md",
            "defense/storyline.md",
            "defense/objeciones.md",
        ):
            with self.subTest(target=target):
                self.claim_as("people", target)
                errors = checker.check(self.root, write=True)
                self.assertTrue(
                    any(target in e and "más de un rol" in e for e in errors), errors
                )
                shutil.copy(REPO / ".claude/agents/people.md", self.root / ".claude/agents/people.md")

    def test_sole_owner_must_declare_the_deck(self):
        path = self.root / ".claude/agents/caio.md"
        path.write_text(path.read_text().replace("- `plan/slides.md`", "- slides"))
        errors = checker.check(self.root, write=True)
        self.assertTrue(
            any("plan/slides.md" in e and "caio no declara" in e for e in errors),
            errors,
        )

    def test_missing_role_folder_is_rejected(self):
        (self.root / "defense/evidence").rmdir()
        errors = checker.check(self.root, write=True)
        self.assertTrue(
            any("ruta inexistente" in e and "defense/evidence/" in e for e in errors),
            errors,
        )

    def test_invalid_role_description_is_a_validation_error(self):
        path = self.root / ".claude/agents/board.md"
        body = path.read_text().split("---", 2)[2]
        path.write_text("---\nname: board\ndescription: 7\ntools: Read\n---" + body)
        errors = checker.check(self.root, write=True)
        self.assertTrue(
            any("frontmatter inválido" in error for error in errors), errors
        )

    def test_harness_specific_skill_metadata_is_rejected(self):
        path = self.root / ".agents/skills/board-review/SKILL.md"
        path.write_text(
            path.read_text().replace(
                "name: board-review", "name: board-review\nargument-hint: ejemplo"
            )
        )
        errors = checker.check(self.root, write=True)
        self.assertTrue(
            any("claves no portables: argument-hint" in error for error in errors),
            errors,
        )

    def test_delivery_gate_rejects_draft_before_rendering(self):
        self.write(
            "plan/slides.md",
            "---\nowner: caio\nstatus: draft\nmarp: true\n---\n# Ejemplo\n",
        )
        for name in ("build-deck.sh", "plan-check.py", "okf-check.py"):
            self.write(
                f"scripts/{name}",
                (REPO / f"scripts/{name}").read_text(encoding="utf-8"),
            )
        env = dict(os.environ, CAIO_PYTHON=sys.executable)
        result = subprocess.run(
            ["bash", str(self.root / "scripts/build-deck.sh"), "entrega", "--delivery"],
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "Entrega rechazada: deck declarado draft", result.stdout + result.stderr
        )


if __name__ == "__main__":
    unittest.main()
