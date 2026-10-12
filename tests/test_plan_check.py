import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "plan_check", REPO / "scripts/plan-check.py"
)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PlanCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.deck = self.root / "plan/slides.md"
        self.deck.parent.mkdir()

    def write(
        self, body="# Portada", metadata="owner: caio\nstatus: ready\nmarp: true"
    ):
        self.deck.write_text(f"---\n{metadata}\n---\n{body}\n", encoding="utf-8")

    def result(self, mode="draft"):
        return checker.check(self.root, self.deck, mode)

    def test_ten_slides_pass_eleven_fail(self):
        self.write("\n---\n".join(f"# Slide {i}" for i in range(10)))
        self.assertEqual(self.result()["slides"], 10)
        self.assertEqual(self.result()["errors"], [])
        self.write("\n---\n".join(f"# Slide {i}" for i in range(11)))
        self.assertTrue(any("Máximo 10" in e for e in self.result()["errors"]))

    def test_frontmatter_and_fences_are_not_slides(self):
        self.write(
            "# Portada\n```markdown\n---\n[falso](missing.md)\n```\n---\n# Equipo"
        )
        self.assertEqual(self.result()["slides"], 2)
        self.assertEqual(self.result()["errors"], [])

    def test_marp_asterisk_separator(self):
        self.write("# Portada\n***\n# Equipo")
        self.assertEqual(self.result()["slides"], 2)

    def test_empty_slide_rejected(self):
        self.write("# Portada\n---\n")
        self.assertTrue(self.result()["errors"])

    def test_invalid_frontmatter_owner_and_status(self):
        for metadata in (
            "owner: finance\nstatus: ready\nmarp: true",
            "owner: caio\nstatus: unknown\nmarp: true",
            "owner: caio\nstatus: ready\nmarp: false",
        ):
            with self.subTest(metadata=metadata):
                self.write(metadata=metadata)
                self.assertTrue(self.result()["errors"])
        for text in ("# Sin frontmatter", "---\nowner: caio"):
            self.deck.write_text(text)
            self.assertTrue(self.result()["errors"])

    def test_draft_delivery_and_explicit_pending(self):
        self.write(
            "# Setup\nPendiente: evidencia", "owner: caio\nstatus: draft\nmarp: true"
        )
        self.assertEqual(self.result()["errors"], [])
        self.assertTrue(self.result("delivery")["errors"])
        self.write("# Plan\nTODO: definir")
        self.assertTrue(
            any("pendiente" in e for e in self.result("delivery")["errors"])
        )
        self.write("# Una sección con evidencia no requerida por este fixture")
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_relative_root_links_and_anchors(self):
        annex = self.root / "plan/annexes/architecture.md"
        annex.parent.mkdir()
        annex.write_text('# Diseño técnico\n# Diseño técnico\n<a id="custom"></a>\n')
        self.write(
            "# Deck\n[Anexo](annexes/architecture.md#diseño-técnico)\n"
            "[Duplicado](/plan/annexes/architecture.md#diseño-técnico-1)\n"
            "[ID](annexes/architecture.md#custom)\n[Web](https://example.org/path)"
        )
        self.assertEqual(self.result()["errors"], [])
        self.assertEqual(self.result()["references"], ["plan/annexes/architecture.md"])
        self.write("# Deck\n[Anexo](annexes/architecture.md#ausente)")
        self.assertTrue(any("Anchor inexistente" in e for e in self.result()["errors"]))

    def test_broken_local_reference(self):
        self.write("# Deck\n[Anexo](annexes/missing.md)")
        self.assertTrue(
            any("Referencia local rota" in e for e in self.result()["errors"])
        )

    def test_bundle_root_resolution_and_transitive_pending(self):
        material = self.root / "material"
        (material / "unidades").mkdir(parents=True)
        (material / "index.md").write_text("[Ficha](/unidades/example.md#fuente)")
        (material / "unidades/example.md").write_text(
            "# Fuente\nPendiente: verificación humana\n[Inicio](/index.md)"
        )
        self.write("# Deck\n[Material](/material/index.md)")
        self.assertEqual(self.result()["errors"], [])
        self.assertEqual(len(self.result()["references"]), 2)
        self.assertTrue(self.result("delivery")["errors"])

    def test_reference_style_and_image(self):
        (self.root / "plan/annex.md").write_text("# Fuente")
        self.write("# Deck\n[Anexo][evidence]\n[evidence]: annex.md#fuente")
        self.assertEqual(self.result()["errors"], [])
        self.write("# Deck\n[Anexo][missing]\n![Imagen](absent.png)")
        self.assertEqual(len(self.result()["errors"]), 2)

    def test_same_document_anchor_and_escape(self):
        self.write("# Deck\n[Inicio](#deck)")
        self.assertEqual(self.result()["errors"], [])
        self.write("# Deck\n[Fuera](../../external.md)")
        self.assertTrue(any("fuera del repo" in e for e in self.result()["errors"]))

    def test_cli_invalid_and_json(self):
        self.write()
        base = [
            "python3",
            str(REPO / "scripts/plan-check.py"),
            "--root",
            str(self.root),
        ]
        result = subprocess.run(
            base + ["--json"], capture_output=True, text=True, check=False
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["slides"], 1)
        for args in (["--mode", "invalid"], ["--deck", "missing.md"], ["--unknown"]):
            self.assertNotEqual(
                subprocess.run(
                    base + args, capture_output=True, check=False
                ).returncode,
                0,
            )

    def test_build_invalid_argument(self):
        for args in (["invalid"], ["html", "extra"]):
            result = subprocess.run(
                ["bash", str(REPO / "scripts/build-deck.sh")] + args,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
