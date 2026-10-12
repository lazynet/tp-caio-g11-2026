---
type: Concepto
title: Ownership y matriz RACI
description: Cinco roles que conviene distinguir al escalar IA, la regla de una sola A y un ejemplo de RACI para un copiloto comercial.
tags: [m1, gobierno, ownership, raci]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Principio

"AI ownership no es AI team ownership." El error más común al escalar es que el
equipo técnico termine siendo dueño de todo: plataforma, modelo, riesgo, adopción y
hasta el resultado de negocio. Ese esquema no escala y asigna accountability a quien
muchas veces no controla el proceso que se modifica (p. 8).[^m1u4-lectura]

Slide 11: "AI cambia el proceso. No elimina su dueño." Y slide 12: introducir IA no
debería trasladar automáticamente el accountability del proceso hacia
Technology.[^m1u4-slides]

# Roles que conviene distinguir

No son necesariamente puestos distintos: en organizaciones pequeñas una persona cubre
varios. Lo que no puede faltar es accountability (slide 11).[^m1u4-slides]

| Rol | Responde por |
|---|---|
| Business Owner | El outcome de negocio: ingresos, costo, calidad, satisfacción, riesgo operacional o el KPI que el sistema busca mejorar |
| AI / Product Owner | Evolución del producto o workflow: prioridades, experiencia, roadmap, métricas, trade-offs. Aplicar IA no debería reducirse a automatizar el proceso existente: muchas veces la oportunidad es rediseñarlo |
| Domain / Process Expert | Conoce el trabajo real: excepciones, casos borde, reglas informales; define qué significa "correcto" |
| Engineering / Platform Owner | Arquitectura, integraciones, lifecycle técnico, reliability, entornos, despliegues, observabilidad y rollback |
| Security / Risk / Legal | Define o valida guardrails, requisitos regulatorios, privacidad, threat model y excepciones |

El CAIO diseña el sistema de governance y facilita estas interfaces, pero no debería
convertirse automáticamente en el business owner de cada iniciativa (p. 8-9).[^m1u4-lectura]

# RACI

| Letra | Significado |
|---|---|
| R, Responsible | Realiza el trabajo |
| A, Accountable | Responde finalmente por el resultado o decisión |
| C, Consulted | Debe participar antes de decidir |
| I, Informed | Debe conocer la decisión o el resultado |

**Regla: idealmente una sola A por decisión**, aunque haya varios R o C. Evita dos
fallas: que nadie sea responsable o que varios crean ser la autoridad final
(p. 9).[^m1u4-lectura]

## Ejemplo, copiloto de propuestas comerciales

El equipo de ventas usa un copiloto que arma borradores desde el CRM y un catálogo
aprobado; el vendedor revisa y envía.

| Rol | RACI posible |
|---|---|
| Director Comercial | A |
| Product/AI team | R |
| Engineering / Platform | R |
| Equipo de Ventas / Domain experts | C |
| Security / Data | C |
| CAIO / AI governance | C o I, según riesgo y política |

La matriz "no pretende ser una plantilla universal": hace visibles preguntas que
suelen aparecer recién cuando el sistema falla.[^m1u4-lectura]

# Ejercicio 3, el agente de refunds

Agente de customer service que emite refunds de hasta USD 100 sin aprobación
individual, construido por la plataforma central y pagado con presupuesto de
Tecnología. Opciones: A CTO, B CAIO, C Head of Customer Support, D developer, E CFO
(p. 10, slide 13).[^m1u4-lectura] La lectura no da la clave. Por el principio de
arriba (el negocio conserva el outcome) y la tabla de decision rights, la
respuesta coherente es C; es una inferencia de este bundle, no una respuesta del
material.

# Relación con el plan

Respalda el people plan (RACI con una sola A) y el gobierno. Ver
[decision rights](/conceptos/m1u4-decision-rights.md) y los
[AI Champions](/conceptos/m1u4-champions-y-literacy.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 3 y ejercicio 3 (p. 8-10)
[^m1u4-slides]: M1U4, slides 11, 12 y 13
