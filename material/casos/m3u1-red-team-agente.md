---
type: Caso
title: Red team contra un agente de IA corporativo
description: Ejercicio de la unidad en que un red team compromete un agente con acceso a bases internas, con hallazgos y recomendaciones.
tags: [m3, seguridad, red-teaming, agentes]
sources:
  - id: m3u1
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: M3U1 (el archivo dice Unidad 9), 20 slides
    pages: slides 15-18
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:09:00Z }
---

# Escenario

Ejercicio ilustrativo (no hay empresa ni cifras): un red team ataca un agente de
IA corporativo, como un chatbot o un sistema autónomo de decisión.[^m3u1]

- **Sistema objetivo:** agente con acceso a bases de conocimiento internas, que responde consultas y ejecuta acciones automatizadas.
- **Objetivo del atacante:** extraer información sensible, inducir acciones no autorizadas o generar contenido inapropiado que comprometa a la organización.
- **Vectores:** prompt injection para revelar datos del sistema; roleplay adversario para eludir restricciones éticas; explotación de contexto para acceder a datos confidenciales; llamadas maliciosas a las API del agente.

# Hallazgos

| Hallazgo | Detalle |
|---|---|
| Vulnerabilidades de datos | El agente reveló fragmentos de su prompt de sistema y datos de usuarios previos ante inyección directa |
| Acciones no autorizadas | Se lo indujo a operar fuera de su alcance mediante contexto engañoso |
| Debilidades en API | Endpoints sin autenticación adecuada permitían consultas sin restricciones |

# Recomendaciones

| Recomendación | Contenido |
|---|---|
| Separación de contextos | Aislar el prompt del sistema de las entradas del usuario |
| Autenticación en API | Tokens y control de acceso en todos los endpoints |
| Monitoreo en tiempo real | Detectar y bloquear patrones de ataque en ejecución |
| Entrenamiento adversario | Incorporar los ataques descubiertos al ciclo de mejora |

Fuente de las tablas: [^m3u1]

# Qué enseña

Cada hallazgo cae en una capa de la pirámide: la fuga de datos en prevención, la
falta de autenticación en prevención y el monitoreo en detección. Ver
[capas de seguridad](/conceptos/m3u1-capas-seguridad.md),
[prompt injection](/conceptos/m3u1-prompt-injection-jailbreaks.md) y
[proceso de red teaming](/conceptos/m3u1-proceso-red-teaming.md).

[^m3u1]: M3U1, slides 15-18.
