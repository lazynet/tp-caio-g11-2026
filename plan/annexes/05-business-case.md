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

El presupuesto base es el de la opción que propone el CAIO para T2-T4: **el
frente producto se difiere** hasta que G2 traiga señal de cliente. El producto
queda como un tramo condicional, con costo propio, que se libera en G2 o no se
libera. En T2, el base usa el **replan de B** (arquitecto 0,4 y DevOps/QA 0,8)
para que T2 entre en el sobre; la excepción acotada queda costeada como
alternativa.

Responsable humano de cada cifra y de cada gate: **pendiente**. Ninguna cifra es
apta para entrega: todo es borrador sin verificación humana, las fichas de
`context/` están en `draft` y los costos son supuestos del equipo sin cotización.

## Supuestos de partida

**Convención de tiempo y de cálculo.** T0 es el cuarto trimestre de 2026 y T1-T4
son los trimestres de 2027; el Q1-Q4 de los Anexos B y C se lee como T1-T4. Una
persona-trimestre son **480 horas de costeo** (160 por mes): con ellas se pasa de
horas a FTE. Las 520 horas de 13 semanas × 40 h son calendario bruto, sin
descontar feriados ni licencias, y no se usan para FTE ni para costo
([convenciones](../../context/supuestos/convenciones-de-calculo.md)).

**Redondeo.** Los medios, los rangos y las pérdidas estimadas se redondean al
entero más cercano. Los **techos y las reservas que se autorizan** se redondean
al entero superior del máximo calculado, para que la autorización nunca quede
por debajo del cálculo ([convenciones](../../context/supuestos/convenciones-de-calculo.md)).

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
| Rampa de la ganancia (T1/T2/T3/T4) | Fracción del objetivo de throughput que se alcanza: base 0/25/60/100%; pesimista 0/10/30/60%; optimista 0/40/80/100% | [Supuesto](../../context/supuestos/rampa-de-la-ganancia.md) |
| Línea de base de atribución | Base prospectiva congelada en las semanas 1-4 de T1; la serie retrospectiva de T0 estima ruido. El OKR se informa al lado contra T0 | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo F](06-roadmap-riesgo.md) |
| Poblaciones de capacitación | Básico ~65 × 6 h; intermedio ~50 × 12 h; avanzado ~10; 8 champions al 10% | [Supuesto](../../context/supuestos/poblaciones-de-capacitacion.md) |
| Precios externos y contingencia | Rangos sin cotización; 15% de contingencia sobre la caja | [Supuesto](../../context/supuestos/precios-externos-sin-cotizar.md) |
| Capacidades que hoy no existen | Gateway, inventario de arquitectura, legal dedicado a IA | [Supuesto](../../context/supuestos/capacidades-ausentes.md) |
| Suscripción del agente de código | 40-45 seats × USD 40-45 por mes = 4,8-6,1 mil por trimestre | Cálculo sobre [uso de IA](../../context/hechos/uso-ia-interno.md) y [costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real / lo pagado | ~12× en el agente de código | [Hecho](../../context/hechos/costos-tecnologia-e-ia.md) (telemetría, no factura) |
| Régimen del año 2 | Caja de ~48 mil de base común (~93 si el producto sigue) más 1,5 FTE senior (~95 mil) | [Supuesto](../../context/supuestos/costo-de-regimen-del-ano-2.md) |
| Cierre y base mínima tras un corte | Un mes de preaviso del contractor y de laboratorio, cubierto por una reserva que se actualiza en cada gate; queda el núcleo de gobierno y la pasarela instalada; si P sigue, también la base común que P usa | [Cierre](../../context/supuestos/costos-de-cierre-por-corte.md), [base mínima](../../context/supuestos/base-minima-tras-un-corte.md) |
| Sobre de capacidad separado | Tiempo clave contra 1-2,25 FTE; horas distribuidas como segundo sobre | [Propuesta de Finanzas](../../context/supuestos/sobre-de-capacidad-separado.md) |
| Seats nuevos | Ninguno: la meta de adopción es de activación | [Anexo B](02-arquitectura.md) |

**Escenario de costos que consume este anexo.** T1 acotado (T1-b del
[Anexo B](02-arquitectura.md)), el contractor de IA aplicada que **reemplaza** la
fracción interna de B desde T1 (alternativa B1 del [Anexo D](04-personas-cultura.md)),
el replan de T2 de B y el frente producto diferido. La excepción acotada de T2 y
la alternativa con producto desde T2 quedan costeadas como comparación.

**Qué es producto en el costo.** Se cargan al frente producto el consumo de
modelos, el red team del piloto, el incremento de infraestructura del piloto y
los desarrolladores senior (1,5 / 1,0 FTE en T3-T4). El
[Anexo B](02-arquitectura.md) lo confirma y etiqueta sus renglones por frente.

**Dónde va la capacitación.** El supuesto de capacidad de inversión pone la
capacitación dentro del 1%-3% de caja. Acá se cuenta como **tiempo**, porque son
horas propias sin gasto externo. Si el Directorio la quiere en la caja, suma
27-102 mil.

## Evidencia

### Inversión por trimestre (miles de USD, escenario recomendado: producto diferido y replan de T2)

Consolidado de los Insumos para Finanzas de los Anexos [B](02-arquitectura.md),
[C](03-gobierno-seguridad.md) y [D](04-personas-cultura.md), con valores medios.
Se separa la **caja**, que sale de la empresa, del **tiempo** reasignado, que es
costo de oportunidad. La columna "Fr." dice a qué frente pertenece cada renglón:
**B** base común, **I** frente interno.

| Concepto | Fr. | T0 | T1 | T2 | T3 | T4 | Año (rango) | Dueño |
|---|---|---|---|---|---|---|---|---|
| Infraestructura (T1-b: solo telemetría en T1; T3-T4 sin piloto, al nivel de T2) | B | — | 1,0 | 8,3 | 8,3 | 8,3 | 14-38 | B |
| Asesoría legal externa | B | — | 7,0 | 7,0 | — | — | 8-20 | C |
| Pasarela de salida, DLP y logs | B | — | — | 3,8 | 3,8 | 3,8 | 4,5-18 | C |
| Red team externo y auditoría ISO 27001 ampliada (capa D del Anexo C: cota superior, ver nota) | B | — | — | — | — | 21,3 | 11,6-31 | C |
| Contractor de IA aplicada (50% en T1, 100% en T2-T4) | B | — | 11,6 | 23,2 | 23,2 | 23,2 | 47-116 | D |
| Contingencia 15% | | — | 2,9 | 6,3 | 5,3 | 8,5 | 13-33 | E |
| **Caja incremental** | | — | **22,6** | **48,6** | **40,5** | **65,0** | **98-255** | |
| Esfuerzo técnico de la base (0,6 / 1,2 / 1,5 / 1,4 FTE) | B | 0,3 | 11,2 | 21,3 | 26,6 | 24,5 | 50-118 | B |
| Gobierno, seguridad, Council, pruebas de bypass y ejercicios | B | — | 13,0 | 16,1 | 9,6 | 10,4 | 27-72 | C |
| Retrospectiva de T0, capacitación, champions y líder del programa | I | 4,0 | 17,6 | 32,5 | 17,5 | 13,0 | 39-130 | D |
| **Tiempo reasignado a costo cargado** | | **4,2** | **41,8** | **69,8** | **53,7** | **47,9** | **115-320** | |
| FTE de personas clave | | — | 1,6 | 2,2 | 2,2 | 2,1 | 2,0 promedio | |
| Horas distribuidas de la dotación (FTE) | | — | 590 h (1,2) | ~1.210 h (2,5) | ~580 h (1,2) | ~410 h (0,8) | 1,5 promedio | |
| **FTE equivalentes** | | — | **2,8** | **4,7** | **3,4** | **3,0** | **3,5 promedio** | |

Año: caja 177 (98-255) y tiempo 217 (115-320); económico **394** (213-575). Los
totales de FTE suman antes de redondear. Tres decisiones de los dueños definen
este cuadro: la infraestructura de T3-T4 sin piloto queda al nivel de T2 y su
incremento va a P (B); T2 usa el replan de B (−0,3 FTE clave, −5 mil de tiempo);
y el avanzado de D se costea con 480 h.

**Excepción acotada en lugar del replan.** Si el board elige la excepción, T2
queda en 2,5 FTE clave y 75,2 de tiempo, y el año en tiempo 223 (118-328) y
económico 399 (216-583). La caja no cambia.

**Capa D del Anexo C.** El red team externo y la auditoría ampliada son la capa
de demostración externa, que el [Anexo C](03-gobierno-seguridad.md) (D9b)
propone condicionar a la evidencia contractual que se junta en T1 y se decide
en G3. Como esa evidencia no depende de la señal de producto de G2, el base la
cuenta como cota superior. Si se saca a un tramo condicional, como P, la caja
base baja a 152 (85-220) y el techo de caja de T4 a 59; el tramo suma 25
(13-36). `caio` la deja en la base como cota superior, con la liberación
condicionada en G3 a la señal contractual ([Anexo F](06-roadmap-riesgo.md)).

**Tramo condicional del frente producto (P).** Solo si G2 trae la señal de
cliente. Si no la trae, no se gasta.

| Concepto de P | T3 | T4 | Tramo (rango) | Dueño |
|---|---|---|---|---|
| Consumo de modelos del piloto | 7,5 | 7,5 | 6-24 | B |
| Red team del piloto | 10,0 | — | 5-15 | B |
| Incremento de infraestructura del piloto | 3,8 | 3,8 | 3-12 | B |
| Contingencia 15% | 3,2 | 1,7 | 2-8 | E |
| **Caja de P** | **24,4** | **12,9** | **37 (16-59)** | |
| Desarrolladores senior del piloto (1,5 / 1,0 FTE) | 23,6 | 15,8 | 39 (23-56) | B |
| FTE clave con P | 3,7 | 3,1 | | |

Con P, el año suma caja 214 (114-314) y tiempo 257 (137-376). Comparación: con
el producto desde T2 (sin replan, porque el diseño del piloto queda en T2) da
caja 214 (114-314) y tiempo 278 (150-406). Diferir ahorra el desarrollador de
T2 (~16 mil de tiempo), habilita el replan (~5 más) y deja la decisión de gastar
en P para G2. El diseño del piloto, que el replan saca de T2, B lo absorbe en las
semanas 1-4 de T3 sin sumar fracción.

T0 (1,8-6,7 mil de tiempo) es un **costo previo propuesto**: la reconstrucción
retrospectiva de D y el día de verificación del historial de B, antes de G0. No
hay registro de que se haya ejecutado. Quién autoriza gastarlo antes del
presupuesto 2027 está **pendiente**. La suscripción vigente no es incremental:
ya está en el gasto de hoy y el plan no suma seats.

**Contra el techo de caja.** La caja con contingencia, 98-255 mil (114-314 con
P), entra en el 3% de la facturación si esta es de al menos USD 3,3-8,5 millones
anuales (3,8-10,5 con P), y en el 1% si es de al menos 9,8-25,5 millones
(11,4-31,4 con P). Lo verifica en `private/` quien tiene acceso, sin publicar el
dato ni el resultado.

### Contra el sobre de tiempo: T1 entra; T2 entra con el replan

El sobre del [supuesto de capacidad](../../context/supuestos/capacidad-de-inversion.md)
es 10%-15% del tiempo de 10-15 personas clave: **1 a 2,25 FTE**. El supuesto no
dice nada de las horas repartidas en toda la dotación (básico, intermedio,
avanzado, champions). Hay dos lecturas, y el board elige:

- **Estricta:** todo cuenta contra 1-2,25 FTE.
- **Separada (propuesta de Finanzas, [ficha](../../context/supuestos/sobre-de-capacidad-separado.md)):**
  las personas clave contra el sobre, y las horas distribuidas como un
  **segundo sobre que el board aprueba explícitamente en G0**.

| Alternativa de T1 | Clave | Distribuidas | Total | Contra 2,25 FTE | Caja T1 | Tiempo T1 |
|---|---|---|---|---|---|---|
| T1-a, IA interna de 0,5 | 2,3 | 1,2 | 3,5 | 1,56× | 12 | 57 |
| T1-b con IA interna de 0,3 (Anexo B) | 1,9 | 1,2 | 3,1 | 1,38× | 9 (5-13) | 49 (26-71) |
| **T1-E: T1-b con contractor B1 (recomendada)** | **1,6** | **1,2** | **2,8** | **1,25×; clave 0,70×** | **23 (13-32)** | **42 (22-61)** |
| T1-E estricta: el intermedio de Tecnología pasa a T2 | 1,6 | 0,8 | 2,4 | 1,06× | 23 (13-32) | 37 (20-54) |
| T1 mínimo: básico e intermedio pasan a T2 | 1,6 | 0 | 1,6 | 0,70× | 23 (13-32) | 29 (16-41) |

Lectura:

- **Con la lectura separada, T1-E entra si el sobre real llega a 1,6 FTE clave.**
  Eso pide al menos 11 personas al 15% o 16 al 10%. **Si el sobre disponible es el
  extremo inferior (1,0 FTE), ninguna versión de T1 entra.** El board confirma en
  G0 que dispone de ese piso. Las 590 horas distribuidas son ~9 h por persona de
  la dotación, y el board las aprueba como sobre propio.
- **Con la lectura estricta, ninguna versión que cumpla el básico ≥ 90% en T1
  entra.** T1-E estricta excede el sobre en 0,15 FTE. T1 mínimo entra, pero
  rompe la meta de básico del [Anexo D](04-personas-cultura.md).
- La vía de IA aplicada de T1 cambia caja por tiempo: el contractor B1 suma
  ~13 mil de caja y libera 0,3 FTE clave. Como el recurso que no entra es el
  tiempo, y la caja sí, Finanzas recomienda B1 (ver "Tensiones").

**Piso de capacidad del plan, por trimestre (FTE clave).** Es lo que el board
tiene que confirmar disponible, no lo que el supuesto promete:

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Producto diferido y replan de T2 (recomendado) | 1,6 | 2,2 | 2,2 | 2,1 |
| Producto diferido con la excepción de T2 | 1,6 | 2,5 | 2,2 | 2,1 |
| Con P liberado en G2 | 1,6 | 2,2 | 3,7 | 3,1 |
| Producto desde T2 (comparación, sin replan) | 1,6 | 3,5 | 3,7 | 3,1 |
| Horas distribuidas (segundo sobre) | 590 h | ~1.210 h | ~580 h | ~410 h |

Sin replan, **T2 excedía el máximo del sobre en ~0,3 FTE**, y no había holgura en
T3 ni en T4 para correrlo. El [Anexo B](02-arquitectura.md) ("Exceso de T2")
propone dos salidas, y Finanzas toma la primera como base:

- **Replan de B (recomendado):** arquitecto 0,5 → 0,4 (el diseño del piloto pasa
  a T3) y DevOps/QA 1,0 → 0,8 (las evals en CI y la reejecución de la prueba de
  portabilidad pasan a los 0,2 FTE pagados y sin asignar del contractor). T2
  queda en 2,23 FTE clave: entra, con ~0,03 de holgura. Baja el tiempo de T2 en
  ~5 mil (3-8) y no suma caja. Depende de que se apruebe el contractor: sin él,
  el 0,2 no existe.
- **Excepción acotada en G0 (alternativa):** el board aprueba 0,3 FTE por encima
  del sobre en T2. No suma caja; deja el tiempo de T2 en 75,2 y saca ~3-8 mil de
  horas facturables.

Lo decide el board en G0. La holgura que queda es mínima en los tres trimestres
(~0,03 en T2, ~0,04 en T3, ~0,14 en T4). Si G2 libera P, el sobre de T3-T4 se
amplía a 3,7 / 3,1: esa ampliación se decide en G2, no en G0.

### IA aplicada: alternativas costeadas

B y D coinciden en que el contractor **reemplaza** la fracción interna de T2-T4,
no la complementa, y los dos adoptan como base el contractor al 50% desde T1
(B1). El rol interno de 0,3 FTE en T1 queda como alternativa de B, válida solo
si la dirección técnica demuestra antes de G0 experiencia en evals y harness. Año
completo sin T0, con el producto diferido, medios (rango):

| Alternativa | Caja | Tiempo | Económico | FTE clave T1 / T2 / T3 / T4 |
|---|---|---|---|---|
| 1. Reemplaza desde T1 (contractor B1) — **base** | 177 (98-255) | 213 (113-313) | 390 | 1,6 / 2,2 / 2,2 / 2,1 |
| 2. Rol interno de 0,3 en T1, reemplaza desde T2 | 164 (91-236) | 220 (117-324) | 384 | 1,9 / 2,2 / 2,2 / 2,1 |
| 3. Complementa (T1-a, contractor y fracción interna) | 166 (92-239) | 290 (157-421) | 455 | 2,3 / — |
| 4. Sin contractor, con T1-b (los hitos de IA aplicada de T1 pasan a T2) | 83 (44-122) | 274 (149-400) | 357 | **1,6 / 3,3 / 3,0 / 2,9** |
| 4-a. Sin contractor, con T1-a (todo interno; versión anterior de la fila 4) | 86 (45-126) | 290 (157-421) | 375 | 2,3 / 3,3 / 3,0 / 2,9 |

Las filas 2, 3 y 4-a restan el frente producto a los valores con producto que se
costearon antes y aplican los cambios que no dependen de la vía (infraestructura
sin piloto y avanzado a 480 h); la fila 1 sale del cuadro de arriba. La fila 4
parte de la 1: saca el contractor con su contingencia (−94; 54-133) y suma 0,8
FTE de IA aplicada interna en T2-T4 a costo de especialista (+56; 32-79) y el
replan de T2 que deja de existir (+5; 3-8). El replan se aplica solo a las filas
1 y 2: sin contractor no hay quien absorba el 0,2, y B dice que sin él no hay
replan ([Anexo B](02-arquitectura.md), alternativa C). B no costea la 3 con
replan. La 2 cuesta casi lo mismo que la 1. El 0,5 del contractor en T1 se
dimensionó para T1-a: con T1-b, el 0,2 que excede los 0,3 que pide B es traspaso
y documentación, según D.

**Sobre el económico total, la fila 4 es la más barata, y no entra.** Ahorra caja,
que es el recurso que sí entra, y gasta tiempo clave, que es el que no.

#### Dos contingencias del contractor, que no se resuelven igual

Las fracciones clave de T2 sin contractor son las de B en su alternativa C (0,5
arquitecto, 1,0 DevOps/QA y 0,8 de IA aplicada interna: 2,3) más las de C y D,
que no cambian (~1,0: 0,45 de gobierno y seguridad, ~0,38 de actividades clave y
0,2 del líder del programa). En T3 y T4, B suma 2,3 y 2,2 y C y D, ~0,7.

| Contingencia | Qué falta | FTE clave T2 / T3 / T4 | Contra el máximo del sobre (2,25) | Respuesta |
|---|---|---|---|---|
| **A. Hay contractor, pero sin el 0,2 adicional** (el traspaso se lo come o el contrato no lo incluye) | Las evals en CI y la reejecución de la prueba de portabilidad vuelven a DevOps/QA | 2,5 / 2,2 / 2,1 | +0,25 en T2 | La **excepción acotada** de 0,3 en T2, aprobada en G0 como respaldo. +5 de tiempo (3-8), sin caja |
| **B. No hay contractor** (el Directorio no lo aprueba o no se contrata a tiempo) | Toda la fracción de IA aplicada de T2-T4 (0,8 FTE) y el replan | **3,3 / 3,0 / 2,9** | **+1,1 / +0,8 / +0,7** | La excepción **no alcanza**. Ver abajo |

La contingencia B no se cubre con tiempo: pediría ampliar el sobre clave casi un
50% por encima de su máximo en T2, con 0 holgura hoy, y lo que ahorra es caja
(~94), el recurso que no falta. **Propuesta de Finanzas: el contractor (o el rol
interno demostrado en T1 y el contractor desde T2, fila 2) es condición de no
inicio de los hitos de IA aplicada de T2-T4**: gateway con ruteo, evals en CI,
caso de referencia y prueba de portabilidad y costo. B ya aplica esa regla en T1.
Sin contractor contratado al cierre de T1, G1 no libera el T2 diseñado; libera
un T2 sin esos hitos, que redimensiona `architect` (propuesta en el reporte), y
sus consecuencias se aceptan de antemano:

- Las condiciones de G2 de portabilidad y cobertura de precio quedan sin medir:
  la palanca de precio sale del deck y no hay compromisos de volumen.
- El caso de referencia no llega a L2 en el año.
- El plan se reduce a inventario, línea base, controles y formación. La caja
  baja (sin contractor), pero el throughput que se mide es el de la adopción
  sola, sin plataforma.

La alternativa de financiar la contingencia B con tiempo (fila 4) queda costeada
y a la vista: si el board la prefiere, tiene que confirmar en G0 un piso de
3,3 / 3,0 / 2,9 FTE clave, no de 2,2 / 2,2 / 2,1.

### Beneficios por palanca

Regla: cada beneficio se cuenta una sola vez y se declara su tipo. **Ninguno es
caja dentro de los 12 meses.**

| Palanca | Tipo | 12 meses (base) | A régimen (anual) | Supuesto y fuente |
|---|---|---|---|---|
| Productividad interna en equipos propios | Capacidad liberada (horas evitadas), no caja | 62 mil (28-105) a costo cargado | 130 mil (59-219) con g = 15%; 48 con 5%; 200 con 25% | Lectura A del [Anexo B](02-arquitectura.md): a output fijo, un throughput de x libera x/(1+x) de las horas ([ganancia](../../context/supuestos/ganancia-de-productividad.md), [N y costo](../../context/supuestos/desarrolladores-en-equipos-propios.md), [rampa](../../context/supuestos/rampa-de-la-ganancia.md)) |
| Margen en staffing | Margen | 0 | 0 en base | En contratos por hora, menos horas es menos facturación ([supuesto](../../context/supuestos/ganancia-de-productividad.md)). Solo hay margen con precio por resultado ([apunte](../../material/apuntes/2026-09-29-tokenomics-aiops.md)) |
| Ingresos nuevos por IA en el producto | Ingreso | 0 | Sin cifra | Hoy no hay IA en lo que se vende ni precio validado ([hecho](../../context/hechos/ia-en-producto-y-oferta.md)). Sin compromiso contractual antes de G4 ([Anexo B](02-arquitectura.md)) |
| Riesgo de concentración y licencia para operar | Riesgo evitado | Sin cifra | Sin cifra | El cliente principal pesa 40%-50% ([hecho](../../context/hechos/cartera-y-concentracion.md)) y los bancos deben gobernar la IA de sus terceros ([hecho](../../context/hechos/regulacion-clientes-financieros.md)) |
| Cobertura del cambio de precio de los tokens | Exposición evitada | Sin cifra | ~19-24 mil por cada 1× de múltiplo evitado | 4,8-6,1 mil por trimestre × 4. Sin prueba de que el gateway la capture (ver "Gateway: suscripción contra consumo") |

**Throughput.** Se usa la unidad del [Anexo B](02-arquitectura.md): pull request
aceptado (mergeado, con las compuertas de calidad aprobadas y sin reversión a 14
días) por persona activa y por trimestre, estratificado por tipo y tamaño de
cambio. La cohorte son los equipos propios. La ganancia se atribuye contra la
base prospectiva congelada en las semanas 1-4 de T1, con incidentes y retrabajo
al lado; contra la serie de T0 se informa el OKR, sin atribuir.

**Una sola definición de rampa.** La rampa es la fracción del **objetivo de
throughput** que se alcanza en el trimestre, como dice la
[ficha](../../context/supuestos/rampa-de-la-ganancia.md). El throughput del
trimestre t es g × rampa_t, y es lo que miden los gates. Las horas evitadas son
g × rampa_t / (1 + g × rampa_t). El throughput que resulta en cada escenario:

| Escenario | g | T2 | T3 | T4 | Capacidad liberada en 12 meses |
|---|---|---|---|---|---|
| Pesimista | 5% | +0,5% | +1,5% | +3,0% | 12 (5-21) |
| Base | 15% | +3,75% | +9,0% | +15,0% | 62 (28-105) |
| Optimista | 25% | +10,0% | +20,0% | +25,0% | 114 (51-192) |

La base pasa G2 (≥ +3%) y G3 (≥ +8%). El pesimista cae en "espera" en G2 y, al
vencer las 6 semanas, corta (ver "Pesimista con la regla de F"). Aplicar la rampa sobre las horas
ya convertidas, g/(1+g) × rampa_t, daría 60 / 12 / 110: subestima levemente y no
corresponde a la definición de la ficha.

Las dos conversiones responden preguntas distintas:

- **Lectura A, horas evitadas, la del base:** valúa capacidad.
- **Lectura B, output adicional:** vale g × rampa_t en vez de la conversión. Da
  69 mil a 12 meses en el base, y solo vale si hay demanda con precio. Va como
  sensibilidad.

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
seats. Por eso no se carga como costo del plan, salvo en el estrés. El Anexo B
pone 58-73 mil por trimestre (12×); acá se usa el incremental (11×), porque una
vez la suscripción ya se paga.

Las palancas de M2U4 (prompts concisos, modelo adecuado, caché) bajan el múltiplo
([tokenomics](../../material/conceptos/m2u4-tokenomics.md)), pero el curso no da
un porcentaje con fuente.

### Gateway: suscripción contra consumo

El gateway no se justifica por un ahorro prometido. Lo que compra depende del
esquema de precio del agente de código, y en dos de los tres casos no ahorra
nada (miles de USD por año; la suscripción es 19-24):

| Esquema de precio | Sin gateway | Con gateway | Qué compra el gateway |
|---|---|---|---|
| Suscripción plana vigente; el agente no pasa por el gateway | 19-24 | 19-24 más el gateway | Nada en precio: control y telemetría de las superficies enrutables |
| Suscripción plana, pero enrutar el agente obliga a facturar por API | 19-24 | Hasta 211-267 de incremental a 12× | **Adelanta la exposición en vez de cubrirla.** No se enruta el agente mientras la suscripción sea plana |
| El proveedor pasa a cobrar por consumo, k× | k × (19-24) | k × (19-24) × (1 − s), más el gateway | Ahorro si el ruteo, la caché y los topes bajan el consumo en una fracción s |

**Base del cálculo: el gasto elegible.** El ahorro se calcula sobre el gasto que
el modelo financiero pone a precio de consumo **y** que puede pasar por el
gateway, con la misma población y los mismos precios que el resto del anexo. Hoy
ese gasto es el del agente de código (40-45 seats; suscripción de 19-24 por año;
multiplicador k sobre ella). El consumo de los casos propios ya está dentro del
renglón de infraestructura, y las otras superficies (chat, Workspace y el IDE si
no admite proxy) se pagan por seat y no enrutan: quedan fuera del gasto elegible
y su exposición se informa aparte, como pide el [Anexo B](02-arquitectura.md).
Si alguna pasa a cobrar por consumo, entra al gasto elegible solo con su propia
telemetría de costo.

El ahorro anual es k × gasto elegible × *fc* × s, donde *fc* es
la **fracción del costo** del gasto elegible que pasa por el gateway (ponderada
por costo a precio de lista, no por cantidad de eventos) y s es la reducción de
consumo medida sobre **esa misma población** de tareas. El gateway se paga en el
tercer caso si *fc* × s ≥ costo del gateway / (k × gasto elegible
anual). Como hoy el gasto elegible es el del agente, el umbral no cambia de
valor: lo que cambia es la definición, que fija qué se mide en la prueba de T2.
La fracción de eventos sobre las cuatro superficies sigue siendo la métrica de
cobertura de controles, pero no se multiplica por s. Con el renglón entero de
infraestructura a régimen sin piloto, 18-48 por año (cota superior: incluye
retrieval, trazas y evals, no solo el gateway), el umbral de *fc* × s
es:

| Múltiplo k | 2× | 4× | 6× | 12× |
|---|---|---|---|---|
| Reducción necesaria (*fc* × s), medio y rango | 76% (37%-125%) | 38% (19%-62%) | 25% (12%-42%) | 13% (6%-21%) |

Lectura: a 2× el gateway pide bajar el consumo tres cuartos, y en el extremo
caro no se paga por precio; a 12× alcanza con bajarlo un octavo. **Hueco sin base:** no hay medición de qué fracción del
tráfico es enrutable, ni de cuánto baja el consumo el ruteo; tampoco se sabe si
enrutar el agente de código preserva la suscripción plana
([Anexo B](02-arquitectura.md) condiciona el ruteo a un endpoint configurable), ni
si la calidad se sostiene con modelos más baratos, que solo se evalúa con la
suite de evals de T2. La prueba de portabilidad y costo de T2 del
[Anexo B](02-arquitectura.md) lo mide, con criterio de aceptación a 6×
(*fc* × s contra este umbral, 25%). Hasta entonces la cobertura de
precio es una opción, no un ahorro. Hoy B define su *f* como eventos sobre las
cuatro superficies y conserva umbrales anteriores (55% / 37% / 18%): la propuesta de denominador y de cifras para `architect` queda como desacuerdo a la vista hasta que B la adopte.

### ROI, payback y equilibrio

Modelo del equipo con valores medios. T0 entra en el año. La capacidad se valúa
con la lectura A a costo cargado: es el piso.

| Escenario | Caja | Tiempo | Capacidad liberada | ROI económico 12 m | Beneficio de caja 12 m |
|---|---|---|---|---|---|
| Pesimista, estrés sin frenar (base común e interno enteros) | 177 | 217 | 12 (5-21) | −97% | 0 |
| **Base (producto diferido, sin señal)** | **177** | **217** | **62 (28-105)** | **−84%** | **0** |
| Base con señal en G2 (P en T3-T4) | 214 | 257 | 62 (28-105) | −87% | 0 |
| Optimista (P en T3-T4) | 214 | 257 | 114 (51-192) | −76% | 0 |

El optimista con P rinde menos en 12 meses que sin P (−71%): el producto compra
la opción de un contrato en G4, no retorno en el año.

En la base, el neto económico acumulado es −69 en T1, −178 en T2, −252 en T3 y
−332 en T4.

**Año 2, fuera del alcance e ilustrativo** ([supuesto](../../context/supuestos/costo-de-regimen-del-ano-2.md)):
régimen de 48 mil de caja de la base común (33 de infraestructura sin piloto y
15 de pasarela) más 95 mil de mantenimiento, ~143 mil por año. Si el producto
sigue, suma 15 de infraestructura del piloto y 30 de consumo, y el régimen llega
a ~188.

- **Equilibrio del frente interno, una exigencia propia.** Con la lectura A, el
  régimen sin producto pide liberar el 14,3% de las horas de la cohorte. Eso
  exige una ganancia **atribuible** de throughput de **~17%** (g = x/(1−x)),
  entre 9% y 46% según N y el costo, medida contra la **base prospectiva de T1**,
  la misma de los gates. Si la ganancia atribuible llega a +20%, libera ~166 mil
  por año contra ~143 de régimen, un margen de ~24 mil. Ese margen desaparece si
  N × costo resulta ~14% menor que el medio, y en el extremo bajo (15 personas a
  USD 2.500) el equilibrio sube a 46%.
- **El equilibrio y el OKR están en bases distintas.** El +20% del borrador de
  OKR se mide contra T0 e incluye lo que el throughput haya mejorado entre T0 y
  la base de T1, antes de cualquier intervención
  ([convenciones](../../context/supuestos/convenciones-de-calculo.md)). El
  puente es (1 + meta contra T0) = (1 + d) × (1 + ganancia contra T1), donde d
  es la mejora de T0 a la base de T1. Cumplir el OKR asegura el ~17% atribuible
  **solo si d < ~2,8%** (1,20 / 1,167 − 1). Con d = 0 son lo mismo; con
  d = +5%, cumplir el OKR deja ~14% atribuible, debajo del equilibrio. d se
  mide en G1 con la serie retrospectiva de T0 y la base congelada; hasta
  entonces, **no se dice que el OKR cubre el equilibrio** y no se le atribuye al
  plan la mejora previa.
- **Si el régimen carga también el producto**, el equilibrio sube a **~23%**
  (13%-71%) y ni con d = 0 lo cubre la meta: a +20% atribuible faltan ~21 mil
  por año. Finanzas propone el ~17%: el producto lo tiene que pagar el producto,
  no la productividad. `caio` adopta el ~17% como titular, con el ~23% en la
  misma línea ([Anexo F](06-roadmap-riesgo.md)).
- Si la capacidad se vende, el equilibrio baja en proporción a cuánto supera la
  tarifa al costo, y eso se calcula en `private/`.
- **Inversión del año 1:** ningún escenario la recupera en 24 meses con
  productividad sola. El acumulado a 24 meses es −345 en el optimista (con P y
  régimen de 188), −344 en la base y −477 en el pesimista sin frenar.
- **Payback:** no hay dentro del horizonte con productividad sola. Llega antes
  solo con ingreso de producto, con capacidad vendida o si el board le asigna
  valor a la palanca de riesgo.

### Cuánto pierdo si corto

Cada fila suma, en medios y en máximos, lo ejecutado hasta el gate más T0, más el
costo de cierre: un mes de preaviso del contractor a su dedicación vigente y un
mes de infraestructura de laboratorio
([cierre](../../context/supuestos/costos-de-cierre-por-corte.md)). Legal y red team
se contratan por etapa y no comprometen más allá del gate. Aparte se muestra la
**base mínima** que queda el resto del año si se conservan los controles: el
núcleo de gobierno (25% del líder, 20% de seguridad y el Council) más la
pasarela, si ya está instalada ([base mínima](../../context/supuestos/base-minima-tras-un-corte.md)).
Escenario recomendado, sin P:

| Corte en | Caja ejecutada + cierre | Tiempo ejecutado + T0 | Perdido hasta cerrar: medio / máximo | Base mínima del resto del año (caja / tiempo) | Año con el corte: medio / máximo |
|---|---|---|---|---|---|
| G1 | 27 (15-38) | 46 (24-68) | **73 / 106** | 0 / 29 (17-40) | **102 / 146** |
| G2 | 82 (46-117) | 116 (58-174) | 198 / 291 | 8 (3-12) / 19 (11-27) | 224 / 330 |
| G3 | 122 (68-176) | 170 (88-251) | 292 / 427 | 4 (2-6) / 10 (6-13) | 305 / 447 |
| Sin corte | 177 (98-255) | 217 (115-320) | 394 / 575 | — | 394 / 575 |

Con la excepción de T2 en lugar del replan, el corte en G2 pierde 203 / 299 y el
de G3, 297 / 435 (año 230 / 338 y 310 / 454).

**Dos máximos, no uno.** Cortar en G1 cuesta hasta **106 hasta cerrar** (caja
hasta 38, tiempo hasta 68), pero el año con el corte llega a **146** si se
conserva la base mínima, que en G1 es solo tiempo (máximo calculado 40,2; se
autoriza hasta 41 por la regla de techos). La caja del corte,
hasta 38, supera el techo de T1 (33): la diferencia es la reserva de cierre, y
por eso el pedido G0 la autoriza de antemano (ver "Pedido G0").

**Reserva de cierre vigente, actualizada en cada gate.** El cierre ya está
sumado en la columna "caja ejecutada + cierre" de la tabla: lo que faltaba era
la **autorización**, no la cuenta. El costo de cierre crece cuando el contractor
pasa al 100% y el laboratorio a su nivel de T2, así que la reserva de G0 cubre
solo un corte en G1 ([cierre](../../context/supuestos/costos-de-cierre-por-corte.md)):

| Reserva vigente desde | Qué cubre (un mes) | Cierre calculado: medio (rango) | Reserva autorizada | Ampliación en ese gate |
|---|---|---|---|---|
| G0 | Contractor al 50% y laboratorio de T1 | 4 (2,4-6,0) | **6** | — |
| G1 | Contractor al 100% y laboratorio de T2 | 11 (6-15) | **15** | +9 |
| G2 sin P | Igual que G1 | 11 (6-15) | 15 | 0 |
| G2 con P liberado | Más el tenant del piloto | 12 (6,5-17) | **17** | +2 |
| G3 | Igual que G2, con P o sin P | 11-12 (6-17) | 15 o 17 | 0 |

Reglas que propone Finanzas:

- **Renglón propio.** "Reserva de cierre" es un renglón de caja separado del
  techo operativo del trimestre y de la base mínima: no se gasta salvo en un
  corte, no financia otro renglón y no se suma a la caja del año en el escenario
  sin corte.
- **Autoridad.** La aprueba quien aprueba el gate, en el mismo acto: el board en
  G0 y en cada liberación. **Ningún gate libera el compromiso nuevo (contractor al
  100%, tenant del piloto) sin antes ampliar la reserva** al cierre que ese
  compromiso genera.
- **Al final del año.** Si G4 no renueva y el contractor termina en plazo con el
  preaviso dado dentro de T4, la reserva no se usa y se libera.

Con esto, el compromiso máximo de caja autorizado sube por etapas: 39 en G0
(33 + 6), y en G1 el techo de T2 más una reserva de 15. El techo de un trimestre
y la reserva vigente se informan siempre por separado.

**Corte mixto en G3: se corta el frente interno y P sigue.** La regla de F corta
I y la base común si el throughput queda debajo de +5% en G3, pero P puede
seguir si cumple su SLO, y P usa servicios de la base común. Finanzas propone
una **regla de precedencia** para `caio`:

1. **Seguridad primero:** mientras un frente opere, el núcleo de gobierno, la
   pasarela y los bloqueos no se cortan.
2. **Dependencias después:** el frente que sigue conserva la parte de la base
   común que usa (la "base común mínima para P").
3. **Caja al final:** todo lo demás de la base común y del frente cortado se
   corta, con su cierre.

La **base común mínima para P** en T4 es un supuesto de Finanzas que confirma
`architect` ([base mínima](../../context/supuestos/base-minima-tras-un-corte.md)):
infraestructura de base al nivel de T2 (gateway, trazas y evals en CI), pasarela,
el contractor al 50% para las evals del piloto, 0,5 FTE de DevOps/QA y el núcleo
de gobierno. La capa D (red team externo e ISO ampliada) se financia porque G3
la habilita con P liberado. Año con P liberado en G2, medios (rango):

| Escenario | Caja | Tiempo | Económico |
|---|---|---|---|
| Con P, sin corte | 214 (114-314) | 257 (137-376) | 471 |
| **Corte mixto en G3: I y base común cortados, P sigue con su base mínima** | **205 (109-300)** | **226 (121-332)** | **431** |
| Ídem, si G3 no financia la capa D | 180 (95-265) | 226 (121-332) | 406 |

T4 en el corte mixto: caja 52 (28-75) de la base común mínima para P, 13
(5-21) del tramo P y 4 (2-6) de cierre del 50% del contractor que se deja; tiempo
17 (10-25) de base mínima para P y 16 (9-23) de P. **Lectura para el CFO: con P
vivo, el gate de throughput de G3 protege tiempo (~30), no caja (~9).** La caja
de T4 es casi toda infraestructura, contractor y capa D, que P también necesita.

**Pesimista con la regla de F.** El pesimista (g = 5%) da +0,5% de throughput
en G2. La regla de G2 del [Anexo F](06-roadmap-riesgo.md) manda a **esperar**, no
a cortar, entre 0% y +3%: T3 se libera sin escalado y se vuelve a medir a las 6
semanas. La espera vence ahí: si sigue entre 0% y +3%, se corta el frente
interno y queda la base mínima. El producto nunca se liberó, porque sin señal de
cliente G2 lo difiere.

Supuesto de Finanzas para costearlo: "T3 sin escalado" cuesta lo mismo que T3 sin
producto, y es una cota superior. Ningún renglón del cuadro está identificado
como escalado: el plan no suma seats y P ya salió. Por la misma razón, la
condición de F que "frena la expansión de seats" (uso de Tecnología debajo de
60% en G2) **no frena ningún gasto de este anexo**. Lo que sí se puede frenar en
T3 son las horas de champions y de intermedio que no sean rediseño, ~13 de
tiempo en el medio; la propuesta para `caio` va en "Tensiones".

| Pesimista | Año: medio (rango) | Capacidad liberada | Neto |
|---|---|---|---|
| **Con la regla de F: la espera vence a las 6 semanas y corta** | **265 (141-388)** | ~3 | **≈ −262** |
| Si la espera no venciera: espera en G2, corte en G3 | 305 (164-447) | ~5 | ≈ −300 |
| Estrés sin frenar: base común e interno enteros | 394 (213-575) | 12 | −382; −502 si el precio pasa a 12× desde T3 |
| Comparación: el estrés con el producto desde T2 | 492 (264-720) | 12 | −480; −600 con 12× desde T3 |

Con la regla de F, los gates le ahorran al pesimista **~120 mil** contra el
estrés del mismo plan (~82 si la espera no venciera). Un corte directo en G2
daría ≈ −223, pero la regla no lo ordena: espera antes de cortar. Contra la
comparación con el producto desde T2 (−480), la diferencia es ~218 y se parte en
dos: **~120 de los gates** (−382 → −262) y **~98 de diferir el producto**
(−480 → −382). Las dos piezas pesan parecido; ninguna explica sola el ahorro.

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

Neto económico a 12 meses, en la base (−332 mil), moviendo un supuesto por vez:

| Supuesto | Valor | Neto 12 m |
|---|---|---|
| Throughput | 10% / 25% | −351 / −297 |
| Desarrolladores en equipos propios | 15 / 20 | −341 / −323 |
| Costo por desarrollador | 2.500 / 7.000 | −362 / −303 |
| Tiempo reasignado | −30% | −267 |
| Conversión del throughput | Lectura B en vez de A | −325 |
| Exposición por consumo desde T3 (de la empresa, no del plan) | 4× / 12× | −365 / −452 |
| Frente producto liberado en G2 | Tramo P | −409 |
| Excepción de T2 en lugar del replan | +0,3 FTE clave en T2 | −337 |

**Los tres supuestos que más mueven el resultado** son el tiempo reasignado, el
esquema de precio de los tokens y, a régimen, el throughput, que a 12 meses pesa
poco por la rampa. Los escenarios los combinan:

| Escenario | Throughput a T4 y rampa | Precio de tokens | Producto |
|---|---|---|---|
| Pesimista | 5%, rampa 0/10/30/60: por debajo del piso del supuesto; con la regla de F la espera vence a las 6 semanas y corta | Consumo a 12× desde T3, sin mitigar (solo en el estrés) | Sin señal de cliente: P no se libera |
| Base | 15%, rampa 0/25/60/100 | Plano | Sin señal en G2: P no se libera. Con señal, suma su tramo |
| Optimista | 25%, rampa 0/40/80/100 | Plano | Señal en G2, piloto en T3-T4 y un cliente con interés contractual en G4 (sin ingreso en los 12 meses) |

Hay un estrés aparte, no modelado: la pérdida parcial del cliente principal
([supuesto](../../context/supuestos/continuidad-de-clientes-principales.md)). Con
20% menos de facturación, el peso de la caja del plan sobre la facturación sube
25%, y los gates de T2-T4 se congelan hasta revisar el techo.

**Tipo de cambio.** Licencias, tokens y servicios externos se pagan en USD. El
tiempo está costeado en USD de mercado sobre personal en Argentina. Una
apreciación real del peso de más de 20% invalida el
[supuesto de costo](../../context/supuestos/costo-cargado-por-rol.md) y encarece
el tiempo en USD sin cambiar la caja.

### Modelo recalculable

El modelo no se versiona como script. Con las fichas de la tabla de supuestos y
estas fórmulas, un tercero reproduce todas las tablas del anexo. Los valores
reales (facturación, tarifa, nómina) se cargan solo en `private/`.

| Magnitud | Fórmula |
|---|---|
| Costo de tiempo de una actividad | horas × costo mensual del rol / 160, o fracción del rol × costo mensual × meses |
| FTE de un trimestre | horas / 480, o la fracción de rol declarada en el anexo dueño |
| Valor medio de un renglón | (mínimo + máximo) / 2; los totales suman mínimos con mínimos y máximos con máximos |
| Caja con contingencia | Σ renglones de caja × 1,15 |
| Throughput del trimestre t | g × rampa_t |
| Capacidad liberada en el trimestre t (lectura A) | N × costo × 3 × (g × rampa_t) / (1 + g × rampa_t) |
| Lectura B (sensibilidad) | N × costo × 3 × g × rampa_t |
| ROI económico a 12 meses | (capacidad − caja − tiempo) / (caja + tiempo) |
| Beneficio de caja | horas vendidas × tarifa (`private/`) + contrataciones evitadas de un plan aprobado; hoy 0 |
| Régimen anual de la capacidad | N × costo × 12 × g / (1 + g) |
| Throughput de equilibrio | x = costo del año 2 / (N × costo × 12); g* = x / (1 − x) |
| Incremental por consumo | (k − 1) × suscripción del agente de código por trimestre |
| Umbral de reducción para el gateway | (*fc* × s)* = costo del gateway / (k × gasto elegible anual); hoy el gasto elegible es la suscripción del agente de código |
| Puente del equilibrio con el OKR | (1 + meta contra T0) = (1 + d) × (1 + ganancia contra T1); el OKR cubre g* si d < (1 + meta) / (1 + g*) − 1 |
| Umbral de facturación para un techo p | caja con contingencia / p |
| Pérdida al cortar en Gk | caja y tiempo de T1..Tk + T0 + cierre (un mes de contractor y de laboratorio, sin contingencia) |
| Base mínima del resto del año | (núcleo de gobierno + pasarela, si está instalada) × trimestres restantes; si P sigue, más la base común mínima para P |
| Reserva de cierre vigente | Un mes del contractor a la dedicación que libera el gate, más un mes de laboratorio (y del tenant del piloto si P está liberado), redondeado al entero superior del máximo |
| Techo de un gate | máximo con contingencia, redondeado al entero superior |

**Contingencia: una sola regla.** El 15% cubre el **error de precio de los
renglones estimados**. Los renglones nombrados sin estimar (certificación del
nivel avanzado, certificaciones del programa de partners) **no tienen
cobertura propia**: entran solo con una cotización antes de su gate y dentro del
techo aprobado, usando contingencia no consumida o desplazando otro renglón. Si
no entran, no se hacen. El techo no se mueve. La misma regla está en la
[ficha de precios](../../context/supuestos/precios-externos-sin-cotizar.md).

La instrumentación de uso no está entre los no estimados: B la costea como tiempo
dentro de DevOps/QA. La contingencia anual (13-33 mil) no cubre el error de
precio del contractor, cuyo rango tiene 68 mil de ancho, ni el de la
infraestructura, con 24. Por eso los techos de los gates se fijan sobre
**máximos** con contingencia, no sobre medios. La regla es no gastar fuera del
techo, sin excepciones.

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: sale de horas facturables o de entregas a clientes | Alta | Alto | Piso de capacidad por trimestre confirmado en G0; sobre por rol aprobado; suplentes ([Anexo D](04-personas-cultura.md)) | Utilización bajo la meta de 80% dos meses seguidos por causa del plan: se recorta el frente que más tiempo consume |
| El sobre clave disponible está en el extremo inferior (1,0 FTE) | Media | Alto | El board confirma el piso de 1,6 en G0 | Piso no confirmado: T1 no arranca en su versión T1-E |
| Contingencia A: hay contractor, pero su 0,2 libre se consume en el traspaso o el contrato no lo incluye | Media | Medio | Excepción acotada de 0,3 FTE aprobada en G0 como respaldo; `people` confirma el 0,2 en el alcance del contrato | 0,2 no confirmado al cierre de T1: T2 va con la excepción (2,5 FTE clave) |
| Contingencia B: no hay contractor (ni rol interno demostrado) | Media | Alto | Contractor como condición de no inicio de los hitos de IA aplicada de T2-T4; la excepción no alcanza (T2 pediría 3,3 FTE clave) | Sin contractor contratado al cierre de T1: G1 libera un T2 sin gateway con ruteo, evals en CI, caso de referencia ni prueba de portabilidad |
| Cambio a pago por consumo | Alta ([Anexo B](02-arquitectura.md)) | Alto | Gateway con ruteo, caché y topes; FinOps mensual desde T2; no enrutar el agente si eso pierde la suscripción plana | Múltiplo efectivo de más de 6× sin mitigar en un trimestre: se congela la expansión y se topea el consumo |
| La ganancia no aparece o se paga con retrabajo | Media | Alto | Base congelada; costo por PR aceptado; incidentes y retrabajo junto al throughput | Bandas de G2 y G3 (abajo) |
| La espera de G2 se estira sin decisión | Media | Medio | Regla de F: la espera vence a las 6 semanas | — |
| La capacidad liberada no se vuelve caja | Alta | Medio | Destino decidido en G2 (producto propio, producto del Cliente A o venta) | Sin destino en G2: la capacidad no se cuenta como beneficio |
| El piloto de producto no tiene comprador | Media | Medio | P diferido: el presupuesto base no lo incluye y su tramo se libera solo con señal de cliente y matriz habilitante | Sin señal en G2: P no se libera (16-59 de caja y 23-56 de tiempo que no se gastan) |
| El cierre cuesta más que lo previsto, o la reserva vigente no cubre el corte | Baja | Medio | Contratos por etapa, preaviso de un mes, nada a más de 12 meses antes de G4; reserva de cierre autorizada en G0 (6) y ampliada en G1 (15) y en G2 si se libera P (17), antes de cada compromiso nuevo | Reserva no ampliada: el gate no libera el compromiso nuevo |
| Doble conteo de costos entre anexos | Media | Bajo | Tabla de solapes | — |
| El gasto de tecnología sube contra el OKR de menos de 3,5% | Alta | Medio | Reformular el resultado clave (ver tensiones) | — |

## Decisiones

### Recomendación de Finanzas

**Un único pedido G0 por T1-E, con techo máximo, y el resto por gates.** El board
aprueba T1-E, el marco de gates y el producto diferido. Cada trimestre siguiente
se libera solo si cumple su condición, y el tramo de producto, solo con señal de
cliente en G2.

Cortar en G1 cuesta ~73 mil económicos en el medio y **hasta 106 hasta cerrar**:
27 de caja (hasta 38) y 46 de tiempo (hasta 68). Con la base mínima del resto
del año, **hasta 146**. El año completo, sin P, puede llegar a 255 de caja y 320
de tiempo. Esa diferencia es la reversibilidad que compra el diseño.

Alternativas descartadas:

- **A. Aprobar el año completo:** compromete toda la caja con un business case
  que no cierra con productividad sola. Descartada.
- **B. Solo el frente interno, sin la base común:** es más barato, pero no tapa
  el riesgo de precio de los tokens, no abre ingresos y deja sin controles la
  relación con los bancos. Queda como repliegue si fallan los gates.
- **C. Producto desde T2, ampliando el sobre clave a ~3,7 FTE:** gasta en P antes
  de tener señal (37 de caja y 55 de tiempo) y saca de horas facturables lo que
  el sobre no tiene. Queda como opción si el board prefiere velocidad.
- **D. Recomendada: G0 por T1-E, producto diferido y gates**, con el tramo de
  producto condicionado a la señal de G2.

### Pedido G0 y gates económicos (para que `caio` los integre)

**Pedido G0, único.** Incluye siete cosas:

1. **Caja de T1:** techo de 33 mil (máximo calculado 32,2: contractor B1 hasta
   16,5; legal hasta 10; telemetría hasta 1,5; contingencia hasta 4,2).
2. **Reserva de cierre:** hasta 6 mil de caja (un mes de contractor y de
   laboratorio), que solo se usa si un gate corta. Con ella, el compromiso
   máximo de caja que autoriza G0 es **39 mil**. Cubre solo un corte en G1: el
   board se compromete a ampliarla a 15 en G1 y a 17 en G2 si libera P, antes
   de liberar el compromiso nuevo (ver "Reserva de cierre vigente").
3. **Tiempo de T1:** techo de 62 mil, que son 1,6 FTE de personas clave y
   **590 h distribuidas** en la dotación, como segundo sobre.
4. **Piso de capacidad:** el board confirma que el sobre clave disponible es de
   al menos 1,6 FTE en T1 (11 personas al 15% o 16 al 10%) y fija el de T2-T4:
   2,2 / 2,2 / 2,1 con el producto diferido y el replan de T2 de
   [B](02-arquitectura.md), o 2,5 en T2 si elige la excepción acotada. Más la
   lectura del sobre, estricta o separada.
5. **Base mínima tras un corte:** si G1 rechaza seguir, se conserva el núcleo de
   gobierno el resto del año, hasta 41 mil de tiempo (máximo calculado 40,2) y
   sin caja. Es lo que lleva
   el máximo del año con corte en G1 a 146.
6. **T0:** autorizar, o ratificar si hay registro de que ya se hizo, hasta 7 mil
   de tiempo previo a G0. Hoy es una propuesta: no consta que se haya ejecutado.
7. **IA aplicada y producto:** contractor B1, o el rol interno en T1 si
   demuestra capacidad y el contractor desde T2. Sin contractor, los hitos de IA
   aplicada de T2-T4 no se inician (contingencia B: la excepción de 0,3 no la
   cubre). El producto, diferido hasta G2, con su tramo condicional.

El techo de caja se confirma contra el presupuesto 2027 en `private/`.

Esta tabla es una **proyección de la de F** ([Anexo F](06-roadmap-riesgo.md),
"Gates por condición"): resume lo económico y no da órdenes propias. Donde F
tiene una consecuencia por condición, acá se lista la misma; la pérdida de la
última columna vale solo cuando el resultado es un corte.

| Gate | Cuándo | Libera (caja / tiempo, techo) y reserva vigente | Condiciones con efecto económico | Si no se cumple, según F | Pérdida si se corta | Reversible |
|---|---|---|---|---|---|---|
| G0 | Aprobación | T1: 33 / 62; reserva 6 | Pedido G0 completo; techo y piso de capacidad confirmados; vía de IA aplicada | No arranca T1; T0 queda hundido (≤ 7). Sin vía de IA aplicada, sus hitos pasan a T2 | — | Sí |
| G1 | Fin de T1 | T2: 71 / 106 (71 / 114 con la excepción); reserva **ampliada a 15** | Base congelada con la unidad de B; matriz de los clientes que concentran la facturación; uso de T1 dentro del sobre; contractor contratado (propuesta de Finanzas) | **Ninguna condición de G1 corta el plan.** Base insuficiente: 6 semanas más sin atribuir ganancia; sin base al cierre, sale el resultado clave de throughput y el frente interno no escala. Matriz ambigua: *default-deny* y revisión legal hasta el mes 4. Sobre excedido: T2 solo con replan de capacidad. Sin contractor: T2 sin los hitos de IA aplicada (propuesta, pendiente en F) | Solo si el board decide no liberar T2: hasta 106 hasta cerrar; con la base mínima (hasta 41 de tiempo), hasta 146 en el año | Sí |
| G2 | Fin de T2 | T3: 59 / 78; P, solo con señal: 38 / 34 más; reserva 15 (**17** con P) | Throughput: **pasa** ≥ +3% con intervalo que no cruza +3%, sin más retrabajo; **espera** entre 0% y +3% o con intervalo que cruza +3%: T3 sin escalado y nueva medición a las 6 semanas; **corta** ≤ 0% o con más retrabajo. FinOps con el múltiplo medido; destino de la capacidad decidido | Throughput: espera o corte del frente interno, que deja la base mínima; la espera vencida corta igual. Cobertura de precio no demostrada: la palanca sale del deck. Más de 6× sin mitigar: se congela la expansión y se topea el consumo. Sin señal de cliente: P se difiere y sus condiciones de G3 no aplican | Corte del frente interno: 198 (máximo 291) hasta cerrar; año 224 / 330 | Sí |
| G3 | Fin de T3 | T4: 95 / 69; P, si sigue: 21 / 23 más; reserva 15 (17 con P) | Throughput: **pasa** ≥ +8%; **espera** +5% a +8%, solo base mínima y mantenimiento, nueva medición a las 6 semanas; **corta** < +5%. Costo por PR sin subir. Señal contractual o P liberado para la capa D. SLO del piloto, solo si P se liberó | Throughput < +5%: corte del frente interno y de la base común; queda la base mínima. **Si P sigue, rige la precedencia** (seguridad, dependencias, caja) y P conserva su base común mínima. Sin señal contractual ni P: la capa D no se financia | Sin P: 292 (máximo 427) hasta cerrar; año 305 / 447. Con P vivo, corte mixto: año 431 (con P sin corte, 471) | Sí |
| G4 | Fin de T4 | Año 2: régimen de ~143 (~188 con P), en el presupuesto 2028 | Trayectoria hacia ~17% de throughput **atribuible contra la base de T1** (~23% si P sigue; menos si la capacidad se vende) **o** interés contractual en el producto; decisiones sobre contractor, on-premise e ISO 42001 | No se financia el régimen. Queda el frente interno con las licencias vigentes y la base mínima, ~53 por año (29-78); el gateway se da de baja salvo que FinOps muestre que acota más de lo que cuesta | — | Contrato a más de 12 meses o hardware: irreversible |

Las bandas "espera" son la parte económica; la tabla completa de pasa, espera y
corta por condición es de `caio` ([Anexo F](06-roadmap-riesgo.md)). Si esta
tabla y la de F difieren, manda F y esta se corrige.
Irreversibles marcados (de los Anexos [B](02-arquitectura.md) y
[C](03-gobierno-seguridad.md)): compromisos de volumen a más de 12 meses, capex
en infraestructura propia y firma con un cliente. Ninguno se toma antes de G4.

### Solapes entre anexos

Regla: **el base cuenta los dos renglones** salvo donde los dos dueños ya
acordaron la consolidación. La consolidación es un ahorro que confirma el dueño.

| Solape | Renglones | Ahorro posible | Estado |
|---|---|---|---|
| IA aplicada | 0,5 / 0,8 FTE de B y contractor de D | 32-79 de tiempo en T2-T4 y 4-10 en T1 | **Consolidado**: B y D acuerdan que el contractor reemplaza; el base ya lo descuenta |
| Pruebas de bypass y migración | DevOps/QA de B (2,1-10,7, dentro de su fracción) y prueba de integración de C (1,1-5,6) | Hasta 1,1-5,6 | Lo resuelven `architect` y `governance` |
| Red team | Piloto en T3 (B, 5-15, solo en el tramo P) y externo en T4 (C, 10-25) | 5-15 si P se libera y un contrato cubre el piloto y la reprueba | Desacuerdo a la vista en la [ficha](../../context/supuestos/precios-externos-sin-cotizar.md); `architect` y `governance` |
| Gateway y pasarela de salida | Infraestructura (B, 14-38) y pasarela, DLP y logs (C, 4,5-18) | Hasta 4,5-18 si son la misma pieza | `architect` |
| Infraestructura de T3-T4 sin piloto | B la dimensionaba "con el piloto y su tráfico" (2-6 por mes) | 1,5-6 por trimestre (3-12 en T3 y T4 juntos), más 6-24 por año a régimen | **Consolidado**: `architect` confirma que sin P baja al nivel de T2; el incremento pasa al tramo P |
| Seguridad | 20% de un senior de DevOps o seguridad (C) y DevOps/QA (B) | Sin cuantificar | `architect` y `governance` |

## Tensiones con otras miradas

| Tensión | Planteada por | Posición de Finanzas | Estado |
|---|---|---|---|
| Vía de IA aplicada en T1: contractor al 50% (B1) o rol interno de 0,3 FTE | `architect`, `people` | B y D ya adoptan B1 como base; el rol interno queda como alternativa de B si se demuestra antes de G0. Finanzas recomienda B1 porque el recurso que no entra es el tiempo clave (1,6 contra 1,9 FTE), con ~13 mil más de caja; la alternativa 2 cuesta casi lo mismo | **Acordada entre dueños**; la aprueba el Directorio en G0 por la restricción de no contratar |
| Sin contractor, la excepción de 0,3 no alcanza: T2 pediría 3,3 FTE clave | `finance` (re-revisión docente) | El contractor es condición de no inicio de los hitos de IA aplicada de T2-T4; la fila 4 queda costeada si el board prefiere pagar con tiempo | **Propuesta** a `caio`, `architect` y `people`: hoy B, D y F dicen que la excepción cubre la falta de contractor |
| Exceso de ~0,3 FTE clave en T2 con el producto diferido | `finance` | `architect` propone el replan de B (T2 en 2,2 FTE clave, −5 mil de tiempo) y la excepción acotada como respaldo. Finanzas toma el replan como base y deja la excepción costeada | **Pendiente del board en G0**: replan o excepción |
| El equilibrio queda en ~17% sin producto y ~23% si el régimen carga el producto; el OKR de +20% se mide contra otra base | `finance` | El producto lo paga el producto: la cifra que corresponde es ~17%, atribuible contra la base de T1. No se compara restando puntos con el +20% contra T0: el OKR lo cubre solo si de T0 a la base de T1 el throughput sube menos de ~2,8% | **Reabierta**: `caio` mantiene ~17% con ~23% al lado, pero tiene que sacar "3 puntos debajo del OKR" de la slide 8 y de la defensa |
| La condición de F que frena la expansión de seats no frena ningún gasto: el plan no suma seats | `finance` (re-revisión docente) | Propuesta: que el "corta" del uso de Tecnología en G2 (<60%) frene las horas de champions y de intermedio de T3 que no sean rediseño (~13 de tiempo en el medio), o que se rotule como condición sin efecto presupuestario | **Propuesta** a `caio` |
| Denominadores del gateway: *f* de eventos sobre cuatro superficies (B) contra el gasto elegible del modelo (E) | `finance` (re-revisión docente) | Para la prueba económica, *fc* es fracción del costo del gasto elegible (hoy, el agente de código), y *s* se mide sobre esa población; la fracción de eventos queda como métrica de control | **Desacuerdo a la vista** hasta que `architect` adopte la definición |
| Reserva de cierre: G0 autoriza 6 y los cortes de G2-G3 cuestan hasta 15 | `finance` (re-revisión docente) | Reserva vigente que se amplía en G1 (15) y en G2 con P (17), con renglón propio y la misma autoridad que el gate | **Propuesta** a `caio` para F y la slide 8 |
| La espera de G2 no tiene regla de salida | `finance` | Si a las 6 semanas sigue entre 0% y +3%, corta el frente interno | **Resuelta**: adoptada por `caio` en F |
| +20% de throughput con agentes a 12× lo pagado, contra el OKR de gasto de tecnología de menos de 3,5% | `architect` | A régimen, la base libera ~130 mil por año, que cubren consumo incremental hasta ~7× la suscripción. La caja del plan suma gasto de tecnología: el OKR es incompatible salvo que baje la nube. Propuesta: medirlo sin la inversión del plan, o por persona activa | **Escalada a `caio`** para reformular el resultado clave |
| Sobre de capacidad: lectura estricta o separada | `finance` | La separada es propuesta de Finanzas; con la estricta, T1 no entra sin recortar el básico | **Decide el board en G0** |
| Horas por persona-trimestre: 520 (D, calendario) o 480 (E, costeo) | `finance` | E usa 480 para FTE y costo; D ya costea el avanzado con 480 (480-720 h) | **Resuelta** |
| El tiempo de gobierno compite con horas facturables | `governance` | Dos lentes: caja (lo que aprueba el CFO) y económica (caja más tiempo a costo cargado) | **Resuelta** |
| Staffing facturado por hora desincentiva el uso de IA | `people` | Productividad en staffing = 0 en el base. Las horas de capacitación de Operaciones (~400 h) cuestan 4-14 mil a costo; a tarifa de venta valen más, y eso se calcula en `private/` | **Resuelta** para el costo; el modelo comercial queda **escalado a `caio`** |
| Contractor contra la restricción de no contratar | `people` | 47-116 mil de caja, reversible por ser un contrato corto | **Explicitada**: decide el Directorio |
| Matriz de clientes y política sin ratificar | `governance`, `people` | Sin matriz no se libera el producto; la meta de Operaciones no tiene beneficio asignado | **Explicitada** como condición de gate |

## Insumos para el deck

- **Frase para el CFO:** con el producto diferido, el plan cuesta 98-255 mil USD
  de caja y ~3,5 FTE de tiempo en el año, y no genera caja propia en 12 meses.
  Compra un tope al riesgo de precio de los tokens, los controles que piden los
  bancos y la opción de un ingreso de producto, que se paga solo si G2 trae
  señal (16-59 de caja más). Cortarlo en G1 cuesta hasta 106 hasta cerrar y
  hasta 146 en el año con la base mínima.
- **Decisión que se le pide al board:** un único pedido G0 por T1-E: hasta 33 de
  caja más 6 de reserva de cierre, 1,6 FTE clave más 590 h distribuidas, el piso
  de capacidad de T2-T4 con el producto diferido (2,2 / 2,2 / 2,1 con el replan
  de T2, o la excepción), la base mínima si se corta (hasta 41 de tiempo) y T0
  hasta 7.
- **Cifra de alerta:** a 12×, el consumo incremental (211-267 mil al año) iguala
  a toda la caja del plan. Es exposición de la empresa, con o sin plan. El
  gateway la acota solo si baja el consumo (~13% a 12×, ~25% a 6×), y eso no
  está medido: lo mide la prueba de T2.
- **Equilibrio:** ~17% de throughput atribuible a régimen sin producto (~23% si
  se le carga el producto), medido contra la base de T1. Es una exigencia
  propia: el OKR de +20% contra T0 la cubre solo si de T0 a la base de T1 el
  throughput sube menos de ~2,8%, y eso se mide en G1.
- **Contingencias del contractor:** sin su 0,2 adicional, la excepción de 0,3 en
  T2 alcanza; sin contractor, T2 pediría ~3,3 FTE clave y la excepción no
  alcanza: el contractor es condición de no inicio de los hitos de IA aplicada.
- **Reserva de cierre:** 6 en G0, ampliada a 15 en G1 y a 17 en G2 si se libera
  P, siempre antes del compromiso nuevo.
- **Para la Slide 9:** el pesimista espera en G2, la espera vence a las 6 semanas
  y corta (≈ −262), contra el estrés sin frenar del mismo plan (−382); ≈ −300 si
  la espera no venciera.

## Cautelas

- Todo es borrador sin verificación humana: las cifras son rangos o medios de
  supuestos del equipo sin cotización, y las fichas de `context/` están en
  `draft`. Nada es apto para entrega.
- N × costo por desarrollador es una cuenta de mercado, no la nómina de la empresa.
- La valuación de la capacidad a costo cargado y con la lectura A es un piso
  deliberado. La tarifa no se publica ni se deriva de márgenes internos.
- Supuestos sin ficha propia: las fracciones por rol de T1-E (están en los
  Anexos B, C y D), las bandas de espera de G2 y G3 (Anexo F) y el costo de "T3
  sin escalado" (lectura de Finanzas en este anexo).
- El corte de G3 deja solo la base mínima en T4: `caio` adopta el corte del
  frente interno y de la base común ([Anexo F](06-roadmap-riesgo.md)). Si el corte
  alcanzara solo al frente interno y la base común siguiera en T4, el ahorro
  sería ~13 de tiempo: el año quedaría en ~381 y el neto en ≈ −369, casi igual al
  estrés (−382). El gate de throughput protege solo si también frena la base común.
  Con P vivo, la base común mínima para P (supuesto de Finanzas, sin confirmar
  por `architect`; el 50% del contractor es un supuesto sin dato) deja el
  ahorro del corte mixto en ~9 de caja y ~30 de tiempo.
- El replan de T2 depende de que el contractor tenga 0,2 FTE pagados y sin
  asignar en T2, que tiene que confirmar `people` ([Anexo D](04-personas-cultura.md)).
  Si el traspaso se los come (contingencia A), rige la excepción: +5 mil de
  tiempo y 2,5 FTE clave en T2. Si no hay contractor (contingencia B), la
  excepción no alcanza: T2 pediría ~3,3 FTE clave.
- El puente del equilibrio con el OKR supone que la mejora de T0 a la base de T1
  (d) se puede medir con la serie retrospectiva; con cohortes chicas, su ruido
  puede ser del mismo orden que el ~2,8% que separa las dos bases.
- El rango del equilibrio (9%-46%) mueve N y el costo por desarrollador con el
  régimen fijo en su medio; no suma el error del régimen.
- La comparación del gateway bajo suscripción y bajo consumo es un umbral, no un
  ahorro: no hay medición de la fracción enrutable ni del efecto del ruteo.
- El Δp de la palanca de riesgo usa el margen EBITDA como proxy conservador.
- No se usaron las cifras del curso sin fuente primaria (60%-80% de ahorro de
  inferencia, ROI de 2,8×-4,1×, 360 → 7 USD) ([huecos](../../material/huecos.md)).
- Responsable humano de cada gate y de cada cifra: **pendiente**.
