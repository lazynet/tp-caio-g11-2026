---
type: Supuesto
title: "Rampa de la ganancia de productividad"
description: "La ganancia de throughput llega por tramos: en el escenario base, 0% del objetivo en T1, 25% en T2, 60% en T3 y 100% en T4; en el pesimista 0/10/30/60% y en el optimista 0/40/80/100%."
status: draft
tags: [supuesto, finanzas, productividad]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T01:10:00Z }
---
# Supuesto

| Escenario | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Base | 0% | 25% | 60% | 100% |
| Pesimista | 0% | 10% | 30% | 60% |
| Optimista | 0% | 40% | 80% | 100% |

El porcentaje es la fracción del objetivo de throughput de la
[ganancia de productividad](/supuestos/ganancia-de-productividad.md) que se
alcanza en cada trimestre.

# Por qué es razonable

- T1 mide la línea de base y forma a los equipos: atribuirle ganancia
  contaminaría la comparación.
- La adopción por área sube de a poco (ver [uso de IA](/hechos/uso-ia-interno.md)),
  y el piloto de delivery mostró un efecto temprano que todavía no está probado
  más allá de su primera semana (ver [pilotos](/hechos/encuesta-y-pilotos-ia.md)).

# Qué lo invalidaría

- Que la medición de T2 no muestre ganancia contra la línea de base de T0.
- Que la ganancia aparezca pero se pague con más incidentes o retrabajo.

# Cautelas

- Las rampas pesimista y optimista las fija el anexo E (ronda 3, hallazgo H17).
  El pesimista las combina con un objetivo de 5%, por debajo del piso de la
  [ganancia de productividad](/supuestos/ganancia-de-productividad.md): es el
  caso de corte, no un escenario que el plan espere.
- La unidad de throughput y su conversión a valor las define el anexo E
  (hallazgo H09); la rampa se aplica sobre esa definición.
