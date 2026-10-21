---
type: Supuesto
title: "Capacidades que el plan da por ausentes"
description: "El plan supone brechas de gateway, inventario de arquitectura y capacidad legal dedicada a IA, sujetas a relevamiento y cobertura según la alternativa elegida y las capacidades existentes."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-21
  scope: "Revalidación registrada por instrucción expresa de Martín en la sesión del 21/10/2026 sobre el contenido vigente del PR #52. Brechas de gateway, inventario de arquitectura y capacidad legal como hipótesis de planificación. R-16 asigna el relevamiento técnico a Tecnología dentro de las 24-40 h de Arquitectura antes de M3 y el legal a Seguridad antes de M4; R-15 exige brecha documentada para liberar plataforma. Se mantiene como Supuesto de diseño: esta declaración no acredita mediciones, contratos, disponibilidad ni ejecución de decisiones futuras."
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
    title: "Política de IA existente y temas que requieren revisión legal"
  - id: uso-ia
    resource: "context/hechos/uso-ia-interno.md"
    title: "Harness interno informado y alcance técnico por relevar"
  - id: inventario-datos
    resource: "context/hechos/inventario-y-distribucion-de-datos.md"
    title: "Existencia informada del inventario de datos, distinto del de arquitectura"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, R-15 (condición de brecha documentada) y R-16 (relevamiento técnico y legal)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21 }
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
  [política de IA](/hechos/gobierno-y-politica-ia.md) deja temas que requieren
  revisión legal. Esos documentos motivan el relevamiento de capacidad
  disponible.[^tamano-estructura][^gobierno-ia]

# Cómo verificarlo

Relevar componentes, inventarios y asesoría disponibles, y contrastar su alcance
y capacidad con la alternativa seleccionada. El
[harness interno](/hechos/uso-ia-interno.md) entra en ese relevamiento y puede
ofrecer capacidades reutilizables.[^uso-ia]

Quién y cuándo (R-16):[^resoluciones]

| Relevamiento | Lo hace | Hito | Si no se hace |
|---|---|---|---|
| Técnico: gateway, inventario de arquitectura y alcance del harness interno | El Responsable de Tecnología, dentro de las 24-40 h de Arquitectura ya costeadas | Decisión del mes 3 | No hay brecha documentada y no se cumple la condición 1 para liberar plataforma (R-15); si no cabe en esas horas, se recostea antes de la segunda liberación |
| Legal: capacidad dedicada a IA | Lo encarga el Responsable de seguridad; una asesoría externa entra solo con cotización verificada por el CFO | Antes de la revisión de contratos ambiguos del mes 4 y de la cláusula tipo de los meses 7-9 | Los contratos ambiguos siguen en *default-deny* |

Si el relevamiento encuentra capacidad equivalente, se reduce alcance y costo.

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
[^resoluciones]: Anexo G, R-15 (la brecha documentada es condición para liberar plataforma) y R-16 (relevamiento técnico por el Responsable de Tecnología antes del mes 3; legal encargado por el Responsable de seguridad antes del mes 4).
