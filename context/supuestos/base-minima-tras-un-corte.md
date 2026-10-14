---
type: Supuesto
title: "Base mínima que queda después de un corte"
description: "Si el plan se corta en un gate, se supone que la empresa conserva el resto del año un núcleo de gobierno (fracciones de liderazgo y seguridad más el comité) y la pasarela de salida si ya está instalada; si el frente producto sigue, conserva además la parte de la base común que usa."
status: draft
tags: [supuesto, finanzas, gobierno, riesgo]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T12:00:00Z }
---
# Supuesto

Después de un corte, lo que sigue hasta fin de año es:

| Componente | Se conserva |
|---|---|
| Núcleo de gobierno | Las fracciones de liderazgo y de seguridad que fija el anexo C, más el comité de IA |
| Pasarela de salida | Solo si ya está instalada al momento del corte |
| Plataforma, piloto de producto, contractor y capacitación | No, salvo la base común mínima para el producto (abajo) |

Se costea por trimestre restante con el [costo por rol](/supuestos/costo-cargado-por-rol.md)
y los [precios externos](/supuestos/precios-externos-sin-cotizar.md).

## Corte parcial: se corta el frente interno y el producto sigue

Regla de precedencia propuesta por Finanzas: primero la seguridad (el núcleo de
gobierno y la pasarela no se cortan mientras un frente opere), después las
dependencias (el frente que sigue conserva lo que usa de la base común) y al
final la caja (el resto se corta). La **base común mínima para el producto**
supuesta es:

| Componente | Se conserva |
|---|---|
| Núcleo de gobierno y pasarela | Sí, como en el corte total |
| Infraestructura de base (gateway, trazas, evals en CI) | Al nivel del segundo trimestre del plan |
| Contractor de IA aplicada | Al 50%, para las evals y el harness del piloto |
| DevOps/QA | 0,5 FTE para operar el gateway y las evals del piloto |
| Capa de demostración externa | Si el gate la habilita por el producto liberado |
| Capacitación, champions y caso de referencia interno | No |

# Por qué es razonable

- El uso de IA sigue aunque el plan se corte (ver [uso de IA](/hechos/uso-ia-interno.md)),
  y los clientes financieros siguen exigiendo gobierno sobre el uso de IA de sus
  proveedores (ver [regulación](/hechos/regulacion-clientes-financieros.md)).
- La política de uso aceptable existe y hay que sostenerla (ver
  [gobierno y política](/hechos/gobierno-y-politica-ia.md)).

# Qué lo invalidaría

- Que el Directorio decida cortar también el gobierno: la base baja a cero y
  vuelve el riesgo de uso sin control.
- Que un cliente exija controles que el núcleo no cubre.
- Que el piloto de producto necesite más plataforma que la supuesta, o que pueda
  correr sin el gateway propio.

# Cautelas

- Los montos por gate están en el anexo E; esta ficha fija la composición.
- No describe personas: las fracciones son por función.
- La base común mínima para el producto es un supuesto de Finanzas que tiene
  que confirmar el dueño de la arquitectura; el 50% del contractor no tiene
  dato que lo respalde.
