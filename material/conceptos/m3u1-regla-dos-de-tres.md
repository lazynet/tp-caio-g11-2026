---
type: Concepto
title: "Regla de dos de tres para agentes"
description: "Regla de diseño de la Clase 9: sin supervisión humana, un agente puede leer contenido no confiable, acceder a datos sensibles o actuar hacia afuera, pero como máximo dos de las tres."
tags: [m3, seguridad, agentes, gobierno]
sources:
  - id: clase9
    resource: "Hoy atacamos · CAIO Clase 9.pdf"
    title: "Hoy atacamos, CAIO Clase 9, láminas 04, 12 y 14"
status: draft
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T14:30:00Z }
---

# Regla

"Los filtros no alcanzan." Un agente puede tener tres capacidades de riesgo:[^clase9]

| Letra | Capacidad |
|---|---|
| A | Lee contenido no confiable |
| B | Accede a datos sensibles |
| C | Actúa hacia afuera |

"Sin supervisión humana, un agente puede tener como máximo dos." A + B + C = "acá
no" (lámina 04).[^clase9]

La lámina la atribuye a dos fuentes: "Trifecta letal", de Simon Willison (2025), y
"Agents Rule of Two", de Meta (2025).[^clase9]

# Aplicación

- **Caso FinBot (lámina 12):** A sí, B sí, C sí. "Sin humano en el medio: acá no."
  Ver [FinBot](/casos/m3u1-finbot.md).[^clase9]
- **Scorecard (lámina 14):** "Regla de dos de tres" es uno de los diez controles, y
  "Agentes con A+B+C sin humano" es uno de los tres indicadores, con meta 0. Ver
  [scorecard](/conceptos/m3u1-scorecard-seguridad-directorio.md).[^clase9]

# Relación con otras fichas

Complementa los [criterios de gobierno agéntico de M1U4](/conceptos/m1u4-criterios-gobierno-agentico.md)
(autonomía, acceso, consecuencia y reversibilidad) y la
[escala de autonomía L0-L4](/conceptos/m1u4-escala-autonomia-l0-l4.md): esta regla
fija un límite combinado en vez de graduar cada variable. Lectura de esta ficha, no
del curso.

# Cautelas

* Ficha nueva, en borrador, sin verificación humana. Cotejo del agente contra las
  láminas 04, 12 y 14 (las dos primeras leídas como imagen) el 2026-10-21.
* Las atribuciones a Simon Willison y a Meta son del curso; no se cotejaron las
  publicaciones originales.
* La lámina no define qué cuenta como "supervisión humana" ni como "actuar hacia
  afuera". Si el plan usa la regla, tiene que definirlos.

[^clase9]: Hoy atacamos, CAIO Clase 9, láminas 04, 12 y 14
