---
type: Caso
title: Caso, dataset sintético de tickets de soporte con Gemini en BigQuery
description: Workflow de seis pasos para generar 10.000 tickets etiquetados sin PII, validados contra un data contract.
tags: [m1, datos, caso, sinteticos]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 14 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Contexto

Una empresa de telecomunicaciones quiere entrenar un clasificador de tickets de
soporte en cinco categorías: facturación, conectividad, portabilidad, equipos y
consultas generales. Tiene 50.000 tickets reales con nombres, DNIs y teléfonos, así
que no los puede usar directo. La solución: un dataset sintético de 10.000 tickets
etiquetados (p. 9).[^m1u3]

# Pasos

| # | Paso | Detalle |
|---|---|---|
| 1 | Esquema y [data contract](/conceptos/m1u3-data-contracts.md) | YAML con Data Contract CLI: `id`, `descripcion` (20-500 caracteres), `categoria` y `prioridad` con enum |
| 2 | Ejemplos few-shot | 5 por categoría (25 en total), elegidos a mano y verificados sin PII, en la tabla `ejemplos_fewshot` de BigQuery |
| 3 | Generar con Gemini en BigQuery | `ML.GENERATE_TEXT` con el esquema, los ejemplos y una instrucción; prompt en español argentino que prohíbe nombres, DNIs, correos y teléfonos reales; temperatura 0,8 y 200 tokens máximos |
| 4 | Privacidad diferencial con Gretel | Verifica que no haya patrones correlacionables con registros reales; ε = 1.0 |
| 5 | Validar contra el contrato | Tipos, enum de `categoria`, largo de `descripcion`, unicidad de `id` |
| 6 | Resultado | 10.000 tickets balanceados (2.000 por categoría), sin PII, con trazabilidad completa y garantías de privacidad diferencial |

Fuente: p. 9-11.[^m1u3]

El dataset se puede compartir con el equipo de ML, con auditores externos o publicar
como benchmark "sin riesgo de exposición de datos de clientes reales".[^m1u3]

# Cautela

El workflow es una receta del curso. Las capacidades de Gemini en BigQuery (febrero de
2025) y de Gretel (octubre de 2024) son afirmaciones del material y no se verificaron
contra la documentación vigente. Una garantía "formal" depende de que la
implementación de privacidad diferencial sea correcta, no solo del valor de ε.

Conceptos: [data moat y sintéticos](/conceptos/m1u3-data-moat-datos-sinteticos.md),
[higiene de datos](/conceptos/m1u3-higiene-de-datos.md).

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

[^m1u3]: M1U3, Tema 7 y ejemplo aplicado (p. 8-11)
