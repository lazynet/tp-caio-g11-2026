---
type: Concepto
title: Versionado y release gates
description: Qué se versiona en un sistema de IA y los cuatro tipos de puertas de liberación que una versión tiene que superar.
tags: [m2, arquitectura, operación, gobierno]
sources:
  - id: m2u4
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf
    title: M2U4 (el archivo dice Unidad 8), 20 slides
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Versionado

En IA el versionado "no se limita al código": abarca modelos, datos, configuraciones y
experimentos completos. Da tres cosas:[^m2u4]

- **Reproducibilidad:** recrear exactamente un experimento pasado.
- **Rollback:** volver a una versión anterior si algo falla.
- **Comparación:** analizar el rendimiento entre iteraciones.

## Qué se versiona

| Elemento | Contenido |
|---|---|
| Modelos | Pesos, arquitectura y configuración del modelo entrenado |
| Datos | Conjuntos de entrenamiento, validación y prueba |
| Código | Scripts de entrenamiento, pipelines y herramientas de procesamiento |
| Configuración | Hiperparámetros, variables de entorno y ajustes del sistema |

# Release gates

Puntos de control, automáticos o manuales, que un sistema debe superar antes de avanzar
en el ciclo de despliegue; garantizan que solo lleguen a producción versiones de alta
calidad.[^m2u4]

| # | Tipo de gate | Qué revisa |
|---|---|---|
| 1 | Pruebas de rendimiento | Benchmarks de velocidad y precisión |
| 2 | Evaluaciones de seguridad | Detección de sesgos y vulnerabilidades |
| 3 | Revisiones éticas | Alineación con principios de IA responsable |
| 4 | Análisis de impacto | Efectos en producción y en usuarios finales |

Juntos, versionado y gates dan un despliegue "controlado, trazable y de alta
calidad".[^m2u4] Los gates 1 y 2 se alimentan de [evals](/conceptos/m2u4-evals.md); el
gate humano antes de efectos irreversibles del agente está en el
[harness](/conceptos/harness-cinco-elementos-diseno.md).

[^m2u4]: M2U4 (Unidad 8), slides 7-10 (la lista de gates está en una imagen de la slide 10).
