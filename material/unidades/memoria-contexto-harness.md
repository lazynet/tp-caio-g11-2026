---
type: Unidad
title: Memoria, contexto y harness
description: Data management en soluciones de GenAI, con las 10 fallas de contexto y el modelo Agente = Modelo + Harness.
tags: [arquitectura, seguridad]
sources:
  - id: harness
    resource: Memoria-Contexto-Harness.pdf
    title: Data Management en Soluciones de Gen IA (16 páginas, no indica unidad)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Contenido

Deck de 16 páginas, "Memoria, contexto y harness". Tesis: "El chatbot solo demuestra.
La solución es el harness." No indica número de unidad.[^harness]

| Páginas | Tema | Concepto |
|---|---|---|
| 2 | Ventana de contexto, entrada y salida, comparación de modelos | [Ventana de contexto](/conceptos/harness-ventana-de-contexto.md) |
| 3-12 | Diez fallas de contexto, cada una con solución agéntica | [Las diez fallas](/conceptos/harness-diez-fallas-contexto.md) |
| 13 | Tres labs con un chatbot tradicional (solo capturas) | [Las diez fallas](/conceptos/harness-diez-fallas-contexto.md) |
| 14 | Qué es un AI harness, con 7 componentes | [Agente = Modelo + Harness](/conceptos/harness-agente-modelo-mas-harness.md) |
| 15 | Tres capas: framework, runtime, harness | [Tres capas](/conceptos/harness-tres-capas.md) |
| 16 | Cinco elementos de diseño | [Cinco elementos](/conceptos/harness-cinco-elementos-diseno.md) |

# Ideas clave

- Las fallas no se arreglan con un modelo más grande: se arreglan con presupuesto de
  working set, memoria versionada, ledger y gates.
- Dato e instrucción comparten canal en la ventana: lo recuperado es dato, nunca una orden.
- Gate humano antes de un efecto irreversible (enviar, pagar, borrar).[^harness]

# Cautelas

Los tamaños de ventana y los nombres de productos son del momento del deck y no se
verificaron. Los tres papers citados (Chroma 2025, Liu 2023, EMNLP 2025) sí se
confirmaron; ver [las diez fallas](/conceptos/harness-diez-fallas-contexto.md).

# Respalda

Arquitectura y seguridad: ver el [mapa](/mapa-plan-fuentes.md).

[^harness]: Data Management en Soluciones de Gen IA (Memoria-Contexto-Harness.pdf), p. 1-16.
