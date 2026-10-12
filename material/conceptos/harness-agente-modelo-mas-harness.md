---
type: Concepto
title: Agente = Modelo + Harness
description: Definición de AI harness con sus siete componentes, y la fórmula que el curso usa para distinguir el agente del chat.
tags: [arquitectura, agentes, harness]
sources:
  - id: harness
    resource: Memoria-Contexto-Harness.pdf
    title: Data Management en Soluciones de Gen IA, 16 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Definición

El AI harness (también agent harness o "arnés de agente") es "el software que rodea al
modelo y le da todo lo que el modelo por sí solo no tiene". La fórmula:
**Agente = Modelo + Harness**, donde el harness es todo lo que no es el modelo.[^harness]

Metáfora de la slide: el modelo es el cerebro; el harness es el cuerpo, las manos, la
memoria de trabajo y las reglas con las que ese cerebro actúa.[^harness]

# Los siete componentes (p. 14)

| # | Componente | Qué hace |
|---|---|---|
| 1 | Herramientas y APIs | Búsqueda, código, archivos, conectores |
| 2 | Memoria y estado | Lo que se recuerda entre turnos o sesiones |
| 3 | Gestión de contexto | Qué entra en el prompt, qué se resume, qué se descarta |
| 4 | Entorno de ejecución / sandbox | Dónde corre el código o las acciones |
| 5 | El loop | Llamar al modelo, ejecutar la herramienta, devolver el resultado, repetir |
| 6 | Guardrails, permisos y auditoría | Qué puede hacer, qué no, y registro de lo que hizo |
| 7 | Verificación y feedback | Chequear resultados, corregir, iterar |

# Por qué importa

Las [diez fallas de contexto](/conceptos/harness-diez-fallas-contexto.md) se resuelven
en el harness: presupuesto de working set, ledger, memoria versionada y gates. Para
dónde se construye hoy, ver [las tres capas](/conceptos/harness-tres-capas.md); para
los cinco elementos de diseño, [este concepto](/conceptos/harness-cinco-elementos-diseno.md).

[^harness]: Data Management en Soluciones de Gen IA (Memoria-Contexto-Harness.pdf), p. 14-15.
