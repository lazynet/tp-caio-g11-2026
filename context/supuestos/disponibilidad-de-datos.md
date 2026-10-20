---
type: Supuesto
title: "Disponibilidad de datos para casos de IA"
description: "Los datos utilizables a corto plazo son los internos de Acme Labs (código propio, tickets, documentación, telemetría y finanzas); los datos productivos de clientes no están disponibles para IA."
status: draft
tags: [supuesto, datos, arquitectura]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Supuesto

En los 12 meses del plan, los casos de IA se alimentan de:

- **Disponibles:** repositorios propios, tickets y documentación de proyectos,
  telemetría de ingeniería y de uso de IA, datos financieros operativos internos.
- **Disponibles con anonimización o datos sintéticos:** datos operativos de los
  productos propios.
- **No disponibles:** datos productivos de clientes y datos de categoría especial.

# Por qué es razonable

- La política interna prohíbe enviar datos personales de clientes a cualquier IA
  externa y pide datos sintéticos en el producto con datos de categoría
  especial (ver [gobierno](/hechos/gobierno-y-politica-ia.md)).
- Acme Labs ya mide uso de IA, costos y salud de repositorios con pipelines
  propios (ver [uso de IA](/hechos/uso-ia-interno.md)).

# Qué lo invalidaría

- Que la calidad de los datos internos sea más desigual de lo esperado (ver
  [stack](/hechos/stack-y-plataforma.md)).
- Que un cliente habilite contractualmente el uso de sus datos.

# Cómo verificarlo

Revisar el [inventario existente](/hechos/inventario-y-distribucion-de-datos.md)
como primer entregable de la fase de diagnóstico: contrastar su vigencia,
cobertura, responsables, clasificación y calidad documentada para las fuentes
elegibles de los casos de IA. Completar las brechas sobre ese inventario y
verificar accesos e integración entre los sistemas que contienen los datos.
