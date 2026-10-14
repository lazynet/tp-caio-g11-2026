---
type: Supuesto
title: "Alternativas de menor alcance y prueba chica de T1"
description: "Para comparar el paquete con opciones más baratas, Finanzas supone la composición y el costo de gobierno mínimo más formación, de un piloto acotado sobre el agente de código actual y de la prueba chica desde la semana 5 de T1, con la misma medición en las tres."
status: draft
tags: [supuesto, finanzas, alternativas]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T20:00:00Z }
---
# Supuesto

Las tres opciones usan la **misma medición**, para que su señal de valor sea
comparable: la serie de T0, la base prospectiva congelada en las semanas 1-4 de
T1 con la unidad del anexo B, telemetría de las herramientas actuales (0,5-1,5
mil USD de caja por trimestre, el nivel de T1-b del anexo B) y 0,2 FTE de
DevOps/QA durante 12 meses para contar y leer los intervalos.

| Componente | (b) Gobierno mínimo y formación | (c) Piloto sobre el agente actual | Prueba chica de T1, dentro del paquete |
|---|---|---|---|
| Gobierno | Capa M del anexo C completa (incluye legal externo) | Solo la matriz de clientes; la política vigente, sin legal | La del paquete |
| Formación | La del anexo D completa (básico, intermedio, avanzado, champions, líder del programa) | Intermedio de la cohorte (~17,5 × 12 h) y 2 champions de Tecnología al 10% durante 12 meses | Usa el intermedio de Tecnología de T1 como vehículo: no suma horas de la cohorte |
| Prácticas sobre el agente de código | Las que traiga la formación | Contrato de agente, skills y guía de revisión: 40-80 h de tech lead | Las mismas 40-80 h, más 2 champions al 10% durante 2 meses (64 h) y 16-24 h de lectura de DevOps/QA al cierre de T1 |
| Plataforma, contractor, pasarela, capa D | No | No | No suma: son del paquete |

Los costos por hora salen del [costo por rol](/supuestos/costo-cargado-por-rol.md)
sobre 160 h por mes, y las horas de la cohorte, del costo por desarrollador de
[N y costo](/supuestos/desarrolladores-en-equipos-propios.md).

El piloto (c) trabaja solo sobre repositorios que la matriz habilite: sin datos de
clientes ([disponibilidad de datos](/supuestos/disponibilidad-de-datos.md)).

# Por qué es razonable

- El agente de código ya está pagado y en uso en Tecnología (ver
  [uso de IA](/hechos/uso-ia-interno.md)); ninguna opción suma seats.
- La [ganancia de productividad](/supuestos/ganancia-de-productividad.md) se
  atribuye al uso sistemático del agente "con contrato de agente, skills y
  compuertas de calidad": es la palanca que (c) toma directamente.
- Las piezas de (b) son renglones que los anexos C y D ya costean; acá solo se
  arman de otra forma.

# Qué lo invalidaría

- Que medir sin el esfuerzo técnico del anexo B cueste bastante más que 0,2 FTE
  (por ejemplo, si el historial de PR no alcanza y hay que instrumentarlo).
- Que la matriz no habilite repositorios suficientes para una cohorte de 15
  personas activas: (c) y la prueba chica se achican o no arrancan.
- Que el intermedio de Tecnología no pueda usarse como vehículo de la prueba y
  las horas de la cohorte se sumen.

# Cautelas

- No hay dato de qué fracción de la ganancia se logra sin la plataforma: el
  anexo E la trata como variable de sensibilidad (0 a 1), sin valor puntual.
- Los montos están en el anexo E; esta ficha fija la composición.
- Las 40-80 h de diseño y las 16-24 h de lectura son supuestos del equipo, sin
  dato.
