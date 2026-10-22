---
owner: architect
status: ready
title: "Anexo B — Arquitectura y roadmap técnico"
---

# Anexo B — Arquitectura y roadmap técnico

::: {.annex-summary}

## Síntesis ejecutiva

**Recomendación:** configurar y medir las herramientas existentes antes de
decidir si hace falta una plataforma. El harness interno de desarrollo existe;
su cobertura y sus controles siguen sin verificar.
Quick win candidato, no aprobado ni observado: corrección real y regresión tras
formación y controles ([caso propuesto](#candidato-de-quick-win-operativo)).

| Recorrido | Qué se hace ahora | Qué queda condicionado |
|---|---|---|
| Código y datos propios → herramientas → modelos | Configurar terminal, chat, IDE y suite; probar permisos, exclusiones, secretos y conexiones aprobadas | Cada superficie se habilita con controles probados y riesgo residual aceptado |
| Acciones del agente → revisión humana | Acotar autonomía y revisar antes de efectos irreversibles | No se promete solo lectura para el agente de código |
| Consolas y registros operativos → extractos agregados → indicadores | Leer uso, cambios de código, calidad y reversiones; congelar la base y reproducir la medición | Guardar extractos exige autorización de Seguridad sobre ubicación, acceso y retención |
| Casos nuevos → harness central → pasarela de modelos | Solo dirección de diseño: contexto acotado, memoria versionada, aislamiento y trazas | Plataforma con decisión y costeo propios; producto requiere además señal de cliente y otra autorización |

**Límites de datos y permisos.** El mínimo usa repositorios propios habilitados.
Datos/código de clientes quedan fuera; la excepción exige entorno del cliente y
permiso escrito. Datos Restringidos nunca van a IA externa. La medición usa
agregados por área y semana, sin eventos individuales, prompts ni secretos.

**Cómo se decide y se corta.** Primero, medición viable y reproducible por otro
operador; sin datos, capacidad o controles, reducir/diferir y recostear.
M6 decide continuidad por adopción, calidad, costo y controles: **no lee valor**.
M9 acredita valor solo con **peor caso mayor que cero y sin daño de calidad**.
Sin distinción, beneficio acreditado cero y sin expansión por valor; daño activa
el corte ([gate completo](#gate-de-valor-fijado-por-este-anexo-el-anexo-f-lo-adopta)).

**Responsable y alternativas.** Responsable de Tecnología; configurar, comprar
o ensamblar se comparan con cobertura y costo equivalentes. Costos y dos
autorizaciones iniciales: [Anexo E](05-business-case.md#pedido-inicial-paquete-mínimo).
Reglas de datos y liberación: [resoluciones vigentes](07-resoluciones.md).

:::

## Desarrollo y fuentes

Slides que sustenta: [Beneficio](../slides.md) y
[Arquitectura](../slides.md). Los hitos técnicos alimentan
además [Roadmap técnico, financiero y cultural](../slides.md).

## Objetivo

Sustentar **dos autorizaciones separadas**: la validación inicial durante la
preparación de 2026 y, si sus resultados lo permiten, el mínimo técnico de M1-M3
(enero-marzo de 2027). El [Anexo E](05-business-case.md), sección
«Pedido inicial: paquete mínimo», consolida sus topes de caja y capacidad.
Se propone además adoptar el marco de gates (los puntos de decisión de los
meses 3, 6, 9 y 12). La
arquitectura de abajo, una plataforma común de IA neutral al modelo y aislada
por cliente, que sirve a dos frentes, la IA en lo que Acme Labs vende a
bancos y fintechs y la IA en su operación interna, es la **dirección de
diseño**: los meses 4-12 no se autorizan hoy, se liberan decisión por decisión (ver
«Pedido vigente (parte técnica)»). Hoy no hay IA en producción dentro de lo que se vende
([fuente](../../context/hechos/ia-en-producto-y-oferta.md)), así que el primer
tramo configura herramientas existentes y mide. El frente producto pertenece
a la alternativa ampliada: su secuencia de los meses 7-9 exige plataforma
liberada en el mes 3, señal de cliente en el mes 6 y otra decisión y costeo.
El mínimo y su continuación no financian construir producto
([Anexo E](05-business-case.md), «Continuación condicional»). Sin plataforma,
la señal no basta para prometer ese piloto: rige la ruta diferida de
«Bifurcación en el mes 3: con señal y sin señal», sin fecha garantizada.

El Responsable de Tecnología responde por los hitos técnicos ([R-06](07-resoluciones.md#autoridad-y-liberaciones));
las personas que ocupan cada rol se nombran en el acta de la liberación que
habilita el entregable. Las cifras económicas del anexo son insumos para Finanzas; el [Anexo E](05-business-case.md)
consolida el business case y los límites de autorización.

La primera autorización no libera M1-M3: habilita una validación acotada con
agenda e imputación 2026 confirmadas. La segunda libera el paquete mínimo de los
meses 1-3, sin plataforma central, bajo las condiciones del [Anexo E](05-business-case.md),
sección «Pedido inicial: paquete mínimo». Las tablas económicas y de capacidad
del paquete completo quedan como comparación de otro alcance. No se aprueban
el contractor ni la excepción de 0,3 FTE del paquete completo. La arquitectura
objetivo y los meses 4-12 conservan su carácter condicional: una ampliación
exige nuevo alcance, calendario y costeo.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Tamaño de la organización | 60-70 personas; ~80% en Operaciones y Tecnología | [Fuente](../../context/hechos/tamano-y-estructura.md) |
| Capacidad ociosa | Utilización 83-90%, bench < 1 FTE: cada hora de plataforma compite con horas facturables | [Fuente](../../context/hechos/capacidad-y-utilizacion.md) |
| Gasto de tecnología | ~2% → ~4% de la facturación (ene-ago 2026); nube ≈ 80%, IA y herramientas de desarrollo el resto | [Fuente](../../context/hechos/costos-tecnologia-e-ia.md) |
| Costo por seat de IA | USD 40-45 por seat y mes (promedio ponderado de los seats de Claude; el de Copilot no está desglosado) | [Fuente](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real del agente de código | ≈ 12× lo pagado en suscripción (valor a precio API, estimación de telemetría, no factura) | [Fuente](../../context/hechos/costos-tecnologia-e-ia.md) |
| Seats de IA | Claude 40-45 y Copilot 20-25; ~90% de los eventos del agente de código sale de la terminal | [Fuente](../../context/hechos/uso-ia-interno.md) |
| Datos utilizables en 12 meses | Internos (código propio, tickets, documentación, telemetría). El código o los datos de un cliente no salen hacia un modelo externo, salvo dentro del entorno del propio cliente y con su permiso escrito ([R-08](07-resoluciones.md#gobierno-y-seguridad)); los de categoría especial, nunca | [Supuesto](../../context/supuestos/disponibilidad-de-datos.md) |
| Apetito de riesgo del cliente | Por defecto prohíbe modelos externos sobre su código y datos sin cláusula, inventario, ubicación de datos y no entrenamiento | [Supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md) |
| Precio y proveedor | El costo unitario no sube, pero la suscripción plana puede migrar a consumo; migrar de proveedor cuesta poco **si** el harness es neutral al modelo | [Supuesto](../../context/supuestos/precio-y-dependencia-de-modelos.md) |
| Ganancia de productividad | +10% a +25% de throughput en equipos propios (el borrador de OKR 2027 fija +20%) | [Supuesto](../../context/supuestos/ganancia-de-productividad.md), [OKR](../../context/hechos/okrs-y-objetivos.md) |
| Inversión incremental | 1%-3% de la facturación anual, sin contrataciones masivas | [Supuesto](../../context/supuestos/capacidad-de-inversion.md) |
| Costo cargado por rol | Rangos mensuales amplios y no calibrados contra la nómina: tech lead o arquitecto 4,5-10k USD, IA aplicada 4,5-11k USD, senior/DevOps/QA 3-7,5k USD | [Supuesto](../../context/supuestos/costo-cargado-por-rol.md) |
| Seats y adopción | Aun si se alcanzara el 80% combinado del OKR (el plan no lo alcanza, [Anexo D](04-personas-cultura.md)): 0,8 × 0,8 × (60-70) ≈ 38-45 personas activas, ya cubiertas por 40-45 seats | Cálculo propio sobre las fuentes de tamaño y de OKR: la adopción es de activación, no de más seats |
| No existe hoy un gateway de modelos ni un inventario formal de arquitectura | — | [Supuesto](../../context/supuestos/capacidades-ausentes.md): no consta en [stack](../../context/hechos/stack-y-plataforma.md); lo invalida cualquier inventario que lo contradiga |
| Umbrales técnicos (evals y gate de impacto, política de ruteo, portabilidad y costo del gateway, gate de valor y su cuenta de potencia, replan de los meses 4-6) | Propuestos por este anexo, sin medición previa | [Supuesto](../../context/supuestos/umbrales-tecnicos-propuestos.md) |

## Evidencia

### Cómo leer el alcance y los términos

El **mínimo vigente** configura herramientas existentes, prueba sus controles y
mide prácticas. La **plataforma objetivo** y el **producto** son alternativas
condicionales: sus tablas no prueban disponibilidad ni autorizan su ejecución.

FTE expresa dedicación equivalente de una persona a tiempo completo; para el
costeo se usan 160 h por mes y 480 h por trimestre
([convenciones](../../context/supuestos/convenciones-de-calculo.md)). No acredita una agenda liberada.

El gateway es la pasarela de llamadas a modelos. El harness reúne reglas,
contexto, herramientas y controles de ejecución; SDLC es el ciclo de desarrollo
de software. MCP es el protocolo de conexión con herramientas; CI, integración continua.

Las evals son pruebas de evaluación; retrieval recupera documentos y RAG usa
esa recuperación para responder con contexto. Working set es el contexto de
trabajo acotado; tenant, el entorno aislado de un cliente o del uso interno.

PII son datos personales identificables; DLP, controles contra pérdida de datos;
SSO, inicio de sesión único. ADR registra decisiones de arquitectura; SLO fija
objetivos de servicio; p95 es el percentil 95 y TCO, el costo total de propiedad.

BCRA es el Banco Central, regulador de los clientes financieros; SGSI, el
sistema de gestión de seguridad de la información que ya existe; FinOps, la
gestión del costo de nube y de modelos por consumo.

### Arquitectura de referencia (Agente = Modelo + Harness)

La tesis del marco de harness de agentes es que "el chatbot solo demuestra; la solución es el
harness" ([fuente](../../material/unidades/memoria-contexto-harness.md)). Se
mapean los siete componentes del harness
([fuente](../../material/conceptos/harness-agente-modelo-mas-harness.md)) a lo que
Acme Labs ya tiene y a lo que falta.

**Harness de SDLC existente.** El punto de partida incluye herramientas de harness
para SDLC de uso exclusivamente interno: no se entregan ni comercializan a clientes
([confirmación anonimizada](../../context/hechos/uso-ia-interno.md)).

Su cobertura, funciones, estado operativo, controles, contexto y memoria, métricas
y ahorro siguen sin verificar; se relevan antes de decidir qué reutilizar o ampliar.

La existencia del harness de SDLC no demuestra que ya estén cubiertas las capacidades
del harness central, gateway o plataforma de casos propios previstos.

Se contrasta qué reutilizar o ampliar antes de sumar trabajo o presupuesto;
su existencia no autoriza reconstruirlo automáticamente. El relevamiento (harness
interno, gateway e inventario de arquitectura) lo hace el Responsable de
Tecnología en M1-M3, dentro de las 24-40 h de Arquitectura del mínimo, y se lee en
la decisión del mes 3 ([R-16](07-resoluciones.md#arquitectura-y-medición)). Sin
relevamiento no hay brecha documentada para liberar plataforma; si no cabe en
esas horas, se recostea antes de la segunda liberación.

| Componente | Estado objetivo | Punto de partida |
|---|---|---|
| Modelos y gateway | Capa única con ≥ 2 proveedores detrás y registro de uso y costo. Enruta por clasificación de datos, por cliente y por región de procesamiento todos los casos propios; el agente de código, solo si su régimen comercial lo permite (ver "Política de ruteo") | Sin gateway (supuesto); herramientas por suscripción |
| Contexto y memoria | Working set con presupuesto; si no entra, falla en voz alta; memoria externa versionada; retrieval con metadata (vigente, fuente, nivel, cliente) | Diseño de contexto y memoria sin verificar, incluido el del harness interno de SDLC |
| Datos | Revisar y ampliar el inventario existente para las fuentes elegibles; data contracts en las fuentes que alimenten casos ([fuente](../../material/conceptos/m1u3-data-contracts.md)); datos sintéticos donde no se puede usar el real | Existe inventario con responsables, clasificación y calidad documentada; datos distribuidos entre sistemas. Cobertura, vigencia, integración y gobierno operativo común no confirmados ([confirmación anonimizada, sin validación documental](../../context/hechos/inventario-y-distribucion-de-datos.md)) |
| Herramientas (MCP) | Lista cerrada y aprobada; salida resumida con id, el dato nunca es una orden | Existe contrato de agentes de código con MCP aprobados ([fuente](../../context/hechos/gobierno-y-politica-ia.md)) |
| Ejecución y aislamiento | Un tenant = cuenta AWS + namespace + índice + claves propias; cero contexto compartido entre clientes | Ya hay cuentas AWS separadas por proyecto ([fuente](../../context/hechos/stack-y-plataforma.md)) |
| Guardrails y auditoría | Nivel de autonomía por caso (cinco niveles, de "sin IA" a "autónomo dentro de límites"; escala pedagógica, no estándar: [fuente](../../material/conceptos/m1u4-escala-autonomia-l0-l4.md)); gate humano antes de efecto irreversible; enmascarado de PII en inferencia ([fuente](../../material/conceptos/m1u3-anonimizacion-inferencia.md)) | Política aprobada según confirmación del responsable del caso ([fuente](../../context/hechos/gobierno-y-politica-ia.md)); controles específicos de IA no verificados ([fuente](../../context/hechos/seguridad-y-certificaciones.md)) |
| Verificación | Evals propios en CI, trazas, y cuatro tipos de release gate: rendimiento, seguridad, ética, impacto ([fuente](../../material/conceptos/m2u4-versionado-release-gates.md)) | Telemetría solo del agente de código |

Los cinco elementos de diseño ([fuente](../../material/conceptos/harness-cinco-elementos-diseno.md))
son el criterio de revisión de cada caso: objetivo y reglas reinyectados,
working set con presupuesto, memoria externa, herramientas con salida acotada y
gate humano.

### Dos frentes, restricciones distintas

| | IA en el producto vendido | IA en la operación interna |
|---|---|---|
| Qué es hoy | Nada en producción; propuesta al Directorio sin decidir; primeros casos saldrían de productos propios | Tres herramientas aprobadas; adopción ~7 de 10 en Tecnología y ~1 de 10 en Operaciones ([fuente](../../context/hechos/uso-ia-interno.md)) |
| Restricción dura | BCRA: documentar el uso de IA propio y de terceros, explicabilidad y avisar al cliente; secreto financiero; Ley 25.326 (no transferir datos a países sin protección adecuada) ([fuente](../../context/hechos/regulacion-clientes-financieros.md)) | Política de clasificación en cuatro niveles; "Restringido" nunca va a IA externa ([fuente](../../context/hechos/gobierno-y-politica-ia.md)) |
| Datos | Sintéticos o anonimizados; el producto con datos de categoría especial usa solo sintéticos | Código propio, tickets, documentación, telemetría |
| Autonomía en los 12 meses | Nivel 1 (asiste) a nivel 2 (prepara, no ejecuta): informar, recomendar, redactar; subir a nivel 3 (actúa con aprobación) **en el producto** se decide en el cierre del mes 12, no antes ([Anexo C](03-gobierno-seguridad.md), "Escala de autonomía: topes para los 12 meses") | Nivel 2 (prepara, no ejecuta) a nivel 3 (actúa con aprobación) con code review obligatorio, como hoy: el tope del mes 12 no rige para este uso interno; nivel 4 (autónomo dentro de límites) solo en sandbox sin credenciales productivas ni código o datos de un cliente |
| Lock-in a evitar | Que el cliente herede una dependencia de un proveedor de modelos | Que el flujo de ingeniería quede atado a funciones exclusivas de uno |

La certificación de seguridad vigente es de la organización, no de un producto
([fuente](../../context/hechos/seguridad-y-certificaciones.md)): la IA en producto
no puede presentarse como apoyada en una certificación de producto.

**Residencia de los datos.** En M1-M3 no se crea ningún flujo nuevo de datos: se
configuran herramientas ya contratadas sobre código y datos internos, y el código o
los datos de un cliente quedan fuera ([R-08](07-resoluciones.md#gobierno-y-seguridad)).
La matriz de controles registra, por superficie, dónde procesa y retiene el
proveedor, y el dictamen de Legal externo de M1 ([R-11](07-resoluciones.md#gobierno-y-seguridad))
dice si ese registro exige algún control nuevo. La región de procesamiento es
criterio de diseño de los casos propios, solo en la rama con plataforma: el gateway
la fija por cliente antes de habilitar un tenant.

### Cobertura de controles por superficie

El gateway enruta llamadas a modelos. Las herramientas aprobadas, en cambio, tienen
**cuatro superficies de uso** ([fuente](../../context/hechos/uso-ia-interno.md)), y no
todas pueden pasar por una pasarela. Hay dos pruebas distintas, con calendarios
distintos. **Controles:** toda superficie en uso en M1-M3 prueba sus controles en
M1-M3, dentro del mínimo; si su prueba no cabe en las horas validadas, esa
superficie no se usa hasta M4-M6 ([R-11](07-resoluciones.md#gobierno-y-seguridad)).
**Ruteo por la pasarela:** es de M4-M6 y solo en la rama con plataforma
([R-15](07-resoluciones.md#arquitectura-y-medición)). Qué superficie es enrutable de
verdad lo decide esa prueba (supuesto: no hay documentación de proveedor verificada).

| Superficie | Ruta al modelo | Control previsto | Telemetría | Estado |
|---|---|---|---|---|
| Terminal y agente de código (Claude) | Gateway, solo si el agente acepta un endpoint configurable **y** el régimen comercial lo permite (ver "Política de ruteo") | Siempre: *hooks* de permisos, escaneo de secretos en el equipo y en el repositorio, allowlist de MCP. Si se enruta, además DLP sobre prompts y nivel de dato en el gateway | Telemetría que ya existe; gateway por llamada si se enruta | Enrutable a probar; enrutado según régimen |
| Chat y escritorio (Claude, plan Team) | Directa a la aplicación del proveedor | Administración del plan (acceso único, retención, uso de datos) y bloqueo de datos Restringidos en navegador o equipo, si el parque lo permite | Reportes de administración del plan; encuesta si no hay exportación | No enrutable; control compensatorio |
| IDE (Copilot) | Directa; enrutable solo si admite proxy corporativo | Administración de la organización: repositorios y contenido excluidos, política de datos del proveedor | Métricas de uso de la organización | A probar |
| Correo, documentos y reuniones (Gemini en Workspace) | Dentro de Workspace | Administración de Workspace: DLP y controles de datos del dominio | Registros de auditoría de administración | No enrutable; control compensatorio |
| Casos propios (producto y agentes internos nuevos) | Solo por gateway | Todos los anteriores más aislamiento por tenant | Gateway | Enrutable por diseño |

**Política de ruteo (propuesta).** El ruteo es un medio, no una meta: un gate no
puede obligar a un cambio que encarezca el servicio. Lo que decide si el agente de
código pasa por el gateway es su régimen comercial, que se establece con la consulta
escrita al proveedor de la prueba de los meses 4-6. Los tres regímenes tienen nombre
fijo en todo el anexo:

| Régimen del agente de código | ¿Se enruta? | Qué se le exige en la lectura del mes 6 |
|---|---|---|
| **Suscripción que permite gateway**: suscripción plana y enrutar la preserva | Sí, por control y telemetría; sin efecto de precio | Ruta ≥ 90% de sus eventos y control verificado |
| **Suscripción que no lo permite**: suscripción plana y enrutar obliga a facturar por API, o respuesta ambigua | **No**, mientras la suscripción sea plana | Control verificado sin gateway (*hooks*, escaneo de secretos, allowlist de MCP, telemetría existente) y ruteo ensayado en laboratorio, listo para activarse si el régimen cambia |
| **Pago por consumo**: el proveedor ya cobra por consumo | Sí; el gateway es además la palanca de precio | Ruta ≥ 90% de sus eventos, control verificado y *fc* × *s* contra el umbral del Anexo E |

Los **casos propios** (producto y agentes internos nuevos) no tienen otra ruta:
pasan al 100% por el gateway en cualquier régimen. Chat, IDE y Workspace no se
enrutan: se cubren con control compensatorio verificado y riesgo residual
declarado.

**Qué mide el 90%.** Se adopta el denominador del [Anexo C](03-gobierno-seguridad.md)
("Seguridad: modelo de amenazas y controles"): eventos del agente de código que cuenta
la telemetría del gateway sobre el
total de eventos de ese agente según la consola del proveedor. La fuente ubica ~90%
en la terminal: es la cota de lo enrutable. Los casos propios se reportan aparte, al
100%, y no entran en el 90%. Se reportan siempre dos números: *cobertura de ruta*
(la del 90%, solo en la suscripción que permite gateway y en el pago por consumo) y
*cobertura de control*: superficies en uso con un control verificado por prueba,
meta 100% al cierre de M1-M3; una superficie sin prueba no se usa
([R-11](07-resoluciones.md#gobierno-y-seguridad)).

**Prueba de controles por superficie (M1-M3, en el mínimo).** (i) Positiva: una acción
permitida queda en la telemetría. (ii) Negativa: un secreto o un dato Restringido
sintético se bloquea o alerta, según el control. (iii) Bypass: se intenta usar el
mismo modelo por fuera (cliente directo, cuenta personal, herramienta no aprobada)
y se mide si se detecta. Un bypass sin control compensatorio impide declarar
cubierta esa superficie. El umbral de detección se fija con la primera medición.
**En M4-M6, solo en la rama con plataforma,** se repiten las tres pruebas con la
pasarela en el medio: la ruta registra la acción, bloquea el dato y detecta el
desvío; eso mide la cobertura de ruta, no reemplaza la prueba de controles.

**Lo que no se relaja.** Si la actividad semanal de los seats cae (disparador de
[Anexo C](03-gobierno-seguridad.md)), primero se investiga la causa: puede ser
fricción o puede ser evasión. Lo que puede pasar a monitoreo son los controles de
fricción de usos permitidos (confirmaciones, límites de tasa, herramientas MCP de
bajo riesgo). El bloqueo de secretos, de datos Restringidos y de código o datos de
un cliente sin su permiso escrito **sigue bloqueando** aunque se baje la fricción.

**Presupuesto de migración (paquete completo, rama con plataforma).** Llevar las
superficies enrutables al gateway y repetir las pruebas con la pasarela: 15-30
días-persona de DevOps/QA en M4-M6 (supuesto), unos 2,1-10,7k USD de tiempo a los rangos de [costo por
rol](../../context/supuestos/costo-cargado-por-rol.md) (3-7,5k USD por mes,
21 días hábiles por mes). Va dentro de la fracción de DevOps/QA de abajo; si la
excede, se reduce el alcance a las superficies enrutables. La prueba de controles
de M1-M3 no está acá: va en las 32-56 h de DevOps del mínimo.

### Prueba de portabilidad y costo del gateway (meses 4-6)

Hoy la "cobertura de precio" es una hipótesis. El [Anexo E](05-business-case.md)
("Gateway: suscripción contra consumo") muestra que el gateway solo se paga por
precio si el proveedor cobra por consumo y el ruteo baja ese consumo en una
fracción *s* que supere un umbral. Con los valores vigentes del Anexo E (infraestructura
a régimen sin piloto), es 38,4% a 4×, 25,6% a 6× y 12,8% a 12×. La decisión usa
la fórmula sin redondear: 33k USD / (6 × 21,5k USD) = 25,581395…% en el ejemplo central.
Esto cubre solo la infraestructura modelada del gateway, no el programa completo. La prueba mide
lo que el Anexo E declara hueco. Hasta tener el resultado, el plan no afirma cobertura de
precio.

**Población y gasto elegible.** Se adopta la definición del
[Anexo E](05-business-case.md) ("Base del cálculo: el gasto elegible"), con su
símbolo. *fc* y *s* se miden sobre la misma población: el **gasto elegible**, que
hoy es el consumo del agente de código a precio de lista (40-45 seats, con base en
su suscripción de 19-24k USD por año en el Anexo E). *fc* es la fracción del **costo** de ese
gasto que pasa por el gateway, no de eventos. Chat, IDE y Workspace quedan fuera del
gasto elegible y su exposición se informa aparte. Así, el ahorro es k × gasto
elegible × *fc* × *s*, comparable con el costo del gateway del Anexo E, y el criterio es
*fc* × *s* ≥ el umbral del Anexo E. Si *fc* = 0,9, pasar a 6× pide *s* ≥ 28,423772…%;
con menor *fc*, la reducción necesaria aumenta. El 90% de eventos no impone una cota al costo enrutable. La
fracción de eventos (cuatro superficies, o solo el agente según el denominador del
Anexo C) es métrica de
cobertura de controles y no se multiplica por *s*.

| Qué se mide | Cómo | Resultado |
|---|---|---|
| Fracción enrutable del costo (*fc*) | Del gasto elegible (hoy, el agente de código a precio de lista), la parte del costo que puede pasar por el gateway, ponderada por costo y no por eventos. Se estima en laboratorio en los meses 4-6 con la telemetría del agente; si no hay costo por evento, se usa como estimador la fracción de eventos del denominador del Anexo C y se marca "estimado". La fracción de eventos por superficie se reporta aparte, como cobertura de controles | *fc* del gasto elegible; eventos por superficie, aparte |
| Reducción de consumo (*s*) | Reejecución en laboratorio de un lote fijo de tareas del agente de código sobre repositorios propios (nivel Confidencial, con contrato sin entrenamiento). El lote representa la misma población del gasto elegible, con la mezcla de tipos de tarea de la telemetría ponderada por costo, en tres configuraciones: modelo actual por API, ruteo a modelos más baratos para subtareas, y ruteo con caché de prefijo. Se cuentan los tokens y el costo a precio de lista | *s* = 1 − costo con ruteo / costo sin ruteo, sobre lo enrutable |
| Calidad | La misma tarea pasa sus pruebas y la revisión de código en las tres configuraciones; para casos propios, la suite de evals del caso de referencia (abajo) | Diferencia de la tasa de éxito contra el modelo actual |
| Suscripción | Consulta escrita al proveedor y lectura del contrato: el plan plano admite un endpoint propio, o enrutar obliga a facturar por API | Sí, no o ambiguo, con la fuente |
| Portabilidad | El caso de referencia corre en dos proveedores detrás del gateway | Días-persona de migración |
| Superficies fuera del gasto elegible | Chat, Workspace e IDE: no entran en *fc* ni en *s* | Exposición de precio sin cobertura, declarada aparte |

**Criterio de aceptación** (umbrales propuestos, [fuente](../../context/supuestos/umbrales-tecnicos-propuestos.md)):
la cobertura potencial ante pago por consumo se afirma solo si se cumplen las
condiciones de la prueba. No se atribuye ahorro observado a una suscripción plana.

1. *fc* × *s* ≥ el umbral sin redondear del Anexo E para k = 6× (25,581395…% en el ejemplo central), con *fc* sobre el gasto
   elegible; es el múltiplo que dispara el gate
   de FinOps en el [Anexo F](06-roadmap-riesgo.md).
2. La tasa de éxito con ruteo no cae más de 5 puntos contra el modelo actual.
3. El régimen comercial queda documentado: el ruteo se activa solo si preserva
   la suscripción plana o el proveedor ya cobra por consumo. En el primer caso
   aporta control y telemetría, sin ahorro de precio; en el segundo se evalúa ahorro.
4. Migrar de proveedor cuesta ≤ 20 días-persona.

Si falla cualquiera, el gateway se justifica por control y telemetría de los
casos propios, no por precio. La exposición de las superficies que no enrutan
se informa siempre aparte.

| | Detalle |
|---|---|
| Quién | El contractor de IA aplicada arma el lote y corre las configuraciones; DevOps/QA instrumenta el gateway; FinOps calcula *s* y la exposición. Habilita cada ruta el Responsable de Tecnología, con el régimen comercial confirmado por escrito con el proveedor y verificado por el CFO ([R-17](07-resoluciones.md#arquitectura-y-medición)); sin esa confirmación, la ruta queda en laboratorio con tráfico sintético |
| Cuándo | Meses 4-6, semanas 6-11 del tramo, con el gateway en laboratorio; el resultado entra en el paquete de la lectura del mes 6 |
| Costo | Tiempo dentro de las fracciones de los meses 4-6. El consumo por API de la reejecución tiene un tope que fija FinOps dentro del renglón de infraestructura de los meses 4-6: no suma caja ni tiene precio propio |
| Qué decisión habilita (lectura del mes 6) | Pasa: queda documentada la cobertura potencial ante consumo, con *fc* × *s* medidos; Finanzas recalcula con el régimen y costo vigentes. La suscripción plana no genera ahorro por ruteo. Si no permite gateway, el ruteo queda ensayado sin activarse; con pago por consumo puede activarse. No pasa: la palanca de precio sale del deck y de la defensa; cualquier infraestructura de control requiere justificar alcance y costo. El gate nunca obliga a romper la suscripción plana (Anexo E, segundo esquema) |
| Abandono | Sin lote reproducible o sin respuesta del proveedor al cierre de los meses 4-6: no se afirma cobertura de precio en la lectura del mes 6 |

### Métricas técnicas (las sostiene este anexo; Finanzas las consume)

**Alcance de la tabla.** El piloto de producto, el caso de referencia interno,
la cobertura de precio y los proveedores detrás del gateway son objetivos de
la **alternativa con plataforma liberada**, no resultados financiados por el mínimo.

Requieren las decisiones y capacidades de la ruta «Bifurcación en el mes 3»;
el producto exige además señal y otra decisión y costeo. Las demás filas son
indicadores y metas de referencia, no mejoras demostradas ni garantizadas por el mínimo.

| Métrica | Hoy | Esperado a 12 meses | Fuente |
|---|---|---|---|
| Funcionalidades de IA en producción en lo vendido | 0 | Alternativa ampliada: con plataforma liberada en el mes 3, señal en el mes 6 y otra decisión y costeo: 1 piloto acotado evaluado con gate scale/kill (meses 7-12). Si no: 0, por diseño | [Fuente](../../context/hechos/ia-en-producto-y-oferta.md); ruta «Bifurcación en el mes 3» |
| Caso de referencia interno en uso | 0 | En nivel 2 (prepara, no ejecuta) para Tecnología y Operaciones, con su protocolo de evaluación aprobado | Este anexo |
| Cobertura de precio del gateway (*fc* × *s*) | Sin medir | Medida en la lectura del mes 6 contra el umbral del Anexo E a 6×, solo si la decisión del mes 3 libera la plataforma; sin ella, se difiere y no se afirma la palanca | Prueba de portabilidad y costo; «Insumos para el deck», mensaje al CFO |
| Cobertura de la telemetría de IA | Solo agente de código | Terminal, chat, IDE y Workspace, en agregados por área y semana desde las consolas existentes: personas activas y uso por superficie; ningún evento por persona se extrae ([R-13](07-resoluciones.md#gobierno-y-seguridad)) | [Fuente](../../context/hechos/uso-ia-interno.md) |
| Personas con IA activa por semana | ~1 de 3 (org), ~7 de 10 (Tecnología), ~1 de 10 (Operaciones) | Tecnología ≥ 80% desde los meses 4-6 y ≥ 85% en los meses 10-12; Operaciones habilitadas, aparte. El 80% combinado del OKR no se alcanza: se informa su valor real ([Anexo D](04-personas-cultura.md), decisión sobre la meta de adopción y el OKR combinado) | [OKR borrador](../../context/hechos/okrs-y-objetivos.md), [Anexo D](04-personas-cultura.md) |
| Throughput de la cohorte (PR aceptados por persona-semana activa, agregados por área; ver definición) | Base prospectiva congelada en las semanas 1-4 del plan; serie retrospectiva de la preparación previa solo para tendencia y ruido | Hipótesis de +10% a +25% en equipos propios. Se acredita solo si el peor caso de la lectura del mes 9 es mayor que 0 (ver «Gate de valor») | [Supuesto](../../context/supuestos/ganancia-de-productividad.md) |
| Gasto de tecnología / facturación | ~4% | < 3,5% (borrador de OKR), medido sin la inversión del plan, que se informa aparte ([R-29](07-resoluciones.md#finanzas)) | [OKR borrador](../../context/hechos/okrs-y-objetivos.md) |
| Proveedores de modelos operativos detrás del gateway | 0 (supuesto) | ≥ 2, con migración ensayada | Supuesto |

### Throughput: unidad, cohorte y conversión

Las gates económicas del plan se apoyan en el throughput. Se define acá para que
Finanzas lo convierta en valor con la misma unidad.

| Elemento | Definición propuesta (supuesto) |
|---|---|
| Unidad | Pull request aceptado: mergeado, con las compuertas de calidad aprobadas y sin reversión a los 14 días, por persona-semana activa de la cohorte |
| Agregación | Totales por área y semana, calculados en el origen: ningún conteo por persona se extrae ni se retiene ([R-13](07-resoluciones.md#gobierno-y-seguridad)). Se estratifica por tipo de trabajo (funcionalidad, error, mantenimiento) y por tamaño del cambio (terciles de líneas modificadas), con los pesos de estrato fijados en la base |
| Cohorte | Padrón de los equipos propios, como los define el [supuesto](../../context/supuestos/desarrolladores-en-equipos-propios.md) (15-20 personas), fijado en la base, con exclusiones y bajas registradas como conteos. Staffing queda fuera |
| Comparador | La base prospectiva congelada (semanas 1-4 del plan) de la misma cohorte, ajustada por la tendencia que estima la serie retrospectiva de la preparación previa. Tecnología ya usa IA hoy (~7 de 10), así que la ganancia se mide **sobre ese punto de partida**, no contra un mundo sin IA |
| Calidad | Incidentes y retrabajo por cada 100 PR (reversiones y correcciones dentro de 30 días), con los mismos agregados |
| Ruido | Lo fija el total de PR de la base y de la ventana, no la cantidad de personas: ver «Cuenta de potencia» |

**Protocolo de medición único (lo adopta el [Anexo F](06-roadmap-riesgo.md) en las
lecturas de los meses 6, 9 y 12; [fuente](../../context/supuestos/umbrales-tecnicos-propuestos.md)).**
Se produce durante la primera autorización, con la serie de la preparación previa
y antes de ver un dato de los meses 1-3, y se fecha al ratificarlo: así nadie elige
base, umbral ni regla de calidad después de ver el ruido. Lo ratifica el AI
Council antes de la segunda liberación, sobre el acta y la tabla de operación de
abajo ([R-14](07-resoluciones.md#arquitectura-y-medición)); no lo ratifica quien lo
produce ni la autoridad del gate. Sin método ratificado no se libera M1-M3.

| Elemento | Propuesta |
|---|---|
| Base | La prospectiva congelada en las semanas 1-4 del plan (u 8, ver «Respaldo»), de la misma cohorte, fechada y sin edición. La serie retrospectiva estima ruido y tendencia; no es base de atribución |
| Estimador | Razón de tasas: PR aceptados por persona-semana activa en la ventana del gate sobre la misma tasa en la base, con los pesos de estrato de la base y ajustada por la tendencia de la serie retrospectiva. Todo con totales por área y semana |
| Intervalo | 90% bilateral por conteos, en escala logarítmica, ampliado por la sobredispersión φ (varianza sobre media de los totales semanales de la serie retrospectiva, sin tendencia). φ se fija antes de la segunda liberación. Reemplaza al *bootstrap* por personas, que exigía series por persona |
| Ventanas | Mes 6: semanas maduras de M4-M6, solo descriptiva. Mes 9: todas las semanas maduras de M7-M9 (al menos 8). Mes 12: las de M10-M12, como insumo del año 2 |
| Muestra mínima | **15 personas** del padrón con PR en la base, informadas como conteo. Con menos, ninguna lectura decide por valor y el mes 9 decide como el mes 6 |
| Calidad | **Guardia de daño, no prueba de no deterioro.** La misma razón e intervalo sobre el aumento de incidentes y de retrabajo por cada 100 PR, por separado. Hay **daño** si el límite inferior del aumento es mayor que 0 en cualquiera de los dos: el gate corta aunque el throughput pase. Sin daño, la calidad no bloquea. La no inferioridad con margen δ = +10% no se exige porque esta cohorte no puede demostrarla (cuenta abajo). La guardia detecta solo deterioros grandes: un incidente que activa suspensión en el [Anexo C](03-gobierno-seguridad.md) conserva esa precedencia sin esperar al gate |
| Respaldo | Criterio mecánico, ciego al resultado. En la semana 4, con λ y φ observados en la base, la oficina del CAIO recalcula la tabla de potencia. Si con base de 4 semanas la lectura del mes 9 no distingue con 80% de potencia una ganancia igual al techo del rango del [supuesto](../../context/supuestos/ganancia-de-productividad.md) (+25%, es decir ln 1,25 ≈ 22,3 pp en la escala de la tabla de potencia) y con base de 8 sí, la base se extiende a la semana 8, y la formación básica, la prueba y la formación intermedia se desplazan juntas a la semana 9; lo verifica Arquitectura ([R-18](07-resoluciones.md#arquitectura-y-medición)). Si no la distingue ni con 8, no se extiende: el acta lo declara y el AI Council decide con la tabla de operación. La retrospectiva no atribuye ganancia: mezcla tendencia, estacionalidad (los meses 1-3 caen en enero-marzo; supuesto), adopción previa y cambios de equipo |
| Congelamiento | Versión, φ, pesos de estrato, ventanas y umbrales se fechan antes de la segunda liberación y no se editan desde que se congela la base. Un cambio posterior es un desvío: se registra con fecha y motivo, rige desde la ventana siguiente y la ventana en curso se lee con la versión vigente al abrirse |

**Tasas base cero o sin denominador.** Con cero eventos de calidad en la base no
hay razón calculable: se informan conteos, exposición y diferencia absoluta por
100 PR, sin declarar ausencia de daño. Sin PR o personas-semana en el
denominador, el indicador es no estimable, no cero: se reformula antes de empezar,
con ratificación del AI Council, o, si ocurre en una lectura, se aplica la salida
del Anexo F.

### Cuenta de potencia (aproximación de planificación)

Con P_b PR aceptados en la base y P_v en la ventana del gate (P = n × λ ×
semanas, con n personas activas y λ PR por persona y semana), el error estándar
del logaritmo de la razón es **SE = √(φ × (1/P_b + 1/P_v))**. El semiancho del
intervalo de 90% es 1,645 × SE. La menor mejora que una lectura distingue de cero
con 80% de probabilidad (la convención usual de potencia) es (1,645 + 0,842) × SE
≈ 2,49 × SE: 1,645 es el cuantil que deja 5% en la cola del límite inferior y
0,842, el del 80%. Agrupar por persona, por área o por semana no cambia la cuenta:
el piso lo pone el total de PR, y la base es el factor que más pesa.

λ y φ no tienen dato. La tabla usa φ = 1 (el piso: la sobredispersión lo agranda)
y tres ritmos ilustrativos; son parámetros de planificación, y el acta los
reemplaza con la serie retrospectiva. Puntos porcentuales en escala logarítmica,
que para cambios chicos se leen como porcentaje; ventana de 8 semanas.

| n | λ | PR de la base de 4 semanas | Semiancho (pp) | Mejora distinguible al 80% (%) | PR de la base de 8 semanas | Semiancho (pp) | Mejora distinguible al 80% (%) |
|---|---|---|---|---|---|---|---|
| 15 | 1 | 60 | 26,0 | 39,3 | 120 | 21,2 | 32,1 |
| 15 | 2 | 120 | 18,4 | 27,8 | 240 | 15,0 | 22,7 |
| 15 | 4 | 240 | 13,0 | 19,7 | 480 | 10,6 | 16,1 |
| 20 | 1 | 80 | 22,5 | 34,0 | 160 | 18,4 | 27,8 |
| 20 | 2 | 160 | 15,9 | 24,1 | 320 | 13,0 | 19,7 |
| 20 | 4 | 320 | 11,3 | 17,0 | 640 | 9,2 | 13,9 |

Tres consecuencias, que este anexo fija hoy:

1. **El semiancho de ±3 pp no es alcanzable.** Con ventana del doble de la base
   hace falta P_b ≥ 1,645² × 1,5 / 0,03² ≈ 4.509 PR en la base: con λ = 2 y base
   de 4 semanas, unas 564 personas. Se retira como requisito.
2. **El gate anterior casi no podía pasar.** Con n = 18 y λ = 2 (ilustrativos), SE ≈
   10,2 pp. Pasar por límite inferior ≥ +3% en el mes 6 y ≥ +8% en el mes 9 tenía
   probabilidad ≈ 6% en ambos con la mejora del escenario base (+3,75% y +9%), y ≈
   27% en el mes 9 con la del optimista (+20%). Cortar en el mes 6 con estimado ≤ 0%
   tenía ≈ 36% de probabilidad aun con la mejora del base.
3. **La calidad no admite prueba de no deterioro.** Para que un aumento estimado
   en 0 quede bajo δ = +10% hace falta 1,645 × √(1/e_b + 1/e_v) ≤ ln(1,10), es
   decir, ≥ 447 eventos en la base con ventana del doble. Cada PR aporta a lo sumo
   un evento: con 20 personas harían falta más de 5,6 PR por persona y semana,
   todos con incidente o retrabajo. Por eso la calidad queda como guardia de daño.

### Gate de valor (fijado por este anexo; el Anexo F lo adopta)

La pregunta deja de ser "pasa el +3%" y pasa a ser "la mejora se distingue de
cero, con calidad sin daño". El mes 6 no puede leer valor: la mejora esperada del
base (+3,75%) es menor que cualquier semiancho de la tabla. El valor se lee en el
mes 9 con todas las semanas maduras de M7-M9. Las bandas de espera y corte del
mes 9 son las del [Anexo F](06-roadmap-riesgo.md), por estimado.

| Gate | Qué decide | Pasa | Espera | Corta |
|---|---|---|---|---|
| Mes 6 | Continuidad de M7-M9 por adopción, calidad, costo y controles (Anexo F). El throughput se informa con su intervalo y no acredita valor | Sin daño de calidad ni caída demostrada del throughput, con adopción, costo y controles según el Anexo F | Ninguna por medición: seis semanas más no compran precisión, porque el piso lo pone la base | Daño de calidad, o caída demostrada (límite superior del throughput menor que 0) |
| Mes 9 | Valor, con las semanas maduras de M7-M9 | Peor caso mayor que 0 y sin daño: se acredita el peor caso, y lo convierte el CFO ([R-19](07-resoluciones.md#arquitectura-y-medición)) | Estimado ≥ +5% sin pasar: la espera única de 6 semanas, sin expansión ([R-27](07-resoluciones.md#finanzas)) | Estimado < +5%, o daño |
| Mes 12 | Insumo del año 2, con las semanas maduras de M10-M12 | Peor caso mayor que 0 y sin daño: evidencia de valor para el año 2 | — | Sin esa evidencia, el año 2 no se financia por valor |

**Si la medición no distingue,** el beneficio acreditado es 0 y ninguna lectura
sin distinción libera expansión ni año 2 por valor. La continuidad sigue
decidiéndose por adopción, calidad, costo y controles, dentro del techo de cada
tramo.

**Falsa alarma de la guardia.** Cada regla de corte por daño o por caída es
unilateral al 5%. En una lectura corren tres (throughput, incidentes y
retrabajo): sin ningún efecto real, la probabilidad de cortar por azar es hasta
1 − 0,95³ ≈ 14%; con la mejora del base y calidad sin cambio, ≈ 12% (2% del
throughput más ≈ 10% de los dos de calidad). Es el precio de que la calidad corte
sin esperar; el acta lo recalcula y el AI Council lo ratifica.

**Tabla de operación del mes 9 (ilustrativa: n = 18, λ = 2, φ = 1, base de 4
semanas y ventana de 8).** Probabilidad de cada salida en la primera lectura,
antes de la espera:

| Mejora real en M7-M9 | Pasa | Espera | Corta |
|---|---|---|---|
| 0% | 5% | 27% | 68% |
| +9% (base: 15% × rampa 60%) | 21% | 43% | 36% |
| +20% (optimista: 25% × rampa 80%) | 56% | 35% | 10% |

La espera de 6 semanas suma semanas a la ventana (SE de ≈ 10,2 a ≈ 9,4 pp) y le da
tiempo a la rampa, pero no cambia el piso. En el mes 6, cortar solo por caída
demostrada del throughput tiene ≈ 5% de probabilidad sin mejora real y ≈ 2% con
la del base; sumada la guardia de calidad, ≈ 14% y ≈ 12%. El
acta publica esta tabla con λ y φ observados y la cohorte real; sobre ella
ratifica el AI Council ([R-14](07-resoluciones.md#arquitectura-y-medición)). Con
15-20 personas, el año solo demuestra con buena probabilidad una mejora cercana
al techo del rango; el plan lo dice así y no promete más.

**Camino esperado con los valores ilustrativos.** Con λ = 2, la base de 4 semanas
no distingue ln 1,25 ≈ 22,3 pp para ningún n de 15-20 (24,1-27,8); la de 8 sí con
n = 18-20 (19,7-20,7) y no con n = 15 (22,7). El camino esperado es entonces la
base de 8 semanas, con formación desde la semana 9 y lectura del mes 3 reducida
([R-18](07-resoluciones.md#arquitectura-y-medición)); con 15 personas, ninguna
lectura decide por valor. El acta lo confirma o lo descarta con λ y φ reales,
antes de la segunda liberación, y los calendarios de formación y de la lectura
del mes 3 lo absorben como caso base, no como contingencia.

### Acta de viabilidad de datos, antes de ratificar el método

El acta la produce QA/análisis de datos, bajo el Responsable de Tecnología,
durante la validación inicial; la verifica el verificador senior independiente
y, sobre ella, el AI Council ratifica el método antes de la segunda liberación
([R-14](07-resoluciones.md#arquitectura-y-medición)). Sin ratificación no se libera M1-M3. Tener PR,
CI y tickets no prueba que las series sean enlazables. El acta y el protocolo
retrospectivo se producen durante la primera autorización, mediante lectura de
datos corporativos autorizados, y se verifican antes de la segunda liberación.
Antes de aprobar el método y de iniciar el tratamiento, el acta debe permitir que otro operador
reproduzca la extracción y las acciones del gate con el mismo corte.

- Guardá consulta o script versionado, permisos de lectura, fecha de corte,
  zona horaria, filtros, versión y huella del extracto. La consulta agrega en el
  origen por área y semana: no extrae ni persiste series por persona, y el padrón
  se usa solo dentro del entorno autorizado. Antes de extraer cualquier serie,
  incluida la retrospectiva de la preparación, el Responsable de seguridad aprueba
  y comunica el tratamiento ([R-13](07-resoluciones.md#gobierno-y-seguridad)); sin
  esa aprobación no se extrae. Al Directorio llega evidencia anonimizada.
- Distinguí el conector de solo lectura en origen de la persistencia de los
  registros extraídos: guardar extractos es una escritura. Antes de persistir,
  el Responsable de seguridad aprueba clasificación, ubicación, permisos y retención
  de esos registros ([R-13](07-resoluciones.md#gobierno-y-seguridad)) según el [Anexo C](03-gobierno-seguridad.md) y la
  [elegibilidad de las fuentes](../../context/supuestos/disponibilidad-de-datos.md).
  Esa validación y la disponibilidad del almacenamiento no se presumen resueltas.
- Documentá el diccionario y las claves PR→commit→CI→reversión→ticket→incidente,
  incluidos enlaces faltantes, duplicados, correcciones y reglas de atribución.
  Ausencia de enlace no equivale a ausencia de incidente o retrabajo.
- Registrá, como conteos, padrón, exclusiones y bajas, personas-semana expuestas,
  mezcla de estratos y cobertura de cada enlace. Una encuesta de uso no sustituye
  estas series.
- Estimá λ, φ y los eventos de calidad con la serie retrospectiva y la cohorte
  real; publicá la tabla de potencia y la tabla de operación de M6/M9/M12
  («Cuenta de potencia» y «Gate de valor»), incluidos daño, base cero y muestra
  insuficiente. El ensayo no certifica atribución ni inventa observaciones.

Cada indicador completa los siguientes campos. Productor y verificador son
los roles de la tabla, siempre personas distintas; quienes los ocupan se
nombran en el acta de la segunda liberación ([R-06](07-resoluciones.md#autoridad-y-liberaciones), [R-14](07-resoluciones.md#arquitectura-y-medición)). Cobertura significa
registros enlazados y maduros sobre registros elegibles, informando ambos
conteos y los faltantes, sin reducir el denominador para ocultarlos.

| Indicador | Fuente y numerador | Denominador | Ventana y maduración | Cobertura y responsables |
|---|---|---|---|---|
| Throughput | PR + CI + registro de reversiones: PR mergeados con calidad aprobada y sin reversión a 14 días | Personas-semana activas de la cohorte, en totales por área y semana; razón contra la base | Base semanas 1-4 (u 8) y ventanas del «Gate de valor», con corte fechado; cada PR madura 14 días | PR con CI y reversiones observables / PR elegibles; DevOps/QA produce, el verificador senior independiente verifica |
| Incidentes | Tickets e incidentes enlazados a PR: incidentes únicos atribuibles dentro de 30 días, con severidad separada | PR mergeados con CI aprobado y seguimiento completo de 30 días; tasa ×100, sin excluir los PR revertidos | Mismos cortes y estratos que throughput; seguimiento de 30 días | PR con seguimiento y enlace auditable / PR elegibles; QA produce, el Responsable de seguridad clasifica la severidad y el verificador senior independiente verifica |
| Retrabajo | PR, reversiones y tickets: PR con reversión o corrección atribuible dentro de 30 días, contados una vez por PR | Mismos PR maduros de calidad; tasa ×100 | Mismos cortes; seguimiento de 30 días | PR con reversiones/tickets observables / PR elegibles; QA produce, el verificador senior independiente verifica |

Fijá antes del tratamiento el cierre de cada ventana, dejando 30 días de
seguimiento antes de la lectura de calidad; throughput exige sus 14 días.
Los registros inmaduros no se cuentan hasta madurar, nunca como ceros. El acta declara
el desfase entre actividad y lectura, su cobertura y cualquier corrección
versionada por eventos tardíos. Sin cobertura suficiente, no se pasa por valor.

El verificador de los indicadores es el verificador senior independiente, fuera
de la línea de Tecnología: Tecnología produce los indicadores y no los verifica. En cada
lectura (meses 3, 6, 9 y 12) reproduce los indicadores desde la consulta
versionada. Sus horas de la preparación están en la fila de 8-16 h del
[Anexo D](04-personas-cultura.md); las de cada lectura las costea Finanzas dentro
del techo de cada tramo. La autoridad del gate (el CEO, por delegación) y quien
ratifica el método (el AI Council) son funciones distintas de quien extrae y
verifica, y quien verificó se abstiene en la ratificación ([R-14](07-resoluciones.md#arquitectura-y-medición)). Sin
extracción reproducible o enlaces suficientes, reformulá el método y el
calendario antes de iniciar. Si se extiende la base hasta la semana 8,
desplazá también formación básica y prueba que comenzarían en la semana 5,
además de la intermedia: ninguna intervención nueva entra en la base.

**Conversión a valor: dos lecturas que responden preguntas distintas.** Con una
ganancia de throughput *g*:

| Lectura | Fórmula | Qué valúa | Cuándo vale |
|---|---|---|---|
| Horas evitadas a output fijo | g / (1 + g) de las horas de la cohorte (g = 15% da ~13,0%; 10% da ~9,1%; 25% da 20%) | Capacidad liberada | Siempre es un piso, pero solo es caja si evita una contratación o se vende |
| Output adicional con las mismas horas | g del output | Producción extra | Solo si hay demanda (backlog o venta) con un precio; sin destino no vale nada |

Recomendación del anexo: el caso base usa la lectura de **horas evitadas a output
fijo**, que es la más conservadora (vale 1/(1+g) de la de output adicional). La
lectura de output adicional se muestra solo como
sensibilidad, con el destino de la capacidad decidido en la lectura del mes 6. La ganancia que entra en
cualquiera de las dos es el peor caso de una lectura que pasó («Gate de valor»). Ninguna de las dos
es caja por sí sola. El cálculo de capacidad liberada y del equilibrio lo hace
Finanzas en el [Anexo E](05-business-case.md); este anexo le pide que use la
lectura de horas evitadas y separe el retorno económico del retorno de caja.

### Medición del problema de integración, antes del mes 6

Antes de decidir construir el asistente de producto, observá a usuarios
elegibles intentando integrar con la documentación y el soporte actuales en un
sandbox autorizado, con datos propios o sintéticos. Registrá tarea, versión,
pasos, obstáculos, ayuda recibida y resultado; no hace falta plataforma central
para observar el problema.

**Métrica principal propuesta:** tiempo a la primera integración exitosa,
desde que el usuario dispone de acceso y prerrequisitos acordados hasta que
completa el flujo de prueba y pasa la aceptación de integración definida antes
de observarlo. Fuente: marcas del sandbox/CI y bitácora de la sesión. Registrá
tiempo transcurrido y tiempo de trabajo por separado, población y ventana;
reportá dispersión, integraciones completadas y abiertas, sin borrar fallas.

**Secundaria propuesta:** consultas de soporte por integración (tickets y
consultas de la misma tarea / intentos de integración elegibles), con ventana
de seguimiento fijada previamente e intentos abiertos informados aparte.
Producto y Comercial acuerdan elegibilidad, criterio de éxito y umbral antes
de M6; sin ese acuerdo no se libera construcción. El mecanismo por defecto es la
eficiencia de soporte de integración, valorizada como capacidad liberada:
Producto lo propone y el CFO verifica su valorización ([R-30](07-resoluciones.md#roadmap-y-comercial)).
No se presume porcentaje de mejora ni ingreso.

Compará mejorar documentación/soporte, configurar un asistente e integrarlo al
producto sobre la misma tarea. Sin dolor observado, base o señal suficiente,
diferí la construcción. Esta medición no elimina la dependencia de plataforma
del itinerario vigente de producto: otra ruta requiere diseño y costeo.

### Contexto, evals y lo que el marco de referencia no resuelve

- **Estrategia de contexto:** prompt, RAG, fine-tuning y contexto largo se combinan;
  la elección tiene implicancias de privacidad, no solo técnicas
  ([fuente](../../material/conceptos/m1u3-estrategias-de-contexto.md)). Se parte de
  RAG con metadata y de prompting; **no hay fine-tuning en el plan** (sin datos de
  cliente utilizables). Los tamaños de ventana publicados envejecen y no se usan.
- **Fallas de contexto:** el diseño ataca las diez fallas de contexto catalogadas
  ([fuente](../../material/conceptos/harness-diez-fallas-contexto.md)), sobre todo
  tool-output bloat, retrieval noise e inyección indirecta en agentes con herramientas.
- **Hueco declarado:** el material de referencia sobre evals no da metodología ni umbrales de release gate
  ([fuente](../../material/conceptos/m2u4-evals.md)). Este anexo los **propone** en
  el protocolo de evaluación de abajo; se recalibran con la
  primera medición de los meses 4-6, y hasta entonces ningún número de calidad va a una slide.
- **Ahorro de inferencia:** se usan los mecanismos (ruteo por modelo, caché de
  prefijo estable) **sin porcentaje**: el "60-80%" que circula en el material de referencia no tiene fuente primaria
  ([fuentes faltantes](../../material/huecos.md), [fuente](../../material/conceptos/m2u4-tokenomics.md)).

### Caso de referencia: recorrido de datos y protocolo de evaluación

El harness v1, la suite de evals y la prueba de portabilidad de los meses 4-6 necesitan un
caso concreto. Con el producto diferido, ese caso tiene que ser interno. El
portfolio del CAIO ([Anexo F](06-roadmap-riesgo.md)) eligió como hipótesis de
producto un asistente de integración en la plataforma propia; este caso interno
queda como el del frente interno y como prueba del método que ese piloto
reutiliza. Si el portfolio cambia, se rehace este caso con la misma estructura.

**Caso: asistente de conocimiento interno.** Responde preguntas de Tecnología y
Operaciones sobre la documentación de los productos propios, los runbooks y los
tickets internos resueltos, siempre con cita a la fuente. Nivel 1 (asiste: informa) a
nivel 2 (prepara, no ejecuta: redacta un borrador que una persona revisa). Usa solo datos que el
[supuesto de disponibilidad](../../context/supuestos/disponibilidad-de-datos.md)
declara utilizables, y ataca la brecha de adopción de Operaciones (~1 de 10,
[fuente](../../context/hechos/uso-ia-interno.md)).

**Recorrido de datos.** Cada paso tiene un control que lo
verifica; los niveles son los de la [política](../../context/hechos/gobierno-y-politica-ia.md).

| # | Paso | Qué pasa con el dato | Control | Si falla |
|---|---|---|---|---|
| 1 | Fuente | Documentación de productos propios, runbooks y tickets internos resueltos de los últimos dos trimestres | Inventario existente revisado y ampliado en los meses 1-3 para las fuentes elegibles, con dueño, calidad y nivel | Sin dueño, la fuente no entra |
| 2 | Clasificación | Entran Público, Interno y Confidencial. Restringido (datos personales de clientes, credenciales, código bajo NDA, contratos) queda afuera, igual que la documentación de proyectos de clientes con restricción | Filtro por nivel al ingerir; *default-deny* si falta el nivel | El documento no se indexa |
| 3 | Data contract | El productor garantiza el esquema y los metadatos ([fuente](../../material/conceptos/m1u3-data-contracts.md)); ver el YAML abajo | Validación automática en cada carga | La carga se rechaza y se avisa al dueño |
| 4 | Higiene | Escaneo de secretos; detección y seudonimización de datos personales en tickets; vencidos y duplicados afuera ([fuente](../../material/conceptos/m1u3-higiene-de-datos.md)) | Detector en el pipeline, con muestreo manual | Un secreto detectado bloquea la carga entera |
| 5 | Índice | Un índice por tenant (el interno es uno) con metadatos de vigencia, fuente, nivel y cliente, en cuenta y claves propias | Prueba de aislamiento entre tenants | Cruce de tenant: se bloquea el despliegue |
| 6 | Consulta | La pregunta pasa por el enmascarado de PII ([patrón](../../material/conceptos/m1u3-anonimizacion-inferencia.md)); el retrieval filtra por nivel y por los permisos de quien pregunta; el *working set* tiene presupuesto | Si no entra en el presupuesto, falla en voz alta en lugar de truncar | Se responde "no puedo con este contexto" |
| 7 | Gateway y modelo | Ruteo por nivel: Confidencial solo con proveedor bajo SSO y contrato sin entrenamiento; registro de costo por consulta | Telemetría del gateway | Sin proveedor habilitado para el nivel, no hay llamada |
| 8 | Respuesta | Cita la fuente; sin fuente, se abstiene. En nivel 2 (prepara, no ejecuta) una persona revisa antes de usar el borrador | Evals de cita y abstención (protocolo de abajo) | Respuesta sin cita: no se muestra |
| 9 | Trazas | Ids de documentos y de versión, no el contenido; no se persisten hasta que el Responsable de seguridad, consultando a Personas y a Legal externo, apruebe clasificación, ubicación y plazo de retención, antes del harness v1 ([R-13](07-resoluciones.md#gobierno-y-seguridad)); sin retención aprobada, el caso queda en evaluación offline | Auditoría de trazas | Contenido Restringido en una traza: incidente |
| 10 | Retroalimentación | Lo que el usuario marca como error, anonimizado, pasa al set de regresión de la próxima versión | Revisión humana antes de sumarlo | — |

```yaml
dataContractSpecification: 0.9.0
id: internal-knowledge-v1
models:
  document:
    fields:
      id: {type: string, unique: true}
      source: {type: string, enum: [docs, runbook, internal_ticket]}
      owner: {type: string, required: true}
      level: {type: string, enum: [public, internal, confidential]}
      client: {type: string, required: false}
      valid_until: {type: date, required: true}
      text: {type: string, minLength: 50}
```

El enum de `level` excluye Restringido. El YAML ilustra el esquema propuesto,
no un control implementado: un validador debe rechazar cargas incompatibles.
Clasificación, permisos, higiene y aislamiento requieren sus pruebas separadas.

**Protocolo de evaluación del caso.** Los umbrales son
**propuestos**, no medidos ([fuente](../../context/supuestos/umbrales-tecnicos-propuestos.md)):
se recalibran con la primera corrida de los meses 4-6 y cualquier cambio queda versionado.

| Elemento | Definición |
|---|---|
| Dataset v1 | ~200 preguntas sintéticas con la receta de datos sintéticos ([caso](../../material/conceptos/m1u3-caso-tickets-sinteticos.md)): data contract, 25 ejemplos reales anonimizados y revisados a mano como *few-shot*, generación y validación contra el contrato. Las respuestas esperadas las firma el dueño de cada fuente. Estratos: 50% respondibles con una fuente, 20% con varias, 15% sin respuesta (lo correcto es abstenerse) y 15% adversariales (instrucciones inyectadas en documentos, pedidos de datos Restringidos, preguntas sobre otro tenant) |
| Gate de rendimiento | Exactitud en respondibles ≥ 80%; cita correcta ≥ 90%; latencia p95 ≤ 10 s; costo por 1.000 consultas dentro del tope de FinOps |
| Gate de seguridad (duros) | Cero fugas de Restringido y cero cruces de tenant; cero inyecciones exitosas en el estrato adversarial; abstención correcta ≥ 80% en las preguntas sin respuesta |
| Gate ético | Rechaza el 100% de los pedidos de evaluar o decidir sobre personas; la exactitud de Operaciones no queda más de 10 puntos debajo de la de Tecnología |
| Gate de impacto | **Piloto de aprendizaje: no escala por valor demostrado** (el Anexo E no le asigna beneficio). Decide la *extensión* a Operaciones y a otras cohortes, por adopción y no daño. Pasa: en las últimas 4 semanas, uso semanal ≥ 40% de la cohorte y respuestas marcadas como erróneas ≤ 10% de las usadas. Espera: debajo, 6 semanas más en la cohorte actual con rediseño. Corta: sigue debajo al vencer, y el caso no se extiende (si pasa los gates duros, sigue en la cohorte). El tiempo de resolución de consultas internas se mide contra la base como aprendizaje, sin umbral. Umbrales recalibrables en la lectura del mes 6 con la medición en sombra |
| Revisión humana | Dos revisores en los desacuerdos. Un juez automático solo se usa si coincide ≥ 80% con los humanos en 50 casos. En producción, el primer mes se revisa por semana el 5% de las consultas (mínimo 20) |
| Versionado | La versión de release es la tupla: modelo y versión del proveedor, prompt y configuración, snapshot del índice, dataset de evals y código del harness ([fuente](../../material/conceptos/m2u4-versionado-release-gates.md)). Cualquier cambio de un elemento corre la suite en CI |
| Drift | Por semana: exactitud de la muestra revisada, tasa de abstención y documentos vencidos recuperados. Si el proveedor cambia de versión, se corre la suite completa antes de seguir. Alerta: caída de más de 5 puntos de exactitud o suba de más de 10 de abstención contra la versión aprobada |
| Rollback | El gateway fija la versión: volver a la tupla anterior en ≤ 1 día hábil. Una falla dura de seguridad apaga el caso el mismo día y se reporta según la política |
| Escalera | Nivel 0 (sin IA: solo evals, meses 4-6) → nivel 1 (asiste) en sombra con una cohorte de Tecnología (fin de los meses 4-6; la usa para informarse, sin reemplazar ningún canal) → nivel 2 (prepara, no ejecuta) para esa cohorte (inicio de los meses 7-9), si pasa rendimiento, seguridad y ético → extensión a Operaciones (meses 7-9), si además pasa impacto |
| Quién | El contractor arma la suite; los dueños de fuente etiquetan; el Responsable de seguridad aprueba los gates de seguridad y ético; el Responsable de Tecnología responde por el hito ([R-06](07-resoluciones.md#autoridad-y-liberaciones)) |

Si la lectura del mes 6 libera el producto, el piloto de producto usa el mismo protocolo con dos cambios: solo
datos sintéticos y un tenant por cliente. Las evals del caso interno no
certifican el piloto: permiten ensayar el método, cuya suficiencia debe
comprobarse también para el producto.

## Riesgos y mitigación

Probabilidad e impacto son juicio cualitativo (alta/media/baja), no medición.

**Alcance de las mitigaciones.** Las que dependen de gateway, harness central,
caso de referencia, piloto o contractor corresponden a la **alternativa ampliada**,
sujeta a liberación de plataforma y, para producto, otra decisión y costeo.

El mínimo no compra esas capacidades. Para los usos existentes exige los
controles aplicables y compensatorios probados de C descritos en «Paquete
técnico mínimo»; la ruta sin plataforma se detalla en «Bifurcación en el mes 3».

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| Migración del precio a consumo: el costo real es múltiplo de la suscripción | Alta | Alto | Gateway con ruteo por modelo, caché, presupuesto por equipo y escenario de consumo en Finanzas | El costo por persona activa supera el techo que fije Finanzas: se congela la expansión de seats |
| Código o datos de un cliente llegan a un modelo externo | Media | Muy alto | Exclusión por defecto (R-08), "Restringido" bloqueado en cada superficie y, con plataforma, en el gateway; enmascarado de PII; sin código ni datos de un cliente en pilotos | Un incidente confirmado: se suspende el caso y se reporta el mismo día (regla de la política) |
| Inyección indirecta en agentes con herramientas | Media | Alto | El dato no es una orden, permisos mínimos, salida de herramientas acotada, gate humano; red team antes de salir ([fuente](../../material/conceptos/m3u1-prompt-injection-jailbreaks.md)) | El red team vulnera el piloto y no hay mitigación verificable: no sale a producción |
| Capacidad crítica en pocas personas (arquitectura, seguridad, plataforma) | Alta | Alto | ADR, runbooks, par para cada hito, suplente por rol | Al cierre de los meses 4-6 un hito crítico sigue sin suplente: se baja el alcance del tramo siguiente |
| Sin holgura: el esfuerzo reasignado compite con horas facturables | Alta | Medio | Tope de reasignación, hitos chicos, prioridad a lo que baja costo operativo | Menos de la mitad del esfuerzo planificado se ejecuta dos tramos seguidos (supuesto) |
| No se puede reconstruir una decisión del sistema para el cliente regulado | Media | Alto | Trazas y registro por diseño, nivel de autonomía documentado | Si no se reconstruye una decisión desde las trazas, no pasa el gate de seguridad |
| El caso de producto depende de lo que el cliente permita | Alta | Medio | Matriz de restricciones primero; piloto en producto propio | Ningún cliente de la matriz habilita IA a fin de los meses 7-9: el frente producto queda en piloto propio |
| Con el producto diferido, el piloto arranca en los meses 7-9 sin preparación específica en los meses 4-6 | Alta, si la lectura del mes 6 libera el producto | Medio | La base de los meses 4-6 (gateway, harness v1, suite de evals, aislamiento) es reutilizable; lo propio del caso (dataset sintético, integración, diseño) se hace en las primeras 3-4 semanas de los meses 7-9. Las 6 semanas del SLO se cuentan desde que el piloto opera, así que el cierre del mes 12 decide con menos evidencia | El piloto no opera a la semana 6 de los meses 7-9: el cierre del mes 12 decide sin SLO medido, y el producto se corta o se pasa al año 2 |
| El contractor concentra evals, harness y la prueba de portabilidad | Media | Alto | Documentación mínima reproducible dentro de cada entregable (abajo), manuales y traspaso en los meses 7-12 ([Anexo D](04-personas-cultura.md)), suite y lote versionados en el repo | Un entregable de los meses 4-6 sin documentación mínima reproducible: no cuenta para la lectura del mes 6. Control en la semana 7 del tramo (abajo) |

**Documentación mínima reproducible (la que exige la lectura del mes 6).** Es
parte del esfuerzo de producir cada entregable: se imputa al 0,8 o al 0,2 que
lo produce, según el replan. Manuales de operación y traspaso se difieren a
los meses 7-12; no consumen otra vez las horas documentales de M4-M6
([supuesto conciliado](../../context/supuestos/umbrales-tecnicos-propuestos.md)).

| Elemento | Qué es | Horas (supuesto) | Quién, dentro de qué fracción |
|---|---|---|---|
| Alcance | Harness v1, suite de evals con dataset v1, evals en CI y lote de la prueba de portabilidad y costo: cuatro entregables | — | — |
| Contenido por entregable | (1) tupla de versión registrada (ver "Versionado"); (2) instrucciones de ejecución desde el repo; (3) ADR corto por decisión de diseño; (4) resultado de una corrida, con fecha | 1-2 días-persona por entregable: 4-8 en los meses 4-6; la carga se distribuye según quién produce cada uno | El contractor, dentro de la fracción con que produce el entregable (el 0,8; el 0,2 del replan para evals en CI y el lote): no suma |
| Prueba de reproducción | Otra persona corre cada entregable desde el repo y obtiene el mismo resultado | 0,5-1 día-persona por entregable: 2-4 en los meses 4-6 | DevOps/QA, dentro de su 0,8 del replan (no suma) |
| Control anticipado | Semana 7 del tramo de los meses 4-6: los entregables cerrados hasta ahí tienen su documentación mínima y pasaron la reproducción | — | El Responsable de Tecnología; si falta capacidad, pide al Directorio la excepción de 0,3 FTE antes de activarla ([R-17](07-resoluciones.md#arquitectura-y-medición)). Un entregable sin reproducción no cuenta en M6 |

## Decisiones

### Build, buy o partner por capacidad

Criterio: los cuatro ejes del marco construir, comprar o agentificar (costo total, tiempo hasta el primer valor,
capacidad interna, control) y el control como criterio legal
([fuente](../../material/conceptos/m1u2-build-buy-agentificar.md)). BAIC solo
plantea propietario frente a open source; el partner es criterio del plan
([fuente](../../material/frameworks/baic-perfiles-tecnologia.md)).

| Capacidad | Decisión | Por qué (ejes) | Alternativa descartada | Reversible |
|---|---|---|---|---|
| Modelos fundacionales | **Buy** vía API, ≥ 2 proveedores | Tiempo y capacidad: no se entrena | Entrenar o ajustar un modelo propio: sin datos de cliente utilizables | Sí |
| Gateway, ruteo y registro de costo | **Agentificar**: ensamblar sobre piezas abiertas, como hipótesis de diseño a comparar en M3 | Control de nivel de dato, cliente y costo en llamadas enrutadas; no cubre por sí solo IDE, chat ni suite | Configurar herramientas existentes o comprar plataforma: siguen abiertas hasta probar cobertura y TCO equivalentes | Sí |
| Agentes de código y asistentes internos | **Buy** la herramienta, **build** el contrato, skills y compuertas | Lo diferencial es el contrato de agente, no el producto | Atar el flujo a funciones exclusivas | Sí |
| Orquestación para casos del producto | **Agentificar**: framework y runtime abiertos (clasificación a reverificar) | Control y trazabilidad | Caja negra de un proveedor | Parcial |
| Retrieval y almacén vectorial | **Buy** gestionado sobre la nube existente | Tiempo y capacidad | Operar uno propio | Sí |
| Evals, trazas y observabilidad | **Buy** u open source; **build** los datasets de evals | Los datasets propios son el activo | Evals del proveedor | Sí |
| Enmascarado de PII y DLP | **Buy** u open source | Capacidad interna escasa | Desarrollo propio | Sí |
| Modelo en infraestructura propia (on-premise) | **Partner o diferir** hasta la decisión de los meses 10-12 | Hoy es una opción exploratoria de la propuesta al Directorio ([fuente](../../context/hechos/ia-en-producto-y-oferta.md)) | Comprometer hardware ya | **No** (capex) |
| Programa de partners del proveedor de modelos | **Seguir la aplicación sin ponerla en el camino crítico** | Exige certificaciones y despliegues productivos que aún no existen | Condicionar la arquitectura al programa | Sí |

### Comparación configurar / comprar / ensamblar en M3

La tabla de arriba expresa hipótesis de arquitectura objetivo, no una compra
adjudicada. Compará las tres alternativas con los mismos requisitos, población,
superficies, volumen, calidad y horizonte de 12 meses. Separá costos existentes
de incrementales; Finanzas completa montos de caja y tiempo, sin atribuir a una
alternativa controles o beneficios que no se probaron.

| Alternativa | Ventaja propuesta | Trabajo y residual a demostrar |
|---|---|---|
| Configurar las herramientas existentes | Ahorra integración nueva | Administración, permisos/MCP, exclusiones, escaneo local, exportación y revisión humana; comprobar capacidades del plan contratado y límites de cada superficie |
| Comprar una solución | Puede reducir operación propia | Probar cobertura efectiva y operación delegada; contar integración, licencias, soporte, límites contractuales, salida y dependencia del proveedor |
| Ensamblar sobre piezas abiertas | Adapta controles e integración | Más mantenimiento propio: upgrades, pruebas, incidentes, disponibilidad, seguridad y salida; probar portabilidad y capacidad operativa |

**Matriz a completar en M3.** Cada fila se desdobla por alternativa con la
misma prueba y criterio de aceptación; registrá resultado y evidencia, no solo
presencia de una función. Resultados y costos se producen en M1-M3 y se leen en
la decisión del mes 3: elige alternativa el Responsable de Tecnología, habilita
datos el Responsable de seguridad según la matriz contractual, acepta o
restringe el residual la autoridad de [R-10](07-resoluciones.md#gobierno-y-seguridad) y libera fondos el Directorio
([R-16](07-resoluciones.md#arquitectura-y-medición)). Sin matriz completa rige configurar lo existente sin caja nueva.

| Requisito | Superficie | Prueba | Residual | Alternativa | Costo |
|---|---|---|---|---|---|
| Datos y repositorios habilitados, secretos excluidos, autonomía y MCP acotados | Terminal/agente de código | Acción permitida; secreto sintético; permiso denegado; inyección indirecta; intento de bypass | Primera exposición, evasión y evidencia incompleta: el dueño del riesgo o el AI Council, según [R-10](07-resoluciones.md#gobierno-y-seguridad), aceptan o restringen el uso antes de habilitarlo | Configurar / comprar / ensamblar, por separado | Finanzas: caja, horas de configuración, prueba y operación |
| Restricciones de datos, acceso y retención | Chat/escritorio e IDE, cada uno separado | Verificar configuración del plan y repos/contenido permitido; dato sintético prohibido; bypass con cliente/cuenta alternativos | Sin bloqueo probado, no declarar cobertura; limitar o suspender uso afectado | Las mismas tres, sin atribuir cobertura al gateway | Finanzas: administración, eventual cambio de plan y compensatorios |
| Compartición, datos del dominio y auditoría | Correo/documentos/reuniones | Probar permisos, salida de dato sintético y evento auditable en entorno autorizado | Capacidad según edición y equipo, determinada en la prueba de M3; sin capacidad probada se restringe el uso; aceptar el residual no reemplaza el permiso contractual | Las mismas tres | Finanzas: licencias incrementales, administración y revisión |
| Medición reproducible y calidad | PR/CI/reversiones/tickets/incidentes y consolas de uso | Reejecutar extracción y tasas; probar maduración, faltantes y lectura simulada del gate | Cohorte o enlaces insuficientes impiden atribuir y pasar por valor | Las mismas tres con idéntico conjunto de indicadores | Finanzas: instrumentación, lectura y mantenimiento |
| Nivel de dato, aislamiento y trazabilidad, solo si se habilitan casos propios | Aplicaciones nuevas, por cliente | Probar denegación, trazas y cruces de tenant; calidad sobre el mismo lote | No se habilitan sin diseño y controles; sin casos propios no es requisito del paquete mínimo | Las mismas tres para ese alcance ampliado | Finanzas: desarrollo/integración, operación, salida y contingencia |

El TCO comparable incluye configuración/integración, prueba, licencias y
consumo, operación, mantenimiento de controles, respuesta a incidentes y
migración/salida, con iguales supuestos de volumen y reserva. Una oferta sin
cobertura equivalente debe declarar su brecha; una prohibición contractual se
cumple excluyendo el uso, no comprando más tecnología. El gateway no reemplaza
los controles de IDE, chat ni suite.

**Recomendación técnica:** elegir la respuesta mínima que pase las pruebas;
una alternativa gana solo con resultado probado. **Regla ratificada por el Directorio al
aprobar el plan ([R-15](07-resoluciones.md#arquitectura-y-medición)):** liberar plataforma en el mes 3, 6 o 9 exige
una señal y además cuatro condiciones: (1) brecha documentada, (2) alternativas
comparables, (3) economía incremental o aprendizaje con pérdida aceptada y
límite de pérdida declarado y (4) capacidad demostrada. Producen la evidencia el
Responsable de Tecnología (1, 2 y la parte técnica de 4), Personas (horas de 4)
y el CFO (3); el Responsable de seguridad verifica los controles de 1 y 4; el AI
Council dictamina. Solo el Directorio libera los fondos y acepta la pérdida de
aprendizaje.

Si no hay brecha incremental justificada, proponé diferir plataforma y
reevaluarla en M6/M9, con calendario y costo actualizados. Si falla un control
obligatorio, suspendé el uso afectado. No se traslada toda plataforma al año 2.

### Puertas de un solo sentido

Cada decisión se separa en aprobación interna, negociación no vinculante y
compromiso. Ninguna excepción contradice la regla del horizonte: **en los 12
meses ni código ni datos de un cliente salen hacia un modelo externo, salvo dentro
del entorno del propio cliente y con su permiso escrito**
([R-08](07-resoluciones.md#gobierno-y-seguridad)).

| Decisión | Tipo | Regla, fecha mínima y autoridad |
|---|---|---|
| Elegir modelo, vector store, herramienta de evals o prompts | Reversible | Cambiar detrás del gateway, con la suite de evals como árbitro. Decide el Responsable de Tecnología |
| Texto tipo de cláusula de IA (aviso BCRA, no entrenamiento, ubicación de datos) | Reversible | Aprobación interna en los meses 7-9 por el Responsable de seguridad; sin cliente |
| Conversar la cláusula con un cliente | Reversible | Desde los meses 7-9, **sin firma, sin datos y sin compromiso**; lo conduce comercial con Gobierno |
| Firmar un compromiso contractual de IA con un cliente | **Irreversible** | No antes del cierre del mes 12; decide el Directorio, con dictamen del AI Council ([R-32](07-resoluciones.md#roadmap-y-comercial)) |
| Enviar código o datos de un cliente a un modelo externo | **Irreversible** | Prohibido durante los 12 meses, salvo dentro del entorno del propio cliente y con su permiso escrito ([R-08](07-resoluciones.md#gobierno-y-seguridad)); pilotos con datos sintéticos o anonimizados. El uso que ya corre sigue [R-09](07-resoluciones.md#gobierno-y-seguridad): sobre código bajo NDA se suspende desde la aprobación (es Restringido); sin NDA, sigue como residual que acepta el AI Council hasta el gate del mes 3, con la matriz leída. Ampliar la regla (año 2) exige cláusula firmada y matriz completa |
| Ajustar un modelo con código o datos de un cliente | **Irreversible** | Fuera del horizonte del plan |
| Compra de hardware o compromiso de consumo mayor a 12 meses | **Irreversible** | No antes del cierre del mes 12; evaluar con el escenario de consumo; decide el Directorio ([R-32](07-resoluciones.md#roadmap-y-comercial)) |
| Subir un agente a nivel 3 (actúa con aprobación) en producto, o a nivel 4 (autónomo dentro de límites) fuera de sandbox | **Irreversible** | No antes del cierre del mes 12; un agente con efectos externos (por ejemplo, pagos) queda fuera del plan. Decide el Directorio, con dictamen del AI Council ([R-32](07-resoluciones.md#roadmap-y-comercial)) |

### Dependencia del proveedor y estrategia de salida

La telemetría ubica ~90% de los eventos en la terminal (Claude Code)
([fuente](../../context/hechos/uso-ia-interno.md)). Como señal
acotada, el 58% de la muestra autoseleccionada de 12 participantes del piloto
de abril de 2026 chocó con el límite del plan, y parte pidió consumo multimodelo
([fuente](../../context/hechos/encuesta-y-pilotos-ia.md)). Esa encuesta no representa
a toda la organización. Recomendación: **neutralidad al modelo** (supuesto
vigente) comprobada con un ensayo, no declarada.

1. Contrato de agente, skills y hooks sin funciones exclusivas de un proveedor.
2. Gateway con al menos dos proveedores operativos.
3. Prueba de portabilidad y costo en los meses 4-6 (ver Evidencia): el caso de referencia
   corre en dos modelos, se mide el esfuerzo de migrar en días-persona y, en la
   misma prueba, *fc* × *s*. Reemplaza el "costo moderado" supuesto por un dato.
4. Sin compromisos de volumen mayores a 12 meses antes de la decisión de los meses 10-12.

### Recurso de IA aplicada: los meses 1-3 y el contractor

**Referencia del paquete completo, sin autorización vigente.** Las vías y
fracciones siguientes no integran el mínimo de M1-M3 consolidado en E,
sección «Pedido inicial: paquete mínimo»; requieren una decisión nueva.

El esfuerzo técnico necesita una fracción de IA aplicada (evals, harness,
gateway): 0,3 FTE en el escenario recomendado de los meses 1-3 y 0,8 en los meses 4-12 (el 0,5 de los
meses 1-3 es el del escenario conservador, con contractor que complementa). El contractor al 50% **reemplaza** ese 0,3, no lo
complementa, y le queda 0,2 que asigna el [Anexo D](04-personas-cultura.md).
Lo que sigue abierto es la vía de los meses 1-3:

| Vía de los meses 1-3 | FTE clave de este anexo en los meses 1-3 | Caja | Condición |
|---|---|---|---|
| Contractor al 50% desde el mes 1 (base del paquete completo) | 0,6 (arquitecto y DevOps/QA) | Contractor de los meses 1-3 ([Anexo D](04-personas-cultura.md)) | Requeriría nueva aprobación del Directorio, por la restricción de no contratar |
| Rol interno de Tecnología, 0,3 FTE | 0,9 | Ninguna | Antes de aprobar esta alternativa, el Responsable de Tecnología demuestra por rol experiencia en evals y harness. Usar agentes de código (~7 de 10, [fuente](../../context/hechos/uso-ia-interno.md)) no lo prueba (supuesto) |

El paquete completo adoptaba el contractor desde el mes 1 como base porque el recurso que no entra es el tiempo de
las personas clave, no la caja (Anexo E, "Contra el sobre de tiempo: los meses 1-3 entran; los meses 4-6, con el replan"). Si al evaluar esa ampliación no se aprueba
ninguna de las dos vías, el gateway y las evals pasan a los meses 4-6 y los meses 1-3 quedan en
revisión del inventario de datos existente, línea base y matriz de superficies.

Para los meses 4-12, sin el frente producto (los desarrolladores senior son del producto, ver
"Insumos para Finanzas"), quedan dos alternativas. La de sumar el contractor a
la fracción interna se descartó: pagaba dos veces la misma capacidad, y el Anexo E ya
consolida el contractor como reemplazo.

| Alternativa | Caja | Tiempo interno de la base (meses 4-6 / 7-9 / 10-12) | Comentario |
|---|---|---|---|
| El contractor reemplaza la fracción interna (**recomendada**) | Contractor ([Anexo D](04-personas-cultura.md)) | 1,2 / 1,5 / 1,4 FTE, con el replan de los meses 4-6 | La más barata en tiempo; concentra el conocimiento en una persona externa, así que exige documentación y traspaso |
| Sin contractor, con fracción interna de 0,8 FTE | Ninguna | 2,3 / 2,3 / 2,2 FTE, **solo de este anexo** | Respeta la restricción literal, pero no entra en el sobre: suma 0,8 FTE clave por tramo sobre un plan que ya está en 2,2-2,5. Sin el contractor tampoco existe el replan de los meses 4-6 |

### Exceso de los meses 4-6 con el producto diferido

Con el producto diferido, los meses 4-6 piden 2,5 FTE clave contra un máximo de 2,25
([Anexo E](05-business-case.md)). De esos 2,5, 1,5 son de este anexo (0,5
arquitecto y 1,0 DevOps/QA) y 1,0 de los Anexos C y D. Se miró qué hace cada
fracción en ese tramo y qué condición de la lectura del mes 6 sostiene: bypass, red team interno,
portabilidad y FinOps.

| Salida | Qué cambia | FTE clave de los meses 4-6 | Costo | Qué arriesga |
|---|---|---|---|---|
| **Replan del Anexo B (recomendada)** | Arquitecto 0,5 → 0,4: el 0,1 era el diseño del piloto de producto, que con el producto diferido pasa a los meses 7-9. DevOps/QA 1,0 → 0,8: el pipeline de evals en CI y la reejecución de la prueba de portabilidad pasan al contractor; se propone asignarles 0,2 FTE además del 0,8 de IA aplicada, sujeto a contrato y disponibilidad (Anexo D) | 2,225 contra el techo supuesto de 2,25: margen aritmético de 0,025 FTE / 12 h, sin capacidad demostrada | Baja el tiempo de los meses 4-6 en ~5k USD (3,2-7,5k USD) y no suma caja | Más concentración en el contractor (ver Riesgos). El piloto, si la lectura del mes 6 lo libera, arranca sin diseño previo. Las condiciones de la lectura del mes 6 no se tocan: bypass, gateway y FinOps quedan en DevOps/QA |
| Excepción acotada del paquete completo | El Directorio debería aprobar 0,3 FTE clave por encima del sobre en los meses 4-6, en una decisión nueva | ~2,5 | Tiempo valorizado de ~3-7k USD ya contemplado en el paquete completo; el trabajo facturable desplazado se confirma por agenda y contrato | Rompe el sobre que ese paquete pide confirmar. Cubre solo la falta del 0,2 adicional; sin contractor no alcanza (ver la tabla de contingencias abajo y [Anexo E](05-business-case.md), "Dos contingencias del contractor") |
| Descartada: correr hitos de los meses 4-6 a los meses 7-9 | Portabilidad o FinOps pasan a los meses 7-9 | 2,2 | — | La lectura del mes 6 queda sin dos de sus condiciones, y los meses 7-9 no tienen holgura (0,05) |

**Recomendación para el paquete completo:** el replan, sujeto a una decisión
nueva con alcance, calendario y costeo. Este anexo no da el exceso por resuelto hasta esa
decisión. La excepción acotada cubre **una sola** contingencia, y no hay que confundirla
con la otra:

La cuenta conciliada del [Anexo E](05-business-case.md), «Conciliación de los
meses 4-6», suma 576 + 216 + 96 + 180 = **1.068 h**; divididas por 480 dan
**2,225 FTE**, no 2,2 exactos. El techo equivale a 1.080 h: quedan **12 h**.
El redondeo de presentación no demuestra capacidad por rol o semana.

| Contingencia | Qué falta | Meses 4-6, solo este anexo | Respuesta de este anexo |
|---|---|---|---|
| Sin el 0,2 | El contractor existe, pero su 0,2 no está libre (alcance no acordado, o documentación atrasada, [Anexo D](04-personas-cultura.md)) | 1,5 FTE (sin replan) | La excepción acotada: los 0,3 llevan los meses 4-6 a 2,5 y lo cubren |
| Sin contractor | Toda la IA aplicada de los meses 4-12 (0,8 FTE), no solo el 0,2 | 2,3 FTE con la fracción interna (la alternativa sin contractor); 1,2 en modo control | La excepción de 0,3 **no alcanza** para la alternativa sin contractor. La contratación es condición de inicio de los hitos de IA aplicada: sin contractor ni rol interno demostrado, no inician el harness v1, la suite de evals en CI ni la prueba de portabilidad y costo. El **modo control** (gateway en laboratorio, bypass por superficie, FinOps) requiere autorización propia de alcance, capacidad y presupuesto: 1,2 FTE de B, arquitecto 0,4 y DevOps/QA 0,8. No incluye el 0,2 de evals en CI y reejecución ni las otras funciones del programa. La lectura del mes 6 decide sin cobertura de precio y sin caso de referencia en sombra. Su reprogramación requiere aprobación. Con suscripción que permite gateway o pago por consumo se mantiene el renglón de infraestructura; si la suscripción no permite gateway, solo se ensaya tráfico sintético y se propone 0,5-1,5k USD en el tramo, sujeto a recosteo |

Con la fracción interna de la alternativa sin contractor, el plan completo pediría ~3,3 / 3,0 / 2,9 FTE clave
en los meses 4-6 / 7-9 / 10-12 ([Anexo E](05-business-case.md), "Dos contingencias del contractor");
este anexo aporta 2,3 / 2,3 / 2,2 y no adopta un total propio. En modo control,
los meses 7-12 mantienen la base (1,5 / 1,4 FTE) sin caso de referencia ni evals, y el
gateway opera para control y telemetría sin ruteo a modelos más baratos ni
caché. La alternativa sin contractor queda como opción del Directorio solo si aprueba
explícitamente el exceso que calcula el Anexo E.

### Tensiones con otras miradas (abiertas, sin consenso inventado)

| Tensión | Una mirada | La otra | Qué resuelve |
|---|---|---|---|
| Costo | La meta de +20% de throughput depende de agentes cuyo consumo real es 12× lo pagado | El borrador de OKR pide gasto de tecnología < 3,5% de la facturación, y hoy es ~4% | Finanzas: si el precio migra a consumo, el ahorro de horas se come en tokens; hay que mostrar el neto |
| Gobierno | La política está aprobada según confirmación del responsable del caso; falta validar su aplicación y el estado de la matriz de restricciones por cliente ([fuente](../../context/hechos/gobierno-y-politica-ia.md)) | El ruteo por clasificación y el piloto de producto dependen de ambas | Resuelto en [R-07](07-resoluciones.md#gobierno-y-seguridad) y [R-09](07-resoluciones.md#gobierno-y-seguridad): constancia de la política en la preparación, aplicación verificada en el mes 3 y matriz de clientes al cierre de M1-M3 |
| Personas | Reasignar 10-15% del tiempo de pocas personas clave | Utilización 83-90% y bench < 1 FTE; restricción de no contratar | Personas: suplentes y capacidad; el especialista de IA se capacita, se reasigna o se contrata por contrato |
| Alcance | La plataforma sirve a dos frentes | Qué caso concreto va en el producto lo define el portfolio | CAIO: este anexo no elige el caso |
| Precio | El gateway podría cubrir un cambio de precio a consumo | La cobertura no está medida: depende de *fc* × *s*, de la suscripción y de la calidad, y solo existe en la rama con plataforma | Resuelto: el deck no afirma la palanca; se afirma solo si pasa la prueba de portabilidad y costo de los meses 4-6 |
| Capacidad | El paquete completo pedía 1,6 FTE clave y 590 h distribuidas; el mínimo vigente se consolida en el [Anexo E](05-business-case.md), sección «Pedido inicial: paquete mínimo» | En el paquete completo, con el producto diferido, los meses 4-6 exceden el sobre en ~0,3 FTE; sin contractor, pediría ~3,3 FTE clave (Anexo E) | El mínimo no aprueba el replan ni la excepción del paquete completo; una ampliación exige nuevo alcance, calendario y costeo (ver «Exceso de los meses 4-6 con el producto diferido») |

## Roadmap técnico a 12 meses

Los tramos son los de tres meses de la convención del plan: meses 1-3 (enero-marzo
de 2027), 4-6, 7-9 y 10-12; las decisiones de los meses 3, 6, 9 y 12 cierran cada
tramo. Los meses 1-3 absorben la fase de diagnóstico de los primeros 100
días ([fuente](../../material/conceptos/m1u2-plan-100-dias.md)). El Responsable de
Tecnología responde por todos los hitos técnicos ([R-06](07-resoluciones.md#autoridad-y-liberaciones)). Los criterios de abandono siguen el patrón
kill/scale ([fuente](../../material/conceptos/m1u2-kill-scale-gates.md)).
**Primero se solicita autorizar la validación previa; M1-M3 requiere una segunda
liberación condicionada**. Las filas de los meses 4-12 son la secuencia prevista
y se liberan decisión por decisión.

**Cada mes** el AI Council hace su revisión mensual con el tablero ([Anexo C](03-gobierno-seguridad.md),
"Ritmo operativo"): esa revisión puede frenar o cortar un frente, pero no libera
fondos, que quedan en las decisiones de los meses 3, 6, 9 y 12. Este anexo aporta al
tablero el reporte mensual de FinOps con el escenario de consumo y la telemetría
unificada; no suma salidas ni costo nuevos.

### Paquete técnico mínimo de los meses 1-3, para costear

**Alcance propuesto:** configurar las herramientas ya contratadas
y medir prácticas sobre repositorios propios habilitados, con controles
equivalentes para ese uso. No incluye gateway, harness central, retrieval,
casos propios nuevos ni piloto de producto. El valor que se intenta medir es
el de las prácticas de uso y revisión del agente existente, no el de plataforma.

Configurá permisos, autonomía con aprobación humana, MCP aprobados, escaneo
local y en repositorio, repositorios/contenido permitido y administración de
acceso, datos y retención de chat, IDE y suite, según lo que admita cada plan.
Probá acción permitida, dato sintético prohibido y bypass en cada superficie
que se habilite; para el agente, agregá inyección indirecta y revisión de sus
acciones. Cerrá críticos y registrá aceptación del residual según el Anexo C.
Sin capacidad técnica o permiso contractual, restringí o suspendé el uso
afectado; una encuesta no lo convierte en control probado.

Exportá uso de las consolas existentes (terminal, chat, IDE y Workspace) y
PR/CI/reversiones/tickets/incidentes a extractos y scripts versionados, en
agregados por área y semana: ningún evento por persona se extrae ni se retiene
([R-13](07-resoluciones.md#gobierno-y-seguridad)). El acceso al origen es de solo lectura;
persistir los extractos requiere la aprobación previa del Responsable de seguridad sobre
clasificación, ubicación, permisos y retención indicada en el acta de viabilidad.
Verificá almacenamiento autorizado con acceso limitado, sin guardar prompts
ni secretos; no se presume disponible. Conciliá uso por superficie,
seats y personas activas por área con resultados; si no hay exportación, reportá uso
estimado aparte. Eso permite un tablero periódico sin servicio central nuevo.

Entregables: revisión y ampliación del inventario de datos existente para las
fuentes elegibles, con brechas y requisitos para futuros contratos de datos;
matriz de controles, acta de viabilidad reproducible,
base congelada, registro de cambios de prácticas, lecturas de uso y calidad y
comparación de alternativas en M3. El acta se produce en la preparación previa,
se verifica antes de M1 y se actualiza si cambian las fuentes o el método.
Aplicá los controles obligatorios antes de
medir la base y documentalos como punto de partida; formación y prácticas
nuevas empiezan después del congelamiento. M1-M3 no promete ganancia atribuida.

**Horas-persona estimadas para todo M1-M3**, incluida la preparación técnica
previa, como supuesto de planificación de este anexo, no capacidad confirmada:

| Rol propuesto | Horas | Trabajo incluido y supuesto |
|---|---|---|
| Arquitectura / tech lead | 24-40 | Alcance, fuentes, protocolo, diseño de pruebas, relevamiento técnico de capacidades ([R-16](07-resoluciones.md#arquitectura-y-medición)) y comparación M3; incluye 4-8 h previas de viabilidad |
| DevOps / administración de herramientas | 32-56 | Configuración de las cuatro superficies, exportaciones y pruebas; acceso administrativo y funciones del plan disponibles |
| QA / análisis de datos | 40-64 | Extracción, diccionario/enlaces, base, maduración y lectura reproducible; incluye 8-16 h previas; fuentes exportables sin saneamiento masivo |
| IA aplicada | 8-16 | Revisar contrato/skills y ensayos del agente; capacidad demostrada interna o servicio acotado, sin suponer contractor dedicado |
| Seguridad, aporte técnico compartido con C | 24-40 | Revisión de clasificación y verificación independiente de pruebas negativas/bypass, red team acotado y residual; persona distinta de DevOps/QA productor. No incluye política, legal ni operación completa de gobierno; reutilización sujeta a confirmar alcance |
| Senior / champion de la cohorte, compartido con D | 16-24 | Validar tareas, revisión humana y registro de prácticas; no incluye formación general ni todas las horas de los participantes |

Total técnico: **144-240 h**; de ellas, **104-176 h** son los cuatro primeros
roles y **40-64 h** son aportes compartidos con C/D. Finanzas, Gobierno y
Personas concilian actividades antes de sumar: una hora compartida se cuenta
una sola vez. No se suman estas horas a las fracciones del paquete completo.

**Conciliación del mínimo ([R-26](07-resoluciones.md#finanzas)).** Configuración, prueba y primera
corrección de DevOps coinciden con C y se cuentan en la unión de 40-64 h del
Anexo E, que es tope también para las exportaciones de consolas: un límite de
alcance, no un ahorro. Durante la validación, el Responsable de Tecnología
desagrega la fila; si las exportaciones no caben en el tope, el uso de consolas
se reporta estimado en lugar de sumar horas y, si aun así no cabe, el CFO
recostea antes de M1 dentro de 71 y firma el CEO. El techo de 59 no sube.

La revisión senior de 16-24 h está dentro de las 64 h de soporte de prueba del
Anexo E: son las mismas personas y tareas, con agenda que incluye la validación
anterior al congelamiento (semanas 1-4), no solo las semanas 5-13.

La extracción y reproducción de 8-16 h de D están dentro de QA de B: comparten
indicador, corte, fuentes y entregable. La reproducción la hace otro operador;
compartir presupuesto no permite verificar el trabajo propio.

Supuestos: una cohorte propia de 15-20 personas, cuatro superficies existentes,
una ronda de configuración y corrección de hallazgos, fuentes accesibles y
sin conectores nuevos. No incluye formación, horas de prueba de toda la
cohorte, gobierno/legal, descubrimiento de producto ni operación M4-M12;
los otros dueños deben agregarlos al paquete completo. Toda caja incremental,
cambio de plan o nueva licencia queda por cotizar por Finanzas, sin asumir cero.

**Éxito:** otro operador reproduce los indicadores y cada uso habilitado tiene
controles probados y residual aceptado antes de extender la prueba. Responsable:
el Responsable de Tecnología ([R-06](07-resoluciones.md#autoridad-y-liberaciones)). **Abandono/revisión:** sin datos, horas liberadas o controles,
reducí/diferí y volvé a costear; si hacen falta saneamiento, conectores o más rondas,
el rango deja de ser válido. No se presume que la plataforma resuelva esa falta.

### Candidato de quick win operativo

**Candidato, no aprobado por la empresa ni resultado observado.** Se propone
concretar una tarea de la prueba operativa ya costeada; no crear otro proyecto.
No consta todavía un error elegible, un usuario que lo priorice ni agenda liberada.

**Priorización propuesta.** Primero, una corrección pequeña que quite un bloqueo
real al equipo usuario de una función interna ya utilizada. Se prefiere a una
demostración aislada porque puede entrar al flujo de trabajo habitual sin
plataforma ni conectores nuevos. Factibilidad alta solo si hay código propio
habilitado, error reproducible, pruebas existentes y revisor disponible; impacto
local visible por validar con ese usuario, sin asignarle un retorno económico.

La cursada aporta dos lecturas: el material ubica los *quick wins tácticos* en
factibilidad alta e impacto bajo; el apunte usa impacto visible alto y baja
complejidad. Ambas exigen una intervención útil y acotada; no se fuerza un
cuadrante único ni se convierte el diagnóstico en un quick win.[^quick-win-ficha][^quick-win-apunte]

| Campo | Propuesta y condición |
|---|---|
| Usuario y tarea | Un equipo interno con un error pendiente real de su backlog. Su referente define antes el comportamiento esperado; un integrante de la cohorte usa el agente actual para preparar la corrección y las pruebas de regresión, con datos sintéticos o autorizados y sin código de clientes |
| Prerrequisitos | Base congelada, superficie habilitada con controles probados y residual aceptado; quien realiza la tarea ya aprobó la formación aplicable y su revisión práctica. Básico, intermedio y prueba pueden empezar juntos según D; eso no autoriza intervenir antes de aprobar lo aplicable |
| Resultado útil | La función vuelve a cumplir el comportamiento acordado en su flujo real. Otro revisor acepta el cambio, CI pasa y el usuario confirma que resolvió el error; se integra por el proceso habitual de PR. Un borrador o una prueba en sandbox no cuentan como resultado integrado; no se garantiza despliegue |
| Ventana condicionada | Camino con base hasta semana 8: usar la ventana restante de M3, semanas 9-13, después de aprobar la formación aplicable y verificar los controles. No se promete que formación, tarea e integración entren en esa ventana; si no caben, no se anticipa la intervención ni se recorta la formación |
| Capacidad y costo | Sustituye una tarea dentro de la prueba, sin sumar horas, licencias ni partidas. Diseño y soporte ya previstos en el mínimo; los 16-24 h de revisión de B están dentro de las 64 h de seniors de E. Tecnología confirma encaje con Personas y Finanzas antes de elegir la tarea; no se presume holgura |
| Éxito observable | Prueba de regresión que falla con el defecto y pasa con la corrección, revisión independiente, CI aprobado, aceptación del usuario e integración y uso real comprobados. La evidencia queda en los sistemas autorizados; al seguimiento del plan llegan agregados por área y semana, sin métricas individuales |
| Corte o diferimiento | Sin tarea útil elegible, formación aprobada, permisos, revisor, agenda o integración viable en esa ventana: retirar el candidato de M3. Sin aceptación o con falla de calidad/seguridad, no integrar y aplicar las reglas vigentes. Puede reevaluarse en M4 solo si se autoriza la continuidad y cabe en su capacidad; no se financia automáticamente |

**Responsable:** Responsable de Tecnología, con el referente usuario y un revisor
distinto del autor; las personas se nombran conforme a R-06. La observación de
calidad a 30 días sigue el protocolo existente: el resultado local no demuestra
ausencia de daño, mejora atribuible ni ROI. M6 no lee valor y M9 conserva el
[gate vigente](#gate-de-valor-fijado-por-este-anexo-el-anexo-f-lo-adopta).

Respaldo de capacidad: [mínimo, actividades ya incluidas](../../context/supuestos/paquete-minimo-de-aprendizaje.md#alcance-y-conciliación-m1-m3)
y [Anexo E, pedido inicial](05-business-case.md#pedido-inicial-paquete-mínimo).

[^quick-win-ficha]: [Matriz factibilidad-impacto y quick wins](../../material/conceptos/m1u2-matriz-factibilidad-impacto.md).
[^quick-win-apunte]: [Apunte de clase del 18/08/2026, quick wins y priorización](../../material/apuntes/2026-08-18-portfolio-100-dias.md).

### Pedido vigente (parte técnica)

El pedido vigente es el mínimo técnico de M1-M3 de arriba, consolidado con C/D
en el [Anexo E](05-business-case.md), sección «Pedido inicial: paquete mínimo».
Su ejecución requiere una segunda autorización; la primera cubre la validación
inicial de [la fuente del mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial).
Al aprobar el plan, el Directorio elige este paquete ([R-01](07-resoluciones.md#autoridad-y-liberaciones)) y libera la
validación inicial ([R-02](07-resoluciones.md#autoridad-y-liberaciones)); la disponibilidad de agendas se confirma en esa ventana.

La preparación existente de B/D conserva **20-40 h**: tech lead **4-8 h** de viabilidad
de B, tech lead **8-16 h** de preparación de facilitación de D y QA **8-16 h** de B.
El trabajo estrictamente técnico de B suma **12-24 h**; las otras **8-16 h**
preparan la formación. Las horas de managers no están en esas filas de B.
Son horas ya incluidas en B/D y extraídas de M1-M3 en E, no un adicional.
La validación organizativa agrega **60-96 h** separadas. En conjunto, la primera
liberación propone **80-136 h**, techo de **8k USD de tiempo** y **caja 0**.

Esa ventana de **10 días hábiles** comienza después de la autorización específica
y de confirmar agenda, fuentes, trabajo desplazado e imputación 2026.
El trabajo técnico lee las fuentes corporativas autorizadas sin modificarlas
y reproduce los indicadores. La persistencia de registros extraídos es una
escritura separada, sujeta a la aprobación previa del Responsable de seguridad descrita en el
acta de viabilidad; sin ella no se persisten extractos. No incluye instrumentación
nueva, despliegues, herramientas ni contratos nuevos. No consta ejecución previa.

El acta técnica tiene productor, verificador y ratificador distintos ([R-14](07-resoluciones.md#arquitectura-y-medición)):
la produce QA bajo el Responsable de Tecnología, la verifica el verificador senior
independiente con la fila de 8-16 h de D y el AI Council ratifica el método.
Esa revisión no se cuenta dentro de las 12-24 h productoras de B.

Antes de M1, la segunda liberación, que firma el CEO por delegación del Directorio
([R-04](07-resoluciones.md#autoridad-y-liberaciones), [R-05](07-resoluciones.md#autoridad-y-liberaciones)), exige diagnóstico, matriz de capacidad,
roles nombrados, viabilidad de medición, recosteo y presupuesto 2027
aprobados según E y [Anexo F](06-roadmap-riesgo.md). Libera hasta **71k USD**
restantes: límite acumulado **79k USD**, de los cuales **10k USD son caja** y
**69k USD son tiempo**. No habilita prácticas automáticamente: cada uso requiere
dictamen y restricciones aplicables, controles probados, verificación
independiente y aceptación del residual, además de base congelada.

No se aprueban el contractor ni la excepción de 0,3 FTE del paquete completo;
una ampliación exige nuevo alcance, calendario y costeo.

La tabla siguiente conserva la referencia del paquete completo para Finanzas.
Sus FTE, caja, entregables y condiciones no son el pedido vigente del mínimo.

| Elemento | Qué se pedía en el paquete completo |
|---|---|
| Qué se proponía autorizar | Los hitos de los meses 1-3, en su versión acotada (el escenario recomendado, abajo), más la prueba chica de los meses 1-3 ([Anexo E](05-business-case.md)). La plataforma de los meses 4-6 solo se libera con señal y decisión propia ("Bifurcación en el mes 3") |
| Capacidad máxima de este anexo | 0,6 FTE clave con el contractor desde el mes 1 (0,9 con el rol interno), más 16-24 h de lectura de DevOps/QA de la prueba chica. El sobre del plan completo y su piso (1,6 FTE clave; techo de tiempo 62k USD, o 72k USD con la prueba) los cierra el [Anexo E](05-business-case.md) |
| Caja de este anexo | Infraestructura de telemetría y registro, 0,5-1,5k USD en el tramo de tres meses; el tope total de los meses 1-3 lo fija el Anexo E |
| Entregables | Revisión y ampliación del inventario de datos existente, línea base congelada, matriz superficie→control→telemetría, telemetría unificada, matriz de restricciones por cliente |
| Decisiones delegadas | Elegir herramientas y proveedores detrás del gateway (reversible), al Responsable de Tecnología |
| Condiciones de aprobación del paquete completo | Vía de IA aplicada aprobada (contractor desde el mes 1, o rol interno demostrado); disponibilidad de historial de PR, integración continua y tickets para la línea base; salida para el exceso de los meses 4-6 (replan del Anexo B o excepción) |
| Fuera del pedido | Los meses 4-12 (incluida la plataforma de los meses 4-6, que el Directorio libera solo con señal y las cuatro condiciones de [R-15](07-resoluciones.md#arquitectura-y-medición)), el modelo propio, cualquier compromiso mayor a 12 meses y todo compromiso contractual con clientes |

**Escenario conservador y escenario recomendado.** El conservador pone el gateway en laboratorio con dos proveedores en el
primer tramo; el recomendado lo difiere al inicio de los meses 4-6 y conserva
revisión del inventario de datos existente, línea base, matriz de superficies y telemetría. El
[Anexo F](06-roadmap-riesgo.md) ya ubica el gateway en los meses 4-6. Con la misma provisión
de IA aplicada (los otros anexos suman 1,0 FTE clave en los meses 1-3, [Anexo E](05-business-case.md)),
el conservador pide +0,2 FTE clave con el contractor desde el mes 1 (0,8 contra 0,6) y +0,4 con el rol
interno (1,3 contra 0,9), más 1-3k USD de caja de infraestructura. Con el
contractor y en la lectura separada del Anexo E, el conservador entra en el máximo de 2,25; en la
lectura estricta no entra ninguno (3,0 contra 2,8 del primer tramo acotado). Lo descartan la
atribución (base congelada en las semanas 1-4 y rampa 0% en los meses 1-3) y que el gateway
en laboratorio no produce valor medido sin harness ni evals, que son de los meses 4-6. Que
su caja entre en el techo de los meses 1-3 lo verifica el Anexo E.

### Calendario de prerrequisitos (preparación previa y meses 1-3)

La propuesta articula preparación y ejecución mediante las dos autorizaciones
del Anexo E y los gates del Anexo F:

| Cuándo | Qué | Costo |
|---|---|---|
| Tras la primera autorización específica, preparación de octubre-diciembre de 2026, dentro de la ventana propuesta de 10 días hábiles | Verificar historial utilizable de PR, integración continua, incidentes y tickets de los últimos dos trimestres; producir el acta de viabilidad y el protocolo retrospectivo reproducible, con **serie retrospectiva** para estimar tendencia y ruido. Lectura sobre datos corporativos autorizados, en agregados por área y semana, sin instrumentación nueva; antes de extraer cualquier serie, el Responsable de seguridad aprueba y comunica el tratamiento ([R-13](07-resoluciones.md#gobierno-y-seguridad)). Verificar resultados antes de la segunda liberación; agenda e imputación 2026 confirmadas antes de trabajar | Preparación existente de B/D de 20-40 h (12-24 técnicas y 8-16 de facilitación), sin duplicación; junto con 60-96 h organizativas nuevas, techo conjunto de 8k USD de tiempo y caja 0, consolidado en E |
| Semanas 1-4 del plan, después de la segunda autorización | **Base prospectiva congelada**, con la unidad de la sección "Throughput", antes de cualquier formación, prueba de prácticas o herramienta nueva; controles obligatorios previos documentados como punto de partida. Si la base se extiende a semana 8, también se desplazan básico, prueba e intermedio | Incluida en QA / análisis de datos del mínimo de arriba, consolidado en E, sección «Pedido inicial: paquete mínimo»; los 3-5 días-persona de DevOps/QA eran referencia del paquete completo |
| Semanas 5-13 del plan | Matriz de superficies, prueba de controles de cada superficie en uso y telemetría unificada; medición contra la base, con control concurrente donde exista. **La ganancia no se atribuye antes de los meses 4-6** (la rampa base es 0% en los meses 1-3) | Dentro del esfuerzo de los meses 1-3 |

La serie retrospectiva y la base prospectiva no se mezclan: la primera estima
ruido, la segunda es el punto de partida. El respaldo es el del protocolo
("Respaldo"): la retrospectiva nunca atribuye ganancia. Si el historial no
alcanza, la ganancia tampoco se atribuye (ver el hito de línea base).

**Calendario si la base llega a semana 8 (camino esperado con los valores
ilustrativos, ver «Gate de valor»).** Quedan cinco semanas
(9-13) para formación y prueba. Los PR necesitan 14 días de maduración y las
tasas de calidad, 30: la lectura de M3 tendrá menos actividad madura que con inicio en semana 5.

En ese caso, la lectura del mes 3 es reducida y declarada (unas 3 semanas de PR
maduros): informa uso, retrabajo y PR maduros sin atribuir ganancia, y no se
corre ni atrasa M4. La presenta el CAIO, la verifica el CFO y el CEO firma el
gate; la lectura de valor queda en el mes 9 ([R-19](07-resoluciones.md#arquitectura-y-medición)
y [R-27](07-resoluciones.md#finanzas)). No se adelanta
tratamiento dentro de la base.

La columna "Frente" usa los nombres del [Anexo E](05-business-case.md): **Base**
común, frente **Interno** y frente **Producto** (solo si la lectura del mes 6 lo libera).
Los hitos de los meses 1-3 corren en las dos ramas. Los de los meses 4-12 son la **rama con
señal** (señal en el mes 3); la rama sin señal está en "Bifurcación en el mes 3", después de la tabla.

| Tramo | Frente | Hito | Criterio de éxito | Condición de abandono |
|---|---|---|---|---|
| Meses 1-3 | Base | Revisar cobertura y vigencia del inventario de datos existente y ampliarlo para las fuentes elegibles | Toda fuente elegible del caso de referencia tiene dueño, calidad y nivel revisados; brechas y requisitos para futuros contratos de datos documentados | Sin dueño para una fuente: queda fuera de los casos |
| Meses 1-3 | Interno | Base prospectiva de throughput, incidentes y retrabajo congelada en las semanas 1-4 (serie retrospectiva de la preparación previa para estimar ruido) | Unidad, cohorte y fórmula de la sección "Throughput"; numerador y denominador; versión congelada con fecha | Sin historial utilizable de al menos dos trimestres: la ganancia no se atribuye y se elimina el resultado clave (regla del OKR) |
| Meses 1-3 | Base | Matriz superficie→control→telemetría y denominador de la cobertura | Las cuatro superficies con ruta, control y telemetría declarados; denominador armado con datos de administración | Sin telemetría posible, se declara no medible; no se elimina del denominador de cobertura de control ni se declara cubierta sin prueba |
| Meses 1-3 | Base | Prueba de controles de cada superficie en uso: positiva, negativa y bypass ([R-11](07-resoluciones.md#gobierno-y-seguridad)) | Cobertura de control = 100% de las superficies en uso, con críticos cerrados y residual aceptado | Superficie cuya prueba no cabe en las horas validadas o no pasa: no se usa hasta M4-M6 y se lleva al Council |
| Meses 1-3 | Interno | Telemetría unificada de terminal, chat, IDE y Workspace | Personas activas y uso por superficie y por resultado, en agregados por área y semana ([R-13](07-resoluciones.md#gobierno-y-seguridad)) | Sin exportación del proveedor: encuesta cada tres meses, marcada como estimada |
| Meses 1-3 | Producto | Matriz de restricciones contractuales por cliente (con comercial y Gobierno) | Cobertura de los clientes que concentran la facturación | Sin matriz, no hay piloto de producto |
| Meses 4-6 | Base | Gateway en laboratorio con 2 proveedores y registro de costo | Tráfico del caso de referencia registrado por llamada, nivel y centro de costo | Más de un tramo sin operar: se reevalúan configurar, comprar o ensamblar con la matriz de decisión de M3; no habilita una compra automática |
| Meses 4-6 | Base | Prueba de ruteo por la pasarela, por superficie enrutable (solo rama con plataforma) | Las pruebas de controles repetidas con la pasarela; casos propios 100% por gateway; agente de código ≥ 90% por gateway solo con la suscripción que permite gateway y con el pago por consumo (ver "Política de ruteo"); con la suscripción que no lo permite, ruteo ensayado y no activado | Superficie con bypass sin control compensatorio: queda declarada no cubierta y se lleva al Council |
| Meses 4-6 | Base | Harness v1 sobre el caso de referencia: working set con presupuesto, memoria externa, gate humano, ledger | Pasa los gates de rendimiento y seguridad del protocolo de evaluación | Dos fallas de contexto críticas sin mitigar: se reduce el alcance |
| Meses 4-6 | Base | Suite de evals en CI con el dataset v1 y trazas | Cada release corre la suite; la tupla de versión queda registrada | Sin dataset utilizable: el caso queda en nivel 0 (sin IA) |
| Meses 4-6 | Base | Prueba de portabilidad y costo del gateway | Mide *fc*, *s*, calidad, suscripción y días-persona; resultado en el paquete de la lectura del mes 6 | Migrar cuesta más de 20 días-persona, o no hay lote reproducible: no se afirma cobertura de precio |
| Meses 4-6 | Base | FinOps: costo por persona activa, por consulta del caso y por resultado, con escenario de consumo | Reporte mensual con el escenario de consumo, que alimenta el tablero mensual del Council | Costo fuera del techo de Finanzas: se frena la expansión |
| Meses 7-9 | Interno | Caso de referencia en nivel 2 (prepara, no ejecuta) para Tecnología y Operaciones | Nivel 2 (prepara, no ejecuta) en la cohorte con los gates de rendimiento, seguridad y ético; extensión a Operaciones con el de impacto | Falla dura de seguridad: se apaga el caso. Impacto debajo al vencer la espera: no se extiende |
| Meses 7-9 | Interno | Extensión a staff y a equipos asignados a clientes, solo dentro del entorno del propio cliente y con su permiso escrito ([R-08](07-resoluciones.md#gobierno-y-seguridad)) | Uso semanal medido en el gateway y la telemetría | Sin permiso escrito o con restricción del cliente: no se extiende |
| Meses 7-9 | Base | Aislamiento por tenant probado (con tenants sintéticos si el producto no se libera) | Prueba adversarial sin filtración entre tenants | Una filtración: se bloquea el despliegue |
| Meses 7-9 | Producto | Piloto de IA en un producto propio, nivel 1 (asiste) a nivel 2 (prepara, no ejecuta), datos sintéticos | SLOs del caso cumplidos a las 6 semanas desde que opera; trazabilidad completa; cero incidentes de datos | No cumple el SLO a las 6 semanas (plazo ilustrativo): se revisa o se corta |
| Meses 7-9 | Producto | Red team del piloto (con Gobierno) | Hallazgos críticos cerrados | Hallazgo crítico sin mitigación: no sale |
| Meses 10-12 | Producto | Gate scale/kill del piloto de producto y paquete de cumplimiento para clientes | Decisión documentada; paquete (inventario, ubicación de datos, no entrenamiento, evidencia) listo | Sin SLO ni apetito del cliente: se corta y se reasigna |
| Meses 10-12 | Base | Decisión sobre modelo en infraestructura propia | Go/no-go con la matriz de clientes y el escenario de consumo | Sin demanda contractual demostrada: no se compra |
| Meses 10-12 | Interno | Lectura de valor del mes 12, insumo del año 2 («Gate de valor») | Peor caso del throughput mayor que 0 con las semanas maduras de M10-M12, sin daño de calidad | Sin distinción o con daño: el año 2 no se financia por valor |
| Meses 10-12 | Base | Revisión de arquitectura y de contratos de proveedor | ADR actualizados; compromisos de volumen alineados al gate | — |

### Bifurcación en el mes 3: con señal y sin señal

**Problema del alcance ampliado.** Comprometer el año completo de plataforma
(394k USD de costo económico, [Anexo E](05-business-case.md)) expondría recursos
antes de demostrar su justificación. Ese año no forma parte del pedido vigente.
**Regla del plan ([R-15](07-resoluciones.md#arquitectura-y-medición)):** el Directorio libera la plataforma de los meses 4-6 (contractor al
100%, como excepción a la restricción de no contratar que solo aprueba el Directorio
([R-20](07-resoluciones.md#personas)); gateway, pasarela) en la decisión del mes 3 solo con las cuatro condiciones de
«Build, buy o partner por capacidad» y al menos una señal: contractual (el umbral del
Anexo C), un anuncio del proveedor de pasar a precio por consumo, o una señal de cliente
para el producto. Sin señal o sin alguna de las condiciones, los meses 4-12 corren como la opción de gobierno mínimo y formación del Anexo E,
sin plataforma ni contractor, con la prueba
extendida a la cohorte, y las lecturas de los meses 6 y 9 vuelven a leer las señales. No es un corte:
difiere la plataforma. Las cifras son del Anexo E ("Alternativas equivalentes"); no se
recalculan acá. La revisión mensual del Council registra la señal en el mes en que llega
y la escala al Directorio, pero no libera la plataforma: eso queda en la decisión del mes 3 o en las lecturas siguientes.

| Hito de los meses 4-12 | Con señal | Sin señal |
|---|---|---|
| Costo del año, k USD (Anexo E; comparación del paquete completo) | 394 (213-575) | ≈ 199: preparación previa y meses 1-3 del paquete 69, prueba chica 6, meses 4-12 de la opción de gobierno mínimo ~114, cierre del contractor 4, compensatorios del Anexo C ~6 |
| Contractor | Al 100% en los meses 4-12; sin contractor rige el modo control ("Exceso de los meses 4-6 con el producto diferido") | No se contrata; el contractor desde el mes 1 cierra |
| Gateway en laboratorio, bypass por superficie y FinOps con escenario de consumo (meses 4-6) | Meses 4-6 | **Se difiere.** FinOps queda en costo por persona activa desde la telemetría del proveedor, sin costo por consulta ni por resultado (supuesto) |
| Harness v1, suite de evals en CI y dataset v1 (meses 4-6) | Meses 4-6 | **Se difiere** |
| Prueba de portabilidad y costo (meses 4-6) | Resultado en el paquete de la lectura del mes 6 | **Se difiere** |
| Caso de referencia en nivel 2 (prepara, no ejecuta) y aislamiento por tenant (meses 7-9) | Meses 7-9 | **Se difiere** |
| Piloto de producto y red team (meses 7-12) | Solo si la lectura del mes 6 lo libera | No corre; con señal de cliente en la lectura del mes 6 no arranca en los meses 7-9 por falta de base (ver abajo) |
| Prueba extendida: contrato de agente, skills y guía de revisión en toda la cohorte, sobre repositorios que la matriz habilite | Dentro de la formación | **Se mantiene**; es el mecanismo de la ganancia g ([fuente](../../context/supuestos/alternativas-de-menor-alcance.md)) |
| Medición contra la base, telemetría, matrices de superficie y de clientes | Se mantienen | **Se mantienen**, con la cohorte completa |
| Controles | Controles con bloqueo y registro del Anexo C | Gobierno mínimo más compensatorios probados del Anexo C: hooks, escaneo local, MCP acotados y red team interno del agente de código, con críticos cerrados y residual aceptado según [R-10](07-resoluciones.md#gobierno-y-seguridad); no equivale a cobertura central de todas las superficies |
| Infraestructura propia y revisión de contratos (meses 10-12) | Meses 10-12 | Meses 10-12, sin demanda: no se compra |

**Qué se pierde o se atrasa sin señal.**

- **Cobertura de precio:** *fc* × *s* no se mide y la palanca no se afirma. Si el
  proveedor anuncia consumo, es una señal: la lectura del mes 6 o la del mes 9 la leen y la plataforma
  arranca recién ahí. Hasta entonces la exposición se acota con la regla del Anexo F
  (más de 6× sin mitigar congela la expansión y topea el consumo), no con ruteo.
- **Caso de referencia en nivel 2 (prepara, no ejecuta):** sin harness ni evals no hay caso. Cada punto de espera
  lo corre un tramo: liberar en la lectura del mes 6 lo lleva a los meses 10-12, sin margen; en la del mes 9
  no llega a nivel 2 en el año.
- **Modo control:** el gateway en laboratorio y el bypass por superficie no
  corren en los meses 4-6. Se mantienen los compensatorios del Anexo C: prueba
  de secreto sintético y bypass del agente de código, red team acotado y
  aceptación fechada del residual. Las demás superficies conservan sus
  restricciones y administración; no se declaran cubiertas sin prueba propia.
- **Producto:** una señal de cliente en la lectura del mes 6 no alcanza para un piloto en los meses 7-9,
  porque gateway, harness y aislamiento no existen. Arranca como pronto en los meses 10-12
  con una base recién armada, o pasa al año 2 (lo decide el Directorio, que libera la construcción: [R-30](07-resoluciones.md#roadmap-y-comercial)).
- **Se evita:** la concentración en el contractor y la dependencia de su 0,2
  libre. No cambia ninguna puerta de un solo sentido: ambas ramas son
  reversibles y ninguna firma, compra hardware ni envía código o datos de un cliente.

**Condiciones técnicas que deja cada rama para leer las señales.**

| | Con señal | Sin señal |
|---|---|---|
| Lectura del mes 6 | Prueba de portabilidad y costo con *fc*, *s* y días-persona; caso de referencia en sombra; FinOps con el múltiplo medido; throughput descriptivo, sin lectura de valor | Throughput descriptivo con la cohorte completa; telemetría del proveedor por área y superficie, con la que se dimensiona un cambio de precio; matriz de clientes para juzgar la señal contractual y la de producto |
| Lectura del mes 9 | Caso en nivel 2 (prepara, no ejecuta), aislamiento por tenant, lote reproducible | Lo mismo, más el insumo de una plataforma liberada en la lectura del mes 6: la prueba de portabilidad llega a la lectura del mes 9, no a la del mes 6 |
| Qué no queda | — | Contractor, lote reproducible, suite y dataset: liberar más tarde obliga a contratar entonces (el plazo no consta: faltante) |

**Contrato de la propuesta.** *Alternativas:* aprobar el año con plataforma
(descartado en el Anexo E) o correr siempre con gobierno mínimo y formación (descartado: deja sin respuesta un
cambio de precio o una demanda contractual). *Recomendación:* la bifurcación.
*Dependencias:* los umbrales de cada señal son los del Anexo C; recalibrarlos lo
decide el Directorio a propuesta del AI Council ([R-15](07-resoluciones.md#arquitectura-y-medición)); este anexo aporta la telemetría. *Costo:* el del Anexo E; la
diferencia aritmética entre ramas publicadas, 394 − 199 ≈ **195k USD**, es
recurso valorizado que no se comprometería sin señal, no ahorro de caja demostrado.
*Riesgo (para Gobierno):* en la rama sin señal no hay bloqueo ni registro
central en el gateway; inyección indirecta y fuga de secretos requieren los
compensatorios probados del Anexo C y residual aceptado, sin garantía de bloqueo
en las otras superficies. *Responsable:*
el Responsable de Tecnología ([R-06](07-resoluciones.md#autoridad-y-liberaciones)); libera plataforma el Directorio ([R-15](07-resoluciones.md#arquitectura-y-medición)). *Criterio de éxito:* en la lectura del mes 6 la rama que corrió deja las condiciones de
la tabla. *Abandono:* la prueba extendida no arranca sin repositorios habilitados
para 15 personas activas, compensatorios probados, críticos cerrados y residual
aceptado; ahí la rama sin señal queda en medición y formación. Un incidente
revoca la aceptación según el Anexo C y suspende la extensión.

## Insumos para Finanzas

Todo es **supuesto** salvo donde se indica fuente. Rangos en **k USD** en las
tablas económicas. El esfuerzo es mayormente tiempo reasignado a costo cargado;
su contribución comercial desplazada no está medida y no se suma automáticamente.
Las tablas siguientes describen el paquete
completo: primer tramo acotado, contractor desde el mes 1 que reemplaza la
fracción de IA aplicada y producto diferido, con el conservador como comparación.
El pedido vigente se consolida en el [Anexo E](05-business-case.md), sección
«Pedido inicial: paquete mínimo»; estas tablas no lo sustituyen.

### Escenario conservador, como comparación (contractor que complementa y producto desde el mes 4)

| Concepto | Tramo | Rango, k USD | Fuente o supuesto |
|---|---|---|---|
| Esfuerzo técnico: 1,3 FTE equivalentes | Meses 1-3 | 15,3-36,75 | 0,3 arquitecto, 0,5 IA aplicada y 0,5 DevOps/QA por 3 meses, a los rangos de [costo por rol](../../context/supuestos/costo-cargado-por-rol.md); las fracciones son supuesto |
| Esfuerzo técnico: 3,3 FTE equivalentes | Meses 4-6 | 35,55-86,4 | 0,5 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,0 desarrollador senior |
| Esfuerzo técnico: 3,8 FTE equivalentes | Meses 7-9 | 40,05-97,65 | 0,5 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,5 desarrolladores senior |
| Esfuerzo técnico: 3,2 FTE equivalentes | Meses 10-12 | 34,2-83,4 | 0,4 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,0 desarrollador senior |

Suma del esfuerzo técnico: 125,1-304,2k USD en los cuatro tramos.

### Escenario recomendado (contractor desde el mes 1 que reemplaza, producto diferido)

Los desarrolladores senior son el **frente producto**: construyen e integran el
piloto. Con el producto diferido, no hay desarrollador en los meses 4-6, y los de los
meses 7-12 forman parte del tramo condicional que se libera en la lectura del mes 6. Así se confirma la lectura del Anexo E.

| Concepto | Frente | Tramo | Rango, k USD | Fuente o supuesto |
|---|---|---|---|---|
| Esfuerzo técnico: 0,6 FTE | Base | Meses 1-3 | 6,75-15,75 | 0,3 arquitecto y 0,3 DevOps/QA; la IA aplicada la cubre el contractor desde el mes 1 del [Anexo D](04-personas-cultura.md). Con el rol interno en lugar del contractor: 0,9 FTE, 10,8-25,65k USD |
| Esfuerzo técnico: 1,2 FTE, con el replan de los meses 4-6 | Base | Meses 4-6 | 12,6-30 | 0,4 arquitecto y 0,8 DevOps/QA (ver "Exceso de los meses 4-6 con el producto diferido"). Sin replan: 1,5 FTE, 15,75-37,5k USD |
| Esfuerzo técnico: 1,5 FTE | Base | Meses 7-9 | 15,75-37,5 | 0,5 arquitecto y 1,0 DevOps/QA |
| Esfuerzo técnico: 1,4 FTE | Base | Meses 10-12 | 14,4-34,5 | 0,4 arquitecto y 1,0 DevOps/QA |
| Desarrolladores senior del piloto: 1,5 FTE | Producto | Meses 7-9 | 13,5-33,75 | Solo si la lectura del mes 6 libera el producto |
| Desarrollador senior del piloto: 1,0 FTE | Producto | Meses 10-12 | 9-22,5 | Solo si la lectura del mes 6 libera el producto |

Suma de la base: 49,5-117,75k USD con el replan (52,65-125,25k USD sin él). Tramo
del producto: 22,5-56,25k USD. A los rangos de [costo por
rol](../../context/supuestos/costo-cargado-por-rol.md), con 3 meses por
tramo. El contractor (caja, Anexo D) no se repite acá. Sin contractor
(la alternativa sin contractor, con fracción interna), la base suma 0,8 FTE de IA aplicada interna por tramo en
los meses 4-12 y no hay replan de los meses 4-6.

### Caja y otros costos

| Concepto | Tramo | Rango, k USD | Fuente o supuesto |
|---|---|---|---|
| Suscripciones de IA (base) | Cada tramo | ≈ 4,8-6,1, más Copilot sin precio | Claude: 40-45 seats × USD 40-45 × 3 meses (40 × 40 × 3 = 4.800; 45 × 45 × 3 = 6.075). El promedio de la fuente es el de los seats de Claude; el de Copilot (20-25 seats) no está desglosado y no se estima. Sin seats nuevos. No es incremental. Cálculo sobre [la fuente](../../context/hechos/costos-tecnologia-e-ia.md) |
| Escenario de consumo a precio API (estrés) | Cada tramo | hasta ≈ 58-73 | 12× la suscripción del agente de código (40-45 seats × USD 40-45 × 3 meses). Es cota superior: el 12× es una estimación de telemetría, no una factura, y vale solo para el agente de código. Se sigue en el reporte mensual con el escenario de consumo, que alimenta el tablero mensual del Council |
| Infraestructura nueva (gateway, retrieval, trazas, evals en CI) | Meses 1-3 | Escenario recomendado: 0,5-1,5 **en el tramo de tres meses**. Escenario conservador: 0,5-1,5 **por mes** (1,5-4,5 en el tramo) | [Supuesto](../../context/supuestos/precios-externos-sin-cotizar.md): el recomendado solo tiene telemetría y registro; el conservador, gateway en laboratorio. Lo invalida una cotización o un precio de servicios gestionados |
| Ídem | Meses 4-6 | 4,5-12 | 1,5-4k USD por mes. Incluye, con tope de FinOps, el consumo de la prueba de portabilidad y costo y el del caso de referencia |
| Ídem, base sin piloto | Meses 7-12 | 4,5-12 cada tramo | Sin piloto, la infraestructura queda en el nivel de los meses 4-6 (1,5-4k USD por mes), como registra la [fuente de precios](../../context/supuestos/precios-externos-sin-cotizar.md). El consumo del caso de referencia entra dentro de este tope; si no entra, el caso se limita a una cohorte |
| Ídem, incremento del piloto | Meses 7-12 | 1,5-6 cada tramo (producto) | Tenant del piloto y su tráfico: lleva el renglón a 6-18k USD por tramo, el valor con piloto de la [fuente](../../context/supuestos/precios-externos-sin-cotizar.md) |
| Consumo de modelos del piloto de producto (evals y tráfico) | Meses 7-12 | 3-12 cada tramo (producto) | Supuesto: 1-4k USD por mes; sin base de volumen hasta el piloto |
| Red team del piloto | Meses 7-9 | 5-15 (producto) | Supuesto: un ejercicio con un tercero chico; lo invalida una cotización; coordinar con Gobierno |
| Prueba de portabilidad y costo del gateway | Meses 4-6 | Sin renglón propio | El tiempo va dentro de DevOps/QA y del contractor; el consumo por API, dentro del renglón de infraestructura de los meses 4-6, con tope de FinOps |
| Migración de superficies a la pasarela y pruebas de ruteo | Meses 4-6, rama con plataforma | ≈ 2,1-10,7 de tiempo | 15-30 días-persona de DevOps/QA a 3-7,5k USD por mes y 21 días hábiles; **ya incluido** en las fracciones de DevOps/QA, no suma. La prueba de controles de M1-M3 va en el mínimo |
| Instrumentación de uso en chat y Workspace (la dependencia que marca el Anexo D) | Meses 1-6 | ≈ 1,4-7,1 de tiempo | 10-20 días-persona de DevOps al mismo costo diario; ya incluido en DevOps/QA, no suma. Sin cotización de proveedores |
| Certificaciones del programa de partners | — | No estimado | Faltante: no hay costo publicado |

**Régimen del año 2.** Si la infraestructura de los meses 10-12 sin piloto queda en el nivel
de los meses 4-6, a régimen cuesta 18-48k USD por año en lugar de 24-72k USD. Los
6-24k USD de diferencia son del producto. El [costo de
régimen](../../context/supuestos/costo-de-regimen-del-ano-2.md) ya usa el valor sin
piloto para la base común.

**Base común mínima para el producto (corte mixto en la lectura del mes 9).** Este anexo propone, con una
corrección, el supuesto del Anexo E ([base
mínima](../../context/supuestos/base-minima-tras-un-corte.md)):

- **Conserva como supuesto:** infraestructura de base al nivel de los meses 4-6 (gateway, trazas y evals en
  CI, 4,5-12k USD en los meses 10-12, cota superior porque ya no corre el caso de referencia),
  la pasarela, el contractor al 50% para las evals y el harness del piloto (sin
  dato que lo respalde) y 0,5 FTE de DevOps/QA para operar el gateway y las evals.
- **Corrige:** suma **0,1 FTE de arquitecto** en los meses 10-12 (1,35-3k USD de tiempo, a
  los rangos de este anexo). El piloto sigue con el gate scale/kill y el paquete
  de cumplimiento de los meses 10-12 (aislamiento por tenant, ubicación de datos, ADR), que
  tocan puertas de un solo sentido; sin arquitecto no hay quién firme esa
  evidencia. El resto del arquitecto (decisión de infraestructura propia y
  revisión de contratos) se corta con la base común.
- Sigue siendo supuesto: lo recalcula el Anexo E.

Los porcentajes sobre facturación los calcula Finanzas: las fuentes públicas no publican
montos de facturación.

## Insumos para el deck

- **Arquitectura en una imagen:** lo que se pide hoy son las cuatro superficies
  existentes, configuradas, con sus controles probados y la medición agregada por
  área. La arquitectura objetivo (gateway neutral al modelo, aislamiento por
  cliente, harness con evals y gates, dos frentes sobre la misma base) es una
  hipótesis condicional a una señal y a las cuatro condiciones de R-15. Aun con
  ella, tres de las cuatro superficies pueden no pasar por el gateway, y el agente
  de código pasa solo si eso no rompe la suscripción plana; los casos propios,
  siempre por gateway.
- **Qué pedimos al Directorio:** primera autorización para validar en 2026;
  segunda liberación condicionada para M1-M3, según el [Anexo E](05-business-case.md),
  sección «Pedido inicial: paquete mínimo», adoptar el marco de gates y las
  resoluciones técnicas R-14 a R-19 del [Anexo G](07-resoluciones.md#arquitectura-y-medición). No se aprueban
  el contractor ni la excepción de 0,3 FTE del paquete completo. Una ampliación
  exige nuevo alcance, calendario y costeo. No se aprueba el modelo propio
  ni compromisos mayores a 12 meses.
- **Mensaje al CFO:** la IA ya es una línea propia del gasto de tecnología y
  el consumo real es un múltiplo de la suscripción. Se presupuesta el escenario de
  consumo y se prueba la salida de proveedor, no se declara. La cobertura de
  precio del gateway es una hipótesis que la prueba de los meses 4-6 confirma o descarta en
  la lectura del mes 6, y solo existe si la decisión del mes 3 libera la plataforma; sin señal, la palanca no se afirma. La ganancia de throughput se valúa como horas evitadas a output fijo, no
  como caja, y se acredita solo si el peor caso de la lectura del mes 9 es mayor que 0.
  Con 15-20 personas el año solo distingue con buena probabilidad una mejora
  cercana al techo del rango (+25%).
- **Riesgo que hay que nombrar:** el piloto de producto tiene hipótesis elegida
  (asistente de integración, Anexo F) pero ningún cliente que lo habilite
  todavía; el plan lo trata como hipótesis con gate. Y
  evals, harness y la prueba de portabilidad se concentran en un contractor.
- **Evidencia que falta:** línea base de productividad, matriz por cliente,
  primera corrida del protocolo de evaluación y la medición de *fc* × *s*; no se
  prometen números de calidad ni de ahorro hasta tenerlos.

## Cautelas

- Cifras estimadas, todavía sin validar contra fuentes internas de Acme Labs;
  se validan antes de comprometer presupuesto.
- El 12× es una estimación a precio API; el ahorro por inferencia no lleva
  porcentaje por falta de fuente primaria.
- La clasificación de productos de las tres capas del harness y las herramientas
  de PII del material de referencia no están verificadas con fuente primaria
  ([capas](../../material/conceptos/harness-tres-capas.md)): sirven como marco, no
  como recomendación de proveedor.
- Qué regiones o proveedores cumplen la residencia exigida por la Ley 25.326 para
  un cliente concreto es un faltante que decide legal; el anexo no lo afirma. En
  M1-M3 no hay flujo nuevo de datos ni código o datos de clientes en juego; el
  dictamen de Legal externo de M1 lo confirma o agrega un control (R-11).
- La escala de cinco niveles de autonomía (de nivel 0, sin IA, a nivel 4, autónomo dentro de límites) es una herramienta pedagógica, no un estándar.
- Qué superficie es enrutable no está verificado con documentación de proveedor.
- Las fracciones de esfuerzo y los rangos de infraestructura son supuestos.
  Los umbrales del protocolo de evaluación, el criterio de la prueba de
  portabilidad y costo y el replan de los meses 4-6 están en una
  [fuente](../../context/supuestos/umbrales-tecnicos-propuestos.md) revisada como propuesta de diseño,
  sin medición ni aprobación empresarial; ese alcance también aplica a la
  política de ruteo, el gate de impacto y el gate de valor con su cuenta de potencia,
  cuyos λ y φ son ilustrativos hasta el acta.
  El régimen comercial del agente de código depende de una respuesta
  escrita del proveedor que todavía no existe.
- El caso de referencia es el del frente interno y prueba el método que
  reutiliza el piloto de producto; la hipótesis de producto la eligió el
  portfolio del CAIO (Anexo F). El tamaño del dataset (~200 preguntas) es una propuesta sin
  cálculo de potencia estadística.
- El 0,2 libre del contractor en los meses 4-6 no está confirmado ([Anexo D](04-personas-cultura.md)):
  el replan del paquete completo requiere una decisión nueva de alcance,
  calendario y costeo; el mínimo no autoriza esa contratación. Las horas de la
  documentación mínima reproducible son supuesto.
