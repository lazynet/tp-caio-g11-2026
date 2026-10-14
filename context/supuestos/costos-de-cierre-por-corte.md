---
type: Supuesto
title: "Costos de cierre al cortar el plan en un gate"
description: "Si el plan se corta en un gate, el cierre suma un mes de dedicación del contractor por preaviso y un mes de infraestructura de laboratorio, legal y red team no comprometen gasto más allá del gate vigente, y la reserva que lo cubre se amplía en cada gate que sube ese compromiso."
status: draft
tags: [supuesto, finanzas, riesgo]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T12:00:00Z }
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

## Composición por gate

El cierre depende de la dedicación que el gate anterior liberó:

| Corte en | Contractor | Laboratorio | Otros |
|---|---|---|---|
| G1 | Un mes al 50% (dedicación de T1) | Un mes del nivel de T1 (solo telemetría) | — |
| G2 o G3, sin producto | Un mes al 100% | Un mes del nivel de T2 | — |
| G2 o G3, con el producto liberado | Un mes al 100% | Un mes del nivel de T2 | Un mes del tenant del piloto |
| Corte parcial que conserva el producto | Un mes de la dedicación que se deja | — (se conserva) | — |

## Reserva de cierre (propuesta de Finanzas)

- El cierre se cubre con una **reserva** de caja, renglón propio, distinto del
  techo operativo del trimestre y de la base mínima. Solo se usa en un corte.
- La reserva se **actualiza en cada gate** que sube el compromiso (más
  dedicación del contractor, tenant del piloto), en el mismo acto y con la misma
  autoridad que aprueba el gate, y antes de liberar el compromiso nuevo.
- Si el contrato termina en plazo con el preaviso dado, la reserva no se usa.

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
- La reserva es una regla de autorización propuesta, no una decisión del
  Directorio: está pendiente de aprobación.
