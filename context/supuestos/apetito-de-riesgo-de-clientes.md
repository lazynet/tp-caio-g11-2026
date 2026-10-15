---
type: Supuesto
title: "Apetito de riesgo de los clientes financieros frente a la IA"
description: "Se asume que los bancos y PSP clientes no van a permitir que su código ni sus datos pasen por modelos externos sin una cláusula contractual explícita y controles demostrables."
status: draft
tags: [supuesto, compliance, clientes]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Supuesto

Por defecto, un cliente financiero prohíbe usar modelos externos sobre su código y
sus datos. Para habilitarlo pide, como mínimo: cláusula contractual, inventario
del uso, ubicación de los datos, no entrenamiento con sus datos y evidencia de
controles (registro, revisión humana, gestión de incidentes).

# Por qué es razonable

- El BCRA obliga a las entidades a documentar y gestionar el uso de IA propio y
  de terceros (ver [regulación](/hechos/regulacion-clientes-financieros.md)).
- El secreto financiero y la Ley 25.326 limitan qué datos pueden salir del banco.
- La propia política de Acme Labs exige validar cliente por cliente y la
  matriz de restricciones todavía no existe (ver [gobierno](/hechos/gobierno-y-politica-ia.md)).
- En los clientes de consultoría es el cliente quien elige las herramientas
  (ver [IA en producto](/hechos/ia-en-producto-y-oferta.md)).

# Qué lo invalidaría

- Que los contratos vigentes resulten permisivos al armar la matriz.
- Que los clientes pidan activamente IA a su proveedor como condición.

# Cómo verificarlo

Completar la matriz de restricciones contractuales por cliente (pendiente del
área comercial) y registrar el resultado como hecho anonimizado.
