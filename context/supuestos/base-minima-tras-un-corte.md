---
type: Supuesto
title: "Base mínima que queda después de un corte"
description: "Continuidad propuesta tras un corte, diferenciando el núcleo restringido del mínimo, el gobierno del paquete completo y la base del producto activo, con capacidad, controles y autorización pendientes."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Martín confirmó los tres escenarios y sus aclaraciones: mínimo con 12 h trimestrales de tech lead, 12 h de Seguridad y 12 h de staff, total 36 h por 675-1.687,50 USD de tiempo y techo 2.000 USD por trimestre sin caja nueva; después de M3, 108 h y techo 6.000 USD sujetos a autorización propia, fuera de los 79.000 acumulados hasta cerrar y en reemplazo de la continuación. El paquete completo conserva gobierno y pasarela si está instalada y es necesaria; producto activo propone contractor al 50%, DevOps/QA 0,5 FTE y Arquitectura 0,1 FTE como hipótesis no medidas. Incluye demostración externa solo con alcance y presupuesto aprobados, no habilitar pilotos con el núcleo restringido y excluir o suspender usos si no se sostienen obligaciones y controles. Confirmado en esta conversación como supuesto, sin acreditar disponibilidad, continuidad autorizada ni aprobación empresarial."
tags: [supuesto, finanzas, gobierno, riesgo]
sources:
  - id: minimo
    resource: "context/supuestos/paquete-minimo-de-aprendizaje.md"
    title: "Paquete mínimo vigente, núcleo restringido tras un corte"
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, continuidad tras corte y base común del producto"
  - id: gobierno
    resource: "plan/annexes/03-gobierno-seguridad.md"
    title: "Anexo C, núcleo de gobierno y controles por superficie"
  - id: arquitectura
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, base común mínima propuesta para el producto"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Rangos de costo por rol como supuestos de planificación"
  - id: precios
    resource: "context/supuestos/precios-externos-sin-cotizar.md"
    title: "Rangos externos de diseño, sin cotización"
  - id: uso-ia
    resource: "context/hechos/uso-ia-interno.md"
    title: "Uso de IA informado y cautelas de la ficha"
  - id: politica
    resource: "context/hechos/gobierno-y-politica-ia.md"
    title: "Política de IA informada y aplicación pendiente de comprobar"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

La continuidad hasta fin de año se propone según el alcance que se corte. No
es automática ni queda autorizada por verificar esta ficha.[^finanzas][^minimo]

## Corte del experimento mínimo

El núcleo restringido por trimestre propone 12 h de tech lead, 12 h de
Seguridad y 12 h de staff para accesos, incidentes y revisión de permisos:
36 h. Con los costos por rol, suma 675-1.687,50 USD de tiempo, con techo
propuesto de 2.000 USD por trimestre y sin caja nueva.[^minimo][^costo-rol]

Después de M3, tres trimestres suman 108 h y un techo de 6.000 USD de tiempo.
Requiere autorización explícita en la salida, no está incluido en los
79.000 USD acumulados hasta cerrar y reemplaza la continuación; no se suma
además de ella.[^minimo]

Este núcleo no mantiene un piloto activo ni habilita usos cuyos controles no
cubre. Sin capacidad para sostener obligaciones y controles, se excluye o
suspende el uso hasta cubrirlos.[^minimo]

## Corte del paquete completo

La alternativa con plataforma conserva el siguiente alcance si se autoriza
su continuidad y se confirma capacidad:[^finanzas][^gobierno]

| Componente | Se conserva |
|---|---|
| Núcleo de gobierno | Las fracciones de liderazgo y de seguridad que fija el Anexo C, más el comité de IA |
| Pasarela de salida | Solo si ya está instalada al momento del corte y resulta necesaria para los usos que continúan |
| Plataforma, piloto de producto, contractor y capacitación | No, salvo la base común mínima para el producto (abajo) |

Se costea por tramo de tres meses restante con el [costo por rol](/supuestos/costo-cargado-por-rol.md)
y los [precios externos](/supuestos/precios-externos-sin-cotizar.md). Son
hipótesis de costo, no capacidad ni contratos acreditados.[^costo-rol][^precios]

## Corte parcial: se corta el frente interno y el producto sigue

Regla de precedencia propuesta por Finanzas: primero la seguridad (se
mantienen los controles necesarios mientras un frente opere), después las
dependencias (el frente que sigue conserva lo que usa de la base común) y al
final la caja (el resto se corta). La **base común mínima para el producto**
supuesta es:[^finanzas][^arquitectura]

| Componente | Se conserva |
|---|---|
| Núcleo de gobierno y pasarela | Los controles necesarios para el producto, con capacidad y presupuesto propios |
| Infraestructura de base (gateway, trazas, evals en CI) | Al nivel de los meses 4-6 |
| Contractor de IA aplicada | Al 50%, para las evals y el harness del piloto |
| DevOps/QA | 0,5 FTE para operar el gateway y las evals del piloto |
| Arquitecto | 0,1 FTE para el gate scale/kill del piloto y el paquete de cumplimiento de los meses 10-12 (aislamiento por tenant, ubicación de datos, ADR) |
| Capa de demostración externa | Solo si el gate la habilita por el producto liberado y se aprueban alcance y presupuesto |
| Capacitación, champions y caso de referencia interno | No |

El 50% del contractor y las fracciones técnicas son hipótesis de capacidad,
sin validación empírica de suficiencia. La aprobación del uso actual no se
presume; hay que verificar controles y autorización para cada alcance que
continúe.[^arquitectura][^gobierno]

# Por qué es razonable

- El uso de IA informado permite plantear un escenario de continuidad tras
  un corte, sin demostrar que ese uso futuro esté autorizado (ver
  [uso de IA](/hechos/uso-ia-interno.md)).[^uso-ia]
- La existencia de una política informada no prueba su aplicación operativa
  ni la suficiencia del núcleo (ver
  [gobierno y política](/hechos/gobierno-y-politica-ia.md)).[^politica]
- Los requisitos regulatorios y contractuales se revisan por caso; la ficha
  no atribuye una obligación general sobre toda IA de terceros ni acredita
  que un cliente haya trasladado requisitos a su contrato.[^gobierno]

# Qué lo invalidaría

- Que no se autorice o no haya capacidad para el núcleo: no se presume
  continuidad con costo cero; se excluyen o suspenden los usos hasta sostener
  obligaciones y controles aplicables.
- Que un cliente exija controles que el núcleo no cubre.
- Que el piloto de producto necesite más plataforma que la supuesta, o que pueda
  correr sin el gateway propio.

# Cautelas

- Los montos del paquete completo por gate están en el Anexo E; no se
  trasladan al mínimo vigente ni se suman al cierre ya presupuestado.
- No describe personas: las fracciones son por función.
- La base del producto es una propuesta compartida por los anexos E y B,
  incluido el 0,1 FTE de Arquitectura; esa coincidencia no acredita
  disponibilidad ni suficiencia, tampoco para el contractor al 50%.
- La verificación registra revisión humana de escenarios, sin aprobar
  continuidad, contratación, capacidad ni gasto.

[^minimo]: Paquete mínimo de aprendizaje, núcleo restringido de 36 h por trimestre, costo 675-1.687,50 USD y techo 2.000 USD; tres trimestres tras M3 requieren autorización propia de 6.000 USD fuera de los 79.000 acumulados hasta cerrar, sin piloto activo ni usos con controles no cubiertos.
[^finanzas]: Anexo E, continuidad tras corte, separación de cierre y base restante y precedencia propuesta en el corte mixto con producto activo.
[^gobierno]: Anexo C, núcleo de gobierno y controles aplicables por superficie y alcance; requisitos y autorización pendientes de comprobar en cada caso.
[^arquitectura]: Anexo B, base común mínima propuesta para el producto: infraestructura, contractor al 50%, DevOps/QA 0,5 FTE y Arquitectura 0,1 FTE, sin evidencia de suficiencia de esas fracciones.
[^costo-rol]: Costos por rol supuestos: tech lead 4.500-10.000 USD/mes, senior de Seguridad 3.000-7.500 y staff 1.500-5.000; 160 h mensuales para costear las fracciones.
[^precios]: Precios externos sin cotizar, rangos de diseño que requieren validar alcance y contratación.
[^uso-ia]: Uso de IA informado en el caso, con sus cautelas; no acredita continuidad futura autorizada.
[^politica]: Política de IA informada por el responsable del caso, con aplicación operativa y controles pendientes de comprobar.
