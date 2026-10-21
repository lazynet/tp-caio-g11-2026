---
type: Supuesto
title: "Ganancia de productividad por IA en ingeniería"
description: "El caso de negocio supone entre 10% y 25% más de throughput por desarrollador al cabo de 12 meses en los equipos propios, no en los equipos asignados a clientes."
status: draft
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Hipótesis de diseño confirmada por Martín: 10%-25% de mejora de throughput por desarrollador a los 12 meses en equipos propios, excluyendo staffing y sin deterioro de calidad. Incluye base prospectiva congelada en semanas 1-4, comparación trimestral con incidentes y retrabajo, serie retrospectiva del cuarto trimestre de 2026 para tendencia y ruido y resultado del OKR informado aparte. Se corrige el fundamento: la meta propuesta de +20% y el piloto de una semana no acreditan el rango ni un piso conservador. Se conserva la validación pendiente de medición y conversión económica. Confirmado en esta conversación."
tags: [supuesto, finanzas, productividad]
sources:
  - id: okr-organizacion
    resource: "context/hechos/okrs-y-objetivos.md"
    title: "Borrador de OKR 2027 y meta propuesta de throughput"
  - id: pilotos-ia
    resource: "context/hechos/encuesta-y-pilotos-ia.md"
    title: "Piloto de delivery y límites de extrapolación de la primera semana"
  - id: convenciones-calculo
    resource: "context/supuestos/convenciones-de-calculo.md"
    title: "Base prospectiva, serie retrospectiva y valuación de la capacidad"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Se aplica a los equipos que trabajan en modo producto, donde la organización
controla las herramientas. En staffing el efecto depende de lo que permita
cada cliente y no se cuenta.

Se modela la hipótesis de que el uso sistemático de agentes de código (con
contrato de agente, skills y compuertas de calidad) eleve entre 10% y 25% el
throughput por desarrollador en 12 meses, sin bajar la calidad.

# Por qué es razonable

- El borrador de OKR 2027 propone +20% como meta; sirve como referencia del
  objetivo de diseño (ver [OKR](/hechos/okrs-y-objetivos.md)).[^okr-organizacion]
- El piloto de delivery aporta una experiencia acotada a su primera semana y
  su fuente advierte que no se puede extrapolar (ver
  [pilotos](/hechos/encuesta-y-pilotos-ia.md)).[^pilotos-ia]
- El rango de 10%-25% se adopta como hipótesis que requiere medición
  prospectiva; esos antecedentes no acreditan la magnitud anual ni permiten
  calificar el piso como conservador.

# Qué lo invalidaría

- Que la línea de base congelada en los meses 1-3 no se mida o resulte inestable. La serie
  retrospectiva del cuarto trimestre de 2026 no la reemplaza: no atribuye
  ganancia y solo da una lectura contra tendencia (ver
  [convenciones](/supuestos/convenciones-de-calculo.md)).[^convenciones-calculo]
- Que la mejora de velocidad se pague con más incidentes o retrabajo.
- Para el caso económico, que el tiempo liberado no se traduzca en margen
  (por ejemplo, en contratos facturados por hora, donde menos horas es menos
  facturación). Esa conversión requiere validar las condiciones comerciales.

# Cómo verificarlo

Congelar la línea de base en las semanas 1-4 del plan y usar la serie retrospectiva
del cuarto trimestre de 2026 solo para estimar tendencia y ruido. Comparar cada
tramo de tres meses contra la base, junto con incidentes y retrabajo.[^convenciones-calculo]

El resultado contra el OKR, que usa el cuarto trimestre de 2026, se informa al
lado.[^okr-organizacion]

# Cautelas

- La mejora técnica y su conversión económica tienen dueños distintos. Mide el
  Responsable de Tecnología con el protocolo del Anexo B; lee el AI Council en
  los meses 6 y 9 contra los umbrales, calidad primero; convierte el CFO: la
  capacidad liberada cuenta como beneficio solo si en el mes 6 hay un destino
  decidido, y se valoriza a costo cargado, no como caja. El mes 3 no atribuye
  ganancia. Sin pasar, rige la espera única o el corte; sin destino en el mes 6,
  el beneficio es 0 (R-19)[^resoluciones].
- El rango sigue siendo una hipótesis hasta esa medición, sujeto a revisión
  por inestabilidad de la base, deterioro de calidad o falta de conversión
  económica para el caso de negocio.

[^okr-organizacion]: OKR y objetivos de la organización y de Tecnología, borrador 2027 y meta propuesta de +20% de throughput.
[^pilotos-ia]: Encuesta y pilotos internos de IA, experiencia de delivery limitada a la primera semana y sin extrapolación.
[^convenciones-calculo]: Convenciones de cálculo del caso de negocio, base prospectiva, lectura retrospectiva y valuación de la capacidad.
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
