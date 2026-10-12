# Plan Maestro CAIO · Grupo 11

**Equipo:** Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro ·
Rafael Cioffi · Nicolas Tanos

Repo del Trabajo Integrador Final de la Diplomatura CAIO (UTN BA): un Plan
Maestro del CAIO a 12 meses, presentado en 10 slides como máximo (incluyendo
portada y equipo) más anexos.

**Estado:** estamos en setup. El caso todavía no está elegido; Flexibility
(software para fintech y bancos) es un candidato. Ver
[Pendientes del equipo](#pendientes-del-equipo).

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
| Node.js 18 o más nuevo | generar el deck con Marp |
| Chrome, Edge o Chromium | Marp lo usa para exportar pdf y pptx |
| pandoc | generar el pptx editable |
| Un editor de markdown (VS Code, Obsidian, etc.) | leer y editar |

No necesitás saber programar: todo es markdown, y el agente corre los comandos
por vos si se lo pedís.

### Instalación según tu sistema

**macOS** (con [Homebrew](https://brew.sh)):

```bash
brew install git gh node pandoc
gh auth login
```

**Windows** (PowerShell; `winget` viene con Windows 10 y 11):

```powershell
winget install Git.Git GitHub.cli OpenJS.NodeJS.LTS JohnMacFarlane.Pandoc
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
sudo apt install git gh nodejs npm pandoc chromium
gh auth login
```

Si tu distro trae un Node más viejo que 18 (`node --version`), instalalo desde
[nodejs.org](https://nodejs.org). Si `gh` no está en tus repos, seguí
[las instrucciones oficiales](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).
En Fedora: `sudo dnf install git gh nodejs pandoc chromium`.

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

2. Abrí tu agente ahí: `claude`, `codex`, o la carpeta en VS Code con el chat de Copilot.
3. Pedile: *"leé AGENTS.md y material/index.md y contame en qué estado está el plan"*.
4. Generá el deck: `./scripts/build-deck.sh` (o pedíselo al agente) y abrí
   `out/deck-marp.html` en el navegador.

## Cómo está organizado

| Carpeta | Qué hay | Agente dueño |
|---|---|---|
| `plan/slides.md` | las 10 slides, fuente única del deck | `caio`, único editor; los demás le proponen |
| `plan/annexes/` | un anexo por tema: el detalle que sostiene cada slide | el agente dueño del tema (`owner:`) |
| `context/` | hechos **públicos** o anonimizados del caso y supuestos, uno por archivo, con su fuente; vacío hasta que elijamos caso | — |
| `private/` | datos internos reales — **solo local, nunca se versiona** | quien tenga el acceso |
| `material/` | una ficha por unidad y por framework de la cursada, y qué sección del plan respalda cada uno | — |
| `defense/` | storyline, objeciones, evidencia | `caio`; `board` aporta desde `reviews/` |
| `defense/evidence/` | una ficha por evidencia: qué objeción responde y de dónde sale | `caio` |
| `reviews/` | revisiones del board y del peer review, con fecha | `board` |
| `out/` | decks generados — **no se versiona ni se edita** | el script |

El agente dueño no es el responsable humano: quién del grupo se hace cargo de
cada sección se decide cuando elijamos caso.

`context/`, `material/` y `defense/evidence/` siguen el formato abierto
[OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md):
un archivo markdown por concepto, con su fuente arriba y links entre fichas. Para
ver qué hay, abrí el `index.md` de cada carpeta. Las reglas están en `AGENTS.md`,
"Bases de conocimiento (OKF)"; si escribís con un agente, ya las conoce.

## Los agentes

Cada agente es un copiloto con una mirada. Se invocan por nombre:

| Agente | Le pedís… |
|---|---|
| `caio` | la historia, qué entra en las 10 slides, el roadmap con escenarios |
| `architect` | arquitectura objetivo, build vs buy, roadmap técnico |
| `governance` | gobierno, políticas, seguridad, EU AI Act |
| `people` | estructura, talento, AI literacy, cambio cultural |
| `finance` | inversión, ROI, escenarios, el relato para el CFO |
| `board` | que te destroce una sección antes que lo haga el board real |

Ejemplos:

- *"Con el agente finance, armá el borrador de plan/annexes/finance.md"*
- *"Usá architect para proponer 2 alternativas de arquitectura con tradeoffs"*
- *"Con el agente board, revisá solo plan/annexes/finance.md"*: revisión
  focalizada de un borrador.
- *"Corré el skill board-review sobre plan/"*: las cuatro miradas en paralelo,
  después el board, y el resultado queda en `reviews/`. Es la revisión integral,
  para antes del peer review y de la entrega.

Cada agente devuelve lo mismo, adaptado a su rol: problema, evidencia o
supuesto, alternativas, recomendación, dependencias, costo, riesgo, responsable
humano, criterio de éxito y condición de abandono (ver `AGENTS.md`).

Las definiciones son compartidas, pero eso no prueba que cada herramienta las
cargue igual. Esto es lo que sabemos hoy:

| Herramienta | Instrucciones (`AGENTS.md`) | Agentes por rol | Skill `board-review` |
|---|---|---|---|
| Claude Code | observado | listados como disponibles; invocación a probar | listado como disponible; invocación a probar |
| VS Code + Copilot | configurado en `.vscode/settings.json`; a probar | a probar | a probar |
| Codex | documentado por OpenAI; a probar acá | **no** deja elegirlos (observado con codex-cli 0.162.1): pedile *"lanzá un subagente con las instrucciones de .claude/agents/finance.md"* | a probar |

Si probás una celda "a probar", contalo en el grupo y actualizá la tabla.
Las definiciones viven una sola vez en `.claude/agents/` y `.agents/skills/`.
No las copies a otras carpetas para "tu" herramienta: se desincronizan.

## Cómo trabajamos

1. **Una sección, un dueño.** Antes de arrancar un anexo, avisá en el grupo cuál
   tomás. Cada anexo declara su agente dueño (`owner:`) arriba; las slides las
   edita solo `caio`, y los demás le proponen cambios.
2. **Todo número tiene fuente.** Si es un supuesto, se marca como supuesto. Una
   cifra entra a la entrega solo si una persona la verificó contra la fuente.
3. **Nada interno de ninguna organización en el repo.** Ver [Datos privados](#datos-privados).
4. **Revisión a la medida.** Para compartir el borrador de una sección alcanza
   con una revisión focalizada y feedback humano; el `board-review` completo va
   antes del peer review y de la entrega.
5. **Desacuerdos a la vista.** Si dos miradas chocan, se dejan las alternativas
   con su evidencia; no se inventa consenso.
6. **Las slides no se tocan en el pptx.** Si algo está mal en el deck, se corrige
   en `plan/slides.md` y se regenera.
7. **Cambios a `main` por pull request.** Trabajá en una rama, abrí un PR, y se
   mergea cuando pasa el chequeo `leak-guard`. Si no sabés cómo, pedíselo a tu
   agente: *"commiteá esto en una rama nueva y abrí un PR"*.

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
| Hook pre-commit | frena el commit si encuentra un dato prohibido | tu máquina, lo activa `scripts/setup.sh` |
| `leak-guard` | repite el chequeo y busca credenciales en toda la historia | GitHub Actions, en cada push y PR |
| Push protection | rechaza pushes con tokens o claves conocidas | GitHub |

El chequeo combina patrones fijos (mails corporativos, claves, CUIT, archivos
marcados confidenciales, cualquier cosa en `private/`) con una denylist privada
de nombres que vive fuera del repo. No uses nunca `git commit --no-verify`.

### Si se filtró algo

1. Avisale a Martin enseguida. No hagas más commits encima.
2. Martin borra el dato de **toda la historia** (no alcanza con un commit que lo
   saque), fuerza el push y, si hace falta, le pide a GitHub Support que purgue
   las vistas cacheadas.
3. Si era una credencial, se rota: hay que darla por comprometida.

## Generar el deck

```bash
./scripts/build-deck.sh          # todos los formatos
./scripts/build-deck.sh marp     # solo Marp: html, pdf, pptx
./scripts/build-deck.sh pandoc   # solo pandoc: pptx
```

| Salida | Sirve para |
|---|---|
| `deck-marp.html` / `.pdf` | revisar y presentar; el mejor diseño |
| `deck-marp.pptx` | entregar si piden pptx (las slides van como imagen) |
| `deck-pandoc.pptx` | pptx con texto editable, diseño básico |

Estamos probando alternativas: si alguien quiere sumar otro renderer, se agrega
al script, no se arma a mano.

## Fechas

| Hito | Fecha |
|---|---|
| Versión para peer review | martes 27/10 |
| Entrega final | 28/10 → 4/11 |
| Votación top 3 | 5/11 → 8/11 |
| Defensa ante el board (tentativo) | martes 10/11, 18:30 |

## Pendientes del equipo

- [x] Dónde colaboramos: GitHub, `lazynet/tp-caio-g11-2026` (público hasta que estemos todos)
- [x] Diplomatura, plan a 12 meses y tope de 10 slides incluyendo portada y equipo
- [ ] Caso: Flexibility es candidato, no está elegido
- [ ] Alcance del caso, una vez elegido
- [ ] Responsables humanos de cada sección
- [ ] Formato del deck final (ver "Generar el deck")
- [ ] Material de M3U4 (cierre y defensa del Plan Maestro), que no tenemos
