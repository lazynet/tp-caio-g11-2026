# Plan Maestro CAIO — Flexibility · Grupo 11

**Equipo:** Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro ·
Rafael Cioffi · Nicolas Tanos

Repo del Trabajo Integrador Final de la Diplomatura CAIO (UTN BA): un Plan
Maestro del CAIO a 12 meses para Flexibility, presentado en 10 slides más anexos.

> **El repo es público.** Ningún dato interno de Flexibility entra acá: ver
> [Datos privados](#datos-privados) antes de escribir nada.

Acá no se escriben slides a mano. Se escribe markdown y el deck se **genera**.
Los agentes de IA del repo ayudan a producir cada sección y a atacarla antes de
que la vea otro equipo.

## Qué necesitás

| Herramienta | Para qué | Cómo |
|---|---|---|
| Cuenta de GitHub | escribir en el repo | [github.com/signup](https://github.com/signup) |
| git y [GitHub CLI](https://cli.github.com) | bajar y subir cambios | `brew install git gh` y después `gh auth login` |
| Un agente de IA | trabajar con los agentes por rol | cualquiera de los tres: [Claude Code](https://claude.com/claude-code), [Codex](https://developers.openai.com/codex) o VS Code con GitHub Copilot |
| Node.js | generar el deck con Marp | `brew install node` |
| pandoc | generar el pptx editable | `brew install pandoc` |
| Un editor de markdown | leer y editar | cualquiera (VS Code, Obsidian, etc.) |

No necesitás saber programar: todo es markdown, y el agente corre los comandos
por vos si se lo pedís.

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
   gh repo clone lazynet/tp-caio-g11-2026
   cd tp-caio-g11-2026
   ./scripts/setup.sh
   ```

2. Abrí tu agente ahí: `claude`, `codex`, o la carpeta en VS Code con el chat de Copilot.
3. Pedile: *"leé AGENTS.md y material/README.md y contame en qué estado está el plan"*.
4. Generá el deck: `./scripts/build-deck.sh` (o pedíselo al agente) y abrí
   `out/deck-marp.html` en el navegador.

## Cómo está organizado

| Carpeta | Qué hay | Quién escribe |
|---|---|---|
| `plan/slides.md` | las 10 slides, fuente única del deck | `caio` integra |
| `plan/annexes/` | un anexo por tema: el detalle que sostiene cada slide | el agente dueño del tema |
| `context/` | datos **públicos** o anonimizados de Flexibility, con su fuente | Martin (tiene el acceso) |
| `private/` | datos internos reales — **solo local, nunca se versiona** | Martin |
| `material/` | índice del material de la cursada por sección del plan | — |
| `defense/` | storyline, objeciones, evidencia | `caio` + `board` |
| `reviews/` | revisiones del board y del peer review, con fecha | `board` |
| `out/` | decks generados — **no se versiona ni se edita** | el script |

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
- *"Corré el skill board-review sobre plan/"*: las cuatro miradas en paralelo,
  después el board, y el resultado queda en `reviews/`. En Claude Code y Copilot
  también podés escribir `/board-review plan/`.

Todos leen las mismas definiciones, pero cada herramienta las carga distinto:

| Herramienta | Instrucciones (`AGENTS.md`) | Agentes por rol | Skill `board-review` |
|---|---|---|---|
| Claude Code | automático | automático (`.claude/agents/`) | automático |
| VS Code + Copilot | automático (lo fija `.vscode/settings.json`) | automático (`.claude/agents/`) | automático |
| Codex | automático | **no**: pedile *"lanzá un subagente con las instrucciones de .claude/agents/finance.md"* | automático (`.agents/skills/`) |

Las definiciones viven una sola vez en `.claude/agents/` y `.agents/skills/`.
No las copies a otras carpetas para "tu" herramienta: se desincronizan.

## Cómo trabajamos

1. **Una sección, un dueño.** Antes de arrancar un anexo, avisá en el grupo cuál
   tomás. Cada anexo declara `owner:` arriba.
2. **Todo número tiene fuente.** Si es un supuesto, se marca como supuesto.
3. **Nada interno de Flexibility en el repo.** Ver [Datos privados](#datos-privados).
4. **Board antes de compartir.** Corré el skill `board-review` sobre lo tuyo
   antes de pedir review humano.
5. **Las slides no se tocan en el pptx.** Si algo está mal en el deck, se corrige
   en `plan/slides.md` y se regenera.
6. **Cambios a `main` por pull request.** Trabajá en una rama, abrí un PR, y se
   mergea cuando pasa el chequeo `leak-guard`. Si no sabés cómo, pedíselo a tu
   agente: *"commiteá esto en una rama nueva y abrí un PR"*.

## Datos privados

El repo es público: cualquiera en internet lo puede leer, y lo que se pushea no
se puede despublicar. Borrarlo después o pasar el repo a privado no alcanza,
porque puede haber quedado en clones, forks o caches.

**Nunca entra al repo:** nombres de clientes o de proyectos internos de
Flexibility, nombres de personas de Flexibility, montos de contratos, tarifas,
P&L, headcount, mails o rutas corporativas, credenciales.

**Cómo se escribe en cambio:** "Cliente A (banco)", "Cliente B (fintech)";
cifras en rangos, ratios o índice base 100; personas por rol ("el CFO").

**Dónde va el dato real:** en `private/`, que no se versiona. Solo Martin tiene
esos datos.

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
- [ ] Formato del deck final (ver "Generar el deck")
- [ ] Alcance dentro de Flexibility: organización completa, un área o un equipo
- [ ] Material de M3U4 (cierre y defensa del Plan Maestro), que no tenemos
