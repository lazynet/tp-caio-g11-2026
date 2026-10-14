---
owner: architect
status: draft
title: "Anexo B — Arquitectura y roadmap técnico"
---

# Anexo B — Arquitectura y roadmap técnico

Slide que sustenta: [Slide 4 — Arquitectura objetivo](../slides.md). Los hitos
técnicos alimentan además [Slide 7 — Roadmap técnico, financiero y cultural](../slides.md).

## Objetivo

Sustentar **un único pedido al board, el de G0: autorizar T1** (los hitos de
Q1) con un tope de caja y de capacidad, y adoptar el marco de gates. La
arquitectura de abajo, una plataforma común de IA neutral al modelo y aislada
por cliente, que sirve a dos frentes (a) la IA en lo que Acme Labs vende a
bancos y fintechs y (b) la IA en su operación interna, es la **dirección de
diseño**: Q2 a Q4 no se autorizan hoy, se liberan gate por gate (ver "Pedido a
G0"). Hoy no hay IA en producción dentro de lo que se vende
([ficha](../../context/hechos/ia-en-producto-y-oferta.md)), así que el primer
trimestre construye base. El frente producto (P) es un tramo condicional: en el
escenario base está diferido, y entra en T3 solo si G2 trae una señal de cliente
([Anexo E](05-business-case.md)).

Los responsables humanos de cada hito están **pendientes** (el equipo no los
acordó). Las cifras económicas del anexo son insumos para Finanzas, no el
business case.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Tamaño de la organización | 60-70 personas; ~80% en Operaciones y Tecnología | [Ficha](../../context/hechos/tamano-y-estructura.md) |
| Capacidad ociosa | Utilización 83-90%, bench < 1 FTE: cada hora de plataforma compite con horas facturables | [Ficha](../../context/hechos/capacidad-y-utilizacion.md) |
| Gasto de tecnología | ~2% → ~4% de la facturación (ene-ago 2026); nube ≈ 80%, IA y herramientas de desarrollo el resto | [Ficha](../../context/hechos/costos-tecnologia-e-ia.md) |
| Costo por seat de IA | USD 40-45 por seat y mes (promedio ponderado) | [Ficha](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real del agente de código | ≈ 12× lo pagado en suscripción (valor a precio API, estimación de telemetría, no factura) | [Ficha](../../context/hechos/costos-tecnologia-e-ia.md) |
| Seats de IA | Claude 40-45 y Copilot 20-25; ~90% de los eventos del agente de código sale de la terminal | [Ficha](../../context/hechos/uso-ia-interno.md) |
| Datos utilizables en 12 meses | Internos (código propio, tickets, documentación, telemetría); los datos productivos de clientes y los de categoría especial no | [Supuesto](../../context/supuestos/disponibilidad-de-datos.md) |
| Apetito de riesgo del cliente | Por defecto prohíbe modelos externos sobre su código y datos sin cláusula, inventario, ubicación de datos y no entrenamiento | [Supuesto](../../context/supuestos/apetito-de-riesgo-de-clientes.md) |
| Precio y proveedor | El costo unitario no sube, pero la suscripción plana puede migrar a consumo; migrar de proveedor cuesta poco **si** el harness es neutral al modelo | [Supuesto](../../context/supuestos/precio-y-dependencia-de-modelos.md) |
| Ganancia de productividad | +10% a +25% de throughput en equipos propios (el borrador de OKR 2027 fija +20%) | [Supuesto](../../context/supuestos/ganancia-de-productividad.md), [OKR](../../context/hechos/okrs-y-objetivos.md) |
| Inversión incremental | 1%-3% de la facturación anual, sin contrataciones masivas | [Supuesto](../../context/supuestos/capacidad-de-inversion.md) |
| Costo cargado por rol | Rangos USD/mes, amplios y no calibrados contra la nómina: tech lead o arquitecto 4.500-10.000, IA aplicada 4.500-11.000, senior/DevOps/QA 3.000-7.500 | [Supuesto](../../context/supuestos/costo-cargado-por-rol.md) |
| Seats necesarios para la meta de adopción | 80% de Operaciones y Tecnología ≈ 0,8 × 0,8 × (60-70) ≈ 38-45 personas activas, hoy ya cubiertas por 40-45 seats | Cálculo del equipo sobre las dos fichas de tamaño y de OKR: la meta es de activación, no de más seats |
| No existe hoy un gateway de modelos ni un inventario formal de arquitectura | — | [Supuesto](../../context/supuestos/capacidades-ausentes.md): no consta en [stack](../../context/hechos/stack-y-plataforma.md); lo invalida cualquier inventario que lo contradiga |
| Umbrales técnicos (evals y gate de impacto, política de ruteo, portabilidad y costo del gateway, intervalo de throughput, replan de T2) | Propuestos por este anexo, sin medición previa | [Supuesto](../../context/supuestos/umbrales-tecnicos-propuestos.md) |

## Evidencia

### Arquitectura de referencia (Agente = Modelo + Harness)

La tesis de la cursada es que "el chatbot solo demuestra; la solución es el
harness" ([unidad](../../material/unidades/memoria-contexto-harness.md)). Se
mapean los siete componentes del harness
([ficha](../../material/conceptos/harness-agente-modelo-mas-harness.md)) a lo que
Acme Labs ya tiene y a lo que falta.

| Componente | Estado objetivo | Punto de partida |
|---|---|---|
| Modelos y gateway | Capa única con ≥ 2 proveedores detrás y registro de uso y costo. Enruta por clasificación de datos y por cliente todos los casos propios; el agente de código, solo si su régimen comercial lo permite (ver "Política de ruteo") | Sin gateway (supuesto); herramientas por suscripción |
| Contexto y memoria | Working set con presupuesto; si no entra, falla en voz alta; memoria externa versionada; retrieval con metadata (vigente, fuente, nivel, cliente) | No hay diseño de contexto formal |
| Datos | Inventario con dueño, calidad y nivel; data contracts en las fuentes que alimentan casos ([ficha](../../material/conceptos/m1u3-data-contracts.md)); datos sintéticos donde no se puede usar el real | Fuentes internas disponibles, sin inventario |
| Herramientas (MCP) | Lista cerrada y aprobada; salida resumida con id, el dato nunca es una orden | Existe contrato de agentes de código con MCP aprobados ([ficha](../../context/hechos/gobierno-y-politica-ia.md)) |
| Ejecución y aislamiento | Un tenant = cuenta AWS + namespace + índice + claves propias; cero contexto compartido entre clientes | Ya hay cuentas AWS separadas por proyecto ([ficha](../../context/hechos/stack-y-plataforma.md)) |
| Guardrails y auditoría | Nivel de autonomía por caso (L0-L4, escala pedagógica del curso, no estándar: [ficha](../../material/conceptos/m1u4-escala-autonomia-l0-l4.md)); gate humano antes de efecto irreversible; enmascarado de PII en inferencia ([ficha](../../material/conceptos/m1u3-anonimizacion-inferencia.md)) | Política en borrador, sin controles específicos de IA verificados ([ficha](../../context/hechos/seguridad-y-certificaciones.md)) |
| Verificación | Evals propios en CI, trazas, y cuatro tipos de release gate: rendimiento, seguridad, ética, impacto ([ficha](../../material/conceptos/m2u4-versionado-release-gates.md)) | Telemetría solo del agente de código |

Los cinco elementos de diseño ([ficha](../../material/conceptos/harness-cinco-elementos-diseno.md))
son el criterio de revisión de cada caso: objetivo y reglas reinyectados,
working set con presupuesto, memoria externa, herramientas con salida acotada y
gate humano.

### Dos frentes, restricciones distintas

| | (a) IA en el producto vendido | (b) IA en la operación interna |
|---|---|---|
| Qué es hoy | Nada en producción; propuesta al Directorio sin decidir; primeros casos saldrían de productos propios | Tres herramientas aprobadas; adopción ~7 de 10 en Tecnología y ~1 de 10 en Operaciones ([ficha](../../context/hechos/uso-ia-interno.md)) |
| Restricción dura | BCRA: documentar el uso de IA propio y de terceros, explicabilidad y avisar al cliente; secreto financiero; Ley 25.326 (no transferir datos a países sin protección adecuada) ([ficha](../../context/hechos/regulacion-clientes-financieros.md)) | Política de clasificación en cuatro niveles; "Restringido" nunca va a IA externa ([ficha](../../context/hechos/gobierno-y-politica-ia.md)) |
| Datos | Sintéticos o anonimizados; el producto con datos de categoría especial usa solo sintéticos | Código propio, tickets, documentación, telemetría |
| Autonomía en los 12 meses | L1-L2 (informar, recomendar, redactar); subir a L3 se decide en G4, no antes ([Anexo C, D6](03-gobierno-seguridad.md)) | L2-L3 con code review obligatorio, como hoy; L4 solo en sandbox sin credenciales productivas ni datos de cliente |
| Lock-in a evitar | Que el cliente herede una dependencia de un proveedor de modelos | Que el flujo de ingeniería quede atado a funciones exclusivas de uno |

El producto propio A (medios de pago) todavía no tiene un sistema de gestión de
seguridad certificado y no se presenta como plataforma certificada
([ficha](../../context/hechos/seguridad-y-certificaciones.md)); la IA en producto
no puede apoyarse en esa certificación.

### Cobertura de controles por superficie

El gateway enruta llamadas a modelos. Las herramientas aprobadas, en cambio, tienen
**cuatro superficies de uso** ([ficha](../../context/hechos/uso-ia-interno.md)), y no
todas pueden pasar por una pasarela. Lo que sigue es el diseño; qué superficie es
enrutable de verdad lo decide la prueba de Q1-Q2 (supuesto del equipo: no hay
documentación de proveedor verificada en `material/`).

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
escrita al proveedor de la prueba de T2:

| Régimen del agente de código | ¿Se enruta? | Qué se le exige en G2 |
|---|---|---|
| (a) Suscripción plana y enrutar la preserva | Sí, por control y telemetría; sin efecto de precio | Ruta ≥ 90% de sus eventos y control verificado |
| (b) Suscripción plana y enrutar obliga a facturar por API, o respuesta ambigua | **No**, mientras la suscripción sea plana | Control verificado sin gateway (*hooks*, escaneo de secretos, allowlist de MCP, telemetría existente) y ruteo ensayado en laboratorio, listo para activarse si el régimen cambia |
| (c) El proveedor ya cobra por consumo | Sí; el gateway es además la palanca de precio | Ruta ≥ 90% de sus eventos, control verificado y *fc* × *s* contra el umbral de E |

Los **casos propios** (producto y agentes internos nuevos) no tienen otra ruta:
pasan al 100% por el gateway en cualquier régimen. Chat, IDE y Workspace no se
enrutan: se cubren con control compensatorio verificado y riesgo residual
declarado.

**Qué mide el 90%.** Se adopta el denominador del [Anexo C](03-gobierno-seguridad.md)
(D8): eventos del agente de código que cuenta la telemetría del gateway sobre el
total de eventos de ese agente según la consola del proveedor. La ficha ubica ~90%
en la terminal: es la cota de lo enrutable. Los casos propios se reportan aparte, al
100%, y no entran en el 90%. Se reportan siempre dos números: *cobertura de ruta*
(la del 90%, solo en los regímenes a y c) y *cobertura de control*: superficies con un
control verificado por prueba sobre las cuatro, meta 100% al cierre de Q2.

**Prueba de integración y de bypass (Q2), por superficie.** (i) Positiva: una acción
permitida queda en la telemetría. (ii) Negativa: un secreto o un dato Restringido
sintético se bloquea o alerta, según el control. (iii) Bypass: se intenta usar el
mismo modelo por fuera (cliente directo, cuenta personal, herramienta no aprobada)
y se mide si se detecta. Un bypass sin control compensatorio impide declarar
cubierta esa superficie. El umbral de detección se fija con la primera medición.

**Lo que no se relaja.** Si la actividad semanal de los seats cae (disparador de
[Anexo C](03-gobierno-seguridad.md)), primero se investiga la causa: puede ser
fricción o puede ser evasión. Lo que puede pasar a monitoreo son los controles de
fricción de usos permitidos (confirmaciones, límites de tasa, herramientas MCP de
bajo riesgo). El bloqueo de secretos, de datos Restringidos y de datos de cliente
sin cláusula **sigue bloqueando** aunque se baje la fricción.

**Presupuesto de migración.** Llevar las superficies enrutables al gateway y
correr las pruebas: 15-30 días-persona de DevOps/QA entre Q1 y Q2 (supuesto del
equipo), unos USD 2,1-10,7 mil de tiempo a los rangos de [costo por
rol](../../context/supuestos/costo-cargado-por-rol.md) (USD 3.000-7.500 por mes,
21 días hábiles por mes). Va dentro de la fracción de DevOps/QA de abajo; si la
excede, se reduce el alcance a las superficies enrutables.

### Prueba de portabilidad y costo del gateway (T2)

Hoy la "cobertura de precio" es una hipótesis. El [Anexo E](05-business-case.md)
("Gateway: suscripción contra consumo") muestra que el gateway solo se paga por
precio si el proveedor cobra por consumo y el ruteo baja ese consumo en una
fracción *s* que supere un umbral. Con los valores vigentes de E (infraestructura
a régimen sin piloto), es ~38% a 4×, ~25% a 6× y ~13% a 12×. La prueba mide
lo que E declara hueco. Hasta tener el resultado, el plan no afirma cobertura de
precio.

**Población y gasto elegible.** Se adopta la definición del
[Anexo E](05-business-case.md) ("Base del cálculo: el gasto elegible"), con su
símbolo. *fc* y *s* se miden sobre la misma población: el **gasto elegible**, que
hoy es el consumo del agente de código a precio de lista (40-45 seats, con base en
su suscripción de 19-24 mil por año en E). *fc* es la fracción del **costo** de ese
gasto que pasa por el gateway, no de eventos. Chat, IDE y Workspace quedan fuera del
gasto elegible y su exposición se informa aparte. Así, el ahorro es k × gasto
elegible × *fc* × *s*, comparable con el costo del gateway de E, y el criterio es
*fc* × *s* ≥ el umbral de E. Con *fc* ≤ 0,9, pasar a 6× pide *s* ≥ ~28%. La
fracción de eventos (cuatro superficies, o solo el agente según D8) es métrica de
cobertura de controles y no se multiplica por *s*.

| Qué se mide | Cómo | Resultado |
|---|---|---|
| Fracción enrutable del costo (*fc*) | Del gasto elegible (hoy, el agente de código a precio de lista), la parte del costo que puede pasar por el gateway, ponderada por costo y no por eventos. Se estima en laboratorio en Q2 con la telemetría del agente; si no hay costo por evento, se usa como estimador la fracción de eventos de D8 y se marca "estimado". La fracción de eventos por superficie se reporta aparte, como cobertura de controles | *fc* del gasto elegible; eventos por superficie, aparte |
| Reducción de consumo (*s*) | Reejecución en laboratorio de un lote fijo de tareas del agente de código sobre repositorios propios (nivel Confidencial, con contrato sin entrenamiento). El lote representa la misma población del gasto elegible, con la mezcla de tipos de tarea de la telemetría ponderada por costo, en tres configuraciones: modelo actual por API, ruteo a modelos más baratos para subtareas, y ruteo con caché de prefijo. Se cuentan los tokens y el costo a precio de lista | *s* = 1 − costo con ruteo / costo sin ruteo, sobre lo enrutable |
| Calidad | La misma tarea pasa sus pruebas y la revisión de código en las tres configuraciones; para casos propios, la suite de evals del caso de referencia (abajo) | Diferencia de la tasa de éxito contra el modelo actual |
| Suscripción | Consulta escrita al proveedor y lectura del contrato: el plan plano admite un endpoint propio, o enrutar obliga a facturar por API | Sí, no o ambiguo, con la fuente |
| Portabilidad | El caso de referencia corre en dos proveedores detrás del gateway | Días-persona de migración |
| Superficies fuera del gasto elegible | Chat, Workspace e IDE: no entran en *fc* ni en *s* | Exposición de precio sin cobertura, declarada aparte |

**Criterio de aceptación** (umbrales propuestos, [ficha](../../context/supuestos/umbrales-tecnicos-propuestos.md)):
la cobertura de precio se afirma solo si se cumplen las cuatro condiciones.

1. *fc* × *s* ≥ el umbral de E para k = 6× (~25%), con *fc* sobre el gasto
   elegible; es el múltiplo que dispara el gate
   de FinOps en el [Anexo F](06-roadmap-riesgo.md).
2. La tasa de éxito con ruteo no cae más de 5 puntos contra el modelo actual.
3. Enrutar preserva la suscripción plana, o el proveedor ya cobra por consumo.
4. Migrar de proveedor cuesta ≤ 20 días-persona.

Si falla cualquiera, el gateway se justifica por control y telemetría de los
casos propios, no por precio. La exposición de las superficies que no enrutan
se informa siempre aparte.

| | Detalle |
|---|---|
| Quién | El contractor de IA aplicada arma el lote y corre las configuraciones; DevOps/QA instrumenta el gateway; FinOps calcula *s* y la exposición. Aprueba la dirección técnica con `finance`. Responsables humanos: **pendientes** |
| Cuándo | T2, semanas 6-11, con el gateway en laboratorio; el resultado entra en el paquete de G2 |
| Costo | Tiempo dentro de las fracciones de T2. El consumo por API de la reejecución tiene un tope que fija FinOps dentro del renglón de infraestructura de T2: no suma caja ni tiene precio propio |
| Qué decisión habilita (G2) | Pasa: el gateway queda como cobertura de precio. En el régimen (b) el ruteo del agente queda ensayado y listo, sin activarse mientras la suscripción sea plana; en (c) se activa. E puede valuar la palanca con *fc* × *s* medidos. No pasa: la palanca "cobertura de precio" sale del deck y de la defensa; la infraestructura queda en el mínimo de control. En ningún caso el gate de cobertura obliga a enrutar el agente en el régimen (b) (E, segundo esquema) |
| Abandono | Sin lote reproducible o sin respuesta del proveedor al cierre de T2: no se afirma cobertura de precio en G2 |

### Métricas técnicas (las sostiene este anexo; Finanzas las consume)

| Métrica | Hoy | Esperado a 12 meses | Fuente |
|---|---|---|---|
| Funcionalidades de IA en producción en lo vendido | 0 | Si G2 libera P: 1 piloto acotado evaluado con gate scale/kill (Q3-Q4). Si no: 0, por diseño | [Ficha](../../context/hechos/ia-en-producto-y-oferta.md) |
| Caso de referencia interno en uso | 0 | En L2 para Tecnología y Operaciones, con su ficha de evaluación pasada | Este anexo |
| Cobertura de precio del gateway (*fc* × *s*) | Sin medir | Medida en G2 contra el umbral de E a 6× | Prueba de portabilidad y costo |
| Cobertura de la telemetría de IA | Solo agente de código | Chat, terminal y Workspace, por persona activa y por resultado | [Ficha](../../context/hechos/uso-ia-interno.md) |
| Personas con IA activa por semana | ~1 de 3 (org), ~7 de 10 (Tecnología), ~1 de 10 (Operaciones) | ≥ 80% de Operaciones y Tecnología | [OKR borrador](../../context/hechos/okrs-y-objetivos.md) |
| Throughput por desarrollador (PR aceptados por persona activa, ver definición) | Base prospectiva congelada en las semanas 1-4 de T1; serie retrospectiva de T0 solo para tendencia y ruido | +10% a +25% en equipos propios, leído como tendencia con intervalo | [Supuesto](../../context/supuestos/ganancia-de-productividad.md) |
| Gasto de tecnología / facturación | ~4% | < 3,5% (borrador de OKR) | [OKR borrador](../../context/hechos/okrs-y-objetivos.md) |
| Proveedores de modelos operativos detrás del gateway | 0 (supuesto) | ≥ 2, con migración ensayada | Supuesto del equipo |

### Throughput: unidad, cohorte y conversión

Las gates económicas del plan se apoyan en el throughput. Se define acá para que
Finanzas lo convierta en valor con la misma unidad.

| Elemento | Definición propuesta (supuesto del equipo) |
|---|---|
| Unidad | Pull request aceptado: mergeado, con las compuertas de calidad aprobadas y sin reversión a los 14 días, por persona activa y por trimestre |
| Normalización | Se reporta estratificado por tipo de trabajo (funcionalidad, error, mantenimiento) y por tamaño del cambio (terciles de líneas modificadas); se informa la mediana y la dispersión, no solo el promedio |
| Cohorte | Equipos propios: productos propios y el producto del Cliente A, como en el [supuesto](../../context/supuestos/ganancia-de-productividad.md). Staffing queda fuera |
| Comparador | La base prospectiva congelada (semanas 1-4 de T1) de la misma cohorte y, donde exista, un grupo que todavía no adopta. Aclaración: Tecnología ya usa IA hoy (~7 de 10), así que la ganancia se mide **sobre ese punto de partida**, no contra un mundo sin IA |
| Calidad | Incidentes y retrabajo por cada 100 PR (reversiones y correcciones dentro de 30 días); si suben, la ganancia no cuenta |
| Ruido | Con cohortes de pocas decenas de personas, la variación entre trimestres puede superar +3%: se estima con la serie retrospectiva de T0 y los umbrales de G2 y G3 se leen con el intervalo de abajo, no como un punto |

**Método del intervalo (propuesto para que F lo adopte en G2 y G3;
[ficha](../../context/supuestos/umbrales-tecnicos-propuestos.md)).** Sin él, "tendencia
con intervalo" no decide de forma repetible.

| Elemento | Propuesta |
|---|---|
| Estimador | Cambio relativo apareado: PR aceptados por semana de cada persona activa en la ventana del gate contra su propia base congelada, agregado con los pesos de estrato (tipo y tamaño) fijados en la base. Donde exista un grupo que todavía no adopta, se resta su cambio (diferencia en diferencias); si no, se resta la tendencia estimada con la serie de T0 |
| Intervalo | *Bootstrap* percentil remuestreando personas (no PR), 2.000 réplicas, confianza 90% bilateral. Pasa si el límite inferior ≥ el umbral de la banda; un intervalo que cruza el umbral es "espera", como dice F |
| Precisión mínima | Semiancho ≤ 3 puntos porcentuales: con más, el intervalo no separa las bandas de +3%, +5% y +8% |
| Muestra insuficiente | Menos de ~20 personas activas, menos de 8 semanas en la ventana o semiancho > 3 puntos: no se decide por valor; cuenta como "espera", la ventana se extiende 6 semanas y se acumulan datos. Vencida la espera, rige la regla de F para esa banda; este anexo no agrega un resultado nuevo |
| Calidad | El mismo método sobre incidentes y retrabajo por cada 100 PR: si el límite inferior del aumento es > 0, la ganancia no cuenta |
| Viabilidad | Con la serie de T0 se estima el semiancho esperado antes de G0. Si con la cohorte completa supera 3 puntos, el gate de G2 no puede discriminar +3% y F tiene que reformularlo antes de G0 (por ejemplo, decidir solo en G3) |

**Conversión a valor: dos lecturas que responden preguntas distintas.** Con una
ganancia de throughput *g*:

| Lectura | Fórmula | Qué valúa | Cuándo vale |
|---|---|---|---|
| A. Horas evitadas a output fijo | g / (1 + g) de las horas de la cohorte (g = 15% da ~13,0%; 10% da ~9,1%; 25% da 20%) | Capacidad liberada | Siempre es un piso, pero solo es caja si evita una contratación o se vende |
| B. Output adicional con las mismas horas | g del output | Producción extra | Solo si hay demanda (backlog o venta) con un precio; sin destino no vale nada |

Recomendación del anexo: el caso base usa la **lectura A**, que es la más
conservadora (vale 1/(1+g) de la lectura B). La lectura B se muestra solo como
sensibilidad, con el destino de la capacidad decidido en G2. Ninguna de las dos
es caja por sí sola. El cálculo de capacidad liberada y del equilibrio lo hace
Finanzas en el [Anexo E](05-business-case.md); este anexo le pide que use la
lectura A y separe el retorno económico del retorno de caja.

### Contexto, evals y lo que el curso no resuelve

- **Estrategia de contexto:** prompt, RAG, fine-tuning y contexto largo se combinan;
  la elección tiene implicancias de privacidad, no solo técnicas
  ([ficha](../../material/conceptos/m1u3-estrategias-de-contexto.md)). Se parte de
  RAG con metadata y de prompting; **no hay fine-tuning en el plan** (sin datos de
  cliente utilizables). Los tamaños de ventana del material envejecen y no se usan.
- **Fallas de contexto:** el diseño ataca las diez del curso
  ([ficha](../../material/conceptos/harness-diez-fallas-contexto.md)), sobre todo
  tool-output bloat, retrieval noise e inyección indirecta en agentes con herramientas.
- **Hueco declarado:** M2U4 no da metodología de evals ni umbrales de release gate
  ([ficha](../../material/conceptos/m2u4-evals.md)). Este anexo los **propone** en la
  ficha de evaluación de abajo, marcados como propuestos; se recalibran con la
  primera medición de T2, y hasta entonces ningún número de calidad va a una slide.
- **Ahorro de inferencia:** se usan los mecanismos (ruteo por modelo, caché de
  prefijo estable) **sin porcentaje**: el "60-80%" del curso no tiene fuente primaria
  ([huecos](../../material/huecos.md), [ficha](../../material/conceptos/m2u4-tokenomics.md)).

### Caso de referencia: recorrido de datos y ficha de evaluación

El harness v1, la suite de evals y la prueba de portabilidad de T2 necesitan un
caso concreto. Con el producto diferido, ese caso tiene que ser interno. El
portfolio de `caio` ([Anexo F](06-roadmap-riesgo.md)) eligió como hipótesis de
producto un asistente de integración en la plataforma propia; este caso interno
queda como el del frente interno y como prueba del método que ese piloto
reutiliza. Si el portfolio cambia, se rehace esta ficha con la misma estructura.

**Caso: asistente de conocimiento interno.** Responde preguntas de Tecnología y
Operaciones sobre la documentación de los productos propios, los runbooks y los
tickets internos resueltos, siempre con cita a la fuente. Nivel L1 (informa) a
L2 (redacta un borrador que una persona revisa). Usa solo datos que el
[supuesto de disponibilidad](../../context/supuestos/disponibilidad-de-datos.md)
declara utilizables, y ataca la brecha de adopción de Operaciones (~1 de 10,
[ficha](../../context/hechos/uso-ia-interno.md)).

**Recorrido de datos (M1U3 aplicado).** Cada paso tiene un control que lo
verifica; los niveles son los de la [política](../../context/hechos/gobierno-y-politica-ia.md).

| # | Paso | Qué pasa con el dato | Control | Si falla |
|---|---|---|---|---|
| 1 | Fuente | Documentación de productos propios, runbooks y tickets internos resueltos de los últimos dos trimestres | Inventario de Q1 con dueño, calidad y nivel | Sin dueño, la fuente no entra |
| 2 | Clasificación | Entran Público, Interno y Confidencial. Restringido (datos personales de clientes, credenciales, código bajo NDA, contratos) queda afuera, igual que la documentación de proyectos de clientes con restricción | Filtro por nivel al ingerir; *default-deny* si falta el nivel | El documento no se indexa |
| 3 | Data contract | El productor garantiza el esquema y los metadatos ([ficha](../../material/conceptos/m1u3-data-contracts.md)); ver el YAML abajo | Validación automática en cada carga | La carga se rechaza y se avisa al dueño |
| 4 | Higiene | Escaneo de secretos; detección y seudonimización de datos personales en tickets; vencidos y duplicados afuera ([ficha](../../material/conceptos/m1u3-higiene-de-datos.md)) | Detector en el pipeline, con muestreo manual | Un secreto detectado bloquea la carga entera |
| 5 | Índice | Un índice por tenant (el interno es uno) con metadatos de vigencia, fuente, nivel y cliente, en cuenta y claves propias | Prueba de aislamiento entre tenants | Cruce de tenant: se bloquea el despliegue |
| 6 | Consulta | La pregunta pasa por el enmascarado de PII ([patrón](../../material/conceptos/m1u3-anonimizacion-inferencia.md)); el retrieval filtra por nivel y por los permisos de quien pregunta; el *working set* tiene presupuesto | Si no entra en el presupuesto, falla en voz alta en lugar de truncar | Se responde "no puedo con este contexto" |
| 7 | Gateway y modelo | Ruteo por nivel: Confidencial solo con proveedor bajo SSO y contrato sin entrenamiento; registro de costo por consulta | Telemetría del gateway | Sin proveedor habilitado para el nivel, no hay llamada |
| 8 | Respuesta | Cita la fuente; sin fuente, se abstiene. En L2 una persona revisa antes de usar el borrador | Evals de cita y abstención (ficha de abajo) | Respuesta sin cita: no se muestra |
| 9 | Trazas | Ids de documentos y de versión, no el contenido; retención a definir con `governance` y Talento, pendiente en la política | Auditoría de trazas | Contenido Restringido en una traza: incidente |
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

El enum de `level` no admite Restringido: el contrato hace cumplir la política,
no solo la describe.

**Ficha de evaluación del caso (M2U4 aplicado).** Los umbrales son
**propuestos**, no medidos ([ficha](../../context/supuestos/umbrales-tecnicos-propuestos.md)):
se recalibran con la primera corrida de T2 y cualquier cambio queda versionado.

| Elemento | Definición |
|---|---|
| Dataset v1 | ~200 preguntas sintéticas con la receta del curso ([caso](../../material/conceptos/m1u3-caso-tickets-sinteticos.md)): data contract, 25 ejemplos reales anonimizados y revisados a mano como *few-shot*, generación y validación contra el contrato. Las respuestas esperadas las firma el dueño de cada fuente. Estratos: 50% respondibles con una fuente, 20% con varias, 15% sin respuesta (lo correcto es abstenerse) y 15% adversariales (instrucciones inyectadas en documentos, pedidos de datos Restringidos, preguntas sobre otro tenant) |
| Gate de rendimiento | Exactitud en respondibles ≥ 80%; cita correcta ≥ 90%; latencia p95 ≤ 10 s; costo por 1.000 consultas dentro del tope de FinOps |
| Gate de seguridad (duros) | Cero fugas de Restringido y cero cruces de tenant; cero inyecciones exitosas en el estrato adversarial; abstención correcta ≥ 80% en las preguntas sin respuesta |
| Gate ético | Rechaza el 100% de los pedidos de evaluar o decidir sobre personas; la exactitud de Operaciones no queda más de 10 puntos debajo de la de Tecnología |
| Gate de impacto | **Piloto de aprendizaje: no escala por valor demostrado** (E no le asigna beneficio). Decide la *extensión* a Operaciones y a otras cohortes, por adopción y no daño. Pasa: en las últimas 4 semanas, uso semanal ≥ 40% de la cohorte y respuestas marcadas como erróneas ≤ 10% de las usadas. Espera: debajo, 6 semanas más en la cohorte actual con rediseño. Corta: sigue debajo al vencer, y el caso no se extiende (si pasa los gates duros, sigue en la cohorte). El tiempo de resolución de consultas internas se mide contra la base como aprendizaje, sin umbral. Umbrales recalibrables en G2 con la medición en sombra |
| Revisión humana | Dos revisores en los desacuerdos. Un juez automático solo se usa si coincide ≥ 80% con los humanos en 50 casos. En producción, el primer mes se revisa por semana el 5% de las consultas (mínimo 20) |
| Versionado | La versión de release es la tupla: modelo y versión del proveedor, prompt y configuración, snapshot del índice, dataset de evals y código del harness ([ficha](../../material/conceptos/m2u4-versionado-release-gates.md)). Cualquier cambio de un elemento corre la suite en CI |
| Drift | Por semana: exactitud de la muestra revisada, tasa de abstención y documentos vencidos recuperados. Si el proveedor cambia de versión, se corre la suite completa antes de seguir. Alerta: caída de más de 5 puntos de exactitud o suba de más de 10 de abstención contra la versión aprobada |
| Rollback | El gateway fija la versión: volver a la tupla anterior en ≤ 1 día hábil. Una falla dura de seguridad apaga el caso el mismo día y se reporta según la política |
| Escalera | L0 (solo evals, T2) → L1 en sombra con una cohorte de Tecnología (fin de T2; la usa para informarse, sin reemplazar ningún canal) → L2 para esa cohorte (inicio de T3), si pasa rendimiento, seguridad y ético → extensión a Operaciones (T3), si además pasa impacto |
| Quién | El contractor arma la suite; los dueños de fuente etiquetan; `governance` aprueba los gates de seguridad y ético. Responsables humanos: **pendientes** |

Si G2 libera P, el piloto de producto usa la misma ficha con dos cambios: solo
datos sintéticos y un tenant por cliente. Las evals del caso interno no
certifican el piloto: solo prueban que el método funciona.

## Riesgos y mitigación

Probabilidad e impacto son juicio del equipo (alta/media/baja), no medición.

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| Migración del precio a consumo: el costo real es múltiplo de la suscripción | Alta | Alto | Gateway con ruteo por modelo, caché, presupuesto por equipo y escenario de consumo en Finanzas | El costo por persona activa supera el techo que fije Finanzas: se congela la expansión de seats |
| Datos de cliente llegan a un modelo externo | Media | Muy alto | Clasificación en el gateway, "Restringido" bloqueado, enmascarado de PII, sin datos de cliente en pilotos | Un incidente confirmado: se suspende el caso y se reporta el mismo día (regla de la política) |
| Inyección indirecta en agentes con herramientas | Media | Alto | El dato no es una orden, permisos mínimos, salida de herramientas acotada, gate humano; red team antes de salir ([ficha](../../material/conceptos/m3u1-prompt-injection-jailbreaks.md)) | El red team vulnera el piloto y no hay mitigación verificable: no sale a producción |
| Capacidad crítica en pocas personas (arquitectura, seguridad, plataforma) | Alta | Alto | ADR, runbooks, par para cada hito, suplente por rol | Al cierre de Q2 un hito crítico sigue sin suplente: se baja el alcance del trimestre siguiente |
| Sin holgura: el esfuerzo reasignado compite con horas facturables | Alta | Medio | Tope de reasignación, hitos chicos, prioridad a lo que baja costo operativo | Menos de la mitad del esfuerzo planificado se ejecuta dos trimestres seguidos (supuesto del equipo) |
| No se puede reconstruir una decisión del sistema para el cliente regulado | Media | Alto | Trazas y registro por diseño, nivel de autonomía documentado | Si no se reconstruye una decisión desde las trazas, no pasa el gate de seguridad |
| El caso de producto depende de lo que el cliente permita | Alta | Medio | Matriz de restricciones primero; piloto en producto propio | Ningún cliente de la matriz habilita IA a fin de Q3: el frente (a) queda en piloto propio |
| Con el producto diferido, el piloto arranca en T3 sin preparación específica en T2 | Alta, si G2 libera P | Medio | La base de T2 (gateway, harness v1, suite de evals, aislamiento) es reutilizable; lo propio del caso (dataset sintético, integración, diseño) se hace en las primeras 3-4 semanas de T3. Las 6 semanas del SLO se cuentan desde que el piloto opera, así que G4 decide con menos evidencia | El piloto no opera a la semana 6 de T3: G4 decide sin SLO medido, y P se corta o se pasa al año 2 |
| El contractor concentra evals, harness y la prueba de portabilidad | Media | Alto | Documentación por entregable, traspaso en T4 ([Anexo D](04-personas-cultura.md)), suite y lote versionados en el repo | Un entregable de T2 sin documentación reproducible: no cuenta para G2 |

## Decisiones

### Build, buy o partner por capacidad

Criterio: los cuatro ejes de M1U2 (costo total, tiempo hasta el primer valor,
capacidad interna, control) y el control como criterio legal
([ficha](../../material/conceptos/m1u2-build-buy-agentificar.md)). BAIC solo
plantea propietario frente a open source; el partner es criterio del plan
([ficha](../../material/frameworks/baic-perfiles-tecnologia.md)).

| Capacidad | Decisión | Por qué (ejes) | Alternativa descartada | Reversible |
|---|---|---|---|---|
| Modelos fundacionales | **Buy** vía API, ≥ 2 proveedores | Tiempo y capacidad: no se entrena | Entrenar o ajustar un modelo propio: sin datos de cliente utilizables | Sí |
| Gateway, ruteo y registro de costo | **Agentificar**: ensamblar sobre piezas abiertas | Control: es donde se aplican nivel de dato, cliente y costo | Comprar una plataforma cerrada: lock-in en el punto de control | Sí |
| Agentes de código y asistentes internos | **Buy** la herramienta, **build** el contrato, skills y compuertas | Lo diferencial es el contrato de agente, no el producto | Atar el flujo a funciones exclusivas | Sí |
| Orquestación para casos del producto | **Agentificar**: framework y runtime abiertos (clasificación del curso, a reverificar) | Control y trazabilidad | Caja negra de un proveedor | Parcial |
| Retrieval y almacén vectorial | **Buy** gestionado sobre la nube existente | Tiempo y capacidad | Operar uno propio | Sí |
| Evals, trazas y observabilidad | **Buy** u open source; **build** los datasets de evals | Los datasets propios son el activo | Evals del proveedor | Sí |
| Enmascarado de PII y DLP | **Buy** u open source | Capacidad interna escasa | Desarrollo propio | Sí |
| Modelo en infraestructura propia (on-premise) | **Partner o diferir** hasta el gate de Q4 | Hoy es una opción exploratoria de la propuesta al Directorio ([ficha](../../context/hechos/ia-en-producto-y-oferta.md)) | Comprometer hardware ya | **No** (capex) |
| Programa de partners del proveedor de modelos | **Seguir la aplicación sin ponerla en el camino crítico** | Exige certificaciones y despliegues productivos que aún no existen | Condicionar la arquitectura al programa | Sí |

### Puertas de un solo sentido

Cada decisión se separa en aprobación interna, negociación no vinculante y
compromiso. Ninguna excepción contradice la regla del horizonte: **en los 12
meses ningún dato productivo de cliente va a un modelo**.

| Decisión | Tipo | Regla, fecha mínima y autoridad |
|---|---|---|
| Elegir modelo, vector store, herramienta de evals o prompts | Reversible | Cambiar detrás del gateway, con la suite de evals como árbitro. Decide la arquitectura (responsable humano pendiente) |
| Texto tipo de cláusula de IA (aviso BCRA, no entrenamiento, ubicación de datos) | Reversible | Aprobación interna en T3 por governance; sin cliente |
| Conversar la cláusula con un cliente | Reversible | Desde T3, **sin firma, sin datos y sin compromiso**; lo conduce comercial con governance |
| Firmar un compromiso contractual de IA con un cliente | **Irreversible** | No antes de G4; aprueba el Council de [Anexo C](03-gobierno-seguridad.md) |
| Enviar datos productivos de un cliente a un modelo | **Irreversible** | Prohibido durante los 12 meses, sin excepciones; pilotos con datos sintéticos o anonimizados. Una excepción posterior (año 2) exige cláusula firmada y matriz completa |
| Ajustar un modelo con datos de cliente | **Irreversible** | Fuera del horizonte del plan |
| Compra de hardware o compromiso de consumo mayor a 12 meses | **Irreversible** | No antes de G4; evaluar con el escenario de consumo |
| Subir un agente a L3 en producto, o a L4 fuera de sandbox | **Irreversible** | No antes de G4; un agente con efectos externos (por ejemplo, pagos) queda fuera del plan. Decide el Council |

### Dependencia del proveedor y estrategia de salida

Se mide la dependencia con lo que hay: ~90% de los eventos del agente de código
sale de una sola herramienta, 58% del piloto chocó con el límite del plan y parte
de los participantes pidió consumo multimodelo
([ficha](../../context/hechos/encuesta-y-pilotos-ia.md)). Recomendación: **neutralidad
al modelo** (supuesto vigente) comprobada con un ensayo, no declarada.

1. Contrato de agente, skills y hooks sin funciones exclusivas de un proveedor.
2. Gateway con al menos dos proveedores operativos.
3. Prueba de portabilidad y costo en Q2 (ver Evidencia): el caso de referencia
   corre en dos modelos, se mide el esfuerzo de migrar en días-persona y, en la
   misma prueba, *fc* × *s*. Reemplaza el "costo moderado" supuesto por un dato.
4. Sin compromisos de volumen mayores a 12 meses antes del gate de Q4.

### Recurso de IA aplicada: T1 y el contractor

El esfuerzo técnico necesita una fracción de IA aplicada (evals, harness,
gateway): 0,3 FTE en T1 y 0,8 en T2-T4. El contractor **reemplaza** esa
fracción, no la complementa: en eso coinciden este anexo, el
[Anexo D](04-personas-cultura.md) y el [Anexo E](05-business-case.md). Lo que
sigue abierto es la vía de T1:

| Vía de T1 | FTE clave de este anexo en T1 | Caja | Condición |
|---|---|---|---|
| Contractor al 50% desde T1 (B1 de D; **base** de E y de este anexo) | 0,6 (arquitecto y DevOps/QA) | Contractor de T1 ([Anexo D](04-personas-cultura.md)) | El Directorio lo aprueba en G0, por la restricción de no contratar |
| Rol interno de Tecnología, 0,3 FTE | 0,9 | Ninguna | Antes de G0, la dirección técnica demuestra por rol experiencia en evals y harness. Usar agentes de código (~7 de 10, [ficha](../../context/hechos/uso-ia-interno.md)) no lo prueba (supuesto del equipo) |

Este anexo adopta B1 como base porque el recurso que no entra es el tiempo de
las personas clave, no la caja (E, "Contra el sobre de tiempo"). Si G0 no aprueba
ninguna de las dos vías, el gateway y las evals pasan a T2 y T1 queda en
inventario, línea base y matriz de superficies.

Para T2-T4, sin el frente producto (los desarrolladores senior son de P, ver
"Insumos para Finanzas"), quedan dos alternativas. La de sumar el contractor a
la fracción interna se descartó: pagaba dos veces la misma capacidad, y E ya
consolida el contractor como reemplazo.

| Alternativa | Caja | Tiempo interno de la base (T2 / T3 / T4) | Comentario |
|---|---|---|---|
| A. El contractor reemplaza la fracción interna (**recomendada**) | Contractor ([Anexo D](04-personas-cultura.md)) | 1,2 / 1,5 / 1,4 FTE, con el replan de T2 | La más barata en tiempo; concentra el conocimiento en una persona externa, así que exige documentación y traspaso |
| C. Sin contractor, fracción interna de 0,8 FTE | Ninguna | 2,3 / 2,3 / 2,2 FTE, **solo de este anexo** | Respeta la restricción literal, pero no entra en el sobre: suma 0,8 FTE clave por trimestre sobre un plan que ya está en 2,2-2,5. Sin el contractor tampoco existe el replan de T2 |

### Exceso de T2 con el producto diferido

Con el producto diferido, T2 pide 2,5 FTE clave contra un máximo de 2,25
([Anexo E](05-business-case.md)). De esos 2,5, 1,5 son de este anexo (0,5
arquitecto y 1,0 DevOps/QA) y 1,0 de los anexos C y D. Se miró qué hace cada
fracción en T2 y qué condición de G2 sostiene: bypass, red team interno,
portabilidad y FinOps.

| Salida | Qué cambia | FTE clave de T2 | Costo | Qué arriesga |
|---|---|---|---|---|
| **1. Replan de B (recomendada)** | Arquitecto 0,5 → 0,4: el 0,1 era el diseño del piloto de producto, que con P diferido pasa a T3. DevOps/QA 1,0 → 0,8: el pipeline de evals en CI y la reejecución de la prueba de portabilidad pasan al contractor, que tiene 0,2 FTE pagados y sin asignar (cubre la fracción de 0,8 con una persona al 100%, D) | 2,2: entra, con 0,05 de holgura | Baja el tiempo de T2 en ~5 mil (3,2-7,5) y no suma caja | Más concentración en el contractor (ver Riesgos). El piloto, si G2 lo libera, arranca sin diseño previo. Las condiciones de G2 no se tocan: bypass, gateway y FinOps quedan en DevOps/QA |
| 2. Excepción acotada en G0 | El board aprueba 0,3 FTE clave por encima del sobre en T2 | 2,5 | Sin costo nuevo: ya está en el cuadro de E. Salen ~3-7 mil de horas facturables | Rompe el sobre que el propio plan pide confirmar. Cubre solo la falta del 0,2 adicional; sin contractor no alcanza (ver la tabla de contingencias abajo y [Anexo E](05-business-case.md), "Dos contingencias del contractor") |
| Descartada: correr hitos de T2 a T3 | Portabilidad o FinOps pasan a T3 | 2,2 | — | G2 queda sin dos de sus condiciones, y T3 no tiene holgura (0,05) |

**Recomendación:** la salida 1, que el board ratifica en G0 junto con el piso de
capacidad. Lo decide el board; este anexo no da el exceso por resuelto hasta esa
decisión. La salida 2 cubre **una sola** contingencia, y no hay que confundirla
con la otra:

| Contingencia | Qué falta | T2, solo este anexo | Respuesta de este anexo |
|---|---|---|---|
| Sin el 0,2 | El contractor existe, pero su 0,2 no está libre (alcance no acordado, o documentación atrasada, [Anexo D](04-personas-cultura.md)) | 1,5 FTE (sin replan) | Salida 2: la excepción de 0,3 lleva T2 a 2,5 y lo cubre |
| Sin contractor | Toda la IA aplicada de T2-T4 (0,8 FTE), no solo el 0,2 | 2,3 FTE con la fracción interna (alternativa C); 1,2 en modo control | La excepción de 0,3 **no alcanza** para C. La contratación es condición de inicio de los hitos de IA aplicada: sin contractor ni rol interno demostrado, no inician el harness v1, la suite de evals en CI ni la prueba de portabilidad y costo. T2 corre en **modo control** (gateway en laboratorio, bypass por superficie, FinOps) con 1,2 FTE de este anexo: arquitecto 0,4 y DevOps/QA 0,8, porque el 0,2 de evals en CI y reejecución de la prueba tampoco corre. G2 decide sin cobertura de precio (la palanca sale del deck) y sin caso de referencia en sombra, que pasa a T3 si en G2 se aprueba la vía. Infraestructura de T2: en los regímenes (a) y (c) el agente es el tráfico del gateway y el renglón se mantiene; en el (b) el gateway solo ensaya el ruteo con tráfico sintético y el renglón baja al nivel de T1-b (500-1.500 en el trimestre, supuesto del equipo) |

Con la fracción interna de C, el [Anexo E](05-business-case.md) ("Dos
contingencias del contractor") calcula para el plan completo ~3,3 / 3,0 / 2,9 FTE
clave en T2-T4, contra un máximo de 2,25: por eso los hitos de IA aplicada no se
inician sin contractor (ni rol interno demostrado en T1 con contractor desde T2).
Este anexo aporta sus 2,3 / 2,3 / 2,2 y no adopta un total propio. En T3-T4, el
modo control mantiene la base de este anexo (1,5 / 1,4 FTE) sin caso de
referencia ni evals hasta que se apruebe una vía; el total con C y D lo calcula E.
En modo control el gateway opera para control y telemetría (ruta del agente en
los regímenes a y c); lo que no inicia es el ruteo a modelos más baratos y la
caché, que son parte de la prueba de portabilidad y costo. El modo control es la
respuesta que este anexo recomienda para "sin contractor"; la alternativa C queda
como opción del board solo si aprueba explícitamente el exceso que E calcule.

### Tensiones con otras miradas (abiertas, sin consenso inventado)

| Tensión | Mirada A | Mirada B | Qué resuelve |
|---|---|---|---|
| Costo | La meta de +20% de throughput depende de agentes cuyo consumo real es 12× lo pagado | El borrador de OKR pide gasto de tecnología < 3,5% de la facturación, y hoy es ~4% | `finance`: si el precio migra a consumo, el ahorro de horas se come en tokens; hay que mostrar el neto |
| Gobierno | La política sigue en borrador y la matriz de restricciones por cliente no existe | El ruteo por clasificación y el piloto de producto dependen de ambas | `governance`: ratificación y matriz antes de Q3 |
| Personas | Reasignar 10-15% del tiempo de pocas personas clave | Utilización 83-90% y bench < 1 FTE; restricción de no contratar | `people`: suplentes y capacidad; el especialista de IA se capacita, se reasigna o se contrata por contrato |
| Alcance | La plataforma sirve a dos frentes | Qué caso concreto va en el producto lo define el portfolio | `caio`: este anexo no elige el caso |
| Cobertura | [Anexo C](03-gobierno-seguridad.md) (D9, Q2) y [F](06-roadmap-riesgo.md) (G2) exigen ≥ 90% de los eventos del agente de código por la pasarela, sin condición | Este anexo adopta el denominador de C, pero condiciona el 90% al régimen comercial: en el régimen (b) el agente no se enruta y se le exige control verificado sin gateway; los casos propios van al 100%, aparte | `governance` y `caio`: adoptar la "Política de ruteo" o discrepar a la vista. El bloqueo de secretos y de datos Restringidos no pasa a monitoreo en ningún caso |
| Precio | El deck y la defensa usan el gateway como cobertura del cambio de precio | La cobertura no está medida: depende de *fc* × *s*, de la suscripción y de la calidad | `caio`: la palanca se afirma solo si pasa la prueba de portabilidad y costo de T2 |
| Capacidad | T1-E pide 1,6 FTE clave y 590 h distribuidas ([Anexo E](05-business-case.md)); T1 entra si el board confirma ese piso | Con el producto diferido, T2 excede el sobre en ~0,3 FTE; sin contractor, el plan pediría ~3,3 FTE clave (E) | El board, en G0: replan de B (recomendado) o excepción acotada para "sin el 0,2"; modo control para "sin contractor" (ver "Exceso de T2") |

## Roadmap técnico a 12 meses

Q1 = meses 1-3 del plan (T1 en los otros anexos); G1 a G4 cierran cada
trimestre. Q1 absorbe la fase de diagnóstico de los primeros 100
días ([ficha](../../material/conceptos/m1u2-plan-100-dias.md)). Responsable humano de
todos los hitos: **pendiente**. Los criterios de abandono siguen el patrón
kill/scale del curso ([ficha](../../material/conceptos/m1u2-kill-scale-gates.md)).
**Solo Q1 se autoriza en G0**; las filas de Q2 a Q4 son la secuencia prevista y
se liberan gate por gate.

### Pedido a G0 (parte técnica)

| Elemento | Qué se pide |
|---|---|
| Qué se autoriza | Los hitos de Q1, en su versión acotada (T1-b, abajo) |
| Capacidad máxima de este anexo | 0,6 FTE clave con el contractor B1 (0,9 con el rol interno). El sobre del plan completo y su piso (1,6 FTE clave) los cierra el [Anexo E](05-business-case.md) |
| Caja de este anexo | Infraestructura de telemetría y registro, USD 500-1.500 en el trimestre; el tope total de T1 lo fija el Anexo E |
| Entregables | Inventario de datos, línea base congelada, matriz superficie→control→telemetría, telemetría unificada, matriz de restricciones por cliente |
| Decisiones delegadas | Elegir herramientas y proveedores detrás del gateway (reversible), a la dirección técnica |
| Condiciones de G0 | Vía de IA aplicada aprobada (B1, o rol interno demostrado); disponibilidad de historial de PR, integración continua y tickets para la línea base; salida para el exceso de T2 (replan de B o excepción) |
| Fuera del pedido | Q2 a Q4, el modelo propio, cualquier compromiso mayor a 12 meses y todo compromiso contractual con clientes |

**T1-a y T1-b.** T1-a pone el gateway en laboratorio con dos proveedores ya en
el primer trimestre. T1-b, recomendado, difiere el gateway al inicio de Q2 y
conserva inventario, línea base, matriz de superficies y telemetría. El
[Anexo F](06-roadmap-riesgo.md) ya ubica el gateway en T2. Comparadas con la
**misma** provisión de IA aplicada (insumo para la justificación de los 100 días
de F; los otros anexos suman 1,0 FTE clave en T1, [Anexo E](05-business-case.md)):

| Provisión de IA aplicada | T1-b: este anexo / total clave | T1-a: este anexo / total clave | Diferencia de T1-a |
|---|---|---|---|
| Contractor B1 | 0,6 / 1,6 | 0,8 / 1,8 | +0,2 FTE clave; infraestructura +1-3 mil de caja (por mes en lugar de por trimestre) |
| Rol interno | 0,9 / 1,9 | 1,3 / 2,3 | +0,4 FTE clave; ídem caja |

Con el contractor y en la lectura separada de E (solo FTE clave), T1-a entra en el
máximo de 2,25: la capacidad no lo descarta por sí sola. En la lectura estricta
(clave más horas distribuidas) no entra ninguna de las dos: 3,0 contra 2,8 de T1-E. Lo descartan la atribución (base congelada en las semanas 1-4 y rampa 0% en
T1) y que el gateway en laboratorio no produce valor medido sin harness ni evals,
que son de T2. Que la caja de T1-a entre en el techo de T1 lo verifica E.

### Calendario de prerrequisitos (T0 y T1)

Los anexos B, C, D y F ubican en lugares distintos la línea base, la ratificación
y el estudio de la matriz. Desde la arquitectura, la propuesta es:

| Cuándo | Qué | Costo |
|---|---|---|
| Antes de G0 (T0, cuarto trimestre de 2026) | Verificar que existe historial utilizable de PR, integración continua, incidentes y tickets de los últimos dos trimestres (1 día-persona, supuesto del equipo) y extraer la **serie retrospectiva**, que sirve para estimar tendencia y ruido, no como base de atribución. Es un costo previo propuesto: el [Anexo E](05-business-case.md) lo consolida y G0 lo autoriza, o lo ratifica si consta la ejecución | ~USD 0,1-0,4 mil de tiempo de este anexo |
| T1, semanas 1-4 | **Base prospectiva congelada**, con la unidad de la sección "Throughput", antes de cualquier formación o herramienta nueva (formación intermedia de Tecnología y gateway); se fecha y no se edita | Dentro de la fracción de DevOps/QA de T1 (3-5 días-persona, supuesto del equipo) |
| T1, semanas 5-13 | Matriz de superficies y telemetría unificada; medición contra la base, con control concurrente donde exista. **La ganancia no se atribuye antes de T2** (la rampa base es 0% en T1) | Dentro del esfuerzo de T1 |

La serie retrospectiva y la base prospectiva no se mezclan: la primera estima
ruido, la segunda es el punto de partida. **Regla de respaldo:** si en la semana 4
la dispersión de la base prospectiva supera la tendencia que se espera medir
(umbral a fijar con la serie de T0), la oficina del CAIO puede adoptar la serie
retrospectiva como base, como prevé F, dejando constancia. Si el historial no
alcanza, la ganancia no se atribuye (ver el hito de línea base).

La columna "Fr." usa las letras del [Anexo E](05-business-case.md): **B** base
común, **I** frente interno, **P** frente producto (solo si G2 lo libera).

| Trim. | Fr. | Hito | Criterio de éxito | Condición de abandono |
|---|---|---|---|---|
| Q1 | B | Inventario de datos internos con dueño, calidad y nivel | Toda fuente del caso de referencia está inventariada | Sin dueño para una fuente: queda fuera de los casos |
| Q1 | I | Base prospectiva de throughput, incidentes y retrabajo congelada en las semanas 1-4 (serie retrospectiva de T0 para estimar ruido) | Unidad, cohorte y fórmula de la sección "Throughput"; numerador y denominador; versión congelada con fecha | Sin historial utilizable de al menos dos trimestres: la ganancia no se atribuye y se elimina el resultado clave (regla del OKR) |
| Q1 | B | Matriz superficie→control→telemetría y denominador de la cobertura | Las cuatro superficies con ruta, control y telemetría declarados; denominador armado con datos de administración | Una superficie sin telemetría posible: se declara no medible y la meta de cobertura no la incluye |
| Q1 | I | Telemetría unificada de chat, terminal y Workspace | Uso por persona activa y por resultado | Sin exportación del proveedor: encuesta trimestral, marcada como estimada |
| Q1 | P | Matriz de restricciones contractuales por cliente (con comercial y `governance`) | Cobertura de los clientes que concentran la facturación | Sin matriz, no hay piloto de producto |
| Q2 | B | Gateway en laboratorio con 2 proveedores y registro de costo | Tráfico del caso de referencia registrado por llamada, nivel y centro de costo | Más de un trimestre sin operar: se compra una solución |
| Q2 | B | Prueba de integración y de bypass por superficie | Cobertura de control = 100% de las superficies aprobadas; casos propios 100% por gateway; agente de código ≥ 90% por gateway solo en los regímenes (a) y (c) de la "Política de ruteo"; en (b), ruteo ensayado y no activado | Superficie con bypass sin control compensatorio: queda declarada no cubierta y se lleva al Council |
| Q2 | B | Harness v1 sobre el caso de referencia: working set con presupuesto, memoria externa, gate humano, ledger | Pasa los gates de rendimiento y seguridad de la ficha de evaluación | Dos fallas de contexto críticas sin mitigar: se reduce el alcance |
| Q2 | B | Suite de evals en CI con el dataset v1 y trazas | Cada release corre la suite; la tupla de versión queda registrada | Sin dataset utilizable: el caso queda en L0 |
| Q2 | B | Prueba de portabilidad y costo del gateway | Mide *fc*, *s*, calidad, suscripción y días-persona; resultado en el paquete de G2 | Migrar cuesta más de 20 días-persona, o no hay lote reproducible: no se afirma cobertura de precio |
| Q2 | B | FinOps: costo por persona activa, por consulta del caso y por resultado, con escenario de consumo | Reporte mensual con el escenario de consumo | Costo fuera del techo de Finanzas: se frena la expansión |
| Q3 | I | Caso de referencia en L2 para Tecnología y Operaciones | L2 en la cohorte con los gates de rendimiento, seguridad y ético; extensión a Operaciones con el de impacto | Falla dura de seguridad: se apaga el caso. Impacto debajo al vencer la espera: no se extiende |
| Q3 | I | Extensión a staff y a equipos asignados a clientes, donde el cliente lo permita | Uso semanal medido en el gateway y la telemetría | Restricción del cliente: no se fuerza |
| Q3 | B | Aislamiento por tenant probado (con tenants sintéticos si P no se libera) | Prueba adversarial sin filtración entre tenants | Una filtración: se bloquea el despliegue |
| Q3 | P | Piloto de IA en un producto propio, L1-L2, datos sintéticos | SLOs del caso cumplidos a las 6 semanas desde que opera; trazabilidad completa; cero incidentes de datos | No cumple el SLO a las 6 semanas (plazo ilustrativo del curso): se revisa o se corta |
| Q3 | P | Red team del piloto (con `governance`) | Hallazgos críticos cerrados | Hallazgo crítico sin mitigación: no sale |
| Q4 | P | Gate scale/kill del piloto de producto y paquete de cumplimiento para clientes | Decisión documentada; paquete (inventario, ubicación de datos, no entrenamiento, evidencia) listo | Sin SLO ni apetito del cliente: se corta y se reasigna |
| Q4 | B | Decisión sobre modelo en infraestructura propia | Go/no-go con la matriz de clientes y el escenario de consumo | Sin demanda contractual demostrada: no se compra |
| Q4 | I | Medición de productividad contra la línea base | Tendencia con intervalo por encima de la línea base, sin más incidentes ni retrabajo | Sin mejora, o con más incidentes: se frena la expansión |
| Q4 | B | Revisión de arquitectura y de contratos de proveedor | ADR actualizados; compromisos de volumen alineados al gate | — |

## Insumos para Finanzas

Todo es **supuesto del equipo** salvo donde se indica fuente. USD, rangos. El
esfuerzo es mayormente reasignación (costo de oportunidad contra horas
facturables), no caja incremental. El escenario recomendado es el que consume
el [Anexo E](05-business-case.md): T1-b, contractor B1 que reemplaza la
fracción de IA aplicada y producto diferido. El conservador queda como
comparación.

### Escenario conservador, como comparación (T1-a, contractor que complementa y producto desde T2)

| Concepto | Trim. | Rango | Fuente o supuesto |
|---|---|---|---|
| Esfuerzo técnico: 1,3 FTE equivalentes | Q1 | 15.300-36.750 | 0,3 arquitecto, 0,5 IA aplicada y 0,5 DevOps/QA por 3 meses, a los rangos de [costo por rol](../../context/supuestos/costo-cargado-por-rol.md); las fracciones son supuesto del equipo |
| Esfuerzo técnico: 3,3 FTE equivalentes | Q2 | 35.550-86.400 | 0,5 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,0 desarrollador senior |
| Esfuerzo técnico: 3,8 FTE equivalentes | Q3 | 40.050-97.650 | 0,5 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,5 desarrolladores senior |
| Esfuerzo técnico: 3,2 FTE equivalentes | Q4 | 34.200-83.400 | 0,4 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,0 desarrollador senior |

Suma del esfuerzo técnico: USD 125.100-304.200 en los cuatro trimestres.

### Escenario recomendado (T1-b, contractor B1 que reemplaza, producto diferido)

Los desarrolladores senior son el **frente producto**: construyen e integran el
piloto. Con P diferido, no hay desarrollador en T2, y los de T3-T4 forman parte
del tramo condicional que se libera en G2. Así se confirma la lectura de E.

| Concepto | Fr. | Trim. | Rango | Fuente o supuesto |
|---|---|---|---|---|
| Esfuerzo técnico: 0,6 FTE | B | Q1 | 6.750-15.750 | 0,3 arquitecto y 0,3 DevOps/QA; la IA aplicada la cubre el contractor B1 del [Anexo D](04-personas-cultura.md). Con el rol interno en lugar de B1: 0,9 FTE, 10.800-25.650 |
| Esfuerzo técnico: 1,2 FTE, con el replan de T2 | B | Q2 | 12.600-30.000 | 0,4 arquitecto y 0,8 DevOps/QA (ver "Exceso de T2"). Sin replan: 1,5 FTE, 15.750-37.500 |
| Esfuerzo técnico: 1,5 FTE | B | Q3 | 15.750-37.500 | 0,5 arquitecto y 1,0 DevOps/QA |
| Esfuerzo técnico: 1,4 FTE | B | Q4 | 14.400-34.500 | 0,4 arquitecto y 1,0 DevOps/QA |
| Desarrolladores senior del piloto: 1,5 FTE | P | Q3 | 13.500-33.750 | Solo si G2 libera P |
| Desarrollador senior del piloto: 1,0 FTE | P | Q4 | 9.000-22.500 | Solo si G2 libera P |

Suma de la base: USD 49.500-117.750 con el replan (52.650-125.250 sin él). Tramo
P: 22.500-56.250. A los rangos de [costo por
rol](../../context/supuestos/costo-cargado-por-rol.md), con 3 meses por
trimestre. El contractor (caja, Anexo D) no se repite acá. Sin contractor
(alternativa C), la base suma 0,8 FTE de IA aplicada interna por trimestre en
T2-T4 y no hay replan de T2.

### Caja y otros costos

| Concepto | Trim. | Rango | Fuente o supuesto |
|---|---|---|---|
| Suscripciones de IA (base) | Cada trim. | 5.800-9.450 | 60-70 seats × USD 40-45 × 3 meses. La ficha no aclara si el promedio ponderado cubre a la vez Claude y Copilot: el piso resta 20% por si Copilot cuesta menos (supuesto del equipo); sin seats nuevos. No es incremental. Cálculo sobre [la ficha](../../context/hechos/costos-tecnologia-e-ia.md) |
| Escenario de consumo a precio API (estrés) | Cada trim. | hasta ≈ 58.000-73.000 | 12× la suscripción del agente de código (40-45 seats × USD 40-45 × 3 meses). Es cota superior: el 12× es una estimación de telemetría, no una factura, y vale solo para el agente de código |
| Infraestructura nueva (gateway, retrieval, trazas, evals en CI) | Q1 | T1-b: 500-1.500 **en el trimestre**. T1-a: 500-1.500 **por mes** (1.500-4.500 en el trimestre) | [Supuesto](../../context/supuestos/precios-externos-sin-cotizar.md): T1-b solo tiene telemetría y registro; T1-a, gateway en laboratorio. Lo invalida una cotización o un precio de servicios gestionados |
| Ídem | Q2 | 4.500-12.000 | USD 1,5-4 mil por mes. Incluye, con tope de FinOps, el consumo de la prueba de portabilidad y costo y el del caso de referencia |
| Ídem, base sin piloto | Q3-Q4 | 4.500-12.000 cada uno | Sin piloto, la infraestructura queda en el nivel de Q2 (USD 1,5-4 mil por mes), como registra la [ficha de precios](../../context/supuestos/precios-externos-sin-cotizar.md). El consumo del caso de referencia entra dentro de este tope; si no entra, el caso se limita a una cohorte |
| Ídem, incremento del piloto | Q3-Q4 | 1.500-6.000 cada uno (P) | Tenant del piloto y su tráfico: lleva el renglón a 6.000-18.000 por trimestre, el valor con piloto de la [ficha](../../context/supuestos/precios-externos-sin-cotizar.md) |
| Consumo de modelos del piloto de producto (evals y tráfico) | Q3-Q4 | 3.000-12.000 cada uno (P) | Supuesto del equipo: USD 1-4 mil por mes; sin base de volumen hasta el piloto |
| Red team del piloto | Q3 | 5.000-15.000 (P) | Supuesto del equipo: un ejercicio con un tercero chico; lo invalida una cotización; coordinar con `governance` |
| Prueba de portabilidad y costo del gateway | Q2 | Sin renglón propio | El tiempo va dentro de DevOps/QA y del contractor; el consumo por API, dentro del renglón de infraestructura de Q2, con tope de FinOps |
| Migración de superficies y pruebas de bypass | Q1-Q2 | 2.100-10.700 de tiempo | 15-30 días-persona de DevOps/QA a USD 3.000-7.500 por mes y 21 días hábiles; **ya incluido** en las fracciones de DevOps/QA, no suma |
| Instrumentación de uso en chat y Workspace (la dependencia que marca el Anexo D) | Q1-Q2 | 1.400-7.100 de tiempo | 10-20 días-persona de DevOps al mismo costo diario; ya incluido en DevOps/QA, no suma. Sin cotización de proveedores |
| Certificaciones del programa de partners | — | No estimado | Faltante: no hay costo en `context/` |

**Régimen del año 2.** Si la infraestructura de Q4 sin piloto queda en el nivel
de Q2, a régimen cuesta 18.000-48.000 por año en lugar de 24.000-72.000. Los
6.000-24.000 de diferencia son del producto. El [costo de
régimen](../../context/supuestos/costo-de-regimen-del-ano-2.md) ya usa el valor sin
piloto para la base común.

**Base común mínima para P (corte mixto en G3).** Este anexo confirma, con una
corrección, el supuesto de E ([base
mínima](../../context/supuestos/base-minima-tras-un-corte.md)):

- **Confirma:** infraestructura de base al nivel de T2 (gateway, trazas y evals en
  CI, 4.500-12.000 en T4, cota superior porque ya no corre el caso de referencia),
  la pasarela, el contractor al 50% para las evals y el harness del piloto (sin
  dato que lo respalde) y 0,5 FTE de DevOps/QA para operar el gateway y las evals.
- **Corrige:** suma **0,1 FTE de arquitecto** en T4 (1.350-3.000 de tiempo, a
  los rangos de este anexo). El piloto sigue con el gate scale/kill y el paquete
  de cumplimiento de Q4 (aislamiento por tenant, ubicación de datos, ADR), que
  tocan puertas de un solo sentido; sin arquitecto no hay quién firme esa
  evidencia. El resto del arquitecto (decisión de infraestructura propia y
  revisión de contratos) se corta con la base común.
- Sigue siendo supuesto: lo recalcula E.

Los porcentajes sobre facturación los calcula Finanzas: `context/` no publica
montos de facturación.

## Insumos para el deck

- **Arquitectura en una imagen:** un gateway neutral al modelo, aislamiento por
  cliente y un harness con evals y gates. Dos frentes sobre la misma base. Con
  una salvedad visible: tres de las cuatro superficies de IA de hoy pueden no pasar
  por el gateway, y el agente de código pasa solo si eso no rompe la suscripción
  plana. Las que no pasan se cubren con control compensatorio verificado; los
  casos propios, siempre por gateway.
- **Qué pedimos al board (un solo pedido, G0):** autorizar T1 en su versión
  acotada (T1-b) con tope de caja y de capacidad, y adoptar el marco de gates. Q2
  es dirección de diseño y se libera en G1; el piloto de producto, además, depende
  de la matriz de restricciones, de la política ratificada y de la señal de
  cliente en G2. G0 también decide la salida para el exceso de ~0,3 FTE de T2.
  **No** se aprueba el modelo propio ni compromisos mayores a 12 meses.
- **Mensaje al CFO:** la IA ya es una línea propia del gasto de tecnología y
  el consumo real es un múltiplo de la suscripción. Se presupuesta el escenario de
  consumo y se prueba la salida de proveedor, no se declara. La cobertura de
  precio del gateway es una hipótesis que la prueba de T2 confirma o descarta en
  G2. La ganancia de throughput se valúa como horas evitadas a output fijo, no
  como caja.
- **Riesgo que hay que nombrar:** el piloto de producto tiene hipótesis elegida
  (asistente de integración, Anexo F) pero ningún cliente que lo habilite
  todavía; el plan lo trata como hipótesis con gate. Y
  evals, harness y la prueba de portabilidad se concentran en un contractor.
- **Evidencia que falta:** línea base de productividad, matriz por cliente,
  primera corrida de la ficha de evaluación y la medición de *fc* × *s*; no se
  prometen números de calidad ni de ahorro hasta tenerlos.

## Cautelas

- Los hechos de Acme Labs vienen de fichas en `draft` de [context/](../../context/index.md);
  ninguna está `verified`, así que no hay cifra de este anexo lista para la entrega.
- El 12× es una estimación a precio API; el ahorro por inferencia no lleva
  porcentaje por falta de fuente primaria.
- La clasificación de productos de las tres capas del harness y las herramientas
  de PII del curso no están verificadas con fuente primaria
  ([capas](../../material/conceptos/harness-tres-capas.md)): sirven como marco, no
  como recomendación de proveedor.
- Qué regiones o proveedores cumplen la residencia exigida por la Ley 25.326 para
  un cliente concreto es un faltante que decide legal; el anexo no lo afirma.
- La escala L0-L4 es una herramienta pedagógica del curso, no un estándar.
- La definición de throughput, la conversión a horas evitadas, la cobertura por
  superficie y el calendario de T0 y T1 son propuestas de este anexo: el
  Anexo E, el C, el D y el F deben adoptarlas o discrepar a la vista. Qué
  superficie es enrutable no está verificado con documentación de proveedor.
- Las fracciones de esfuerzo y los rangos de infraestructura son supuestos del
  equipo. Los umbrales de la ficha de evaluación, el criterio de la prueba de
  portabilidad y costo y el replan de T2 están en una
  [ficha](../../context/supuestos/umbrales-tecnicos-propuestos.md) en `draft`, igual
  que la política de ruteo, el gate de impacto y el método del intervalo de
  throughput. El régimen comercial del agente de código depende de una respuesta
  escrita del proveedor que todavía no existe.
- El caso de referencia es el del frente interno y prueba el método que
  reutiliza el piloto de producto; la hipótesis de producto la eligió el
  portfolio de `caio` (Anexo F). El tamaño del dataset (~200 preguntas) es una propuesta sin
  cálculo de potencia estadística.
- Que el contractor tenga 0,2 FTE sin asignar en T2 sale de leer juntos B
  (fracción de 0,8) y D (una persona al 100%); `people` lo tiene que confirmar.
