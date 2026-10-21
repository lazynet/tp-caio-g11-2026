import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "plan_check", REPO / "scripts/plan-check.py"
)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PlanCheckTests(unittest.TestCase):
    def test_spanish_todo_is_not_a_pending_marker(self):
        self.write(
            "# Deck\nsobre todo la terminal\nTODO real\nPendiente humano\nPOR DEFINIR\nFIXME real"
        )
        pending = self.result()["pending"]
        self.assertEqual(len(pending), 4)
        self.assertFalse(any("sobre todo" in item for item in pending))

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

    def annex(self, name="finance.md", body="", owner="finance", status="ready"):
        target = self.root / "plan/annexes" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        sections = "".join(f"## {s}\n\nTexto.\n\n" for s in checker.ANNEX_SECTIONS)
        target.write_text(
            f"---\nowner: {owner}\nstatus: {status}\ntitle: Anexo\n---\n"
            f"# Anexo\n{body}\n{sections}",
            encoding="utf-8",
        )
        return target

    def concept(
        self,
        path="context/source.md",
        status="draft",
        body="# Fuente",
        human="human:reviewer",
        kind="Supuesto",
    ):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        review = (
            f"{status}: {{by: '{human}', at: 2026-10-11, scope: 'Fuente y supuesto revisados'}}\n"
            if status in ("accepted", "verified")
            else ""
        )
        target.write_text(
            f"---\ntype: {kind}\ntitle: Fuente\ndescription: Supuesto de prueba.\n"
            f"generated: {{by: human:author, at: 2026-10-11}}\nstatus: {status}\n"
            f"{review}---\n{body}\n",
            encoding="utf-8",
        )
        return target

    def catalog(self, target, line, category, basis=None, blocking=False):
        relative = str(target.relative_to(self.root))
        entry = {
            "path": relative,
            "line": line,
            "text": target.read_text().splitlines()[line - 1],
            "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "category": category,
            "blocking": blocking,
            "reason": "Clasificación específica del ejemplo independiente.",
            "basis": basis or {},
        }
        path = self.root / "scripts/delivery-findings.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"version": 1, "entries": [entry]}))
        return path

    def citation(self, target, first, last=None):
        return {
            "path": str(target.relative_to(self.root)),
            "line": first,
            "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "text": "\n".join(
                target.read_text().splitlines()[first - 1 : last or first]
            ),
        }

    def future(self):
        target = self.annex(
            body=(
                "Pendiente: elegir proveedor para el piloto.\n"
                "Decide el Directorio.\n"
                "Se decide antes de abrir el piloto en M4.\n"
                "Sin decisión, el piloto queda suspendido."
            )
        )
        self.write("# Deck\n[Anexo](annexes/finance.md)")
        basis = dict(
            zip(
                ("scope", "authority", "decision", "consequence"),
                (self.citation(target, n) for n in range(7, 11)),
            )
        )
        path = self.catalog(target, 7, "future_decision", basis)
        return target, path

    def test_catalog_future_is_reported_without_blocking(self):
        self.future()
        result = self.result("delivery")
        self.assertEqual(result["errors"], [])
        self.assertEqual(len(result["pending"]), 1)
        self.assertFalse(result["findings"][0]["blocking"])
        self.assertEqual(result["findings"][0]["category"], "future_decision")

    def test_stale_catalog_warns_in_draft_and_rejects_delivery(self):
        target, _ = self.future()
        target.write_text(target.read_text() + "\n")
        draft = self.result("draft")
        self.assertEqual(draft["errors"], [])
        self.assertTrue(any("Documento modificado" in w for w in draft["warnings"]))
        self.assertEqual(draft["findings"][0]["category"], "unclassified")
        self.assertTrue(self.result("delivery")["errors"])
        command = [
            checker.sys.executable,
            str(REPO / "scripts/plan-check.py"),
            "--root",
            str(self.root),
            "--mode",
            "draft",
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ADVERTENCIA: Catálogo de entrega inválido", result.stdout)
        self.assertIn("PENDIENTE DE ENTREGA", result.stdout)
        self.assertNotIn("BLOQUEO [", result.stdout)
        target.write_text(target.read_text() + "\n[Roto](missing.md)\n")
        draft = self.result("draft")
        self.assertTrue(
            any("Referencia local rota" in error for error in draft["errors"])
        )
        self.assertTrue(draft["warnings"])

    def test_catalog_decision_can_cite_a_gate_without_calendar_date(self):
        target, _ = self.future()
        target.write_text(
            target.read_text().replace(
                "Se decide antes de abrir el piloto en M4.",
                "Se decide antes de habilitar el piloto.",
            )
        )
        self.catalog(
            target,
            7,
            "future_decision",
            dict(
                zip(
                    ("scope", "authority", "decision", "consequence"),
                    (self.citation(target, n) for n in range(7, 11)),
                )
            ),
        )
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_one_operational_rule_can_supply_all_four_fields(self):
        rule = (
            "Regla propuesta: Seguridad valida cada afirmación antes de publicarla; "
            "si aparece una afirmación sin evidencia, la retira y corrige el procedimiento."
        )
        target = self.annex(body=rule)
        self.write("# Deck\n[Anexo](annexes/finance.md)")
        self.catalog(
            target,
            7,
            "execution_condition",
            {
                field: self.citation(target, 7)
                for field in ("scope", "authority", "decision", "consequence")
            },
        )
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_catalog_multiline_citation_keeps_trailing_blank(self):
        target, path = self.future()
        data = json.loads(path.read_text())
        data["entries"][0]["basis"]["scope"] = self.citation(target, 7, 12)
        path.write_text(json.dumps(data))
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_catalog_execution_condition_is_reported(self):
        target = self.annex(
            body=(
                "Control pendiente de prueba para el chat.\n"
                "Seguridad autoriza su uso.\n"
                "La prueba se exige antes de habilitar cada caso.\n"
                "Sin prueba no se habilita ese caso."
            )
        )
        self.write("# Deck\n[Anexo](annexes/finance.md)")
        self.catalog(
            target,
            7,
            "execution_condition",
            dict(
                zip(
                    ("scope", "authority", "decision", "consequence"),
                    (self.citation(target, n) for n in range(7, 11)),
                )
            ),
        )
        result = self.result("delivery")
        self.assertEqual(result["errors"], [])
        self.assertFalse(result["findings"][0]["blocking"])
        self.assertEqual(result["findings"][0]["category"], "execution_condition")

    def test_catalog_history_has_explicit_temporal_limit(self):
        target = self.concept(
            status="verified",
            body=(
                "# Fuente\nEn abril de 2025, la matriz estaba pendiente.\n"
                "No describe el estado actual ni habilita usos."
            ),
        )
        self.write("# Deck\n[Fuente](/context/source.md)")
        self.catalog(
            target,
            10,
            "historical_uncertainty",
            {
                "record": self.citation(target, 10),
                "limit": self.citation(target, 11),
            },
        )
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_catalog_exact_metadata_and_fake_metadata(self):
        target = self.concept(status="verified")
        target.write_text(
            target.read_text().replace(
                "description: Supuesto de prueba.",
                "description: Supuesto de prueba.\ntags: [pendiente, ejemplo]",
            )
        )
        self.write("# Deck\n[Fuente](/context/source.md)")
        self.catalog(target, 5, "metadata")
        self.assertEqual(self.result("delivery")["errors"], [])
        target = self.concept(
            status="verified", body="# Fuente\ntags: [pendiente, ejemplo]"
        )
        self.catalog(target, 10, "metadata")
        self.assertTrue(self.result("delivery")["errors"])

    def test_catalog_new_detection_and_real_pending_remain_blocking(self):
        target, _ = self.future()
        target.write_text(target.read_text() + "\nPendiente: revisar presupuesto.\n")
        result = self.result("delivery")
        self.assertTrue(result["errors"])
        self.assertEqual(result["findings"][-1]["category"], "unclassified")
        self.assertTrue(result["findings"][-1]["blocking"])
        target = self.concept(
            status="verified", body="# Fuente\nPendiente: revisión de la fuente."
        )
        self.write("# Deck\n[Fuente](/context/source.md)")
        self.catalog(target, 10, "required_gap", blocking=True)
        self.assertTrue(self.result("delivery")["errors"])

    def test_catalog_requires_all_four_future_fields(self):
        for field in ("scope", "authority", "decision", "consequence"):
            with self.subTest(field=field):
                _, path = self.future()
                data = json.loads(path.read_text())
                del data["entries"][0]["basis"][field]
                path.write_text(json.dumps(data))
                self.assertTrue(self.result("delivery")["errors"])

    def test_catalog_fails_closed_on_changed_text_location_or_support(self):
        for mutation in ("text", "location", "support", "remove"):
            with self.subTest(mutation=mutation):
                target, _ = self.future()
                text = target.read_text()
                text = {
                    "text": text.replace("elegir proveedor", "revisar evidencia"),
                    "location": text.replace("# Anexo\n", "# Anexo\n\n"),
                    "support": text.replace("Directorio", "equipo sin autoridad"),
                    "remove": text.replace("Pendiente:", "Propuesta:"),
                }[mutation]
                target.write_text(text)
                self.assertTrue(self.result("delivery")["errors"])

    def test_catalog_rejects_unknown_duplicate_and_invalid_entries(self):
        for mutation in ("category", "key", "duplicate", "version", "type", "json"):
            with self.subTest(mutation=mutation):
                _, path = self.future()
                data = json.loads(path.read_text())
                entry = data["entries"][0]
                if mutation == "category":
                    entry["category"] = "approved"
                elif mutation == "key":
                    entry["bypass"] = True
                elif mutation == "duplicate":
                    data["entries"].append(entry.copy())
                elif mutation == "version":
                    data["version"] = 2
                elif mutation == "type":
                    entry["blocking"] = "false"
                path.write_text("{broken" if mutation == "json" else json.dumps(data))
                self.assertTrue(self.result("delivery")["errors"])

    def test_catalog_never_admits_placeholders_or_required_gap(self):
        for marker in ("TODO", "TBD", "FIXME"):
            with self.subTest(marker=marker):
                target, path = self.future()
                target.write_text(target.read_text().replace("Pendiente", marker))
                data = json.loads(path.read_text())
                entry = data["entries"][0]
                entry["text"] = target.read_text().splitlines()[6]
                entry["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
                entry["basis"] = dict(
                    zip(
                        ("scope", "authority", "decision", "consequence"),
                        (self.citation(target, n) for n in range(7, 11)),
                    )
                )
                path.write_text(json.dumps(data))
                self.assertTrue(self.result("delivery")["errors"])
        target, path = self.future()
        data = json.loads(path.read_text())
        data["entries"][0]["category"] = "required_gap"
        data["entries"][0]["basis"] = {}
        path.write_text(json.dumps(data))
        self.assertTrue(self.result("delivery")["errors"])

    def test_catalog_does_not_override_other_validations(self):
        self.future()
        self.concept(status="draft")
        private = self.root / "private/data.md"
        private.parent.mkdir()
        private.write_text("Texto sintético de prueba.")
        self.write(
            "# Deck\n[Anexo](annexes/finance.md)\n[Fuente](/context/source.md)\n"
            "[Roto](missing.md)\n[Privado](/private/data.md)",
            metadata="owner: caio\nstatus: draft\nmarp: true",
        )
        errors = self.result("delivery")["errors"]
        for fragment in ("deck declarado draft", "status: verified", "rota", "privad"):
            self.assertTrue(any(fragment in error for error in errors), errors)

    def test_private_links_including_file_uri_are_rejected(self):
        target = self.root / "private/data.md"
        target.parent.mkdir()
        target.write_text("Texto sintético.")
        for link in (
            "/private/data.md",
            "../private/data.md",
            "/%70rivate/data.md",
            target.as_uri(),
        ):
            with self.subTest(link=link):
                self.write(f"# Deck\n[Fuente]({link})")
                self.assertTrue(self.result("delivery")["errors"])

    def test_private_directory_case_aliases_are_rejected(self):
        target = self.root / "Private/data.md"
        target.parent.mkdir()
        target.write_text("Texto sintético.")
        self.write("# Deck\n[Fuente](/Private/data.md)")
        self.assertTrue(self.result("delivery")["errors"])
        if (self.root / "private/data.md").is_file():
            self.write("# Deck\n[Fuente](/PRIVATE/data.md)")
            self.assertTrue(self.result("delivery")["errors"])

    def test_used_draft_rejected_and_human_verified_accepted(self):
        self.concept()
        self.write("# Deck\n[Fuente](/context/source.md)")
        self.assertEqual(self.result()["errors"], [])
        result = self.result("delivery")
        self.assertEqual(result["evidence"], ["context/source.md"])
        self.assertTrue(
            any("entrega exige status: verified" in e for e in result["errors"])
        )
        self.concept(status="verified")
        self.assertEqual(self.result("delivery")["errors"], [])
        self.assertIn("type: Supuesto", (self.root / "context/source.md").read_text())

    def test_verified_requires_human_declaration(self):
        self.concept(status="verified", human="codex/test")
        self.write("# Deck\n[Fuente](/context/source.md)")
        self.assertTrue(
            any("exige human:" in e for e in self.result("delivery")["errors"])
        )
        target = self.concept(status="verified")
        target.write_text(
            target.read_text().replace(
                "verified: {by: 'human:reviewer', at: 2026-10-11, scope: 'Fuente y supuesto revisados'}\n",
                "",
            )
        )
        self.assertTrue(
            any(
                "verified debe ser un mapping" in e
                for e in self.result("delivery")["errors"]
            )
        )

    def test_used_accepted_is_valid_draft_but_never_delivery(self):
        self.write("# Deck\n[Fuente](/context/source.md)")
        for residual in (
            "",
            "verified: {by: 'human:reviewer', at: 2026-10-11, scope: 'Revisión previa'}\n",
        ):
            with self.subTest(residual=residual):
                target = self.concept(status="accepted")
                if residual:
                    target.write_text(
                        target.read_text().replace(
                            "---\n# Fuente", residual + "---\n# Fuente"
                        )
                    )
                self.assertEqual(self.result()["errors"], [])
                result = self.result("delivery")
                self.assertEqual(result["evidence"], ["context/source.md"])
                self.assertTrue(
                    any(
                        "entrega exige status: verified" in e for e in result["errors"]
                    ),
                    result["errors"],
                )

    def test_unused_reference_definition_is_navigation(self):
        self.concept()
        self.write("# Deck\n[unused]: /context/source.md")
        result = self.result("delivery")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["evidence"], [])
        self.assertEqual(result["references"], ["context/source.md"])
        self.write("# Deck\n[Fuente][unused]\n[unused]: /context/source.md")
        self.assertTrue(
            any(
                "entrega exige status: verified" in e
                for e in self.result("delivery")["errors"]
            )
        )
        self.write("# Deck\n[unused]: /context/missing.md")
        self.assertTrue(
            any("Referencia local rota" in e for e in self.result("delivery")["errors"])
        )

    def test_shortcut_reference_selects_evidence(self):
        self.concept()
        self.write("# Deck\n[source]\n[source]: /context/source.md")
        self.assertEqual(self.result()["evidence"], ["context/source.md"])
        self.write("# Deck\n[SOURCE]\n[source]: /context/source.md")
        self.assertTrue(
            any(
                "entrega exige status: verified" in e
                for e in self.result("delivery")["errors"]
            )
        )
        self.concept(status="verified")
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_unused_library_and_related_concepts_do_not_block(self):
        self.concept("context/unused.md", body="# Fuente\nTODO: revisión")
        self.write("# Deck")
        self.assertEqual(self.result("delivery")["errors"], [])
        self.concept(status="verified", body="# Fuente\n[Relacionado](/unused.md)")
        self.write("# Deck\n[Fuente](/context/source.md)")
        result = self.result("delivery")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["evidence"], ["context/source.md"])
        self.assertIn("context/unused.md", result["references"])

    def test_evidence_used_via_annex_and_defense(self):
        self.concept("material/source.md", kind="Mapa")
        self.concept(
            "defense/evidence/source.md",
            kind="Evidencia",
            status="verified",
            body="# Fuente\nDato.[^public]\n[^public]: Fuente pública\n",
        )
        target = self.root / "defense/evidence/source.md"
        target.write_text(
            target.read_text().replace(
                "title: Fuente",
                "sources: [{id: public, resource: 'https://example.org'}]\ntitle: Fuente",
            )
        )
        annex = self.annex(
            body="[Fuente](/material/source.md)\n[Defensa](/defense/storyline.md)"
        )
        (self.root / "defense/storyline.md").write_text(
            "# Defensa\n[Fuente](evidence/source.md)"
        )
        self.write("# Deck\n[Anexo](annexes/finance.md)")
        result = self.result("delivery")
        self.assertEqual(
            result["evidence"], ["defense/evidence/source.md", "material/source.md"]
        )
        self.assertTrue(any("material/source.md" in e for e in result["errors"]))
        self.concept("material/source.md", status="verified", kind="Mapa")
        self.assertEqual(self.result("delivery")["errors"], [])
        annex.write_text(annex.read_text() + "\nTODO: presupuesto")
        self.assertTrue(
            any("pendiente" in e for e in self.result("delivery")["errors"])
        )

    def test_used_concept_pending_and_schema_errors(self):
        self.write("# Deck\n[Fuente](/context/source.md)")
        self.concept(status="verified", body="# Fuente\nPendiente: revisión")
        self.assertTrue(
            any("pendiente" in e for e in self.result("delivery")["errors"])
        )
        target = self.concept(status="verified")
        target.write_text(
            target.read_text().replace("type: Supuesto", "type: Inválido")
        )
        self.assertTrue(
            any("type desconocido" in e for e in self.result("delivery")["errors"])
        )
        self.concept(status="verified", body="# Fuente\n[Relacionado](/missing.md)")
        self.assertTrue(
            any("Referencia local rota" in e for e in self.result("delivery")["errors"])
        )
        self.concept(status="verified", body="# Fuente\n[Relacionado](source.md)")
        self.assertTrue(
            any("absoluto al bundle" in e for e in self.result("delivery")["errors"])
        )

    def test_validator_failures_cannot_approve(self):
        self.concept(status="verified")
        self.write("# Deck\n[Fuente](/context/source.md)")
        for failure in (FileNotFoundError("validator unavailable"),):
            with patch.object(checker.subprocess, "run", side_effect=failure):
                self.assertTrue(self.result("delivery")["errors"])
        for message in ("PyYAML missing", "validator crashed"):
            with patch.object(
                checker.subprocess,
                "run",
                return_value=subprocess.CompletedProcess([], 1, "", message),
            ):
                self.assertTrue(
                    any(message in e for e in self.result("delivery")["errors"])
                )

    def test_delivery_cli_json_with_validator_output(self):
        self.concept()
        self.write("# Deck\n[Fuente](/context/source.md)")
        command = [
            "python3",
            str(REPO / "scripts/plan-check.py"),
            "--root",
            str(self.root),
            "--mode",
            "delivery",
            "--json",
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertTrue(json.loads(result.stdout)["errors"])
        self.assertEqual(result.stderr, "")
        self.concept(status="verified")
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["evidence"], ["context/source.md"])

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

    def test_noncanonical_horizontal_rules_rejected(self):
        for separator in (
            "___",
            "- - -",
            "* * *",
            "_ _ _",
            "----",
            "****",
            "____",
            "  -\t- -  ",
        ):
            with self.subTest(separator=separator):
                self.write(f"\n{separator}\n".join(f"# Slide {i}" for i in range(11)))
                for mode in ("draft", "delivery"):
                    self.assertTrue(
                        any(
                            "Separador no admitido" in e
                            for e in self.result(mode)["errors"]
                        )
                    )
        for separator in ("---", "***", "   ---\t"):
            self.write(f"# Deck\n{separator}\n# Equipo")
            self.assertEqual(self.result("delivery")["errors"], [])
            self.assertEqual(self.result()["slides"], 2)
        self.write("# Deck\n<!--\n___\n-->\n```\n- - -\n```\n`___`")
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_local_html_links_rejected_direct_and_via_annex(self):
        self.concept()
        annex = self.root / "plan/annex.md"
        for destination in (
            "/context/source.md",
            "/context/missing.md",
            "../context/source.md",
            "../context/missing.md",
        ):
            for attribute in ("href", "src"):
                for syntax in (f'"{destination}"', f"'{destination}'", destination):
                    html = f"<a {attribute}={syntax}>Fuente</a>"
                    for indirect in (False, True):
                        with self.subTest(
                            destination=destination,
                            attribute=attribute,
                            syntax=syntax,
                            indirect=indirect,
                        ):
                            annex.write_text(f"# Anexo\n{html}")
                            self.write(
                                "# Deck\n[Anexo](annex.md)"
                                if indirect
                                else f"# Deck\n{html}"
                            )
                            for mode in ("draft", "delivery"):
                                self.assertTrue(
                                    any(
                                        "Enlace HTML local no admitido" in e
                                        for e in self.result(mode)["errors"]
                                    )
                                )
        self.write(
            '# Deck\n<a href="https://example.org/missing">Web</a>\n<img src="//example.org/image">\n<a href="#deck">Inicio</a>\n<a id="custom"></a>'
        )
        with patch.object(
            checker,
            "resolve_link",
            side_effect=AssertionError("No leer links HTML externos"),
        ):
            self.assertEqual(self.result("delivery")["errors"], [])
        self.write(
            '# Deck\n`<a href="missing.md">TODO</a>`\n<!-- <img src="missing.png"> -->\n```html\n<a href="missing.md">TODO</a>\n```'
        )
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_yaml_syntax_duplicates_mapping_and_types(self):
        valid = "owner: caio\nstatus: ready\nmarp: true"
        for metadata in (
            valid + "\ninvalid: [",
            valid + "\nstatus: draft",
            "status: draft\n" + valid,
            "[caio, ready, true]",
            "null",
            "owner: [caio]\nstatus: ready\nmarp: true",
            "owner: caio\nstatus: [ready]\nmarp: true",
            'owner: caio\nstatus: ready\nmarp: "true"',
            valid + "\nextra: {key: one, key: two}",
            valid + "\n? [key]\n: value",
            valid + "\nextra: !!python/object:bad {}",
        ):
            with self.subTest(metadata=metadata):
                self.write(metadata=metadata)
                for mode in ("draft", "delivery"):
                    self.assertTrue(self.result(mode)["errors"])
        for metadata in (
            valid,
            "{owner: caio, status: ready, marp: true}",
            valid + "\nextra: {nested: [one, two]}",
        ):
            self.write(metadata=metadata)
            self.assertEqual(self.result("delivery")["errors"], [])

    def test_missing_yaml_dependency_keeps_cli_json_clean(self):
        self.write()
        result = subprocess.run(
            [
                "python3",
                "-S",
                str(REPO / "scripts/plan-check.py"),
                "--root",
                str(self.root),
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("PyYAML", json.loads(result.stdout)["errors"][0])
        self.assertEqual(result.stderr, "")

    def test_code_comments_ignored_with_visible_pending_line_numbers(self):
        body = "# Deck\n`[falso](missing.md) TODO`\n``[falso](missing.md) ` TODO``\n<!--\nTODO\n[falso](missing.md)\n-->\n~~~~markdown\nTODO\n[falso](missing.md)\n~~~~\n```\nTODO\n```\nTODO: real"
        self.write(body)
        result = self.result("delivery")
        self.assertEqual(result["references"], [])
        self.assertEqual(result["pending"], ["plan/slides.md:20: TODO: real"])
        self.assertEqual(len(result["errors"]), 1)
        self.write(body.replace("TODO: real", "[Real](missing.md)"))
        self.assertTrue(
            any("Referencia local rota" in e for e in self.result()["errors"])
        )
        annex = self.root / "plan/annex.md"
        annex.write_text(
            "# Anexo\n<!--\nTODO\n-->\n`TODO [falso](missing.md)`\n```\nTODO\n```\nTODO: real"
        )
        self.write("# Deck\n[Anexo](annex.md)")
        self.assertEqual(self.result()["pending"], ["plan/annex.md:9: TODO: real"])

    def test_process_text_rejected_in_deck_and_annex(self):
        for phrase in (
            "La bifurcación que decidió lazynet el 14",
            "Actualización de ronda 11b",
            "Reemplaza a la versión anterior",
            "El pedido anterior queda como alternativa",
            "Cifras no aptas para el peer review",
            "Las fichas siguen en `draft`",
            "Lo revisa `finance`",
            "Decisión de Martin",
            "Lo marcó la re-revisión docente",
            "Las cinco dimensiones de M1U1",
            "Sin fuente primaria ([huecos](../x.md))",
            "y `context/` no registra ninguno",
            "Regla vigente del borrador: una señal",
            "| Dimensión (m2 u4) |",
        ):
            with self.subTest(phrase=phrase):
                self.write(f"# Plan\n{phrase}")
                self.assertTrue(
                    any("texto de proceso" in e for e in self.result()["errors"])
                )
        self.write()
        self.annex(body="Ver el reporte de esta ronda")
        self.assertTrue(any("texto de proceso" in e for e in self.result()["errors"]))

    def test_business_text_is_not_process_text(self):
        self.concept("material/unidades/m1u1-x.md")
        self.write(
            "# Plan\nUna ronda de configuración, el mes anterior y la "
            "[fuente](../material/unidades/m1u1-x.md) del CFO.[^m1u2]\n"
            "<!-- ronda 11 -->\n\n[^m1u2]: Modelo de madurez.\n"
            "Equipo: Gabriela T. · Martin V."
        )
        self.assertEqual(self.result()["errors"], [])

    def test_process_text_cites_file_line(self):
        self.write("# Plan\n\nVer esta ronda")
        self.assertTrue(any("plan/slides.md:8:" in e for e in self.result()["errors"]))

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
        self.annex(
            "architecture.md",
            body='# Diseño técnico\n# Diseño técnico\n<a id="custom"></a>',
            owner="architect",
        )
        self.write(
            "# Deck\n[Anexo](annexes/architecture.md#diseño-técnico)\n"
            "[Duplicado](/plan/annexes/architecture.md#diseño-técnico-1)\n"
            "[ID](annexes/architecture.md#custom)\n[Web](https://example.org/path)"
        )
        self.assertEqual(self.result()["errors"], [])
        self.assertEqual(self.result()["references"], ["plan/annexes/architecture.md"])
        self.write("# Deck\n[Anexo](annexes/architecture.md#ausente)")
        self.assertTrue(any("Anchor inexistente" in e for e in self.result()["errors"]))

    def test_annex_requires_frontmatter_owner_and_sections(self):
        self.write("# Deck\n[Anexo](annexes/finance.md)")
        annex = self.annex()
        self.assertEqual(self.result()["errors"], [])
        annex.write_text(annex.read_text().replace("## Decisiones", "## Otra cosa"))
        self.assertTrue(
            any("falta la sección ## Decisiones" in e for e in self.result()["errors"])
        )
        self.annex(owner="board")
        self.assertTrue(any("owner del anexo" in e for e in self.result()["errors"]))
        annex.write_text("# Sin frontmatter\n")
        self.assertTrue(any("Falta frontmatter" in e for e in self.result()["errors"]))

    def test_annex_delivery_rejects_draft_and_unreferenced(self):
        self.write("# Deck\n[Anexo](annexes/finance.md)")
        self.annex()
        self.assertEqual(self.result("delivery")["errors"], [])
        self.annex(status="draft")
        self.assertTrue(
            any("anexo declarado draft" in e for e in self.result("delivery")["errors"])
        )
        self.annex()
        self.annex("people.md", owner="people")
        self.assertEqual(self.result()["errors"], [])
        self.assertTrue(
            any("no referenciado" in e for e in self.result("delivery")["errors"])
        )

    def test_underscore_annex_is_template(self):
        (self.root / "plan/annexes").mkdir(parents=True)
        (self.root / "plan/annexes/_template.md").write_text("# Sin estructura\n")
        self.write("# Deck")
        self.assertEqual(self.result("delivery")["errors"], [])

    def test_repo_template_passes_annex_check(self):
        template = REPO / "plan/annexes/_template.md"
        self.assertEqual(checker.check_annex(template, REPO, "draft"), [])

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
        self.assertEqual(self.result("delivery")["errors"], [])
        self.assertEqual(self.result("delivery")["evidence"], [])
        (material / "unidades/example.md").write_text("# Fuente\n[Mal](/missing.md)")
        self.assertTrue(self.result("delivery")["errors"])

    def test_reference_style_and_image(self):
        (self.root / "plan/annex.md").write_text("# Fuente")
        self.write("# Deck\n[Anexo][evidence]\n[evidence]: annex.md#fuente")
        self.assertEqual(self.result()["errors"], [])
        self.write("# Deck\n[Anexo][missing]\n![Imagen](absent.png)")
        self.assertEqual(len(self.result()["errors"]), 2)

    def test_adjacent_footnotes_are_not_reference_links(self):
        self.write("# Deck\nDato.[^a][^b]\n\n[^a]: Fuente A\n[^b]: Fuente B")
        self.assertEqual(self.result()["errors"], [])
        self.write("# Deck\n[Anexo][missing][^a]\n\n[^a]: Fuente A")
        self.assertEqual(len(self.result()["errors"]), 1)

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
