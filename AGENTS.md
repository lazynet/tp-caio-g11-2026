# AGENTS.md — tp-caio-2026

`AGENTS.md` es el contrato portable para los agentes de IA: Claude Code, Codex y
GitHub Copilot lo leen de forma nativa. Las reglas del repo van acá; no agregues
un `CLAUDE.md`, porque Claude Code deja de leer este archivo si existe uno.

## Idioma

**Todo en español rioplatense**: la conversación con el equipo, los documentos,
las definiciones de agentes y skills, los comentarios en scripts y los mensajes
de commit. Registro ejecutivo en los entregables y voseo en todo el repo.
Solo quedan en inglés los nombres de archivos y carpetas, las claves de
frontmatter y los identificadores de código, porque las herramientas los esperan así.

## Qué es este repo

El Trabajo Integrador Final de la *Diplomatura Chief AI Officer (CAIO)* de UTN BA:
un **Plan Maestro del CAIO a 12 meses** para **Flexibility** (flexibility SRL,
empresa argentina que desarrolla software para fintech y bancos), defendido ante
un board.

El plan tiene que integrar:

- Estrategia integral: arquitectura, gobierno, seguridad, people plan y finanzas.
- Roadmap técnico, financiero y cultural, con hitos y criterios de éxito.
- Financial storytelling para un CFO escéptico.
- Roadmap ajustado por riesgo: escenarios, contingencias, decisiones reversibles e irreversibles.
- Preparación de la defensa: storyline, objeciones anticipadas, evidencia.

**Regla de formato:** máximo 10 slides. Lo que el board tiene que *decidir* va en
las slides; lo que lo *sustenta*, en los anexos.

**Equipo:** Grupo 11, 6 integrantes (ver `README.md`). El onboarding del equipo
está en `README.md`: mantenelo al día cuando cambie la forma de trabajo.

**Todo se genera.** `plan/slides.md` (markdown compatible con Marp, una slide por
`---`) es la única fuente del deck. `scripts/build-deck.sh` lo renderiza en
`out/` (fuera de git) con Marp y pandoc para comparar formatos. Un deck generado
no se edita nunca: se corrige el markdown y se regenera.

## Fechas

| Hito | Fecha |
|---|---|
| Equipo y alcance | 2026-10-13 (sugerido) |
| Versión para peer review | 2026-10-27 |
| Entrega final | 2026-10-28 → 2026-11-04 |
| Votación top 3 | 2026-11-05 → 2026-11-08 |
| Defensa ante el board (tentativo) | 2026-11-10 18:30 |

## Estructura

| Path | Qué tiene |
|---|---|
| `context/` | Datos de Flexibility en los que se apoya el plan, cada uno con su fuente |
| `material/` | Índice del material de la cursada: qué unidad o framework respalda cada sección |
| `plan/slides.md` | Las 10 slides, fuente única del deck |
| `plan/annexes/` | Un archivo por anexo, referenciado desde las slides |
| `defense/` | Storyline, banco de objeciones, mapa de evidencia |
| `reviews/` | Revisiones del board y del peer review, con fecha |
| `scripts/build-deck.sh` | Genera el deck: `all` (default), `marp` o `pandoc` |
| `.claude/agents/` | Los agentes por rol, fuente única para todas las herramientas |
| `.agents/skills/` | Skills portables; `.claude/skills` es un symlink a esta carpeta |

## Fuentes

- Material de la cursada (PDFs, frameworks): Google Drive de Martin,
  `~/Library/CloudStorage/GoogleDrive-martin@example.invalid/Mi unidad/Personales/Diplomatura Chief AI Officer (CAIO)/`.
  Se lee desde ahí y los PDFs no se copian al repo. Si no tenés acceso, usá
  `material/README.md`.
- Notebook consolidado: https://notebook.google.com/notebook/57ec4d6d-41a0-4030-9273-9bfc94cfb4ae
  (los agentes no pueden leerlo; los extractos se pegan en `material/`).

## Reglas

- **La audiencia es toda la cohorte.** Compañeros, el equipo de peer review y los
  docentes leen todo lo que está en `plan/`, `defense/` y `reviews/`. Los datos
  internos de Flexibility (nombres de clientes, montos de contratos, tarifas,
  P&L, headcount por persona) nunca van ahí tal cual: se usan rangos, ratios o
  clientes anonimizados. La fuente real queda solo en `context/`, con
  `confidential: true` en el frontmatter.
- **Todo número tiene fuente.** Una cifra en una slide se rastrea hasta un anexo,
  y el anexo dice el supuesto o la fuente. Los supuestos se marcan como tales.
- **Un dueño por sección.** Cada slide o anexo declara su agente dueño en el
  frontmatter (`owner: finance`). Los demás proponen; el dueño escribe.
- **Board antes del peer review.** Corré el skill `board-review` sobre cualquier
  set de slides antes de que lo vea el equipo o el equipo revisor.
- Commits: `tipo: descripción corta` en español, sin trailers.

## Agentes

Copilotos sintéticos por rol, definidos en `.claude/agents/`. Cada uno es dueño
de una mirada, no de un árbol de archivos; `caio` integra.

| Agente | Es dueño de | Foco en slides y anexos |
|---|---|---|
| `caio` | Storyline, integración, roadmap ajustado por riesgo | Resumen ejecutivo, roadmap, decisiones que se piden |
| `architect` | Arquitectura objetivo, plataforma, datos, roadmap técnico | Arquitectura e hitos técnicos |
| `governance` | Gobierno de IA, seguridad, compliance, IA responsable | Modelo operativo, políticas, controles |
| `people` | People plan, diseño organizacional, cambio y roadmap cultural | Talento, adopción, hitos culturales |
| `finance` | Business case, presupuesto, ROI, relato para el CFO | Financial storytelling, escenarios |
| `board` | Revisión adversarial como board, CFO escéptico y corrector | Objeciones, brechas contra la consigna |

Cómo se usan en cada herramienta:

- **Claude Code** y **GitHub Copilot (VS Code)** cargan `.claude/agents/` solos.
- **Codex** no permite elegir un agente personalizado al lanzar un subagente
  (probado con codex-cli 0.162.1). Para usar un rol, lanzá un subagente con el
  contenido de `.claude/agents/<rol>.md` como instrucciones, o adoptá ese rol vos mismo.
