---
type: Unidad
title: M2U4 AIOps, observabilidad y economía
description: Operación de sistemas de IA en producción, con evals, versionado, release gates y tokenomics.
tags: [m2, arquitectura, finanzas]
sources:
  - id: m2u4
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf
    title: M2U4 (el archivo dice Unidad 8), 20 slides, subtítulo "Evaluaciones, Versionado, Tokenomics y Casos Prácticos"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Contenido

El número de unidad del archivo (8) no coincide con el del programa: se mapeó por
título. Cuatro bloques:[^m2u4]

| Bloque | Idea | Concepto |
|---|---|---|
| Evals y observabilidad | Medir, monitorear y garantizar calidad | [Evals](/conceptos/m2u4-evals.md), [observabilidad](/conceptos/m2u4-observabilidad.md), [ciclo completo](/conceptos/m2u4-ciclo-evals-observabilidad.md) |
| Versionado y release gates | Control de cambios y despliegue seguro | [Versionado y release gates](/conceptos/m2u4-versionado-release-gates.md) |
| Tokenomics e inferencia | Economía del uso de tokens y costos operativos | [Tokenomics](/conceptos/m2u4-tokenomics.md) |
| Caso práctico | Evals y observabilidad sobre un agente real | [Caso del agente](/conceptos/m2u4-caso-evals-agente.md) |

# Ideas clave

- Evals y observabilidad son inseparables: calidad del modelo y fiabilidad operativa
  van de la mano.
- Versionado más release gates dan despliegues controlados, reproducibles y de alta
  calidad.
- Optimizar tokens es optimizar la economía completa de la inferencia.
- La mejora continua pide datos reales, métricas claras y trazabilidad total.[^m2u4]

# Cautelas

Las slides dicen "60-80% menos costo de inferencia" sin fuente. Se buscó una fuente
primaria y no se encontró; hay evidencia de ahorros grandes por caché y ruteo
(FrugalGPT, hasta 98% en el mejor caso; lecturas de caché a 0,1x), pero no del rango
60-80%. No va en una slide del plan. Detalle y fuentes en
[tokenomics](/conceptos/m2u4-tokenomics.md).

# Respalda

Arquitectura, roadmap técnico y finanzas: ver el [mapa](/mapa-plan-fuentes.md).

[^m2u4]: M2U4 (el archivo dice Unidad 8), Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf, slides 1-20.
