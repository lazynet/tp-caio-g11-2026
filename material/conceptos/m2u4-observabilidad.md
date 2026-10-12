---
type: Concepto
title: Observabilidad en IA
description: Capacidad de entender el estado interno de un sistema de IA a partir de sus salidas, con logs, métricas y trazas.
tags: [m2, arquitectura, operación]
sources:
  - id: m2u4
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf
    title: M2U4 (el archivo dice Unidad 8), 20 slides
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Definición

"La capacidad de entender el estado interno de un sistema de IA a partir de sus
salidas externas".[^m2u4]

# Los tres pilares

| Pilar | Qué es | En el agente (caso práctico) |
|---|---|---|
| Logs | Registro detallado de eventos y errores | Detectar errores y eventos críticos |
| Métricas | Indicadores cuantitativos del estado, en tiempo real | Supervisar CPU, memoria y consumo |
| Trazas | Seguimiento del flujo de decisiones a través del sistema | Entender decisiones y flujos |

Cada pilar da una capa distinta de visibilidad; juntos permiten entender el
comportamiento real del agente.[^m2u4]

# Por qué es crítica

- **Detección proactiva de fallos:** anomalías antes de que lleguen al usuario.
- **Comportamiento en producción real:** los modelos se comportan distinto fuera del entorno de pruebas.
- **Mejora continua basada en datos:** las métricas de producción alimentan el ciclo de reentrenamiento.[^m2u4]

Complementa a los [evals](/conceptos/m2u4-evals.md); juntos forman el
[ciclo completo](/conceptos/m2u4-ciclo-evals-observabilidad.md).

[^m2u4]: M2U4 (Unidad 8), slides 4, 6 y 18.
