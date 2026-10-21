---
type: Supuesto
title: "Número de personas clave del sobre de capacidad"
description: "El sobre de 1 a 2,25 FTE de tiempo clave supone 10 a 15 personas de arquitectura, IA aplicada, plataforma, gobierno y liderazgo; su disponibilidad real requiere validación por rol y dedicación."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Supuesto de diseño confirmado por Martín: 10-15 personas clave con dedicación de 10%-15%, equivalentes a extremos de 1 y 2,25 FTE, sujetos a disponibilidad real por rol. Incluye actualizar la referencia a capacidad de inversión, retirar la inferencia incorrecta de que menos de diez personas impide alcanzar 1 FTE y limitar los pisos de 1,6-1,8 FTE a las alternativas del paquete completo, sin trasladarlos al alcance mínimo. La separación del tiempo distribuido se revisa en su propia ficha. Confirmado en esta conversación."
tags: [supuesto, finanzas, capacidad]
sources:
  - id: capacidad-inversion
    resource: "context/supuestos/capacidad-de-inversion.md"
    title: "Sobre propuesto de caja y tiempo clave, sujeto a validación"
  - id: tamano-estructura
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Dotación y roles de la organización al corte de septiembre de 2026"
  - id: capacidad-paquete-completo
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, capacidad del paquete completo y advertencia de no trasladar sus pisos al mínimo"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

El [supuesto de capacidad](/supuestos/capacidad-de-inversion.md) propone un
grupo de **10 a 15 personas clave** con dedicación de 10%-15% de su tiempo.
Esta ficha explicita su conversión a FTE:[^capacidad-inversion]

| Extremo | Cuenta | FTE clave |
|---|---|---|
| Inferior | 10 personas × 10% | 1,0 |
| Superior | 15 personas × 15% | 2,25 |

El grupo son los roles que sostienen la base común y el programa: arquitectura,
plataforma y DevOps, IA aplicada, gobierno y seguridad, y liderazgo del programa.
La propuesta de separar las horas de capacitación y de ejercicios de mesa se
revisa en la ficha de [sobres separados](/supuestos/sobre-de-capacidad-separado.md).

# Por qué es razonable

- Es un grupo acotado dentro de una dotación de 60 a 70 personas (ver
  [tamaño y estructura](/hechos/tamano-y-estructura.md)), sin contratación
  masiva.[^tamano-estructura]
- La estimación permite expresar el sobre en FTE; su disponibilidad requiere
  contrastar las dedicaciones efectivamente liberables por rol.

**El rango es un supuesto de diseño.** La cantidad de personas y su dedicación
se contrastan con la nómina y la asignación de trabajo antes de liberar horas.

# Qué lo invalidaría

- Que la suma de dedicaciones efectivamente liberadas por rol no cubra el
  requerimiento del alcance seleccionado.
- Que el presupuesto 2027 o la carga de proyectos de clientes reduzcan el
  porcentaje liberable por debajo del 10%.

# Cómo verificarlo

Quien tiene acceso a la nómina y a la asignación 2027 cuenta, en `private/`, las
personas con esos roles y su porcentaje liberable. Antes de liberar el trabajo,
se confirman el número y el piso requerido por el alcance seleccionado, sin
publicar el dato.

# Cautelas

- El rango requiere validación y aprobación de capacidad por parte de la
  organización.
- Los pisos de 1,6-1,8 FTE citados en las alternativas del paquete completo se
  conservan como referencias de ese alcance; no se trasladan al mínimo, como
  advierte el Anexo E.[^capacidad-paquete-completo]
- Menos de diez personas puede superar 1 FTE según su dedicación: por ejemplo,
  9 personas al 15% equivalen a 1,35 FTE. La disponibilidad se evalúa por rol.
- Un número de personas más alto no crea horas por sí solo: lo que cuenta es el
  tiempo realmente liberado y el trabajo que se desplaza.

[^capacidad-inversion]: Capacidad de inversión para el plan de IA, supuesto de 10%-15% del tiempo de 10-15 personas clave.
[^tamano-estructura]: Tamaño y estructura de la organización, dotación de septiembre de 2026 y límites del dimensionamiento.
[^capacidad-paquete-completo]: Anexo E, sección "Capacidad del paquete completo: piso clave y total interno"; advierte no trasladar los pisos al mínimo.
