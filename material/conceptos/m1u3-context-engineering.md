---
type: Concepto
title: Context engineering
description: Evolución del prompting hacia el diseño, prueba, versionado y medición del contexto que recibe un LLM.
tags: [m1, datos, arquitectura, evals]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 14 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Qué es

Disciplina que "sistematiza el diseño, la selección, la compresión y la gestión del
contexto" entregado al LLM en la inferencia. Supera el prompting artesanal hacia un
enfoque de ingeniería "reproducible y medible" (p. 3).[^m1u3]

El prompting empezó como práctica artesanal: instrucciones en lenguaje natural
ajustadas por intuición. Sigue siendo valioso, pero no alcanza para sistemas
confiables y escalables. El contexto pasa a ser un artefacto de ingeniería:
**diseñado, probado, versionado y optimizado** (p. 7).[^m1u3]

# Dimensiones

| Dimensión | Qué decide |
|---|---|
| Selección | Qué fragmentos son más relevantes para una consulta (el problema central de RAG) |
| Compresión | Reducir tokens sin perder información crítica: resumen automático, extracción de entidades, estructuras (JSON, tablas) en vez de texto libre |
| Estructuración | Cómo se ordena: instrucciones del sistema, ejemplos few-shot, documento de referencia, pregunta. Orden y estructura afectan de forma medible la calidad |
| Estado en conversaciones largas | Memoria explícita: qué recordar, qué comprimir, qué descartar |
| Evaluación | Medir el impacto de cada decisión sobre precisión, relevancia, coherencia y tasa de alucinaciones |

Fuente: Tema 6, p. 7-8.[^m1u3]

# Evaluación sistemática

Requiere benchmarks específicos del dominio, pipelines de evaluación automatizada y
tratar cada cambio de contexto como un experimento con hipótesis y métricas claras.
Eso distingue al *context engineer* del *prompt engineer*: no se trata solo de
escribir mejores instrucciones, sino de construir sistemas de contexto "robustos,
mantenibles y medibles" (p. 8).[^m1u3]

# Relación con otros conceptos

- Las opciones de fuente de conocimiento están en
  [estrategias de contexto](/conceptos/m1u3-estrategias-de-contexto.md).
- El contexto es la superficie por donde se filtra PII:
  [anonimización en inferencia](/conceptos/m1u3-anonimizacion-inferencia.md).
- El contexto como parte del harness del agente y sus fallas: ver
  [Memoria, contexto y harness](/unidades/memoria-contexto-harness.md).

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

[^m1u3]: M1U3, Tema 6 (p. 7-8) y conceptos clave (p. 3)
