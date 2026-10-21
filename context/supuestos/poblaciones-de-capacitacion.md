---
type: Supuesto
title: "Poblaciones y tiempos de capacitación en IA"
description: "El paquete completo supone poblaciones y dedicaciones de formación, champions y liderazgo, distintas de las del mínimo y sujetas a validación y aprobación de capacidad."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Poblaciones de diseño confirmadas por Martín para el paquete completo: básico 65 por 6 h, intermedio 50 por 12 h, avanzado 10 al 10%-15% durante un trimestre, directivo 3 h por persona, champions 8 al 10% en M4-M12 y líder al 20% durante doce meses; Operaciones con 40% supuesto de horas básicas e intermedias. Se distingue el mínimo con básico 60-70 e intermedio 15-20, sin avanzado ni champions al 10%. Incluye corregir la dedicación de certificación como propuesta, imputar horas directivas, conciliar contribución desplazada sin equipararla a tarifa y ajustar calendario si se extiende la base. Capacidad y agendas siguen sujetas a validación y aprobación. Confirmado en esta conversación."
tags: [supuesto, personas, capacitación]
sources:
  - id: tamano-estructura
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Dotación y peso aproximado de Operaciones y Tecnología"
  - id: capacidad-utilizacion
    resource: "context/hechos/capacidad-y-utilizacion.md"
    title: "Propuesta de dedicación a certificación y restricciones de capacidad"
  - id: pilotos-ia
    resource: "context/hechos/encuesta-y-pilotos-ia.md"
    title: "Uso y formación en el piloto, con sus límites de población"
  - id: convenciones
    resource: "context/supuestos/convenciones-de-calculo.md"
    title: "Convenciones de horas y costeo por rol"
  - id: paquete-minimo
    resource: "context/supuestos/paquete-minimo-de-aprendizaje.md"
    title: "Poblaciones del mínimo, valoración de formación y conciliación económica"
  - id: personas
    resource: "plan/annexes/04-personas-cultura.md"
    title: "Anexo D, AI literacy por nivel y rol e insumos del paquete mínimo"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Los siguientes valores corresponden al **paquete completo**, como supuestos
de diseño sujetos a capacidad disponible.[^personas]

| Nivel o rol | Personas | Tiempo propuesto | Horas modeladas |
|---|---|---|---|
| Básico | ~65 (toda la dotación) | 6 h por persona, en los meses 1-3 | 390 |
| Intermedio | ~50 | 12 h por persona, entre los meses 1 y 9 | 600 |
| Avanzado | ~10 | 10-15% de la jornada durante un tramo de tres meses (meses 4-6) | 480-720 |
| Directivo | Primera línea y Directorio | 3 h por persona; imputación por rol y facilitación a confirmar | Según cantidad de participantes |
| Champions | 8 (uno cada ~8 personas), con al menos 2 de Operaciones y 2 de áreas de staff | 10% de la jornada en los meses 4-12 | 1.152 |
| Líder del programa de adopción | Una persona | 20% de su jornada durante 12 meses | 384 |
| Operaciones dentro de básico e intermedio | — | ~40% de esas horas, como reparto supuesto a validar | Según cohorte |

El [mínimo](/supuestos/paquete-minimo-de-aprendizaje.md) reserva básico para
60-70 personas (360-420 h) e intermedio para 15-20 (180-240 h), sin avanzado ni
red de champions al 10%.[^paquete-minimo]

Los cálculos usan 160 h mensuales y 480 h por persona-tramo: básico 65 × 6;
intermedio 50 × 12; avanzado 10 × 480 × 10%-15%; champions 8 × 160 × 9 × 10%;
líder 160 × 12 × 20%.[^convenciones]

# Por qué es razonable

- La dotación es de 60-70 personas, con cerca de 80% en Operaciones y
  Tecnología (ver [tamaño y estructura](/hechos/tamano-y-estructura.md)).[^tamano-estructura]
- La propuesta interna de certificación contemplaba 10-15% del tiempo semanal;
  su disponibilidad requiere autorización (ver
  [capacidad y utilización](/hechos/capacidad-y-utilizacion.md)).[^capacidad-utilizacion]
- El piloto mostró uso alto con capacitación baja (ver
  [pilotos](/hechos/encuesta-y-pilotos-ia.md)): el básico apunta a esa brecha.[^pilotos-ia]

# Qué lo invalidaría

- Que la utilización no deje liberar esas horas sin perder facturación
  comprometida.
- Que el nivel intermedio necesite más horas para mover el uso de ejemplos al
  pedir.

# Cautelas

- Las horas se costean por rol según las
  [convenciones](/supuestos/convenciones-de-calculo.md).[^convenciones]
  El mínimo usa 10-35 USD/h como supuesto agregado de formación, sujeto a
  validar la mezcla de participantes.[^paquete-minimo]
- El costo de oportunidad requiere conciliar contribución desplazada y trabajo
  recuperable, sin equipararlo a la tarifa facturable ni duplicar el costo
  cargado.[^paquete-minimo]
- Las horas de participantes directivos requieren imputación por rol; no
  quedan absorbidas automáticamente por el tiempo asignado al líder.
- Los valores del paquete completo y del mínimo deben reconciliarse con la
  alternativa elegida y la capacidad por persona y semana.
- El avanzado se expresa en el Anexo D con 480 h por persona-tramo, la
  convención de costeo (ver [convenciones](/supuestos/convenciones-de-calculo.md)):
  480-720 h en total.[^personas][^convenciones]
- El uso semanal por área que mide el programa alimenta el tablero mensual del
  AI Council; no suma horas a esta ficha.
- Si se extiende la línea de base, se ajusta el calendario de formación y
  prácticas antes de ejecutarlas.[^paquete-minimo]
- La verificación registra supuestos de diseño; personas, agendas y capacidad
  siguen sujetas a validación y aprobación organizacional.

[^tamano-estructura]: Tamaño y estructura de la organización, dotación y pesos aproximados de las áreas.
[^capacidad-utilizacion]: Capacidad, utilización y bench, dedicación propuesta a certificación y restricciones del proyecto de adopción.
[^pilotos-ia]: Encuesta y pilotos internos de IA, uso y finalización de cursos en una muestra autoseleccionada.
[^convenciones]: Convenciones de calendario y cálculo, 160 h por mes, 480 h por tramo y costo por rol.
[^paquete-minimo]: Paquete mínimo de aprendizaje, poblaciones, tasa agregada de formación, conciliación de capacidad y contribución desplazada.
[^personas]: Anexo D, AI literacy por nivel y rol e insumos del paquete mínimo, como propuestas de diseño.
