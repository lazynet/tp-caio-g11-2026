---
owner: governance
status: draft
title: "Anexo C — Gobierno, seguridad y compliance"
---

# Anexo C — Gobierno, seguridad y compliance

Slides que sustenta: [Gobierno y seguridad](../slides.md).

## Objetivo

Sustentar las tres decisiones de gobierno y seguridad que la slide «Gobierno y seguridad» le pide al
Directorio, y el modelo que las sostiene:

1. **Política de IA:** aplicar la que el responsable del caso informó aprobada el
   20/10/2026, después de revisar versión, alcance y constancia de aprobación.
2. **Alcance y topes:** sin crédito ni scoring en 12 meses, y la escala de autonomía.
3. **Controles:** ningún uso nuevo sin prueba previa. El pedido vigente es el paquete
   mínimo M1-M3 que consolida el [Anexo E](05-business-case.md), en dos autorizaciones
   (preparación 2026 y, después de la validación inicial, M1-M3). Los controles técnicos
   de plataforma y la demostración externa son opciones que se liberan por señal en los
   meses 3 y 9; los montos anuales de este anexo son referencia, no un pedido de hoy.

**El modelo que las sostiene:** un AI Council de cinco asientos dentro del comité de
tecnología, sin gatekeeper, con derechos de decisión por rol.

Hoy la organización tiene una política informada como aprobada, tres herramientas
aprobadas y ninguna evidencia de controles específicos de IA más allá de la política. Todo lo demás de este anexo es
propuesta del plan y empieza solo con esas autorizaciones. Los gates son los meses 3,
6, 9 y 12; los tramos, los meses 1-3 (enero-marzo de 2027), 4-6, 7-9 y 10-12. Cada
control declara cuánta velocidad cuesta y cuándo se abandona.

La [aprobación informada](../../context/hechos/gobierno-y-politica-ia.md) no acredita
controles implementados, operación del Council ni cierre de matriz, inventarios o riesgos.
El borrador v1.0 de abril es un antecedente histórico, por contrastar con la versión aprobada.

La IA que Acme Labs vende a bancos y fintechs es la que más exige: hoy no hay IA en
producción dentro de lo que se vende ([fuente](../../context/hechos/ia-en-producto-y-oferta.md)),
así que el gobierno se construye antes del primer caso, no después del primer incidente.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Tamaño de la organización | 60-70 personas, ~80% en Operaciones y Tecnología | [Fuente](../../context/hechos/tamano-y-estructura.md) |
| Política de IA | Aprobada según confirmación del responsable del caso del 20/10/2026; versión, alcance y aprobación documentada por revisar. El borrador v1.0 y sus pendientes de abril son antecedentes históricos, salvo la aprobación informada | [Fuente y cautelas](../../context/hechos/gobierno-y-politica-ia.md) |
| Inventario de casos de uso y registro de riesgos de IA | Sin evidencia en el registro de partida; estado actual por contrastar. La aprobación de la política no los acredita | [Fuente](../../context/hechos/gobierno-y-politica-ia.md) |
| Herramientas aprobadas | 3 (Claude Team, GitHub Copilot, Gemini en Workspace); 40-45 seats de Claude | [Fuente](../../context/hechos/uso-ia-interno.md) |
| Certificación de seguridad | ISO/IEC 27001 de la organización; un producto propio no tiene la suya | [Fuente](../../context/hechos/seguridad-y-certificaciones.md) |
| Controles específicos de IA (red teaming, DLP sobre prompts) | Sin evidencia | [Fuente](../../context/hechos/seguridad-y-certificaciones.md) |
| Concentración de capacidad | Gobierno y seguridad dependen de pocas personas | [Fuente](../../context/hechos/tamano-y-estructura.md) |
| Apetito de riesgo de los clientes | Prohíben por defecto modelos externos sobre su código y datos, salvo cláusula y controles demostrables. La evidencia contractual se junta en los meses 1-3 y se lee en la decisión del mes 3 (ver "Licencia para vender") | [Supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md) |
| Datos disponibles para IA | Internos; los datos productivos de clientes no | [Supuesto](../../context/supuestos/disponibilidad-de-datos.md) |
| Inversión incremental del plan | 1%-3% de la facturación anual, más 10%-15% del tiempo de personas clave | [Supuesto](../../context/supuestos/capacidad-de-inversion.md) |
| Costo cargado por rol | Tech lead 4.500-10.000 USD/mes; senior DevOps 3.000-7.500; analista funcional 2.000-5.500; staff 1.500-5.000. Rangos amplios, no calibrados contra la nómina | [Supuesto](../../context/supuestos/costo-cargado-por-rol.md) |
| Costo horario por rol | Tech lead 28,125-62,5 USD/h; senior DevOps 18,75-46,875; analista funcional 12,5-34,375; staff 9,375-31,25. Es el costo mensual dividido 160 h; cada actividad usa el rol que la hace, sin promedios de la empresa. Donde el anexo muestra la tasa redondeada a la unidad (por ejemplo, 13-34 USD/h), es solo para leer: las cuentas usan estos valores exactos | Supuesto, derivado del costo cargado por rol |
| Disponibilidad | Utilización facturable ~83% y bench casi nulo: el tiempo de gobierno compite con horas facturables | [Fuente](../../context/hechos/capacidad-y-utilizacion.md) |
| Los clientes principales siguen | La facturación está muy concentrada en pocos clientes (rango en la fuente) | [Supuesto](../../context/supuestos/continuidad-de-clientes-principales.md) |

## Evidencia

### Punto de partida frente a la meta a 12 meses

| Métrica | Hoy | Esperado a los 12 meses | Fuente |
|---|---|---|---|
| Política de IA | Aprobación informada el 20/10/2026; documentación e implementación por revisar | Versión, alcance y aprobación documentados; política aplicada, con revisión anual y onboarding | [Fuente](../../context/hechos/gobierno-y-politica-ia.md) |
| Inventario de usos de IA | Sin evidencia en el registro de partida; estado actual por contrastar | 100% de las herramientas, servidores MCP, funciones de IA embebidas y casos de producto | Objetivo propuesto por el equipo |
| Matriz de restricciones por cliente | Pendiente en abril; se validaba a mano. Estado actual por contrastar | Cubre los clientes que concentran la mayor parte de la facturación (la fuente da el alcance) | [Antecedente](../../context/hechos/gobierno-y-politica-ia.md) y [alcance](../../context/hechos/cartera-y-concentracion.md) |
| Registro de riesgos de IA | Sin evidencia en el registro de partida; estado actual por contrastar | Vivo, revisado cada mes por el Council | Objetivo propuesto por el equipo |
| Controles técnicos de IA | Sin evidencia | Con señal en el mes 3: pasarela de salida y DLP, logs de acciones, red team interno; el externo, si se financia la demostración externa. Sin señal: *hooks* y escaneo de secretos en el equipo y red team acotado (ver "Controles según la decisión del mes 3") | Objetivo propuesto por el equipo |
| Certificación | ISO 27001 vigente | ISO 27001 con alcance extendido a IA; ISO 42001 como decisión de los meses 10-12, no como meta | [Fuente](../../context/hechos/seguridad-y-certificaciones.md) |

Las metas son objetivos del equipo, no benchmarks: se calibran con la línea base que
sale de los meses 1-3.

### Qué enseña el piloto interno

El piloto de abril de 2026 cumplió valor y adopción, pero falló en capacitación: solo
el 17% completó los tres cursos obligatorios y el 58% chocó con el límite de uso
([fuente](../../context/hechos/encuesta-y-pilotos-ia.md), n=12 y autoseleccionado). Dos
lecciones para el gobierno: un control que depende de que la gente lea un curso no es un
control, y un control que frena el uso empuja a la gente fuera del sistema oficial (el
anti-patrón del *governance perfecto*, [Council vs CoE](../../material/conceptos/m1u4-council-vs-coe.md)).

### Marco regulatorio: lo propio y lo heredado

En el escenario del plan, Acme Labs actúa como **proveedor tecnológico** de bancos y PSP
([fuente](../../context/hechos/regulacion-clientes-financieros.md), cotejada con los
textos ordenados del BCRA y las leyes actualizadas). Se separa lo que obliga a Acme Labs
de lo que le llega por contrato, según el sujeto y la actividad.

| Norma o marco | Quién está obligado | Cómo llega a Acme Labs | Estado de verificación |
|---|---|---|---|
| BCRA, requisitos mínimos de tecnología y seguridad (texto ordenado al 13/02/2026, Com. "A" 8401): sección 4.6 (IA propia o de terceros) y sección 10 (terceros) | Entidades financieras y PSP registrados (sección 1.1) | **Heredada**: como proveedor tecnológico, los servicios de IA de Acme Labs entran en la evaluación y las condiciones de tercerización del cliente | Cotejado con el texto ordenado oficial. La 4.6 exige a la entidad documentar objetivos de uso de IA propia o de terceros; definir responsables, modelos, datos, métricas y umbrales; evaluar riesgos; prevenir sesgos, documentar explicabilidad, revisar resultados e informar al cliente. La 10 exige evaluar y formalizar la relación con terceros, y la entidad conserva la responsabilidad. **No respalda** que un cliente le exija a Acme Labs controles concretos ni que le compre IA: eso, si existe, llega por contrato (ver "Licencia para vender"). Cambios posteriores, a revisar antes de la entrega |
| BCRA, proveedores de servicios de pago (texto ordenado al 02/10/2026, Com. "A" 8488), secciones 1 y 2 | Quien debe inscribirse como PSP según la función que desempeña, incluidos quienes ofrecen cuentas de pago | **Según la entidad operadora** del producto propio de pagos y su función y registro como PSP. Desarrollar el software no vuelve obligada a Acme Labs por sí solo | Cotejado con el texto ordenado oficial. Los requisitos específicos de habilitación del producto no se verificaron |
| Ley 21.526, arts. 39-40 (secreto financiero) | Entidades alcanzadas y su personal. El art. 39 protege sus **operaciones pasivas**, con las excepciones legales; el art. 40 regula la información que recibe el BCRA | **Heredada** de los clientes que sean entidades alcanzadas: condiciona qué información de esas operaciones puede salir hacia un modelo. Un PSP no se equipara a un banco | Cotejada con el texto actualizado |
| Ley 25.326 e información de la AAIP (datos personales y sensibles; el art. 12 restringe transferencias internacionales sin protección adecuada, con excepciones) | Quien trata datos personales | **Propia** cuando Acme Labs trata datos personales: enviar datos a un modelo alojado en el exterior exige evaluar destino, datos y mecanismo aplicable (la AAIP describe cláusulas contractuales modelo y normas corporativas vinculantes) | Cotejada con el texto actualizado y la AAIP. El rol de Acme Labs (responsable o encargado) lo confirma asesoría legal |
| EU AI Act (Reg. 2024/1689, modificado por el Omnibus 2026/1744) | Proveedores y desplegadores con sistemas o resultados usados en la UE (art. 2.1.c) | **No aplica por defecto**; se activa si un cliente opera en la UE o el resultado se usa allá | Fechas leídas de una copia del DOUE; falta cotejar con EUR-Lex ([fuentes faltantes](../../material/huecos.md)) |
| NIST AI RMF 1.0 | Nadie (voluntario) | **Voluntaria**: cada riesgo del registro lleva su función (Govern, Map, Measure, Manage) y su evidencia; se declara alineación, no cumplimiento | Confirmado en la página de NIST; el mapeo es por función, las subcategorías (por ejemplo GOVERN 1.6) no se verificaron |
| ISO/IEC 42001:2023 | Nadie (certificación voluntaria) | **Voluntaria**: se alinea con brecha documentada, no se certifica en el año | Confirmada la edición; ver el mapeo en Riesgos y en "Compliance: alcance explícito" |
| Guía SIGEN 197/2026 | Sector público nacional | **No aplica**; solo si un cliente es un organismo público | Existe; el anexo no se leyó |
| UIF y comunicaciones del producto de medios de pago | Sujetos obligados | Sin evaluar | **Hueco**: no se verificó |

**Rol proveedor frente a desplegador.** Cuando la IA va dentro de un producto que se
vende al banco, Acme Labs es **proveedor** (art. 3.3 del AI Act) y el banco es
**desplegador**; el proveedor es quien sostiene gestión de riesgos, documentación,
registros y supervisión humana. El art. 25 lo vuelve proveedor aun cuando solo integre
con marca propia un motor de terceros, o cuando oriente un modelo genérico a un uso de
alto riesgo ([fuente](../../material/frameworks/eu-ai-act-proveedor-desplegador.md)). La
consecuencia práctica es una **hipótesis**: aun fuera del alcance de la UE, algunos
clientes podrían pedirle por contrato esa disciplina de proveedor. Hay que separar dos
cosas que la hipótesis mezcla. Lo que el regulador le exige al **banco** (el texto ordenado de
tecnología del BCRA lo obliga a gestionar la IA propia o de terceros y a formalizar la
relación con sus terceros) es un requisito regulatorio del cliente;
que el banco se lo traslade a Acme Labs como condición de compra o de renovación es una
**exigencia comercial al proveedor**, y eso no está probado. Solo la evidencia
contractual de los meses 1-3 (ver "Licencia para vender") la confirma o la descarta.

**Calendario.** Según la fuente sobre el Omnibus, el alto riesgo del Anexo III (que incluye el
scoring crediticio) rige desde el 2027-12-02 ([fuente](../../material/conceptos/m1u4-ai-omnibus-sigen.md)),
que **cae dentro de la ventana**: los meses 10-12 terminan en diciembre de 2027. La Comisión Europea
[publica esa fecha](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
y enumera otros usos de alto riesgo además del crédito (empleo y educación, por ejemplo).
Eso confirma el calendario, no que aplique a Acme Labs. EUR-Lex pidió verificación
antirrobot y no se cotejó el texto consolidado: la fecha no va a una slide sin chequearla.

## Riesgos y mitigación

Registro de riesgos inicial. Probabilidad e impacto son **inherentes**: se valoran antes
del control, son cualitativos y siguen el criterio del equipo hasta tener la línea base de
los meses 1-3. El rol dueño de cada riesgo, su prueba y su **residual** están en la tabla
siguiente; las personas están a designar. La aceptación siempre se decide sobre el residual.

| Riesgo | Prob. inherente | Impacto inherente | Mitigación (control) | Disparador de abandono o escalamiento |
|---|---|---|---|---|
| **Datos de cliente en un modelo externo.** Datos o código de un cliente pasan por un modelo externo sin cláusula | Media | Alto: incumplimiento contractual y secreto financiero, con clientes muy concentrados | Matriz de restricciones por cliente (meses 1-3), default-deny sobre código de cliente; con señal en el mes 3, pasarela con allowlist (meses 4-6) | Un solo incidente confirmado: el responsable de seguridad suspende el uso de IA sobre ese cliente hasta cerrar el análisis de causa (ver "Derechos de decisión"); el Council lo revisa en su revisión mensual |
| **Inyección indirecta de prompts.** Prompt injection indirecta en un agente de código (repositorios, tickets, comentarios de PR, servidores MCP) | Media | Alto | Mínimo privilegio en credenciales, aprobación humana en el nivel "actúa con aprobación", entorno sin credenciales productivas, validación de salida con código determinístico | Un agente ejecuta una acción fuera de su alcance en pruebas: baja a "prepara, no ejecuta" hasta corregir |
| **Agencia excesiva.** Un agente con permisos de escritura sobre sistemas productivos | Baja | Muy alto | Tope de autonomía por nivel de riesgo (ver "Escala de autonomía"); "autónomo dentro de límites" solo en sandbox | Cualquier pedido de "autónomo dentro de límites" con acceso a producción pasa a decisión del Council |
| **Fuga de secretos.** Secretos en prompts o contexto | Media | Medio-alto | Escaneo de secretos antes del envío, lista cerrada de lo que nunca se envía (definida en el antecedente de abril; vigencia en la versión aprobada por contrastar), rotación | **Primer secreto expuesto confirmado**: se revoca y rota, se contiene el canal afectado y el responsable de seguridad decide con evidencia si se reanuda. **Recurrencia** (más de uno por tramo de tres meses): se bloquea el envío automático y se pasa a revisión previa |
| **IA embebida sin aprobar.** IA embebida en software de terceros activada sin aprobación (por ejemplo, funciones nuevas en la suite ofimática) | Alta | Medio | Inventario que incluye IA embebida; revisión de cambios de proveedor cada mes | Función de IA activa con datos Restringidos: se desactiva y se registra como incidente |
| **Un gobierno que frena.** Cuello de botella: el gobierno frena la entrega y la adopción migra por fuera | Media | Alto | Intake en niveles, SLA de 5 días hábiles para riesgo medio, autoservicio para riesgo bajo | Más del 20% de las solicitudes supera el SLA dos meses seguidos: se simplifica el proceso, no se agrega personal |
| **Capacidad concentrada.** Gobierno y seguridad dependen de pocas personas | Alta | Alto | Dos suplentes con runbooks; documentación de decisiones en el inventario | Una persona clave se va y no hay suplente entrenado: congelar altas de casos de riesgo alto |
| **Depender de un proveedor.** Dependencia de un solo proveedor de modelos y cambio de precio o límites | Media | Medio | Diseño neutral al modelo; ver [supuesto](../../context/supuestos/precio-y-dependencia-de-modelos.md) | Aumento de precio o recorte de límites que rompa el presupuesto: revisar proveedor en el Council |
| **Declarar controles que no existen.** Certificación de un producto propio, cumplimiento de IA | Baja | Muy alto: pérdida de confianza | Toda afirmación comercial sobre seguridad o IA la valida el responsable de seguridad; ningún producto propio se presenta como certificado | Una afirmación sin evidencia aparece en una propuesta: se retira y se corrige el procedimiento |

### Criterio de aceptación del riesgo residual

Propuesta que se integra como regla de los gates. El residual se
valora después de probar el control, no antes.

| Residual (prob. / impacto) | Quién lo acepta | Condición |
|---|---|---|
| Baja con impacto hasta Alto, o Media con impacto Medio | Dueño del riesgo | Queda en el registro; el Council lo ve en la revisión mensual |
| Media con impacto Medio-alto o Alto, o Baja con Muy alto | Council, con informe al CEO | Control compensatorio nombrado y fecha de revisión, como máximo la siguiente decisión de tramo (meses 3, 6, 9 o 12) |
| Alta con impacto Alto o mayor | Nadie | Se reduce o se suspende el uso; no hay excepción (ver "Catálogo de decisiones del Anexo C") |

**Combinaciones sin fila.** Media / Bajo, Media / Muy alto, Alta / Bajo, Alta / Medio y
Alta / Medio-alto no están en la tabla. No se aceptan por omisión: cuentan como residual no
aceptado, el uso afectado no se habilita ni se amplía, y si ya corre rige la suspensión
preventiva de Seguridad (ver "Derechos de decisión"). Agregar esas filas queda pendiente de decisión
del responsable humano de este anexo.

### Prueba, evidencia y residual de cada riesgo

Cada riesgo lleva su función del NIST AI RMF, un dueño por rol (sale de "Derechos de
decisión"; la persona está a designar), cómo se prueba el control y qué evidencia deja.
El residual es un **objetivo propuesto**, no una medición: se confirma o se corrige con
la prueba.

| Riesgo | Función NIST | Dueño del riesgo | Prueba del control | Evidencia esperada | Residual objetivo | Acepta |
|---|---|---|---|---|---|---|
| Datos de cliente en un modelo externo | Map, Manage | Responsable comercial del cliente | Revisión cruzada de la matriz contra los contratos; dato sintético marcado enviado por cada superficie (meses 4-6) | Matriz versionada con aprobador; informe de *bypass* por superficie; bloqueos en la pasarela | Baja / Alto en lo que pasa por la pasarela (casos propios y, si su régimen lo permite, el agente de código); Media / Alto en el resto | Council |
| Inyección indirecta de prompts | Measure, Manage | Dueño de negocio del caso | Red team interno (meses 4-6) y externo (meses 10-12) con inyección indirecta en repos y tickets sintéticos | Informe de red team con hallazgos y cierre; logs de acciones del agente | Baja / Alto | Dueño |
| Agencia excesiva | Govern, Manage | Dueño de negocio del caso | Revisión por tramo de tres meses de los permisos efectivos de cada agente contra su nivel de autonomía | Inventario con nivel por agente; exportación de permisos; acta | Baja / Muy alto | Council |
| Fuga de secretos | Measure, Manage | Responsable de seguridad | Secreto sintético por superficie (ejemplo abajo) | Bloqueo y alerta en la pasarela o en el equipo, según la superficie; ticket del ejercicio de mesa | Baja / Medio-alto donde hay bloqueo técnico; Media / Medio-alto donde solo hay control compensatorio | Dueño; Council si no hay bloqueo técnico |
| IA embebida sin aprobar | Govern, Map | Responsable de Tecnología | Cruce mensual de las novedades del proveedor contra el inventario | Inventario con fecha de revisión; configuración exportada | Media / Medio | Dueño |
| Un gobierno que frena | Govern, Measure | Responsable de Tecnología | Porcentaje de solicitudes fuera de SLA, desde el registro del intake | Reporte mensual del intake | Baja / Alto | Dueño |
| Capacidad concentrada | Govern | Responsable de Tecnología | El suplente corre el runbook sin el titular en el ejercicio de mesa (meses 4-6 y 10-12) | Runbooks versionados; acta del ejercicio | Media / Alto: baja poco en el año | Council |
| Depender de un proveedor | Map, Manage | Responsable de Tecnología | Ensayo de portabilidad del [Anexo B](02-arquitectura.md) | Informe del ensayo con la comparación de calidad | Media / Medio | Dueño |
| Declarar controles que no existen | Govern | Responsable de seguridad | Muestreo por tramo de tres meses de propuestas enviadas contra el registro de afirmaciones validadas | Registro de afirmaciones; muestra revisada | Baja / Muy alto | Council |

### Ejemplo completo: un secreto en un prompt

| Paso | Contenido |
|---|---|
| Riesgo | Una credencial (clave de nube, token de repositorio, cadena de conexión) sale en un prompt hacia un modelo externo. Inherente: Media / Medio-alto |
| Control | Escaneo de secretos en la pasarela antes del envío (previene), alerta al responsable de seguridad (detecta) y runbook de revocación y rotación (corrige). Dueño del control: ingeniería de seguridad |
| Prueba (meses 4-6) | Un juego de secretos **sintéticos** de formatos distintos, enviado por cada superficie de la matriz superficie→control→telemetría (ver "Seguridad"); nunca una credencial real. Criterio propuesto: donde hay bloqueo técnico (casos propios por la pasarela; el agente de código con *hooks* y escaneo en el equipo, y por la pasarela si su régimen la permite), todos bloqueados y alertados; en las superficies sin bloqueo técnico se registra que no hay bloqueo, como resultado esperado y no como falla oculta. En el ejercicio de mesa se mide el tiempo de alerta a revocación; el umbral lo propone seguridad y no está medido |
| Evidencia | Informe de la prueba por superficie y formato, logs de la pasarela con los bloqueos, ticket del ejercicio con sus tiempos y acta del Council. Es la misma evidencia que pediría la auditoría de la ISO 27001 con alcance extendido |
| Residual | Formatos que el escaneo no reconoce (Baja / Medio-alto): lo acepta el responsable de seguridad. Superficies sin bloqueo técnico (chat y escritorio, IDE y suite ofimática; y, en el régimen de suscripción que no permite gateway, lo que los *hooks* y el escaneo del equipo no reconocen del agente de código) (Media / Medio-alto): lo acepta el Council con control compensatorio (cuentas corporativas, consola de administración, rotación periódica) y revisión en la siguiente decisión de tramo |
| Cuándo vence la aceptación | El primer secreto expuesto por una superficie aceptada reabre la decisión (disparador del riesgo de fuga de secretos). El bloqueo de secretos no se relaja nunca (ver "Controles por tramo") |

### NIST y la ISO 42001: mapeo, evidencia y qué no se afirma

| Función NIST | Qué la implementa acá | Evidencia esperada | Elemento de sistema de gestión ([ISO 42001](../../material/conceptos/m1u4-eu-ai-act-nist-iso.md)) |
|---|---|---|---|
| Govern | Council, derechos de decisión, política, criterio de aceptación | Política aprobada con versión y alcance documentados, actas, matriz RACI | Políticas y responsabilidades |
| Map | Intake (ver "Intake y clasificación de riesgo") con preguntas de contexto, cliente y Anexo III; matriz de restricciones; inventario | Registros del intake, matriz, inventario | Gestión de riesgos y oportunidades |
| Measure | Pruebas de la tabla anterior, red teams, cobertura de la pasarela | Informes de prueba y métricas de cobertura | Monitoreo |
| Manage | Controles por tramo, incidentes, aceptación del residual | Tickets, registro de residuales aceptados, revisión por tramo | Procesos y mejora continua |

**Alinear no es certificar.** El NIST AI RMF es voluntario: se declara "alineado", nunca
"cumple". La ISO 27001 es la única certificación que el plan toca, y solo para extender
su alcance. Para la ISO 42001 se documenta la brecha en los meses 10-12 y certificar es una
decisión del cierre del mes 12. La frase comercial permitida es "alineado con el NIST AI RMF,
brecha frente a ISO 42001 documentada"; cualquier otra cae en el riesgo de declarar controles
que no existen. El mapeo de esta tabla es por función: las cláusulas de la 42001 no se
cotejaron contra su texto.

## Decisiones

### Modelo operativo: AI Council liviano, con CoE virtual

| Alternativa | Ventaja | Costo o riesgo | Veredicto |
|---|---|---|---|
| Solo un AI Council | Barato, decide rápido | Sin nadie que habilite: queda en comité fantasma | Descartada |
| Solo un CoE | Habilita y construye | En 60-70 personas sería una *software factory* central que compite con el delivery | Descartada |
| **Council de 5 asientos + CoE virtual** (recomendada) | Decide y habilita con tiempo reasignado, sin estructura nueva | Depende de pocas personas (riesgo de capacidad concentrada) | **Elegida** |
| Asignar la función solo a Tecnología | Cero comités | El negocio pierde el *accountability* del resultado y del riesgo comercial | Descartada |

**Council.** Cinco asientos con voto, y se integra al comité de tecnología, que el
antecedente de abril define como aprobador de herramientas
([fuente](../../context/hechos/gobierno-y-politica-ia.md)), para no crear
burocracia paralela: responsable de Tecnología (preside), responsable de seguridad,
responsable de Operaciones (delivery, que es quien conoce las restricciones de cada
cliente), responsable de Experiencia de cliente y comercial, y responsable de Finanzas.
Talento participa cuando hay temas de personas; el CEO es sponsor y última instancia.
Legal: la estructura no muestra un área interna ([fuente](../../context/hechos/tamano-y-estructura.md)),
así que se asume asesoría externa a demanda (ver Cautelas).

**CoE virtual.** No es un equipo nuevo: es el 10%-15% del tiempo de un grupo acotado
([supuesto](../../context/supuestos/capacidad-de-inversion.md)) que mantiene plantillas,
*golden paths*, el inventario y la capacitación, junto con Arquitectura y Personas. Su
función es habilitar; no aprueba nada que el Council no le delegó.

### Derechos de decisión (una sola A por decisión)

| Decisión | A (decide) | R | C | I |
|---|---|---|---|---|
| Autorizar la validación inicial en preparación de 2026 | Directorio o autoridad formalmente delegada | CAIO | Operaciones y managers, Finanzas, Seguridad | Council |
| Liberar M1-M3 tras la validación inicial | Directorio o autoridad formalmente delegada | CAIO | Operaciones y managers, Finanzas, Seguridad | Council |
| Política de IA y sus cambios | Directorio (ratifica) | Responsable de seguridad | Council, CEO | Toda la organización |
| Aprobar una herramienta o modelo nuevo | Responsable de Tecnología | Administrador de licencias | Seguridad, Finanzas | Council |
| Qué datos puede usar un caso | Dueño del dato | Seguridad | Legal externo, Operaciones | Council |
| Usar IA sobre el código o los datos de un cliente (en el horizonte: solo lo que el cliente permite en su entorno; enviarlos a un modelo externo, no antes del cierre del mes 12) | Responsable comercial del cliente | Operaciones | Seguridad, Legal externo | Council |
| Nivel de autonomía de un agente | Dueño de negocio del caso | Ingeniería | Seguridad | Council |
| Salida a producción de una función de IA en el producto | Dueño de producto | Ingeniería | Seguridad, Operaciones | Council |
| Excepción a una política de riesgo alto | Council | Responsable de seguridad | Dueño del caso | CEO |
| Incidente de IA (contención y comunicación al cliente) | Responsable de seguridad | Ingeniería | Comercial, Legal externo | CEO, Council |
| Suspensión preventiva de un uso por control incumplido, incidente o residual no aceptado | Responsable de seguridad | Ingeniería y dueño del caso | Dueño del riesgo | Council, CEO y autoridad del gate |
| Gasto de IA fuera del presupuesto | Responsable de Finanzas | Tecnología | Council | CEO |

Regla de gobierno: la IA cambia el proceso, no elimina a su dueño
([RACI](../../material/conceptos/m1u4-raci-ownership.md)). El responsable de cada
rol está **a designar**; Personas desarrolla los roles y su capacidad.

**Seguridad precede a valor, gasto y adopción.** El responsable de seguridad puede
suspender preventivamente el uso o la superficie afectados aunque los indicadores
económicos y de adopción cumplan. El Council también puede frenar un frente en su revisión
mensual. La contención no espera la siguiente reunión ni habilita gasto nuevo. Una
suspensión preventiva solo se levanta por el procedimiento de reanudación que sigue; un
desacuerdo con ella escala al CEO, última instancia del Council.

**Incidentes antes del plan de M1-M3.** El plan de incidentes es un entregable de los meses
1-3 (la ruta de incidentes y suspensión de la fila «Política e intake» del insumo del
paquete mínimo), y el ejercicio de mesa de los meses 4-6 lo prueba ya escrito. Quedan
pendientes de diseño y decisión humana la definición de incidente de IA, las severidades,
los plazos de contención y de aviso al cliente y la preservación de evidencia; este anexo
no les fija valores. Ningún uso del paquete mínimo se habilita sin esa ruta de incidentes y
suspensión escrita. Mientras tanto rigen la A del responsable de seguridad para contener y
comunicar, la suspensión preventiva y el aviso al cliente que pida su contrato.

Para reanudar, ingeniería produce la prueba corregida y una persona distinta la verifica;
la autoridad del residual lo acepta según la tabla de este anexo. La autoridad del gate
registra la reanudación y decide los fondos, si corresponden. Productor, verificador y
persona que firma el gate se asignan por separado y quedan a designar; quien produce la
evidencia no verifica su propio trabajo ni autoriza su propio pase.

**Verificador independiente: actividad costeada y salida sin perfil.** Identificar al
verificador es un entregable de la validación inicial, con horas de verificador senior
costeadas en el [Anexo E](05-business-case.md); en M1-M3 la verificación de los
compensatorios tiene 8-16 h propias (ver "Insumos para Finanzas"). Hoy la regla escrita
para cuando no hay una persona independiente es no declarar probado el control y
suspender o reducir el uso. Como la capacidad de seguridad está concentrada en pocas
personas, falta decidir cómo se reduce. Propuesta de Gobierno, sin confirmar todavía
por el responsable humano de este anexo:

| Alternativa | Costo | Riesgo | Abandono |
|---|---|---|---|
| (a) Excluir la superficie sin verificador hasta tener uno | Sin contratación externa prevista. No recupera lo ya incurrido; el ajuste de alcance y sus horas se confirman dentro del techo o se recostea | Achica la prueba y la medición de la cohorte | Si la exclusión deja sin superficies a la cohorte, se reduce o se detiene el tramo y se vuelve al autorizante |
| (b) Verificador externo acotado | Sin cotizar: no está en ningún techo | Dependencia y plazo de contratación; exige recosteo y autorización antes de comprometerlo | Si la cotización no entra en el techo autorizado, no se contrata y rige (a) |

Recomendación de Gobierno: (a) mientras (b) no esté cotizada y autorizada. Ninguna
de las dos permite declarar probado un control que verificó su productor.

### Validación inicial: dos autorizaciones antes de M1

**Propuesta en borrador.** El diseño se detalla en la
[fuente de horas y techos](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial)
y en el [Anexo F](06-roadmap-riesgo.md).

El aval para incorporar la propuesta al borrador no acredita acuerdo del equipo
ni autorización empresarial.

**Primera autorización.** El Directorio o su autoridad formalmente delegada autoriza
una preparación de diez días hábiles en 2026: 60-96 h organizativas más las 20-40 h
técnicas existentes, total 80-136 h.

El techo es 8k USD de tiempo valorizado y cero caja incremental. Operaciones y
managers liberan las agendas y explicitan el trabajo desplazado antes de empezar;
CAIO coordina y Finanzas concilia costo y solapes.

Se contrasta el diagnóstico, concilia la capacidad semanal y revisa la versión,
el alcance y la aprobación documentada de la política, además del estado de las
restricciones; se prepara el alcance y pide cotización legal. Esta etapa
no ejecuta el dictamen externo ni habilita nuevos despliegues o contratos.

Su verificador independiente valida evidencia organizativa; no sustituye las
pruebas técnicas de C.

**Segunda autorización, antes de M1.** La misma autoridad decide continuar, reducir o
resecuenciar, o detener, con diagnóstico revisado, capacidad aceptada, acta de viabilidad
técnica y presupuesto 2027 comprobado.

Puede liberar hasta los 71k USD restantes del pedido: el acumulado propuesto
es 79k USD (10k USD de caja y 69k USD de tiempo), no 79k USD nuevos.

Productor, verificador y firmante son personas distintas, con designaciones empresariales
pendientes; el Council recomienda y revisa riesgos, sin liberar fondos.

El pase económico no habilita prácticas ni superficies. El dictamen externo de 8-16 h
ya presupuestado permanece en M1; política, matriz y controles aplicables deben estar
completos antes de los usos que los requieran, con residual aceptado según la tabla de C.

La base prospectiva ocupa semanas 1-4, con extensión hasta la 8; formación y prácticas
empiezan después de congelarla. Los controles urgentes y la suspensión preventiva de
Seguridad no esperan a la base.

Si faltan evidencia, independencia o agendas, o se excede el techo, se reduce o detiene
y se vuelve al autorizante antes de ampliar el alcance.

### Ritmo operativo

**El riesgo se mira cada mes.** Después de las dos autorizaciones iniciales, la
liberación de fondos sigue las decisiones trimestrales. Hay tres cadencias:

| Cadencia | Qué se revisa | Dónde se hace |
|---|---|---|
| Semanal (20 min) | Incidentes, solicitudes del intake y bloqueos | Dentro de la reunión técnica existente |
| Mensual (2 h) | Revisión mensual del Council con el tablero: caja y tiempo consumidos contra el techo del tramo, uso semanal por área, incidentes y secretos expuestos, señales de plataforma (contrato, precio por consumo, cliente) y avance de hitos. Además, inventario, excepciones, registro de riesgos y costo de IA | Council, integrado al comité de tecnología |
| Cada tres meses | Estado de los controles, valor, niveles de autonomía y decisiones de escalar o retirar; **liberación de fondos** | Informe al Directorio y decisiones de los meses 3, 6, 9 y 12 |

**Qué puede hacer la revisión mensual:** frenar o cortar un frente, activar una
contingencia, registrar una señal en el mes en que llega y escalarla al Directorio.
**No libera fondos:** eso queda en las autorizaciones iniciales y en las decisiones
de los meses 3, 6, 9 y 12, a cargo del Directorio o autoridad formalmente delegada.

**Qué no cambia.** Las esperas de 6 semanas y los métodos de medición (intervalo de
throughput, base congelada) siguen igual: el throughput necesita semanas de datos y una
lectura mensual no tiene señal estadística. El tablero mensual lo muestra como tendencia,
sin decidir por él.

**Costo: cero adicional.** El tablero se arma con salidas mensuales que ya existen: el
reporte mensual del intake y el cruce mensual de novedades del proveedor (tabla de controles
de este anexo), el reporte mensual de FinOps con el escenario de consumo
([Anexo B](02-arquitectura.md)), el registro de riesgos que el Council ya revisa cada mes y
el uso semanal por área ([Anexo D](04-personas-cultura.md)). El [Anexo E](05-business-case.md)
presupuesta el Council a 5 asientos × 6 h por tramo de tres meses; tres reuniones mensuales
de 2 h entran ahí (ver "Insumos para Finanzas"). Es la misma reunión que el registro de
riesgos "revisado cada mes por el Council".

**Controles de revisión por tramo.** La revisión de permisos efectivos de cada agente y el
muestreo de propuestas enviadas siguen **por tramo de tres meses**: hacerlos cada mes agrega
horas de ingeniería de seguridad y de analista que el presupuesto no tiene, así que no se
pasan a mensual sin una decisión de costo del [Anexo E](05-business-case.md). El Council los
ve en la revisión mensual solo como estado del tablero.

### Governance Stack aplicado a Acme Labs

| Capa | Qué existe | Qué se hace | Tramo |
|---|---|---|---|
| Principios | 4 principios documentados en el antecedente de abril (herramientas corporativas, desconfiar del output, responsable humano, lo que no se mide no se justifica) | Se propone mantenerlos, contrastando con la versión aprobada | Meses 1-3 |
| Política | Aprobada según confirmación del responsable del caso del 20/10/2026; versión y alcance por revisar | Revisar aprobación documentada y aplicar la política; proponer tres alcances: uso interno, IA en el producto y proveedores o modelos. Los cambios requieren decisión empresarial | Meses 1-6 |
| Estándares | Clasificación de datos en 4 niveles y lista de lo que nunca se envía en el antecedente de abril; vigencia por contrastar | Se suma la matriz de restricciones por cliente, la escala de autonomía (niveles 0 a 4) y la de riesgo | Meses 1-3 |
| Controles | El antecedente de abril define revisión del output, aprobación por el comité y reporte de incidentes sin sanción; implementación por probar | Se suman pasarela de salida, DLP, escaneo de secretos y logs de acciones | Meses 4-9 |
| Evidencia | Auditoría mensual de uso prevista en el antecedente; ejecución por contrastar | Inventario, registro de riesgos, logs y actas del Council: la evidencia sale del trabajo normal | Meses 1-12 |

### Intake y clasificación de riesgo

Un solo formulario corto, con tres niveles y una lista de prohibidos. Las variables son
autonomía, acceso, consecuencia y reversibilidad
([criterios](../../material/conceptos/m1u4-criterios-gobierno-agentico.md)). Los niveles del
intake (1 a 3) miden riesgo; no son los niveles de autonomía de la escala de más abajo.

| Nivel | Criterio | Quién aprueba | Plazo objetivo |
|---|---|---|---|
| 1. Bajo | Autonomía "sin IA" o "asiste", datos Público o Interno, herramienta ya aprobada | Autoservicio: se registra en el inventario | Inmediato |
| 2. Medio | Autonomía "prepara, no ejecuta" o "actúa con aprobación" sobre sistemas internos, o datos Confidenciales con herramienta aprobada | Dueño del caso y responsable de seguridad | 5 días hábiles |
| 3. Alto | Toca código o datos de un cliente, o va dentro del producto que se vende | Cada decisión con su A de "Derechos de decisión": el uso sobre un cliente, el Responsable comercial del cliente, con la matriz verificada; la salida a producción, el Dueño de producto. El residual lo acepta quien fija el "Criterio de aceptación del riesgo residual" (por ejemplo, el Council en Media / Alto). Los datos productivos de un cliente no salen hacia un modelo externo durante el horizonte | Hasta el siguiente Council (30 días como máximo), si el residual le corresponde al Council |
| Prohibido en el plan | Decisiones de crédito o scoring sobre personas, datos de categoría especial, autonomía "autónomo dentro de límites" con acceso a producción, datos productivos de clientes hacia un modelo externo | No se aprueba en el horizonte; reabrirlo es una decisión del cierre del mes 12 que rige después (ver "Catálogo de decisiones del Anexo C") | Ver "Escala de autonomía" |

**Cuatro decisiones que no se mezclan.** En un caso de cliente o de producto, usar IA
sobre un cliente, salir a producción, aceptar el residual y liberar fondos tienen cada una
su A (ver "Derechos de decisión" y "Criterio de aceptación del riesgo residual"). El Council
revisa el caso y acepta el residual que le toca; no es una segunda A del uso ni de la
salida a producción. Los fondos los liberan las autorizaciones iniciales y las decisiones
de los meses 3, 6, 9 y 12; el gasto fuera del presupuesto, Finanzas.

**Regla transitoria hasta que exista la matriz de un cliente.** Junta lo que el plan ya fija,
para usos nuevos y existentes:

- Lo que el contrato de un cliente prohíbe queda afuera, sea un uso nuevo o uno que ya
  existe (slide «Gobierno y seguridad», decisión 3). Si ya corre, lo suspende Seguridad
  como control incumplido (ver "Derechos de decisión").
- La restricción de "Derechos de decisión" rige sin cambios: en el horizonte, IA sobre el
  código o los datos de un cliente solo en lo que el cliente permite en su entorno, y
  enviarlos a un modelo externo, no antes del cierre del mes 12. Donde la superficie no
  tiene bloqueo técnico, la cubre un control compensatorio (ver "Tres cosas que no se
  confunden").
- **Tensión pendiente:** el intake (fila de prohibidos) y el catálogo nombran solo los
  *datos productivos* hacia un modelo externo; la restricción de arriba alcanza al código y
  a los datos. Hasta que el responsable humano de este anexo lo concilie, rige la restricción
  más estricta y no se habilita ningún alcance nuevo por la redacción más corta.
- Un uso nuevo o ampliado sobre un cliente no se habilita sin la lectura de su contrato: la
  matriz frena los casos de cliente hasta completarse, mientras tanto cada caso se valida a
  mano ([Anexo D](04-personas-cultura.md), "Staffing") con el Responsable comercial del
  cliente como A, y lo ambiguo queda afuera (*default-deny*).
- Un uso existente que toque código o datos de un cliente no se acepta automáticamente por
  ser una herramienta aprobada: entra en la revisión del residual de usos existentes (ver
  "Calendario del mínimo propuesto"). Este anexo no dispone detenerlo, salvo la suspensión
  preventiva de Seguridad. Queda pendiente de decisión humana qué rige para ese uso hasta
  tener la matriz (pausarlo o aceptarlo como residual) y si encaja en la restricción de
  arriba; si se acepta, lo hace la autoridad que fija el criterio de aceptación (el Council,
  con informe al CEO, si el residual es Media / Alto).

El plazo de 5 días hábiles es un objetivo del equipo, más rápido que las 2 a 4 semanas
del antecedente de la política de abril, cuyo plazo vigente está por contrastar, para
que el control no empuje el uso fuera del sistema oficial. El cambio requiere decisión empresarial.

### Escala de autonomía: topes para los 12 meses

La escala tiene cinco niveles, con el nombre fijo que se usa en todo el anexo:

| Nivel | Nombre |
|---|---|
| 0 | Sin IA |
| 1 | Asiste |
| 2 | Prepara, no ejecuta |
| 3 | Actúa con aprobación |
| 4 | Autónomo dentro de límites |

| Ámbito | Tope | Reversible |
|---|---|---|
| Agentes de código internos con Claude Code, Copilot | Nivel 3 (actúa con aprobación) y *hooks* de permisos | Sí |
| Agentes de código con credenciales productivas | Nivel 2 (prepara, no ejecuta) | Sí |
| Nivel 4 (autónomo dentro de límites) | Solo en *sandbox*, sin credenciales productivas ni acceso a datos de cliente. Con efectos externos, no en el horizonte | Sí |
| Funciones de IA dentro del producto que se vende | Niveles 1-2 ("asiste" y "prepara, no ejecuta") durante todo el horizonte. Subir al nivel 3 es una decisión del cierre del mes 12 (efecto externo), que rige después | Sí hasta que se activa; luego es irreversible (ver "Catálogo de decisiones del Anexo C") |

La escala de autonomía es un marco de referencia, no un estándar oficial.

### Compliance: alcance explícito

- **No se ofrecen decisiones de crédito ni scoring en los 12 meses.** Es una delimitación
  del plan y un apetito de riesgo propuesto, no una clasificación normativa: vender a bancos
  y fintechs no vuelve por sí solo de alto riesgo un uso, y la fuente regulatoria de este
  anexo no acredita un régimen específico del BCRA para crédito o scoring. La exclusión evita
  cargar con los deberes de proveedor de un caso crediticio del Anexo III si un cliente opera
  en la UE (disparador, ver más abajo) mientras los controles maduran. Es **reversible**: el cierre del mes 12 decide si se reabre
  para el plan siguiente, si un cliente lo pide y el Council aprueba el costo de proveedor de
  alto riesgo; no se ejecuta dentro del horizonte.
  Excluir el crédito no demuestra por sí solo que no haya otros usos de alto riesgo (empleo,
  educación): el intake pregunta por cada categoría del Anexo III y un sí pasa el caso a
  Nivel 3 con Legal externo.
- **ISO/IEC 42001: alinear, no certificar en el año.** Se extiende el alcance de la ISO
  27001 existente con los controles de IA y se registra la brecha frente a 42001. Alternativa
  descartada por ahora: certificar 42001, que suma costo de auditoría y carga documental sin
  que haya hoy un cliente que lo exija ([supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md)).
  La decisión de certificar se toma en el cierre del mes 12 y es **reversible**.
- **EU AI Act: tratarlo como disparador, no como obligación.** Se pregunta a cada cliente
  si opera en la UE o usa resultados allá. Si la respuesta es sí, el caso pasa a Nivel 3.
- **El NIST AI RMF organiza el registro de riesgos** (Govern, Map, Measure, Manage):
  cada riesgo lleva su función, su prueba y su evidencia (ver Riesgos). Se declara
  alineación, sin buscar cumplimiento formal.
- **La política aprobada se documenta y aplica (meses 1-3).** Se revisan versión,
  alcance y constancia de aprobación; no se pide aprobarla de nuevo. Los cambios
  propuestos siguen el derecho de decisión del Directorio y son compromisos internos
  enmendables: no firman nada con un cliente. Se propone revisión anual y revisión
  extraordinaria en la lectura del mes 6.

### Catálogo de decisiones del Anexo C: ámbito, fecha y compromiso

Tres pasos que no se confunden: **aprobación interna** (Council o Directorio),
**negociación no vinculante** con un cliente y **firma** de un compromiso. Ninguna
excepción puede contradecir una prohibición del horizonte.

| Decisión | Ámbito | Fecha mínima | Autoridad | Condición | Compromiso exacto |
|---|---|---|---|---|---|
| Decidir cambios de alcance de la política aprobada | Interno | Meses 1-3 | Directorio | Segunda autorización: M1-M3 tras la validación inicial; versión, alcance y aprobación documentada revisados | Compromiso interno enmendable; sin firma con clientes; no es una nueva aprobación de la política existente |
| Cláusula tipo de IA para contratos | Interno y negociación | Meses 7-9 | Council | Una función de IA con documentación técnica y supervisión humana | Texto listo y negociación no vinculante |
| Firma de un compromiso contractual de IA con un cliente | Externo | Cierre del mes 12 | Council | Cláusula tipo, matriz del cliente y red team sin críticos | Irreversible: el compromiso queda firmado |
| Enviar datos productivos de un cliente a un modelo externo | Externo | No antes del cierre del mes 12 | Responsable comercial del cliente (A del uso); el residual lo acepta el Council según el criterio de aceptación | Cláusula firmada, matriz y controles demostrados | Irreversible |
| Subir una función de IA del producto al nivel 3 (actúa con aprobación) | Externo | Cierre del mes 12 | Council | Evidencia del piloto y red team externo sin críticos | Rige después del horizonte |
| Nivel 4 (autónomo dentro de límites) con efectos externos o acceso a producción | Externo | Fuera del horizonte | Council | Decisión del cierre del mes 12 para el plan siguiente | Prohibido hasta entonces |
| Reabrir crédito o scoring | Producto | Cierre del mes 12 (decisión) | Council con Legal externo | Pedido de un cliente y costo de proveedor de alto riesgo aprobado | Rige después del horizonte |

### Seguridad: modelo de amenazas y controles

Las amenazas siguen el OWASP Top 10 for LLM Applications 2025 (LLM01 inyección de
prompts, LLM02 divulgación de información sensible, LLM06 agencia excesiva, LLM07 filtración
del prompt del sistema), que complementa el marco de seguridad de sistemas de IA (ataques y defensa, de prompt
injection a red teaming; [unidad](../../material/unidades/m3u1-seguridad.md)).

| Amenaza | Prevención | Detección | Respuesta | Conexión con lo existente |
|---|---|---|---|---|
| Inyección de prompts directa e indirecta | Mínimo privilegio, contenido no confiable segregado, validación de salida con código | Logs de acciones de agentes y alertas de desvío | Red teaming interno (meses 4-6) y externo (meses 10-12) | Revisión de PR obligatoria para código con IA ([fuente](../../context/hechos/stack-y-plataforma.md)) |
| Fuga de datos (DLP) | Clasificación de 4 niveles, anonimización, cifrado, control de acceso | Escaneo de secretos y PII en prompts | Plan de incidentes con aviso al cliente | Política con aprobación informada, definiciones de abril por contrastar y controles por probar; cuentas AWS separadas por proyecto |
| Aislamiento de datos de clientes | Entornos y credenciales por cliente; la IA no cruza datos entre proyectos | Auditoría del acceso por proyecto | Suspensión por cliente | Staffing opera con las herramientas de cada cliente, fuera del alcance del control |
| Cadena de suministro (modelos, servidores MCP, proveedores) | Lista cerrada de servidores MCP, contrato sin entrenamiento, revisión de cambios del proveedor | Revisión mensual de proveedores y subprocesadores | Retiro del proveedor | Contrato organizacional de agentes de código |
| Secretos | Escaneo previo al envío y rotación | Alertas | Primera exposición: revocar y rotar, contener el canal y decidir la reanudación con evidencia; la recurrencia escala a bloqueo (riesgo de fuga de secretos) | Auditoría periódica de vulnerabilidades de código e imágenes |

**Matriz superficie → control → telemetría.** La pasarela enruta llamadas a modelos; los tres
productos corporativos tienen superficies que quizá no pasen por ella
([fuente](../../context/hechos/uso-ia-interno.md)). Lo siguiente es el diseño a probar en los
meses 4-6, no una capacidad demostrada: ningún control de esta tabla se verificó contra el
producto real.

**Tres cosas que no se confunden.** *Prohibición*: lo que la política dice que no se hace;
rige en todas las superficies, pero por sí sola no impide nada. *Bloqueo técnico*: un control
que detiene el envío (pasarela con DLP, escaneo de secretos antes del envío); solo existe donde
la superficie lo admite y se prueba en los meses 4-6. *Control compensatorio*: lo que reemplaza al
bloqueo donde no se puede bloquear (cuentas corporativas, consola de administración, rotación,
auditoría); detecta o reduce, no previene. Donde hay prohibición sin bloqueo técnico queda un
**residual** que acepta el Council (criterio de aceptación) y que se informa al board.

| Superficie | Prohibición (política) | Bloqueo técnico | Control compensatorio | Telemetría | Riesgo de *bypass* | Estado |
|---|---|---|---|---|---|---|
| Casos propios (producto y agentes internos nuevos) | Datos prohibidos y secretos | Solo por la pasarela, 100%: DLP y escaneo de secretos | No hace falta: no tienen otra ruta | Logs de la pasarela | Bajo: sin ruta alternativa por diseño | Por diseño; a probar en los meses 4-6 |
| Agente de código en terminal (~90% de los eventos de ese agente) | Secretos y datos de cliente | *Hooks* de permisos y escaneo de secretos en el equipo y el repositorio, siempre. DLP sobre prompts en la pasarela **solo si el régimen comercial permite enrutarlo** (suscripción que permite gateway o pago por consumo; [Anexo B](02-arquitectura.md), "Política de ruteo") | Suscripción que no permite gateway (la suscripción plana se rompería): lista cerrada de MCP, telemetría existente y ruteo ensayado, listo para activarse | Consola del proveedor; logs de la pasarela si se enruta | Uso con una cuenta o configuración personal | A probar en los meses 4-6 |
| Asistente de código en el IDE | Secretos y datos de cliente | Ninguno demostrado: no pasa por la pasarela hasta probar lo contrario | Política de la organización del proveedor y lista de repos permitidos | Consola de administración del proveedor | Alto: sin ruta por la pasarela | A probar en los meses 4-6; si no hay control técnico, rige la política y se reporta aparte |
| Chat y escritorio del asistente general | Datos Restringidos y de cliente | Bloqueo en navegador o equipo, solo si el parque lo permite (a probar) | Cuentas corporativas, ajustes de retención y conectores | Consola de administración | Alto: cuentas personales | A probar en los meses 4-6 |
| Asistente de la suite ofimática | Datos Restringidos y de cliente | Ninguno de la organización: lo da la configuración del administrador | Revisión mensual de funciones nuevas (riesgo de IA embebida sin aprobar) | Registros de auditoría de la suite | Medio: activación por defecto del proveedor | A probar en los meses 4-6 |
| Servidores MCP y conectores | Servidores fuera de la lista | Lista cerrada (allowlist) donde se pueda imponer | Revisión de cambios e inventario | Inventario y logs de la pasarela | Medio: instalación local por una persona | A probar en los meses 4-6 |

**Denominador del 90%.** Eventos del agente de código en terminal que la telemetría de la
pasarela cuenta sobre el total de eventos del agente (según la consola del proveedor). El 90%
rige solo si el agente se enruta (suscripción que permite gateway o pago por consumo, según el
[Anexo B](02-arquitectura.md)). Si enrutar obliga a facturar
por API (suscripción que no permite gateway), el agente no se enruta mientras la suscripción
sea plana y se le exige control verificado sin pasarela; no cuenta en el 90% ni se presenta
como "enrutado". Los casos
propios van al 100% por la pasarela, aparte. Las demás superficies no entran en el 90%: se
reportan con su propia cobertura (seats activos bajo control sobre seats activos) y las que
quedan afuera se listan como riesgo aceptado, no se cuentan como cubiertas. Un gate de
cobertura nunca obliga a enrutar si eso encarece el servicio: la tensión con el
[Anexo F](06-roadmap-riesgo.md) queda abierta (ver "Tensiones con otras áreas"). La
prueba de integración y de *bypass* por herramienta, y la
migración de la configuración, tienen costo propio en "Insumos para Finanzas".

El aislamiento de clientes tiene un límite: el staffing trabaja con las herramientas que
permite cada cliente ([fuente](../../context/hechos/uso-ia-interno.md)), por lo que el
control de Acme Labs no alcanza a esos equipos; para ellos rige la cláusula contractual.

### Red teams: cuatro alcances

El plan nombra cuatro ejercicios distintos. Los internos son tiempo; los externos no
tienen cotización y sus montos son los supuestos ya publicados ([precios sin cotizar](../../context/supuestos/precios-externos-sin-cotizar.md)).

| Ejercicio | Qué prueba | Cuándo y condición | Costo | Dueño |
|---|---|---|---|---|
| Interno acotado al agente de código | Inyección indirecta y acciones no autorizadas con repositorios y tickets sintéticos | Las dos ramas; antes de habilitar cada uso del mínimo M1-M3 | Tiempo, dentro de la prueba previa por superficie de este anexo y del aporte de seguridad del [Anexo B](02-arquitectura.md) | Gobierno |
| Interno de la pasarela y las superficies | Bloqueo, registro y *bypass* con la plataforma | Meses 4-6, solo con señal en el mes 3 | 40-80 h: 750-3.750 USD de tiempo | Gobierno |
| Del piloto de producto | La primera función de IA antes de salir | Meses 7-9, solo con señal de cliente en el mes 6 | 5.000-15.000 USD de caja | Arquitectura, con Gobierno |
| Externo | Evidencia de un tercero para clientes y para la firma del mes 12 | Meses 10-12, solo con señal contractual o producto en el mes 9 | 10.000-25.000 USD de caja | Gobierno |

**Desacuerdo a la vista (piloto y externo).** Cubren alcances distintos y no se suman ni
se sustituyen automáticamente. El [Anexo E](05-business-case.md) estima un ahorro de
5.000-15.000 USD si el producto se libera y un mismo contrato cubre el piloto y la
reprueba. Criterio de Gobierno: el ejercicio del piloto reemplaza al externo solo si su
alcance incluye las superficies y controles que pida el cliente, no solo el producto.
Lo concilian Arquitectura, Gobierno y Finanzas; si no hay producto, no hay solape.

### Controles por tramo

Los objetivos son propuestas del equipo, a calibrar con la línea base de los meses 1-3. Los
meses 1-3 (enero-marzo de 2027) rigen en las dos ramas de la decisión del mes 3. Los meses
4-6 y 10-12 describen la **rama con señal en el mes 3**; la rama sin señal, que corre como la
alternativa de gobierno mínimo y formación del [Anexo E](05-business-case.md), está en "Controles según la decisión del mes
3". Los meses 7-9 dependen de la señal de cliente.

| Tramo | Controles | Criterio de éxito | Costo en velocidad | Condición de abandono o cambio |
|---|---|---|---|---|
| Meses 1-3 | Revisar versión, alcance y aprobación documentada de la política y aplicarla; inventario v1; matriz de restricciones de los clientes principales y lectura de la evidencia contractual para la decisión del mes 3 (ver "Licencia para vender"); intake en 3 niveles; plan de incidentes | Política con documentación revisada y aplicación registrada; inventario con las 3 herramientas aprobadas, los servidores MCP y la IA embebida; matriz al 100% de los clientes principales | Bajo: solo trámite. La matriz frena los casos de cliente hasta completarse | Si más del 30% de los contratos queda ambiguo a los 4 meses, se aplica *default-deny* sobre el código de ese cliente y se pide revisión legal |
| Meses 4-6 | Matriz superficie→control→telemetría (ver "Seguridad") con prueba de integración y de *bypass* por herramienta; pasarela con allowlist y DLP sobre prompts; escaneo de secretos; logs de acciones; red team interno; ejercicio de mesa de incidentes, que incluye la ruta de primera exposición de un secreto | Si su régimen comercial lo permite, al menos el 90% de los eventos del agente de código pasa por la pasarela (denominador en "Seguridad"); si no, control verificado sin pasarela y ruteo ensayado; casos propios, 100%. Cada superficie restante tiene su control compensatorio y su cobertura reportada aparte, y el residual sin bloqueo técnico va al Council; red team con hallazgos críticos cerrados | Medio: fricción en el agente de código | Si la actividad semanal de seats cae más de 15% frente a la línea base de los meses 1-3 dos meses seguidos, **solo los usos permitidos** pasan a monitoreo; el bloqueo de secretos, PII y datos prohibidos no se relaja nunca |
| Meses 7-9 | Revisión del modelo de amenazas de la primera función de IA en el producto; criterios de *eval* para salir a producción; documentación de proveedor; cláusula tipo para contratos | Una función de IA con documentación técnica, registro de eventos, supervisión humana y cláusula tipo lista para negociar con el cliente (la firma, no antes del cierre del mes 12) | Medio: agrega un gate antes de salir | Si tras dos ciclos del red team del piloto (el del [Anexo B](02-arquitectura.md), ver "Red teams: cuatro alcances") persisten hallazgos críticos, la función queda en autonomía nivel 0-1 ("sin IA" o "asiste") o se cancela |
| Meses 10-12 | Red team externo; extensión del alcance de ISO 27001 a IA; revisión de niveles de autonomía; informe anual al Directorio; decisión de certificación 42001 | Cero hallazgos críticos abiertos; brecha frente a 42001 documentada; decisión registrada | Bajo | Sin señal contractual ni producto liberado en la lectura del mes 9, el red team externo y la extensión ISO (la demostración externa) se difieren. Si ningún cliente exige 42001, no se certifica; si el costo de la auditoría supera el rango de Finanzas, se difiere |

**Cautelas del plan.** Seis puntos quedan abiertos y no se inventan:

1. La función legal es externa y su costo es un supuesto sin cotización.
2. El rol de Acme Labs frente a la Ley 25.326 (responsable o encargado del tratamiento)
   necesita asesoría.
3. Los textos ordenados del BCRA de tecnología (13/02/2026) y de PSP (02/10/2026) obligan a la
   entidad respecto de la IA y de sus terceros (ver la tabla del marco), pero no prueban que un
   cliente le exija controles de IA a Acme Labs; eso lo prueba, o no, la evidencia contractual
   (ver "Licencia para vender"). Los cambios posteriores a esas fechas se revisan antes de la entrega.
4. Legal externo debe confirmar alcance, versión vigente, rol y excepciones de BCRA, AI Act y Ley 25.326; esta lectura no valida ninguna de esas obligaciones.
5. La matriz de restricciones de clientes depende del área comercial y no existe todavía
   ([fuente](../../context/hechos/gobierno-y-politica-ia.md)).
6. Los residuales del registro y los umbrales de señal son propuestas del equipo: se
   confirman con las pruebas de los meses 4-6 y con la evidencia contractual de los meses 1-3.

### Licencia para vender: qué evidencia la sostiene y qué cuesta el gobierno mínimo

**Problema.** El deck dice que la base compra "licencia para venderles a bancos". Hoy eso
se apoya en un [supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md), no
en contratos. El BCRA obliga al banco a gestionar la IA de sus terceros y a formalizar esa
relación; eso no prueba que le exija controles a Acme Labs ni que le compre IA. Pedir controles tampoco es
pedir IA: son dos señales distintas.

**Tres paquetes, con los renglones de "Insumos para Finanzas".** El paquete se parte según
qué riesgo reduce cada uno. El gobierno mínimo rige siempre; los controles técnicos propios
dependen de la señal que lee la decisión del mes 3 (la plataforma de los meses 4-6); la
demostración externa, de la señal contractual o del producto en la lectura del mes 9.

| Paquete | Renglones | Caja (USD) | Tiempo (USD) | Total (USD) | Qué reduce | Qué no reduce |
|---|---|---|---|---|---|---|
| Gobierno mínimo | Líder, seguridad, Council, matriz e inventario, legal externo, ejercicios de mesa | 8.000-20.000 | 24.650-62.125 | 32.650-82.125 | Datos de cliente en un modelo externo, por matriz y *default-deny*; IA embebida sin aprobar; un gobierno que frena; declarar controles que no existen; aplicación de la política aprobada | La inyección indirecta de prompts y la fuga de secretos quedan solo en política: no hay bloqueo, log ni prueba que mostrarle a un cliente |
| Controles técnicos propios | Pasarela con DLP y logs, pruebas de *bypass*, red team interno | 4.500-18.000 | 1.875-9.375 | 6.375-27.375 | Datos de cliente en un modelo externo y fuga de secretos, con bloqueo y registro; inyección indirecta probada; la evidencia del ejemplo del secreto en un prompt | Las superficies sin ruta por la pasarela (residual aceptado) |
| Demostración externa | Red team externo; extensión de la ISO 27001 a IA | 11.600-31.000 | — | 11.600-31.000 | Declarar controles que no existen, con evidencia de un tercero; la condición del cierre del mes 12 (red team externo sin críticos) | Ningún riesgo propio que los controles técnicos no cubran: vale si un cliente la pide o si el producto sigue |
| **Paquete completo (rama con señal en el mes 3)** | | **24.100-69.000** | **26.525-71.500** | **50.625-140.500** | | |

**Recomendación para la referencia anual (no es el pedido de hoy).** El pedido vigente
es el mínimo M1-M3 del [Anexo E](05-business-case.md). Para el año, el gobierno mínimo
se financia siempre. Los controles técnicos y la demostración externa se liberan por señal,
según la regla vigente del [Anexo E](05-business-case.md):
la decisión del mes 3 libera la plataforma (y con ella los controles técnicos) si hay al
menos una señal; una prohibición pura se cumple excluyendo el uso, como se aclara abajo.
La demostración externa se decide en la lectura del mes 9. Sin señal, el
año corre como la alternativa de gobierno mínimo y formación del Anexo E y cuesta lo que el gobierno mínimo: 32.650-82.125 USD,
más hasta 1.875-9.375 USD de tiempo de los controles compensatorios (ver "Controles según la
decisión del mes 3"; el Anexo E los suma a esa rama, que en todo el plan da ≈ 199k USD en el año). Ahorra
la caja de los controles técnicos (4.500-18.000 USD) y la de la demostración externa
(11.600-31.000 USD). **Desacuerdo a la vista:** una
alternativa financia los controles técnicos por riesgo propio, porque los riesgos de datos de
cliente en un modelo externo y de fuga de secretos exponen a Acme Labs aunque no venda
IA, y eso es cierto. En la rama sin plataforma ese riesgo no se mitiga con
pasarela: se acepta como residual con controles compensatorios. Quien quiera los controles
técnicos sin señal tiene que pedir una excepción al board, con su caja. Las cuatro
condiciones propuestas más abajo requieren ratificación del Council o del Directorio; no se dan por aprobadas.

**Qué evidencia se pide (meses 1-3).** No se inventan clientes ni cláusulas: se leen los
documentos que ya existen, con la misma lectura que arma la matriz.

| Fuente | Qué se busca | Rol que la junta |
|---|---|---|
| Contratos vigentes de los cinco primeros clientes (más del 90% de la facturación, [fuente](../../context/hechos/cartera-y-concentracion.md)) | Cláusulas de subcontratación, confidencialidad y secreto, tratamiento y transferencia de datos, herramientas o IA | Operaciones con el área comercial |
| Cuestionarios de evaluación de proveedores recibidos en los últimos 24 meses | Preguntas sobre IA: inventario, no entrenamiento, ubicación de datos, logs, certificaciones, y si la respuesta condiciona algo | Responsable de seguridad |
| RFP, pliegos y pedidos de renovación de los últimos 24 meses | Requisitos de IA como condición o como puntaje | Área comercial |
| Informes de auditoría de clientes sobre Acme Labs | Observaciones sobre IA o terceros | Responsable de seguridad |

**Cómo se registra.** Una fila por documento, **solo en un registro interno de acceso restringido**: alias del cliente
(los de la fuente de cartera, sin segmento), tipo de documento, fecha, texto del requisito, clasificación
(prohíbe, condiciona, pide evidencia de controles, pide IA, silencio), si es condición o
pregunta, y horizonte (vigente o renovación con fecha). Fuera de ese registro sale solo el
agregado, sin alias ni textos, como agregado anonimizado que valida una persona designada.

**Umbral que la convierte en señal** (propuesta,
[supuesto](../../context/supuestos/umbral-de-evidencia-contractual.md)). La señal
contractual es una de las tres que puede liberar la plataforma en el mes 3; se lee al fin de
los meses 1-3 y se vuelve a leer en los meses 6 y 9.

| Señal | Umbral | Cuenta en el mes 3 | Qué decide |
|---|---|---|---|
| Restricción | Al menos un contrato de los cinco primeros prohíbe o condiciona la IA de terceros | Sí: prohibición y condicionamiento cuentan como restricción, igual que en la fuente del umbral. Registrar cuál de las dos aplica | La prohibición pura se cumple excluyendo el uso afectado; no libera plataforma. Si condiciona, documentar los controles exigidos y evaluar la respuesta |
| Licencia para vender | Uno de los dos primeros clientes, o dos de los cinco primeros, piden evidencia de controles de IA como condición o puntaje de contratación o renovación dentro de 18 meses. Las preguntas sin consecuencia no cuentan | Sí | Bajo la regla vigente, habilita liberar los controles técnicos en el mes 3, solos o con otra señal; la demostración externa se decide en el mes 9. Ver propuesta de condiciones adicionales |
| Demanda | Un cliente pide una función de IA | No es esta señal: es la de cliente para el producto, que define el [Anexo F](06-roadmap-riesgo.md) | Libera el piloto de producto en el mes 6 |
| Sin señal | Ninguna de las anteriores | Sin señal contractual en el mes 3 | Meses 4-12 como la alternativa de gobierno mínimo y formación (ver "Controles según la decisión del mes 3"); los meses 6 y 9 releen |

**Una señal, respuestas distintas.** La definición de restricción incluye tanto el
condicionamiento como la prohibición, como la
[fuente del umbral](../../context/supuestos/umbral-de-evidencia-contractual.md). Contarla no
autoriza el uso prohibido ni justifica comprar plataforma. La exclusión del uso afectado
es la respuesta a una prohibición pura; el Council registra su cumplimiento.

**Regla vigente y condiciones adicionales propuestas.** El [Anexo E](05-business-case.md) y el
[Anexo F](06-roadmap-riesgo.md) liberan plataforma ante al menos una de las señales de
contrato, precio por consumo o cliente. La redacción "restricción o licencia" tiene que
alinearse con la exclusión de la prohibición pura. Los umbrales contractuales siguen siendo supuestos
sin ratificar; este anexo no presupone una decisión nueva del board.

**Cuatro condiciones adicionales propuestas, pendientes de ratificación por el
Council o el Directorio.** Ante una señal, se recomienda evaluar la respuesta mínima y exigir:

1. **Brecha documentada:** requisito y superficie afectados, control actual probado y
   residual; explicar qué falta y por qué excluir el uso o configurar lo existente no alcanza.
2. **Alternativas comparables:** configuración actual, compra y ensamblado, con igual
   requisito, superficie, pruebas, cobertura y costo total de operación e integración.
3. **Economía incremental o aprendizaje con pérdida aceptada:** comparar costos futuros
   evitables desde el mismo historial; declarar límite de pérdida, evidencia buscada y
   condición de corte si se elige aprender. Una señal contractual no demuestra repago.
4. **Capacidad demostrada:** horas por rol liberadas, operación y mantenimiento asignables,
   dependencia comercial validada y controles aplicables probados antes de ampliar.

El Council recomienda con evidencia; una persona designada por el Directorio firma la
decisión del gate y el presupuesto, con nombre y alcance de autoridad en el acta
**a designar**. No decide un sistema de IA ni un indicador automático. Estas cuatro
condiciones no sustituyen la regla vigente hasta su ratificación. Si se ratifican y falta
brecha incremental, se difiere plataforma y se reevalúa en los meses 6 y 9; no se la pasa por defecto
al año 2. Un control obligatorio incumplido suspende el uso afectado.

**Cómo se lee en el mes 3.** La evidencia de los meses 1-3 son los mismos contratos de la
matriz, que ya es condición de la decisión del mes 3; los cuestionarios, RFP y auditorías
pueden llegar después.

- **Quién produce:** los roles de la tabla de fuentes; seguridad consolida el agregado
  (cuántos de los cinco primeros, qué clasificación, sin alias ni textos). **Quién verifica:**
  una persona del equipo distinta del productor, con Legal externo para los textos ambiguos.
  **Quién declara la señal:** el Council sobre esa verificación. **Quién firma el gate:**
  la persona designada por el Directorio, con autoridad y límites asentados. Las tres
  personas (productor, verificador y autoridad del gate) están a designar.
- **Cuándo:** el agregado llega al Council al menos dos semanas antes de la decisión del mes 3
  (propuesta, a fijar antes de la segunda liberación). El agregado anonimizado lo valida una persona
  designada antes; hasta entonces es supuesto y no sustenta la decisión.
- **Qué cuenta:** solo el documento leído y clasificado. El ambiguo o no leído no cuenta;
  si por eso no se llega al umbral, el resultado es "sin señal por lectura incompleta" y no
  "señal no probada", se completa en los meses 4-6 (como dice el Anexo E) y se relee en la
  lectura del mes 6.
- **Meses 6 y 9:** misma tabla, sobre lo nuevo desde la decisión anterior (renovaciones, RFP,
  cuestionarios) y la lectura que faltaba. Una señal que aparece en el mes 6 libera los
  controles técnicos desde los meses 7-9; una que aparece en el mes 9, desde los meses 10-12
  (ver "Controles según la decisión del mes 3"). La prohibición pura sigue excluyendo el
  uso; las cuatro condiciones adicionales solo rigen si fueron ratificadas.

La lectura cabe en las horas de la matriz porque son los mismos contratos. Si no
alcanza, el faltante es de 20-40 h de analista funcional (250-1.375 USD: 12,5-34,375 USD/h,
el costo mensual del supuesto dividido 160), que no está sumado al total.

### Controles según la decisión del mes 3: qué rige siempre y qué depende de la plataforma

Cada control dice si rige desde la decisión del mes 3 en las dos ramas o solo si esa
decisión libera la plataforma. La velocidad que cuesta es la de "Controles por tramo"; los
compensatorios son tiempo, sin caja.

**Requisito previo por superficie (propuesta del equipo).** Antes de ejecutar una prueba
o ampliar un uso, completar y probar el registro requisito→superficie→control→evidencia→residual.
Debe declarar fuentes y repositorios habilitados por política y matriz, datos propios o
sintéticos permitidos, permisos y MCP acotados, ausencia de credenciales productivas,
escaneo local aplicable, prueba adversarial y revisión humana del resultado.

| Superficie que se propone usar | Prueba previa y evidencia mínima | Límite si no puede bloquearse |
|---|---|---|
| Agente de código en terminal | Lista de repositorios y fuentes habilitados; permisos y MCP efectivos; secreto sintético bloqueado y alertado por el escaneo local; intento de instrucción indirecta y acción no autorizada; revisión humana de cambios antes de ejecutar | No se declara bloqueo fuera de las rutas probadas; una falla del control obligatorio impide iniciar o ampliar ese uso |
| IDE | Repositorios habilitados y configuración corporativa; escaneo local antes de enviar contexto o aceptar cambios; prueba con secreto e instrucción sintéticos; revisión humana del código | Si no se puede impedir el envío automático de contexto excluido, deshabilitar esa función o excluir el repositorio; el residual restante requiere aceptación |
| Chat y escritorio | Fuentes y conectores permitidos, ajustes corporativos y retención; escaneo local de archivos a adjuntar; prueba adversarial sintética de exfiltración y revisión humana previa al envío y al uso del resultado | No atribuir DLP central ni bloqueo técnico al control manual; excluir contenido no autorizado |
| Suite ofimática | Permisos efectivos de documentos y conectores; revisión de funciones embebidas; escaneo local de archivos que se incorporan; prueba sintética de acceso indebido e instrucción indirecta; revisión humana | Si no se puede acotar el contexto a fuentes permitidas, no habilitar esa función sobre el conjunto afectado |
| MCP y conectores | Lista cerrada de servidores y acciones, permisos mínimos probados y sin credenciales productivas; prueba de lectura y acción no autorizadas con fuentes sintéticas; revisión humana de acciones | Deshabilitar el servidor o la acción que no pueda acotarse; probar también la superficie desde la que se invoca |

Ingeniería produce la evidencia por superficie; un verificador distinto la revisa. El dueño
del riesgo o el Council acepta el residual según su autoridad, con vencimiento; las personas
están a designar. Gasto dentro del techo o buena adopción no reemplazan esta
aceptación. Seguridad puede suspender el uso afectado según "Derechos de decisión".

**Calendario del mínimo propuesto.** Para los usos del paquete mínimo, las pruebas por
superficie se ejecutan en M1-M3 antes de habilitar, con las horas del Anexo E; el resto de las
tablas sigue en M4-M6. La ejecución queda **condicionada a validar horas, costo y capacidad**
del "Insumo para el paquete mínimo M1-M3", consolidado en el [Anexo E](05-business-case.md).
No se declaran controles instalados. Sin esa validación, prueba y aceptación, el uso
afectado no se inicia ni se amplía. El residual de usos existentes también debe revisarse:
no hay aceptación automática por ser una herramienta ya aprobada.

| Control | Rige en las dos ramas | Solo con señal en el mes 3 |
|---|---|---|
| Política aprobada con documentación revisada y aplicación registrada, intake en 3 niveles, inventario, plan de incidentes, ejercicios de mesa | Sí (gobierno mínimo) | — |
| Matriz de clientes con *default-deny* (riesgo de datos de cliente en un modelo externo) y topes de la escala de autonomía | Sí (gobierno mínimo) | — |
| *Hooks* de permisos, escaneo de secretos en el equipo y el repositorio y lista cerrada de MCP por configuración, en el agente de código | Sí, **compensatorio**: probados con un secreto sintético antes de extender la prueba a la cohorte | — |
| Red team interno acotado al agente de código, con repositorios y tickets sintéticos | Sí, compensatorio (riesgo de inyección indirecta de prompts) | — |
| Pasarela con allowlist, DLP y logs; cobertura ≥90% (suscripción que permite gateway o pago por consumo) y 100% de casos propios | No | Sí (meses 4-6) |
| Prueba de *bypass* por superficie, y red team de la pasarela | Solo para el agente de código | Todas las superficies |
| Piloto de producto en autonomía niveles 1-2, modelo de amenazas del producto, *evals* y cláusula tipo | No | Solo con señal de cliente en el mes 6 |
| Red team externo y extensión de la ISO 27001 (la demostración externa) | No | Señal contractual o producto en el mes 9 (meses 10-12) |

**Qué control es exigible y cuál es opción.** Criterio propuesto: un control es
**exigible** cuando este anexo lo motiva con una restricción contractual, un riesgo del
registro o una necesidad de evidencia, y rige en las dos ramas; es **opción** cuando se
libera solo por una señal. Ningún control es exigible hoy por una norma verificada: lo
confirma Legal externo (cautela 4), y el motivo contractual depende de la matriz, que
todavía no existe. La clasificación la preparó Gobierno a partir de las tablas de este
anexo; no agrega controles ni cifras y la confirma o corrige su responsable humano.

| Control | Motivo | Exigible u opción | Alternativa de menor costo |
|---|---|---|---|
| Política aprobada: revisión documental y aplicación | Evidencia: la aprobación informada no acredita controles; riesgo de declarar controles que no existen | Exigible | Revisar la versión aprobada en vez de redactar otra; 0 USD adicionales |
| Intake en 3 niveles | Riesgos de un gobierno que frena y de IA embebida sin aprobar | Exigible | Autoservicio en riesgo bajo; el SLA del nivel 2 se puede relajar |
| Matriz por cliente con *default-deny* | Contrato (cláusulas de los cinco primeros clientes, por leer) y riesgo de datos de cliente en un modelo externo | Exigible | Leer solo los contratos de la matriz; lo ambiguo, a *default-deny* |
| Inventario con IA embebida | Riesgo de IA embebida sin aprobar | Exigible | Reutilizar registros y consolas; 0 USD |
| Revisión legal focalizada | Evidencia: alcance normativo sin confirmar y textos ambiguos de la matriz | Exigible | Dictamen de 8-16 h en vez de la revisión normativa completa |
| Council liviano | Derecho de decisión para aceptar el residual | Exigible | Dentro del comité de tecnología, sin reunión adicional |
| Plan de incidentes y ejercicios de mesa | Riesgos de fuga de secretos (ruta de primera exposición) y de capacidad concentrada (el suplente corre el runbook) | Exigible | Candidata, no adoptada: montar la ruta de IA sobre el circuito de reporte de incidentes del antecedente de abril (vigencia por contrastar) y acotar los ejercicios de mesa. Su efecto en horas y costo no está estimado; si se acota a un solo ejercicio, el suplente se prueba una sola vez |
| Topes de la escala de autonomía | Riesgo de agencia excesiva | Exigible | Hasta el nivel 3 con revisión humana; el nivel 4, solo en *sandbox* |
| *Hooks*, escaneo local de secretos y MCP cerrados en el agente de código | Riesgos de fuga de secretos y de datos de cliente sin pasarela | Exigible, compensatorio | Ya es la alternativa barata a la pasarela: tiempo, sin caja |
| Red team interno acotado al agente de código | Riesgo de inyección indirecta de prompts | Exigible, compensatorio | Repositorios y tickets sintéticos |
| Prueba previa por superficie con verificador independiente | Evidencia: sin independencia no se declara probado | Exigible antes de habilitar cada uso | Excluir la superficie o la función que no se pueda probar |
| Pasarela con allowlist, DLP y logs; *bypass* en todas las superficies | Riesgos de datos de cliente y de fuga de secretos, con bloqueo central | Opción: señal en el mes 3 | Compensatorios con residual aceptado. Desacuerdo a la vista: financiarla por riesgo propio (ver "Licencia para vender") |
| Piloto de producto, modelo de amenazas, *evals* y cláusula tipo | Señal de cliente | Opción: lectura del mes 6 | No hacerlo; el producto se difiere |
| Red team externo y extensión de la ISO 27001 | Evidencia de un tercero | Opción: lectura del mes 9 | Diferir; el red team interno queda como evidencia propia |
| Certificación ISO 42001 | Solo si un cliente la exige | Opción: cierre del mes 12 | Brecha documentada, sin certificar |

**Calendario sin señal.** Meses 4-6: gobierno mínimo y compensatorios. La lectura del mes 6
relee las señales: si hay una, los controles técnicos corren en los meses 7-9 y la cobertura
se mide en la lectura del mes 9; el red team externo, en los meses 10-12 solo si los
controles técnicos cerraron. Si la señal llega en el mes 9, los controles técnicos corren
en los meses 10-12 y la demostración externa queda para el año siguiente. Es consecuencia
de la secuencia del [Anexo B](02-arquitectura.md), no un costo medido.

**Condiciones de las lecturas de los meses 6 y 9 sin señal** (propuesta para el
Anexo F): matriz al 100% de los clientes principales; compensatorios probados y críticos del
red team cerrados; residual de los riesgos de datos de cliente en un modelo externo, de
inyección indirecta y de fuga de secretos aceptado por el Council con fecha de revisión;
lectura de la señal contractual hecha. No se piden cobertura por pasarela ni bypass de todas
las superficies.

**Riesgo residual sin pasarela.** Sin los controles técnicos centrales, la inyección
indirecta y la fuga de secretos no tienen bloqueo ni registro centrales. El gobierno mínimo
solo no alcanza: la rama operativa sin señal exige los compensatorios probados de la
tabla, porque la rama sin señal no agrega superficie: no hay casos propios ni agentes nuevos,
y la prueba extendida corre sobre los repositorios que la matriz habilita, sin datos de
cliente. Propuesta: aceptar el residual solo después de esas pruebas. Hoy hay 40-45 seats
de Claude y no hay evidencia de controles específicos de IA.

| Riesgo | Residual objetivo sin controles técnicos | Acepta | Vence |
|---|---|---|---|
| Datos de cliente en un modelo externo | Media / Alto (sin allowlist en la pasarela) | Council, con informe al CEO | Meses 6 y 9 |
| Inyección indirecta de prompts | Media / Alto (sin logs centrales) | Council, con informe al CEO | Meses 6 y 9 |
| Fuga de secretos | Baja / Medio-alto en el agente de código (bloqueo local); Media / Medio-alto en el resto | Council | Meses 6 y 9 |

La aceptación vale **solo si** se cumple el requisito previo por superficie: fuentes y
repositorios habilitados por política y matriz, datos propios o sintéticos permitidos,
permisos y MCP acotados, autonomía hasta el nivel 3 ("actúa con aprobación") con revisión
humana, sin credenciales productivas, escaneo local y prueba adversarial con compensatorios
probados y residual aceptado por la autoridad correspondiente. Si falta una condición, la
prueba no se inicia ni se extiende. Un incidente confirmado de datos de cliente en un
modelo externo, de inyección
indirecta o de fuga de secretos la revoca: se suspende la extensión y el Council le pide al
board reabrir los controles técnicos como decisión de seguridad, fuera de las tres señales
(propuesta). El responsable de la aceptación está a designar.

**Alternativas.** (i) Financiar los controles técnicos sin señal: 4.500-18.000 USD de caja,
como excepción a la regla vigente. (ii) No extender la prueba a la cohorte: reduce el riesgo,
pero deja a la alternativa de gobierno mínimo y formación sin su medición. (iii) Aceptar solo con la política: descartada,
es lo que hoy deja sin prueba.
**Costo de la rama anual:** los compensatorios suman hasta 1.875-9.375 USD de tiempo
(la parte de tiempo de los controles técnicos), que el Anexo E suma a la rama sin señal
de **≈ 199k USD**, no a la alternativa de **161k USD** de "Alternativas equivalentes". El
pedido mínimo M1-M3 se vuelve a costear aparte; no hereda esos totales. Sin el escaneo local de
secretos probado, la fuga de secretos
no tiene bloqueo en ninguna superficie. **Éxito:** secreto sintético bloqueado y alertado
en el agente; críticos del red team cerrados. **Abandono:** incidente confirmado o
condición incumplida.

### Tensiones con otras áreas

- **Con Arquitectura:** la pasarela de salida y la lista de servidores MCP condicionan el
  diseño de la plataforma. Alternativa: Gobierno define el requisito (allowlist, registro,
  sin entrenamiento) y Arquitectura elige la herramienta; el costo de los meses 4-6 es un
  rango hasta que lo confirme.
- **Con Arquitectura (ruteo del agente de código):** la política del Anexo B rige: se enruta
  solo si el régimen comercial lo permite, y el 90% rige en los regímenes de suscripción que
  permite gateway y de pago por consumo; el Anexo F la adopta.
- **Con Finanzas (bifurcación):** los controles técnicos dependen de la señal del mes 3 y no
  se financian "por riesgo propio"; el residual de los riesgos de datos de cliente en un
  modelo externo, de inyección indirecta y de fuga de secretos sin pasarela lo asume el
  Council (ver "Controles según la decisión del mes 3").
- **Con Finanzas:** alrededor de la mitad (51%-52%) del costo de este anexo es tiempo reasignado, no caja, pero el
  tiempo compite con horas facturables (utilización ~83%). Finanzas decide si lo trata
  como costo de oportunidad o lo ignora.
- **Con Personas:** la alfabetización en IA es un control débil por sí solo (el piloto
  mostró 17% de cursos completos); se propone medirla por conducta (uso de la pasarela,
  revisión de output) y no por cursos terminados.
- **Con Personas (medición del uso):** qué se mide del uso de las personas y cuánto se
  retiene no tiene una A en este anexo. El [Anexo D](04-personas-cultura.md) pone al CAIO
  como A de las métricas de adopción y deja alcance y retención de la telemetría a Gobierno
  con Talento. Elegir la A, y si la medición pide revisión laboral y de datos de empleados,
  queda pendiente de decisión entre los responsables humanos de C y D.
- **Con el Anexo F (calificación de riesgos):** el riesgo de datos de cliente en un modelo
  externo es Media / Alto inherente acá y Media / Muy alto en el
  [Anexo F](06-roadmap-riesgo.md), que no rotula si sus valores son inherentes o
  residuales; las superficies sin control técnico central (Alta / Alto en F) no son una fila
  de este registro. Si F los usa como residuales, el gate choca con "Alta con impacto Alto o
  mayor: nadie lo acepta". La conciliación queda pendiente entre los responsables humanos
  de C y F, sin elegir valores por consenso.
- **Con CAIO:** si el board prioriza velocidad, se puede relajar el SLA del Nivel 2, pero
  no la matriz de clientes ni la prohibición de crédito.

## Insumos para Finanzas

### Insumo para el paquete mínimo M1-M3: controles aplicables equivalentes

**Propuesta de alcance, no presupuesto aprobado.** Para operar sobre herramientas
corporativas existentes sin plataforma central, se mantienen los mismos requisitos de
datos, permisos, prueba, revisión y aceptación; cambia la implementación y se excluyen
superficies que no puedan cumplirlos. No se promete cobertura de pasarela ni producto nuevo.

Los rangos siguientes son **supuestos de planificación**, sin medición
ni cotización. Suponen reutilizar política, consolas, escáner local y contratos existentes;
una cohorte acotada a repositorios propios o sintéticos, sin datos de cliente, y una primera
prueba con corrección y repetición. No presuponen disponibilidad de agendas ni controles
ya funcionando. Si hace falta compra, integración nueva o más ciclos, reducir alcance o
volver a costear antes de iniciar. El responsable de cada rol está a designar.

| Control mínimo | Entregable verificable | Horas por rol en M1-M3 (supuesto) | Pago externo incremental (supuesto) |
|---|---|---|---|
| Política e intake | Versión, alcance y aprobación documentada revisados; aplicación de la política aprobada, datos permitidos/prohibidos, revisión humana y ruta de incidentes y suspensión; cambios propuestos sujetos a decisión empresarial | Tech lead de gobierno: 8-16 h; seguridad: 4-8 h; staff de Operaciones/comercial: 2-4 h | 0 USD adicionales; revisión legal en su fila |
| Matriz habilitante | Restricciones de los clientes principales clasificadas, fuentes/repositorios habilitados y excluidos, ambigüedades con *default-deny*; agregado verificado por otra persona | Analista funcional: 32-48 h; seguridad: 4-8 h; staff de Operaciones/comercial: 4-8 h | 0 USD adicionales; revisión legal en su fila |
| Inventario y riesgo | Herramientas, funciones embebidas, repositorios, MCP, permisos, superficie→control→telemetría, responsables por rol y registro de residuales con vencimiento | Analista funcional: 16-24 h; senior DevOps: 4-8 h | 0 USD; se reutilizan registros y consolas disponibles |
| Revisión legal focalizada | Dictamen de alcance y textos ambiguos, límites de uso/no entrenamiento y tratamiento de datos; no reemplaza la revisión normativa completa posterior | Tech lead de gobierno: 2-4 h; analista funcional: 4-8 h; asesor externo: 8-16 h | 2.000-6.000 USD; supuesto de 250-375 USD/h × 8-16 h, sin cotización; sustituye la porción inicial del renglón anual, no se suma dos veces |
| Compensatorios y prueba previa por superficie habilitada | Configuración y escaneo local, permisos/MCP acotados, sin credenciales productivas; secreto e instrucción sintéticos, intentos de acceso/acción indebidos, corrección y repetición; verificación independiente, revisión humana y acta de aceptación o exclusión | Senior DevOps productor: 40-64 h; seguridad verificadora independiente: 8-16 h; analista funcional: 8-16 h para fuentes, casos de prueba y registro | 0 USD si las herramientas existentes alcanzan; no incluye compra ni red team externo |

**Decisión y seguimiento incluidos en el alcance.** Conservar la cadencia existente del
Council: por M1-M3, cinco asientos × 6 h por asiento, distribuidos en 12 h de tech lead,
6 h de senior DevOps/seguridad y 12 h de staff (supuesto ya usado en el renglón anual).
Incluye lectura, aceptación o rechazo del residual y revisión mensual; no es una reunión
adicional. Si esas horas no alcanzan, Finanzas debe volver a costearlas antes de comprometerlas.

**Regla de costeo para Finanzas.** Las horas por entregable son partidas disjuntas: no
sumar además los porcentajes anuales de líder y seguridad sobre esas mismas actividades;
no duplicar matriz/inventario, Council, legal ni los compensatorios anuales. Productor y
verificador deben ser personas distintas aunque compartan banda de costo; si no hay
independencia disponible, no se declara probado el control. Los USD de tiempo salen del
[supuesto de costo cargado por rol](../../context/supuestos/costo-cargado-por-rol.md);
las licencias existentes y la capacitación las concilian Arquitectura y Personas.

**Seguridad: política fuera del aporte técnico de B.** Las 24-40 h técnicas del
[Anexo B](02-arquitectura.md) pueden reutilizarse para matriz y pruebas solo con confirmación
de alcance. Las 4-8 h de política de este anexo no están incluidas en B: se suman aparte,
más 6 h de Council; total provisional de Seguridad: 34-54 h. No se absorbe la política
en el aporte técnico ni se presume confirmado el solape de matriz y pruebas; Finanzas
debe conciliarlo y volver a costear el mínimo antes de comprometer horas.

**Tres diferencias con el [supuesto del paquete mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md), sin acuerdo.**
Ese supuesto está revisado como base de planificación y deja sus solapes «a validar por
sus dueños». Lo que sigue es la lectura de Gobierno; ningún responsable humano de B o
de C la confirmó todavía, y este anexo no cambia el supuesto.

| Punto | Supuesto del mínimo | Lectura de C | Diferencia | Quién lo resuelve |
|---|---|---|---|---|
| Tech lead de gobierno en M1-M3 | C 22-36 h | Las filas de C suman 22-32 h: política 8-16, legal 2-4 y Council 12; no hay otra fila de tech lead | 0-4 h, hasta 250 USD al costo alto; el techo de 59k USD y el acumulado de 79k USD no cambian | Responsable humano de C; después Finanzas corrige el supuesto y el Anexo E |
| Seguridad: matriz y verificación dentro de las 24-40 h de B | Dentro, con confirmación de alcance | Matriz, sí. Verificación, solo si B aclara que en los compensatorios seguridad verifica y no produce: si produce pruebas en B y las verifica en C, verifica su propio trabajo | Sin cambio de horas si B lo aclara | Responsables de B y C |
| DevOps: configuración de B y de C como una sola tarea | Unión 40-64 h; total 44-72 con inventario | B no declara compartida esa fila y el contenido difiere en parte (B suma exportaciones; C, pruebas sintéticas, corrección y repetición) | Sin unión, 76-128 h: +32-56 h, +600-2.625 USD | Responsable de B, desagregando su fila |

Hasta que se resuelvan, la unión de DevOps sigue como supuesto y no como ahorro: si no
se confirma, Finanzas recostea el tramo antes de comprometerlo.

**Criterio de éxito:** cada superficie habilitada tiene prueba reproducible, hallazgos
críticos cerrados y residual firmado por su autoridad antes de operar. **Abandono:** control
obligatorio incumplido, incidente, falta de verificador o capacidad no liberada: suspender
el uso afectado, reducir alcance y volver a costear. La ejecución de estos entregables en M1-M3
queda condicionada a validar horas, costo y capacidad; el resto de las tablas conserva
su calendario.

### Referencia anual, pendiente de conciliación con el pedido mínimo

Todas las cifras son rangos en USD, supuestos sin cotización, salvo donde se
cita una fuente. Cada costo de tiempo se calcula por actividad y por rol con el supuesto de
costo cargado, ya ampliado; los rangos son amplios a propósito. "Tiempo" es costo de oportunidad (reasignación), "caja" es gasto externo.

| Concepto | Tramo | Tipo | Rango (USD) | Fuente o supuesto |
|---|---|---|---|---|
| Líder de gobierno y riesgo: 25% de un tech lead durante 12 meses | Meses 1-12 | Tiempo | 13.500-30.000 | 4.500-10.000 por mes ([supuesto](../../context/supuestos/costo-cargado-por-rol.md)) × 25% × 12 |
| Ingeniería de seguridad: 20% de un senior DevOps o seguridad | Meses 1-12 | Tiempo | 7.200-18.000 | 3.000-7.500 por mes × 20% × 12 |
| AI Council: 5 personas × 2 h por mes × 12 (la revisión mensual del Council; sin costo adicional por el tablero) | Meses 1-12 | Tiempo | 2.250-5.625 | 24 h de sesión × 5 asientos: 2 a costo de tech lead, 1 de senior DevOps y 2 de staff (9-63 USD/h según el rol), supuesto: 24 × (2 × 28,125 + 18,75 + 2 × 9,375) a 24 × (2 × 62,5 + 46,875 + 2 × 31,25). Equivale a 5 asientos × 6 h por tramo de tres meses |
| Matriz de restricciones por cliente e inventario v1 | Meses 1-3 | Tiempo | 1.250-5.500 | 100-160 h de analista funcional (13-34 USD/h), supuesto |
| Asesoría legal externa (BCRA, Ley 25.326, cláusulas tipo) | Meses 1-6 | Caja | 8.000-20.000 | Supuesto, sin cotización |
| Pasarela de salida, DLP y logs de acciones | Meses 4-12 | Caja | 4.500-18.000 | 500-2.000 por mes × 9, supuesto; lo confirma Arquitectura |
| Prueba de integración y de *bypass* por herramienta, y migración de la configuración de la pasarela (60-120 h) | Meses 4-6 | Tiempo | 1.125-5.625 | 60-120 h de senior DevOps o seguridad (19-47 USD/h), supuesto; lo confirma Arquitectura |
| Red team interno (40-80 h) | Meses 4-6 | Tiempo | 750-3.750 | 40-80 h de senior DevOps o seguridad (19-47 USD/h) |
| Red team externo | Meses 10-12 | Caja | 10.000-25.000 | Supuesto, sin cotización |
| Extensión del alcance de ISO 27001 a IA (2-4 jornadas de auditoría) | Meses 10-12 | Caja | 1.600-6.000 | 800-1.500 por jornada, supuesto; depende del calendario de la auditoría externa prevista para 2027 |
| Ejercicios de mesa de incidentes (2 × 8 personas × 3 h) | Meses 4-6 y 10-12 | Tiempo | 450-3.000 | 48 h entre el costo de staff y de tech lead (9-63 USD/h) |
| **Total** | Meses 1-12 | | **50.625-140.500** | Caja: 24.100-69.000; tiempo: 26.525-71.500 |

No incluye licencias de las herramientas de IA ni capacitación (las cubren Arquitectura y
Personas), ni una certificación ISO 42001 (decisión de los meses 10-12). Finanzas debe contrastar el
total con la franja del 1%-3% de la facturación del [supuesto](../../context/supuestos/capacidad-de-inversion.md).

**Cómo lo usa el [Anexo E](05-business-case.md).** Los renglones coinciden con su cuadro
de inversión, en k USD (legal 8k-20k, pasarela 4,5k-18k, red team externo e ISO 11,6k-31k,
tiempo 27k-72k redondeado). Tres lecturas de gobierno sobre esas cifras:

- **Techo de los meses 1-3.** Legal aparece en tres autorizaciones distintas. La preparación
  de 2026 no lleva caja: prepara el alcance y pide cotización. M1-M3 lleva el legal focalizado,
  2.000-6.000 USD de caja (8-16 h × 250-375 USD/h, fila «Revisión legal focalizada» del
  insumo del paquete mínimo). El renglón anual de 8.000-20.000 USD es la referencia del
  paquete completo, que no se autoriza hoy, y el focalizado sustituye su porción inicial sin
  sumarse dos veces. Además, los meses 1-3 llevan el tiempo del líder, de seguridad, del
  Council y de la matriz.
- **Base mínima tras un corte (paquete completo, alternativa; no se traslada al mínimo).**
  Es el núcleo de gobierno de la referencia anual: 25% del líder, 20% de seguridad y el
  Council, que suman ≈ 5.740-13.410 USD por tramo de tres meses (un cuarto de los renglones
  anuales: 5.737,5-13.406,25). Tres tramos dan ≈ 17.200-40.200 USD, que es el "hasta 40k USD"
  de tiempo que el Anexo E usa, en la tabla de cortes del paquete completo, para un corte en
  la decisión del mes 3. La pasarela se suma solo si ya está instalada ([base mínima](../../context/supuestos/base-minima-tras-un-corte.md)).
  El pedido vigente es el paquete mínimo, con otro núcleo: después del mes 3, 108 h
  (36 por tramo: 12 de tech lead, 12 de seguridad y 12 de staff), caja 0 y tiempo hasta 6k
  USD, con aprobación explícita en el gate de salida ([Anexo E](05-business-case.md),
  "Segunda autorización: inicio M1-M3 y reservas de salida"). Son núcleos de alcances
  distintos: se usa uno u otro según el alcance, nunca la suma.
- **Controles técnicos y demostración externa, condicionales** (ver "Licencia para vender" y
  "Controles según la decisión del mes 3"). Los renglones de los controles técnicos (pasarela,
  4.500-18.000 USD de caja) y de la demostración externa (11.600-31.000 USD) no se gastan sin señal; el
  Anexo E ya condiciona la demostración externa a la lectura del mes 9 y los controles técnicos
  a la decisión del mes 3.

## Insumos para el deck

- **Mensaje de la slide:** "Gobierno que habilita": un Council de 5 asientos dentro del
  comité de tecnología, intake en 3 niveles con respuesta en 5 días hábiles para el riesgo
  medio, y control técnico de la salida de datos donde la superficie lo admite; en el resto,
  política y control compensatorio con residual aceptado por el Council, no una garantía
  de bloqueo.
- **Revisión mensual:** el Council mira el riesgo cada mes (2 h, con tablero) y puede frenar,
  cortar o escalar; no libera fondos. Las dos autorizaciones iniciales y las decisiones
  de los meses 3, 6, 9 y 12 corresponden al Directorio o autoridad formalmente delegada.
  La revisión mensual no suma costo.
- **Slide «Gobierno y seguridad» (propuesta para el deck):** este anexo exige la prueba antes
  de habilitar o ampliar un uso, y la revisión del residual de los usos existentes; no
  dispone detener el uso actual de las herramientas aprobadas, salvo la suspensión
  preventiva de Seguridad. Un título como «Ningún uso nuevo
  o ampliado sin probar antes sus controles» lo dice sin sobreprometer. Sin plataforma
  hay bloqueo local en el agente de código, no en una pasarela.
- **Pedido al board 1:** aplicar la política de IA cuya aprobación informó el responsable
  del caso el 20/10/2026, revisando versión, alcance y aprobación documentada. Los cambios
  propuestos requieren decisión empresarial; no se solicita aprobar la política de nuevo.
- **Pedido al board 2:** aprobar el alcance explícito (sin decisiones de crédito ni
  scoring en 12 meses) y los topes de la escala de autonomía del plan (niveles 0 a 4).
- **Pedido al board 3:** pedido vigente de controles: insumo M1-M3 de este anexo,
  consolidado en el [Anexo E](05-business-case.md), sección "Pedido inicial: paquete mínimo".
  La validación inicial se autoriza primero; M1-M3 requiere el segundo pase y conserva
  las condiciones de habilitación por superficie de este anexo.
  Los tres paquetes y montos anuales del paquete completo son referencia de otro alcance; no se
  autorizan hoy ni se trasladan a la continuación del mínimo.
- **Mensaje sobre la licencia para vender:** hoy es un supuesto; los meses 1-3 juntan la
  evidencia, la decisión del mes 3 la lee para liberar la plataforma y la lectura del mes 9
  decide si se paga el paquete que la demuestra.
- **Mensaje honesto:** la política tiene aprobación informada, sin documentación de
  aprobación revisada ni controles probados. Inventario, riesgos y matriz siguen sin
  evidencia actualizada; la operación del Council no está acreditada. Un producto propio no está certificado.
  Decir "certificados" donde no lo estamos es el riesgo de declarar controles que no existen.
