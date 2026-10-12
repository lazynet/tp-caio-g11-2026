"""Ejemplos del contrato, independientes del schema implementado."""

import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(
    os.environ.get(
        "OKF_CHECK_SCRIPT", Path(__file__).resolve().parents[1] / "scripts/okf-check.py"
    )
)
spec = importlib.util.spec_from_file_location("okf_check", SCRIPT)
okf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(okf)

META = """type: Hecho
title: Ejemplo público
description: Una afirmación de prueba.
generated: {by: codex/test, at: 2026-10-11T12:00:00Z}
sources:
  - {id: primary, resource: 'https://example.org/report', title: Informe}
"""
BODY = "La medida publicada es 12.[^primary]\n\n[^primary]: Informe público.\n"
VERIFIED = """status: verified
verified: {by: 'human:reviewer', at: 2026-10-11, scope: 'Informe, medida publicada'}
"""


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for bundle in ("context", "material", "defense/evidence"):
            self.write(bundle + "/index.md", '---\nokf_version: "0.2"\n---\n')

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def concept(self, meta=META, body=BODY, path="context/sample.md"):
        return self.write(path, "---\n" + meta + "---\n" + body)

    def check(self, path, delivery=False):
        checker = okf.Checker(self.root, delivery)
        checker.check(path)
        return checker

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), *args],
            capture_output=True,
            check=False,
            text=True,
        )

    def test_absent_status_is_draft_not_delivery(self):
        path = self.concept()
        self.assertEqual(self.check(path).errors, [])
        self.assertTrue(self.check(path, True).errors)
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("no implica aptitud", result.stdout)

    def test_reviewed_assumption_stays_assumption(self):
        path = self.concept(META.replace("Hecho", "Supuesto") + VERIFIED)
        self.assertEqual(self.check(path, True).errors, [])
        self.assertIn("type: Supuesto", path.read_text())

    def test_verified_requires_human_complete_block(self):
        cases = [
            "status: verified\n",
            VERIFIED.replace("human:reviewer", "codex/test"),
            VERIFIED.replace("2026-10-11,", "ayer,"),
            VERIFIED.replace("scope: 'Informe, medida publicada'", "scope: ''"),
            "status: verified\nverified: true\n",
        ]
        for extra in cases:
            with self.subTest(extra=extra):
                checker = self.check(self.concept(META + extra), True)
                self.assertTrue(checker.errors)
                self.assertTrue(
                    any("verified" in e for e in checker.errors), checker.errors
                )

    def test_human_block_with_draft_does_not_allow_delivery(self):
        path = self.concept(
            META + VERIFIED.replace("status: verified", "status: draft")
        )
        self.assertTrue(self.check(path, True).errors)

    def test_missing_sources_are_errors_without_documented_gap(self):
        meta = META.split("sources:")[0]
        for kind, location in [
            ("Hecho", "context/sample.md"),
            ("Evidencia", "defense/evidence/sample.md"),
            ("Concepto", "material/sample.md"),
        ]:
            with self.subTest(kind=kind):
                checker = self.check(
                    self.concept(
                        meta.replace("Hecho", kind), "Texto sin fuente.\n", location
                    )
                )
                self.assertTrue(
                    any("faltan sources" in e for e in checker.errors), checker.errors
                )

    def test_documented_draft_gap_warns_but_delivery_fails(self):
        path = self.concept(
            META.split("sources:")[0],
            "Texto.\n\n# Cautelas\n\nFalta identificar la fuente.\n",
        )
        checker = self.check(path)
        self.assertEqual(checker.errors, [])
        self.assertTrue(checker.warnings)
        self.assertTrue(self.check(path, True).errors)

    def test_huecos_gap_is_specific_to_concept(self):
        path = self.concept(META.split("sources:")[0], "Texto.\n")
        self.write("material/huecos.md", "Falta fuente para otra.md.\n")
        self.assertTrue(self.check(path).errors)
        self.write("material/huecos.md", "Falta fuente para sample.md.\n")
        self.assertEqual(self.check(path).errors, [])

    def test_structural_errors_never_become_warnings(self):
        for old, new in [
            ("type: Hecho", "type: [Hecho]"),
            ("type: Hecho", "type: Inventado"),
            ("title: Ejemplo público", "title: false"),
            ("description: Una afirmación de prueba.", "description: []"),
            ("generated: {by: codex/test, at: 2026-10-11T12:00:00Z}", "generated: []"),
            ("codex/test", "unknown/test"),
            ("2026-10-11T12:00:00Z", "nunca"),
            ("sources:\n  -", "sources: false\nunused:\n  -"),
        ]:
            with self.subTest(new=new):
                self.assertTrue(
                    self.check(
                        self.concept(
                            META.replace(old, new), BODY + "\n# Cautelas\nFaltantes.\n"
                        )
                    ).errors
                )

    def test_missing_metadata_is_compatible_only_when_documented(self):
        meta = "type: Supuesto\n"
        self.assertTrue(self.check(self.concept(meta, "Propuesta.\n")).errors)
        checker = self.check(
            self.concept(meta, "Propuesta.\n# Cautelas\nFaltan metadatos.\n")
        )
        self.assertEqual(checker.errors, [])
        self.assertEqual(len(checker.warnings), 3)

    def test_safe_yaml_mapping_closure_and_duplicate_keys(self):
        for text in [
            "---\n- Hecho\n---\n",
            "---\ntype: Hecho\n",
            "---\ntype: Hecho\ntype: Supuesto\n---\n",
            "---\nx: !!python/object/apply:os.system ['false']\n---\n",
            "---\ntitle: [\n---\n",
        ]:
            with self.subTest(text=text):
                self.assertTrue(
                    self.check(self.write("context/sample.md", text)).errors
                )

    def test_source_ids_definitions_and_citations(self):
        for meta, body in [
            (META + "  - {id: primary, resource: report}\n", BODY),
            (META, BODY.replace("[^primary]:", "[^other]:")),
            (META, "Texto.[^primary]\n"),
            (META, BODY + "\n[^primary]: Duplicada.\n"),
            (META.replace("id: primary", "id: false"), BODY),
            (META, "Texto.[^ghost]\n\n[^ghost]: Documento.\n"),
        ]:
            with self.subTest(meta=meta, body=body):
                self.assertTrue(self.check(self.concept(meta, body)).errors)

    def test_source_resource_wrong_type_is_structural(self):
        path = self.concept(
            META.replace("'https://example.org/report'", "false"),
            BODY + "\n# Cautelas\nFalta información.\n",
        )
        self.assertTrue(any("resource" in e for e in self.check(path).errors))

    def test_present_sources_need_citations(self):
        self.assertTrue(self.check(self.concept(body="Texto sin cita.\n")).errors)
        self.assertTrue(
            self.check(
                self.concept(
                    META.replace("Hecho", "Supuesto"), "Atribución sin cita.\n"
                )
            ).errors
        )

    def test_legacy_log_is_draft_only(self):
        path = self.write("context/log.md", "# Registro\n")
        self.assertEqual(self.check(path).errors, [])
        self.assertTrue(self.check(path, True).errors)

    def test_status_wrong_type_is_structural(self):
        for status in ("[]", "{}", "true", "null", "approved"):
            with self.subTest(status=status):
                self.assertTrue(
                    self.check(self.concept(META + f"status: {status}\n")).errors
                )

    def test_consecutive_footnotes_are_not_markdown_reference_links(self):
        meta = META + "  - {id: secondary, resource: another-report}\n"
        body = (
            "Dato.[^primary][^secondary]\n\n[^primary]: Informe.\n[^secondary]: Otro.\n"
        )
        self.assertEqual(self.check(self.concept(meta, body)).errors, [])

    def test_internal_types_and_assumption_do_not_need_sources(self):
        for kind, path in [
            ("Mapa", "material/sample.md"),
            ("Hueco", "material/sample.md"),
            ("Supuesto", "context/sample.md"),
        ]:
            with self.subTest(kind=kind):
                meta = META.split("sources:")[0].replace("Hecho", kind)
                self.assertEqual(
                    self.check(self.concept(meta, "Contenido propio.\n", path)).errors,
                    [],
                )

    def test_internal_type_with_attribution_needs_source(self):
        meta = META.split("sources:")[0].replace("Hecho", "Mapa")
        self.assertTrue(
            self.check(self.concept(meta, BODY, "material/sample.md")).errors
        )

    def test_indices_and_navigation_do_not_require_citations(self):
        path = self.concept()
        index = self.write(
            "context/index.md", '---\nokf_version: "0.2"\n---\n[Ejemplo](/sample.md)\n'
        )
        self.assertEqual(self.check(index, True).errors, [])
        for fm in [
            "",
            '---\nokf_version: "0.2"\ntitle: Extra\n---\n',
            "---\nokf_version: 0.2\n---\n",
        ]:
            self.assertTrue(self.check(self.write("context/index.md", fm)).errors)
        nested = self.write("context/nested/index.md", "# Índice\n")
        self.assertEqual(self.check(nested).errors, [])
        self.assertTrue(
            self.check(
                self.write("context/nested/index.md", '---\nokf_version: "0.2"\n---\n')
            ).errors
        )
        self.assertEqual(self.check(path).errors, [])

    def test_local_links_anchors_references_and_code_examples(self):
        self.concept(
            body=BODY + "\n# Revisión pública\n# Revisión pública\n",
            path="context/target.md",
        )
        valid = [
            "[Ir](/target.md#revisión-pública)",
            "[Ir](/target.md#revisión-pública-1)",
            "[Ir][target]\n\n[target]: /target.md",
            "[Ir](https://example.org/not-fetched)",
            "`[Ejemplo](/missing.md)`",
            "```md\n[Ejemplo](/missing.md)\n```",
        ]
        for link in valid:
            with self.subTest(link=link):
                self.assertEqual(
                    self.check(self.concept(body=BODY + "\n" + link)).errors, []
                )
        for link in [
            "[Ir](/missing.md)",
            "[Ir](target.md)",
            "[Ir](/target.md#missing)",
            "[Ir](/../material/index.md)",
            "[Ir][undefined]",
            "[Ir](/%2e%2e/material/index.md)",
        ]:
            with self.subTest(link=link):
                self.assertTrue(
                    self.check(self.concept(body=BODY + "\n" + link)).errors
                )

    def test_delivery_selection_ignores_unselected_drafts(self):
        self.concept(META + VERIFIED)
        self.concept(path="context/unselected.md")
        result = self.cli(
            "--delivery", "--path", "context/sample.md", "context/sample.md"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 archivos", result.stdout)
        self.assertNotEqual(self.cli("--delivery").returncode, 0)
        self.assertNotEqual(
            self.cli(
                "--delivery",
                "--path",
                "context/sample.md",
                "--path",
                "context/unselected.md",
            ).returncode,
            0,
        )

    def test_selection_errors_and_symlink_escape(self):
        self.concept()
        self.write("outside.md", "Texto")
        (self.root / "context/escape.md").symlink_to(self.root / "outside.md")
        for path in [
            "context/absent.md",
            "outside.md",
            "context/escape.md",
            "context",
            "context/empty",
        ]:
            with self.subTest(path=path):
                self.assertNotEqual(self.cli("--path", path).returncode, 0)

    def test_bundle_type_boundary(self):
        self.assertTrue(self.check(self.concept(path="material/sample.md")).errors)


if __name__ == "__main__":
    unittest.main()
