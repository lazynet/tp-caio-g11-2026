---
owner: finance
status: ready
title: "Anexo E — Business case y escenarios"
---

# Anexo E — Business case y escenarios

Slides que sustenta: [Alternativas](../slides.md) y
[Costo y riesgo](../slides.md). Los gates económicos alimentan además
[Roadmap técnico, financiero y cultural](../slides.md).

## Objetivo

Decirle al board, con números trazables, **qué compra la plata, cuándo se ve y
cómo se frena**. El plan protege, mide y explora, y cada frente se justifica de
manera distinta:

- **Protección del negocio existente.** Hay usos de IA en curso. Los controles
  que los acompañan no se justifican por principio ni por retorno: cada uno
  declara **qué restricción contractual, qué riesgo específico o qué necesidad de
  evidencia** lo motiva, y cuál es la alternativa de menor costo —configurar lo
  existente, restringir el uso o ampliar controles—. Un control que no pueda
  nombrar ese motivo se reformula o se retira. Este anexo informa su costo; el
  valor lo juzga quien acepta el riesgo.
- **Eficiencia operativa.** La productividad interna se mide, no se presupuesta.
  La capacidad liberada no es caja hasta que exista una vía para convertirla
  —venderla o evitar una contratación—, y hoy no existe ninguna de las dos.
- **Crecimiento comercial.** Es una opción estratégica a explorar con evidencia,
  no un ingreso del año ni un alcance aprobado. El modelo imputa ingresos
  nuevos 0.

**Pedido inicial: paquete mínimo.**
Medir antes de ampliar, con herramientas existentes y controles aplicables probados,
sin plataforma central. Se pide primero una validación previa acotada; M1-M3
requiere una segunda autorización, con techos de caja y capacidad. La propuesta
económica vigente está en «Pedido inicial: paquete mínimo»: primera autorización
de caja 0 USD / tiempo 8k USD durante la preparación de 2026; segunda,
condicionada y no liberada ahora, de caja 10k USD / tiempo 61k USD para
M1-M3 y reservas de cierre.

**Qué fija y qué libera el Directorio hoy ([R-03 y R-04](07-resoluciones.md#autoridad-y-liberaciones)).**
Fija los techos: **79** hasta cerrar M3 (**85** con el núcleo de guardia) y
**121** como suma de techos del año (**118** sin gastar reservas), con un techo
por tramo: M4-M6 **+16**, M7-M9 **+13** y M10-M12 **+13**. Libera hoy solo **8**.
El CEO firma la segunda liberación y cada gate dentro del techo de su tramo;
superar el techo de un tramo, o cualquier camino con espera que supere 121,
vuelve al Directorio. Cuenta: 79 + 16 + 13 + 13 = 121; 121 − 3 de reservas = 118
(«Techos por tramo», más abajo).

**Qué es el número que se pide.** El límite acumulado de **79k USD** es el **límite de
autorización del alcance presupuestado**, y se compone de caja 9, tiempo
valorizado a costo cargado 59, preparación técnica 3, validación organizativa 5 y
reservas contingentes 3 (1 de caja y 2 de cierre), en k USD. Equivale a
caja 10 + tiempo 69, y a las dos liberaciones, 8 + 71. No autoriza el año ni
acredita aprobación empresarial.

No es una previsión de gasto: es un techo, y los rangos calculados de cada
componente, más abajo, quedan por debajo de los techos redondeados. Tampoco es el
costo económico incremental total: la contribución comercial desplazada es una
magnitud distinta, todavía sin medir, que se informa por separado
(«Conclusión económica»).

El pedido completo 33+6 de caja / 72+7 de tiempo y sus ramas ≈199/≈400 quedan
como **alternativa** (paquete completo), no como pedido vigente. Las tablas de
plataforma, retorno y cortes que siguen describen ese alcance: **su ROI de −84%
corresponde a una inversión que hoy no se solicita** y no debe leerse como
resultado del mínimo. El paquete completo a 12 meses no se paga con productividad
interna; el mínimo compra evidencia sin presupuestar beneficios.

**Quién responde por cada cifra y por cada gate.** El CFO responde por cada cifra
de este anexo y verifica cifras, caja y reservas en cada liberación y gate; no
libera fondos. Cada gate lo produce el CAIO, lo dictamina el AI Council y lo firma
el CEO por delegación dentro del techo de su tramo; lo que supera un techo o amplía el
alcance vuelve al Directorio ([R-04 y R-06](07-resoluciones.md#autoridad-y-liberaciones)).
Las cifras son estimaciones que el CFO contrasta con las fuentes internas antes
de la segunda liberación; sin ese contraste no se libera M1-M3. Los costos son
supuestos sin cotización.

## Supuestos de partida

**Convención de tiempo y de cálculo.** La preparación previa es octubre-diciembre de 2026 y los cuatro tramos de tres meses de 2027 son los meses 1-3, 4-6,
 7-9 y 10-12; los Anexos B y C usan los mismos tramos. Una
persona-tramo son **480 horas de costeo** (160 por mes): con ellas se pasa de
horas a FTE. Las 520 horas de 13 semanas × 40 h son calendario bruto, sin
descontar feriados ni licencias, y no se usan para FTE ni para costo
([convenciones](../../context/supuestos/convenciones-de-calculo.md)).

**Redondeo.** Los medios, los rangos y las pérdidas estimadas se redondean al
entero más cercano. Los **techos y las reservas que se autorizan** se redondean
al entero superior del máximo calculado, para que la autorización nunca quede
por debajo del cálculo ([convenciones](../../context/supuestos/convenciones-de-calculo.md)).

**Moneda y montos.** Montos económicos en **k USD** (1k USD = 1.000 USD),
por actividad y por rol. En tablas y fórmulas monetarias, un número sin unidad
se lee en k USD; horas, FTE, porcentajes y múltiplos conservan su unidad.
Los costos unitarios se expresan en USD/h o USD/mes; los importes exactos
menores se conservan en USD. Son supuestos de planificación, sin cotización. Las fuentes
no publican la facturación ni bases de la empresa: este anexo **no** calcula
porcentajes sobre la facturación. Da el umbral de facturación que hace falta
para que el plan entre en el techo, y lo verifica Finanzas con los datos internos.

| Supuesto | Valor | Fuente |
|---|---|---|
| Capacidad de inversión | Caja incremental de 1%-3% de la facturación anual, más 10%-15% del tiempo de un grupo acotado de personas clave | [Supuesto](../../context/supuestos/capacidad-de-inversion.md) |
| Costo cargado por rol | Rangos supuestos de planificación en USD/mes, no calibrados contra la nómina | [Supuesto](../../context/supuestos/costo-cargado-por-rol.md) |
| Capacidad disponible | Utilización facturable 83%-90%, bench menor a 1 FTE, restricción de no contratar | [Hecho](../../context/hechos/capacidad-y-utilizacion.md) |
| Ganancia de throughput (g) | +10% a +25% por desarrollador a 12 meses, solo en equipos propios | [Supuesto](../../context/supuestos/ganancia-de-productividad.md) |
| Desarrolladores en equipos propios (N) y su costo | 15-20 personas (17,5); USD 2.500-7.000 por mes (4.750). N × costo **no** es la nómina | [Supuesto](../../context/supuestos/desarrolladores-en-equipos-propios.md) |
| Rampa de la ganancia (meses 1-3 / 4-6 / 7-9 / 10-12) | Fracción del objetivo de throughput que se alcanza: base 0/25/60/100%; pesimista 0/10/30/60%; optimista 0/40/80/100% | [Supuesto](../../context/supuestos/rampa-de-la-ganancia.md) |
| Línea de base de atribución | Base prospectiva congelada en las semanas 1-4 del plan; la serie retrospectiva de la preparación previa estima ruido. El OKR se informa al lado contra el cuarto trimestre de 2026; no cambia de base: la retrospectiva solo da lectura contra tendencia, sin atribución (Anexo B, "Respaldo") | [Convenciones](../../context/supuestos/convenciones-de-calculo.md), [Anexo F](06-roadmap-riesgo.md) |
| Poblaciones de capacitación | Básico ~65 × 6 h; intermedio ~50 × 12 h; avanzado ~10; 8 champions al 10% | [Supuesto](../../context/supuestos/poblaciones-de-capacitacion.md) |
| Precios externos y contingencia | Rangos sin cotización; 15% de contingencia sobre la caja | [Supuesto](../../context/supuestos/precios-externos-sin-cotizar.md) |
| Capacidades que hoy no existen | Gateway, inventario de arquitectura, legal dedicado a IA | [Supuesto](../../context/supuestos/capacidades-ausentes.md) |
| Suscripción del agente de código | 40-45 seats × USD 40-45 por mes = 4,8-6,1k USD por tramo de tres meses | Cálculo sobre [uso de IA](../../context/hechos/uso-ia-interno.md) y [costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real / lo pagado | ~12× en el agente de código | [Hecho](../../context/hechos/costos-tecnologia-e-ia.md) (telemetría, no factura) |
| Régimen del año 2 | Caja de ~48k USD de base común (~93 si el producto sigue) más 1,5 FTE senior (~95k USD) | [Supuesto](../../context/supuestos/costo-de-regimen-del-ano-2.md) |
| Cierre y base mínima tras un corte | Un mes de preaviso del contractor y de laboratorio, cubierto por una reserva que se actualiza en cada gate; queda el núcleo de gobierno y la pasarela instalada; si el producto sigue, también la base común que el producto usa | [Cierre](../../context/supuestos/costos-de-cierre-por-corte.md), [base mínima](../../context/supuestos/base-minima-tras-un-corte.md) |
| Sobre de capacidad separado | Tiempo clave contra 1-2,25 FTE; horas distribuidas como segundo sobre | [Propuesta de Finanzas](../../context/supuestos/sobre-de-capacidad-separado.md) |
| Seats nuevos | Ninguno: la meta de adopción es de activación | [Anexo B](02-arquitectura.md) |
| Alternativas más baratas y prueba chica de los meses 1-3 | Composición del gobierno mínimo y formación y del piloto acotado, misma medición en las tres | [Supuesto](../../context/supuestos/alternativas-de-menor-alcance.md) |

**Escenario de costos que consume este anexo.** El primer tramo acotado del
[Anexo B](02-arquitectura.md), el contractor de IA aplicada que **reemplaza** la
fracción interna del Anexo B desde el mes 1 (el contractor desde el mes 1, según el [Anexo D](04-personas-cultura.md)),
el replan de los meses 4-6 del Anexo B y el frente producto diferido. La excepción acotada de los meses 4-6 y
la alternativa con producto desde el mes 4 quedan costeadas como comparación.

**Qué es producto en el costo.** Se cargan al frente producto el consumo de
modelos, el red team del piloto, el incremento de infraestructura del piloto y
los desarrolladores senior (1,5 / 1,0 FTE en los meses 7-12). El
[Anexo B](02-arquitectura.md) lo confirma y etiqueta sus renglones por frente.

**Dónde va la capacitación.** Las horas internas son **tiempo valorizado**;
un curso, certificación o facilitación externa es **caja incremental**.
No se convierte tiempo propio en caja por una decisión de presentación.
El paquete mínimo no incluye formación externa; cualquier excepción requiere
cotización, nuevo costeo y autorización antes de comprometerla. En el paquete
completo, los cursos y certificaciones externos sin estimar solo entran dentro
del techo, desplazando partidas o usando contingencia no consumida, según
[precios externos](../../context/supuestos/precios-externos-sin-cotizar.md).

## Evidencia

### Inversión del paquete completo por tramo (alternativa, k USD)

Consolidado de los Insumos para Finanzas de los Anexos [B](02-arquitectura.md),
[C](03-gobierno-seguridad.md) y [D](04-personas-cultura.md), con valores medios.
Se separa la **caja**, que sale de la empresa, del **tiempo** reasignado, que es
costo de oportunidad. La columna "Frente" dice a qué frente pertenece cada renglón:
la base común o el frente interno.

| Concepto | Frente | Previa | Meses 1-3 | Meses 4-6 | Meses 7-9 | Meses 10-12 | Año (rango) | Dueño |
|---|---|---|---|---|---|---|---|---|
| Infraestructura (primer tramo acotado: solo telemetría en los meses 1-3; los meses 7-12 sin piloto, al nivel de los meses 4-6) | Base común | — | 1,0 | 8,3 | 8,3 | 8,3 | 14-38 | Arquitectura |
| Asesoría legal externa | Base común | — | 7,0 | 7,0 | — | — | 8-20 | Gobierno |
| Pasarela de salida, DLP y logs | Base común | — | — | 3,8 | 3,8 | 3,8 | 4,5-18 | Gobierno |
| Red team externo y auditoría ISO 27001 ampliada (demostración externa del Anexo C: cota superior, ver nota) | Base común | — | — | — | — | 21,3 | 11,6-31 | Gobierno |
| Contractor de IA aplicada (50% en los meses 1-3, 100% en los meses 4-12) | Base común | — | 11,6 | 23,2 | 23,2 | 23,2 | 47-116 | Personas |
| Contingencia 15% | | — | 2,9 | 6,3 | 5,3 | 8,5 | 13-33 | Finanzas |
| **Caja incremental** | | — | **22,6** | **48,6** | **40,5** | **65,0** | **98-255** | |
| Esfuerzo técnico de la base (0,6 / 1,2 / 1,5 / 1,4 FTE) | Base común | 0,3 | 11,2 | 21,3 | 26,6 | 24,5 | 50-118 | Arquitectura |
| Gobierno, seguridad, Council, pruebas de bypass y ejercicios | Base común | — | 13,0 | 16,1 | 9,6 | 10,4 | 27-72 | Gobierno |
| Retrospectiva de la preparación previa, capacitación, champions y líder del programa | Interno | 4,0 | 17,6 | 32,5 | 17,5 | 13,0 | 39-130 | Personas |
| **Tiempo reasignado a costo cargado** | | **4,2** | **41,8** | **69,8** | **53,7** | **47,9** | **115-320** | |
| FTE de personas clave | | — | 1,6 | 2,2 | 2,2 | 2,1 | 2,0 promedio | |
| Horas distribuidas de la dotación (FTE) | | — | 590 h (1,2) | ~1.210 h (2,5) | ~580 h (1,2) | ~410 h (0,8) | 1,5 promedio | |
| **FTE equivalentes** | | — | **2,8** | **4,7** | **3,4** | **3,0** | **3,5 promedio** | |

La suma de las filas, con un decimal, difiere del total publicado en hasta 0,1
(caja 22,5/22,6 en los meses 1-3, 40,6/40,5 en los 7-9 y 65,1/65,0 en los 10-12;
tiempo 4,3/4,2 en la previa y 69,9/69,8 en los meses 4-6). Las diferencias se
atribuyen al redondeo de las filas; los componentes sin redondear no están
publicados en este anexo.

Año: caja 177 (98-255) y tiempo 217 (115-320); económico **394** (213-575). La
prueba chica (la aprobación de hoy, en las dos ramas) suma 6 (3-9) de tiempo y nada de caja: la
rama llega a ≈ 400 (216-584); ROI, cortes de los meses 6 y 9 y pesimista van sin la prueba.
Los FTE suman antes de redondear. Decisiones de los dueños: infraestructura de
los meses 7-12 al nivel de los meses 4-6 (Anexo B), replan de los meses 4-6 (−0,3 FTE clave, −5) y avanzado del Anexo D en el medio
de su rango de costo (4,8-25,2 → 15,0; 480-720 h, medio 600).

**Excepción acotada en lugar del replan.** Si el board elige la excepción, los meses 4-6
quedan en 2,5 FTE clave y 75,2 de tiempo, y el año en tiempo 223 (118-328) y
económico 399 (216-583). La caja no cambia.

**La demostración externa.** El red team externo y la auditoría ampliada son la demostración externa. El [Anexo C](03-gobierno-seguridad.md) (sección "Licencia para vender")
propone condicionarla a la evidencia contractual que se junta en los meses 1-3 y se decide
en el mes 9. Como esa evidencia no depende de la señal de producto del mes 6, el base la
cuenta como cota superior. Si se saca a un tramo condicional, como el producto, la caja
base baja a 152 (85-220) y el techo de caja de los meses 10-12 a 59; el tramo suma 25
(13-36). CAIO la deja en la base como cota superior, con la liberación
condicionada en el mes 9 a la señal contractual ([Anexo F](06-roadmap-riesgo.md)).

**Tramo condicional del frente producto.** Solo si la lectura del mes 6 trae la señal de
cliente. Si no la trae, no se gasta.

| Concepto del producto | Meses 7-9 | Meses 10-12 | Tramo (rango) | Dueño |
|---|---|---|---|---|
| Consumo de modelos del piloto | 7,5 | 7,5 | 6-24 | Arquitectura |
| Red team del piloto | 10,0 | — | 5-15 | Arquitectura |
| Incremento de infraestructura del piloto | 3,8 | 3,8 | 3-12 | Arquitectura |
| Contingencia 15% | 3,2 | 1,7 | 2-8 | Finanzas |
| **Caja del producto** | **24,4** | **12,9** | **37 (16-59)** | |
| Desarrolladores senior del piloto (1,5 / 1,0 FTE) | 23,6 | 15,8 | 39 (23-56) | Arquitectura |
| FTE clave con el producto | 3,7 | 3,1 | | |

Con el producto, el año suma caja 214 (114-314) y tiempo 257 (137-376). Con el producto
desde el mes 4 (sin replan) da la misma caja y tiempo 278 (150-406): diferir ahorra el
desarrollador de los meses 4-6 (~16), habilita el replan (~5) y deja el producto para la lectura del mes 6. El Anexo B absorbe el
diseño del piloto en las semanas 1-4 de los meses 7-9.

**Preparación del paquete completo, alternativa.** Los 1,8-6,7k USD de tiempo
corresponden a la retrospectiva de D y al día de verificación del historial de B.
Son un costo previo propuesto, sin ejecución registrada. El Directorio no
autoriza esta preparación: no forma parte del pedido y queda como antecedente
([R-28](07-resoluciones.md#finanzas)). Si un gate propusiera reactivar el
paquete completo, el CFO presenta antes una estimación común desde ese gate y
decide el Directorio; sin esa decisión, nada de este alcance se ejecuta.

No es la validación inicial del mínimo de 8k USD ni queda financiada por ella.
Si se propone reutilizar trabajo entre ambos alcances, conciliar entregables,
horas y costo una sola vez antes de autorizarlo; no sumar ambas preparaciones
ni dar por ejecutada ninguna. La suscripción vigente no es incremental:
ya está en el gasto de hoy y el plan no suma seats.

**Contra el techo de caja.** La caja con contingencia, 98-255k USD (114-314 con
el producto), entra en el 3% de la facturación si esta es de al menos USD 3,3-8,5 millones
anuales (3,8-10,5 con el producto), y en el 1% si es de al menos 9,8-25,5 millones
(11,4-31,4 con el producto). Lo verifica Finanzas con los datos internos, sin publicar el
dato ni el resultado.

### Capacidad del paquete completo: piso clave y total interno

**No trasladar estos pisos al mínimo.** Con prueba, usando el piso clave
redondeado publicado: 1,8 + 654/480 = **3,1625 FTE internos M1-M3**.
Es una aproximación de planificación, no disponibilidad probada por persona.
M4-M6: (1.068 + 1.208)/480 = **4,7417 FTE internos**, de los cuales
2,225 son clave; margen clave: 2,25×480 − 1.068 = **12 h**.
El contractor externo va aparte. Los sobres separados no liberan agendas:
la matriz semanal privada de D concilia ambas bolsas, trabajo desplazado,
recuperación e ingresos/contribución. No se financian horas iniciales con
ganancias futuras ni se suman costo cargado y contribución perdida dos veces.

El sobre del [supuesto de capacidad](../../context/supuestos/capacidad-de-inversion.md)
es 10%-15% del tiempo de un grupo acotado de personas clave. Cuántas son es un
**supuesto de Finanzas, sin fuente**: [10 a 15](../../context/supuestos/personas-clave-del-sobre.md),
de donde salen **1 a 2,25 FTE**. El supuesto de capacidad no dice nada de las
horas repartidas en toda la dotación (básico, intermedio, avanzado, champions,
ejercicios de mesa). Hay dos lecturas, y el board elige:

- **Estricta:** todo cuenta contra 1-2,25 FTE.
- **Separada (propuesta de Finanzas, [fuente](../../context/supuestos/sobre-de-capacidad-separado.md)):**
  las personas clave contra el sobre, y las horas distribuidas como un
  **segundo sobre que el board aprueba explícitamente en la aprobación de hoy**.

| Alternativa de los meses 1-3 | Clave | Distribuidas | Total | Contra 2,25 FTE | Caja meses 1-3 | Tiempo meses 1-3 |
|---|---|---|---|---|---|---|
| Primer tramo completo, IA interna de 0,5 | 2,3 | 1,2 | 3,5 | 1,56× | 12 | 57 |
| Primer tramo completo con contractor desde el mes 1 (comparación con igual provisión, Anexo B) | 1,8 | 1,2 | 3,0 | 1,33×; clave 0,80× | 25 (14-36) | 46 (24-67) |
| Primer tramo acotado con IA interna de 0,3 (Anexo B) | 1,9 | 1,2 | 3,1 | 1,38× | 9 (5-13) | 49 (26-71) |
| **Primer tramo acotado con contractor desde el mes 1 (recomendada)** | **1,6** | **1,2** | **2,8** | **1,25×; clave 0,70×** | **23 (13-32)** | **42 (22-61)** |
| Primer tramo acotado, versión estricta: el intermedio de Tecnología pasa a los meses 4-6 | 1,6 | 0,8 | 2,4 | 1,06× | 23 (13-32) | 37 (20-54) |
| Primer tramo mínimo: básico e intermedio pasan a los meses 4-6 | 1,6 | 0 | 1,6 | 0,70× | 23 (13-32) | 29 (16-41) |

Lectura:

- **Con la lectura separada, el primer tramo acotado entra si el sobre real llega a 1,6 FTE clave, y
  1,8 con la prueba chica de la aprobación de hoy.** Eso pide 12 personas al 15% o 15 al 12% (sin la
  prueba, 11 al 15%). **Si el sobre disponible es el extremo inferior (1,0 FTE),
  ninguna versión de los meses 1-3 entra.** El board confirma en la aprobación de hoy que dispone de ese piso. Las 590 horas distribuidas son ~9 h por persona de
  la dotación, y el board las aprueba como sobre propio.
- **Con la lectura estricta, ninguna versión que cumpla el básico ≥ 90% en los meses 1-3
  entra.** La versión estricta del primer tramo acotado excede el sobre en 0,15 FTE. El primer tramo mínimo entra, pero
  rompe la meta de básico del [Anexo D](04-personas-cultura.md).
- La vía de IA aplicada de los meses 1-3 cambia caja por tiempo: el contractor desde el mes 1 suma
  ~13k USD de caja y libera 0,3 FTE clave. Como el recurso que no entra es el
  tiempo, y la caja sí, Finanzas recomienda el contractor desde el mes 1 (ver "Tensiones").
- **El primer tramo completo con contractor, contra el primer tramo acotado:** +0,2 FTE clave del Anexo B (+4 de tiempo, 2-6)
  y +2 de caja (1-3) por el gateway en laboratorio ([Anexo B](02-arquitectura.md)).
  Entra en el techo en el medio (25 contra 33), no en el máximo (35,7). Lo que la
  descarta es que el gateway en laboratorio no mide valor sin harness ni evals,
  que son de los meses 4-6.

**Conciliación de los meses 4-6 (actividad → horas → rol → sobre).** Con el replan, 480 horas
por FTE ([convenciones](../../context/supuestos/convenciones-de-calculo.md)):

| Actividad | Horas | FTE | Rol | Sobre |
|---|---|---|---|---|
| Arquitectura (0,4, replan) y DevOps/QA (0,8) del Anexo B | 576 | 1,2 | Arquitectura, plataforma | Clave |
| Gobierno y seguridad (25% de un tech lead, 20% de un senior) | 216 | 0,45 | Liderazgo técnico, seguridad | Clave |
| Líder del programa (20%) | 96 | 0,2 | Liderazgo técnico | Clave |
| Council (5 × 6 h), pruebas de *bypass* (90 h), red team interno (60 h) | 180 | 0,375 | Liderazgo, seguridad, staff | Clave |
| **Clave de los meses 4-6** | **1.068** | **2,225** | | **0,025 bajo 2,25** |
| Intermedio (200 h), avanzado (600 h) y champions (384 h) | 1.184 | 2,47 | Dotación | Distribuido |
| Ejercicio de mesa de incidentes (8 personas × 3 h) | 24 | 0,05 | Dotación | Distribuido |
| **Distribuido de los meses 4-6** | **1.208** | **2,5** | | Segundo sobre |

**La revisión mensual del Council no suma costo.** Los 5 asientos × 6 h de cada tramo de tres meses ya están presupuestados (30 h, como en la fila del Council de la tabla de arriba para los meses 4-6; el resto de los tramos va dentro de la fila de gobierno, con el mismo supuesto del [Anexo C](03-gobierno-seguridad.md)). Tres reuniones mensuales de 2 h con 5 asientos son 30 h: las mismas. El tablero se arma con salidas que ya existen, así que no hay otra línea de costo.

Las 2.790 h distribuidas del año son 590 (meses 1-3: 390 de básico y 200 de intermedio) +
1.208 + 584 + 408, con los ejercicios del [Anexo C](03-gobierno-seguridad.md) (48 h) dentro. **Regla:** los
ejercicios de mesa cuentan como distribuidos, porque participan 8 personas de la
dotación por ejercicio; así queda en la
[fuente del sobre separado](../../context/supuestos/sobre-de-capacidad-separado.md).
Si se contaran como clave, los meses 4-6 pasarían a **2,275 y excederían el máximo en 0,025
FTE**: el replan no entraría solo y regiría la excepción de los meses 4-6 (más abajo), sin
forzar la cuenta. Las horas del avanzado usan el punto medio de 480-720 (600). El
costo de la fila del Anexo D en los meses 4-6 (32,5) es el medio del rango de costo del Anexo D, como en el
resto del anexo: intermedio 200 h × 22,5 USD/h (4,5) + champions 384 h (8,6) +
líder del programa (4,35) + avanzado 15,0 (medio de 4,8-25,2, equivale a ~667 h).
A 600 h × 22,5 daría 13,5 (−1,5, sin mover cifras del deck); con 480 h, 28,3,
que subestima el medio. Separar los sobres no crea horas: el board confirma
capacidad real y trabajo desplazado en la aprobación de hoy.

**Piso de capacidad del plan, por tramo de tres meses (FTE clave).** Es lo que el board
tiene que confirmar disponible, no lo que el supuesto promete:

| | Meses 1-3 | Meses 4-6 | Meses 7-9 | Meses 10-12 |
|---|---|---|---|---|
| Producto diferido y replan de los meses 4-6 (recomendado) | 1,6 | 2,2 | 2,2 | 2,1 |
| Producto diferido con la excepción de los meses 4-6 | 1,6 | 2,5 | 2,2 | 2,1 |
| Con el producto liberado en el mes 6 | 1,6 | 2,2 | 3,7 | 3,1 |
| Producto desde el mes 4 (comparación, sin replan) | 1,6 | 3,5 | 3,7 | 3,1 |
| Sin contractor, modo control del Anexo B (sin hitos de IA aplicada) | 1,6 | 2,2 | 2,2 | 2,1 |
| Sin contractor, fracción interna de 0,8 (alternativa sin contractor, con fracción interna, del Anexo B; comparación) | 1,6 | 3,3 | 3,0 | 2,9 |
| Horas distribuidas (segundo sobre) | 590 h | ~1.210 h | ~580 h | ~410 h |

Sin replan, **los meses 4-6 excedían el máximo del sobre en ~0,3 FTE**, y no había holgura en
los meses 7-9 ni en los meses 10-12 para correrlo. El [Anexo B](02-arquitectura.md) ("Exceso de los meses 4-6 con el producto diferido")
propone dos salidas, y Finanzas toma la primera como base:

- **Replan del Anexo B (recomendado):** arquitecto 0,5 → 0,4 (el diseño del piloto pasa
  a los meses 7-9) y DevOps/QA 1,0 → 0,8 (las evals en CI y la reejecución de la prueba de
  portabilidad pasan a los 0,2 FTE pagados y sin asignar del contractor). Los meses 4-6
  quedan en 2,225 FTE clave: entran, con 0,025 de holgura. Baja el tiempo de los meses 4-6 en
  ~5k USD (3-8) y no suma caja. Depende de que se apruebe el contractor y de que
  su 0,2 esté libre. La documentación mínima reproducible va dentro de la
  fracción que produce cada entregable: 0,8 para IA aplicada y 0,2 para los dos
  entregables del replan. Manuales de operación y traspaso se difieren, según
  [B, «Documentación mínima reproducible»](02-arquitectura.md) y
  [D, «Holgura de 0,2 FTE»](04-personas-cultura.md).
  Si falta solo el 0,2, rige la excepción; si falta el
  contractor, el Anexo B corre los meses 4-6 en modo control (1,2 FTE del Anexo B, sin harness, evals ni
  prueba de portabilidad) y Finanzas recalcula los meses 4-12 (fila 5 de "IA aplicada:
  alternativas costeadas").
- **Excepción acotada en la aprobación de hoy (alternativa):** el board aprueba 0,3 FTE por encima
  del sobre en los meses 4-6. No suma caja; deja el tiempo de los meses 4-6 en 75,2 y saca ~3-8k USD de
  horas facturables.

Lo decide el board en la aprobación de hoy. La holgura que queda es mínima en los tres tramos
(0,025 en los meses 4-6, ~0,04 en los meses 7-9, ~0,14 en los meses 10-12). Si la lectura del mes 6 libera el producto, el sobre de los meses 7-12 se
amplía a 3,7 / 3,1: esa ampliación se decide en el mes 6, no en la aprobación de hoy.

### IA aplicada del paquete completo: alternativas costeadas

Los Anexos B y D coinciden en que el contractor **reemplaza** la fracción interna de los meses 4-12,
no la complementa, y los dos adoptan como base el contractor al 50% desde el mes 1
(recomendado). El rol interno de 0,3 FTE en los meses 1-3 queda como alternativa del Anexo B, válida solo
si la dirección técnica demuestra antes de la aprobación de hoy experiencia en evals y harness. Año
completo sin la preparación previa, con el producto diferido, medios (rango):

| Alternativa | Caja | Tiempo | Económico | FTE clave, meses 1-3 / 4-6 / 7-9 / 10-12 |
|---|---|---|---|---|
| 1. Reemplaza desde el mes 1 (contractor desde el mes 1) — **base** | 177 (98-255) | 213 (113-313) | 390 | 1,6 / 2,2 / 2,2 / 2,1 |
| 2. Rol interno de 0,3 en los meses 1-3, reemplaza desde el mes 4 | 164 (91-236) | 220 (117-323) | 384 | 1,9 / 2,2 / 2,2 / 2,1 |
| 3. Complementa (primer tramo completo, contractor y fracción interna) | 166 (92-239) | 290 (157-421) | 455 | 2,3 / — |
| 4. Sin contractor, con el primer tramo acotado (los hitos de IA aplicada de los meses 1-3 pasan a los meses 4-6) | 83 (44-122) | 274 (149-400) | 357 | **1,6 / 3,3 / 3,0 / 2,9** |
| 4-a. Sin contractor, con el primer tramo completo (todo interno; comparación) | 86 (45-126) | 290 (157-421) | 375 | 2,3 / 3,3 / 3,0 / 2,9 |
| 5. Sin contractor, modo control del Anexo B (sin harness, evals, caso de referencia ni prueba de portabilidad) | 83 (44-122), con infraestructura de base mantenida | 213 (113-313) | 296, con ese alcance | 1,6 / 2,2 / 2,2 / 2,1 |

Las filas 2, 3 y 4-a restan el frente producto a lo costeado con producto (la 1
sale del cuadro de arriba). La 4 y la 5 parten de la 1 y sacan el contractor con
su contingencia (−94; 54-133); la 4 suma 0,8 FTE de IA aplicada interna en los meses 4-12
(+56; 32-79) y el replan que deja de existir (+5; 3-8), porque sin contractor no
hay quien absorba el 0,2 ([Anexo B](02-arquitectura.md), alternativa sin contractor, con fracción interna). La 5
mantiene el replan de los meses 4-6 y 1,5 / 1,4 FTE del Anexo B en los meses 7-12 (modo control del Anexo B,
"Exceso de los meses 4-6 con el producto diferido"); con la suscripción que no permite gateway, la infraestructura de los meses 4-6 baja a
0,5-1,5. La diferencia de caja M4-M6 con contingencia es 3,45-13,225
(resta de intervalos sin presumir correlación; diferencia de medios 8,3375).
La fila 5 compara solo M4-M6: el paquete completo no se pide y no se publica un
año de 75/288 restando solo M4-M6. Si el Directorio liberara plataforma con una
suscripción que no permite gateway, el Responsable de Tecnología costea M7-M12,
el CFO lo verifica antes del gate del mes 6 y, sin ese costeo, no se libera
M7-M9 ([R-17](07-resoluciones.md#arquitectura-y-medición)).

**Qué decide este cuadro.** Describe el intercambio entre caja, tiempo y
entregables del paquete completo; no elige una alternativa equivalente por
menor total. La fila 5 conserva control, sin cobertura de precio ni caso de
referencia; la fila 4 agrega capacidad interna y exige aprobar su exceso de
tiempo clave. Cada una requiere autorización propia. El año de la fila 5 no se
compara; rige la regla de R-17 del párrafo anterior.

#### Dos contingencias del contractor, que no se resuelven igual

Sin contractor, el Anexo B vuelve a la alternativa sin contractor, con fracción interna (2,3 FTE en los meses 4-6) y los Anexos C y D suman ~1,0
(en los meses 7-12, ~0,7).

| Contingencia | Qué falta | FTE clave, meses 4-6 / 7-9 / 10-12 | Contra el máximo del sobre (2,25) | Respuesta |
|---|---|---|---|---|
| **Hay contractor, pero sin el 0,2 adicional** (el traspaso se lo come o el contrato no lo incluye) | Las evals en CI y la reejecución de la prueba de portabilidad vuelven a DevOps/QA | 2,5 / 2,2 / 2,1 | +0,25 en los meses 4-6 | La **excepción acotada** de 0,3 en los meses 4-6, aprobada en la aprobación de hoy como respaldo. +5 de tiempo (3-8), sin caja |
| **No hay contractor** (el Directorio no lo aprueba o no se contrata a tiempo) | Toda la fracción de IA aplicada de los meses 4-12 (0,8 FTE) y el replan | Modo control del Anexo B: 2,2 / 2,2 / 2,1. Con fracción interna (alternativa C): **3,3 / 3,0 / 2,9** | Modo control: entra. Fracción interna: **+1,1 / +0,8 / +0,7** | La excepción **no alcanza**. el Anexo B corre los meses 4-6 en **modo control**, sin hitos de IA aplicada (fila 5). Ver abajo |

La contingencia de que no haya contractor no se cubre con tiempo: con la fracción interna pediría ~50%
más que el máximo del sobre en los meses 4-6, para ahorrar caja (~94), el recurso que no
falta (fila 4: si el board la prefiere, confirma un piso de 3,3 / 3,0 / 2,9).
**Propuesta de Finanzas: el contractor (o la fila 2) es condición de inicio de
los hitos de IA aplicada de los meses 4-12** (ruteo y caché, evals en CI, caso de
referencia, prueba de portabilidad y costo). Con señal en el mes 3 y sin contractor al
cierre de los meses 1-3, la decisión del mes 3 libera el **modo control** del Anexo B ([Anexo B](02-arquitectura.md), "Exceso de
los meses 4-6 con el producto diferido"; fila 5: 83 de caja y 213 de tiempo), con consecuencias aceptadas de
antemano: la palanca de precio sale del deck, el caso de referencia no llega al nivel 2 de autonomía («prepara, no ejecuta») en el año y el throughput es el de la adopción sola, con beneficio φ × 62
(ver "Alternativas equivalentes").

### Beneficios por palanca

Regla: cada beneficio se cuenta una sola vez y se declara su tipo. **Ninguno es
caja dentro de los 12 meses.**

| Palanca | Tipo | 12 meses (base) | A régimen (anual) | Supuesto y fuente |
|---|---|---|---|---|
| Productividad interna en equipos propios | Capacidad liberada (horas evitadas), no caja | 62k USD (28-105) a costo cargado | 130k USD (59-219) con g = 15%; 48 con 5%; 200 con 25% | La lectura de horas evitadas a output fijo del [Anexo B](02-arquitectura.md): a output fijo, un throughput de x libera x/(1+x) de las horas ([ganancia](../../context/supuestos/ganancia-de-productividad.md), [N y costo](../../context/supuestos/desarrolladores-en-equipos-propios.md), [rampa](../../context/supuestos/rampa-de-la-ganancia.md)) |
| Margen en staffing | Margen | 0 | 0 en base | En contratos por hora, menos horas es menos facturación ([supuesto](../../context/supuestos/ganancia-de-productividad.md)). Solo hay margen con precio por resultado ([apunte](../../material/apuntes/2026-09-29-tokenomics-aiops.md)) |
| Ingresos nuevos por IA en el producto | Ingreso | 0 | Sin cifra | Hoy no hay IA en lo que se vende ni precio validado ([hecho](../../context/hechos/ia-en-producto-y-oferta.md)). Sin compromiso contractual antes del mes 12 ([Anexo B](02-arquitectura.md)) |
| Riesgo de concentración y licencia para operar | Riesgo evitado | Sin cifra | Sin cifra | El cliente principal pesa 40%-50% ([hecho](../../context/hechos/cartera-y-concentracion.md)) y los bancos deben gobernar la IA de sus terceros ([hecho](../../context/hechos/regulacion-clientes-financieros.md)) |
| Cobertura del cambio de precio de los tokens | Exposición evitada | Sin cifra | ~19-24k USD por cada 1× de múltiplo evitado | 4,8-6,1k USD por tramo de tres meses × 4. Sin prueba de que el gateway la capture (ver "Gateway: suscripción contra consumo") |

**Throughput.** Se usa la unidad del [Anexo B](02-arquitectura.md): pull request
aceptado (mergeado, con las compuertas de calidad aprobadas y sin reversión a 14
días) por persona activa y por tramo de tres meses, estratificado por tipo y tamaño de
cambio. La cohorte son los equipos propios. La ganancia se atribuye contra la
base prospectiva congelada en las semanas 1-4 del plan, con incidentes y retrabajo
al lado; contra la serie de la preparación previa se informa el OKR, sin atribuir; la serie de la preparación previa
tampoco sustituye a la base si esta resulta ruidosa (Anexo B, "Respaldo").

**Una sola definición de rampa.** La rampa es la fracción del **objetivo de
throughput** que se alcanza en el tramo, como dice la
[fuente](../../context/supuestos/rampa-de-la-ganancia.md). El throughput del
tramo t es g × rampa_t, y es lo que miden los gates. Las horas evitadas son
g × rampa_t / (1 + g × rampa_t). El throughput que resulta en cada escenario:

| Escenario | g | Meses 4-6 | Meses 7-9 | Meses 10-12 | Capacidad liberada en 12 meses |
|---|---|---|---|---|---|
| Pesimista | 5% | +0,5% | +1,5% | +3,0% | 12 (5-21) |
| Base | 15% | +3,75% | +9,0% | +15,0% | 62 (28-105) |
| Optimista | 25% | +10,0% | +20,0% | +25,0% | 114 (51-192) |

**Regla de gate vigente.** El gate de valor lo fija el [Anexo B](02-arquitectura.md) («Gate de valor»): el mes 6 no lee valor y decide por adopción, calidad, costo y controles; el mes 9 pasa con peor caso mayor que 0, espera con estimado ≥ +5% y corta debajo; el mes 12 es insumo del año 2. Las ramas, pérdidas y σ de esta sección del paquete completo se calcularon con la regla anterior (+3% en el mes 6, +8% en el mes 9, espera en el mes 6) y quedan como antecedente; si el paquete se reactiva, se recalculan con la regla vigente ([R-28](07-resoluciones.md#finanzas)).

**El base es condicional a la regla del Anexo F, no un paso asegurado.** El Anexo F pasa un gate
si el **límite inferior** del intervalo llega al umbral, no el estimado. Con
+3,75% y +9%, las lecturas de los meses 6 y 9 pasan solo si el semiancho es ≤ 0,75 y ≤ 1 punto; con
semiancho de 3 (el máximo que admite el Anexo B), los límites son 0,75 y 6, y ninguno pasa.
La calidad pesa igual: si el aumento de incidentes o retrabajo queda incierto (el
intervalo cruza 0 y su límite superior supera el margen de no inferioridad del Anexo B),
el throughput no puede pasar; sin dato de la preparación previa, el pase del base es una condición,
no un estimado.
Que pase depende de σ, la dispersión entre personas del cambio relativo, y de n,
las personas activas (semiancho ≈ 1,645 σ / √n, aproximación normal del
*bootstrap*). **σ no tiene dato:** el Anexo B lo estima con la serie de la preparación previa durante la primera autorización, antes de la segunda liberación.
La tabla dice qué σ haría falta, no cuál hay:

| n activas | σ máx. para pasar la lectura del mes 6 | σ máx. para pasar la lectura del mes 9 | σ máx. para semiancho ≤ 3 |
|---|---|---|---|
| 15 | 1,8 | 2,4 | 7,1 |
| 20 | 2,0 | 2,7 | 8,2 |

Una dispersión entre personas de 2 puntos es muy baja para PR por semana: lo
esperable es que el base **espere** en el mes 6 y, si a las 6 semanas el límite sigue
debajo de +3%, corte. Extender la ventana baja el ruido de conteo de cada
persona, pero no suma personas independientes. Por eso el año del base se lee en
tres ramas, sin probabilidad asignada: **pasa las lecturas de los meses 6 y 9** (−332); **pasa la lectura del mes 6 y no la del mes 9**,
con los meses 10-12 en base mínima (≈ −275: 305 de costo, ~30 de capacidad); **la espera del mes 6
vence y corta** (≈ −245: 265 de costo, ~19 de capacidad, con la misma
aproximación de medio tramo (meses 7-9) del pesimista; las partes publicadas dan −246). Es también
el camino de una base que no resuelve (la decisión sobre la base que no resuelve, del [Anexo F](06-roadmap-riesgo.md)): si no se puede atribuir, la
capacidad no cuenta y el neto es ≈ −265. Ninguna alternativa de esa decisión está costeada. Si la serie de la preparación previa da semiancho > 3 con
la cohorte completa, el Anexo F reformula la lectura del mes 6 antes de la segunda liberación (por ejemplo, decidir solo en el mes 9
si σ ≤ 2,4 con n=15), como prevé el Anexo B, o presenta el base como espera-y-corte. El mínimo es de
**15 activas** ([N y cohorte](../../context/supuestos/desarrolladores-en-equipos-propios.md)).
El pesimista espera en el mes 6 y corta al vencer las 6 semanas.

La lectura de horas evitadas a output fijo valúa capacidad y es la del base; la lectura de output adicional con las mismas horas
(g × rampa_t) da 69k USD y solo vale con demanda con precio.

**Puente a caja.** La capacidad liberada se vuelve caja solo por dos vías.
Ninguna existe hoy, así que el beneficio de caja a 12 meses es **0** en los tres
escenarios:

- **Venta:** horas vendidas × tarifa de venta. La tarifa no se publica y se calcula con los datos internos.
- **Contratación evitada:** solo cuenta contra un plan de contratación aprobado,
  y no hay registro de ninguno (la restricción es no contratar).

La lectura del mes 6 pide decidir el destino de la capacidad, y desde ahí el puente se mide.

**Cómo se lee la palanca de riesgo sin inventar probabilidades.** El gasto en
controles se paga si baja la probabilidad de perder el ingreso que protege en al
menos Δp = costo de los controles / (peso del ingreso protegido × margen). Como
margen se usa el EBITDA de 21%-30% ([hecho](../../context/hechos/situacion-economica.md)),
que subestima lo perdido y por eso exige un Δp más alto. Si los controles
costaran 1% de la facturación y protegen al cliente principal (40%-50%), alcanza
con bajar entre 7 y 12 puntos porcentuales la probabilidad de perderlo en el año:
Δp = 0,01 / (0,40-0,50 × 0,21-0,30) = 6,7%-11,9%, sobre la facturación anual
como base común del costo y del ingreso protegido. No hay
estimación de esa probabilidad: la juzga el board.

### Tokenomics: de suscripción plana a consumo

El agente de código consume unas 12 veces lo que se paga
([hecho](../../context/hechos/costos-tecnologia-e-ia.md)), y el plan supone que la
suscripción plana no es estable ([supuesto](../../context/supuestos/precio-y-dependencia-de-modelos.md)).
Costo incremental en k USD por tramo de tres meses si el proveedor cobra por consumo:

| Múltiplo pagado | 2× | 4× | 6× | 12× |
|---|---|---|---|---|
| Incremental por tramo de tres meses | 4,8-6,1 | 14,4-18,2 | 24,0-30,4 | 52,8-66,8 |

A 12×, el incremental anual (211-267k USD) es del orden de **toda la caja del
plan**. Es una **exposición de la empresa con o sin plan**: el plan no suma
seats. Por eso no se carga como costo del plan, salvo en el estrés. El Anexo B
pone 58-73k USD por tramo de tres meses (12×); acá se usa el incremental (11×), porque una
vez la suscripción ya se paga.

Las palancas de tokenomics (prompts concisos, modelo adecuado, caché) bajan el múltiplo
([tokenomics](../../material/conceptos/m2u4-tokenomics.md)), pero la fuente no da
un porcentaje.

### Gateway: suscripción contra consumo

**La señal no es repago.** El ejemplo medio **33/(6×21,5)=25,6%** cubre
solo la infraestructura anual del gateway a régimen, no el paquete.
Cubrir el diferencial publicado de **233** a 12× pide
**233/(12×21,5)=90,3%** ponderado del gasto elegible (fc×s).
Son costos, horizontes de inversión y bases de consumo distintos; ninguna
de las dos cuentas mide ahorro real ni prueba que una señal pague plataforma.

El gateway no se justifica por un ahorro prometido. Lo que compra depende del
esquema de precio del agente de código, y en dos de los tres casos no ahorra
nada (k USD por año; la suscripción es 19-24). Los casos son los
regímenes (suscripción que permite gateway, suscripción que no lo permite y pago por consumo) de la política de ruteo del [Anexo B](02-arquitectura.md):

| Esquema de precio | Sin gateway | Con gateway | Qué compra el gateway |
|---|---|---|---|
| Suscripción que permite gateway: plana vigente, con o sin ruteo del agente | 19-24 | 19-24 más el gateway | Nada en precio: control y telemetría de las superficies enrutables |
| Suscripción que no lo permite: plana, pero enrutar el agente obliga a facturar por API | 19-24 | Hasta 211-267 de incremental a 12× | **Adelanta la exposición en vez de cubrirla.** No se enruta el agente mientras la suscripción sea plana |
| Pago por consumo: el proveedor pasa a cobrar por consumo, k× | k × (19-24) | k × (19-24) × (1 − *fc* × s), más el gateway | Ahorro si el ruteo, la caché y los topes bajan el consumo de lo enrutable en una fracción s |

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
anual), con *fc* y s sobre el consumo del agente de código a precio de lista;
con *fc* = 0,9, a 6× pide s ≥ 28,4% (13,7%-46,3%).
Con una fracción enrutable menor, el umbral de s aumenta. El Anexo B adoptó la misma definición
("Población y gasto elegible"); su respaldo por fracción de eventos vale solo
marcado "estimado". El 90% de ruta del Anexo B es otra métrica (eventos del agente, en
los regímenes de suscripción que permite gateway y de pago por consumo) y no se multiplica por s. Con el renglón entero de
infraestructura a régimen sin piloto, 18-48 por año (cota superior), el umbral
es (centro ilustrativo de 21,5; extremos sin redondear de 19,2-24,3,
calculados como seats × costo mensual × 12 / 1.000):

| Múltiplo k | 2× | 4× | 6× | 12× |
|---|---|---|---|---|
| Reducción necesaria (*fc* × s), centro y rango | 76,7% (37,0%-125,0%) | 38,4% (18,5%-62,5%) | 25,6% (12,3%-41,7%) | 12,8% (6,2%-20,8%) |

Lectura: a 2× el gateway pide bajar el consumo tres cuartos, y en el extremo
caro no se paga por precio; a 12× alcanza con bajarlo un octavo. **Hueco sin base:** no hay medición de qué fracción del
tráfico es enrutable, ni de cuánto baja el consumo el ruteo; tampoco se sabe si
enrutar el agente de código preserva la suscripción plana
([Anexo B](02-arquitectura.md) condiciona el ruteo del agente al régimen comercial:
si enrutar rompe la suscripción plana, no se enruta), ni
si la calidad se sostiene con modelos más baratos, que solo se evalúa con la
suite de evals de los meses 4-6. La prueba de portabilidad y costo de los meses 4-6 lo mide contra el
umbral a 6× (25,6% con base anual central de 21,5). Hasta entonces la cobertura de precio es una opción, no un
ahorro.

### ROI, payback y equilibrio

**Paquete completo, no retorno del mínimo.** Recálculo con N=17,5,
costo=4.750, tres meses por tramo y las rampas publicadas:
base 62,1313−394 = **−331,8687; ROI −84,2306%**;
optimista sin producto 114,1080−394 = **−279,8920; ROI −71,0386%**;
optimista con producto 114,1080−471 = **−356,8920; ROI −75,7733%**.
La denominación de base y optimista no implica probabilidad ni pase de gates.

Modelo con valores medios. La preparación previa entra en el año. La capacidad se valúa
con la lectura de horas evitadas a costo cargado: es el piso.

| Escenario | Caja | Tiempo | Capacidad liberada | ROI económico 12 m | Beneficio de caja 12 m |
|---|---|---|---|---|---|
| Pesimista, estrés sin frenar (base común e interno enteros) | 177 | 217 | 12 (5-21) | −97% | 0 |
| Rama sin señal en el mes 3: los meses 4-12 como gobierno mínimo y formación, con la prueba (incluida) | ≈ 39 | ≈ 160 | ≥ φ × 62 | −100% a −69% | 0 |
| **Base, rama con señal (producto diferido), si las lecturas de los meses 6 y 9 pasan por límite inferior** | **177** | **217** | **62 (28-105)** | **−84%** | **0** |
| Base con señal en el mes 6 (producto en los meses 7-12) | 214 | 257 | 62 (28-105) | −87% | 0 |
| Optimista (producto en los meses 7-12) | 214 | 257 | 114 (51-192) | −76% | 0 |

El optimista con el producto rinde menos en 12 meses que sin el producto (−71%): el producto compra
la opción de un contrato en el mes 12, no retorno en el año.

**VPN: no se calcula, y no se inventa una tasa.** El caso no trae tasa de descuento ni
costo de capital, y el horizonte es de 12 meses con beneficio de caja 0 en todos los
escenarios del año: descontar flujos que en su mayoría son egresos no cambia la
decisión del board, que es cuánto arriesgar para medir. El VPN pasa a ser la métrica
correcta cuando haya flujos positivos de caja que descontar (régimen del año 2 o un contrato
del producto) y el board fije la tasa. Hasta entonces el anexo usa ROI económico,
neto acumulado y equilibrio, que no necesitan tasa. Quien tiene acceso verifica en
privado si Acme Labs usa una tasa interna de aprobación.

En la base, el neto económico acumulado es −69 en los meses 1-3, −178 en los meses 4-6, −252 en los meses 7-9 y
−332 en los meses 10-12.

**Año 2, fuera del alcance e ilustrativo** ([supuesto](../../context/supuestos/costo-de-regimen-del-ano-2.md)):
régimen de 48k USD de caja de la base común (33 de infraestructura sin piloto y
15 de pasarela) más 95k USD de mantenimiento, ~143k USD por año. Si el producto
sigue, suma 15 de infraestructura del piloto y 30 de consumo, y el régimen llega
a ~188.

- **Equilibrio operativo anual del régimen del año 2, frente interno.** No
  recupera la inversión inicial del año 1 (ver "Inversión del año 1" y
  "Payback") y no es ROI. Con la lectura de horas evitadas, el régimen sin producto pide liberar el 14,3% de las horas de la cohorte. Eso
  exige una ganancia **atribuible** de throughput de **~17%** (g = x/(1−x)),
  entre 9% y 46% según N y el costo, medida contra la **base prospectiva de los meses 1-3**,
  la misma de los gates. Si la ganancia atribuible llega a +20%, libera ~166k USD
  por año contra ~143 de régimen, un margen de ~24k USD. Ese margen desaparece si
  N × costo resulta ~14% menor que el medio, y en el extremo bajo (15 personas a
  USD 2.500) el equilibrio sube a 46%.
- **Observado, rebasing y contrafactual son tres cosas.** El +20% del OKR es
  crecimiento **observado contra el cuarto trimestre de 2026**
  ([convenciones](../../context/supuestos/convenciones-de-calculo.md)).
  Rebasing: (1 + OKR) = (1 + d) × (1 + observado contra los meses 1-3), con d la mejora del
  cuarto trimestre de 2026 a la base de los meses 1-3, medida en el mes 3. Contrafactual: el estimador del Anexo B resta c, el
  cambio del grupo que no adopta (o la tendencia de la preparación previa) en la misma ventana,
  como cambio relativo en la misma unidad, medido desde el mes 6. El atribuible es
  1,20/(1+d) − 1 − c, y el OKR cubre el equilibrio solo si
  **1,20/(1+d) − 1 − c ≥ 0,1667**. Con c = 0, pide d < ~2,8%; con d = 0, c ≤
  ~3,3 puntos; d y c comparten esos ~3 puntos. Ejemplo: d = 0 y c = +5 dejan
  +15% atribuible, debajo del equilibrio. Hasta medir d y c, **no se dice que
  el OKR cubre el equilibrio**.
- **Si el régimen carga también el producto**, el equilibrio operativo anual sube a **~23%**
  (13%-71%) y ni con d = 0 lo cubre la meta: a +20% atribuible faltan ~21k USD
  por año. Finanzas propone el ~17%: el producto lo tiene que pagar el producto,
  no la productividad. CAIO adopta el ~17% como titular, con el ~23% en la
  misma línea ([Anexo F](06-roadmap-riesgo.md)).
- Si la capacidad se vende, el equilibrio baja en proporción a cuánto supera la
  tarifa al costo, y eso se calcula con los datos internos.
- **Inversión del año 1:** ningún escenario la recupera en 24 meses con
  productividad sola. El acumulado a 24 meses es −345 en el optimista (con el producto y
  régimen de 188), −344 en la base y −477 en el pesimista sin frenar.
- **Payback:** no hay dentro del horizonte con productividad sola. Llega antes
  solo con ingreso de producto, con capacidad vendida o si el board le asigna
  valor a la palanca de riesgo.

### Cuánto pierdo si corto

**Paquete completo, alternativa.** Esta sección usa el contractor y la
plataforma de ese alcance. Para el pedido vigente, ver «Pedido inicial:
paquete mínimo», que separa salida inmediata y esperas costeadas.

Cada fila suma, en medios y en máximos, lo ejecutado hasta el gate más la preparación previa, más el
costo de cierre: un mes de preaviso del contractor a su dedicación vigente y un
mes de infraestructura de laboratorio
([cierre](../../context/supuestos/costos-de-cierre-por-corte.md)). Legal y red team
se contratan por etapa y no comprometen más allá del gate. Aparte se muestra la
**base mínima** que queda el resto del año si se conservan los controles: el
núcleo de gobierno (25% del líder, 20% de seguridad y el Council) más la
pasarela, si ya está instalada ([base mínima](../../context/supuestos/base-minima-tras-un-corte.md)).
Rama con señal, sin el producto. La fila del mes 3 incluye la prueba chica de la aprobación de hoy (+6 en el medio,
+9 en el máximo); las demás, no:

| Corte en | Caja ejecutada + cierre | Tiempo ejecutado + preparación previa | Perdido hasta cerrar: medio / máximo | Base mínima del resto del año (caja / tiempo) | Año con el corte: medio / máximo |
|---|---|---|---|---|---|
| Mes 3 | 27 (15-38) | 52 (27-77), con la prueba | **79 / 115** | 0 / 29 (17-40) | **107 / 156** |
| Mes 6 | 82 (46-117) | 116 (58-174) | 198 / 291 | 8 (3-12) / 19 (11-27) | 224 / 330 |
| Mes 9 | 122 (68-176) | 170 (88-251) | 292 / 427 | 4 (2-6) / 10 (6-13) | 305 / 447 |
| Sin corte | 177 (98-255) | 217 (115-320) | 394 / 575 | — | 394 / 575 |

Con la excepción de los meses 4-6 en lugar del replan, el corte en el mes 6 pierde 203 / 299 y el
del mes 9, 297 / 435 (año 230 / 338 y 310 / 454).

**Dos máximos, no uno.** Cortar en el mes 3 cuesta hasta **115 hasta cerrar** y
**156** en el año con la base mínima, que en el mes 3 es solo tiempo (techo 41). La
caja del corte (hasta 38) supera el techo de los meses 1-3 (33) por la reserva de cierre.

Los acumulados se redondean después de sumar componentes: M3 más núcleo
da 107,4521 de medio y 155,5250 de máximo, que se publican como 107/156,
con el Council anual de 2,25-5,625 de [C](03-gobierno-seguridad.md).
Sumar los renglones ya redondeados (79+29) daría 108 y perdería esa precisión.

**Reserva de cierre vigente, actualizada en cada gate.** El cierre ya está
sumado en la columna "caja ejecutada + cierre" de la tabla: lo que faltaba era
la **autorización**, no la cuenta. El costo de cierre crece cuando el contractor
pasa al 100% y el laboratorio a su nivel de los meses 4-6, así que la reserva de la aprobación de hoy cubre
solo un corte en el mes 3 ([cierre](../../context/supuestos/costos-de-cierre-por-corte.md)).
**Sin señal en el mes 3 no se amplía a 15**: el contractor cierra (≈ 4, dentro de los 6)
y el gobierno mínimo y formación no firma compromisos con preaviso. La ampliación vale con señal en el mes 3, o en
la lectura del mes 6 o del mes 9 que libere la plataforma, antes de contratar:

| Reserva vigente desde | Qué cubre (un mes) | Cierre calculado: medio (rango) | Reserva autorizada | Ampliación en ese gate |
|---|---|---|---|---|
| Hoy | Contractor al 50% y laboratorio de los meses 1-3 | 4 (2,4-6,0) | **6** | — |
| Mes 3 sin señal | Sin contractor; solo telemetría | < 1 | 6 (sin ampliar) | 0 |
| Mes 3 con señal | Contractor al 100% y laboratorio de los meses 4-6 | 11 (6-15) | **15** | +9 |
| Mes 6 sin el producto | Igual que el mes 3 con señal | 11 (6-15) | 15 | 0 |
| Mes 6 con el producto liberado | Más el tenant del piloto | 12 (6,5-17) | **17** | +2 |
| Mes 9 | Igual que el mes 6, con el producto o sin el producto | 11-12 (6-17) | 15 o 17 | 0 |

Reglas que propone Finanzas:

- **Renglón propio.** "Reserva de cierre" es un renglón de caja separado del
  techo operativo del tramo y de la base mínima: no se gasta salvo en un
  corte, no financia otro renglón y no se suma a la caja del año en el escenario
  sin corte.
- **Autoridad.** La aprueba quien aprueba el gate, en el mismo acto: el board en
  la aprobación de hoy y en cada liberación. **Ningún gate libera el compromiso nuevo (contractor al
  100%, tenant del piloto) sin antes ampliar la reserva** al cierre que ese
  compromiso genera.
- **Al final del año.** Si el cierre del mes 12 no renueva y el contractor termina en plazo con el
  preaviso dado dentro de los meses 10-12, la reserva no se usa y se libera.

**Corte mixto en el mes 9: se corta el frente interno y el producto sigue.** La regla del Anexo F corta
el frente interno y la base común si el throughput queda debajo de +5% en el mes 9, pero el producto puede
seguir si cumple su SLO, y el producto usa servicios de la base común. Finanzas propone
una **regla de precedencia** para CAIO:

1. **Seguridad primero:** mientras un frente opere, el núcleo de gobierno, la
   pasarela y los bloqueos no se cortan.
2. **Dependencias después:** el frente que sigue conserva la parte de la base
   común que usa (la "base común mínima para el producto").
3. **Caja al final:** todo lo demás de la base común y del frente cortado se
   corta, con su cierre.

La **base común mínima para el producto** en los meses 10-12 es un supuesto de Finanzas que
Arquitectura confirmó con una corrección ([base mínima](../../context/supuestos/base-minima-tras-un-corte.md),
[Anexo B](02-arquitectura.md), "Caja y otros costos"): infraestructura de base al
nivel de los meses 4-6 (gateway, trazas y evals en CI), pasarela, el contractor al 50% para
las evals del piloto (sin dato que lo respalde), 0,5 FTE de DevOps/QA, **0,1 FTE
de arquitecto** para el gate scale/kill y el paquete de cumplimiento del cuarto tramo (+2
de tiempo, 1,4-3: 0,1 × 3 meses × 4.500-10.000) y el núcleo de gobierno. La demostración externa (red team externo e ISO ampliada) se financia porque la lectura del mes 9
la habilita con el producto liberado. Año con el producto liberado en el mes 6, medios (rango), sumados
desde componentes y redondeados una sola vez:

| Escenario | Caja | Tiempo | Económico |
|---|---|---|---|
| Con el producto, sin corte | 214 (114-314) | 257 (137-376) | 471 |
| **Corte mixto en el mes 9: frente interno y base común cortados, el producto sigue con su base mínima** | **205 (109-300)** | **229 (122-335)** | **433** |
| Ídem, si la lectura del mes 9 no financia la demostración externa | 180 (95-265) | 229 (122-335) | 409 |

los meses 10-12 en el corte mixto: caja 52 (28-75) de la base común mínima para el producto, 13
(5-21) del tramo del producto y 4 (2-6) de cierre del 50% del contractor que se deja; tiempo
20 (11-28) de base mínima para el producto y 16 (9-23) del producto. **Lectura para el CFO: con el producto
vivo, el gate de throughput del mes 9 protege tiempo (~28), no caja (~9).** La caja
de los meses 10-12 es casi toda infraestructura, contractor y la demostración externa, que el producto también necesita.

**Pesimista con la regla anterior (antecedente; ver «Regla de gate vigente» en «Beneficios por palanca»).** El pesimista (g = 5%) da +0,5% de throughput
en el mes 6. La regla del mes 6 del [Anexo F](06-roadmap-riesgo.md) manda a **esperar**, no
a cortar, entre 0% y +3%: el tramo de los meses 7-9 se libera sin escalado y se vuelve a medir a las 6
semanas. La espera vence ahí: si sigue entre 0% y +3%, se corta el frente
interno y queda la base mínima. El producto nunca se liberó, porque sin señal de
cliente, la lectura del mes 6 lo difiere.

Supuesto de Finanzas para costearlo: "los meses 7-9 sin escalado" cuesta lo mismo que los meses 7-9 sin
producto (cota superior): ningún renglón es escalado, porque el plan no suma
seats y el producto ya salió.

| Pesimista | Año: medio (rango) | Capacidad liberada | Neto |
|---|---|---|---|
| **Con la regla del Anexo F: la espera vence a las 6 semanas y corta** | **265 (141-388)** | ~3 | **≈ −262** |
| Si la espera no venciera: espera en el mes 6, corte en el mes 9 | 305 (164-447) | ~5 | ≈ −300 |
| Estrés sin frenar: base común e interno enteros | 394 (213-575) | 12 | −382; −502 si el precio pasa a 12× desde el mes 7 |
| Comparación: el estrés con el producto desde el mes 4 | 492 (264-720) | 12 | −480; −600 con 12× desde el mes 7 |

Contra el producto desde el mes 4 (−480), el pesimista ahorra ~218: **~120 de los
gates** (−382 → −262; ~82 si la espera no venciera) y **~98 de diferir el
producto** (−480 → −382).

### Costo de no actuar

El costo de no actuar no es un beneficio del plan ni se suma al ROI: es lo que la
empresa sigue exponiendo si no mide ni controla. Se lista por separado para no
contarlo dos veces con la palanca de riesgo (ver «Cómo se lee la palanca de riesgo
sin inventar probabilidades»). **No hay cifra de probabilidad ni de pérdida para
ninguno de estos ítems**: cada uno remonta a un hecho o supuesto del caso.

| Exposición | Sin plan | Con el mínimo | Qué se puede decir con la evidencia | Fuente |
|---|---|---|---|---|
| Consumo de modelos | Se paga la suscripción plana y se consume ~12× lo pagado, sin medición por superficie. Si el proveedor pasa a cobrar por consumo, el incremental es 211-267k USD al año a 12×, con o sin plan | **No la reduce**: el mínimo no incluye gateway. Se reevalúa en M3/M6/M9 con nuevo costeo | La exposición existe y el mínimo no la cubre: es un argumento para el hito de plataforma, no un beneficio del pedido | [costos de tecnología](../../context/hechos/costos-tecnologia-e-ia.md), [precio y dependencia](../../context/supuestos/precio-y-dependencia-de-modelos.md) |
| Clientes financieros | Sin matriz de restricciones, inventario de uso ni cláusula, un cliente que por defecto prohíbe modelos externos sobre su código no tiene base para habilitar IA | Matriz, inventario y legal focalizado (caja 2-6) como entregables de M1-M3 | El ingreso en juego es el del cliente principal (40%-50% de la facturación). Si los controles costaran 1% de la facturación, alcanzaría con bajar entre 7 y 12 puntos porcentuales la probabilidad anual de perderlo (Δp = 0,01 / (peso × margen), ver «Cómo se lee la palanca de riesgo»; el mínimo cuesta mucho menos); esa probabilidad no tiene estimación y la juzga el board | [apetito de riesgo de los clientes](../../context/supuestos/apetito-de-riesgo-de-clientes.md), [continuidad de clientes](../../context/supuestos/continuidad-de-clientes-principales.md) |
| Reglas y aplicación por contrastar | El responsable del caso informó que la política está aprobada; falta revisar su respaldo documental y contrastar la regla vigente sobre uso personal del seat corporativo, su aplicación y el intake | Revisión documental de la política aprobada, aplicación e intake con estado actualizado, inventario de uso | La aprobación informada no acredita aplicación ni controles. El uso fuera de las herramientas aprobadas **no está medido**: no se le pone cifra ni se atribuye ahorro a la aprobación | [gobierno y política de IA](../../context/hechos/gobierno-y-politica-ia.md), [encuesta y pilotos](../../context/hechos/encuesta-y-pilotos-ia.md) |

**Cómo se usa en la defensa.** Contra el pedido de 79 de exposición presupuestaria
máxima autorizada (caja 10 + tiempo 69) no se pone una cifra de «costo de no actuar» para ganar el ROI, que es
−84% en el paquete completo y no se positiviza. Se dice qué exposición sigue abierta
si el board dice que no, cuál cubre el mínimo (clientes, reglas y aplicación por contrastar) y cuál no
(consumo). Es la forma honesta de contestar al CFO escéptico: el plan no promete
retorno en 12 meses y compra la información para decidir.

**Problema y recomendación.** Sin esta lista, «medir antes de ampliar» parece
inacción prudente. Recomendación: presentar las tres exposiciones con su fuente y
sin monto. **Alternativa descartada:** poner un monto de pérdida esperada con una
probabilidad supuesta; inflaría el argumento y no hay base. **Dependencias:**
matriz de restricciones (Anexo C), medición de consumo si se reevalúa la
plataforma (Anexo B). **Riesgo:** que el board lea la lista como beneficio; por eso
va fuera del ROI. **Responsable humano:** el CAIO la presenta y el CFO verifica que
no tenga monto ([R-06](07-resoluciones.md#autoridad-y-liberaciones)). **Criterio de éxito:** cada
exposición tiene un indicador observable al cierre de M1-M3 (matriz y inventario
entregados; consumo medido o declarado no medido). **Condición de abandono:** si la
matriz muestra que los contratos vigentes son permisivos, la fila de clientes baja
de prioridad y se informa.

### Fuentes de financiación

El plan se financia **con recursos internos**: margen operativo y reasignación de
tiempo, no deuda ni aportes externos. El supuesto es una inversión incremental de 1%
a 3% de la facturación anual con EBITDA de 21%-30%
([capacidad de inversión](../../context/supuestos/capacidad-de-inversion.md)). El techo
de caja del mínimo (10) requiere una facturación anual de al menos 334k USD al 3% o 1
millón al 1%; se verifica en privado contra el presupuesto 2027.

| Fuente | Cómo se aplicaría | Estado | Ventaja | Riesgo |
|---|---|---|---|---|
| Interna (margen operativo y tiempo reasignado) | Caja 10 y tiempo 69 por etapa, con techos y reserva de cierre | **Vigente** | Reversible: se frena en cada gate sin deuda ni covenants | Compite con otras inversiones del Directorio; el tiempo reasignado puede salir de horas facturables |
| Externa (crédito, financiación de proveedor, subsidio) | No se usa | **No se asume** | Podría liberar caja | Sin cotización ni tasa en el caso; el monto del mínimo es chico frente a su costo de gestión; compromisos de volumen a más de 12 meses son irreversibles y el plan no toma ninguno antes del mes 12; USD |
| Híbrida (el cliente cofinancia el piloto de producto) | Solo el tramo del producto, con señal de cliente en el mes 6 | **Alternativa, no presupuestada** | Valida demanda con plata ajena | Ingreso nuevo 0 en el base; condiciona al cliente y puede ceder control; requiere un acuerdo comercial que hoy no existe |

**Recomendación.** Interna para todo el año y para el mínimo. La híbrida se
evalúa solo si el producto se libera con señal de cliente (mes 6) y como
condición comercial de ese tramo, no como fuente del plan. La externa se descarta
mientras el pedido sea de este tamaño; se reabre si el board amplía al paquete completo
y el presupuesto 2027 no cubre la caja (33+6). **Dependencias:** presupuesto 2027,
agendas confirmadas. **Costo:** los techos vigentes; la financiación externa
no tiene costo calculado. **Responsable humano:** el CFO verifica la fuente de
financiación contra el presupuesto 2027 en la segunda liberación ([R-05](07-resoluciones.md#autoridad-y-liberaciones)). **Criterio de éxito:**
la caja ejecutada no supera el techo de cada liberación. **Condición de abandono:**
si el presupuesto 2027 fija un techo de gasto de tecnología más bajo (lo que invalida
el supuesto de capacidad de inversión), se reduce o resecuencia el pedido en vez de
buscar fuente externa.

**Riesgos financieros y dónde se gestionan.** Tipo de cambio (ver «Sensibilidad»);
exposición por consumo (Riesgos y «Gateway: suscripción contra consumo»); costo de
cierre (reserva por gate, «Cuánto pierdo si corto»); concentración de clientes
(estrés aparte de «Sensibilidad»); doble conteo (tabla de solapes).

### Métricas financieras que se leen en cada gate

La cursada separa tres familias de indicadores que conectan la IA con el negocio:
adopción interna, impacto financiero y calidad de los modelos
([roadmap financiero y narrativa](../../material/conceptos/m3u4-roadmap-tridimensional.md)).
Finanzas es dueña de la segunda y **usa, sin redefinirlas**, las otras dos, que
conservan su dueño.

| Familia | Métrica | Cómo se lee en el gate | Dónde se define |
|---|---|---|---|
| Impacto financiero | Caja y tiempo ejecutados contra el techo y la reserva de cierre vigente | Exposición presupuestaria máxima propuesta hasta cerrar (79 en M3); sin reserva suficiente no se libera el compromiso nuevo | Este anexo («Pedido inicial: paquete mínimo»); «Cuánto pierdo si corto» corresponde al paquete completo |
| Impacto financiero | Throughput atribuible, con el gate de valor del [Anexo B](02-arquitectura.md) | M3 no atribuye ganancia. M6 no lee valor: decide la continuidad por adopción, calidad, costo y controles y corta solo por daño de calidad o caída demostrada. M9 pasa con peor caso mayor que 0 y sin daño, y se acredita el peor caso; espera con estimado ≥ +5%; corta debajo. M12 es insumo del año 2. Una sola espera de 6 semanas, en M9, con subtramo 1 / 6 dentro del techo del tramo, que recomienda el AI Council, verifica el CFO y firma el CEO; al vencer sin pasar, se corta ([R-27](07-resoluciones.md#finanzas)). Ampliar a plataforma lo decide el Directorio ([R-15](07-resoluciones.md#arquitectura-y-medición)) | [Anexo F](06-roadmap-riesgo.md), [umbrales propuestos](../../context/supuestos/umbrales-tecnicos-propuestos.md) y este anexo |
| Impacto financiero | Costo por PR aceptado | No sube en el mes 9; separa lo que cuesta producir del throughput | Este anexo («Costo por outcome») |
| Impacto financiero | Múltiplo efectivo del consumo y destino de la capacidad liberada | Más de 6× sin mitigar en un tramo congela la expansión; sin destino en el mes 6 la capacidad no se cuenta como beneficio | Este anexo («Riesgos y mitigación») |
| Adopción interna | Cohorte activa (mínimo 15) y utilización | Condiciona la lectura del throughput; no se compra «uso» | [Anexo D](04-personas-cultura.md) |
| Calidad | Incidentes y retrabajo junto al throughput | Una ganancia con más retrabajo no pasa | [Anexo B](02-arquitectura.md) y [Anexo C](03-gobierno-seguridad.md) |

El beneficio de caja del año es 0 y el ingreso nuevo, 0: ningún gate se lee contra un
retorno que el plan no presupuesta.

### Costo por outcome

La métrica del costo por outcome es el **costo por outcome aceptado**
([fuente](../../material/conceptos/m1u4-costo-por-outcome.md)). Para el frente
interno se propone el **costo por PR aceptado**, con la unidad del Anexo B: las
licencias, el consumo, la parte de plataforma y las horas de revisión humana,
divididas por los PR aceptados de la cohorte.

**No tiene valor medido:** se mide contra la base congelada en los meses 1-3, y la lectura del mes 9 le pide
que no suba mientras sube el throughput. Sensibilidad **ilustrativa**, en USD
por PR y por tramo de tres meses: licencias de la cohorte de 17,5 a la parte por seat de la
suscripción (21,5k USD / 42,5 seats, ~2,2k USD por tramo de tres meses), 12 semanas por
tramo de tres meses y dos valores **supuestos sin fuente propia** de PR aceptados por persona y
semana (2 y 4). La revisión humana se muestra por cada 15 minutos por PR a
4.750 / 160 = ~30 USD/h. No incluye la plataforma imputada.

| PR aceptados por persona y semana | Licencia, precio plano | Licencia a 6× | Revisión, cada 15 min por PR |
|---|---|---|---|
| 2 (420 por tramo de tres meses) | ~5 | ~32 | ~7 |
| 4 (840 por tramo de tres meses) | ~3 | ~16 | ~7 |

Lectura: con precio plano, el costo por PR lo mueven la revisión humana y el
retrabajo; a 6×, el consumo. El tope de costo por PR y de consumo lo propone FinOps
con la base de los meses 1-3 y lo fija el CFO en el mes 3, antes de cualquier
piloto, como parámetro de control: lo verifica, no libera gasto. Un gasto de IA
fuera del presupuesto que entra en el techo del tramo lo firma el CEO; por
encima de ese techo, el Directorio ([R-04](07-resoluciones.md#autoridad-y-liberaciones),
[Anexo G](07-resoluciones.md#quién-produce-verifica-y-firma-cada-decisión)).
En el producto, el outcome lo fija el diseño del experimento.

### Sensibilidad

Neto económico a 12 meses, en la base (−332k USD), moviendo un supuesto por vez:

Los netos se calculan con 62,1313 de capacidad y 394 de costo antes de
redondear. Para el estrés de consumo se usa la base anual central ilustrativa
de 21,5k USD de «Gateway: suscripción contra consumo»: el incremental de
medio año es (k−1) × 21,5 / 2. No se suman netos ya redondeados.

| Supuesto | Valor | Neto 12 m |
|---|---|---|
| Throughput | 10% / 25% | −351 / −297 |
| Desarrolladores en equipos propios | 15 / 20 | −341 / −323 |
| Costo por desarrollador | 2.500 / 7.000 | −361 / −302 |
| Tiempo reasignado | −30% | −267 |
| Conversión del throughput | Output adicional en vez de horas evitadas | −325 |
| Exposición por consumo desde el mes 7 (de la empresa, no del plan) | 4× / 12× | −364 / −450 |
| Frente producto liberado en el mes 6 | Tramo del producto | −409 |
| Excepción de los meses 4-6 en lugar del replan | +0,3 FTE clave en los meses 4-6 | −337 |

**Los tres supuestos que más mueven el resultado** son el tiempo reasignado, el
esquema de precio de los tokens y, a régimen, el throughput, que a 12 meses pesa
poco por la rampa. Los escenarios los combinan:

| Escenario | Throughput al mes 12 y rampa | Precio de tokens | Producto |
|---|---|---|---|
| Pesimista | 5%, rampa 0/10/30/60: por debajo del piso del supuesto; con la regla del Anexo F la espera vence a las 6 semanas y corta | Consumo a 12× desde el mes 7, sin mitigar (solo en el estrés) | Sin señal de cliente: el producto no se libera |
| Base | 15%, rampa 0/25/60/100 | Plano | Sin señal en el mes 6: el producto no se libera. Con señal, suma su tramo |
| Optimista | 25%, rampa 0/40/80/100 | Plano | Señal en el mes 6, piloto en los meses 7-12 y un cliente con interés contractual en el mes 12 (sin ingreso en los 12 meses) |

**Equivalencia de nombres.** El *conservador* del roadmap financiero de la cursada
([roadmap financiero y narrativa](../../material/conceptos/m3u4-roadmap-tridimensional.md))
corresponde acá al **pesimista**. Se mantiene «pesimista» porque no es una versión prudente del base:
combina throughput bajo con consumo a 12× sin mitigar, así que es un estrés, y llamarlo conservador
sugeriría un caso razonable. Los valores no cambian.

Hay un estrés aparte, no modelado: la pérdida parcial del cliente principal
([supuesto](../../context/supuestos/continuidad-de-clientes-principales.md)). Con
20% menos de facturación, el peso de la caja del plan sobre la facturación sube
25%, y los gates de los meses 4-12 se congelan hasta revisar el techo.

**Tipo de cambio.** Licencias, tokens y servicios externos se pagan en USD. El
tiempo está costeado en USD de planificación sobre personal en Argentina, que
cobra en pesos: costo en USD = costo en ARS / tipo de cambio, así que una
apreciación real del peso encarece el tiempo en USD en la misma proporción, sin
cambiar la caja. Hay dos umbrales distintos. Más de 20% invalida el
[supuesto de costo](../../context/supuestos/costo-cargado-por-rol.md) entero.
Mucho antes, el techo de tiempo del mínimo deja de alcanzar: ver «Sensibilidad
del pedido mínimo».

### Sensibilidad del pedido mínimo

El techo de tiempo de M1-M3 (59) tiene una holgura de 59 − 58,265625 = **0,734375**
sobre el máximo calculado, que ya incluye la verificación de la lectura del mes 3; los techos de caja, de 9 − 8,625 = 0,375. Cada fila
mueve un supuesto con el resto al máximo calculado y dice qué lo rompe:

| Supuesto | Valor que se mueve | Efecto | Qué rompe y qué se hace |
|---|---|---|---|
| Tarifa media de la formación distribuida (540-660 h) | 10-35 USD/h | 5,4-23,1 de tiempo: el supuesto solo mueve **17,7** dentro del rango | Una tarifa media de más de **36,1 USD/h** rompe 59: (59 − 35,165625) / 660 = 36,11 USD/h. Como varias bandas por rol superan 35 USD/h, la mezcla real se confirma en la matriz de la validación |
| DevOps sin el tope de la unión (R-26) | 76-128 h en lugar de 44-72 | +0,6-2,625 de tiempo; máximo **60,890625** | Excede 59 en 1,89: rige el tope y no la suma; si las exportaciones no entran, se reportan como uso estimado y, si aun así no entra, se recostea dentro de 71 o vuelve al Directorio |
| Cotización legal de M1-M3 | 8-16 h × 250-375 USD/h | Caja 2-6 de legal | Con la provisión de herramientas entera (1,5), el techo de 9 admite hasta 9 / 1,15 − 1,5 = **6,33** de legal: 16,9 h a 375 USD/h o 395 USD/h por 16 h. Ejemplo: 500 USD/h × 8-16 h da caja 4,6-10,9 con contingencia y rompe 9. Sin usar herramientas, el máximo es 7,83 (20,9 h a 375) |
| Tipo de cambio real | Apreciación del peso | El tiempo en USD sube en la misma proporción | Con todas las horas al máximo, una apreciación real de más de **1,26%** (0,734375 / 58,265625) obliga a recostear antes de M1, y un recosteo que no entra en 59 se reduce o resecuencia. En M4-M6 el margen es 1,56% (0,215625 / 13,784375) y en M7-M9 y M10-M12, 0,37% (0,040625 / 10,959375): cada gate recostea con el tipo de cambio del momento antes de firmar. La preparación tiene 26% (1,65 / 6,35). La caja no cambia |

Lectura: el mínimo no tiene holgura en tiempo. Cualquiera de los cuatro, al
máximo, obliga a recostear antes de M1; el techo de 59 no sube ([R-26](07-resoluciones.md#finanzas)).
Recostear dentro de 71 lo firma el CEO; superar 71 vuelve al Directorio
([R-05](07-resoluciones.md#autoridad-y-liberaciones)).

### Modelo recalculable

El modelo no se publica como script. Con las fuentes de la tabla de supuestos y
estas fórmulas, un tercero reproduce todas las tablas del anexo. Los valores
reales (facturación, tarifa, nómina) se cargan solo en el registro interno de Finanzas.

| Magnitud | Fórmula |
|---|---|
| Costo de tiempo de una actividad | horas × costo mensual del rol / 160, o fracción del rol × costo mensual × meses |
| FTE de un tramo | horas / 480, o la fracción de rol declarada en el anexo dueño |
| Valor medio de un renglón | (mínimo + máximo) / 2; los totales suman mínimos con mínimos y máximos con máximos |
| Caja con contingencia | Σ renglones de caja × 1,15 |
| Throughput del tramo t | g × rampa_t |
| Capacidad liberada en el tramo t (horas evitadas) | N × costo × 3 × (g × rampa_t) / (1 + g × rampa_t) |
| Output adicional (sensibilidad) | N × costo × 3 × g × rampa_t |
| ROI económico a 12 meses | (capacidad − caja − tiempo) / (caja + tiempo) |
| Beneficio de caja | horas vendidas × tarifa (dato interno) + contrataciones evitadas de un plan aprobado; hoy 0 |
| Régimen anual de la capacidad | N × costo × 12 × g / (1 + g) |
| Throughput de equilibrio | x = costo del año 2 / (N × costo × 12); g* = x / (1 − x) |
| Incremental por consumo | (k − 1) × suscripción del agente de código por tramo de tres meses |
| Umbral de reducción para el gateway | (*fc* × s)* = costo del gateway / (k × gasto elegible anual); hoy el gasto elegible es la suscripción del agente de código |
| Puente del equilibrio con el OKR | atribuible = (1 + meta contra el cuarto trimestre de 2026) / (1 + d) − 1 − c; el OKR cubre g* si atribuible ≥ g* (d: mejora del cuarto trimestre de 2026 a la base de los meses 1-3; c: cambio del control en la ventana, en la misma unidad) |
| Semiancho del intervalo (aproximación) | ≈ 1,645 × σ / √n; un gate pasa si estimado − semiancho ≥ umbral |
| Costo por PR aceptado | (licencias y consumo de la cohorte + plataforma imputada + horas de revisión × costo/hora) / PR aceptados |
| Umbral de facturación para un techo p | caja con contingencia / p |
| Pérdida al cortar en una decisión | caja y tiempo de los tramos ejecutados hasta ella + preparación previa + cierre (un mes de contractor y de laboratorio, sin contingencia) |
| Base mínima del resto del año | (núcleo de gobierno + pasarela, si está instalada) × tramos restantes; si el producto sigue, más la base común mínima para el producto |
| Reserva de cierre vigente | Un mes del contractor a la dedicación que libera el gate, más un mes de laboratorio (y del tenant del piloto si el producto está liberado), redondeado al entero superior del máximo |
| Techo de un gate | máximo con contingencia, redondeado al entero superior |

**Contingencia: una sola regla.** El 15% cubre el **error de precio de los
renglones estimados**. Los renglones nombrados sin estimar (certificación del
nivel avanzado, certificaciones del programa de partners) **no tienen
cobertura propia**: entran solo con una cotización antes de su gate y dentro del
techo aprobado, usando contingencia no consumida o desplazando otro renglón. Si
no entran, no se hacen. El techo no se mueve. La misma regla está en la
[fuente de precios](../../context/supuestos/precios-externos-sin-cotizar.md).

La contingencia anual (13-33k USD) no cubre el error de
precio del contractor, cuyo rango tiene 68k USD de ancho, ni el de la
infraestructura, con 24. Por eso los techos de los gates se fijan sobre
**máximos** con contingencia, no sobre medios. La regla es no gastar fuera del
techo, sin excepciones.

## Riesgos y mitigación

**Registro del paquete completo: alternativa y antecedente.** Los pisos,
excepciones, reservas y referencias a «hoy» de esta tabla corresponden a ese
alcance. Son condiciones propuestas para el paquete completo, no autorizaciones
del mínimo ni de la validación actual de 8k USD. No acreditan aprobación vigente.

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El tiempo reasignado no existe: sale de horas facturables o de entregas a clientes | Alta | Alto | Piso de capacidad por tramo de tres meses confirmado en la aprobación de hoy; sobre por rol aprobado; suplentes ([Anexo D](04-personas-cultura.md)) | Utilización bajo la meta de 80% dos meses seguidos por causa del plan: se recorta el frente que más tiempo consume |
| El sobre clave disponible está en el extremo inferior (1,0 FTE) | Media | Alto | El board confirma el piso de ~1,8 en la aprobación de hoy (1,6 sin la prueba chica) | Piso no confirmado: los meses 1-3 no arrancan en su versión del primer tramo acotado |
| Contingencia: hay contractor, pero su 0,2 libre se consume en el traspaso o el contrato no lo incluye | Media | Medio | Excepción acotada de 0,3 FTE aprobada en la aprobación de hoy como respaldo; Personas confirma el 0,2 en el alcance del contrato | 0,2 no confirmado al cierre de los meses 1-3: los meses 4-6 van con la excepción (2,5 FTE clave) |
| Contingencia: con señal en el mes 3, no hay contractor (ni rol interno demostrado); sin señal no se busca | Media | Alto | Contractor como condición de no inicio de los hitos de IA aplicada de los meses 4-12; la excepción no alcanza (con fracción interna, los meses 4-6 pedirían 3,3 FTE clave) | Con señal y sin contractor contratado al cierre de los meses 1-3: la decisión del mes 3 libera el modo control del Anexo B (2,2 FTE clave), sin harness, evals en CI, caso de referencia ni prueba de portabilidad |
| Cambio a pago por consumo | Alta ([Anexo B](02-arquitectura.md)) | Alto | Gateway con ruteo, caché y topes; FinOps mensual desde el mes 4; no enrutar el agente si eso pierde la suscripción plana | Múltiplo efectivo de más de 6× sin mitigar en un tramo de tres meses: se congela la expansión y se topea el consumo |
| La ganancia no aparece o se paga con retrabajo | Media | Alto | Base congelada; costo por PR aceptado; incidentes y retrabajo junto al throughput | Bandas de los meses 6 y 9 (abajo) |
| La espera del mes 6 se estira sin decisión | Media | Medio | Regla del Anexo F: la espera vence a las 6 semanas | — |
| La capacidad liberada no se vuelve caja | Alta | Medio | Destino decidido en el mes 6 (productos propios, producto de un cliente o venta) | Sin destino en el mes 6: la capacidad no se cuenta como beneficio |
| El piloto de producto no tiene comprador | Media | Medio | Producto diferido: el presupuesto base no lo incluye y su tramo se libera solo con señal de cliente, matriz habilitante y plataforma liberada en el mes 3: sin ella no hay base técnica en los meses 7-9 y la señal que llega en el mes 6 no lo arranca antes de los meses 10-12 ([Anexo B](02-arquitectura.md)) | Sin señal en el mes 6, o sin plataforma: el producto no arranca en los meses 7-9 (16-59 de caja y 23-56 de tiempo que no se gastan; el costo desde el mes 10 no está calculado) |
| El cierre cuesta más que lo previsto, o la reserva vigente no cubre el corte | Baja | Medio | Contratos por etapa, preaviso de un mes, nada a más de 12 meses antes del mes 12; reserva de cierre autorizada en la aprobación de hoy (6) y ampliada en el mes 3 con señal (15; sin señal no hace falta) y en el mes 6 si se libera el producto (17), antes de cada compromiso nuevo | Reserva no ampliada: el gate no libera el compromiso nuevo |
| Doble conteo de costos entre anexos | Media | Bajo | Tabla de solapes | — |
| El gasto de tecnología sube contra el OKR de menos de 3,5% | Alta | Medio | Reformular el resultado clave (ver tensiones) | — |

## Decisiones

### Costos publicados de alcances distintos: referencia, no comparación

El Directorio no elige entre estos alcances por su neto ni manda a
homogeneizarlos: quedan como antecedente ([R-28](07-resoluciones.md#finanzas)).
Si un gate propone ampliar, el CFO presenta antes una estimación común desde ese
gate (gasto futuro evitable, igual población, controles, calidad, medición,
operación y cierre) y decide el Directorio; sin esa estimación no hay decisión
de ampliación. La tabla registra los alcances publicados; sus netos son
ilustrativos, no una elección equivalente.
Montos económicos en k USD; no son techos anuales aprobados.

| Alcance | Caja / tiempo → económico | Qué significa |
|---|---|---|
| Piloto independiente | 5 / 42 → **47** | Cohorte, matriz, prácticas y medición; sin formación general ni legal; −47 a +15 solo como sensibilidad |
| Gobierno y formación desde el inicio | 21 / 141 redondeados → **161 publicado** | Política, matriz, inventario, legal y medición; sin compensatorios añadidos a la rama posterior; no forzar 162 con sumandos redondeados |
| Rama sin señal después de arrancar paquete | ≈39 / ≈160 → **≈199** | ≈69 previa/arranque +6 prueba +114 continuación +4 cierre +6 compensatorios; medio sin rango propio, porque sus componentes mezclan medios de alcances distintos; no es corte total M3 |
| Paquete con señal sin producto ni prueba | 177 / 217 → **394** | Plataforma, controles, formación y demostración externa condicional como cota superior |
| Mismo paquete con prueba | +≈6 de tiempo → **≈400** | Cabecera del paquete completo con señal; ni caja ni autorización anual |
| Paquete con producto sin prueba | 214 / 257 → **471** (251-690) | Otro alcance; optimista ≈114 de capacidad, neto ≈−357. Rango: caja 114-314 + tiempo 137-376 |
| **Paquete mínimo, sin plataforma** | **Caja 2,3-13,8 / tiempo con previa 24,6375-100,31875 → ≈71 (27-114)** | Proyección condicional M1-M12 del paquete mínimo, incluida validación organizativa previa; básico general, cohorte/intermedio, controles probados, medición y descubrimiento; sin valor de capacidad presupuestado; sin reservas gastadas ni construcción de producto |

La fila del paquete mínimo no homogeneiza las demás. Los diferenciales
**394−161=233**, **394−47=347** y **400−199=201** contestan preguntas distintas.
En M3 se comparan únicamente gastos futuros evitables desde el historial común;
preparación y M1-M3 ya ejecutados son hundidos, no costo incremental de continuar.

**Decisión que admite cada cuadro.** El mínimo tiene tareas y techos para
autorizar validación, M1-M3 y luego continuidad o salida por gate. Los cuadros
de 47/161/199/394/400/471 registran alcances y sensibilidades anteriores;
no sostienen elegir plataforma, contratar ni descartar otra opción por su neto.
Para esa decisión falta una estimación común desde el gate de elección, con
igual población, controles aplicables, calidad, medición, operación y cierre.
Los costos hundidos no se trasladan al nuevo pedido.

#### Composición de las tres opciones originales

La pregunta del CFO: por qué pagar 394 si opciones más baratas compran parte del
mismo aprendizaje. El supuesto declara misma medición, pero no prueba
equivalencia de controles ni costo completo para cada superficie habilitada
([supuesto](../../context/supuestos/alternativas-de-menor-alcance.md)).
Año 1, k USD, medio (rango):

| | Paquete completo | Gobierno mínimo y formación, sin plataforma ni contractor | Piloto sobre el agente de código |
|---|---|---|---|
| Caja | 177 (98-255) | 21 (12-30): legal y telemetría, con contingencia | 5 (2-7): telemetría |
| Tiempo | 217 (115-320); 1,6-2,2 FTE clave | 141 (71-211); ~1,2 FTE clave en los meses 1-3, ~0,9 después | 42 (22-62); ~0,8 FTE clave en los meses 1-3, ~0,4 después |
| Costo económico | 394 (213-575) | 161 (82-240) | 47 (24-69) |
| Qué compra | Plataforma, controles, harness y evals, caso de referencia, portabilidad, base común del producto y demostración externa | Política, matriz, inventario, legal, formación y medición. El costo original no incluye todos los compensatorios hoy exigidos por C: no habilita uso solo por política | Cohorte, prácticas, matriz y medición; faltan formación general y legal; controles aplicables por conciliar antes de habilitar |
| Capacidad liberada en 12 meses | 62 (28-105) | ≥ φ_gobierno × 62 | ≥ φ_piloto × 62 |
| Neto 12 m (ROI) | −332 (−84%) | −161 a −99 (−100% a −62%) | −47 a +15 (−100% a +32%) |
| Señal de valor y gate | Antecedente: throughput por límite inferior en el mes 6 (+3%) y en el mes 9 (+8%); hoy rige el gate de valor del Anexo B (valor solo en el mes 9, peor caso mayor que 0). Caso de referencia y prueba de portabilidad en el mes 6 | El mismo throughput en los meses 6 y 9; adopción | El mismo throughput en los meses 6 y 9, en la cohorte |
| Abandono | Regla vigente: daño de calidad o caída demostrada en el mes 6; estimado < +5% o daño en el mes 9, o espera vencida | Las mismas | Las mismas; además, si la matriz no habilita repositorios para 15 activas |

**φ es la fracción de la ganancia g que se logra sin plataforma ni contractor, y
no tiene dato:** se muestran sus extremos, 0 y 1. Con la lectura de horas evitadas, la capacidad
es al menos φ × 62. Aporte marginal de cada pieza, cualitativo porque no hay base
para cuantificarlo:

- **Formación:** mueve la adopción en toda la dotación; sobre el throughput de la
  cohorte actúa a través del uso.
- **Prácticas sobre el agente existente:** son el mecanismo de g según la
  [fuente de ganancia](../../context/supuestos/ganancia-de-productividad.md)
  ("contrato de agente, skills y compuertas de calidad"), no el gateway. Las
  compra el piloto acotado y las mide la prueba chica de los meses 1-3 (abajo).
- **Plataforma y contractor:** no tienen un mecanismo directo de throughput en el
  año. Compran control y telemetría, la cobertura de precio si la prueba de los meses 4-6 la demuestra,
  el caso de referencia, evidencia técnica para un banco y la base del producto.
  Que las evals en CI bajen el retrabajo es una hipótesis sin dato.

**Sensibilidad algebraica, sin recomendación por ranking.** Los netos publicados
no demuestran que 47 o 161 compren la misma cobertura que 394. La relación
47/62 ≈76% solo indica qué fracción de capacidad cubriría aquel costo parcial;
no prueba repago de un piloto habilitado con todos sus controles. El diferencial
233 tampoco es todavía el precio incremental de una decisión equivalente.
Las siguientes cuentas muestran qué habría que medir si se homogeneizaran los
alcances; no justifican hoy financiar ese diferencial:

- **Precio:** cubrir 233 exige **90,3% ponderado de todo el gasto elegible**
  a 12×: fc×s = 233/(12×21,5) = 0,9031; a 6×, más del 100%.
  No es reducción solo del tráfico enrutable: si fc≤0,9, ni s=100% alcanza.
- **Protección del ingreso:** se paga si baja en Δp la probabilidad de perder el
  ingreso protegido ("Cómo se lee la palanca de riesgo"). Lo juzga el board.
- **Producto:** la opción de un contrato en el mes 12, sin ingreso en el año.

Lo caro del paquete empieza en los meses 4-6: por eso la señal se lee en el mes 3, antes de gastar la plataforma.

### Prueba chica de los meses 1-3 (referencia de actividades)

El [Anexo F](06-roadmap-riesgo.md) ("Primeros 100 días") deja sin costear una
prueba desde la semana 5 con el agente de código actual
([supuesto](../../context/supuestos/alternativas-de-menor-alcance.md)):

| | Prueba chica, semanas 5-13 del plan |
|---|---|
| Qué es | Contrato de agente, skills y guía de revisión en la cohorte de equipos propios, sobre repositorios que la matriz habilite; el intermedio de Tecnología de los meses 1-3 es el vehículo |
| Caja | 0: no suma seats ni herramientas |
| Tiempo | ~6 (3-9): diseño de 40-80 h de tech lead (1,1-5,0), 2 champions al 10% durante 2 meses (1,2-3,0: 0,4 persona-mes × 3,0-7,5) y lectura de 16-24 h de DevOps/QA (0,3-1,1) |
| Capacidad | +0,17 FTE clave (los meses 1-3 pasan de 1,6 a ~1,8: 0,80× del máximo) y +64 h distribuidas; techo de tiempo de los meses 1-3 de 62 a 72 (62 + 9,1, al entero superior) |
| Qué aprende | Si las prácticas mueven uso, retrabajo y PR aceptados, y la dispersión σ del cambio entre personas, el dato que decide si la lectura del mes 6 puede discriminar +3% |
| Gate | Se lee en el mes 3, sin atribuir ganancia (la rampa de los meses 1-3 es 0%) y sin poder de corte |
| Abandono | Se suspende si sube el retrabajo o los incidentes contra la base congelada, o si la matriz no habilita repositorios para la cohorte |

**Secuencia condicionada a la base.** Si se congela en semana 4, básico,
intermedio y prueba arrancan desde semana 5; si se extiende hasta semana 8,
los tres se desplazan a semana 9 y se revisa completitud M3. Lo que no despeja es la
atribución: con 15-20 personas y σ sin dato, su efecto no se separa del de la
formación. Eso la vuelve aprendizaje, no valor, pero no la impide. Va en la aprobación del paquete completo (alternativa), no en la autorización de la validación actual de 8k USD.

**Tarifa de las 64 h: una sola, la de rol** (≈ 19-47 USD/h). Son horas de dos
desarrolladores senior ([costo por rol](../../context/supuestos/costo-cargado-por-rol.md)),
no capacitación masiva: los 10-35 USD/h del Anexo D son un piso para la dotación entera
(darían 0,6-2,2 y un techo de 71). El Anexo D costea así sus champions: es sesgo del Anexo D.

### Recomendación de Finanzas con paquete completo (alternativa)

**No es el pedido inicial: lo es el mínimo.** Se conserva
para comparar alcances; una señal habilita evaluar inversión, no demuestra repago.
La restricción de C incluye prohibición o condicionamiento: una prohibición pura
excluye el uso y no libera plataforma. Rige la regla del Directorio: una señal
más cuatro condiciones (brecha documentada, alternativas comparables, economía
incremental o pérdida de aprendizaje aceptada y capacidad demostrada); dictamina
el AI Council y libera el Directorio; si falta una, sigue el mínimo
([R-15](07-resoluciones.md#arquitectura-y-medición)). Se conservan relecturas M6/M9 dentro del año.

**Escenario del paquete completo, no autorización vigente.** Los dos recorridos
siguientes reconstruyen su bifurcación histórica. No se recomienda elegir entre
400 y 199 por su total: compran alcances distintos. Antes de solicitar cualquiera,
se requiere comparación del gasto futuro evitable desde el mismo gate y nuevo
costeo; hoy rigen las dos autorizaciones del mínimo.

- **La decisión del mes 3 libera la plataforma de los meses 4-6** (contractor al 100%, gateway, pasarela) solo
  con al menos una señal para evaluar lo que el gobierno mínimo y formación no compra: restricción o licencia
  para vender según el [umbral contractual](../../context/supuestos/umbral-de-evidencia-contractual.md)
  (prohibición o condicionamiento; la prohibición pura excluye uso y no libera plataforma),
  anuncio del proveedor de pasar a consumo, o señal de cliente para el producto.
  Año de esta rama: ≈ **400** (216-584), el paquete más la prueba.
- **Sin ninguna, los meses 4-12 corren como gobierno mínimo y formación, con la prueba extendida al piloto acotado:** ≈ **199**
  en el año (la preparación previa y los meses 1-3 del paquete 69, prueba 6, los meses 4-12 del gobierno mínimo y formación ~114, cierre del
  contractor 4, compensatorios del Anexo C ~6; medio sin rango propio): caja ≈ 39 (meses 1-3:
  22,6, cierre 4 y legal de los meses 4-6 más telemetría del gobierno mínimo y formación, ~12 con contingencia) y
  tiempo ≈ 160. La extensión usa champions e intermedio que el gobierno mínimo y formación ya paga
  ([supuesto](../../context/supuestos/alternativas-de-menor-alcance.md)), pero no
  los controles compensatorios que el Anexo C exige para aceptar el residual del riesgo de datos de cliente en un modelo externo, el de inyección indirecta de prompts y el de fuga de secretos
  ([Anexo C](03-gobierno-seguridad.md), "Controles según la decisión del mes 3"): tiempo sin caja, hasta 1,9-9,4 según el Anexo C
  (cota superior; usamos el medio, 5,6). Sin ellos la prueba no se extiende.
  No es un corte: difiere la plataforma, y las lecturas de los meses 6 y 9 releen las señales, a costa de
  demorar el caso de referencia y la prueba de portabilidad.

En el paquete completo, cortar en el mes 3 cuesta 79 en el medio (coincide por azar con el techo de 79 del mínimo; son cifras distintas), hasta 115 hasta cerrar y 156 en el año, contra
un año completo de hasta 255 de caja y 320 de tiempo: esa es la reversibilidad.
Quedan descartados aprobar el año completo (compromete la caja con un caso que no
cierra) y el producto desde el mes 4 (gasta 37 de caja y 55 de tiempo antes de la señal).

### Pedido inicial: paquete mínimo

**Problema y recomendación.** Tres frentes con justificación distinta y una sola
respuesta mínima.

- **Protección.** Hay usos de IA en curso sin controles probados por superficie
  y sin matriz de restricciones de clientes. Cada control de este tramo se
  vincula a una restricción contractual, a un riesgo identificado o a una
  necesidad de evidencia concreta, y se prueba antes de habilitar el uso; los
  que no puedan hacerlo se reducen o se excluyen junto con el uso que los
  motiva. No se presupuesta beneficio por este frente.
- **Eficiencia.** El valor incremental no está medido: hay uso y hay gasto, sin
  una base contra la cual compararlos. Lo que se compra es la medición, no la
  mejora: la rampa de los meses 1-3 es 0% y el tramo no promete atribución.
  Produce la medición Tecnología, la verifica el verificador senior
  independiente, fuera de la línea de Tecnología; lee el AI Council en los meses
  6 y 9 y convierte el CFO: la capacidad cuenta como beneficio solo si en el mes 6 hay un destino
  decidido; si no, es 0 ([R-19](07-resoluciones.md#arquitectura-y-medición)).
- **Crecimiento.** No se compra en este tramo y no se amplía el alcance. Es una
  opción no costeada, con ingreso nuevo 0 hasta un contrato firmado. El
  descubrimiento de integración ya costeado en la continuación condicional
  (meses 4-6) es la única actividad comercial prevista: lo lidera Producto y
  Comercial gestiona la señal sin costo propio. Ampliarla con alcance costeado lo
  decide el Directorio en el gate del mes 6; sin señal escrita en ese gate, la
  oportunidad se archiva ([R-31](07-resoluciones.md#roadmap-y-comercial)).

La respuesta mínima es común a los tres: configuración, controles probados y
medición sobre herramientas existentes, sin plataforma central. Fuente de
**todos los supuestos del mínimo**, conciliaciones y límites:
[paquete mínimo de aprendizaje](../../context/supuestos/paquete-minimo-de-aprendizaje.md).
No son precios cotizados ni disponibilidad humana demostrada.

**Validación temprana: qué cubre la preparación y qué no.** La preparación
técnica previa de 20-40 h (techo 3) ya tiene contenido asignado: 4-8 h de
viabilidad técnica y 8-16 h de extracción e historial del
[Anexo B](02-arquitectura.md), más 8-16 h de preparación de facilitación del
[Anexo D](04-personas-cultura.md). Esas horas **no cubren** la validación
organizativa que el hito necesita: completar la matriz de capacidad, designar al
verificador independiente que exige el [Anexo C](03-gobierno-seguridad.md) y
cotizar el dictamen legal con alcance acordado. Completar la matriz no estaba
costeado en ningún anexo.

Por eso **el hito no se afirma contenido en el techo anterior de 74**: se
recosteó como primera liberación acotada («Primera autorización») con 60-96 h
organizativas adicionales (techo 5), y el acumulado pasó a 79. Personas confirma
las 60-96 h como estimación de planificación y las contrasta el día 2 de la
ventana con una prueba de una hora sobre un área; si no entran, el día 3 se
reduce el detalle o se recostea dentro del techo 5, y si lo exceden la ventana
se detiene y vuelve al Directorio ([R-24](07-resoluciones.md#personas)).
**No consta ejecución previa de la preparación:** se autoriza como nueva. La
aprueba el Directorio al aprobar el plan; produce el CAIO y verifica el CFO.
Arranca cuando Operaciones y los managers confirman agendas e imputación 2026 y
el Responsable de Tecnología confirma el acceso a las fuentes; sin eso la ventana
no empieza y M1 no arranca ([R-02](07-resoluciones.md#autoridad-y-liberaciones)).
La liberación del resto del tramo no es automática por aprobar la validación.

**Entregables M1-M3.** Política/intake con estado actualizado, matriz de restricciones,
inventario y legal focalizado; permisos/MCP/escaneo y pruebas por superficie,
críticos cerrados y residual aceptado; padrón y extracción reproducible de
PR/CI/reversiones/tickets/incidentes, calidad y base congelada; básico para toda
la organización, intermedio de 15-20 personas y prueba de prácticas sobre el agente.
Uso, cobertura y faltantes se informan separados de resultados.

No incluye gateway, retrieval, harness central, evals en CI de plataforma,
producto, avanzado ni contractor continuo. Controles equivalentes significa
mismo requisito y prueba para el mismo uso habilitado; no equivalencia con una
plataforma de producto. Si lo existente no cumple, excluir/suspender ese uso.

**Conciliación por actividad y rol.** k USD; rangos de horas y costo,
sin preparación. Formación distribuida a 10-35 USD/h, según el piso de D;
soporte al costo mensual de su rol/160. No se usan tarifas facturables.

| Rol / actividad | Horas M1-M3 | FTE internos (h/480) | Tiempo a costo cargado |
|---|---|---|---|
| Tech lead / arquitectura / líder / facilitación / managers | 146-272 | 0,304-0,567 | 4,10625-17,0 |
| DevOps productor | 44-72 | 0,092-0,150 | 0,825-3,375 |
| QA / datos | 48-72 | 0,100-0,150 | 0,9-3,375 |
| IA aplicada interna | 8-16 | 0,017-0,033 | 0,225-1,1 |
| Seguridad verificadora, distinta persona del productor | 34-54 | 0,071-0,113 | 0,6375-2,53125 |
| Seniors de soporte de prácticas | 64 | 0,133 | 1,2-3,0 |
| Analista funcional | 60-96 | 0,125-0,200 | 0,75-3,3 |
| Staff | 26-40 | 0,054-0,083 | 0,24375-1,25 |
| **Soporte clave total** | **430-686** | **0,8958-1,4292** | **8,8875-34,93125** |
| Básico, 60-70 × 6 h | 360-420 | 0,750-0,875 | 3,6-14,7 |
| Intermedio, cohorte 15-20 × 12 h | 180-240 | 0,375-0,500 | 1,8-8,4 |
| **Distribuido total** | **540-660** | **1,125-1,375** | **5,4-23,1** |
| **Total interno M1-M3** | **970-1.346** | **2,0208-2,8042** | **14,2875-58,03125** |

A esta demanda de actividades se suma, declarada aparte, la verificación de la
lectura del mes 3 (4-5 h, 0,075-0,234375, del margen de 34 h): total
974-1.351 h y 14,3625-58,265625 de tiempo, debajo de 59 («Continuación
condicional», más abajo).

Referencia de planificación: 1.158/480 = **2,4125 FTE internos**,
1,1625 clave + 1,25 distribuido; no reemplaza reservar máximos por rol.
Sin capacidad demostrada no se inicia la actividad. No hereda el piso de ~1,8
clave ni el contractor del paquete completo. Ambas bolsas se concilian sobre
las mismas personas en la matriz privada de D; no hay ganancias futuras para pagarlas.

**Reserva propuesta de capacidad:** hasta **720 h / 1,5 FTE de soporte clave**,
más **540-660 h de formación**; máximo combinado **1.380 h / 2,875 FTE de
costeo**, sin preparación ni cierre condicional.

Es un supuesto para solicitar agendas, según la [fuente del mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md#reserva-propuesta-de-capacidad-m1-m3).
La demanda costeada es 970-1.346 h, con el tech lead de gobierno en 22-32 h
([R-25](07-resoluciones.md#finanzas)). Las 34 h de margen sobre las 686 h
de soporte máximo no representan ejecución ni reserva financiera adicional.

El margen no tiene actividad ni rol costeado; usarlo requiere estimación y
autorización previa. Si no cabe en el techo de tiempo de 59, reducir o
resecuenciar, o elevar un recosteo. Los techos de caja, tiempo y salida se mantienen.

Solapes adoptados por el Directorio ([R-26](07-resoluciones.md#finanzas)):
QA B contiene D 8-16; seniors 64 contienen B 16-24; la matriz de seguridad entra
en las 24-40 h de B, con Seguridad que verifica y no produce los compensatorios.
DevOps 40-64 h (unión de B 32-56 y C 40-64, más inventario 4-8) es el tope de
configuración, prueba, corrección y exportaciones: un límite de alcance, no un
ahorro. Las 8-16 h de managers cubren solo la actualización semanal de agendas;
la validación inicial de agendas se imputa en la primera liberación. Confirman
el desglose el Responsable de Tecnología y el Responsable de seguridad durante
la validación, antes de la segunda liberación.

**Si DevOps no entra en el tope.** Las exportaciones se reportan como uso
estimado, sin sumar horas; si aun así no entra, el CFO recostea antes de M1
dentro de 71 y firma el CEO; superar 71 vuelve al Directorio; el techo de 59 no
sube. Sensibilidad de referencia: sin la unión, DevOps pasaría de
44-72 a 76-128 h: agrega 32-56 h y 600-2.625 USD de tiempo, a costo de su rol.
La demanda total sería 1.002-1.402 h y 14,8875-60,65625 de tiempo:
el máximo excede el techo de 59. Es una sensibilidad, no el presupuesto
elegido: por eso rige el tope y no la suma.
Derivación: [actividades del mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md#alcance-y-conciliación-m1-m3)
y [costo por rol](../../context/supuestos/costo-cargado-por-rol.md).

Seguridad B 24-40 puede reutilizarse para matriz y pruebas de C solo con
confirmación de alcance. Política C 4-8 no está en B y se suma aparte,
más Council 6: Seguridad provisional 34-54 h.

Diseño de prueba 40-80 y lectura 16-24 de E se incluyen una vez.
Council ya está repartido: TL 12, Seguridad 6,
staff 12. No sumar porcentajes anuales de C/D sobre estas mismas tareas.

#### Primera autorización: validación inicial previa a M1

**10 días hábiles** dentro de octubre-diciembre de 2026. La primera liberación
(caja 0, tiempo hasta 8) la aprueba el Directorio al aprobar el plan; produce el
CAIO y verifica el CFO ([R-02](07-resoluciones.md#autoridad-y-liberaciones)).

Antes de trabajar, Operaciones y los managers confirman agendas, trabajo
desplazado e imputación 2026, y el Responsable de Tecnología confirma el acceso a
las fuentes. Sin esas condiciones, la ventana no comienza y M1 no arranca.

**Validación organizativa adicional.** Supuestos nuevos de horas-persona,
incluidos entrevistadores, entrevistados, managers y autoridad que decide.
Tarifas de la [fuente de costo por rol](../../context/supuestos/costo-cargado-por-rol.md)/160:

| Rol | Horas adicionales | USD/h, supuesto | Tiempo, k USD |
|---|---|---|---|
| TL, coordinación, managers y autoridad de decisión | 16-24 | 28,125-62,5 | 0,45-1,5 |
| Analista funcional | 20-32 | 12,5-34,375 | 0,25-1,1 |
| Staff de Operaciones, Personas, Comercial y Finanzas | 16-24 | 9,375-31,25 | 0,15-0,75 |
| Senior verificador independiente | 8-16 | 18,75-46,875 | 0,15-0,75 |
| **Total organizativo adicional** | **60-96** | Por rol | **1-4,1; techo 5** |

La autoridad se costea provisoriamente en TL/staff según la tarea; no describe
su remuneración real. El verificador es otra persona que quien produce el
entregable revisado. Si el rol o su costo no encajan, se vuelve a costear.

| Actividad | TL | Analista | Staff | Verificador | Total, h |
|---|---|---|---|---|---|
| Entrevistas y contraste del diagnóstico | 4-8 | 4-6 | 8-12 | — | 16-26 |
| Conciliación del padrón y matriz persona/semana | 4 | 8-14 | 4-6 | — | 16-24 |
| Estado de políticas, restricciones y separación de funciones | 4-6 | 4-6 | 2 | 4-8 | 14-22 |
| Conciliación económica, solapes y trabajo desplazado | 2 | 4-6 | 2-4 | — | 8-12 |
| Verificación, decisión y cierre documental | 2-4 | — | — | 4-8 | 6-12 |
| **Total, h** | **16-24** | **20-32** | **16-24** | **8-16** | **60-96** |

Alcance supuesto: 4-6 entrevistas de una hora y una ronda de contraste sobre
documentos existentes. El total incluye el tiempo de todos los participantes;
no compra entrevistas individuales a toda la organización ni implementación.

Entregables: diagnóstico contrastado con faltantes visibles; padrón conciliado;
matriz privada persona/semana de capacidad, formación y trabajo desplazado;
productor, verificador independiente y autoridades identificados por entregable.

También: estado actual de políticas y restricciones, viabilidad técnica y de
medición, solapes B/C/D confirmados o rechazados, recosteo y acta de continuar,
reducir/resecuenciar o detener. Productor, verificador y firmante se separan por
rol; las personas que ocupan cada rol se nombran en el acta de la liberación que
habilita el entregable ([R-06](07-resoluciones.md#autoridad-y-liberaciones)).

Todo el trabajo organizativo se trata como adicional. Una equivalencia confirmada
por B/C/D se descuenta una sola vez de la ejecución posterior; no se presume
absorbida en 59 de tiempo, 720 h de soporte ni las 34 h de margen M1-M3.

**Preparación técnica existente, separada y sin ejecución registrada:** TL
12-24 h y QA 8-16 h, total **20-40 h / 0,4875-2,25k USD; techo 3**. Ya se
extrajo de B/D en la tabla M1-M3; no se vuelve a sumar allí.

La primera liberación reúne **80-136 h / 1,4875-6,35k USD calculados**, con
**caja 0 / tiempo hasta 8** por suma de techos 5+3. Requiere agenda propia
pre-M1; el tiempo existente no representa nueva nómina ni caja incremental.

Incluye reconstrucción retrospectiva y preparación sobre fuentes existentes;
no habilita formación, prácticas, herramientas nuevas, despliegues ni contratos.
La base prospectiva sigue en semanas 1-4 de M1; no se adelanta a esta ventana.

Durante la ventana se prepara el alcance y se solicita cotización del dictamen
legal, sin contratarlo. No se supone cotización gratuita: si el proveedor cobra,
se pide autorización previa y se vuelve a costear antes de comprometerse.

**Corte previo a M1.** Si no resulta viable, no se libera la segunda etapa.
La exposición es el tiempo efectivamente ejecutado, **hasta 8**, y caja 0.
El cierre documental ya está incluido en la validación.

No se activa el cierre técnico 16-24 h reservado para M1-M3: esta etapa no
instala herramientas ni asume contratos nuevos. Cualquier obligación distinta
invalida ese supuesto y exige costear su cierre antes de comprometerla.

Diez días son una ventana propuesta, no disponibilidad demostrada. Más entrevistas,
participantes o rondas, fuentes no exportables, instrumentación nueva, ausencia de
verificador o costos fuera del rango exigen reducir/resecuenciar o recostear.

#### Segunda autorización: inicio M1-M3 y reservas de salida

Antes de M1, el CEO firma la segunda liberación por delegación del Directorio,
con dictamen del AI Council; el CAIO produce el paquete y el CFO verifica costo,
caja, reservas, presupuesto 2027 y contribución desplazada. El acta acepta
diagnóstico y padrón, la matriz de capacidad validada por Operaciones/managers,
el acta de viabilidad con método ratificado, los nombres de productor,
verificador y firmante, los solapes conciliados y el recosteo
([R-05](07-resoluciones.md#autoridad-y-liberaciones)). La capacidad se lee con
sobre separado: la reserva de soporte clave (hasta 720 h) y la de formación
(540-660 h) se confirman por separado.

El acta resuelve continuar, reducir/resecuenciar o detener; un bloqueante abierto
no es conformidad. Sin acta, M1-M3 no arranca y la exposición queda en lo
ejecutado de la primera liberación (hasta 8). Un recosteo dentro de 71 lo firma
el CEO; uno que supere 71 vuelve al Directorio.

**Formación vigente:** básico de 6 h e intermedio de 12 h (540-660 h). Si la
matriz no confirma esas horas, Personas propone reducir o resecuenciar, el CFO
verifica y el CEO lo firma en la segunda liberación dentro del techo de 59; el
módulo de uso seguro no se recorta ([R-21](07-resoluciones.md#personas)).

La segunda liberación permite iniciar base y controles con herramientas
existentes. No habilita prácticas automáticamente: requieren base congelada,
dictamen aplicable, controles probados, verificación y aceptación del residual.

**Caja M1-M3:** legal focalizado **2-6** (C: 8-16 h externas × 250-375 USD/h)
y provisión para herramientas/exportación **0-1,5**, más 15%: **2,3-8,625;
techo 9**. No incluye seats nuevos ni contractor. La provisión no acredita precio
ni necesidad de compra; si el costo real no entra, reducir o volver a costear antes de usar.
Legal externo no se cuenta también como tiempo interno.

**Reservas de salida:** caja **1**, por hasta un mes de herramientas (máximo
0,5, redondeado arriba); legal por hitos sin preaviso. Cierre interno 16-24 h
de senior para exportar/revocar/archivar: 0,3-1,125, **reserva de tiempo 2**.
Si la contratación exige más preaviso, ampliar reserva antes de comprometer.
Son autorizaciones contingentes, no gasto ni doble contingencia del 15%.

El dictamen legal íntegro permanece en M1-M3, sujeto a alcance y cotización;
no se cuenta como ejecutado ni se suma de nuevo a la validación previa.

**Segunda liberación, condicionada y no autorizada ahora:** **caja 9 + reserva
1 = 10**; **tiempo M1-M3 59 + reserva de cierre 2 = 61**; total **71**,
que es también **68 operativos (9 + 59) + 3 de reservas (1 + 2)**.
Es disjunta de la primera liberación 8: **8 + 71 = 79 acumulados**.

**Estimado contra techo hasta el mes 3.** El costo calculado hasta cerrar M3,
sin reservas ni núcleo, es **18-73**: tiempo M1-M3 14,3625-58,265625 (con la
verificación de la lectura del mes 3) + caja 2,3-8,625 + validación previa
1,4875-6,35 = 18,15-73,240625. El techo es **79**:
la diferencia son las reservas contingentes (3) y el redondeo hacia arriba de
cada techo.

**Conciliación del techo vigente:** 74 + 5 organizativos adicionales = **79**;
**caja 10 / tiempo 69 = 59 + 3 + 5 + 2**. Preparación técnica 3, legal y
cierre ya estaban costeados; solo la validación organizativa agrega 5 al techo.

El techo de caja 10 requiere facturación anual de al menos 334k USD al 3%
o 1 millón al 1%; quien tiene acceso verifica presupuesto 2027 en privado.

**Exposición presupuestaria máxima autorizada del tramo (M3):** si nada demuestra
valor y se abandona la prueba, el límite propuesto hasta cerrar llega a
**79 = 10 de caja + 69 de tiempo**, sin deducir ganancias. **No equivale a una
pérdida económica incremental ni a una salida de caja de ese monto:** el
desembolso de caja modelado es 2,3-8,6 (techo 9; la reserva de caja de 1 es
contingente) y el resto es tiempo valorizado de personas que ya están en la
organización. Núcleo posterior M4-M12: **108 h**, 36 por tramo
(TL 12 + Seguridad 12 + staff 12), **caja 0 / tiempo hasta 6** (2 por tramo).

Se ocupa de accesos, incidentes y permisos; no mantiene el experimento ni habilita
usos sin controles. El máximo del año con corte M3 es **85 = 79+6**.

Los **6 de núcleo requieren aprobación explícita en el gate de salida M3**: la
firma el CEO dentro de 85, con verificación del CFO ([R-03](07-resoluciones.md#autoridad-y-liberaciones)).
No forman parte del límite acumulado de 79 ni de las dos liberaciones. Si no hay capacidad, suspender
usos afectados hasta cubrir obligaciones. No suma a la continuación de abajo.

**Cadencia del Council tras un corte (supuesto de costeo).** Las 36 h por tramo
incluyen una sola sesión del AI Council por tramo, de 2 h con sus cinco asientos
(TL 4 h, Seguridad 2 h, staff 4 h, a máximo 0,47), y no la cadencia mensual.
La mensual no entra: 30 h de Council a máximo cuestan 1,41 y, sumadas al núcleo
(1,6875), dan 3,09 contra el techo de 2 por tramo. Quién supervisa el núcleo y
quién lo pausa lo fija el [Anexo C](03-gobierno-seguridad.md); si fija otra
cadencia, se recostea antes del gate de salida, y si no entra en el techo,
vuelve al Directorio.

**Continuación condicional sin plataforma (no aprobada hoy).** Supuestos de
operación del paquete mínimo, sin sumar fracciones del paquete completo:

| Rol | Horas por tramo M4-M12 | Descubrimiento adicional, solo M4-M6 |
|---|---|---|
| Tech lead / líder interno (oficina del CAIO); incluye 14-24 h de la oficina del CAIO | 36-60 | 8-16 |
| DevOps | 8-16 | — |
| QA / datos | 32-48 | — |
| IA aplicada | 4-8 | — |
| Seguridad | 12-20 | — |
| Senior | 16-24 | 8-16 |
| Analista funcional | 8-16 | 16-24 |
| Staff | 12-20 | 4-8 |
| Personas: comunicación del cambio, frenos y agendas | 4-6 | — |
| **Subtotal de mantenimiento** | **132-218 h / 0,275-0,454 FTE** | **36-64 h / 0,075-0,133 FTE** |
| Verificador senior independiente: reproduce los indicadores de la lectura del gate (y de la relectura de la espera, si la hay) | 4-5 | — |
| **Total interno** | **136-223 h / 0,283-0,465 FTE** | **36-64 h / 0,075-0,133 FTE** |

Mantiene controles/prácticas, seguimiento y lectura; no hay nuevas cohortes,
avanzado ni formación general adicional presupuestada. El descubrimiento antes
de M6 observa integración con documentación/soporte actuales, tiempo a primera
integración exitosa y consultas por intento; no compra construcción de producto.
Si hacen falta cambios legales, conectores o más soporte, se vuelve a costear.
La caja de 0-1,5 por tramo, más 15%, es una provisión única para herramientas o
consulta legal puntual (abajo).

| Tramo condicional | Caja calculada / techo | Tiempo calculado / techo | FTE internos totales |
|---|---|---|---|
| M4-M6, con descubrimiento | 0-1,725 / **2** | 3,3375-13,784375 / **14** | 172-287 h / 480 = **0,358-0,598** |
| M7-M9 | 0-1,725 / **2** | 2,725-10,959375 / **11** | 136-223 h / 480 = **0,283-0,465** |
| M10-M12 | 0-1,725 / **2** | 2,725-10,959375 / **11** | **0,283-0,465** |

Cuenta de las dos filas nuevas, por tramo: Personas 4-6 h × 9,375-31,25 USD/h =
0,0375-0,1875; verificador 4-5 h × 18,75-46,875 USD/h = 0,075-0,234375. M4-M6
pasa de 3,225-13,3625 a 3,3375-13,784375 y M7-M9 y M10-M12, de 2,6125-10,5375 a
2,725-10,959375. Todos quedan debajo de su techo, con holgura de 0,215625 en
M4-M6 y de 0,040625 en los otros dos; ningún techo cambia. El verificador a 6 h
por tramo no entraría: 10,5375 + 0,1875 + 0,28125 = 11,00625 contra 11.

**Verificador en la lectura del mes 3.** Reproduce los indicadores de M3 en 4-5 h
(0,075-0,234375), que son el primer uso del margen de 34 h sobre la reserva de
soporte clave: el soporte pasa a 434-691 h (margen de 29-30 h), el total M1-M3 a
974-1.351 h y el tiempo calculado a 14,3625-58,265625, debajo de 59. La demanda de
actividades de [R-25](07-resoluciones.md#finanzas) (970-1.346 h) no cambia; la
verificación se suma aparte y declarada.

Proyección de continuar el mínimo todo el año, sin esperas: **≈71 (27-114)
económicos**, rango calculado **26,9375-114,11875**: caja 2,3-13,8 y tiempo
con preparación técnica y validación organizativa 24,6375-100,31875
(14,3625 + 1,4875 + 3,3375 + 2 × 2,725 = 24,6375; 58,265625 + 6,35 + 13,784375 +
2 × 10,959375 = 100,31875). Medio 70,53, que redondea a 71; incluye el verificador y la fila de Personas.

**Techos por tramo ([R-03 y R-04](07-resoluciones.md#autoridad-y-liberaciones)).**
El Directorio los fija hoy al aprobar el plan, sin liberarlos; el CEO firma cada
gate dentro del techo de su tramo:

| Hasta | Techo del tramo, caja + tiempo | Acumulado |
|---|---|---|
| Cerrar M3 (preparación 8, M1-M3 68 y reservas 3) | — | **79** |
| M4-M6, con descubrimiento | 2 + 14 = **16** | 95 |
| M7-M9 | 2 + 11 = **13** | 108 |
| M10-M12 | 2 + 11 = **13** | **121** |

Suma de techos por tramo y preparación: **118 = caja 15 (9 + 2 + 2 + 2) + tiempo
103 (8 + 59 + 14 + 11 + 11)**, sin gastar reservas; con las reservas de salida
(1 + 2), **121**. El adicional organizativo es 1-4,1 calculado y techo 5; no se
altera la caja ni la ejecución M1-M3. Dentro de cada tramo, caja y tiempo no se
compensan entre sí. Superar el techo de un tramo, aunque el acumulado quede
debajo de 121, vuelve al Directorio.

#### Oficina del CAIO, líder, cambio y legal después de M1: dónde se costean

Ninguna de estas líneas sube un techo. La holgura que queda entre el máximo
calculado y el techo es chica: tiempo 0,734375 en M1-M3, 0,215625 en M4-M6 y
0,040625 en M7-M9 y M10-M12; caja 0,375 en M1-M3 y 0,275 por tramo después. Por
eso cada línea se absorbe en una fila declarada o queda fuera, con la cuenta:

| Línea | Dónde se costea | Cuenta | Si no entra |
|---|---|---|---|
| Oficina del CAIO | El CAIO es un rol existente reasignado, sin contratación ni caja. Su dedicación al mínimo es la del líder interno: M1-M3, 48-96 h (10%-20% de 480) dentro de la fila «Tech lead / arquitectura / líder», donde produce los paquetes de liberación y de gate y aprueba el instrumento del básico; M4-M12, dentro de las 36-60 h por tramo de «Tech lead / líder interno» (7,5%-12,5%) | Ya incluida en 58,265625 y en 13,784375 / 10,959375; en M4-M12, 14-24 de las 36-60 h son de la oficina del CAIO | Si el CAIO es otra persona que el líder, sus horas no están costeadas: la holgura de M1-M3 da 11 h a 62,5 USD/h. Más que eso se recostea; si supera el techo del tramo, vuelve al Directorio |
| Líder interno M4-M12 | Absorbido en las 36-60 h por tramo de la fila del tech lead: coordina, sigue agendas y produce el paquete del gate. No hay cohortes nuevas | Una fila propia al 20% (96 h) costaría 2,7-6,0 por tramo: M4-M6 13,784375 + 6,0 = 19,78 contra 14; M7-M9 10,959375 + 6,0 = 16,96 contra 11. **No entra** | El 20% de 12 meses es del paquete completo; pedirlo en el mínimo vuelve al Directorio |
| Cambio M4-M12 | Fila nueva de Personas, 4-6 h por tramo: comunicación de cada gate, seguimiento de frenos y de la postura sobre el empleo, agendas | 0,0375-0,1875 por tramo; **entra** (ver la tabla de tramos) | Un programa de cambio mayor que este es alcance ampliado: lo decide el Directorio |
| Verificador de los indicadores en M3, M6, M9 y M12 ([Anexo B](02-arquitectura.md)) | Fila propia: 4-5 h por lectura en M3 (margen de 34 h) y 4-5 h por tramo después, que en M10-M12 cubren también la relectura de la espera del mes 9 | M1-M3 0,075-0,234375; cada tramo 0,075-0,234375; **entra**, con las holguras de arriba | Más horas por lectura no entran en M7-M12 (a 6 h, 11,00625 contra 11): se reduce el alcance de la reproducción o vuelve al Directorio |
| Aprobación del tratamiento de eventos de uso en la preparación ([R-13](07-resoluciones.md#gobierno-y-seguridad)) | 2-4 h del Responsable de seguridad, como «autoridad de decisión» dentro de las 16-24 h de esa fila de la validación organizativa (actividad «Estado de políticas, restricciones y separación de funciones»). La regla por defecto, agregados por área, no necesita dictamen legal ([Anexo C](03-gobierno-seguridad.md)) | 2-4 h × 18,75-46,875 = 0,0375-0,1875, a una tarifa no mayor que la de TL con que se costea esa fila | Si la fila no las absorbe, entran en la holgura del techo 5 (5 − 4,1 = 0,9: 19 h a 46,875 USD/h); el techo de 8 no cambia |
| Legal externo M4-M12 ([Anexo C](03-gobierno-seguridad.md), «Legal externo después de M1») | La provisión de caja del tramo (0-1,5 + 15%) es única para herramientas o consulta legal, con las consultas y disparadores del cuadro de C. Si legal es condición para un uso, tiene prioridad sobre herramientas | Techo 2 / 1,15 = 1,74 antes de contingencia: 4,6 h a 375 USD/h o 7,0 h a 250. C publica 5,3-8 h (2.000 / 375 a 2.000 / 250) sin descontar la contingencia de 15%, que rige toda la caja. Herramientas 1,5 + legal 4 h a 375 = 3,0 × 1,15 = 3,45 contra 2: **las dos al máximo no entran** | Lo que no entra se recostea dentro del techo del tramo, o vuelve al Directorio. Quedan fuera la revisión normativa completa y un dictamen nuevo: son alcance ampliado ([R-28](07-resoluciones.md#finanzas)) |
| Asesoría laboral sobre la postura de empleo ([R-20](07-resoluciones.md#personas)) | Dos opciones: (a) 2-4 h dentro de las 8-16 h del dictamen legal de M1-M3, si su cotización deja ese espacio (el dictamen queda en 12-14 h como máximo); (b) fuera de 79, aprobada por el Directorio, como la facilitación externa ([R-22](07-resoluciones.md#personas)) | (a) no cambia la caja: el máximo sigue en 16 h × 375 = 6. (b) 2-4 h × 250-375 = 0,5-1,5; con 15%, 0,575-1,725. Sumarla a 8,625 rompe 9: la holgura de caja (0,375) es menos de 1 h a 375 USD/h | Rige (a) si la cotización lo permite, la verifica el CFO y la firma el CEO en la segunda liberación; si no, (b). No va en la primera liberación: su caja es 0. La postura tiene costo incremental 0 ([R-20](07-resoluciones.md#personas)): con (a), la asesoría usa caja ya presupuestada; con (b), es caja aparte que decide el Directorio |

Una ampliación de alcance exige volver a costear antes de comprometer.
No es un presupuesto anual aprobado ni equiparable automáticamente a 47/161/394.
Los acumulados incluyen preparación imputada a 2026 más ejecución 2027;
no representan exclusivamente presupuesto 2027.

Con alcance y contratos constantes se mantienen reservas 1 de caja / 2 de
tiempo; cada gate las recalcula antes de asumir obligaciones nuevas.
Salidas sin plataforma, máximos por suma de techos, sin restar beneficio.
Las filas M3/M6/M9/M12 suponen corte inmediato al cierre del gate. Con el gate
de valor del [Anexo B](02-arquitectura.md) solo hay espera en el mes 9; se costea
por separado abajo, con aprobación explícita antes de iniciarla:

| Decisión de salida | Hasta cerrar, caja / tiempo → económico | Núcleo restante, h / techo de tiempo | Máximo económico del año con salida |
|---|---|---|---|
| Previo a M1 | 0 / 8 → **8** | — | **8**, sin inicio M1-M3 |
| M3 | 10 / 69 → **79** | 108 / 6 | **85** |
| M6: corte por daño de calidad, caída demostrada, adopción, costo o controles | 12 / 83 → **95** | 72 / 4 | **99** |
| M9 inmediato | 14 / 94 → **108** | 36 / 2 | **110** |
| Espera M9 vencida, corte tras 6 semanas | 15 / 100 → **115** | 18 / 1 | **116** |
| M12 | 16 / 105 → **121** | — | **121**, sin autorizar régimen posterior |

Estas exposiciones son límites propuestos, no costos ejecutados. La continuidad
y el núcleo se reemplazan en los tramos restantes; no se suman ambas ramas.
El núcleo restante requiere aprobación explícita en cada gate de salida.
No hay espera en el mes 6:
ese gate no espera por medición, porque seis semanas más no compran precisión
([Anexo B](02-arquitectura.md), «Gate de valor»).

**Antecedente del mínimo, sin validación organizativa:** 89 era el máximo de
corte inmediato M6 antes de corregir Seguridad; corregida, pasó a 90. El máximo
vigente es **95**, con techo adicional 5 de validación; no es una espera vencida.

**Subtramo de espera del mes 9, supuestos.** Una sola espera de seis semanas, en
M10-M12, sin expansión, producto ni nuevo descubrimiento.

La carga se estima por tareas: TL 18-30 h coordina y lee; DevOps 4-8 mantiene
configuración y exporta; QA 16-24 repite extracción, enlaces y cálculo.

IA 2-4 y seniors 8-12 sostienen prácticas congeladas; Seguridad 6-10 revisa
accesos/incidentes/residual; analista 4-8 concilia registros; staff 6-10
documenta decisión y permisos. La verificación de la relectura sale de la fila
del verificador del tramo.

La bolsa equivale a la mitad de las tareas trimestrales de mantenimiento:
**64-106 h**, costo **1,30625-5,26875**, techo **6** de tiempo.
Es un supuesto de carga, no una conversión de semanas calendario a meses.

Caja: herramientas 0-0,75 +15% = **0-0,8625**, techo **1**.
Si no alcanza para controles, muestra madura y relectura, cortar o volver a costear
antes de comprometer; no prorrogar ni atribuir ganancia con muestra insuficiente.

| Subtramo a aprobar | Actividades y horas | Caja / tiempo, techos del subtramo | Reserva de salida caja / tiempo | Pérdida acumulada al vencer y cortar, caja / tiempo → total |
|---|---|---|---|---|
| Espera del mes 9 | Controles, prácticas congeladas, nueva medición y lectura; 64-106 h | 1 / 6 | 1 / 2, vigentes y usadas una sola vez | 15 / 100 → **115**; con núcleo restante, **116** |

La espera **sustituye** la porción de continuidad de M10-M12 que utiliza; no se
agrega al trimestre completo 2/11 ni a un núcleo simultáneo. La reserva 1/2
cubre solo cierre: no financia medición y no se vuelve a sumar por esperar.

Después de la espera, el núcleo del trimestre parcial es TL 6 + Seguridad 6 +
staff 6 = **18 h**, costo **0,3375-0,84375**, techo **1** de tiempo y caja 0.

Es una distribución propuesta de tareas; validar la cadencia obligatoria
antes de aprobar el gate.

Si pasa la relectura, volver a costear y aprobar el resto del trimestre descontando
las actividades ya financiadas en la espera, sin sumar otra vez 136-223 h.

**La espera va dentro del techo de su tramo.** Sus techos 1 / 6 son subtopes del
techo de M10-M12 (2 / 11), no se suman a él. El resto del trimestre se recostea
contra lo que la espera calculó o ejecutó, no contra su techo redondeado. Cuenta:
espera 1,30625-5,26875 de tiempo + resto 1,41875-5,690625 = 2,725-10,959375,
debajo de 11; caja 0,8625 + 0,8625 = 1,725, debajo de 2. La fila de Personas no corre
durante la espera (sin expansión ni comunicación nueva); va en el resto del
tramo. Con esa regla, ningún camino supera el techo de su tramo ni 121:

| Camino | Hasta cerrar | Con núcleo restante | Cuenta |
|---|---|---|---|
| Sin espera, hasta M12 | 121 | — | 79 + 16 + 13 + 13 |
| Corte en el mes 6 | 95 | 99 | 79 + 16; núcleo M7-M12 2 + 2 |
| Corte inmediato en el mes 9 | 108 | 110 | 95 + 13; núcleo M10-M12 2 |
| Espera del mes 9 que vence y corta | 115 | 116 | 108 + 7; núcleo parcial 1. M10-M12 usa 7 + 1 = 8 de 13 |
| Espera del mes 9 que pasa, hasta M12 | 121 | — | M10-M12 dentro de 13 |

Si el recosteo del resto del tramo no entra en lo que queda de su techo, se
reduce el alcance o vuelve al Directorio; el CEO no firma un tramo por encima
de su techo aunque el acumulado quede debajo de 121.

Regla del Directorio ([R-27](07-resoluciones.md#finanzas)), con el gate de valor
del [Anexo B](02-arquitectura.md): una sola espera, en el mes 9, cuando el
estimado es ≥ +5% sin que el peor caso pase de 0; el AI Council recomienda
abrirla, el CFO verifica y el CEO firma el subtramo dentro del techo de su tramo.
Si al vencer no pasa valor/calidad con versión congelada, se corta el frente
interno, sin segunda espera; si otro frente sigue, aplicar la precedencia de F y
volver a costearlo. Los máximos de esta tabla son del mínimo sin plataforma ni producto.

**Beneficio de caja estimado: 0; ingreso nuevo: 0 en el modelo.** Capacidad
liberada: sin cifra hasta medir; no asignar automáticamente los 62 del paquete
completo. Para este presupuesto conservador sin beneficios cuantificados, ROI
económico modelado −100%, no resultado observado. Una misma hora no se suma
como capacidad evitada y venta; conciliar trabajo y contribución desplazados
sin sumar dos veces el mismo costo de oportunidad. Si la lectura del mes 9 pasa,
se acredita solo el peor caso, y lo convierte el CFO con destino decidido
([R-19](07-resoluciones.md#arquitectura-y-medición)).

**Lecturas M3/M6/M9/M12 ([Anexo B](02-arquitectura.md), «Gate de valor»).** M3
compra acta reproducible, cobertura, calidad, dispersiones y restricciones; no
promete atribución (rampa inicial cero). Básico/intermedio/prueba solo después
de congelar base: semana 5 o semana 9 si se extiende; revisar completitud M3.
M6 no lee valor: decide la continuidad de M7-M9 por adopción, calidad, costo y
controles, y corta solo por daño de calidad o caída demostrada del throughput
(límite superior menor que 0). M9 lee valor: pasa con peor caso mayor que 0 y
sin daño; espera con estimado ≥ +5% sin pasar; corta con estimado < +5% o daño.
M12 es insumo del año 2. Seguridad puede suspender antes de cualquier lectura
económica.

La opción de configurar/comprar/ensamblar plataforma sigue abierta en **M3,
M6 y M9**, dentro de los 12 meses. Comparar costos futuros evitables con igual
cobertura, volumen, calidad, operación y salida, incluida la capacidad que
falta para construir más tarde; no copiar tramos ya ejecutados ni costos hundidos.
Regla del Directorio ([R-15](07-resoluciones.md#arquitectura-y-medición)):
señal contractual/precio/producto, más brecha documentada, alternativas
comparables, economía incremental o pérdida de aprendizaje aceptada y capacidad
demostrada; una prohibición pura excluye uso. El CFO produce la evidencia de la
economía incremental, dictamina el AI Council y libera el Directorio; si falta
una condición, no se libera y sigue el mínimo. Ni una señal ni el mero anuncio de precio
demuestran que la inversión se pague. No se difiere plataforma al año 2 por defecto.

**Responsables:** produce el CAIO; verifica otra persona (el CFO las cifras, el
Responsable de seguridad los controles); acepta el residual el dueño del riesgo o
el AI Council; firma el gate el CEO dentro del techo de su tramo; Operaciones y managers
confirman agendas. Las personas se nombran en el acta de cada liberación
([R-06](07-resoluciones.md#autoridad-y-liberaciones),
[R-10](07-resoluciones.md#gobierno-y-seguridad)).
**Éxito:** controles probados antes de habilitar, básicos ≥90% con evaluación
práctica si el calendario lo permite, medición reproducible con faltantes visibles,
horas conciliadas y decisión documentada. **Abandono/revisión:** control obligatorio
incumplido, críticos abiertos, daño, falta de perfil/verificador/agenda, costos fuera
del techo o base no resolutiva: suspender uso afectado, reducir/resecuenciar o cortar
la prueba según F; no declarar valor ni ampliar con datos insuficientes.

### Pedido completo 33+6 / 72+7 y gates económicos (alternativa)

Todo «hoy», «recomendado» o «aprueba» dentro de esta sección y su tabla se refiere
al pedido completo. No constituye el pedido vigente ni libera caja o tiempo del
paquete mínimo. El pedido vigente y sus gates están en
[F, «Gates por condición (pasa, espera, corta)»](06-roadmap-riesgo.md#gates-por-condición-pasa-espera-corta).
Los importes y compromisos de esta alternativa no se trasladan al mínimo.

**Pedido de hoy, único.** Elige la vía del contractor desde el mes 1 y autoriza solo
su tramo de los meses 1-3 (hasta 16,5 de caja, dentro del techo de 33); los tramos de los meses 4-12
se liberan con las decisiones de los meses 3, 6 y 9. No es una aprobación anual. Incluye siete cosas:

1. **Caja de los meses 1-3:** techo de 33k USD (máximo calculado 32,2: contractor desde el mes 1 hasta
   16,5; legal hasta 10; telemetría hasta 1,5; contingencia hasta 4,2).
2. **Reserva de cierre:** hasta 6k USD de caja (un mes de contractor y de
   laboratorio), que solo se usa si un gate corta. Con ella, el compromiso
   máximo de caja que autoriza la aprobación de hoy es **39k USD**. Cubre solo un corte en el mes 3: el
   board se compromete a ampliarla a 15 en el mes 3 con señal y a 17 en el mes 6 si libera el producto, antes
   de liberar el compromiso nuevo (ver "Reserva de cierre vigente").
3. **Tiempo de los meses 1-3:** techo de **72k USD** con la prueba chica, que son ~1,8 FTE
   de personas clave y **~654 h distribuidas** en la dotación, como segundo
   sobre (62, 1,6 FTE y 590 h sin la prueba).
4. **Piso de capacidad:** el board confirma que el sobre clave disponible es de
   al menos **~1,8 FTE en los meses 1-3**, el techo con la prueba (12 personas al 15% o 15 al
   12%). Entre 1,6 y 1,8 entra el primer tramo acotado sin la prueba (propuesta de Finanzas); bajo 1,6
   no entra ninguna versión. Fija además el de los meses 4-12:
   2,2 / 2,2 / 2,1 con el producto diferido y el replan de los meses 4-6 del
   [Anexo B](02-arquitectura.md), o 2,5 en los meses 4-6 si elige la excepción acotada. Más la
   lectura del sobre, estricta o separada.
5. **Base mínima tras un corte:** si la decisión del mes 3 rechaza seguir, se conserva el núcleo de
   gobierno el resto del año, hasta 41k USD de tiempo (máximo calculado 40,2) y
   sin caja. Es lo que lleva
   el máximo del año con corte en el mes 3 a 156.
6. **Preparación previa:** autorizar, o ratificar si hay registro de que ya se hizo, hasta 7k USD
   de tiempo previo a la aprobación de hoy. Hoy es una propuesta: no consta que se haya ejecutado.
7. **IA aplicada y producto:** la vía del contractor desde el mes 1 (o el rol interno en los meses 1-3 si demuestra
   capacidad, con el contractor desde el mes 4), solo en su tramo de los meses 1-3; las decisiones de los meses 3, 6 y 9
   liberan los de los meses 4-12. Con señal y sin contractor, los hitos de IA aplicada de los meses 4-12 no se
   inician (la contingencia de que no haya contractor: la excepción de 0,3 no la cubre). El producto,
   diferido hasta el mes 6, con su tramo condicional.

El techo de caja se confirma contra el presupuesto 2027.

Las condiciones de throughput de los meses 6 y 9 de esta tabla son la regla anterior del paquete completo, conservada como antecedente; la vigente es la del Anexo B, «Gate de valor». Esta tabla **proyecta la tabla del Anexo F** ([Anexo F](06-roadmap-riesgo.md), "Gates por
condición"), no da órdenes propias; si difieren, manda el Anexo F. La pérdida vale solo
si el resultado es un corte. Cuatro palabras no son sinónimos:

- **Corte:** el frente deja de financiarse y queda la base mínima. Solo por una
  regla del Anexo F: la lectura del mes 6 con estimado ≤ 0% o más retrabajo, o espera vencida; la lectura del mes 9 con
  estimado < +5%.
- **Suspensión:** se frena un gasto puntual y se vuelve a medir, sin cortar el
  frente: la lectura del mes 6 en espera (los meses 7-9 sin escalado, nueva medición a las 6 semanas) y uso de
  Tecnología <60% (horas de champions e intermedio de los meses 7-9).
- **Mantenimiento:** el frente sigue sin escalar. La lectura del mes 9 en espera: los meses 10-12 con la base
  mínima y mantenimiento. Adopción en 60%-80%: el tramo de los meses 7-9 sigue y se mide al cierre de ese tramo.
- **Excepción:** el board aprueba algo fuera del sobre, sin caja (0,3 FTE en los meses 4-6,
  en la aprobación de hoy).

#### Hoy

| Campo | Contenido |
|---|---|
| Cuándo | Aprobación |
| Libera (caja / tiempo, techo) y reserva vigente | Meses 1-3: 33 / 72 (con la prueba chica); reserva 6 |
| Condiciones con efecto económico | Pedido de hoy completo; techo y piso de capacidad confirmados; vía de IA aplicada |
| Si no se cumple, según el Anexo F | No arrancan los meses 1-3; la preparación previa queda hundida (≤ 7). Sin vía de IA aplicada, sus hitos pasan a los meses 4-6 |
| Pérdida si se corta | — |
| Reversible | Sí |

#### Mes 3

| Campo | Contenido |
|---|---|
| Cuándo | Fin de los meses 1-3 |
| Libera (caja / tiempo, techo) y reserva vigente | Con señal, meses 4-6 de la plataforma: 71 / 106 (71 / 114 con la excepción); reserva **ampliada a 15**. Sin señal, meses 4-6 como gobierno mínimo y formación |
| Condiciones con efecto económico | **Bifurcación:** al menos una señal (umbral contractual, anuncio de precio por consumo o cliente para el producto) libera la plataforma (contractor al 100%, gateway, pasarela). Además: base congelada con la unidad del Anexo B; matriz de los clientes que concentran la facturación; uso de los meses 1-3 dentro del sobre; contractor contratado |
| Si no se cumple, según el Anexo F | **Ninguna condición del mes 3 corta el plan.** Sin señal: los meses 4-12 como gobierno mínimo y formación con la prueba extendida (≈ 199 en el año); las lecturas de los meses 6 y 9 releen las señales. Base insuficiente: 6 semanas más sin atribuir ganancia; sin base al cierre, sale el resultado clave de throughput y el frente interno no escala. Matriz ambigua: *default-deny* y revisión legal hasta el mes 4. Sobre excedido: los meses 4-6 solo con replan de capacidad. Si el respaldo de aprobación o el alcance de la política no están revisados: un plazo de 6 semanas para completarlos, sin casos nuevos ([R-07](07-resoluciones.md#gobierno-y-seguridad)); es un plazo de la política, no la espera de throughput de [R-27](07-resoluciones.md#finanzas); al vencer sin aprobación documentada o sin cobertura aplicable al producto demostrada, no hay el producto en el año (38 / 34 que no se liberan). Evidencia contractual incompleta: se completa en los meses 4-6; sin ella en el mes 9, la demostración externa (11,6-31 de caja) no se financia. Básico <50% al cierre de los meses 1-3: rediseño del mes 3 con cambio de formato de la capacitación ([R-21](07-resoluciones.md#personas)). Con señal y sin contractor: los meses 4-6 en el modo control del Anexo B, sin los hitos de IA aplicada; la caja de los meses 4-6 baja ~27 (contractor con contingencia) |
| Pérdida si se corta | Solo si el board decide **no liberar los meses 4-6** (no es una regla de corte): 79, hasta 115 hasta cerrar; con la base mínima (hasta 41 de tiempo), hasta 156 en el año |
| Reversible | Sí |

#### Mes 6

| Campo | Contenido |
|---|---|
| Cuándo | Fin de los meses 4-6 |
| Libera (caja / tiempo, techo) y reserva vigente | Meses 7-9: 59 / 78; el producto, solo con señal de cliente y plataforma liberada en el mes 3: 38 / 34 más; reserva 15 (**17** con el producto) |
| Condiciones con efecto económico | Throughput: **pasa** con límite inferior ≥ +3%, sin más retrabajo; **espera** con estimado > 0% y límite inferior < +3%, o muestra insuficiente: los meses 7-9 sin escalado y nueva medición a las 6 semanas; **corta** con estimado ≤ 0% o más retrabajo. FinOps con el múltiplo medido; destino de la capacidad decidido |
| Si no se cumple, según el Anexo F | Throughput: **suspensión** (espera) o **corte** del frente interno, que deja la base mínima; la espera vencida corta igual. Cobertura de precio no demostrada: la palanca sale del deck. Más de 6× sin mitigar: se congela la expansión y se topea el consumo. Sin señal de cliente, o sin plataforma del mes 3: el producto se difiere y sus condiciones del mes 9 no aplican |
| Pérdida si se corta | Corte del frente interno: 198 (máximo 291) hasta cerrar; año 224 / 330 |
| Reversible | Sí |

#### Mes 9

| Campo | Contenido |
|---|---|
| Cuándo | Fin de los meses 7-9 |
| Libera (caja / tiempo, techo) y reserva vigente | Meses 10-12: 95 / 69; el producto, si sigue: 21 / 23 más; reserva 15 (17 con el producto) |
| Condiciones con efecto económico | Throughput: **pasa** con límite inferior ≥ +8%; **espera** con estimado ≥ +5% y límite inferior < +8%, o muestra insuficiente: **mantenimiento** (solo base mínima), nueva medición a las 6 semanas; **corta** con estimado < +5%. Costo por PR sin subir. Señal contractual o producto liberado para la demostración externa. SLO del piloto, solo si el producto se liberó |
| Si no se cumple, según el Anexo F | Throughput < +5%: corte del frente interno y de la base común; queda la base mínima. **Si el producto sigue, rige la precedencia** (seguridad, dependencias, caja) y el producto conserva su base común mínima. Sin señal contractual ni el producto: la demostración externa no se financia |
| Pérdida si se corta | Sin el producto: 292 (máximo 427) hasta cerrar; año 305 / 447. Con el producto vivo, corte mixto: año 433 (con el producto sin corte, 471) |
| Reversible | Sí |

#### Mes 12

| Campo | Contenido |
|---|---|
| Cuándo | Fin de los meses 10-12 |
| Libera (caja / tiempo, techo) y reserva vigente | Año 2: régimen de ~143 (~188 con el producto), en el presupuesto 2028 |
| Condiciones con efecto económico | Trayectoria hacia el equilibrio operativo anual de ~17% de throughput **atribuible contra la base de los meses 1-3** (~23% si el producto sigue; menos si la capacidad se vende) **o** interés contractual en el producto; decisiones sobre contractor, on-premise e ISO 42001 |
| Si no se cumple, según el Anexo F | No se financia el régimen. Queda el frente interno con las licencias vigentes y la base mínima, ~53 por año (29-78); el gateway se da de baja salvo que FinOps muestre que acota más de lo que cuesta |
| Pérdida si se corta | — |
| Reversible | Contrato a más de 12 meses o hardware: irreversible |

Irreversibles marcados (de los Anexos [B](02-arquitectura.md) y
[C](03-gobierno-seguridad.md)): compromisos de volumen a más de 12 meses, capex
en infraestructura propia y firma con un cliente. Ninguno se toma antes del mes 12.

### Solapes entre anexos

Regla: **el base cuenta los dos renglones** salvo donde los dos dueños ya
acordaron la consolidación. La consolidación es un ahorro que confirma el dueño.

| Solape | Renglones | Ahorro posible | Estado |
|---|---|---|---|
| IA aplicada | 0,5 / 0,8 FTE del Anexo B y contractor del Anexo D | 32-79 de tiempo en los meses 4-12 y 4-10 en los meses 1-3 | **Consolidado**: los Anexos B y D acuerdan que el contractor reemplaza; el base ya lo descuenta |
| Pruebas de bypass y migración | DevOps/QA del Anexo B (2,1-10,7, dentro de su fracción) y prueba de integración del Anexo C (1,1-5,6) | Hasta 1,1-5,6 | Lo resuelven Arquitectura y Gobierno |
| Red team | Piloto en los meses 7-9 (Arquitectura, 5-15, solo en el tramo del producto) y externo en los meses 10-12 (Gobierno, 10-25) | 5-15 como sensibilidad publicada, sin descuento aplicado | Desacuerdo a la vista en la [fuente](../../context/supuestos/precios-externos-sin-cotizar.md); según C, un único contrato debe cubrir piloto, reprueba y las superficies/controles que pida el cliente. Sin producto no hay solape; no sustituir alcances ni elegir un precio hasta conciliarlos |
| Gateway y pasarela de salida | Infraestructura (Arquitectura, 14-38) y pasarela, DLP y logs (Gobierno, 4,5-18) | Hasta 4,5-18 si son la misma pieza | Arquitectura |
| Infraestructura de los meses 7-12 sin piloto | El Anexo B la dimensionaba "con el piloto y su tráfico" (2-6 por mes) | 1,5-6 por tramo de tres meses (3-12 en los meses 7-9 y los meses 10-12 juntos), más 6-24 por año a régimen | **Consolidado**: Arquitectura confirma que sin el producto baja al nivel de los meses 4-6; el incremento pasa al tramo del producto |
| Seguridad | 20% de un senior de DevOps o seguridad (Gobierno) y DevOps/QA (Arquitectura) | Sin cuantificar | Arquitectura y Gobierno |

## Tensiones con otras miradas

Las tensiones de capacidad/contratación del paquete completo son antecedentes:
ningún «hoy» de esas filas autoriza ese alcance. Rige el pedido mínimo de E;
cualquier excepción exige nuevo costeo y nueva decisión.

| Tensión | Planteada por | Posición de Finanzas | Estado |
|---|---|---|---|
| Exceso de ~0,3 FTE clave en los meses 4-6 con el producto diferido | Finanzas | Arquitectura propone el replan del Anexo B (los meses 4-6 en 2,2 FTE clave, −5k USD de tiempo) y la excepción acotada como respaldo. Finanzas toma el replan como base y deja la excepción costeada | **Regla del Directorio si se reactiva el paquete** ([R-17](07-resoluciones.md#arquitectura-y-medición), [R-28](07-resoluciones.md#finanzas)): rige el replan de B; la excepción de 0,3 FTE solo con aprobación previa del Directorio. Hoy el paquete no se pide |
| El base presentado como paso asegurado del mes 6 y del mes 9, cuando el Anexo F decide por límite inferior; "~20 personas" sin definir con una cohorte de 15-20 | Finanzas | El año del base es condicional y se lee en tres ramas (−332 / ≈ −275 / ≈ −245); el mínimo pasa a 15 activas, como supuesto | **Propuesta** a Arquitectura (Anexo B, "Muestra insuficiente") y a CAIO (Anexo F y slide «Costo y riesgo») |
| +20% de throughput con agentes a 12× lo pagado, contra el OKR de gasto de tecnología de menos de 3,5% | Arquitectura | A régimen, la base libera ~130k USD por año, que cubren consumo incremental hasta ~7× la suscripción. La caja del plan suma gasto de tecnología: el OKR es incompatible salvo que baje la nube. Propuesta: medirlo sin la inversión del plan, o por persona activa | **Escalada a CAIO** para reformular el resultado clave |
| Sobre de capacidad: lectura estricta o separada | Finanzas | La separada es propuesta de Finanzas; con la estricta, los meses 1-3 no entran sin recortar el básico | **Regla del Directorio para el mínimo** ([R-05](07-resoluciones.md#autoridad-y-liberaciones)): lectura separada; la reserva clave (hasta 720 h) y la de formación (540-660 h) se confirman por separado en la segunda liberación, antes de M1; sin agendas confirmadas, se reduce o resecuencia con recosteo |
| Staffing facturado por hora desincentiva el uso de IA | Personas | Productividad en staffing = 0 en el base. Las horas de capacitación de Operaciones (~400 h) cuestan 4-14k USD a costo; a tarifa de venta valen más, y eso se calcula con los datos internos | **Resuelta** para el costo; el modelo comercial queda **escalado a CAIO** |
| Contractor contra la restricción de no contratar; vía de IA en los meses 1-3 | Personas, Arquitectura | Antecedente del paquete completo, sin decisión de contratación hoy. Pedido vigente: mínimo de E; una excepción externa o plataforma exige cotización, nuevo costeo y nueva decisión. No se autoriza el tramo de contractor de 16,5 | **Sin contratación autorizada hoy** |
| El «costo de no actuar» como argumento de ROI | Material de la cursada | Se lista aparte y sin monto: no hay probabilidad ni pérdida con fuente, y sumarlo al ROI doblaría la palanca de riesgo. Alternativa: poner un monto supuesto con rango; infla el argumento | **Vigente**; lo juzga el board |
| Financiar con fuentes externas o híbridas | Material de la cursada | Interna, porque el pedido es chico y reversible; la híbrida solo en el tramo del producto con señal de cliente | **Vigente:** interna. La híbrida solo se evalúa si el Directorio libera el producto en el mes 6; como condición comercial de ese tramo, con cifras verificadas por el CFO ([R-30](07-resoluciones.md#roadmap-y-comercial), [R-04](07-resoluciones.md#autoridad-y-liberaciones)) |
| El paquete contra alcances más baratos | Finanzas | Alcances publicados como referencia; una ampliación exige estimación común desde el gate ([R-28](07-resoluciones.md#finanzas)); una señal no demuestra repago | **Vigente:** pedido inicial mínimo; plataforma se reevalúa M3/M6/M9 con la señal y las cuatro condiciones de la regla del Directorio ([R-15](07-resoluciones.md#arquitectura-y-medición)) |

## Conclusión económica

Tres magnitudes distintas, que responden preguntas distintas:

| Magnitud | Meses 1-3 | Qué responde |
|---|---|---|
| Recursos valorizados a costo cargado | 14,4-58,3, con la verificación de la lectura del mes 3 | Cuánto vale el tiempo asignado |
| Desembolso incremental de caja | 2,3-8,6 | Cuánto sale efectivamente de la empresa |
| Contribución comercial desplazada | sin medir | Cuánto margen se deja de ganar |

La validación previa (80-136 h; 1,4875-6,35 calculados, techo 8) es tiempo
valorizado sin desembolso de caja. Sobre estas magnitudes se fija el **límite de
autorización del alcance presupuestado**: 79 acumulados (caja 9 + tiempo
valorizado 59 + preparación técnica 3 + validación organizativa 5 + reservas 3).
Es un techo, no un gasto esperado.

**Cómo se combinan sin doble conteo.** Depende del escenario de comparación y de
qué costos son evitables:

- Frente a **«no hacer el programa»**, el costo cargado de una persona en nómina
  no es evitable —el sueldo se paga igual—, así que el incremental es el
  desembolso de caja más la contribución desplazada.
- En una **valuación del recurso consumido**, corresponde el costo cargado,
  porque mide lo que vale el tiempo asignado.
- **El doble conteo aparece** al sumar, sobre la misma hora, el costo cargado y
  la tarifa completa: la tarifa ya contiene ese costo. Se evita midiendo la
  contribución como margen sobre costos evitables.

Cada magnitud se informa por separado, con el escenario que la hace pertinente.

**Alcance del ROI.** El ROI económico modelado de −100% corresponde **al alcance
mínimo y a los supuestos de ese modelo**, que no presupuesta beneficios
cuantificados dentro de los 12 meses. No implica que el programa carezca de
beneficios: los de protección y de opción se declaran sin cifra porque no hay
base para estimarlos sin inventarlos. Tampoco equivale a una pérdida efectiva de
caja: el desembolso modelado del tramo es 2,3-8,6 y el resto es tiempo valorizado de
personas que ya están en la organización. El −84% corresponde al paquete
completo, que no se pide hoy.

**Lo que este pedido no promete.** Beneficio de caja estimado: 0. Ingreso nuevo:
0. El mínimo no compra repago: compra la evidencia que permite decidir si
ampliar, con gates que lo frenan y con la exposición presupuestaria de cada
salida declarada por adelantado.

## Insumos para el deck

- **Frase para el CFO:** «Medir antes de ampliar: pedido inicial, paquete mínimo
  sin plataforma central. Primero, caja 0 / tiempo 8 para validar; después,
  solo si pasa el hito, caja 10 / tiempo 61 para M1-M3 y cierre. El Directorio
  fija hoy 79 hasta el mes 3 y 121 en el año, con techos por tramo de 16, 13 y
  13, y libera solo 8. Hasta el mes 3 el estimado es 18-73 contra el techo de 79:
  caja 9, tiempo valorizado 59, preparación técnica 3, validación organizativa 5
  y reservas 3.
  De eso, el desembolso de caja modelado es 2,3-8,6; el resto es tiempo de gente que ya
  está en la organización y reservas contingentes. No promete repago: beneficio
  de caja 0 e ingreso nuevo 0, con ROI modelado −100% porque este alcance no
  presupuesta beneficios cuantificados. Compra tres cosas: controles probados
  sobre usos que ya operan, la medición que hoy no existe y la opción de decidir
  en el mes 3 con evidencia. La exposición presupuestaria de cada salida está
  declarada».
- **Capacidad inicial:** 970-1.346 h de actividades (más 4-5 h de verificación de la lectura del mes 3) / 480 = 2,0208-2,8042 FTE internos,
  incluidos 0,8958-1,4292 clave y 1,125-1,375 distribuidos; referencia 2,4125.
  Previo a M1: validación organizativa 60-96 h + técnica 20-40 h = 80-136 h;
  agendas e imputación 2026 confirmadas antes de trabajar, sin contractor continuo.
- **Reserva propuesta:** 720 h clave más formación de hasta 660 h; máximo
  1.380 h, sujeto a agendas confirmadas. Reserva no equivale a horas ejecutadas.
- **Salida M3:** exposición presupuestaria máxima autorizada de 79 hasta cerrar; núcleo M4-M12 108 h, caja 0 y techo
  6 de tiempo; máximo anual con corte 85 solo si el núcleo se aprueba explícitamente
  en el gate de salida. Los 6 no están en los 79; reservas no son gasto automático.
- **Salidas y esperas:** corte inmediato M6 95 hasta cerrar / 99 con núcleo;
  M9 108/110; M12 121. Una espera de seis semanas requiere subtramo aprobado
  64-106 h, caja 1 / tiempo 6, reservas 1/2 compartidas; solo hay espera en el
  mes 9 (el mes 6 ya no espera por medición); al vencer y cortar: 115/116. Sustituye continuidad y núcleo del período, sin
  duplicarlos, y va dentro del techo de su tramo: ningún camino con espera supera
  121; si uno lo hiciera, o superara el techo de un tramo, vuelve al Directorio.
- **Proyección anual sin esperas:** ≈71 (27-114), con el verificador y la fila de Personas; techos sin gastar reservas
  118 (15 caja / 103 tiempo), con cierre 121. No es autorización anual.
- **Continuidad por gate:** M4-M6 2/14 de caja/tiempo (techo del tramo 16), con
  descubrimiento de integración; M7-M9 2/11 (13); M10-M12 2/11 (13). Los techos
  se fijan hoy y no se liberan; el CEO firma cada gate dentro del techo de su
  tramo ([R-03 y R-04](07-resoluciones.md#autoridad-y-liberaciones)). Plataforma abierta
  en M3/M6/M9, con nuevo costeo del futuro evitable, la señal y las cuatro
  condiciones de la regla del Directorio ([R-15](07-resoluciones.md#arquitectura-y-medición)). [F, «Línea de tiempo integrada»](06-roadmap-riesgo.md#línea-de-tiempo-integrada)
  y las slides [«Roadmap técnico, financiero y cultural» y «Costo y riesgo»](../slides.md)
  presentan este pedido mínimo y sus liberaciones condicionadas.
- **Estimado contra techo hasta el mes 3:** 18-73 calculado, sin reservas ni
  núcleo, contra el techo de 79. **71 = 68 operativos + 3 de reservas.**
- **ROI, con definición y período:** ROI económico a 12 meses = (capacidad
  liberada − caja − tiempo) / (caja + tiempo). En el mínimo, −100% modelado
  (capacidad 0 hasta medir); en el paquete completo, −84% en la base.
- **Exposición al consumo, también con el mínimo:** el incremental modelado a
  12× es 211-267k USD al año, con o sin plan; no es consumo futuro facturado ni
  ahorro observado. El mínimo no lo mitiga con gateway. Compararlo con toda la
  caja anual del paquete completo es solo un benchmark de aquel alcance,
  no el costo ni un beneficio del mínimo. En una ampliación autorizada, la
  prueba de plataforma mide si el gateway reduce el gasto elegible; los umbrales
  ~12,8% a 12× y ~25,6% a 6× no acreditan ahorro por sí solos.
- **Equilibrio del paquete completo, no aplicable al mínimo:** régimen del año 2
  (no recupera la inversión del año 1,
  no es ROI ni payback): ~17% de throughput atribuible (~23% con producto), contra la
  base de los meses 1-3. El +20% del OKR lo cubre solo si 1,20/(1+d) − 1 − c ≥ 16,7%: d es
  la mejora del cuarto trimestre de 2026 a la base de los meses 1-3 (se mide en el mes 3) y c, el cambio del grupo que no
  adopta (desde el mes 6).
- **Alternativas de otro alcance:** 47/161/≈199/394/≈400/471 son costos publicados
  de alcances distintos: referencia, sin elección entre ellos ([R-28](07-resoluciones.md#finanzas)). Base del paquete −331,9
  (ROI −84,2%); optimista sin producto −279,9 y con producto −356,9.
  No trasladar capacidad o retorno del paquete completo al mínimo.
- **Narrativa financiera, en tres pasos (datos → narrativa → decisión):**
  1. *Datos:* el paquete completo no se repaga en 12 meses (ROI −84% en la base) y el
     beneficio de caja del año es 0. El mínimo cuesta hasta 79 y compra evidencia.
  2. *Narrativa:* sin retorno prometido, se compra información para decidir. Lo que
     el board evita es seguir expuesto sin medir: clientes que por defecto
     prohíben modelos externos, reglas y aplicación por contrastar y un consumo de ~12× lo pagado que el
     mínimo no cubre. Sin montos inventados.
  3. *Decisión:* aprobar la primera autorización (caja 0 / tiempo 8) y fijar los
     criterios para liberar la segunda; ampliar solo si las métricas de los gates pasan.
- **Frase para la objeción «¿y el VPN?»:** «No hay flujos positivos de caja en el
  horizonte ni una tasa del caso; calcularlo sería inventar la tasa. Cuando haya
  contrato o régimen del año 2, se calcula con la tasa que fije el board».
- **Fuente de la plata:** interna (margen operativo y tiempo reasignado), por
  etapas y reversible; sin deuda. La cofinanciación de un cliente es solo del tramo
  del producto.

## Cautelas

- El tech lead de gobierno se costea en 22-32 h, la suma de las actividades de C
  (8-16 de política + 2-4 de legal + 12 de Council). Frente al rango anterior de
  22-36 h, el máximo baja 4 h × 62,5 USD/h = 250 USD; el techo de 59 no cambia
  ([R-25](07-resoluciones.md#finanzas)).
- Las 8-16 h de Personas (convocatorias y registro de completitud) van en un solo
  sobre, el clave, dentro de la fila de staff (26-40 h). Pasarlas al distribuido
  movería el soporte clave de 430-686 h y el margen de 34 h que fija
  [R-25](07-resoluciones.md#finanzas).
- La primera liberación tiene caja 0: si la decisión sobre eventos de uso por
  persona ([R-13](07-resoluciones.md#gobierno-y-seguridad)) se toma en la
  preparación y necesita consulta legal externa paga, esa consulta no está
  costeada ahí. Rige el default de agregados por área, que no la necesita, y la
  consulta entra en el dictamen de M1-M3; otra cosa requiere caja aparte del
  Directorio.
- Rige la clasificación de controles exigibles y opcionales del Anexo C
  ([R-11](07-resoluciones.md#gobierno-y-seguridad)); este anexo no descuenta
  costos por ella. La ruta de incidentes se monta sobre el circuito del SGSI
  existente, dentro de las horas de "Política e intake": 0 USD adicionales en
  M1-M3 ([R-12](07-resoluciones.md#gobierno-y-seguridad)). Solapes, autoridad y
  estimación de Personas están resueltos en R-26, R-04 y R-24. La viabilidad
  técnica la verifica el verificador senior independiente dentro de las horas ya
  costeadas ([R-14](07-resoluciones.md#arquitectura-y-medición)).
- N × costo por desarrollador es una cuenta de planificación, no la nómina de la empresa.
- La valuación de la capacidad a costo cargado y con la lectura de horas evitadas es un piso
  deliberado. La tarifa no se publica ni se deriva de márgenes internos.
- Supuestos sin fuente propia: las fracciones por rol del primer tramo acotado (están en los
  Anexos B, C y D), las bandas de espera del mes 6 y del mes 9 (Anexo F), el costo de "los meses 7-9
  sin escalado", y los valores ilustrativos de PR por persona y semana (2 y 4) y
  de 15 minutos de revisión por PR (lecturas de Finanzas en este anexo).
- El corte del mes 9 alcanza al frente interno y a la base común ([Anexo F](06-roadmap-riesgo.md)).
  Si solo cortara el interno, el año quedaría en ~381 (neto ≈ −369). El 50% del
  contractor en la base común mínima para el producto no tiene dato.
- El puente del equilibrio supone que d (serie de la preparación previa) y c (grupo que no adopta
  o tendencia) se pueden medir; con cohortes chicas, su ruido puede ser del
  orden de los ~3 puntos que comparten. Las ramas del base no llevan
  probabilidad: dependen de σ, que no tiene dato.
- El rango del equilibrio (9%-46%) mueve N y el costo por desarrollador con el
  régimen fijo en su medio; no suma el error del régimen.
- La comparación del gateway bajo suscripción y bajo consumo es un umbral, no un
  ahorro: no hay medición de la fracción enrutable ni del efecto del ruteo.
- El Δp de la palanca de riesgo usa el margen EBITDA como proxy conservador.
- No se usaron cifras sin fuente primaria (60%-80% de ahorro de
  inferencia, ROI de 2,8×-4,1×, 360 → 7 USD, 70% más de retención con reskilling) ([fuentes faltantes](../../material/huecos.md)).
