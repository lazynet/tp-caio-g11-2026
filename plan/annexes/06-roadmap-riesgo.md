---
owner: caio
status: draft
title: "Anexo F — Roadmap ajustado por riesgo"
---

# Anexo F — Roadmap ajustado por riesgo

Slides que sustenta: [Slide 7 — Roadmap técnico, financiero y cultural](../slides.md)
y [Slide 9 — Riesgos, escenarios y decisiones reversibles](../slides.md).

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
con techo de caja y de capacidad, adoptar el marco de gates y elegir hoy cómo se
cubre la capacidad de T2-T4. El resto del año no se aprueba hoy.

Las cifras vienen del anexo que se cita. Lo que este anexo agrega son decisiones
del CAIO (bandas de espera fuera de lo económico, plazos de corrección, el
calendario único y el catálogo de decisiones), marcadas como propuestas. Donde
dos anexos chocan, queda como decisión pendiente. Responsable humano de cada
gate y de cada decisión: **pendiente**.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Convención de tiempo | T0 = cuarto trimestre de 2026, antes de G0; T1 = enero-marzo de 2027 … T4 = octubre-diciembre de 2027. El Q1-Q4 de los Anexos B y C se lee como T1-T4 | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo E](05-business-case.md) |
| Patrón de gates | Kill/scale por etapa, con criterio de éxito y de abandono declarados antes de empezar | [Kill/scale gates](../../material/conceptos/m1u2-kill-scale-gates.md), [kill-fast](../../material/conceptos/m1u1-kill-fast.md) |
| Primeros 100 días | T1 absorbe el diagnóstico y la base: inventario, línea de base, política, matriz | [Plan de 100 días](../../material/conceptos/m1u2-plan-100-dias.md) |
| Capacidad | Utilización 83%-90%, bench menor a 1 FTE, restricción de no contratar; sobre de 1-2,25 FTE de personas clave | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md), [sobre](../../context/supuestos/capacidad-de-inversion.md) |
| Clientes principales | Su continuidad es el escenario base; su pérdida parcial es estrés | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |
| Calendario externo | Un producto propio en inversión depende de una habilitación externa con fecha dentro de 2027, que puede superponerse con T2-T3 | [Ingresos](../../context/hechos/estructura-de-ingresos.md) |
| Throughput | Unidad: PR aceptado por persona activa en equipos propios. Se valúa como horas evitadas a output fijo, g/(1+g) (lectura A), y no es caja | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |

## Evidencia

### Pedido G0, único

Es el mismo pedido en la portada, las slides 3, 4 y 8, y los Anexos B y E.

| Elemento | Qué se aprueba | Fuente |
|---|---|---|
| 1. T1 en su versión acotada (T1-E) | Inventario de datos, línea de base congelada, matriz superficie→control→telemetría, telemetría unificada, matriz de clientes, política ratificada, nivel básico. El gateway pasa a T2 | [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md) |
| 2. Techo de caja de T1 | Hasta 32 mil USD (contractor hasta 16,5, legal hasta 10, telemetría hasta 1,5 y contingencia) | [Anexo E](05-business-case.md) |
| 3. Techo de tiempo de T1 | Hasta 61 mil: 1,6 FTE de personas clave (0,70× del sobre) y 590 h distribuidas en la dotación | [Anexo E](05-business-case.md) |
| 4. T0 ya ejecutado | Ratificar hasta 7 mil de tiempo | [Anexo E](05-business-case.md) |
| 5. IA aplicada de T1 | Contractor B1, o un rol interno si demuestra experiencia en evals y harness antes de G0 (DP3) | [Anexo B](02-arquitectura.md), [Anexo D](04-personas-cultura.md) |
| 6. Capacidad de T2-T4 | Elegir y dejar escrito: ampliar el sobre clave o diferir el producto, y la lectura del sobre (DP1) | [Anexo E](05-business-case.md) |
| 7. Marco de gates | Las tablas de abajo como regla de liberación de fondos | Este anexo |

El techo de caja se confirma contra el presupuesto 2027 en `private/`. Fuera del
pedido: T2-T4, el modelo propio, compromisos a más de 12 meses y todo compromiso
con clientes.

### Calendario único de T0 y T1 (decisión del CAIO)

B y D ubicaban la línea de base en lugares distintos (B: retrospectiva congelada
al cierre del mes 1 de T1; D: retrospectiva en T0 y base prospectiva en las
semanas 1-4 de T1). E costeó las dos. El CAIO propone una sola secuencia:

| Cuándo | Qué | Quién verifica | Costo |
|---|---|---|---|
| Antes de G0 (T0) | Verificar que existe historial de PR, integración continua, incidentes y tickets (B); serie retrospectiva de uso, incidentes y retrabajo, y diseño de la encuesta de chat y suite ofimática (D). La política queda lista para ratificar, no ratificada | Pendiente; el Directorio ve el resultado en G0 | 1,8-6,7 mil de tiempo, ratificado en G0 ([Anexo E](05-business-case.md)) |
| T1, semanas 1-4 | **Base prospectiva congelada** con la unidad de B, antes de cualquier formación o herramienta nueva | Oficina del CAIO, con `finance` | Dentro de T1 |
| T1, semanas 5-13 | Política ratificada, matriz de clientes, básico, champions, intermedio de Tecnología, matriz de superficies y telemetría | `governance`, área comercial, `architect` | Dentro de T1 |
| T2 en adelante | Gateway, formación de Operaciones y staff; medición contra la base congelada | Oficina del CAIO | Techos por gate |

La serie retrospectiva sirve para estimar tendencia y ruido; **la ganancia se
atribuye solo contra la base prospectiva**, y no antes de T2 (la rampa base es 0%
en T1, [rampa](../../context/supuestos/rampa-de-la-ganancia.md)). Alternativa a la
vista: usar la retrospectiva de B como base si cuatro semanas resultan
demasiado ruidosas; lo decide la oficina del CAIO en la semana 4. El Anexo B
tiene que alinear su hito de línea base con esta secuencia (pendiente de
`architect`). Quién autoriza gastar T0 antes del presupuesto: **pendiente**.

### Línea de tiempo integrada

| Trim. | Técnico (B) | Gobierno y seguridad (C) | Cultural (D) | Financiero (E): techo caja / tiempo |
|---|---|---|---|---|
| T0 | Verificación del historial | Política lista para ratificar | Serie retrospectiva y diseño de la encuesta | — (hasta 7 de tiempo) |
| T1 | Inventario de datos; base congelada; matriz de superficies; telemetría unificada | Política ratificada; inventario v1; matriz de clientes; intake en 3 niveles | Básico para todos; champions; intermedio de Tecnología | 32 / 61 |
| T2 | Gateway con 2 proveedores; harness v1; evals en CI; portabilidad; FinOps | Pasarela y DLP; prueba de bypass por superficie; red team interno; ejercicio de incidentes | Intermedio para Operaciones y staff; champions con tiempo | 70 / 138 |
| T3 | Piloto en un producto propio (L1-L2, datos sintéticos), **solo si G2 lo libera**; aislamiento por tenant | Amenazas de la función; criterios de eval; cláusula tipo, sin firma | Casos por rol; calidad de prompts | 97 / 111 |
| T4 | Gate del piloto; go/no-go de modelo propio; productividad contra la base | Red team externo; ISO 27001 extendida a IA; gate de 42001 | Traspaso del contractor; Tecnología ≥85% | 115 / 91 |

Techos máximos por trimestre, en miles de USD ([Anexo E](05-business-case.md)).
El año, con contingencia: caja de 114-314 mil y tiempo de 150-408 mil, unos
4,5 FTE promedio (3,0 de personas clave). Con el frente producto, las personas
clave suman 3,5 / 3,7 / 3,1 FTE en T2-T4; si se difiere, 2,5 / 2,2 / 2,1.

### Gates por condición (pasa, espera, corta)

Cada condición tiene su resultado y su acción. Un "espera" libera solo lo que
dice la fila y fija un plazo para volver a medir. Las condiciones de un frente
no frenan al otro: **B** = base común, **I** = frente interno, **P** = frente
producto. Si P se difirió, sus condiciones son "no aplica" y sus fondos no se
liberan. Bandas económicas: [Anexo E](05-business-case.md); el resto, propuesta
del CAIO sobre los umbrales de B, C y D.

| Gate | Condición | Fr. | Pasa | Espera (plazo) | Corta | Fondos que afecta |
|---|---|---|---|---|---|---|
| G0 | Pedido G0 completo y techo confirmado | B | Aprobado | — | No arranca T1; T0 queda hundido (≤7) | T1: 32 / 61 |
| G0 | Vía de IA aplicada de T1 | B | B1 o rol interno demostrado | — | Ninguna: los hitos de IA aplicada pasan a T2 | Contractor de T1 |
| G1 | Base congelada con la unidad de B | I | Congelada con fecha | Historial insuficiente: 6 semanas más; no se atribuye ganancia | Sin base al cierre de la espera: se elimina el resultado clave de throughput y el frente interno no escala | Escalado de T2 |
| G1 | Política ratificada | B | Ratificada | En el orden del día sin votar: 6 semanas; T2 sin casos de cliente | No ratificada: no hay frente producto en el año | Fondos de P |
| G1 | Matriz de los clientes que concentran la facturación | P | Completa | Contratos ambiguos: *default-deny* y revisión legal hasta el mes 4 | Más del 30% ambiguo al mes 4: sin piloto con ese cliente; Operaciones sin meta | Fondos de P |
| G1 | Básico ≥90% de la dotación | I | ≥90% | 50%-90%: se libera T2 y se rediseña el formato | <50% al cierre de T2: cambio de formato, no se repite el curso | Capacitación de T2 |
| G1 | Uso de T1 dentro del sobre aprobado | B | Dentro | — | Excedido: T2 solo con replan de capacidad aprobado | T2 entero |
| G2 | Throughput como tendencia con intervalo, sin más retrabajo | I | ≥ +3% | 0% a +3%, o intervalo que cruza +3%: T3 sin escalado; se vuelve a medir a las 6 semanas | Sin mejora o con más retrabajo: queda la base mínima | T3: 97 / 111 |
| G2 | Uso semanal de Tecnología | I | ≥80% | 60%-80%: T3 sigue; formación rediseñada con casos por rol; se vuelve a medir al cierre de T3 | <60%: se frena la expansión de seats | Expansión de seats |
| G2 | Cobertura de controles | B | ≥90% de los eventos del agente de código y de los casos propios por el gateway; 100% de superficies con control verificado | Superficie con bypass sin control compensatorio: se declara no cubierta y va al Council | Gateway sin operar más de un trimestre: se compra una solución | Infraestructura |
| G2 | Red team interno y ensayo de portabilidad | B | Críticos cerrados; portabilidad ≤20 días-persona | Críticos abiertos: el piloto no arranca hasta cerrarlos. Portabilidad >20: sin compromisos de volumen y umbral recalibrado | — | Piloto de T3 |
| G2 | FinOps: múltiplo de consumo medido | B | ≤6× efectivo | — | >6× sin mitigar en un trimestre: se congela la expansión y se topea el consumo | Expansión |
| G2 | Señal de cliente (definida en la ficha de experimento) | P | Señal cumplida: el piloto entra en T3 según la opción de DP1 | — | Sin señal: P se difiere; sus condiciones de G3 no aplican | Consumo y red team del piloto |
| G3 | Throughput | I | ≥ +8% | +5% a +8%: solo base mínima y mantenimiento; se vuelve a medir a las 6 semanas. Si sigue debajo de +8%, T4 se ejecuta con la base mínima | < +5%: corte del frente interno | T4: 115 / 91 |
| G3 | Costo por PR aceptado | I | No sube | Sube con throughput en alza: se revisa el consumo en FinOps | Sube con throughput plano: se aplica el corte de arriba | Consumo |
| G3 | SLO del piloto a las 6 semanas; cero filtración entre tenants; red team del piloto | P | Cumplidos | SLO incumplido: vuelve a L0-L1 y se revisa | Una filtración, o críticos tras dos ciclos: se cancela la función | Fondos de P en T4 |
| G4 | Trayectoria al equilibrio (~23% de throughput, menos si la capacidad se vende) **o** interés contractual en el producto | I/P | Una de las dos | — | Ninguna: no se renueva el régimen; queda el frente interno con controles | Año 2 |
| G4 | Tecnología ≥85%; Operaciones habilitadas ≥60%; red team externo sin críticos | B/I | Cumplidos | Se informa contra el OKR, con las dos métricas | — | Año 2 |

**Casos de prueba que pidió la revisión del board:**

- **Adopción de Tecnología en 70% en G2:** cae en "espera". T3 se libera, la
  formación se rediseña y se vuelve a medir al cierre de T3. Con <60%, corta la
  expansión de seats, no el plan.
- **Throughput de +6%:** en G2 pasa (≥ +3%). En G3 queda en "espera": se libera
  solo la base mínima y se vuelve a medir a las 6 semanas; si sigue debajo de
  +8%, T4 corre con la base mínima, y G4 decide sin trayectoria al equilibrio.
- **Producto diferido:** en G2 sin señal, P sale del año. No se liberan el
  consumo ni el red team del piloto; las condiciones de P en G3 no aplican; G4
  decide solo con el frente interno y la base común.

### Escenarios

Tomados del [Anexo E](05-business-case.md). El pesimista se muestra de dos
formas: con los gates ejecutados y como estrés sin frenar.

| Escenario | Supuestos | Qué pasa con el roadmap | Resultado del año (miles de USD) |
|---|---|---|---|
| Pesimista, ejecutado | Throughput 5%, rampa 0/10/30/60; sin señal de cliente | Corte en G2: queda la base mínima (gobierno y pasarela) | Neto ≈ −245 (el año cuesta ~247, hasta 362) |
| Pesimista, estrés sin frenar | Lo mismo, sin aplicar los gates | Todo el año ejecutado | −481; −601 si el precio pasa a 12× desde T3 |
| Base | Throughput 15%, rampa 0/25/60/100; precio plano; piloto evaluado, sin contrato | G4 con frente interno y piloto evaluado | ROI económico −88%; neto acumulado −433 |
| Optimista | Throughput 25%, rampa 0/40/80/100; un cliente con interés contractual en G4 | En G4 se decide el primer compromiso contractual, que rige después | ROI económico −78% |

En ninguno el ROI a 12 meses es positivo con productividad sola, y el
beneficio de caja es cero en los tres ([Anexo E](05-business-case.md)). La
diferencia entre el pesimista ejecutado y el estrés, ~236 mil, es lo que compran
los gates.

### Contingencias

| Disparador | Contingencia | Fuente |
|---|---|---|
| El proveedor pasa a cobrar por consumo | Gateway con ruteo, caché y topes; a más de 6× efectivo sin mitigar, se congela la expansión. A 12×, el incremental anual es de 211-267 mil: exposición de la empresa, con o sin plan | [Anexo E](05-business-case.md), [Anexo B](02-arquitectura.md) |
| Pérdida parcial del cliente principal | Se congelan los gates de T2-T4 hasta revisar el techo; con 20% menos de facturación, la caja pesa 25% más | [Anexo E](05-business-case.md) |
| Incidente de datos de un cliente | Se suspende la IA sobre ese cliente y se reporta el mismo día | [Anexo C](03-gobierno-seguridad.md) |
| Primer secreto expuesto | Revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo | [Anexo C](03-gobierno-seguridad.md) |
| Se va una persona clave sin suplente | Se congelan altas de casos de riesgo alto y se baja el alcance del trimestre siguiente | [Anexo C](03-gobierno-seguridad.md), [Anexo B](02-arquitectura.md) |
| La utilización cae bajo 80% dos meses por el plan | Se recorta el frente que más tiempo consume | [Anexo E](05-business-case.md), [Anexo D](04-personas-cultura.md) |
| La habilitación externa de un producto propio coincide con T2-T3 | El piloto no se pone en el camino crítico de esa habilitación | Criterio del CAIO sobre [ingresos](../../context/hechos/estructura-de-ingresos.md) |
| Cortar en un gate | Cierre: un mes de preaviso del contractor y del laboratorio; legal y red team por etapa | [Anexo E](05-business-case.md) |

## Riesgos y mitigación

Registro consolidado: los riesgos que cambian el roadmap. El detalle está en el
anexo de cada dueño.

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: T2-T4 piden 3,5 / 3,7 / 3,1 FTE clave contra un sobre de 1-2,25 | Alta | Alto | T1-E entra en el sobre clave; la elección para T2-T4 se toma en G0 (DP1) | T1 excede el sobre aprobado: T2 solo con replan |
| Cambio a pago por consumo | Alta | Alto | Gateway y FinOps desde T2 | Más de 6× efectivo en un trimestre |
| Datos de un cliente llegan a un modelo externo | Media | Muy alto | Matriz, *default-deny*, pasarela; bloqueo de secretos y datos prohibidos que nunca pasa a monitoreo | Un incidente confirmado |
| Superficies de IA que no pasan por el gateway | Alta | Alto | Matriz superficie→control→telemetría y prueba de bypass en T2 ([Anexo B](02-arquitectura.md), [Anexo C](03-gobierno-seguridad.md)) | Bypass sin control compensatorio |
| La productividad no aparece o trae retrabajo | Media | Alto | Base congelada y costo por PR aceptado | Menos de +5% en G3 |
| Cumplir el OKR de +20% no cubre el régimen (equilibrio ~23%) | Alta | Medio | El caso descansa en producto y riesgo, no en productividad (DP8) | Sin trayectoria ni interés contractual en G4 |
| El piloto de producto no tiene comprador | Media | Medio | Señal de cliente definida en la ficha de experimento | Sin señal en G2 |
| Alto riesgo regulatorio fuera del crédito | Media | Alto | Clasificación caso por caso (empleo, educación y otros usos); la fecha del Anexo III del AI Act que cita C (2027-12-02) cae dentro de T4; Legal externo confirma | Un caso clasificado de alto riesgo sin dictamen |
| Capacidad crítica en pocas personas | Alta | Alto | Suplentes, runbooks, contractor con traspaso | Hito crítico sin suplente al cierre de T2 |
| Operaciones no puede adoptar por contrato del cliente | Alta | Medio | Dos métricas publicadas, con denominadores | Matriz sin completar al cierre de T1 |
| Prompt injection en agentes con herramientas | Media | Alto | Mínimo privilegio, gate humano, red team | Acción fuera de alcance en pruebas |
| Declarar controles o certificaciones que no existen | Baja | Muy alto | Toda afirmación comercial la valida seguridad | Una afirmación sin evidencia en una propuesta |
| El gobierno frena la entrega y el uso migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles | Más del 20% fuera de SLA dos meses |

## Decisiones

### Catálogo único de decisiones

Une las puertas del [Anexo B](02-arquitectura.md) y el catálogo D7b del
[Anexo C](03-gobierno-seguridad.md). Separa tres pasos: **aprobación interna**,
**negociación no vinculante** y **firma**. Regla del horizonte: en los 12 meses
ningún dato productivo de cliente va a un modelo, y ninguna excepción la
contradice.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto | Tipo |
|---|---|---|---|---|---|---|
| Pedido G0 (T1-E y marco de gates) | Interno | G0 | Directorio | Techo confirmado | Hasta 32 de caja y 61 de tiempo | Reversible: cortar en G1 cuesta 73 en el medio y hasta 106 ([Anexo E](05-business-case.md)) |
| Vía de IA aplicada de T1 | Interno | G0 | Directorio | DP3 | Contrato corto, un mes de preaviso | Reversible |
| Capacidad de T2-T4: ampliar o diferir | Interno | G0 | Directorio | DP1 | Sobre escrito por trimestre | Reversible en cada gate |
| Capacitar y reasignar en vez de contratar | Interno | G0 | Directorio | — | — | Reversible; se revisa en G2 |
| Sin crédito ni scoring; clasificación caso por caso | Producto | G0 | Directorio | — | Alcance del año | Reversible: reabrir es decisión de G4, que rige después |
| Ratificar la política de IA | Interno | T1 | Directorio | G0 aprobado | Compromiso interno enmendable; sin firma con clientes | Reversible con costo de credibilidad; revisión anual y extraordinaria en G2 |
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

### Ficha de experimento del frente producto (se completa en G1)

El frente producto se financia solo con una ficha completa, que elige el equipo
con el Council en G1 usando RICE ajustado por riesgo
([ficha](../../material/conceptos/m1u2-rice-ajustado-por-riesgo.md)).

| Campo | Qué se exige | Estado |
|---|---|---|
| Usuario | Un usuario del cliente, no un equipo interno de Acme Labs | Pendiente |
| Problema | Una tarea del cliente que la plataforma o un producto propio ya resuelve sin IA | Pendiente |
| Datos permitidos | Sintéticos o anonimizados; nunca productivos de cliente en el horizonte | Fijado por el catálogo |
| Outcome | Una métrica del cliente con línea de base | Pendiente |
| SLO | Fijado antes de T3, medido a las 6 semanas (plazo ilustrativo del curso) | Pendiente |
| Costo máximo | Consumo del piloto (6-24 mil) y red team del piloto (5-15 mil) | [Anexo E](05-business-case.md) |
| Evidencia comercial exigida (señal de G2) | Propuesta del CAIO: un cliente acepta por escrito, sin compromiso, evaluar el piloto con datos sintéticos | Pendiente de acuerdo del equipo |
| Contingencia sin cliente | P se difiere; lo construido queda como capacidad del frente interno y no se presenta como producto | Fijado por los gates |

Los tipos de candidato, sin asociarlos a un producto ni a un cliente concreto:

| Tipo | Cuenta como | A favor | En contra |
|---|---|---|---|
| Función de IA en la plataforma propia, usada por el cliente | Producto vendible | Es la línea de mayor margen relativo ([ingresos](../../context/hechos/estructura-de-ingresos.md)) | Usuario en un cliente financiero: matriz y aviso de uso de IA |
| Función en un producto propio en inversión | Producto vendible | Producto nuevo, sin legado | Sin sistema de gestión certificado ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)); calendario externo propio |
| Asistente para el equipo interno de soporte | **Frente interno**, no producto | Usuario interno, datos propios | No prueba disposición a pagar: se mide como eficiencia |

Es reversible hasta la firma de G4. Quién decide: el equipo con el Council
(**pendiente**).

### Decisiones pendientes para el board o el equipo

| # | Tensión | Alternativas | Propuesta del CAIO | Decide |
|---|---|---|---|---|
| DP1 | T1-E entra en el sobre clave (1,6 contra 1-2,25 FTE), pero T2-T4 no: 3,5 / 3,7 / 3,1 FTE clave con producto ([Anexo E](05-business-case.md)) | (a) Ampliar el sobre clave hasta ~3,7 FTE, que sale de horas facturables. (b) Diferir el producto hasta la señal de G2: 2,5 / 2,2 / 2,1, y T2 excede 0,3 FTE que replanea `architect`. Además, lectura del sobre: estricta (todo contra 1-2,25) o separada (horas distribuidas como segundo sobre) | (b), con una ampliación condicionada: si G2 trae la señal de cliente, el board decide en G2 ampliar el sobre para el piloto de T3. Lectura separada, aprobada explícitamente | Board, en G0 |
| DP2 | La caja del plan suma gasto de tecnología, contra el OKR de menos de 3,5% de la facturación | A. Mantener el resultado clave y recortar el plan. B. Medirlo sin la inversión del plan. C. Medirlo por persona activa | B o C: el OKR mide eficiencia de la base, no la inversión | Directorio, en el presupuesto 2027 |
| DP3 | IA aplicada en T1: rol interno de 0,3 FTE (B) o contractor B1 al 50% (D, E) | A. Rol interno, si demuestra experiencia antes de G0. B1. Contractor desde T1, que reemplaza la fracción de B en T2-T4 | B1: el recurso que no entra es el tiempo clave (1,6 contra 1,9 FTE), con ~13 mil más de caja. Choca con "no contratar" | Directorio, en G0 |
| DP4 | Compromiso sobre el empleo ([Anexo D](04-personas-cultura.md)) | A. Sin compromiso. B. La ganancia por IA no se usa para desvincular en 12 meses. C. B con excepciones | Se lleva sin elegir: B baja el miedo pero ata margen | Board |
| DP5 | Meta de adopción: el 80% combinado del OKR no se alcanza ni con las metas del plan (Tecnología 85% y Operaciones habilitadas 60% dan como mucho 72,5%) | A. Mantener el 80% combinado. B. Reemplazarlo por dos métricas con denominador | B: Tecnología ≥80% desde T2 (OKR) y ≥85% en T4; Operaciones habilitadas, con su valor sobre el total al lado. Ninguna meta propia se presenta como cumplimiento del 80% | Directorio, con el OKR 2027 |
| DP6 | Staffing facturado por hora desincentiva el uso de IA ([Anexo E](05-business-case.md)) | A. Productividad 0 en staffing. B. Precio por resultado | A en los 12 meses; B como opción del año 2 | Directorio, año 2 |
| DP7 | Solapes de costo que quedan ([Anexo E](05-business-case.md)): pruebas de bypass (B y C), red team (B 5-15 contra C 10-25), gateway y pasarela, seguridad. IA aplicada ya está consolidada | Contar los dos renglones o consolidar | El base cuenta los dos hasta que confirmen los dueños | `architect`, `governance` |
| DP8 | El equilibrio a régimen pide ~23% de throughput, por encima del +20% del OKR ([Anexo E](05-business-case.md)) | A. Subir la meta. B. Vender la capacidad liberada (se calcula en `private/`). C. Apoyar el caso en producto y riesgo, no en productividad | C, dicho sin vueltas ante el board; B se evalúa en G2 cuando se decide el destino de la capacidad | Directorio |

## Cautelas

- **Borrador sin verificación humana.** Las fichas de `context/` están en
  `draft`; las fracciones de FTE, las bandas de espera, los plazos de 6 semanas,
  los costos de cierre y la separación del sobre son supuestos sin ficha propia
  todavía.
- Los umbrales de los gates son supuestos del equipo de cada anexo, a calibrar
  con la línea de base de T1.
- El plazo de 6 semanas del SLO del piloto es ilustrativo del curso.
- La enrutabilidad de cada superficie de IA no está verificada con
  documentación de proveedor: se prueba en T2.
- La fecha del Anexo III del AI Act viene de la lectura del Anexo C, sin cotejo
  del texto consolidado; no va a una slide.
- La anonimización del caso necesita revisión de un humano autorizado: los
  alias y rangos de concentración siguen siendo inferibles para quien conozca la
  cartera. Este anexo no asocia clientes con productos, segmentos ni calendarios.
- Responsable humano de cada gate y de cada decisión pendiente: **pendiente**.
