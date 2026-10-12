# Seguimiento independiente del setup

**Veredicto: APTO PARA SETUP, con caso pendiente.** H1–H8 quedan cerrados en el
alcance observado abajo. Esto permite empezar con el equipo; no certifica una
entrega, fuentes de terceros ni la elección del caso.

- Fecha local: 2026-10-12, Argentina (UTC−03).
- SHA final congelado: `e9eb842dce8151eaaff274a7d40997c0caa4c8e3`.
- Tree final: `e3eb256e34aeb6690b07eb86eeb76f78850b5d70`.
- Controles iniciales: `84af6b1c05d829360c757f4f1e4ffff3857ee304`, tree
  `ac32a46ec0fb492f0809b2e30d46d007923f33f2`. Entre ese SHA y el final solo
  cambian README y AGENTS; no cambian scripts, tests ni el skill.
- Referencia: `reviews/2026-10-11-setup-harness.md`, sin modificaciones.
- Revisor: Codex. No se leyeron reportes de autores ni conversación anterior;
  no hubo subagentes, fixes, instalaciones, push, PR ni merge.

## Cierre de hallazgos

| Hallazgo | Evidencia independiente de cierre | Ubicación actual |
|---|---|---|
| H1 — Índice vs working tree | Hook con índice inválido y working válido: exit 1. Índice válido y working inválido: exit 0. La suite también cubre links y archivos untracked; retirar snapshot o flag del hook hace fallar la regresión. | `.githooks/pre-commit:7`; `scripts/okf-check.py:365` |
| H2 — Separadores vs Marp | Los mismos fixtures `___` y `- - -` renderizan once secciones con Marp 4.1.2, pero el checker los rechaza. Once slides con `---` o `***` también fallan en draft y delivery. Retirar el rechazo de variantes hace fallar ocho subcasos. | `scripts/plan-check.py:216` |
| H3 — HTML local | Links locales HTML existentes e inexistentes se rechazan, directos y vía anexo. El enlace relativo sigue renderizándose en Marp, por lo que el cierre es una prohibición explícita del formato. Retirar ese control produce 48 fallas. | `scripts/plan-check.py:244` |
| H4 — YAML | `invalid: [` y `status` duplicado se rechazan. Se acepta YAML seguro con tipos correctos; falta de PyYAML devuelve error JSON limpio. Retirar unicidad produce tres fallas. | `scripts/plan-check.py:48` |
| H5 — Código/comentarios | Las probes originales de código inline, TODO cercado, comentario HTML y etiqueta SRC/src pasan. Un TODO visible y un link real roto siguen rechazándose. Retirar guards de código, comentarios y normalización hace fallar sus tests. | `scripts/plan-check.py:88`; `scripts/okf-check.py:77` y `:82` |
| H6 — Binarios | NUL y UTF-16: strict exit 2 con omisión redactada; texto con término sintético: exit 1. La suite cubre PARCIAL sin strict, PDF, payload de symlink y ambos sentidos índice/working. Retirar el estado de omisión produce seis fallas. | `scripts/leak-check.sh:125` y `:158` |
| H7 — Captura board | El skill exige diff HEAD, bytes y hashes de tracked/nuevos/fuentes, doble chequeo y copia inmutable. Su receta se reprodujo en memoria con staged, unstaged, parcial y archivo nuevo: captura completa, sin archivos de captura y cambio posterior detectable. | `.agents/skills/board-review/SKILL.md:24` |
| H8 — Draft vs verified | Cierre por lectura: focalizada discute la cifra draft como supuesto y nombra la verificación pendiente; integral exige verified. Se mantiene «no evaluable» para el esqueleto de setup. No se ejecutó el flujo de agentes. | `.agents/skills/board-review/SKILL.md:43` |

README y AGENTS del SHA final coinciden con los controles: PyYAML en ambos modos,
OKF staged en pre-commit, separadores compactos, links locales Markdown y
omisiones de privacidad parciales/rechazadas en strict. COMPLETA no garantiza privacidad.

## Comandos y salidas observadas

La suite se ejecutó una sola vez. No se repitió tras la alineación documental,
porque `git diff --name-only 84af6b1 HEAD` devuelve solo AGENTS y README.

```text
python3 -m unittest discover -s tests -v
Ran 76 tests in 13.241s
OK
Shell verificado: GNU bash, version 3.2.57(1)-release (arm64-apple-darwin26)
Shell verificado: GNU bash, version 5.3.20(1)-release (aarch64-apple-darwin25.6.0)

python3 tmp/audit/run-audit.py hook
hook invalid_index_valid_worktree exit=1
hook valid_index_invalid_worktree exit=0
binary_denylist exit=2
utf16_denylist exit=2
plain_denylist exit=1

python3 tmp/audit/run-audit.py probes
inline_code: errors=[]
visible_pending_in_code: errors=[]
yaml_invalid: Frontmatter YAML inválido
duplicate_yaml: Clave YAML duplicada: status
html_reference: Enlace HTML local no admitido
okf_reference_case: errors=[]
okf_comment_reference: errors=[]

python3 tmp/audit/followup-audit.py extra_probes
Once slides: --- / *** / ___ / - - - / * * * / _ _ _ / ---- / **** / ____
Todos: draft rejected=True; delivery rejected=True
html_via_annex: cuatro destinos existentes/inexistentes; rejected=True
visible_TODO ["plan/slides.md:12: TODO: real"]
missing_PyYAML exit=1; error="plan-check necesita PyYAML también en borrador"

python3 tmp/audit/followup-audit.py board_capture
staged / unstaged / partial:
captured_all_bytes=True diff_HEAD_has_final=True stable=True capture_writes=False
concurrent_change_detected=True

python3 scripts/plan-check.py --mode draft
plan-check (draft): 10 slides; 12 pendientes; 0 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas
python3 scripts/plan-check.py --mode delivery
Entrega rechazada: deck declarado draft
```

Se ejecutaron solo las nueve mutaciones necesarias para los guards nuevos, en
copias de scripts/tests/hook. Todas tuvieron base exit 0 y mutación exit 1 con
falla de aserción; no se contaron errores de ejecución como prueba del guard.

| Guard retirado en copia | Fallas observadas |
|---|---:|
| H1 snapshot del índice | 1 |
| H1 flag staged del hook | 1 |
| H2 rechazo de separador no canónico | 8 |
| H3 prohibición de HTML local | 48 |
| H4 claves YAML únicas | 3 |
| H5 código inline | 1 |
| H5 comentarios OKF | 1 |
| H5 etiquetas Markdown normalizadas | 3 |
| H6 registro de omisiones | 6 |

## Render y límites

Se leyó package.json de la caché disponible y se comprobó Marp CLI 4.1.2 antes
de usarlo. El intento inicial con la antigua ruta falló; no se usó ese intento
como evidencia de un render nuevo. No se reinstaló ninguna herramienta.

```text
python3 tmp/audit/run-audit.py render_probes
underscore_separator: checker rechaza; Marp exit=0; rendered_sections=11
spaced_separator: checker rechaza; Marp exit=0; rendered_sections=11
html_link_render: checker rechaza; Marp exit=0; html_link_present=True
frozen Marp exit=0
frozen_html_sha256=d53fd171ee71b875ff5d09f9f1e2288f9f2b09b6862f332232026bdb5f614d5e
```

El deck generado conserva el hash del HTML contrastado en la auditoría original.
No se repitió QA visual ni se regeneraron PDF/PPTX: no cambió la fuente del deck.
Los logs propios y drivers quedan ignorados en `tmp/audit/followup-*`.

H7 verifica instrucciones y su receta, no una invocación efectiva de board-review;
H8 es un cierre documental. Siguen sin comprobarse runtimes de roles,
onboarding Windows/Linux, CI, secreto remoto, protección de ramas y gitleaks.

No se certificaron fuentes, cifras ni privacidad exhaustiva. El caso, alcance,
responsables humanos y formato final siguen pendientes. No hay nuevos bloqueos
observados para setup dentro de H1–H8; no se amplió el alcance de la auditoría.
