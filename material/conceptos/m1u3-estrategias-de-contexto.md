---
type: Concepto
title: Estrategias de contexto, prompt vs RAG vs fine-tuning vs long context
description: Las cuatro formas de darle a un LLM conocimiento específico, con sus ventajas, límites y costos.
tags: [m1, datos, arquitectura, rag, fine-tuning]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 14 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Qué es

Cuando un LLM tiene que responder sobre datos de la empresa, documentos recientes
o conocimiento de dominio, hay cuatro estrategias. La elección **no es binaria**:
los sistemas de producción más sofisticados combinan varias, por ejemplo RAG para
recuperar contexto y fine-tuning para adaptar tono y formato.[^m1u3]

La decisión no es solo técnica: tiene implicancias en privacidad, cumplimiento,
escalabilidad y ventaja competitiva.[^m1u3]

# Comparación

| Estrategia | Qué hace | Cuándo conviene | Límite o costo |
|---|---|---|---|
| Prompt engineering | Incluye la información relevante y las instrucciones directo en el prompt | Contexto chico y bien definido; es lo más rápido y barato | No escala si la información es extensa o dinámica |
| RAG | Recupera en tiempo real, desde una base vectorial, solo los fragmentos relevantes para cada consulta | Bases de millones de documentos e información que cambia, sin reentrenar | La calidad depende del sistema de recuperación: si trae fragmentos equivocados, el modelo responde sobre una base errónea |
| Fine-tuning | Ajusta los pesos del modelo sobre un dataset del dominio | Tareas muy específicas y repetitivas; internalizar estilo, formato o conocimiento | Más costoso; exige datos etiquetados de calidad |
| Long context | Mete libros, bases de código o históricos enteros en una ventana de hasta 1 millón de tokens (Gemini 1.5 Pro y 2.0 según el material) | Simplifica la arquitectura: no hace falta un sistema de recuperación aparte | Costo computacional alto y posible degradación de la atención en el centro de la ventana |

Fuente de la tabla: Tema 5, p. 7.[^m1u3]

# Relación con el plan

- Definición de RAG del glosario: combina recuperación desde una base externa con
  generación, "con información actualizada sin necesidad de reentrenamiento" (p. 2).[^m1u3]
- La selección de contexto es "el problema central de RAG" y una de las dimensiones
  del [context engineering](/conceptos/m1u3-context-engineering.md).[^m1u3]
- Los datos que viajan en el contexto pueden contener PII: ver
  [anonimización en inferencia](/conceptos/m1u3-anonimizacion-inferencia.md).
- La cifra de ventana (1 M de tokens) es del material de 2024-2025 y envejece rápido:
  no va en una slide sin chequear el modelo vigente.

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

[^m1u3]: M1U3, Tema 5 (p. 7) y conceptos clave (p. 2)
