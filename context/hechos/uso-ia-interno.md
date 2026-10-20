---
type: Hecho
title: "Uso actual de IA en la operación interna"
description: "Acme Labs usa herramientas de IA corporativas y herramientas de harness para su SDLC de uso exclusivamente interno; su alcance e impacto siguen por contrastar."
status: draft
tags: [caso, ia, adopcion]
sources:
  - id: confirmacion-caso-2026-10-20
    resource: "Confirmación del responsable del caso, 20/10/2026 (anonimizada)"
    title: "Herramientas de harness para el SDLC de uso exclusivamente interno"
  - id: interno-adopcion-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Reportes de adopción de IA y licencias, abril a octubre de 2026 (privado, anonimizado)"
  - id: interno-telemetria-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Telemetría de uso de agentes de código por área, septiembre y octubre de 2026 (privado, anonimizado)"
  - id: interno-politica-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)"
  - id: interno-okr-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Harness para el SDLC

El responsable del caso confirmó que hay herramientas de harness para el SDLC
y que su uso es exclusivamente interno: no se entregan ni se comercializan a
clientes.[^confirmacion-caso-2026-10-20]

Esta confirmación acredita uso interno informado, no una funcionalidad de IA
de la oferta. Su alcance, cobertura y capacidades concretas siguen por relevar;
no se infiere que sean una plataforma central o un gateway de modelos.

La existencia de herramientas no demuestra impacto incremental. La línea de
base, la calidad de resultados y los costos se contrastan antes de atribuirles
valor o ahorro.

# Herramientas aprobadas

| Herramienta | Uso | Alcance |
|---|---|---|
| Claude (plan Team: chat, escritorio y Claude Code) | Asistente general y agente de código | Seats asignados por persona |
| GitHub Copilot | Asistente de código en el IDE | Desarrolladores de proyectos internos |
| Gemini en Google Workspace | Correo, documentos, planillas y reuniones | Toda la organización, incluido en la licencia de Workspace |

Cualquier otra herramienta (Cursor, Perplexity, etc.) necesita aprobación previa
del comité de tecnología.[^interno-politica-ia-2026]

# Evolución de licencias

| Momento | Claude | Copilot |
|---|---|---|
| Marzo de 2026 | Piloto aprobado por el Directorio para menos de 10 seats | Seats para desarrolladores |
| Abril de 2026 | 10-15 seats | 20-25 seats, casi todos activos |
| Octubre de 2026 | 40-45 seats, cerca de dos tercios activos en la semana | 20-25 seats, cerca de 80% activos |

En abril, alrededor del 60% de la organización tenía uso detectado de Gemini
dentro de Workspace, sin campaña de adopción.[^interno-adopcion-ia-2026]

# Adopción del agente de código por área (septiembre de 2026)

| Área | Personas con actividad / total |
|---|---|
| Toda la organización | ~1 de cada 3 |
| Tecnología | ~7 de cada 10 |
| Operaciones (staffing) | ~1 de cada 10 |
| Áreas de staff y dirección | baja (ver cautelas) |

Cerca del 90% de los eventos sale de la terminal (Claude Code), no del chat ni
del escritorio.[^interno-telemetria-ia-2026]

# Meta

El borrador de OKR de Tecnología 2027 propone que al menos 80% de las personas
de Operaciones y Tecnología use IA de forma activa cada semana, medido por uso y
no por seats asignados.[^interno-okr-2026]

# Cautelas

- El harness del SDLC se registra por confirmación del responsable, sin revisión
  documental ni técnica de su alcance o resultados en esta sesión.
- Su uso exclusivamente interno no demuestra ni descarta otros posibles casos
  de IA en producto; esos casos requieren evidencia propia.
- La telemetría mide solo el agente de código. Las áreas de staff usan sobre todo
  el chat y Gemini, que esa telemetría no capta: su valor subestima el uso real.
- Las personas de Operaciones trabajan con las herramientas que permite cada
  cliente; su baja adopción no es solo cultural.
- Hay diferencias entre fuentes sobre la cantidad de seats; se publican rangos.

[^interno-adopcion-ia-2026]: Reportes de adopción de IA y licencias, abril a octubre de 2026 (privado, anonimizado)
[^confirmacion-caso-2026-10-20]: Confirmación del responsable del caso, 20/10/2026: existen herramientas de harness para el SDLC, solo de uso interno.
[^interno-telemetria-ia-2026]: Telemetría de uso de agentes de código por área, septiembre y octubre de 2026 (privado, anonimizado)
[^interno-politica-ia-2026]: Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)
[^interno-okr-2026]: OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)
