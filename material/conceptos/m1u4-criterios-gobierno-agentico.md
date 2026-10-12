---
type: Concepto
title: Criterios de gobierno agéntico, autonomía, acceso, consecuencia, reversibilidad y blast radius
description: Heurística de cuatro preguntas para calibrar la exigencia de governance, más blast radius y los límites del human-in-the-loop.
tags: [m1, gobierno, agentes, seguridad, riesgo]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Cuatro preguntas para decidir governance

| Variable | Pregunta |
|---|---|
| Autonomy | ¿Solo informa o puede actuar? (ver [escala L0-L4](/conceptos/m1u4-escala-autonomia-l0-l4.md)) |
| Access | ¿A qué datos, sistemas, tools y credenciales puede acceder? |
| Consequence | ¿Qué impacto tiene un error? |
| Reversibility | ¿La acción se puede deshacer fácil y completamente? |

"A mayor autonomía, acceso y consecuencia, y menor reversibilidad, mayor debería ser
la exigencia de governance, testing, permissions, observability y oversight."
(sección 6.4, p. 14-15; slide 17)[^m1u4-lectura][^m1u4-slides]

# Blast radius

Concepto que la lectura atribuye a Anthropic. La pregunta: **si este agente falla o
es manipulado, ¿cuál es el máximo daño que técnicamente puede producir?**
(p. 14)[^m1u4-lectura]

El riesgo no depende solo de la probabilidad de error sino de qué puede hacer cuando
se equivoca. Ejemplos de la lectura: un agente read-only sobre una base de datos
tiene otro blast radius que uno con escritura; uno que emite créditos hasta USD 50,
otro que uno ilimitado.

> "No controlar solamente lo que el agente debería hacer. Limitar también lo que
> puede hacer."

Formas de limitar el daño de manera determinística: sandboxes, virtual machines,
egress controls, permisos granulares y boundaries del entorno. Complementan, no
reemplazan, los controles probabilísticos del modelo.[^m1u4-lectura]

# Human-in-the-loop no alcanza

La aprobación humana es un control valioso con límites. La lectura cita análisis de
Anthropic (2026): los usuarios experimentados tienden a conceder más autonomía e
intervenir cuando el agente se desvía, en vez de aprobar cada acción; y los usuarios
de Claude Code aprobaban **aproximadamente el 93% de los permission prompts**, lo que
indica *approval fatigue* (p. 14). Son citas de segunda mano: las dos publicaciones
figuran en las lecturas (p. 25) pero no se verificaron.[^m1u4-lectura]

El oversight humano se diseña según:

- el conocimiento real de quien aprueba;
- la frecuencia de las aprobaciones;
- la posibilidad de detectar un error;
- la reversibilidad de la acción;
- la magnitud del daño posible;
- los permisos técnicos del agente.

Comparación de la slide 18:[^m1u4-slides]

| Opción A | Opción B |
|---|---|
| Permisos amplios, "¿estás seguro?" 25 veces, aprobación mecánica, approval fatigue | Sandbox, permisos mínimos, límites de monto, herramientas restringidas, rollback y observability |

# Ejercicio 5, ¿dónde cambia el governance?

Sistemas: A resume Zoom calls; B sugiere una respuesta a un cliente; C envía emails
automáticamente; D emite refunds hasta USD 100; E tiene escritura sobre el ERP
financiero. Se pide dónde aparece el primer salto cualitativo y qué vuelve más
riesgosos los siguientes, usando las cuatro variables. "No hay frontera universal"
(p. 15, slide 19).[^m1u4-lectura] Por la escala L0-L4, el salto de L1-L2 (A, B) a L3-L4
(C en adelante) es donde el agente pasa a actuar.

# Relación con el plan

Respalda el risk-adjusted roadmap y la sección de seguridad. Para el control concreto
que implementa estos límites ver el [Governance Stack](/conceptos/m1u4-governance-stack.md);
para el red teaming y DLP, [M3U1](/unidades/m3u1-seguridad.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, secciones 6.2 a 6.4 y ejercicio 5 (p. 14-15, 25)
[^m1u4-slides]: M1U4, slides 17, 18 y 19
