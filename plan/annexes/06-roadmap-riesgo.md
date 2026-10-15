---
owner: caio
status: draft
title: "Anexo F — Roadmap ajustado por riesgo"
---

# Anexo F — Roadmap ajustado por riesgo

Slides que sustenta: [Slide 3 — Beneficio principal y captura](../slides.md),
[Slide 8 — Roadmap a doce meses](../slides.md),
[Slide 9 — Compromiso, pérdida y escenarios](../slides.md) y
[Slide 10 — Resolución propuesta](../slides.md).

> **Borrador sin verificación humana.** Todas las fichas de `context/` están en
> `draft` y ninguna cifra de este anexo es apta para el peer review ni para la
> entrega. Los umbrales, bandas y plazos de los gates son supuestos del equipo o
> decisiones propuestas por el CAIO, a calibrar con la línea de base de los
> meses 1-3. Los gates son propuestas a ratificar, no resultados observados.

## Objetivo

Poner en una sola línea de tiempo los tracks técnico ([Anexo B](02-arquitectura.md)),
de gobierno ([Anexo C](03-gobierno-seguridad.md)), cultural ([Anexo D](04-personas-cultura.md))
y financiero ([Anexo E](05-business-case.md)), con un gate cada tres meses que
integra las condiciones de los cuatro dueños y dice qué pasa si cada una falla, y
una revisión mensual del Council en el medio: **el riesgo se mira cada mes; la
plata se libera cada tres.**

Sustenta **un único pedido al board: el paquete mínimo de los meses 1-3**
(enero-marzo de 2027), recosteado por `finance` en el [Anexo E](05-business-case.md),
"Pedido inicial: paquete mínimo". Compra configuración, controles probados y
medición sobre herramientas existentes, sin plataforma central. El resto del año
no se aprueba hoy. Decisión humana de Martin (2026-10-15): el pedido inicial pasa
a ser el paquete mínimo, en vez del pedido anterior de 33+6 de caja y 72+7 de
tiempo, que queda solo como alternativa (Anexo E, "Pedido anterior 33+6 / 72+7 y
gates económicos (alternativa)"). La bifurcación por señal que decidió lazynet el
2026-10-14 sigue como regla vigente de la opción de plataforma, que se relee en
los meses 3, 6 y 9.

La narrativa del cierre es **valor medible; seguridad aceptable; fondos por
decisión**. Las cifras vienen del anexo que se cita. Lo que este anexo agrega son
decisiones del CAIO (bandas fuera de lo económico, plazos de corrección, el
calendario, la hipótesis de producto y el catálogo de decisiones), marcadas como
propuestas. Donde dos anexos chocan, queda como decisión pendiente. Responsable
humano de cada gate y de cada decisión: **pendiente**, con productor de evidencia,
verificador y autoridad firmante diferenciados ([Anexo C](03-gobierno-seguridad.md),
"Derechos de decisión").

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Convención de tiempo | La preparación previa es octubre-diciembre de 2026, antes de la aprobación de hoy; después, cuatro tramos de tres meses: meses 1-3 (enero-marzo de 2027), 4-6, 7-9 y 10-12 (octubre-diciembre de 2027). Cada tramo termina en un gate (meses 3, 6, 9 y 12) y cada mes hay una revisión del Council, que no libera fondos | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo E](05-business-case.md) |
| Patrón de gates | Kill/scale por etapa, con criterio de éxito y de abandono declarados antes de empezar | [Kill/scale gates](../../material/conceptos/m1u2-kill-scale-gates.md), [kill-fast](../../material/conceptos/m1u1-kill-fast.md) |
| Primeros 100 días | Los meses 1-3 absorben el diagnóstico y la base: inventario, línea de base, política, matriz y controles. No hay quick win de negocio medido; ver "Primeros 100 días" | [Plan de 100 días](../../material/conceptos/m1u2-plan-100-dias.md) |
| Capacidad | Utilización 83%-90% como promedio de toda la empresa, sin corte por proyecto; bench menor a 1 FTE; restricción de no contratar. El promedio no prueba que haya horas libres en los roles necesarios | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md) |
| Paquete mínimo | Entregables, horas por rol, caja y reservas como supuestos de planificación, sin precios cotizados ni agendas liberadas | [Paquete mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md), [Anexo E](05-business-case.md) |
| Clientes principales | Su continuidad es el escenario base; su pérdida parcial es estrés | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |
| Throughput | Unidad: PR aceptado por persona activa en equipos propios. Se valúa como horas evitadas a output fijo y no es caja | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| Línea de base | Base prospectiva congelada en las semanas 1-4 del plan (hasta la 8 si no resuelve); la serie de la preparación previa estima ruido y es contra la que se informa el OKR, sin atribuir | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo B](02-arquitectura.md) |

## Evidencia

### El pedido de hoy: paquete mínimo de los meses 1-3

El pedido completo está en la [Slide 10](../slides.md); la [Slide 9](../slides.md)
muestra su pérdida máxima. Cifras en miles de USD, techos propuestos por `finance`
(Anexo E, "Pedido inicial: paquete mínimo"). La slide redondea los FTE; acá van
los rangos exactos.

| Elemento | Qué se aprueba | Fuente |
|---|---|---|
| 1. Entregables M1-M3 | Política/intake con estado actualizado, matriz de restricciones, inventario y legal focalizado; permisos, MCP y escaneo con pruebas por superficie, críticos cerrados y residual aceptado; padrón, extracción reproducible y base congelada; básico para toda la organización, intermedio de una cohorte de 15-20 personas y prueba de prácticas sobre el agente de código que ya se usa. Sin gateway, retrieval, harness central, producto, avanzado ni contractor continuo | Anexo E; [Anexo B](02-arquitectura.md), "Paquete técnico mínimo"; [Anexo C](03-gobierno-seguridad.md), "Insumo para el paquete mínimo" |
| 2. Caja M1-M3 | Legal focalizado 2-6 y provisión de herramientas/exportación 0-1,5, más 15%: 2,3-8,625; **techo 9**. Sin seats nuevos ni contractor | Anexo E |
| 3. Reserva de caja | **1**, para hasta un mes de herramientas y legal por hitos sin preaviso. Compromiso máximo de caja: **10** | Anexo E |
| 4. Tiempo M1-M3 | 966-1.342 h internas, 14,2-57,9 a costo cargado; **techo 58** | Anexo E |
| 5. Preparación previa | 20-40 h (tech lead y QA), 0,5-2,25; **techo 3**, separada del tramo y sin ejecución registrada | Anexo E |
| 6. Cierre interno | 16-24 h de senior para exportar, revocar accesos y archivar; **reserva de tiempo 2** | Anexo E |
| 7. Capacidad total | **2,0125-2,7958 FTE internos** en M1-M3 (referencia 2,4042): **0,8875-1,4208 clave** y **1,125-1,375 distribuidos**. Ambas bolsas sobre las mismas personas, conciliadas por persona y semana en la matriz privada de D | Anexo E; [Anexo D](04-personas-cultura.md), "Capacidad efectiva" |
| 8. Núcleo tras un corte | Si se corta en el mes 3: 108 h en M4-M12 (36 por tramo), caja 0, **tiempo hasta 6**. Accesos, incidentes y permisos; no mantiene el experimento | Anexo E |
| 9. Marco de decisión | Las tablas de abajo como regla de liberación de fondos, con la revisión mensual del Council (que puede frenar o cortar, pero no libera fondos) y la precedencia de seguridad sobre dependencias y caja | Este anexo |

**Autorización total de hoy: caja 9 + 1 = 10; tiempo 58 + 3 + 2 = 63.** El tiempo
no es nueva nómina ni pago externo. Pérdida máxima de aprendizaje si se sale en el
mes 3: **73 hasta cerrar** (10 + 63), sin deducir beneficios; **79 en el año** con
el núcleo. Fuera del pedido: los meses 4-12, la plataforma, el producto, el
modelo propio, compromisos a más de 12 meses y todo compromiso con clientes.
El techo de caja se confirma contra el presupuesto 2027 en privado.

**Antes de iniciar**, el board recibe: alcance y techos definidos; horas por rol
liberadas en la matriz privada, con trabajo desplazado y recuperación; vía de IA
aplicada interna demostrada (8-16 h) y perfil de facilitación (16-32 h) o la
excepción externa decidida; acta de viabilidad del protocolo y decisión de
calendario; controles aplicables probados antes de usar cada superficie. Si falta
algo, se reduce o difiere y se recostea; el presupuesto no libera tiempo por sí solo.

**Calendario de controles.** El [Anexo C](03-gobierno-seguridad.md) conserva las
pruebas y compensatorios en M4-M6 y deja adelantarlos a M1-M3 como opción pendiente
de validar horas, costo y capacidad ("Calendario conservado"). El paquete mínimo
los costea en M1-M3 porque ningún uso nuevo se inicia sin prueba. Si la validación
falla, ese uso no se inicia ni se amplía en M1-M3 y la prueba de prácticas espera.

### Calendario único de la preparación previa y los meses 1-3 (decisión del CAIO)

| Cuándo | Qué | Quién verifica | Costo |
|---|---|---|---|
| Antes de la aprobación de hoy (preparación previa, octubre-diciembre de 2026) | Acta de viabilidad de datos ([Anexo B](02-arquitectura.md), "Acta de viabilidad de datos"): extracción reproducible, diccionario, enlace PR/CI/reversiones/tickets/incidentes, cohorte elegible, precisión esperada y lectura simulada de pasa/espera/corta. Protocolo único del Anexo B congelado. Conciliación del perímetro de personas (ver [Anexo A](01-diagnostico.md)). La política queda lista para ratificar, con su estado actual confirmado | Pendiente; el Directorio ve el resultado en la aprobación de hoy | Hasta 3 de tiempo (20-40 h) |
| Semanas 1-4 del plan | **Base prospectiva congelada** con la unidad del Anexo B, antes de cualquier formación, práctica o herramienta nueva. Política/intake, matriz, inventario y legal focalizado arrancan en paralelo | Productor: oficina del CAIO; verificador distinto, pendiente | Dentro de M1-M3 |
| Semanas 5-13 (o 9-13 si la base se extiende) | Básico para toda la organización, intermedio de la cohorte y prueba de prácticas sobre repositorios que la matriz habilite, solo en superficies con controles probados | `governance`, `people`, `architect` | Dentro de M1-M3 |
| Meses 4-12 | Continuidad condicional sin plataforma; descubrimiento del asistente antes del mes 6; opción de plataforma releída en los meses 3, 6 y 9 | Oficina del CAIO | Techos por gate |

**Base que no resuelve.** Si en la semana 4 la base no resuelve (criterio mecánico
del [Anexo B](02-arquitectura.md), "Respaldo"), se extiende a la semana 8 y **se
desplazan juntos el básico, el intermedio y la prueba a la semana 9**: mover solo el
intermedio no protege la base. La meta de completitud del básico en el mes 3
(≥90%) se revisa con ese calendario más corto, sin presentarla como lograda por
asistencia. La retrospectiva nunca atribuye ganancia ni libera capital
([convenciones](../../context/supuestos/convenciones-de-calculo.md)). Es la
alternativa que comparten B, D y E; queda propuesta del CAIO hasta que la
ratifique un humano.

### Primeros 100 días: por qué no hay quick win de negocio en los meses 1-3

El método de M1U2 pide 2-3 quick wins con valor medido entre los días 31 y 70
([ficha](../../material/conceptos/m1u2-plan-100-dias.md)). El plan se aparta a
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

Lo que se entrega al día 90: política ratificada o su estado actualizado, matriz
de restricciones, inventario, controles probados por superficie con residual
aceptado, base congelada con cobertura y faltantes, básico con su porcentaje de
cobertura y la lectura de la prueba. Lo primero que puede pedir un banco son la
política y la matriz.

### Revisión mensual del Council

**El riesgo se mira cada mes; la plata se libera cada tres.** Entre gate y gate,
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
  valida `finance`; no se afirma costo cero fuera de esas horas.

### Línea de tiempo integrada

**Cada mes: revisión del Council con poder de corte; los fondos se liberan en los
meses 3, 6, 9 y 12.** Techos en miles de USD, caja / tiempo
([Anexo E](05-business-case.md)). Los meses 4-12 **no se aprueban hoy**.

| Tramo | Técnico y datos | Gobierno y seguridad | Cultural | Financiero: techo caja / tiempo |
|---|---|---|---|---|
| Preparación previa | Acta de viabilidad; protocolo congelado | Estado de la política confirmado | Conciliación del perímetro de personas | — / 3 |
| Meses 1-3: diagnóstico, base, política, formación y prueba | Configuración de herramientas existentes; extracción y base; prueba de prácticas | Política/intake, matriz, inventario, legal focalizado; controles probados por superficie | Básico para todos; intermedio de la cohorte | **9 / 58**, más reserva de caja 1 y de cierre 2 |
| Meses 4-6: solución según evidencia | Mantener controles y medición; descubrimiento del asistente (tiempo a primera integración exitosa); opción de plataforma si se cumplen regla y condiciones | Pruebas y residuales con vencimiento; lectura de señal contractual | Seguimiento de adopción con denominadores | 2 / 14, condicional |
| Meses 7-9: aplicación y producto condicional | Continuidad; producto solo con base y señal del mes 6 y ruta técnica costeada | Amenazas de la función, si existe; cláusula tipo sin firma | Casos por rol dentro de horas aprobadas | 2 / 11, condicional |
| Meses 10-12: evaluación y traspaso | Lectura contra la base; traspaso y salida documentada | Revisión de residuales; irreversibles para después | Tecnología ≥85%; Operaciones habilitadas ≥60% | 2 / 11, condicional |

**Sin plataforma, la base no es "solo política".** En cualquier tramo sin
plataforma central rige gobierno mínimo **más compensatorios aplicables probados
por superficie**, según el [Anexo C](03-gobierno-seguridad.md), "Controles según la
decisión del mes 3": fuentes y repositorios habilitados, datos propios o sintéticos,
permisos/MCP acotados, sin credenciales productivas, escaneo local, prueba
adversarial y revisión humana, con **críticos cerrados** y residual aceptado según
autoridad. El requisito se prueba antes de usar, no después de extender. Una
superficie que no puede cumplir se excluye; no se declara cubierta por un gateway.

**Si se libera plataforma o producto**, su alcance, calendario y techos se
recostean antes de liberar: no se copian los tramos del paquete anterior
(71/106, 59/78, 95/69, ni el producto 38/34 y 21/23 del Anexo E anterior). Ninguna
proyección de continuidad es autorización anual: continuar el mínimo todo el año
proyecta ≈67 (25-108) económicos, con suma de techos 112 y hasta 115 con salida.

### Gates por condición (pasa, espera, corta)

Los gates son la aprobación de hoy y los meses 3, 6, 9 y 12. **Solo los gates
liberan fondos.** Un "espera" libera solo lo que dice la fila y fija un plazo.
Cuatro términos que no son sinónimos: **corte** (el frente deja de financiarse y
queda el núcleo), **suspensión** (se frena un uso o gasto puntual y se vuelve a
medir), **mantenimiento** (el frente sigue sin escalar) y **excepción** (el board
aprueba algo fuera de lo previsto). Bandas económicas: [Anexo E](05-business-case.md);
el resto, propuesta del CAIO sobre los umbrales de los Anexos B, C y D.

**Regla de precedencia (propuesta de `finance`, adoptada).** Si un corte alcanza
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
decide por valor: cuenta como espera. **Calidad primero:** daño en retrabajo o
incidentes corta aunque el throughput pase; calidad incierta cuenta como espera y,
vencida, como no pasa. Bases cero: tratamiento del Anexo B, sin pseudoconteos ni
datos inventados. Datos faltantes se reportan "sin medir".

**El paso no está asegurado.** Con estimados de +3,75% y +9% y semiancho de 3
puntos, los límites inferiores son +0,75% y +6%, debajo de +3% y +8%. Pasarían
solo con semianchos ≤0,75 y ≤1 punto. Es aproximación de planificación: el
bootstrap real puede ser asimétrico y decide su límite inferior. N≥15 y ocho
semanas no garantizan pasar.

| Gate | Condición | Pasa | Espera (plazo) | Corta o falta | Fondos que afecta |
|---|---|---|---|---|---|
| Hoy | Alcance y techos definidos; horas por rol liberadas; vía de IA aplicada y facilitación demostradas; acta de viabilidad y calendario; controles aplicables probados antes de usar | Paquete mínimo aprobado | — | Reducir o diferir y recostear; no se afirma que el presupuesto libera tiempo. La preparación queda hundida (≤3) | M1-M3: 9 / 58, reserva 1 de caja y 2 de cierre |
| Mes 3 | Base congelada con fecha, cobertura y faltantes | Congelada | Historial insuficiente: 6 semanas más, sin atribuir | Sin base al vencer: no se decide por valor; se reformula antes de continuar | Continuidad M4-M6 |
| Mes 3 | Política ratificada, con su estado actual confirmado | Ratificada | En orden del día sin votar: 6 semanas; sin casos nuevos | No ratificada: sin frente producto en el año | Producto |
| Mes 3 | Matriz habilitante de los clientes principales | Completa | Ambiguos: *default-deny* y revisión legal hasta el mes 4 | Más de 30% ambiguo al mes 4: sin piloto con ese cliente | Producto |
| Mes 3 | Básico ≥90% con evaluación práctica (meta revisada si la base se extendió) | ≥90% | ≥50% y <90%: se rediseña el formato | <50%: cambio de formato, no se repite el curso | Formación M4-M6 |
| Mes 3 | Controles por superficie: críticos cerrados, residual aceptado | Probados | — | Control obligatorio incumplido: se suspende el uso afectado | Uso de esa superficie |
| Mes 3 | Consumo dentro de los techos | Dentro | — | Excedido: continuidad solo con recosteo aprobado | M4-M6 |
| Mes 3 | Opción de plataforma: señal (ver definición abajo). Regla vigente: la señal libera evaluar la plataforma. Propuesta pendiente de ratificación: además, brecha documentada, alternativas comparables, economía incremental o pérdida de aprendizaje aceptada, y capacidad demostrada | Con regla vigente: señal. Con la propuesta ratificada: señal más las cuatro condiciones, con reserva y contrato para el compromiso nuevo | — | Sin justificación incremental: continuar el mínimo costeado y releer en los meses 6 y 9. No pasa al año 2 por defecto | Plataforma, a recostear |
| Mes 6 | Throughput, calidad primero | Límite inferior ≥ +3% sin daño | **Suspensión.** Estimado >0% sin pasar, o muestra insuficiente: 6 semanas; si sigue en la banda, corte del frente interno | Estimado ≤0% o daño: corte del frente interno; queda el núcleo | M7-M9 |
| Mes 6 | Adopción de Tecnología, con cobertura y denominador publicados | ≥80% | **Mantenimiento.** ≥60% y <80%: formación rediseñada | **Suspensión.** <60%: se frenan horas de formación que no sean rediseño. Adopción no equivale a valor | Formación M7-M9 |
| Mes 6 | Controles: cobertura por superficie probada; críticos cerrados; residual aceptado. Si hay gateway y se declara cobertura de precio: *fc* × *s* contra el umbral, calidad y portabilidad del Anexo B | Cumplidos | Superficie no cubierta: se declara y escala al Council | Sin prueba económica, se retira el beneficio de precio; conservar un gateway exige justificar control frente a la alternativa menor | Uso y plataforma |
| Mes 6 | Producto: problema observado, base de tiempo a primera integración exitosa y métrica principal acordadas antes de liberar; comparación con documentación/soporte; señal comercial escrita (ver "Hipótesis de producto") | Board decide recostear y liberar construcción | — | Sin evidencia: diferir. Sin plataforma ni ruta técnica alternativa diseñada y costeada, no se promete M7-M9 | Producto, a recostear |
| Mes 9 | Throughput, calidad primero | Límite inferior ≥ +8% | **Mantenimiento.** Estimado ≥ +5% sin pasar: núcleo y mantenimiento, relectura a 6 semanas | Estimado < +5%: corte del frente interno; precedencia si otro frente sigue | M10-M12 |
| Mes 9 | Producto, si existe: SLO acordado, cero cruces de tenant, críticos cerrados | Cumplidos | SLO incumplido: vuelve a "asiste" y se revisa | Una filtración: se cancela la función | Producto |
| Mes 9 | Señal tardía de plataforma | Se evalúa con calendario y costo nuevos | — | No se usa la promesa del itinerario original | Plataforma |
| Mes 12 | Tecnología ≥85%; Operaciones habilitadas ≥60%; ambos denominadores y el combinado original informados | Cumplidos | Se informa contra el OKR | — | Año 2 |
| Mes 12 | Trayectoria al equilibrio o interés contractual (Anexo E) | Una de las dos | — | Sin fundamento: no se financia régimen completo | Año 2 |

**Una sola definición de señal (texto del [Anexo C](03-gobierno-seguridad.md),
"Licencia para vender").** Restricción incluye prohibición o condicionamiento,
conforme a la [ficha del umbral](../../context/supuestos/umbral-de-evidencia-contractual.md).
Una prohibición pura se cumple excluyendo el uso afectado y no libera plataforma.
La regla del borrador libera ante señal; se propone agregar brecha documentada,
alternativas equivalentes, economía incremental o aprendizaje con pérdida aceptada
y capacidad demostrada. Estas cuatro condiciones requieren ratificación humana
Council/Directorio; firma una persona designada con autoridad registrada. Ni una
señal ni el anuncio de precio demuestran que la inversión se pague
([Anexo E](05-business-case.md), "Gateway: suscripción contra consumo").

**Regla de riesgo residual.** Ningún gate pasa con un residual en la franja "no se
acepta" del [Anexo C](03-gobierno-seguridad.md); los residuales aceptados llevan
fecha de revisión. Seguridad antes que dependencias y caja.

**Casos de prueba:**

- **Sin señal en el mes 3:** sigue el mínimo costeado; las lecturas de los meses 6
  y 9 releen señales. Una señal entre gates se registra en su mes y espera al gate.
- **Throughput de +6% con semiancho 3:** pasa el mes 6 (límite +3%); en el mes 9
  queda en mantenimiento y se relee a las 6 semanas.
- **Pesimista (+0,5% en el mes 6):** espera; a las 6 semanas sigue debajo de +3%
  y se corta el frente interno: salida en el mes 6, hasta 89 hasta cerrar.
- **Control incumplido en cualquier mes:** Seguridad suspende el uso afectado sin
  esperar al gate; reanudar exige prueba corregida, verificación independiente y
  residual aceptado.

### Escenarios

Para el paquete mínimo, el [Anexo E](05-business-case.md) no presupuesta
beneficios: **beneficio de caja estimado: 0; ingreso nuevo: 0**; capacidad sin
cifra hasta medir. Por eso los escenarios se expresan como pérdida máxima por
punto de salida, no como ROI. El ROI económico modelado sin beneficios es −100%;
no es un resultado observado.

| Escenario | Qué pasa | Hasta cerrar, caja / tiempo → económico | Máximo del año |
|---|---|---|---|
| Corte en el mes 3 | La base no resuelve, falla un control o no hay agendas | 10 / 63 → **73** | **79** con núcleo |
| Pesimista con la regla | Espera en el mes 6, vence y corta | 12 / 77 → **89** | **93** |
| Corte en el mes 9 | Estimado < +5% | 14 / 88 → **102** | **104** |
| Continuidad todo el año sin plataforma | Pasan los gates | 16 / 99 → **115** como límite | Proyección ≈67 (25-108); no autorizado hoy |
| Con señal y, si se ratifican, las cuatro condiciones | Respuesta mínima de plataforma | A recostear antes de liberar | Sin cifra: no se hereda 394/≈400 |

Las salidas son límites por suma de techos, sin restar beneficio. La diferencia
entre cortar a tiempo y seguir sin frenar es lo que compran los gates.

**Referencia del paquete anterior (alcances distintos, pendientes de homogeneizar).**
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
| El proveedor pasa a cobrar por consumo | Se registra como señal; con plataforma liberada, gateway con ruteo, caché y topes; a más de 6× efectivo sin mitigar, se congela la expansión. A 12×, el incremental anual es de 211-267 mil: exposición de la empresa, con o sin plan | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| Falta perfil interno de facilitación del básico | Comparar liberar un facilitador interno contra una intervención externa acotada de 16-32 h que **reemplace** esa fila, sin sumar ambas; precio, caja y preaviso requieren cotización y la excepción la decide el Directorio. Sin vía demostrada, diferir el módulo y recostear | [Anexo D](04-personas-cultura.md) |
| Falta perfil de IA aplicada (8-16 h) o verificador independiente | No iniciar el hito afectado; reducir o recostear. Un 0,3 interno no reemplaza a un especialista | [Anexo E](05-business-case.md), [Anexo D](04-personas-cultura.md) |
| Pérdida parcial del cliente principal | Se congelan los gates de los meses 4-12 hasta revisar el techo | [Anexo E](05-business-case.md) |
| Incidente de datos de un cliente | Se suspende la IA sobre ese cliente y se reporta el mismo día | [Anexo C](03-gobierno-seguridad.md) |
| Primer secreto expuesto | Revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo | [Anexo C](03-gobierno-seguridad.md) |
| Se va una persona clave sin suplente | Se congelan altas de casos de riesgo alto y se baja el alcance del tramo siguiente | [Anexo C](03-gobierno-seguridad.md) |
| La utilización cae bajo 80% dos meses por el plan | Se recorta el frente que más tiempo consume | [Anexo D](04-personas-cultura.md) |
| Cortar en un gate o en una revisión mensual | Cierre con las reservas vigentes: 1 de caja y 2 de tiempo (16-24 h senior), recalculadas en cada gate antes de asumir obligaciones nuevas; si un contrato exige más preaviso, ampliarlas antes de comprometer | [Anexo E](05-business-case.md) |

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: el mínimo pide 2,0-2,8 FTE internos en M1-M3 con utilización 83%-90% | Alta | Alto | Matriz privada por persona y semana con trabajo desplazado y recuperación, antes de iniciar ([Anexo D](04-personas-cultura.md)) | Horas por rol no liberadas: no iniciar la actividad afectada |
| El diagnóstico mezcla poblaciones y fechas | Alta | Medio | Conciliar corte, nómina, contratistas, personas/FTE y horas por rol ([Anexo A](01-diagnostico.md)) | Sin conciliación no se derivan horas de los agregados |
| La base no resuelve o los datos no son extraíbles | Media | Alto | Acta de viabilidad previa; extensión a la semana 8 desplazando básico, intermedio y prueba | Sin datos ni precisión no se atribuye ganancia |
| La productividad no aparece o trae retrabajo | Media | Alto | Calidad primero; espera del mes 6 vence a las 6 semanas | Debajo de +3% al vencer la espera, o menos de +5% en el mes 9 |
| Superficies sin control técnico central | Alta | Alto | Compensatorios probados por superficie antes de usar ([Anexo C](03-gobierno-seguridad.md)) | Control obligatorio incumplido: se suspende el uso |
| Datos de un cliente llegan a un modelo externo | Media | Muy alto | Matriz, *default-deny*, escaneo local, exclusión de usos prohibidos | Un incidente confirmado |
| Cambio a pago por consumo | Alta | Alto | Se registra como señal; con plataforma, FinOps y prueba de costo | Más de 6× efectivo en un tramo |
| Una señal libera plataforma sin necesidad incremental | Media | Alto | Propuesta de cuatro condiciones, pendiente de ratificación | Sin brecha documentada, no se libera |
| La hipótesis de producto no tiene problema ni comprador | Media | Medio | Medición antes del mes 6 y señal comercial escrita | Sin problema, base o señal |
| Alto riesgo regulatorio fuera del crédito | Media | Alto | Clasificación caso por caso; Legal externo confirma | Un caso de alto riesgo sin dictamen |
| Declarar controles o certificaciones que no existen | Baja | Muy alto | Toda afirmación comercial la valida seguridad | Una afirmación sin evidencia |
| El gobierno frena la entrega y el uso migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles | Más del 20% fuera de SLA dos meses |

## Decisiones

### Decisiones del CAIO sobre los titulares

| Decisión | Elegida | Alternativa a la vista | Por qué | Tipo |
|---|---|---|---|---|
| Pedido inicial | Paquete mínimo M1-M3 sin plataforma central (decisión de Martin, 2026-10-15; costeo de `finance`) | Pedido anterior 33+6 de caja y 72+7 de tiempo con la prueba chica y contractor (Anexo E, alternativa) | Falta evidencia de valor incremental para ampliar inversión; el mínimo compra la medición con la menor pérdida máxima (73 hasta cerrar) | Reversible en cada gate |
| Opción de plataforma | Regla vigente: señal en los meses 3, 6 o 9 (bifurcación de lazynet, 2026-10-14); propuesta pendiente de ratificación: señal más cuatro condiciones | Pasar toda la plataforma al año 2; o liberarla con cualquier señal sin comparar alternativas | Una señal no demuestra necesidad de esa implementación ni repago; diferir al año 2 exige una decisión adicional justificada | Reversible: se relee en los meses 6 y 9 |
| Base que no resuelve | Extender a la semana 8 solo si el criterio de la semana 4 lo dispara, y desplazar juntos básico, intermedio y prueba a la semana 9 | Retrospectiva sin atribuir; o extender siempre | No atrasa la formación cuando la base resuelve y protege la base cuando no | Reversible antes de la aprobación |
| Medición del asistente | Base de tiempo a primera integración exitosa antes del mes 6, con descubrimiento costeado en M4-M6 | Medir recién en los meses 7-9, después de liberar | Sin base no hay criterio para financiar construcción | Reversible |
| Espera del mes 6 | Vence a las 6 semanas: si sigue en la banda, corta el frente interno | Sin salida hasta el mes 9 | Una espera sin regla de salida es gasto sin techo | Reversible |
| Meta de adopción | Metas por área (Tecnología ≥80% en el mes 6 y ≥85% en el 12; Operaciones habilitadas ≥60%), con combinado original, habilitados/total y cobertura publicados | Mantener el 80% combinado como meta única | Cumplir exactamente 85%/60% con toda Operaciones habilitada da 72,5%: es el resultado de esas metas, no un techo; las metas pueden superarse ([Anexo D](04-personas-cultura.md)) | Reversible, con el OKR 2027 |
| Equilibrio en las slides | No va a las slides del mínimo: sin beneficio presupuestado no hay equilibrio que mostrar | ~17% de throughput atribuible del paquete anterior como titular | Mostrarlo sugeriría un retorno que el mínimo no modela | Reversible |

### Hipótesis de producto (M1U2 aplicado: RICE ajustado por riesgo)

La tesis "IA que se vende" necesita un caso concreto, pero hoy es **hipótesis,
no beneficio validado**. El CAIO elige **una** hipótesis y la compara con dos
alternativas y con no tener frente producto. Los puntajes son **supuestos del
CAIO, sin medición** ([ficha RICE](../../material/conceptos/m1u2-rice-ajustado-por-riesgo.md)).

**Hipótesis elegida: asistente de integración en la plataforma propia.**

| Campo | Hipótesis | Estado |
|---|---|---|
| Usuario | El desarrollador de un banco o fintech cliente que integra funcionalidades de la plataforma | Supuesto |
| Tarea | Encontrar la funcionalidad, armar la llamada e interpretar errores en el sandbox | Supuesto |
| Problema y base, antes del mes 6 | Observar a usuarios elegibles integrando con la documentación y el soporte actuales y medir **tiempo a la primera integración exitosa**; consultas de soporte por integración como secundaria propuesta ([Anexo B](02-arquitectura.md), "Medición del problema de integración, antes del mes 6") | Propuesto; el descubrimiento (36-64 h) está costeado en M4-M6 ([Anexo E](05-business-case.md)) |
| Captura de valor | Elegir antes de financiar si se captura eficiencia, ingreso por función o retención, y cómo. No convertir mejora de servicio en ingreso ni sumar toda la facturación protegida | Pendiente de Producto, Comercial y `finance` |
| Datos | Documentación propia y sandbox con datos sintéticos. Ningún dato productivo de cliente | Fijado por el catálogo |
| Autonomía | "Asiste" (nivel 1): sugiere, el desarrollador ejecuta | Propuesto |
| Costo de construir | No está en el pedido: se recostea si el mes 6 lo libera. Referencia anterior: tramo de producto 37 (16-59) de caja y 39 (23-56) de tiempo, con plataforma | A recostear |
| Señal comercial (mes 6) | Un cliente, con un interlocutor que maneja presupuesto, acepta por escrito evaluar el asistente en el sandbox **y** acepta como referencia un rango de precio sujeto a resultados, sin compromiso de compra. Evaluar sin presupuesto ni rango es interés exploratorio: no libera | Propuesta del CAIO |
| Alternativas a la misma tarea | Mejorar documentación o soporte, configurar un asistente, o integrarlo al producto. Si documentación o soporte resuelven mejor, desplazan al asistente | Se comparan con la misma métrica |

| Opción | Reach | Impact | Confidence | Effort | Riesgo | Puntaje | Por qué |
|---|---|---|---|---|---|---|---|
| **1. Asistente de integración en la plataforma propia** | 3 | 1 | 50% | 2,5 | 1 | **0,60** | Línea de soporte de mayor margen relativo ([ingresos](../../context/hechos/estructura-de-ingresos.md)); sin datos de cliente |
| 2. Función en el producto propio de medios de pago | 1 | 2 | 50% | 3 | 3 | 0,11 | Habilitación externa que puede caer en los meses 4-9 y sin sistema de gestión certificado ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) |
| 3. Servicio de agentes de código para otras software factories | 2 | 1 | 50% | 4 | 2 | 0,13 | El programa de partners exige certificaciones que no hay y compite con horas facturables ([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)) |
| 4. Solo eficiencia, sin frente producto | — | — | — | 0 | — | No aplica | Hoy es el estado del pedido mínimo; se compara con la opción 1 en el mes 6, con la base en la mano |

La señal no prueba disposición a pagar: precio y compra se validan con el piloto
medido. Quién valida los puntajes: el equipo con el Council (**pendiente**).

### Catálogo único de decisiones

Une las puertas del [Anexo B](02-arquitectura.md) y el catálogo del
[Anexo C](03-gobierno-seguridad.md). Separa **aprobación interna**, **negociación
no vinculante** y **firma**. Regla del horizonte: en los 12 meses ningún dato
productivo de cliente va a un modelo.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto | Tipo |
|---|---|---|---|---|---|---|
| El pedido de hoy: paquete mínimo y marco de decisión | Interno | Hoy | Directorio | Techos y horas confirmados | Caja 9 + reserva 1; tiempo 58 + preparación 3 + cierre 2 | Reversible: salir en el mes 3 cuesta hasta 73 hasta cerrar, 79 en el año |
| Ratificar o no las cuatro condiciones de plataforma | Interno | Hoy o mes 3 | Council recomienda; firma una persona designada por el Directorio | Evidencia de B y C | Regla escrita | Reversible |
| Excepción externa para facilitación | Interno | Antes de iniciar | Directorio | Sin perfil interno demostrado | Hasta 16-32 h que reemplazan la fila interna, con cotización | Reversible |
| Continuidad sin plataforma por tramo | Interno | Meses 3, 6 y 9 | Directorio | Gates de este anexo | 2/14, 2/11, 2/11 | Reversible en cada gate |
| Liberar plataforma | Interno | Meses 3, 6 o 9 | Directorio | Regla vigente o ratificada | A recostear | Reversible hasta contratos largos |
| Liberar construcción del producto | Interno | Mes 6 | Directorio | Base, comparación y señal comercial | A recostear | Reversible en el mes 9 |
| Sin crédito ni scoring; clasificación caso por caso | Producto | Hoy | Directorio | — | Alcance del año | Reversible al cierre |
| Ratificar la política de IA | Interno | Meses 1-3 | Directorio | Estado actual confirmado | Compromiso interno enmendable | Reversible con costo de credibilidad |
| Postura sobre el empleo | Interno | Hoy o meses 1-3 | Directorio, con asesoría laboral | — | Texto comunicado | Poco reversible una vez comunicada |
| Cláusula tipo de IA | Interno | Meses 7-9 | Council | Una función con ficha | Texto listo | Reversible |
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
| Capacidad del mínimo | 2,0-2,8 FTE internos M1-M3 sin horas libres demostradas | Liberar por persona con trabajo desplazado; reducir alcance; resecuenciar | Matriz privada antes de iniciar; sin ella no se inicia | Managers, Operaciones y Finanzas |
| Cuatro condiciones de plataforma | Regla vigente (señal) contra propuesta de B/C | Ratificar; o conservar la vigente como apuesta de aprendizaje explícita | Ratificarlas, con pérdida de aprendizaje declarada | Council y Directorio |
| Calendario de controles | C conserva M4-M6; el mínimo los costea en M1-M3 | Adelantar con validación de horas; o no iniciar usos nuevos hasta M4 | Adelantar solo lo validado; sin prueba no se usa | `governance` con `finance` |
| Meta de adopción | 80% combinado contra metas por área | Mantener el combinado; o metas por área con combinado informado | Metas por área; definición de "activo" y ventana antes de medir | Directorio, con el OKR 2027 |
| Gasto de tecnología del OKR | La caja del plan suma gasto contra el OKR de menos de 3,5% | Mantener y recortar; o medir sin la inversión del plan | Medir sin la inversión; el gasto se informa igual | Directorio, presupuesto 2027 |
| Compromiso sobre el empleo | Qué se promete ([Anexo D](04-personas-cultura.md)) | Sin compromiso; o compromiso con excepciones | Compromiso con excepciones; costo sin cuantificar | Directorio, con asesoría laboral |

## Cautelas

- Las horas, techos y reservas del mínimo son supuestos de planificación sin
  cotización ni agendas liberadas; los solapes entre B, C y D los propone
  `finance` y siguen sin validar por sus dueños.
- Las bandas de espera, los plazos de 6 semanas y los umbrales de los gates son
  propuestas a ratificar, a calibrar con la base.
- Los puntajes RICE son juicio del CAIO; el outcome del asistente no tiene base.
- El método del intervalo (90%, semiancho de 3 puntos, 15 personas activas) es
  propuesta del Anexo B; el acta de viabilidad comprueba si es alcanzable.
- La fecha del Anexo III del AI Act viene del Anexo C, sin cotejo del texto
  consolidado; no va a una slide.
- La anonimización necesita revisión de un humano autorizado: alias y rangos de
  concentración siguen siendo inferibles para quien conozca la cartera.
- El cierre de un corte de la revisión mensual a mitad de tramo no está calculado
  aparte: usa las reservas vigentes.
- Responsable humano de cada gate y de cada decisión: **pendiente**.
