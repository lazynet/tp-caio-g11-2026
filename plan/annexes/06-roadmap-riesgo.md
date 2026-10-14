---
owner: caio
status: draft
title: "Anexo F — Roadmap ajustado por riesgo"
---

# Anexo F — Roadmap ajustado por riesgo

Slides que sustenta: [Slide 3 — Tesis](../slides.md),
[Slide 7 — Roadmap técnico, financiero y cultural](../slides.md) y
[Slide 9 — Riesgos, escenarios y decisiones reversibles](../slides.md).

> **Borrador sin verificación humana.** Todas las fichas de `context/` están en
> `draft` y ninguna cifra de este anexo es apta para el peer review ni para la
> entrega. Los umbrales, bandas y plazos de los gates son supuestos del equipo o
> decisiones propuestas por el CAIO, a calibrar con la línea de base de los
> meses 1-3.

## Objetivo

Poner en una sola línea de tiempo los tracks técnico ([Anexo B](02-arquitectura.md)),
de gobierno ([Anexo C](03-gobierno-seguridad.md)), cultural ([Anexo D](04-personas-cultura.md))
y financiero ([Anexo E](05-business-case.md)), con un gate cada tres meses que
integra las condiciones de los cuatro dueños y dice qué pasa si cada una falla, y
una revisión mensual del Council en el medio: **el riesgo se mira cada mes; la
plata se libera cada tres.**
Sustenta **un único pedido al board, el de la aprobación de hoy** (ver "El pedido
de hoy, único"): autorizar los meses 1-3 (enero-marzo de 2027) con la prueba
chica, con techo de caja y de capacidad, confirmar el piso de capacidad, elegir
hoy entre el replan de los meses 4-6 y la excepción acotada, y adoptar el marco
de gates. El resto del año no se aprueba hoy, y la plataforma de los meses 4-6 no
es un compromiso de hoy: **la decisión de plataforma del mes 3 la libera solo con
una señal** (contractual, de precio por consumo o de cliente). Sin señal, los
meses 4-12 siguen como gobierno mínimo y formación (≈ 199 en el año contra ≈ 400
con señal; [Anexo E](05-business-case.md), "Recomendación de Finanzas", decidida
por lazynet el 2026-10-14).

Las cifras vienen del anexo que se cita. Lo que este anexo agrega son decisiones
del CAIO (bandas de espera fuera de lo económico, plazos de corrección, el
calendario único, la hipótesis de producto y el catálogo de decisiones),
marcadas como propuestas. Donde dos anexos chocan, queda como decisión
pendiente. Responsable humano de cada gate y de cada decisión: **pendiente**.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Convención de tiempo | La preparación previa es octubre-diciembre de 2026, antes de la aprobación de hoy; después, cuatro tramos de tres meses: meses 1-3 (enero-marzo de 2027), 4-6, 7-9 y 10-12 (octubre-diciembre de 2027). Cada tramo termina en un gate (meses 3, 6, 9 y 12) y cada mes hay una revisión del Council, que no libera fondos | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo E](05-business-case.md) |
| Patrón de gates | Kill/scale por etapa, con criterio de éxito y de abandono declarados antes de empezar | [Kill/scale gates](../../material/conceptos/m1u2-kill-scale-gates.md), [kill-fast](../../material/conceptos/m1u1-kill-fast.md) |
| Primeros 100 días | Los meses 1-3 absorben el diagnóstico y la base: inventario, línea de base, política, matriz. No hay quick win de negocio medido en los meses 1-3; la adaptación se justifica en "Primeros 100 días" | [Plan de 100 días](../../material/conceptos/m1u2-plan-100-dias.md) |
| Capacidad | Utilización 83%-90%, bench menor a 1 FTE, restricción de no contratar; sobre de 1-2,25 FTE de personas clave | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md), [sobre](../../context/supuestos/capacidad-de-inversion.md) |
| Clientes principales | Su continuidad es el escenario base; su pérdida parcial es estrés | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |
| Calendario externo | Un producto propio en inversión depende de una habilitación externa con fecha dentro de 2027, que puede superponerse con los meses 4-9 | [Ingresos](../../context/hechos/estructura-de-ingresos.md) |
| Throughput | Unidad: PR aceptado por persona activa en equipos propios. El throughput de cada tramo es g × rampa; se valúa como horas evitadas a output fijo (lectura A) y no es caja | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| Línea de base | Base prospectiva congelada en las semanas 1-4 del plan; la serie de la preparación previa estima ruido y es contra la que se informa el OKR, sin atribuir | [Convenciones](../../context/supuestos/convenciones-de-calculo.md) |

## Evidencia

### El pedido de hoy, único

El pedido completo está en la [Slide 8](../slides.md); las demás slides piden su
parte. Es el mismo que cierran el [Anexo B](02-arquitectura.md) y el
[Anexo E](05-business-case.md).

| Elemento | Qué se aprueba | Fuente |
|---|---|---|
| 1. El primer tramo acotado (meses 1-3) | Inventario de datos, línea de base congelada, matriz superficie→control→telemetría, telemetría unificada, matriz de clientes, evidencia contractual, política ratificada, nivel básico, y la prueba chica desde la semana 5 (ver "Primeros 100 días"). El gateway pasa a los meses 4-6, solo con señal en el mes 3 | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| 2. Techo de caja de los meses 1-3 y reserva de cierre | Hasta 33 mil USD (máximo calculado 32,2: contractor hasta 16,5, legal hasta 10, telemetría hasta 1,5 y contingencia), más una reserva de cierre de hasta 6 que solo se usa si un gate corta. Compromiso máximo de caja en la aprobación de hoy: 39. La reserva cubre solo un corte en la decisión del mes 3: el board se compromete a ampliarla a 15 en el mes 3 si libera la plataforma y a 17 en el mes 6 si libera el producto, antes de liberar el compromiso nuevo (ver "Contingencias") | [Anexo E](05-business-case.md), "Reserva de cierre vigente" |
| 3. Techo de tiempo de los meses 1-3 | Hasta 72 mil con la prueba chica: ~1,8 FTE de personas clave (0,80× del sobre) y ~654 h distribuidas en la dotación, como segundo sobre (62, 1,6 FTE y 590 h sin la prueba) | [Anexo E](05-business-case.md) |
| 4. Piso de capacidad | Sobre clave de al menos ~1,8 FTE en los meses 1-3 con la prueba chica (Anexo E; 1,6 sin ella); con señal en el mes 3, 2,2 / 2,2 / 2,1 en los meses 4-12 con el producto diferido y el replan de los meses 4-6, o 2,5 en los meses 4-6 con la excepción acotada; sin señal, ~0,9 (gobierno mínimo y formación, del Anexo E); lectura del sobre (decisión pendiente "Sobre de capacidad") | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| 5. Salida para el exceso de los meses 4-6 (con señal en el mes 3) | Replan del Anexo B (meses 4-6 en 2,2 FTE clave), con la **excepción** acotada de 0,3 FTE aprobada como respaldo. La excepción cubre solo la falta del 0,2 libre del contractor; sin contractor no alcanza (ver fila 8) | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| 6. Base mínima tras un corte | Si la decisión del mes 3 corta, el núcleo de gobierno sigue el resto del año: hasta 41 mil de tiempo, sin caja | [Anexo E](05-business-case.md) |
| 7. La preparación previa (costo previo propuesto) | Autorizar, o ratificar si consta la ejecución, hasta 7 mil de tiempo | [Anexo E](05-business-case.md) |
| 8. IA aplicada y condición de inicio | El contractor desde el mes 1 (recomendado), o un rol interno si demuestra experiencia en evals y harness antes de la aprobación de hoy y el contractor desde el mes 4 (decisión pendiente "Vía de IA aplicada"). Hoy se autoriza solo su tramo de los meses 1-3 (hasta 16,5, dentro del techo de 33); el de los meses 4-12 se libera solo si la decisión del mes 3 trae una señal, y sin señal el contrato se cierra con un mes de preaviso. Con señal, el contractor es **condición de inicio de los hitos de IA aplicada de los meses 4-12** (harness, evals en CI, ruteo y caché, caso de referencia, prueba de portabilidad y costo); con señal y sin contractor, los meses 4-6 corren en **modo control** (ver la contingencia sin contractor) | [Anexo B](02-arquitectura.md), "Exceso de los meses 4-6 con el producto diferido"; [Anexo E](05-business-case.md), "Dos contingencias del contractor"; [Anexo D](04-personas-cultura.md) |
| 9. Marco de gates | Las tablas de abajo como regla de liberación de fondos, con la revisión mensual del Council (que puede frenar o cortar, pero no libera fondos), la salida de la espera del mes 6, el alcance del corte del mes 9, la regla de precedencia, el método del intervalo de throughput y la reserva de cierre por gate | Este anexo |

El techo de caja se confirma contra el presupuesto 2027 en `private/`. Fuera del
pedido: los meses 4-12, el tramo de producto, el modelo propio, compromisos a más
de 12 meses y todo compromiso con clientes.

### Calendario único de la preparación previa y los meses 1-3 (decisión del CAIO)

| Cuándo | Qué | Quién verifica | Costo |
|---|---|---|---|
| Antes de la aprobación de hoy (preparación previa, octubre-diciembre de 2026) | Verificar que existe historial de PR, integración continua, incidentes y tickets (Anexo B); serie retrospectiva de uso, incidentes y retrabajo, y diseño de la encuesta de chat y suite ofimática (Anexo D). Con esa serie, el semiancho esperado del intervalo de throughput: si supera 3 puntos con la cohorte completa, la lectura del mes 6 no puede discriminar +3% y se reformula antes de la aprobación de hoy (por ejemplo, decidir solo en el mes 9; [Anexo B](02-arquitectura.md), "Método del intervalo"); también se estima el semiancho de calidad y se fija el protocolo único del Anexo B —base, estimador, intervalo, δ y factor de proyección— que no se edita desde el congelamiento de la base. La política queda lista para ratificar, no ratificada | Pendiente; el Directorio ve el resultado en la aprobación de hoy | 1,8-6,7 mil de tiempo: costo previo propuesto, autorizado, o ratificado si consta, hoy ([Anexo E](05-business-case.md)) |
| Semanas 1-4 del plan | **Base prospectiva congelada** con la unidad del Anexo B, antes de cualquier formación o herramienta nueva | Oficina del CAIO, con `finance` | Dentro de los meses 1-3 |
| Semanas 5-13 del plan | Política ratificada, matriz de clientes, evidencia contractual, básico, champions, intermedio de Tecnología con la prueba chica, matriz de superficies y telemetría | `governance`, área comercial, `architect` | Dentro de los meses 1-3 |
| Meses 4-6 en adelante | Gateway, formación de Operaciones y staff; medición contra la base congelada | Oficina del CAIO | Techos por gate |

La serie retrospectiva sirve para estimar tendencia y ruido; **la ganancia se
atribuye solo contra la base prospectiva**, y no antes de los meses 4-6 (la rampa
base es 0% en los meses 1-3, [rampa](../../context/supuestos/rampa-de-la-ganancia.md)).
Respaldo: en la semana 4 la oficina del CAIO aplica el criterio mecánico del
[Anexo B](02-arquitectura.md) ("Respaldo"); la retrospectiva nunca atribuye
ganancia y, si se usa, no libera capital ([convenciones](../../context/supuestos/convenciones-de-calculo.md)).
Si la base no resuelve, prolongarla a la semana 8 es un desacuerdo abierto
(decisión pendiente "Base que no resuelve"). El OKR se informa al lado, contra la
serie de la preparación previa. Quién autoriza gastar la preparación previa antes
del presupuesto: **pendiente**.

### Primeros 100 días: por qué no hay quick win de negocio en los meses 1-3

El método de M1U2 pide 2-3 quick wins con valor medido entre los días 31 y 70
([ficha](../../material/conceptos/m1u2-plan-100-dias.md)). El plan se aparta a
propósito, y eso tiene un costo que reconocemos: **posterga a la lectura del mes
6 el primer aprendizaje de valor; la prueba chica adelanta a la decisión del mes
3 uno de aprendizaje**. Es una preferencia de secuencia (base y matriz antes que
herramienta), no una imposibilidad:

- **El gateway en laboratorio en los meses 1-3 no entra.** Pide 1,8 FTE clave
  contra 1,6 del primer tramo acotado sin la prueba y suma 1-3 mil de caja (36
  contra 33 en el máximo; [Anexo E](05-business-case.md)). La capacidad sola no
  lo descarta: lo descarta que el gateway no mide valor sin harness ni evals, que
  son de los meses 4-6 ([Anexo B](02-arquitectura.md)), y que con la bifurcación
  la plataforma se gana con una señal en el mes 3.
- **La prueba chica, costeada.** Una prueba con el agente de código que
  Tecnología ya usa, sobre la cohorte, desde la semana 5 y en repositorios que la
  matriz habilite, con el intermedio de Tecnología como vehículo. Cuesta ~6 mil
  de tiempo (3-9) y nada de caja; lleva los meses 1-3 a ~1,8 FTE clave y el techo
  de tiempo a 72 ([Anexo E](05-business-case.md), "Prueba chica de los meses 1-3
  (primeros 100 días)"). No contamina la base, congelada en las semanas 1-4: el
  intermedio ya cambia a la cohorte desde la semana 5. Lo que no despeja es la
  atribución (15-20 personas, σ sin dato), así que se lee en el mes 3 como
  aprendizaje (uso, retrabajo, PR aceptados y la dispersión σ que decide si la
  lectura del mes 6 discrimina +3%), sin atribuir ganancia. Se suspende si sube
  el retrabajo o si la matriz no habilita repositorios. La incluimos en el pedido
  de hoy; sin señal en el mes 3, se extiende a la cohorte en los meses 4-12.
- **Precondiciones.** La fase 2 del método pide datos disponibles y criterio de
  éxito; sin matriz de clientes ni inventario no se sabe qué datos se pueden usar.

Lo que sí se entrega medido al día 90, y le sirve al negocio: la política
ratificada y la matriz de clientes (lo primero que puede pedir un banco), la
telemetría unificada con uso por persona activa, el básico con su porcentaje de
cobertura, la línea de base congelada y la lectura de la prueba. La primera
señal de negocio, con plataforma, es el caso de referencia en "asiste" (nivel 1),
en sombra, al cierre de los meses 4-6 ([Anexo B](02-arquitectura.md)), que se lee
en la lectura de impacto del mes 6.

### Revisión mensual del Council

**El riesgo se mira cada mes; la plata se libera cada tres.** Entre gate y gate,
el AI Council hace una revisión mensual de 2 horas con un tablero: caja y tiempo
consumidos contra el techo del tramo, uso semanal por área, incidentes y secretos
expuestos, señales de plataforma (contrato, precio por consumo, cliente) y avance
de hitos. Es la misma reunión en la que el Council revisa el registro de riesgos
cada mes ([Anexo C](03-gobierno-seguridad.md), "Ritmo operativo").

- **Qué puede hacer:** frenar o cortar un frente, activar una contingencia de la
  tabla de "Contingencias", registrar una señal en el mes en que llega y
  escalarla al Directorio.
- **Qué no puede hacer:** liberar fondos. Eso queda en los gates de los meses 3,
  6, 9 y 12, con las condiciones de "Gates por condición".
- **Qué no cambia:** las esperas de 6 semanas y el método de medición (intervalo
  de throughput, base congelada). El throughput necesita semanas de datos y una
  lectura mensual no tiene señal estadística: el tablero lo muestra como
  tendencia, sin decidir por él.
- **De dónde sale el tablero:** de salidas mensuales que ya existen: el reporte
  mensual del intake y el cruce mensual de novedades del proveedor (Anexo C,
  controles del riesgo de IA embebida sin aprobar y del riesgo de un gobierno que
  frena), el reporte mensual de FinOps con el escenario de consumo (Anexo B), el
  registro de riesgos (Anexo C) y el uso semanal por área (Anexo D).
- **Costo: cero adicional.** El Anexo E ya presupuesta el Council a 5 asientos ×
  6 h por tramo de tres meses; tres reuniones mensuales de 2 h entran ahí
  ([Anexo E](05-business-case.md)).

### Línea de tiempo integrada

Columnas: técnico ([Anexo B](02-arquitectura.md)), gobierno y seguridad
([Anexo C](03-gobierno-seguridad.md)), cultural ([Anexo D](04-personas-cultura.md))
y financiero ([Anexo E](05-business-case.md)). **Cada mes: revisión del Council
con poder de corte; los fondos se liberan en los meses 3, 6, 9 y 12.**

| Tramo | Técnico | Gobierno y seguridad | Cultural | Financiero: techo caja / tiempo |
|---|---|---|---|---|
| Preparación previa | Verificación del historial | Política lista para ratificar | Serie retrospectiva y diseño de la encuesta | — (hasta 7 de tiempo, propuesto) |
| Meses 1-3 | Inventario de datos; base congelada; matriz de superficies; telemetría unificada | Política ratificada; inventario v1; matriz de clientes; evidencia contractual registrada; intake en 3 niveles | Básico para todos; champions; intermedio de Tecnología; prueba chica con la cohorte del intermedio desde la semana 5 | 33 / 72 con la prueba, más reserva de cierre de 6 (15 desde el mes 3 con señal; 17 desde el mes 6 con el producto) |
| Meses 4-6, con señal en el mes 3 | Gateway con 2 proveedores; harness v1 y evals en CI sobre el caso de referencia; prueba de portabilidad y costo; FinOps. Sin contractor: modo control (gateway en laboratorio, bypass, FinOps) | Pasarela y DLP; prueba de bypass por superficie; red team interno; ejercicio de incidentes | Intermedio para Operaciones y staff; champions con tiempo | 71 / 106 (71 / 114 con la excepción) |
| Meses 7-9 | Caso de referencia en "prepara, no ejecuta"; piloto en un producto propio (hasta "prepara, no ejecuta", datos sintéticos), **solo si la lectura del mes 6 lo libera**; aislamiento por tenant | Amenazas de la función; criterios de eval; cláusula tipo, sin firma | Casos por rol; calidad de prompts | 59 / 78 (+38 / 34 con el producto) |
| Meses 10-12 | Gate del piloto, si existe; go/no-go de modelo propio; productividad contra la base | Red team externo e ISO 27001 extendida a IA (la demostración externa: solo con señal contractual en el mes 9); gate de 42001 | Traspaso del contractor; Tecnología ≥85% | 95 / 69 (+21 / 23 con el producto) |
| Meses 4-12, sin señal en el mes 3 | Sin gateway, harness ni caso de referencia; FinOps por persona activa con la telemetría del proveedor ([Anexo B](02-arquitectura.md), "Bifurcación en el mes 3: con señal y sin señal") | Solo el gobierno mínimo: política, matriz, inventario y legal; los riesgos de inyección indirecta de prompts y de fuga de secretos quedan en política | Formación para toda la dotación; prueba extendida a la cohorte; contractor cerrado | Sin techo propio por tramo en el Anexo E: año ≈ 199 (caja ≈ 39); las lecturas de los meses 6 y 9 releen las señales |

Techos máximos por tramo de tres meses, en miles de USD ([Anexo E](05-business-case.md)).
Los meses 4-12 muestran la rama con señal en el mes 3. Ese año, con contingencia,
el producto diferido y el replan de los meses 4-6, sin la prueba (que suma ~6 de
tiempo): caja de 98-255 mil y tiempo de 115-320 mil, unos 3,5 FTE promedio (2,0
de personas clave): 1,6 / 2,2 / 2,2 / 2,1. Si la lectura del mes 6 libera el
producto, los meses 7-12 suben a 3,7 / 3,1 FTE clave y la caja a 114-314. El
producto diferido es el escenario base en las dos ramas, no una contingencia.

### Gates por condición (pasa, espera, corta)

Los gates son la aprobación de hoy, la decisión de plataforma del mes 3, la
lectura de impacto del mes 6, la segunda lectura de impacto del mes 9 y el cierre
del año, en el mes 12. En la tabla, la columna "Gate" usa la forma corta ("Hoy",
"Mes 3", "Mes 6", "Mes 9", "Mes 12"). **Solo los gates liberan fondos.** La
revisión mensual del Council (ver "Revisión mensual del Council") puede frenar o
cortar un frente, activar una contingencia o escalar una señal en el mes en que
aparece, pero no libera fondos ni adelanta un gate; las esperas de 6 semanas y el
método de medición no cambian.

Cada condición tiene su resultado y su acción. Un "espera" libera solo lo que
dice la fila y fija un plazo para volver a medir. Cada celda dice qué pasa al
vencer el plazo, con cuatro términos que no son sinónimos (los mismos del
[Anexo E](05-business-case.md)): **corte** (el frente deja de financiarse y
queda la base mínima: mes 6 con estimado ≤ 0%, más retrabajo o espera vencida;
mes 9 con estimado < +5%), **suspensión** (se frena un gasto puntual y se vuelve
a medir: mes 6 en espera, uso de Tecnología <60%), **mantenimiento** (el frente
sigue sin escalar: mes 9 en espera, adopción en 60%-80%) y **excepción** (el
board aprueba algo fuera del sobre, sin caja: 0,3 FTE en los meses 4-6). **La
decisión del mes 3 sigue sin condición de corte, pero ahora decide la
plataforma:** su columna "Corta" dice qué no se libera; sin señal, los meses 4-12
corren sin plataforma, y no liberar los meses 4-6 sigue siendo una decisión del
board, no una regla de abandono. Las condiciones de un frente no frenan al otro;
la columna "Frente" dice a cuál toca: **Base** = la base común, **Interno** = el
frente interno, **Producto** = el frente producto. Si el producto se difirió, sus
condiciones son "no aplica" y sus fondos no se liberan. Bandas económicas:
[Anexo E](05-business-case.md); el resto, propuesta del CAIO sobre los umbrales
de los Anexos B, C y D.

**Regla de precedencia (propuesta de `finance`, adoptada).** Si un corte alcanza
a la base común y otro frente sigue, se aplica en este orden: **seguridad** (el
núcleo de gobierno, la pasarela y los bloqueos no se cortan mientras un frente
opere), **dependencias** (el frente que sigue conserva la parte de la base común
que usa; para el producto, la base común mínima del [Anexo E](05-business-case.md))
y **caja** (el resto se corta, con su cierre). El caso que la activa es el corte
mixto del mes 9 (abajo).

**Cómo se lee el throughput (método del [Anexo B](02-arquitectura.md), "Método
del intervalo").** Cambio relativo apareado por persona activa contra su base
congelada, con pesos de estrato y descontando el cambio de un grupo que no
adopta o, si no existe, la tendencia de la preparación previa. Intervalo *bootstrap* por persona,
2.000 réplicas, 90% bilateral. **Pasa si el límite inferior es mayor o igual al
umbral**; el estimado puntual ubica la banda de espera o de corte. Con muestra
insuficiente (menos de 8 semanas o semiancho mayor a 3 puntos, con al menos 15
personas activas) no se decide por valor: cuenta como espera de 6 semanas, que
suma semanas y no personas, y, vencida, rige la regla de la fila. Con menos de
15 personas activas no se espera: la lectura del mes 6 se reformula antes de la aprobación de hoy ([Anexo B](02-arquitectura.md),
"Viabilidad"). El mismo método se aplica al retrabajo y a los incidentes, y la
calidad se lee en tres casos ([Anexo B](02-arquitectura.md), "Protocolo de
medición único"): daño (límite inferior > 0) corta; incierto (cruza 0, límite
superior > margen) cuenta como espera y, vencida, como no pasa; no deterioro
demostrado (límite superior ≤ margen) deja decidir al throughput.

**El escenario base no tiene asegurado el paso.** Con +3,75% en el mes 6 y
+9% en el mes 9, pasa solo si el semiancho es ≤ 0,75 y ≤ 1 punto; con ±3, los
límites son 0,75 y 6, y ninguno pasa. Lo esperable es espera en el mes 6 y, si
vence, corte. Por eso el año del base es condicional ([Anexo E](05-business-case.md),
"El base es condicional a la regla del Anexo F").

**Límites de las bandas.** El umbral pertenece a la banda superior: +3% y 80%
pasan en el mes 6, +8% pasa en el mes 9 y +5% espera. Un intervalo cuyo límite inferior
queda debajo del umbral de "pasa" cuenta como espera. Un daño de calidad corta
aunque el throughput pase.

| Gate | Condición | Frente | Pasa | Espera (plazo) | Corta | Fondos que afecta |
|---|---|---|---|---|---|---|
| Hoy | El pedido de hoy completo, techo y piso de capacidad confirmados | Base | Aprobado | — | No arrancan los meses 1-3; la preparación previa queda hundida (≤7) | Meses 1-3: 33 / 72 (con la prueba chica), más reserva de cierre de 6 (ampliable a 15 en el mes 3 con señal y a 17 en el mes 6 con el producto) |
| Hoy | Vía de IA aplicada de los meses 1-3 | Base | Contractor desde el mes 1 o rol interno demostrado | — | Ninguna: los hitos de IA aplicada pasan a los meses 4-6; con señal en el mes 3 y sin contractor ni rol interno, rige la fila del contractor del mes 3 | Contractor de los meses 1-3 |
| Mes 3 | Base congelada con la unidad del Anexo B | Interno | Congelada con fecha | Historial insuficiente: 6 semanas más; no se atribuye ganancia | Sin base al cierre de la espera: se elimina el resultado clave de throughput y el frente interno no escala | Escalado de los meses 4-6 |
| Mes 3 | Política ratificada | Base | Ratificada | En el orden del día sin votar: 6 semanas; meses 4-6 sin casos de cliente | No ratificada: no hay frente producto en el año | Fondos del producto |
| Mes 3 | Matriz de los clientes que concentran la facturación | Producto | Completa | Contratos ambiguos: *default-deny* y revisión legal hasta el mes 4 | Más del 30% ambiguo al mes 4: sin piloto con ese cliente; Operaciones sin meta | Fondos del producto |
| Mes 3 | Evidencia contractual registrada en `private/` y su agregado anonimizado ([Anexo C](03-gobierno-seguridad.md), "Licencia para vender") | Base | Registrada | Incompleta: se completa en los meses 4-6, antes del mes 9 | Sin evidencia en el mes 9: la demostración externa no se financia | Demostración externa (meses 10-12) |
| Mes 3 | Básico ≥90% de la dotación | Interno | ≥90% | ≥50% y <90%: se liberan los meses 4-6 y se rediseña el formato | <50% al cierre de los meses 4-6: cambio de formato, no se repite el curso | Capacitación de los meses 4-6 |
| Mes 3 | Uso de los meses 1-3 dentro del sobre aprobado | Base | Dentro | — | Excedido: meses 4-6 solo con replan de capacidad aprobado | Meses 4-6 enteros |
| Mes 3 | Señal que pague la plataforma de los meses 4-6: restricción (qué restricción cuenta: decisión pendiente "Qué restricción cuenta como señal") o licencia para vender según el umbral contractual, anuncio del proveedor de pasar a consumo, o señal de cliente para el producto | Base | Al menos una | — | Ninguna: los meses 4-12 corren como gobierno mínimo y formación, con la prueba extendida a la cohorte, el contractor cerrado y la reserva de cierre en 6 (≈ 199 en el año contra 394; [Anexo E](05-business-case.md), "Alternativas equivalentes"); las lecturas de los meses 6 y 9 vuelven a leer las señales. No es un corte: difiere la plataforma | Meses 4-6: contractor al 100%, gateway, pasarela |
| Mes 3 | Con señal: contractor contratado (o rol interno demostrado en los meses 1-3 con contractor desde el mes 4) | Base | Contratado | — | Sin contractor: se liberan los meses 4-6 en modo control del Anexo B (contingencia sin contractor; la caja de los meses 4-6 baja ~27). En el mes 6, cobertura de precio y caso de referencia quedan "sin medir", no "pasa" | Meses 4-6: contractor e hitos de IA aplicada |
| Mes 3 | Con señal: reserva de cierre ampliada a 15 | Base | Ampliada | — | No ampliada: no se libera el contractor al 100% | Meses 4-6: contractor |
| Mes 6 | Throughput como tendencia con intervalo, sin más retrabajo; calidad incierta cuenta como espera | Interno | Límite inferior del intervalo ≥ +3% (método del [Anexo B](02-arquitectura.md)) | **Suspensión.** Estimado >0% con límite inferior <+3%, o muestra insuficiente: meses 7-9 sin escalado; se vuelve a medir a las 6 semanas y, si sigue en la banda, se corta el frente interno y queda la base mínima | Estimado ≤0% o daño de calidad: se corta el frente interno; queda la base mínima | Meses 7-9: 59 / 78 (con señal) |
| Mes 6 | Uso semanal de Tecnología | Interno | ≥80% | **Mantenimiento.** ≥60% y <80%: los meses 7-9 siguen; formación rediseñada con casos por rol; se vuelve a medir al cierre de los meses 7-9 | **Suspensión.** <60%: se suspenden en los meses 7-9 las horas de champions y de intermedio que no sean rediseño (~13 de tiempo en el medio); el plan no suma seats, así que no hay expansión que frenar | Capacitación de los meses 7-9 |
| Mes 6 | Cobertura de controles (rama con señal en el mes 3; sin señal: *hooks* y escaneo local probados con secreto sintético, red team acotado cerrado y residual aceptado por el Council de los riesgos de datos de cliente en un modelo externo, de inyección indirecta de prompts y de fuga de secretos, [Anexo C](03-gobierno-seguridad.md), "Controles según la decisión del mes 3") | Base | Casos propios 100% por el gateway; agente de código ≥90% por el gateway solo si su régimen comercial lo permite ([Anexo B](02-arquitectura.md), "Política de ruteo": suscripción que permite gateway o pago por consumo); en la suscripción que no lo permite, control verificado sin gateway y ruteo ensayado; 100% de superficies con control verificado | Superficie con bypass sin control compensatorio: se declara no cubierta y va al Council | Gateway sin operar más de tres meses: se compra una solución | Infraestructura |
| Mes 6 | Red team interno y prueba de portabilidad y costo (rama con señal en el mes 3) | Base | Críticos cerrados; portabilidad ≤20 días-persona; cobertura de precio medida (*fc* × *s* sobre el gasto elegible, hoy el consumo del agente de código, contra el umbral del Anexo E a 6×, ~25%; calidad sin caída mayor a 5 puntos; suscripción preservada, o el proveedor ya cobra por consumo) | Críticos abiertos: el piloto no arranca hasta cerrarlos. Portabilidad >20: sin compromisos de volumen. Cobertura no demostrada: el gateway sigue por control, y la palanca de precio sale del deck | — | Piloto de los meses 7-9; palanca de precio |
| Mes 6 | FinOps: múltiplo de consumo medido | Base | ≤6× efectivo | — | >6× sin mitigar en un tramo de tres meses: se congela la expansión y se topea el consumo | Expansión |
| Mes 6 | Señal de cliente para la hipótesis de producto (ver "Hipótesis de producto"), con matriz habilitante y plataforma liberada en el mes 3 | Producto | Señal cumplida: el board decide ampliar el sobre de los meses 7-12 para el piloto | — | Sin señal, o sin plataforma del mes 3: el producto se difiere (como pronto a los meses 10-12; el costo desde ahí no está calculado) y sus condiciones del mes 9 no aplican | Producto: 38 / 34; reserva de cierre a 17 antes de liberar el tenant del piloto |
| Mes 9 | Throughput; un daño de calidad corta; calidad incierta cuenta como espera | Interno | Límite inferior del intervalo ≥ +8% (método del [Anexo B](02-arquitectura.md)) | **Mantenimiento.** Estimado ≥ +5% con límite inferior < +8%, o muestra insuficiente: solo base mínima y mantenimiento; se vuelve a medir a las 6 semanas. Si sigue debajo de +8%, los meses 10-12 se ejecutan con la base mínima, sin corte | Estimado < +5%: corte del frente interno y de la base común; queda la base mínima en los meses 10-12. Si el producto sigue, rige la precedencia y conserva la base común mínima para el producto (corte mixto: año 433 en vez de 471) | Meses 10-12: 95 / 69 |
| Mes 9 | Costo por PR aceptado | Interno | No sube | Sube con throughput en alza: se revisa el consumo en FinOps | Sube con throughput plano: se aplica el corte de arriba | Consumo |
| Mes 9 | Señal contractual ([Anexo C](03-gobierno-seguridad.md), "Licencia para vender") o producto liberado en el mes 6 | Base | Una de las dos: se financia la demostración externa (red team externo e ISO 27001 ampliada) | — | Ninguna: la demostración externa no se financia y la licencia para vender queda como hipótesis | Demostración externa de los meses 10-12 (11,6-31 de caja) |
| Mes 9 | SLO del piloto a las 6 semanas; cero filtración entre tenants; red team del piloto | Producto | Cumplidos | SLO incumplido: vuelve a "sin IA" o "asiste" y se revisa | Una filtración, o críticos tras dos ciclos: se cancela la función | Producto: 21 / 23 |
| Mes 12 | Trayectoria al equilibrio (~17% de throughput atribuible contra la base del plan; ~23% si sigue el producto; menos si la capacidad se vende) **o** interés contractual en el producto | Interno / Producto | Una de las dos | — | Ninguna: no se financia el régimen (~143, ~188 con el producto); queda el frente interno con las licencias vigentes y la base mínima (~53 mil por año, en el presupuesto 2028) | Año 2 |
| Mes 12 | Tecnología ≥85%; Operaciones habilitadas ≥60%; red team externo sin críticos, si se financió | Base / Interno | Cumplidos | Se informa contra el OKR, con las dos métricas | — | Año 2 |

**Regla de riesgo residual.** Ningún gate pasa con un riesgo residual en la
franja "no se acepta" del [Anexo C](03-gobierno-seguridad.md); los residuales
que acepta el Council llevan fecha de revisión.

**Casos de prueba:**

- **Sin señal en el mes 3:** ni el umbral contractual, ni un anuncio de consumo,
  ni un cliente. El contractor cierra con un mes de preaviso y los meses 4-12
  corren sin plataforma (≈ 199 en el año). Si la lectura del mes 6 trae una
  señal, la plataforma arranca en los meses 7-9, el caso de referencia en
  "prepara, no ejecuta" llega como pronto en los meses 10-12 y un piloto de
  producto no arranca antes de los meses 10-12 (lo decide `caio` en el mes 6;
  [Anexo B](02-arquitectura.md), "Bifurcación en el mes 3: con señal y sin
  señal"). Si la señal llega entre gates, la revisión mensual la registra en su
  mes y la escala; los fondos esperan al gate siguiente.
- **Throughput de +6%:** en el mes 6 pasa si el límite inferior del intervalo
  llega a +3% (con un semiancho de 3 puntos, sí). En el mes 9 queda en "espera":
  se libera solo la base mínima y se vuelve a medir a las 6 semanas; si sigue
  debajo de +8%, los meses 10-12 corren con la base mínima, y el cierre del mes
  12 decide sin trayectoria al equilibrio.
- **Pesimista (+0,5% en el mes 6):** espera; a las 6 semanas sigue debajo de
  +3%, y se corta el frente interno en los meses 7-9. Queda la base mínima
  ([Anexo E](05-business-case.md)).
- **Sin señal de cliente en el mes 6 (base):** el producto no entra al año. No se
  liberan el consumo, el red team ni la infraestructura del piloto; las
  condiciones del producto en el mes 9 no aplican; el cierre del mes 12 decide
  con el frente interno y la base común.
- **Corte mixto (producto liberado en el mes 6; throughput debajo de +5% en el
  mes 9):** fila del mes 9 y "Alcance del corte del mes 9" en "Decisiones"; el
  año queda en 433 en vez de 471.

### Escenarios

Tomados del [Anexo E](05-business-case.md). La primera fila es la rama sin
señal en el mes 3; las demás, la rama con señal y sin la prueba, como las calcula
el Anexo E. El pesimista se muestra con los gates ejecutados y como estrés sin
frenar.

| Escenario | Supuestos | Qué pasa con el roadmap | Resultado del año (miles de USD) |
|---|---|---|---|
| Sin señal en el mes 3 | Ninguna de las tres señales; φ, la fracción de la ganancia que se logra sin plataforma ni contractor, sin dato (0 a 1) | Meses 4-12 como gobierno mínimo y formación; las lecturas de los meses 6 y 9 releen las señales | ≈ 199 (caja ≈ 39), sin rango propio; capacidad ≥ φ × 62; neto −199 a −137 (ROI −100% a −69%) |
| Pesimista, ejecutado | Throughput 5%, rampa 0/10/30/60; sin señal de cliente | Espera en el mes 6 (+0,5%); vence a las 6 semanas y corta el frente interno; queda la base mínima | Neto ≈ −262 (el año cuesta ~265, hasta 388). Si la espera no venciera, corta en el mes 9 (+1,5%): ≈ −300 |
| Pesimista, estrés sin frenar | Lo mismo, sin aplicar los gates | Base común e interno enteros | −382; −502 si el precio pasa a 12× desde los meses 7-9 |
| Base | Throughput 15%, rampa 0/25/60/100; precio plano; sin señal en el mes 6 | Producto diferido. Condicional a que las lecturas de los meses 6 y 9 pasen por límite inferior (con +3,75%, el mes 6 pide semiancho ≤ 0,75) | Si pasan los meses 6 y 9: ROI económico −84%, neto −332 (−409 si el mes 6 libera el producto). Pasa el mes 6 y no el 9: ≈ −275. La espera del mes 6 vence y corta: ≈ −245 |
| Optimista | Throughput 25%, rampa 0/40/80/100; señal en el mes 6 y un cliente con interés contractual en el mes 12 | Piloto en los meses 7-12; en el cierre del mes 12 se decide el primer compromiso contractual, que rige después | ROI económico −76% (con el tramo de producto) |

En ninguno el ROI a 12 meses es positivo con productividad sola, y el
beneficio de caja es cero en todos ([Anexo E](05-business-case.md)). En el año 1,
la rama sin señal pierde menos que el paquete con cualquier φ: la plataforma se
paga solo con una señal, y por eso la decisión del mes 3 la decide. La
diferencia entre el pesimista ejecutado y el estrés, ~120 mil (~82 si la espera
no venciera), es lo que compran los gates. El estrés con el producto desde los
meses 4-6 daría −480: diferirlo protege aparte.

### Contingencias

Cualquier contingencia de esta tabla la puede activar la revisión mensual del
Council en el mes en que aparece el disparador, sin esperar al gate; lo que
requiera fondos nuevos espera al gate siguiente.

| Disparador | Contingencia | Fuente |
|---|---|---|
| El proveedor pasa a cobrar por consumo | Gateway con ruteo, caché y topes; a más de 6× efectivo sin mitigar, se congela la expansión. A 12×, el incremental anual es de 211-267 mil: exposición de la empresa, con o sin plan | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| **Sin el 0,2 del contractor.** Hay contractor, pero su 0,2 libre de los meses 4-6 se va en el traspaso o no está en el contrato | Rige la excepción acotada de 0,3 FTE en los meses 4-6, aprobada hoy como respaldo: meses 4-6 en 2,5 FTE clave, +5 mil de tiempo (3-8), sin caja. El disparador es el control de la semana 7 de los meses 4-6 sobre la documentación mínima reproducible ([Anexo B](02-arquitectura.md)), no el cierre del tramo | [Anexo E](05-business-case.md), "Dos contingencias del contractor"; [Anexo B](02-arquitectura.md) |
| **Sin contractor.** Con señal en el mes 3, el contractor no se aprueba y no hay rol interno demostrado | La excepción no alcanza. Los hitos de IA aplicada no inician; meses 4-6 en modo control con 1,2 FTE del Anexo B (2,2 FTE clave del plan; caja del año 83 en lugar de 177); la lectura del mes 6, sin cobertura de precio ni caso de referencia en sombra: la palanca de precio sale del deck. La fracción interna de 0,8 (3,3 / 3,0 / 2,9 FTE clave) excede el sobre más allá de la excepción: solo con aprobación explícita del exceso | [Anexo E](05-business-case.md), fila 5; [Anexo B](02-arquitectura.md), "Exceso de los meses 4-6 con el producto diferido" |
| Pérdida parcial del cliente principal | Se congelan los gates de los meses 4-12 hasta revisar el techo; con 20% menos de facturación, la caja pesa 25% más | [Anexo E](05-business-case.md) |
| Incidente de datos de un cliente | Se suspende la IA sobre ese cliente y se reporta el mismo día | [Anexo C](03-gobierno-seguridad.md) |
| Primer secreto expuesto | Revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo | [Anexo C](03-gobierno-seguridad.md) |
| Se va una persona clave sin suplente | Se congelan altas de casos de riesgo alto y se baja el alcance del tramo siguiente | [Anexo C](03-gobierno-seguridad.md), [Anexo B](02-arquitectura.md) |
| La utilización cae bajo 80% dos meses por el plan | Se recorta el frente que más tiempo consume | [Anexo E](05-business-case.md), [Anexo D](04-personas-cultura.md) |
| La habilitación externa de un producto propio coincide con los meses 4-9 | El piloto no se pone en el camino crítico de esa habilitación | Criterio del CAIO sobre [ingresos](../../context/hechos/estructura-de-ingresos.md) |
| Cortar en un gate o en una revisión mensual | Cierre: un mes de preaviso del contractor y del laboratorio, pagado con la reserva de cierre vigente: 6 desde la aprobación de hoy, ampliada a 15 en el mes 3 si se libera la plataforma y a 17 en el mes 6 si se libera el producto, siempre antes del compromiso nuevo, con la misma autoridad del gate. Es un renglón de caja propio, separado del techo del tramo y de la base mínima; legal y red team, por etapa | [Anexo E](05-business-case.md), "Reserva de cierre vigente" |

## Riesgos y mitigación

Registro consolidado: los riesgos que cambian el roadmap. El detalle está en el
anexo de cada dueño.

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: con señal en el mes 3, el producto diferido y el replan, los meses 4-12 piden 2,2 / 2,2 / 2,1 FTE clave contra 1-2,25, sin holgura (3,7 / 3,1 en los meses 7-12 si el mes 6 libera el producto) | Alta | Alto | Piso de ~1,8 confirmado hoy (1,6 sin la prueba); la excepción de los meses 4-6 como respaldo (decisión pendiente "Sobre de capacidad") | Los meses 1-3 exceden el sobre aprobado: meses 4-6 solo con replan |
| Con señal, el replan de los meses 4-6 depende de 0,2 FTE libres del contractor, supuesto condicional del Anexo D (ver decisión "Meses 4-6") | Media | Medio | Excepción acotada aprobada hoy | Contingencias "sin el 0,2 del contractor" y "sin contractor" |
| Cambio a pago por consumo | Alta | Alto | El anuncio es una señal que la revisión mensual registra y escala; libera la plataforma en el gate siguiente; con ella, gateway, FinOps y prueba de portabilidad y costo. Hasta entonces, la regla de 6× | Más de 6× efectivo en un tramo de tres meses |
| Datos de un cliente llegan a un modelo externo | Media | Muy alto | Matriz, *default-deny*, pasarela; bloqueo de secretos y datos prohibidos que nunca pasa a monitoreo | Un incidente confirmado |
| Superficies de IA que no pasan por el gateway | Alta | Alto | Matriz superficie→control→telemetría y prueba de bypass en los meses 4-6 ([Anexo B](02-arquitectura.md), [Anexo C](03-gobierno-seguridad.md)) | Bypass sin control compensatorio |
| La productividad no aparece o trae retrabajo | Media | Alto | Base congelada y costo por PR aceptado; la espera del mes 6 vence a las 6 semanas | Debajo de +3% al vencer la espera del mes 6, o menos de +5% en el mes 9 |
| El equilibrio pide ~17% de throughput atribuible contra la base del plan (9%-46%; ~23% con el producto); el OKR de +20% contra el cuarto trimestre de 2026 lo cubre solo si 1,20/(1+d) − 1 − c ≥ 16,7% (d, medido en el mes 3; c, el cambio del grupo que no adopta, desde el mes 6) | Alta | Medio | El caso no descansa solo en productividad: producto y riesgo (decisión pendiente "Exigencia de equilibrio") | Sin trayectoria ni interés contractual en el mes 12 |
| La hipótesis de producto no tiene comprador | Media | Medio | Señal de cliente exigida en el mes 6; el tramo de producto no se gasta sin ella | Sin señal en el mes 6 |
| La licencia para vender no se confirma | Media | Medio | Evidencia contractual en los meses 1-3; demostración externa condicionada en el mes 9 | Sin señal contractual en el mes 9 |
| Alto riesgo regulatorio fuera del crédito | Media | Alto | Clasificación caso por caso (empleo, educación y otros usos); la fecha del Anexo III del AI Act que cita el Anexo C (2027-12-02) cae dentro de los meses 10-12; Legal externo confirma | Un caso clasificado de alto riesgo sin dictamen |
| Capacidad crítica en pocas personas | Alta | Alto | Suplentes, runbooks, contractor con traspaso | Hito crítico sin suplente al cierre de los meses 4-6 |
| Operaciones no puede adoptar por contrato del cliente | Alta | Medio | Dos métricas publicadas, con denominadores | Matriz sin completar al cierre de los meses 1-3 |
| Prompt injection en agentes con herramientas | Media | Alto | Mínimo privilegio, gate humano, red team | Acción fuera de alcance en pruebas |
| Declarar controles o certificaciones que no existen | Baja | Muy alto | Toda afirmación comercial la valida seguridad | Una afirmación sin evidencia en una propuesta |
| El gobierno frena la entrega y el uso migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles | Más del 20% fuera de SLA dos meses |

## Decisiones

### Decisiones del CAIO sobre los titulares

Nueve cruces que dejaron abiertos los dueños. La primera la decidió un humano
(lazynet, 2026-10-14); las tres siguientes son la base del Anexo E: elegir la
otra opción obliga a recalcular el Anexo E, y la alternativa queda costeada.

| Decisión | Elegida | Alternativa a la vista | Por qué | Tipo |
|---|---|---|---|---|
| Plataforma de los meses 4-6 | Bifurcación en el mes 3: hoy se compra el primer tramo acotado y la prueba chica; la decisión del mes 3 libera contractor al 100%, gateway y pasarela solo con una señal contractual, de precio por consumo o de cliente; sin señal, los meses 4-12 como gobierno mínimo y formación (≈ 199 en el año) | El paquete completo desde hoy (≈ 400 con la prueba), o solo gobierno mínimo y formación, o solo el piloto sobre el agente actual, todo el año, sin plataforma | En el año 1, las dos opciones baratas le ganan al paquete con cualquier φ; el diferencial de ~233 lo pagan solo opciones sin valor medido ([Anexo E](05-business-case.md), "Alternativas equivalentes"). Sin señal se difiere, no se corta | Reversible: las lecturas de los meses 6 y 9 releen las señales |
| Meses 4-6 (rama con señal) | Replan del Anexo B (2,2 FTE clave, tiempo del año 217, económico 394) con la excepción como respaldo aprobado hoy | Excepción acotada (2,5 FTE clave, tiempo 223, económico 399), que saca ~3-8 mil de horas facturables | El recurso escaso es el tiempo clave; el replan no suma caja. Depende del 0,2 libre del contractor, supuesto condicional del Anexo D ("Holgura de 0,2 FTE del contractor en los meses 4-6 (replan del Anexo B)"): se sostiene solo si el contrato lo incluye hoy; si no, rige la excepción (contingencia sin el 0,2 del contractor). Sin contractor no alcanza ninguno: contingencia sin contractor | Reversible: el respaldo entra sin nueva aprobación |
| Redondeo de techos | Hacia arriba: 33 de caja, 72 de tiempo con la prueba (62 sin ella), 41 de base mínima | El número redondo (32 / 71 / 40) y recortar componentes | La autorización nunca queda debajo del cálculo (32,2, 62 + 9,1 y 40,2) | Reversible |
| Demostración externa del Anexo C | En la base como cota superior, con la liberación condicionada en el mes 9 a la señal contractual | Tramo condicional como el producto: caja base 152 (85-220), techo de los meses 10-12 59, tramo de 25 (13-36) | La evidencia contractual no depende de la señal de producto; contar el renglón y condicionar el gasto compatibiliza los Anexos E y C | Reversible hasta el mes 9 |
| Equilibrio en las slides | ~17% atribuible contra la base del plan sin producto, con ~23% con el producto en la misma línea | ~23% como titular: "el OKR y el equilibrio se miden contra bases distintas" | El producto lo tiene que pagar el producto. No se resta contra el +20% del OKR, que es observado contra el cuarto trimestre de 2026: lo cubre solo si 1,20/(1+d) − 1 − c ≥ 16,7% (d, medido en el mes 3; c, el cambio del grupo que no adopta, desde el mes 6) | Reversible |
| Espera del mes 6 | Vence a las 6 semanas: si sigue en la banda, se corta el frente interno (pesimista ≈ −262) | Sin salida: meses 7-9 enteros y corte en el mes 9 (≈ −300) | Una espera sin regla de salida es gasto sin techo; los gates pasan a ahorrar ~120 en lugar de ~82 | Reversible |
| Alcance del corte del mes 9 | Frente interno y base común; queda la base mínima en los meses 10-12. Si el producto sigue, rige la precedencia y conserva su base común mínima (año 433 contra 471) | Solo el frente interno: ≈ −369, casi igual al estrés (−382) | Si el corte no alcanza a la base común, el gate de throughput casi no protege. Con el producto vivo protege ~38, casi todo tiempo | Reversible |
| Contractor como condición de inicio de los hitos de IA aplicada de los meses 4-12 | Con señal y sin contractor, modo control del Anexo B (caja del año 83, 2,2 FTE clave) | La alternativa sin contractor, con fracción interna de 0,8 (tiempo del año 274, 3,3 FTE clave en los meses 4-6) | La contingencia sin contractor no se cubre con tiempo: excede el sobre casi un 50% en los meses 4-6, y lo que ahorra es caja, el recurso que no falta | Reversible: la lectura del mes 6 puede aprobar la vía y mover el caso de referencia a los meses 7-9 |
| Ruteo del agente de código | Según su régimen comercial ([Anexo B](02-arquitectura.md), "Política de ruteo"): se enruta en la suscripción que permite gateway y en el pago por consumo; en la suscripción que no lo permite, no, con control verificado sin gateway y ruteo ensayado | ≥90% de ruteo sin condición, como pedía la versión anterior de este anexo y pide hoy el Anexo C | Un gate no puede obligar a un cambio que encarezca el servicio. Texto del Anexo B, compatible con el Anexo E, porque además exige el ruteo ensayado. El Anexo C lo adoptó en esta ronda | Reversible |

### Hipótesis de producto (M1U2 aplicado: RICE ajustado por riesgo)

La tesis "IA que se vende" necesita un caso concreto. El CAIO elige **una**
hipótesis y la compara con dos alternativas y con no tener frente producto. Los
puntajes son **supuestos del CAIO, sin medición**: el curso no da una fórmula
para el riesgo, así que el factor 1-3 que divide el puntaje es una propuesta del
equipo ([ficha RICE](../../material/conceptos/m1u2-rice-ajustado-por-riesgo.md)).
El equipo y el Council los validan en la decisión del mes 3.

**Hipótesis elegida: asistente de integración en la plataforma propia.**

| Campo | Hipótesis | Estado |
|---|---|---|
| Usuario | El desarrollador de un banco o fintech cliente que integra funcionalidades de la plataforma | Supuesto |
| Tarea | Encontrar la funcionalidad, armar la llamada e interpretar errores en el sandbox | Supuesto |
| Outcome | Tiempo hasta la primera integración exitosa en sandbox, y consultas de integración al soporte por integración | Sin línea de base: se mide en las primeras 4 semanas de los meses 7-9, si el producto se libera |
| Datos | Documentación técnica y de referencia de la plataforma, propiedad de Acme Labs, y un sandbox con datos sintéticos. Ningún dato productivo de cliente | Fijado por el catálogo |
| Autonomía | "Asiste" (nivel 1): sugiere, el desarrollador ejecuta | Propuesto |
| SLO | Parte de los umbrales propuestos de la ficha de evaluación del [Anexo B](02-arquitectura.md) (exactitud, cita, cero cruces de tenant), recalibrados al caso antes de los meses 7-9; medido a las 6 semanas (plazo ilustrativo del curso) | Pendiente |
| Costo | Tramo de producto, medio (rango): 37 (16-59) de caja y 39 (23-56) de tiempo. Techo autorizado si la lectura del mes 6 lo libera: 38 / 34 en los meses 7-9 y 21 / 23 en los meses 10-12 (caja / tiempo) ([Anexo E](05-business-case.md)) | Costeado |
| Señal comercial (mes 6) | Proporcional a la etapa: un cliente, con un interlocutor que maneja presupuesto, acepta por escrito evaluar el asistente en el sandbox con datos sintéticos **y** acepta como referencia un rango de precio sujeto a resultados, sin compromiso de compra. El rango lo propone el área comercial antes del mes 6 (pendiente; no se publica). Aceptar evaluar sin interlocutor de presupuesto ni rango de precio es interés exploratorio: no libera el producto | Propuesta del CAIO, pendiente de acuerdo del equipo |
| Contingencia sin señal | El producto se difiere; el método queda como capacidad del frente interno y no se presenta como producto | Fijado por los gates |

**Comparación.** Reach: 3 = los clientes de la plataforma; 2 = un segmento
nuevo; 1 = un producto que todavía no factura. Impact y Confidence, con la
escala del curso. Effort en tramos de tres meses de una persona clave
(persona-tramo).

| Opción | Reach | Impact | Confidence | Effort | Riesgo | Puntaje | Por qué |
|---|---|---|---|---|---|---|---|
| **1. Asistente de integración en la plataforma propia** | 3 | 1 | 50% | 2,5 (el tramo de producto del Anexo E) | 1 | **0,60** | La línea de soporte de la plataforma es la de mayor margen relativo ([ingresos](../../context/hechos/estructura-de-ingresos.md)); reutiliza el gateway, el harness y la ficha de evaluación del caso interno; sin datos de cliente |
| 2. Función en el producto propio de medios de pago | 1 | 2 | 50% | 3 (supuesto: suma trabajo de cumplimiento sin costear) | 3 | 0,11 | Producto sin legado, pero con habilitación externa que puede caer en los meses 4-9 y sin sistema de gestión certificado ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) |
| 3. Servicio de implementación de agentes de código para otras software factories | 2 | 1 | 50% | 4 (supuesto: consume las personas clave que no entran) | 2 | 0,13 | Segmento de la propuesta al Directorio ([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)); el programa de partners exige certificaciones y despliegues que no hay, y compite con horas facturables |
| 4. Solo gobierno y eficiencia, sin frente producto | — | — | — | 0 | — | No aplica | Ahorra un tramo que hoy no se gasta. Deja el plan en ROI −84% y sin opción de ingreso; la tesis pasa a ser solo eficiencia ([Anexo E](05-business-case.md), escenario base con el producto diferido) |

El producto propio que maneja datos de categoría especial queda fuera sin
puntuar: su riesgo choca con la regla de datos del horizonte. Tensión a la
vista: la propuesta al Directorio esperaba los primeros casos productivos en los
productos propios, porque ahí Acme Labs decide las herramientas
([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)). La opción 1
cumple esa condición: la plataforma también es propia.

**Por qué merece la inversión, y por qué hoy no la recibe.** Es la única opción
que puede obtener una señal comercial proporcional sin datos de cliente, con el
menor esfuerzo incremental, sobre la línea de mayor margen. Esa señal no prueba
disposición a pagar: prueba interés con presupuesto y un rango de precio
aceptado como referencia. El precio y la compra se validan recién en el cierre
del mes 12, con el piloto medido. Aun así, **hoy está diferida**: el tramo de
producto solo se libera con la señal del mes 6, y hasta entonces cuesta cero. Se
compara con la alternativa 4 recién en el mes 6, con la señal en la mano. Es
reversible hasta la firma del mes 12. Quién valida los puntajes: el equipo con el
Council (**pendiente**).

### Catálogo único de decisiones

Une las puertas del [Anexo B](02-arquitectura.md) y el "Catálogo de decisiones
del Anexo C: ámbito, fecha y compromiso" del [Anexo C](03-gobierno-seguridad.md). Separa tres pasos: **aprobación interna**,
**negociación no vinculante** y **firma**. Regla del horizonte: en los 12 meses
ningún dato productivo de cliente va a un modelo, y ninguna excepción la
contradice.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto | Tipo |
|---|---|---|---|---|---|---|
| El pedido de hoy (primer tramo acotado, piso de capacidad y marco de gates) | Interno | Hoy | Directorio | Techo confirmado | Hasta 33 de caja más 6 de reserva de cierre (ampliable a 15 en el mes 3 con señal y a 17 en el mes 6 con el producto) y 72 de tiempo con la prueba chica | Reversible: cortar en el mes 3 cuesta 79 en el medio, hasta 115 hasta cerrar y 155 en el año ([Anexo E](05-business-case.md)) |
| Liberar la plataforma de los meses 4-6 | Interno | Mes 3 | Directorio | Al menos una señal: umbral contractual, anuncio de consumo o cliente para el producto | Meses 4-6: 71 / 106, contractor al 100%, gateway y pasarela | Reversible: sin señal se difiere y las lecturas de los meses 6 y 9 releen |
| Vía de IA aplicada de los meses 1-3 | Interno | Hoy | Directorio | Decisión pendiente "Vía de IA aplicada" | Contrato corto, un mes de preaviso | Reversible |
| Capacidad de los meses 4-12: replan o excepción en los meses 4-6, con el producto diferido | Interno | Hoy | Directorio | Decisión pendiente "Sobre de capacidad" | Sobre escrito por tramo de tres meses | Reversible en cada gate |
| Capacitar y reasignar en vez de contratar | Interno | Hoy | Directorio | — | — | Reversible; se revisa en el mes 6 |
| Sin crédito ni scoring; clasificación caso por caso | Producto | Hoy | Directorio | — | Alcance del año | Reversible: reabrir es decisión del cierre del mes 12, que rige después |
| Ratificar la política de IA | Interno | Meses 1-3 | Directorio | Pedido de hoy aprobado | Compromiso interno enmendable; sin firma con clientes | Reversible con costo de credibilidad; revisión anual y extraordinaria en el mes 6 |
| Postura sobre el empleo (decisión pendiente "Compromiso sobre el empleo") | Interno | Hoy o meses 1-3 | Directorio, con asesoría laboral | — | Texto comunicado | Poco reversible una vez comunicada |
| Liberar el tramo de producto | Interno | Mes 6 | Directorio | Señal comercial proporcional (interlocutor con presupuesto y rango de precio de referencia) | Producto: 38 / 34 en los meses 7-9, 21 / 23 en los meses 10-12 | Reversible en el mes 9 |
| Financiar la demostración externa | Interno | Mes 9 | Directorio | Señal contractual o producto liberado | Red team externo e ISO ampliada | Reversible |
| Modelo, proveedor, herramientas detrás del gateway | Interno | Meses 4-6 | Dirección técnica | Evals como árbitro | — | Reversible |
| Cláusula tipo de IA | Interno | Meses 7-9 | Council | Una función con ficha y supervisión humana | Texto listo | Reversible |
| Conversar la cláusula con un cliente | Negociación | Meses 7-9 | Comercial con `governance` | Sin firma, sin datos, sin compromiso | Ninguno | Reversible |
| Firmar un compromiso contractual de IA con un cliente | Externo | Mes 12 | Council | Cláusula tipo, matriz del cliente, red team sin críticos | Firmado; rige después del horizonte | **Irreversible** |
| Enviar datos productivos de un cliente a un modelo | Externo | Prohibido en el horizonte; la excepción la decide el cierre del mes 12 | Responsable comercial con el Council | Cláusula firmada, matriz, controles demostrados | Rige después del horizonte | **Irreversible** |
| Ajustar un modelo con datos de cliente | Externo | Fuera del horizonte | — | — | — | **Irreversible** |
| Subir una función del producto a "actúa con aprobación" (nivel 3) | Externo | Mes 12 | Council | Evidencia del piloto y red team externo sin críticos | Rige después del horizonte | **Irreversible** una vez activa |
| "Autónomo dentro de límites" (nivel 4) fuera de sandbox o con efectos externos | Externo | Fuera del horizonte | Council | Decisión del cierre del mes 12 para el plan siguiente | Prohibido hasta entonces | **Irreversible** |
| Hardware propio o consumo comprometido a más de 12 meses | Interno | Mes 12 | Directorio | Escenario de consumo | Contrato | **Irreversible** |

Ninguna decisión irreversible se toma antes del cierre del mes 12, y las que se
toman ahí rigen para el plan siguiente.

### Decisiones pendientes para el board o el equipo

| Tema | Tensión | Alternativas | Propuesta del CAIO | Decide |
|---|---|---|---|---|
| Sobre de capacidad | El primer tramo acotado entra en el sobre clave (~1,8 con la prueba chica, 1,6 sin ella, contra 1-2,25 FTE). Con señal en el mes 3, los meses 4-12 entran solo con el producto diferido y el replan, sin holgura ([Anexo E](05-business-case.md)) | Producto desde el mes 4, ampliando el sobre a ~3,7 FTE clave, que sale de horas facturables; o diferir el producto hasta la señal del mes 6: 2,2 / 2,2 / 2,1 con el replan de los meses 4-6 del Anexo B, o 2,5 en los meses 4-6 con la excepción acotada. Además, lectura del sobre: estricta (todo contra 1-2,25) o separada (horas distribuidas como segundo sobre) | Diferir el producto, con el replan y la excepción como respaldo; si la lectura del mes 6 trae la señal, el board decide ampliar el sobre de los meses 7-12. Lectura separada, aprobada explícitamente. Piso del sobre ≥ ~1,8 FTE en los meses 1-3, a confirmar | Board, hoy |
| Gasto de tecnología del OKR | La caja del plan suma gasto de tecnología, contra el OKR de menos de 3,5% de la facturación | Mantener el resultado clave y recortar el plan; medirlo sin la inversión del plan; o medirlo por persona activa | Medirlo sin la inversión del plan o por persona activa: el OKR mide eficiencia de la base, no la inversión. Cambia cómo se mide, no lo que se gasta: el gasto del plan se informa igual | Directorio, en el presupuesto 2027 |
| Vía de IA aplicada | IA aplicada en los meses 1-3: rol interno de 0,3 FTE (Anexo B) o el contractor desde el mes 1 al 50% (Anexos D y E) | Rol interno, si demuestra experiencia antes de la aprobación de hoy; o el contractor desde el mes 1 (recomendado), que reemplaza la fracción del Anexo B en los meses 4-12 | El contractor desde el mes 1: el recurso que no entra es el tiempo clave (1,6 contra 1,9 FTE), con ~13 mil más de caja. Choca con "no contratar" | Directorio, hoy |
| Compromiso sobre el empleo | Qué se promete sobre el empleo ([Anexo D](04-personas-cultura.md), decisión sobre el empleo) | Sin compromiso; la ganancia por IA no se usa para desvincular en 12 meses; o ese compromiso con excepciones | El compromiso con excepciones, como propone el Anexo D: baja el miedo sin atar todo el margen. No es política aprobada; el costo no está cuantificado | Directorio, con asesoría laboral |
| Meta de adopción | El 80% combinado del OKR no se alcanza ni con las metas del plan (Tecnología 85% y Operaciones habilitadas 60% dan como mucho 72,5%) | Mantener el 80% combinado, o reemplazarlo por dos métricas con denominador | Dos métricas: Tecnología ≥80% desde los meses 4-6 (OKR) y ≥85% en los meses 10-12; Operaciones habilitadas, con su valor sobre el total y el 80% combinado informados al lado. Ninguna meta propia se presenta como cumplimiento del 80% | Directorio, con el OKR 2027 |
| Staffing por hora | Staffing facturado por hora desincentiva el uso de IA ([Anexo E](05-business-case.md)) | Productividad 0 en staffing, o precio por resultado | Productividad 0 en los 12 meses; precio por resultado como opción del año 2 | Directorio, año 2 |
| Solapes de costo | Solapes de costo que quedan ([Anexo E](05-business-case.md)): pruebas de bypass (Arquitectura y Gobierno), red team (Arquitectura 5-15 contra Gobierno 10-25), gateway y pasarela, seguridad. IA aplicada e infraestructura sin piloto ya están consolidadas | Contar los dos renglones o consolidar | El base cuenta los dos hasta que confirmen los dueños | `architect`, `governance` |
| Exigencia de equilibrio | El equilibrio a régimen pide ~17% de throughput atribuible sin producto (~23% con el producto), medido contra la base del plan. Es una exigencia propia: el OKR de +20% contra el cuarto trimestre de 2026 la cubre solo si 1,20/(1+d) − 1 − c ≥ 16,7% (d, medido en el mes 3; c, el cambio del grupo que no adopta, desde el mes 6) | Subir la meta; vender la capacidad liberada (se calcula en `private/`); o apoyar el caso también en producto y riesgo, no solo en productividad | Apoyar el caso en producto y riesgo, dicho sin vueltas ante el board; vender la capacidad se evalúa en el mes 6, cuando se decide su destino | Directorio |
| Base que no resuelve | Si en la semana 4 la base prospectiva no resuelve (criterio mecánico del [Anexo B](02-arquitectura.md), "Respaldo"), el base no puede pasar la lectura del mes 6 por throughput (≈ −265 sin crédito de capacidad, ≈ −245 si se atribuye; validado por `finance`, alternativas sin costear) | Retrospectiva como lectura contra tendencia, sin atribuir (Anexo B); prolongar siempre la base a la semana 8 y correr 4 semanas la formación (Anexo B); o prolongarla solo si el criterio de la semana 4 lo dispara (Anexo D) | Sin propuesta propia todavía: prolongarla solo si el criterio lo dispara no atrasa la prueba ni el básico cuando la base resuelve, y prolongarla siempre le da a la decisión del mes 3 una lectura de σ con 5 semanas en vez de 9 ([Anexo D](04-personas-cultura.md)). Se decide antes de la aprobación de hoy | `people` con `architect` y `caio` |
| Qué restricción cuenta como señal | Qué restricción contractual cuenta como señal en la decisión del mes 3 | Lectura amplia, la del Anexo E y la [ficha del umbral](../../context/supuestos/umbral-de-evidencia-contractual.md): un contrato que prohíbe **o** condiciona la IA de terceros es señal. Lectura recortada, la del Anexo C ("Licencia para vender"): cuenta solo si condiciona, es decir, acepta la IA con controles que Acme Labs debe demostrar | Sin propuesta propia. Evidencia de la lectura amplia: es el umbral de la ficha y el texto del Anexo E, y deja más vías para liberar la plataforma. Evidencia de la recortada: el supuesto de partida ya es que los clientes prohíben por defecto; un contrato que solo prohíbe lo confirma, probablemente exista entre cinco bancos y liberaría la plataforma sin pedir nada que gobierno mínimo y formación no compre, lo que desactiva la bifurcación. Con la recortada, la ficha del umbral suma "cuenta en el mes 3 solo si condiciona" | Board, hoy |

## Cautelas

- Las fracciones de FTE, las bandas de espera, los plazos de 6 semanas, los
  costos de cierre y la separación del sobre son supuestos sin ficha propia; los
  umbrales de los gates, supuestos de cada anexo a calibrar con la base del plan.
- Los puntajes RICE de la hipótesis de producto son juicio del CAIO, sin
  medición ni validación del equipo; el outcome no tiene línea de base.
- El plazo de 6 semanas del SLO del piloto es ilustrativo del curso.
- El método del intervalo (90%, semiancho de 3 puntos, 15 personas activas como
  mínimo, supuesto de Finanzas) y el
  gate de impacto del caso de referencia (uso ≥40%, errores ≤10%) son
  propuestas del Anexo B sin medición; antes de la aprobación de hoy se comprueba
  con la serie de la preparación previa que el semiancho de 3 puntos es
  alcanzable.
- La revisión mensual del Council no tiene costo propio porque entra en las horas
  del Council que el Anexo E ya presupuesta por tramo; si el tablero pidiera
  trabajo nuevo, no sería costo cero y lo tendría que validar `finance`.
- La reserva de cierre se calcula por gate (Anexo E, "Reserva de cierre vigente"); el cierre de un corte de la revisión mensual a mitad de tramo no está calculado.
- La política de ruteo depende de la consulta escrita al proveedor (suscripción
  que permite gateway, suscripción que no lo permite o pago por consumo), que
  todavía no se hizo. La base común mínima para el producto supone el
  contractor al 50%, sin dato que lo respalde.
- La señal comercial del mes 6 (interlocutor con presupuesto y rango de precio
  aceptado como referencia) es una propuesta del CAIO: no prueba disposición a
  pagar y el rango todavía no existe.
- La enrutabilidad de cada superficie de IA no está verificada con
  documentación de proveedor: se prueba en los meses 4-6.
- La fecha del Anexo III del AI Act viene de la lectura del Anexo C, sin cotejo
  del texto consolidado; no va a una slide.
- La anonimización del caso necesita revisión de un humano autorizado: los
  alias y rangos de concentración siguen siendo inferibles para quien conozca la
  cartera. Este anexo no nombra un alias de cliente junto a un producto, pero sí
  vincula un producto propio con una habilitación externa de 2027, y las fichas
  de `context/` todavía tienen asociaciones que esa revisión tiene que juzgar.
- La rama sin señal (≈ 199) es un medio sin rango propio y no tiene techos por
  tramo en el Anexo E; los compensatorios del Anexo C que suma son una cota
  superior.
- Responsable humano de cada gate y de cada decisión: **pendiente**.
