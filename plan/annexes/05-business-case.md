---
owner: finance
status: draft
title: "Anexo E — Business case y escenarios"
---

# Anexo E — Business case y escenarios

Slide que sustenta: [Slide 8 — Business case](../slides.md). Los gates económicos
alimentan además [Slide 7 — Roadmap técnico, financiero y cultural](../slides.md) y
[Slide 9 — Riesgos, escenarios y decisiones reversibles](../slides.md).

## Objetivo

Decirle al board, con números trazables, **qué compra la plata, cuándo se ve y
cómo se frena**. La conclusión adelantada: con la valuación conservadora de este
anexo, el plan a 12 meses **no se paga con productividad interna** y no genera
caja propia. Es un año de inversión con salida por etapas. Se justifica solo si
además prende uno de dos motores: ingresos por IA en el producto o protección
del ingreso de los clientes financieros. Por eso se le pide al board un único
pedido G0 por T1, con techo máximo de caja y de capacidad, y no el año entero.

Responsable humano de cada cifra y de cada gate: **pendiente**. Ninguna cifra es
apta para entrega: todo es borrador sin verificación humana, las fichas de
`context/` están en `draft` y los costos son supuestos del equipo sin cotización.

## Supuestos de partida

**Convención de tiempo y de cálculo.** T0 es el cuarto trimestre de 2026 y T1-T4
son los trimestres de 2027; el Q1-Q4 de los Anexos B y C se lee como T1-T4. Una
persona-trimestre son 480 horas (160 por mes)
([convenciones](../../context/supuestos/convenciones-de-calculo.md)).

**Moneda y montos.** Miles de USD de mercado, por actividad y por rol. `context/`
no publica la facturación ni bases de la empresa: este anexo **no** calcula
porcentajes sobre la facturación. Da el umbral de facturación que hace falta
para que el plan entre en el techo, y lo verifica quien tiene acceso a `private/`.

| Supuesto | Valor | Ficha |
|---|---|---|
| Capacidad de inversión | Caja incremental de 1%-3% de la facturación anual, más 10%-15% del tiempo de un grupo acotado de personas clave | [Supuesto](../../context/supuestos/capacidad-de-inversion.md) |
| Costo cargado por rol | Rangos amplios de mercado en USD por mes, no calibrados contra la nómina | [Supuesto](../../context/supuestos/costo-cargado-por-rol.md) |
| Capacidad disponible | Utilización facturable 83%-90%, bench menor a 1 FTE, restricción de no contratar | [Hecho](../../context/hechos/capacidad-y-utilizacion.md) |
| Ganancia de throughput (g) | +10% a +25% por desarrollador a 12 meses, solo en equipos propios | [Supuesto](../../context/supuestos/ganancia-de-productividad.md) |
| Desarrolladores en equipos propios (N) y su costo | 15-20 personas (17,5); USD 2.500-7.000 por mes (4.750). N × costo **no** es la nómina | [Supuesto](../../context/supuestos/desarrolladores-en-equipos-propios.md) |
| Rampa de la ganancia (T1/T2/T3/T4) | Base 0/25/60/100%; pesimista 0/10/30/60%; optimista 0/40/80/100% | [Supuesto](../../context/supuestos/rampa-de-la-ganancia.md) (la ficha deja pendientes las rampas extremas: se fijan acá) |
| Poblaciones de capacitación | Básico ~65 × 6 h; intermedio ~50 × 12 h; avanzado ~10; 8 champions al 10% | [Supuesto](../../context/supuestos/poblaciones-de-capacitacion.md) |
| Precios externos y contingencia | Rangos sin cotización; 15% de contingencia sobre la caja | [Supuesto](../../context/supuestos/precios-externos-sin-cotizar.md) |
| Capacidades que hoy no existen | Gateway, inventario de arquitectura, legal dedicado a IA | [Supuesto](../../context/supuestos/capacidades-ausentes.md) |
| Suscripción del agente de código | 40-45 seats × USD 40-45 por mes = 4,8-6,1 mil por trimestre | Cálculo sobre [uso de IA](../../context/hechos/uso-ia-interno.md) y [costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real / lo pagado | ~12× en el agente de código | [Hecho](../../context/hechos/costos-tecnologia-e-ia.md) (telemetría, no factura) |
| Régimen del año 2 | Caja de ~93 mil más 1,5 FTE senior (~95 mil) | [Supuesto](../../context/supuestos/costo-de-regimen-del-ano-2.md); sigue valiendo con el escenario recomendado |
| Seats nuevos | Ninguno: la meta de adopción es de activación | [Anexo B](02-arquitectura.md) |

**Escenario de costos que consume este anexo (ronda 3).** El base pasa al
escenario recomendado de los Anexos B y D: T1 acotado (T1-b) y el contractor de
IA aplicada que **reemplaza** la fracción interna de B desde T1 (alternativa B1
del [Anexo D](04-personas-cultura.md)). El conservador de rondas anteriores
queda como alternativa costeada (ver "IA aplicada").

**Dónde va la capacitación.** El supuesto de capacidad de inversión pone la
capacitación dentro del 1%-3% de caja. Acá se cuenta como **tiempo**, porque son
horas propias sin gasto externo. Si el Directorio la quiere en la caja, suma
27-102 mil.

## Evidencia

### Inversión por trimestre (miles de USD, escenario recomendado)

Consolidado de los Insumos para Finanzas de los Anexos [B](02-arquitectura.md),
[C](03-gobierno-seguridad.md) y [D](04-personas-cultura.md) en su ronda 3, con
valores medios. Se separa la **caja**, que sale de la empresa, del **tiempo**
reasignado, que es costo de oportunidad.

| Concepto | T0 | T1 | T2 | T3 | T4 | Año (rango) | Dueño |
|---|---|---|---|---|---|---|---|
| Infraestructura (T1-b: solo telemetría en T1) | — | 1,0 | 8,2 | 12,0 | 12,0 | 17-50 | B |
| Consumo de modelos del piloto de producto | — | — | — | 7,5 | 7,5 | 6-24 | B |
| Red team del piloto | — | — | — | 10,0 | — | 5-15 | B |
| Asesoría legal externa | — | 7,0 | 7,0 | — | — | 8-20 | C |
| Pasarela de salida, DLP y logs | — | — | 3,8 | 3,8 | 3,8 | 4,5-18 | C |
| Red team externo y auditoría ISO 27001 ampliada | — | — | — | — | 21,3 | 11,6-31 | C |
| Contractor de IA aplicada (50% en T1, 100% en T2-T4) | — | 11,6 | 23,2 | 23,2 | 23,2 | 47-116 | D |
| Contingencia 15% | — | 2,9 | 6,3 | 8,5 | 10,2 | 15-41 | E |
| **Caja incremental** | — | **22,6** | **48,6** | **65,0** | **78,0** | **114-314** | |
| Esfuerzo técnico sin IA aplicada (0,6 / 2,5 / 3,0 / 2,4 FTE) | 0,3 | 11,2 | 42,4 | 50,2 | 40,2 | 84-204 | B |
| Gobierno, seguridad, Council, pruebas de bypass y ejercicios | — | 13,0 | 16,1 | 9,6 | 10,4 | 27-72 | C |
| Retrospectiva de T0, capacitación, champions y líder del programa | 4,0 | 17,6 | 33,7 | 17,5 | 13,0 | 39-133 | D |
| **Tiempo reasignado a costo cargado** | **4,2** | **41,8** | **92,2** | **77,3** | **63,6** | **150-408** | |
| FTE de personas clave | — | 1,6 | 3,5 | 3,7 | 3,1 | 3,0 promedio | |
| FTE en horas distribuidas de la dotación | — | 1,2 | 2,6 | 1,2 | 0,9 | 1,5 promedio | |
| **FTE equivalentes** | — | **2,8** | **6,1** | **4,9** | **4,0** | **4,5 promedio** | |

T0 (1,8-6,7 mil de tiempo) se ejecuta **antes de G0**: la reconstrucción
retrospectiva de D y el día de verificación del historial de B. Quién autoriza
gastar ese tiempo antes del presupuesto 2027 está **pendiente**. La suscripción
vigente no es incremental: ya está en el gasto de hoy y el plan no suma seats.

**Contra el techo de caja.** La caja con contingencia, 114-314 mil, entra en el
3% de la facturación si esta es de al menos USD 3,8-10,5 millones anuales, y en
el 1% si es de al menos 11,4-31,4 millones. Lo verifica en `private/` quien tiene
acceso, sin publicar el dato ni el resultado.

### Contra el sobre de tiempo: un T1 que entra (H02)

El sobre del [supuesto de capacidad](../../context/supuestos/capacidad-de-inversion.md)
es 10%-15% del tiempo de 10-15 personas clave: **1 a 2,25 FTE**. El supuesto no
dice nada de las horas repartidas en toda la dotación (básico, intermedio,
avanzado, champions). Hay dos lecturas, y el board elige:

- **Estricta:** todo cuenta contra 1-2,25 FTE.
- **Separada (propuesta de Finanzas, no está en la ficha):** las personas clave
  contra el sobre, y las horas distribuidas como un **segundo sobre que el board
  aprueba explícitamente en G0**. Es lo que la revisión llama "ampliar el sobre".

| Alternativa de T1 | Clave | Distribuidas | Total | Contra 2,25 FTE | Caja T1 | Tiempo T1 |
|---|---|---|---|---|---|---|
| Ronda 2 (T1-a, IA interna de 0,5) | 2,3 | 1,2 | 3,5 | 1,56× | 12 | 57 |
| T1-b con IA interna de 0,3 (Anexo B) | 1,9 | 1,2 | 3,1 | 1,38× | 9 (5-13) | 49 (26-71) |
| **T1-E: T1-b con contractor B1 (recomendada)** | **1,6** | **1,2** | **2,8** | **1,25×; clave 0,70×** | **23 (13-32)** | **42 (22-61)** |
| T1-E estricta: el intermedio de Tecnología pasa a T2 | 1,6 | 0,8 | 2,4 | 1,06× | 23 (13-32) | 37 (20-54) |
| T1 mínimo: básico e intermedio pasan a T2 | 1,6 | 0 | 1,6 | 0,70× | 23 (13-32) | 29 (16-41) |

Lectura:

- **Con la lectura separada, T1-E entra.** Usa 1,6 FTE clave dentro del sobre
  (alcanza con 11 personas al 15% o 16 al 10%). Las 590 horas distribuidas son
  ~9 h por persona de la dotación, y el board las aprueba como sobre propio.
- **Con la lectura estricta, ninguna versión que cumpla el básico ≥ 90% en T1
  entra.** T1-E estricta excede el sobre en 0,15 FTE. T1 mínimo entra, pero
  rompe la meta de básico del [Anexo D](04-personas-cultura.md).
- La vía de IA aplicada de T1 cambia caja por tiempo: el contractor B1 suma
  ~13 mil de caja y libera 0,3 FTE clave. Como el recurso que no entra es el
  tiempo, y la caja sí, Finanzas recomienda B1 (ver "Tensiones").

**El año sigue sin entrar, y eso se decide en G0, no en G1.** Con el frente
producto, las personas clave suman 3,5 / 3,7 / 3,1 FTE en T2-T4 (1,4-1,65× el
sobre). Si se difiere el producto hasta tener señal de cliente, bajan a
2,5 / 2,2 / 2,1: T3 y T4 entran, y T2 excede el sobre en 0,3 FTE, que replanea `architect`.

El board elige en G0 una de dos opciones y la deja escrita: **(a)** ampliar el
sobre clave de T2-T4 hasta ~3,7 FTE, sabiendo que sale de horas facturables, o
**(b)** diferir el producto y replanear T2. Las horas distribuidas de T2
(~1.260 h, 2,6 FTE) también necesitan su sobre aprobado.

### IA aplicada: alternativas costeadas (H11)

B y D coinciden en que el contractor **reemplaza** la fracción interna de T2-T4,
no la complementa. Difieren en T1: B propone 0,3 FTE de un rol interno que se
confirma antes de G0, y D propone el contractor al 50% desde T1. Año completo sin
T0, medios (rango):

| Alternativa | Caja | Tiempo | Económico | FTE clave en T1 |
|---|---|---|---|---|
| 1. Reemplaza desde T1 (contractor B1) — **base** | 214 (114-314) | 275 (148-402) | 489 | 1,6 |
| 2. Rol interno de 0,3 en T1, reemplaza desde T2 | 201 (107-295) | 282 (152-412) | 483 | 1,9 |
| 3. Complementa (T1-a, conservador de la ronda 2) | 203 (108-298) | 346 (189-502) | 549 | 2,3 |
| 4. Sin contractor (T1-a, todo interno) | 123 (61-185) | 346 (189-502) | 468 | 2,3 |

Sobre el económico total, la 4 es la más barata, pero usa 0,8 FTE clave más que
la 1 en cada trimestre de T2-T4, y ese es el recurso que no entra. La 2 cuesta casi
lo mismo que la 1 (483 contra 489) y solo es válida si el rol interno demuestra en G0 experiencia en
evals y harness ([Anexo B](02-arquitectura.md)). El 0,5 del contractor en T1 se
dimensionó para T1-a: con T1-b, el 0,2 que excede los 0,3 que pide B es traspaso
y documentación, según D.

### Beneficios por palanca

Regla: cada beneficio se cuenta una sola vez y se declara su tipo. **Ninguno es
caja dentro de los 12 meses.**

| Palanca | Tipo | 12 meses (base) | A régimen (anual) | Supuesto y fuente |
|---|---|---|---|---|
| Productividad interna en equipos propios | Capacidad liberada (horas evitadas), no caja | 60 mil (27-101) a costo cargado | 130 mil (59-219) con g = 15%; 48 con 5%; 200 con 25% | Lectura A del [Anexo B](02-arquitectura.md): a output fijo, g de throughput libera g/(1+g) de las horas ([ganancia](../../context/supuestos/ganancia-de-productividad.md), [N y costo](../../context/supuestos/desarrolladores-en-equipos-propios.md), [rampa](../../context/supuestos/rampa-de-la-ganancia.md)) |
| Margen en staffing | Margen | 0 | 0 en base | En contratos por hora, menos horas es menos facturación ([supuesto](../../context/supuestos/ganancia-de-productividad.md)). Solo hay margen con precio por resultado ([apunte](../../material/apuntes/2026-09-29-tokenomics-aiops.md)) |
| Ingresos nuevos por IA en el producto | Ingreso | 0 | Sin cifra | Hoy no hay IA en lo que se vende ni precio validado ([hecho](../../context/hechos/ia-en-producto-y-oferta.md)). Sin compromiso contractual antes de G4 ([Anexo B](02-arquitectura.md)) |
| Riesgo de concentración y licencia para operar | Riesgo evitado | Sin cifra | Sin cifra | El cliente principal pesa 40%-50% ([hecho](../../context/hechos/cartera-y-concentracion.md)) y los bancos deben gobernar la IA de sus terceros ([hecho](../../context/hechos/regulacion-clientes-financieros.md)) |
| Cobertura del cambio de precio de los tokens | Exposición evitada | Sin cifra | ~19-24 mil por cada 1× de múltiplo evitado | 4,8-6,1 mil por trimestre × 4. El 60%-80% de ahorro del curso no tiene fuente ([huecos](../../material/huecos.md)) |

**Throughput (H09).** Se usa la unidad del [Anexo B](02-arquitectura.md): pull
request aceptado (mergeado, con las compuertas de calidad aprobadas y sin
reversión a 14 días) por persona activa y por trimestre, estratificado por tipo
y tamaño de cambio. La cohorte son los equipos propios, y la ganancia se mide
contra la base congelada, con incidentes y retrabajo al lado.

Las dos conversiones responden preguntas distintas:

- **Lectura A, horas evitadas, la del base:** valúa capacidad.
- **Lectura B, output adicional:** vale g en vez de g/(1+g). Da 69 mil a 12 meses
  en el base, y solo vale si hay demanda con precio. Va como sensibilidad.

**Puente a caja.** La capacidad liberada se vuelve caja solo por dos vías.
Ninguna existe hoy, así que el beneficio de caja a 12 meses es **0** en los tres
escenarios:

- **Venta:** horas vendidas × tarifa de venta. La tarifa no se publica y se
  calcula en `private/`.
- **Contratación evitada:** solo cuenta contra un plan de contratación aprobado,
  y `context/` no registra ninguno (la restricción es no contratar).

G2 pide decidir el destino de la capacidad, y desde ahí el puente se mide.

**Cómo se lee la palanca de riesgo sin inventar probabilidades.** El gasto en
controles se paga si baja la probabilidad de perder el ingreso que protege en al
menos Δp = costo de los controles / (peso del ingreso protegido × margen). Como
margen se usa el EBITDA de 21%-30% ([hecho](../../context/hechos/situacion-economica.md)),
que subestima lo perdido y por eso exige un Δp más alto. Si los controles
costaran 1% de la facturación y protegen al cliente principal (40%-50%), alcanza
con bajar entre 7 y 12 puntos la probabilidad de perderlo. El equipo no tiene
esa probabilidad: la juzga el board.

### Tokenomics: de suscripción plana a consumo

El agente de código consume unas 12 veces lo que se paga
([hecho](../../context/hechos/costos-tecnologia-e-ia.md)), y el plan supone que la
suscripción plana no es estable ([supuesto](../../context/supuestos/precio-y-dependencia-de-modelos.md)).
Costo incremental en miles de USD por trimestre si el proveedor cobra por consumo:

| Múltiplo pagado | 2× | 4× | 6× | 12× |
|---|---|---|---|---|
| Incremental por trimestre | 4,8-6,1 | 14,4-18,2 | 24,0-30,4 | 52,8-66,8 |

A 12×, el incremental anual (211-267 mil) es del orden de **toda la caja del
plan**. Es una **exposición de la empresa con o sin plan**: el plan no suma
seats, y el gateway acota el rango. Por eso no se carga como costo del plan,
salvo en el estrés sin frenar. El Anexo B pone 58-73 mil por trimestre (12×);
acá se usa el incremental (11×), porque una vez la suscripción ya se paga.

Las palancas de M2U4 (prompts concisos, modelo adecuado, caché) bajan el múltiplo
([tokenomics](../../material/conceptos/m2u4-tokenomics.md)), pero el curso no da
un porcentaje con fuente. El gateway se justifica por el rango de costo que
acota, no por un ahorro prometido.

### ROI, payback y equilibrio

Modelo del equipo con valores medios y el escenario de costos recomendado. T0
entra en el año. La capacidad se valúa con la lectura A a costo cargado: es el
piso.

| Escenario | Caja | Tiempo | Capacidad liberada | ROI económico 12 m | Beneficio de caja 12 m |
|---|---|---|---|---|---|
| Pesimista, estrés sin frenar | 214 | 279 | 12 (5-20) | −98% | 0 |
| Base | 214 | 279 | 60 (27-101) | −88% | 0 |
| Optimista | 214 | 279 | 110 (50-185) | −78% | 0 |

En la base, el neto económico acumulado es −69 en T1, −201 en T2, −324 en T3 y
−433 en T4. El "ROI sobre la caja" de rondas anteriores se retira: usaba como
beneficio capacidad que no es caja.

**Año 2, fuera del alcance e ilustrativo** ([supuesto](../../context/supuestos/costo-de-regimen-del-ano-2.md)):
régimen de 93 mil de caja más 95 mil de mantenimiento, 188 mil por año.

- **Equilibrio.** Con la lectura A, el régimen pide liberar el 18,8% de las horas
  de la cohorte. Eso exige un throughput de **~23%** (g = x/(1−x)), entre 13% y
  71% según N y el costo. **Está por encima de la meta de +20% del borrador de
  OKR**: cumplir la meta no alcanza para cubrir el régimen (escalado a `caio`).
  Si la capacidad se vende, el equilibrio baja en proporción a cuánto supera la
  tarifa al costo, y eso se calcula en `private/`.
- **Inversión del año 1:** ningún escenario la recupera en 24 meses con
  productividad sola. El acumulado a 24 meses es −372 en el optimista, −491 en
  la base y −621 en el pesimista.
- **Payback:** no hay dentro del horizonte con productividad sola. Llega antes
  solo con ingreso de producto, con capacidad vendida o si el board le asigna
  valor a la palanca de riesgo.

### Cuánto pierdo si corto (H10)

Cada fila suma, en medios y en máximos, lo ejecutado hasta el gate más T0, más el
costo de cierre. Aparte se muestra la **base mínima** que queda el resto del año
si se conservan los controles. El cierre lo definen supuestos nuevos del equipo:

- el contractor tiene un mes de preaviso a su dedicación vigente;
- la infraestructura de laboratorio tarda un mes en darse de baja;
- legal y red team se contratan por etapa y no comprometen más allá del gate.

La base mínima es el núcleo de gobierno (25% del líder, 20% de seguridad y el
Council) más la pasarela, si ya está instalada.

| Corte en | Caja ejecutada + cierre | Tiempo ejecutado + T0 | Perdido: medio / máximo | Base mínima del resto del año (caja / tiempo) | Año con el corte: medio / máximo |
|---|---|---|---|---|---|
| G1 | 27 (15-38) | 46 (24-68) | **73 / 106** | 0 / 29 (17-40) | 102 / 146 |
| G2 | 82 (46-117) | 138 (71-206) | **220 / 323** | 8 (3-12) / 19 (11-27) | 247 / 362 |
| G3 | 148 (80-216) | 216 (114-317) | **363 / 533** | 4 (2-6) / 10 (6-13) | 377 / 553 |
| Sin corte | 214 (114-314) | 279 (150-408) | 493 / 722 | — | 493 / 722 |

**Pesimista ejecutado contra estrés sin frenar.** Si el throughput no llega al
umbral de G2 y se corta ahí, el año cuesta ~247 mil (hasta 362) y libera casi
nada (~1 mil): neto ≈ −245. El estrés sin frenar, con todo el año ejecutado y
la rampa pesimista, da −481. Si además el precio pasa a 12× desde T3, la
exposición de la empresa lleva el total a −601. La diferencia entre las dos
cifras, ~236 mil, es lo que compran los gates.

### Costo por outcome

La métrica de M1U4 es el **costo por outcome aceptado**
([ficha](../../material/conceptos/m1u4-costo-por-outcome.md)). Para el frente
interno se propone el **costo por PR aceptado**, con la unidad del Anexo B: las
licencias, el consumo, la parte de plataforma y las horas de revisión humana,
divididas por los PR aceptados de la cohorte.

**No tiene valor hoy:** se mide contra la base congelada en T1. El gate le pide
que no suba de un trimestre a otro mientras sube el throughput. En el producto,
el outcome lo fija la ficha de experimento que elija el portfolio.

### Sensibilidad

Neto económico a 12 meses, en la base (−433 mil), moviendo un supuesto por vez:

| Supuesto | Valor | Neto 12 m |
|---|---|---|
| Throughput | 10% / 25% | −451 / −401 |
| Desarrolladores en equipos propios | 15 / 20 | −442 / −425 |
| Costo por desarrollador | 2.500 / 7.000 | −462 / −405 |
| Tiempo reasignado | −30% | −349 |
| Conversión del throughput | Lectura B en vez de A | −424 |
| Exposición por consumo desde T3 (de la empresa, no del plan) | 4× / 12× | −466 / −553 |

**Los tres supuestos que más mueven el resultado** son el tiempo reasignado, el
esquema de precio de los tokens y, a régimen, el throughput, que a 12 meses pesa
poco por la rampa. Los escenarios los combinan:

| Escenario | Throughput a T4 y rampa | Precio de tokens | Producto |
|---|---|---|---|
| Pesimista | 5%, rampa 0/10/30/60: por debajo del piso del supuesto, es el caso del kill | Consumo a 12× desde T3, sin mitigar (solo en el estrés sin frenar) | Sin señal de cliente |
| Base | 15%, rampa 0/25/60/100 | Plano | Piloto evaluado, sin contrato |
| Optimista | 25%, rampa 0/40/80/100 | Plano | Un cliente con interés contractual en G4 (sin ingreso en los 12 meses) |

Hay un estrés aparte, no modelado: la pérdida parcial del cliente principal
([supuesto](../../context/supuestos/continuidad-de-clientes-principales.md)). Con
20% menos de facturación, el peso de la caja del plan sobre la facturación sube
25%, y los gates de T2-T4 se congelan hasta revisar el techo.

**Tipo de cambio.** Licencias, tokens y servicios externos se pagan en USD. El
tiempo está costeado en USD de mercado sobre personal en Argentina. Una
apreciación real del peso de más de 20% invalida el
[supuesto de costo](../../context/supuestos/costo-cargado-por-rol.md) y encarece
el tiempo en USD sin cambiar la caja.

### Modelo recalculable (H17)

El modelo no se versiona como script. Con las fichas de la tabla de supuestos y
estas fórmulas, un tercero reproduce todas las tablas del anexo. Los valores
reales (facturación, tarifa, nómina) se cargan solo en `private/`.

| Magnitud | Fórmula |
|---|---|
| Costo de tiempo de una actividad | horas × costo mensual del rol / 160, o fracción del rol × costo mensual × meses |
| FTE de un trimestre | horas / 480, o la fracción de rol declarada en el anexo dueño |
| Valor medio de un renglón | (mínimo + máximo) / 2; los totales suman mínimos con mínimos y máximos con máximos |
| Caja con contingencia | Σ renglones de caja × 1,15 |
| Capacidad liberada en el trimestre t (lectura A) | N × costo × 3 × g / (1 + g) × rampa_t |
| Lectura B (sensibilidad) | N × costo × 3 × g × rampa_t |
| ROI económico a 12 meses | (capacidad − caja − tiempo) / (caja + tiempo) |
| Beneficio de caja | horas vendidas × tarifa (`private/`) + contrataciones evitadas de un plan aprobado; hoy 0 |
| Régimen anual de la capacidad | N × costo × 12 × g / (1 + g) |
| Throughput de equilibrio | x = costo del año 2 / (N × costo × 12); g* = x / (1 − x) |
| Incremental por consumo | (k − 1) × suscripción del agente de código por trimestre |
| Umbral de facturación para un techo p | caja con contingencia / p |
| Pérdida al cortar en Gk | caja y tiempo de T1..Tk + T0 + cierre (un mes de contractor y de laboratorio) |
| Base mínima del resto del año | (núcleo de gobierno + pasarela, si está instalada) × trimestres restantes |

**Contingencia y renglones sin estimar.** Los renglones sin cotización
(certificación del nivel avanzado, certificaciones del programa de partners)
quedan **excluidos del techo**: entran solo con una cotización antes de su gate y
dentro del techo de caja aprobado, desplazando otro renglón si hace falta.

La instrumentación de uso ya no está entre ellos: B la costea como tiempo dentro
de DevOps/QA. La contingencia anual (15-41 mil) no cubre el error de precio del
contractor, cuyo rango tiene 58 mil de ancho, ni el de la infraestructura, con
32. Por eso los techos de los gates se fijan sobre **máximos** con contingencia,
no sobre medios. La regla es no gastar fuera del techo, sin excepciones.

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: sale de horas facturables o de entregas a clientes | Alta | Alto | Sobre por rol y trimestre aprobado en G0; suplentes ([Anexo D](04-personas-cultura.md)) | Utilización bajo la meta de 80% dos meses seguidos por causa del plan: se recorta el frente que más tiempo consume |
| Cambio a pago por consumo | Alta ([Anexo B](02-arquitectura.md)) | Alto | Gateway con ruteo, caché y topes; FinOps mensual desde T2 | Múltiplo efectivo de más de 6× sin mitigar en un trimestre: se congela la expansión y se topea el consumo |
| La ganancia no aparece o se paga con retrabajo | Media | Alto | Base congelada; costo por PR aceptado; incidentes y retrabajo junto al throughput | Bandas de G2 y G3 (abajo) |
| La capacidad liberada no se vuelve caja | Alta | Medio | Destino decidido en G2 (producto propio, producto del Cliente A o venta) | Sin destino en G2: la capacidad no se cuenta como beneficio |
| El piloto de producto no tiene comprador | Media | Medio | El frente producto se libera solo con señal de cliente y matriz habilitante | Sin señal en G2: se difiere (13-45 de caja y 32-79 de tiempo menos) |
| El cierre cuesta más que lo previsto | Baja | Medio | Contratos por etapa, preaviso de un mes, nada a más de 12 meses antes de G4 | — |
| Doble conteo de costos entre anexos | Media | Bajo | Tabla de solapes | — |
| El gasto de tecnología sube contra el OKR de menos de 3,5% | Alta | Medio | Reformular el resultado clave (ver tensiones) | — |

## Decisiones

### Recomendación de Finanzas

**Un único pedido G0 por T1-E, con techo máximo, y el resto por gates.** El board
aprueba T1-E y el marco de gates. Cada trimestre siguiente se libera solo si
cumple su condición.

Cortar en G1 cuesta ~73 mil económicos en el medio y **hasta 106 en el máximo**:
27 de caja (hasta 38) y 46 de tiempo (hasta 68). El año completo puede llegar a
314 de caja y 408 de tiempo. Esa diferencia es la reversibilidad que compra el
diseño.

Alternativas descartadas:

- **A. Aprobar el año completo:** compromete toda la caja con un business case
  que no cierra con productividad sola. Descartada.
- **B. Solo el frente interno:** es más barato, pero no tapa el riesgo de precio
  de los tokens, no abre ingresos y deja sin controles la relación con los bancos.
  Queda como repliegue si fallan los gates de producto.
- **C. Recomendada: G0 por T1-E y gates**, con el frente producto condicionado a
  una señal de cliente.

### Pedido G0 y gates económicos (para que `caio` los integre)

**Pedido G0, único.** Incluye cinco cosas:

1. **Caja de T1:** hasta 32 mil (contractor B1 hasta 16,5; legal hasta 10;
   telemetría hasta 1,5; contingencia).
2. **Tiempo de T1:** hasta 61 mil, que son 1,6 FTE de personas clave y 590 h
   distribuidas.
3. **T0:** ratificar el tiempo ya ejecutado, hasta 7 mil.
4. **IA aplicada de T1:** contractor B1, o el rol interno si demuestra capacidad.
5. **T2-T4:** la elección entre ampliar el sobre clave o diferir el producto,
   con el sobre de horas distribuidas y la lectura del sobre (estricta o separada).

El techo de caja se confirma contra el presupuesto 2027 en `private/`.

| Gate | Cuándo | Libera (caja / tiempo, techo máximo) | Condición económica | Si no se cumple | Reversible |
|---|---|---|---|---|---|
| G0 | Aprobación | T1: 32 / 61 | Pedido G0 completo | No arranca T1; T0 queda hundido (≤ 7) | Sí |
| G1 | Fin de T1 | T2: 70 / 138 | Base congelada con la unidad del Anexo B; matriz de los clientes que concentran la facturación; el uso de T1 dentro del sobre aprobado | Corte: base mínima, ~29 de tiempo el resto del año | Sí |
| G2 | Fin de T2 | T3: 97 / 111 | **Pasa:** throughput ≥ +3% como tendencia con intervalo, sin más retrabajo. **Espera:** entre 0% y +3% o con un intervalo que cruza +3%; se libera T3 sin escalado y se vuelve a medir a las 6 semanas. **Corta:** sin mejora o con más retrabajo. Además, FinOps con el múltiplo medido y el destino de la capacidad decidido. Producto solo con señal de cliente | Corte: perdido 220 (máximo 323) | Sí |
| G3 | Fin de T3 | T4: 115 / 91 | **Pasa:** throughput ≥ +8%. **Espera:** +5% a +8%; se liberan solo la base mínima y el mantenimiento, y se vuelve a medir a las 6 semanas. **Corta:** menos de +5%. SLO del piloto solo si el producto no se difirió; costo por PR sin subir | Corte: perdido 363 (máximo 533) | Sí |
| G4 | Fin de T4 | Año 2 | Trayectoria hacia ~23% de throughput (menos si la capacidad se vende) **o** interés contractual en el producto; decisiones sobre contractor, on-premise e ISO 42001 | No se renueva el régimen | Contrato a más de 12 meses o hardware: irreversible |

Las bandas "espera" son la parte económica; la tabla completa de pasa, espera y
corta por condición es de `caio` ([Anexo F](06-roadmap-riesgo.md)).
Irreversibles marcados (de los Anexos [B](02-arquitectura.md) y
[C](03-gobierno-seguridad.md)): compromisos de volumen a más de 12 meses, capex
en infraestructura propia y firma con un cliente. Ninguno se toma antes de G4.

### Solapes entre anexos

Regla: **el base cuenta los dos renglones** salvo donde los dos dueños ya
acordaron la consolidación. La consolidación es un ahorro que confirma el dueño.

| Solape | Renglones | Ahorro posible | Estado |
|---|---|---|---|
| IA aplicada | 0,5 / 0,8 FTE de B y contractor de D | 32-79 de tiempo en T2-T4 y 4-10 en T1 | **Consolidado**: B y D acuerdan que el contractor reemplaza; el base ya lo descuenta |
| Pruebas de bypass y migración | DevOps/QA de B (2,1-10,7, dentro de su fracción) y prueba de integración de C (1,1-5,6) | Hasta 1,1-5,6 | Nuevo; lo resuelven `architect` y `governance` |
| Red team | Piloto en T3 (B, 5-15) y externo en T4 (C, 10-25) | 5-15 si un contrato cubre el piloto y la reprueba | Desacuerdo a la vista en la [ficha](../../context/supuestos/precios-externos-sin-cotizar.md); `architect` y `governance` |
| Gateway y pasarela de salida | Infraestructura (B, 17-50) y pasarela, DLP y logs (C, 4,5-18) | Hasta 4,5-18 si son la misma pieza | `architect` |
| Seguridad | 20% de un senior de DevOps o seguridad (C) y DevOps/QA (B) | Sin cuantificar | `architect` y `governance` |

## Tensiones con otras miradas

| Tensión | Planteada por | Posición de Finanzas | Estado |
|---|---|---|---|
| Vía de IA aplicada en T1: rol interno de 0,3 FTE (B) o contractor al 50% (D) | `architect`, `people` | Las dos están costeadas. Finanzas recomienda el contractor porque el recurso que no entra es el tiempo clave (1,6 contra 1,9 FTE), con ~13 mil más de caja. Si G0 demuestra un rol interno con experiencia, la alternativa 2 cuesta lo mismo | **Desacuerdo a la vista**; decide el Directorio en G0 |
| Qué base se congela en T1: retrospectiva al cierre del mes 1 (B) o prospectiva en las semanas 1 a 4 (D) | `architect`, `people` | Las dos están costeadas (T0 y T1). La rampa de 0% en T1 es compatible con ambas, y la ganancia se atribuye solo contra la base congelada | **Escalada a `caio`** para el calendario único |
| El throughput de equilibrio (~23%) supera la meta de +20% del OKR | `finance` (H09) | Con la lectura A, cumplir la meta no cubre el régimen del año 2. O sube la meta, o se vende capacidad, o el caso descansa en producto y riesgo | **Escalada a `caio`** |
| +20% de throughput con agentes a 12× lo pagado, contra el OKR de gasto de tecnología de menos de 3,5% | `architect` | A régimen, la base libera ~130 mil por año, que cubren consumo incremental hasta ~7× la suscripción. La caja del plan suma gasto de tecnología: el OKR es incompatible salvo que baje la nube. Propuesta: medirlo sin la inversión del plan, o por persona activa | **Escalada a `caio`** para reformular el resultado clave |
| Sobre de capacidad: lectura estricta o separada | `finance` (H02) | La separada es propuesta de Finanzas y no está en la ficha; con la estricta, T1 no entra sin recortar el básico | **Decide el board en G0** |
| El tiempo de gobierno compite con horas facturables | `governance` | Dos lentes: caja (lo que aprueba el CFO) y económica (caja más tiempo a costo cargado) | **Resuelta** |
| Staffing facturado por hora desincentiva el uso de IA | `people` | Productividad en staffing = 0 en el base. Las horas de capacitación de Operaciones (~400 h) cuestan 4-14 mil a costo; a tarifa de venta valen más, y eso se calcula en `private/` | **Resuelta** para el costo; el modelo comercial queda **escalado a `caio`** |
| Contractor contra la restricción de no contratar | `people` | 47-116 mil de caja, reversible por ser un contrato corto | **Explicitada**: decide el Directorio |
| Matriz de clientes y política sin ratificar | `governance`, `people` | Sin matriz no se libera el producto; la meta de Operaciones no tiene beneficio asignado | **Explicitada** como condición de gate |

## Insumos para el deck

- **Frase para el CFO:** el plan cuesta 114-314 mil USD de caja y ~4,5 FTE de
  tiempo en el año, y no genera caja propia en 12 meses. Compra un tope al riesgo
  de precio de los tokens, la licencia para seguir vendiéndoles a bancos y la
  opción de un ingreso de producto. Cortarlo en G1 cuesta ~27 mil de caja, hasta
  38 en el máximo.
- **Decisión que se le pide al board:** un único pedido G0 por T1-E (hasta 32 de
  caja y 1,6 FTE clave más 590 h distribuidas), con el sobre de T2-T4 elegido en
  G0: ampliarlo o diferir el producto.
- **Cifra de alerta:** a 12×, el consumo incremental (211-267 mil al año) iguala
  a toda la caja del plan. Es exposición de la empresa, con o sin plan.
- **Equilibrio:** ~23% de throughput a régimen, **por encima** de la meta de +20%
  del OKR. Cumplir la meta no alcanza.
- **Para la Slide 9:** el kill ejecutado en G2 (≈ −245) contra el estrés sin
  frenar (−481, o −601 con 12×), y los irreversibles diferidos hasta G4.

## Cautelas

- Todo es borrador sin verificación humana: las cifras son rangos o medios de
  supuestos del equipo sin cotización, y las fichas de `context/` están en
  `draft`. Nada es apto para entrega.
- N × costo por desarrollador es una cuenta de mercado, no la nómina de la empresa.
- La valuación de la capacidad a costo cargado y con la lectura A es un piso
  deliberado. La tarifa no se publica ni se deriva de márgenes internos.
- Son supuestos nuevos, sin ficha todavía: la separación del sobre en clave y
  distribuido, las fracciones por rol de T1-E, los costos de cierre (un mes de
  preaviso y de laboratorio), la base mínima tras un corte y las bandas de espera
  de G2 y G3.
- El Δp de la palanca de riesgo usa el margen EBITDA como proxy conservador.
- No se usaron las cifras del curso sin fuente primaria (60%-80% de ahorro de
  inferencia, ROI de 2,8×-4,1×, 360 → 7 USD) ([huecos](../../material/huecos.md)).
- Responsable humano de cada gate y de cada cifra: **pendiente**.
