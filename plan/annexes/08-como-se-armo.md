---
owner: caio
status: ready
title: "Anexo H — Cómo se armó este plan"
---

# Anexo H — Cómo se armó este plan

::: {.annex-summary}
## Síntesis ejecutiva

**El plan se produjo con los mismos controles que le proponemos a Acme:**
asistentes de IA con rol acotado, fuentes trazables, revisión adversarial y
decisión humana. Todo es público en
el [repositorio público del Grupo 11](https://github.com/lazynet/tp-caio-g11-2026).

| Decisión que sustenta | Recomendación y alternativa |
|---|---|
| Confiar en un plan elaborado con asistentes de IA | Un repo versionado como fuente única, con agentes por rol y chequeos automáticos, frente a un chat general y un documento editado a mano |

| Evidencia para decidir | Implicación |
|---|---|
| Un agente por mirada: CAIO, arquitectura, gobierno, personas, finanzas y board ([agentes](https://github.com/lazynet/tp-caio-g11-2026/tree/main/.claude/agents)) | Cada sección tiene un editor y una mirada que la ataca antes del board |
| Hechos, supuestos y material de la cursada como fichas con fuente y estado ([contexto](https://github.com/lazynet/tp-caio-g11-2026/tree/main/context), [material](https://github.com/lazynet/tp-caio-g11-2026/tree/main/material)) | Toda cifra entregada remonta a una ficha que una persona declaró verificada |
| Chequeos en cada commit y en CI: datos privados, estructura de fichas y gate de entrega ([CI](https://github.com/lazynet/tp-caio-g11-2026/tree/main/.github/workflows)) | Lo que no pasa el gate no llega al PDF; ningún chequeo certifica la verdad del contenido |
| El deck y este PDF se generan desde markdown ([deck](https://github.com/lazynet/tp-caio-g11-2026/blob/main/plan/slides.md)) | Nada se edita a mano: se corrige la fuente y se regenera |

**Límite:** los agentes proponen y atacan; las personas del equipo deciden,
declaran fuentes verificadas y aprueban cada cambio a `main`.
:::

## Desarrollo y fuentes

Slide que sustenta: la portada del [deck](../slides.md), desde el enlace
"Anexo H — Cómo se armó el plan". Describe el método de producción y los
controles con que se elaboró el plan. Las reglas completas del repo están en
[AGENTS.md](https://github.com/lazynet/tp-caio-g11-2026/blob/main/AGENTS.md) y
el flujo de trabajo del equipo, en el
[README](https://github.com/lazynet/tp-caio-g11-2026/blob/main/README.md).

## Objetivo

Mostrar cómo se produjo el plan y por qué sus cifras se pueden rastrear, para
que el board evalúe el método además del resultado. El repo aplica a escala
chica lo que el plan propone para Acme: uso de IA con rol acotado, controles
probados y decisión humana ([Anexo C](03-gobierno-seguridad.md)).

## Supuestos de partida

| Supuesto | Cómo se aplica | Fuente o tipo |
|---|---|---|
| Un asistente de IA rinde más con una mirada acotada que con todo el problema | Un agente por rol, con su foco y su contrato de salida | [AGENTS.md](https://github.com/lazynet/tp-caio-g11-2026/blob/main/AGENTS.md), sección "Agentes"; supuesto del equipo |
| La IA puede inventar cifras o fuentes | Cada afirmación cita su ficha; una persona declara cuáles están verificadas | [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) |
| El repo es público y el caso usa información de una organización real | Los datos internos viven fuera del repo y se publican anonimizados | [AGENTS.md](https://github.com/lazynet/tp-caio-g11-2026/blob/main/AGENTS.md), sección "Datos privados" |
| Ocho personas y varios agentes editan en paralelo | Un editor por archivo, una rama por tarea y cambios a `main` solo por pull request | [README](https://github.com/lazynet/tp-caio-g11-2026/blob/main/README.md), "Backlog y seguimiento" |

## Evidencia

Cada componente se puede inspeccionar en el repo:

| Componente | Qué hace | Dónde verlo |
|---|---|---|
| Agentes por rol | el CAIO integra y es el único que edita el deck; arquitectura, gobierno, personas y finanzas escriben sus anexos; el board simulado revisa como board, CFO escéptico y corrector | [.claude/agents](https://github.com/lazynet/tp-caio-g11-2026/tree/main/.claude/agents) |
| Bases de conocimiento OKF | Un archivo por hecho, supuesto o concepto de la cursada, con tipo, fuentes, estado y quién lo generó | [context](https://github.com/lazynet/tp-caio-g11-2026/tree/main/context), [material](https://github.com/lazynet/tp-caio-g11-2026/tree/main/material), [defense/evidence](https://github.com/lazynet/tp-caio-g11-2026/tree/main/defense/evidence) |
| Revisión adversarial | El skill `board-review` corre las miradas de rol y consolida como board; los informes quedan fechados | [board-review](https://github.com/lazynet/tp-caio-g11-2026/tree/main/.agents/skills/board-review), [reviews](https://github.com/lazynet/tp-caio-g11-2026/tree/main/reviews) |
| Control de datos privados | `leak-check` revisa patrones fijos y una lista privada en cada commit y en CI | [leak-check.sh](https://github.com/lazynet/tp-caio-g11-2026/blob/main/scripts/leak-check.sh) |
| Control de fuentes | `okf-check` valida fichas, fuentes citadas, estados y declaraciones humanas | [okf-check.py](https://github.com/lazynet/tp-caio-g11-2026/blob/main/scripts/okf-check.py) |
| Gate de entrega | `plan-check` exige secciones, links válidos, anexos referenciados y ninguna marca abierta; el build arma el PDF solo si pasa | [plan-check.py](https://github.com/lazynet/tp-caio-g11-2026/blob/main/scripts/plan-check.py), [build-deck.sh](https://github.com/lazynet/tp-caio-g11-2026/blob/main/scripts/build-deck.sh) |
| Multi harness | Los roles se definen una vez y se usan desde Claude Code, Codex o Copilot; un chequeo regenera los adaptadores | [harness-check.py](https://github.com/lazynet/tp-caio-g11-2026/blob/main/scripts/harness-check.py) |
| Seguimiento | Cada sección tiene su issue; cada cambio entra por pull request con los chequeos en verde | [Issues](https://github.com/lazynet/tp-caio-g11-2026/issues), [pull requests](https://github.com/lazynet/tp-caio-g11-2026/pulls?q=is%3Apr) |

## Riesgos y mitigación

| Riesgo | Mitigación | Límite |
|---|---|---|
| Cifras o fuentes inventadas por un agente | Fichas con fuente; solo una persona declara `verified`; el gate rechaza cifras sin respaldo | El gate valida estructura y declaración, no la verdad de la fuente |
| Publicar datos internos en un repo público | Datos reales solo en una carpeta local fuera de git; `leak-check` en commit y en CI | Cubre texto; la revisión humana antes de escribir sigue siendo obligatoria |
| Consenso aparente entre agentes | Los desacuerdos quedan explícitos con alternativas; el board simulado ataca cada sección | Un mismo modelo de base puede compartir sesgos entre roles |
| Dependencia de quien armó el harness | Todo es markdown y scripts documentados; el README guía el onboarding sin programar | La curva inicial existe para quien no usa git |

## Decisiones

| Decisión | Alternativa descartada | Por qué | Reversible |
|---|---|---|---|
| Repo versionado como fuente única | Documento compartido editado a mano | Historial, revisión por cambio y un PDF regenerable | Sí |
| Agentes por rol | Un solo chat general | Miradas separadas y un editor por archivo evitan pisarse y hacen visibles los choques | Sí |
| Fichas OKF con estado | Notas y PDFs sueltos | Cada cifra remonta a una fuente y a una persona que la declaró | Sí |
| Repo público | Repo privado | Transparencia ante la cohorte; obliga a anonimizar con rigor | No: lo publicado puede quedar en copias aunque después se borre |
