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
trimestre construye base y el producto entra recién en el tercero.

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
| No existe hoy un gateway de modelos ni un inventario formal de arquitectura | — | Supuesto del equipo: no consta en [stack](../../context/hechos/stack-y-plataforma.md); lo invalida cualquier inventario que lo contradiga |

## Evidencia

### Arquitectura de referencia (Agente = Modelo + Harness)

La tesis de la cursada es que "el chatbot solo demuestra; la solución es el
harness" ([unidad](../../material/unidades/memoria-contexto-harness.md)). Se
mapean los siete componentes del harness
([ficha](../../material/conceptos/harness-agente-modelo-mas-harness.md)) a lo que
Acme Labs ya tiene y a lo que falta.

| Componente | Estado objetivo | Punto de partida |
|---|---|---|
| Modelos y gateway | Capa única que enruta por clasificación de datos y por cliente, con ≥ 2 proveedores detrás y registro de uso y costo | Sin gateway (supuesto); herramientas por suscripción |
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
| Terminal y agente de código (Claude) | Gateway, si el agente acepta un endpoint configurable | Allowlist, DLP sobre prompts, escaneo de secretos, nivel de dato, *hooks* de permisos | Gateway por llamada, más la telemetría que ya existe | Enrutable, a probar |
| Chat y escritorio (Claude, plan Team) | Directa a la aplicación del proveedor | Administración del plan (acceso único, retención, uso de datos) y bloqueo de datos Restringidos en navegador o equipo, si el parque lo permite | Reportes de administración del plan; encuesta si no hay exportación | No enrutable; control compensatorio |
| IDE (Copilot) | Directa; enrutable solo si admite proxy corporativo | Administración de la organización: repositorios y contenido excluidos, política de datos del proveedor | Métricas de uso de la organización | A probar |
| Correo, documentos y reuniones (Gemini en Workspace) | Dentro de Workspace | Administración de Workspace: DLP y controles de datos del dominio | Registros de auditoría de administración | No enrutable; control compensatorio |
| Casos propios (producto y agentes internos nuevos) | Solo por gateway | Todos los anteriores más aislamiento por tenant | Gateway | Enrutable por diseño |

**Denominador.** Se reportan siempre dos números. (1) *Cobertura de ruta*: eventos
que pasan por el gateway sobre eventos totales de las cuatro superficies, con los
totales tomados de los reportes de administración de cada herramienta (si una no
exporta, su uso se estima por encuesta y se marca "estimado"). (2) *Cobertura de
control*: superficies con un control verificado por prueba sobre las cuatro. Meta
propuesta: (2) = 100% al cierre de Q2; (1) ≥ 90% **solo para el agente de código y los
casos propios** (la ficha ubica ~90% de sus eventos en la terminal, que es la cota
de lo enrutable). Para el total, la meta se fija en G1 cuando exista el
denominador. Esto difiere del "90% del uso con seats corporativos" de
[Anexo C](03-gobierno-seguridad.md): ver Tensiones.

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

### Métricas técnicas (las sostiene este anexo; Finanzas las consume)

| Métrica | Hoy | Esperado a 12 meses | Fuente |
|---|---|---|---|
| Funcionalidades de IA en producción en lo vendido | 0 | 1 piloto acotado evaluado con gate scale/kill (Q3-Q4) | [Ficha](../../context/hechos/ia-en-producto-y-oferta.md) |
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
| Ruido | Con cohortes de pocas decenas de personas, la variación entre trimestres puede superar +3%: se estima con la serie retrospectiva de T0 y los umbrales de G2 y G3 se leen como tendencia con intervalo, no como un punto |

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
  ([ficha](../../material/conceptos/m2u4-evals.md)). Los umbrales se fijan sobre una
  línea base medida en Q1-Q2; hasta entonces ningún número de calidad va a una slide.
- **Ahorro de inferencia:** se usan los mecanismos (ruteo por modelo, caché de
  prefijo estable) **sin porcentaje**: el "60-80%" del curso no tiene fuente primaria
  ([huecos](../../material/huecos.md), [ficha](../../material/conceptos/m2u4-tokenomics.md)).

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
3. Ensayo de portabilidad en Q2: el mismo caso corre en dos modelos y se mide el
   esfuerzo de migrar en días-persona. Reemplaza el "costo moderado" supuesto por un dato.
4. Sin compromisos de volumen mayores a 12 meses antes del gate de Q4.

### Recurso de IA aplicada: T1 y el contractor

El esfuerzo técnico necesita una fracción de IA aplicada (evals, harness,
gateway). El [Anexo D](04-personas-cultura.md) solo prevé el perfil externo
desde T2. Se resuelve por rol y por vía, sin nombres:

| Trimestre | Vía | Condición |
|---|---|---|
| T1 | Rol interno de Tecnología con uso previo de agentes de código (hoy ~7 de 10 los usan, [ficha](../../context/hechos/uso-ia-interno.md)), 0,3 FTE | **Condición de G0**: la dirección técnica confirma, por rol, quién cubre esa fracción. Que alguien use agentes no prueba que sepa diseñar evals ni un harness (supuesto del equipo): si no hay un rol con experiencia demostrada, el gateway se mueve a T2 y T1 queda en inventario, línea base y matriz de superficies |
| T2-T4 | Contractor ([Anexo D, D2](04-personas-cultura.md)) **o** rol interno | Decide el Directorio, por la restricción de no contratar |

Para T2-T4 hay tres alternativas, costeadas en "Insumos para Finanzas":

| Alternativa | Caja | Tiempo interno | Comentario |
|---|---|---|---|
| A. El contractor **reemplaza** la fracción interna de IA aplicada (recomendada) | Contractor ([Anexo D](04-personas-cultura.md)) | Sin la fracción de IA: 2,5 / 3,0 / 2,4 FTE en T2 / T3 / T4 | La más barata en tiempo; concentra el conocimiento en una persona externa, así que exige documentación y traspaso |
| B. El contractor **complementa** la fracción interna | Contractor | 3,3 / 3,8 / 3,2 FTE | Es lo que hoy suma Finanzas por prudencia; paga dos veces la misma capacidad salvo que el contractor haga trabajo distinto |
| C. Sin contractor, fracción interna de 0,8 FTE | Ninguna | 3,3 / 3,8 / 3,2 FTE | Respeta la restricción literal; el tiempo sale de pocas personas con utilización alta, y el riesgo de concentración crece |

### Tensiones con otras miradas (abiertas, sin consenso inventado)

| Tensión | Mirada A | Mirada B | Qué resuelve |
|---|---|---|---|
| Costo | La meta de +20% de throughput depende de agentes cuyo consumo real es 12× lo pagado | El borrador de OKR pide gasto de tecnología < 3,5% de la facturación, y hoy es ~4% | `finance`: si el precio migra a consumo, el ahorro de horas se come en tokens; hay que mostrar el neto |
| Gobierno | La política sigue en borrador y la matriz de restricciones por cliente no existe | El ruteo por clasificación y el piloto de producto dependen de ambas | `governance`: ratificación y matriz antes de Q3 |
| Personas | Reasignar 10-15% del tiempo de pocas personas clave | Utilización 83-90% y bench < 1 FTE; restricción de no contratar | `people`: suplentes y capacidad; el especialista de IA se capacita, se reasigna o se contrata por contrato |
| Alcance | La plataforma sirve a dos frentes | Qué caso concreto va en el producto lo define el portfolio | `caio`: este anexo no elige el caso |
| Cobertura | [Anexo C](03-gobierno-seguridad.md): ≥90% del uso con seats corporativos por la pasarela, y modo monitoreo si cae la actividad | Tres de las cuatro superficies pueden no ser enrutables; el monitoreo podría quitar el bloqueo de datos prohibidos | `governance` y `architect`: meta de ruta solo para lo enrutable, 100% de control verificado, y el bloqueo de secretos y datos Restringidos no pasa a monitoreo |
| Calendario | Versión anterior de este anexo: línea base retrospectiva congelada en el mes 1 de T1 | [Anexo F](06-roadmap-riesgo.md), decisión del CAIO: T0 con verificación y serie retrospectiva; base **prospectiva** congelada en las semanas 1-4 de T1; ganancia atribuida solo contra ella | **Resuelta, este anexo se alinea.** Queda un riesgo a la vista: cuatro semanas de PR pueden ser ruidosas (cohortes de pocas decenas de personas); F prevé usar la retrospectiva como base si la oficina del CAIO lo decide en la semana 4, y este anexo lo respalda con la regla de abajo |
| Valor | [Anexo E](05-business-case.md) valúa la ganancia como costo × ganancia | Con output fijo, la capacidad liberada es g/(1+g) | `finance`: adoptar la lectura A y separar retorno económico del de caja |
| Capacidad | T1 de este anexo pide 1,3 FTE (T1-a) | T1 del plan completo pide 3,5 FTE contra un sobre de ~2,25 | `caio` y `finance`: T1-b baja 0,4 FTE de este anexo, pero no alcanza solo para entrar en el sobre; el resto depende de C y D |

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
| Capacidad máxima de este anexo | T1-b: 0,9 FTE equivalentes; T1-a: 1,3. El sobre del plan completo lo cierra el [Anexo E](05-business-case.md) |
| Caja de este anexo | Infraestructura de laboratorio y telemetría, USD 0,5-1,5 mil en T1-b (1,5-4,5 en T1-a); el tope total de T1 lo fija el Anexo E |
| Entregables | Inventario de datos, línea base congelada, matriz superficie→control→telemetría, telemetría unificada, matriz de restricciones por cliente |
| Decisiones delegadas | Elegir herramientas y proveedores detrás del gateway (reversible), a la dirección técnica |
| Condiciones de G0 | Rol interno confirmado para la fracción de IA; disponibilidad de historial de PR, integración continua y tickets para la línea base |
| Fuera del pedido | Q2 a Q4, el modelo propio, cualquier compromiso mayor a 12 meses y todo compromiso contractual con clientes |

**T1-a y T1-b.** T1-a es el Q1 original de este anexo (1,3 FTE, gateway en
laboratorio con dos proveedores en el primer trimestre). T1-b, recomendado, baja a
0,9 FTE: difiere el gateway al inicio de Q2 y conserva inventario, línea base,
matriz de superficies y telemetría. Cambia una condición de G1 en el
[Anexo F](06-roadmap-riesgo.md) ("gateway registrando costo"), que decide `caio`.

### Calendario de prerrequisitos (T0 y T1)

Los anexos B, C, D y F ubican en lugares distintos la línea base, la ratificación
y el estudio de la matriz. Desde la arquitectura, la propuesta es:

| Cuándo | Qué | Costo |
|---|---|---|
| Antes de G0 (T0, cuarto trimestre de 2026) | Verificar que existe historial utilizable de PR, integración continua, incidentes y tickets de los últimos dos trimestres (1 día-persona, supuesto del equipo) y extraer la **serie retrospectiva**, que sirve para estimar tendencia y ruido, no como base de atribución. El costo de T0 lo consolida el [Anexo F](06-roadmap-riesgo.md) (ratificado en G0) | ~USD 0,1-0,4 mil de tiempo de este anexo |
| T1, semanas 1-4 | **Base prospectiva congelada**, con la unidad de la sección "Throughput", antes de cualquier formación o herramienta nueva (formación intermedia de Tecnología y gateway); se fecha y no se edita | Dentro de la fracción de DevOps/QA de T1 (3-5 días-persona, supuesto del equipo) |
| T1, semanas 5-13 | Matriz de superficies y telemetría unificada; medición contra la base, con control concurrente donde exista. **La ganancia no se atribuye antes de T2** (la rampa base es 0% en T1) | Dentro del esfuerzo de T1 |

La serie retrospectiva y la base prospectiva no se mezclan: la primera estima
ruido, la segunda es el punto de partida. **Regla de respaldo:** si en la semana 4
la dispersión de la base prospectiva supera la tendencia que se espera medir
(umbral a fijar con la serie de T0), la oficina del CAIO puede adoptar la serie
retrospectiva como base, como prevé F, dejando constancia. Si el historial no
alcanza, la ganancia no se atribuye (ver el hito de línea base).

| Trim. | Hito | Criterio de éxito | Condición de abandono |
|---|---|---|---|
| Q1 | Inventario de datos internos con dueño, calidad y nivel | Toda fuente que alimenta un caso de Q2-Q3 está inventariada | Sin dueño para una fuente: queda fuera de los casos |
| Q1 | Base prospectiva de throughput, incidentes y retrabajo congelada en las semanas 1-4 (serie retrospectiva de T0 para estimar ruido) | Unidad, cohorte y fórmula de la sección "Throughput"; numerador y denominador; versión congelada con fecha | Sin historial utilizable de al menos dos trimestres: la ganancia no se atribuye y se elimina el resultado clave (regla del OKR) |
| Q1 | Matriz superficie→control→telemetría y denominador de la cobertura | Las cuatro superficies con ruta, control y telemetría declarados; denominador armado con datos de administración | Una superficie sin telemetría posible: se declara no medible y la meta de cobertura no la incluye |
| Q1 | Telemetría unificada de chat, terminal y Workspace | Uso por persona activa y por resultado | Sin exportación del proveedor: encuesta trimestral, marcada como estimada |
| Q1 | Matriz de restricciones contractuales por cliente (con comercial y `governance`) | Cobertura de los clientes que concentran la facturación | Sin matriz, no hay piloto de producto |
| Q2 | Gateway en laboratorio con 2 proveedores y registro de costo (T1-a lo adelanta a Q1) | Tráfico del piloto registrado por llamada, nivel y centro de costo | Más de un trimestre sin operar: se compra una solución |
| Q2 | Prueba de integración y de bypass por superficie | Cobertura de control = 100% de las superficies aprobadas; ruta ≥ 90% del agente de código y de los casos propios | Superficie con bypass sin control compensatorio: queda declarada no cubierta y se lleva al Council |
| Q2 | Harness v1: working set con presupuesto, memoria externa, gate humano, ledger | Pasa los gates de rendimiento y seguridad con umbrales fijados sobre la línea base | Dos fallas de contexto críticas sin mitigar: se reduce el alcance |
| Q2 | Suite de evals propia en CI y trazas | Cada release del caso corre la suite; resultados versionados | Sin dataset utilizable: el caso queda en L0-L1 |
| Q2 | Ensayo de portabilidad entre proveedores | Un caso corre en dos modelos; se mide el esfuerzo en días-persona | Esfuerzo mayor a 20 días-persona (umbral inicial, supuesto del equipo, se ajusta con la medición) |
| Q2 | FinOps: costo por persona activa y por resultado, con escenario de consumo | Reporte mensual con el escenario de consumo | Costo fuera del techo de Finanzas: se frena la expansión |
| Q3 | Piloto de IA en un producto propio, L1-L2, datos sintéticos o anonimizados | SLOs del caso cumplidos, trazabilidad completa, cero incidentes de datos | No cumple el SLO a las 6 semanas (plazo ilustrativo del curso): se revisa o se corta |
| Q3 | Aislamiento por tenant probado | Prueba adversarial sin filtración entre tenants | Una filtración: se bloquea el despliegue |
| Q3 | Red team del piloto (con `governance`) | Hallazgos críticos cerrados | Hallazgo crítico sin mitigación: no sale |
| Q3 | Extensión interna a Operaciones y staff donde el cliente lo permita | Uso semanal medido en el gateway y la telemetría | Restricción del cliente: no se fuerza |
| Q4 | Gate scale/kill del piloto de producto y paquete de cumplimiento para clientes | Decisión documentada; paquete (inventario, ubicación de datos, no entrenamiento, evidencia) listo | Sin SLO ni apetito del cliente: se corta y se reasigna |
| Q4 | Decisión sobre modelo en infraestructura propia | Go/no-go con la matriz de clientes y el escenario de consumo | Sin demanda contractual demostrada: no se compra |
| Q4 | Medición de productividad contra la línea base | Tendencia con intervalo por encima de la línea base, sin más incidentes ni retrabajo | Sin mejora, o con más incidentes: se frena la expansión |
| Q4 | Revisión de arquitectura y de contratos de proveedor | ADR actualizados; compromisos de volumen alineados al gate | — |

## Insumos para Finanzas

Todo es **supuesto del equipo** salvo donde se indica fuente. USD, rangos. El
esfuerzo es mayormente reasignación (costo de oportunidad contra horas
facturables), no caja incremental. **Cambio respecto de la ronda anterior:** hay
dos versiones de T1 y tres alternativas de IA aplicada; el anexo recomienda T1-b y
la alternativa A, y Finanzas debe recostear. La tabla "Escenario conservador" es
lo que el Anexo E consumía hasta ahora.

### Escenario conservador (T1-a y contractor que complementa)

| Concepto | Trim. | Rango | Fuente o supuesto |
|---|---|---|---|
| Esfuerzo técnico: 1,3 FTE equivalentes | Q1 | 15.300-36.750 | 0,3 arquitecto, 0,5 IA aplicada y 0,5 DevOps/QA por 3 meses, a los rangos de [costo por rol](../../context/supuestos/costo-cargado-por-rol.md); las fracciones son supuesto del equipo |
| Esfuerzo técnico: 3,3 FTE equivalentes | Q2 | 35.550-86.400 | 0,5 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,0 desarrollador senior |
| Esfuerzo técnico: 3,8 FTE equivalentes | Q3 | 40.050-97.650 | 0,5 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,5 desarrolladores senior |
| Esfuerzo técnico: 3,2 FTE equivalentes | Q4 | 34.200-83.400 | 0,4 arquitecto, 0,8 IA aplicada, 1,0 DevOps/QA y 1,0 desarrollador senior |

Suma del esfuerzo técnico: USD 125.100-304.200 en los cuatro trimestres.

### Escenario recomendado (T1-b y contractor que reemplaza, alternativa A)

| Concepto | Trim. | Rango | Fuente o supuesto |
|---|---|---|---|
| Esfuerzo técnico: 0,9 FTE equivalentes | Q1 | 10.800-25.650 | 0,3 arquitecto, 0,3 rol interno de IA y 0,3 DevOps/QA. Incluye la base prospectiva y la matriz de superficies |
| Esfuerzo técnico: 2,5 FTE equivalentes | Q2 | 24.750-60.000 | 0,5 arquitecto, 1,0 DevOps/QA y 1,0 desarrollador senior; la IA aplicada la cubre el contractor del [Anexo D](04-personas-cultura.md) |
| Esfuerzo técnico: 3,0 FTE equivalentes | Q3 | 29.250-71.250 | 0,5 arquitecto, 1,0 DevOps/QA y 1,5 desarrolladores senior |
| Esfuerzo técnico: 2,4 FTE equivalentes | Q4 | 23.400-57.000 | 0,4 arquitecto, 1,0 DevOps/QA y 1,0 desarrollador senior |

Suma del esfuerzo técnico: USD 88.200-213.900. El contractor (caja de 40.500-99.000
según el Anexo D) no se repite acá. La alternativa C (sin contractor) tiene el
mismo tiempo que el escenario conservador y sin caja de contractor.

### Caja y otros costos

| Concepto | Trim. | Rango | Fuente o supuesto |
|---|---|---|---|
| Suscripciones de IA (base) | Cada trim. | 5.800-9.450 | 60-70 seats × USD 40-45 × 3 meses. La ficha no aclara si el promedio ponderado cubre a la vez Claude y Copilot: el piso resta 20% por si Copilot cuesta menos (supuesto del equipo); sin seats nuevos. No es incremental. Cálculo sobre [la ficha](../../context/hechos/costos-tecnologia-e-ia.md) |
| Escenario de consumo a precio API (estrés) | Cada trim. | hasta ≈ 58.000-73.000 | 12× la suscripción del agente de código (40-45 seats × USD 40-45 × 3 meses). Es cota superior: el 12× es una estimación de telemetría, no una factura, y vale solo para el agente de código |
| Infraestructura nueva (gateway, retrieval, trazas, evals en CI) | Q1 | T1-a: 1.500-4.500; T1-b: 500-1.500 | Supuesto del equipo: USD 0,5-1,5 mil por mes con gateway en laboratorio; en T1-b solo telemetría y registro. Lo invalida una cotización o un precio de servicios gestionados |
| Ídem | Q2 | 4.500-12.000 | USD 1,5-4 mil por mes |
| Ídem | Q3-Q4 | 6.000-18.000 cada uno | USD 2-6 mil por mes, con el piloto y su tráfico |
| Consumo de modelos del piloto de producto (evals y tráfico) | Q3-Q4 | 3.000-12.000 cada uno | Supuesto del equipo: USD 1-4 mil por mes; sin base de volumen hasta el piloto |
| Red team del piloto | Q3 | 5.000-15.000 | Supuesto del equipo: un ejercicio con un tercero chico; lo invalida una cotización; coordinar con `governance` |
| Migración de superficies y pruebas de bypass | Q1-Q2 | 2.100-10.700 de tiempo | 15-30 días-persona de DevOps/QA a USD 3.000-7.500 por mes y 21 días hábiles; **ya incluido** en las fracciones de DevOps/QA, no suma |
| Instrumentación de uso en chat y Workspace (la dependencia que marca el Anexo D) | Q1-Q2 | 1.400-7.100 de tiempo | 10-20 días-persona de DevOps al mismo costo diario; ya incluido en DevOps/QA, no suma. Sin cotización de proveedores |
| Certificaciones del programa de partners | — | No estimado | Faltante: no hay costo en `context/` |

Los porcentajes sobre facturación los calcula Finanzas: `context/` no publica
montos de facturación.

## Insumos para el deck

- **Arquitectura en una imagen:** un gateway neutral al modelo, aislamiento por
  cliente y un harness con evals y gates. Dos frentes sobre la misma base. Con
  una salvedad visible: tres de las cuatro superficies de IA de hoy pueden no pasar
  por el gateway y se cubren con control compensatorio verificado.
- **Qué pedimos al board (un solo pedido, G0):** autorizar T1 en su versión
  acotada (T1-b) con tope de caja y de capacidad, y adoptar el marco de gates. Q2
  es dirección de diseño y se libera en G1; el piloto de producto, además, depende
  de la matriz de restricciones y de la política ratificada. **No** se aprueba el
  modelo propio ni compromisos mayores a 12 meses.
- **Mensaje al CFO:** la IA ya es una línea propia del gasto de tecnología y
  el consumo real es un múltiplo de la suscripción. Se presupuesta el escenario de
  consumo y se prueba la salida de proveedor, no se declara. La ganancia de
  throughput se valúa como horas evitadas a output fijo, no como caja.
- **Riesgo que hay que nombrar:** el piloto de producto no tiene caso elegido ni
  cliente que lo habilite todavía; el plan lo trata como hipótesis con gate. Y T1
  necesita un rol interno con experiencia en IA aplicada que hoy no está identificado.
- **Evidencia que falta:** línea base de productividad, matriz por cliente y
  umbrales de evals; no se prometen números de calidad hasta tenerlos.

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
- Todas las fracciones de esfuerzo, rangos de infraestructura y umbrales de
  abandono propuestos son supuestos del equipo, a convertir en fichas.
