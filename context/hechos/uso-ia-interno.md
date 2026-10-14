---
type: Hecho
title: "Uso actual de IA en la operación interna"
description: "Acme Labs usa tres herramientas de IA generativa con licencia corporativa; la adopción es alta en Tecnología y baja en Operaciones y en las áreas de staff."
status: draft
tags: [caso, ia, adopcion]
sources:
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
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
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
| Abril de 2026 | 10-15 seats | 20-25 seats, 95% activos |
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

- La telemetría mide solo el agente de código. Las áreas de staff usan sobre todo
  el chat y Gemini, que esa telemetría no capta: su valor subestima el uso real.
- Las personas de Operaciones trabajan con las herramientas que permite cada
  cliente; su baja adopción no es solo cultural.
- Hay diferencias entre fuentes sobre la cantidad de seats; se publican rangos.

[^interno-adopcion-ia-2026]: Reportes de adopción de IA y licencias, abril a octubre de 2026 (privado, anonimizado)
[^interno-telemetria-ia-2026]: Telemetría de uso de agentes de código por área, septiembre y octubre de 2026 (privado, anonimizado)
[^interno-politica-ia-2026]: Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)
[^interno-okr-2026]: OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)
