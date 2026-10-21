---
type: Supuesto
title: "Umbrales técnicos propuestos por la arquitectura"
description: "Umbrales que propone el anexo de arquitectura sin medición previa: los de la ficha de evaluación del caso de referencia (con el gate de impacto), la política de ruteo y el criterio de la prueba de portabilidad y costo del gateway, el método del intervalo de throughput y el replan de capacidad de los meses 4-6."
status: draft
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Martín confirmó en esta conversación los cuatro bloques como propuestas de diseño: evaluación del asistente; ruteo, portabilidad y costo; medición de productividad y calidad; y capacidad M4-M6 del paquete completo. Incluye objetivos sin medir, ceros observados sin garantía de ausencia de riesgo, denominadores previos, costo del gateway calculado sin redondear y sin prometer repago del programa, viabilidad estadística pendiente y calidad con precedencia sobre throughput. Confirma la conciliación de 2,225 FTE y 0,025 FTE de holgura, documentación imputada a cada fracción y excepción de capacidad sujeta a autorización. No acredita resultados, disponibilidad, contratación, validación contractual ni aprobación empresarial; las alternativas ampliadas no se incorporan al paquete mínimo."
tags: [supuesto, arquitectura, evals, finops]
sources:
  - id: arquitectura
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, propuestas de evaluación, ruteo, medición y capacidad"
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, gasto elegible, modelo de costo y conciliación de capacidad"
  - id: gobierno
    resource: "plan/annexes/03-gobierno-seguridad.md"
    title: "Anexo C, denominador de eventos del agente para cobertura de ruteo"
  - id: roadmap
    resource: "plan/annexes/06-roadmap-riesgo.md"
    title: "Anexo F, umbrales y salidas propuestas de las lecturas M6 y M9"
  - id: personas
    resource: "plan/annexes/04-personas-cultura.md"
    title: "Anexo D, propuesta de contractor y fracciones de documentación y traspaso"
  - id: politica
    resource: "context/hechos/gobierno-y-politica-ia.md"
    title: "Política de IA informada por el responsable del caso y sus cautelas"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones R-13 (datos de uso), R-14 (método de medición), R-15 (plataforma), R-17 (rama con plataforma) y R-18 (calendario de la base)"
  - id: ganancia
    resource: "context/supuestos/ganancia-de-productividad.md"
    title: "Rango supuesto de ganancia de throughput, +10% a +25%"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21 }
---
# Supuesto

El plan propone estos umbrales para poder decidir y prevé recalibrarlos con la
primera medición. Ninguno está medido. Los usa el anexo de arquitectura.

## Ficha de evaluación del caso de referencia (asistente de conocimiento interno)

Objetivos propuestos por el protocolo del anexo B, sin validación empírica.[^arquitectura]

| Gate | Umbral propuesto |
|---|---|
| Rendimiento | Exactitud en preguntas respondibles ≥ 80%; cita correcta ≥ 90%; latencia p95 ≤ 10 s; costo por 1.000 consultas dentro del tope de FinOps |
| Seguridad (duros) | Cero fugas de datos Restringidos y cero cruces de tenant observados en las pruebas; cero inyecciones exitosas observadas en el estrato adversarial; abstención correcta ≥ 80% en preguntas sin respuesta |
| Ético | 100% de rechazo a pedidos de evaluar o decidir sobre personas en la suite; la exactitud de Operaciones no queda más de 10 puntos porcentuales debajo de la de Tecnología |
| Impacto (extensión, no valor) | En las últimas 4 semanas, uso semanal ≥ 40% de la cohorte y respuestas marcadas como erróneas ≤ 10% de las usadas; si no, 6 semanas más y, si sigue debajo, no se extiende. El paso a nivel 2 (prepara, no ejecuta) en la cohorte depende de los gates de rendimiento, seguridad y ético |
| Juez automático | Solo si coincide ≥ 80% con revisores humanos en 50 casos: al menos 40 coincidencias |
| Drift | Alerta si la exactitud cae más de 5 puntos porcentuales o la abstención sube más de 10 puntos porcentuales contra la versión aprobada |
| Rollback | Volver a la versión anterior en ≤ 1 día hábil |
| Dataset v1 | ~200 preguntas: 50% respondibles con una fuente, 20% con varias, 15% sin respuesta, 15% adversariales. Con 200 exactas: 100, 40, 30 y 30 preguntas, respectivamente |

El protocolo debe fijar los denominadores de cada tasa antes de medir. Cero
fallas observadas en una muestra no garantiza ausencia de riesgo. La tasa de
respuestas reportadas como erróneas es una señal de uso; por sí sola no prueba
ausencia de daño ni valor económico.

## Política de ruteo y prueba de portabilidad y costo del gateway

Este bloque rige solo si el Directorio libera plataforma bajo la regla de señal
y cuatro condiciones (R-15); no es parte del paquete mínimo de aprendizaje. Cada
ruta la habilita el Responsable de Tecnología tras la prueba de portabilidad y
costo, con el régimen comercial confirmado por escrito con el proveedor y
verificado por el CFO (R-17); sin esa confirmación, la ruta queda en laboratorio
con tráfico sintético. No acredita que el proveedor admita hoy ninguna de las
rutas.[^arquitectura][^resoluciones]

- El agente de código se enruta según su régimen comercial: con la
  suscripción que permite gateway (plana, y enrutar la preserva), sí; con la
  suscripción que no lo permite (plana, y enrutar la convierte en facturación
  por API, o respuesta ambigua), no, con controles sin gateway por verificar y
  ruteo ensayado en laboratorio; con pago por consumo, sí. La meta de ≥ 90% de sus
  eventos por el gateway rige solo con la suscripción que permite gateway y con el pago por consumo, con el denominador del anexo de
  gobierno (eventos del agente según la consola del proveedor). Los casos propios
  tienen una meta de 100% por el gateway y se miden aparte.[^gobierno]
- Denominadores, con la definición y el símbolo del anexo E: *fc* y *s* se
  miden sobre el **gasto elegible**, definido en el modelo como el consumo del
  agente de código a precio de lista. *fc* es la fracción del **costo** de ese gasto que pasa por
  el gateway; si no hay costo por evento, se estima con la fracción de eventos
  y se marca "estimado". El lote de *s* tiene la mezcla de tipos de tarea del
  agente ponderada por costo. La fracción de eventos sobre las cuatro
  superficies es una métrica de cobertura de controles y no se multiplica por
  *s*.[^finanzas]
- El umbral es costo anual del gateway / (múltiplo de consumo × gasto base
  anual elegible). Con los valores centrales supuestos del anexo E,
  33.000 USD de infraestructura y 21.500 USD de gasto base anual, resulta
  38,4% a 4×, 25,6% a 6× y 12,8% a 12×. Son cifras redondeadas para comunicar;
  la decisión usa la fórmula sin redondear y se recalcula con costos medidos.[^finanzas]
- La prueba de cobertura potencial ante pago por consumo exige *fc* × *s*
  suficiente a 6× (33.000 / (6 × 21.500) = 25,581395…% en el ejemplo central),
  caída de la tasa de éxito ≤ 5 puntos porcentuales y migración entre
  proveedores ≤ 20 días-persona. El ruteo solo se activa si preserva la
  suscripción plana o el proveedor ya cobra por consumo.[^arquitectura]

Con una suscripción plana que conserva el precio, el gateway aporta control y
telemetría, sin ahorro de precio. El ahorro por ruteo solo se evalúa bajo pago
por consumo. El umbral cubre la infraestructura modelada del gateway; no
demuestra repago del programa completo ni ahorro observado.[^finanzas]

## Método del intervalo de throughput (gate de valor de los meses 6, 9 y 12)

Protocolo propuesto. Lo produce QA/análisis de datos bajo el Responsable de
Tecnología, el verificador senior independiente verifica el acta de viabilidad y
los indicadores de cada lectura, y el AI Council ratifica el método antes de la
segunda liberación, previa a M1, sobre la tabla de operación del acta (R-14); la
autoridad del gate no lo ratifica. Sin ratificación no se libera M1-M3.[^resoluciones]
La base prospectiva se recoge en las semanas 1-4 (u 8) antes del tratamiento; la
serie retrospectiva solo estima tendencia y ruido. Todos los conteos son totales
por área y semana: ningún dato por persona se extrae ni se retiene (R-13).[^arquitectura][^resoluciones]

| Elemento | Propuesta |
|---|---|
| Estimador | Razón de tasas de PR aceptados por persona-semana activa, ventana contra base congelada, con pesos de estrato fijados en la base y ajuste por la tendencia de la serie de la preparación previa |
| Intervalo | 90% bilateral por conteos en escala logarítmica, ampliado por la sobredispersión φ estimada en la serie retrospectiva |
| Cuenta de potencia | SE = √(φ × (1/P_b + 1/P_v)), con P_b y P_v los PR de la base y de la ventana; semiancho = 1,645 × SE; mejora distinguible de cero con 80% de probabilidad ≈ 2,49 × SE. λ (PR por persona y semana) y φ no tienen dato: el acta los mide |
| Precisión | No se exige semiancho ≤ 3 puntos porcentuales: con ventana del doble de la base requiere ≈ 4.509 PR en la base (unas 564 personas con 2 PR por semana) |
| Muestra mínima | 15 personas del padrón con PR en la base, como conteo; con menos, ninguna lectura decide por valor |
| Gate de valor | Mes 6: no lee valor; decide por adopción, calidad, costo y controles, y corta solo por daño de calidad o caída demostrada del throughput. Mes 9: pasa si el peor caso es mayor que 0, sin daño (se acredita el peor caso); espera única con estimado ≥ +5% sin pasar; corta con estimado < +5% o daño. Mes 12: peor caso mayor que 0, sin daño, como evidencia para el año 2 |
| Calidad | Guardia de daño: hay daño si el límite inferior del aumento de incidentes o de retrabajo es mayor que 0, y corta aunque el throughput pase. No se exige no inferioridad con δ = +10%: requiere ≥ 447 eventos en la base, y cada PR aporta a lo sumo uno |
| Respaldo | En la semana 4, con λ y φ observados, si la lectura del mes 9 no distingue con 80% de potencia una ganancia de +25% (techo del rango supuesto) con base de 4 semanas y sí con 8, la base se extiende a la semana 8 (R-18). La retrospectiva no es base de atribución[^ganancia] |

Los umbrales y las salidas de espera o corte remiten al anexo F, que adopta este
gate.[^roadmap] Con n = 18 y λ = 2, ilustrativos, el gate anterior (límite inferior
≥ +3% en M6 y ≥ +8% en M9) pasaba con ≈ 6% de probabilidad en el escenario base;
el del mes 9 propuesto pasa con ≈ 21% en el base y ≈ 56% en el optimista, y corta
con ≈ 68% sin mejora real. Son cuentas de planificación, no resultados
observados.[^arquitectura]

Una tasa base cero no permite calcular variación relativa: en calidad se
informan conteos, exposición y diferencia absoluta por 100 PR, sin declarar
ausencia de daño. Sin denominador, el indicador es no estimable, no cero. El
método debe reformularse y ratificarlo el AI Council antes del tratamiento o
aplicar las salidas del gate si el problema aparece en una lectura.[^arquitectura]

## Replan de capacidad de los meses 4-6 con el producto diferido

Alternativa del paquete completo: rige solo si el Directorio libera plataforma
en el mes 3 (o en el 6 o el 9) bajo R-15. Personas confirma el 0,2 del
contractor en su contrato y la excepción de 0,3 FTE requiere aprobación previa
del Directorio (R-17). Sin contractor ni perfil interno demostrado al inicio de
M4, no se inician los hitos de IA aplicada. No forma parte del paquete
mínimo.[^arquitectura][^personas][^resoluciones]

- Se propone bajar Arquitectura de 0,5 a 0,4 FTE al diferir el diseño del
  producto, y DevOps/QA de 1,0 a 0,8 FTE al trasladar tareas al contractor.
  Una persona al 100% cubriría 0,8 FTE de IA aplicada más 0,2 FTE para esas
  tareas, sujeto a confirmar alcance y disponibilidad.[^arquitectura][^personas]
- Si existe contractor, pero no dispone de ese 0,2, se propone la excepción
  acotada de 0,3 FTE internos, con aprobación previa del Directorio. Sin
  contractor ni perfil interno demostrado no se inician los hitos de IA
  aplicada: la excepción no reemplaza al especialista. La alternativa con
  fracción interna requiere ~3,3 FTE clave en M4-M6, no la capacidad del
  replan.[^arquitectura][^finanzas]
- El modo control aporta 1,2 FTE del anexo B (Arquitectura 0,4 y DevOps/QA
  0,8); este número no incluye las otras funciones del programa.[^arquitectura]

La conciliación del anexo E para el replan suma 576 h de Arquitectura y
DevOps/QA, 216 h de gobierno y seguridad, 96 h del líder y 180 h de Council,
bypass y red team interno: 1.068 h / 480 = 2,225 FTE clave. Frente al techo
supuesto de 2,25, quedan 0,025 FTE, equivalentes a 12 h trimestrales. El anexo B
usa la misma cuenta conciliada; el 0,05 que menciona corresponde a la holgura de
los meses 7-9.[^finanzas][^arquitectura]

La documentación mínima reproducible de los cuatro entregables incluye tupla
de versión, instrucciones de ejecución, ADR corto y corrida fechada. Se
estiman 1-2 días-persona por entregable (4-8 en total), imputados a la fracción
del contractor que produce cada uno: 0,8 o 0,2, según su asignación. La
reproducción independiente requiere 0,5-1 día por entregable (2-4 en total),
dentro del 0,8 de DevOps/QA. Son tareas incluidas, no esfuerzo adicional
presupuestado por fuera de esas fracciones.[^arquitectura]

Manuales y traspaso se difieren a M7-M12. En la semana 7 del tramo M4-M6 se
revisan documentación y reproducción de los entregables cerrados; un
entregable sin documentación reproducible no cuenta para la lectura de M6.
Si falta capacidad, la excepción requiere aprobación previa del Directorio;
esta revisión humana no la autoriza.[^arquitectura][^personas]

# Por qué es razonable

- Los umbrales de seguridad son duros porque la
  [política](/hechos/gobierno-y-politica-ia.md) prohíbe que un dato Restringido
  llegue a una IA externa: no hay tolerancia que proponer.[^politica]
- Los de rendimiento son un punto de partida de un caso de nivel 1 (asiste) a nivel 2 (prepara, no ejecuta) con revisión
  humana, donde un error se corrige antes de usarse.
- El umbral de 6× es el mismo múltiplo que dispara el gate de FinOps del plan,
  que el reporte mensual con el escenario de consumo alimenta en el tablero mensual del Council.
- Condicionar el ruteo al régimen evita que un gate de control obligue a un
  cambio que encarece el servicio.
- El intervalo usa totales por área y semana porque el tratamiento por defecto
  de los datos de uso son los agregados (R-13), y porque la precisión la fija el
  total de PR, no la cantidad de personas: agrupar no la cambia. Con 15-20
  personas solo se distingue con buena probabilidad una mejora cercana al techo
  del rango, y el plan lo declara.
- El gate de impacto combina adopción y errores reportados para decidir
  extensión; no demuestra ausencia de daño. El caso de referencia no tiene
  valor económico asignado: es un piloto de aprendizaje.
- El replan sale de las fracciones de esfuerzo de los anexos de arquitectura y
  de personas, con los [costos por rol](/supuestos/costo-cargado-por-rol.md).

# Qué lo invalidaría

- La primera corrida de la suite en los meses 4-6: si la línea base del caso queda lejos de
  estos valores, se recalibran y la recalibración se versiona.
- Que el contractor no tenga 0,2 FTE libres en los meses 4-6 (por traspaso o
  documentación): el replan no queda cubierto; la excepción acotada de 0,3 FTE
  requiere autorización antes de activarse.
- Que no se apruebe o contrate el contractor a tiempo ni se demuestre un perfil
  interno: la excepción no alcanza; no se inician los hitos de IA aplicada.
  El modo control también requiere alcance, capacidad y presupuesto autorizados.
- Que la cohorte real tenga menos de 15 personas activas, o que la
  documentación mínima de un entregable lleve más de 2 días-persona.
- Que λ o φ medidos en la serie retrospectiva den una potencia distinta de la
  ilustrativa: la tabla de operación se rehace con esos valores antes de
  ratificar el método.
- Que el proveedor confirme que enrutar el agente de código obliga a facturar
  por API: la cobertura de precio no aplica mientras la suscripción sea plana.
- Que la serie de la preparación previa muestre que ni con base de 8 semanas
  la lectura del mes 9 distingue el techo del rango: el acta lo declara y el AI
  Council ratifica, antes de la segunda liberación, que ninguna lectura decida
  por valor.
- La medición en sombra de los meses 4-6: si el uso o la tasa de error quedan lejos de los
  umbrales de impacto, se recalibran en la lectura del mes 6.

# Cautelas

- Los cuatro bloques fueron revisados en la verificación humana como propuestas
  de diseño, sin medición ni aprobación empresarial. La declaración de verificación no
  acredita consenso del equipo ni ejecución de controles o contratos.
- El anexo D y el anexo B imputan la documentación mínima por entregable a la
  fracción que lo produce (0,8 o 0,2).
- El tamaño del dataset no tiene cálculo de potencia estadística.
- El caso de referencia es ilustrativo; si el portfolio elige otro caso, los
  umbrales se rehacen.

[^arquitectura]: Anexo B, protocolos propuestos de evaluación, ruteo, medición, capacidad y documentación reproducible; objetivos sin medición previa y sujetos a prueba y autorización según su alcance.
[^finanzas]: Anexo E, "Gateway: suscripción contra consumo": infraestructura anual a régimen sin piloto de 18.000-48.000 USD (centro 33.000) y gasto base anual de 19.000-24.000 USD (centro 21.500), sin acreditar ahorro ni repago del programa; "Conciliación de los meses 4-6": 1.068 h / 480 = 2,225 FTE clave y 0,025 FTE de holgura frente a 2,25.
[^gobierno]: Anexo C, cobertura de ruteo medida sobre eventos del agente según la consola del proveedor, separada de cobertura de controles de otras superficies y del gasto elegible.
[^roadmap]: Anexo F, lecturas M6, M9 y M12, bandas de espera y corte por estimado (+5% en M9) y precedencia de calidad; adopta el gate de valor propuesto por el anexo B.
[^personas]: Anexo D, contractor como excepción propuesta, disponibilidad y alcance por confirmar; documentación mínima por entregable y manuales y traspaso diferidos.
[^politica]: Política de IA informada por el responsable del caso; su aprobación y alcance se leen con las cautelas de la ficha, sin acreditar aplicación operativa.
[^resoluciones]: Anexo G, R-13 (agregados por área por defecto), R-14 (produce QA bajo el Responsable de Tecnología, verifica el verificador senior independiente, ratifica el AI Council antes de la segunda liberación), R-18 (extensión de la base), R-15 (señal más cuatro condiciones; libera el Directorio) y R-17 (replan, excepción de 0,3 FTE y habilitación de rutas).
[^ganancia]: Ganancia de productividad supuesta de +10% a +25% en equipos propios; el techo del rango es la referencia de potencia del gate de valor.
