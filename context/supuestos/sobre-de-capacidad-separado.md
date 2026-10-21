---
type: Supuesto
title: "Sobre de capacidad separado en tiempo clave y distribuido"
description: "Propuesta de separar el tiempo clave de 1 a 2,25 FTE y las horas distribuidas en la dotación, con aprobación organizacional y conciliación de la capacidad real por alcance."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-21
  scope: "Revalidación registrada por instrucción expresa de Martín en la sesión del 21/10/2026 sobre el contenido vigente del PR #52. Separación de tiempo clave de 1-2,25 FTE y tiempo distribuido de capacitación y ejercicios. R-05 exige a Operaciones y managers conciliar agendas y capacidad por persona antes de la segunda liberación; sin encaje se reduce o resecuencia con recosteo y no se libera M1-M3. Cada alcance conserva su propia cuenta y los alcances ampliados requieren autorización separada. Se mantiene como Supuesto de diseño: esta declaración no acredita mediciones, contratos, disponibilidad ni ejecución de decisiones futuras."
tags: [supuesto, finanzas, capacidad, propuesta]
sources:
  - id: capacidad-inversion
    resource: "context/supuestos/capacidad-de-inversion.md"
    title: "Sobre de caja y tiempo propuesto, sujeto a validación"
  - id: personas-clave
    resource: "context/supuestos/personas-clave-del-sobre.md"
    title: "Conversión del grupo propuesto a 1-2,25 FTE y límites por alcance"
  - id: capacidad-utilizacion
    resource: "context/hechos/capacidad-y-utilizacion.md"
    title: "Utilización facturable y competencia por horas del equipo"
  - id: poblaciones-capacitacion
    resource: "context/supuestos/poblaciones-de-capacitacion.md"
    title: "Supuestos de poblaciones y dedicaciones de formación y champions"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

El sobre de la [capacidad de inversión](/supuestos/capacidad-de-inversion.md)
(10-15% del tiempo de 10-15 personas clave, de 1 a 2,25 FTE; el número de personas es
un [supuesto aparte](/supuestos/personas-clave-del-sobre.md)) se propone leer
**separado**:[^capacidad-inversion][^personas-clave]

| Sobre | Qué cuenta | Quién lo aprueba |
|---|---|---|
| Tiempo clave | Fracciones de arquitectura, IA aplicada, plataforma, gobierno y liderazgo del programa | La organización, previa validación de las dedicaciones por rol |
| Tiempo distribuido | Horas de capacitación básica, intermedia y avanzada, de champions y de los ejercicios de mesa de incidentes (2 × 8 personas × 3 h = 48 horas-persona al año), repartidas en la dotación (ver [poblaciones](/supuestos/poblaciones-de-capacitacion.md))[^poblaciones-capacitacion] | El board, mediante autorización explícita del sobre distribuido |

La alternativa es la lectura **estricta**: todo cuenta contra 1-2,25 FTE.

Regla de clasificación: las pruebas de *bypass*, el red team interno y el Council
cuentan como tiempo clave; los ejercicios de mesa de incidentes y toda la
capacitación, como distribuido, aunque participe alguna persona clave.

# Por qué es razonable

- El supuesto de capacidad habla de un grupo acotado de personas clave y no
  dice nada de las horas repartidas en toda la dotación.
- Distinguir actividades clave y distribuidas permite dimensionar cada bolsa
  por alcance y contrastarlas con las agendas reales, incluidas las personas
  que participan en ambas.

# Qué lo invalidaría

- Que el board no apruebe el sobre distribuido: rige la lectura estricta y se
  recalcula la viabilidad del alcance seleccionado.
- Que las horas distribuidas bajen la utilización facturable por debajo de la
  meta (ver [capacidad y utilización](/hechos/capacidad-y-utilizacion.md)).[^capacidad-utilizacion]
- Que las dedicaciones liberables por rol sean insuficientes para el alcance
  seleccionado, considerando las horas de ambas bolsas.

# Cautelas

- **Para el paquete mínimo rige la lectura separada**, adoptada por el
  Directorio: la reserva de soporte clave (hasta 720 h) y la de formación
  (540-660 h) se confirman por separado en la segunda liberación, antes de M1,
  que firma el CEO con verificación del CFO. Sin agendas confirmadas, se reduce
  o resecuencia con recosteo y no se libera M1-M3 (R-05)[^resoluciones]. En otros alcances, la
  lectura se decide con ese alcance.
- Leerlo separado no agranda la capacidad real: las horas igual salen de horas
  facturables. Solo hace visible un segundo sobre que hay que aprobar.
- Cada alcance usa su propio cálculo de horas y requerimientos; no se trasladan
  las horas por persona ni los pisos de capacidad de otras alternativas.
- La conciliación por persona y semana debe evitar contar las mismas horas en
  ambas bolsas y confirmar el trabajo que se desplaza.

[^capacidad-inversion]: Capacidad de inversión para el plan de IA, sobre de caja y tiempo sujeto a validación presupuestaria y de capacidad.
[^personas-clave]: Número de personas clave del sobre de capacidad, extremos de 1 y 2,25 FTE y validación por rol.
[^capacidad-utilizacion]: Capacidad, utilización y bench, utilización facturable y restricciones del proyecto de adopción.
[^poblaciones-capacitacion]: Poblaciones y horas de capacitación por nivel, supuestos de diseño de formación y champions.
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
