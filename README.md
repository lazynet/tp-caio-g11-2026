# Plan Maestro CAIO — Flexibility · Grupo 11

**Equipo:** Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro ·
Rafael Cioffi · Nicolas Tanos

Repo del Trabajo Integrador Final de la Diplomatura CAIO (UTN BA): un Plan
Maestro del CAIO a 12 meses para Flexibility, presentado en 10 slides más anexos.

Acá no se escriben slides a mano. Se escribe markdown y el deck se **genera**.
Los agentes de IA del repo ayudan a producir cada sección y a atacarla antes de
que la vea otro equipo.

## Qué necesitás

| Herramienta | Para qué | Cómo |
|---|---|---|
| git + acceso al repo | bajar y subir cambios | _(remote a definir — ver Pendientes)_ |
| Un agente de IA | trabajar con los agentes por rol | cualquiera de los tres: [Claude Code](https://claude.com/claude-code), [Codex](https://developers.openai.com/codex) o VS Code con GitHub Copilot |
| Node.js | generar el deck con Marp | `brew install node` |
| pandoc | generar el pptx editable | `brew install pandoc` |
| Un editor de markdown | leer y editar | cualquiera (VS Code, Obsidian, etc.) |

No necesitás saber programar: todo es markdown, y el agente corre los comandos
por vos si se lo pedís.

## Primeros 15 minutos

1. Cloná el repo y entrá a la carpeta.
2. Abrí tu agente ahí: `claude`, `codex`, o la carpeta en VS Code con el chat de Copilot.
3. Pedile: *"leé AGENTS.md y material/README.md y contame en qué estado está el plan"*.
4. Generá el deck: `./scripts/build-deck.sh` (o pedíselo al agente) y abrí
   `out/deck-marp.html` en el navegador.

## Cómo está organizado

| Carpeta | Qué hay | Quién escribe |
|---|---|---|
| `plan/slides.md` | las 10 slides, fuente única del deck | `caio` integra |
| `plan/annexes/` | un anexo por tema: el detalle que sostiene cada slide | el agente dueño del tema |
| `context/` | datos de Flexibility, con su fuente | Martin (tiene el acceso) |
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
3. **Nada confidencial de Flexibility en `plan/`.** El plan lo leen los
   compañeros, el equipo de peer review y los docentes. Nombres de clientes,
   tarifas y P&L van en rangos o anonimizados.
4. **Board antes de compartir.** Corré el skill `board-review` sobre lo tuyo
   antes de pedir review humano.
5. **Las slides no se tocan en el pptx.** Si algo está mal en el deck, se corrige
   en `plan/slides.md` y se regenera.

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

- [ ] Dónde colaboramos (remote del repo, carpeta compartida)
- [ ] Formato del deck final (ver "Generar el deck")
- [ ] Alcance dentro de Flexibility: organización completa, un área o un equipo
- [ ] Material de M3U4 (cierre y defensa del Plan Maestro), que no tenemos
