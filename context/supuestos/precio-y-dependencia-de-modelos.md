---
type: Supuesto
title: "Precio de los modelos y dependencia de proveedor"
description: "Se asume que el costo por unidad de capacidad de los modelos no sube en 12 meses, pero que el precio de las suscripciones planas puede ajustarse hacia el consumo real."
status: draft
tags: [supuesto, finanzas, arquitectura, riesgo]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Supuesto

- El costo por unidad de capacidad de los modelos se mantiene o baja durante el plan.
- El esquema de suscripción plana no es estable: el consumo real equivale a un
  múltiplo alto de lo que se paga (ver [costos](/hechos/costos-tecnologia-e-ia.md)),
  así que el plan presupuesta un escenario en el que se paga por consumo.
- Cambiar de proveedor de modelos tiene un costo de migración moderado si el
  harness (contratos de agente, skills, telemetría) se diseña neutral al modelo.

# Por qué es razonable

La tendencia del mercado es de precios unitarios en baja, pero los proveedores
ajustan planes y límites; el piloto interno ya chocó con límites de uso y parte
de los participantes advirtió sobre la dependencia de un solo proveedor (ver
[encuesta](/hechos/encuesta-y-pilotos-ia.md)).

# Qué lo invalidaría

- Un aumento de precios o recorte de límites del proveedor principal.
- Que la arquitectura termine acoplada a funciones exclusivas de un proveedor.

# Cómo verificarlo

Revisión mensual de costo por persona activa y por resultado, con un escenario
de pago por consumo en el anexo financiero.
