---
type: Concepto
title: Costo por outcome aceptado
description: Métrica de economía de IA que reemplaza al costo por millón de tokens y conecta costo, adopción, outcome y valor.
tags: [m1, finanzas, economia, metricas]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Idea

La economía de IA no debería reducirse al costo por millón de tokens: "el modelo más
barato puede producir peores resultados, requerir más reintentos o aumentar la
revisión humana" (p. 13).[^m1u4-lectura]

La métrica propuesta es el **costo por outcome aceptado**.

# Ejemplos de la lectura

| Outcome | Métrica |
|---|---|
| Ticket | Costo por ticket resuelto correctamente |
| Factura | Costo por factura procesada sin intervención |
| Lead | Costo por lead calificado |
| Código | Costo por pull request aceptado |
| Documento | Costo por documento aprobado |

El CAIO conecta la cadena **cost → adoption → outcome → value**, aunque la empresa no
tenga un P&L separado para IA.[^m1u4-lectura]

# Relación con el plan

Es la métrica puente para el financial storytelling ante el CFO. Entra en la etapa de
Validation de [de demo a producción](/conceptos/m1u4-demo-a-produccion.md). La
economía de tokens y el versionado están en [M2U4](/unidades/m2u4-aiops.md); el
business case en [M1U2](/unidades/m1u2-portfolio-100-dias.md). La lectura no da
valores ni benchmarks: cualquier cifra hay que sacarla de datos propios.

Unidad: [M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 5.3 (p. 13)
