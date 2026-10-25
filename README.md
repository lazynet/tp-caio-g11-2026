# Plan Maestro CAIO · Grupo 11

**Equipo:** Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro ·
Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo

Repo del Trabajo Integrador Final de la Diplomatura CAIO (UTN BA): un Plan
Maestro del CAIO a 12 meses, entregado en un único PDF de menos de 10 MB: 10
slides como máximo (incluyendo portada y equipo) más anexos.

**Estado:** el plan está completo y la entrega final se genera con el gate de
entrega (`build-deck.sh entrega --delivery`). El caso elegido es **Acme Labs**,
confirmado por el equipo. El alcance acordado en comisión es la organización
completa (IA en el producto y en la operación interna).

Acuerdo informado por Martín el 20/10/2026 (seguimiento cerrado:
[#15](https://github.com/lazynet/tp-caio-g11-2026/issues/15)). Los
[responsables](#responsables-del-equipo) están acordados y el seguimiento se
hace en el [backlog de GitHub Issues](#backlog-y-seguimiento).

> **El repo es público.** Ningún dato interno de ninguna organización entra acá:
> ver [Datos privados](#datos-privados) antes de escribir nada.

Acá no se escriben slides a mano. Se escribe markdown y el deck se **genera**.
Los agentes de IA del repo ayudan a producir cada sección y a atacarla antes de
que la vea otro equipo.

## Qué necesitás

| Herramienta | Para qué |
|---|---|
| Cuenta de GitHub ([github.com/signup](https://github.com/signup)) | escribir en el repo |
| git y [GitHub CLI](https://cli.github.com) (`gh`) | bajar y subir cambios |
| Un agente de IA: [Claude Code](https://claude.com/claude-code), [Codex](https://developers.openai.com/codex) o VS Code con GitHub Copilot | trabajar con los agentes por rol |
| Python 3.11 o más nuevo, con PyYAML y pypdf | correr los chequeos (datos privados, OKF, deck) y armar el PDF de entrega |
| Node.js 18 o más nuevo | generar el deck con Marp |
| Chrome, Edge o Chromium | Marp lo usa para exportar pdf y pptx; también imprime los anexos |
| pandoc | generar el pptx editable y el html de los anexos |
| Un editor de markdown (VS Code, Obsidian, etc.) | leer y editar |

No necesitás saber programar: todo es markdown, y el agente corre los comandos
por vos si se lo pedís.

### Instalación según tu sistema

**macOS** (con [Homebrew](https://brew.sh)):

```bash
brew install git gh node pandoc python
gh auth login
```

**Windows** (PowerShell; `winget` viene con Windows 10 y 11):

```powershell
winget install Git.Git GitHub.cli OpenJS.NodeJS.LTS JohnMacFarlane.Pandoc Python.Python.3.12
gh auth login
```

Después usá **Git Bash** (se instala con Git) para todos los comandos de este
README: los scripts son bash y no corren en PowerShell ni en `cmd`. Edge ya
viene instalado, así que Marp no necesita nada más.

Para que Claude Code encuentre el skill `board-review` hace falta que git cree
symlinks: activá el **Modo de desarrollador** (Configuración → Sistema → Para
programadores) y cloná con el flag que figura en
[Primeros 15 minutos](#primeros-15-minutos). Si preferís evitarte esto, usá
[WSL](https://learn.microsoft.com/windows/wsl/install) y seguí las
instrucciones de Linux adentro de WSL.

**Linux** (Debian o Ubuntu 24.04+):

```bash
sudo apt install git gh nodejs npm pandoc chromium python3 python3-venv
gh auth login
```

Si tu distro trae un Node más viejo que 18 (`node --version`), instalalo desde
[nodejs.org](https://nodejs.org). Si `gh` no está en tus repos, seguí
[las instrucciones oficiales](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).
En Fedora: `sudo dnf install git gh nodejs pandoc chromium python3`.

Las instrucciones de Windows y Linux todavía no están probadas en este repo. Si
algo falla, contalo y corregí este README.

### Python y PyYAML

Los chequeos son Python: el de datos privados usa solo la biblioteca estándar;
el de OKF y el del deck (`plan-check`, en los dos modos) necesitan **PyYAML** y
fallan sin él; el PDF de entrega además necesita **pypdf**. CI usa
Python 3.11 o más nuevo. Después de clonar, instalá los dos en un entorno
virtual `.venv` dentro del repo (no se versiona), nunca con `pip` global:

**macOS y Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pyyaml pypdf
```

**Windows (Git Bash):** ahí Python se llama `python` (o `py`), no `python3`, y
los scripts lo eligen con la variable `CAIO_PYTHON`:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install pyyaml pypdf
export CAIO_PYTHON=python
```

Activá el `.venv` (y en Windows exportá `CAIO_PYTHON`) en cada terminal antes de
commitear o correr scripts: el hook pre-commit corre `scripts/okf-check.sh
--staged` y necesita PyYAML. Si el agente commitea por vos, pedile que active
el `.venv` primero. Un `alias python3=python` no sirve: los scripts no heredan alias.
Sin `CAIO_PYTHON`, los scripts usan `python3`.

## Cómo sumarte

1. Abrí un issue con la plantilla **"Sumarme al equipo"**:
   [github.com/lazynet/tp-caio-g11-2026/issues/new/choose](https://github.com/lazynet/tp-caio-g11-2026/issues/new/choose).
2. Martin te manda la invitación (`scripts/add-member.sh <usuario> <issue>`).
3. Aceptala en [github.com/lazynet/tp-caio-g11-2026/invitations](https://github.com/lazynet/tp-caio-g11-2026/invitations)
   (vence a los 7 días).

Mientras el repo sea público podés leerlo y clonarlo sin invitación; la
invitación te da permiso para escribir. Cuando estemos todos adentro, el repo
pasa a privado (`scripts/make-private.sh`) y los que ya están conservan el acceso.

## Primeros 15 minutos

1. Cloná el repo y activá el chequeo de datos privados:

   ```bash
   gh repo clone lazynet/tp-caio-g11-2026 -- -c core.symlinks=true
   cd tp-caio-g11-2026
   ./scripts/setup.sh
   ```

   El `-c core.symlinks=true` solo importa en Windows; en macOS y Linux no cambia nada.
   Después creá el `.venv` con PyYAML y pypdf (ver [Python y PyYAML](#python-y-pyyaml)).

2. Abrí tu agente ahí: `claude`, `codex`, o la carpeta en VS Code con el chat de Copilot.
3. Pedile: *"leé AGENTS.md y material/index.md y contame en qué estado está el plan"*.
4. Generá el deck: `./scripts/build-deck.sh` (o pedíselo al agente) y abrí
   `out/deck-marp.html` en el navegador.

## Cómo está organizado

| Carpeta | Qué hay | Agente dueño |
|---|---|---|
| `plan/slides.md` | las 10 slides, fuente única del deck | `caio`, único editor; los demás le proponen |
| `plan/annexes/` | un anexo por tema (`NN-tema.md`, copiado de `_template.md`): la evidencia que sostiene cada slide | el agente dueño del tema (`owner:`) |
| `context/` | hechos **públicos** o anonimizados de Acme Labs y supuestos, uno por archivo, con su fuente y estado de revisión | — |
| `private/` | datos internos reales — **solo local, nunca se versiona** | quien tenga el acceso |
| `material/` | una ficha por unidad y por framework de la cursada, y qué sección del plan respalda cada uno | — |
| `defense/` | storyline y objeciones; `structure-pilot.md` es el piloto de la propuesta de Lucho ([#27](https://github.com/lazynet/tp-caio-g11-2026/issues/27)), no incorporada a la entrega | `caio`; `board` aporta desde `reviews/` |
| `defense/evidence/` | una ficha por evidencia: qué objeción responde y de dónde sale | `caio` |
| `reviews/` | revisiones del board, de los docentes simulados y del setup, con fecha | `board` |
| `plan/theme/` | `acme.css`, el tema de Marp del deck | `caio` |
| `scripts/` | build, chequeos (privados, OKF, deck, harness) y setup | — |
| `tests/` | pruebas de los scripts | — |
| `.claude/agents/`, `.agents/skills/` | roles y skills (fuente única); `.codex/agents/` se genera | — |
| `out/` | decks generados y `Grupo11-AcmeLabs-PlanMaestroCAIO.pdf` — **no se versiona ni se edita** | el script |

El agente dueño organiza la edición; el responsable humano coordina la revisión
y la defensa de su sección. El reparto acordado está en la tabla siguiente.

## Responsables del equipo

| Actividad | Responsable humano | Fuente | Tarea de seguimiento |
|---|---|---|---|
| Diagnóstico: leerlo y defenderlo | Martín | [Anexo A](plan/annexes/01-diagnostico.md) | [#15](https://github.com/lazynet/tp-caio-g11-2026/issues/15) |
| Arquitectura | Nico | [Anexo B](plan/annexes/02-arquitectura.md) | [#16](https://github.com/lazynet/tp-caio-g11-2026/issues/16) |
| Gobierno y seguridad | Rafa | [Anexo C](plan/annexes/03-gobierno-seguridad.md) | [#17](https://github.com/lazynet/tp-caio-g11-2026/issues/17) |
| Personas y cultura | Pablo | [Anexo D](plan/annexes/04-personas-cultura.md) | [#18](https://github.com/lazynet/tp-caio-g11-2026/issues/18) |
| Business case | Gabriela | [Anexo E](plan/annexes/05-business-case.md) | [#19](https://github.com/lazynet/tp-caio-g11-2026/issues/19) |
| Roadmap y riesgo | Maxi | [Anexo F](plan/annexes/06-roadmap-riesgo.md) | [#20](https://github.com/lazynet/tp-caio-g11-2026/issues/20) |
| Resoluciones del Directorio | Martín | [Anexo G](plan/annexes/07-resoluciones.md) | [#52](https://github.com/lazynet/tp-caio-g11-2026/pull/52) |
| Defensa: storyline, objeciones y quién presenta cada slide | Lucho | [Defensa](defense/) | [#21](https://github.com/lazynet/tp-caio-g11-2026/issues/21) |
| Verificar el material de la cursada | Eduardo | [Índice del material](material/index.md) | [#22](https://github.com/lazynet/tp-caio-g11-2026/issues/22) |

Estos responsables son del TP: no reemplazan a las autoridades de Acme Labs
que deben validar datos, liberar agendas, aceptar riesgos o aprobar presupuesto.
El reparto de slides se acuerda en la tarea de defensa.

Rafa y Maxi no tienen assignee en GitHub
([#17](https://github.com/lazynet/tp-caio-g11-2026/issues/17),
[#20](https://github.com/lazynet/tp-caio-g11-2026/issues/20)); su responsable
figura en el texto.

`context/`, `material/` y `defense/evidence/` siguen el formato abierto
[OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md):
un archivo markdown por concepto, con su fuente arriba y links entre fichas. Para
ver qué hay, abrí el `index.md` de cada carpeta. Las reglas están en `AGENTS.md`,
"Bases de conocimiento (OKF)"; si escribís con un agente, ya las conoce.

## Los agentes

Cada agente es un copiloto con una mirada. Probá invocarlo por nombre según
el soporte de tu harness (ver la matriz de abajo):

| Agente | Le pedís… |
|---|---|
| `caio` | la historia, qué entra en las 10 slides, el roadmap con escenarios |
| `architect` | arquitectura objetivo, build vs buy, roadmap técnico |
| `governance` | gobierno, políticas, seguridad, EU AI Act |
| `people` | estructura, talento, AI literacy, cambio cultural |
| `finance` | inversión, ROI, escenarios, el relato para el CFO |
| `board` | que te destroce una sección antes que lo haga el board real |

Ejemplos:

- *"Con el agente finance, iterá plan/annexes/05-business-case.md"*
- *"Usá architect para proponer 2 alternativas de arquitectura con tradeoffs"*
- *"Corré board-review sobre plan/annexes/05-business-case.md"*: revisión focalizada de
  un borrador, con un solo revisor pertinente. El path es obligatorio.
- *"Corré board-review --integral y guardá la revisión en reviews/"*: las cuatro
  miradas y después el board consolida, sobre `plan/` y `defense/` si no das otro objetivo.
  Es para antes del peer review y de la entrega.
- *"Corré board-review sobre plan/annexes/05-business-case.md --chat"*: la revisión vuelve
  en la conversación y no se escribe ningún archivo.

Ni el skill ni el agente `board` escriben en `reviews/` si no se lo pedís; ante
la duda responden en el chat y te ofrecen guardar.

Cada agente sigue el contrato común de salida de `AGENTS.md`, sección "Agentes".

Las definiciones son compartidas. El descubrimiento, las herramientas y los
permisos dependen del harness. La compatibilidad documentada no equivale a una
invocación probada con el plan:

| Herramienta | Instrucciones (`AGENTS.md`) | Agentes por rol | Skill `board-review` |
|---|---|---|---|
| Claude Code | observado el 2026-10-11; requiere condiciones de carga de abajo | `.claude/agents/`; listados, invocación no probada al 2026-10-25 | `.claude/skills/`; listado, invocación no probada al 2026-10-25 |
| VS Code + Copilot | configurado en `.vscode/settings.json`; carga no probada al 2026-10-25 | `.claude/agents/` compatible según documentación; invocación no probada al 2026-10-25 | `.agents/skills/` y alias Claude; invocación no probada al 2026-10-25 |
| Codex | observado: leyó `AGENTS.md` y ejecutó briefs en worktrees | `.codex/agents/*.toml` generado; carga e invocación no probada al 2026-10-25 en el runtime de cada integrante | `.agents/skills/`; listado en esta sesión de Codex, invocación no probada al 2026-10-25 |

Claude Code admite `AGENTS.md` directamente desde la versión 2.1.277, pero su
carga puede quedar desplazada por un `CLAUDE.md` o `CLAUDE.local.md` en el repo o
en sus ancestros. Revisá la configuración de instrucciones del proyecto; para
versiones anteriores, actualizá o pedí explícitamente leer `AGENTS.md`.
Ver [condiciones de carga de Claude](https://code.claude.com/docs/en/memory#agentsmd).

VS Code documenta agentes en formato Claude; esto no certifica Copilot CLI ni el
agente cloud. Ver [ubicaciones y formatos de VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents).
Codex documenta agentes propios en TOML; que no tenga un flag `--agent` no
demuestra que no pueda delegar a un rol. Ver [subagentes de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Los roles se editan solo en `.claude/agents/`; los skills, en `.agents/skills/`.
Después de cambiar un rol, corré `python3 scripts/harness-check.py --write` y
versioná los adaptadores generados. CI rechaza rutas inexistentes de `plan/` y `defense/` en los roles, dueños sin
rol y adaptadores desactualizados. `--write` no borra archivos huérfanos.

Si no hay invocación nativa, pedile al agente leer `.claude/agents/<rol>.md` y
adoptar ese rol. El frontmatter `tools` configura Claude; los adaptadores Codex
transportan el texto y heredan los permisos de su sesión. Las restricciones de
escritura por rol siguen siendo instrucciones, no un aislamiento de filesystem.

Para registrar una prueba, anotá herramienta y versión, rol, prompt, archivos
leídos o modificados y resultado. Probá lectura, edición del archivo propio y
revisión sin cambios; para `board-review`, además aislamiento de contexto y
consolidación. Nunca marques toda una fila como probada por haber listado roles.

## Cómo trabajamos

1. **Una sección, un dueño.** Coordiná con el responsable humano y registrá el
   trabajo en su issue. Cada anexo declara su agente dueño (`owner:`) arriba;
   las slides las edita solo `caio`, y los demás le proponen cambios.
2. **Todo número tiene fuente.** Si es un supuesto, se marca como supuesto. Una
   cifra entra a la entrega solo si una persona la verificó contra la fuente.
3. **Nada interno de ninguna organización en el repo.** Ver [Datos
   privados](#datos-privados).
4. **Revisión a la medida.** Para compartir el borrador de una sección alcanza
   con una revisión focalizada y feedback humano; el `board-review` completo va
   antes del peer review y de la entrega.
5. **Desacuerdos a la vista.** Si dos miradas chocan, se dejan las alternativas
   con su evidencia; no se inventa consenso.
6. **Las slides no se tocan en el pptx.** Si algo está mal en el deck, se
   corrige en `plan/slides.md` y se regenera.
7. **Cambios a `main` por pull request.** El ruleset «main protegida» no acepta
   push directo ni force-push a `main` y exige que pasen los chequeos
   `leak-check` y `gitleaks`: trabajá en una rama y abrí un PR. El ruleset no
   exige aprobaciones (0 requeridas); por convención del equipo, Martin revisa
   cada PR (`.github/CODEOWNERS` se lo solicita). No uses `--admin` ni saltees
   hooks. Enlazá el issue que resuelve y su evidencia de cierre. Si no sabés
   cómo, pedíselo a tu agente: *"commiteá esto en una rama nueva y abrí un PR"*.

## Datos privados

El repo es público: cualquiera en internet lo puede leer, y lo que se pushea no
se puede despublicar. Borrarlo después o pasar el repo a privado no alcanza,
porque puede haber quedado en clones, forks o caches.

La regla vale para cualquier organización que analicemos, sea cual sea el caso.

**Nunca entra al repo:** nombres de clientes o de proyectos internos, nombres de
personas de la organización, montos de contratos, tarifas, P&L, headcount,
mails o rutas corporativas, credenciales.

**Cómo se escribe en cambio:** "Cliente A (banco)", "Cliente B (fintech)";
cifras en rangos, ratios o índice base 100; personas por rol ("el CFO").

**Dónde va el dato real:** solo en `private/`, que no se versiona y existe solo
en la máquina de quien tiene el acceso. `context/` lleva hechos públicos o
anonimizados y supuestos, nunca el dato real.

**Qué te protege:**

| Capa | Qué hace | Dónde |
|---|---|---|
| Hook pre-commit | frena el commit si encuentra un dato prohibido en lo que está staged, y valida los bundles OKF del índice completo | tu máquina, lo activa `scripts/setup.sh` |
| `leak-guard` en PR | repite el chequeo sobre todo el repo (parcial si no recibe la denylist) y gitleaks busca credenciales en la historia | GitHub Actions |
| `leak-guard` en push | lo mismo en modo estricto: falla si falta la denylist. Detecta, no previene: el push ya es público | GitHub Actions |

El chequeo combina patrones fijos (claves privadas, CUIT, archivos marcados
confidenciales y cualquier cosa en `private/`) con una denylist privada que vive
fuera del repo y lleva los nombres y los dominios de mail de la organización del
caso. No uses nunca `git commit --no-verify`. Ninguna capa garantiza que no se
filtre nada: la defensa principal es no escribir el dato. La protección de
`main` exige que pasen `leak-check` y `gitleaks`, pero no exige aprobaciones.
Que el secreto `LEAK_DENYLIST` esté configurado en GitHub no está verificado en
este README.

`scripts/leak-check.sh` usa solo Python estándar y git:

```bash
./scripts/leak-check.sh                 # lo staged, como el hook
./scripts/leak-check.sh --all           # todos los archivos versionados
./scripts/leak-check.sh --all --strict  # falla si no hay denylist o si omite algo
```

Que `--strict` pase no certifica que no haya datos privados: solo dice que no
encontró los patrones ni los términos de la denylist en lo que pudo leer.

Sin `.leak-denylist` (ni `LEAK_DENYLIST`) la revisión sale **PARCIAL**: solo
patrones fijos. La cobertura es texto UTF-8: binarios, archivos con NUL, UTF-16
o PDF se omiten (`⚠ archivo #N: omisión`), la revisión queda **PARCIAL** y
`--strict` la rechaza. Un symlink se revisa por su contenido (la ruta que
guarda), nunca siguiendo el destino. **COMPLETA** quiere decir que corrió con
denylist y sin omisiones, no que el repo esté libre de datos privados.

Para no publicar nombres ni valores en logs, cada hallazgo dice solo categoría,
número de archivo y línea (`✗ archivo #3, línea 12: CUIT`). El
número es la posición en el listado de git (separado por NUL) del modo que
corriste. Para ver solo ese archivo en tu máquina, desde la raíz del repo y sin
pegar el listado en ningún lado (el `3` es el número del hallazgo):

```bash
sel='import os,subprocess,sys; out=subprocess.run(["git",*sys.argv[2:]],stdout=subprocess.PIPE,check=True).stdout; print(repr(os.fsdecode([p for p in out.split(b"\0") if p][int(sys.argv[1])-1])))'
python3 -c "$sel" 3 diff --cached --name-only -z --diff-filter=ACMR  # staged
python3 -c "$sel" 3 ls-files -z                                       # --all
```

Separa por NUL, así que funciona aunque el nombre tenga espacios o saltos de línea.

### Si se filtró algo

1. Avisale a Martin enseguida. No hagas más commits encima.
2. Martin borra el dato de **toda la historia** (no alcanza con un commit que lo
   saque), fuerza el push y, si hace falta, le pide a GitHub Support que purgue
   las vistas cacheadas.
3. Si era una credencial, se rota: hay que darla por comprometida.

## Generar el deck

```bash
./scripts/build-deck.sh          # todos los formatos y el PDF de borrador
./scripts/build-deck.sh entrega  # PDF de borrador (-borrador.pdf): deck + anexos
./scripts/build-deck.sh entrega --delivery  # el PDF final; exige ready y fuentes verificadas
./scripts/build-deck.sh marp     # solo Marp: html, pdf, pptx
./scripts/build-deck.sh pandoc   # solo pandoc: pptx
./scripts/build-deck.sh html     # solo el html de Marp, lo más rápido
```

Antes de renderizar, el script corre `plan-check.py --mode draft`; con
`entrega --delivery`, usa `--mode delivery` y corta antes del render si falla.
Separá slides solo con `---` o `***` en su
propia línea: se rechazan variantes con espacios (`- - -`) o `___`. Los links
locales van en Markdown (`[anexo](annexes/05-business-case.md)`); `href`/`src` locales
en HTML se rechazan. El frontmatter se lee como YAML seguro y no admite claves
duplicadas.

| Salida | Sirve para |
|---|---|
| `Grupo11-AcmeLabs-PlanMaestroCAIO.pdf` | deck, índice y anexos en un PDF; es el que se entrega y solo lo escribe `entrega --delivery`; revisá el render |
| `Grupo11-AcmeLabs-PlanMaestroCAIO-borrador.pdf` | el mismo PDF en modo borrador (`all` y `entrega` sin `--delivery`); nunca pisa el final |
| `deck-marp.html` / `.pdf` | revisar y presentar; el mejor diseño |
| `deck-marp.pptx` | entregar si piden pptx (las slides van como imagen) |
| `deck-pandoc.pptx` | pptx con texto editable, diseño básico |

### La entrega y los anexos

La consigna pide **un único PDF de menos de 10 MB** con la presentación y los
anexos. `build-deck.sh entrega --delivery` lo arma en
`out/Grupo11-AcmeLabs-PlanMaestroCAIO.pdf`, con título "Grupo 11 · Acme Labs —
Plan Maestro CAIO" en sus metadatos: el deck de Marp y después cada anexo de
`plan/annexes/` en orden de nombre (`01-diagnostico.md`,
`02-arquitectura.md`...), en A4. Entre el deck y los anexos agrega una página de
índice con títulos y links internos. Las páginas de anexos se numeran desde 1 al
pie; el índice usa esa numeración. Las filas de tablas se mantienen juntas si
caben en una página, sin achicar la tipografía. El pie requiere un Chrome con
soporte de cajas de margen CSS; verificá que aparezca en el PDF generado. Si
pasa los 10 MB, el script falla y dice el peso.

Un anexo no es un depósito de datos crudos: es la **evidencia procesada** que
deja ver al CFO o al board de dónde salió cada número de una slide. Para
arrancar uno, copiá `plan/annexes/_template.md`, que trae la estructura que
pidió el equipo docente: objetivo, supuestos de partida, evidencia, riesgos y
mitigación, y decisiones. `plan-check` exige esas secciones y el frontmatter
(`owner`, `status`, `title`); en entrega, además, que el anexo esté en `ready` y
que una slide lo enlace. Los archivos que empiezan con `_` no se validan ni se
entregan.

En el PDF de entrega, los links a slides y anexos incluidos navegan dentro del
PDF, también hacia sus anclas. Los demás archivos del repo apuntan a GitHub, con
`CAIO_PUBLIC_REF=main` por defecto. Para fijar una versión auditable, usá un
commit publicado: `CAIO_PUBLIC_REF=<sha> ./scripts/build-deck.sh entrega
--delivery`. El build rechaza links a `private/`, destinos internos inexistentes
y cualquier URI `file://` que sobreviva en el PDF final.

## Validar

Corré estos chequeos desde la raíz del repo, con el `.venv` activo. En Windows,
donde dice `python3` usá `python`.

```bash
./scripts/okf-check.sh                                    # bundles OKF de tu working tree, borrador (CI lo corre sobre el checkout)
python3 scripts/harness-check.py                         # roles, rutas y adaptadores generados
./scripts/okf-check.sh --staged                           # índice completo, borrador (como el hook)
./scripts/okf-check.sh --delivery --path material/unidades/m1u2-portfolio-100-dias.md
python3 scripts/plan-check.py --mode draft                # estructura del deck
python3 scripts/plan-check.py --mode delivery             # el deck, como para entregar
```

`okf-check` y `plan-check` necesitan PyYAML en los dos modos; en entrega,
`plan-check` además valida con `okf-check` las fichas que usa el deck.

- **Borrador** acepta fichas `draft` con faltantes identificados. Toda ficha
  nueva declara `status`; una sin `status` se lee como `draft`.
- **Aceptación documental** (`status: accepted`) declara que una persona acepta
  incorporar la ficha al corpus. Requiere `accepted: { by, at, scope }`, con
  `by: human:<usuario-github>`, fecha ISO y alcance explícito. No acredita
  cotejo primario, verificación del contenido ni vigencia normativa; conserva
  las cautelas.
- **Entrega** (`--delivery`, con `--path` para las fichas que usa la entrega;
  `--mode delivery` para el deck) exige `status: verified` con el bloque
  `verified:` de una persona y un deck sin pendientes. `--path` acepta solo
  archivos o carpetas de `context/`, `material/` y `defense/evidence/`: pasá las
  fichas que de verdad cita la entrega. El ejemplo de arriba es una ficha real
  que falla con fichas no verificadas: al 2026-10-25 no declara `status` y se
  lee como `draft`.
- Al 2026-10-25 hay 20 fichas `accepted`, 10 `draft` y 74 sin `status`; el gate
  de entrega (`plan-check.py --mode delivery`) exige que el deck cite fichas
  `verified`. Los chequeos de entrega rechazan las fichas sin revisión declarada
  y los pendientes del deck; no se resuelve cambiando etiquetas sin revisar las
  fuentes.
- Los chequeos validan estructura y que la revisión humana esté declarada. No
  prueban que una cifra sea cierta ni que el plan esté completo: eso lo revisan
  personas.

## Fechas

| Hito | Fecha |
|---|---|
| Versión para peer review | martes 27/10 |
| Entrega final | 28/10 → 4/11 |
| Votación top 3 | 5/11 → 8/11 |
| Defensa ante el board (tentativo) | martes 10/11, 18:30 |

## Estado final

El plan está completo y pasa el gate de entrega. Ya están acordados el caso Acme
Labs, el alcance de toda la organización, los ocho responsables y el formato de
entrega.

- **Decisiones de las revisiones de sección** (#11–#14 y #16–#20): las tomó
  Martín como responsable del caso el 21/10 y el Directorio las sintetiza en el
  [Anexo G](plan/annexes/07-resoluciones.md) (R-01 a R-34, con
  [#52](https://github.com/lazynet/tp-caio-g11-2026/pull/52) y
  [#62](https://github.com/lazynet/tp-caio-g11-2026/pull/62)). No equivalen a
  ratificaciones de cada responsable: si no estás de acuerdo con una, objetala
  en el PR o en su issue.
- **Material de la cursada:** 20 fichas quedaron en `accepted` por instrucción
  expresa de Martín (21/10/2026). Eso no acredita verificación humana del
  contenido; los cotejos externos de
  [#56](https://github.com/lazynet/tp-caio-g11-2026/issues/56) se resolvieron
  con R-34 y el destino de la capacidad
  ([#60](https://github.com/lazynet/tp-caio-g11-2026/issues/60)), con R-33.
- **Defensa** ([#21](https://github.com/lazynet/tp-caio-g11-2026/issues/21)):
  sigue abierta, pero no condiciona la entrega. Falta acordar quién presenta
  cada slide (hay una propuesta en `defense/storyline.md`) y hacer el ensayo
  antes de la defensa (ver Fechas).
- **Propuesta de Lucho**
  ([#27](https://github.com/lazynet/tp-caio-g11-2026/issues/27)): no se
  incorporó a la entrega; `defense/structure-pilot.md` es su piloto y queda como
  referencia.

## Backlog y seguimiento

**GitHub Issues es el backlog del equipo.** Este README enlaza las tareas;
el estado y las decisiones se actualizan en cada issue, sin duplicar una lista
de pendientes en otro archivo.

- [Todas las tareas abiertas](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aopen+-label%3Aacceso).
- [Mis tareas](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aopen+assignee%3A%40me+-label%3Aacceso).
- [Tareas cerradas](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aclosed+-label%3Aacceso).
- [Cargar un issue con los formularios del equipo](https://github.com/lazynet/tp-caio-g11-2026/issues/new/choose).

Las ocho tareas de revisión están en [Responsables del equipo](#responsables-del-equipo).
Los comentarios de Gabriela se discutieron en issues propios y quedaron resueltos
en el Anexo G:

| Issue | Qué se resolvió | Resolución |
|---|---|---|
| [#11](https://github.com/lazynet/tp-caio-g11-2026/issues/11) | Valor estratégico de gobierno, seguridad y medición | R-11, R-12 |
| [#12](https://github.com/lazynet/tp-caio-g11-2026/issues/12) | Exploración comercial como opción no costeada | R-30, R-31 |
| [#13](https://github.com/lazynet/tp-caio-g11-2026/issues/13) | Capacidad, formación y horas de M1-M3 | R-21, R-24, R-25, R-26 |
| [#14](https://github.com/lazynet/tp-caio-g11-2026/issues/14) | Validación inicial antes de liberar el esfuerzo completo | R-02, R-05, R-24 |

### Estados

Cada issue abierto del backlog lleva **una sola** etiqueta de estado. Al moverlo, sacá la
anterior y agregá la nueva; no se considera iniciado solo por estar asignado.
Los pedidos de acceso al equipo se siguen aparte, con la etiqueta `acceso`.

| Estado | Cuándo usarlo | Ver tareas |
|---|---|---|
| `estado:pendiente` | La tarea está registrada y todavía no empezó | [Pendientes](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aopen+label%3A%22estado%3Apendiente%22) |
| `estado:en-curso` | El responsable está trabajando y registra avances | [En curso](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aopen+label%3A%22estado%3Aen-curso%22) |
| `estado:en-revision` | Hay un resultado enlazado, pendiente de feedback | [En revisión](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aopen+label%3A%22estado%3Aen-revision%22) |
| `estado:bloqueada` | No puede avanzar: el issue explica qué falta y cómo destrabarlo | [Bloqueadas](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aopen+label%3A%22estado%3Abloqueada%22) |
| Cerrado | Cumple los criterios con evidencia y feedback, o se descartó con una decisión registrada | [Cerradas](https://github.com/lazynet/tp-caio-g11-2026/issues?q=is%3Aissue+is%3Aclosed+-label%3Aacceso) |

### Cómo seguir una tarea

1. Abrí el issue, confirmá el responsable y revisá objetivo, archivos,
   dependencias y criterios de cierre. Si no podés asignarlo, dejá el nombre en el texto.
2. Al empezar, pasalo a `estado:en-curso`. Comentá avances, dudas y decisiones;
   lo que se acuerde por WhatsApp se registra ahí con su autor y contexto.
3. Enlazá el resultado: conclusiones de revisión, evidencia o un PR. Si una tarea
   es grande, abrí issues específicos y enlazalos desde la tarea de sección.
4. Pasalo a `estado:en-revision` y pedí feedback al responsable del tema. Un PR
   mergeado puede cerrar una subtarea, pero no prueba por sí solo toda la revisión.
5. Cerrá cuando se cumplan sus criterios, con un comentario que resuma resultado,
   evidencia y feedback humano. Quitá la etiqueta de estado al cerrarlo.

Una propuesta descartada también se cierra, dejando el motivo y la decisión
humana. Si el resultado requiere cambios en varias secciones, la tarea queda
abierta hasta enlazar su integración o registrar el seguimiento pendiente.

### Cómo cargar un issue propio

No necesitás usar git ni un agente: podés hacerlo desde la web de GitHub.

1. Entrá al repo, abrí **Issues** y elegí **New issue**. Antes de crear uno,
   buscá si el tema ya está abierto: si solo agregás una duda o un avance,
   comentá en el issue existente.
2. Elegí el formulario según lo que necesitás:

   | Formulario | Para qué sirve |
   |---|---|
   | [Tarea del plan](https://github.com/lazynet/tp-caio-g11-2026/issues/new?template=task.yml) | Registrar trabajo concreto, con resultado y criterios de cierre |
   | [Propuesta de cambio](https://github.com/lazynet/tp-caio-g11-2026/issues/new?template=proposal.yml) | Discutir una observación o mejora antes de modificar el plan |
   | [Verificación de fuentes](https://github.com/lazynet/tp-caio-g11-2026/issues/new?template=verification.yml) | Cotejar una cita, cifra o supuesto, o registrar material faltante |
   | Sumarme al equipo | Pedir acceso al repo; no se usa para tareas del plan |

3. Completá el título con una acción concreta. Por ejemplo: «Revisar las horas
   del básico del anexo D». El formulario te pide responsable, contexto,
   archivos o fuentes y qué tiene que pasar para cerrar.
4. En **Assignees**, elegí quién coordina. Si cargás una tarea tuya, elegí tu
   usuario. Si no podés editar ese campo o la persona no aparece, dejá su nombre
   en el formulario y avisá en el issue para completar la asignación.
5. Enlazá la tarea de sección y los issues relacionados usando `#` y el número
   (por ejemplo, `#18` para Personas). Las propuestas no quedan aprobadas por
   abrir el issue: registrá quién debe revisarlas.
6. Revisá que el texto y los adjuntos respeten [Datos privados](#datos-privados)
   y publicá con **Submit new issue**. Los tres formularios de trabajo agregan
   `estado:pendiente`; pasalo a en curso cuando efectivamente empieces.

Para seguirlo, usá **Comment** en el mismo issue. Dejá qué avanzó, qué falta y
el link a la evidencia o al PR; si traés un acuerdo de WhatsApp, atribuíselo
a quien lo hizo y registrá la decisión, sin copiar datos privados.

Ejemplo de avance: «Revisé el básico de D y propongo separar uso seguro de
práctica por herramienta. Falta acordar la población con Pablo. La comparación
de horas está en el PR enlazado». Esto registra una propuesta, no un cambio aprobado.

Para terminar, cumplí los criterios y dejá el feedback humano y el resultado.
Usá **Close issue** y quitá la etiqueta de estado; si se descarta una propuesta,
usá **Close as not planned** con el motivo. Si no tenés permiso para cerrar o
cambiar etiquetas, pedilo en un comentario y dejá explícito el estado real.
