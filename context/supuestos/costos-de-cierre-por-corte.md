---
type: Supuesto
title: "Costos de cierre al cortar el plan en un gate"
description: "Costos y reservas de salida propuestos, diferenciados entre el mínimo vigente y el paquete completo, sujetos a condiciones contractuales y autorización antes de asumir compromisos."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-21
  scope: "Revalidación registrada por instrucción expresa de Martín en la sesión del 21/10/2026 sobre el contenido vigente del PR #52. Reservas de salida por alcance: mínimo con caja de hasta 500 USD y reserva de 1.000, cierre interno de 16-24 h y reserva de tiempo de 2.000; paquete completo con preaviso y rangos de cierre supuestos, sujetos a negociación. R-03 separa la continuidad del corte y exige recostear compromisos que excedan la reserva antes de firmar. Se mantiene como Supuesto de diseño: esta declaración no acredita mediciones, contratos, disponibilidad ni ejecución de decisiones futuras."
tags: [supuesto, finanzas, riesgo]
sources:
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, reservas del paquete completo y salida del mínimo"
  - id: minimo
    resource: "context/supuestos/paquete-minimo-de-aprendizaje.md"
    title: "Paquete mínimo vigente, reservas de caja y tiempo para cierre"
  - id: precios
    resource: "context/supuestos/precios-externos-sin-cotizar.md"
    title: "Rangos de diseño de infraestructura y servicios externos sin cotización"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Costo cargado supuesto por rol y convención de 160 h mensuales"
  - id: convenciones
    resource: "context/supuestos/convenciones-de-calculo.md"
    title: "Convenciones de preparación, caja, tiempo y autorizaciones"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

La composición original corresponde al paquete completo con contractor y
plataforma, no al mínimo vigente. Ambas salidas se separan abajo; son
supuestos de planificación sujetos a contratos, costos y autorización.[^finanzas][^minimo]

| Componente | Costo de cierre supuesto |
|---|---|
| Contractor de IA aplicada | Un mes de preaviso a la dedicación que se cancela, como condición a negociar |
| Infraestructura de laboratorio | Un mes supuesto hasta darla de baja; validar condiciones de facturación y baja |
| Asesoría legal y red team | Cero adicional más allá del gate solo si los contratos por etapa no dejan compromisos ni penalidades |
| Suscripciones existentes | Fuera del cierre incremental del modelo, bajo el supuesto de que continúan con o sin plan |

La exposición económica acumulada hasta cerrar suma lo que se haya ejecutado
hasta el gate, la preparación previa y el cierre. Se presentan caja y tiempo
por separado; su suma no equivale íntegramente a pérdida de caja ni acredita
una pérdida contable (ver [convenciones](/supuestos/convenciones-de-calculo.md)).[^convenciones]

## Composición por gate

El cierre del paquete completo depende de la dedicación que se hubiera
autorizado y contratado en el gate anterior.[^finanzas]

| Corte en | Contractor | Laboratorio | Otros |
|---|---|---|---|
| Mes 3 | Un mes al 50% (dedicación de los meses 1-3) | Un mes del nivel de los meses 1-3 (solo telemetría) | — |
| Mes 3 sin señal (el contractor cierra; gobierno y formación continúan) | Un mes al 50%, dentro de la reserva propuesta del primer tramo | La telemetría que continúa no se cuenta como baja; su eventual cierre se estima por debajo de 1.000 USD | No ampliar reserva solo si no se asumen nuevos compromisos de salida; verificarlo antes de continuar |
| Mes 6 o 9, sin producto | Un mes al 100% | Un mes del nivel de los meses 4-6 | — |
| Mes 6 o 9, con el producto liberado | Un mes al 100% | Un mes del nivel de los meses 4-6 | Un mes del tenant del piloto |
| Corte parcial que conserva el producto | Un mes de la dedicación que se deja | — (se conserva) | — |

### Rangos de caja y reservas propuestas del paquete completo

| Corte | Composición calculada (USD) | Rango de cierre (USD) | Reserva propuesta (USD) |
|---|---|---|---|
| M3, contractor al 50% | 50% × 4.500-11.000 más un tercio de 500-1.500 de telemetría trimestral | 2.417-6.000, redondeado al USD | 6.000 |
| Posterior, contractor al 100%, sin producto | 4.500-11.000 más 1.500-4.000 de infraestructura | 6.000-15.000 | 15.000 |
| Posterior, con tenant del piloto | Cierre anterior más 500-2.000 del tenant | 6.500-17.000 | 17.000 |

Los rangos combinan costos supuestos por rol e infraestructura sin cotizar.
En M3, el equivalente mensual de telemetría es una convención de cálculo, no
una condición de facturación acreditada.[^costo-rol][^precios][^finanzas]

En un corte parcial se costea solo la dedicación que se cancela. La parte de
contractor e infraestructura que continúe con el producto es continuidad,
presupuestada aparte, no costo de darla de baja.[^finanzas]

## Salida del mínimo vigente

Sin contractor ni plataforma central, se proponen estas reservas:[^minimo]

| Componente | Cierre estimado | Reserva propuesta |
|---|---|---|
| Herramientas | Hasta un mes, máximo supuesto 500 USD (1.500 trimestrales / 3) | Caja: 1.000 USD |
| Cierre interno senior | 16-24 h para exportar, revocar y archivar: 16 × 3.000 / 160 a 24 × 7.500 / 160 = 300-1.125 USD | Tiempo: 2.000 USD |

La legal por hitos solo se considera sin preaviso si el contrato lo permite.
Si las condiciones exigen más, se amplía la reserva antes de comprometer.
No se suman de nuevo reservas ya incluidas en los techos del mínimo.[^finanzas][^minimo]

## Reserva de cierre (propuesta de Finanzas)

- El cierre del paquete completo se cubre con una **reserva** propuesta de
  caja, renglón propio, distinto del techo operativo y de la continuidad.
  El mínimo distingue reserva de caja y de tiempo. Solo se usan si ocurre el
  cierre; la reserva no es gasto ejecutado.[^finanzas][^minimo]
- La reserva se **actualiza en cada gate** que sube el compromiso (más
  dedicación del contractor, tenant del piloto), en el mismo acto y con la misma
  autoridad que aprueba el gate, y antes de liberar el compromiso nuevo.
- Si el contrato termina en plazo con el preaviso dado, la reserva no se usa.
- Las tablas del anexo E que ya incluyen cierre no vuelven a sumarlo. La
  reserva identifica autorización contingente, no otro costo agregado al
  mismo cierre.[^finanzas]

# Por qué es razonable

- El mes de preaviso es una condición de diseño a negociar; la ficha no
  acredita que sea habitual ni que esté pactada.
- La baja de infraestructura en un mes y la contratación de servicios por
  etapa permiten modelar una salida acotada solo si las condiciones reales
  lo admiten; no se deducen de usar nube ni de tener un presupuesto por
  ejercicio.[^precios]

# Qué lo invalidaría

- Un contrato con preaviso más largo, compromiso de volumen o penalidad.
- Reservas de capacidad o hardware que comprometan más de 12 meses antes del cierre del mes 12.

# Cautelas

- Vale solo si los contratos se firman con esas condiciones: es una regla de
  contratación del plan, además de un supuesto de costo.
- Los montos de exposición acumulada por gate están en el Anexo E; esta ficha
  concilia composición de salida y reservas propuestas.
- El Directorio aprueba la reserva del mínimo (caja 1 / tiempo 2) dentro de la
  segunda liberación; el CFO la recalcula en cada gate antes de asumir
  obligaciones nuevas y, sin reserva suficiente, el gate no libera el compromiso
  nuevo (R-03)[^resoluciones].
- La verificación registra revisión humana de los supuestos, sin acreditar
  contratos, facturas, ejecución ni aprobación del gasto.

[^finanzas]: Anexo E, "Cuánto pierdo si corto", reservas de cierre del paquete completo, corte mixto y "Pedido inicial: paquete mínimo"; las reservas son propuestas de autorización y el cierre ya incluido no se vuelve a sumar.
[^minimo]: Paquete mínimo de aprendizaje, sin contractor ni plataforma central; cierre interno de 16-24 h senior y reservas de salida de 1.000 USD de caja y 2.000 USD de tiempo.
[^precios]: Precios externos sin cotizar, rangos de diseño de telemetría, infraestructura y tenant del piloto; se cotizan solo si un gate libera plataforma o producto, y el CFO verifica la cotización antes de contratar.
[^costo-rol]: Rangos supuestos de IA aplicada de 4.500-11.000 USD/mes y senior DevOps/QA de 3.000-7.500 USD/mes, con 160 h mensuales para costear.
[^convenciones]: Convenciones de cálculo y separación de caja y tiempo, preparación previa y liberaciones sujetas a autorización.
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
