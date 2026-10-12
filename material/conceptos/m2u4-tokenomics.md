---
type: Concepto
title: Tokenomics e inferencia
description: Economía de los tokens y costos de inferencia, con las palancas de optimización del curso y el chequeo externo de la cifra de 60-80%.
tags: [m2, finanzas, arquitectura, costos]
sources:
  - id: m2u4
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_8.pdf
    title: M2U4 (el archivo dice Unidad 8), 20 slides
  - id: frugalgpt
    resource: https://arxiv.org/abs/2305.05176
    title: "Chen, Zaharia, Zou. FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance (2023)"
  - id: anthropic-caching
    resource: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
    title: Anthropic, documentación de prompt caching (consultada 2026-10-11)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Qué es un token

Unidad mínima de procesamiento de un LLM, "equivalente aproximadamente a ¾ de una
palabra en inglés". El costo de cada llamada a la API se calcula por tokens
consumidos, y hay dos tipos: **de entrada** (el prompt) y **de salida** (la
respuesta).[^m2u4]

# Costos de la inferencia

Son multidimensionales:[^m2u4]

| Costo | Qué es |
|---|---|
| Computacional | GPUs y CPUs para ejecutar el modelo en tiempo real |
| Energético | Electricidad de los centros de datos durante la inferencia |
| De API | Tarifas por uso de modelos como servicio (el curso nombra a OpenAI y Anthropic) |

# Palancas de optimización

El curso las llama "la palanca más directa para reducir costos operativos sin
sacrificar la calidad":[^m2u4]

1. **Prompts más concisos:** menos tokens de entrada, menos costo por llamada.
2. **Modelo adecuado al caso:** no siempre el más grande es el más eficiente.
3. **Caché y reutilización:** evitar recalcular respuestas idénticas.

El objetivo económico es maximizar el valor generado y minimizar el gasto operativo.
El [harness](/conceptos/harness-diez-fallas-contexto.md) suma otra palanca: un prefijo
estable para que el cache pegue y no reenviar el contexto entero en cada turno
(falla 9).

# Cautela resuelta: "reducir costos de inferencia hasta un 60-80%"

La slide 15 dice que un sistema bien optimizado "puede reducir costos de inferencia
hasta un 60-80% sin pérdida perceptible de calidad", sin fuente.[^m2u4]

**Resultado de la búsqueda: no se encontró una fuente primaria para el rango
60-80%.** Lo que sí hay:

- **FrugalGPT** (Stanford, 2023) reporta que puede "igualar el desempeño del mejor LLM
  individual (p. ej. GPT-4) con hasta un 98% de reducción de costo", usando adaptación
  de prompts, aproximación (caché, fine-tuning) y cascadas de modelos. Es un resultado
  de investigación en benchmarks de 2023, el mejor caso, no un número típico.[^frugalgpt]
- **Prompt caching de Anthropic:** las lecturas de caché cuestan 0,1 veces el precio
  base de entrada (0,05 en Opus 5.5 y Sonnet 5.5; 0,025 en Fable 5.1), y las escrituras
  de 5 minutos 1,25 veces. El ahorro depende de cuánto prefijo se reutiliza.[^anthropic-caching]

**Cómo usarlo:** el 60-80% sigue sin fuente y no va en una slide. Si el plan necesita
una cifra, se calcula con la tarifa vigente del proveedor elegido y el patrón de uso
real, como supuesto marcado, o se cita el mecanismo (caché, ruteo) sin porcentaje.

[^m2u4]: M2U4 (Unidad 8), slides 11-15.
[^frugalgpt]: Chen, Zaharia y Zou, FrugalGPT, resumen en arXiv: https://arxiv.org/abs/2305.05176
[^anthropic-caching]: Anthropic, prompt caching: https://platform.claude.com/docs/en/build-with-claude/prompt-caching (multiplicadores de la tabla de precios; los precios cambian, reverificar antes de usar).
