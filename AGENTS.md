# AGENTS.md — tp-caio-g11-2026

`AGENTS.md` es el contrato portable para los agentes de IA y la fuente única de
las reglas del repo. Claude y VS Code leen los roles de `.claude/agents/`
(soporte por runtime en `README.md`); los adaptadores de Codex se
generan.

## Idioma

**Todo en español rioplatense**: la conversación con el equipo, los documentos,
las definiciones de agentes y skills, los comentarios en scripts y los mensajes
de commit. Registro ejecutivo en los entregables y voseo en todo el repo.
Solo quedan en inglés los nombres de archivos y carpetas, las claves de
frontmatter y los identificadores de código, porque las herramientas los esperan así.

## Qué es este repo

El Trabajo Integrador Final de la *Diplomatura Chief AI Officer (CAIO)* de UTN BA:
un **Plan Maestro del CAIO a 12 meses** para una organización, defendido ante un board.

**Estado y responsables:** consultá el estado y el reparto acordado en
`README.md`; es su única fuente. No conviertas pendientes en decisiones.

**Entrega:** un único PDF de menos de 10 MB, con máximo diez slides (portada y
equipo incluidas) y anexos. Generar el PDF no lo habilita: usá
`scripts/build-deck.sh entrega --delivery`, que exige el gate de entrega.

El plan tiene que integrar:

- Estrategia integral: arquitectura, gobierno, seguridad, people plan y finanzas.
- Roadmap técnico, financiero y cultural, con hitos y criterios de éxito.
- Financial storytelling para un CFO escéptico.
- Roadmap ajustado por riesgo: escenarios, contingencias, decisiones reversibles e irreversibles.
- Preparación de la defensa: storyline, objeciones anticipadas, evidencia.

**Regla de formato:** lo que el board tiene que *decidir* va en las slides; lo que
lo *sustenta*, en anexos de evidencia procesada (`plan/annexes/_template.md`).

**Equipo:** Grupo 11, 8 integrantes. Onboarding y reparto en `README.md`.

**Todo se genera.** `plan/slides.md` (markdown compatible con Marp, slides
separadas por `---` o `***` compactos; links locales en Markdown, no en HTML) es
la única fuente del deck. `scripts/build-deck.sh` lo renderiza en `out/` (fuera
de git) y arma `out/Grupo11-AcmeLabs-PlanMaestroCAIO.pdf` (deck + anexos), el
único entregable (borrador: `-borrador`). Nada generado se edita: se corrige el
markdown y se regenera. Requisitos (Python 3.11+, PyYAML y pypdf en `.venv`,
`CAIO_PYTHON`) y chequeos en `README.md`.

**Fechas:** consultá el cronograma de `README.md`, sección "Fechas".

## Estructura

| Path | Qué tiene |
|---|---|
| `context/` | Bundle OKF: hechos públicos o anonimizados y supuestos sobre el caso, cada uno con su fuente |
| `material/` | Bundle OKF: unidades y frameworks de la cursada, y qué sección del plan respalda cada uno |
| `plan/slides.md` | Las 10 slides, fuente única del deck |
| `plan/theme/acme.css` | El tema de Marp del deck (portado de Claude Design); `slides.md` usa sus clases en bloques HTML |
| `plan/annexes/` | Un anexo por archivo (`NN-tema.md`, desde `_template.md`), enlazado en slides |
| `defense/` | Storyline, banco de objeciones; `defense/evidence/` es un bundle OKF |
| `reviews/` | Revisiones del board y del peer review, con fecha |
| `scripts/build-deck.sh` | Genera el deck y la entrega: `all` (default), `entrega`, `marp`, `pandoc` o `html` |
| `.claude/agents/` | Los agentes por rol, fuente única para todas las herramientas |
| `.agents/skills/` | Skills portables; `.claude/skills` es un symlink a esta carpeta |
| `.codex/agents/` | Adaptadores TOML generados desde `.claude/agents/`; no se editan |
| `scripts/harness-check.py` | Valida roles, rutas y adaptadores; `--write` los regenera |

## Fuentes

- Material de la cursada (PDFs, frameworks): carpeta de Google Drive de Martin.
  La ruta local está en `private/sources.md`, que no se versiona. Los PDFs no se
  copian al repo; si no tenés acceso, usá `material/index.md`.
- Notebook consolidado: https://notebook.google.com/notebook/57ec4d6d-41a0-4030-9273-9bfc94cfb4ae
  (los agentes no pueden leerlo; los extractos se pegan en `material/`).

## Datos privados

**El repo es público** (github.com/lazynet/tp-caio-g11-2026). Lo que se pushea no se
puede despublicar: aunque después se borre o el repo pase a privado, puede quedar
en forks, clones y caches. La regla vale para **cualquier organización** que se
analice, sea cual sea el caso elegido:

- **Nunca se versiona** ningún dato interno de una organización: nombres de
  clientes, proyectos internos, personas, montos de contratos, tarifas, P&L,
  headcount, mails o rutas corporativas, credenciales.
- **El dato real vive solo en `private/`**, que está en `.gitignore` y existe
  solo en la máquina de quien tiene acceso. Los agentes pueden leerlo para
  razonar, pero lo que escriben fuera de `private/` sale anonimizado.
- **Cómo se anonimiza:** clientes como "Cliente A (banco)" o "Cliente B
  (fintech)"; cifras como rangos, ratios o índices (base 100); personas por rol
  ("CFO", "Chief Architect"). Si un dato no se puede anonimizar sin perder
  sentido, no va.
- `context/` tiene hechos públicos (sitio web, prensa, LinkedIn) o ya
  anonimizados, cada uno con su fuente, y supuestos marcados como tales. Nunca
  datos internos reales.
- **Antes de escribir cualquier archivo fuera de `private/`**, el agente revisa
  que no contenga nada de lo anterior. Si tenés acceso a fuentes internas de una
  organización (repos, colecciones QMD `flex-*`, Drive), extremá el cuidado.
- **Chequeo automático:** `scripts/leak-check.sh` corre en cada commit (hook que
  activa `scripts/setup.sh`) y en GitHub Actions (`leak-guard`). Revisa patrones
  fijos y una denylist privada (`.leak-denylist` local, secreto `LEAK_DENYLIST`
  en GitHub). Cubre solo texto UTF-8: lo que omite deja la revisión PARCIAL y
  `--strict` la rechaza. Ni COMPLETA ni `--strict` certifican ausencia de datos
  privados. Nunca uses `git commit --no-verify` para saltearlo.

## Bases de conocimiento (OKF)

`context/`, `material/` y `defense/evidence/` siguen
[OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md):
un archivo por concepto, con frontmatter YAML, y links markdown absolutos al
bundle (`/unidades/m1u2-portfolio-100-dias.md`) para que el grafo se pueda recorrer.

- **`type` es obligatorio.** Usamos `Hecho` y `Supuesto` en `context/`; `Unidad`,
  `Framework`, `Concepto`, `Caso`, `Apunte de clase`, `Programa`, `Mapa` y `Hueco`
  en `material/`; `Evidencia` en `defense/evidence/`. Si necesitás un tipo nuevo,
  sumalo acá. Para buscar algo en `material/`, empezá por `material/index.md` y
  `material/mapa-plan-fuentes.md`; antes de usar una cifra, mirá `material/huecos.md`.
- **También van** `title`, `description` (una oración) y `generated: { by, at }`.
  Quien escribe va en `generated.by` (`claude-code/<modelo>`, `codex/<modelo>`,
  `copilot/<modelo>` o `human:<usuario-github>`).
- **Fuentes.** `sources` lleva un `id` por fuente, y cada afirmación la cita con
  una nota al pie cuya etiqueta es el `id`: `[^m1u2]`. Es obligatorio en `Hecho`,
  `Evidencia` y en toda afirmación atribuida a terceros. `Mapa` y `Hueco` pueden
  ir sin fuentes externas porque describen el estado del corpus.
- **Estado.** `draft` (default), `accepted` (admitida al corpus) o `verified`.
  Ficha nueva: `status` explícito; cautelas en `# Cautelas`.
- **Declaración humana.** `accepted` y `verified` requieren un bloque homónimo
  `{ by: human:<usuario-github>, at: <fecha ISO>, scope: "<fuente y alcance>" }`.
  Declaraciones humanas, registradas solo por instrucción expresa.
  `accepted` admite material; toda cifra entregada exige `verified`. Antes de
  pasar una ficha de `context/` a `verified`, recalculá sus cifras derivadas con
  sus insumos, retirá o acotá lo que la fuente no acredita y mostrá ese diff.
- **Revisar no cambia el tipo.** Un `Supuesto` o una propuesta revisados siguen
  siendo supuesto o propuesta; no se convierten en `Hecho`.
- **Draft y entrega.** Un borrador admite faltantes si están identificados (en
  `# Cautelas` o en `material/huecos.md`). La versión de peer review y la entrega
  no: toda cifra de una slide o anexo entregado remonta a una ficha `verified`.
- **Índices.** La raíz de cada bundle tiene un `index.md` con `okf_version` como
  único frontmatter. Al sumar un concepto, se agrega su línea con la `description`.
- **Chequeo automático:** `scripts/okf-check.sh` corre en borrador en el
  pre-commit (índice completo, `--staged`) y en CI (árbol versionado); YAML
  seguro, sin claves duplicadas. `--delivery` y `plan-check.py --mode delivery`
  validan estructura y revisión declarada, no la verdad del contenido.

## Reglas

- **La audiencia es toda la cohorte** y cualquiera en internet: aplicá "Datos
  privados".
- **Todo número tiene fuente.** Una cifra en una slide se rastrea hasta un
  anexo, y el anexo dice el supuesto o la fuente. Los supuestos se marcan como
  tales. Cada cifra, criterio, umbral o superlativo nuevo en slides o anexos se
  cita con su línea del anexo fuente antes de commitear; si el anexo no lo dice,
  queda como faltante y no se agrega.
- **Los totales se recalculan.** Antes de commitear un anexo, recalculá cada
  total y promedio desde sus componentes y mostrá la comparación.
- **Un editor por archivo.** `caio` es el único que edita `plan/slides.md`. Cada
  anexo declara su agente dueño en el frontmatter (`owner: finance`) y lo
  escribe ese dueño; los demás le proponen cambios. Los responsables humanos
  están en `README.md`; una asignación nueva requiere acuerdo del equipo.
- **Seguimiento.** GitHub Issues es el backlog: registrá el trabajo en el issue
  de su sección y enlazalo desde el PR con evidencia de cierre. Flujo:
  `README.md`, "Backlog y seguimiento".
- **Edición entre sesiones.** El rol define quién puede editar, no bloquea el
  archivo: coordiná en el issue, con una rama o worktree por tarea. Dos sesiones
  del mismo rol no editan el mismo archivo en paralelo.
- **Desacuerdos a la vista.** Si dos miradas chocan, se dejan explícitas con
  alternativas y evidencia, sin inventar consenso.
- **Revisiones proporcionales.** Un borrador alcanza con una revisión focalizada
  (el agente de esa mirada o `board` sobre la sección) y feedback humano. El
  skill `board-review` completo se corre antes del peer review y de la entrega.
- Que slides o PDF no desbordan se afirma tras abrir el render y describir lo
  visto; contar páginas no es revisión visual.
- En `plan/slides.md`, secciones y slides se citan por nombre ("ver Roadmap"),
  no por número: los eyebrows y el paginador no coinciden.
- Slides, anexos, fichas e índices se editan con Edit, no con scripts
  (reemplazos masivos, `awk` seguido de `mv`); revisá `git diff` antes de reportar.
- Commits: `tipo: descripción corta` en español, sin trailers.
- Cambios a `main` por PR y con chequeos en verde; sin cupo fijo de
  aprobaciones, el ruleset pide una extra si hay cambios no atribuidos (agentes).
  No uses `--admin` ni saltees hooks. No publiques sin autorización del pedido.

## Agentes

Copilotos sintéticos por rol: `caio`, `architect`, `governance`, `people`,
`finance` y `board`. Cada uno es dueño de la mirada que dice la `description`
de `.claude/agents/<rol>.md`; `caio` integra y edita el deck.

**Contrato común de salida.** Toda propuesta de un agente dice, en breve y
adaptado a su rol: problema, evidencia o supuesto, alternativas, recomendación,
dependencias, costo (si corresponde), riesgo, responsable humano (pendiente o
acordado), criterio de éxito y condición de abandono. Si falta información, el
agente la marca como faltante o supuesto y sigue; no la inventa.

**Multi harness.** El soporte por runtime está en `README.md`, "Los agentes".
Sin rol nativo, leé `.claude/agents/<rol>.md` y adoptalo; su campo `tools` no
configura permisos fuera de Claude. Listar, cargar e invocar son evidencias
distintas.
