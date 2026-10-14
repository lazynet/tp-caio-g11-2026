---
owner: people
status: draft
title: "Anexo D — Personas, cambio y roadmap cultural"
---

# Anexo D — Personas, cambio y roadmap cultural

Slide que sustenta: [Slide 6 — Personas y cultura](../slides.md).

Convención de tiempo: **T1 a T4** son los cuatro trimestres del plan. Se asume
que T1 arranca con la aprobación del presupuesto 2027 (supuesto del equipo) y
que el cuarto trimestre de 2026 es la línea de base (T0), coherente con el
borrador de OKR de Tecnología 2027.[^okr]

## Objetivo

Sustentar la decisión de personas que se le pide al board: **capacitar y
reasignar en lugar de contratar**, con un programa de AI literacy por nivel y por
rol, una red de champions con tiempo asignado y un solo perfil especializado a
prueba, medido por **uso real semanal** y no por seats comprados. Este anexo
desarrolla roles y capacidad dentro de los derechos de decisión que defina
`governance`; no los redefine.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Dotación | 60 a 70 personas, nómina y contractors; ~40% Operaciones (staffing en equipos de clientes), ~40% Tecnología, el resto staff | [Tamaño y estructura](../../context/hechos/tamano-y-estructura.md) |
| Utilización facturable | 83-90%, bench menor a 1 FTE: la capacitación compite con horas facturables | [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md) |
| Restricción de contratación | No contratar gente nueva y potenciar al equipo con IA; sin contrataciones masivas | [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md), [Capacidad de inversión](../../context/supuestos/capacidad-de-inversion.md) |
| Tiempo de capacitación aceptado por la propia empresa | 10% a 15% del tiempo semanal durante una certificación | [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md) |
| Clientes financieros | Por defecto prohíben modelos externos sobre su código y datos; la matriz de restricciones por cliente no existe todavía | [Apetito de riesgo](../../context/supuestos/apetito-de-riesgo-de-clientes.md), [Gobierno y política](../../context/hechos/gobierno-y-politica-ia.md) |
| Costo cargado por rol | Rangos de mercado en USD por mes, amplios y no calibrados contra la nómina (staff 1.500-5.000; desarrollador semisenior 2.000-5.000; analista 2.000-5.500; tech lead 4.500-10.000; especialista IA 4.500-11.000) | [Costo cargado por rol](../../context/supuestos/costo-cargado-por-rol.md) |
| Jornada | 160 h por mes, 1.920 h por año por persona | Supuesto del equipo (convención de cálculo) |
| Costo horario de capacitación | USD 10 a 35 por hora (1.500 a 5.500 mensuales sobre 160 h, el tramo de staff, desarrolladores semisenior y analistas) | Supuesto del equipo, derivado de [Costo cargado por rol](../../context/supuestos/costo-cargado-por-rol.md). **Es costo, no tarifa facturable** |
| Ganancia de productividad | 10% a 25% de throughput por desarrollador a 12 meses, solo en equipos propios; en staffing no se cuenta | [Ganancia de productividad](../../context/supuestos/ganancia-de-productividad.md) |
| Alcance del art. 4 del AI Act sobre Acme Labs | Sin decidir (art. 2.1.c); se adopta como piso igual | [Huecos](../../material/huecos.md), [art. 4](../../material/frameworks/eu-ai-act-proveedor-desplegador.md) |

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
peso parecido, la base de hoy es ~4 de cada 10 (promedio de ~7 y ~1 de cada 10,
cálculo de este anexo). Y si Tecnología llegara a 85%, Operaciones tendría que
llegar a ~75% para cumplir la meta combinada. Eso no es alcanzable si los clientes
prohíben las herramientas, y las metas propias de este anexo tampoco llegan a 80%
combinado (ver "Meta de adopción y OKR combinado"). Ver desacuerdo D1.

### Calidad de uso y capacitación

| Métrica (piloto de abril, n=12, autoseleccionado) | Resultado | Fuente |
|---|---|---|
| Completaron los tres cursos obligatorios | 17% | [Encuesta y pilotos](../../context/hechos/encuesta-y-pilotos-ia.md) |
| No hicieron ningún curso | 50% | idem |
| Primer freno: falta de tiempo para capacitarse | dos de cada tres | idem |
| Piden casos prácticos por rol en lugar de cursos genéricos | más de la mitad | idem |
| Usan *few-shot* (ejemplos del resultado esperado) | 5% o menos | idem |
| Uso frecuente (3+ días por semana) | 92% | idem |

En el piloto, **los 12 participantes usaron y valoraron la herramienta** (NPS +42)
y **la capacitación falló**. Es una señal de ese grupo, no una prueba sobre toda
la organización: n=12, autoseleccionado, sin grupo de comparación, así que el
piloto tampoco demuestra que el formato de casos por rol cause una mejor
capacitación. Esa hipótesis la prueba el plan midiendo, no la da por cierta. El
análisis de prompts cubre solo el chat. Este anexo **no extiende** la valoración
del piloto a "la gente": cuando habla de la organización, usa la telemetría y la
encuesta de la línea base de T1.

### Qué respalda el diseño (cursada)

- Literacy en tres niveles de profundidad y tres roles; el curso no los cruza,
  el cruce es decisión de este plan: [niveles](../../material/conceptos/m3u2-ai-literacy-niveles.md).
- Champions: perfil, cuatro fases y 10% de la jornada como ejemplo de tiempo
  asignado; sin sponsor ni entregable concreto se vuelven *status meetings*:
  [programa](../../material/conceptos/m3u2-programa-champions.md),
  [champions y literacy](../../material/conceptos/m1u4-champions-y-literacy.md).
- Frenos (miedo al reemplazo, tecnoestrés, desconfianza) y estrategias de
  transición: [frenos y transición](../../material/conceptos/m3u2-frenos-y-transicion.md).
  La cifra "hasta 60% menos de resistencia" **no se usa**: no tiene fuente
  primaria ([huecos](../../material/huecos.md)).
- Tres modos de la IA (automatización, aumentación, supervisión):
  [tres modos](../../material/conceptos/m2u3-tres-modos-ia.md).
- ADKAR, Kotter y Lean Change no están en el material: no se usan.

## Roles y capacidad

Principio: **cada rol se cubre primero reasignando o capacitando**. Se contrata o
se terceriza solo donde hay un riesgo de continuidad que la capacitación no
cierra a tiempo. La ficha de estructura marca que arquitectura, seguridad y
gobierno están concentradas en pocas personas y pide tratarlo como riesgo de
continuidad.[^estructura]

| Rol de IA | Quién lo cubre | Vía | Tiempo (supuesto del equipo) | Qué cambia |
|---|---|---|---|---|
| Lidera el programa de adopción (oficina del CAIO) | Un perfil técnico interno | Reasignar | 20% de una persona, 12 meses | Opera literacy, champions y métricas; no decide políticas |
| Especialista en IA aplicada (evals, harness, gobierno técnico) | Un perfil externo a prueba | **Tercerizar (contractor)**; alternativas en D2 y "Cobertura de IA aplicada" | 0,5 persona en T1; 1 persona de T2 a T4 | Absorbe la concentración de capacidades críticas; documenta y transfiere |
| Champions | Personas de Tecnología, Operaciones y staff | Reasignar | 10% de la jornada, T2 a T4 | Casos prácticos por rol, soporte entre pares, feedback |
| Desarrolladores | Equipo actual | Capacitar | Nivel intermedio y avanzado | Pasan de escribir a **supervisar y revisar** agentes; el humano sigue siendo responsable final ([política](../../context/hechos/gobierno-y-politica-ia.md)) |
| QA y automatización | Equipo actual | Capacitar | Nivel avanzado | Pasan a diseñar evals y compuertas de calidad |
| Analistas funcionales | Equipo actual | Capacitar | Nivel intermedio | Especifican casos de uso y definen "correcto" |
| Delivery manager y personas en staffing | Operaciones | Capacitar | Nivel básico e intermedio | Gestionan qué herramientas permite cada cliente y llevan a la matriz las consultas de uso |
| Dueño de la política, sponsor, administrador de licencias | Ya existen en Tecnología | Sin cambio | Sin cambio | Los define y sostiene `governance`; este anexo los toma como dados |

RACI de personas (roles, no personas; una sola A por decisión,
[RACI](../../material/conceptos/m1u4-raci-ownership.md)):

| Decisión | A | R | C | I |
|---|---|---|---|---|
| Plan de literacy y calendario | CAIO | Líder del programa | Managers de área, Finanzas | Toda la organización |
| Selección y tiempo de champions | Manager de cada champion | Líder del programa | CAIO | Champions |
| Métricas de adopción | CAIO | Líder del programa | Tecnología, Talento | Directorio |
| Contratación o contractor de IA aplicada | Directorio | CAIO | Finanzas, Talento | Managers |
| Herramientas permitidas por cliente | Área comercial | Delivery manager | Gobierno y seguridad, CAIO | Operaciones |

Responsable humano de cada fila: **pendiente**.

### Antes y después de un proceso: del requerimiento al cambio en producción

Aplicación del [grafo humano-agente](../../material/conceptos/m2u3-grafo-humano-agente.md)
a un proceso de delivery de **equipos propios** (no de staffing, donde el cliente
fija las herramientas). Es un **diseño propuesto**: `context/` no documenta el
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
| 6. Liberar y operar | DevOps y el equipo | Igual, con registro de qué parte tuvo asistencia de agente | Tech lead autoriza la liberación; incidentes los trata el equipo, con `governance` |

**Handoffs que cambian:** el analista entrega criterios verificables por una
compuerta (antes, texto para leer); el desarrollador entrega código con las
pruebas que lo respaldan; QA entrega la compuerta y no solo el resultado. Donde
el contrato del cliente prohíbe las herramientas, el flujo vuelve al "antes" en
esos nodos y el plan no lo fuerza (ver "Staffing").

**Qué se mide antes y después:** tiempo de ciclo del requerimiento a producción,
retrabajo (cambios reabiertos) e incidentes, **contra la base prospectiva
congelada** de T1, por área y agregado. No se atribuye mejora antes de T2.

### Cobertura de IA aplicada, por trimestre

El [Anexo B](02-arquitectura.md) necesita 0,5 FTE de IA aplicada en T1 y 0,8 de
T2 a T4 dentro de su esfuerzo técnico. Este anexo, en su versión anterior, solo
disponía el perfil externo desde T2: T1 quedaba sin cobertura. Además, desde
T2 el esfuerzo técnico de B y el contractor de D se leían como dos recursos.
`context/` no registra ningún perfil interno de IA aplicada con tiempo libre
(la capacidad es de pocas personas y el bench es menor a 1 FTE), así que **no se
asume que exista**.

| Trimestre | Necesidad (Anexo B) | Vía propuesta | Alternativa | Qué lo demuestra |
|---|---|---|---|---|
| T1 | 0,5 FTE | Contractor al 50%, aprobado en G0 | Perfil interno reasignado, solo si antes de G0 se demuestra por rol: porcentaje liberado, trabajo desplazado y quién lo cubre | Contrato corto firmado, o declaración de capacidad por rol validada por Operaciones |
| T2 a T4 | 0,8 FTE | El mismo contractor, 1 persona | Idem | Entregable verificable por trimestre; documentación y traspaso |

**Reemplaza, no complementa.** El contractor es la fuente del 0,5 de T1 y del 0,8
de T2 a T4 de B; el 0,2 restante es documentación, traspaso y coordinación con el
programa. Contar la fracción de B y el contractor a la vez duplica el costo
(solape que Finanzas marca como "IA aplicada"). Recosteo de cada alternativa:

| Alternativa | Caja (USD) | Tiempo interno | Riesgo |
|---|---|---|---|
| A. Solo perfil interno | 0 | 0,5 FTE en T1 y 0,8 de T2 a T4 sacados de horas facturables | Sin perfil demostrado, T1 no arranca; concentración de capacidades críticas sin mitigar |
| B1. Contractor desde T1 (recomendada) | T1: 6.750-16.500 (0,5 x 3 meses x 4.500-11.000); T2-T4: 40.500-99.000 | Se libera el tiempo de B que cubre | Sube la caja de T1 contra el techo de G0 y choca con "no contratar" (decide el Directorio) |
| B2. Contractor desde T2 (versión anterior) | T2-T4: 40.500-99.000 | T1 queda sin cubrir: el hito de B se corre o se resiente | Atrasa el gateway de laboratorio y las evals de T1 |

El total de B1 es una decisión de G0, no de G1. Si el Directorio la rechaza, la
alternativa es A con la prueba de capacidad previa a G0, o diferir los hitos de
IA aplicada de T1 (lo que decide `architect`).

## AI literacy por nivel y por rol

Cruce de los dos ejes del curso (decisión de este plan). Horas por persona y
población son supuestos del equipo; el nivel básico es el piso para todos.

| Nivel | Población (aprox.) | Contenido | Formato | Horas por persona | Horas totales |
|---|---|---|---|---|---|
| Básico | Toda la organización, ~65 | Uso seguro, clasificación de datos, qué se puede enviar, verificar el output, reportar incidentes | Sesiones breves y guía de una página; **casos de su rol** | 6 | ~390 |
| Intermedio | Operaciones y Tecnología usuarias frecuentes, ~50 | Pedir bien (ejemplos, contraargumentos), identificar casos de uso, supervisar | Talleres con casos reales del rol y práctica entre pares | 12 | ~600 |
| Avanzado | Especialistas que diseñan e implementan, ~10 | Agentes, evals, harness, gobernanza técnica | Proyecto aplicado con tiempo asignado | 10-15% del tiempo semanal durante un trimestre | 480-720 |
| Directivo | Primera línea y Directorio | Decidir inversión, riesgo, regulación y ROI | Briefings con casos | 3 | Dentro de la oficina del CAIO, sin costo aparte (supuesto) |

Cálculo del avanzado, con la convención de costeo del plan (480 h por
persona-trimestre, [convenciones](../../context/supuestos/convenciones-de-calculo.md)):
10 personas x 480 h x 10-15% = 480-720 h. Las 520 h de 13 semanas x 40 h son
calendario bruto y no se usan para costo. Poblaciones y horas coinciden con la
ficha [poblaciones de capacitación](../../context/supuestos/poblaciones-de-capacitacion.md)
y con el [Anexo E](05-business-case.md). Los niveles y los
roles salen de [AI literacy](../../material/conceptos/m3u2-ai-literacy-niveles.md);
los contenidos del básico y el intermedio responden a lo que el piloto mostró
faltante (uso seguro, ejemplos, verificación).

**Pedido de formato.** Más de la mitad del piloto pide casos prácticos por rol:
se arma ese formato con champions y se descarta el curso obligatorio genérico.
Cada módulo se agenda **dentro de la semana laboral**, con aviso al manager, para
corregir las fallas de comunicación que registró la encuesta.

**Art. 4 del AI Act.** Para el plan es un piso de people plan, que
la ficha de la cursada ya da como vigente. El texto original exige garantizar un
nivel suficiente de alfabetización; el texto tras el Omnibus pide "apoyar el
desarrollo" y no exige un nivel por individuo
([art. 4](../../material/frameworks/eu-ai-act-proveedor-desplegador.md)).
**Cautela:** si alcanza a Acme Labs y la versión vigente del art. 4 siguen sin
verificar contra EUR-Lex ([huecos](../../material/huecos.md)). El plan cumple el
espíritu de ambos textos (formación proporcional al rol, con registro de quién
completó qué), pero **no cita fechas ni sanciones en slides** hasta cerrar esa
verificación.

## Programa de champions

- **Tamaño:** 8 champions, una persona cada ~8 de la dotación (supuesto del
  equipo); al menos 2 de Operaciones y 2 de staff, porque la brecha está ahí.
- **Perfil:** curiosidad, comunicación y vocación de servicio; no necesariamente
  el más técnico ([programa](../../material/conceptos/m3u2-programa-champions.md)).
- **Contrato:** mandato explícito, sponsor y un entregable por trimestre (una
  guía de casos de su rol, un taller). El tiempo (10%) lo libera el manager y se
  agenda; si no se libera, el champion no se computa como activo.
- **Costo de no hacerlo bien:** los champions sin tiempo ni entregable se
  vuelven reuniones de estado ([champions y literacy](../../material/conceptos/m1u4-champions-y-literacy.md)).

## Gestión del cambio

| Freno | Evidencia en el caso | Quién pierde qué | Respuesta |
|---|---|---|---|
| Falta de tiempo | Dos de cada tres en el piloto; utilización 83-90% | Operaciones: cada hora de curso es una hora no facturada | Horas dentro de la jornada, módulos cortos, calendario por equipo; el costo está en Insumos para Finanzas |
| Prohibición del cliente | Supuesto de apetito de riesgo; matriz inexistente | Staffing: queda afuera de la ganancia | Ver "Staffing" abajo |
| Miedo al reemplazo | Freno de la cursada; no hay medición propia | Todos, y más en perfiles junior | Comunicación transparente y decisión D3 |
| Dependencia de un proveedor | El piloto lo advierte y propone consumo multimodelo | Equipos que ya construyeron hábitos | Fuera del alcance de este anexo; lo resuelve `architect` |
| Desconfianza en el output | Pocos piden contraargumentos o advierten alucinaciones | Quien revisa | Nivel intermedio centrado en verificar y supervisar |
| Incentivo contrario en staffing facturado por hora | Mencionado en las condiciones de invalidez de la ganancia de productividad | Personas y empresa: menos horas es menos facturación | Tensión con Finanzas, ver T1 |

**Staffing en equipos de clientes que prohíben herramientas externas.** El plan
no les pide usar lo que el contrato no permite. Tres frentes:

1. **Usos permitidos sin tocar el cliente:** propuestas, documentación
   propia, tickets y correo internos, con las herramientas corporativas y la
   clasificación de datos vigente.
2. **Literacy igual:** nivel básico e intermedio para todos, porque es
   formación de la persona y no depende del contrato.
3. **Matriz de clientes primero:** hasta que `governance` y el área comercial la
   completen, cada caso se valida a mano (pendiente declarado de la política).
   Las personas en staffing reportan consultas de uso de forma sencilla y sin
   sanción, igual que los incidentes.

**Dependencia de personas clave.** La capacidad en arquitectura, seguridad y
gobierno está en pocas personas: el contractor de D2 y la documentación
obligatoria de lo que arma el champion o el líder son la mitigación de
continuidad.

## Roadmap cultural trimestral y métricas

Línea de base (T0) = cuarto trimestre de 2026, anterior a la aprobación del
presupuesto 2027 (G0). Los umbrales son supuestos del equipo, a validar con la
línea de base. Toda métrica se reporta con numerador y
denominador y **por área, agregada**: ningún dato individual
([OKR](../../context/hechos/okrs-y-objetivos.md)). El alcance y la retención de
la telemetría los define `governance` con Talento (pendiente declarado).

| Trimestre | Hitos | Indicador adelantado (uso real) | Indicador rezagado |
|---|---|---|---|
| T0 (antes de G0) | Solo reconstrucción **retrospectiva** con datos que ya existen (telemetría y reportes de adopción de los últimos meses, series de incidentes y retrabajo si el repositorio las conserva) y diseño de la encuesta de chat y Gemini. Política: queda lista para ratificar, no ratificada | Serie retrospectiva de uso del agente de código por área | Serie retrospectiva de throughput, incidentes y retrabajo, con su hueco declarado si no existe |
| T1, semanas 1 a 4 | **Congelar la base prospectiva** antes de cualquier capacitación o herramienta nueva para usuarios: encuesta de chat y Gemini, uso semanal por área, throughput, incidentes y retrabajo de los equipos propios | Línea de base por área publicada y congelada al cierre de la semana 4 | Línea de base prospectiva de throughput, incidentes y retrabajo |
| T1, semanas 5 a 13 | Ratificación de la política y matriz de los cinco clientes principales (con `governance`); básico para todos; selección de champions; intermedio para Tecnología | Básico completado: ≥90% de la dotación al cierre del trimestre | Sin objetivo: se mide la línea de base |
| T2 | Intermedio para Operaciones y staff; arranca el avanzado; champions con tiempo asignado (el contractor ya está desde T1 si se aprueba B1) | Uso activo semanal de Tecnología ≥80% (la meta del OKR); Operaciones habilitadas ≥40% | Throughput de equipos propios: sin deterioro de calidad |
| T3 | Casos prácticos por rol publicados por champions; revisión de calidad de prompts | Tecnología ≥80% sostenido; prompts con ejemplos del resultado esperado: de ≤5% a ≥30% (muestra agregada) | Incidentes y retrabajo sin aumento sobre la base |
| T4 | Traspaso del contractor a la oficina del CAIO; evaluación de lo que escala | Tecnología ≥85%; Operaciones habilitadas ≥60%; staff ≥50% | Throughput entre +10% y +25% en equipos propios ([supuesto](../../context/supuestos/ganancia-de-productividad.md)) |

"Habilitadas" = personas cuyos clientes y herramientas lo permiten según la
matriz, como denominador. Se informa también el valor sobre el total, para no
esconder la brecha.

**Calendario único de T0 y T1 (H12).** Una sola secuencia reemplaza las tres
versiones anteriores (D en T0, B/C/F en T1):

| Cuándo | Qué existe | Quién lo verifica | Costo |
|---|---|---|---|
| Antes de G0 (T0) | Serie retrospectiva de uso, incidentes y retrabajo; diseño de la encuesta; política lista para ratificar | Responsable humano pendiente; el Directorio ve el resultado en G0 | 60-100 h del perfil técnico que lidera el programa (Insumos para Finanzas) |
| T1, semanas 1 a 4 | Base prospectiva congelada | Oficina del CAIO, con `finance` para throughput | Dentro del 20% del líder del programa |
| T1, semanas 5 a 13 | Política ratificada, matriz de cinco clientes, básico e intermedio de Tecnología | `governance` y área comercial | Horas de capacitación (Insumos para Finanzas) |

Retrospectiva y prospectiva no se mezclan: la serie retrospectiva sirve para
entender la tendencia previa y el ruido; **la ganancia se atribuye solo contra la
base prospectiva congelada**, y no se computa antes de T2 (la rampa de E ya
asume 0% en T1). Capacitación e intermedio para Tecnología empiezan en la semana
5 justamente para que formación y herramientas nuevas no contaminen esa base.
Esto comprime el básico a nueve semanas: sigue siendo viable para el 90% al cierre
de T1, pero lo valida la oficina del CAIO en la semana 5.

**Meta de adopción y OKR combinado (H14).** El borrador de OKR pide 80% en
Operaciones y Tecnología juntas. Con áreas de igual peso, las metas de este anexo
no lo alcanzan, ni siquiera en el mejor caso:

| Operaciones habilitada (% de Operaciones) | Operaciones habilitadas 60% da, sobre Operaciones total | Combinado con Tecnología 85% (igual peso) |
|---|---|---|
| 25% | 15% | 50% |
| 50% | 30% | 57,5% |
| 100% (toda Operaciones habilitada) | 60% | 72,5% |

Para llegar a 80% combinado con Tecnología 85%, Operaciones debería llegar a 75% sobre
su total. Por eso: **no se presenta ninguna meta propia como cumplimiento del 80%**.
Se publican siempre las dos métricas, cada una con numerador y denominador:
(a) uso semanal activo de Tecnología y (b) uso semanal de Operaciones habilitadas, con
el valor sobre el total de Operaciones al lado. Si el Directorio mantiene el OKR
combinado, se informa su resultado real, que será menor al 80%. Metas por trimestre
unificadas para todo el plan (incluido el Anexo F): Tecnología ≥80% desde T2 (cifra del
OKR) y ≥85% al cierre de T4 (meta interna de este anexo); la diferencia 80/85 no es una
contradicción, sino meta del OKR y meta de cierre.

**Criterios de éxito (al cierre de T4):** Tecnología ≥85% de uso semanal activo;
Operaciones habilitadas ≥60%; nivel básico ≥90%; ningún aumento de incidentes
ni retrabajo en equipos propios; capacidades críticas con un reemplazo
documentado.

**Condiciones de abandono o cambio de rumbo:**

| Disparador | Acción |
|---|---|
| Al cierre de T2, uso activo en Tecnología <60% pese a tiempo asignado | Frenar la expansión de seats y rediseñar la formación con casos por rol; revisar causas con los managers |
| Básico completado <50% al cierre de T2 | Cambiar el formato (de sesión a práctica en equipo) y reasignar tiempo; no repetir el mismo curso |
| Asistencia de champions <60% dos meses seguidos | Disolver la red o rediseñar su mandato con sponsor nuevo |
| Subida de incidentes o retrabajo asociada a uso de IA | Pausar el nivel avanzado hasta revisar compuertas de calidad con `architect` |
| Contractor de IA sin entregable verificable al cierre de T3 | No renovar; traspasar a la oficina del CAIO |

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| La capacitación desplaza horas facturables y baja utilización | Alta (utilización 83-90%, sin bench) | Medio | Horas topeadas por trimestre (ver Insumos para Finanzas); módulos cortos; calendario por equipo | Utilización <80% (meta interna) atribuible al programa |
| Operaciones no puede adoptar por contrato del cliente | Alta | Medio | Matriz de clientes; meta sobre habilitadas; usos permitidos | Matriz sin completar al cierre de T1 |
| Champions sin tiempo ni entregable | Media | Medio | Mandato, sponsor y entregable trimestral | Ver tabla de abandono |
| Pérdida de una persona clave en arquitectura, seguridad o gobierno | Media | Alto | Contractor a prueba, documentación, transferencia | No hay reemplazo documentado al cierre de T3 |
| Adopción declarada ≠ uso real (seats comprados, uso detectado) | Media | Medio | Medir uso real semanal por área, no seats | Métrica de seats sin correlato en uso |
| Telemetría solo cubre el agente de código | Alta | Medio | Medir chat y Gemini por encuesta o telemetría ampliada, con `architect` y `governance` | Sin medición de staff al cierre de T1 |
| Miedo al reemplazo reduce la adopción y la franqueza | Media | Medio | Comunicación transparente, D3 | Caída de uso tras un anuncio o un cambio de estructura |
| El consumo real a precio de API (~12x lo pagado) sube el costo si cambia el esquema de precios | Media | Alto (no es de personas) | Lo trata `finance`; este anexo solo informa que más uso empuja ese costo | Ver anexo de Finanzas |

## Decisiones

| # | Decisión | Alternativas | Elección | Reversibilidad |
|---|---|---|---|---|
| D1 | Cómo medir la meta de adopción en Operaciones | A: 80% sobre Operaciones y Tecnología, como el borrador de OKR. B: 80% en Tecnología y una meta propia sobre personas **habilitadas** en Operaciones. | **B**, informando también A | Reversible: se cambia al completar la matriz |
| D2 | Capacidad especializada en IA aplicada | A: sin incorporación, solo reasignar. B1: un contractor a prueba desde T1 (50% en T1, 100% de T2 a T4), que reemplaza la fracción de IA aplicada de B. B2: lo mismo desde T2. C: dos contrataciones en nómina. | **B1**: única forma de cubrir la concentración de capacidades sin romper la restricción de no contratar de forma masiva. **Choca con la restricción literal de "no contratar gente nueva"**: lo decide el Directorio. A es viable si ese techo se mantiene, con más riesgo de continuidad | B reversible (contrato corto); C poco reversible |
| D3 | Qué se dice sobre el empleo | A: sin compromiso. B: compromiso explícito de que la ganancia por IA no se usa para desvincular durante los 12 meses. C: compromiso con excepciones. | **Postura propuesta: C**, con el texto de "Postura sobre el empleo (propuesta)". La decide el Directorio, con asesoría laboral; no es una política aprobada. B baja más el miedo pero ata margen; A deja el freno sin respuesta | B y C poco reversibles una vez comunicados |
| D4 | Formato de la formación | A: curso obligatorio genérico. B: casos prácticos por rol con champions, en horario laboral. | **B**, por el pedido del piloto (más de la mitad de 12 autoseleccionados) y porque la falta de tiempo fue el primer freno; el efecto del formato se mide en T2-T3 | Reversible |
| D5 | Art. 4 del AI Act | A: esperar a decidir si alcanza a Acme Labs. B: adoptarlo como piso, con registro. | **B**, sin citar fechas ni sanciones | Reversible |

### Postura sobre el empleo (propuesta) y métricas de comportamiento

**Propuesta, no política aprobada.** Texto sugerido para el Directorio, a revisar
con asesoría laboral antes de comunicarlo: «Durante los 12 meses del plan, la
ganancia de productividad por IA no se usa para desvincular a una persona.
Primero se reasigna y se capacita. Quedan afuera, y se dicen de antemano, las
causales que ya existían sin relación con la IA (desempeño sostenido, causa
justa, pérdida de un cliente).» Es la opción C de D3. Alternativas: B, sin
excepciones (más tranquilizadora, ata más el margen); A, sin compromiso (no
responde el miedo al reemplazo, que la cursada marca como freno). **Costo y
riesgo:** el costo es de margen y lo cuantifica `finance`; no está en este anexo.
Riesgo: una promesa que no se cumple destruye la confianza que se busca; por eso
se comunica solo después de la decisión del Directorio.

**Métricas de comportamiento** (qué hace la gente, no qué declara). Todas por
área, agregadas, con numerador y denominador y sin dato individual. Línea de base
en T1; las que no tienen fuente hoy son supuestos del equipo:

| Comportamiento observable | Cómo se observa | Qué señala | Fuente |
|---|---|---|---|
| Pedidos con ejemplos del resultado esperado | Muestra agregada de prompts del chat | Calidad de uso (hoy ≤5%, meta ≥30% en T3) | [Encuesta y pilotos](../../context/hechos/encuesta-y-pilotos-ia.md) |
| Cambios con asistencia de agente que pasan la compuerta de pruebas y revisión de un humano distinto del autor | Registro del repositorio y de la compuerta | Supervisión real, no aprobación de trámite | Supuesto; depende de `architect` |
| Consultas de uso y reportes de incidentes de staffing | Conteo del canal de consultas | Confianza para preguntar: sube al principio, y eso es bueno | Supuesto del equipo |
| Asistencia a módulos y a talleres de champions | Registro de asistencia | Tiempo realmente liberado | Supuesto del equipo |
| Pulso trimestral anónimo: miedo a ser reemplazado | Encuesta de tres preguntas, con mínimo de respuestas por grupo | Si el miedo baja con la comunicación | Supuesto; no hay medición propia hoy |
| Rotación voluntaria de perfiles junior | Dato de Talento, por área | Efecto colateral del miedo | Supuesto; la serie histórica es un faltante |

**No se miden** el uso por persona ni el volumen de prompts como desempeño
individual: esa medición mataría la franqueza que se necesita. Un cambio de
comportamiento sin mejora en tiempo de ciclo o calidad (los indicadores
rezagados) se lee como uso de trámite y dispara la revisión del formato.

### Tensiones con otras miradas

- **T1, con `finance`.** El caso de negocio supone 10% a 25% de throughput solo
  en equipos propios y descuenta staffing. En contratos facturados por hora,
  menos horas es menos facturación, así que el staffing tiene un incentivo en
  contra de usar IA. Alternativas: A, no medir productividad en staffing y
  medir solo habilitación; B, evaluar un cambio de modelo comercial (precio por
  resultado), que excede este anexo. Se deja visible.
- **T2, con `governance`.** La matriz de clientes y la ratificación de la
  política son prerrequisito de la meta de Operaciones y están fuera de este
  anexo. Si no se cierran al fin de T1, D1 pasa de B a "sin meta en Operaciones".
- **T3, con `architect`.** Medir uso en chat y Gemini requiere instrumentación
  que hoy no existe; sin eso, la métrica de staff es una encuesta.

## Insumos para Finanzas

Costo de horas = horas x USD 10-35 (supuesto del equipo). **Es un piso**: el
costo de oportunidad real es la tarifa facturable de esas horas, que no está en
`context/` ([huecos](../../material/huecos.md)); Finanzas la aplica sobre las horas.

| Concepto | Trimestre | Horas | Rango de costo (USD) | Fuente o supuesto |
|---|---|---|---|---|
| Nivel básico, ~65 personas x 6 h | T1 | ~390 | 3.900 - 13.650 | Supuesto del equipo |
| Nivel intermedio, ~50 personas x 12 h | T1-T3 | ~600 | 6.000 - 21.000 | Supuesto del equipo |
| Nivel avanzado, ~10 personas x 480 h x 10-15% (convención de costeo) | T2 | 480 - 720 | 4.800 - 25.200 | 10-15% de [Capacidad y utilización](../../context/hechos/capacidad-y-utilizacion.md); resto, supuesto |
| Champions, 8 personas x 10% x 9 meses | T2-T4 | ~1.150 | 11.500 - 40.250 | 10% de [programa](../../material/conceptos/m3u2-programa-champions.md); resto, supuesto |
| **Subtotal horas de capacitación** | T1-T4 | **~2.620 - 2.860** | **~26.200 - 100.100** | Suma |
| Líder del programa, 20% de una persona, 12 meses | T1-T4 | 0 (reasignación) | 10.800 - 24.000 | 20% x 12 x USD 4.500-10.000 ([tech lead](../../context/supuestos/costo-cargado-por-rol.md)) |
| Contractor de IA aplicada, 9 meses, 100% | T2-T4 | n/a | 40.500 - 99.000 | 9 x USD 4.500-11.000 ([costo por rol](../../context/supuestos/costo-cargado-por-rol.md)). Reemplaza la fracción de 0,8 FTE de IA aplicada del Anexo B: no se suma con ella |
| Contractor de IA aplicada en T1, 50% (alternativa B1) | T1 | n/a | 6.750 - 16.500 | 0,5 x 3 meses x USD 4.500-11.000. Reemplaza el 0,5 FTE de IA aplicada de T1 del Anexo B. **Pasa a caja un costo que B tenía como tiempo** |
| T0: reconstrucción retrospectiva y diseño de encuesta | T0 | 60 - 100 | 1.700 - 6.300 | Supuesto del equipo: 1,5 a 2,5 semanas del perfil técnico que lidera el programa, a USD 28-63 por hora (4.500-10.000 mensuales de tech lead sobre 160 h) |
| Certificación o curso externo del nivel avanzado | T2 | n/a | **Sin estimar** | Falta cotización; no se inventa |
| Instrumentación de medición de uso en chat y Gemini | T1 | n/a | Incluida en DevOps/QA del [Anexo B](02-arquitectura.md) (1.400-7.100 de tiempo); no suma | Costeada por `architect`, sin cotización de proveedores |
| Reconocimiento de champions | T2-T4 | n/a | 0 (no monetario) | Supuesto del equipo; si es monetario, Finanzas lo ajusta |
| **Total identificado** | T0-T4 | | **~86.000 - 245.900** | Suma de los renglones con costo, incluida la alternativa B1. Sin B1: ~79.200 - 229.400. No descuenta el solape con el Anexo B |

Escala: las ~2.620-2.860 horas son unas 40-44 horas por persona de la dotación
([tamaño y estructura](../../context/hechos/tamano-y-estructura.md)), cerca del
2% a 2,5% de una jornada anual.

**Cómo entra en el Anexo E.** Las horas de este anexo son **tiempo distribuido**
en la dotación (el segundo sobre de E: 590 h en T1), no el sobre de personas
clave. El tiempo clave que D aporta en T1 es el 20% del líder del programa, y el
sobre que el board confirma en G0 es de **≥1,6 FTE clave** en T1 ([Anexo E](05-business-case.md)).
El desglose de las 590 h de T1 entre básico e intermedio lo consolida E; D da las
poblaciones y las horas por nivel. No se publica una base de horas totales de la
empresa. Si el costo total entra dentro
del 1% a 3% de la facturación que se asume como capacidad de inversión
([supuesto](../../context/supuestos/capacidad-de-inversion.md)) lo calcula
Finanzas: la facturación en USD no se publica.

## Insumos para el deck

- **Decisión que se le pide al board:** aprobar capacitar y reasignar en vez de
  contratar, más **un** perfil especializado a prueba (D2), aclarando que choca con
  la restricción actual de no contratar.
- **Frase central:** en el piloto de abril (12 personas que se anotaron solas) el
  uso fue alto (NPS +42) y la capacitación falló: el primer freno fue el tiempo.
  El plan responde con casos por rol, horas dentro de la jornada y champions con
  tiempo asignado, y mide en T1 si pasa lo mismo en toda la organización.
- **Redacción sugerida para la slide 6 (propuesta para `caio`):** reemplazar
  «El piloto mostró que la gente valora la IA (NPS +42) y que falló la
  capacitación: 17% completó los cursos.» por «En el piloto de abril (n=12,
  autoseleccionado) el uso fue alto (NPS +42) y la capacitación falló: solo 17%
  completó los cursos. Es una señal, no una medición de toda la organización:
  la base de T1 la mide.»
- **Cifra para el CFO:** ~2.620-2.860 horas de capacitación, ~40-44 horas por
  persona, a USD 26.200-100.100 al costo cargado; Finanzas suma el costo de
  oportunidad a tarifa facturable. Total de personas identificado ~USD 86.000-245.900 (con contractor desde T1).
- **Señal de alerta que debe ir en la slide:** la meta combinada de 80% del
  borrador de OKR 2027 es inalcanzable con Operaciones prohibida por contrato (D1).
- **Qué se mide:** uso real semanal por área, no seats; condiciones de abandono
  a T2 y T3 explícitas.

## Cautelas

- Las poblaciones, horas por nivel, tamaño de la red de champions y umbrales de
  cada trimestre son **supuestos del equipo**, sin ficha propia; el equipo debe
  convertirlos en fichas `Supuesto` o validarlos con la línea de base.
- Las cifras de adopción vienen de fichas en `draft`; varias son rangos o
  proporciones aproximadas, y la telemetría solo mide el agente de código.
- n=12 en el piloto, autoseleccionado: no representa a la organización ni prueba
  que el formato cause mejor capacitación.
- El antes y después del proceso de delivery es un diseño propuesto sobre un
  proceso típico supuesto; falta validarlo con un delivery manager.
- La postura sobre el empleo es una propuesta; falta la decisión del Directorio y
  la revisión laboral.
- Responsable humano de cada acción: **pendiente**.
- No se usaron cifras del curso sin fuente primaria (60% menos de resistencia).

[^okr]: [OKR y objetivos](../../context/hechos/okrs-y-objetivos.md), borrador de OKR de Tecnología 2027, objetivo de eficiencia operativa con IA.
[^estructura]: [Tamaño y estructura](../../context/hechos/tamano-y-estructura.md), sección "Dependencia de personas clave".
