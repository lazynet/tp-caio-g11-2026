# AGENTS.md — tp-caio-g11-2026

`AGENTS.md` es el contrato portable para los agentes de IA y la fuente única de
las reglas del repo. No agregues un `CLAUDE.md` ni copias de estas reglas para
otra herramienta: dos contratos se desincronizan.

## Idioma

**Todo en español rioplatense**: la conversación con el equipo, los documentos,
las definiciones de agentes y skills, los comentarios en scripts y los mensajes
de commit. Registro ejecutivo en los entregables y voseo en todo el repo.
Solo quedan en inglés los nombres de archivos y carpetas, las claves de
frontmatter y los identificadores de código, porque las herramientas los esperan así.

## Qué es este repo

El Trabajo Integrador Final de la *Diplomatura Chief AI Officer (CAIO)* de UTN BA:
un **Plan Maestro del CAIO a 12 meses** para una organización, defendido ante un board.

**Estado (setup):**

- **Acordado:** la diplomatura, el plan a 12 meses y el tope de diez slides,
  incluyendo portada y equipo.
- **Pendiente:** el caso, su alcance, los responsables humanos de cada sección y
  el formato final del deck. Flexibility (empresa argentina de software para
  fintech y bancos) es un **candidato**, no el caso elegido: no apliques sus
  restricciones a todo caso ni redactes el plan antes de que el equipo elija.

El plan tiene que integrar:

- Estrategia integral: arquitectura, gobierno, seguridad, people plan y finanzas.
- Roadmap técnico, financiero y cultural, con hitos y criterios de éxito.
- Financial storytelling para un CFO escéptico.
- Roadmap ajustado por riesgo: escenarios, contingencias, decisiones reversibles e irreversibles.
- Preparación de la defensa: storyline, objeciones anticipadas, evidencia.

**Regla de formato:** máximo 10 slides, incluyendo portada y equipo. Lo que el
board tiene que *decidir* va en las slides; lo que lo *sustenta*, en los anexos.

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
| `context/` | Bundle OKF: hechos públicos o anonimizados y supuestos sobre el caso, cada uno con su fuente |
| `material/` | Bundle OKF: unidades y frameworks de la cursada, y qué sección del plan respalda cada uno |
| `plan/slides.md` | Las 10 slides, fuente única del deck |
| `plan/annexes/` | Un archivo por anexo, referenciado desde las slides |
| `defense/` | Storyline, banco de objeciones; `defense/evidence/` es un bundle OKF |
| `reviews/` | Revisiones del board y del peer review, con fecha |
| `scripts/build-deck.sh` | Genera el deck: `all` (default), `marp` o `pandoc` |
| `.claude/agents/` | Los agentes por rol, fuente única para todas las herramientas |
| `.agents/skills/` | Skills portables; `.claude/skills` es un symlink a esta carpeta |

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
- **El dato real vive solo en `private/`**, que está en `.gitignore` y existe solo
  en la máquina de quien tiene acceso. Los agentes pueden leerlo para razonar,
  pero lo que escriben fuera de `private/` sale anonimizado.
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
  en GitHub). Nunca uses `git commit --no-verify` para saltearlo.

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
  Quien escribe va en `generated.by` (`claude-code/<modelo>`, `codex/<modelo>` o
  `human:<usuario-github>`).
- **Fuentes.** `sources` lleva un `id` por fuente, y cada afirmación la cita con
  una nota al pie cuya etiqueta es el `id`: `[^m1u2]`. Es obligatorio en `Hecho`,
  `Evidencia` y en toda afirmación atribuida a terceros. `Mapa` y `Hueco` pueden
  ir sin fuentes externas porque describen el estado del corpus.
- **Estado.** `status` es `draft` o `verified`; las fichas nuevas lo explicitan, y
  una ficha sin `status` se lee como `draft`. Las cautelas van en `# Cautelas`.
- **Verificación.** `status: verified` solo vale con un bloque
  `verified: { by: human:<usuario-github>, at: <fecha ISO>, scope: "<fuente y
  alcance revisados>" }`. Es una declaración humana: un agente nunca escribe
  `verified` ni pasa una ficha a `verified` por su cuenta.
- **Revisar no cambia el tipo.** Un `Supuesto` o una propuesta revisados siguen
  siendo supuesto o propuesta; no se convierten en `Hecho`.
- **Draft y entrega.** Un borrador admite faltantes si están identificados (en
  `# Cautelas` o en `material/huecos.md`). La versión de peer review y la entrega
  no: toda cifra de una slide o anexo entregado remonta a una ficha `verified`.
- **Índices.** La raíz de cada bundle tiene un `index.md` con `okf_version` como
  único frontmatter. Al sumar un concepto, se agrega su línea con la `description`.
- **Chequeo automático:** `scripts/okf-check.sh` corre en el pre-commit y en CI.

## Reglas

- **La audiencia es toda la cohorte**, y además cualquiera en internet: aplicá
  siempre la sección "Datos privados".
- **Todo número tiene fuente.** Una cifra en una slide se rastrea hasta un anexo,
  y el anexo dice el supuesto o la fuente. Los supuestos se marcan como tales.
- **Un editor por archivo.** `caio` es el único que edita `plan/slides.md`. Cada
  anexo declara su agente dueño en el frontmatter (`owner: finance`) y lo escribe
  ese dueño; los demás le proponen cambios. El dueño agente no es el responsable
  humano: esos se asignan cuando el equipo los acuerde, y no se inventan.
- **Desacuerdos a la vista.** Si dos miradas chocan, se deja explícito con las
  alternativas y la evidencia de cada una; nadie lo resuelve inventando consenso.
- **Revisiones proporcionales.** El borrador de una sección alcanza con una
  revisión focalizada (el agente de esa mirada o `board` sobre esa sección) y
  feedback humano. El skill `board-review` completo se corre antes del peer
  review y de la entrega.
- Commits: `tipo: descripción corta` en español, sin trailers.

## Agentes

Copilotos sintéticos por rol, definidos en `.claude/agents/`. Cada uno es dueño
de una mirada; `caio` integra y edita el deck.

| Agente | Es dueño de | Foco en slides y anexos |
|---|---|---|
| `caio` | Storyline, integración, roadmap ajustado por riesgo, `plan/slides.md` | Resumen ejecutivo, roadmap, decisiones que se piden |
| `architect` | Arquitectura objetivo, plataforma, datos, roadmap técnico | Arquitectura e hitos técnicos |
| `governance` | Gobierno de IA, derechos de decisión, seguridad, compliance | Modelo operativo, políticas, controles |
| `people` | Roles y capacidad de personas, cambio y roadmap cultural | Talento, adopción, hitos culturales |
| `finance` | Business case, presupuesto, ROI, validación de cifras económicas | Financial storytelling, escenarios |
| `board` | Revisión adversarial como board, CFO escéptico y corrector | Objeciones, brechas contra la consigna |

**Contrato común de salida.** Toda propuesta de un agente dice, en breve y
adaptado a su rol: problema, evidencia o supuesto, alternativas, recomendación,
dependencias, costo (si corresponde), riesgo, responsable humano (pendiente o
acordado), criterio de éxito y condición de abandono. Si falta información, el
agente la marca como faltante o supuesto y sigue; no la inventa.

**Soporte por herramienta.** Que las definiciones sean compartidas no prueba que
todas las herramientas las carguen igual:

- **Claude Code:** observado (2026-10-11) que inyecta `AGENTS.md` al iniciar y
  lista los seis agentes de `.claude/agents/` y el skill `board-review` como
  disponibles. Invocarlos de punta a punta está pendiente de probar.
- **GitHub Copilot (VS Code):** `.vscode/settings.json` activa
  `chat.useAgentsMdFile`; la carga de agentes y skills está pendiente de probar.
- **Codex:** observado con codex-cli 0.162.1 que no deja elegir un agente
  personalizado al lanzar un subagente. Práctica que funcionó: lanzar un
  subagente genérico con el contenido de `.claude/agents/<rol>.md` como
  instrucciones, o adoptar ese rol vos mismo.
