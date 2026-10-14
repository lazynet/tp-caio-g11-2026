---
type: Supuesto
title: "Convenciones de calendario y de cálculo del plan"
description: "El plan usa una preparación previa en octubre-diciembre de 2026, cuatro tramos de tres meses en 2027 (meses 1-3 a 10-12) con revisión mensual del Council, la base de atribución congelada en las semanas 1-4 del plan, 480 horas de costeo por persona y tramo, costo horario = costo mensual del rol / 160 y techos redondeados hacia arriba."
status: draft
tags: [supuesto, convención, finanzas]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T14:00:00Z }
---
# Supuesto

| Convención | Valor |
|---|---|
| Preparación previa | Octubre-diciembre de 2026: antes de que el plan gaste. Se extrae la serie retrospectiva, que estima tendencia y ruido |
| Tramos del plan | Meses 1-3 (enero-marzo de 2027), meses 4-6 (abril-junio), meses 7-9 (julio-septiembre) y meses 10-12 (octubre-diciembre). Cada tramo tiene su techo de fondos y termina en una decisión: la de plataforma del mes 3, las lecturas de impacto de los meses 6 y 9 y el cierre del mes 12. La decisión inicial es la aprobación de hoy |
| Revisión mensual | El AI Council revisa cada mes el tablero: puede frenar, cortar o escalar una señal, pero no libera fondos; los fondos se liberan solo en los meses 3, 6, 9 y 12 |
| Arranque del mes 1 | Con la aprobación del presupuesto 2027 |
| Línea de base de atribución | Base prospectiva congelada en las semanas 1-4 del plan, antes de cualquier formación o herramienta nueva. La atribución no cambia de base. En la semana 4 la oficina del CAIO aplica un criterio fijado en la aprobación de hoy con datos de la base (semiancho placebo proyectado > 3 puntos con N ≥ 15; Anexo B, "Respaldo"): si se cumple, la serie retrospectiva de la preparación previa se usa solo como lectura contra tendencia, sin atribuir ganancia ni liberar capital, y se deja constancia |
| Comparación con el OKR | El OKR de throughput se mide contra el cuarto trimestre de 2026: se informa al lado, contra la serie de la preparación previa, sin atribuir ganancia. Para compararlo con una exigencia medida contra la base del plan se usa el puente (1 + meta contra el cuarto trimestre de 2026) = (1 + d) × (1 + ganancia contra la base), donde d es la mejora del cuarto trimestre de 2026 a la base del plan; sin d medido, las dos cifras no se restan |
| Jornada | 160 horas por mes, 1.920 horas por año por persona |
| Persona-tramo | 480 horas de costeo por tramo de tres meses (160 × 3). Con ellas se pasa de horas a FTE. Las 520 horas de 13 semanas × 40 h son calendario bruto, sin descontar feriados ni licencias, y no se usan para FTE ni para costo |
| Costo horario | Costo mensual del rol que hace la actividad ([costo por rol](/supuestos/costo-cargado-por-rol.md)) dividido 160 |
| Redondeo | Medios, rangos y pérdidas estimadas, al entero más cercano. Techos y reservas que se autorizan, al entero superior del máximo calculado |
| Moneda | USD; los montos del plan son rangos |

# Por qué es razonable

- El presupuesto 2027 es el primer momento en que el plan puede recibir fondos,
  y la base prospectiva se congela con la misma unidad que después miden los
  gates. El borrador de OKR fija su meta contra el cuarto trimestre de 2026
  (ver [OKR](/hechos/okrs-y-objetivos.md)): por eso la preparación previa sigue siendo la
  referencia del OKR, aunque no la de atribución.
- 160 horas es la convención usual para pasar de costo mensual a horario.
- Redondear los techos hacia arriba evita que una autorización quede por debajo
  del máximo que se calculó con los mismos supuestos.

# Qué lo invalidaría

- Que el presupuesto 2027 se apruebe tarde: el mes 1 se corre y el plan pierde
  meses dentro de 2027.
- Que la empresa use otra jornada de referencia para costear horas.
- Que no haya historial suficiente para la serie de la preparación previa ni para la base
  prospectiva: la ganancia no se atribuye.

# Cautelas

- El costo horario es **costo, no tarifa facturable**. Se calcula por rol y no
  como promedio de la empresa: un promedio multiplicado por las horas de toda la
  dotación acercaría la nómina, que no se publica.
- La secuencia de la línea de base es una decisión del CAIO en el anexo F, que
  esta ficha registra como convención; versiones anteriores ubicaban la base en la preparación previa.
