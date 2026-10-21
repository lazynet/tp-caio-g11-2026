---
type: Supuesto
title: "Capacidad de inversión para el plan de IA"
description: "El plan propone un sobre de caja incremental de 1%-3% de la facturación anual y una reasignación de 10%-15% del tiempo de un grupo de personas clave, sujetos a validación presupuestaria y de capacidad."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Supuesto de diseño confirmado por Martín: caja incremental de 1%-3% de la facturación anual y 10%-15% del tiempo de 10-15 personas clave, sujetos a validación presupuestaria. Incluye corregir EBITDA a 21%-30%, retirar las afirmaciones no acreditadas de caja disponible y de que el gasto adicional no desestabiliza, distinguir gastos externos como caja y capacitación interna como tiempo, y conservar la restricción de no contratar del proyecto de adopción, con excepciones sujetas a autorización. Confirmado en esta conversación."
tags: [supuesto, finanzas]
sources:
  - id: situacion-economica
    resource: "context/hechos/situacion-economica.md"
    title: "Rentabilidad y margen EBITDA mensual al cierre de agosto de 2026"
  - id: costos-tecnologia
    resource: "context/hechos/costos-tecnologia-e-ia.md"
    title: "Peso del gasto tecnológico sobre facturación al corte de agosto de 2026"
  - id: capacidad-utilizacion
    resource: "context/hechos/capacidad-y-utilizacion.md"
    title: "Restricción de contratación y dedicación propuesta a certificación"
  - id: personas-clave
    resource: "context/supuestos/personas-clave-del-sobre.md"
    title: "Supuesto del número de personas clave del sobre de capacidad"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Como techo de diseño para los 12 meses, se propone una caja incremental en IA
de entre 1% y 3% de la facturación anual: licencias, consumo de modelos,
capacitación externa y perfiles especializados sujetos a autorización.

Se agrega la reasignación de 10% a 15% del tiempo de un grupo acotado de
personas clave, supuesto entre 10 y 15 (ver
[personas clave del sobre](/supuestos/personas-clave-del-sobre.md)).[^personas-clave]
La capacitación interna se cuenta como tiempo reasignado; los gastos externos,
como caja. No se propone contratación masiva.

# Por qué es razonable

- La empresa presenta un margen EBITDA mensual de 21%-30% entre enero y agosto
  de 2026 (ver [situación económica](/hechos/situacion-economica.md)). La
  liquidez disponible requiere una validación propia.[^situacion-economica]
- El gasto de tecnología, nube incluida, ronda el 4% de la facturación al corte
  de agosto. El 1%-3% adicional propuesto es material y requiere evaluar su
  impacto presupuestario (ver [costos](/hechos/costos-tecnologia-e-ia.md)).[^costos-tecnologia]
- La restricción del proyecto de adopción es no contratar y potenciar al equipo
  actual. Su propuesta de capacitación contempla 10%-15% del tiempo durante la
  certificación (ver [capacidad](/hechos/capacidad-y-utilizacion.md)).[^capacidad-utilizacion]
  La disponibilidad del tiempo por rol se valida para el alcance del plan.

# Qué lo invalidaría

- Que el Directorio priorice otras inversiones, como los productos propios.
- La pérdida de un cliente relevante.
- Que el presupuesto 2027 fije un techo de costo de tecnología más bajo.

# Cómo verificarlo

Contrastar los rangos con el presupuesto 2027, la liquidez disponible, las
prioridades del Directorio y el tiempo efectivamente liberable por rol.

# Cautelas

- Los rangos son techos de diseño sujetos a validación y aprobación
  presupuestaria; no acreditan caja ni agendas disponibles.
- Se conserva la restricción de no contratar del proyecto de adopción.
  Cualquier excepción para perfiles especializados requiere autorización expresa.
- El número de personas clave se revisa en su propia ficha y se contrasta con
  la disponibilidad real.

[^situacion-economica]: Situación económica 2026, rango EBITDA mensual al cierre de agosto.
[^costos-tecnologia]: Costos de tecnología e IA, ratio sobre facturación al corte de agosto de 2026.
[^capacidad-utilizacion]: Capacidad, utilización y bench, restricción del proyecto de adopción y propuesta de certificación.
[^personas-clave]: Número de personas clave del sobre de capacidad, supuesto de diseño a validar.
