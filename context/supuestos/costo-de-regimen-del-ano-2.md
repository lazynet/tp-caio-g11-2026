---
type: Supuesto
title: "Costo de régimen del año 2"
description: "Para evaluar el equilibrio más allá de los 12 meses se supone un costo de régimen anual de cerca de 63 mil USD de caja de la base común (infraestructura y pasarela), 30 mil más de consumo si el producto sigue, y 1,5 FTE de mantenimiento a costo de senior."
status: draft
tags: [supuesto, finanzas]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T02:40:00Z }
---
# Supuesto

| Componente del año 2 | Valor |
|---|---|
| Caja anual de la base común (infraestructura y pasarela) | ~63 mil USD |
| Consumo de modelos del producto, solo si el piloto sigue después de G4 | ~30 mil USD |
| Mantenimiento | 1,5 FTE a costo de senior (~95 mil USD por año) |

Sin producto, el régimen es ~158 mil por año; con producto, ~188.

Es ilustrativo y queda fuera del alcance de los 12 meses: sirve para calcular el
throughput de equilibrio, no para pedir fondos.

# Por qué es razonable

- La caja extiende a régimen los costos mensuales de T4 de
  [precios externos](/supuestos/precios-externos-sin-cotizar.md).
- El mantenimiento usa el rango senior del [costo por rol](/supuestos/costo-cargado-por-rol.md).

# Qué lo invalidaría

- Un cambio del esquema de precios de los modelos hacia el consumo (ver
  [precio y dependencia de modelos](/supuestos/precio-y-dependencia-de-modelos.md)).
- Que el plan termine el año con más componentes en producción que los previstos.

# Cautelas

- Valor vigente en el anexo E al 2026-10-14.
- La infraestructura de T4 se dimensionó con el tráfico del piloto: sin producto
  podría ser menor, y lo confirma el anexo B.
- Se separa el consumo del producto porque lo tiene que pagar el producto, no la
  productividad interna: con él, el throughput de equilibrio sube de ~19% a ~23%.
