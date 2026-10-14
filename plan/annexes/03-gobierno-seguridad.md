---
owner: governance
status: draft
title: "Anexo C — Gobierno, seguridad y compliance"
---

# Anexo C — Gobierno, seguridad y compliance

Slide que sustenta: [Slide 5 — Gobierno y seguridad](../slides.md).

## Objetivo

Sustentar tres pedidos al board: aprobar un modelo de gobierno liviano (un AI Council
de cinco asientos que se apoya en el comité de tecnología, sin gatekeeper), ratificar
la política de IA que hoy está en borrador y financiar por gate un paquete de controles:
el gobierno mínimo siempre, los controles técnicos de la plataforma si G1 encuentra una
señal y la demostración externa si la señal contractual llega a G3. El gobierno tiene que habilitar la entrega: cada control
declara cuánta velocidad cuesta y cuándo se abandona.

La IA que Acme Labs vende a bancos y fintechs es la que más exige: hoy no hay IA en
producción dentro de lo que se vende ([ficha](../../context/hechos/ia-en-producto-y-oferta.md)),
así que el gobierno se construye antes del primer caso, no después del primer incidente.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Tamaño de la organización | 60-70 personas, ~80% en Operaciones y Tecnología | [Ficha](../../context/hechos/tamano-y-estructura.md) |
| Política de IA | v1.0 en borrador desde abril de 2026, sin ratificación del Directorio, sin matriz de restricciones de clientes | [Ficha](../../context/hechos/gobierno-y-politica-ia.md) |
| Inventario de casos de uso y registro de riesgos de IA | No existen | [Ficha](../../context/hechos/gobierno-y-politica-ia.md) |
| Herramientas aprobadas | 3 (Claude Team, GitHub Copilot, Gemini en Workspace); 40-45 seats de Claude | [Ficha](../../context/hechos/uso-ia-interno.md) |
| Certificación de seguridad | ISO/IEC 27001 de la organización; un producto propio no tiene la suya | [Ficha](../../context/hechos/seguridad-y-certificaciones.md) |
| Controles específicos de IA (red teaming, DLP sobre prompts) | Sin evidencia | [Ficha](../../context/hechos/seguridad-y-certificaciones.md) |
| Concentración de capacidad | Gobierno y seguridad dependen de pocas personas | [Ficha](../../context/hechos/tamano-y-estructura.md) |
| Apetito de riesgo de los clientes | Prohíben por defecto modelos externos sobre su código y datos, salvo cláusula y controles demostrables. La evidencia contractual se junta en el Q1 y se lee en G1 (D9b) | [Supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md) |
| Datos disponibles para IA | Internos; los datos productivos de clientes no | [Supuesto](../../context/supuestos/disponibilidad-de-datos.md) |
| Inversión incremental del plan | 1%-3% de la facturación anual, más 10%-15% del tiempo de personas clave | [Supuesto](../../context/supuestos/capacidad-de-inversion.md) |
| Costo cargado por rol | Tech lead 4.500-10.000 USD/mes; senior DevOps 3.000-7.500; analista funcional 2.000-5.500; staff 1.500-5.000. Rangos amplios, no calibrados contra la nómina | [Supuesto](../../context/supuestos/costo-cargado-por-rol.md) |
| Costo horario por rol | Tech lead 28-63 USD/h; senior DevOps 19-47; analista funcional 13-34; staff 9-31. Es el costo mensual dividido 160 h; cada actividad usa el rol que la hace, sin promedios de la empresa | Supuesto del equipo, derivado del anterior |
| Disponibilidad | Utilización facturable ~83% y bench casi nulo: el tiempo de gobierno compite con horas facturables | [Ficha](../../context/hechos/capacidad-y-utilizacion.md) |
| Los clientes principales siguen | La facturación está muy concentrada en pocos clientes (rango en la ficha) | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |

## Evidencia

### Punto de partida frente a la meta a 12 meses

| Métrica | Hoy | Esperado a los 12 meses | Fuente |
|---|---|---|---|
| Política de IA | Borrador v1.0, sin ratificar | Ratificada por el Directorio, con revisión anual y onboarding | [Ficha](../../context/hechos/gobierno-y-politica-ia.md) |
| Inventario de usos de IA | No hay | 100% de las herramientas, servidores MCP, funciones de IA embebidas y casos de producto | Objetivo propuesto por el equipo |
| Matriz de restricciones por cliente | No hay; se valida a mano | Cubre los clientes que concentran la mayor parte de la facturación (la ficha da el alcance) | [Ficha](../../context/hechos/cartera-y-concentracion.md) |
| Registro de riesgos de IA | No hay | Vivo, revisado cada mes por el Council | Objetivo propuesto por el equipo |
| Controles técnicos de IA | Sin evidencia | Con señal en G1: pasarela de salida y DLP, logs de acciones, red team interno; el externo, si se financia la capa D. Sin señal: *hooks* y escaneo de secretos en el equipo y red team acotado (D9c) | Objetivo propuesto por el equipo |
| Certificación | ISO 27001 vigente | ISO 27001 con alcance extendido a IA; ISO 42001 como decisión del Q4, no como meta | [Ficha](../../context/hechos/seguridad-y-certificaciones.md) |

Las metas son objetivos del equipo, no benchmarks: se calibran con la línea base que
sale del Q1.

### Qué enseña el piloto interno

El piloto de abril de 2026 cumplió valor y adopción, pero falló en capacitación: solo
el 17% completó los tres cursos obligatorios y el 58% chocó con el límite de uso
([ficha](../../context/hechos/encuesta-y-pilotos-ia.md), n=12 y autoseleccionado). Dos
lecciones para el gobierno: un control que depende de que la gente lea un curso no es un
control, y un control que frena el uso empuja a la gente fuera del sistema oficial (el
anti-patrón del *governance perfecto*, [Council vs CoE](../../material/conceptos/m1u4-council-vs-coe.md)).

### Marco regulatorio: lo propio y lo heredado

Acme Labs no es entidad financiera: es **tercero** de bancos y PSP
([ficha](../../context/hechos/regulacion-clientes-financieros.md)). Se separa lo que
obliga a Acme Labs de lo que le llega por contrato.

| Norma o marco | Quién está obligado | Cómo llega a Acme Labs | Estado de verificación |
|---|---|---|---|
| BCRA Com. "A" 7777 y 7783 (gobierno de IA propia y de terceros, aviso al cliente de uso de IA, explicabilidad) | Bancos y PSP clientes | **Heredada**: por contrato y por el análisis de riesgos de terceros del cliente | Leída la [A 7777, sección 4.6](https://www.bcra.gob.ar/pdfs/comytexord/A7777.pdf) (versión 1a, vigencia 06/09/2023). **Respalda** que la entidad debe identificar y documentar el uso de IA "por sí o por terceros", asignar roles, analizar riesgos y avisar al cliente. **No respalda** que el banco le exija a Acme Labs controles concretos ni que le compre IA: eso, si existe, llega por contrato (ver D9b). La sección 10 (terceras partes) no se leyó, y la vigencia en 2026 no está cotejada |
| BCRA Com. "A" 6885 (PSP que ofrecen cuentas de pago) | Un producto propio de medios de pago, **si** obtiene la habilitación | **Propia y directa** en ese caso | Solo verificada por encabezado y alcance |
| Ley 21.526, arts. 39-40 (secreto financiero) | Entidades y su personal | **Heredada**: restringe qué información del banco puede salir hacia un modelo | Verificada contra la ley |
| Ley 25.326 (datos personales; prohíbe transferir a países sin protección adecuada) | Quien trata datos personales | **Propia**: condiciona enviar datos a modelos alojados en el exterior | Verificada; el rol de Acme Labs (responsable o encargado) falta confirmarlo con asesoría legal |
| EU AI Act (Reg. 2024/1689, modificado por el Omnibus 2026/1744) | Proveedores y desplegadores con sistemas o resultados usados en la UE (art. 2.1.c) | **No aplica por defecto**; se activa si un cliente opera en la UE o el resultado se usa allá | Fechas leídas de una copia del DOUE; falta cotejar con EUR-Lex ([huecos](../../material/huecos.md)) |
| NIST AI RMF 1.0 | Nadie (voluntario) | **Voluntaria**: cada riesgo del registro lleva su función (Govern, Map, Measure, Manage) y su evidencia; se declara alineación, no cumplimiento | Confirmado en la página de NIST; el mapeo es por función, las subcategorías (por ejemplo GOVERN 1.6) no se verificaron |
| ISO/IEC 42001:2023 | Nadie (certificación voluntaria) | **Voluntaria**: se alinea con brecha documentada, no se certifica en el año | Confirmada la edición; ver el mapeo en Riesgos y D7 |
| Guía SIGEN 197/2026 | Sector público nacional | **No aplica**; solo si un cliente es un organismo público | Existe; el anexo no se leyó |
| UIF y comunicaciones del producto de medios de pago | Sujetos obligados | Sin evaluar | **Hueco**: no se verificó |

**Rol proveedor frente a desplegador.** Cuando la IA va dentro de un producto que se
vende al banco, Acme Labs es **proveedor** (art. 3.3 del AI Act) y el banco es
**desplegador**; el proveedor es quien sostiene gestión de riesgos, documentación,
registros y supervisión humana. El art. 25 lo vuelve proveedor aun cuando solo integre
con marca propia un motor de terceros, o cuando oriente un modelo genérico a un uso de
alto riesgo ([ficha](../../material/frameworks/eu-ai-act-proveedor-desplegador.md)). La
consecuencia práctica es una **hipótesis**: aun fuera del alcance de la UE, algunos
clientes podrían pedirle por contrato esa disciplina de proveedor. Hay que separar dos
cosas que la hipótesis mezcla. Lo que el regulador le exige al **banco** (la A 7777 lo
obliga a gobernar el uso de IA de sus terceros) es un requisito regulatorio del cliente;
que el banco se lo traslade a Acme Labs como condición de compra o de renovación es una
**exigencia comercial al proveedor**, y eso no está probado. Solo la evidencia
contractual del Q1 (D9b) la confirma o la descarta.

**Calendario.** Según la ficha del Omnibus, el alto riesgo del Anexo III (que incluye el
scoring crediticio) rige desde el 2027-12-02 ([ficha](../../material/conceptos/m1u4-ai-omnibus-sigen.md)),
que **cae dentro de la ventana**: T4 termina en diciembre de 2027. La Comisión Europea
[publica esa fecha](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
y enumera otros usos de alto riesgo además del crédito (empleo y educación, por ejemplo).
Eso confirma el calendario, no que aplique a Acme Labs. EUR-Lex pidió verificación
antirrobot y no se cotejó el texto consolidado: la fecha no va a una slide sin chequearla.

## Riesgos y mitigación

Registro de riesgos inicial (probabilidad e impacto cualitativos, criterio del equipo
hasta tener la línea base del Q1). El rol dueño de cada riesgo, su prueba y su residual
están en la tabla siguiente; las personas quedan pendientes.

| Riesgo | Prob. | Impacto | Mitigación (control) | Disparador de abandono o escalamiento |
|---|---|---|---|---|
| R1. Datos o código de un cliente pasan por un modelo externo sin cláusula | Media | Alto: incumplimiento contractual y secreto financiero, con clientes muy concentrados | Matriz de restricciones por cliente (Q1), default-deny sobre código de cliente; con señal en G1, pasarela con allowlist (Q2) | Un solo incidente confirmado: el Council suspende el uso de IA sobre ese cliente hasta cerrar el análisis de causa |
| R2. Prompt injection indirecta en un agente de código (repositorios, tickets, comentarios de PR, servidores MCP) | Media | Alto | Mínimo privilegio en credenciales, aprobación humana en L3, entorno sin credenciales productivas, validación de salida con código determinístico | Un agente ejecuta una acción fuera de su alcance en pruebas: baja a L2 hasta corregir |
| R3. Agencia excesiva: un agente con permisos de escritura sobre sistemas productivos | Baja | Muy alto | Tope de autonomía por nivel de riesgo (ver Decisiones); L4 solo en sandbox | Cualquier pedido de L4 con acceso a producción pasa a decisión del Council |
| R4. Fuga de secretos en prompts o contexto | Media | Medio-alto | Escaneo de secretos antes del envío, lista cerrada de lo que nunca se envía (ya en la política), rotación | **Primer secreto expuesto confirmado**: se revoca y rota, se contiene el canal afectado y el responsable de seguridad decide con evidencia si se reanuda. **Recurrencia** (más de uno por trimestre): se bloquea el envío automático y se pasa a revisión previa |
| R5. IA embebida en software de terceros activada sin aprobación (por ejemplo, funciones nuevas en la suite ofimática) | Alta | Medio | Inventario que incluye IA embebida; revisión de cambios de proveedor cada mes | Función de IA activa con datos Restringidos: se desactiva y se registra como incidente |
| R6. Cuello de botella: el gobierno frena la entrega y la adopción migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles para riesgo medio, autoservicio para riesgo bajo | Más del 20% de las solicitudes supera el SLA dos meses seguidos: se simplifica el proceso, no se agrega personal |
| R7. Capacidad concentrada: gobierno y seguridad dependen de pocas personas | Alta | Alto | Dos suplentes con runbooks; documentación de decisiones en el inventario | Una persona clave se va y no hay suplente entrenado: congelar altas de casos de riesgo alto |
| R8. Dependencia de un solo proveedor de modelos y cambio de precio o límites | Media | Medio | Diseño neutral al modelo; ver [supuesto](../../context/supuestos/precio-y-dependencia-de-modelos.md) | Aumento de precio o recorte de límites que rompa el presupuesto: revisar proveedor en el Council |
| R9. Declarar controles que no existen (certificación de un producto propio, cumplimiento de IA) | Baja | Muy alto: pérdida de confianza | Toda afirmación comercial sobre seguridad o IA la valida el responsable de seguridad; ningún producto propio se presenta como certificado | Una afirmación sin evidencia aparece en una propuesta: se retira y se corrige el procedimiento |

### Criterio de aceptación del riesgo residual

Propuesta del equipo, que `caio` integra como regla de los gates. El residual se
valora después de probar el control, no antes.

| Residual (prob. / impacto) | Quién lo acepta | Condición |
|---|---|---|
| Baja con impacto hasta Alto, o Media con impacto Medio | Dueño del riesgo | Queda en el registro; el Council lo ve en la revisión mensual |
| Media con impacto Medio-alto o Alto, o Baja con Muy alto | Council, con informe al CEO | Control compensatorio nombrado y fecha de revisión, como máximo el siguiente trimestral |
| Alta con impacto Alto o mayor | Nadie | Se reduce o se suspende el uso; no hay excepción (D7b) |

### Prueba, evidencia y residual de cada riesgo

Cada riesgo lleva su función del NIST AI RMF, un dueño por rol (sale de D2; la persona
queda pendiente), cómo se prueba el control y qué evidencia deja. El residual es un
**objetivo propuesto**, no una medición: se confirma o se corrige con la prueba.

| Riesgo | Función NIST | Dueño del riesgo | Prueba del control | Evidencia esperada | Residual objetivo | Acepta |
|---|---|---|---|---|---|---|
| R1 | Map, Manage | Responsable comercial del cliente | Revisión cruzada de la matriz contra los contratos; dato sintético marcado enviado por cada superficie (Q2) | Matriz versionada con aprobador; informe de *bypass* por superficie; bloqueos en la pasarela | Baja / Alto en lo que pasa por la pasarela (casos propios y, en los regímenes a y c, el agente de código); Media / Alto en el resto | Council |
| R2 | Measure, Manage | Dueño de negocio del caso | Red team interno (Q2) y externo (Q4) con inyección indirecta en repos y tickets sintéticos | Informe de red team con hallazgos y cierre; logs de acciones del agente | Baja / Alto | Dueño |
| R3 | Govern, Manage | Dueño de negocio del caso | Revisión trimestral de los permisos efectivos de cada agente contra su nivel L | Inventario con nivel por agente; exportación de permisos; acta | Baja / Muy alto | Council |
| R4 | Measure, Manage | Responsable de seguridad | Secreto sintético por superficie (ejemplo abajo) | Bloqueo y alerta en la pasarela o en el equipo, según la superficie; ticket del ejercicio de mesa | Baja / Medio-alto donde hay bloqueo técnico; Media / Medio-alto donde solo hay control compensatorio | Dueño; Council si no hay bloqueo técnico |
| R5 | Govern, Map | Responsable de Tecnología | Cruce mensual de las novedades del proveedor contra el inventario | Inventario con fecha de revisión; configuración exportada | Media / Medio | Dueño |
| R6 | Govern, Measure | Responsable de Tecnología | Porcentaje de solicitudes fuera de SLA, desde el registro del intake | Reporte mensual del intake | Baja / Alto | Dueño |
| R7 | Govern | Responsable de Tecnología | El suplente corre el runbook sin el titular en el ejercicio de mesa (Q2 y Q4) | Runbooks versionados; acta del ejercicio | Media / Alto: baja poco en el año | Council |
| R8 | Map, Manage | Responsable de Tecnología | Ensayo de portabilidad del [Anexo B](02-arquitectura.md) | Informe del ensayo con la comparación de calidad | Media / Medio | Dueño |
| R9 | Govern | Responsable de seguridad | Muestreo trimestral de propuestas enviadas contra el registro de afirmaciones validadas | Registro de afirmaciones; muestra revisada | Baja / Muy alto | Council |

### Ejemplo completo: R4, un secreto en un prompt

| Paso | Contenido |
|---|---|
| Riesgo | Una credencial (clave de nube, token de repositorio, cadena de conexión) sale en un prompt hacia un modelo externo. Inherente: Media / Medio-alto |
| Control | Escaneo de secretos en la pasarela antes del envío (previene), alerta al responsable de seguridad (detecta) y runbook de revocación y rotación (corrige). Dueño del control: ingeniería de seguridad |
| Prueba (Q2) | Un juego de secretos **sintéticos** de formatos distintos, enviado por cada superficie de la matriz D8; nunca una credencial real. Criterio propuesto: donde hay bloqueo técnico (casos propios por la pasarela; el agente de código con *hooks* y escaneo en el equipo, y por la pasarela si su régimen la permite), todos bloqueados y alertados; en las superficies sin bloqueo técnico se registra que no hay bloqueo, como resultado esperado y no como falla oculta. En el ejercicio de mesa se mide el tiempo de alerta a revocación; el umbral lo propone seguridad y no está medido |
| Evidencia | Informe de la prueba por superficie y formato, logs de la pasarela con los bloqueos, ticket del ejercicio con sus tiempos y acta del Council. Es la misma evidencia que pediría la auditoría de la ISO 27001 con alcance extendido |
| Residual | Formatos que el escaneo no reconoce (Baja / Medio-alto): lo acepta el responsable de seguridad. Superficies sin bloqueo técnico (chat y escritorio, IDE y suite ofimática; y, en el régimen b, lo que los *hooks* y el escaneo del equipo no reconocen del agente de código) (Media / Medio-alto): lo acepta el Council con control compensatorio (cuentas corporativas, consola de administración, rotación periódica) y revisión en el siguiente trimestral |
| Cuándo vence la aceptación | El primer secreto expuesto por una superficie aceptada reabre la decisión (disparador de R4). El bloqueo de secretos no se relaja nunca (D9) |

### NIST y la ISO 42001: mapeo, evidencia y qué no se afirma

| Función NIST | Qué la implementa acá | Evidencia esperada | Elemento de sistema de gestión ([ISO 42001 según la cursada](../../material/conceptos/m1u4-eu-ai-act-nist-iso.md)) |
|---|---|---|---|
| Govern | Council, derechos de decisión (D2), política, criterio de aceptación | Política ratificada, actas, matriz RACI | Políticas y responsabilidades |
| Map | Intake (D5) con preguntas de contexto, cliente y Anexo III; matriz de restricciones; inventario | Fichas del intake, matriz, inventario | Gestión de riesgos y oportunidades |
| Measure | Pruebas de la tabla anterior, red teams, cobertura de la pasarela | Informes de prueba y métricas de cobertura | Monitoreo |
| Manage | Controles por trimestre (D9), incidentes, aceptación del residual | Tickets, registro de residuales aceptados, revisión trimestral | Procesos y mejora continua |

**Alinear no es certificar.** El NIST AI RMF es voluntario: se declara "alineado", nunca
"cumple". La ISO 27001 es la única certificación que el plan toca, y solo para extender
su alcance. Para la ISO 42001 se documenta la brecha en el Q4 y certificar es una decisión
de ese gate. La frase comercial permitida es "alineado con el NIST AI RMF, brecha frente a
ISO 42001 documentada"; cualquier otra cae en R9. El mapeo de esta tabla es por función:
las cláusulas de la 42001 no se cotejaron contra su texto.

## Decisiones

### D1. Modelo operativo: AI Council liviano, con CoE virtual

| Alternativa | Ventaja | Costo o riesgo | Veredicto |
|---|---|---|---|
| A. Solo un AI Council | Barato, decide rápido | Sin nadie que habilite: queda en comité fantasma | Descartada |
| B. Solo un CoE | Habilita y construye | En 60-70 personas sería una *software factory* central que compite con el delivery | Descartada |
| C. **Council de 5 asientos + CoE virtual** (recomendada) | Decide y habilita con tiempo reasignado, sin estructura nueva | Depende de pocas personas (R7) | **Elegida** |
| D. Asignar la función solo a Tecnología | Cero comités | El negocio pierde el *accountability* del resultado y del riesgo comercial | Descartada |

**Council.** Cinco asientos con voto, y se integra al comité de tecnología que ya aprueba
herramientas ([ficha](../../context/hechos/gobierno-y-politica-ia.md)) para no crear
burocracia paralela: responsable de Tecnología (preside), responsable de seguridad,
responsable de Operaciones (delivery, que es quien conoce las restricciones de cada
cliente), responsable de Experiencia de cliente y comercial, y responsable de Finanzas.
Talento participa cuando hay temas de personas; el CEO es sponsor y última instancia.
Legal: la estructura no muestra un área interna ([ficha](../../context/hechos/tamano-y-estructura.md)),
así que se asume asesoría externa a demanda (ver Cautelas).

**CoE virtual.** No es un equipo nuevo: es el 10%-15% del tiempo de un grupo acotado
([supuesto](../../context/supuestos/capacidad-de-inversion.md)) que mantiene plantillas,
*golden paths*, el inventario y la capacitación, junto con `architect` y `people`. Su
función es habilitar; no aprueba nada que el Council no le delegó.

### D2. Derechos de decisión (una sola A por decisión)

| Decisión | A (decide) | R | C | I |
|---|---|---|---|---|
| Política de IA y sus cambios | Directorio (ratifica) | Responsable de seguridad | Council, CEO | Toda la organización |
| Aprobar una herramienta o modelo nuevo | Responsable de Tecnología | Administrador de licencias | Seguridad, Finanzas | Council |
| Qué datos puede usar un caso | Dueño del dato | Seguridad | Legal externo, Operaciones | Council |
| Usar IA sobre el código o los datos de un cliente (en el horizonte: solo lo que el cliente permite en su entorno; enviarlos a un modelo externo, no antes de G4) | Responsable comercial del cliente | Operaciones | Seguridad, Legal externo | Council |
| Nivel de autonomía de un agente | Dueño de negocio del caso | Ingeniería | Seguridad | Council |
| Salida a producción de una función de IA en el producto | Dueño de producto | Ingeniería | Seguridad, Operaciones | Council |
| Excepción a una política de riesgo alto | Council | Responsable de seguridad | Dueño del caso | CEO |
| Incidente de IA (contención y comunicación al cliente) | Responsable de seguridad | Ingeniería | Comercial, Legal externo | CEO, Council |
| Gasto de IA fuera del presupuesto | Responsable de Finanzas | Tecnología | Council | CEO |

Regla de la cursada: la IA cambia el proceso, no elimina a su dueño
([RACI](../../material/conceptos/m1u4-raci-ownership.md)). El responsable humano de cada
rol queda **pendiente**; el equipo lo asigna y `people` lo desarrolla.

### D3. Ritmo operativo

| Cadencia | Qué se revisa | Dónde se hace |
|---|---|---|
| Semanal (20 min) | Incidentes, solicitudes del intake y bloqueos | Dentro de la reunión técnica existente |
| Mensual (60 min) | Inventario, excepciones, registro de riesgos, adopción y costo de IA | Council, integrado al comité de tecnología |
| Trimestral | Estado de los controles, valor, niveles de autonomía y decisiones de escalar o retirar | Informe al Directorio y gate del plan |

### D4. Governance Stack aplicado a Acme Labs

| Capa | Qué existe | Qué se hace | Trimestre |
|---|---|---|---|
| Principios | 4 principios de la política en borrador (herramientas corporativas, desconfiar del output, responsable humano, lo que no se mide no se justifica) | Se mantienen | Q1 |
| Política | Política de uso aceptable v1.0, sin ratificar | Se ratifica y se parte en tres: uso interno, IA en el producto y proveedores o modelos | Q1-Q2 |
| Estándares | Clasificación de datos en 4 niveles; lista de lo que nunca se envía | Se suma la matriz de restricciones por cliente, la escala de autonomía L0-L4 y la de riesgo | Q1 |
| Controles | Revisión del output, aprobación por el comité, reporte de incidentes sin sanción | Se suman pasarela de salida, DLP, escaneo de secretos y logs de acciones | Q2-Q3 |
| Evidencia | Auditoría mensual de uso | Inventario, registro de riesgos, logs y actas del Council: la evidencia sale del trabajo normal | Q1-Q4 |

### D5. Intake y clasificación de riesgo

Un solo formulario corto, con tres niveles y una lista de prohibidos. Las variables son
autonomía, acceso, consecuencia y reversibilidad
([criterios](../../material/conceptos/m1u4-criterios-gobierno-agentico.md)).

| Nivel | Criterio | Quién aprueba | Plazo objetivo |
|---|---|---|---|
| 1. Bajo | L0-L1, datos Público o Interno, herramienta ya aprobada | Autoservicio: se registra en el inventario | Inmediato |
| 2. Medio | L2-L3 sobre sistemas internos, o datos Confidenciales con herramienta aprobada | Dueño del caso y responsable de seguridad | 5 días hábiles |
| 3. Alto | Toca código o datos de un cliente, o va dentro del producto que se vende | Council, con verificación de la matriz del cliente. Los datos productivos de un cliente no salen hacia un modelo externo durante el horizonte | Hasta el siguiente Council (30 días como máximo) |
| Prohibido en el plan | Decisiones de crédito o scoring sobre personas, datos de categoría especial, L4 con acceso a producción, datos productivos de clientes hacia un modelo externo | No se aprueba en el horizonte; reabrirlo es una decisión del G4 que rige después (ver D7b) | Ver D6 |

El plazo de 5 días hábiles es un objetivo del equipo, más rápido que las 2 a 4 semanas de
la política en borrador, para que el control no empuje el uso fuera del sistema oficial.

### D6. Escala de autonomía L0-L4: topes para los 12 meses

| Ámbito | Tope | Reversible |
|---|---|---|
| Agentes de código internos con Claude Code, Copilot | L3 (actúa con aprobación) y *hooks* de permisos | Sí |
| Agentes de código con credenciales productivas | L2 (prepara, no ejecuta) | Sí |
| L4 (autónomo dentro de límites) | Solo en *sandbox*, sin credenciales productivas ni acceso a datos de cliente. Con efectos externos, no en el horizonte | Sí |
| Funciones de IA dentro del producto que se vende | L1-L2 durante todo el horizonte. Subir a L3 es una decisión del G4 (efecto externo), que rige después | Sí hasta que se activa; luego es irreversible (D7b) |

La escala L0-L4 es una herramienta de la cursada, no un estándar oficial.

### D7. Compliance: alcance explícito

- **No se ofrecen decisiones de crédito ni scoring en los 12 meses.** Excluye el caso
  crediticio del Anexo III y la parte más pesada del
  régimen del BCRA sobre modelos. Es **reversible**: el G4 decide si se reabre para el plan
  siguiente, si un cliente lo pide y el Council aprueba el costo de proveedor de alto riesgo;
  no se ejecuta dentro del horizonte.
  Excluir el crédito no demuestra por sí solo que no haya otros usos de alto riesgo (empleo,
  educación): el intake pregunta por cada categoría del Anexo III y un sí pasa el caso a
  Nivel 3 con Legal externo.
- **ISO/IEC 42001: alinear, no certificar en el año.** Se extiende el alcance de la ISO
  27001 existente con los controles de IA y se registra la brecha frente a 42001. Alternativa
  descartada por ahora: certificar 42001, que suma costo de auditoría y carga documental sin
  que haya hoy un cliente que lo exija ([supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md)).
  La decisión de certificar se toma en el gate del Q4 y es **reversible**.
- **EU AI Act: tratarlo como disparador, no como obligación.** Se pregunta a cada cliente
  si opera en la UE o usa resultados allá. Si la respuesta es sí, el caso pasa a Nivel 3.
- **El NIST AI RMF organiza el registro de riesgos** (Govern, Map, Measure, Manage):
  cada riesgo lleva su función, su prueba y su evidencia (ver Riesgos). Se declara
  alineación, sin buscar cumplimiento formal.
- **La política se ratifica en el Directorio (T1).** Es un compromiso interno que se enmienda
  con costo de credibilidad, no una decisión irreversible: no firma nada con un cliente.
  Por eso va con revisión anual y con revisión extraordinaria en G2.

### D7b. Catálogo de decisiones del Anexo C: ámbito, fecha y compromiso

Tres pasos que no se confunden: **aprobación interna** (Council o Directorio),
**negociación no vinculante** con un cliente y **firma** de un compromiso. Ninguna
excepción puede contradecir una prohibición del horizonte.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto |
|---|---|---|---|---|---|
| Ratificar la política de IA | Interno | T1 | Directorio | G0 aprobado | Compromiso interno enmendable; sin firma con clientes |
| Cláusula tipo de IA para contratos | Interno y negociación | T3 | Council | Una función de IA con ficha y supervisión humana | Texto listo y negociación no vinculante |
| Firma de un compromiso contractual de IA con un cliente | Externo | G4 | Council | Cláusula tipo, matriz del cliente y red team sin críticos | Irreversible: el compromiso queda firmado |
| Enviar datos productivos de un cliente a un modelo externo | Externo | No antes de G4 | Responsable comercial del cliente, con Council | Cláusula firmada, matriz y controles demostrados | Irreversible |
| Subir una función de IA del producto a L3 | Externo | G4 | Council | Evidencia del piloto y red team externo sin críticos | Rige después del horizonte |
| L4 con efectos externos o acceso a producción | Externo | Fuera del horizonte | Council | Decisión del G4 para el plan siguiente | Prohibido hasta entonces |
| Reabrir crédito o scoring | Producto | G4 (decisión) | Council con Legal externo | Pedido de un cliente y costo de proveedor de alto riesgo aprobado | Rige después del horizonte |

### D8. Seguridad: modelo de amenazas y controles

Las amenazas siguen el OWASP Top 10 for LLM Applications 2025 (LLM01 inyección de
prompts, LLM02 divulgación de información sensible, LLM06 agencia excesiva, LLM07 filtración
del prompt del sistema), que la cursada no cita pero complementa la unidad M3U1
([unidad](../../material/unidades/m3u1-seguridad.md)).

| Amenaza | Prevención | Detección | Respuesta | Conexión con lo existente |
|---|---|---|---|---|
| Inyección de prompts directa e indirecta | Mínimo privilegio, contenido no confiable segregado, validación de salida con código | Logs de acciones de agentes y alertas de desvío | Red teaming interno (Q2) y externo (Q4) | Revisión de PR obligatoria para código con IA ([ficha](../../context/hechos/stack-y-plataforma.md)) |
| Fuga de datos (DLP) | Clasificación de 4 niveles, anonimización, cifrado, control de acceso | Escaneo de secretos y PII en prompts | Plan de incidentes con aviso al cliente | Política en borrador y cuentas AWS separadas por proyecto |
| Aislamiento de datos de clientes | Entornos y credenciales por cliente; la IA no cruza datos entre proyectos | Auditoría del acceso por proyecto | Suspensión por cliente | Staffing opera con las herramientas de cada cliente, fuera del alcance del control |
| Cadena de suministro (modelos, servidores MCP, proveedores) | Lista cerrada de servidores MCP, contrato sin entrenamiento, revisión de cambios del proveedor | Revisión mensual de proveedores y subprocesadores | Retiro del proveedor | Contrato organizacional de agentes de código |
| Secretos | Escaneo previo al envío y rotación | Alertas | Primera exposición: revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo (R4) | Auditoría periódica de vulnerabilidades de código e imágenes |

**Matriz superficie → control → telemetría.** La pasarela enruta llamadas a modelos; los tres
productos corporativos tienen superficies que quizá no pasen por ella
([ficha](../../context/hechos/uso-ia-interno.md)). Lo siguiente es el diseño a probar en el Q2,
no una capacidad demostrada: ningún control de esta tabla se verificó contra el producto real.

**Tres cosas que no se confunden.** *Prohibición*: lo que la política dice que no se hace;
rige en todas las superficies, pero por sí sola no impide nada. *Bloqueo técnico*: un control
que detiene el envío (pasarela con DLP, escaneo de secretos antes del envío); solo existe donde
la superficie lo admite y se prueba en el Q2. *Control compensatorio*: lo que reemplaza al
bloqueo donde no se puede bloquear (cuentas corporativas, consola de administración, rotación,
auditoría); detecta o reduce, no previene. Donde hay prohibición sin bloqueo técnico queda un
**residual** que acepta el Council (criterio de aceptación) y que se informa al board.

| Superficie | Prohibición (política) | Bloqueo técnico | Control compensatorio | Telemetría | Riesgo de *bypass* | Estado |
|---|---|---|---|---|---|---|
| Casos propios (producto y agentes internos nuevos) | Datos prohibidos y secretos | Solo por la pasarela, 100%: DLP y escaneo de secretos | No hace falta: no tienen otra ruta | Logs de la pasarela | Bajo: sin ruta alternativa por diseño | Por diseño; a probar en el Q2 |
| Agente de código en terminal (~90% de los eventos de ese agente) | Secretos y datos de cliente | *Hooks* de permisos y escaneo de secretos en el equipo y el repositorio, siempre. DLP sobre prompts en la pasarela **solo si el régimen comercial permite enrutarlo** (regímenes a y c del [Anexo B](02-arquitectura.md), "Política de ruteo") | Régimen b (la suscripción plana se rompería): lista cerrada de MCP, telemetría existente y ruteo ensayado, listo para activarse | Consola del proveedor; logs de la pasarela si se enruta | Uso con una cuenta o configuración personal | A probar en el Q2 |
| Asistente de código en el IDE | Secretos y datos de cliente | Ninguno demostrado: no pasa por la pasarela hasta probar lo contrario | Política de la organización del proveedor y lista de repos permitidos | Consola de administración del proveedor | Alto: sin ruta por la pasarela | A probar en el Q2; si no hay control técnico, rige la política y se reporta aparte |
| Chat y escritorio del asistente general | Datos Restringidos y de cliente | Bloqueo en navegador o equipo, solo si el parque lo permite (a probar) | Cuentas corporativas, ajustes de retención y conectores | Consola de administración | Alto: cuentas personales | A probar en el Q2 |
| Asistente de la suite ofimática | Datos Restringidos y de cliente | Ninguno de la organización: lo da la configuración del administrador | Revisión mensual de funciones nuevas (R5) | Registros de auditoría de la suite | Medio: activación por defecto del proveedor | A probar en el Q2 |
| Servidores MCP y conectores | Servidores fuera de la lista | Lista cerrada (allowlist) donde se pueda imponer | Revisión de cambios e inventario | Inventario y logs de la pasarela | Medio: instalación local por una persona | A probar en el Q2 |

**Denominador del 90%.** Eventos del agente de código en terminal que la telemetría de la
pasarela cuenta sobre el total de eventos del agente (según la consola del proveedor). El 90%
rige solo si el agente se enruta (regímenes a y c del Anexo B). Si enrutar obliga a facturar
por API (régimen b), el agente no se enruta mientras la suscripción sea plana y se le exige
control verificado sin pasarela; no cuenta en el 90% ni se presenta como "enrutado". Los casos
propios van al 100% por la pasarela, aparte. Las demás superficies no entran en el 90%: se
reportan con su propia cobertura (seats activos bajo control sobre seats activos) y las que
quedan afuera se listan como riesgo aceptado, no se cuentan como cubiertas. Un gate de
cobertura nunca obliga a enrutar si eso encarece el servicio: la tensión con F queda abierta
(D10). La prueba de integración y de *bypass* por herramienta, y la
migración de la configuración, tienen costo propio en "Insumos para Finanzas".

El aislamiento de clientes tiene un límite: el staffing trabaja con las herramientas que
permite cada cliente ([ficha](../../context/hechos/uso-ia-interno.md)), por lo que el
control de Acme Labs no alcanza a esos equipos; para ellos rige la cláusula contractual.

### D9. Controles por trimestre

Los objetivos son propuestas del equipo, a calibrar con la línea base del Q1. Q1 rige en
las dos ramas de G1. Q2 y Q4 describen la **rama con señal**; la rama sin señal, que corre
como la opción (b) de [E](05-business-case.md), está en D9c. Q3 depende de la señal de cliente.

| Trim. | Controles | Criterio de éxito | Costo en velocidad | Condición de abandono o cambio |
|---|---|---|---|---|
| Q1 | Ratificar la política; inventario v1; matriz de restricciones de los clientes principales y lectura de la evidencia contractual para G1 (D9b); intake en 3 niveles; plan de incidentes | Política firmada; inventario con las 3 herramientas aprobadas, los servidores MCP y la IA embebida; matriz al 100% de los clientes principales | Bajo: solo trámite. La matriz frena los casos de cliente hasta completarse | Si más del 30% de los contratos queda ambiguo a los 4 meses, se aplica *default-deny* sobre el código de ese cliente y se pide revisión legal |
| Q2 | Matriz superficie→control→telemetría (D8) con prueba de integración y de *bypass* por herramienta; pasarela con allowlist y DLP sobre prompts; escaneo de secretos; logs de acciones; red team interno; ejercicio de mesa de incidentes, que incluye la ruta de primera exposición de un secreto | Si su régimen comercial lo permite, al menos el 90% de los eventos del agente de código pasa por la pasarela (denominador en D8); si no, control verificado sin pasarela y ruteo ensayado; casos propios, 100%. Cada superficie restante tiene su control compensatorio y su cobertura reportada aparte, y el residual sin bloqueo técnico va al Council; red team con hallazgos críticos cerrados | Medio: fricción en el agente de código | Si la actividad semanal de seats cae más de 15% frente a la línea base del Q1 dos meses seguidos, **solo los usos permitidos** pasan a monitoreo; el bloqueo de secretos, PII y datos prohibidos no se relaja nunca |
| Q3 | Revisión del modelo de amenazas de la primera función de IA en el producto; criterios de *eval* para salir a producción; documentación de proveedor; cláusula tipo para contratos | Una función de IA con ficha técnica, registro de eventos, supervisión humana y cláusula tipo lista para negociar con el cliente (la firma, no antes de G4) | Medio: agrega un gate antes de salir | Si tras dos ciclos de red team persisten hallazgos críticos, la función queda en L0-L1 o se cancela |
| Q4 | Red team externo; extensión del alcance de ISO 27001 a IA; revisión de niveles de autonomía; informe anual al Directorio; gate de certificación 42001 | Cero hallazgos críticos abiertos; brecha frente a 42001 documentada; decisión del gate registrada | Bajo | Sin señal contractual ni producto liberado en G3, el red team externo y la extensión ISO (capa D) se difieren. Si ningún cliente exige 42001, no se certifica; si el costo de la auditoría supera el rango de Finanzas, se difiere |

**Cautelas del plan.** Seis puntos quedan abiertos y no se inventan:

1. La función legal es externa y su costo es un supuesto sin cotización.
2. El rol de Acme Labs frente a la Ley 25.326 (responsable o encargado del tratamiento)
   necesita asesoría.
3. De la A 7777 se leyó solo la sección 4.6, versión 1a (ver la tabla del marco): no prueba una
   exigencia comercial al proveedor; eso lo prueba, o no, la evidencia contractual (D9b).
4. Legal externo debe confirmar alcance, versión vigente, rol y excepciones de BCRA, AI Act y Ley 25.326; esta lectura no verifica ninguna ficha.
5. La matriz de restricciones de clientes depende del área comercial y no existe todavía
   ([ficha](../../context/hechos/gobierno-y-politica-ia.md)).
6. Los residuales del registro y los umbrales de señal son propuestas del equipo: se
   confirman con las pruebas del Q2 y con la evidencia contractual del Q1.

### D9b. Licencia para vender: qué evidencia la sostiene y qué cuesta el gobierno mínimo

**Problema.** El deck dice que la base compra "licencia para venderles a bancos". Hoy eso
se apoya en un [supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md), no
en contratos. La A 7777 obliga al banco a gobernar el uso de IA de sus terceros; no
prueba que le exija controles a Acme Labs ni que le compre IA. Pedir controles tampoco es
pedir IA: son dos señales distintas.

**Tres capas, con los renglones de "Insumos para Finanzas".** El paquete se parte según
qué riesgo reduce cada capa. M rige siempre; T depende de la señal que lee G1 (la
plataforma de T2); D, de la señal contractual o del producto en G3.

| Capa | Renglones | Caja (USD) | Tiempo (USD) | Total (USD) | Qué reduce | Qué no reduce |
|---|---|---|---|---|---|---|
| M. Gobierno mínimo | Líder, seguridad, Council, matriz e inventario, legal externo, ejercicios de mesa | 8.000-20.000 | 24.650-62.150 | 32.650-82.150 | R1 por matriz y *default-deny*; R5, R6, R9; la política ratificada | R2 y R4 quedan solo en política: no hay bloqueo, log ni prueba que mostrarle a un cliente |
| T. Controles técnicos propios | Pasarela con DLP y logs, pruebas de *bypass*, red team interno | 4.500-18.000 | 1.875-9.375 | 6.375-27.375 | R1 y R4 con bloqueo y registro; R2 probado; la evidencia del ejemplo de R4 | Las superficies sin ruta por la pasarela (residual aceptado) |
| D. Demostración externa | Red team externo; extensión de la ISO 27001 a IA | 11.600-31.000 | — | 11.600-31.000 | R9 con evidencia de un tercero; la condición del G4 (red team externo sin críticos) | Ningún riesgo propio que T no cubra: vale si un cliente la pide o si el producto sigue |
| **Paquete completo (rama con señal)** | | **24.100-69.000** | **26.525-71.525** | **50.625-140.525** | | |

**Recomendación.** M se financia siempre. T y D se liberan por señal, como decidió el
board en E: G1 libera la plataforma (y con ella T) si hay al menos una señal; D se decide
en G3. Sin señal, el año corre como la opción (b) de E y cuesta lo que M: 32.650-82.150, más
hasta 1.875-9.375 de tiempo de los controles compensatorios de D9c (E los suma: ≈ 199 en el año). Ahorra
la caja de T (4.500-18.000) y la de D (11.600-31.000). **Desacuerdo a la vista:** antes este
anexo financiaba T por riesgo propio, porque R1 y R4 exponen a Acme Labs aunque no venda
IA, y eso sigue siendo cierto. Con la decisión del board ese riesgo no se mitiga con
pasarela: se acepta como residual con controles compensatorios (D9c). Quien quiera T sin
señal tiene que pedir una excepción al board, con su caja.

**Qué evidencia se pide (Q1).** No se inventan clientes ni cláusulas: se leen los
documentos que ya existen, con la misma lectura que arma la matriz.

| Fuente | Qué se busca | Rol que la junta |
|---|---|---|
| Contratos vigentes de los cinco primeros clientes (más del 90% de la facturación, [ficha](../../context/hechos/cartera-y-concentracion.md)) | Cláusulas de subcontratación, confidencialidad y secreto, tratamiento y transferencia de datos, herramientas o IA | Operaciones con el área comercial |
| Cuestionarios de evaluación de proveedores recibidos en los últimos 24 meses | Preguntas sobre IA: inventario, no entrenamiento, ubicación de datos, logs, certificaciones, y si la respuesta condiciona algo | Responsable de seguridad |
| RFP, pliegos y pedidos de renovación de los últimos 24 meses | Requisitos de IA como condición o como puntaje | Área comercial |
| Informes de auditoría de clientes sobre Acme Labs | Observaciones sobre IA o terceros | Responsable de seguridad |

**Cómo se registra.** Una fila por documento, **solo en `private/`**: alias del cliente
(los de la ficha de cartera, sin segmento), tipo de documento, fecha, texto del requisito, clasificación
(prohíbe, condiciona, pide evidencia de controles, pide IA, silencio), si es condición o
pregunta, y horizonte (vigente o renovación con fecha). Fuera de `private/` sale solo el
agregado, sin alias ni textos, como ficha anonimizada que verifica una persona del equipo.

**Umbral que la convierte en señal** (propuesta del equipo,
[supuesto](../../context/supuestos/umbral-de-evidencia-contractual.md)). La señal
contractual es una de las tres que puede liberar la plataforma en G1; se lee al fin de T1
y se vuelve a leer en G2 y G3.

| Señal | Umbral | Cuenta en G1 | Qué decide |
|---|---|---|---|
| Restricción | Al menos un contrato de los cinco primeros prohíbe o condiciona la IA de terceros | **Solo si condiciona**: acepta la IA con controles que Acme Labs debe demostrar. Si solo prohíbe, no | La matriz y el *default-deny* pasan de prudencia a obligación (capa M) |
| Licencia para vender | Uno de los dos primeros clientes, o dos de los cinco primeros, piden evidencia de controles de IA como condición o puntaje de contratación o renovación dentro de 18 meses. Las preguntas sin consecuencia no cuentan | Sí | Libera T en G1, sola o con otra señal; la capa D se decide en G3 |
| Demanda | Un cliente pide una función de IA | No es esta señal: es la de cliente para el producto, que define [F](06-roadmap-riesgo.md) | Libera el piloto de producto en G2 |
| Sin señal | Ninguna de las anteriores | Sin señal contractual en G1 | T2-T4 como (b) (D9c); G2 y G3 releen |

**Desacuerdo a la vista sobre la restricción.** E escribe "restricción o licencia" sin
distinguir. Esta lectura la recorta porque el supuesto de partida ya es que los clientes
prohíben por defecto: un contrato que solo prohíbe confirma ese supuesto, probablemente
exista entre cinco bancos, y liberaría la plataforma casi siempre sin que nadie pida nada
que (b) no compre. La alternativa es la lectura literal de E, que desactiva la
bifurcación en la práctica. Decide el board en G0.

**Cómo se lee en G1.** La evidencia de T1 son los mismos contratos de la matriz, que ya es
condición de G1; los cuestionarios, RFP y auditorías pueden llegar después.

- **Quién junta:** los roles de la tabla de fuentes. **Quién consolida:** el responsable de
  seguridad, que arma el agregado (cuántos de los cinco primeros, qué clasificación, sin alias
  ni textos). **Quién declara la señal:** el Council, con Legal externo para los textos
  ambiguos. Personas pendientes.
- **Cuándo:** el agregado llega al Council al menos dos semanas antes de G1 (propuesta,
  a fijar en G0). La ficha anonimizada la verifica una persona del equipo antes; hasta
  entonces es supuesto y no sustenta el gate.
- **Qué cuenta:** solo el documento leído y clasificado. El ambiguo o no leído no cuenta;
  si por eso no se llega al umbral, el resultado es "sin señal por lectura incompleta" y no
  "señal no probada", se completa en T2 (como dice E) y se relee en G2.
- **G2 y G3:** misma tabla, sobre lo nuevo desde el gate anterior (renovaciones, RFP,
  cuestionarios) y la lectura que faltaba. Una señal que aparece en G2 libera T desde T3;
  una que aparece en G3, desde T4 (D9c).

La lectura cabe en las horas de la matriz porque son los mismos contratos. Si no
alcanza, el faltante es de 20-40 h de analista funcional (260-1.360 USD, al costo
horario del supuesto), que no está sumado al total.

### D9c. Controles por rama de G1: qué rige siempre y qué depende de la plataforma

Cada control dice si rige desde G1 en las dos ramas o solo si G1 libera la plataforma.
La velocidad que cuesta es la de D9; los compensatorios son tiempo, sin caja.

| Control | Rige en las dos ramas | Solo con señal en G1 |
|---|---|---|
| Política ratificada, intake en 3 niveles, inventario, plan de incidentes, ejercicios de mesa | Sí (capa M) | — |
| Matriz de clientes con *default-deny* (R1) y topes L0-L4 | Sí (M) | — |
| *Hooks* de permisos, escaneo de secretos en el equipo y el repositorio y lista cerrada de MCP por configuración, en el agente de código | Sí, **compensatorio**: probados con un secreto sintético antes de extender la prueba a la cohorte | — |
| Red team interno acotado al agente de código, con repositorios y tickets sintéticos | Sí, compensatorio (R2) | — |
| Pasarela con allowlist, DLP y logs; cobertura ≥90% (regímenes a y c) y 100% de casos propios | No | Sí (T2) |
| Prueba de *bypass* por superficie, y red team de la pasarela | Solo para el agente de código | Todas las superficies |
| Piloto de producto en L1-L2, modelo de amenazas del producto, *evals* y cláusula tipo | No | Solo con señal de cliente en G2 |
| Red team externo y extensión de la ISO 27001 (capa D) | No | Señal contractual o producto en G3 (T4) |

**Calendario sin señal.** T2: capa M y compensatorios. G2 relee las señales: si hay una, T
corre en T3 y la cobertura se mide en G3; el red team externo, en T4 solo si T cerró. Si la
señal llega en G3, T corre en T4 y D queda para el año siguiente. Es consecuencia de la
secuencia de [B](02-arquitectura.md), no un costo medido.

**Condiciones de G2 y G3 sin señal** (propuesta a `caio` para F): matriz al 100% de los
clientes principales; compensatorios probados y críticos del red team cerrados; residual
de R1, R2 y R4 aceptado por el Council con fecha de revisión; lectura de la señal
contractual hecha. No se piden cobertura por pasarela ni bypass de todas las superficies.

**Riesgo residual sin pasarela.** Sin T, R2 y R4 no tienen bloqueo central ni registro; en
la capa M quedan en la política. Propuesta: **aceptarlo**, con los compensatorios de la
tabla, porque la rama sin señal no agrega superficie: no hay casos propios ni agentes nuevos,
y la prueba extendida corre sobre los repositorios que la matriz habilita, sin datos de
cliente. Hoy hay 40-45 seats de Claude y no hay evidencia de controles específicos de IA.

| Riesgo | Residual objetivo sin T | Acepta | Vence |
|---|---|---|---|
| R1 | Media / Alto (sin allowlist en la pasarela) | Council, con informe al CEO | G2 y G3 |
| R2 | Media / Alto (sin logs centrales) | Council, con informe al CEO | G2 y G3 |
| R4 | Baja / Medio-alto en el agente de código (bloqueo local); Media / Medio-alto en el resto | Council | G2 y G3 |

La aceptación vale **solo si** se cumplen cuatro condiciones: repositorios habilitados por
la matriz, autonomía hasta L3 con aprobación humana, sin credenciales productivas, y los
compensatorios probados. Si falta una, la prueba no se extiende. Un incidente confirmado de
R1, R2 o R4 la revoca: se suspende la extensión y el Council le pide al board reabrir T
como decisión de seguridad, fuera de las tres señales (propuesta). El responsable humano
de la aceptación queda pendiente.

**Alternativas.** (i) Financiar T sin señal: 4.500-18.000 de caja, contra la decisión del
board. (ii) No extender la prueba a la cohorte: reduce el riesgo, pero deja a (b) sin su
medición. (iii) Aceptar solo con la política: descartada, es lo que hoy deja sin prueba.
**Costo:** los compensatorios suman hasta 1.875-9.375 de tiempo (la parte de tiempo de T),
que E suma a la rama sin señal (no al (b) de "Alternativas equivalentes"); sin el escaneo local de secretos probado, R4 no tiene bloqueo en
ninguna superficie. **Éxito:** secreto sintético bloqueado y alertado en el agente; críticos
del red team cerrados. **Abandono:** incidente confirmado o condición incumplida.

### D10. Tensiones con otras miradas

- **Con `architect`:** la pasarela de salida y la lista de servidores MCP condicionan el
  diseño de la plataforma. Alternativa: gobierno define el requisito (allowlist, registro,
  sin entrenamiento) y `architect` elige la herramienta; el costo del Q2 es un rango hasta
  que lo confirme.
- **Con `architect` (ruteo del agente de código):** la política del Anexo B rige: se enruta
  solo si el régimen comercial lo permite, y el 90% rige en los regímenes a y c; F la adoptó.
- **Con `finance` (bifurcación):** T pasó de "por riesgo propio" a depender de la señal de
  G1; el residual de R1, R2 y R4 sin pasarela lo asume el Council (D9c).
- **Con `finance`:** alrededor de la mitad (51%-52%) del costo de este anexo es tiempo reasignado, no caja, pero el
  tiempo compite con horas facturables (utilización ~83%). Finanzas decide si lo trata
  como costo de oportunidad o lo ignora.
- **Con `people`:** la alfabetización en IA es un control débil por sí solo (el piloto
  mostró 17% de cursos completos); se propone medirla por conducta (uso de la pasarela,
  revisión de output) y no por cursos terminados.
- **Con `caio`:** si el board prioriza velocidad, se puede relajar el SLA del Nivel 2, pero
  no la matriz de clientes ni la prohibición de crédito.

## Insumos para Finanzas

Todas las cifras son rangos en USD, supuestos del equipo sin cotización, salvo donde se
cita una ficha. Cada costo de tiempo se calcula por actividad y por rol con el supuesto de
costo cargado, ya ampliado; los rangos son amplios a propósito. "Tiempo" es costo de oportunidad (reasignación), "caja" es gasto externo.

| Concepto | Trim. | Tipo | Rango (USD) | Fuente o supuesto |
|---|---|---|---|---|
| Líder de gobierno y riesgo: 25% de un tech lead durante 12 meses | Q1-Q4 | Tiempo | 13.500-30.000 | 4.500-10.000 por mes ([supuesto](../../context/supuestos/costo-cargado-por-rol.md)) × 25% × 12 |
| Ingeniería de seguridad: 20% de un senior DevOps o seguridad | Q1-Q4 | Tiempo | 7.200-18.000 | 3.000-7.500 por mes × 20% × 12 |
| AI Council: 5 personas × 2 h por mes × 12 | Q1-Q4 | Tiempo | 2.250-5.650 | 24 h de sesión × 5 asientos: 2 a costo de tech lead, 1 de senior DevOps y 2 de staff (9-63 USD/h según el rol), supuesto del equipo |
| Matriz de restricciones por cliente e inventario v1 | Q1 | Tiempo | 1.250-5.500 | 100-160 h de analista funcional (13-34 USD/h), supuesto del equipo |
| Asesoría legal externa (BCRA, Ley 25.326, cláusulas tipo) | Q1-Q2 | Caja | 8.000-20.000 | Supuesto del equipo, sin cotización |
| Pasarela de salida, DLP y logs de acciones | Q2-Q4 | Caja | 4.500-18.000 | 500-2.000 por mes × 9, supuesto; lo confirma `architect` |
| Prueba de integración y de *bypass* por herramienta, y migración de la configuración de la pasarela (60-120 h) | Q2 | Tiempo | 1.125-5.625 | 60-120 h de senior DevOps o seguridad (19-47 USD/h), supuesto del equipo; lo confirma `architect` |
| Red team interno (40-80 h) | Q2 | Tiempo | 750-3.750 | 40-80 h de senior DevOps o seguridad (19-47 USD/h) |
| Red team externo | Q4 | Caja | 10.000-25.000 | Supuesto del equipo, sin cotización |
| Extensión del alcance de ISO 27001 a IA (2-4 jornadas de auditoría) | Q4 | Caja | 1.600-6.000 | 800-1.500 por jornada, supuesto; depende del calendario de la auditoría externa prevista para 2027 |
| Ejercicios de mesa de incidentes (2 × 8 personas × 3 h) | Q2 y Q4 | Tiempo | 450-3.000 | 48 h entre el costo de staff y de tech lead (9-63 USD/h) |
| **Total** | Q1-Q4 | | **50.625-140.525** | Caja: 24.100-69.000; tiempo: 26.525-71.525 |

No incluye licencias de las herramientas de IA ni capacitación (las cubre `architect` y
`people`), ni una certificación ISO 42001 (decisión del Q4). Finanzas debe contrastar el
total con la franja del 1%-3% de la facturación del [supuesto](../../context/supuestos/capacidad-de-inversion.md).

**Cómo lo usa el [Anexo E](05-business-case.md).** Los renglones coinciden con su cuadro
de inversión (legal 8-20, pasarela 4,5-18, red team externo e ISO 11,6-31, tiempo 27-72
redondeado). Tres lecturas de gobierno sobre esas cifras:

- **Techo de T1.** De este anexo, T1 lleva la parte de legal (hasta 10 de caja en el pedido
  G0) y el tiempo del líder, de seguridad, del Council y de la matriz.
- **Base mínima tras un corte.** Es el núcleo de la capa M: 25% del líder, 20% de
  seguridad y el Council, que suman 5.740-13.410 por trimestre. Tres trimestres dan
  17.200-40.200, que es el "hasta 40" de tiempo que E usa para un corte en G1. La pasarela
  se suma solo si ya está instalada ([base mínima](../../context/supuestos/base-minima-tras-un-corte.md)).
- **Capas T y D condicionales (D9b, D9c).** Los renglones de T (pasarela, 4.500-18.000 de caja)
  y de D (11.600-31.000) no se gastan sin señal; E ya condiciona D en G3 y T en G1.

## Insumos para el deck

- **Mensaje de la slide:** "Gobierno que habilita": un Council de 5 asientos dentro del
  comité de tecnología, intake en 3 niveles con respuesta en 5 días hábiles para el riesgo
  medio, y control técnico de la salida de datos donde la superficie lo admite; en el resto,
  política y control compensatorio con residual aceptado por el Council, no una garantía
  de bloqueo.
- **Slide 5 (`plan/slides.md:79`):** el texto ya dice bloqueo en la pasarela y en el equipo.
  Propuesta a `caio` para `:85` (punto 3): ver el reporte de esta ronda.
- **Pedido al board 1:** ratificar la política de IA que está en borrador desde abril de 2026.
- **Pedido al board 2:** aprobar el alcance explícito (sin decisiones de crédito ni
  scoring en 12 meses) y los topes de autonomía L0-L4 del plan.
- **Pedido al board 3:** financiar por gate. Gobierno mínimo siempre (32.650-82.150, supuesto
  del equipo, sujeto a cotización). Con señal en G1, los controles técnicos (6.375-27.375),
  y la demostración externa (11.600-31.000 de caja) se decide en G3 contra la evidencia
  contractual. Con las tres capas, 50.625-140.525 (24.100-69.000 de caja). Sin señal, D9c.
- **Mensaje sobre la licencia para vender:** hoy es un supuesto; el Q1 junta la
  evidencia, G1 la lee para liberar la plataforma y G3 decide si se paga la capa que la demuestra.
- **Mensaje honesto:** hoy no hay inventario, registro de riesgos, matriz de clientes ni
  controles técnicos de IA con evidencia; un producto propio no está certificado.
  Decir "certificados" donde no lo estamos es el riesgo R9.
