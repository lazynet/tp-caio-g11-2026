---
type: Supuesto
title: "Paquete mínimo de aprendizaje sin plataforma central"
description: "Finanzas concilia los insumos de B/C/D para medir valor con controles probados y herramientas existentes, con techos por etapa y salida acotada."
status: draft
tags: [supuesto, finanzas, capacidad, controles]
generated: { by: codex/gpt-6, at: 2026-10-15T22:00:00Z }
---

# Supuesto

Propuesta de Finanzas de ronda 11, pendiente de aprobación humana. No es una
cotización ni prueba de disponibilidad. El detalle reproducible vive en el anexo E,
«Pedido inicial: paquete mínimo»; B/C/D son insumos de diseño, no evidencia externa.

## Alcance y conciliación M1-M3

Herramientas existentes, cuatro superficies y cohorte propia de 15-20 personas.
Se pagan controles aplicables equivalentes para cada uso habilitado: política,
matriz, inventario, dictamen legal, configuración, pruebas negativas, corrección,
verificación independiente y aceptación del residual. Sin gateway ni plataforma
central, producto, avanzado, red de champions al 10% o contractor continuo.

Supuesto explícito de unión de actividades, a validar por sus dueños:

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

## Costos y límites

Costo horario = rango mensual del [rol](/supuestos/costo-cargado-por-rol.md)/160;
formación distribuida a 10-35 USD/h, piso ya usado en D, no tarifa de venta.
Persona-tramo de 480 h y techos hacia arriba según
[convenciones](/supuestos/convenciones-de-calculo.md).

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

Techos iniciales: caja 9 + reserva 1 = **10**; tiempo 59 + preparación 3 +
reserva de cierre 2 = **64**. Total autorizado hoy propuesto: **74** económicos,
sin núcleo posterior ni continuidad autorizados.

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
gate de salida M3** y no forman parte de los 74 iniciales.

Sin capacidad para el núcleo, excluir/suspender uso hasta que se cubran
obligaciones; no se abandona una obligación legal.

Proyección anual sin esperas ni reservas gastadas: caja 2,3-13,8 y tiempo con
preparación 23,225-94,96875; económico 25,525-108,76875, **≈67 (26-109)**.

Suma de techos por tramo y preparación **113** (caja 15 / tiempo 98); con cierre
**116**. Es una proyección condicional, no autorización anual.

### Esperas M6/M9 y pérdidas de salida

Cada espera de seis semanas exige aprobación propia antes de iniciarse, sin
expansión ni descubrimiento nuevo. Supuesto de carga por tareas, equivalente a
mitad del mantenimiento trimestral, no conversión de semanas a meses:

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

| Salida | Pérdida acumulada hasta cerrar, caja / tiempo → total | Núcleo restante, h / techo | Máximo anual con núcleo aprobado al salir |
|---|---|---|---|
| M3 inmediato | 10 / 64 → 74 | 108 / 6 | 80 |
| M6 inmediato | 12 / 78 → 90 | 72 / 4 | 94 |
| Espera M6 vencida | 13 / 84 → 97 | 54 / 3 | 100 |
| M9 inmediato | 14 / 89 → 103 | 36 / 2 | 105 |
| Espera M9 vencida | 15 / 95 → 110 | 18 / 1 | 111 |
| M12 | 16 / 100 → 116 | — | 116, sin régimen posterior |

Las filas de espera suponen continuidad sin esperas anteriores; si una espera
M6 pasa y luego se espera en M9, recomponer los subtramos antes de autorizar.

89 era el máximo de corte inmediato M6 del costeo anterior; corregida Seguridad
es 90. Nunca fue el máximo tras esperar. Una sola espera por gate; propuesta
pendiente de ratificación para M9:

Si no pasa valor/calidad con versión congelada,
cortar el frente interno y aplicar precedencia de F si otro frente continúa.

Las esperas no están incluidas en la proyección anual sin esperas: una secuencia
nueva se recompone por subtramos y redondeos. Toda pérdida incluye cierre una
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

Responsables humanos, ratificación del calendario, solapes y precios: pendientes.
La base puede extenderse hasta semana 8; básico, intermedio y prueba se desplazan
a semana 9 y se revisa completitud M3. No se promete señal causal M3.
Beneficio de caja estimado: 0; ingreso nuevo: 0. Capacidad sin cifra hasta medir;
ni horas futuras financian agendas iniciales ni una hora se cuenta como ahorro
y venta a la vez. El costo cargado no prueba contribución perdida: conciliar
en privado sin duplicarla. Ningún supuesto pasa a verified por este costeo.
