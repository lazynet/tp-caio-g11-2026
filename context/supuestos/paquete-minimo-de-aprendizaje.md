---
type: Supuesto
title: "Paquete mínimo de aprendizaje sin plataforma central"
description: "Finanzas concilia los insumos de B/C/D para medir valor con controles probados y herramientas existentes, con techos por etapa y salida acotada."
status: draft
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Ficha completa confirmada por Martín en tres bloques: preparación previa de 80-136 h, caja 0 y techo de tiempo 8 mil USD; ejecución M1-M3 de 970-1.350 h con reserva de capacidad de 1.380 h y segunda autorización propuesta de 71 mil, acumulado 79 mil; continuidad, descubrimiento, esperas y salidas con techos por etapa y proyección condicional de 118 mil, 121 mil con cierre. Incluye escenarios emparejados para descontar preparación, formación a 10-35 USD/h como supuesto agregado a validar, cargas de espera y núcleo parcial sujetas a cadencia, recomposición de secuencias de espera y exposición máxima separada en caja y tiempo. Se conservan pendientes el acuerdo del equipo, cotizaciones, solapes, personas, agendas, ratificaciones y autorizaciones empresariales; no se acredita ejecución, disponibilidad ni beneficios medidos. Confirmado en esta conversación."
tags: [supuesto, finanzas, capacidad, controles]
sources:
  - id: arquitectura
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, actividades técnicas, controles y protocolo de medición"
  - id: gobierno
    resource: "plan/annexes/03-gobierno-seguridad.md"
    title: "Anexo C, gobierno mínimo, legal y verificación de controles"
  - id: personas
    resource: "plan/annexes/04-personas-cultura.md"
    title: "Anexo D, insumo para el paquete mínimo y actividades de formación"
  - id: business-case
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, pedido inicial, continuidad y exposiciones de salida del mínimo"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Rangos de planificación de costo cargado mensual por rol"
  - id: convenciones
    resource: "context/supuestos/convenciones-de-calculo.md"
    title: "Convenciones de calendario, horas de costeo y redondeos"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---

# Supuesto

Propuesta de Finanzas con validación inicial, adoptada por el Directorio al
aprobar el plan (Anexo G)[^resoluciones]. Las estimaciones
requieren cotización y confirmación de disponibilidad en cada liberación.

El detalle reproducible vive en el Anexo E, «Pedido inicial: paquete mínimo».[^business-case]
B/C/D son insumos de diseño, no evidencia externa; las fichas referidas conservan
su propio estado de revisión y sus cautelas.[^arquitectura][^gobierno][^personas]

## Alcance y conciliación M1-M3

Herramientas existentes, cuatro superficies y cohorte propia de 15-20 personas.
Se pagan controles aplicables equivalentes para cada uso habilitado: política,
matriz, inventario, dictamen legal, configuración, pruebas negativas, corrección,
verificación independiente y aceptación del residual. Sin gateway ni plataforma
central, producto, avanzado, red de champions al 10% o contractor continuo.

Unión de actividades adoptada por el Directorio (R-26)[^resoluciones]; la
confirman Tecnología y Seguridad antes de la segunda liberación:[^arquitectura][^gobierno][^personas]

| Rol / actividad | Horas M1-M3, sin preparación | Derivación y solape tratado |
|---|---|---|
| Tech lead / arquitectura / adopción | 146-272 | B 24-40 + C 22-32 (política, legal y Council) + D «Insumo para el paquete mínimo»: 48-96 líder, 16-32 facilitación y 8-16 managers + E anterior 40-80 diseño de prueba; menos preparación 12-24 |
| DevOps productor | 44-72 | Unión de B 32-56 y C 40-64 para configurar/probar, más C 4-8 inventario; se toma 40-64 para la unión, no la suma |
| QA / datos | 48-72 | B 40-64 contiene D «Insumo para el paquete mínimo»: 8-16 de reproducción; más lectura de prueba E 16-24; menos preparación 8-16 |
| IA aplicada interna | 8-16 | B, tareas distintas de facilitación y diseño; exige competencia demostrada |
| Seguridad verificadora | 34-54 | B 24-40 técnicas, reutilizables para matriz y pruebas de C solo con confirmación de alcance; política C 4-8 aparte porque B la excluye; más 6 de Council; persona distinta del productor |
| Seniors de la cohorte que sostienen prácticas | 64 | Soporte de prueba E anterior, contiene B 16-24 de revisión; no sumar champions de D |
| Analista funcional | 60-96 | C: matriz 32-48, inventario 16-24, legal 4-8, compensatorios 8-16 |
| Staff | 26-40 | C: política 2-4, matriz 4-8, Council 12; D «Insumo para el paquete mínimo»: administración 8-16 |
| Básico | 360-420 | 60-70 × 6 h, reservar toda la población, no solo el 90% objetivo |
| Intermedio de la cohorte | 180-240 | 15-20 × 12 h; reemplaza la población anterior, no se suma a ella |

La unión de DevOps supone que la configuración y la primera corrección de B/C
son la misma tarea y caben en 40-64 h; la de QA y Seguridad supone reutilización
del mismo entregable técnico, sin absorber política en Seguridad.

DevOps 40-64 h es un tope de alcance, no un ahorro: si las exportaciones no
entran, se reportan como uso estimado; si aun así no entra, el CFO recostea
antes de M1 dentro de 71 y firma el CEO; superar 71 vuelve al Directorio. Roles acumulados requieren agenda por persona.

Las restas de preparación de TL y QA emparejan extremos del mismo escenario;
no son restas de intervalos independientes. El remanente por actividad debe
conciliarse antes de ejecutar; si esa correspondencia no se confirma, recostear.

## Reserva propuesta de capacidad M1-M3

Supuesto de planificación para solicitar capacidad; Operaciones y los managers
confirman personas, agendas y trabajo desplazado antes de cada actividad. Rige
la lectura separada: la reserva clave y la de formación se confirman por separado
en la segunda liberación (R-05)[^resoluciones].

| Destino | Reserva propuesta | Derivación |
|---|---|---|
| Soporte clave, repartido entre roles | Hasta 720 h / 1,5 FTE de costeo | 1,5 × 480 h; demanda estimada de soporte 430-686 h |
| Formación básica | 360-420 h | 60-70 personas × 6 h |
| Formación intermedia | 180-240 h | Cohorte de 15-20 personas × 12 h |
| Máximo combinado | 1.380 h / 2,875 FTE de costeo | 720 + 420 + 240; no incluye preparación previa ni cierre condicional |

El soporte tiene 34 h de margen sobre su demanda máxima estimada (720 − 686).
Ese margen agregado no cubre automáticamente faltantes de otro rol o semana.
La formación de quienes también producen o verifican se suma en su agenda.

La demanda costeada es 970-1.346 h; la reserva de capacidad no es ejecución
ni una reserva financiera adicional. El margen de 34 h no tiene actividad ni
rol costeado: usarlo exige estimar su costo y autorizarlo antes de comprometerlo.

Se mantienen los techos financieros del mínimo. Si la asignación adicional no
cabe en ellos, reducir o resecuenciar el alcance, o elevar un recosteo para
aprobación. No financiar agendas iniciales con productividad futura.

Los insumos de D se refieren al Anexo D (`plan/annexes/04-personas-cultura.md`),
sección «Insumo para el paquete mínimo»; son supuestos de planificación,
no agendas liberadas, y se integran con esta corrección.

Preparación separada: tech lead 12-24 h (B 4-8 + D «Insumo para el paquete mínimo»:
8-16 de facilitación) y QA 8-16 h de B. Total 20-40 h, extraídas de sus filas:
no agregadas por segunda vez.

No consta ejecución previa. No usar formación ni prácticas antes de congelar base.

Los 40-80 h de diseño y las 64 h de seniors de E anterior sostienen la prueba;
no se hereda su costo redondeado de 6 mil ni su lectura adicional de 16-24 h dos
veces. Básico e intermedio de esos mismos roles son bloques distintos.

## Validación inicial

Primera autorización específica durante octubre-diciembre de 2026, por **10 días
hábiles**. Antes de trabajar: imputación del tiempo a presupuesto 2026 aprobada,
agendas, fuentes y trabajo desplazado confirmados por las autoridades correspondientes.

Sin esas condiciones la ventana no comienza y M1 no arranca. La aprueba el
Directorio al aprobar el plan; produce el CAIO y verifica el CFO; el Responsable
de Tecnología confirma el acceso a las fuentes (R-02)[^resoluciones].

**Validación organizativa adicional**, 60-96 h: estimación de Finanzas confirmada
por Personas como estimación de planificación, con las condiciones de validez del
Anexo D. El día 2 de la ventana, una prueba de una hora sobre un área confirma el
export; si la matriz no entra, el día 3 se reduce el detalle a horas clave y
cohorte o se recostea dentro del techo 5, y si lo excede la ventana se detiene y
vuelve al Directorio (R-24)[^resoluciones]. Costo
horario según [costo por rol](/supuestos/costo-cargado-por-rol.md)/160;[^costo-rol] las horas
incluyen entrevistadores, entrevistados, managers, staff y autoridad que decide:

| Rol | Horas | USD/h | Tiempo, miles de USD |
|---|---|---|---|
| TL, coordinación, managers y autoridad de decisión | 16-24 | 28,125-62,5 | 0,45-1,5 |
| Analista funcional | 20-32 | 12,5-34,375 | 0,25-1,1 |
| Staff de Operaciones, Personas, Comercial y Finanzas | 16-24 | 9,375-31,25 | 0,15-0,75 |
| Senior verificador independiente | 8-16 | 18,75-46,875 | 0,15-0,75 |
| **Total organizativo adicional** | **60-96** | Por rol | **1-4,1; techo 5** |

La autoridad se aproxima con TL/staff según la tarea; no es su remuneración real.
El verificador es otra persona que quien produjo lo revisado. Si esas funciones
o su costo no encajan en los rangos, se vuelve a costear.

| Actividad | TL | Analista | Staff | Verificador | Total, h |
|---|---|---|---|---|---|
| Entrevistas y contraste del diagnóstico | 4-8 | 4-6 | 8-12 | — | 16-26 |
| Conciliación del padrón y matriz persona/semana | 4 | 8-14 | 4-6 | — | 16-24 |
| Estado de políticas, restricciones y separación de funciones | 4-6 | 4-6 | 2 | 4-8 | 14-22 |
| Conciliación económica, solapes y trabajo desplazado | 2 | 4-6 | 2-4 | — | 8-12 |
| Verificación, decisión y cierre documental | 2-4 | — | — | 4-8 | 6-12 |
| **Total, h** | **16-24** | **20-32** | **16-24** | **8-16** | **60-96** |

Alcance: 4-6 entrevistas de una hora y una ronda de contraste con documentos
existentes; todas las horas de participación están incluidas. No supone entrevistar
individualmente a toda la organización ni implementar controles.

Entregables: diagnóstico contrastado y faltantes; padrón conciliado; matriz privada
persona/semana con capacidad, formación y trabajo desplazado; productor, verificador
independiente y autoridades identificados por entregable.

También: estado actual de políticas y restricciones, viabilidad técnica/de medición,
conciliación de solapes y recosteo. La decisión documentada es continuar,
reducir/resecuenciar o detener; un bloqueo no se presenta como aprobación.

Todo el trabajo organizativo se trata como adicional hasta confirmar equivalencias
con B/C/D; una equivalencia se descuenta una sola vez de la ejecución posterior.
No se presume absorbido en 59 mil, 720 h ni las 34 h de margen de M1-M3.

La preparación técnica existente se conserva separada: **20-40 h / 0,4875-2,25
mil; techo 3**, ya extraída de B/D, sin ejecución registrada. Validación y
preparación suman **80-136 h / 1,4875-6,35 mil; techo de tiempo 8 = 5+3**.

**Caja de la primera liberación: 0.** Agenda propia pre-M1 e imputación 2026;
sin formación, prácticas, herramientas nuevas, despliegues ni contratos nuevos.
La retrospectiva no sustituye la base prospectiva de semanas 1-4 de M1.

Se prepara alcance y solicita cotización legal sin contratar el dictamen. No
se supone cotización gratuita: si se cobra, requiere autorización y recosteo
previos. El dictamen completo permanece en M1-M3.

**Corte previo a M1:** costo efectivamente ejecutado hasta 8 mil de tiempo,
caja 0; el cierre documental está incluido. No se activa el cierre técnico
16-24 h de M1-M3 porque no se despliegan herramientas ni se asumen contratos.

Diez días son una ventana propuesta, no disponibilidad demostrada. Más entrevistas,
participantes o rondas, fuentes no exportables, instrumentación nueva, falta de
verificador o costos fuera de rango exigen reducir/resecuenciar o recostear.

## Segunda autorización antes de M1

La firma el CEO por delegación del Directorio, con dictamen del AI Council; el
CFO verifica costo, caja, reservas y presupuesto 2027 (R-05)[^resoluciones].
Condiciones: diagnóstico y padrón aceptados; matriz de capacidad validada por
Operaciones/managers; productor, verificador y firmante nombrados; viabilidad
técnica/de medición con método ratificado; recosteo. Sin acta, M1-M3 no arranca;
un recosteo que supere 71 vuelve al Directorio.

Libera base y controles con herramientas existentes; no habilita prácticas
automáticamente. Requieren base congelada, dictamen aplicable, controles probados,
verificación independiente y aceptación del residual.

## Costos y límites

El soporte se costea con el rango mensual del
[rol](/supuestos/costo-cargado-por-rol.md)/160.[^costo-rol] Persona-tramo de 480 h
y techos hacia arriba según [convenciones](/supuestos/convenciones-de-calculo.md).[^convenciones]

La formación distribuida se valora a 10-35 USD/h como supuesto agregado propio,
sujeto a validar la mezcla de participantes. No deriva automáticamente de las
bandas por rol, algunas de las cuales superan 35 USD/h; si no alcanza, recostear.

Legal focalizado C: 8-16 h externas × 250-375 USD/h = 2-6 mil USD; reemplaza
la porción inicial de asesoría anterior. Herramientas/exportación: provisión
0-1,5 mil por trimestre, sin seats nuevos; no prueba compra necesaria ni precio.
15% de contingencia sobre ambos: M1-M3 2,3-8,625, techo 9 mil.
Si lo existente no alcanza, reducir/excluir superficie o recostear; no usar
contingencia para agregar alcance ni suponer asesoría completa por ese precio.

Sin contractor ni laboratorio central: reserva de caja 1 mil para hasta un mes
de herramientas (máximo 0,5, redondeado arriba). Legal por hitos sin preaviso;
si no se consigue ese contrato, recostear reserva antes de firmar.
Cierre interno: 16-24 h de senior para exportar, revocar y archivar, costo
0,3-1,125 mil, reserva de tiempo 2 mil. Reservas solo ante salida, no gasto base.

Seguridad provisional cuesta 0,6375-2,53125 mil. Soporte clave total: 430-686 h,
8,8875-34,93125 mil, 0,8958-1,4292 FTE. Con formación distribuida 540-660 h,
M1-M3 totaliza **970-1.346 h / 2,0208-2,8042 FTE**, costo **14,2875-58,03125**.
Se suma aparte, declarada, la verificación de la lectura del mes 3 por el
verificador senior independiente: 4-5 h × 18,75-46,875 USD/h = 0,075-0,234375,
primer uso del margen de 34 h (soporte 434-691 h; total 974-1.351 h; tiempo
14,3625-58,265625, debajo de 59). La demanda de actividades de R-25 no cambia.[^resoluciones]

Segunda liberación, condicionada y no aprobada ahora: caja 9 + reserva 1 = **10**;
tiempo M1-M3 59 + reserva de cierre 2 = **61**. Total **71**, disjunto de la
primera liberación de caja 0 / tiempo 8. Es también 68 operativos (9 + 59) más
3 de reservas (1 + 2).

Estimado hasta cerrar M3, sin reservas ni núcleo: **18-73** (tiempo
14,3625-58,265625 + caja 2,3-8,625 + validación previa 1,4875-6,35 =
18,15-73,240625), contra el techo de 79.

Sensibilidad (detalle en el Anexo E, «Sensibilidad del pedido mínimo»)[^business-case]:
el techo de 59 tiene 0,734375 de holgura. La rompen, cada una con el resto al
máximo, una tarifa media de formación de más de 36,1 USD/h, DevOps sin el tope
de la unión (60,890625) o una apreciación real del peso de más de 1,26%
(0,734375 / 58,265625); en M7-M9 y M10-M12 el margen es 0,37%. El techo de caja de 9 admite hasta 6,33 de legal con la
provisión de herramientas entera. Cualquiera obliga a recostear antes de M1.

Límite acumulado propuesto **79 = 8 + 71**, caja **10** / tiempo **69**
(59 + preparación técnica 3 + validación organizativa 5 + cierre 2). El techo
anterior era 74; el adicional organizativo agrega 5 sin cambiar caja ni M1-M3.

El Directorio fija hoy, al aprobar el plan, 79 hasta cerrar M3 (85 con el
núcleo), 121 como suma de techos del año (118 sin gastar reservas) y un techo
por tramo: M4-M6 16 (caja 2 + tiempo 14), M7-M9 13 (2 + 11) y M10-M12 13
(2 + 11); 79 + 16 + 13 + 13 = 121. Libera hoy solo 8. Núcleo posterior y
continuidad no se liberan hoy: el CEO firma la segunda liberación y cada gate
dentro del techo de su tramo, y el núcleo de 108 h en el gate de salida dentro
de 85, con verificación del CFO; superar el techo de un tramo, o cualquier
camino con espera que supere 121, vuelve al Directorio (R-03, R-04)[^resoluciones].

## Continuación condicional y salida

Por trimestre M4-M12, solo mantener controles, registro, prácticas y medición:
tech lead / líder interno (oficina del CAIO) 36-60 h; DevOps 8-16; QA 32-48;
IA 4-8; Seguridad 12-20; seniors 16-24; analista 8-16; staff 12-20; Personas
4-6 para comunicación del cambio, frenos y agendas. Subtotal de mantenimiento
132-218 h por trimestre; con el verificador senior independiente, que reproduce
los indicadores de la lectura del gate (4-5 h), 136-223 h. Son supuestos nuevos, no fracciones heredadas de plataforma. Caja
0-1,5 mil más 15%, provisión única para herramientas o consulta legal puntual
(hasta 1,74 mil antes de contingencia: 4,6-7,0 h a 375-250 USD/h, con las
consultas del Anexo C)[^gobierno]; sin nuevo dictamen salvo cambio de alcance, que
exige recosteo.

Personas suma 4-6 h × 9,375-31,25 USD/h = 0,0375-0,1875 mil por trimestre y el
verificador 4-5 h × 18,75-46,875 = 0,075-0,234375. Tiempo por trimestre: M4-M6
3,3375-13,784375 (techo 14), M7-M9 y M10-M12 2,725-10,959375 (techo 11). Ningún
techo cambia; el verificador a 6 h no entraría (11,00625 contra 11).

Dónde se costea lo que no tiene fila propia, sin subir techos (detalle y cuentas
en el Anexo E, «Oficina del CAIO, líder, cambio y legal después de M1»)[^business-case]:
el CAIO es un rol existente reasignado y su dedicación es la del líder interno
(48-96 h en M1-M3; dentro de las 36-60 h del tech lead después). Un líder al 20%
como fila propia (96 h, 2,7-6,0 mil por trimestre) no entra: 13,784375 + 6,0 = 19,78
contra 14 en M4-M6. De las 36-60 h del tech lead, 14-24 son de la oficina del
CAIO. La asesoría laboral de R-20 va dentro de las 8-16 h del
dictamen si la cotización deja 2-4 h; si no, queda fuera de 79 y la decide el
Directorio (R-20)[^resoluciones]. Herramientas y legal al máximo en un mismo trimestre no entran
(3,0 × 1,15 = 3,45 contra 2): se recostea o vuelve al Directorio.

Antes de M6 se agrega descubrimiento sobre integración con documentación/soporte
actuales: tech lead 8-16 h, senior 8-16, analista 16-24, staff Comercial/Producto
4-8. Total 36-64 h, costo 0,6125-2,825 mil, una sola vez en M4-M6.
Observar tiempo a primera integración exitosa y consultas por intento, sin
prometer mejora, construir producto ni cargar ingresos. La observación requiere
acceso/consentimiento y no publica datos de clientes.

Tras corte del experimento, núcleo restringido por trimestre: 12 h tech lead,
12 Seguridad y 12 staff para accesos, incidentes y revisión de permisos;
36 h a costo 0,675-1,6875 mil, techo 2 mil por trimestre, sin caja nueva.
Incluye una sesión del AI Council de 2 h por trimestre, no la cadencia mensual:
30 h de Council (1,40625 mil a máximo) más el núcleo darían 3,09 contra 2.
No mantiene un piloto activo ni autoriza uso que requiera controles no cubiertos.

Después de M3: 108 h y techo 6 mil de tiempo para M4-M12, en reemplazo de la
continuación, nunca además de ella. Los 6 requieren **aprobación explícita en el
gate de salida M3** y no forman parte del límite acumulado de 79.

Sin capacidad para el núcleo, excluir/suspender uso hasta que se cubran
obligaciones; no se abandona una obligación legal.

Proyección anual sin esperas ni reservas gastadas: caja 2,3-13,8 y tiempo con
preparación técnica y validación organizativa 24,6375-100,31875; económico
26,9375-114,11875, **≈71 (27-114)** (medio 70,53).

Los acumulados incluyen preparación imputada a 2026 más ejecución 2027;
no representan exclusivamente presupuesto 2027.

Suma de techos por tramo y preparación **118** (caja 15 = 9 + 2 + 2 + 2 / tiempo
103 = 8 + 59 + 14 + 11 + 11); con cierre **121**. Son techos fijados, no gasto
liberado ni autorización anual.

### Espera del mes 9 y pérdidas de salida

La tabla expresa exposición máxima propuesta, separada en caja y tiempo
valorizado. Sus totales no representan íntegramente desembolso de caja ni
pérdida económica incremental.

Con el gate de valor del Anexo B, el mes 6 no lee valor y no espera por
medición: decide por adopción, calidad, costo y controles, y corta solo por daño
de calidad o caída demostrada. Solo el mes 9 puede abrir una espera, si el
estimado es ≥ +5% sin que el peor caso pase de 0.[^arquitectura]

La espera de seis semanas exige aprobación propia antes de iniciarse, sin
expansión ni descubrimiento nuevo. Supuesto de carga por tareas, equivalente a
mitad del mantenimiento trimestral, sin equivalencia calendario automática:

| Rol | Horas por espera | Tarea |
|---|---|---|
| Tech lead | 18-30 | Coordinar seguimiento y leer la nueva medición |
| DevOps | 4-8 | Mantener configuración y exportar |
| QA / datos | 16-24 | Repetir extracción, enlaces y cálculo |
| IA aplicada | 2-4 | Sostener prácticas congeladas |
| Seniors | 8-12 | Revisar prácticas y registrar calidad |
| Seguridad | 6-10 | Revisar accesos, incidentes y residual |
| Analista | 4-8 | Conciliar registros |
| Staff | 6-10 | Documentar decisión y permisos |

Total **64-106 h**, costo **1,30625-5,26875**, techo **6** de tiempo. Herramientas
0-0,75 mil +15%: caja **0-0,8625**, techo **1** por espera. Las reservas 1 de
caja / 2 de tiempo siguen vigentes una sola vez; no compran medición.

La espera sustituye la porción de continuidad utilizada, sin sumar el trimestre
completo ni núcleo simultáneo. Si pasa, recostear el resto descontando tareas ya
financiadas; si no alcanza para controles/medición, cortar o recostear antes.

Tras espera y corte, núcleo parcial TL 6 + Seguridad 6 + staff 6 = 18 h, costo
0,3375-0,84375, techo 1 y caja 0. Se agrega solo el núcleo de tramos posteriores
completos; esta distribución de tareas requiere validar la cadencia obligatoria.

| Salida | Exposición máxima acumulada hasta cerrar, caja / tiempo → total | Núcleo restante, h / techo | Máximo anual con núcleo aprobado al salir |
|---|---|---|---|
| Previo a M1 | 0 / 8 → 8 | — | 8, sin inicio M1-M3 |
| M3 inmediato | 10 / 69 → 79 | 108 / 6 | 85 |
| Corte en M6 | 12 / 83 → 95 | 72 / 4 | 99 |
| M9 inmediato | 14 / 94 → 108 | 36 / 2 | 110 |
| Espera M9 vencida | 15 / 100 → 115 | 18 / 1 | 116 |
| M12 | 16 / 105 → 121 | — | 121, sin régimen posterior |

La espera va dentro del techo de M10-M12. Sus techos 1 / 6 son subtopes de
2 / 11, y el resto del trimestre se recostea contra lo que la espera calculó o
ejecutó: 1,30625-5,26875 + 1,41875-5,690625 = 2,725-10,959375 de tiempo y
0,8625 + 0,8625 = 1,725 de caja. Así ningún camino supera el techo de su tramo
ni 121: corte en M6, 95 (99); en M9, 108 (110); espera del mes 9 que vence, 115
(116); que pasa, 121. La espera del mes 6 (102 / 105) ya no existe.

El máximo propuesto de corte inmediato M6 es **95**, incluidos los 5 de
validación organizativa. Regla del Directorio: una sola espera, en el mes 9; el AI Council recomienda abrirla, el CFO verifica y el CEO
firma el subtramo dentro del techo de su tramo (R-27)[^resoluciones]. Sin segunda espera:

Si no pasa valor/calidad con versión congelada,
cortar el frente interno y aplicar precedencia de F si otro frente continúa.

Las esperas no están incluidas en la proyección anual sin esperas. Si el
recosteo del resto de un tramo no entra en lo que queda de su techo, se reduce
el alcance o vuelve al Directorio. Toda exposición incluye cierre una
sola vez y presupone el mínimo sin plataforma ni producto.

# Por qué es razonable

Concilia actividades publicadas de B/C/D y conserva soporte explícito de la
prueba. Un mínimo puede tener poca caja y requerir tiempo sustantivo. Continuar,
cortar o evaluar plataforma en M3/M6/M9 son decisiones separadas.

# Qué lo invalidaría

Fuentes no exportables, tareas compartidas distintas, falta de perfiles o agendas,
más de una corrección, precios fuera del techo, control obligatorio no demostrable,
cambio contractual o base que no resuelve. Se reduce/resecuencia o recostea.

# Cautelas

Primera liberación: la aprueba el Directorio al aprobar el plan, antes de
trabajar; no consta preparación ejecutada ni costo hundido de esa etapa
(R-02)[^resoluciones]. Productor, verificador y firmante se
separan por rol y las personas se nombran en el acta de cada liberación (R-06)[^resoluciones].
Los solapes rigen por R-26 y los precios siguen sin cotizar: cada cotización la
verifica el CFO antes de contratar. La reserva de capacidad se confirma por
persona y semana en la matriz de la validación; sin esa confirmación no se libera
M1-M3 y se reduce o resecuencia con recosteo (R-05)[^resoluciones].
La base puede extenderse hasta semana 8; básico, intermedio y prueba se desplazan
a semana 9 y se revisa completitud M3. No se promete señal causal M3.
Beneficio de caja estimado: 0; ingreso nuevo: 0. Capacidad sin cifra hasta medir;
ni horas futuras financian agendas iniciales ni una hora se cuenta como ahorro
y venta a la vez. El costo cargado no prueba contribución perdida: conciliar
en privado sin duplicarla.

La verificación de esta ficha registra la revisión humana de la propuesta de
diseño. El costeo por sí solo no verifica las fichas referidas ni acredita
cotizaciones, agendas, ejecución o autorizaciones empresariales.

Cambios posteriores a la verificación registrada, que su alcance no cubre y
requieren una nueva revisión humana: la demanda M1-M3 baja de 970-1.350 h a
970-1.346 h por R-25; los techos por tramo 16/13/13 y la regla de esperas dentro
del techo de su tramo (R-03, R-04, R-27); la fila de Personas de 4-6 h por
trimestre, con la continuidad en 132-218 h; la provisión de caja única para herramientas o consulta legal
después de M1; la asesoría laboral de R-20; la cadencia del Council tras un
corte; el estimado 18-73 hasta M3 y la sensibilidad del techo de 59; el
verificador senior independiente por lectura y la eliminación de la espera del
mes 6 por el gate de valor del Anexo B, con la proyección en 26,9375-114,11875.[^resoluciones][^business-case]

[^arquitectura]: Anexo B, actividades técnicas y protocolo de medición como insumos de diseño.
[^gobierno]: Anexo C, gobierno mínimo, legal y verificación de controles como insumos de diseño.
[^personas]: Anexo D, «Insumo para el paquete mínimo», formación y soporte de adopción.
[^business-case]: Anexo E, «Pedido inicial: paquete mínimo», continuidad, esperas y exposiciones de salida.
[^costo-rol]: Costo mensual cargado por rol, rangos supuestos de planificación sujetos a contraste privado.
[^convenciones]: Convenciones de calendario y cálculo del plan, 160 h por mes, 480 h por tramo y redondeo de techos.
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
