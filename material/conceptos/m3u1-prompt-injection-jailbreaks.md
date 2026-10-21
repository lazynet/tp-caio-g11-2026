---
type: Concepto
title: Prompt injection y jailbreaks
description: Qué es la inyección de prompts, cómo se clasifican los jailbreaks, qué riesgos generan y cómo se mitigan.
tags: [m3, seguridad, prompt-injection, jailbreak, owasp]
sources:
  - id: m3u1
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: M3U1 (el archivo dice Unidad 9), 20 slides
    pages: slides 3-6
  - id: owasp-llm01
    resource: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
    title: OWASP Top 10 for LLM Applications 2025, LLM01 Prompt Injection
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:09:00Z }
status: draft
---

# Definición

La inyección de prompts manipula el comportamiento de un LLM con entradas
elaboradas: el atacante inserta instrucciones ocultas que el modelo interpreta
como legítimas y lo desvían de su propósito original.[^m3u1] La idea central de la
unidad: *"El modelo no distingue entre instrucciones del sistema y entradas
maliciosas del usuario."*[^m3u1]

OWASP la define de forma equivalente: ocurre cuando los prompts del usuario alteran
el comportamiento o la salida del LLM de maneras no previstas, aun si la entrada
es imperceptible para una persona, siempre que el modelo la procese.[^owasp-llm01]

# Jailbreaks

Son un tipo específico de inyección de prompts, pensado para eludir los
mecanismos de seguridad del modelo y lograr contenido no deseado o acciones fuera
de su propósito.[^m3u1] OWASP coincide: es la forma de inyección en que el modelo
descarta por completo sus protocolos de seguridad.[^owasp-llm01]

| Técnica (según el curso) | Qué hace |
|---|---|
| Roleplay adversario | El modelo adopta un personaje sin restricciones |
| Instrucciones disfrazadas | Comandos maliciosos embebidos en texto inocente |
| Contexto engañoso | Se fabrica un escenario falso que justifica el pedido |

# Riesgos

| Riesgo | Descripción |
|---|---|
| Información errónea | Contenido falso o desinformación deliberada |
| Código malicioso | Scripts dañinos o exploits funcionales |
| Filtración de datos | Exposición de información confidencial del sistema o de usuarios |
| Contenido ofensivo | Material inapropiado, ilegal o dañino |

Fuente de la tabla: [^m3u1]

# Mitigación

El curso propone tres medidas:[^m3u1]

1. **Filtrado robusto de entradas:** detectar y bloquear patrones de inyección antes del procesamiento.
2. **Validación de prompts:** verificar integridad y contexto de cada instrucción recibida.
3. **Entrenamiento adversario continuo:** exponer el modelo a ejemplos de ataque.

# Complemento OWASP (no está en el curso)

OWASP distingue inyección **directa** (la entrada del propio usuario) de
**indirecta** (contenido externo, como un sitio o un archivo, con instrucciones
embebidas) y suma estas defensas, varias ausentes de las slides:[^owasp-llm01]

- Acotar rol, capacidades y límites del modelo en el prompt del sistema.
- Definir formatos de salida esperados y validarlos con código determinístico.
- Filtrar entradas y salidas (filtros semánticos y de strings).
- **Mínimo privilegio:** credenciales propias de la aplicación y funciones extendidas manejadas en código, no por el modelo.
- **Aprobación humana** para acciones de alto riesgo.
- Segregar e identificar el contenido no confiable.
- Pruebas adversarias y simulaciones de ataque, tratando al modelo como usuario no confiable.

Para el plan: en la mitigación de prompt injection (slide 6) el curso se queda en
filtrar, validar y entrenar; el caso de la slide 18 suma separación de contextos,
autenticación de API y monitoreo, pero ninguna slide trae mínimo privilegio ni
aprobación humana. Esa es la defensa de fondo contra agentes según OWASP, y conecta
con los niveles de autonomía de [M1U4](/unidades/m1u4-rol-gobernanza.md).

# Cautelas

Cotejo del 2026-10-20 contra las slides 3 a 6 de M3U1 (el archivo dice Unidad 9; también
se leyeron las slides 1, 2 y 15 a 20 para ubicar el contexto y el caso): la definición, la
frase citada, los tres tipos de jailbreak, los cuatro riesgos y las tres medidas coinciden
con el texto de las slides. La única corrección es la de la sección "Para el plan": la
versión anterior decía que el curso se queda en filtrar, validar y entrenar sin
distinguir la slide 6 del caso de la slide 18.

La sección "Complemento OWASP" se cotejó con la página LLM01:2025 Prompt Injection del
OWASP GenAI Security Project (WebFetch del 2026-10-20): coinciden la definición, la
descripción del jailbreak, la distinción directa e indirecta y las siete defensas
listadas. Es lectura de la página web en esa fecha, no de una versión archivada.

# Relacionado

- [Capas de seguridad](/conceptos/m3u1-capas-seguridad.md)
- [Proceso de red teaming](/conceptos/m3u1-proceso-red-teaming.md)
- [Caso: red team a un agente](/casos/m3u1-red-team-agente.md)

[^m3u1]: M3U1, slides 3-6.
[^owasp-llm01]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection.
