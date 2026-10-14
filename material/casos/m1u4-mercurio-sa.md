---
type: Caso
title: Caso Mercurio SA, operating model, readiness, ownership, autonomía y cambio regulatorio
description: Actividad integradora de M1U4 sobre una empresa argentina de ecommerce de 350 empleados sin CAIO, con cinco iniciativas de IA y un giro regulatorio.
tags: [m1, gobierno, caso, defensa]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Contexto (lectura p. 20-22)

Mercurio es una empresa argentina de ecommerce y servicios con **350 empleados**. Tiene
CEO, CTO, VP Product, Head of Data, Security Lead, Legal externo y líderes en Customer
Service, Finanzas, HR y Operaciones. **Ningún CAIO formal.** La adopción de IA creció
de forma orgánica: algunos empleados usan ChatGPT o Claude por su cuenta, hay
experimentos internos y varias áreas quieren avanzar hacia agentes.[^m1u4-lectura]

## Iniciativas

| | Iniciativa | Qué hace |
|---|---|---|
| A | Copilot interno | Resume documentos y responde preguntas sobre políticas internas |
| B | Customer Service Agent | Responde consultas de clientes con información del CRM y la base de conocimiento |
| C | Refund Agent | Customer Service propone que emita refunds automáticos de hasta USD 100 |
| D | Collections Agent | Finanzas quiere que contacte clientes morosos, negocie alternativas predefinidas y registre acuerdos en el ERP |
| E | Recruiting AI | RRHH quiere un sistema que analice CVs y recomiende quién pasa a entrevista |

La versión de las slides (23) es distinta: E pasa a "IA para filtrar candidatos" y
suma una opción "Features de IA embebidas en CRM / HRIS", para reforzar el tema de
inventario de IA de terceros. La consigna de la slide: elegir una y escribir
"letra + principal riesgo + accountable".[^m1u4-slides]

# Las cinco partes

| Parte | Consigna | Conceptos que se aplican |
|---|---|---|
| 1. Operating model | El CEO pide asumir el liderazgo de IA: ¿cargo CAIO o rol existente?, ¿qué se centraliza?, ¿qué se delega a los equipos de negocio?, ¿hace falta un AI Council y para qué decisiones? | [Decision rights](/conceptos/m1u4-decision-rights.md), [arquitectura organizacional](/conceptos/m1u4-arquitectura-organizacional.md), [Council vs CoE](/conceptos/m1u4-council-vs-coe.md) |
| 2. Readiness | Elegir dos pilares del modelo de Microsoft y definir estado actual, evidencia, target a 12 meses y una iniciativa para cerrar el gap | [Maturity model](/conceptos/m1u4-microsoft-agentic-maturity.md) |
| 3. Ownership | Elegir B, C, D o E y definir Business Owner, Product Owner, Domain Expert, Engineering/Platform Owner, Security/Risk/Legal y Accountable final | [RACI](/conceptos/m1u4-raci-ownership.md) |
| 4. Autonomía | Clasificar A-E en L0-L4. Para la de mayor autonomía: sistemas que toca, permisos, blast radius, acciones reversibles y dónde tiene sentido el human oversight | [Escala L0-L4](/conceptos/m1u4-escala-autonomia-l0-l4.md), [criterios](/conceptos/m1u4-criterios-gobierno-agentico.md) |
| 5. Cambio regulatorio | Seis meses después Mercurio contrata empleados en España y vende a clientes de la UE, y quiere desplegar Recruiting AI también en España: ¿qué nueva conversación abre el CAIO antes? | [EU AI Act, NIST e ISO](/conceptos/m1u4-eu-ai-act-nist-iso.md) |

Fuente: p. 21-22.[^m1u4-lectura]

# Qué se espera

"No se espera que el alumno realice un análisis jurídico completo": se espera que
reconozca que el contexto de uso puede cambiar la clasificación de riesgo, las
obligaciones y el diseño de governance (p. 22).[^m1u4-lectura] Objetivo de la slide:
conectar ownership + autonomy + risk + governance + regulación.[^m1u4-slides]

# Lectura propuesta (no es clave del material)

El material no incluye soluciones. Estas notas son una inferencia de este bundle
usando los conceptos de la unidad, pensadas para practicar la defensa:

- **Mayor autonomía:** D (cobranzas) suele ser el de mayor autonomía y consecuencia
  porque contacta clientes y escribe en el ERP; es el caso para el análisis de blast
  radius.
- **Giro regulatorio:** E (Recruiting AI) es la que cambia: empleo y gestión de
  trabajadores aparece entre las áreas high-risk del Anexo III. Con el calendario
  vigente aplicaría desde el 2 de diciembre de 2027, no desde 2026
  ([verificación](/conceptos/m1u4-ai-omnibus-sigen.md)).
- **Inventario:** las features de IA embebidas en CRM/HRIS (opción E de la slide) son
  el recordatorio de que el [inventario](/conceptos/m1u4-inventario-y-operating-rhythm.md)
  debe incluir IA de terceros.

# Relación con el plan

Sirve de ejercicio de defensa para el board: la misma estructura de cinco preguntas
se puede aplicar a Acme Labs. Unidad: [M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 10 (p. 20-22)
[^m1u4-slides]: M1U4, slide 23
