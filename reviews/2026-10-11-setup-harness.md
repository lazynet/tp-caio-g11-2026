# Auditoría independiente del setup

**Veredicto: APTO CON CAMBIOS.** El contrato y el deck representan correctamente
un setup con caso pendiente. Hay dos fallas altas en los controles que conviene
cerrar antes del trabajo habitual del equipo; este informe no habilita una entrega.

- Fecha local: 2026-10-11, Argentina (UTC−03). El brief sugería 2026-10-12;
  se ajustó al día observado con `date`.
- SHA congelado revisado: `085ec7829607afd2b80df6173bc70b65ecd0f51c`.
- Base del diff: `21960493f6cb405ed57337432602aac4391e5a73`.
- Rama: `review/setup-harness`. Árbol limpio al comenzar y al terminar las pruebas.
- Revisor: Codex, con evidencia propia. No se leyeron reportes de autores ni
  conversación anterior. No se lanzaron subagentes ni se implementaron fixes.

## Alcance y criterio

Se revisaron los 25 archivos del diff integrado: README, AGENTS, los seis roles,
`board-review`, workflows, ignores, índices, ajuste de evaluación del programa,
fuente del deck, scripts y tests. También se contrastaron el hook pre-commit,
`setup.sh`, el symlink de skills y la configuración de VS Code.

El criterio es iniciar trabajo con el equipo, no defender un plan terminado.
`context/` solo contiene su índice y `plan/annexes/` solo `.gitkeep`: eso es
correcto en esta etapa. No se eligió caso ni se certificaron hechos de terceros.

Las pruebas adversarias y las mutaciones se hicieron en copias, repos y corpus
temporarios. El único cambio versionado de esta auditoría es este informe.
Los dueños sugeridos abajo son agentes; todos los responsables humanos siguen pendientes.

## Hallazgos

### H1 — Alta: el hook OKF valida otra versión que la que se commitea

**Ubicación:** `.githooks/pre-commit:7`, `scripts/okf-check.sh:7`,
`scripts/okf-check.py:251`. **Dueño sugerido:** `architect` para scripts;
`governance` para el control.

El scanner de privacidad usa `--cached`, pero OKF lee archivos del working tree.
Una ficha inválida staged y corregida sin stagear pasa el hook. La situación
inversa frena un índice válido por errores que no entrarían al commit.

En un repo sintético, con los scripts y el hook congelados, se guardó
`type: Invalid` en el índice y una ficha Supuesto válida en el working tree:

```text
hook invalid_index_valid_worktree exit=0
✓ leak-check: revisión PARCIAL; sin hallazgos
✓ okf-check: 4 archivos conformes en borrador; no implica aptitud para slides/entrega

git show :context/source.md
---
type: Invalid
---
# Fuente

hook valid_index_invalid_worktree exit=1
✗ context/source.md: type desconocido o inválido para el bundle
✗ okf-check: 6 errores
```

**Condición de cierre:** validar el snapshot del índice en pre-commit, incluidos
sus links, o rechazar explícitamente una divergencia relevante. Probar ambos
sentidos y observar fallar esa regresión al retirar el guard.

### H2 — Alta: el contador admite un deck que Marp renderiza con once slides

**Ubicación:** `scripts/plan-check.py:163`, `scripts/build-deck.sh:20`.
**Dueño sugerido:** `architect`, con `caio` para la regla del deck.

El contador reconoce solo `---` y `***` compactos. Marp 4.1.2 también divide
con `___` y `- - -`. Un archivo con once títulos separados por cualquiera de
estas variantes pasa ambos modos del validador como si tuviera una slide.

Se construyeron esos dos decks sintéticos con frontmatter `owner: caio`,
`status: ready`, `marp: true`, y se pasaron al checker y al renderer real:

```text
underscore_separator {"slides": 1, "errors": [], "pending": [], "references": [], "evidence": []}
underscore_separator Marp exit=0
rendered_sections=11
spaced_separator {"slides": 1, "errors": [], "pending": [], "references": [], "evidence": []}
spaced_separator Marp exit=0
rendered_sections=11
```

**Condición de cierre:** obtener el conteo del parser usado para renderizar o
rechazar todas las variantes fuera del formato permitido. La prueba debe
comparar contra el renderer y fallar al quitar el control.

### H3 — Media: los enlaces HTML eluden la selección de evidencia en entrega

**Ubicación:** `scripts/plan-check.py:92`, `scripts/plan-check.py:179`.
**Dueño sugerido:** `architect`, con `governance` para la trazabilidad.

Un enlace Markdown a una ficha draft activa OKF y rechaza la entrega. El mismo
destino en `<a href="context/source.md">Fuente</a>` queda fuera de references
y evidence. Marp conserva ese enlace HTML en el artefacto.

```text
html_reference {"slides": 1, "errors": [], "pending": [], "references": [], "evidence": []}
markdown_reference: entrega exige status: verified con revisión humana
html_link_render Marp exit=0
html_link_present=True
```

Se probó la resolución relativa desde el deck con una ficha sintética existente,
además del caso absoluto. No depende de una fuente ausente ni de un enlace web.

**Condición de cierre:** reconocer los enlaces HTML locales o prohibirlos con
error explícito. Cubrir una ficha draft y un destino inexistente, tanto directo
como desde un anexo, y verificar la regresión con el guard retirado.

### H4 — Media: el frontmatter del deck no se valida como YAML

**Ubicación:** `scripts/plan-check.py:42` y `scripts/plan-check.py:49`.
**Dueño sugerido:** `architect`.

El parser recoge líneas que coinciden con una expresión regular e ignora el
resto. Con las tres claves esperadas, agregar `invalid: [` deja pasar YAML
malformado; repetir `status: draft` y luego `status: ready` también pasa entrega.

```text
yaml_invalid {"slides": 1, "errors": [], "pending": [], "references": [], "evidence": []}
duplicate_yaml {"slides": 1, "errors": [], "pending": [], "references": [], "evidence": []}
yaml_invalid_render Marp exit=0
```

No se afirma que el renderer falle: en la prueba también aceptó el archivo.
El problema es que el chequeo estructural no rechaza una entrada inválida o
ambigua, mientras el validador OKF sí exige YAML válido y claves únicas.

**Condición de cierre:** definir y validar el frontmatter admitido, rechazando
sintaxis inválida y claves duplicadas. Mantener explícito el requisito de
dependencias si cambia el modo borrador.

### H5 — Media: falsos positivos en contenido Markdown que no es navegable

**Ubicación:** `scripts/plan-check.py:57`, `scripts/plan-check.py:205`,
`scripts/okf-check.py:73`, `scripts/okf-check.py:227`.
**Dueño sugerido:** `architect`.

El deck trata un link dentro de código inline como referencia real. El barrido
de pendientes usa el texto original, por lo que un TODO en un ejemplo cercado
frena entrega. OKF procesa links dentro de comentarios HTML y distingue
mayúsculas en etiquetas de referencia, a diferencia de Markdown.

```text
inline_code: Referencia local rota: missing.md
visible_pending_in_code: Entrega rechazada por pendiente: plan/slides.md:8: TODO: ejemplo
okf_comment_reference: link local inexistente o fuera del bundle: /missing.md
okf_reference_case: referencia Markdown sin definición: SRC
```

El último fixture usa `[Fuente][SRC]` y `[src]: /source.md`, con destino existente.
Los ejemplos y comentarios no deberían ampliar la evidencia usada. No se
confunden estos casos con pendientes visibles del plan actual, que son reales.

**Condición de cierre:** alinear los barridos con el contenido renderizado y
normalizar etiquetas Markdown. Cubrir ejemplos válidos junto con links y
pendientes reales que deben seguir fallando.

### H6 — Media: archivos binarios omitidos con salida «COMPLETA»

**Ubicación:** `scripts/leak-check.sh:79`, `scripts/leak-check.sh:95`,
`README.md:255`. **Dueño sugerido:** `governance`, con `architect` para scripts.

`git grep -I` omite binarios sin registrarlos como revisión incompleta. En un
repo sintético, un término de denylist se detecta como texto UTF-8, pero pasa
con un NUL o codificado en UTF-16. El modo estricto declara «COMPLETA» igual.

```text
binary_denylist exit=0
✓ leak-check: revisión COMPLETA; sin hallazgos
utf16_denylist exit=0
✓ leak-check: revisión COMPLETA; sin hallazgos
plain_denylist exit=1
✗ archivo #2, línea 1: denylist privada
```

Es un límite heredado del scanner previo, ahora acompañado por el nuevo estado
«COMPLETA». El README advierte que ninguna capa garantiza privacidad, pero no
identifica esta omisión concreta. La prueba usó únicamente un término inventado.

**Condición de cierre:** rechazar formatos fuera del alcance, inspeccionarlos,
o informar su omisión y limitar la afirmación de cobertura. Documentar también
que el patrón fijo de mail cubre el candidato actual, no cualquier dominio.

### H7 — Media: la captura de versión de board-review pierde cambios staged

**Ubicación:** `.agents/skills/board-review/SKILL.md:24`.
**Dueño sugerido:** `board`, con `caio` para el contrato de revisión.

El skill pide SHA, status y `git diff -- <objetivo>` para un objetivo sucio.
Ese diff compara working tree contra índice: si el cambio está enteramente
staged, guarda un diff vacío y no permite reconstruir el texto revisado desde HEAD.

```text
git status --short -- context/source.md
M  context/source.md
git diff -- context/source.md
<vacío>
git diff HEAD -- context/source.md
-title: Fuente sintética
+title: Otra fuente sintética
```

**Condición de cierre:** guardar el contenido revisado o un diff completo contra
HEAD, incluidos archivos nuevos sin tracking. Cubrir staged, unstaged, cambios
parciales y archivos nuevos sin mezclar el snapshot con modificaciones posteriores.

### H8 — Baja: requisito de verified sin distinguir la revisión del borrador

**Ubicación:** `.agents/skills/board-review/SKILL.md:28`, frente a
`AGENTS.md:136` y `.claude/agents/board.md:52`.
**Dueño sugerido:** `board`.

El skill exige aceptar una cifra solo si remonta a una ficha verified en todos
los modos. El contrato y el rol board sitúan ese requisito en entrega. Para una
revisión focalizada, un supuesto draft trazable debería poder discutirse como tal.

**Condición de cierre:** distinguir «revisable como supuesto de borrador» de
«aceptable para entrega». En un escenario focalizado con cifra draft, identificar
la verificación pendiente sin hacer pasar el borrador por una cifra aprobada.

## Coherencia que sí se sostiene

- README, AGENTS y los seis roles tratan el caso como pendiente. Las restricciones
  particulares del candidato se expresan como condicionales.
- La contradicción previa de finance que ponía cifras internas en `context/`
  está corregida. El dato real queda en `private/`; fuera, solo público o anonimizado.
- `caio` es el único editor del deck. Los anexos, las métricas y los gates tienen
  dueños por mirada; los agentes no inventan responsables humanos ni consenso.
- `board` no edita plan ni defensa. El guardado en reviews requiere autorización;
  `--chat` prohíbe escribir. La consigna del TIF reemplaza a CAIE como criterio.
- El setup pasa borrador y falla entrega. Una declaración humana estructuralmente
  válida no convierte un Supuesto en Hecho ni certifica su verdad.

## Board-review por lectura, sin ejecutar el flujo

| Escenario | Resultado del contrato leído | Límite o hallazgo |
|---|---|---|
| Focalizada con path | Un revisor pertinente; alcance de una sección | H8; no se probó invocación efectiva |
| Focalizada sin path | Preguntar por objetivo | Correcto por lectura |
| Integral sin path | `plan/`; cuatro roles y board al final | Setup: «no evaluable» como plan |
| `--chat` | Texto, sin archivos, incluso si corre board | Coherente con el rol board |
| Guardado autorizado | Solo reviews; no commit automático | Este commit lo autoriza el brief, no el skill |
| Runtime con 4 slots totales | Tres roles, luego finance, luego board | Aritmética correcta; no se ejecutaron tandas |
| Sin slots o sin subagentes | Secuencia/adoptar roles; declarar aislamiento ausente | No se promete independencia inexistente |
| Objetivo sucio | Guardar versión y diff | H7: captura incompleta |

No se ejecutó una integral sobre el setup ni se generaron preguntas de defensa
del caso: todavía no existe un plan evaluable. Las preguntas de cierre de esta
auditoría están al final y no eligen caso ni inventan contenido.

## Comandos y evidencia

Las siguientes salidas se observaron sobre el SHA congelado. Python observado:
3.11.5; PyYAML instalado: 6.0.1; `core.hooksPath=.githooks`; hook con modo 100755;
`.claude/skills` es symlink a `../.agents/skills`; VS Code declara `chat.useAgentsMdFile`.

```text
git rev-parse HEAD
085ec7829607afd2b80df6173bc70b65ecd0f51c
git status --short
<vacío>

python3 -m unittest discover -s tests -v
Ran 57 tests in 4.698s
OK
Shell verificado: GNU bash, version 3.2.57(1)-release (arm64-apple-darwin26)
Shell verificado: GNU bash, version 5.3.20(1)-release (aarch64-apple-darwin25.6.0)

bash scripts/okf-check.sh
✓ okf-check: 125 archivos conformes en borrador; no implica aptitud para slides/entrega
bash scripts/okf-check.sh --delivery
exit=1; ✗ okf-check: 122 errores

python3 scripts/plan-check.py --mode draft
plan-check (draft): 10 slides; 13 pendientes; 0 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas
python3 scripts/plan-check.py --mode delivery
exit=1; ERROR: Entrega rechazada: deck declarado draft

python3 -S scripts/okf-check.py --path context/index.md
✗ okf-check necesita Python 3 con PyYAML (python3 -m pip install pyyaml)

bash scripts/leak-check.sh --all
✓ leak-check: revisión COMPLETA; sin hallazgos
bash scripts/leak-check.sh --all --strict
✓ leak-check: revisión COMPLETA; sin hallazgos

git diff --check
<sin diagnósticos>
bash -n .githooks/pre-commit scripts/*.sh
<sin diagnósticos>
python3 -m py_compile scripts/okf-check.py scripts/plan-check.py
<sin diagnósticos>
```

Los dos chequeos de privacidad del árbol usaron la denylist local por el mecanismo
del scanner. No se abrió ni volcó su contenido, ni se evaluó su exhaustividad.
Las reproducciones adversarias usaron exclusivamente fixtures sintéticos.

### Mutaciones observadas

No se aceptó el verde de los tests como prueba suficiente. Se copiaron scripts
y tests a un directorio temporal, se corrió el test original, se retiró un guard
por vez y se observó una falla de aserción, no un error de importación.

| Guard retirado en copia | Test existente | Base → mutación |
|---|---|---|
| Path `private/` | `test_private_guard` | 0 → 1; failures=1 |
| Lectura `--cached` | `test_index_differs_from_worktree` | 0 → 1; failures=1 |
| Rechazo de error Git/scanner | `test_git_and_scanner_errors_never_succeed_or_leak` | 0 → 1; failures=3 |
| Autor humano en verified | `test_verified_requires_human_complete_block` | 0 → 1; failures=1 |
| Status verified en entrega | `test_absent_status_is_draft_not_delivery` | 0 → 1; failures=1 |
| Escape del bundle en links | `test_local_links_anchors_references_and_code_examples` | 0 → 1; failures=2 |
| Tope de diez slides | `test_ten_slides_pass_eleven_fail` | 0 → 1; failures=1 |
| Puente plan → OKF | `test_used_draft_rejected_and_human_verified_accepted` | 0 → 1; failures=1 |
| Pendientes de entrega | `test_draft_delivery_and_explicit_pending` | 0 → 1; failures=1 |

La evidencia completa quedó local en `tmp/audit/`: `tests.log`, `hook.log`,
`probes.log`, `mutations.log`, `baseline.log`, `render-probes.log` y los logs por
mutación. El driver es `tmp/audit/run-audit.py`; acepta `hook`, `probes`,
`mutations`, `baseline`, `qa` y `render_probes`. Son artefactos ignorados, no
dependencias del repo ni nuevos tests versionados. No se hizo mutation testing exhaustivo.

## QA del deck y contraste de fuente

Antes de usar los renders se comparó `plan/slides.md` en setup-audit,
deck-validation y setup-integrated: idénticos byte por byte. SHA-256 común:
`c96caed14515278f84e5bdac18c242a49be21d4769dfb644d637d6646d4f87f1`.

Luego se regeneró HTML desde la fuente congelada con el binario cacheado de
Marp CLI 4.1.2, sin instalación ni red. Coincidió exactamente con ambos HTML
provistos: `d53fd171ee71b875ff5d09f9f1e2288f9f2b09b6862f332232026bdb5f614d5e`.

```text
node <cache>/@marp-team/marp-cli/marp-cli.js --allow-local-files plan/slides.md -o tmp/audit/frozen-deck.html
frozen Marp exit=0
frozen_html_sha256=d53fd171ee71b875ff5d09f9f1e2288f9f2b09b6862f332232026bdb5f614d5e
pdfinfo <repo principal>/tmp/worktrees/deck-validation/out/deck-marp.pdf
Pages: 10
Page size: 960 x 540 pts
```

Se contrastó el texto completo extraído con `pdftotext` contra la fuente y se
inspeccionó visualmente `qa-all.png`, con las diez páginas. Los títulos y
pendientes coinciden; no se observaron recortes, superposiciones ni glifos rotos.

El PDF provisto tiene SHA-256
`184f9c16205bab3a6e60948f25616b78a2d02dbcfd1247be341f9d3532e22206`;
el montaje PNG, `ce4418f8b28c190646f0b12b2b2a59a7ee48686e5174d09ff25689849c7a6ffb`.
No se regeneraron PDF ni PPTX en esta auditoría. La legibilidad del esqueleto no
prueba que el futuro contenido completo entre en diez slides.

## Límites

- No se verificaron acceso real a fuentes, cifras, normativa, ni verdad de las
  fichas. Son borradores; el corpus falla entrega como corresponde.
- No se ejecutaron gws, credenciales, vault, push, PR, merge ni configuración de
  herramientas. No se inspeccionaron datos internos del caso.
- El intento inicial `npx --offline` falló con `ENOTCACHED`. Se usó el ejecutable
  cacheado cuya versión 4.1.2 se leyó de su package.json. Se verificó el renderer;
  no se completó `build-deck.sh all` ni su descarga vía npx en esta sesión.
- No se ejecutó CI ni se verificaron secreto remoto, protección de ramas,
  gitleaks en Docker, onboarding Windows/Linux o invocación efectiva de los roles
  en Claude Code y Copilot. Las afirmaciones históricas de observación de esos
  runtimes permanecen como evidencia previa no revalidada.
- Este runtime tiene apply_patch, ejecución y colaboración con cuatro slots,
  pero se respetó la prohibición de subagentes. No permite certificar una prueba
  de los agentes personalizados mediante el nombre del rol.
- No hay `graphify-out/graph.json`; se usó lectura de código y búsqueda dirigida,
  sin instalar ni construir un grafo. No se usó seguimiento de goal porque no se
  pidió crear uno. Se mantuvo la secuencia en el driver y en este informe.
- `verify-before-done` y `pdf` se usaron como guía de verificación. La delegación
  sugerida por el primero se omitió por el brief; en Codex se omitió
  `lh metrics record-verify` conforme al propio skill.

## Cierre y preguntas pendientes

H1 y H2 deben cerrarse antes de tratar los controles como barrera del trabajo
habitual. H3 y H4 deben cerrarse antes de confiar en el modo entrega. H5–H8
requieren ajustar cobertura y procedimiento; ninguno justifica inventar el caso.

Preguntas para el dueño de la integración, sin decisiones inventadas:

1. Quién toma H1 y H2 y aporta la regresión con guard retirado?
2. Se admite HTML y todo Markdown de Marp, o se define un subconjunto validado?
3. Qué formatos puede escanear privacidad y cómo informa los que omite?
4. Qué snapshot guarda board-review cuando hay staging parcial o archivos nuevos?
5. Qué pruebas de runtime y onboarding hará el equipo antes de actualizar las
   celdas «a probar» y qué humanos asumirán las secciones cuando elijan caso?

Las preguntas son parte del reporte de auditoría, no pedidos de aprobación ni
bloqueos para escribirlo. El caso, alcance, formato final y responsables humanos
siguen pendientes del equipo.
