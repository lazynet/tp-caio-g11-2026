---
type: Supuesto
title: "Costo de régimen del año 2"
description: "Para evaluar el equilibrio más allá de los 12 meses se supone un costo de régimen anual de cerca de 48 mil USD de caja de la base común (infraestructura sin piloto y pasarela), 45 mil más si el producto sigue (infraestructura del piloto y consumo), y 1,5 FTE de mantenimiento a costo de senior."
status: draft
tags: [supuesto, finanzas]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T03:18:00Z }
---
# Supuesto

| Componente del año 2 | Valor |
|---|---|
| Caja anual de la base común: infraestructura sin piloto (~33) y pasarela (~15) | ~48 mil USD (24-72) |
| Producto, solo si el piloto sigue después de G4: incremento de infraestructura del piloto (~15) y consumo de modelos (~30) | ~45 mil USD |
| Mantenimiento | 1,5 FTE a costo de senior (~95 mil USD por año) |

Sin producto, el régimen es ~143 mil por año; con producto, ~188.

Es ilustrativo y queda fuera del alcance de los 12 meses: sirve para calcular el
throughput de equilibrio, no para pedir fondos.

# Por qué es razonable

- La caja extiende a régimen los costos mensuales de T4 de
  [precios externos](/supuestos/precios-externos-sin-cotizar.md), con la
  infraestructura de T4 sin piloto al nivel de T2, como la dimensiona el anexo B.
- El mantenimiento usa el rango senior del [costo por rol](/supuestos/costo-cargado-por-rol.md).

# Qué lo invalidaría

- Un cambio del esquema de precios de los modelos hacia el consumo (ver
  [precio y dependencia de modelos](/supuestos/precio-y-dependencia-de-modelos.md)).
- Que el plan termine el año con más componentes en producción que los previstos.

# Cautelas

- Valor vigente en el anexo E al 2026-10-14.
- El anexo B confirma que, sin piloto, la infraestructura de T4 queda al nivel de
  T2 (1,5-4 mil por mes); el incremento del piloto es del frente producto.
- Se separa el costo del producto porque lo tiene que pagar el producto, no la
  productividad interna: con él, el throughput de equilibrio sube de ~17% a ~23%.
