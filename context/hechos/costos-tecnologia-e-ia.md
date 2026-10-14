---
type: Hecho
title: "Costos de tecnología e IA"
description: "El gasto de tecnología se duplicó entre febrero y septiembre de 2026 y pasó de cerca de 2% a 4% de la facturación; la nube es la mayor parte, y el consumo real de IA equivale a unas doce veces lo que se paga por suscripción."
status: draft
tags: [caso, finanzas, ia, finops]
sources:
  - id: interno-costos-tech-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Reportes mensuales de costos de tecnología, febrero a septiembre de 2026 (privado, anonimizado)"
  - id: interno-finanzas-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Cierre financiero interno de agosto de 2026 (privado, anonimizado)"
  - id: interno-telemetria-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Telemetría de uso de agentes de código por área, septiembre y octubre de 2026 (privado, anonimizado)"
  - id: interno-adopcion-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Reportes de adopción de IA y licencias, abril a octubre de 2026 (privado, anonimizado)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Gasto de tecnología (índice, febrero de 2026 = 100)

| Feb | Mar | Abr | May | Jun | Jul | Ago | Sep |
|---|---|---|---|---|---|---|---|
| 100 | 114 | 121 | 153 | 175 | 196 | 228 | 224 |

Incluye nube, herramientas de desarrollo e IA, devengado por mes.[^interno-costos-tech-2026]
Como proporción de la facturación pasó de cerca de 2% a cerca de 4% entre enero
y agosto de 2026.[^interno-finanzas-2026]

# Composición (septiembre de 2026)

| Rubro | Peso |
|---|---|
| Nube | ~80% |
| IA y herramientas de desarrollo | el resto |

El producto del Cliente A es el mayor centro de costo (más del 40%), seguido por
la infraestructura compartida y el proyecto de adopción de IA.[^interno-costos-tech-2026]

# IA

- El costo mensual de suscripciones de IA se duplicó en dos meses (julio a
  septiembre de 2026) por la expansión de seats.[^interno-costos-tech-2026]
- El costo promedio ponderado ronda USD 40-45 por seat y mes, con una mezcla
  mayoritaria de seats estándar y una minoría premium.[^interno-costos-tech-2026]
- Valorizado a precio de API, el consumo del agente de código en septiembre
  equivale a unas **12 veces** lo que se pagó por suscripción ese mes: un cambio
  del esquema de precios hacia el consumo impactaría el costo.[^interno-telemetria-ia-2026]
- Gemini no tiene costo incremental: viene incluido en la licencia de Workspace.
  No hay presupuesto definido para consumo por encima de la suscripción.[^interno-adopcion-ia-2026]

# Cautelas

- El peso de la IA dentro del gasto de tecnología no se publica: combinado con
  otros datos permitiría reconstruir cifras internas.
- Las cifras financieras surgen de un único corte interno (cierre de agosto de
  2026); el plan no usa otros cortes.
- El valor a precio de API es una estimación de la telemetría, no una factura.
- El promedio de USD 40-45 por seat corresponde a los seats de Claude. El costo
  por seat de Copilot no está desglosado en la fuente: un cálculo que lo
  necesite lo trata como supuesto.

[^interno-costos-tech-2026]: Reportes mensuales de costos de tecnología, febrero a septiembre de 2026 (privado, anonimizado)
[^interno-finanzas-2026]: Cierre financiero interno de agosto de 2026 (privado, anonimizado)
[^interno-telemetria-ia-2026]: Telemetría de uso de agentes de código por área, septiembre y octubre de 2026 (privado, anonimizado)
[^interno-adopcion-ia-2026]: Reportes de adopción de IA y licencias, abril a octubre de 2026 (privado, anonimizado)
