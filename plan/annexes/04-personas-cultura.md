---
owner: people
status: draft
title: "Anexo D — Personas, cambio y roadmap cultural"
---

# Anexo D — Personas, cambio y roadmap cultural

Slides que sustenta: [Slide 7 — Personas y cultura](../slides.md).

Convención de tiempo: el plan tiene una **preparación previa** (octubre-diciembre
de 2026) y **cuatro tramos de tres meses** (meses 1-3, 4-6, 7-9 y 10-12, de
enero a diciembre de 2027), con una revisión mensual del AI Council entre
decisiones ([convenciones](../../context/supuestos/convenciones-de-calculo.md)). Se
asume que el mes 1 arranca con la aprobación del presupuesto 2027 (supuesto).
La preparación previa comprende la validación inicial con autorización propia
y la reconstrucción retrospectiva; la base prospectiva se congela en M1-M3.
El horizonte es coherente con el borrador de OKR de Tecnología 2027.[^okr]

**Términos que se repiten.** Los montos en miles de USD van como `8k USD` en
prosa y `k USD` en los encabezados de columna; el costo horario sigue en USD/h.

| Término | Qué significa en este anexo |
|---|---|
| FTE | Dedicación equivalente a una persona a tiempo completo (no es una persona). Para costear, 480 h por persona en un tramo de tres meses ([convenciones](../../context/supuestos/convenciones-de-calculo.md)) |
| Horas clave y distribuidas | Clave: pocas personas con roles que sostienen controles, prueba y adopción (líder, tech lead, DevOps, QA, seguridad). Distribuidas: repartidas entre muchas personas, como la formación |
| Costo cargado | Lo que una persona cuesta a la empresa por mes, más allá del sueldo de bolsillo. Es tiempo valorizado, no un desembolso nuevo |
| Contribución | Margen que deja una hora facturada, después de los costos que se evitan al no trabajarla. No es la tarifa |
| Bench | Personas facturables sin proyecto asignado |
| Staffing | Personas en equipos de clientes, facturadas por hora o por contrato |
| Base prospectiva y retrospectiva | Prospectiva: medición que se congela en las primeras semanas del plan, antes de capacitar. Retrospectiva: reconstrucción con datos que ya existen |
| Throughput y retrabajo | Volumen de trabajo entregado por período, y cambios que se reabren |
| Champions | Personas con tiempo asignado que enseñan casos de su rol a sus pares |
| AI Council | Comité de revisión mensual del plan; recomienda y revisa riesgos, no libera fondos |
| Gate o compuerta | Punto de decisión donde se libera, se frena o se corta |
| RACI | A decide, R ejecuta, C es consultado, I es informado |
| OKR | Objetivos y resultados clave de la empresa |
| NPS | Índice de recomendación |
| Evals, harness | Evals: pruebas para evaluar los resultados de un asistente; pueden incluir revisión humana. Harness: el armado técnico que lo ejecuta y mide |
| *Few-shot* | Pedir con ejemplos del resultado esperado |
| PR, CI, ADR, QA | Cambio de código propuesto para revisión; integración continua; registro corto de una decisión de diseño; aseguramiento de calidad |
| Omnibus | Modificación del AI Act europeo; su alcance regulatorio se trata en el [Anexo C](03-gobierno-seguridad.md) |

## Objetivo

Sustentar la decisión de personas que se le pide al board: **formar, reasignar y
decidir una excepción externa**, con un programa de AI literacy por nivel y por
rol, una red de champions con tiempo asignado y un solo perfil especializado a
prueba, medido por **uso real semanal** y no por seats comprados. Este anexo
desarrolla roles y capacidad dentro de los derechos de decisión que defina
Gobierno; no los redefine.

**Alcance económico.** Las horas y los costos del programa completo
se conservan como referencia de ese alcance. El pedido inicial vigente es el
paquete mínimo sin plataforma central, consolidado en el [Anexo E](05-business-case.md#pedido-inicial-paquete-mínimo).
No hereda los techos ni la contratación del pedido completo; las decisiones
que siguen son propuestas, no autorizaciones vigentes.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Dotación | 60 a 70 personas, nómina y contractors; ~40% Operaciones (staffing en equipos de clientes), ~40% Tecnología, el resto staff | [Tamaño y estructura](../../context/hechos/tamano-y-estructura.md) |
| Utilización facturable | 83-90%, bench menor a 1 FTE: la capacitación compite con horas facturables | [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md) |
| Restricción de contratación | No contratar gente nueva y potenciar al equipo con IA. Un contractor también requiere una excepción explícita; no ampliar nómina no elimina su consumo de caja | [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md); encuadre de la excepción: propuesta de este anexo |
| Tiempo de capacitación aceptado por la propia empresa | 10% a 15% del tiempo semanal durante una certificación | [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md) |
| Clientes financieros | Por defecto prohíben modelos externos sobre su código y datos; la matriz de restricciones por cliente no existe todavía | [Apetito de riesgo](../../context/supuestos/apetito-de-riesgo-de-clientes.md), [Gobierno y política](../../context/hechos/gobierno-y-politica-ia.md) |
| Costo cargado por rol | Rangos de mercado en USD por mes, amplios y no calibrados contra la nómina (staff 1.500-5.000; desarrollador semisenior 2.000-5.000; analista 2.000-5.500; tech lead 4.500-10.000; especialista IA 4.500-11.000) | [Costo cargado por rol](../../context/supuestos/costo-cargado-por-rol.md) |
| Jornada | 160 h por mes, 1.920 h por año por persona | Supuesto (convención de cálculo) |
| Costo horario de capacitación | USD 10 a 35 por hora (1.500 a 5.500 mensuales sobre 160 h, el tramo de staff, desarrolladores semisenior y analistas) | Supuesto, derivado de [Costo cargado por rol](../../context/supuestos/costo-cargado-por-rol.md). **Es costo, no tarifa facturable** |
| Ganancia de productividad | 10% a 25% de throughput por desarrollador a 12 meses, solo en equipos propios; en staffing no se cuenta | [Ganancia de productividad](../../context/supuestos/ganancia-de-productividad.md) |
| Alcance del art. 4 del AI Act sobre Acme Labs | Sin decidir (art. 2.1.c); se adopta como piso igual | [Fuentes faltantes](../../material/huecos.md), [art. 4](../../material/frameworks/eu-ai-act-proveedor-desplegador.md) |

## Evidencia

### Diagnóstico de adopción por área

| Indicador | Hoy | Cautela | Fuente |
|---|---|---|---|
| Personas con actividad de agente de código, toda la organización | ~1 de cada 3 | Solo mide el agente de código | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |
| Tecnología | ~7 de cada 10 | Idem | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |
| Operaciones (staffing) | ~1 de cada 10 | Baja adopción **no es solo cultural**: cada cliente fija las herramientas | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |
| Staff y dirección | Baja, sin medir | Usan chat y Gemini, que la telemetría no capta; el valor subestima el uso | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |
| Uso detectado de Gemini en Workspace (abril, sin campaña) | ~60% de la organización | Detección, no uso frecuente | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |
| Seats activos en la semana (octubre) | Claude: ~2 de cada 3 de 40-45; Copilot: ~80% de 20-25 | Rangos por discrepancia entre fuentes | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |
| Brecha Tecnología vs. Operaciones | ~7x en personas activas | Cociente de los dos valores anteriores (cálculo de este anexo) | [Uso de IA interno](../../context/hechos/uso-ia-interno.md) |

**Lectura.** La brecha no se cierra con más cursos: en Operaciones hay un freno
contractual que la cultura no resuelve. El borrador de OKR 2027 pide 80% de
uso activo semanal en Operaciones y Tecnología juntas.[^okr] Con ambas áreas de
peso parecido, el proxy de agente de código de hoy es ~4 de cada 10 (promedio de
~7 y ~1 de cada 10, cálculo de este anexo), **no la base de toda la IA**. Con
Tecnología en 85%, Operaciones necesita 75% sobre su total para llegar a 80%
combinado. Las restricciones contractuales condicionan esa cobertura; las metas
por área, cumplidas exactamente, tampoco dan 80% (ver "Meta de adopción y OKR
combinado"). No se infiere de ese cálculo un techo de adopción real.

### Calidad de uso y capacitación

**Punto de partida actual.** No hay un programa de formación en IA por rol con
seguimiento de finalización, según la confirmación del responsable del caso del
20/10/2026 ([fuente verificada, sin revisión documental de las actividades](../../context/hechos/formacion-ia-por-rol.md)).

Esto no implica ausencia de cursos o experiencias previas: el piloto de abril
incluyó cursos y midió su finalización. Esa evidencia histórica acotada se
presenta abajo; no acredita un programa vigente para toda la organización.
La fuente está verificada por una persona del equipo, pero conserva la ausencia
de revisión documental de las actividades formativas.

El programa por rol con seguimiento que desarrolla este anexo es una propuesta
del plan; los cursos aislados no equivalen a ese programa.

| Métrica (piloto de abril, n=12, autoseleccionado) | Resultado | Fuente |
|---|---|---|
| Completaron los tres cursos obligatorios | 17% | [Encuesta y pilotos](../../context/hechos/encuesta-y-pilotos-ia.md) |
| No hicieron ningún curso | 50% | idem |
| Primer freno: falta de tiempo para capacitarse | dos de cada tres | idem |
| Piden casos prácticos por rol en lugar de cursos genéricos | más de la mitad | idem |
| Usan *few-shot* (ejemplos del resultado esperado) | 5% o menos | idem |
| Uso frecuente (3+ días por semana) | 92% | idem |

En el piloto, **92% usó la herramienta tres o más días por semana, el NPS fue
+42 (50% promotores y 8% detractores) y solo el 17% (2 de 12) completó los tres
cursos**: el uso fue alto y **la capacitación falló**. Este anexo no infiere
que los 12 la valoraron ni una adhesión unánime. Es una señal de ese grupo, no una prueba sobre toda
la organización: n=12, autoseleccionado, sin grupo de comparación, así que el
piloto tampoco demuestra que el formato de casos por rol cause una mejor
capacitación. Esa hipótesis la prueba el plan midiendo, no la da por cierta. El
análisis de prompts cubre solo el chat. Este anexo **no extiende** la valoración
del piloto a "la gente": cuando habla de la organización, usa la telemetría y la
encuesta de la línea base de los meses 1-3.

### Qué respalda el diseño

- Literacy en tres niveles de profundidad y tres roles; los marcos de referencia
  no los cruzan, el cruce es decisión de este plan: [niveles](../../material/conceptos/m3u2-ai-literacy-niveles.md).
- Champions: perfil, cuatro fases y 10% de la jornada como ejemplo de tiempo
  asignado; sin sponsor ni entregable concreto se vuelven *status meetings*:
  [programa](../../material/conceptos/m3u2-programa-champions.md),
  [champions y literacy](../../material/conceptos/m1u4-champions-y-literacy.md).
- Frenos (miedo al reemplazo, tecnoestrés, desconfianza) y estrategias de
  transición: [frenos y transición](../../material/conceptos/m3u2-frenos-y-transicion.md).
  La cifra "hasta 60% menos de resistencia" **no se usa**: no tiene fuente
  primaria ([fuentes faltantes](../../material/huecos.md)).
- Tres modos de la IA (automatización, aumentación, supervisión):
  [tres modos](../../material/conceptos/m2u3-tres-modos-ia.md).
- Método de estudio de un rol crítico en cuatro fases (mapeo, diagnóstico,
  proyección, diseño): [deep research de un rol](../../material/conceptos/m3u3-deep-research-rol-critico.md).
  El curso lo plantea a 18 meses; acá se adapta a 12 y es decisión de este plan.
- Transición responsable (roles en riesgo, reskilling y upskilling, nuevos roles,
  recolocación) y sus tres principios, transparencia, equidad y participación:
  [transición responsable](../../material/conceptos/m3u3-transicion-responsable.md).
  La cifra "70% más de retención" con reskilling **no se usa**: no tiene fuente
  primaria ([fuentes faltantes](../../material/huecos.md)).
- Perfil de talento AI-ready y compensación: son marcos prospectivos sin niveles,
  pruebas ni cifras, y se usan como criterio y como discusión, no como política:
  [perfil AI-ready](../../material/conceptos/m3u3-perfil-talento-ai-ready.md),
  [compensación](../../material/conceptos/m3u3-compensacion-futuro-sintetico.md).
- Los cuatro frentes del roadmap cultural (cambio, talento, alfabetización,
  innovación): [roadmap tridimensional](../../material/conceptos/m3u4-roadmap-tridimensional.md).
- ADKAR, Kotter y Lean Change no están en el material: no se usan.

## Roles y capacidad

Principio: **cada rol se cubre primero reasignando o capacitando**. La restricción
literal es no contratar; una incorporación externa exige que el Directorio
apruebe la excepción y su caja cuando la formación no cierre la capacidad a
tiempo. La fuente de estructura marca que arquitectura, seguridad y
gobierno están concentradas en pocas personas y pide tratarlo como riesgo de
continuidad.[^estructura]

**Vigencia de esta sección.** La tabla de roles, la RACI, el contractor, los
champions al 10% y el track cultural de los meses 4-12 describen el **alcance del
programa completo**, sujeto a costeo y autorización adicionales. Los techos de
continuidad del mínimo del [Anexo E](05-business-case.md) («Continuación condicional
sin plataforma», no aprobada hoy) no los cubren: ese tramo financia el
seguimiento y la lectura de la base, el mantenimiento de controles y prácticas y,
antes del mes 6, el descubrimiento del asistente, con 128-212 h internas por tramo
M4-M12 más 36-64 h solo en M4-M6; **no incluye nuevas cohortes, avanzado ni
formación general adicional** y no compra champions al 10%. Lo que el mínimo
sí costea en M1-M3 son tareas y horas concretas, detalladas en «Insumo para el
paquete mínimo»: el básico de 6 h para 60-70 personas (360-420 h), el intermedio
de la cohorte de 15-20 (180-240 h), y el soporte del líder (48-96 h), la
facilitación (16-32 h), la validación de agendas de managers (8-16 h), Talento
(8-16 h) y QA o datos (8-16 h). Esos roles y esas decisiones del mínimo no
quedan negados por este rótulo; lo rotulado es lo que excede esas tareas.

| Rol de IA | Quién lo cubre | Vía | Tiempo (supuesto) | Qué cambia |
|---|---|---|---|---|
| Lidera el programa de adopción (oficina del CAIO) | Un perfil técnico interno | Reasignar | 20% de una persona, 12 meses | Opera literacy, champions y métricas; no decide políticas |
| Especialista en IA aplicada (evals, harness, gobierno técnico) | Un perfil externo a prueba | **Tercerizar (contractor)**; alternativas en la decisión sobre IA aplicada y en "Cobertura de IA aplicada" | 0,5 persona en los meses 1-3; 1 persona en los meses 4-12 solo si la decisión del mes 3 encuentra una señal | Absorbe la concentración de capacidades críticas; documenta y transfiere |
| Champions | Personas de Tecnología, Operaciones y staff | Reasignar | 10% de la jornada, meses 4-12 | Casos prácticos por rol, soporte entre pares, feedback |
| Desarrolladores | Equipo actual | Capacitar | Nivel intermedio y avanzado | Pasan de escribir a **supervisar y revisar** agentes; el humano sigue siendo responsable final ([política](../../context/hechos/gobierno-y-politica-ia.md)) |
| QA y automatización | Equipo actual | Capacitar | Nivel avanzado | Pasan a diseñar evals y compuertas de calidad |
| Analistas funcionales | Equipo actual | Capacitar | Nivel intermedio | Especifican casos de uso y definen "correcto" |
| Delivery manager y personas en staffing | Operaciones | Capacitar | Nivel básico e intermedio | Gestionan qué herramientas permite cada cliente y llevan a la matriz las consultas de uso |
| Dueño de la política, sponsor, administrador de licencias | Ya existen en Tecnología | Sin cambio | Sin cambio | Los define y sostiene Gobierno; este anexo los toma como dados |

RACI de personas (roles, no personas; una sola A por decisión,
[RACI](../../material/conceptos/m1u4-raci-ownership.md)):

| Decisión | A | R | C | I |
|---|---|---|---|---|
| Plan de literacy y calendario | CAIO | Líder del programa | Managers de área, Finanzas | Toda la organización |
| Selección y tiempo de champions | Manager de cada champion | Líder del programa | CAIO | Champions |
| Definición de los KPI de adopción (qué se reporta) | CAIO | Líder del programa | Tecnología, Talento | Directorio |
| Contratación o contractor de IA aplicada | Directorio | CAIO | Finanzas, Talento | Managers |
| Herramientas permitidas por cliente | Área comercial | Delivery manager | Gobierno y seguridad, CAIO | Operaciones |

Responsable de cada fila: **a designar**. Ningún rol de esta tabla está cubierto
por una persona ni aceptado por quien lo ocuparía.

La A de la fila de KPI define **qué se reporta**; no equivale a aprobar el
tratamiento del dato de origen. La autoridad de tratamiento y retención de los
eventos de uso por persona, y la revisión laboral y de datos personales que
corresponda, están **por definir con Gobierno y Talento**
([Anexo C](03-gobierno-seguridad.md)); este anexo no elige una A.

**Propuesta operativa, fuera de la RACI: quién completa y valida la matriz
privada de capacidad.** El líder del programa la completa; Operaciones y los
managers de cada persona validan y liberan las agendas, con Talento y Finanzas
como consultados. Es una propuesta de trabajo de Personas, no un derecho de
decisión. Quién es la autoridad (la A) de esa validación no está definido en el
[Anexo C](03-gobierno-seguridad.md) y se remite a Gobierno; este anexo no la elige.

### Perfil AI-ready: qué se desarrolla y qué se busca

Con la restricción de no contratar, el perfil AI-ready es sobre todo un criterio
para **desarrollar y seleccionar adentro**. Las cuatro habilidades del curso
(interacción con IA, interpretación de datos, pensamiento crítico, creatividad)
no traen niveles ni pruebas ([perfil AI-ready](../../material/conceptos/m3u3-perfil-talento-ai-ready.md));
el cruce de abajo es **síntesis propia, un supuesto a validar**:

| Habilidad | Dónde se desarrolla | Dónde se usa como criterio |
|---|---|---|
| Interacción con IA | Nivel básico e intermedio (pedir bien, supervisar) | Selección de champions |
| Interpretación de datos | Intermedio, con los casos del rol | Perfil demostrado para la vía interna de IA aplicada |
| Pensamiento crítico | Intermedio: verificar y detectar alucinaciones | Revisor humano de la compuerta; brief del especialista externo |
| Creatividad | Casos prácticos por rol que publican los champions | Selección de champions |

Contratar o desarrollar: el plan **desarrolla**; la única incorporación es el
especialista externo a prueba, por excepción del Directorio (ver "Decisiones").
Si la excepción se aprueba, el brief del perfil exige pensamiento crítico y
capacidad de documentar y transferir, además del conocimiento técnico. No se
publican pruebas de evaluación de estas habilidades: no hay un instrumento
validado en el material.

### Estudio de impacto sobre un rol crítico (propuesta)

**Alcance: programa ampliado, no el mínimo.** El estudio no tiene tareas ni costeo
propios en el mínimo de E, y sus horas no se absorben en las del líder (48-96 h de
agenda, base, diccionario, seguimiento y cierre). **No inicia con el mínimo.** Antes
de realizarlo exige (1) la postura sobre el empleo aprobada por el Directorio y
comunicada, (2) horas propias estimadas y (3) autorización propia. Las fases y los
tramos de abajo son una secuencia propuesta, relativa a esas condiciones.

**Problema.** El anexo describe qué cambia para cada rol, pero a nivel de
proceso. Falta un estudio por rol que separe lo automatizable, lo aumentado y lo
exclusivamente humano, y que convierta ese diagnóstico en un plan de desarrollo
y no en una lista de reemplazos. El método es el [deep research de un rol](../../material/conceptos/m3u3-deep-research-rol-critico.md),
en cuatro fases.

**Rol a estudiar.** El **desarrollador de equipos propios**: es el rol con
mayor adopción (Tecnología ~7 de cada 10), donde se mide la ganancia de
productividad y donde el paso de escribir a supervisar es más fuerte. Segundo
candidato, solo si el primero cierra: **analista funcional**. Operaciones y
staffing quedan afuera porque el cliente fija las herramientas y el estudio no
tendría qué diagnosticar. Es supuesto de este anexo; lo confirman el CAIO y el
manager de Tecnología.

| Fase | Tramo | Producto | Quién |
|---|---|---|---|
| 1. Mapeo | Después de la postura comunicada y de la autorización propia; no antes de congelar la base | Inventario de tareas del rol, validado con el delivery manager; parte del "antes" ya propuesto en el flujo de delivery | Líder del programa, con personas del rol |
| 2. Diagnóstico | Tras el mapeo (tramo a definir) | Cada tarea clasificada como automatizable, aumentada o humana, contrastada con el uso real medido y con los tres modos de la IA | Líder del programa y tech leads; el CAIO valida |
| 3. Proyección | Tras el diagnóstico (tramo a definir) | Responsabilidades y competencias que emergen (supervisar, revisar, definir "correcto") | Ídem, con Arquitectura y Gobierno |
| 4. Diseño | Tras la proyección (tramo a definir) | Ruta de desarrollo del rol: contenido del avanzado, casos de los champions y criterio de reasignación | CAIO, con Talento |

**Gate que alimenta.** Si el estudio se autoriza y llega a tiempo, el diagnóstico
entra a una decisión posterior como evidencia de qué tareas se aumentan; el diseño
ajusta el formato del tramo siguiente y el criterio de "formar, reasignar" de la
decisión de personas. El mínimo no depende de él. No decide
desvinculaciones: el estudio responde cómo diseñar la mejor versión futura del
rol ([deep research](../../material/conceptos/m3u3-deep-research-rol-critico.md)),
y la postura sobre el empleo lo acota por escrito.

**Datos.** Las tareas reales del rol no se publican: el anexo solo muestra el
resultado por rol y agregado, anonimizado.

**Contrato de la propuesta.**

- **Evidencia o supuesto:** el método es del curso; el rol elegido y los tramos
  son supuestos de este anexo. No hay inventario real del rol todavía.
- **Alternativas:** (1) no hacer estudio por rol y quedarse con el flujo de
  delivery; (2) estudiar los tres roles técnicos a la vez; (3) un rol y luego
  otro. **Recomendación: la tercera.** Una sola vez a la vez, porque las horas del
  líder (20% de una persona) no alcanzan para más.
- **Dependencias:** base prospectiva congelada (mapeo y contraste), horas del
  delivery manager, la postura sobre el empleo comunicada antes de que la
  gente participe.
- **Costo:** **sin estimación ni costeo propios**; no es una partida del mínimo.
  No se supone absorbido por las horas del líder: antes de iniciarlo hay que
  estimar sus horas y pedir la autorización a Finanzas y al Directorio.
- **Riesgo:** que la persona del rol lea el estudio como paso previo a un recorte
  y deje de participar o de ser franca.
- **Responsable humano:** a designar.
- **Criterio de éxito:** inventario validado por al menos dos personas del rol y
  una ruta de desarrollo que los champions y el avanzado puedan usar.
- **Condición de abandono:** el mapeo no se valida con el rol al cierre de su
  tramo, o el delivery manager no libera horas, o falta la postura comunicada:
  no se inicia o se vuelve al flujo de delivery como único insumo.

### Capacidad efectiva: dos bolsas sobre las mismas personas

Separar sobre clave y distribuido **no crea tiempo**. La utilización promedio y
el bench no demuestran disponibilidad por rol. Antes de comprometer el tramo,
Operaciones y cada manager validan las mismas agendas con Talento y Finanzas;
los responsables nominales están por designar. No se financian las horas
iniciales con productividad futura ni se da por liberado tiempo porque tenga costo.

Contraste del **programa publicado**, con 480 h por FTE-tramo
([convenciones](../../context/supuestos/convenciones-de-calculo.md)) y las bolsas
del [Anexo E](05-business-case.md), "Conciliación de los meses 4-6" y "Pedido de
hoy y gates económicos":

| Tramo | Sobre clave interno | Sobre distribuido interno | Total interno | Externo y límite |
|---|---|---|---|---|
| Meses 1-3, con prueba chica | ~1,8 FTE, redondeo publicado | 654 h / 480 = 1,3625 FTE | **~3,16 FTE**; aproximado por el redondeo clave | Contractor 0,5 FTE adicional, si se aprueba la excepción |
| Meses 4-6, con replan y señal | 1.068 h / 480 = 2,225 FTE | 1.208 h / 480 = 2,5167 FTE | **~4,74 FTE** (2.276 h) | Contractor 1 FTE adicional; contra 2,25 FTE clave quedan **12 h** (1.080 − 1.068) |

Los totales no prueban que las agendas entren. El avanzado puede usar 480-720 h
en vez del medio 600; ausencias, simultaneidad y personas con más de un rol pueden
cambiar el encaje. El piso clave no sustituye la validación del total interno.

**Matriz semanal a completar en privado**, una fila por persona, rol y semana,
con identificador privado para conciliar a quienes cubren varias funciones.
Esta es la estructura; no publica dotación nominal, tarifas ni asignaciones reales:

Las filas se agrupan en cinco familias de rol: arquitectura y liderazgo técnico;
DevOps y QA; gobierno, seguridad y Council; líder de adopción y facilitadores;
participantes y champions por área. Cada fila lleva estas columnas, que se
completan en privado:

| Columna | Qué registra | Regla |
|---|---|---|
| Semana / rol (ID privado) | Persona, rol y semana | El ID privado concilia a quien cubre varias funciones |
| Horas disponibles netas | Jornada menos ausencias de esa semana | Salen de la agenda, no de la utilización promedio ni del bench |
| Compromisos vigentes | Trabajo que se mantiene | Con su cliente o contrato, en la columna de abajo |
| Horas clave del plan | Soporte: líder, facilitación, tech lead, DevOps, QA, seguridad | **Columna propia** (propuesta de este anexo): E las valúa al costo del rol sobre 160 h |
| Horas distribuidas del plan | Básico e intermedio, por separado | **Columna propia** (propuesta): E las valúa a 10-35 USD/h |
| Tipo de hora | Una de tres: **absorbible** (cabe en las horas netas menos los compromisos, sin desplazar nada); **interna reprogramable** (desplaza una actividad interna que se puede mover); **facturable desplazada** (desplaza horas que paga un cliente o contrato) | **Columna nueva** (propuesta). Una hora es absorbible solo si la agenda de esa semana lo muestra; no se infiere de un promedio |
| Cliente o contrato (ID privado) y modalidad | ID privado del cliente o contrato del compromiso desplazado, o «interno»; y modalidad: staffing por hora, precio fijo, suscripción o interno | **Columna nueva** (propuesta). Sin ella, «facturable desplazada» no se puede verificar ni cruzar con la matriz de restricciones por cliente de C |
| Trabajo desplazado y quién lo cubre | Qué se posterga y quién lo hace | Debe tener destino, impacto y responsable |
| Recuperación | Horas, fecha y evidencia | Una recuperación futura no habilita una semana sobreasignada |
| Efecto en ingresos y contribución | Solo para horas «facturable desplazada» | Lo calcula Finanzas, en privado (ver «Dónde vive el costo de oportunidad») |
| Valida / fuente | Manager y agenda | Quien libera la agenda, no quien la pide |

Las tres columnas marcadas como nuevas o propias responden al pedido de #18 y #13
y son una propuesta de Personas (agente): **falta que el responsable humano de D las confirme o corrija**.
La matriz real no existe todavía y no se publica.

Horas disponibles netas = jornada menos ausencias; de ahí se descuentan los
compromisos que se mantienen y las horas de **ambas** bolsas. Un mismo bloque
horario cuenta una sola vez aunque la persona sea líder, champion y participante.
El trabajo que se retira de la agenda debe tener destino, impacto y responsable;
una recuperación futura no habilita una semana sobreasignada. Los sobrantes
de otro rol o semana no cubren automáticamente un faltante.

Finanzas distingue costo cargado, ingreso no facturado y contribución perdida,
documenta qué se recupera y no suma dos veces las mismas horas como ahorro e
ingreso ni como costo y contribución. Solo se publican rangos o índices autorizados.
Sin conciliación semanal, reducir o diferir el alcance y volver a costear antes de iniciar.

**Dónde vive el costo de oportunidad.** No en este anexo ni en la matriz. D clasifica
las horas y aporta la evidencia; Finanzas las valúa en privado y
[E, «Conclusión económica»](05-business-case.md#conclusión-económica) informa tres
magnitudes por separado: recursos valorizados a costo cargado, desembolso
incremental de caja y contribución comercial desplazada, hoy **sin medir**.
La contribución es el margen sobre costos evitables de las horas marcadas
«facturable desplazada», no la tarifa por hora: la tarifa contiene el costo
cargado y sumar ambos sobre la misma hora cuenta dos veces. El costo horario de
10-35 USD/h de este anexo es costo cargado de capacitación, no tarifa.

**Dos agendas y dos liberaciones para el mínimo.** La validación inicial de
2026 necesita su propia agenda autorizada antes de empezar: incluye a quienes
entrevistan, responden, verifican y deciden, además de los managers que liberan
su tiempo. No presupone ya conciliada la agenda de ejecución de M1-M3.

Con esa primera liberación se completa la matriz privada de capacidad por
persona y semana: padrón, ausencias, compromisos, soporte, básico e intermedio
sobre las mismas personas, desplazamiento y cobertura. Esta matriz es de D;
la matriz de restricciones por cliente, herramienta y superficie es de C.
Se cruzan para delimitar el alcance, sin que una sustituya a la otra.

La segunda liberación, antes de M1, exige capacidad real y trabajo desplazado
validados por Operaciones y managers, diagnóstico revisado y presupuesto 2027
comprobado. Productor, verificador independiente y autoridad empresarial
firmante son personas distintas, a designar conforme a C. Los responsables
del TP no sustituyen esos roles de la empresa.

### Antes y después de un proceso: del requerimiento al cambio en producción

Aplicación del [grafo humano-agente](../../material/conceptos/m2u3-grafo-humano-agente.md)
a un proceso de delivery de **equipos propios** (no de staffing, donde el cliente
fija las herramientas). Es un **diseño propuesto**: no hay documentación del
proceso real paso a paso, así que el "antes" es un proceso típico supuesto, a
validar con un delivery manager antes de usarlo como línea de base. El modo de
cada nodo sigue los [tres modos](../../material/conceptos/m2u3-tres-modos-ia.md).

| Paso | Antes (nodo y modo) | Después (nodo y modo) | Decisión humana y quién revisa |
|---|---|---|---|
| 1. Especificar | Analista funcional escribe el requerimiento y los criterios de aceptación | Analista escribe el requerimiento y un agente propone casos borde y criterios faltantes (aumentación) | El analista decide qué entra; el tech lead revisa el criterio de "correcto" |
| 2. Diseñar y estimar | Desarrollador y tech lead, en reunión | Desarrollador con asistente de código para alternativas (aumentación); el tech lead decide | Tech lead: diseño y alcance |
| 3. Construir | Desarrollador escribe el código | Agente de código genera el borrador y las pruebas (automatización acotada); el desarrollador **supervisa y corrige** | Desarrollador: es responsable final de lo que se integra ([política](../../context/hechos/gobierno-y-politica-ia.md)) |
| 4. Verificar | QA arma y corre pruebas a mano o con guiones propios | Agente genera pruebas y corre la compuerta de evals; QA diseña las compuertas y revisa los casos que falla (supervisión) | QA: define y aprueba el umbral; nada pasa si la compuerta no corre |
| 5. Revisar el código | Un par humano revisa todo | Revisión asistida por agente que marca riesgos; un humano distinto del autor aprueba | Revisor humano: aprueba o rechaza; un agente nunca aprueba solo |
| 6. Liberar y operar | DevOps y el equipo | Igual, con registro de qué parte tuvo asistencia de agente | Tech lead autoriza la liberación; incidentes los trata el equipo, con Gobierno |

**Handoffs que cambian:** el analista entrega criterios verificables por una
compuerta (antes, texto para leer); el desarrollador entrega código con las
pruebas que lo respaldan; QA entrega la compuerta y no solo el resultado. Donde
el contrato del cliente prohíbe las herramientas, el flujo vuelve al "antes" en
esos nodos y el plan no lo fuerza (ver "Staffing").

**Qué se mide antes y después:** tiempo de ciclo del requerimiento a producción,
retrabajo (cambios reabiertos) e incidentes, **contra la base prospectiva
congelada** de las semanas 1-4 del plan, por área y agregado. No se atribuye
mejora antes de los meses 4-6.

### Cobertura de IA aplicada, por tramo

El [Anexo B](02-arquitectura.md) necesita 0,3 FTE de IA aplicada en los meses 1-3
(el escenario recomendado, con contractor que reemplaza; el 0,5 era del contractor
que complementa, que solo queda en su escenario conservador) y 0,8 en los meses
4-12, dentro de su esfuerzo técnico. El contractor de este anexo y esa
fracción del Anexo B son **un solo recurso**, no dos.
No hay registro de ningún perfil interno de IA aplicada con tiempo libre
(la capacidad es de pocas personas y el bench es menor a 1 FTE), así que **no se
asume que exista**.

| Tramo | Necesidad (Anexo B) | Vía propuesta | Alternativa | Qué lo demuestra |
|---|---|---|---|---|
| Meses 1-3 | 0,3 FTE (contractor que reemplaza) | Contractor al 50%, tramo de los meses 1-3 del paquete completo, **con aprobación propia del Directorio**: cubre el 0,3 del Anexo B y deja 0,2 para incorporación, documentación y coordinación | Perfil interno reasignado, solo si antes de esa aprobación se demuestra por rol: porcentaje liberado, trabajo desplazado y quién lo cubre | Contrato corto firmado, o declaración de capacidad por rol validada por Operaciones |
| Meses 4-12 | 0,8 FTE | El mismo contractor, 1 persona, **solo si la decisión del mes 3 encuentra al menos una señal** (contractual, anuncio de precio por consumo o cliente del producto; [Anexo E](05-business-case.md), "Recomendación de Finanzas"). Sin señal, no hay cobertura: los meses 4-12 corren como la alternativa de gobierno mínimo y formación del Anexo E, sin hitos de IA aplicada | Idem | Señal registrada en el mes 3; entregable verificable por tramo; documentación y traspaso |

**Reemplaza, no complementa.** El contractor es la fuente del 0,3 de los meses 1-3
y del 0,8 de los meses 4-12 del Anexo B; en ambos, el 0,2 restante es documentación,
traspaso y coordinación con el programa (en los meses 4-6 se puede prestar al replan
del Anexo B, ver "Holgura de 0,2 FTE del contractor en los meses 4-6 (replan del
Anexo B)"). Contar la fracción del Anexo B y el contractor a la vez duplica el costo
(solape que Finanzas marca como "IA aplicada"). Costeo de cada alternativa:

**Vigencia.** Esta sección describe el paquete completo, una alternativa que **no
se pide hoy**. El pedido vigente es el mínimo sin contractor continuo, consolidado
en E; el contractor y la excepción de 0,3 FTE requieren una autorización nueva,
con alcance, calendario y costeo propios. Donde abajo dice «aprobación del
paquete completo» se entiende esa autorización futura.

| Alternativa | Caja, k USD | Tiempo interno | Riesgo |
|---|---|---|---|
| Solo perfil interno | 0 | 0,3 FTE en los meses 1-3 y 0,8 en los meses 4-12 sacados de horas facturables | Sin perfil demostrado, el plan no arranca; concentración de capacidades críticas sin mitigar |
| Contractor desde el mes 1 (recomendada) | Meses 1-3: 6,75-16,5 (0,5 x 3 meses x 4.500-11.000 USD por mes); meses 4-12: 40,5-99,0 | Se libera el tiempo del Anexo B que cubre | Sube la caja de los meses 1-3 contra el techo de la aprobación del paquete completo y choca con "no contratar" (decide el Directorio) |
| Contractor desde el mes 4 | Meses 4-12: 40,5-99,0 | Los meses 1-3 quedan sin cubrir: el hito del Anexo B se corre o se resiente | Atrasa el gateway de laboratorio y las evals de los meses 1-3 |

Para el paquete completo, la aprobación elegiría el contractor desde el mes 1 y
autorizaría solo su tramo de los meses 1-3 (hasta 16,5k USD de caja, dentro del techo de 33k USD).
El tramo de los meses 4-12 al 100% (40,5-99,0k USD) se libera en la decisión del
mes 3 solo con al menos una señal; sin ninguna, **el contractor se cierra** (un
mes de preaviso, ~4k USD de caja en el medio según el Anexo E), el mes se usa para
documentar y traspasar lo hecho en los meses 1-3 a la oficina del CAIO, y los meses
4-12 corren como la alternativa del Anexo E: gobierno mínimo y formación, con la
prueba extendida a la cohorte (≈199k USD en el año contra ≈400k USD, Anexo E). Las
lecturas de los meses 6 y 9 vuelven a leer las señales. No es un corte del plan:
difiere la plataforma. Si el Directorio rechaza el contractor desde el mes 1, la
alternativa es el perfil interno solo, con la prueba de capacidad previa a esa
aprobación, o diferir los hitos de IA aplicada de los meses 1-3 (lo que decide
Arquitectura).

### Holgura de 0,2 FTE del contractor en los meses 4-6 (replan del Anexo B)

El [Anexo B](02-arquitectura.md) ("Exceso de los meses 4-6 con el producto
diferido") baja los meses 4-6 a 2,2 FTE clave bajo el supuesto de que el contractor
tiene 0,2 FTE pagados y sin asignar, y que con ellos absorbe el pipeline de evals en
CI y la reejecución de la prueba de portabilidad. El deck adopta ese replan. Este
anexo lo contrasta contra la asignación del propio contractor:

| Fracción del contractor (100% en los meses 4-6) | Asignación de este anexo | Con el replan del Anexo B |
|---|---|---|
| 0,8 | La fracción de IA aplicada del Anexo B (evals, harness, gobierno técnico) | Igual |
| 0,2 | Documentación de traspaso y coordinación con el programa (manuales y traspaso) | Evals en CI y reejecución de la prueba de portabilidad, solo en los meses 4-6, **con la documentación mínima reproducible de esos dos entregables dentro del mismo 0,2**. Los manuales, el traspaso y la coordinación pasan a los meses 7-12 |

**Imputación de la documentación mínima reproducible.** Cada entregable lleva
1-2 días-persona de documentación (tupla de versión, instrucciones de ejecución,
ADR corto y corrida fechada) y se imputa a la fracción del contractor que lo
produce, sin sumarla dos veces ([Anexo B](02-arquitectura.md), «Documentación
mínima reproducible»):

| Entregable de los meses 4-6 | Fracción que lo produce | Documentación mínima, días-persona | Reproducción independiente |
|---|---|---|---|
| Harness v1 | 0,8 | 1-2 | DevOps/QA, dentro de su 0,8 del replan: 0,5-1 día |
| Suite de evals con dataset v1 | 0,8 | 1-2 | Ídem: 0,5-1 día |
| Evals en CI | 0,2 | 1-2 | Ídem: 0,5-1 día |
| Lote de la prueba de portabilidad y costo | 0,2 | 1-2 | Ídem: 0,5-1 día |
| **Total** | 0,8: 2 entregables; 0,2: 2 entregables | **4-8** (0,8: 2-4; 0,2: 2-4) | **2-4**, en DevOps/QA |

La asignación por entregable sale del anexo B (el 0,2 del replan para evals en CI
y el lote; el resto, en el 0,8). Los totales se recalcularon desde las filas:
4 × 1 = 4 y 4 × 2 = 8 días-persona; 4 × 0,5 = 2 y 4 × 1 = 4 días de reproducción.
Son supuestos de horas, no un dato del contractor.

**Decisión de Personas: la holgura no está confirmada, así que el replan es
condicional.** Las horas existen (el 100% se paga), pero no están libres: este
anexo ya las usa en documentación, traspaso y coordinación, que es la mitigación
de continuidad frente a la concentración en una sola persona externa. No hay dato
del contractor: ni su perfil, ni su experiencia en evals y CI, ni el alcance de
su contrato. Todo lo de abajo es un **supuesto de Personas**, no un hecho.

- **Cuándo se puede sostener.** Solo en los meses 4-6 y solo si el alcance
  contractual, aprobado antes con el paquete completo, incluye de forma explícita
  esos dos entregables (evals en CI y reejecución de la prueba). Lo que se desplaza
  a los meses 7-12 son los manuales de operación y el traspaso (este último es de los
  meses 10-12). Todo esto vale solo si la decisión del mes 3 libera el contractor
  al 100%. La documentación mínima reproducible que exige la lectura del mes 6
  es parte de cada entregable y queda en la fracción que lo produce (tabla de
  arriba): la de evals en CI y el lote, en el 0,2, y la del harness y la suite, en el
  0,8, más la reproducción de DevOps/QA (Anexo B). Es un desplazamiento,
  no una holgura: lo que se difiere se hace después, no desaparece.
- **Qué lo sostiene como evidencia.** Un alcance de contrato con esos entregables
  y fechas, y la declaración del contractor de que tiene el perfil. Hoy no existe
  ninguna de las dos; se piden como condición antes de esa aprobación.
- **Cuándo el replan no alcanza, y qué cubre cada respaldo.** Son dos
  contingencias distintas ([Anexo E](05-business-case.md), "Dos contingencias del
  contractor"; [Anexo B](02-arquitectura.md), "Exceso de los meses 4-6 con el
  producto diferido"):
  - **Sin el 0,2** (el contractor existe, pero el alcance no se acordó así, o en
    el control de la semana 20 del plan (la séptima de los meses 4-6) los entregables cerrados no tienen
    su documentación mínima reproducible; la autorización de la excepción se solicita ahí, no al cierre
    del tramo): los meses 4-6 quedan en 2,5 FTE clave y corresponde la **excepción
    acotada de 0,3 FTE**, que el paquete completo propone como respaldo y que
    **requiere aprobación antes de activarse** (la segunda salida
    del Anexo B; ver la decisión "Vía de IA aplicada" del
    [Anexo F](06-roadmap-riesgo.md)). Son ~5k USD de tiempo (3-8k USD) y nada de caja
    nueva: ya está en el cuadro del Anexo E.
  - **Sin contractor** (el Directorio no lo aprueba o no se contrata a tiempo): la
    excepción **no alcanza**. Falta toda la fracción de 0,8 FTE de IA aplicada, no
    solo el 0,2; con fracción interna el plan pediría ~3,3 / 3,0 / 2,9 FTE clave
    en los meses 4-6, 7-9 y 10-12, contra un máximo de 2,25. Este anexo no propone
    cubrirlo con tiempo de personas: la respuesta es el **modo control del Anexo B**
    (2,2 / 2,2 / 2,1 FTE clave, sin harness, evals en CI, caso de referencia ni
    prueba de portabilidad), y cubrirlo con fracción interna queda como opción del
    board solo si aprueba explícitamente ese piso mayor. Además, sin contractor la
    documentación y el traspaso (el 0,2 de este anexo) no tienen quién los haga: la
    mitigación de concentración de capacidades se pierde y queda como riesgo
    aceptado.
- **Costo de la hipótesis para este anexo.** Cero de caja: el 100% del contractor
  ya está en "Insumos para Finanzas". El costo es de riesgo: la documentación
  se corre y la concentración de los meses 4-6 sube.

## AI literacy por nivel y por rol

Cruce de los dos ejes (niveles y roles), decisión de este plan. Horas por persona y
población son supuestos; el nivel básico es el piso para todos.

| Nivel | Población (aprox.) | Contenido | Formato | Horas por persona | Horas totales |
|---|---|---|---|---|---|
| Básico | Toda la organización, ~65 | Uso seguro, clasificación de datos, qué se puede enviar, verificar el output, reportar incidentes | Sesiones breves y guía de una página; **casos de su rol** | 6 | ~390 |
| Intermedio | Operaciones y Tecnología usuarias frecuentes, ~50 | Pedir bien (ejemplos, contraargumentos), identificar casos de uso, supervisar | Talleres con casos reales del rol y práctica entre pares | 12 | ~600 |
| Avanzado | Especialistas que diseñan e implementan, ~10 | Agentes, evals, harness, gobernanza técnica | Proyecto aplicado con tiempo asignado | 10-15% del tiempo semanal durante un tramo de tres meses | 480-720 |
| Directivo | Primera línea y Directorio | Decidir inversión, riesgo, regulación y ROI | Briefings con casos | 3 | Dentro de la oficina del CAIO, sin costo aparte (supuesto) |

Cálculo del avanzado, con la convención de costeo del plan (480 h por
persona-tramo, [convenciones](../../context/supuestos/convenciones-de-calculo.md)):
10 personas x 480 h x 10-15% = 480-720 h. Las 520 h de 13 semanas x 40 h son
calendario bruto y no se usan para costo. Poblaciones y horas coinciden con la
fuente [poblaciones de capacitación](../../context/supuestos/poblaciones-de-capacitacion.md)
y con el [Anexo E](05-business-case.md). Los niveles y los
roles salen de [AI literacy](../../material/conceptos/m3u2-ai-literacy-niveles.md);
los contenidos del básico y el intermedio responden a lo que el piloto mostró
faltante (uso seguro, ejemplos, verificación).

**Pedido de formato.** Más de la mitad del piloto pide casos prácticos por rol:
se arma ese formato con champions y se descarta el curso obligatorio genérico.
Cada módulo se agenda **dentro de la semana laboral**, con aviso al manager, para
corregir las fallas de comunicación que registró la encuesta.

**Art. 4 del AI Act.** Para el plan es un piso del plan de personas, que
las fuentes de referencia ya dan como vigente. El texto original exige garantizar un
nivel suficiente de alfabetización; el texto tras el Omnibus pide "apoyar el
desarrollo" y no exige un nivel por individuo
([art. 4](../../material/frameworks/eu-ai-act-proveedor-desplegador.md)).
**Cautela:** si alcanza a Acme Labs y la versión vigente del art. 4 siguen sin
verificar contra EUR-Lex ([fuentes faltantes](../../material/huecos.md)). El plan cumple el
espíritu de ambos textos (formación proporcional al rol, con registro de quién
completó qué), pero **no cita fechas ni sanciones en slides** hasta cerrar esa
verificación.

## Programa de champions

- **Tamaño:** 8 champions, una persona cada ~8 de la dotación (supuesto);
  al menos 2 de Operaciones y 2 de staff, porque la brecha está ahí.
- **Perfil:** curiosidad, comunicación y vocación de servicio; no necesariamente
  el más técnico ([programa](../../material/conceptos/m3u2-programa-champions.md)).
- **Contrato:** mandato explícito, sponsor y un entregable por tramo de tres meses
  (una guía de casos de su rol, un taller). El tiempo (10%) lo libera el manager y
  se agenda; si no se libera, el champion no se computa como activo.
- **Costo de no hacerlo bien:** los champions sin tiempo ni entregable se
  vuelven reuniones de estado ([champions y literacy](../../material/conceptos/m1u4-champions-y-literacy.md)).

## Gestión del cambio

| Freno | Evidencia en el caso | Quién pierde qué | Respuesta |
|---|---|---|---|
| Falta de tiempo | Dos de cada tres en el piloto; utilización 83-90% | Operaciones: la formación puede desplazar facturación; depende de la agenda, el contrato y la recuperación efectiva | Horas dentro de la jornada, módulos cortos, calendario por equipo; el costo está en Insumos para Finanzas |
| Prohibición del cliente | Supuesto de apetito de riesgo; matriz inexistente | Staffing: queda afuera de la ganancia | Ver "Staffing" abajo |
| Miedo al reemplazo | Freno típico de adopción; no hay medición propia | Todos, y más en perfiles junior | Comunicación transparente y la decisión sobre el compromiso con el empleo |
| Dependencia de un proveedor | El piloto lo advierte y propone consumo multimodelo | Equipos que ya construyeron hábitos | Fuera del alcance de este anexo; lo resuelve Arquitectura |
| Desconfianza en el output | Pocos piden contraargumentos o advierten alucinaciones | Quien revisa | Nivel intermedio centrado en verificar y supervisar |
| Incentivo contrario en staffing facturado por hora | Mencionado en las condiciones de invalidez de la ganancia de productividad | Personas y empresa: menos horas es menos facturación | Tensión con Finanzas, ver "Tensiones con otras miradas" |

**Staffing en equipos de clientes que prohíben herramientas externas.** El plan
no les pide usar lo que el contrato no permite. Tres frentes:

1. **Usos permitidos sin tocar el cliente:** propuestas, documentación
   propia, tickets y correo internos, con las herramientas corporativas y la
   clasificación de datos vigente.
2. **Literacy igual:** nivel básico e intermedio para todos, porque es
   formación de la persona y no depende del contrato.
3. **Matriz de clientes primero:** hasta que Gobierno y el área comercial la
   completen, cada caso se valida a mano (pendiente declarado de la política).
   Las personas en staffing reportan consultas de uso de forma sencilla y sin
   sanción, igual que los incidentes.

**Dependencia de personas clave.** La capacidad en arquitectura, seguridad y
gobierno está en pocas personas: el contractor de IA aplicada y la documentación
obligatoria de lo que arma el champion o el líder son la mitigación de
continuidad.

### Transición responsable: roles, equidad y participación

Las cuatro estrategias del curso ([transición responsable](../../material/conceptos/m3u3-transicion-responsable.md))
aplicadas a un plan sin contratación y con compromiso sobre el empleo:

| Estrategia | Qué hace el plan | Dónde está |
|---|---|---|
| Identificar roles en riesgo | Estudio por rol, desde las tareas y no desde el puesto; empieza por el desarrollador de equipos propios | "Estudio de impacto sobre un rol crítico" |
| Reskilling y upskilling | Upskilling: desarrolladores, QA, analistas (capacitar). Reskilling: la reasignación a líder del programa y a champions | Tabla de roles y capacidad |
| Nuevos roles | Líder del programa, champions y el QA que diseña compuertas: se crean reasignando, sin contratar | Tabla de roles y capacidad |
| Recolocación | **No se desarrolla**: la postura sobre el empleo excluye desvincular por ganancia de IA, y las causales ajenas a la IA siguen su cauce | Ver decisión de empleo y cautelas |

**Principios como criterio de control.**

- **Transparencia.** Los cambios de rol se comunican con su razón, después de la
  decisión del Directorio sobre el empleo, no antes.
- **Participación.** Las personas del rol participan del mapeo; hay al menos 2
  champions de Operaciones y 2 de staff; el pulso anónimo recoge la voz de quienes
  no participan.
- **Equidad.** La transición no puede cargar de más a un grupo. Se observan, por
  grupo y agregado, tres cosas: horas de formación efectivamente liberadas,
  reasignaciones y rotación voluntaria. Los grupos que se miran son **perfiles
  junior** y **Operaciones y staffing**. Hipótesis a contrastar en el mapeo: las
  tareas más automatizables son las de entrada, que hacen los junior (el curso no
  lo afirma; es supuesto de este anexo). Staffing no se evalúa por uso: su baja
  adopción responde al contrato del cliente, no a resistencia (ver "Habilitadas").

**Disparador de abandono de esta línea.** Una diferencia entre grupos en horas
liberadas o en rotación que la agenda o el contrato no expliquen, leída en la
revisión mensual del Council: se corrige la agenda antes de seguir con el
formato. El umbral se fija con la línea de base de los meses 1-3, no se inventa acá.

## Roadmap cultural por tramo y métricas

La preparación previa (octubre-diciembre de 2026) reúne validación inicial y
reconstrucción retrospectiva, con autorización y agendas propias anteriores a
la liberación de M1-M3 y al presupuesto 2027. No adelanta formación ni prácticas.
Los umbrales son supuestos, a validar con la línea de base. Toda
métrica se reporta con numerador y denominador y **por área, agregada**: ningún
dato individual ([OKR](../../context/hechos/okrs-y-objetivos.md)). Agregar el
reporte por área **no vuelve anónimo el dato de origen**: la fuente registra
eventos por persona. Qué se conserva, cuánto tiempo y quién decide ese
tratamiento (con la revisión laboral y de datos personales que corresponda) lo
define Gobierno con Talento, pendiente declarado; no hay una A elegida en este
anexo. La medición se comunica a las personas antes de empezar a medir.

| Tramo | Hitos | Indicador adelantado (uso real) | Indicador rezagado |
|---|---|---|---|
| Preparación previa de 2026, primera liberación propia | Validación inicial del diagnóstico y capacidad; reconstrucción **retrospectiva** con datos existentes y diseño de la encuesta de chat y Gemini. Preparar la revisión del respaldo documental y alcance de la [política aprobada según el responsable del caso](../../context/hechos/gobierno-y-politica-ia.md); documentación aún por verificar | Acta con diagnóstico revisado, agendas M1-M3 conciliadas o faltantes explícitos; serie retrospectiva de uso por área | Serie retrospectiva de throughput, incidentes y retrabajo, con su hueco declarado si no existe |
| Meses 1-3, semanas 1 a 4 del plan, ampliables a 8 según B | **Congelar la base prospectiva** antes de cualquier capacitación o herramienta nueva para usuarios: encuesta de chat y Gemini, uso semanal por área, throughput, incidentes y retrabajo de los equipos propios | Línea de base por área publicada y congelada; si se extiende, se revisa completitud M3 | Línea de base prospectiva de throughput, incidentes y retrabajo |
| Meses 1-3, desde semana 5 o 9 según cierre de base | Verificar la aplicación de la política aprobada, la matriz de restricciones y los permisos (con Gobierno); básico para todos; intermedio y prueba con la cohorte del mínimo definido en E. Básico, intermedio y prueba comienzan juntos, solo después de congelar la base | Básico completado: ≥90% de la dotación al cierre de los meses 1-3, a revalidar si la base se extiende. Prueba: uso semanal de la cohorte, retrabajo y PR aceptados, y la dispersión entre personas; se leen en la decisión del mes 3, sin atribuir ganancia | Sin objetivo: se mide la línea de base |
| Meses 4-6 | Intermedio para Operaciones y staff; arranca el avanzado; champions con tiempo asignado (el contractor está desde el mes 1 si se aprueba; al 100% solo si la decisión del mes 3 encuentra una señal, si no se cierra y la prueba se extiende a la cohorte) | Uso activo semanal de Tecnología ≥80% en M6 (la meta del OKR); Operaciones habilitadas ≥40% en M6, **meta intermedia** hacia ≥60% en M12 | Throughput de equipos propios: sin deterioro de calidad |
| Meses 7-9 | Casos prácticos por rol publicados por champions; revisión de calidad de prompts | Tecnología ≥80% sostenido; prompts con ejemplos del resultado esperado: de ≤5% a ≥30% (muestra agregada) | Incidentes y retrabajo sin aumento sobre la base |
| Meses 10-12 | Traspaso del contractor a la oficina del CAIO (si la decisión del mes 3 lo liberó; si no, el traspaso se hizo en el mes de preaviso); evaluación de lo que escala | Tecnología ≥85%; Operaciones habilitadas ≥60%; staff ≥50% (meta sin fuente de medición hoy: la telemetría no mide chat ni Gemini) | Hipótesis, no meta: throughput entre +10% y +25% en equipos propios, según el [supuesto de ganancia](../../context/supuestos/ganancia-de-productividad.md); el caso base puede no alcanzarlo |

"Habilitadas" = personas cuyos clientes y herramientas lo permiten según la
matriz, como denominador. Se informa también el valor sobre el total, para no
esconder la brecha.

**Cuatro frentes del roadmap cultural.** El [roadmap tridimensional](../../material/conceptos/m3u4-roadmap-tridimensional.md)
organiza lo cultural en cuatro frentes. Los hitos de arriba ya los cubren; el
cruce muestra dónde hay un hueco:

| Frente | Dónde está en este anexo | Hueco |
|---|---|---|
| Gestión del cambio | Tabla de frenos, comunicación y postura sobre el empleo | No |
| Desarrollo de talento | Roles y capacidad, estudio de un rol crítico (alcance ampliado), transición responsable | No |
| Alfabetización en IA | Literacy por nivel y por rol, hitos de los meses 1-9 | No |
| Cultura de innovación | Prueba con la cohorte y condiciones de abandono | **Parcial:** falta registrar qué no funcionó |

Para cerrar el hueco, cada decisión de los meses 3, 6 y 9 deja en el acta una
línea con lo que se probó y no funcionó (aprendizaje del fracaso). No suma costo
ni un hito nuevo; es una práctica del Council.

**Definir «activo» antes de medir.** Propuesta a ratificar por CAIO, Talento y
Gobierno antes de congelar la base: persona que en la semana completó al menos
una tarea laboral con una herramienta de IA permitida y revisó su resultado.
La fuente debe permitir distinguir esa actividad de un seat o una conexión;
si solo registra eventos del agente de código, se publica como proxy. No se
publican tareas ni datos individuales y no se usa la métrica para evaluar personas.

El diccionario previo fija tarea válida, fuente, padrón por área, numerador,
denominador, semana de corte, umbral de cobertura y tratamiento del faltante. Chat/Gemini requieren
una fuente adicional; una encuesta se rotula como uso declarado. No se suman
usuarios de herramientas sin deduplicarlos. Se publican personas con medición / total
y su porcentaje de cobertura; sin cobertura suficiente, el OKR queda «sin medir»
para ese alcance, sin convertir ausencias en inactividad. La ventana móvil de
cuatro semanas es **una propuesta pendiente de aprobación**; no reemplaza la
medición semanal del borrador ni se impone retrospectivamente.

**Alcance de las metas.** El básico completado ≥90% al cierre del mes 3 es un
criterio del **mínimo**: E costea el básico para toda la dotación (360-420 h) y D lo
lee en M3. Sigue siendo una propuesta, con el instrumento de evaluación pendiente.
Lo que sigue se refiere a las metas de los meses 4-12.

**Alcance de las metas de los meses 4-12.** Los hitos y metas de las filas de los
meses 4-6, 7-9 y 10-12 (intermedio ampliado, avanzado, champions con tiempo
asignado, Operaciones ≥40% y ≥60%, prompts ≥30%, staff ≥50% y Tecnología ≥85%)
son **alcance del programa completo**, sujeto a costeo y autorización adicionales.
La continuidad del mínimo de E no los cubre y **no se promete que se cumplan con
sus techos**. En el mínimo se sigue midiendo la base y el uso por área; las metas
se informan, no se prometen, y su respaldo está en el
[supuesto de metas culturales](../../context/supuestos/metas-culturales-propuestas.md).
La expectativa de throughput de la última fila es una hipótesis del supuesto de
ganancia, no una meta.

**Revisión mensual del Council.** Las metas de arriba se cierran por tramo, pero el
uso se mide cada semana, por área: ese uso semanal alimenta el tablero mensual del
AI Council (revisión de 2 horas). El tablero lo muestra como tendencia, sin decidir
por él, y suma señales de incidentes y avance de hitos. La revisión mensual puede
frenar o cortar un frente, activar una contingencia o escalar una señal al
Directorio cuando llega; **no libera fondos**, que quedan en las dos autorizaciones
iniciales y las decisiones de los meses 3, 6, 9 y 12. Las metas y el momento en que se decide no cambian. La
revisión no suma costo: usa el uso semanal por área que este anexo ya mide y el
Council que el Anexo E ya presupuesta.

**Calendario del mínimo.** Primera liberación propuesta de **80-136 h**:
20-40 h técnicas existentes y 60-96 h organizativas nuevas; **techo de 8k USD
de tiempo valorizado y caja incremental cero**, con autorización e imputación
previas para 2026. Son supuestos de la
[validación inicial](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial),
consolidados en [E](05-business-case.md#pedido-inicial-paquete-mínimo).
El calendario de 60-100 h pertenece al programa completo, no al pedido vigente.

| Cuándo | Qué existe | Quién lo verifica | Costo |
|---|---|---|---|
| Preparación previa de 2026, diez días hábiles condicionados a agendas y accesos | Validación del diagnóstico, padrón, matriz persona-semana y restricciones; conciliación económica, verificación y acta de continuar, reducir/resecuenciar o detener | Productor, verificador independiente y autoridad firmante distintos, a designar conforme a C | 80-136 h y techo de tiempo de 8k USD; caja cero; autorización e imputación 2026 propias, separadas de M1-M3 |
| Antes de M1, segunda liberación | Diagnóstico revisado, capacidad y desplazamiento aceptados, roles empresariales designados y presupuesto 2027 comprobado | Autoridad empresarial según C, con conformidad de Operaciones y managers sobre agendas | Libera el alcance y los recursos M1-M3 conciliados en E; no habilita por sí sola herramientas ni prácticas |
| Meses 1-3, semanas 1 a 4, ampliables a 8 por el criterio de B | Base prospectiva congelada antes de cualquier tratamiento | Oficina del CAIO, con Arquitectura para el criterio y Finanzas para throughput | Dentro de las tareas de soporte del mínimo conciliadas en E |
| Meses 1-3, desde semana 5 si cierra la base, o semana 9 si se amplía | Aplicación de la política aprobada y permisos aplicables verificados como condición de inicio; básico, intermedio y prueba comienzan juntos, con la cohorte definida en E | Gobierno, Operaciones y oficina del CAIO; responsables a designar | Participantes y soporte consolidados en E; agendas aún no liberadas |

Retrospectiva y prospectiva no se mezclan: la retrospectiva informa tendencia y
ruido, sin atribuir ganancia. La atribución requiere base prospectiva congelada;
si no resuelve en semana 4, se aplica el criterio de extensión de B y se deja
constancia para la decisión M3. No se presume que el básico no contamina la base.

Si se amplía la base hasta semana 8, **básico, intermedio y prueba comienzan
juntos en semana 9**. Se revisan completitud ≥90% en M3, agendas y costeo con
B/E/F; no se promete completar el mismo alcance en cinco semanas sin validarlo.
Si tampoco resuelve al cierre de la extensión, se informa el faltante y no se
atribuye ganancia ni se sustituye la base por la retrospectiva.

**La formación, ¿llega antes de cada gate?** Verificación de secuencia contra el
roadmap de arriba. Salvo la fila del mes 3, la tabla describe el **programa
completo**; en el mínimo el intermedio de M1-M3 es solo la cohorte de 15-20 y no
hay avanzado:

| Gate | Qué lee | Formación previa | Resultado de la verificación |
|---|---|---|---|
| Mes 3 (único del pedido mínimo) | Uso semanal de la cohorte, retrabajo y PR aceptados; completitud del básico ≥90% | Básico, intermedio y prueba empiezan **juntos** después de congelar la base: semana 5 (nueve semanas hasta el cierre) o semana 9 (cinco semanas) | **No llega antes: llega a la par.** La lectura es de una cohorte recién formada y por eso no atribuye ganancia; con base ampliada, la meta de ≥90% se revisa en vez de prometerse |
| Mes 6 | Tecnología ≥80%; Operaciones habilitadas ≥40% | Básico en M1-M3; intermedio de Operaciones y staff en M4-M6 | Para Operaciones, intermedio y meta caen en el mismo tramo: el margen no está demostrado |
| Mes 9 | Prompts con ejemplos ≥30%; Tecnología ≥80% sostenido | Casos por rol publicados por champions en M7-M9 | Casos y meta en el mismo tramo: se lee al cierre, sin margen previo |
| Mes 12 | Tecnología ≥85%; Operaciones habilitadas ≥60%; staff ≥50% | Por cohorte: Tecnología, con intermedio desde M1-M3 y avanzado en M4-M6; Operaciones y staff, con intermedio en M4-M6 | El margen difiere por cohorte y no se cuantifica acá; la secuencia debe ratificarse por ruta |

Los gates de M6 a M12 dependen de intermedio ampliado, avanzado y champions, que
no están en el pedido de hoy: solo corren si las decisiones de los meses 3, 6 y 9
los autorizan. Las metas no se mueven; la verificación deja a la vista que M3, M6
y M9 se leen con la formación llegando a la par, no antes.

**Meta de adopción y OKR combinado.** El borrador de OKR pide 80% en
Operaciones y Tecnología juntas. Con áreas de igual peso, **cumplir exactamente**
85% en Tecnología y 60% en Operaciones habilitadas da los siguientes resultados.
Si `e` es la fracción de Operaciones habilitada, y solo ese grupo aporta uso
contado, el combinado es `(85% + 60% × e) / 2`:

| Operaciones habilitada (% de Operaciones) | Operaciones habilitadas 60% da, sobre Operaciones total | Combinado con Tecnología 85% (igual peso) |
|---|---|---|
| 25% | 15% | 50% |
| 50% | 30% | 57,5% |
| 100% (toda Operaciones habilitada) | 60% | 72,5% |

El 72,5% es el resultado de esas metas exactas con toda Operaciones habilitada,
**no un máximo teórico**: son metas mínimas y pueden superarse; ambas áreas al
100% darían 100%. Para llegar a 80% combinado con Tecnología en 85%, Operaciones
necesita 75% sobre su total. Por eso no se declara cumplido el OKR con la tabla.

Se conservan las metas por área y se publica además el **combinado original**:
`(activos de Tecnología + activos de Operaciones) / (total de Tecnología + total de
Operaciones)`, con los pesos del padrón real. Para cada área se muestran activos / total;
para Operaciones también activos habilitados / habilitados, habilitados / total y
su tasa sobre el total. Se informa la cobertura de medición por área y combinada;
el proxy de código no representa toda la IA. Un uso permitido fuera del grupo
habilitado por la matriz requiere registro específico y recalcular el ejemplo.
No se predice el resultado real del OKR a partir de metas. Metas por tramo
unificadas para todo el plan (incluido el Anexo F): Tecnología ≥80% desde los meses
4-6 (cifra del OKR) y ≥85% al cierre de los meses 10-12 (meta interna de este
anexo); Operaciones habilitadas ≥40% en M6 es una meta intermedia hacia ≥60% en
M12. El 72,5% corresponde a **85%/60% en M12**, con igual peso y toda Operaciones
habilitada; no corresponde a las metas de M6.

**Criterios de éxito del programa completo (al cierre de los meses 10-12; no los
cubre el mínimo):** Tecnología ≥85% de uso
semanal activo; Operaciones habilitadas ≥60%; nivel básico ≥90%; ningún aumento de
incidentes ni retrabajo en equipos propios; capacidades críticas con un reemplazo
documentado.

**Condiciones de abandono o cambio de rumbo.** Se evalúan en el momento que dice
cada fila; el tablero mensual del Council muestra la tendencia antes, pero no las
dispara por sí solo.

| Disparador | Acción |
|---|---|
| Programa completo: capacidad clave efectiva en los meses 1-3 <1,6 FTE | No iniciar ese alcance; reducir o diferir y volver a costear. Este umbral no es el piso del mínimo vigente: sus tareas y horas se concilian en E, «Pedido inicial: paquete mínimo» |
| Programa completo: capacidad clave entre 1,6 y ~1,8 FTE en los meses 1-3 | Retirar la prueba de ese alcance y revisar metas, calendario y costeo; confirmar también las horas distribuidas. No completar horas iniciales con ganancias futuras ni trasladar estos pisos al mínimo de E |
| Al cierre de los meses 4-6, uso activo en Tecnología <60% pese a tiempo asignado | Suspender en los meses 7-9 las horas de champions y de intermedio que no sean rediseño (~13k USD de tiempo en el medio del programa completo, la cifra del Anexo E; en el mínimo no hay horas de champions ni de intermedio de los meses 7-9 que suspender); rediseñar la formación con casos por rol; revisar causas con los managers. El plan no suma seats: no hay expansión que frenar |
| Al cierre de los meses 4-6, uso activo en Tecnología ≥60% y <80% | Los meses 7-9 siguen; formación rediseñada con casos por rol; se vuelve a medir al cierre de los meses 7-9 (como en el Anexo F) |
| Lectura del mes 3: básico completado ≥50% y <90%, con la evaluación práctica por rol y el denominador de la dotación (meta revisada si la base se extendió) | Se rediseña el formato, como en la banda del Anexo F; no se liberan ni se cortan fondos por esta lectura sola |
| Lectura del mes 3: básico completado <50% | Cambio de formato (de sesión a práctica en equipo) y reasignación de tiempo; no se repite el mismo curso. Se decide en el mes 3, no al cierre de los meses 4-6 |
| Asistencia de champions <60% dos meses seguidos | Disolver la red o rediseñar su mandato con sponsor nuevo |
| Subida de incidentes o retrabajo asociada a uso de IA | Pausar el nivel avanzado hasta revisar compuertas de calidad con Arquitectura |
| La decisión del mes 3 sin ninguna señal (contractual, precio por consumo o cliente del producto) | Cerrar el contractor (preaviso de un mes, traspaso a la oficina del CAIO) y correr los meses 4-12 como la alternativa de gobierno mínimo y formación del Anexo E, con la prueba extendida a la cohorte; las lecturas de los meses 6 y 9 releen las señales |
| Prueba chica: sube el retrabajo o los incidentes contra la base, o la matriz no habilita repositorios para la cohorte | Suspender la prueba (Anexo E); el intermedio de Tecnología sigue |
| Contractor de IA sin entregable verificable al cierre de los meses 7-9 | No renovar; traspasar a la oficina del CAIO |

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| La capacitación desplaza horas facturables y baja utilización | Alta (utilización 83-90%, sin bench) | Medio | Horas topeadas por tramo de tres meses (ver Insumos para Finanzas); módulos cortos; calendario por equipo | Utilización <80% (meta interna) atribuible al programa |
| Operaciones no puede adoptar por contrato del cliente | Alta | Medio | Matriz de clientes; meta sobre habilitadas; usos permitidos | Matriz sin completar al cierre de los meses 1-3 |
| Champions sin tiempo ni entregable | Media | Medio | Mandato, sponsor y entregable por tramo | Ver tabla de abandono |
| Pérdida de una persona clave en arquitectura, seguridad o gobierno | Media | Alto | Contractor a prueba, documentación, transferencia (programa completo). En el mínimo no hay contractor continuo: E solo prevé 4-8 h de IA aplicada por tramo y no hay un reemplazo costeado; la documentación obligatoria con dueño y un par designado quedan **a designar y costear** | No hay reemplazo documentado al cierre de los meses 7-9 |
| El 0,2 del contractor no está libre en los meses 4-6 y el replan del Anexo B no se sostiene | Media (supuesto sin confirmar) | Medio: los meses 4-6 vuelven a 2,5 FTE clave | Alcance contractual con evals en CI y prueba de portabilidad antes de la aprobación del paquete completo; excepción de 0,3 FTE propuesta como respaldo, que requiere aprobación antes de activarse | Control de la semana 20 del plan (la séptima de los meses 4-6) sin documentación mínima reproducible, o alcance contractual sin los dos entregables al cierre de los meses 1-3: se solicita la autorización de la excepción de 0,3 FTE; no se activa sola ni está incluida en el mínimo |
| No hay contractor (no se aprueba o no se contrata a tiempo): la excepción de 0,3 no alcanza | Media (depende del Directorio, decisión sobre IA aplicada) | Alto: falta toda la fracción de 0,8 FTE de IA aplicada; con fracción interna los meses 4-6 pedirían ~3,3 FTE clave | Modo control del Anexo B (2,2 FTE clave, sin hitos de IA aplicada) en vez de cubrirlo con tiempo; decisión del board al aprobar el paquete completo | Sin contractor contratado al cierre de los meses 1-3: la decisión del mes 3 libera el modo control ([Anexo E](05-business-case.md)) |
| Adopción declarada ≠ uso real (seats comprados, uso detectado) | Media | Medio | Medir uso real semanal por área, no seats; el tablero mensual del Council lo muestra cada mes | Métrica de seats sin correlato en uso |
| Telemetría solo cubre el agente de código | Alta | Medio | Medir chat y Gemini por encuesta o telemetría ampliada, con Arquitectura y Gobierno | Sin medición de staff al cierre de los meses 1-3 |
| Miedo al reemplazo reduce la adopción y la franqueza | Media | Medio | Comunicación transparente y compromiso sobre el empleo (ver Decisiones) | Caída de uso tras un anuncio o un cambio de estructura |
| La transición carga de más a junior o a Operaciones y staffing | Media (hipótesis sin contrastar) | Medio | Chequeo de equidad por grupo; staffing no se evalúa por uso; participación en el mapeo | Diferencia entre grupos sin explicación de agenda o contrato en la revisión mensual |
| El estudio de un rol se lee como paso previo a un recorte | Media | Medio | Postura sobre el empleo comunicada antes; participación del rol; el estudio no decide desvinculaciones | El rol no valida el mapeo al cierre de su tramo (el estudio es alcance ampliado y no inicia con el mínimo) |
| El consumo real a precio de API (~12x lo pagado) sube el costo si cambia el esquema de precios | Media | Alto (no es de personas) | Lo trata Finanzas; este anexo solo informa que más uso empuja ese costo | Ver anexo de Finanzas |

## Decisiones

| Tema | Decisión | Alternativas | Elección | Reversibilidad |
|---|---|---|---|---|
| Meta de adopción | Cómo medir la meta de adopción en Operaciones | (1) 80% sobre Operaciones y Tecnología, como el borrador de OKR. (2) 80% en Tecnología y una meta propia sobre personas **habilitadas** en Operaciones. | **La segunda**, informando también la primera | Reversible: se cambia al completar la matriz |
| IA aplicada | Capacidad especializada en IA aplicada | (1) Sin incorporación, solo reasignar con perfil demostrado. (2) Contractor a prueba desde el mes 1 (50% en los meses 1-3, 100% posterior condicional). (3) Lo mismo desde el mes 4. (4) Dos contrataciones en nómina. | **El programa publicado propone el contractor desde el mes 1 como excepción externa**, no como cumplimiento de «no contratar». Consume caja aunque no amplíe nómina; la excepción y el contrato los decide el Directorio. El paquete mínimo se vuelve a costear antes de decidir si requiere esa vía. Sin perfil interno demostrado ni excepción aprobada, no se inician sus hitos | Contrato corto, con cierre y traspaso costeados. Si existe contractor, pero falta el 0,2 del replan, la excepción de 0,3 FTE internos cubre ese exceso acotado. Sin especialista falta el 0,8 completo: la excepción de 0,3 **no lo reemplaza**; aplicar modo control o diferir y volver a costear según B/E |
| Compromiso sobre el empleo | Qué se dice sobre el empleo | (1) Sin compromiso. (2) Compromiso explícito de que la ganancia por IA no se usa para desvincular durante los 12 meses. (3) Compromiso con excepciones. | **Postura propuesta: el compromiso con excepciones**, con el texto de "Postura sobre el empleo (propuesta)". La decide el Directorio, con asesoría laboral; no es una política aprobada. El compromiso sin excepciones baja más el miedo pero ata margen; sin compromiso deja el freno sin respuesta | Los dos compromisos son poco reversibles una vez comunicados |
| Formato de la formación | Formato de la formación | (1) Curso obligatorio genérico. (2) Casos prácticos por rol con champions, en horario laboral. | **Los casos prácticos por rol**, por el pedido del piloto (más de la mitad de 12 autoseleccionados) y porque la falta de tiempo fue el primer freno; el efecto del formato se mide en los meses 4-9 | Reversible |
| Piso de alfabetización | Art. 4 del AI Act | (1) Esperar a decidir si alcanza a Acme Labs. (2) Adoptarlo como piso, con registro. | **Adoptarlo como piso**, sin citar fechas ni sanciones | Reversible |
| Compensación | Si el plan cambia cómo se compensa a quienes trabajan con IA en los 12 meses | (1) Sin cambios de compensación; los modelos nuevos quedan fuera de alcance. (2) Reconocimiento **no monetario** a champions y al líder: tiempo protegido (el 10% ya definido), visibilidad ante el Directorio y registro en su desarrollo de carrera. (3) Prima o bono por colaboración humano-IA, uno de los [modelos del curso](../../material/conceptos/m3u3-compensacion-futuro-sintetico.md). (4) Prima por gestión de sistemas complejos para el especialista | **La 1 para lo monetario, más la 2.** La 3 exige medir impacto por persona y choca con la regla de no medir uso individual, y la caja incremental es cero. La 4 solo aplica al contractor, que se negocia por contrato. Se revisa con evidencia en la decisión del mes 12 para 2028. Costo de la 2: sin cifra; es tiempo ya computado. Responsable: a designar | Reversible: se agrega después; quitar un incentivo ya comunicado es difícil |

### Postura sobre el empleo (propuesta) y métricas de comportamiento

**Propuesta, no política aprobada.** Texto sugerido para el Directorio, a revisar
con asesoría laboral antes de comunicarlo: «Durante los 12 meses del plan, la
ganancia de productividad por IA no se usa para desvincular a una persona.
Primero se reasigna y se capacita. Quedan afuera, y se dicen de antemano, las
causales que ya existían sin relación con la IA (desempeño sostenido, causa
justa, pérdida de un cliente).» Es la postura con excepciones de la decisión sobre
el empleo. Alternativas: el compromiso sin excepciones (más tranquilizadora, ata
más el margen); y sin compromiso (no responde el miedo al reemplazo, que es un
freno típico de adopción). **Costo y riesgo:** el costo es de margen y lo
cuantifica Finanzas; no está en este anexo. Riesgo: una promesa que no se cumple
destruye la confianza que se busca; por eso se comunica solo después de la decisión
del Directorio.

**Métricas de comportamiento** (qué hace la gente, no qué declara). Todas por
área, agregadas, con numerador y denominador y sin dato individual. Línea de base
en los meses 1-3; las que no tienen fuente hoy son supuestos. El uso
semanal por área alimenta el tablero mensual del Council; las metas de las filas
con meta se leen al cierre de cada tramo:

| Comportamiento observable | Cómo se observa | Qué señala | Fuente |
|---|---|---|---|
| Pedidos con ejemplos del resultado esperado | Muestra agregada de prompts del chat | Calidad de uso (hoy ≤5%, meta ≥30% en los meses 7-9) | [Encuesta y pilotos](../../context/hechos/encuesta-y-pilotos-ia.md) |
| Cambios con asistencia de agente que pasan la compuerta de pruebas y revisión de un humano distinto del autor | Registro del repositorio y de la compuerta | Supervisión real, no aprobación de trámite | Supuesto; depende de Arquitectura |
| Consultas de uso y reportes de incidentes de staffing | Conteo del canal de consultas | Confianza para preguntar: sube al principio, y eso es bueno | Supuesto |
| Asistencia a módulos y a talleres de champions | Registro de asistencia | Tiempo realmente liberado | Supuesto |
| Pulso anónimo cada tres meses: miedo a ser reemplazado | Encuesta de tres preguntas, con mínimo de respuestas por grupo | Si el miedo baja con la comunicación | Supuesto; no hay medición propia hoy |
| Rotación voluntaria de perfiles junior | Dato de Talento, por área | Efecto colateral del miedo | Supuesto; la serie histórica es un faltante |
| Horas de formación liberadas, por grupo (junior y resto; Operaciones, staffing y Tecnología) | Registro de asistencia, agregado por grupo con mínimo de personas | Equidad de la transición: nadie queda afuera por agenda | Supuesto |

**No se miden** el uso por persona ni el volumen de prompts como desempeño
individual: esa medición mataría la franqueza que se necesita. Un cambio de
comportamiento sin mejora en tiempo de ciclo o calidad (los indicadores
rezagados) se lee como uso de trámite y dispara la revisión del formato.

### Tensiones con otras miradas

- **Con Finanzas.** El caso de negocio supone 10% a 25% de throughput solo
  en equipos propios y descuenta staffing. En contratos facturados por hora,
  menos horas es menos facturación, así que el staffing tiene un incentivo en
  contra de usar IA. Alternativas: no medir productividad en staffing y
  medir solo habilitación; o evaluar un cambio de modelo comercial (precio por
  resultado), que excede este anexo. Se deja visible.
- **Con Gobierno.** La matriz de clientes y la verificación de aplicación y
  permisos de la política aprobada son prerrequisitos de la meta de Operaciones y están fuera de este
  anexo. Si no se cierran al fin de los meses 1-3, la decisión sobre la meta de
  adopción pasa de la meta propia sobre habilitadas a "sin meta en Operaciones".
- **Con Finanzas, sobre incentivos.** Compensar la colaboración humano-IA
  requiere medir impacto por persona, y este anexo no mide uso individual; además
  la caja incremental es cero. Alternativas: reconocimiento no monetario ahora y
  revisar un esquema monetario con evidencia en el mes 12, o aceptar la medición
  individual con un diseño aparte que excede este anexo. Se deja visible.
- **Con Gobierno.** El estudio de un rol usa tareas reales del rol: requiere que
  Gobierno defina qué se puede inventariar y con qué clasificación, y quién ve el
  resultado, sin que se convierta en evaluación de desempeño.
- **Con Arquitectura.** Medir uso en chat y Gemini requiere instrumentación
  que hoy no existe; sin eso, la métrica de staff es una encuesta.

## Insumo para el paquete mínimo

**Supuestos de planificación a conciliar con B/C/E, no agendas liberadas.**
Recomendación para M1-M3: básico de uso seguro para toda la organización, sin
plataforma central, avanzado, red de champions al 10% ni contractor especializado
continuo por defecto. No sustituye los controles de B/C ni prueba throughput.

**Reserva propuesta.** Solicitar hasta **720 h de soporte clave (1,5 FTE de
costeo)**, repartidas entre roles, más **540-660 h de formación**; máximo
combinado **1.380 h**, sin preparación previa ni cierre condicional.

Es un supuesto de planificación: Operaciones y los managers confirman personas,
agendas y trabajo desplazado antes de iniciar cada actividad. La demanda de
soporte sigue en 430-690 h; las 30 h de margen no están costeadas para ejecutar.

La [fuente del mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md#reserva-propuesta-de-capacidad-m1-m3)
separa demanda, reserva y autorización. Si alguien cumple varios roles y se
capacita, la matriz semanal suma todas sus cargas sin duplicarlas.

**Cuatro cosas que no se confunden.** Las cifras de arriba mezclan, si se leen
rápido, lo que se pide reservar, lo que se calculó, lo que existe y lo que falta
decidir:

| Concepto | Qué es | Cifra M1-M3 | Estado |
|---|---|---|---|
| Reserva propuesta | Capacidad que se pide apartar, como techo de planificación | Hasta 720 h de soporte clave (1,5 FTE de costeo) + 540-660 h de formación; máximo 1.380 h | Supuesto elegido por Martín para el borrador; no es horas ejecutadas |
| Demanda costeada | Actividades con rol y costo asignados | 970-1.350 h = 430-690 h de soporte clave + 540-660 h de formación; las 30 h de margen (1.380 − 1.350) no tienen actividad ni rol | Cálculo de Finanzas sobre supuestos, consolidado en E |
| Disponibilidad real | Horas que cada persona puede dar sin desplazar otro trabajo | **Sin dato**: la utilización promedio y el bench no la prueban | La produce la matriz privada en la primera liberación; hoy nadie la confirmó |
| Decisiones futuras | Lo que aún no se autorizó | Ver la tabla siguiente | Ninguna está aprobada |

Se recalcularon los componentes: 430 + 540 = 970 y 690 + 660 = 1.350 h;
720 + 540 = 1.260 y 720 + 660 = 1.380 h; 1.380 − 1.350 = 30 h; 720 / 480 = 1,5 FTE.

| Decisión | Cuándo | Quién decide | Estado |
|---|---|---|---|
| Autorizar la validación inicial: 10 días hábiles, 80-136 h, techo de 8k USD de tiempo, caja 0 | Hoy, para la preparación previa (octubre-diciembre de 2026) | Directorio o autoridad formalmente delegada, a designar ([RACI de C](03-gobierno-seguridad.md)) | Pedido del plan; sin aprobar. Exige antes agenda, accesos e imputación 2026 confirmados |
| Techo de autorización acumulado de 79k USD (caja 9 + tiempo 59 + preparación técnica 3 + validación organizativa 5 + reservas 3), sin liberar hoy los 71k USD restantes | Hoy | Ídem | Pedido del plan ([E](05-business-case.md#pedido-inicial-paquete-mínimo)). Es un techo, no un gasto esperado |
| Formar y reasignar, sin contratar; intervención externa de 16-32 h que reemplaza la facilitación solo si falta perfil interno | Hoy, y al armar el básico | Directorio, con cotización y aparte del techo | Pedido del plan; sin cotización |
| Segunda liberación: hasta 71k USD (caja 10, tiempo 61) para M1-M3 y cierre | Antes de M1 | Ídem, con conformidad de Operaciones y managers sobre las agendas | Futura. Condicionada a diagnóstico revisado, capacidad sin sobreasignaciones, roles designados y presupuesto 2027 comprobado |
| Continuar, reducir o cortar | Meses 3, 6, 9 y 12 | Ídem | Futuras. El Council recomienda; no libera fondos |
| Paquete completo: contractor de IA aplicada, excepción de 0,3 FTE, avanzado, champions al 10% | Si una decisión futura lo pide | Directorio | **No se pide hoy**; requiere alcance, calendario y costeo nuevos |
| Postura sobre el empleo | Antes de comunicar los cambios de rol | Directorio, con asesoría laboral | Propuesta, no política aprobada |

Comprobación: 9 + 59 + 3 + 5 + 3 = 79 y 10 + 61 = 71; 8 + 71 = 79.

**Formación.** Mantener 6 h por persona del básico: clasificación de datos,
herramientas y superficies permitidas por cliente, revisión del resultado,
consulta e incidente. Incluye Tecnología, Operaciones, staff y dirección, con
casos por rol y datos sintéticos o autorizados.

Las restricciones del cliente no excluyen a las personas del básico ni autorizan
uso sobre ese cliente. Población supuesta: 60-70 personas, referencia ~65
([tamaño y estructura](../../context/hechos/tamano-y-estructura.md)); reservar
**360-420 h**, aunque la meta de completitud M3 sea ≥90%.

| Rol / actividad | Horas M1-M3 propuestas | Fuente o supuesto / qué desplaza |
|---|---|---|
| Participantes de todas las áreas: básico | 360-420 distribuidas | 60-70 × 6 h, desde tamaño/estructura y el nivel básico de este anexo. Puede desplazar delivery, soporte o trabajo de staff, según agenda y contrato |
| Líder interno de adopción: agenda, base, diccionario de actividad, seguimiento y cierre | 48-96 clave | Supuesto de Personas: 0,1-0,2 × 480 h; el extremo alto coincide con el líder del programa completo al 20%. Desplaza liderazgo técnico; no es tiempo libre |
| Facilitación técnica del básico: adaptar casos y dictar sesiones | 16-32 clave | Supuesto de Personas: 8-16 h de preparación + 8-16 h de facilitación de grupos. No incluye evals, harness ni implementación. Desplaza trabajo técnico |
| Managers / Operaciones: validar agendas y cruzarlas con las restricciones de C | 8-16 clave | Supuesto de Personas agregado, no por manager. Desplaza coordinación de delivery. **Posible doble conteo, sin resolver:** la primera liberación ya valida «agendas propias y M1-M3» (60-96 h, fila de liderazgo técnico y managers). Por la regla de «Preparación» (lo adelantado se descuenta una sola vez), lo que esa validación deje cerrado se resta de estas 8-16 h y queda la actualización semanal y el cruce con C. Las horas **no se cambiaron**: el descuento lo deciden el responsable humano de D y el de B (#16, #18) |
| Talento / administración: convocatorias y registro de completitud | 8-16 distribuidas | Supuesto de Personas agregado. Desplaza trabajo de staff |
| QA / datos: extracción y reproducción del indicador existente | 8-16 clave | Supuesto de Personas, solo sobre fuentes existentes, sin plataforma nueva. Desplaza QA o análisis. Si la fuente no permite medir, declarar «sin medir» y volver a costear la instrumentación |
| **Subtotal interno de Personas** | **448-596 h** | **80-160 clave + 368-436 distribuidas**, extremos sumados; punto poblacional ~65: 478-566 h |

No es el total del paquete: B/C/E agregan arquitectura, controles, gobierno,
intermedio y prueba. Finanzas concilia solapes antes de sumar: diccionario,
extracción y revisión pueden figurar en otros insumos. Ningún bloque cuenta
dos veces por tener dos dueños.

Las 6 h de básico del líder, facilitador o manager están en participantes;
el soporte es trabajo adicional, con bloques distintos. Si una persona cubre
varios roles, libera la suma en su agenda semanal. No se heredan los ~1,8 FTE
ni el contrato 0,5 FTE del programa completo.

**Preparación.** Las 8-16 h de preparación de facilitación están dentro de su
fila, no son un adicional. Las 20-40 h técnicas existentes quedan separadas de
las **60-96 h organizativas nuevas** de la primera liberación. Toda tarea de
B/C/D ya presupuestada que se adelante se descuenta una sola vez de su
ejecución posterior; no se suma el subtotal bruto de Personas a E.

**Validación organizativa inicial: estimación de Finanzas (agente); la estimación humana de Personas (#18, pregunta 3) sigue pendiente.** Estimación de
planificación de la [fuente canónica](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial),
sin agendas ni responsables empresariales confirmados:

| Rol, incluidos participantes y decisores | Horas nuevas de preparación 2026 | Trabajo incluido |
|---|---:|---|
| Liderazgo técnico, coordinación y managers | 16-24 | Convocar y coordinar; validar agendas propias y M1-M3, desplazamiento y cobertura; preparar y tomar la decisión y cerrar el acta |
| Analista funcional | 20-32 | Contrastar diagnóstico y documentación; preparar, conducir y sintetizar 4-6 entrevistas de una hora; conciliar padrón y matriz persona-semana |
| Staff de Operaciones, Talento, Comercial y Finanzas, incluidos entrevistados | 16-24 | Participar de entrevistas; aportar compromisos y ausencias; relevar restricciones y roles con C; conciliar horas, costos y solapes B/C/D; aportar evidencia al cierre |
| Verificador senior independiente del productor | 8-16 | Contrastar entregables y conciliación con fuentes; registrar brechas, revisar acta y cierre documental |
| **Total organizativo adicional** | **60-96** | Entrevistados, managers, decisor, preparación, síntesis, verificación y cierre incluidos; no volver a sumar sus horas |

El rol concreto de cada entrevistado se registra en privado y sus horas se
imputan una sola vez a su fila. No se presupone que coordinación, entrevistas
y decisión puedan hacerse por fuera de la jornada.

**Las mismas 60-96 h, por actividad** (misma [fuente canónica](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial);
la matriz de capacidad es la segunda y la cuarta fila):

| Actividad | Liderazgo técnico y managers | Analista | Staff | Verificador | Total, h |
|---|---|---|---|---|---|
| Entrevistas y contraste del diagnóstico | 4-8 | 4-6 | 8-12 | — | 16-26 |
| Conciliación del padrón y matriz persona/semana | 4 | 8-14 | 4-6 | — | 16-24 |
| Estado de políticas, restricciones y separación de funciones | 4-6 | 4-6 | 2 | 4-8 | 14-22 |
| Conciliación económica, solapes y trabajo desplazado | 2 | 4-6 | 2-4 | — | 8-12 |
| Verificación, decisión y cierre documental | 2-4 | — | — | 4-8 | 6-12 |
| **Total** | **16-24** | **20-32** | **16-24** | **8-16** | **60-96** |

Recálculo: 16 + 16 + 14 + 8 + 6 = 60 y 26 + 24 + 22 + 12 + 12 = 96 h por filas;
16-24 + 20-32 + 16-24 + 8-16 = 60-96 h por columnas. Las dos filas ligadas a la
matriz suman 24-36 h (16-24 + 8-12) de las 60-96.

**Qué falta: la estimación humana de la matriz.** Las 16-24 h de la fila de
padrón y matriz son una estimación de Finanzas (agente). Personas (agente) no
tiene una cifra propia para reemplazarla y **tampoco hay estimación del responsable humano de D**:
la confirma o corrige él. Lo que sí se puede decir es qué tendría que cumplirse
para que esa magnitud se sostenga:

- D pide una fila por persona, rol y semana, y la matriz incluye el básico de
  toda la organización: 60-70 personas × 13 semanas = **780-910 filas**
  ([convenciones](../../context/supuestos/convenciones-de-calculo.md)).
- Con 16-24 h, el tiempo por fila es 960 min / 910 ≈ 1,1 min en el extremo más
  exigente y 1.440 min / 780 ≈ 1,8 min en el otro. Eso solo es posible si:
  (1) padrón, ausencias y compromisos se **exportan** de una fuente existente de
  staffing u horas, no se cargan a mano; (2) quien solo hace el básico se
  planifica **por bloque de área o turno**, y el detalle persona/semana queda para
  quienes tienen horas clave, la cohorte del intermedio y los roles acumulados; y
  (3) los managers confirman la agenda de su equipo dentro de las 4 h de la fila
  de liderazgo técnico y managers, algo que este anexo no sostiene con datos.
- Si alguna falla, la estimación sube y se vuelve a costear antes de empezar;
  este anexo no puede cuantificar cuánto. Referencia aritmética, no margen disponible: contra el extremo alto
  calculado (4,1k USD) y el techo de 5k USD quedan 0,9k USD, unas 14 h extra de
  liderazgo técnico al costo alto (900 / 62,5), 26 de analista (900 / 34,375) o 29
  de staff (900 / 31,25). Contra el extremo bajo (1k USD) la diferencia sería
  mayor. Si el costo real excede el techo, se vuelve a costear.
- **Propuesta para medirlo (agente, no aceptada):** el día 2 de la ventana, un
  piloto de una hora con un área para medir minutos por fila y confirmar si
  existe un export; responsable, el responsable humano de D con un manager de
  Operaciones a designar. Se hace dentro de la fila de matriz ya costeada.

El plazo propuesto es **diez días hábiles**, sujeto a accesos, fuentes y agendas:
días 1-4, diagnóstico y entrevistas; 2-7, padrón y capacidad; 4-8, restricciones
y roles con C; 7-9, conciliación y verificación; día 10, decisión y acta.
La primera liberación autoriza producir esa evidencia; no exige tenerla antes.

Operaciones y managers confirman la agenda de esta preparación y el trabajo
desplazado antes de iniciarla. No consume las **720 h** de reserva de soporte
ni las **30 h** de margen de M1-M3. Si las fuentes, entrevistas o correcciones
exceden el alcance, se vuelve al autorizante antes de ampliar plazo o recursos.

La salida admite **continuar, reducir/resecuenciar o detener**. Continuar exige
diagnóstico revisado, capacidad M1-M3 sin sobreasignaciones y presupuesto 2027
comprobado; los faltantes que bloqueen el alcance impiden esa segunda liberación.
El crédito presupuestario no reemplaza permisos legales ni de seguridad.

La conformidad de Martin habilita incorporar esta propuesta al borrador; no
representa autorización empresarial, designación de roles ni consenso del equipo.

**Trabajo desplazado y recuperaciones.** Completar en privado la matriz de
«Capacidad efectiva: dos bolsas sobre las mismas personas», con personas,
semanas, entrega desplazada, reemplazo y recuperación verificable.
No se supone recuperación ni ingreso o contribución cero.

La formación puede desplazar facturación; el salario existente es costo de
tiempo, no caja incremental. Finanzas valúa costo cargado por rol y concilia
ingreso y contribución perdidos sin duplicación. Son hipótesis de planificación,
no capacidad demostrada.

**Excepción externa sustitutiva.** Si no hay perfil interno con esas 16-32 h de
facilitación, comparar liberarlo contra una intervención externa acotada de
**16-32 h que reemplace esa fila**, sin sumar ambas. Precio, caja y preaviso
requieren cotización; no se presume permiso para contratar.

La excepción la decide el Directorio. Sin vía demostrada, diferir el módulo y
volver a costear; no reemplazar un especialista de B con 0,3 FTE internos.

**Dependencias y secuencia.** C define política, permisos y superficies;
Operaciones y managers liberan agendas antes de iniciar. Responsables a
designar. Básico, intermedio y prueba respetan el calendario del mínimo:
base congelada primero, inicio conjunto desde semana 5 o semana 9.

**Intermedio de cohorte.** E incorpora 15-20 participantes × 12 h = 180-240 h,
además del básico; no están en el subtotal de Personas de arriba. B define el soporte
de prueba y E lo concilia una sola vez. La cohorte y su capacidad requieren
validación de los responsables; el básico solo no compra la prueba publicada.

### Comparación de alternativas de formación (#13 y #18, abierta)

**Problema.** La formación distribuida suma 540-660 h de las 970-1.350 h de
M1-M3. Dos escenarios emparejados, no los límites de un rango de proporciones:
en el extremo bajo, 540 / 970 = 55,7% de las horas; en el alto, 660 / 1.350 =
48,9%. A 10-35 USD/h son 5,4-23,1k USD de 14,3-58,3k USD de tiempo valorizado,
con los mismos emparejamientos: 37,8% y 39,6%. Repartida, son 6 h por persona del básico y 12 h
más para la cohorte de 15-20. Cálculos de este anexo sobre la
[supuestos del mínimo](../../context/supuestos/paquete-minimo-de-aprendizaje.md).

| Alternativa | Qué es | Horas M1-M3 | Efecto en esfuerzo, evaluación y calendario | Estado |
|---|---|---|---|---|
| A. Vigente | Básico de 6 h para 60-70 personas + intermedio de 12 h para la cohorte de 15-20 | **540-660** (360-420 + 180-240) | Evaluación práctica por rol; básico, intermedio y prueba empiezan juntos desde la semana 5, o la 9 si se amplía la base | Costeada en E. Es la única |
| B. Núcleo y profundización | Un núcleo obligatorio de uso seguro para todos, y profundización según perfil, herramienta autorizada y práctica | **Sin cifra**: faltan la duración del núcleo, qué perfiles profundizan y cuántas personas | Puede aliviar la agenda de quienes no usan la herramienta, pero suma diseño de rutas, evaluación por ruta y seguimiento. Los contenidos de control del básico no se pueden recortar | Por costear (Finanzas) y acordar (#13) |
| C. Secuenciar | Dictar parte de la formación en M4 en adelante | **Sin cifra** | Baja la presión inicial, pero difiere el aprendizaje y pone en riesgo la meta de completitud ≥90% en M3 y la lectura de la prueba | Por costear y acordar |

**Aritmética de sensibilidad, no ahorro.** Cada hora que se le quite o agregue al
básico por persona mueve 60-70 h, o 0,6-2,45k USD (60 × 10 y 70 × 35 USD/h). Cada
hora del intermedio por persona de la cohorte mueve 15-20 h, o 0,15-0,7k USD.
Nada de eso se resta: no se asume ahorro, y el piso de contenidos del básico
(clasificación de datos, superficies y herramientas permitidas por cliente,
revisión del resultado, consulta e incidente) no baja.

**Qué hay que recostear en cada alternativa:** preparación y facilitación (8-16 h +
8-16 h), soporte de Talento (8-16 h), evaluación práctica, soporte de pares y los
solapes B/C/D, con la base congelada antes de formar y probar. Si la base se
amplía, semanas 9-13 son cinco semanas.

- **Recomendación:** mantener A hasta que B o C tengan costo y calendario
  comparables; no cambiar el alcance por una intuición de ahorro.
- **Dependencias:** Finanzas costea; el responsable humano de D y Operaciones confirman población y
  agendas; el equipo acuerda la opción (#13) y la propaga a B, C, E, F y a quien
  integra las slides.
- **Riesgo:** elegir B o C sin costo diferiría el aprendizaje sin bajar el
  desplazamiento de horas facturables.
- **Responsable humano:** el responsable humano de D, con el equipo; el acuerdo se registra en #13.
- **Criterio de éxito:** una comparación con horas, costo, evaluación y calendario
  equivalentes entre las tres, y una opción registrada en #13.
- **Condición de abandono:** si no hay agenda, perfil o evaluador disponible para
  una alternativa, no se inicia esa actividad; se reduce, se resecuencia o se vuelve a
  costear antes de comprometerla.

**Evaluación práctica del básico (propuesta cualitativa, sin validar).** Hoy no
hay instrumento, evaluador ni reparto de las 6 h definidos. Propuesta de este
anexo: cada persona resuelve **un caso permitido para su rol** (con datos
sintéticos o autorizados) y deja **evidencia de la revisión de su resultado**; lo
evalúa la facilitación técnica ya publicada (16-32 h clave) y lo registra
Talento (8-16 h distribuidas). No se crean fracciones de horas nuevas ni se
asume aprobación. Si no entra en la facilitación ni en las 6 h, se recostea con
Finanzas **antes de iniciar** el básico; sin ella, la completitud queda como
asistencia y no como uso. **Confirmación humana pendiente:** el responsable
humano de D y Operaciones confirman instrumento, evaluador y encaje en las horas.

**Éxito.** Básico completado ≥90% al cierre M3 con evaluación práctica por rol;
diccionario de actividad congelado y cobertura publicada; todas las horas
conciliadas sin doble asignación. Responsable: a designar.

**Abandono o revisión.** Sin permisos, horas o facilitación, no iniciar la
actividad afectada. Si el calendario no sostiene ≥90%, reducir o resecuenciar
y volver a costear con una decisión explícita; no dar la meta por lograda por asistir.

## Insumos para Finanzas

**Referencia del programa completo.** Las tablas anuales siguientes describen
ese alcance, no el pedido inicial vigente ni una autorización de contratación.
El insumo del mínimo está en la sección previa y su consolidación está en E.

Costo de horas = horas x 10-35 USD/h (supuesto). Es valuación a costo
cargado, no ingreso perdido ni caja incremental. Finanzas estima aparte el trabajo,
ingreso y contribución efectivamente desplazados con la matriz de capacidad;
la tarifa sola no representa ese costo de oportunidad. Evitá sumar dos veces
costo cargado y contribución perdida de las mismas horas. Faltan agendas y
contribución por trabajo ([fuentes faltantes](../../material/huecos.md)).

| Concepto | Tramo | Horas | Rango, k USD | Fuente o supuesto |
|---|---|---|---|---|
| Nivel básico, ~65 personas x 6 h | Meses 1-3 | ~390 | 3,9 - 13,65 | Supuesto |
| Nivel intermedio, ~50 personas x 12 h | Meses 1-9 | ~600 | 6,0 - 21,0 | Supuesto |
| Nivel avanzado, ~10 personas x 480 h x 10-15% (convención de costeo) | Meses 4-6 | 480 - 720 | 4,8 - 25,2 | 10-15% de [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md); resto, supuesto |
| Champions, 8 personas x 10% x 9 meses | Meses 4-12 | ~1.150 | 11,5 - 40,25 | 10% de [programa](../../material/conceptos/m3u2-programa-champions.md); resto, supuesto |
| Prueba chica de los meses 1-3: 2 champions de Tecnología al 10% durante 2 meses | Meses 1-3 | 64 | 1,2 - 3,0 | 2 x 10% x 2 x 160 h; el costo no usa 10-35 USD/h (daría 0,64-2,24) sino la tarifa por rol que fija el Anexo E ("Prueba chica de los meses 1-3 (primeros 100 días)": 0,4 persona-mes a 3,0-7,5k USD, equivale a unos 19-47 USD/h). El diseño (40-80 h de tech lead) y la lectura (16-24 h de DevOps/QA) los costea el Anexo E como tiempo clave, no entran acá |
| **Subtotal horas de capacitación** | Meses 1-12 | **~2.684 - 2.924** | **~27,4 - 103,1** | Suma |
| Líder del programa, 20% de una persona, 12 meses | Meses 1-12 | **384 (sobre clave)** | 10,8 - 24,0 | 20% x 12 x 160 h; costo: 20% x 12 x 4.500-10.000 USD por mes ([tech lead](../../context/supuestos/costo-cargado-por-rol.md)). Reasignar no elimina las horas; no integra el subtotal de capacitación |
| Contractor de IA aplicada, 9 meses, 100%, **solo si la decisión del mes 3 encuentra una señal** | Meses 4-12 | n/a | 40,5 - 99,0 | 9 x 4.500-11.000 USD por mes ([costo por rol](../../context/supuestos/costo-cargado-por-rol.md)). Sin señal el renglón sale y queda el cierre que costea el Anexo E (~4k USD en el medio). Reemplaza la fracción de 0,8 FTE de IA aplicada del Anexo B: no se suma con ella |
| Contractor de IA aplicada en los meses 1-3, 50% (contractor desde el mes 1) | Meses 1-3 | n/a | 6,75 - 16,5 | 0,5 x 3 meses x 4.500-11.000 USD por mes. Reemplaza el 0,3 FTE de IA aplicada de los meses 1-3 del Anexo B (contractor que reemplaza); el 0,2 restante es incorporación y documentación. **Pasa a caja un costo que el Anexo B tenía como tiempo.** Alternativa a decidir con Finanzas: contratar al 30% en los meses 1-3 (−2,7 a −6,6k USD de caja: 0,2 x 3 x 4.500-11.000 USD por mes), si el contrato lo admite |
| Preparación previa: reconstrucción retrospectiva y diseño de encuesta | Preparación previa | 60 - 100 | 1,7 - 6,3 | Supuesto: 1,5 a 2,5 semanas del perfil técnico que lidera el programa, a 28-63 USD/h (4.500-10.000 USD mensuales de tech lead sobre 160 h) |
| Certificación o curso externo del nivel avanzado | Meses 4-6 | n/a | **Sin estimar** | Falta cotización; no se inventa |
| Instrumentación de medición de uso en chat y Gemini | Meses 1-3 | n/a | Incluida en DevOps/QA del [Anexo B](02-arquitectura.md) (1,4-7,1k USD de tiempo); no suma | Costeada por Arquitectura, sin cotización de proveedores |
| Reconocimiento de champions | Meses 4-12 | n/a | 0 (no monetario) | Supuesto; si es monetario, Finanzas lo ajusta |
| **Total identificado** | Preparación previa y meses 1-12 | | **~87,2 - 248,9** | Suma de los renglones con costo, incluido el contractor desde el mes 1 y el contractor de los meses 4-12. Sin señal en la decisión del mes 3 (sin el renglón de los meses 4-12): ~46,7 - 149,9, más el cierre del Anexo E. Sin el contractor de los meses 1-3: ~80,4 - 232,4. No descuenta el solape con el Anexo B |

Escala: las ~2.684-2.924 horas son unas 41-45 horas por persona de la dotación
([tamaño y estructura](../../context/hechos/tamano-y-estructura.md)), cerca del
2% a 2,5% de una jornada anual. La revisión mensual del Council no suma costo
a este anexo: el uso semanal por área ya está en la medición de las filas
anteriores.

**Cómo entra en el Anexo E.** Para el mínimo, la referencia vigente de soporte,
participantes y preparación es [E, «Pedido inicial: paquete mínimo»](05-business-case.md#pedido-inicial-paquete-mínimo),
incluida la corrección del solape de Seguridad B/C que concilie Finanzas.
Las partidas de Personas se detallan en «Insumo para el paquete mínimo» y no se
suman al consolidado sin descontar solapes y preparación.

Los pisos **1,6/~1,8 FTE clave** y las **590/654 h distribuidas** pertenecen
al programa completo y **no se confirman hoy**. Sus 64 h de prueba y el líder
al 20% tampoco se trasladan automáticamente al mínimo.

**Horas y costo del avanzado, conciliados con el Anexo E.** El rango es 480-720 h;
para capacidad se usa su punto medio, 600 h. El costo es 4,8-25,2k USD y su
medio es 15k USD, como ya recoge E en "Conciliación de los meses 4-6"; no es
600 h × 22,5 USD/h (13,5k USD). Son dos convenciones de resumen explícitas, no
una corrección pendiente ni un costo adicional. Las 480 h por persona-tramo son
la base del cálculo de jornada, distintas del piso de horas totales del avanzado.
No se publica una base de horas totales de la empresa. Si el costo total entra
dentro del 1% a 3% de la facturación que se asume como capacidad de inversión
([supuesto](../../context/supuestos/capacidad-de-inversion.md)) lo calcula
Finanzas: la facturación en USD no se publica.

## Insumos para el deck

- **Decisión que se le pide al board:** «Formar, reasignar y decidir una excepción
  externa». El pedido inicial es el paquete mínimo sin plataforma central,
  consolidado en E; la excepción externa se decide solo si falta
  perfil/capacidad demostrados. El programa publicado sirve como referencia de
  alcance y no transfiere automáticamente contractor, prueba ni techos al mínimo.
- **Frase central:** en el piloto de abril (12 personas que se anotaron solas) el
  uso fue frecuente (92%, NPS +42) y la capacitación falló (solo 2 de 12, 17%,
  completó los cursos): el primer freno fue el tiempo.
  El plan responde con casos por rol, horas dentro de la jornada y champions con
  tiempo asignado, y mide en los meses 1-3 si pasa lo mismo en toda la organización.
- **Redacción sugerida para la slide 7:** «En el piloto
  de abril (n=12, autoseleccionado) el uso fue frecuente (92% a tres o más días
  por semana, NPS +42) y solo 17% (2 de 12) completó los cursos». Propuesta a
  quien integra las slides: reemplazar «los 12 usaron la herramienta y la
  valoraron», porque la fuente registra 8% de detractores. La slide ya publica esa señal; conservar la cautela: no representa
  a toda la organización, cuya base se mide en M1-M3.
- **Cifra para el CFO:** ~2.684-2.924 horas de capacitación, ~41-45 horas por
  persona, a 27,4-103,1k USD al costo cargado; además hay 384 h del líder en el
  sobre clave. Finanzas concilia ingreso y contribución desplazados sin duplicar
  esas horas. Total de personas del programa publicado ~87,2-248,9k USD
  (con contractor desde el mes 1 y al 100% en los meses 4-12; ~46,7-149,9k USD sin
  señal). No es el presupuesto del nuevo paquete mínimo.
- **Señal de alerta para la slide 7:** Tecnología ≥80% en M6 y ≥85% en M12;
  Operaciones habilitadas ≥60% en M12 (≥40% en M6, meta intermedia).
  Cumplir exactamente 85%/60% en M12 con igual peso y toda Operaciones habilitada
  da 72,5%, no cumplimiento del OKR 80%.
  Conservar metas por área y publicar combinado original, habilitados/total y
  cobertura; las prohibiciones condicionan el uso y deben medirse.
- **Transición responsable (una línea para la slide 7):** «Formar y reasignar
  antes que desvincular: estudio de un rol crítico (alcance ampliado, no incluido en el mínimo), compromiso sobre el empleo
  y chequeo de equidad por grupo». Sin compensación monetaria nueva en 12 meses.
- **Qué se mide:** uso real semanal por área, no seats, que alimenta el tablero
  mensual del Council; condiciones de abandono a los meses 6 y 9 explícitas.

## Cautelas

- Las poblaciones, las horas por nivel y la red de champions son **supuestos**
  ([poblaciones de capacitación](../../context/supuestos/poblaciones-de-capacitacion.md)),
  todavía sin validar contra fuentes internas; se validan antes de comprometer
  presupuesto. Los umbrales de adopción de cada tramo tampoco tienen respaldo
  documental: se validan con la línea de base.
- Las cifras de adopción son estimaciones todavía sin validar contra fuentes
  internas; varias son rangos o proporciones aproximadas, y la telemetría solo
  mide el agente de código.
- n=12 en el piloto, autoseleccionado: no representa a la organización ni prueba
  que el formato cause mejor capacitación.
- El antes y después del proceso de delivery es un diseño propuesto sobre un
  proceso típico supuesto; falta validarlo con un delivery manager.
- La postura sobre el empleo es una propuesta; falta la decisión del Directorio y
  la revisión laboral.
- La holgura de 0,2 FTE del contractor en los meses 4-6 es un supuesto de Personas
  sin dato del contractor; el replan de los meses 4-6 depende de ella y no se da
  por confirmado (ver "Holgura de 0,2 FTE del contractor en los meses 4-6 (replan
  del Anexo B)"). La documentación mínima reproducible se imputa por entregable
  a la fracción que lo produce (0,8 o 0,2); los supuestos de umbrales técnicos todavía dicen
  que este anexo la cargaba entera al 0,8, y quien los verificó tiene que actualizar esa cautela.
- La matriz privada de capacidad no existe: las columnas «tipo de hora», «cliente
  o contrato» y la separación de horas clave y distribuidas son una propuesta de
  Personas (agente) que falta confirmar. Las 16-24 h de padrón y matriz son una
  estimación de Finanzas (agente), sin estimación humana de Personas.
- La comparación de alternativas de formación no tiene cifra para el núcleo con
  profundización ni para la secuenciación; solo la alternativa vigente está
  costeada. Los porcentajes de peso de la formación son cálculo de este anexo.
- El posible doble conteo de managers (8-16 h de M1-M3 frente a la validación
  inicial) sigue sin resolver; las horas no se descontaron.
- Reserva propuesta, demanda costeada, disponibilidad real y decisiones futuras
  son cosas distintas; ninguna agenda está liberada ni ninguna decisión aprobada.
- Responsable de cada acción: **a designar**.
- El curso describe el estudio de un rol a 18 meses; el plan lo adapta a 12 y es
  decisión propia. Las habilidades AI-ready y los modelos de compensación son
  marcos sin niveles ni cifras; su uso acá es criterio y discusión.
- No se usaron cifras sin fuente primaria (60% menos de resistencia; 70% más de
  retención con reskilling).

[^okr]: [OKR y objetivos](../../context/hechos/okrs-y-objetivos.md), borrador de OKR de Tecnología 2027, objetivo de eficiencia operativa con IA.
[^estructura]: [Tamaño y estructura](../../context/hechos/tamano-y-estructura.md), sección "Dependencia de personas clave".
