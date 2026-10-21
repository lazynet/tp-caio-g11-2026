---
type: Concepto
title: Escala de autonomía L0-L4
description: Escala pedagógica de cinco niveles que ordena cuánto puede hacer un agente, de informar a actuar solo dentro de límites.
tags: [m1, gobierno, agentes, autonomia]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Lectura M1U4 p. 13-14 y slide 17: escala pedagógica L0-L4, definiciones y aclaración de que no es un estándar oficial. Cotejo del agente revisado y confirmado por Martín en esta conversación."
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Escala

"Una herramienta pedagógica de esta unidad, **no un estándar oficial**" (p. 13).[^m1u4-lectura]
Citala como marco del curso, no como norma.

| Nivel | Nombre | Qué hace |
|---|---|---|
| L0 | Inform | Busca, resume o explica. No propone una decisión material ni ejecuta acciones |
| L1 | Recommend | Sugiere qué hacer; la decisión sigue siendo humana |
| L2 | Draft | Prepara la acción (redacta el email, genera la orden, configura el cambio) pero no la ejecuta |
| L3 | Act with approval | Puede ejecutar, pero necesita aprobación humana en ciertos puntos |
| L4 | Act autonomously within bounds | Opera sin aprobación caso por caso, dentro de permisos, límites y condiciones explícitas |

Fuente: sección 6.1, p. 13-14; slide 17.[^m1u4-lectura][^m1u4-slides]

**L4 no es "más maduro" que L2.** Un caso de uso puede estar bien diseñado para
quedarse siempre en L1 o L2 (p. 14).[^m1u4-lectura]

# Por qué importa

Un chatbot que resume un documento y un agente que modifica el ERP pueden usar el
mismo modelo, pero no son el mismo sistema de riesgo. Lo que cambia la gobernanza es
la capacidad de actuar sobre el mundo: enviar, borrar, comprar, pagar, aprobar,
modificar, publicar o ejecutar (p. 13).[^m1u4-lectura]

La autonomía es una de las cuatro variables del
[criterio de gobierno de agentes](/conceptos/m1u4-criterios-gobierno-agentico.md),
junto con acceso, consecuencia y reversibilidad. Es también un campo del
[inventario de IA](/conceptos/m1u4-inventario-y-operating-rhythm.md).

# Uso en el caso Mercurio

Se pide clasificar las iniciativas A-E en esta escala y analizar la de mayor
autonomía: ver el [caso Mercurio SA](/casos/m1u4-mercurio-sa.md).

# Relación con el plan

Respalda arquitectura (hasta dónde llega cada agente) y roadmap ajustado por riesgo.
Unidad: [M1U4](/unidades/m1u4-rol-gobernanza.md).

# Cautelas

* Cotejada el 2026-10-20 contra M1U4 lectura, p. 13-14 y slides v3, slide 17: niveles,
  definiciones, la aclaración "no un estándar oficial" y "L4 no es más maduro" coinciden.
  Fiel.
* La slide 17 resume distinto: L3 "ejecuta luego de aprobación humana" (la lectura:
  puede ejecutar y necesita aprobación en ciertos puntos) y L4 se llama "Act within
  bounds". La tabla sigue la lectura.
* Es una escala del curso; el uso para clasificar sistemas de Acme Labs es decisión del
  equipo.

[^m1u4-lectura]: M1U4, lectura, sección 6.1 (p. 13-14)
[^m1u4-slides]: M1U4, slide 17
