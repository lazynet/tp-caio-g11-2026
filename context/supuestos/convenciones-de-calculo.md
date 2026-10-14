---
type: Supuesto
title: "Convenciones de calendario y de cálculo del plan"
description: "El plan usa T0 = cuarto trimestre de 2026, T1-T4 = los trimestres de 2027, la base de atribución congelada en las semanas 1-4 de T1, 480 horas de costeo por persona-trimestre, costo horario = costo mensual del rol / 160 y techos redondeados hacia arriba."
status: draft
tags: [supuesto, convención, finanzas]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T12:00:00Z }
---
# Supuesto

| Convención | Valor |
|---|---|
| T0 | Cuarto trimestre de 2026: antes de que el plan gaste. Se extrae la serie retrospectiva, que estima tendencia y ruido |
| T1 a T4 | Enero-marzo, abril-junio, julio-septiembre y octubre-diciembre de 2027 |
| Arranque de T1 | Con la aprobación del presupuesto 2027 |
| Línea de base de atribución | Base prospectiva congelada en las semanas 1-4 de T1, antes de cualquier formación o herramienta nueva. Si en la semana 4 su dispersión supera la tendencia esperada, la oficina del CAIO puede adoptar la serie retrospectiva de T0, dejando constancia |
| Comparación con el OKR | El OKR de throughput se mide contra el cuarto trimestre de 2026: se informa al lado, contra la serie de T0, sin atribuir ganancia. Para compararlo con una exigencia medida contra la base de T1 se usa el puente (1 + meta contra T0) = (1 + d) × (1 + ganancia contra T1), donde d es la mejora de T0 a la base de T1; sin d medido, las dos cifras no se restan |
| Jornada | 160 horas por mes, 1.920 horas por año por persona |
| Persona-trimestre | 480 horas de costeo (160 × 3). Con ellas se pasa de horas a FTE. Las 520 horas de 13 semanas × 40 h son calendario bruto, sin descontar feriados ni licencias, y no se usan para FTE ni para costo |
| Costo horario | Costo mensual del rol que hace la actividad ([costo por rol](/supuestos/costo-cargado-por-rol.md)) dividido 160 |
| Redondeo | Medios, rangos y pérdidas estimadas, al entero más cercano. Techos y reservas que se autorizan, al entero superior del máximo calculado |
| Moneda | USD; los montos del plan son rangos |

# Por qué es razonable

- El presupuesto 2027 es el primer momento en que el plan puede recibir fondos,
  y la base prospectiva se congela con la misma unidad que después miden los
  gates. El borrador de OKR fija su meta contra el cuarto trimestre de 2026
  (ver [OKR](/hechos/okrs-y-objetivos.md)): por eso T0 sigue siendo la
  referencia del OKR, aunque no la de atribución.
- 160 horas es la convención usual para pasar de costo mensual a horario.
- Redondear los techos hacia arriba evita que una autorización quede por debajo
  del máximo que se calculó con los mismos supuestos.

# Qué lo invalidaría

- Que el presupuesto 2027 se apruebe tarde: T1 se corre y el plan pierde un
  trimestre dentro de 2027.
- Que la empresa use otra jornada de referencia para costear horas.
- Que no haya historial suficiente para la serie de T0 ni para la base
  prospectiva: la ganancia no se atribuye.

# Cautelas

- El costo horario es **costo, no tarifa facturable**. Se calcula por rol y no
  como promedio de la empresa: un promedio multiplicado por las horas de toda la
  dotación acercaría la nómina, que no se publica.
- La secuencia de la línea de base es una decisión del CAIO en el anexo F, que
  esta ficha registra como convención; versiones anteriores ubicaban la base en T0.
