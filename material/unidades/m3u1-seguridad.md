---
type: Unidad
title: M3U1 Seguridad, riesgos y resiliencia
description: Ataques a sistemas de IA y cómo defenderse, de prompt injection a red teaming.
tags: [m3, seguridad, defensa]
sources:
  - id: m3u1
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: M3U1 (el archivo dice Unidad 9), 20 slides
    pages: slides 1-20
  - id: owasp-top10
    resource: https://genai.owasp.org/llm-top-10/
    title: OWASP Top 10 for LLM Applications 2025
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:20:00Z }
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "M3U1 (archivo Unidad 9), 20 slides, estructura, cita y síntesis en tres capas; IDs OWASP LLM01/02/06/07 contra el Top 10 2025 leído el 2026-10-20. Cotejo del agente revisado y confirmado por Martín en esta conversación."
---

# Contenido

La unidad (20 slides) tiene cuatro bloques, los de la agenda de la slide 2:[^m3u1]

1. **Prompt injection y jailbreaks** (slides 3 a 6): [concepto](/conceptos/m3u1-prompt-injection-jailbreaks.md).
2. **DLP** (slides 7 a 10): [tipos de datos y estrategias](/conceptos/m3u1-dlp-datos-en-riesgo.md) y [pipeline seguro](/conceptos/m3u1-pipeline-datos-seguro.md).
3. **Red teaming corporativo** (slides 11 a 14): [proceso y metodologías](/conceptos/m3u1-proceso-red-teaming.md).
4. **Caso práctico** (slides 15 a 18): [red team contra un agente](/casos/m3u1-red-team-agente.md).

La síntesis (slide 19) integra todo en [tres capas](/conceptos/m3u1-capas-seguridad.md):
prevención, detección y respuesta. La slide 20 trae las conclusiones.

# Citas

"El modelo no distingue entre instrucciones del sistema y entradas maliciosas del
usuario." (slide 3)[^m3u1]

# Referencia externa

El curso no cita estándares. La referencia primaria para prompt injection es el
OWASP Top 10 for LLM Applications 2025, que ubica la inyección de prompts como
LLM01 y suma, entre otros, divulgación de información sensible (LLM02),
agencia excesiva (LLM06) y filtración del prompt del sistema (LLM07).[^owasp-top10]
La taxonomía y las defensas del curso son consistentes con OWASP pero más
acotadas: ver el detalle en
[prompt injection y jailbreaks](/conceptos/m3u1-prompt-injection-jailbreaks.md).

# Cautelas

Cotejo del 2026-10-20 contra las 20 slides de M3U1 (el archivo dice Unidad 9): la
agenda de la slide 2, los cuatro bloques, la cita de la slide 3, la síntesis de tres
capas (slide 19, con las listas de cada capa) y el conteo de 20 slides coinciden. Se
sumaron los rangos de slides a la lista de contenido. La ficha no desarrolla el detalle
de las slides 7 a 18; ese detalle vive en las fichas enlazadas, que se cotejan por
separado. La numeración de las referencias OWASP LLM01, LLM02, LLM06 y LLM07 coincide
con la lista de la página del Top 10 for LLM Applications 2025 (WebFetch del 2026-10-20).

La ficha dice "el curso no cita estándares": en las 20 slides no hay ninguna cita a
OWASP, NIST ni otro marco. Es una afirmación sobre estas slides, no sobre el resto de la
cursada.

# Respalda

Seguridad y defensa: ver el [mapa](/mapa-plan-fuentes.md).

[^m3u1]: M3U1 (el archivo dice Unidad 9).
[^owasp-top10]: OWASP GenAI Security Project, Top 10 for LLM Applications 2025.
