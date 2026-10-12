---
type: Concepto
title: Ciclo desplegar, evaluar, monitorear, mejorar
description: El ciclo continuo que combina evals y observabilidad para sostener calidad y fiabilidad de un sistema de IA en producción.
tags: [m2, arquitectura, operación]
sources:
  - id: m2u4
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf
    title: M2U4 (el archivo dice Unidad 8), 20 slides
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Las cuatro etapas

La slide lo dibuja como una rueda de cuatro aspas:[^m2u4]

1. **Desplegar** en producción.
2. **Evaluar** el modelo ([evals](/conceptos/m2u4-evals.md)).
3. **Monitorear** en tiempo real ([observabilidad](/conceptos/m2u4-observabilidad.md)).
4. **Mejorar** continuamente, y volver a desplegar.

La combinación garantiza "tanto la calidad del modelo como la fiabilidad operativa en
producción". Las conclusiones de la unidad las llaman "inseparables".[^m2u4]

# De reactivo a proactivo

| Capacidad | Efecto |
|---|---|
| Detección temprana | Las alertas saltan antes de que el usuario note la degradación |
| Diagnóstico preciso | Las trazas muestran dónde ocurre el fallo |
| Mejora continua | Los datos de producción alimentan el próximo ciclo de evaluación |

Antes de cada despliegue del ciclo, los
[release gates](/conceptos/m2u4-versionado-release-gates.md) deciden si la versión pasa.

[^m2u4]: M2U4 (Unidad 8), slides 5, 19 y 20.
