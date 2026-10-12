---
type: Concepto
title: Evals, observability, traceability e identity de agentes
description: Cuatro capacidades distintas para operar agentes en producción, qué responde cada una y qué datos reconstruir ante un incidente.
tags: [m1, gobierno, agentes, evals, observabilidad]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Por qué cuatro capacidades

Un agente puede fallar distinto a una app tradicional: elegir un tool incorrecto,
recuperar contexto equivocado, interpretar mal una instrucción, tomar un camino
inesperado o ejecutar bien una acción que nunca debió tener permiso de ejecutar
(p. 17).[^m1u4-lectura]

| Capacidad | Pregunta | Qué es |
|---|---|---|
| Evals | ¿Hace bien el trabajo? | Someter al sistema a tareas conocidas y medir si alcanza el resultado esperado |
| Observability | ¿Qué está haciendo en producción? | Entender el comportamiento durante la operación: latencia, errores, tool calls, costos, retries, rutas de ejecución, quality signals, intervenciones humanas |
| Traceability | ¿Podemos reconstruirlo? | Reconstruir técnica y organizacionalmente qué ocurrió |
| Identity y authorization | ¿Quién actúa y con qué permisos? | ¿Actúa como el usuario o con identidad propia? ¿Qué permisos exactos, por cuánto tiempo y bajo qué condiciones? |

Fuente: sección 8, p. 17-18; slide 21.[^m1u4-lectura][^m1u4-slides]

# Evals

En agentes, evaluar solo la respuesta final puede ser insuficiente: hay múltiples
pasos, tool calls, cambios de estado y recuperación de errores. La lectura cita a
Anthropic (2026, *Demystifying evals for AI agents*) para recomendar evals
end-to-end con failure modes reales (sin verificar la fuente). Sirven antes de
producción y durante todo el lifecycle para (p. 17):[^m1u4-lectura]

- comparar modelos;
- detectar regresiones;
- validar cambios de prompts o tools;
- convertir incidentes reales en nuevos casos de prueba;
- decidir si se puede aumentar la [autonomía](/conceptos/m1u4-escala-autonomia-l0-l4.md).

# Traceability no es transparencia

Cadena a poder reconstruir: User → Agent → system instructions → context → model →
retrieval → tool → credential → external system → action → result → human
intervention. **Transparencia** es qué información se ofrece a usuarios o personas
afectadas sobre la intervención de IA; **trazabilidad** permite reconstruir qué
ocurrió (p. 17).[^m1u4-lectura]

# Identity

El NIST lanzó en febrero de 2026 la *AI Agent Standards Initiative*, que según la
lectura apunta a interoperabilidad y seguridad de agentes autónomos, con identidad,
autorización e interacción segura con sistemas externos como problemas emergentes
(p. 18). No se verificó en fuente primaria.[^m1u4-lectura]

# Herramientas de tracing

LangSmith se usa de ejemplo (también se mencionan Langfuse y otras): muestran modelo,
prompts, tool calls, retrieval, tiempos y resultados, y permiten pasar de "el agente
respondió esto" a "podemos reconstruir cómo llegó hasta ahí". El tracing aporta
observabilidad y trazabilidad técnica; el governance suma políticas, controles,
retention, access management, ownership y evidencia (p. 18).[^m1u4-lectura]

**Tener logs no es tener observability**: la capacidad aparece con señales acordadas,
alertas útiles, un owner que las revisa y un proceso para convertir fallas en cambios o
nuevos evals.[^m1u4-lectura]

# Ejercicio 6, incidente de agente

Un agente envió un email incorrecto a 2.000 clientes. Antes de buscar culpables,
escribir cinco datos a recuperar de la traza (p. 18, slide 21). Las columnas de la
slide dan la guía:[^m1u4-lectura][^m1u4-slides]

| Dato | Pregunta |
|---|---|
| Trigger | ¿Quién o qué lo disparó? |
| Agent / version | ¿Qué workflow corría? |
| Context | ¿Qué información recibió? |
| Tool calls | ¿Qué herramientas usó? |
| Action / result | ¿Qué hizo exactamente? |

# Relación con el plan

Respalda la sección de seguridad y las capas de Controls y Evidence del
[Governance Stack](/conceptos/m1u4-governance-stack.md). Más detalle de evals y
release gates en [M2U4](/unidades/m2u4-aiops.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 8 (p. 17-18)
[^m1u4-slides]: M1U4, slide 21
