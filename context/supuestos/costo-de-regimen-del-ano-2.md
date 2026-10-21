---
type: Supuesto
title: "Costo de régimen del año 2"
description: "Escenario ilustrativo del paquete completo para el año 2: caja base de 48.000 USD, 45.000 adicionales con producto y mantenimiento de 1,5 FTE por 94.500 USD de tiempo, sin presupuesto integral ni autorización de continuidad."
status: draft
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Martín confirmó los supuestos y cuentas del año 2 del paquete completo: caja base central 48.000 USD (24.000-72.000), producto adicional 45.000 (18.000-72.000), mantenimiento de 1,5 FTE/2.880 h por 94.500 de tiempo (54.000-135.000); totales económicos centrales 142.500 sin producto y 187.500 con producto, rangos 78.000-207.000 y 96.000-279.000. Confirma cálculo sin redondear y equilibrio de capacidad valorizada de 16,7% y 23,1% de throughput atribuible con cohorte central supuesta. No demuestra ahorro de caja, payback ni recuperación del año 1; no es presupuesto del mínimo ni autorización 2028. Alcance operativo, capacidad y costos pendientes de validar; no acredita cobertura integral del año 2 ni ingresos del producto. Confirmado en esta conversación como supuesto."
tags: [supuesto, finanzas]
sources:
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, régimen ilustrativo del año 2 y equilibrio económico"
  - id: arquitectura
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, infraestructura de base y separación del incremento del piloto"
  - id: precios
    resource: "context/supuestos/precios-externos-sin-cotizar.md"
    title: "Rangos de infraestructura, pasarela y consumo como supuestos sin cotización"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Costo senior supuesto y convención de 160 h mensuales"
  - id: cohorte
    resource: "context/supuestos/desarrolladores-en-equipos-propios.md"
    title: "Cohorte y costo cargado supuestos para valorar capacidad"
  - id: rampa
    resource: "context/supuestos/rampa-de-la-ganancia.md"
    title: "Conversión de throughput a tiempo liberado a output fijo"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Es un escenario del paquete completo, fuera de los doce meses del plan. No es
el presupuesto del mínimo vigente ni una autorización para 2028.[^finanzas]

| Componente anual | Valor central supuesto (USD) | Rango supuesto (USD) |
|---|---|---|
| Caja de la base común: infraestructura sin piloto y pasarela | 48.000 | 24.000-72.000 |
| Caja adicional del producto, solo si continúa | 45.000 | 18.000-72.000 |
| Mantenimiento, 1,5 FTE senior, como tiempo | 94.500 | 54.000-135.000 |
| Total económico sin producto | 142.500 (aproximadamente 143.000) | 78.000-207.000 |
| Total económico con producto | 187.500 (aproximadamente 188.000) | 96.000-279.000 |

Las cuentas extienden rangos de diseño sin cotizar, no gastos reales:[^precios][^costo-rol]

- Infraestructura base: 1.500-4.000 USD/mes × 12 = 18.000-48.000,
  centro 33.000. Pasarela: 500-2.000 × 12 = 6.000-24.000, centro 15.000.
  Suma de caja base: 24.000-72.000, centro 48.000.
- Incremento de infraestructura del producto: 500-2.000 × 12 = 6.000-24.000,
  centro 15.000. Consumo: 1.000-4.000 × 12 = 12.000-48.000, centro 30.000.
  Suma adicional: 18.000-72.000, centro 45.000.
- Mantenimiento: 1,5 × 160 × 12 = 2.880 h; a 3.000-7.500 USD/mes por FTE,
  1,5 × 12 × ese rango = 54.000-135.000, centro 94.500. Su suficiencia
  operativa no está validada.

Los totales centrales usan valores sin redondear: 48.000 + 94.500 = 142.500;
con producto, 142.500 + 45.000 = 187.500. Los rangos suman extremos de
componentes; no representan una probabilidad de ocurrencia.

## Equilibrio económico ilustrativo

La cohorte central supuesta de 17,5 personas a 4.750 USD/mes representa
997.500 USD anuales de costo cargado (`B = 17,5 × 4.750 × 12`).[^cohorte]
Con output fijo, la capacidad liberada valorizada es `B × g / (1 + g)`;
igualarla al costo anual modelado `C` requiere `g = C / (B − C)`, si `C < B`.[^rampa][^finanzas]

- Sin producto: 142.500 / (997.500 − 142.500) = 16,6667%, aproximadamente
  16,7% de throughput atribuible.
- Con producto: 187.500 / (997.500 − 187.500) = 23,1481%, aproximadamente
  23,1% de throughput atribuible.

Es equilibrio de costos modelados contra capacidad valorizada, no ahorro de
caja demostrado. No recupera la inversión del año 1 ni demuestra payback.
Se separan los costos del producto sin presumir ingresos que los paguen.[^finanzas]

# Por qué es razonable

- La caja extiende a régimen los costos mensuales de los meses 10-12 de
  [precios externos](/supuestos/precios-externos-sin-cotizar.md), con la
  infraestructura de los meses 10-12 sin piloto al nivel de los meses 4-6,
  como la propone el Anexo B.[^precios][^arquitectura]
- El mantenimiento usa el rango senior del [costo por rol](/supuestos/costo-cargado-por-rol.md)
  como hipótesis de cálculo, sin demostrar suficiencia de 1,5 FTE.[^costo-rol]

# Qué lo invalidaría

- Un cambio del esquema de precios de los modelos hacia el consumo (ver
  [precio y dependencia de modelos](/supuestos/precio-y-dependencia-de-modelos.md)).
- Que el plan termine el año con más componentes en producción que los previstos.

# Cautelas

- Es un escenario ilustrativo conservado en el Anexo E, no un presupuesto
  integral del año 2. Requiere validar alcance operativo, capacidad y costos
  antes de presupuestar; no acredita cobertura integral de las obligaciones.
- El incremento del piloto corresponde al frente producto, separado de la
  infraestructura base; no se incorpora al mínimo por verificar esta ficha.
- El año 2 no se financia por defecto: el mínimo termina en M12 sin régimen
  posterior y el paquete completo no se pide. Un régimen 2028 lo decide y lo
  costea el Directorio en el cierre del mes 12, con dictamen del AI Council y
  cifras verificadas por el CFO; sin esa resolución no se ejecuta
  (R-28, R-32)[^resoluciones].
- La declaración humana revisa los supuestos y las cuentas, sin acreditar
  beneficios, disponibilidad, contratación ni autorización empresarial.

[^finanzas]: Anexo E, "Año 2, fuera del alcance e ilustrativo": escenario del paquete completo y equilibrio anual, distinto de ahorro de caja, ROI o payback y sin recuperar la inversión del año 1.
[^arquitectura]: Anexo B, infraestructura sin piloto al nivel supuesto de M4-M6 y separación del incremento del frente producto.
[^precios]: Precios externos sin cotizar, rangos mensuales supuestos de infraestructura, pasarela, incremento del piloto y consumo de modelos.
[^costo-rol]: Costo senior supuesto de 3.000-7.500 USD/mes por FTE, con 160 h mensuales para costear tiempo.
[^cohorte]: Desarrolladores en equipos propios, supuestos de 15-20 personas y costo de 2.500-7.000 USD/mes, centros 17,5 y 4.750.
[^rampa]: Rampa de la ganancia, conversión a output fijo: un aumento de throughput `g` libera la fracción `g / (1 + g)` del tiempo; el anexo E usa esa conversión para el equilibrio económico, sin demostrar ahorro de caja.
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
