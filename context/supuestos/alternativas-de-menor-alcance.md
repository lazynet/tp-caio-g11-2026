---
type: Supuesto
title: "Alternativas de menor alcance y prueba chica de los meses 1-3"
description: "Para comparar el paquete con opciones más baratas, Finanzas supone la composición y el costo de gobierno mínimo más formación, de un piloto acotado sobre el agente de código actual y de la prueba chica desde la semana 5 del plan, con la misma medición en las tres."
status: draft
tags: [supuesto, finanzas, alternativas]
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-14T22:00:00Z }
---
# Supuesto

Las tres opciones usan la **misma medición**, para que su señal de valor sea
comparable: la serie de la preparación previa, la base prospectiva congelada en las semanas 1-4 del
plan con la unidad del Anexo B, telemetría de las herramientas actuales (0,5-1,5
mil USD de caja por tramo de tres meses, el nivel del primer tramo acotado del Anexo B) y 0,2 FTE de
DevOps/QA durante 12 meses para contar y leer los intervalos.

| Componente | Gobierno mínimo y formación | Piloto sobre el agente de código | Prueba chica de los meses 1-3, dentro del paquete |
|---|---|---|---|
| Gobierno | Los controles de política del Anexo C completos (incluye legal externo) | Solo la matriz de clientes; la política vigente, sin legal | La del paquete |
| Formación | La del Anexo D completa (básico, intermedio, avanzado, champions, líder del programa) | Intermedio de la cohorte (~17,5 × 12 h) y 2 champions de Tecnología al 10% durante 12 meses | Usa el intermedio de Tecnología de los meses 1-3 como vehículo: no suma horas de la cohorte |
| Prácticas sobre el agente de código | Las que traiga la formación | Contrato de agente, skills y guía de revisión: 40-80 h de tech lead | Las mismas 40-80 h, más 2 champions al 10% durante 2 meses (64 h) y 16-24 h de lectura de DevOps/QA al cierre de los meses 1-3 |
| Plataforma, contractor, pasarela, demostración externa | No | No | No suma: son del paquete |

Los costos por hora salen del [costo por rol](/supuestos/costo-cargado-por-rol.md)
sobre 160 h por mes, y las horas de la cohorte, del costo por desarrollador de
[N y costo](/supuestos/desarrolladores-en-equipos-propios.md).

En la rama sin señal en el mes 3 (los meses 4-12 como gobierno mínimo y formación), la prueba chica se extiende a la
cohorte como el piloto acotado **sin costo adicional**: usa los champions y el intermedio de
Tecnología que la formación del gobierno mínimo ya paga, y el diseño ya se hizo en los meses 1-3.

El piloto acotado trabaja solo sobre repositorios que la matriz habilite: sin datos de
clientes ([disponibilidad de datos](/supuestos/disponibilidad-de-datos.md)).

# Por qué es razonable

- El agente de código ya está pagado y en uso en Tecnología (ver
  [uso de IA](/hechos/uso-ia-interno.md)); ninguna opción suma seats.
- La [ganancia de productividad](/supuestos/ganancia-de-productividad.md) se
  atribuye al uso sistemático del agente "con contrato de agente, skills y
  compuertas de calidad": es la palanca que el piloto acotado toma directamente.
- Las piezas del gobierno mínimo y formación son renglones que los Anexos C y D ya costean; acá solo se
  arman de otra forma.

# Qué lo invalidaría

- Que medir sin el esfuerzo técnico del Anexo B cueste bastante más que 0,2 FTE
  (por ejemplo, si el historial de PR no alcanza y hay que instrumentarlo).
- Que la matriz no habilite repositorios suficientes para una cohorte de 15
  personas activas: el piloto acotado y la prueba chica se achican o no arrancan.
- Que el intermedio de Tecnología no pueda usarse como vehículo de la prueba y
  las horas de la cohorte se sumen.
- Que extender la prueba en los meses 4-12 pida champions o lectura por encima de lo que
  el gobierno mínimo y formación ya paga: el año sin señal (≈ 199 en el Anexo E) sube.

# Cautelas

- No hay dato de qué fracción de la ganancia se logra sin la plataforma: el
  Anexo E la trata como variable de sensibilidad (0 a 1), sin valor puntual.
- Los montos están en el Anexo E; esta ficha fija la composición.
- Las 40-80 h de diseño y las 16-24 h de lectura son supuestos del equipo, sin
  dato.
