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
> decisiones propuestas por el CAIO, a calibrar con la línea de base de T1.

## Objetivo

Poner en una sola línea de tiempo los tracks técnico ([Anexo B](02-arquitectura.md)),
de gobierno ([Anexo C](03-gobierno-seguridad.md)), cultural ([Anexo D](04-personas-cultura.md))
y financiero ([Anexo E](05-business-case.md)), con un gate por trimestre que
integra las condiciones de los cuatro dueños y dice qué pasa si cada una falla.
Sustenta **un único pedido al board, el de G0** (ver "Pedido G0"): autorizar T1
con techo de caja y de capacidad, confirmar el piso de capacidad de T2-T4 con el
producto diferido, elegir hoy entre el replan de T2 y la excepción acotada, y
adoptar el marco de gates. El resto del año no se aprueba hoy.

Las cifras vienen del anexo que se cita. Lo que este anexo agrega son decisiones
del CAIO (bandas de espera fuera de lo económico, plazos de corrección, el
calendario único, la hipótesis de producto y el catálogo de decisiones),
marcadas como propuestas. Donde dos anexos chocan, queda como decisión
pendiente. Responsable humano de cada gate y de cada decisión: **pendiente**.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Convención de tiempo | T0 = cuarto trimestre de 2026, antes de G0; T1 = enero-marzo de 2027 … T4 = octubre-diciembre de 2027. El Q1-Q4 de los Anexos B y C se lee como T1-T4 | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo E](05-business-case.md) |
| Patrón de gates | Kill/scale por etapa, con criterio de éxito y de abandono declarados antes de empezar | [Kill/scale gates](../../material/conceptos/m1u2-kill-scale-gates.md), [kill-fast](../../material/conceptos/m1u1-kill-fast.md) |
| Primeros 100 días | T1 absorbe el diagnóstico y la base: inventario, línea de base, política, matriz. No hay quick win de negocio medido en T1; la adaptación se justifica en "Primeros 100 días" | [Plan de 100 días](../../material/conceptos/m1u2-plan-100-dias.md) |
| Capacidad | Utilización 83%-90%, bench menor a 1 FTE, restricción de no contratar; sobre de 1-2,25 FTE de personas clave | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md), [sobre](../../context/supuestos/capacidad-de-inversion.md) |
| Clientes principales | Su continuidad es el escenario base; su pérdida parcial es estrés | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |
| Calendario externo | Un producto propio en inversión depende de una habilitación externa con fecha dentro de 2027, que puede superponerse con T2-T3 | [Ingresos](../../context/hechos/estructura-de-ingresos.md) |
| Throughput | Unidad: PR aceptado por persona activa en equipos propios. El throughput del trimestre es g × rampa; se valúa como horas evitadas a output fijo (lectura A) y no es caja | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| Línea de base | Base prospectiva congelada en las semanas 1-4 de T1; la serie de T0 estima ruido y es contra la que se informa el OKR, sin atribuir | [Convenciones](../../context/supuestos/convenciones-de-calculo.md) |

## Evidencia

### Pedido G0, único

El pedido completo está en la [Slide 8](../slides.md); las demás slides piden su
parte. Es el mismo que cierran los Anexos [B](02-arquitectura.md) y
[E](05-business-case.md).

| Elemento | Qué se aprueba | Fuente |
|---|---|---|
| 1. T1 en su versión acotada (T1-E) | Inventario de datos, línea de base congelada, matriz superficie→control→telemetría, telemetría unificada, matriz de clientes, evidencia contractual, política ratificada, nivel básico. El gateway pasa a T2 | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| 2. Techo de caja de T1 | Hasta 33 mil USD (máximo calculado 32,2: contractor hasta 16,5, legal hasta 10, telemetría hasta 1,5 y contingencia), más una reserva de cierre de hasta 6 que solo se usa si un gate corta. Compromiso máximo de caja: 39 | [Anexo E](05-business-case.md) |
| 3. Techo de tiempo de T1 | Hasta 62 mil: 1,6 FTE de personas clave (0,70× del sobre) y 590 h distribuidas en la dotación, como segundo sobre | [Anexo E](05-business-case.md) |
| 4. Piso de capacidad | Sobre clave de al menos 1,6 FTE en T1; 2,2 / 2,2 / 2,1 en T2-T4 con el producto diferido y el replan de T2, o 2,5 en T2 con la excepción acotada; lectura del sobre (DP1) | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| 5. Salida para el exceso de T2 | Replan de B (T2 en 2,2 FTE clave), con la excepción acotada de 0,3 FTE aprobada como respaldo | [Anexo B](02-arquitectura.md) |
| 6. Base mínima tras un corte | Si G1 corta, el núcleo de gobierno sigue el resto del año: hasta 41 mil de tiempo, sin caja | [Anexo E](05-business-case.md) |
| 7. T0 (costo previo propuesto) | Autorizar, o ratificar si consta la ejecución, hasta 7 mil de tiempo | [Anexo E](05-business-case.md) |
| 8. IA aplicada de T1 | Contractor B1, o un rol interno si demuestra experiencia en evals y harness antes de G0 (DP3) | [Anexo B](02-arquitectura.md), [Anexo D](04-personas-cultura.md) |
| 9. Marco de gates | Las tablas de abajo como regla de liberación de fondos, con la salida de la espera de G2 y el alcance del corte de G3 | Este anexo |

El techo de caja se confirma contra el presupuesto 2027 en `private/`. Fuera del
pedido: T2-T4, el tramo de producto, el modelo propio, compromisos a más de 12
meses y todo compromiso con clientes.

### Calendario único de T0 y T1 (decisión del CAIO)

| Cuándo | Qué | Quién verifica | Costo |
|---|---|---|---|
| Antes de G0 (T0) | Verificar que existe historial de PR, integración continua, incidentes y tickets (B); serie retrospectiva de uso, incidentes y retrabajo, y diseño de la encuesta de chat y suite ofimática (D). La política queda lista para ratificar, no ratificada | Pendiente; el Directorio ve el resultado en G0 | 1,8-6,7 mil de tiempo: costo previo propuesto, autorizado, o ratificado si consta, en G0 ([Anexo E](05-business-case.md)) |
| T1, semanas 1-4 | **Base prospectiva congelada** con la unidad de B, antes de cualquier formación o herramienta nueva | Oficina del CAIO, con `finance` | Dentro de T1 |
| T1, semanas 5-13 | Política ratificada, matriz de clientes, evidencia contractual, básico, champions, intermedio de Tecnología, matriz de superficies y telemetría | `governance`, área comercial, `architect` | Dentro de T1 |
| T2 en adelante | Gateway, formación de Operaciones y staff; medición contra la base congelada | Oficina del CAIO | Techos por gate |

La serie retrospectiva sirve para estimar tendencia y ruido; **la ganancia se
atribuye solo contra la base prospectiva**, y no antes de T2 (la rampa base es 0%
en T1, [rampa](../../context/supuestos/rampa-de-la-ganancia.md)). Regla de
respaldo: si en la semana 4 la dispersión de la base prospectiva supera la
tendencia que se espera medir, la oficina del CAIO puede adoptar la serie
retrospectiva como base, dejando constancia ([convenciones](../../context/supuestos/convenciones-de-calculo.md)).
El OKR se informa al lado, contra la serie de T0. Quién autoriza gastar T0 antes
del presupuesto: **pendiente**.

### Primeros 100 días: por qué no hay quick win de negocio en T1

El método de M1U2 pide 2-3 quick wins con valor medido entre los días 31 y 70
([ficha](../../material/conceptos/m1u2-plan-100-dias.md)). El plan se aparta a
propósito, por tres razones con evidencia:

- **Capacidad.** T1-E entra en el sobre clave con 1,6 FTE. Adelantar un caso
  con valor medible a T1 pide el gateway en T1 (T1-a), que lleva T1 a 2,3 FTE
  clave contra un máximo de 2,25: ya excede el sobre, y con las horas
  distribuidas suma 3,5, 1,56× con la lectura estricta ([Anexo E](05-business-case.md)).
  No hay holgura que lo pague sin sacar horas facturables.
- **Atribución.** La base prospectiva se congela en las semanas 1-4 de T1 y la
  rampa base es 0% en T1: una ganancia "medida" antes de T2 sería ruido.
- **Precondiciones.** La fase 2 del método pide datos disponibles y criterio de
  éxito; sin matriz de clientes ni inventario no se sabe qué datos se pueden usar.

Lo que sí se entrega medido al día 90, y le sirve al negocio: la política
ratificada y la matriz de clientes (lo primero que puede pedir un banco), la
telemetría unificada con uso por persona activa, el básico con su porcentaje de
cobertura y la línea de base congelada. La primera señal de negocio es el caso
de referencia en L1 en sombra al cierre de T2 ([Anexo B](02-arquitectura.md)),
que se lee en G2. Alternativa a la vista: T1-a con quick win, si el board acepta
el sobre ampliado; no la recomendamos.

### Línea de tiempo integrada

| Trim. | Técnico (B) | Gobierno y seguridad (C) | Cultural (D) | Financiero (E): techo caja / tiempo |
|---|---|---|---|---|
| T0 | Verificación del historial | Política lista para ratificar | Serie retrospectiva y diseño de la encuesta | — (hasta 7 de tiempo, propuesto) |
| T1 | Inventario de datos; base congelada; matriz de superficies; telemetría unificada | Política ratificada; inventario v1; matriz de clientes; evidencia contractual registrada; intake en 3 niveles | Básico para todos; champions; intermedio de Tecnología | 33 / 62, más reserva de cierre de 6 |
| T2 | Gateway con 2 proveedores; harness v1 y evals en CI sobre el caso de referencia; prueba de portabilidad y costo; FinOps | Pasarela y DLP; prueba de bypass por superficie; red team interno; ejercicio de incidentes | Intermedio para Operaciones y staff; champions con tiempo | 71 / 106 (71 / 114 con la excepción) |
| T3 | Caso de referencia en L2; piloto en un producto propio (L1-L2, datos sintéticos), **solo si G2 lo libera**; aislamiento por tenant | Amenazas de la función; criterios de eval; cláusula tipo, sin firma | Casos por rol; calidad de prompts | 59 / 78 (+38 / 34 si P) |
| T4 | Gate del piloto, si existe; go/no-go de modelo propio; productividad contra la base | Red team externo e ISO 27001 extendida a IA (capa D: solo con señal contractual en G3); gate de 42001 | Traspaso del contractor; Tecnología ≥85% | 95 / 69 (+21 / 23 si P) |

Techos máximos por trimestre, en miles de USD ([Anexo E](05-business-case.md)).
El año, con contingencia, el producto diferido y el replan de T2: caja de 98-255
mil y tiempo de 115-320 mil, unos 3,5 FTE promedio (2,0 de personas clave):
1,6 / 2,2 / 2,2 / 2,1. Si G2 libera el producto, T3-T4 suben a 3,7 / 3,1 FTE
clave y la caja a 114-314. El producto diferido es el escenario base, no una
contingencia.

### Gates por condición (pasa, espera, corta)

Cada condición tiene su resultado y su acción. Un "espera" libera solo lo que
dice la fila y fija un plazo para volver a medir. Cada celda dice qué pasa al
vencer el plazo; **la espera de throughput de G2 vence a las 6 semanas y, si
sigue en la banda, corta el frente interno** (es la que costea el
[Anexo E](05-business-case.md)). Las condiciones de un
frente no frenan al otro: **B** = base común, **I** = frente interno, **P** =
frente producto. Si P se difirió, sus condiciones son "no aplica" y sus fondos
no se liberan. Bandas económicas: [Anexo E](05-business-case.md); el resto,
propuesta del CAIO sobre los umbrales de B, C y D.

**Límites de las bandas.** El umbral pertenece a la banda superior: +3% y 80%
pasan en G2, +8% pasa en G3 y +5% espera. Un intervalo que cruza el umbral de
"pasa" cuenta como espera. Más retrabajo corta aunque el throughput pase.

| Gate | Condición | Fr. | Pasa | Espera (plazo) | Corta | Fondos que afecta |
|---|---|---|---|---|---|---|
| G0 | Pedido G0 completo, techo y piso de capacidad confirmados | B | Aprobado | — | No arranca T1; T0 queda hundido (≤7) | T1: 33 / 62, más reserva de cierre de 6 |
| G0 | Vía de IA aplicada de T1 | B | B1 o rol interno demostrado | — | Ninguna: los hitos de IA aplicada pasan a T2. Sin contractor no hay replan: T2 va con la excepción | Contractor de T1 |
| G1 | Base congelada con la unidad de B | I | Congelada con fecha | Historial insuficiente: 6 semanas más; no se atribuye ganancia | Sin base al cierre de la espera: se elimina el resultado clave de throughput y el frente interno no escala | Escalado de T2 |
| G1 | Política ratificada | B | Ratificada | En el orden del día sin votar: 6 semanas; T2 sin casos de cliente | No ratificada: no hay frente producto en el año | Fondos de P |
| G1 | Matriz de los clientes que concentran la facturación | P | Completa | Contratos ambiguos: *default-deny* y revisión legal hasta el mes 4 | Más del 30% ambiguo al mes 4: sin piloto con ese cliente; Operaciones sin meta | Fondos de P |
| G1 | Evidencia contractual registrada en `private/` y su agregado anonimizado ([Anexo C](03-gobierno-seguridad.md), D9b) | B | Registrada | Incompleta: se completa en T2, antes de G3 | Sin evidencia en G3: la capa D no se financia | Capa D de T4 |
| G1 | Básico ≥90% de la dotación | I | ≥90% | ≥50% y <90%: se libera T2 y se rediseña el formato | <50% al cierre de T2: cambio de formato, no se repite el curso | Capacitación de T2 |
| G1 | Uso de T1 dentro del sobre aprobado | B | Dentro | — | Excedido: T2 solo con replan de capacidad aprobado | T2 entero |
| G2 | Throughput como tendencia con intervalo, sin más retrabajo | I | ≥ +3%, con intervalo que no cruza +3% | >0% y <+3%, o intervalo que cruza +3%: T3 sin escalado; se vuelve a medir a las 6 semanas y, si sigue en la banda, se corta el frente interno y queda la base mínima | ≤0% o más retrabajo: se corta el frente interno; queda la base mínima | T3: 59 / 78 |
| G2 | Uso semanal de Tecnología | I | ≥80% | ≥60% y <80%: T3 sigue; formación rediseñada con casos por rol; se vuelve a medir al cierre de T3 | <60%: se frena la expansión de seats | Expansión de seats |
| G2 | Cobertura de controles | B | ≥90% de los eventos del agente de código y de los casos propios por el gateway; 100% de superficies con control verificado | Superficie con bypass sin control compensatorio: se declara no cubierta y va al Council | Gateway sin operar más de un trimestre: se compra una solución | Infraestructura |
| G2 | Red team interno y prueba de portabilidad y costo | B | Críticos cerrados; portabilidad ≤20 días-persona; cobertura de precio medida (f × s contra el umbral de E a 6×, 25%; calidad sin caída mayor a 5 puntos; suscripción preservada) | Críticos abiertos: el piloto no arranca hasta cerrarlos. Portabilidad >20: sin compromisos de volumen. Cobertura no demostrada: el gateway sigue por control, y la palanca de precio sale del deck | — | Piloto de T3; palanca de precio |
| G2 | FinOps: múltiplo de consumo medido | B | ≤6× efectivo | — | >6× sin mitigar en un trimestre: se congela la expansión y se topea el consumo | Expansión |
| G2 | Señal de cliente para la hipótesis de producto (ver "Hipótesis de producto") | P | Señal cumplida: el board decide ampliar el sobre de T3-T4 para el piloto | — | Sin señal: P se difiere; sus condiciones de G3 no aplican | P: 38 / 34 |
| G3 | Throughput | I | ≥ +8% | ≥ +5% y < +8%: solo base mínima y mantenimiento; se vuelve a medir a las 6 semanas. Si sigue debajo de +8%, T4 se ejecuta con la base mínima | < +5%: corte del frente interno y de la base común; queda la base mínima en T4 | T4: 95 / 69 |
| G3 | Costo por PR aceptado | I | No sube | Sube con throughput en alza: se revisa el consumo en FinOps | Sube con throughput plano: se aplica el corte de arriba | Consumo |
| G3 | Señal contractual ([Anexo C](03-gobierno-seguridad.md), D9b) o producto liberado en G2 | B | Una de las dos: se financia la capa D (red team externo e ISO 27001 ampliada) | — | Ninguna: la capa D no se financia y la licencia para vender queda como hipótesis | Capa D de T4 (11,6-31 de caja) |
| G3 | SLO del piloto a las 6 semanas; cero filtración entre tenants; red team del piloto | P | Cumplidos | SLO incumplido: vuelve a L0-L1 y se revisa | Una filtración, o críticos tras dos ciclos: se cancela la función | P: 21 / 23 |
| G4 | Trayectoria al equilibrio (~17% de throughput; ~23% si sigue el producto; menos si la capacidad se vende) **o** interés contractual en el producto | I/P | Una de las dos | — | Ninguna: no se financia el régimen (~143, ~188 con P); queda el frente interno con las licencias vigentes y la base mínima (~53 mil por año, en el presupuesto 2028) | Año 2 |
| G4 | Tecnología ≥85%; Operaciones habilitadas ≥60%; red team externo sin críticos, si se financió | B/I | Cumplidos | Se informa contra el OKR, con las dos métricas | — | Año 2 |

**Regla de riesgo residual.** Ningún gate pasa con un riesgo residual en la
franja "no se acepta" del [Anexo C](03-gobierno-seguridad.md); los residuales
que acepta el Council llevan fecha de revisión.

**Casos de prueba:**

- **Adopción de Tecnología en 70% en G2:** cae en "espera". T3 se libera, la
  formación se rediseña y se vuelve a medir al cierre de T3. Con <60%, corta la
  expansión de seats, no el plan.
- **Throughput de +6%:** en G2 pasa (≥ +3%). En G3 queda en "espera": se libera
  solo la base mínima y se vuelve a medir a las 6 semanas; si sigue debajo de
  +8%, T4 corre con la base mínima, y G4 decide sin trayectoria al equilibrio.
- **Pesimista (+0,5% en G2):** espera; a las 6 semanas sigue debajo de +3%, y se
  corta el frente interno en T3. Queda la base mínima ([Anexo E](05-business-case.md)).
- **Sin señal de cliente en G2 (base):** P no entra al año. No se liberan el
  consumo, el red team ni la infraestructura del piloto; las condiciones de P en
  G3 no aplican; G4 decide con el frente interno y la base común.

### Escenarios

Tomados del [Anexo E](05-business-case.md). El pesimista se muestra de dos
formas: con los gates ejecutados y como estrés sin frenar.

| Escenario | Supuestos | Qué pasa con el roadmap | Resultado del año (miles de USD) |
|---|---|---|---|
| Pesimista, ejecutado | Throughput 5%, rampa 0/10/30/60; sin señal de cliente | Espera en G2 (+0,5%); vence a las 6 semanas y corta el frente interno; queda la base mínima | Neto ≈ −262 (el año cuesta ~265, hasta 388). Si la espera no venciera, corta en G3 (+1,5%): ≈ −300 |
| Pesimista, estrés sin frenar | Lo mismo, sin aplicar los gates | Base común e interno enteros | −382; −502 si el precio pasa a 12× desde T3 |
| Base | Throughput 15%, rampa 0/25/60/100; precio plano; sin señal en G2 | Producto diferido; G4 con el frente interno | ROI económico −84%; neto acumulado −332 (−409 si G2 libera el producto) |
| Optimista | Throughput 25%, rampa 0/40/80/100; señal en G2 y un cliente con interés contractual en G4 | Piloto en T3-T4; en G4 se decide el primer compromiso contractual, que rige después | ROI económico −76% (con el tramo de producto) |

En ninguno el ROI a 12 meses es positivo con productividad sola, y el
beneficio de caja es cero en los tres ([Anexo E](05-business-case.md)). La
diferencia entre el pesimista ejecutado y el estrés, ~120 mil (~82 si la espera
no venciera), es lo que compran los gates. El estrés con el producto desde T2
daría −480: diferirlo protege aparte.

### Contingencias

| Disparador | Contingencia | Fuente |
|---|---|---|
| El proveedor pasa a cobrar por consumo | Gateway con ruteo, caché y topes; a más de 6× efectivo sin mitigar, se congela la expansión. A 12×, el incremental anual es de 211-267 mil: exposición de la empresa, con o sin plan | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| El contractor no se aprueba o su 0,2 libre de T2 se va en el traspaso | Rige la excepción acotada de 0,3 FTE en T2, aprobada como respaldo en G0 (+5 mil de tiempo) | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| Pérdida parcial del cliente principal | Se congelan los gates de T2-T4 hasta revisar el techo; con 20% menos de facturación, la caja pesa 25% más | [Anexo E](05-business-case.md) |
| Incidente de datos de un cliente | Se suspende la IA sobre ese cliente y se reporta el mismo día | [Anexo C](03-gobierno-seguridad.md) |
| Primer secreto expuesto | Revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo | [Anexo C](03-gobierno-seguridad.md) |
| Se va una persona clave sin suplente | Se congelan altas de casos de riesgo alto y se baja el alcance del trimestre siguiente | [Anexo C](03-gobierno-seguridad.md), [Anexo B](02-arquitectura.md) |
| La utilización cae bajo 80% dos meses por el plan | Se recorta el frente que más tiempo consume | [Anexo E](05-business-case.md), [Anexo D](04-personas-cultura.md) |
| La habilitación externa de un producto propio coincide con T2-T3 | El piloto no se pone en el camino crítico de esa habilitación | Criterio del CAIO sobre [ingresos](../../context/hechos/estructura-de-ingresos.md) |
| Cortar en un gate | Cierre: un mes de preaviso del contractor y del laboratorio, pagado con la reserva de cierre de G0; legal y red team por etapa | [Anexo E](05-business-case.md) |

## Riesgos y mitigación

Registro consolidado: los riesgos que cambian el roadmap. El detalle está en el
anexo de cada dueño.

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: con el producto diferido y el replan, T2-T4 piden 2,2 / 2,2 / 2,1 FTE clave contra 1-2,25, sin holgura (3,7 / 3,1 en T3-T4 si G2 libera el producto) | Alta | Alto | Piso confirmado en G0; T1-E entra con 1,6; la excepción de T2 como respaldo (DP1) | T1 excede el sobre aprobado: T2 solo con replan |
| El replan de T2 depende de 0,2 FTE libres del contractor, que `people` no confirmó | Media | Medio | Excepción acotada aprobada en G0 | Contractor no aprobado: T2 con 2,5 FTE clave |
| Cambio a pago por consumo | Alta | Alto | Gateway y FinOps desde T2; prueba de portabilidad y costo | Más de 6× efectivo en un trimestre |
| Datos de un cliente llegan a un modelo externo | Media | Muy alto | Matriz, *default-deny*, pasarela; bloqueo de secretos y datos prohibidos que nunca pasa a monitoreo | Un incidente confirmado |
| Superficies de IA que no pasan por el gateway | Alta | Alto | Matriz superficie→control→telemetría y prueba de bypass en T2 ([Anexo B](02-arquitectura.md), [Anexo C](03-gobierno-seguridad.md)) | Bypass sin control compensatorio |
| La productividad no aparece o trae retrabajo | Media | Alto | Base congelada y costo por PR aceptado; la espera de G2 vence a las 6 semanas | Debajo de +3% al vencer la espera de G2, o menos de +5% en G3 |
| Cumplir el OKR de +20% cubre el régimen sin producto solo en el medio (equilibrio ~17%, 9%-46%; ~23% con el producto) | Alta | Medio | El caso no descansa solo en productividad: producto y riesgo (DP8) | Sin trayectoria ni interés contractual en G4 |
| La hipótesis de producto no tiene comprador | Media | Medio | Señal de cliente exigida en G2; el tramo P no se gasta sin ella | Sin señal en G2 |
| La licencia para vender no se confirma | Media | Medio | Evidencia contractual en T1; capa D condicionada en G3 | Sin señal contractual en G3 |
| Alto riesgo regulatorio fuera del crédito | Media | Alto | Clasificación caso por caso (empleo, educación y otros usos); la fecha del Anexo III del AI Act que cita C (2027-12-02) cae dentro de T4; Legal externo confirma | Un caso clasificado de alto riesgo sin dictamen |
| Capacidad crítica en pocas personas | Alta | Alto | Suplentes, runbooks, contractor con traspaso | Hito crítico sin suplente al cierre de T2 |
| Operaciones no puede adoptar por contrato del cliente | Alta | Medio | Dos métricas publicadas, con denominadores | Matriz sin completar al cierre de T1 |
| Prompt injection en agentes con herramientas | Media | Alto | Mínimo privilegio, gate humano, red team | Acción fuera de alcance en pruebas |
| Declarar controles o certificaciones que no existen | Baja | Muy alto | Toda afirmación comercial la valida seguridad | Una afirmación sin evidencia en una propuesta |
| El gobierno frena la entrega y el uso migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles | Más del 20% fuera de SLA dos meses |

## Decisiones

### Decisiones del CAIO sobre los titulares

Seis cruces que dejaron abiertos los dueños. Las tres primeras ya son la base de
E: elegir la otra opción obliga a recalcular E, y la alternativa queda costeada.

| Decisión | Elegida | Alternativa a la vista | Por qué | Tipo |
|---|---|---|---|---|
| T2 | Replan de B (2,2 FTE clave, tiempo del año 217, económico 394) con la excepción como respaldo aprobado en G0 | Excepción acotada (2,5 FTE clave, tiempo 223, económico 399), que saca ~3-8 mil de horas facturables | El recurso escaso es el tiempo clave; el replan no suma caja. Depende del 0,2 libre del contractor, pendiente de `people` | Reversible: el respaldo entra sin nueva aprobación |
| Redondeo de techos | Hacia arriba: 33 de caja, 62 de tiempo, 41 de base mínima | El número redondo (32 / 61 / 40) y recortar componentes | La autorización nunca queda debajo del cálculo (32,2 y 40,2) | Reversible |
| Capa D del Anexo C | En la base como cota superior, con la liberación condicionada en G3 a la señal contractual | Tramo condicional como P: caja base 152 (85-220), techo de T4 59, tramo de 25 (13-36) | La evidencia contractual no depende de la señal de producto; contar el renglón y condicionar el gasto compatibiliza E y C | Reversible hasta G3 |
| Equilibrio en las slides | ~17% sin producto, con ~23% con el producto en la misma línea | ~23% como titular: "cumplir la meta no alcanza" | El producto lo tiene que pagar el producto. ~17% está 3 puntos debajo del +20%: la meta cubre el régimen en el medio, sin certeza (9%-46%) | Reversible |
| Espera de G2 | Vence a las 6 semanas: si sigue en la banda, se corta el frente interno (pesimista ≈ −262) | Sin salida: T3 entero y corte en G3 (≈ −300) | Una espera sin regla de salida es gasto sin techo; los gates pasan a ahorrar ~120 en lugar de ~82 | Reversible |
| Alcance del corte de G3 | Frente interno y base común; queda la base mínima en T4 | Solo el frente interno: ≈ −369, casi igual al estrés (−382) | Si el corte no alcanza a la base común, el gate de throughput casi no protege | Reversible |

**Propuesta para `finance`:** con la espera que vence, la fila "con la regla
vigente" del pesimista en E pasa a ser la alternativa, y la "regla propuesta",
la vigente. Ver el reporte de integración.

### Hipótesis de producto (M1U2 aplicado: RICE ajustado por riesgo)

La tesis "IA que se vende" necesita un caso concreto. El CAIO elige **una**
hipótesis y la compara con dos alternativas y con no tener frente producto. Los
puntajes son **supuestos del CAIO, sin medición**: el curso no da una fórmula
para el riesgo, así que el factor 1-3 que divide el puntaje es una propuesta del
equipo ([ficha RICE](../../material/conceptos/m1u2-rice-ajustado-por-riesgo.md)).
El equipo y el Council los validan en G1.

**Hipótesis elegida: asistente de integración en la plataforma propia.**

| Campo | Hipótesis | Estado |
|---|---|---|
| Usuario | El desarrollador de un banco o fintech cliente que integra funcionalidades de la plataforma | Supuesto |
| Tarea | Encontrar la funcionalidad, armar la llamada e interpretar errores en el sandbox | Supuesto |
| Outcome | Tiempo hasta la primera integración exitosa en sandbox, y consultas de integración al soporte por integración | Sin línea de base: se mide en las semanas 1-4 de T3, si P se libera |
| Datos | Documentación técnica y de referencia de la plataforma, propiedad de Acme Labs, y un sandbox con datos sintéticos. Ningún dato productivo de cliente | Fijado por el catálogo |
| Autonomía | L1: sugiere, el desarrollador ejecuta | Propuesto |
| SLO | Parte de los umbrales propuestos de la ficha de evaluación del [Anexo B](02-arquitectura.md) (exactitud, cita, cero cruces de tenant), recalibrados al caso antes de T3; medido a las 6 semanas (plazo ilustrativo del curso) | Pendiente |
| Costo máximo | El tramo P: 37 (16-59) de caja y 39 (23-56) de tiempo ([Anexo E](05-business-case.md)) | Costeado |
| Señal comercial (G2) | Un cliente acepta por escrito, sin compromiso, evaluar el asistente en el sandbox con datos sintéticos | Propuesta del CAIO, pendiente de acuerdo del equipo |
| Contingencia sin señal | P se difiere; el método queda como capacidad del frente interno y no se presenta como producto | Fijado por los gates |

**Comparación.** Reach: 3 = los clientes de la plataforma; 2 = un segmento
nuevo; 1 = un producto que todavía no factura. Impact y Confidence, con la
escala del curso. Effort en persona-trimestres de personas clave.

| Opción | Reach | Impact | Confidence | Effort | Riesgo | Puntaje | Por qué |
|---|---|---|---|---|---|---|---|
| **1. Asistente de integración en la plataforma propia** | 3 | 1 | 50% | 2,5 (el tramo P de E) | 1 | **0,60** | La línea de soporte de la plataforma es la de mayor margen relativo ([ingresos](../../context/hechos/estructura-de-ingresos.md)); reutiliza el gateway, el harness y la ficha de evaluación del caso interno; sin datos de cliente |
| 2. Función en el producto propio de medios de pago | 1 | 2 | 50% | 3 (supuesto: suma trabajo de cumplimiento sin costear) | 3 | 0,11 | Producto sin legado, pero con habilitación externa que puede caer en T2-T3 y sin sistema de gestión certificado ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) |
| 3. Servicio de implementación de agentes de código para otras software factories | 2 | 1 | 50% | 4 (supuesto: consume las personas clave que no entran) | 2 | 0,13 | Segmento de la propuesta al Directorio ([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)); el programa de partners exige certificaciones y despliegues que no hay, y compite con horas facturables |
| 4. Solo gobierno y eficiencia, sin frente producto | — | — | — | 0 | — | No aplica | Ahorra un tramo que hoy no se gasta. Deja el plan en ROI −84% y sin opción de ingreso; la tesis pasa a ser solo eficiencia ([Anexo E](05-business-case.md), alternativa B) |

El producto propio que maneja datos de categoría especial queda fuera sin
puntuar: su riesgo choca con la regla de datos del horizonte. Tensión a la
vista: la propuesta al Directorio esperaba los primeros casos productivos en los
productos propios, porque ahí Acme Labs decide las herramientas
([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)). La opción 1
cumple esa condición: la plataforma también es propia.

**Por qué merece la inversión, y por qué hoy no la recibe.** Es la única opción
que prueba disposición a pagar sin datos de cliente, con el menor esfuerzo
incremental, sobre la línea de mayor margen. Aun así, **hoy está diferida**: el
tramo P solo se libera con la señal de G2, y hasta entonces cuesta cero. Se
compara con la alternativa 4 recién en G2, con la señal en la mano. Es
reversible hasta la firma de G4. Quién valida los puntajes: el equipo con el
Council (**pendiente**).

### Catálogo único de decisiones

Une las puertas del [Anexo B](02-arquitectura.md) y el catálogo D7b del
[Anexo C](03-gobierno-seguridad.md). Separa tres pasos: **aprobación interna**,
**negociación no vinculante** y **firma**. Regla del horizonte: en los 12 meses
ningún dato productivo de cliente va a un modelo, y ninguna excepción la
contradice.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto | Tipo |
|---|---|---|---|---|---|---|
| Pedido G0 (T1-E, piso de capacidad y marco de gates) | Interno | G0 | Directorio | Techo confirmado | Hasta 33 de caja más 6 de reserva de cierre y 62 de tiempo | Reversible: cortar en G1 cuesta 73 en el medio, hasta 106 hasta cerrar y 146 en el año ([Anexo E](05-business-case.md)) |
| Vía de IA aplicada de T1 | Interno | G0 | Directorio | DP3 | Contrato corto, un mes de preaviso | Reversible |
| Capacidad de T2-T4: replan o excepción en T2, con el producto diferido | Interno | G0 | Directorio | DP1 | Sobre escrito por trimestre | Reversible en cada gate |
| Capacitar y reasignar en vez de contratar | Interno | G0 | Directorio | — | — | Reversible; se revisa en G2 |
| Sin crédito ni scoring; clasificación caso por caso | Producto | G0 | Directorio | — | Alcance del año | Reversible: reabrir es decisión de G4, que rige después |
| Ratificar la política de IA | Interno | T1 | Directorio | G0 aprobado | Compromiso interno enmendable; sin firma con clientes | Reversible con costo de credibilidad; revisión anual y extraordinaria en G2 |
| Postura sobre el empleo (DP4) | Interno | G0 o T1 | Directorio, con asesoría laboral | — | Texto comunicado | Poco reversible una vez comunicada |
| Liberar el tramo de producto | Interno | G2 | Directorio | Señal de cliente | P: 38 / 34 en T3, 21 / 23 en T4 | Reversible en G3 |
| Financiar la capa D | Interno | G3 | Directorio | Señal contractual o P liberado | Red team externo e ISO ampliada | Reversible |
| Modelo, proveedor, herramientas detrás del gateway | Interno | T2 | Dirección técnica | Evals como árbitro | — | Reversible |
| Cláusula tipo de IA | Interno | T3 | Council | Una función con ficha y supervisión humana | Texto listo | Reversible |
| Conversar la cláusula con un cliente | Negociación | T3 | Comercial con `governance` | Sin firma, sin datos, sin compromiso | Ninguno | Reversible |
| Firmar un compromiso contractual de IA con un cliente | Externo | G4 | Council | Cláusula tipo, matriz del cliente, red team sin críticos | Firmado; rige después del horizonte | **Irreversible** |
| Enviar datos productivos de un cliente a un modelo | Externo | Prohibido en el horizonte; la excepción la decide G4 | Responsable comercial con el Council | Cláusula firmada, matriz, controles demostrados | Rige después del horizonte | **Irreversible** |
| Ajustar un modelo con datos de cliente | Externo | Fuera del horizonte | — | — | — | **Irreversible** |
| Subir una función del producto a L3 | Externo | G4 | Council | Evidencia del piloto y red team externo sin críticos | Rige después del horizonte | **Irreversible** una vez activa |
| L4 fuera de sandbox o con efectos externos | Externo | Fuera del horizonte | Council | Decisión de G4 para el plan siguiente | Prohibido hasta entonces | **Irreversible** |
| Hardware propio o consumo comprometido a más de 12 meses | Interno | G4 | Directorio | Escenario de consumo | Contrato | **Irreversible** |

Ninguna decisión irreversible se toma antes de G4, y las que se toman en G4
rigen para el plan siguiente.

### Decisiones pendientes para el board o el equipo

| # | Tensión | Alternativas | Propuesta del CAIO | Decide |
|---|---|---|---|---|
| DP1 | T1-E entra en el sobre clave (1,6 contra 1-2,25 FTE). T2-T4 entran solo con el producto diferido y el replan, sin holgura ([Anexo E](05-business-case.md)) | (a) Producto desde T2, ampliando el sobre a ~3,7 FTE clave, que sale de horas facturables. (b) Diferir el producto hasta la señal de G2: 2,2 / 2,2 / 2,1 con el replan de T2 de B, o 2,5 en T2 con la excepción acotada. Además, lectura del sobre: estricta (todo contra 1-2,25) o separada (horas distribuidas como segundo sobre) | (b) con el replan y la excepción como respaldo; si G2 trae la señal, el board decide ampliar el sobre de T3-T4. Lectura separada, aprobada explícitamente. Piso del sobre ≥1,6 FTE en T1, a confirmar | Board, en G0 |
| DP2 | La caja del plan suma gasto de tecnología, contra el OKR de menos de 3,5% de la facturación | A. Mantener el resultado clave y recortar el plan. B. Medirlo sin la inversión del plan. C. Medirlo por persona activa | B o C: el OKR mide eficiencia de la base, no la inversión | Directorio, en el presupuesto 2027 |
| DP3 | IA aplicada en T1: rol interno de 0,3 FTE (B) o contractor B1 al 50% (D, E) | A. Rol interno, si demuestra experiencia antes de G0. B1. Contractor desde T1, que reemplaza la fracción de B en T2-T4 | B1: el recurso que no entra es el tiempo clave (1,6 contra 1,9 FTE), con ~13 mil más de caja. Choca con "no contratar" | Directorio, en G0 |
| DP4 | Compromiso sobre el empleo ([Anexo D](04-personas-cultura.md), D3) | A. Sin compromiso. B. La ganancia por IA no se usa para desvincular en 12 meses. C. B con excepciones | C, como propone D: baja el miedo sin atar todo el margen. No es política aprobada; el costo no está cuantificado | Directorio, con asesoría laboral |
| DP5 | Meta de adopción: el 80% combinado del OKR no se alcanza ni con las metas del plan (Tecnología 85% y Operaciones habilitadas 60% dan como mucho 72,5%) | A. Mantener el 80% combinado. B. Reemplazarlo por dos métricas con denominador | B: Tecnología ≥80% desde T2 (OKR) y ≥85% en T4; Operaciones habilitadas, con su valor sobre el total al lado. Ninguna meta propia se presenta como cumplimiento del 80% | Directorio, con el OKR 2027 |
| DP6 | Staffing facturado por hora desincentiva el uso de IA ([Anexo E](05-business-case.md)) | A. Productividad 0 en staffing. B. Precio por resultado | A en los 12 meses; B como opción del año 2 | Directorio, año 2 |
| DP7 | Solapes de costo que quedan ([Anexo E](05-business-case.md)): pruebas de bypass (B y C), red team (B 5-15 contra C 10-25), gateway y pasarela, seguridad. IA aplicada e infraestructura sin piloto ya están consolidadas | Contar los dos renglones o consolidar | El base cuenta los dos hasta que confirmen los dueños | `architect`, `governance` |
| DP8 | El equilibrio a régimen pide ~17% de throughput sin producto, 3 puntos debajo del +20% del OKR: la meta cubre el régimen en el medio, sin certeza (~23% con el producto, donde no alcanza) | A. Subir la meta. B. Vender la capacidad liberada (se calcula en `private/`). C. Apoyar el caso también en producto y riesgo, no solo en productividad | C, dicho sin vueltas ante el board; B se evalúa en G2 cuando se decide el destino de la capacidad | Directorio |

## Cautelas

- **Borrador sin verificación humana.** Las fichas de `context/` están en
  `draft`; las fracciones de FTE, las bandas de espera, los plazos de 6 semanas,
  los costos de cierre y la separación del sobre son supuestos sin ficha propia
  todavía.
- Los umbrales de los gates son supuestos del equipo de cada anexo, a calibrar
  con la línea de base de T1.
- Los puntajes RICE de la hipótesis de producto son juicio del CAIO, sin
  medición ni validación del equipo; el outcome no tiene línea de base.
- El plazo de 6 semanas del SLO del piloto es ilustrativo del curso.
- La enrutabilidad de cada superficie de IA no está verificada con
  documentación de proveedor: se prueba en T2.
- La fecha del Anexo III del AI Act viene de la lectura del Anexo C, sin cotejo
  del texto consolidado; no va a una slide.
- La anonimización del caso necesita revisión de un humano autorizado: los
  alias y rangos de concentración siguen siendo inferibles para quien conozca la
  cartera. Este anexo no asocia clientes con productos, segmentos ni calendarios.
- Responsable humano de cada gate y de cada decisión: **pendiente**.
