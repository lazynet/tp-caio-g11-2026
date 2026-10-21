---
type: Concepto
title: Evals
description: Métodos y métricas para medir rendimiento, precisión y calidad de un sistema de IA, y cómo se diseñan para un agente.
tags: [m2, arquitectura, calidad]
sources:
  - id: m2u4
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf
    title: M2U4 (el archivo dice Unidad 8), 20 slides
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "M2U4 (archivo 'Unidad 8'), slides 3 y 17: definición de evals, tres dimensiones y tres métricas del caso; la ausencia de metodología se verificó recorriendo las 20 slides. Cotejo del agente revisado y confirmado por Martín en esta conversación."
---

# Definición

Las evaluaciones (evals) son "los métodos y métricas utilizados para medir el
rendimiento, la precisión y la calidad de los modelos de IA": la "brújula" que dice si
un modelo cumple sus objetivos.[^m2u4]

| Dimensión | Qué mide |
|---|---|
| Rendimiento | Velocidad y eficiencia al generar respuestas |
| Precisión | Exactitud de las salidas respecto de lo esperado |
| Calidad | Coherencia, relevancia y utilidad de las respuestas |

# Métricas para un agente (caso práctico)

Para cada agente se diseñan métricas específicas, alineadas con objetivos de negocio
y técnicos. El caso propone tres:[^m2u4]

1. **Precisión:** ¿responde bien a los escenarios clave?
2. **Latencia:** ¿cuánto tarda en dar una respuesta útil?
3. **Capacidad de respuesta:** ¿maneja bien casos límite y entradas inesperadas?

Se usan junto con la [observabilidad](/conceptos/m2u4-observabilidad.md) en el
[ciclo completo](/conceptos/m2u4-ciclo-evals-observabilidad.md) y como insumo de los
[release gates](/conceptos/m2u4-versionado-release-gates.md). El
[caso práctico](/conceptos/m2u4-caso-evals-agente.md) los aplica a un agente.

# Qué no dice el curso

No da una metodología de evals (datasets de referencia, LLM-as-judge, umbrales).
Queda como hueco para el plan.

# Cautelas

Cotejada contra las slides 3 y 17 (y el recorrido completo del deck, que no trae
metodología de evals). El curso no vincula explícitamente las evals con los release
gates: ese insumo es lectura del repo.

[^m2u4]: M2U4 (Unidad 8), slides 3 y 17.
