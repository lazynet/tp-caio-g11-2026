---
type: Supuesto
title: "Convenciones de calendario y de cálculo del plan"
description: "El plan usa una preparación previa en octubre-diciembre de 2026, cuatro tramos de tres meses en 2027 (meses 1-3 a 10-12) con revisión mensual del Council, la base de atribución congelada en las semanas 1-4 del plan, 480 horas de costeo por persona y tramo, costo horario = costo mensual del rol / 160 y techos redondeados hacia arriba."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Convenciones de diseño confirmadas por Martín: preparación 2026 de 10 días hábiles con autorización propia, caja 0 y techo de tiempo 8 mil USD; cuatro tramos de 2027 con segunda autorización para M1 y liberaciones presupuestarias separadas de la revisión mensual del Council; base prospectiva semanas 1-4 y retrospectiva sin atribución cuando corresponda; puente multiplicativo entre OKR y base del plan; costeo de 160 horas mensuales, 480 por tramo y 1.920 anuales; costo por rol, redondeos y moneda. Se precisa que las horas son convenciones del modelo y el gate de M3 depende del alcance; el acuerdo del equipo y la autorización empresarial siguen sin acreditar. Confirmado en esta conversación."
tags: [supuesto, convención, finanzas]
sources:
  - id: paquete-minimo
    resource: "context/supuestos/paquete-minimo-de-aprendizaje.md"
    title: "Propuesta de validación inicial y autorizaciones del paquete mínimo"
  - id: okr-organizacion
    resource: "context/hechos/okrs-y-objetivos.md"
    title: "Borrador de OKR 2027 y base del cuarto trimestre de 2026"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Rangos de planificación de costo mensual por rol"
  - id: arquitectura-medicion
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, protocolo de medición y criterio de respaldo"
  - id: roadmap
    resource: "plan/annexes/06-roadmap-riesgo.md"
    title: "Anexo F, secuencia de autorizaciones y línea de base"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

| Convención | Valor |
|---|---|
| Preparación previa | Octubre-diciembre de 2026: validación inicial de 10 días hábiles desde autorización específica, con agendas, trabajo desplazado e imputación 2026 confirmados antes de trabajar. Caja 0 / tiempo hasta 8 mil USD (organizativo 5 + técnico 3); no consta ejecución. La retrospectiva estima tendencia y ruido, sin formación, prácticas, herramientas nuevas, despliegues ni contratos nuevos |
| Tramos del plan | Meses 1-3 (enero-marzo de 2027), meses 4-6 (abril-junio), meses 7-9 (julio-septiembre) y meses 10-12 (octubre-diciembre). Cada tramo tiene su techo y termina en una decisión: revisión técnica del alcance seleccionado en el mes 3, impacto de los meses 6 y 9 y cierre del mes 12. La validación previa tiene autorización propia; M1-M3 requiere una segunda, sin liberar ambos tramos a la vez |
| Revisión mensual | El AI Council revisa cada mes el tablero: puede frenar, cortar o escalar una señal, pero no libera fondos. Las autoridades presupuestarias correspondientes autorizan la preparación 2026 y el inicio M1-M3; las siguientes liberaciones son en los meses 3, 6, 9 y 12 |
| Arranque del mes 1 | Con presupuesto 2027 aprobado y segunda autorización, condicionada a diagnóstico/padrón, matriz de capacidad, autoridades, viabilidad técnica/de medición y recosteo aceptados. Libera base y controles con herramientas existentes; no habilita prácticas automáticamente |
| Línea de base de atribución | Base prospectiva congelada en las semanas 1-4 del plan, antes de cualquier formación o herramienta nueva. La atribución no cambia de base. En la semana 4 la oficina del CAIO aplica un criterio fijado antes de M1 en la segunda autorización, con datos de la base (semiancho placebo proyectado > 3 puntos con N ≥ 15; Anexo B, "Respaldo"): si se cumple, la serie retrospectiva de la preparación previa se usa solo como lectura contra tendencia, sin atribuir ganancia ni liberar capital, y se deja constancia[^arquitectura-medicion] |
| Comparación con el OKR | El OKR de throughput se mide contra el cuarto trimestre de 2026: se informa al lado, contra la serie de la preparación previa, sin atribuir ganancia. Para compararlo con una exigencia medida contra la base del plan se usa el puente (1 + meta contra el cuarto trimestre de 2026) = (1 + d) × (1 + ganancia contra la base), donde d es la mejora del cuarto trimestre de 2026 a la base del plan; sin d medido, las dos cifras no se restan |
| Jornada de costeo (convención del modelo) | 160 horas por mes, 1.920 horas por año por persona |
| Persona-tramo | 480 horas de costeo por tramo de tres meses (160 × 3). Con ellas se pasa de horas a FTE. Las 520 horas de 13 semanas × 40 h son calendario bruto, sin descontar feriados ni licencias, y no se usan para FTE ni para costo |
| Costo horario | Costo mensual del rol que hace la actividad ([costo por rol](/supuestos/costo-cargado-por-rol.md)) dividido 160[^costo-rol] |
| Redondeo | Medios, rangos y pérdidas estimadas, al entero más cercano. Techos y reservas que se autorizan, al entero superior del máximo calculado |
| Moneda | USD; los montos del plan son rangos |

# Por qué es razonable

- El presupuesto 2027 y el hito previo habilitan M1-M3; la preparación requiere
  autorización específica de tiempo imputado a 2026, sin caja nueva. La base
  prospectiva conserva la unidad de los gates y las semanas 1-4 de M1.[^paquete-minimo][^roadmap]
- El borrador de OKR fija su meta contra el cuarto trimestre de 2026
  (ver [OKR](/hechos/okrs-y-objetivos.md)): por eso la preparación previa sigue siendo la
  referencia del OKR, aunque no la de atribución.[^okr-organizacion]
- Se adoptan 160 horas mensuales como convención de planificación para pasar
  de costo mensual a horario y convertir horas a FTE.
- Redondear los techos hacia arriba evita que una autorización quede por debajo
  del máximo que se calculó con los mismos supuestos.

# Qué lo invalidaría

- Que no se autoricen agendas, trabajo desplazado e imputación 2026: no se
  inicia la validación y se vuelve a decidir calendario y costo.
- Que el presupuesto 2027 se apruebe tarde: el mes 1 se corre y el plan pierde
  meses dentro de 2027.
- Que la empresa use otra jornada de referencia para costear horas.
- Que no haya historial suficiente para la serie de la preparación previa ni para la base
  prospectiva: la ganancia no se atribuye.

# Cautelas

- La validación previa es una elección de Martín para el plan; el acuerdo del
  equipo y la autorización empresarial siguen sin acreditar. La verificación de
  esta ficha registra las convenciones de diseño con ese alcance.
  Alcance y costos: [paquete mínimo](/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial).
- El costo horario es **costo, no tarifa facturable**. Se calcula por rol y no
  como promedio de la empresa: un promedio multiplicado por las horas de toda la
  dotación acercaría la nómina, que no se publica.
- La secuencia de la línea de base se define en el Anexo F y esta ficha la
  registra como convención de diseño.[^roadmap]

[^paquete-minimo]: Paquete mínimo de aprendizaje sin plataforma central, validación inicial y segunda autorización antes de M1.
[^okr-organizacion]: OKR y objetivos de la organización y de Tecnología, borrador 2027 y referencia del cuarto trimestre de 2026.
[^costo-rol]: Costo mensual cargado por rol, rangos supuestos de planificación.
[^arquitectura-medicion]: Anexo B, protocolo de medición y apartado "Respaldo", criterio predefinido de precisión de la base.
[^roadmap]: Anexo F, secuencia de autorizaciones y línea de base prospectiva.
