---
type: Supuesto
title: "Costos de cierre al cortar el plan en un gate"
description: "Si el plan se corta en un gate, el cierre suma un mes de dedicación del contractor por preaviso y un mes de infraestructura de laboratorio, y legal y red team no comprometen gasto más allá del gate vigente."
status: draft
tags: [supuesto, finanzas, riesgo]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T01:10:00Z }
---
# Supuesto

| Componente | Costo de cierre supuesto |
|---|---|
| Contractor de IA aplicada | Un mes de preaviso a su dedicación vigente |
| Infraestructura de laboratorio | Un mes hasta darla de baja |
| Asesoría legal y red team | Cero más allá del gate: se contratan por etapa |
| Suscripciones existentes | Fuera del cierre: existen con o sin plan |

La pérdida al cortar en un gate es lo ejecutado hasta ese gate, más T0, más este
cierre (ver [convenciones](/supuestos/convenciones-de-calculo.md)).

# Por qué es razonable

- Un mes de preaviso es una condición habitual de contratación de contractors y
  se puede pactar al contratar.
- La infraestructura nueva corre en la nube con pago por uso (ver
  [stack](/hechos/stack-y-plataforma.md)): no tiene compromiso de largo plazo si
  no se firma uno.
- Los servicios externos se presupuestan por ejercicio (ver
  [precios externos](/supuestos/precios-externos-sin-cotizar.md)).

# Qué lo invalidaría

- Un contrato con preaviso más largo, compromiso de volumen o penalidad.
- Reservas de capacidad o hardware que comprometan más de 12 meses antes de G4.

# Cautelas

- Vale solo si los contratos se firman con esas condiciones: es una regla de
  contratación del plan, además de un supuesto de costo.
- Los montos por gate están en el anexo E; esta ficha fija la composición.
