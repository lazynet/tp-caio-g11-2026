import importlib.util
from io import BytesIO
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "build_delivery", REPO / "scripts/build-delivery.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BuildDeliveryTests(unittest.TestCase):
    def test_index_uses_titles_order_and_actual_destination_pages(self):
        from pypdf import PdfReader, PdfWriter

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "plan/annexes"
            folder.mkdir(parents=True)
            (folder / "01-a.md").write_text(
                '---\nowner: finance\nstatus: draft\ntitle: "Anexo A — Uno & dos"\n---\n# Otro\n',
                encoding="utf-8",
            )
            (folder / "02-b.md").write_text(
                '---\nowner: finance\nstatus: draft\ntitle: ""\n---\n# Anexo B — Segundo\n',
                encoding="utf-8",
            )
            writer = PdfWriter()
            for _ in range(4):
                writer.add_blank_page(width=595, height=842)
            writer.add_named_destination("annex-0", 0)
            writer.add_named_destination("annex-1", 3)
            stream = BytesIO()
            writer.write(stream)
            stream.seek(0)
            annexes = PdfReader(stream)
            self.assertIsInstance(annexes, PdfReader)
            markup = builder.annex_index_html(root, builder.load_plan_check(), annexes)
            self.assertIn("Índice de anexos", markup)
            self.assertIn(
                'href="https://caio.invalid/annexes#annex-0">Anexo A — Uno &amp; dos</a>',
                markup,
            )
            self.assertIn(
                'href="https://caio.invalid/annexes#annex-1">Anexo B — Segundo</a>',
                markup,
            )
            self.assertLess(markup.index("Anexo A"), markup.index("Anexo B"))
            self.assertIn("<td>1</td>", markup)
            self.assertIn("<td>4</td>", markup)
            index_pdf = root / "index.pdf"
            builder.render_annexes(root, markup, index_pdf, numbered=False)
            index = PdfReader(index_pdf)
            self.assertEqual(len(index.pages), 1)
            self.assertEqual(len(index.pages[0].get("/Annots", [])), 2)
            combined = PdfWriter()
            combined.append(index)
            combined.append(annexes)
            builder.rewrite_pdf_links(
                combined, root, builder.load_plan_check().annex_files(root), {}, "main"
            )
            builder.check_portable_pdf(combined)
            for annotation, target in zip(combined.pages[0]["/Annots"], (1, 4)):
                self.assertEqual(
                    annotation.get_object()["/A"]["/D"][0],
                    combined.pages[target].indirect_reference,
                )

    def test_print_css_keeps_rows_whole_and_numbers_annex_pages(self):
        self.assertIn(
            "tr { break-inside: avoid; page-break-inside: avoid; }", builder.CSS
        )
        self.assertIn("@bottom-center", builder.CSS)
        self.assertIn('content: "Anexos · página " counter(page)', builder.CSS)

    def test_build_cli_rejects_private_source_before_rendering(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "deck.pdf").touch()
            folder = root / "plan/annexes"
            folder.mkdir(parents=True)
            (folder / "a.md").write_text(
                "---\nowner: finance\nstatus: draft\ntitle: T\n---\n"
                "# Anexo\n[Fuente](../../private/source.md)\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO / "scripts/build-delivery.py"),
                    "--root",
                    str(root),
                    "--deck",
                    "deck.pdf",
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Enlace a private/", result.stderr)
            self.assertFalse((root / "out/entrega.pdf").exists())

    def test_annex_html_preserves_anchors_references_and_unique_footnotes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "plan/annexes"
            folder.mkdir(parents=True)
            for name in ("a.md", "b.md"):
                (folder / name).write_text(
                    "---\nowner: finance\nstatus: draft\ntitle: T\n---\n"
                    "# Evidencia\n[Sección](#evidencia) · [Otro](b.md#evidencia)\n"
                    "[Fuente][source] · [Slide 3](../slides.md)\n"
                    "\n[source]: ../../context/source.md#fuente\n\n"
                    "Texto[^note].\n\n[^note]: Una nota.\n",
                    encoding="utf-8",
                )
            markup = builder.annexes_html(root, builder.load_plan_check(), "v1")
            self.assertIn('href="#annex-0-evidencia"', markup)
            self.assertIn('href="#annex-1-evidencia"', markup)
            self.assertIn('id="annex-0-fn1"', markup)
            self.assertIn('id="annex-1-fn1"', markup)
            self.assertIn("https://caio.invalid/slides#page-3", markup)
            self.assertIn("blob/v1/context/source.md#fuente", markup)

    def test_portable_targets_and_private_rejection(self):
        root = Path("/example/repo")
        origin = root / "plan/annexes/01-a.md"
        self.assertEqual(
            builder.portable_target(
                root, origin, "../../context/source.md#fuente", [], "release/v1"
            ),
            "https://github.com/lazynet/tp-caio-g11-2026/blob/release%2Fv1/context/source.md#fuente",
        )
        self.assertEqual(
            builder.portable_target(root, origin, "../slides.md#resumen", [], "main"),
            "https://caio.invalid/slides#resumen",
        )
        with self.assertRaisesRegex(ValueError, "private/"):
            builder.portable_target(root, origin, "../../private/source.md", [], "main")

    def test_pdf_links_are_internal_or_public_and_guard_rejects_files(self):
        from pypdf import PdfWriter
        from pypdf.generic import (
            ArrayObject,
            DictionaryObject,
            NameObject,
            TextStringObject,
        )

        root = Path("/example/repo")
        writer = PdfWriter()
        for _ in range(2):
            writer.add_blank_page(width=100, height=100)
        writer.add_named_destination("annex-0", 1)
        writer.add_named_destination("annex-0-section", 1)
        annotations = ArrayObject()
        for uri in (
            "file:///example/repo/plan/annexes/a.md",
            "file:///example/repo/context/source.md#x",
            "file:///example/repo/plan/annexes/a.md#section",
            "https://caio.invalid/slides#intro",
        ):
            annotations.append(
                DictionaryObject(
                    {
                        NameObject("/A"): DictionaryObject(
                            {
                                NameObject("/S"): NameObject("/URI"),
                                NameObject("/URI"): TextStringObject(uri),
                            }
                        )
                    }
                )
            )
        writer.pages[0][NameObject("/Annots")] = annotations
        with self.assertRaisesRegex(ValueError, "file://"):
            builder.check_portable_pdf(writer)
        builder.rewrite_pdf_links(
            writer, root, [root / "plan/annexes/a.md"], {"intro": 0}, "main"
        )
        builder.check_portable_pdf(writer)
        self.assertEqual(annotations[0]["/A"]["/S"], "/GoTo")
        self.assertEqual(
            annotations[1]["/A"]["/URI"],
            "https://github.com/lazynet/tp-caio-g11-2026/blob/main/context/source.md#x",
        )
        self.assertEqual(
            annotations[2]["/A"]["/D"][0], writer.pages[1].indirect_reference
        )
        self.assertEqual(
            annotations[3]["/A"]["/D"][0], writer.pages[0].indirect_reference
        )

    def test_size_limit(self):
        self.assertIsNone(builder.size_error(builder.MAX_BYTES - 1))
        self.assertIn("menos de", builder.size_error(builder.MAX_BYTES))

    def test_annexes_ordered_without_template_or_frontmatter(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "plan/annexes"
            folder.mkdir(parents=True)
            for name in ("02-b.md", "01-a.md", "_template.md"):
                (folder / name).write_text(
                    f"---\nowner: finance\nstatus: draft\ntitle: T\n---\n# {name}\n",
                    encoding="utf-8",
                )
            markdown = builder.annexes_markdown(root, builder.load_plan_check())
        self.assertLess(markdown.index("# 01-a.md"), markdown.index("# 02-b.md"))
        self.assertNotIn("_template", markdown)
        self.assertNotIn("owner:", markdown)
        self.assertEqual(markdown.count("page-break-before"), 1)


if __name__ == "__main__":
    unittest.main()
