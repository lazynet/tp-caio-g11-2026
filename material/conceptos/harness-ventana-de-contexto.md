---
type: Concepto
title: Ventana de contexto
description: Qué entra en la ventana de un modelo, la diferencia entre ventana de entrada y de salida, y la comparación de tamaños que muestra el curso.
tags: [arquitectura, contexto, harness]
sources:
  - id: harness
    resource: Memoria-Contexto-Harness.pdf
    title: Data Management en Soluciones de Gen IA, 16 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Qué es

Entra todo: system, reglas, historial, tools, documentos y la respuesta que se está
escribiendo. No es la "Memory" del producto. Regla del curso: "si no entra, para el
modelo no existe".[^harness]

| Ventana | Qué es |
|---|---|
| De entrada | Lo que se manda: prompt, documentos, resultados de tools. Comparte espacio con la salida: si se reserva mucha salida, entra menos |
| De salida | El tope de lo que el modelo puede emitir en ese turno. El thinking, si existe, suele contar ahí |

Decirle "ignorá lo anterior" no libera tokens.[^harness]

# Comparación del curso

| Modelo | Contexto | Salida |
|---|---|---|
| GPT6 Astra | 1M | 128K |
| Fable 5.1 | 1M | 128K |
| Gemini 3.8 Flash | 1M | 64K |

El pie de la slide cita como fuentes las páginas de API de OpenAI (gpt-6-astra),
Anthropic (Fable 5.1), Google (Gemini 3.8 Flash) y docs.x.ai (4.6).[^harness]

# Cautelas

Los tamaños son del momento en que se armó el deck y cambian con cada versión. No
se verificaron contra las páginas de los proveedores; reverificar antes de usarlos en
una slide. Una ventana grande no evita las [fallas de contexto](/conceptos/harness-diez-fallas-contexto.md):
la calidad cae antes de llenarla.

[^harness]: Data Management en Soluciones de Gen IA (Memoria-Contexto-Harness.pdf), p. 2.
