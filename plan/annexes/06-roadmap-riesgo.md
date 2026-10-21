---
owner: caio
status: draft
title: "Anexo F — Roadmap ajustado por riesgo"
---

# Anexo F — Roadmap ajustado por riesgo

Slides que sustenta, por el nombre de su encabezado:
[Beneficio](../slides.md),
[Roadmap técnico, financiero y cultural](../slides.md),
[Costo y riesgo](../slides.md) y el cierre,
[Autorizar la validación inicial](../slides.md). Montos en k USD
(1k USD = 1.000 USD) salvo que se indique otra unidad.

> **Cifras estimadas, todavía sin validar contra fuentes internas;** se validan
> antes de liberar la ejecución de M1-M3; la validación tiene autorización propia.
> Los umbrales, bandas y plazos de los gates son
> supuestos o decisiones propuestas por el CAIO, a calibrar con la línea de base de
> los meses 1-3. Los gates son propuestas a ratificar, no resultados observados.

## Objetivo

Poner en una sola línea de tiempo los tracks técnico ([Anexo B](02-arquitectura.md)),
de gobierno ([Anexo C](03-gobierno-seguridad.md)), cultural ([Anexo D](04-personas-cultura.md))
y financiero ([Anexo E](05-business-case.md)), con dos autorizaciones iniciales
y luego un gate cada tres meses que integra las condiciones de las cuatro áreas.
El Council revisa cada mes y puede frenar o cortar; **liberar recursos requiere
una decisión explícita de la autoridad del gate**.

Sustenta **un pedido inicial de validación acotada durante la preparación de
2026**, antes de decidir la ejecución del paquete mínimo de los meses 1-3
(enero-marzo de 2027). Finanzas lo costea en el [Anexo E](05-business-case.md),
"Pedido inicial: paquete mínimo". Primero se autoriza tiempo para diagnóstico,
agendas y viabilidad; una segunda decisión puede liberar configuración, controles
y medición con herramientas existentes, sin plataforma central. El resto del año
no se aprueba hoy. Se conserva el paquete mínimo, en vez del pedido
completo de 33+6 de caja y 72+7 de tiempo, que queda solo como alternativa
(Anexo E, "Pedido completo 33+6 / 72+7 y gates económicos (alternativa)"). La
bifurcación por señal sigue como regla vigente de la opción de plataforma, que se
relee en los meses 3, 6 y 9.

La narrativa del cierre es **valor medible; seguridad aceptable; fondos por
decisión**. Las cifras vienen del anexo que se cita. Lo que este anexo agrega son
decisiones del CAIO (bandas fuera de lo económico, plazos de corrección, el
calendario, la hipótesis de producto y el catálogo de decisiones), marcadas como
propuestas. Donde dos anexos chocan, el choque va a "Decisiones pendientes para
el board o el equipo", con alternativas, propuesta y quién decide. Responsable
de cada gate y de cada decisión: a designar, con productor de evidencia,
verificador y autoridad firmante diferenciados ([Anexo C](03-gobierno-seguridad.md),
"Derechos de decisión").

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Convención de tiempo | La preparación previa es octubre-diciembre de 2026, posterior a una autorización específica; termina en la decisión que puede liberar M1-M3. Después, cuatro tramos de tres meses de 2027, con gates en los meses 3, 6, 9 y 12. El Council revisa cada mes, sin liberar fondos | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo E](05-business-case.md) |
| Patrón de gates | Kill/scale por etapa, con criterio de éxito y de abandono declarados antes de empezar | [Kill/scale gates](../../material/conceptos/m1u2-kill-scale-gates.md), [kill-fast](../../material/conceptos/m1u1-kill-fast.md) |
| Primeros 100 días | Los meses 1-3 absorben el diagnóstico y la base: inventario, línea de base, política, matriz y controles. No hay quick win de negocio medido; ver "Primeros 100 días" | [Plan de 100 días](../../material/conceptos/m1u2-plan-100-dias.md) |
| Capacidad | Utilización 83%-90% como promedio de toda la empresa, sin corte por proyecto; bench menor a 1 FTE; restricción de no contratar. El promedio no prueba que haya horas libres en los roles necesarios | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md) |
| Paquete mínimo | Entregables, horas por rol, caja y reservas como supuestos de planificación, sin precios cotizados ni agendas liberadas | [Paquete mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md), [Anexo E](05-business-case.md) |
| Clientes principales | Su continuidad es el escenario base; su pérdida parcial es estrés | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |
| Throughput | Unidad: PR aceptado por persona activa en equipos propios. Se valúa como horas evitadas a output fijo y no es caja | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| Línea de base | Base prospectiva congelada en las semanas 1-4 del plan (hasta la 8 si no resuelve); la serie de la preparación previa estima ruido y es contra la que se informa el OKR, sin atribuir | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo B](02-arquitectura.md) |

## Evidencia

### El pedido de hoy: validar antes de liberar M1-M3

El pedido completo está en el cierre del deck; la slide [Costo y riesgo](../slides.md)
muestra su exposición presupuestaria máxima autorizada. Cifras en k USD, techos propuestos por Finanzas
(Anexo E, "Pedido inicial: paquete mínimo"). La slide redondea los FTE; acá van
los rangos exactos.

| Elemento | Qué se aprueba | Fuente |
|---|---|---|
| 1. Entregables M1-M3 | Política/intake con estado actualizado, matriz de restricciones, inventario y legal focalizado; permisos, MCP y escaneo con pruebas por superficie, críticos cerrados y residual aceptado; padrón, extracción reproducible y base congelada; básico para toda la organización, intermedio de una cohorte de 15-20 personas y prueba de prácticas sobre el agente de código que ya se usa. Sin gateway, retrieval, harness central, producto, avanzado ni contractor continuo | Anexo E; [Anexo B](02-arquitectura.md), "Paquete técnico mínimo"; [Anexo C](03-gobierno-seguridad.md), "Insumo para el paquete mínimo" |
| 2. Caja M1-M3 | Legal focalizado 2-6 y provisión de herramientas/exportación 0-1,5, más 15%: 2,3-8,625; **techo 9**. Sin seats nuevos ni contractor | Anexo E |
| 3. Reserva de caja | **1**, para hasta un mes de herramientas y legal por hitos sin preaviso. Compromiso máximo de caja: **10** | Anexo E |
| 4. Tiempo M1-M3 | 970-1.350 h internas, 14,3-58,3 a costo cargado; **techo 59**. Incluye Seguridad 34-54 h: técnico de B 24-40, política de C 4-8 aparte y Council 6 | Anexo E |
| 5. Preparación previa | Técnica existente 20-40 h, techo 3; validación organizativa adicional 60-96 h, techo 5. Total 80-136 h, **techo 8 de tiempo y caja 0**, con autorización e imputación 2026 propias, sin ejecución registrada | Anexo E; [Hito inicial](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial) |
| 6. Cierre interno | 16-24 h de senior para exportar, revocar accesos y archivar; **reserva de tiempo 2** | Anexo E |
| 7. Capacidad total | **2,0208-2,8125 FTE internos** en M1-M3 (referencia 2,4167): **0,8958-1,4375 clave** y **1,125-1,375 distribuidos**. Ambas bolsas sobre las mismas personas, conciliadas por persona y semana en la matriz privada de D | Anexo E; [Anexo D](04-personas-cultura.md), "Capacidad efectiva" |
| 8. Núcleo tras un corte | Si se corta en el mes 3: 108 h en M4-M12 (36 por tramo), caja 0, **tiempo hasta 6**. Accesos, incidentes y permisos; no mantiene el experimento. Requiere aprobación explícita en el gate de salida y **no forma parte del total autorizado hoy** | Anexo E |
| 9. Marco de decisión | Las tablas de abajo como regla de liberación de fondos, con la revisión mensual del Council (que puede frenar o cortar, pero no libera fondos) y la precedencia de seguridad sobre dependencias y caja | Este anexo |

**Reserva propuesta de capacidad M1-M3:** hasta 720 h de soporte clave
(1,5 FTE de costeo), más 540-660 h de formación; máximo combinado 1.380 h.
Es un supuesto; Operaciones y los managers confirman agendas por persona y semana.

La preparación previa y el cierre condicional tienen sus propias horas y
autorizaciones, fuera de ese sobre de M1-M3.

La demanda costeada sigue en 970-1.350 h **si se confirman las uniones de horas de B, C
y D que propone Finanzas**; sus dueños todavía no las ratificaron, y sin la de DevOps
el tiempo pasa el techo de 59 (ver "Decisiones pendientes"). La reserva de 1.380 h
es una propuesta, no disponibilidad demostrada. Las 30 h de margen sobre el máximo
clave requieren costeo y autorización antes de usarse; no sustituyen el hito
de validación organizativa ([fuente](../../context/supuestos/paquete-minimo-de-aprendizaje.md#reserva-propuesta-de-capacidad-m1-m3)).

**Primera autorización propuesta: caja 0 y tiempo hasta 8.** Una segunda decisión
puede liberar hasta **71 adicionales: caja 10 y tiempo 61**, incluidas reservas.
La exposición presupuestaria máxima autorizada del tramo, acumulada hasta
cerrar en M3, es **79 = caja 10 + tiempo 69**
(59 de M1-M3 + 3 de técnica + 5 de organización + 2 de cierre), sin deducir
beneficios; **85 en el año** si se aprueba el núcleo al salir. Son límites de
autorización de recursos, no pérdida económica incremental ni salida de caja, y no
cuantifican la contribución comercial desplazada, que sigue sin medir
([Anexo E](05-business-case.md#conclusión-económica)). El tiempo no es nueva nómina ni
pago externo. Fuera del pedido: los meses 4-12, la plataforma, el producto, el
modelo propio, compromisos a más de 12 meses y todo compromiso con clientes.
También queda fuera la excepción externa de facilitación (16-32 h): si se
activa, el Directorio la aprueba aparte del techo, con cotización, y suma su
caja a los 79 ([Anexo D](04-personas-cultura.md)).
El techo de caja se confirma contra el presupuesto 2027 en privado.

**Antes de liberar M1-M3**, el board recibe: diagnóstico revisado con brechas y
faltantes explícitos; alcance y techos definidos; horas por rol
liberadas en la matriz privada, con trabajo desplazado y recuperación; vía de IA
aplicada interna demostrada (8-16 h) y perfil de facilitación (16-32 h) o la
excepción externa decidida; acta de viabilidad del protocolo y decisión de
calendario; versión, acta, alcance y aprobación documentada de la política
revisados ([Anexo C](03-gobierno-seguridad.md)); controles aplicables probados
antes de usar cada superficie; las
uniones de horas de B, C y D confirmadas o el tramo recosteado; la lectura del sobre
de capacidad (estricta o separada) para decidir, y la contribución desplazada que
estime la matriz, informada sin umbral propio, y la decisión humana sobre qué rige
para el uso que ya corre sobre clientes hasta tener su matriz (ver "Decisiones
pendientes"). Si falta
algo, se reduce o difiere y se vuelve a costear; el presupuesto no libera tiempo por sí solo.
La autorización económica permite producir base y controles; cada superficie
requiere dictamen, restricciones y pruebas aplicables antes de habilitar usos.

### Validación inicial y dos liberaciones

Propuesta elegida por Martín para el borrador, pendiente de acuerdo del equipo y
autorización empresarial. Los roles de Acme Labs están a designar; los responsables
humanos de las secciones del TP no los sustituyen. Fuente de horas y costos:
[validación inicial](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial).

| Decisión | Condición y evidencia | Autoridad y límite |
|---|---|---|
| Primera liberación, preparación 2026 | Agendas, accesos, trabajo desplazado e imputación presupuestaria de la propia preparación confirmados; alcance acotado y personas designadas para producir, verificar y firmar | Directorio o autoridad formalmente delegada; diez días hábiles, 80-136 h, caja 0 / tiempo hasta 8 |
| Segunda liberación, antes de M1 | Diagnóstico revisado; padrón y matriz persona/semana conciliados para soporte y formación; desplazamiento y recuperación explícitos; acta de viabilidad y protocolo; roles diferenciados; alcance recosteado y presupuesto 2027 comprobado | Directorio o autoridad formalmente delegada decide continuar con alcance validado, reducir/resecuenciar o detener; hasta 71 restantes, no automáticos |

Los días 1-4 contrastan documentos y 4-6 entrevistas focalizadas; los días 2-7
concilian padrón y agendas; los días 4-8 confirman políticas, restricciones y
responsabilidades y preparan la cotización legal; los días 7-9 concilian costos y
solapes y verifican los entregables; el día 10 se documenta la decisión. La
preparación técnica existente corre en paralelo. Son ventanas superpuestas de un
alcance acotado, sin promesa de validación exhaustiva ni iteraciones ilimitadas.

El CAIO coordina; Operaciones y managers liberan agendas; Finanzas concilia costo
cargado, contribución desplazada y presupuesto; Seguridad conserva la facultad de
suspender. Quien produce, quien verifica y quien firma son personas distintas.
El dictamen legal externo sigue dentro de M1-M3: preparar su alcance y pedir
cotización no compromete servicios pagos; si el proveedor cobra, se requiere otra
autorización antes de contratar.

No hay formación, prácticas nuevas, compras ni despliegues en la primera etapa.
La preparación técnica usa lectura y exportación autorizadas de registros
existentes. Los controles necesarios no se postergan para proteger una medición:
se registra el cambio y se preserva o revisa la base con Arquitectura.

**Corte temprano:** si la evidencia no sostiene el alcance o vence el plazo sin
resolver bloqueantes, no se libera el resto. Se reduce/resecuencia con recosteo,
o se detiene con el costo efectivamente trabajado, hasta 8 de tiempo y caja 0.
El cierre documental está incluido; al no desplegar ni contratar, no se activa
el cierre técnico de M1-M3. Una ampliación requiere aprobación previa.

Las dos bolsas son disjuntas: 8 de preparación más 71 del resto del diseño,
incluidas reservas, totalizan 79. La segunda decisión descuenta cualquier tarea
equivalente ya financiada; no vuelve a autorizar la primera. La agenda previa
no consume las 720 h ni el margen de 30 h de M1-M3.

**Calendario de controles.** El [Anexo C](03-gobierno-seguridad.md) conserva las
pruebas y compensatorios en M4-M6 y deja adelantarlos a M1-M3 como opción pendiente
de validar horas, costo y capacidad ("Calendario conservado"). El paquete mínimo
los costea en M1-M3 porque ningún uso nuevo se inicia sin prueba. Si la validación
falla, ese uso no se inicia ni se amplía en M1-M3 y la prueba de prácticas espera.

### Calendario único de la preparación previa y los meses 1-3 (decisión del CAIO)

| Cuándo | Qué | Quién verifica | Costo |
|---|---|---|---|
| Preparación, octubre-diciembre de 2026, después de la primera autorización | Diagnóstico y matriz privada de capacidad; acta de viabilidad de datos: extracción reproducible, diccionario, enlaces, cohorte, precisión y lectura simulada. Protocolo único de B congelado. Estado de política y restricciones confirmado; alcance/cotización legal preparados | Productor, verificador y firmante distintos, a designar; el Directorio recibe el resultado antes de liberar M1-M3 | Hasta 8 de tiempo (80-136 h), caja 0 |
| Semanas 1-4 del plan | **Base prospectiva congelada** con la unidad del Anexo B, antes de cualquier formación, práctica o herramienta nueva. Política/intake, matriz, inventario y legal focalizado arrancan en paralelo | Productor: oficina del CAIO; verificador distinto, a designar | Dentro de M1-M3 |
| Semanas 5-13 (o 9-13 si la base se extiende) | Básico para toda la organización, intermedio de la cohorte y prueba de prácticas sobre repositorios que la matriz habilite, solo en superficies con controles probados | Gobierno, Personas, Arquitectura | Dentro de M1-M3 |
| Meses 4-12 | Continuidad condicional sin plataforma; descubrimiento del asistente antes del mes 6; opción de plataforma releída en los meses 3, 6 y 9 | Oficina del CAIO | Techos por gate |

**Base que no resuelve.** Si en la semana 4 la base no resuelve (criterio mecánico
del [Anexo B](02-arquitectura.md), "Respaldo"), se extiende a la semana 8 y **se
desplazan juntos el básico, el intermedio y la prueba a la semana 9**: mover solo el
intermedio no protege la base. La meta de completitud del básico en el mes 3
(≥90%) se revisa con ese calendario más corto, sin presentarla como lograda por
asistencia. La retrospectiva nunca atribuye ganancia ni libera capital
([convenciones](../../context/supuestos/convenciones-de-calculo.md)). B, D y E
coinciden en mover los tres si se extiende; cuándo extender sigue abierto (F,
"Base que no resuelve" en Decisiones). Requiere ratificación.

**Qué cuesta extender la base.** Quedan cinco semanas (9-13) para formación y
prueba, en lugar de nueve (5-13), y la evidencia madura tarde: un PR se lee a
los 14 días y la calidad a los 30 ([Anexo B](02-arquitectura.md), "Calendario de
prerrequisitos"). La prueba de prácticas queda con unas 3 semanas de PR maduros
al cierre del mes 3, contra unas 7 en el calendario base; es una cuenta de
calendario, no una medición. La facilitación se concentra y el básico tiene
menos tiempo para llegar al 90%. Hay dos salidas: aceptar la compresión y
declarar reducida la lectura del mes 3, sin atribuir ganancia; o correr la
lectura de la prueba hasta 4 semanas después del mes 3, con impacto en el
arranque de M4. Adelantar el básico queda descartado, porque ninguna
intervención entra en la base. B pide que CAIO, Personas y Finanzas ratifiquen
el calendario de lectura y el costo de cualquier desplazamiento. La elección queda
abierta en "Decisiones pendientes para el board o el equipo".

### Primeros 100 días: por qué no hay quick win de negocio en los meses 1-3

El método del plan de 100 días pide 2-3 quick wins con valor medido entre los días
31 y 70 ([Fuente](../../material/conceptos/m1u2-plan-100-dias.md)). El plan se aparta a
propósito y reconoce el costo: **posterga a la lectura del mes 6 el primer
aprendizaje de valor**. La rampa base es 0% en los meses 1-3
([rampa](../../context/supuestos/rampa-de-la-ganancia.md)), así que el mes 3 no
promete atribución.

- **Sin plataforma en los meses 1-3.** El paquete mínimo usa las herramientas
  existentes; el gateway no mide valor sin harness ni evals, y la opción de
  plataforma se evalúa en los meses 3, 6 y 9.
- **La prueba de prácticas, dentro del mínimo.** Sobre la cohorte del intermedio
  (15-20 personas), con el agente de código que Tecnología ya usa, después de
  congelar la base y en repositorios que la matriz habilite. Se lee en el mes 3
  como aprendizaje (uso, retrabajo, PR aceptados y dispersión), sin atribuir
  ganancia. Se suspende si sube el retrabajo, si falla un control o si la matriz
  no habilita repositorios.
- **Precondiciones.** Sin matriz ni inventario no se sabe qué datos se pueden usar.

Lo que se entrega al día 90: política aprobada con respaldo documental revisado y aplicación registrada, matriz
de restricciones, inventario, controles probados por superficie con residual
aceptado, base congelada con cobertura y faltantes, básico con su porcentaje de
cobertura y la lectura de la prueba. Lo primero que puede pedir un banco son la
política y la matriz.

### Revisión mensual del Council

**El riesgo se mira cada mes; los recursos se liberan por decisión.** Tras las
dos autorizaciones iniciales, los gates son trimestrales. Entre gate y gate,
el AI Council hace una revisión mensual de 2 horas con un tablero: caja y tiempo
consumidos contra el techo del tramo, uso semanal por área, incidentes y secretos
expuestos, señales de plataforma (contrato, precio por consumo, cliente) y avance
de hitos. Es la misma reunión en la que el Council revisa el registro de riesgos
([Anexo C](03-gobierno-seguridad.md), "Ritmo operativo").

- **Qué puede hacer:** frenar o cortar un frente, activar una contingencia,
  registrar una señal en el mes en que llega y escalarla al Directorio.
  **Seguridad puede suspender el uso afectado** aunque el gasto o la adopción
  parezcan cumplir ([Anexo C](03-gobierno-seguridad.md), "Derechos de decisión").
- **Qué no puede hacer:** liberar fondos. Eso queda en los gates.
- **Qué no cambia:** las esperas de 6 semanas y el método de medición. Un mes no
  tiene señal estadística: el tablero muestra el throughput como tendencia.
- **Costo:** el paquete mínimo reparte 30 h de Council en M1-M3 (tech lead 12,
  seguridad 6, staff 12) y la continuidad lo incluye en sus horas por tramo
  ([Anexo E](05-business-case.md)). Si el tablero pidiera trabajo nuevo, lo
  valida Finanzas; no se afirma costo cero fuera de esas horas.

### Línea de tiempo integrada

**Dos liberaciones iniciales y luego gates en los meses 3, 6, 9 y 12. Cada mes:
revisión del Council con poder de corte, sin liberar fondos.** Techos en k USD, caja / tiempo
([Anexo E](05-business-case.md)). Los meses 4-12 **no se aprueban hoy**. Sus techos
pagan controles, seguimiento, lectura y el descubrimiento del asistente; no compran
construcción de producto, plataforma, cohortes nuevas, avanzado ni champions al 10%
([Anexo E](05-business-case.md), "Pedido inicial"). Las metas culturales de los meses
4-12 son propuesta del Anexo D sobre un
[supuesto de metas culturales](../../context/supuestos/metas-culturales-propuestas.md)
en borrador: se informan y no se compran con estos techos. Los hitos ampliados exigen
nueva autorización y no pasan al año 2 por defecto.

| Tramo | Técnico y datos | Gobierno y seguridad | Cultural | Financiero: techo caja / tiempo |
|---|---|---|---|---|
| Preparación previa, con autorización propia | Acta de viabilidad; protocolo congelado | Estado de política y restricciones; roles y cotización legal | Diagnóstico y matriz privada; agenda 2026 propia | **0 / 8**, primera liberación |
| Meses 1-3: diagnóstico, base, política, formación y prueba | Configuración de herramientas existentes; extracción y base; prueba de prácticas | Política/intake, matriz, inventario, legal focalizado; controles probados por superficie | Básico para todos; intermedio de la cohorte | **9 / 59**, más reserva de caja 1 y de cierre 2 |
| Meses 4-6: continuidad y descubrimiento | Mantener controles y medición; descubrimiento del asistente (tiempo a primera integración exitosa), sin construir; plataforma solo con decisión y costeo propios, si se cumplen regla y condiciones | Pruebas y residuales con vencimiento; lectura de señal contractual | Seguimiento de adopción con denominadores. Champions, avanzado, cohortes nuevas y estudio del rol: programa ampliado, con costeo y autorización propios | 2 / 14, condicional |
| Meses 7-9: continuidad; producto solo con otra decisión | Controles y medición. Producto: decisión y costeo propios, con base y señal del mes 6 y ruta técnica previa; sin plataforma no hay piloto en estos meses ([Anexo B](02-arquitectura.md)). Sin fecha prometida | Amenazas de la función, si existe; cláusula tipo sin firma | Seguimiento de adopción. Casos por rol y ruta del rol: programa ampliado | 2 / 11, condicional; no incluye producto |
| Meses 10-12: evaluación y traspaso | Lectura contra la base; traspaso y salida documentada | Revisión de residuales; irreversibles para después | Metas propuestas informadas (Tecnología ≥85%; Operaciones habilitadas ≥60%), sin formación nueva en el techo | 2 / 11, condicional |

**Tres dimensiones que dependen entre sí.** El [roadmap tridimensional](../../material/conceptos/m3u4-roadmap-tridimensional.md)
pide que lo técnico, lo financiero y lo cultural avancen en paralelo porque se
condicionan; los principios de gobernanza ética que el curso suma a ese roadmap
viven acá en la columna de gobierno. En este plan, las dependencias que mueven
fechas o fondos son estas:

| Si se atrasa o falla | Qué arrastra | Regla |
|---|---|---|
| Base congelada (técnico) | Básico, intermedio y prueba (cultural); la lectura de throughput que libera fondos (financiero) | Formación y prueba arrancan después de congelar; extensión a la semana 8 desplaza las tres juntas |
| Política y matriz (gobierno) | Repositorios habilitados para la prueba; frente producto | Sin matriz no hay prueba en ese repositorio; la aprobación de la política no habilita por sí sola el producto: su alcance aplicable y los controles deben verificarse |
| Cohorte activa y tiempo liberado (cultural) | La lectura del throughput (financiero) | Con menos de 15 personas activas no se decide por valor: cuenta como espera |
| Agendas y horas por rol (cultural y financiero) | Cualquier actividad del tramo | Sin horas liberadas por rol, la actividad no se inicia |
| Postura sobre el empleo comunicada (cultural) | Participación franca en el estudio del rol | El estudio es alcance ampliado: no arranca antes de esa comunicación ni sin horas y autorización propias ([estudio del rol](04-personas-cultura.md#estudio-de-impacto-sobre-un-rol-crítico-propuesta)) |
| Techo del tramo (financiero) | Alcance técnico del tramo siguiente; horas de formación, solo si se autorizó el programa ampliado | Excedido, la continuidad exige costeo nuevo aprobado |

Las actas de los meses 3, 6 y 9 dejan además una línea con lo que se probó y no
funcionó, como práctica de cultura de innovación del [Anexo D](04-personas-cultura.md);
no suma costo ni hito.

**Sin plataforma, la base no es "solo política".** En cualquier tramo sin
plataforma central rige gobierno mínimo **más compensatorios aplicables probados
por superficie**, según el [Anexo C](03-gobierno-seguridad.md), "Controles según la
decisión del mes 3": fuentes y repositorios habilitados, datos propios o sintéticos,
permisos/MCP acotados, sin credenciales productivas, escaneo local, prueba
adversarial y revisión humana, con **críticos cerrados** y residual aceptado según
autoridad. El requisito se prueba antes de usar, no después de extender. Una
superficie que no puede cumplir se excluye; no se declara cubierta por un gateway.

**Si se libera plataforma o producto**, su alcance, calendario y techos se
vuelven a costear antes de liberar: no se copian los tramos del paquete completo
(71/106, 59/78, 95/69, ni el producto 38/34 y 21/23 de ese paquete). Ninguna
proyección de continuidad es autorización anual: continuar el mínimo todo el año
proyecta ≈70 (27-113) económicos, con suma de techos 118 y hasta 121 con salida,
incluida una sola vez la validación organizativa adicional.

### Gates por condición (pasa, espera, corta)

Los gates son la primera autorización de preparación, la segunda antes de M1 y
los meses 3, 6, 9 y 12. **Solo los gates
liberan fondos.** Un "espera" libera solo lo que dice la fila y fija un plazo.
Cuatro términos que no son sinónimos: **corte** (el frente deja de financiarse y
queda el núcleo), **suspensión** (se frena un uso o gasto puntual y se vuelve a
medir), **mantenimiento** (el frente sigue sin escalar) y **excepción** (el board
aprueba algo fuera de lo previsto). Bandas económicas: [Anexo E](05-business-case.md);
el resto, propuesta del CAIO sobre los umbrales de los Anexos B, C y D.

**Regla de precedencia (propuesta de Finanzas, adoptada).** Si un corte alcanza
a la base y otro frente sigue, se aplica en este orden: **seguridad** (los
controles y el núcleo no se cortan mientras un uso opere), **dependencias** (el
frente que sigue conserva lo que usa) y **caja** (el resto se corta, con su cierre).

**Cómo se lee el throughput (método del [Anexo B](02-arquitectura.md),
"Throughput: unidad, cohorte y conversión").** Cambio relativo apareado por persona activa contra su base
congelada, con pesos de estrato y descontando el cambio de un grupo que no adopta
o la tendencia de la preparación previa. Intervalo *bootstrap* por persona, 2.000
réplicas, 90% bilateral. **Pasa si el límite inferior es mayor o igual al
umbral**; el estimado ubica la banda. Con muestra insuficiente (menos de 8
semanas o semiancho mayor a 3 puntos, con al menos 15 personas activas) no se
decide por valor: cuenta como espera. **Calidad primero**, con los tres casos
del Anexo B: **daño** (el intervalo del aumento de retrabajo o incidentes queda
entero sobre cero) corta aunque el throughput pase; **incierta** (sin daño, pero
sin probar que no empeora) cuenta como espera y, vencida, como no pasa; solo con
**no deterioro demostrado** (el aumento posible queda bajo el margen δ de B) el
gate decide por throughput. En este anexo, "sin deterioro" significa ese tercer
caso, no solo la ausencia de daño. Bases cero: tratamiento del Anexo B, sin pseudoconteos ni
datos inventados. Datos faltantes se reportan "sin medir".

**El paso no está asegurado.** Con estimados de +3,75% y +9% y semiancho de 3
puntos, los límites inferiores son +0,75% y +6%, debajo de +3% y +8%. Pasarían
solo con semianchos ≤0,75 y ≤1 punto. Es aproximación de planificación: el
bootstrap real puede ser asimétrico y decide su límite inferior. N≥15 y ocho
semanas no garantizan pasar. Además, con la cohorte y los datos reales la medición
puede no distinguir la mejora: si la precisión esperada no sostiene el método, se
reformula antes de la segunda liberación o el caso se presenta como espera y corte,
sin prometer que más semanas lo resuelvan ([Anexo B](02-arquitectura.md), "Viabilidad").

**Qué familia de indicador lee cada gate.** La
[estrategia de IA a 12 meses](../../material/conceptos/m3u4-estrategia-12-meses.md)
conecta la IA con el negocio por tres familias de KPI. Esta tabla ordena por familia
lo que mira el board en cada gate. Suma métricas de seguimiento que no están en la
tabla de gates de abajo: de los Anexos D y E, Operaciones habilitadas ≥40% y destino
de la capacidad liberada (mes 6), y Tecnología ≥80% sostenido, pedidos con ejemplos
≥30% y costo por PR aceptado que no sube (mes 9); de la columna de gobierno de este
anexo, residuales revisados (mes 12). En este anexo esas métricas se informan y no
liberan ni cortan fondos; si tienen consecuencia, la fija el anexo de su dueño:

| Gate | Adopción interna | Impacto financiero | Calidad |
|---|---|---|---|
| Mes 3 | Básico ≥90%; cohorte activa de al menos 15 | Caja y tiempo dentro del techo; consumo dentro de los techos | Base congelada; controles probados, críticos cerrados |
| Mes 6 | Tecnología ≥80%; Operaciones habilitadas ≥40% (intermedia) | Límite inferior ≥ +3%; destino de la capacidad liberada | Retrabajo e incidentes sin deterioro; cobertura de controles |
| Mes 9 | Tecnología ≥80% sostenido; pedidos con ejemplos ≥30% | Límite inferior ≥ +8%; costo por PR aceptado que no sube | Incidentes y retrabajo sin aumento; SLO y cero cruces de tenant si hay producto |
| Mes 12 | Metas propuestas: Tecnología ≥85%; Operaciones habilitadas ≥60% | Año 2 decidido y costeado aparte | Residuales revisados |

Adopción no equivale a valor: un uso alto sin mejora de throughput o calidad se
lee como uso de trámite. Las métricas financieras y su dueño están en el
[Anexo E](05-business-case.md#métricas-financieras-que-se-leen-en-cada-gate); las de
adopción y comportamiento, en el [Anexo D](04-personas-cultura.md). Si el estudio del rol
crítico se autoriza aparte, su diagnóstico entra como evidencia de qué tareas se
aumentan, no como condición de pase.

| Gate | Condición | Pasa | Espera (plazo) | Corta o falta | Fondos que afecta |
|---|---|---|---|---|---|
| Primera liberación | Agenda e imputación 2026 confirmadas; alcance, accesos, productor, verificador y firmante definidos | Preparación autorizada por diez días hábiles | Sin capacidad previa, no empezar | No hay trabajo gratuito ni autorización implícita por presupuesto 2027 | Preparación: 0 / 8 |
| Segunda liberación, antes de M1 | Diagnóstico y capacidad revisados; vía de IA aplicada y facilitación demostradas; acta y protocolo; presupuesto 2027, alcance y techos conciliados | Autorizar base y controles de M1-M3; prácticas condicionadas a habilitación por superficie | Reducir/resecuenciar y recostear antes de ejecutar | Detener: costo trabajado hasta 8; cierre documental incluido | Hasta 71 restantes: M1-M3 9 / 59, reserva 1 de caja y 2 de cierre; acumulado 79 |
| Mes 3 | Base congelada con fecha, cobertura y faltantes | Congelada | Historial insuficiente: 6 semanas más, sin atribuir | Sin base al vencer: no se decide por valor; se reformula antes de continuar | Continuidad M4-M6 |
| Mes 3 | Política aplicada, con el respaldo de aprobación revisado antes de M1 y su alcance aplicable al producto | Aprobación documentada y cobertura aplicable al producto | Respaldo o alcance pendientes: 6 semanas; sin casos nuevos | Sin respaldo o cobertura demostrados al vencer: sin frente producto en el año | Producto |
| Mes 3 | Matriz habilitante de los clientes principales | Completa | Ambiguos: *default-deny* y revisión legal hasta el mes 4 | Más de 30% ambiguo al mes 4: sin piloto con ese cliente | Producto |
| Mes 3 | Básico ≥90% con evaluación práctica (meta revisada si la base se extendió) | ≥90% | ≥50% y <90%: se rediseña el formato | <50%: cambio de formato, no se repite el curso | En el mínimo, ninguno: no hay cursos después del mes 3, y el rediseño se vuelve a costear antes de comprometer horas nuevas. Horas de M4-M6, solo si se autorizó el programa ampliado |
| Mes 3 | Controles por superficie: críticos cerrados, residual aceptado | Probados | — | Control obligatorio incumplido: se suspende el uso afectado | Uso de esa superficie |
| Mes 3 | Consumo dentro de los techos | Dentro | — | Excedido: continuidad solo con costeo nuevo aprobado | M4-M6 |
| Mes 3 | Opción de plataforma: señal (ver definición abajo). Regla vigente: la señal libera evaluar la plataforma. Propuesta pendiente de ratificación: además, brecha documentada, alternativas comparables, economía incremental o pérdida de aprendizaje aceptada, y capacidad demostrada | Con regla vigente: señal. Con la propuesta ratificada: señal más las cuatro condiciones, con reserva y contrato para el compromiso nuevo | — | Sin señal: continuar el mínimo costeado y releer M6/M9. Si se ratificaron las cuatro condiciones, la falta de cualquiera impide liberar plataforma. Si no se ratificaron, elevar decisión bajo la regla vigente y volver a costear. No pasa al año 2 por defecto | Plataforma, a costear |
| Mes 6 | Throughput, calidad primero | Límite inferior ≥ +3%, sin deterioro de calidad | **Suspensión.** Estimado >0% sin pasar, calidad incierta o muestra insuficiente: una espera de 6 semanas con subtramo propio aprobado (64-106 h; techos 1 / 6); si sigue en la banda, corte del frente interno: 102 hasta cerrar, 105 en el año | Estimado ≤0% o daño: corte del frente interno; queda el núcleo | M7-M9 |
| Mes 6 | Adopción de Tecnología, con cobertura y denominador publicados | ≥80% | **Mantenimiento.** ≥60% y <80%: la formación se rediseña y se vuelve a costear antes de comprometer horas nuevas | **Suspensión**, solo si se autorizó el programa ampliado: <60%, se frenan sus horas de formación que no sean rediseño. En el mínimo: rediseño y recosteo, sin horas que frenar. Adopción no equivale a valor | En el mínimo, ninguno. Horas de formación M7-M9 del programa ampliado, si se autorizó |
| Mes 6 | Controles: cobertura por superficie probada; críticos cerrados; residual aceptado. Si hay gateway y se declara cobertura de precio: *fc* × *s* contra el umbral, calidad y portabilidad del Anexo B | Cumplidos | Superficie no cubierta: se declara y escala al Council | Sin prueba económica, se retira el beneficio de precio; conservar un gateway exige justificar control frente a la alternativa menor | Uso y plataforma |
| Mes 6 | Producto: problema observado, base de tiempo a primera integración exitosa y métrica principal acordadas antes de liberar; comparación con documentación/soporte; señal comercial escrita (ver "Hipótesis de producto") | El board decide volver a costear y liberar construcción | — | Sin evidencia: diferir. Sin plataforma ni ruta técnica alternativa diseñada y costeada, no se promete M7-M9 | Producto, a costear |
| Mes 9 | Throughput, calidad primero | Límite inferior ≥ +8%, sin deterioro de calidad | **Mantenimiento.** Estimado ≥ +5% sin pasar. Propuesta a ratificar: una sola espera de 6 semanas, sin expansión, con subtramo propio aprobado (techos 1 / 6); al vencer, si no pasa valor/calidad con la versión congelada, corte del frente interno: 115 hasta cerrar, 116 en el año | Estimado < +5%: corte del frente interno; precedencia si otro frente sigue | M10-M12 |
| Mes 9 | Producto, si existe: SLO acordado, cero cruces de tenant, críticos cerrados | Cumplidos | SLO incumplido: vuelve a "asiste" y se revisa | Una filtración: se cancela la función | Producto |
| Mes 9 | Señal tardía de plataforma | Se evalúa con calendario y costo nuevos | — | No se usa la promesa del itinerario original | Plataforma |
| Mes 12 | Metas propuestas (Tecnología ≥85%; Operaciones habilitadas ≥60%); ambos denominadores y el combinado original informados | Se informan | Se informa contra el OKR | — | Ninguno: se informan |
| Mes 12 | Año 2: interés contractual en el producto, o lecturas de valor que pasaron en los meses 6 y 9 (propuesta del CAIO) | El board decide y costea el año 2 aparte | — | Sin ninguna: no se financia el año 2; no pasa por defecto | Año 2, a costear |

**Una sola definición de señal (texto del [Anexo C](03-gobierno-seguridad.md),
"Licencia para vender").** Restricción incluye prohibición o condicionamiento,
conforme a la [fuente del umbral](../../context/supuestos/umbral-de-evidencia-contractual.md).
Una prohibición pura se cumple excluyendo el uso afectado y no libera plataforma.
La regla vigente libera ante señal; se propone agregar brecha documentada,
alternativas equivalentes, economía incremental o aprendizaje con pérdida aceptada
y capacidad demostrada. Estas cuatro condiciones requieren ratificación del
Council y del Directorio; firma una persona designada con autoridad registrada. Ni una
señal ni el anuncio de precio demuestran que la inversión se pague
([Anexo E](05-business-case.md), "Gateway: suscripción contra consumo").

**Regla de riesgo residual.** Ningún gate pasa con un residual en la franja "no se
acepta" del [Anexo C](03-gobierno-seguridad.md); los residuales aceptados llevan
fecha de revisión. Seguridad antes que dependencias y caja.

**Casos de prueba:**

- **Sin señal en el mes 3:** sigue el mínimo costeado; las lecturas de los meses 6
  y 9 releen señales. Una señal entre gates se registra en su mes y espera al gate.
- **Throughput de +6% con semiancho 3:** pasa el mes 6 (límite +3%); en el mes 9
  queda en mantenimiento: una sola espera de 6 semanas, sin expansión (propuesta a
  ratificar); si al vencer no pasa con la versión congelada, corta el frente interno.
- **Pesimista (+0,5% en el mes 6):** espera; a las 6 semanas sigue debajo de +3%
  y se corta el frente interno: hasta 102 hasta cerrar (13 / 89), 105 en el año.
  95 es el máximo con corte inmediato al cierre del mes 6, sin espera.
- **Control incumplido en cualquier mes:** Seguridad suspende el uso afectado sin
  esperar al gate; reanudar exige prueba corregida, verificación independiente y
  residual aceptado.

### Escenarios

Para el paquete mínimo, el [Anexo E](05-business-case.md) no presupuesta
beneficios: **beneficio de caja estimado: 0; ingreso nuevo: 0**; capacidad sin
cifra hasta medir. Por eso los escenarios se expresan como exposición
presupuestaria máxima por punto de salida, no como ROI. Al cortar en M3 coincide con la exposición
presupuestaria máxima autorizada del tramo (79); los demás puntos no están autorizados hoy. El ROI económico modelado sin beneficios es −100% por
construcción (beneficio presupuestado 0): no es un resultado observado y no mide
pérdida económica observada ni caja.

| Escenario | Qué pasa | Hasta cerrar, caja / tiempo → económico | Máximo del año |
|---|---|---|---|
| Corte antes de M1 | La validación inicial no sostiene el alcance | 0 / 8 → **8**, cierre documental incluido | **8** |
| Corte en el mes 3 | La base no resuelve, falla un control o no hay agendas | 10 / 69 → **79** | **85** con núcleo aprobado al salir |
| Corte inmediato en el mes 6 | Estimado ≤0% o daño | 12 / 83 → **95** | **99** |
| Pesimista con la regla | Espera en el mes 6, vence y corta | 13 / 89 → **102** | **105** |
| Corte en el mes 9 | Estimado < +5% | 14 / 94 → **108** | **110** |
| Espera en el mes 9 (propuesta a ratificar) | Vence sin pasar y corta | 15 / 100 → **115** | **116** |
| Éxito: continuidad todo el año sin plataforma | Pasan los gates | 15 / 103 → **118** sin gastar reservas; 16 / 105 → **121** con cierre | Proyección ≈70 (27-113); no autorizado hoy |
| Con señal y, si se ratifican, las cuatro condiciones | Respuesta mínima de plataforma | A costear antes de liberar | Sin cifra: no se hereda 394/≈400 |

Las salidas son límites por suma de techos, sin restar beneficio. La diferencia
entre cortar a tiempo y seguir sin frenar es lo que compran los gates.

**Qué hay en la mano si sale bien.** Si pasan los gates, el mínimo sigue todo el
año sin plataforma, con costo económico proyectado ≈70 (27-113) y techos de 118
sin gastar reservas, 121 con cierre ([Anexo E](05-business-case.md), "Insumos para el deck"). Al mes 12 el
board tiene base congelada, lecturas de throughput y calidad con su intervalo en
los meses 6 y 9, controles probados por superficie con residual aceptado,
adopción por área con su denominador y la decisión del año 2 tomada con esa
evidencia. No es ingreso ni caja: el plan no presupuesta beneficios, y una
mejora medida se convierte en plata solo si se vende o evita una contratación.

**Referencia del paquete completo (alcances distintos, pendientes de homogeneizar).**
47/161/≈199/394/≈400/471 son costos publicados de alcances distintos
([Anexo E](05-business-case.md), "Costos publicados de alcances distintos,
pendientes de homogeneizar"). En ese paquete, ni el optimista recuperaba su costo
en 12 meses (base −332, ROI −84%; optimista sin producto −280). No se trasladan su
capacidad (62) ni su retorno al mínimo. En el mes 3 se comparan gastos futuros
evitables desde el historial común, sin costos hundidos.

### Contingencias

Cualquier contingencia la puede activar la revisión mensual del Council en el mes
en que aparece el disparador; lo que requiera fondos nuevos espera al gate.

| Disparador | Contingencia | Fuente |
|---|---|---|
| El proveedor pasa a cobrar por consumo | Se registra como señal; con plataforma liberada, se prueba si ruteo, caché y topes bajan el gasto elegible, lo que depende del régimen del proveedor; a más de 6× efectivo sin mitigar, se congela la expansión. A 12×, 211-267k USD al año es un escenario: el consumo de septiembre valorizado a precio de API, si se mantiene y se cobra; no es consumo facturado ni pronóstico. Exposición de la empresa, con o sin plan | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| Falta perfil interno de facilitación del básico | Comparar liberar un facilitador interno contra una intervención externa acotada de 16-32 h que **reemplace** esa fila, sin sumar ambas; precio, caja y preaviso requieren cotización y la excepción la decide el Directorio. Sin vía demostrada, diferir el módulo y volver a costear | [Anexo D](04-personas-cultura.md) |
| Falta perfil de IA aplicada (8-16 h) o verificador independiente | No iniciar el hito afectado; reducir o volver a costear. Un 0,3 interno no reemplaza a un especialista | [Anexo E](05-business-case.md), [Anexo D](04-personas-cultura.md) |
| Pérdida parcial del cliente principal | Se congelan los gates de los meses 4-12 hasta revisar el techo | [Anexo E](05-business-case.md) |
| Incidente de datos de un cliente | Seguridad suspende la IA sobre ese cliente y avisa según lo que pida su contrato; plazos y severidades los fija el plan de incidentes de M1-M3, y C todavía no les da valores | [Anexo C](03-gobierno-seguridad.md), "Incidentes antes del plan de M1-M3" |
| Primer secreto expuesto | Revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo | [Anexo C](03-gobierno-seguridad.md) |
| Se va una persona clave sin suplente | Se congelan altas de casos de riesgo alto y se baja el alcance del tramo siguiente | [Anexo C](03-gobierno-seguridad.md) |
| Si el estudio del rol se autoriza aparte: el rol no valida el mapeo al cierre de su tramo, o se lee como paso previo a un recorte | Se vuelve al flujo de delivery como único insumo del rol; la postura sobre el empleo se comunica antes de retomar | [Anexo D](04-personas-cultura.md) |
| Diferencia entre grupos en horas de formación liberadas o en rotación, que la agenda o el contrato no explican | Se corrige la agenda antes de seguir con el formato | [Anexo D](04-personas-cultura.md) |
| La utilización cae bajo 80% dos meses por el plan | Se recorta el frente que más tiempo consume | [Anexo D](04-personas-cultura.md) |
| Cortar en un gate o en una revisión mensual | Cierre con las reservas vigentes: 1 de caja y 2 de tiempo (16-24 h senior), recalculadas en cada gate antes de asumir obligaciones nuevas; si un contrato exige más preaviso, ampliarlas antes de comprometer | [Anexo E](05-business-case.md) |

## Riesgos y mitigación

Probabilidad e impacto son **inherentes**, antes del control, como en el registro del
[Anexo C](03-gobierno-seguridad.md); la aceptación se decide sobre el residual, con su
criterio. Dos valores no coinciden con C: datos de un cliente en un modelo externo es
Media / Alto en C y Media / Muy alto acá, y las superficies sin control técnico central
no son una fila de C. La conciliación queda pendiente entre los responsables humanos de
C y F; no se eligen valores acá.

| Riesgo | Prob. inherente | Impacto inherente | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: el mínimo pide 2,0-2,8 FTE internos en M1-M3 con utilización 83%-90% | Alta | Alto | Matriz privada por persona y semana con trabajo desplazado y recuperación, antes de iniciar ([Anexo D](04-personas-cultura.md)) | Horas por rol no liberadas: no iniciar la actividad afectada |
| El diagnóstico mezcla poblaciones y fechas | Alta | Medio | Conciliar corte, nómina, contratistas, personas/FTE y horas por rol ([Anexo A](01-diagnostico.md)) | Sin conciliación no se derivan horas de los agregados |
| La base no resuelve o los datos no son extraíbles | Media | Alto | Acta de viabilidad previa; extensión a la semana 8 desplazando básico, intermedio y prueba | Sin datos ni precisión no se atribuye ganancia |
| La productividad no aparece o trae retrabajo | Media | Alto | Calidad primero; espera del mes 6 vence a las 6 semanas | Debajo de +3% al vencer la espera, o menos de +5% en el mes 9 |
| Superficies sin control técnico central | Alta | Alto | Compensatorios probados por superficie antes de usar ([Anexo C](03-gobierno-seguridad.md)) | Control obligatorio incumplido: se suspende el uso |
| Datos de un cliente llegan a un modelo externo | Media | Muy alto | Matriz, *default-deny*, escaneo local, exclusión de usos prohibidos | Un incidente confirmado |
| Cambio a pago por consumo | Alta | Alto | Se registra como señal; con plataforma, FinOps y prueba de costo | Más de 6× efectivo en un tramo |
| Una señal libera plataforma sin necesidad incremental | Media | Alto | Propuesta de cuatro condiciones, pendiente de ratificación | Disparador propuesto, aplicable solo tras ratificación: sin brecha documentada, no se libera plataforma. Antes de ratificarlo rige la regla de señal, con costeo previo y aceptación explícita del aprendizaje por el Directorio |
| La hipótesis de producto no tiene problema ni comprador | Media | Medio | Medición antes del mes 6 y señal comercial escrita | Sin problema, base o señal |
| Alto riesgo regulatorio fuera del crédito | Media | Alto | Clasificación caso por caso; Legal externo confirma | Un caso de alto riesgo sin dictamen |
| Declarar controles o certificaciones que no existen | Baja | Muy alto | Toda afirmación comercial la valida seguridad | Una afirmación sin evidencia |
| El gobierno frena la entrega y el uso migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles | Más del 20% fuera de SLA dos meses |

## Decisiones

### Decisiones del CAIO sobre los titulares

| Decisión | Elegida | Alternativa a la vista | Por qué | Tipo |
|---|---|---|---|---|
| Pedido inicial | Validación previa con techo 0 / 8; M1-M3 sin plataforma sujeto a segunda liberación de hasta 71 | Pedido completo 33+6 de caja y 72+7 de tiempo con la prueba chica y contractor (Anexo E, alternativa) | Falta evidencia de capacidad y valor incremental; techo acumulado 79 hasta cerrar en M3, sin afirmar repago | Reversible en cada gate |
| Opción de plataforma | Regla vigente: señal en los meses 3, 6 o 9 (bifurcación por señal); propuesta pendiente de ratificación: señal más cuatro condiciones | Pasar toda la plataforma al año 2; o liberarla con cualquier señal sin comparar alternativas | Una señal no demuestra necesidad de esa implementación ni repago; diferir al año 2 exige una decisión adicional justificada | Reversible: se relee en los meses 6 y 9 |
| Base que no resuelve | Extender a la semana 8 solo si el criterio de la semana 4 lo dispara, y desplazar juntos básico, intermedio y prueba a la semana 9 | Retrospectiva sin atribuir; o extender siempre | No atrasa la formación cuando la base resuelve y protege la base cuando no | Reversible antes de la aprobación |
| Medición del asistente | Base de tiempo a primera integración exitosa antes del mes 6, con descubrimiento costeado en M4-M6 | Medir recién en los meses 7-9, después de liberar | Sin base no hay criterio para financiar construcción | Reversible |
| Espera del mes 6 | Vence a las 6 semanas, con subtramo costeado y aprobado aparte: si sigue en la banda, corta el frente interno (102 hasta cerrar) | Sin salida hasta el mes 9 | Una espera sin regla de salida es gasto sin techo | Reversible |
| Meta de adopción | Metas por área, propuestas (Tecnología ≥80% en el mes 6 y ≥85% en el 12; Operaciones habilitadas ≥60% en el 12, con ≥40% en el 6 como meta intermedia), con combinado original, habilitados/total y cobertura publicados. Las que necesitan formación nueva después del mes 3 dependen del programa ampliado ([Anexo D](04-personas-cultura.md); [supuesto de metas culturales](../../context/supuestos/metas-culturales-propuestas.md), en borrador) | Mantener el 80% combinado como meta única | Cumplir exactamente 85%/60% con toda Operaciones habilitada da 72,5%: es el resultado de esas metas, no un techo; las metas pueden superarse ([Anexo D](04-personas-cultura.md)) | Reversible, con el OKR 2027 |
| Equilibrio en las slides y en los gates | No va a las slides ni al gate del mes 12 del mínimo: el ~17% es del paquete completo y no aplica al mínimo ([Anexo E](05-business-case.md), "Insumos para el deck"), y sin beneficio presupuestado no hay equilibrio que mostrar | ~17% de throughput atribuible del paquete completo como titular | Mostrarlo sugeriría un retorno que el mínimo no modela | Reversible |
| Narrativa financiera | Datos → narrativa → decisión sin ROI positivo: el año compra información; el costo de no actuar se presenta como exposición abierta, sin monetizar daños ni probabilidades. La única exposición modelada es la de consumo, 211-267k USD incrementales al año a 12×: un escenario sobre el consumo de septiembre a precio de API, no consumo facturado ni pronóstico; es de la empresa con o sin plan, y el mínimo no la cubre ([Anexo E](05-business-case.md#costo-de-no-actuar)) | Narrativa de retorno con ROI, payback y VPN, como propone el [financial storytelling](../../material/conceptos/m3u4-financial-storytelling.md) | El mínimo presupuesta beneficio de caja 0; un ROI positivo o un monto de daños evitados por no actuar exigirían inventar probabilidades o tasa. Eso no alcanza a la exposición de consumo, que sí está modelada | Reversible: se cambia cuando haya flujos positivos |

### Hipótesis de producto (RICE ajustado por riesgo)

La tesis "IA que se vende" necesita un caso concreto, pero hoy es **hipótesis,
no beneficio validado**. El CAIO elige **una** hipótesis y la compara con dos
alternativas y con no tener frente producto. Los puntajes son **supuestos del
CAIO, sin medición** ([Fuente: RICE](../../material/conceptos/m1u2-rice-ajustado-por-riesgo.md)).

**Hipótesis elegida: asistente de integración en la plataforma propia.**

| Campo | Hipótesis | Estado |
|---|---|---|
| Usuario | El desarrollador de un banco o fintech cliente que integra funcionalidades de la plataforma | Supuesto |
| Tarea | Encontrar la funcionalidad, armar la llamada e interpretar errores en el sandbox | Supuesto |
| Problema y base, antes del mes 6 | Observar a usuarios elegibles integrando con la documentación y el soporte actuales y medir **tiempo a la primera integración exitosa**; consultas de soporte por integración como secundaria propuesta ([Anexo B](02-arquitectura.md), "Medición del problema de integración, antes del mes 6") | Propuesto; el descubrimiento (36-64 h) está costeado en M4-M6 ([Anexo E](05-business-case.md)) |
| Captura de valor | Elegir antes de financiar si se captura eficiencia, ingreso por función o retención, y cómo. No convertir mejora de servicio en ingreso ni sumar toda la facturación protegida | Pendiente de Producto, Comercial y Finanzas |
| Datos | Documentación propia y sandbox con datos sintéticos. Ningún dato productivo de cliente | Fijado por el catálogo |
| Autonomía | "Asiste" (nivel 1): sugiere, el desarrollador ejecuta | Propuesto |
| Costo de construir | No está en el pedido: se vuelve a costear si el mes 6 lo libera. Referencia del paquete completo: tramo de producto 37 (16-59) de caja y 39 (23-56) de tiempo, con plataforma | A costear |
| Señal comercial (mes 6) | Un cliente, con un interlocutor que maneja presupuesto, acepta por escrito evaluar el asistente en el sandbox **y** acepta como referencia un rango de precio sujeto a resultados, sin compromiso de compra. Evaluar sin presupuesto ni rango es interés exploratorio: no libera | Propuesta del CAIO |
| Alternativas a la misma tarea | Mejorar documentación o soporte, configurar un asistente, o integrarlo al producto. Si documentación o soporte resuelven mejor, desplazan al asistente | Se comparan con la misma métrica |

| Opción | Reach | Impact | Confidence | Effort | Riesgo | Puntaje | Por qué |
|---|---|---|---|---|---|---|---|
| **1. Asistente de integración en la plataforma propia** | 3 | 1 | 50% | 2,5 | 1 | **0,60** | Línea de soporte de mayor margen relativo ([ingresos](../../context/hechos/estructura-de-ingresos.md)); sin datos de cliente |
| 2. Función en el producto propio de medios de pago | 1 | 2 | 50% | 3 | 3 | 0,11 | Habilitación externa que puede caer en los meses 4-9 y sin sistema de gestión certificado ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) |
| 3. Servicio de agentes de código para otras software factories | 2 | 1 | 50% | 4 | 2 | 0,13 | El programa de partners exige certificaciones que no hay y compite con horas facturables ([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)) |
| 4. Solo eficiencia, sin frente producto | — | — | — | 0 | — | No aplica | Hoy es el estado del pedido mínimo; se compara con la opción 1 en el mes 6, con la base en la mano |

La señal no prueba disposición a pagar: precio y compra se validan con el piloto
medido. Quién valida los puntajes: el Council, con Producto (a designar).

### Catálogo único de decisiones

Une las puertas del [Anexo B](02-arquitectura.md) y el catálogo del
[Anexo C](03-gobierno-seguridad.md). Separa **aprobación interna**, **negociación
no vinculante** y **firma**. Regla del horizonte: en los 12 meses ningún dato
productivo de cliente va a un modelo.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto | Tipo |
|---|---|---|---|---|---|---|
| Primera liberación: validación inicial | Interno | Preparación 2026 | Directorio o autoridad formalmente delegada | Agenda, desplazamiento e imputación 2026 confirmados | Caja 0; tiempo hasta 8, diez días hábiles | Reversible: detener antes de M1 cuesta lo ejecutado hasta 8 |
| Segunda liberación: ejecución M1-M3 | Interno | Antes de M1, tras la validación | Directorio o autoridad formalmente delegada | Diagnóstico, matriz privada, viabilidad, responsables y presupuesto 2027 conciliados | Hasta 71 restantes: caja 10; tiempo 61; acumulado 79 | Reversible: hasta 79 al cerrar M3; 85 en el año con núcleo aprobado al salir |
| Ratificar o no las cuatro condiciones de plataforma | Interno | Hoy o mes 3 | Council recomienda; firma una persona designada por el Directorio | Evidencia de B y C | Regla escrita | Reversible |
| Excepción externa para facilitación | Interno | Antes de iniciar | Directorio | Sin perfil interno demostrado | Hasta 16-32 h que reemplazan la fila interna, con cotización | Reversible |
| Continuidad sin plataforma por tramo | Interno | Meses 3, 6 y 9 | Directorio | Gates de este anexo | 2/14, 2/11, 2/11 | Reversible en cada gate |
| Liberar plataforma | Interno | Meses 3, 6 o 9 | Directorio | Regla vigente o ratificada | A costear | Reversible hasta contratos largos |
| Liberar construcción del producto | Interno | Mes 6 | Directorio | Base, comparación y señal comercial | A costear | Reversible en el mes 9 |
| Sin crédito ni scoring; clasificación caso por caso | Producto | Hoy | Directorio | Delimitación y apetito propuestos, no clasificación normativa ([Anexo C](03-gobierno-seguridad.md)) | Alcance del año | Reversible al cierre |
| Aplicar la política de IA, aprobada según el responsable del caso, y decidir sus cambios | Interno | Meses 1-3 | Directorio | Versión, alcance y respaldo de aprobación revisados | Compromiso interno enmendable | Reversible con costo de credibilidad |
| Postura sobre el empleo | Interno | Hoy o meses 1-3 | Directorio, con asesoría laboral | — | Texto comunicado | Poco reversible una vez comunicada |
| Estudio de un rol crítico (alcance ampliado) | Interno | Después de comunicar la postura | Directorio | Postura aprobada y comunicada; horas estimadas | Horas y autorización propias, fuera del techo del mínimo; hoy sin estimación ([estudio del rol](04-personas-cultura.md#estudio-de-impacto-sobre-un-rol-crítico-propuesta)) | Reversible |
| Cláusula tipo de IA | Interno | Meses 7-9 | Council | Una función con clasificación de riesgo | Texto listo | Reversible |
| Firmar un compromiso contractual de IA con un cliente | Externo | Mes 12 | Council | Cláusula, matriz, red team sin críticos | Rige después del horizonte | **Irreversible** |
| Enviar datos productivos de un cliente a un modelo | Externo | Prohibido en el horizonte | Responsable comercial con el Council | Cláusula firmada, controles demostrados | Rige después del horizonte | **Irreversible** |
| Ajustar un modelo con datos de cliente | Externo | Fuera del horizonte | — | — | — | **Irreversible** |
| Subir una función a "actúa con aprobación" (nivel 3) | Externo | Mes 12 | Council | Evidencia del piloto | Rige después del horizonte | **Irreversible** una vez activa |
| Hardware propio o consumo comprometido a más de 12 meses | Interno | Mes 12 | Directorio | Escenario de consumo | Contrato | **Irreversible** |

Ninguna decisión irreversible se toma antes del cierre del mes 12, y las que se
toman ahí rigen para el plan siguiente.

### Decisiones pendientes para el board o el equipo

| Tema | Tensión | Alternativas | Propuesta del CAIO | Decide |
|---|---|---|---|---|
| Uso existente sobre clientes, hasta tener su matriz | El [Anexo C](03-gobierno-seguridad.md), "Regla transitoria hasta que exista la matriz de un cliente", no dispone detenerlo, salvo la suspensión preventiva de Seguridad, y no lo acepta automáticamente | Las que plantea el Anexo C: pausarlo; o aceptarlo como residual. Si se acepta, lo hace la autoridad del criterio de aceptación del Anexo C | Sin propuesta del CAIO: es decisión de los responsables humanos de C, antes de la segunda liberación. No crea permiso ni autoridad nuevos | Responsables humanos de C; aceptación según el criterio del Anexo C |
| Capacidad del mínimo | 2,0-2,8 FTE internos M1-M3 sin horas libres demostradas | Liberar por persona con trabajo desplazado; reducir alcance; resecuenciar | Matriz privada antes de iniciar; sin ella no se inicia | Managers, Operaciones y Finanzas |
| Solapes de horas del mínimo | Finanzas une horas de B, C y D (DevOps, Seguridad, QA, seniors) que sus dueños no ratificaron; sin la unión de DevOps, el máximo de tiempo M1-M3 pasa a 60,9 y supera el techo de 59 ([Anexo E](05-business-case.md), "Pedido inicial") | Ratificar las uniones; o recostear el tramo con las horas sumadas | Confirmarlas o recostear en la validación, antes de la segunda liberación; no comprometer M1-M3 con el techo excedido | Responsables de B, C y D, con Finanzas |
| Lectura del sobre de capacidad | Estricta (todo contra 1-2,25 FTE) o separada; el supuesto del sobre pide decisión explícita del board, y el Anexo E la ubica "en la aprobación de hoy" dentro de tensiones que rotula como antecedentes | Decidirla hoy; o al liberar los 71, con las agendas de la validación | Decidirla en la segunda liberación, con las agendas; sin esa decisión no se libera M1-M3 ([sobre separado](../../context/supuestos/sobre-de-capacidad-separado.md)) | Board, con Finanzas |
| Contribución comercial desplazada | El techo no la cuantifica y hoy está sin medir ([Anexo E](05-business-case.md#conclusión-económica)) | Cota en índice; o umbral como condición de la segunda liberación; o informarla sin umbral | Informarla al decidir los 71, estimada por la matriz de la validación; un umbral, si se quiere, lo propone Finanzas | Finanzas y board |
| Programa cultural ampliado (meses 4-12) | Champions, avanzado, cohortes nuevas y metas de Operaciones no están en los techos del mínimo | Costearlo y autorizarlo aparte; o informar las metas sin comprarlas | Informarlas como propuesta hasta que haya costeo y autorización | Directorio, con Personas y Finanzas |
| Lectura del mes 3 si la base se extiende | Cinco semanas de prueba y unas 3 de PR maduros (ver "Qué cuesta extender la base") | Lectura reducida y declarada; o correr la lectura hasta 4 semanas, con impacto en M4 | Lectura reducida y declarada, sin atribuir ganancia, porque no mueve fondos en M3; correrla solo si el board lo pide, con su costo | CAIO, Personas y Finanzas; responsable de F |
| Cuatro condiciones de plataforma | Regla vigente (señal) contra propuesta de B/C | Ratificar; o conservar la vigente como apuesta de aprendizaje explícita | Ratificarlas, con pérdida de aprendizaje declarada | Council y Directorio |
| Calendario de controles | C conserva M4-M6; el mínimo los costea en M1-M3 | Adelantar con validación de horas; o no iniciar usos nuevos hasta M4 | Adelantar solo lo validado; sin prueba no se usa | Gobierno con Finanzas |
| Meta de adopción | 80% combinado contra metas por área | Mantener el combinado; o metas por área con combinado informado | Metas por área; definición de "activo" y ventana antes de medir | Directorio, con el OKR 2027 |
| Gasto de tecnología del OKR | La caja del plan suma gasto contra el OKR de menos de 3,5% | Mantener y recortar; o medir sin la inversión del plan | Medir sin la inversión; el gasto se informa igual | Directorio, presupuesto 2027 |
| Compromiso sobre el empleo | Qué se promete ([Anexo D](04-personas-cultura.md)) | Sin compromiso; o compromiso con excepciones | Compromiso con excepciones; costo sin cuantificar | Directorio, con asesoría laboral |

## Cautelas

- Las horas, techos y reservas del mínimo son supuestos de planificación sin
  cotización ni agendas liberadas; los solapes entre B, C y D los propone
  Finanzas y siguen sin validar por las áreas responsables.
- La validación inicial y su techo adicional de 5 fueron elegidos por Martín
  para el borrador; faltan acuerdo del equipo, designaciones y autorización
  empresarial. Diez días y 4-6 entrevistas son un alcance estimado, no una
  validación exhaustiva ni evidencia de disponibilidad.
- Las bandas de espera, los plazos de 6 semanas y los umbrales de los gates son
  propuestas a ratificar, a calibrar con la base.
- Los puntajes RICE son juicio del CAIO; el outcome del asistente no tiene base.
- El método del intervalo (90%, semiancho de 3 puntos, 15 personas activas) es
  propuesta del Anexo B; el acta de viabilidad comprueba si es alcanzable.
- La fecha del Anexo III del AI Act viene del Anexo C, sin cotejo del texto
  consolidado; no va a una slide.
- La anonimización necesita una revisión autorizada: alias y rangos de
  concentración siguen siendo inferibles para quien conozca la cartera.
- El cierre de un corte de la revisión mensual a mitad de tramo no está calculado
  aparte: usa las reservas vigentes.
- Las fases y tramos del estudio del rol crítico son propuesta del Anexo D, sin
  inventario real del rol. La tabla de familias de indicadores suma métricas de
  seguimiento (Anexos D y E, y la columna de gobierno) que no son condiciones de
  gate: se informan y no mueven fondos en este anexo.
- Responsable de cada gate y de cada decisión: a designar.
