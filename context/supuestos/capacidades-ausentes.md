---
type: Supuesto
title: "Capacidades que el plan da por ausentes"
description: "El plan supone brechas de gateway, inventario de arquitectura y capacidad legal dedicada a IA, sujetas a relevamiento y cobertura según la alternativa elegida y las capacidades existentes."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Hipótesis de planificación confirmadas por Martín: gateway de modelos e inventario formal de arquitectura supuestos ausentes y capacidad legal interna dedicada a IA supuesta insuficiente. Se conserva pendiente el relevamiento técnico y legal; se distinguen el inventario de datos informado y el harness interno cuyo alcance está por relevar. Construcción y contratación dependen de la alternativa elegida y de la brecha confirmada; encontrar capacidades equivalentes obliga a revisar alcance y costos. Confirmado en esta conversación."
tags: [supuesto, arquitectura, gobierno]
sources:
  - id: stack-plataforma
    resource: "context/hechos/stack-y-plataforma.md"
    title: "Herramientas y plataforma documentadas, con límites de inventario"
  - id: tamano-estructura
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Estructura y roles documentados de la organización"
  - id: gobierno-ia
    resource: "context/hechos/gobierno-y-politica-ia.md"
    title: "Antecedentes y brechas de gobierno pendientes de contraste"
  - id: uso-ia
    resource: "context/hechos/uso-ia-interno.md"
    title: "Harness interno informado y alcance técnico por relevar"
  - id: inventario-datos
    resource: "context/hechos/inventario-y-distribucion-de-datos.md"
    title: "Existencia informada del inventario de datos, distinto del de arquitectura"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

| Capacidad | Supuesto | Consecuencia en el plan |
|---|---|---|
| Gateway de modelos | Se supone ausente | Evaluar capacidades reutilizables y construirlo solo si la alternativa elegida lo requiere y la brecha se confirma |
| Inventario formal de arquitectura | Se supone ausente | Relevar y completar el inventario técnico según la brecha confirmada |
| Función legal dedicada a IA | Se supone sin capacidad interna dedicada suficiente | Evaluar asesoría externa según la brecha confirmada y el alcance seleccionado |

# Por qué es razonable

- La ficha de [stack](/hechos/stack-y-plataforma.md) describe herramientas y
  plataforma sin documentar un gateway ni un inventario formal de arquitectura.[^stack-plataforma]
- La ficha de [tamaño y estructura](/hechos/tamano-y-estructura.md) no muestra
  una función legal en la primera línea, y la
  [política de IA](/hechos/gobierno-y-politica-ia.md) deja pendientes que
  requieren revisión legal. Esos documentos motivan el relevamiento de
  capacidad disponible.[^tamano-estructura][^gobierno-ia]

# Cómo verificarlo

Relevar componentes, inventarios y asesoría disponibles, y contrastar su alcance
y capacidad con la alternativa seleccionada. El
[harness interno](/hechos/uso-ia-interno.md) tiene alcance técnico por relevar y
puede ofrecer capacidades reutilizables.[^uso-ia]

# Qué lo invalidaría

- Cualquier inventario, componente o asesoría vigente que lo contradiga: el
  plan reduciría ese costo.

# Cautelas

- Es un supuesto por ausencia de evidencia, no la prueba de que no existan.
- El [inventario de datos](/hechos/inventario-y-distribucion-de-datos.md) tiene
  existencia informada por el responsable del caso; se distingue del inventario
  de arquitectura.[^inventario-datos]
- La ausencia en una lista de herramientas o en la primera línea del
  organigrama no demuestra inexistencia de capacidades equivalentes.

[^stack-plataforma]: Stack y plataforma de delivery, herramientas documentadas y cautela sobre inventario de arquitectura.
[^tamano-estructura]: Tamaño y estructura de la organización, roles documentados y límites del dimensionamiento.
[^gobierno-ia]: Gobierno y política de IA existentes, antecedentes y estado actual por contrastar.
[^uso-ia]: Uso actual de IA en la operación interna, harness informado sin revisión documental ni técnica de su alcance.
[^inventario-datos]: Inventario y distribución de datos, existencia informada y distinción respecto del inventario de arquitectura.
