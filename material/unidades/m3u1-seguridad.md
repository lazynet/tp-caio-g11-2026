---
type: Unidad
title: M3U1 Seguridad, riesgos y resiliencia
description: Ataques a sistemas de IA y cómo defenderse, de prompt injection a red teaming.
tags: [m3, seguridad, defensa]
sources:
  - id: m3u1
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: M3U1 (el archivo dice Unidad 9), 20 slides
  - id: owasp-top10
    resource: https://genai.owasp.org/llm-top-10/
    title: OWASP Top 10 for LLM Applications 2025
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:20:00Z }
---

# Contenido

La unidad (20 slides) tiene cuatro bloques:[^m3u1]

1. **Prompt injection y jailbreaks:** [concepto](/conceptos/m3u1-prompt-injection-jailbreaks.md).
2. **DLP:** [tipos de datos y estrategias](/conceptos/m3u1-dlp-datos-en-riesgo.md) y [pipeline seguro](/conceptos/m3u1-pipeline-datos-seguro.md).
3. **Red teaming corporativo:** [proceso y metodologías](/conceptos/m3u1-proceso-red-teaming.md).
4. **Caso práctico:** [red team contra un agente](/casos/m3u1-red-team-agente.md).

La síntesis integra todo en [tres capas](/conceptos/m3u1-capas-seguridad.md):
prevención, detección y respuesta.

# Citas

"El modelo no distingue entre instrucciones del sistema y entradas maliciosas del
usuario."[^m3u1]

# Referencia externa

El curso no cita estándares. La referencia primaria para prompt injection es el
OWASP Top 10 for LLM Applications 2025, que ubica la inyección de prompts como
LLM01 y suma, entre otros, divulgación de información sensible (LLM02),
agencia excesiva (LLM06) y filtración del prompt del sistema (LLM07).[^owasp-top10]
La taxonomía y las defensas del curso son consistentes con OWASP pero más
acotadas: ver el detalle en
[prompt injection y jailbreaks](/conceptos/m3u1-prompt-injection-jailbreaks.md).

# Respalda

Seguridad y defensa: ver el [mapa](/mapa-plan-fuentes.md).

[^m3u1]: M3U1 (el archivo dice Unidad 9).
[^owasp-top10]: OWASP GenAI Security Project, Top 10 for LLM Applications 2025.
