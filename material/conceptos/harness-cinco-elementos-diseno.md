---
type: Concepto
title: Cinco elementos de diseño del harness
description: Los cinco elementos con los que el curso resume un harness bien diseñado, desde el objetivo hasta el gate antes de un efecto irreversible.
tags: [arquitectura, seguridad, harness]
sources:
  - id: harness
    resource: Memoria-Contexto-Harness.pdf
    title: Data Management en Soluciones de Gen IA, 16 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
status: draft
---

# Los cinco elementos (p. 16)

El harness es "el sistema alrededor del modelo. No es el chat". Se resume en
cinco elementos:[^harness]

| # | Elemento | Qué exige |
|---|---|---|
| 1 | Objetivo y reglas | Se reafirman en cada turno; no se esperan del chat |
| 2 | Working set | Solo lo de este paso, con presupuesto; si no entra, fallar en voz alta |
| 3 | Memoria externa | Hechos con fecha y versión; el chat no es la base |
| 4 | Tools y MCP | Resumen más id; el volcado vive afuera; el dato no es una orden |
| 5 | Gate | Cortar, compactar a ledger, o pedir un humano antes de un efecto irreversible |

# Cómo se relaciona con las fallas

| Elemento | Fallas que ataca |
|---|---|
| Objetivo y reglas | 10 instruction drift, 3 silent truncation |
| Working set | 1 context rot, 2 lost in the middle, 9 costo y latencia |
| Memoria externa | 6 conflicting needles, 7 compaction loss, 5 retrieval noise |
| Tools y MCP | 4 tool-output bloat, 8 indirect prompt injection |
| Gate | 8 injection, 10 drift, y cualquier efecto irreversible |

La tabla de relación es una lectura del repo sobre las
[diez fallas](/conceptos/harness-diez-fallas-contexto.md); el PDF no la presenta así.
El gate se conecta con los [release gates](/conceptos/m2u4-versionado-release-gates.md)
y con la escala de autonomía de [M1U4](/unidades/m1u4-rol-gobernanza.md).

# Cautelas

Cotejada contra el PDF, p. 16: el título, la frase "El sistema alrededor del modelo.
No es el chat." y los cinco elementos con su texto. La tabla de relación con las
fallas y los vínculos con los release gates y con M1U4 son lectura del repo, no del
curso. El PDF no numera los elementos como pasos ni los ordena por prioridad.

[^harness]: Data Management en Soluciones de Gen IA (Memoria-Contexto-Harness.pdf), p. 16.
