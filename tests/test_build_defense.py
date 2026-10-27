"""Regresiones de la guía de defensa y su separación de la entrega."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote

from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts/build-defense.py"
spec = importlib.util.spec_from_file_location("build_defense", SCRIPT)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BuildDefenseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "defense").mkdir()
        (self.root / "out").mkdir()
        self.write("storyline.md", "# Guion\n\nMensaje del guion.\n")
        self.write(
            "speech-presentacion.md",
            "# Speech\n\nMensaje oral.\n\n"
            "## Preparación del ensayo (propuesta)\n\n"
            "No acredita un ensayo realizado.\n"
            "[Guion](storyline.md#guion) · [Deck](../plan/slides.md)\n",
        )
        self.write(
            "objeciones.md",
            "# Objeciones\n\nRespuesta para el board.\n"
            "[Ensayo](speech-presentacion.md#preparación-del-ensayo-propuesta)\n",
        )

    def write(self, name, text):
        (self.root / "defense" / name).write_text(text, encoding="utf-8")

    def test_cli_builds_separate_pdf_with_content_bookmarks_and_portable_links(self):
        protected = [
            self.root / "out/Grupo11-AcmeLabs-PlanMaestroCAIO.pdf",
            self.root / "out/Grupo11-AcmeLabs-PlanMaestroCAIO-borrador.pdf",
            self.root / "out/deck-marp.pdf",
        ]
        for path in protected:
            path.write_bytes(b"Artefacto previo que debe conservarse")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root)],
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        pdf = PdfReader(self.root / "out/Grupo11-AcmeLabs-Defensa.pdf")
        text = "\n".join(page.extract_text() for page in pdf.pages)
        for phrase in (
            "Mensaje del guion",
            "Mensaje oral",
            "Respuesta para el board",
            "No acredita un ensayo realizado",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(
            [item.title for item in pdf.outline],
            [
                "Guion argumental",
                "Speech por diapositiva",
                "Preparación del ensayo",
                "Banco de objeciones",
            ],
        )
        self.assertEqual(
            pdf.metadata.title, "Grupo 11 · Acme Labs — Preparación de la defensa"
        )
        for path in protected:
            self.assertEqual(
                path.read_bytes(), b"Artefacto previo que debe conservarse"
            )
        names = {str(name).lstrip("/") for name in pdf.named_destinations}
        internal = 0
        uris = []
        for page in pdf.pages:
            for ref in page.get("/Annots", []):
                annotation = ref.get_object()
                action = annotation.get("/A", {})
                target = annotation.get("/Dest", action.get("/D"))
                if isinstance(target, str):
                    self.assertIn(target.lstrip("/"), names)
                    internal += 1
                uri = str(action.get("/URI", ""))
                if uri:
                    uris.append(uri)
        self.assertGreater(internal, 3)
        self.assertTrue(any("/plan/slides.md" in uri for uri in uris))
        self.assertFalse(
            any("caio.invalid" in uri or uri.startswith("file:") for uri in uris)
        )
        for item in pdf.outline:
            self.assertGreaterEqual(pdf.get_destination_page_number(item), 1)
        names = {unquote(name) for name in names}
        self.assertIn("annex-1-preparación-del-ensayo-propuesta", names)

    def test_missing_internal_target_is_rejected_before_replacing_previous_pdf(self):
        self.write(
            "objeciones.md", "# Objeciones\n[Ir](storyline.md#sección-ausente)\n"
        )
        output = self.root / "out/Grupo11-AcmeLabs-Defensa.pdf"
        output.write_bytes(b"Guia anterior")
        with self.assertRaisesRegex(
            ValueError, "Destinos de defensa inexistentes.*sección-ausente"
        ):
            builder.build(self.root, "main")
        self.assertEqual(output.read_bytes(), b"Guia anterior")

    def test_private_links_are_rejected(self):
        self.write("objeciones.md", "# Objeciones\n[Dato](../private/dato.md)\n")
        with self.assertRaisesRegex(ValueError, "Enlace a private/"):
            builder.defense_html(self.root, "main")


if __name__ == "__main__":
    unittest.main()
