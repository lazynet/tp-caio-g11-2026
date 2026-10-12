---
type: Concepto
title: De la demo a producción, Exploration, Validation, Production
description: Tres etapas de madurez de un workflow de IA, requisitos de producción, capacidades compartidas y las dos fricciones del POC huérfano y la plataforma sin presupuesto.
tags: [m1, gobierno, produccion, operating-model]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Idea

"El salto de demo a producción no es un cambio de hosting. Es un cambio de
responsabilidad." Las herramientas permiten demos extraordinarias en días y eso
genera una deuda nueva: decenas de prototipos que parecen a un paso de producción y
nunca se vuelven capacidades confiables (p. 11).[^m1u4-lectura] "Una demo demuestra
posibilidad; producción demuestra repetibilidad."[^m1u4-lectura]

# Tres etapas

El marco lo propone OpenAI en 2026 para clasificar la inversión en workflows de IA
(según la lectura, no se verificó la fuente).[^m1u4-lectura]

| Etapa | Pregunta | Qué importa |
|---|---|---|
| Exploration | ¿Es técnicamente posible y potencialmente útil? | Se permiten atajos; aprender rápido y barato |
| Validation | ¿Funciona suficientemente bien sobre casos representativos y contra un quality bar explícito? | Eval set, casos borde, failure modes, métricas de negocio, usuarios reales, [costo por outcome](/conceptos/m1u4-costo-por-outcome.md), riesgos |
| Production | ¿Podemos operarlo repetidamente con reliability, ownership, seguridad y economía aceptables? | Owner, evals, observability, security, rollback (slide 15) |

Fuente: sección 5.1, p. 11-12; slide 15.[^m1u4-lectura][^m1u4-slides]

# Requisitos de producción agrupados (p. 12)

| Grupo | Incluye |
|---|---|
| Identidad, permisos y seguridad | Identity, authorization, límites de acceso, controles de compliance |
| Calidad y operación | Evals continuas, logging, observability, incident response, rollback, SLAs/SLOs |
| Integración y datos | Entornos, deployment lifecycle, integraciones y [data contracts](/conceptos/m1u3-data-contracts.md) |
| Negocio y adopción | Business owner, soporte operacional, gestión del cambio y presupuesto sostenible |

# Capacidades compartidas

Al crecer el número de soluciones, reconstruir estas capacidades por proyecto es
costoso y riesgoso. OpenAI identifica como inversión central posible: identity,
trusted connectors, curated knowledge, evaluations, observability, model routing y
patrones de agentes reutilizables (p. 12). La pregunta de operating model: "¿qué
construimos una vez para que cien equipos puedan moverse más rápido y de forma más
segura?"[^m1u4-lectura]

# Dos fricciones reales

- **Todos quieren la plataforma, nadie quiere pagarla.** Cada unidad financia su caso
  de uso y pocas absorben identity, observability, evals o conectores. El CAIO tiene
  que hacer explícito quién financia el backbone común y cómo se reparten los costos;
  si no, se reconstruye por proyecto o Technology subsidia indefinidamente.
- **El POC huérfano.** El equipo que hizo la demo no es el que puede operarla; el
  sponsor financia el experimento y nadie presupuestó integración, monitoreo,
  soporte, seguridad ni mantenimiento. Pregunta de graduation: "¿quién lo va a operar
  el lunes siguiente al lanzamiento y con qué presupuesto?" (p. 12)[^m1u4-lectura]

# Ejercicio 4, 18 de 20

Un agente de órdenes de compra, construido en dos semanas, resolvió 18 de 20 casos en
una demo interna. El CFO pregunta cuándo va a producción. Se piden tres cosas que
hay que saber antes de responder (p. 13, slide 16).[^m1u4-lectura] El material no da
la clave; usando las secciones de arriba salen, por ejemplo: qué cubre el eval set y
qué pasa en los casos borde y los 2 fallidos, quién es el owner y el presupuesto de
operación, y qué permisos, rollback y observability tiene.

# Relación con el plan

Respalda el roadmap técnico y los kill/scale gates de
[M1U2](/unidades/m1u2-portfolio-100-dias.md) y los release gates de
[M2U4](/unidades/m2u4-aiops.md). Unidad: [M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 5 (p. 11-13)
[^m1u4-slides]: M1U4, slides 15 y 16
