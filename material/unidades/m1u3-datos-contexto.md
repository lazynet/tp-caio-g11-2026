---
type: Unidad
title: M1U3 Datos y contexto
description: Estrategias de contexto, data contracts y manejo de datos sensibles en inferencia.
tags: [m1, datos, arquitectura, seguridad]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 14 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# De qué trata

La calidad de un sistema de IA no depende solo de la arquitectura del modelo ni del
tamaño del dataset: depende de cómo se gestionan, curan y sirven los datos durante
todo el ciclo de vida. "Una mala higiene de datos se propaga silenciosamente hacia el
modelo, generando sesgos, alucinaciones y respuestas poco confiables" (p. 1).[^m1u3]
La estrategia de datos es responsabilidad compartida entre quienes diseñan, operan y
consumen los sistemas.

El contexto que el modelo recibe en la inferencia es tan importante como los datos de
entrenamiento. La conclusión del documento: la estrategia de datos "no es un paso
previo al desarrollo del sistema de IA: es parte integral de su arquitectura" (p.
11).[^m1u3]

# Los siete temas y sus conceptos

| Tema (p.) | Concepto |
|---|---|
| 1. Higiene de datos a escala (3-4) | [Higiene de datos](/conceptos/m1u3-higiene-de-datos.md) |
| 2. Data moats y datos sintéticos (4-5) | [Data moat y datos sintéticos](/conceptos/m1u3-data-moat-datos-sinteticos.md) |
| 3. Data contracts y calidad (5-6) | [Data contracts](/conceptos/m1u3-data-contracts.md), con el YAML de ejemplo |
| 4. Privacidad y anonimización (6) | [Anonimización de PII](/conceptos/m1u3-anonimizacion-inferencia.md) |
| 5. Prompt vs RAG vs fine-tuning vs long context (7) | [Estrategias de contexto](/conceptos/m1u3-estrategias-de-contexto.md) |
| 6. Context engineering (7-8) | [Context engineering](/conceptos/m1u3-context-engineering.md) |
| 7. Caso práctico con Gemini en BigQuery (8-11) | [Caso de tickets sintéticos](/conceptos/m1u3-caso-tickets-sinteticos.md) |

# Ideas clave

- Un error sistemático en el 5% de los registros puede producir un sesgo perceptible.[^m1u3]
- Las cuatro estrategias de contexto no son excluyentes: los sistemas sofisticados las
  combinan.
- La PII se protege en dos momentos distintos, entrenamiento e inferencia, con
  técnicas diferentes.
- Un data contract convierte la calidad del dato en responsabilidad compartida y
  auditable.
- El dato sintético con privacidad diferencial permite compartir sin exponer PII.

# Integración (conclusión, p. 11)

"Un dataset mal higienizado contamina el fine-tuning; un Data Contract mal definido
permite que datos corruptos lleguen al modelo; una estrategia de contexto inadecuada
desperdicia la capacidad del LLM o expone PII innecesariamente."[^m1u3] Los próximos
módulos aplicarán estos fundamentos a RAG avanzado, evaluación en producción y MLOps
con monitoreo de calidad de datos.

# Lecturas recomendadas del documento (p. 11-12)

Kleppmann (2017), *Designing Data-Intensive Applications*; Huyen (2022), *Designing
Machine Learning Systems*; Geodakyan y Ratner (2022), *Data-Centric AI*; Barocas,
Hardt y Narayanan (2023), *Fairness and Machine Learning*; Dwork y Roth (2014), *The
Algorithmic Foundations of Differential Privacy*; Lewis et al. (2020), *Retrieval-
Augmented Generation for Knowledge-Intensive NLP Tasks*.[^m1u3]

Fuentes web citadas por el documento (blogs de Google Cloud sobre datos sintéticos con
BigQuery DataFrames, Gemini en BigQuery y Gretel; y cuatro herramientas de PII y
data contracts sin URL legible en el PDF): no se verificaron.

# Cautelas

Las fechas de producto (febrero y octubre de 2025/2024), la capacidad de ventana de 1
M de tokens y el calificativo de "estado del arte" son afirmaciones del documento y no
se cotejaron con fuentes actuales.

# Respalda

Arquitectura y seguridad: ver el [mapa](/mapa-plan-fuentes.md). Contexto de agente y
harness en [Memoria, contexto y harness](/unidades/memoria-contexto-harness.md).

[^m1u3]: M1U3, documento de 14 páginas (la cita indica la página)
