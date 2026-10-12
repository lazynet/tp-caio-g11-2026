---
type: Concepto
title: AI Governance Stack, de los principios a la evidencia
description: Cinco capas (Principles, Policy, Standards, Controls, Evidence) que convierten un valor abstracto en algo auditable, con el ejemplo del agente de refunds.
tags: [m1, gobierno, controles, evidencia]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
  - id: iso-42001
    resource: https://www.iso.org/standard/81230.html
    title: ISO, ISO/IEC 42001:2023
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Problema

Muchas organizaciones arrancan publicando principios (transparencia, privacidad, no
discriminación, supervisión humana, seguridad). Son útiles, pero "una organización no
puede auditar *somos responsables* si esa frase no se traduce en comportamientos
verificables" (p. 15).[^m1u4-lectura] El nombre de la capa superior varía (AI
Principles, Responsible AI Charter, AI Policy); el **AI Governance Stack** es una
forma práctica de conectarla con la operación.[^m1u4-lectura]

# Cinco capas

| # | Capa | Qué es |
|---|---|---|
| 1 | Principles / Charter | Qué valores y compromisos guían el uso de IA |
| 2 | Policy | Qué exige o prohíbe formalmente la organización |
| 3 | Standards / Guardrails | Cómo se aplican las políticas a clases concretas de sistemas |
| 4 | Controls | Qué mecanismos humanos o técnicos hacen cumplir los guardrails |
| 5 | Evidence | Qué registros demuestran que el control existió y funcionó |

Fuente: sección 7.1, p. 15-16.[^m1u4-lectura]

# Ejemplo (agente de customer service)

| Capa | Contenido |
|---|---|
| Principio | Toda acción material ejecutada por IA mantiene un responsable humano identificable |
| Política | Los agentes que ejecutan transacciones financieras operan con límites de monto y permisos documentados; fuera de esos límites requieren aprobación humana |
| Standard | El agente puede emitir refunds automáticos hasta USD 100; montos superiores requieren aprobación del supervisor |
| Control | La credencial técnica del agente no tiene permisos para ejecutar una operación superior al límite |
| Evidence | Los logs registran cada refund, la identidad del agente, el monto, la versión del workflow y cualquier aprobación humana |

Fuente: sección 7.2, p. 16. La slide 20 lo muestra con la capa de control y evidencia
juntas: "la herramienta no permite superar USD 100 y el log muestra quién intentó,
bloqueó o aprobó".[^m1u4-lectura][^m1u4-slides]

# Ideas a rescatar

- "Governance que existe solo en un PDF no es governance" (slide 20).[^m1u4-slides]
- El problema suele estar en el último kilómetro: pasar de una frase de policy a un
  control implementable, con owner, y verificar que sigue funcionando.
- La evidencia no se produce cuando llega la auditoría: surge del proceso normal de
  desarrollo y operación.[^m1u4-lectura]
- El control técnico (permisos de la credencial) es la forma determinística de limitar
  el [blast radius](/conceptos/m1u4-criterios-gobierno-agentico.md).

# ISO/IEC 42001 y la lógica de management system

La lectura vincula el stack con ISO/IEC 42001, que adopta la lógica de un
management system: establecer políticas y objetivos, implementar procesos, asignar
responsabilidades, mantenerlos y mejorarlos continuamente. Confirmado: la edición
vigente es ISO/IEC 42001:2023 (Edición 1, diciembre de 2023).[^m1u4-lectura][^iso-42001]
Ver [EU AI Act, NIST AI RMF e ISO/IEC 42001](/conceptos/m1u4-eu-ai-act-nist-iso.md).

# Relación con el plan

Es el esqueleto del modelo operativo de gobierno y de las políticas. Para el evidence
en producción ver [evals, observability y traceability](/conceptos/m1u4-evals-observability-traceability.md).
Unidad: [M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 7 (p. 15-16)
[^m1u4-slides]: M1U4, slide 20
[^iso-42001]: ISO, ISO/IEC 42001:2023, listado en iso.org (consultado el 2026-10-12)
