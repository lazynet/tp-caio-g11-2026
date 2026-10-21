---
type: Supuesto
title: "Paquete mínimo de aprendizaje sin plataforma central"
description: "Finanzas concilia los insumos de B/C/D para medir valor con controles probados y herramientas existentes, con techos por etapa y salida acotada."
status: verified
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
generated: { by: codex/gpt-6, at: 2026-10-20 }
---

# Supuesto

Propuesta de Finanzas con validación inicial, elegida y revisada por Martín para
el plan. El acuerdo del equipo y la autorización de Acme Labs siguen sin
acreditar; las estimaciones requieren cotización y confirmación de disponibilidad.

El detalle reproducible vive en el Anexo E, «Pedido inicial: paquete mínimo».[^business-case]
B/C/D son insumos de diseño, no evidencia externa; las fichas referidas conservan
su propio estado de revisión y sus cautelas.[^arquitectura][^gobierno][^personas]

## Alcance y conciliación M1-M3

Herramientas existentes, cuatro superficies y cohorte propia de 15-20 personas.
Se pagan controles aplicables equivalentes para cada uso habilitado: política,
matriz, inventario, dictamen legal, configuración, pruebas negativas, corrección,
verificación independiente y aceptación del residual. Sin gateway ni plataforma
central, producto, avanzado, red de champions al 10% o contractor continuo.

Supuesto explícito de unión de actividades, a validar por sus dueños:[^arquitectura][^gobierno][^personas]

| Rol / actividad | Horas M1-M3, sin preparación | Derivación y solape tratado |
|---|---|---|
| Tech lead / arquitectura / adopción | 146-276 | B 24-40 + C 22-36 (política, legal y Council) + D «Insumo para el paquete mínimo»: 48-96 líder, 16-32 facilitación y 8-16 managers + E anterior 40-80 diseño de prueba; menos preparación 12-24 |
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

Si no se confirma, recostear antes de iniciar; no declarar estos solapes como
ahorro acordado. Roles acumulados requieren agenda por persona.

Las restas de preparación de TL y QA emparejan extremos del mismo escenario;
no son restas de intervalos independientes. El remanente por actividad debe
conciliarse antes de ejecutar; si esa correspondencia no se confirma, recostear.

## Reserva propuesta de capacidad M1-M3

Supuesto de planificación para solicitar capacidad; Operaciones y los managers
deben confirmar personas, agendas y trabajo desplazado antes de cada actividad.
La elección para el borrador no acredita disponibilidad empresarial.

| Destino | Reserva propuesta | Derivación |
|---|---|---|
| Soporte clave, repartido entre roles | Hasta 720 h / 1,5 FTE de costeo | 1,5 × 480 h; demanda estimada de soporte 430-690 h |
| Formación básica | 360-420 h | 60-70 personas × 6 h |
| Formación intermedia | 180-240 h | Cohorte de 15-20 personas × 12 h |
| Máximo combinado | 1.380 h / 2,875 FTE de costeo | 720 + 420 + 240; no incluye preparación previa ni cierre condicional |

El soporte tiene 30 h de margen sobre su demanda máxima estimada (720 − 690).
Ese margen agregado no cubre automáticamente faltantes de otro rol o semana.
La formación de quienes también producen o verifican se suma en su agenda.

La demanda costeada sigue en 970-1.350 h; la reserva de capacidad no es ejecución
ni una reserva financiera adicional. El margen de 30 h no tiene actividad ni
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

Sin esas condiciones la ventana no comienza. Los responsables humanos se deben
designar; los responsables del TP no sustituyen a quienes liberan agendas,
aceptan riesgo o aprueban presupuesto en Acme Labs.

**Validación organizativa adicional**, estimación de Finanzas (agente) de 60-96 h; la estimación humana de Personas (#18, pregunta 3) sigue pendiente. Costo
horario según [costo por rol](/supuestos/costo-cargado-por-rol.md)/160;[^costo-rol] las horas
incluyen entrevistadores, entrevistados, managers, staff y autoridad que decide:

| Rol | Horas | USD/h | Tiempo, miles de USD |
|---|---|---|---|
| TL, coordinación, managers y autoridad de decisión | 16-24 | 28,125-62,5 | 0,45-1,5 |
| Analista funcional | 20-32 | 12,5-34,375 | 0,25-1,1 |
| Staff de Operaciones, Talento, Comercial y Finanzas | 16-24 | 9,375-31,25 | 0,15-0,75 |
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
No se presume absorbido en 59 mil, 720 h ni las 30 h de margen de M1-M3.

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

Condiciones: diagnóstico y padrón aceptados; matriz de capacidad validada por
Operaciones/managers; autoridades identificadas; viabilidad técnica/de medición,
recosteo y presupuesto 2027 aprobados por la autoridad presupuestaria correspondiente.

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

Seguridad provisional cuesta 0,6375-2,53125 mil. Soporte clave total: 430-690 h,
8,8875-35,18125 mil, 0,8958-1,4375 FTE. Con formación distribuida 540-660 h,
M1-M3 totaliza **970-1.350 h / 2,0208-2,8125 FTE**, costo **14,2875-58,28125**.

Segunda liberación, condicionada y no aprobada ahora: caja 9 + reserva 1 = **10**;
tiempo M1-M3 59 + reserva de cierre 2 = **61**. Total **71**, disjunto de la
primera liberación de caja 0 / tiempo 8.

Límite acumulado propuesto **79 = 8 + 71**, caja **10** / tiempo **69**
(59 + preparación técnica 3 + validación organizativa 5 + cierre 2). El techo
anterior era 74; el adicional organizativo agrega 5 sin cambiar caja ni M1-M3.

Núcleo posterior y continuidad no están autorizados. La elección del borrador
no libera las dos etapas: cada una requiere su autorización empresarial.

## Continuación condicional y salida

Por trimestre M4-M12, solo mantener controles, registro, prácticas y medición:
tech lead 36-60 h; DevOps 8-16; QA 32-48; IA 4-8; Seguridad 12-20;
seniors 16-24; analista 8-16; staff 12-20. Total 128-212 h por trimestre.
Son supuestos nuevos, no fracciones heredadas de plataforma. Caja 0-1,5 mil
más 15%; sin nuevo dictamen salvo cambio de alcance, que exige recosteo.

Antes de M6 se agrega descubrimiento sobre integración con documentación/soporte
actuales: tech lead 8-16 h, senior 8-16, analista 16-24, staff Comercial/Producto
4-8. Total 36-64 h, costo 0,6125-2,825 mil, una sola vez en M4-M6.
Observar tiempo a primera integración exitosa y consultas por intento, sin
prometer mejora, construir producto ni cargar ingresos. La observación requiere
acceso/consentimiento y no publica datos de clientes.

Tras corte del experimento, núcleo restringido por trimestre: 12 h tech lead,
12 Seguridad y 12 staff para accesos, incidentes y revisión de permisos;
36 h a costo 0,675-1,6875 mil, techo 2 mil por trimestre, sin caja nueva.
No mantiene un piloto activo ni autoriza uso que requiera controles no cubiertos.

Después de M3: 108 h y techo 6 mil de tiempo para M4-M12, en reemplazo de la
continuación, nunca además de ella. Los 6 requieren **aprobación explícita en el
gate de salida M3** y no forman parte del límite acumulado de 79.

Sin capacidad para el núcleo, excluir/suspender uso hasta que se cubran
obligaciones; no se abandona una obligación legal.

Proyección anual sin esperas ni reservas gastadas: caja 2,3-13,8 y tiempo con
preparación técnica y validación organizativa 24,225-99,06875; económico
26,525-112,86875, **≈70 (27-113)**.

Los acumulados incluyen preparación imputada a 2026 más ejecución 2027;
no representan exclusivamente presupuesto 2027.

Suma de techos por tramo y preparación **118** (caja 15 / tiempo 103); con cierre
**121**. Es una proyección condicional, no autorización anual.

### Esperas M6/M9 y pérdidas de salida

La tabla expresa exposición máxima propuesta, separada en caja y tiempo
valorizado. Sus totales no representan íntegramente desembolso de caja ni
pérdida económica incremental.

Cada espera de seis semanas exige aprobación propia antes de iniciarse, sin
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
| M6 inmediato | 12 / 83 → 95 | 72 / 4 | 99 |
| Espera M6 vencida | 13 / 89 → 102 | 54 / 3 | 105 |
| M9 inmediato | 14 / 94 → 108 | 36 / 2 | 110 |
| Espera M9 vencida | 15 / 100 → 115 | 18 / 1 | 116 |
| M12 | 16 / 105 → 121 | — | 121, sin régimen posterior |

Las filas de espera suponen continuidad sin esperas anteriores; si una espera
M6 pasa y luego se espera en M9, recomponer los subtramos antes de autorizar.

El máximo propuesto de corte inmediato M6 es **95**, incluidos los 5 de
validación organizativa, sin esperar. Una sola espera por gate; la propuesta
sigue pendiente de ratificación para M9:

Si no pasa valor/calidad con versión congelada,
cortar el frente interno y aplicar precedencia de F si otro frente continúa.

Las esperas no están incluidas en la proyección anual sin esperas: una secuencia
nueva se recompone por subtramos y redondeos. Toda exposición incluye cierre una
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

Responsables humanos, ratificación empresarial del calendario, solapes y precios:
pendientes. Primera liberación e imputación 2026 requieren aprobación empresarial
antes de trabajar; no consta preparación ejecutada ni costo hundido de esa etapa.
La reserva de capacidad es un supuesto del borrador, pendiente de confirmación
por persona y semana; no libera por sí sola el hito de validación organizativa.
La base puede extenderse hasta semana 8; básico, intermedio y prueba se desplazan
a semana 9 y se revisa completitud M3. No se promete señal causal M3.
Beneficio de caja estimado: 0; ingreso nuevo: 0. Capacidad sin cifra hasta medir;
ni horas futuras financian agendas iniciales ni una hora se cuenta como ahorro
y venta a la vez. El costo cargado no prueba contribución perdida: conciliar
en privado sin duplicarla.

La verificación de esta ficha registra la revisión humana de la propuesta de
diseño. El costeo por sí solo no verifica las fichas referidas ni acredita
cotizaciones, agendas, ejecución o autorizaciones empresariales.

[^arquitectura]: Anexo B, actividades técnicas y protocolo de medición como insumos de diseño.
[^gobierno]: Anexo C, gobierno mínimo, legal y verificación de controles como insumos de diseño.
[^personas]: Anexo D, «Insumo para el paquete mínimo», formación y soporte de adopción.
[^business-case]: Anexo E, «Pedido inicial: paquete mínimo», continuidad, esperas y exposiciones de salida.
[^costo-rol]: Costo mensual cargado por rol, rangos supuestos de planificación sujetos a contraste privado.
[^convenciones]: Convenciones de calendario y cálculo del plan, 160 h por mes, 480 h por tramo y redondeo de techos.
