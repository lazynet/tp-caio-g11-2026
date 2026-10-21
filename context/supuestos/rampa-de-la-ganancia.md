---
type: Supuesto
title: "Rampa de la ganancia de productividad"
description: "La ganancia de throughput llega por tramos: en el escenario base, 0% del objetivo en los meses 1-3, 25% en los meses 4-6, 60% en los meses 7-9 y 100% en los meses 10-12; en el pesimista 0/10/30/60% y en el optimista 0/40/80/100%."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Rampas de diseño confirmadas por Martín: base 0/25/60/100%, pesimista 0/10/30/60% y optimista 0/40/80/100% del objetivo de throughput por tramo. Incluye mejora modelada g por rampa y capacidad liberada a producción fija g por rampa dividido por uno más esa mejora; caso pesimista con objetivo 5% y espera o eventual corte según medición y gates. Se precisa que el 0% inicial es una convención de planificación, que la trayectoria temporal sigue siendo un supuesto y que los gates contrastan el modelo con mediciones reales. Confirmado en esta conversación."
tags: [supuesto, finanzas, productividad]
sources:
  - id: ganancia-productividad
    resource: "context/supuestos/ganancia-de-productividad.md"
    title: "Hipótesis de mejora de throughput y condiciones de medición"
  - id: uso-ia
    resource: "context/hechos/uso-ia-interno.md"
    title: "Adopción observada por área y límites de la telemetría"
  - id: pilotos-ia
    resource: "context/hechos/encuesta-y-pilotos-ia.md"
    title: "Experiencia de delivery limitada a la primera semana"
  - id: convenciones-calculo
    resource: "context/supuestos/convenciones-de-calculo.md"
    title: "Línea de base prospectiva y convenciones de costeo"
  - id: escenarios-financieros
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, rampas y objetivos modelados por escenario"
  - id: umbrales-tecnicos
    resource: "context/supuestos/umbrales-tecnicos-propuestos.md"
    title: "Gates de impacto, espera y condiciones de corte"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

| Escenario | Meses 1-3 | Meses 4-6 | Meses 7-9 | Meses 10-12 |
|---|---|---|---|---|
| Base | 0% | 25% | 60% | 100% |
| Pesimista | 0% | 10% | 30% | 60% |
| Optimista | 0% | 40% | 80% | 100% |

El porcentaje es la fracción del objetivo de throughput de la
[ganancia de productividad](/supuestos/ganancia-de-productividad.md) que se
modela en cada tramo de tres meses.[^ganancia-productividad]

Con un objetivo g, la mejora modelada del tramo t es g × rampa_t. Los gates
contrastan esa mejora con mediciones reales.[^umbrales-tecnicos]

Si se valúa como horas evitadas a output fijo, la fracción liberada es
g × rampa_t / (1 + g × rampa_t); la rampa no se aplica sobre horas ya
convertidas.

# Por qué es razonable

- Se asigna 0% de ganancia modelada a los meses 1-3 como convención de
  planificación para medición y formación, sin anticipar beneficios del tramo.
- La telemetría muestra diferencias de adopción por área (ver
  [uso de IA](/hechos/uso-ia-interno.md)); la trayectoria temporal propuesta
  sigue siendo un supuesto.[^uso-ia]
- El piloto de delivery aporta una experiencia limitada a su primera semana
  (ver [pilotos](/hechos/encuesta-y-pilotos-ia.md)), sin acreditar estas rampas.[^pilotos-ia]

# Qué lo invalidaría

- Que la medición de los meses 4-6 no muestre ganancia contra la línea de base
  congelada en las semanas 1-4 del plan (ver
  [convenciones](/supuestos/convenciones-de-calculo.md)).[^convenciones-calculo]
- Que la ganancia aparezca pero se pague con más incidentes o retrabajo.

# Cautelas

- Las rampas y los objetivos son convenciones del modelo del Anexo E. El
  pesimista usa un objetivo de 5%: modela +0,5% en M4-M6, +1,5% en M7-M9 y +3%
  en M10-M12.[^escenarios-financieros]
- Ese caso se trata como espera y eventual corte según las mediciones y los
  gates, incluida la espera de 6 semanas y el corte si vence sin mejora.[^umbrales-tecnicos]
- La unidad de throughput y su valuación las define el Anexo E; la rampa se
  aplica sobre el throughput, no sobre su valuación.

[^ganancia-productividad]: Ganancia de productividad por IA en ingeniería, rango propuesto y validaciones pendientes.
[^uso-ia]: Uso actual de IA en la operación interna, diferencias por área y cautelas de telemetría.
[^pilotos-ia]: Encuesta y pilotos internos de IA, experiencia de delivery limitada a la primera semana y sin extrapolación.
[^convenciones-calculo]: Convenciones de calendario y cálculo, línea de base prospectiva y costeo.
[^escenarios-financieros]: Anexo E, escenarios y sensibilidades del modelo de productividad.
[^umbrales-tecnicos]: Umbrales técnicos propuestos, gates de impacto y reglas de espera y corte.
