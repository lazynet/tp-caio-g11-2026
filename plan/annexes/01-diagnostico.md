---
owner: caio
status: ready
title: "Anexo A — Diagnóstico y punto de partida"
---

# Anexo A — Diagnóstico y punto de partida

::: {.annex-summary}
## Síntesis ejecutiva

**La IA ya se usa en la operación, pero su aporte incremental no está medido
contra una base.** Aplicamos el [diagnóstico de madurez en cinco dimensiones](../../material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md) para
priorizar brechas de gobierno, medición y adopción. Es una hipótesis de
escritorio, a contrastar antes de liberar la ejecución.

| Qué condiciona el plan | Qué hacemos primero |
|---|---|
| El uso interno y el harness del SDLC ya existen; no prueban mejora ni IA productiva en la oferta | Medir capacidad con calidad, sin atribuir beneficios retrospectivos |
| La utilización facturable estimada es 83–90%; el promedio no demuestra horas libres por rol | Conciliar personas, FTE, agendas y trabajo desplazado |
| Hay política e inventario de datos; falta verificar su cobertura y aplicación para los usos elegibles | Probar controles y restricciones por herramienta y cliente |
| La oportunidad de producto sigue siendo una hipótesis | Estudiar el problema de integración antes de decidir construir |

**Recomendación:** mantener el paquete mínimo y financiar primero diez días
hábiles de validación en 2026: hasta 8k USD de tiempo propio y caja 0. La segunda
liberación depende de diagnóstico revisado, agendas conciliadas y las demás
condiciones del [Anexo G](07-resoluciones.md#autoridad-y-liberaciones).

**Responsabilidad:** Martín coordina la revisión del diagnóstico en el TP.
En Acme, el CAIO produce, hay verificación independiente según el entregable y
el CEO decide la continuidad condicionada. Las personas se nombran en las actas.

**Éxito y corte:** diagnóstico trazable y alcance ejecutable. Si faltan capacidad,
fuentes o viabilidad para una actividad, se reduce, resecuencia o detiene antes
de M1. La validación no convierte los supuestos en hechos por sí sola.

**Para profundizar:** [puntajes por dimensión](#puntaje-propuesto-por-dimensión),
[perímetro por conciliar](#perímetro-por-conciliar-antes-de-liberar-m1-m3),
[validación inicial](#validación-inicial-con-autorización-propia) y
[cautelas](#cautelas).
:::

## Desarrollo y fuentes

Slide que sustenta: [Problema](../slides.md). El diagnóstico también ordena el
beneficio que se mide en la slide [Beneficio](../slides.md). Montos en k USD
(1k USD = 1.000 USD).

> **Cifras estimadas, todavía sin validar contra fuentes internas.** Se validan
> antes de liberar la ejecución de M1-M3, en la validación inicial que el Directorio
> libera al aprobar el plan ([R-02](07-resoluciones.md#autoridad-y-liberaciones)).

## Objetivo

Mostrar dónde está Acme Labs hoy en las cinco dimensiones del diagnóstico de
madurez
([Fuente](../../material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md)) y
de ahí sacar las dos o tres brechas que el plan ataca primero.

**El diagnóstico es una hipótesis.** Antes de liberar la ejecución de M1-M3, hay que
conciliar corte, nómina, contratistas, personas/FTE y horas por rol: las fuentes
documentales cubren poblaciones, unidades y fechas distintas (ver "Perímetro por
conciliar"). Además, las cifras se validan contra fuentes internas. Son
exigencias distintas: validar una cifra no libera agendas, y una agenda aprobada
no sustituye la trazabilidad.

**El puntaje es una propuesta del CAIO a validar, no un hecho.** Sale de leer las
fuentes del caso, todas con cifras estimadas, sin entrevistas ni encuestas
propias: el paso 2 del método de diagnóstico de madurez (entrevistas y encuestas
por nivel) no se hizo. El puntaje se valida en la validación inicial: produce el
CAIO, verifica el verificador senior independiente y el CEO recibe el resultado en
la segunda liberación ([R-06](07-resoluciones.md#autoridad-y-liberaciones)).

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Escala | 1 (Inicial) a 5 (Transformacional); el método describe solo los niveles 1, 3 y 5 | [Fuente: diagnóstico de madurez](../../material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md) |
| Cómo se lee un 2 | Entre el nivel 1 y el 3 descriptos: hay piezas del 3, pero sin formalizar ni medir | Criterio del CAIO, porque el método no describe el 2 |
| Alcance | La organización completa: producto que se vende y operación interna | [Índice del caso](../../context/index.md) |
| Estrategia de partida | El escenario parte sin una estrategia de IA formal aprobada, aunque hay iniciativas y objetivos propuestos | [Supuesto del caso](../../context/supuestos/estrategia-de-ia-de-partida.md) |
| Evidencia | Solo hechos y supuestos anonimizados del caso | [Índice del caso](../../context/index.md) |
| Corte temporal | Datos hasta octubre de 2026 con cortes distintos por fuente: nómina y contratistas a septiembre, utilización promedio de 2026, concentración y cifras financieras del cierre de agosto | [Situación económica](../../context/hechos/situacion-economica.md), [tamaño](../../context/hechos/tamano-y-estructura.md), [capacidad](../../context/hechos/capacidad-y-utilizacion.md) |

## Evidencia

### Puntaje propuesto por dimensión

| Dimensión | Propuesta | Evidencia principal | Brecha frente al nivel 3 |
|---|---|---|---|
| Estrategia y liderazgo | 2 | El escenario parte sin estrategia de IA formal aprobada ([supuesto](../../context/supuestos/estrategia-de-ia-de-partida.md)). Hay iniciativas y objetivos propuestos: propuestas al Directorio y un borrador de OKR 2027 con eficiencia con IA ([OKR](../../context/hechos/okrs-y-objetivos.md), [IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)). El 2 refleja ese avance parcial; no se deriva solo de la ausencia de aprobación | Estrategia de IA aprobada, con dueño y atada a resultados del negocio |
| Datos e infraestructura | 2 provisional | Hay AWS en varias cuentas, Kubernetes, GitOps y observabilidad ([stack](../../context/hechos/stack-y-plataforma.md)). Existe inventario de datos con responsables, clasificación y calidad documentada; las fuentes están distribuidas entre sistemas ([inventario](../../context/hechos/inventario-y-distribucion-de-datos.md)). Falta contrastar cobertura, accesos, integración y gobierno operativo para los casos de IA | Reutilizar y completar el inventario existente; demostrar acceso común, gobierno y calidad adecuados a las fuentes elegibles |
| Talento y cultura | 2 provisional | No hay programa de formación en IA por rol con seguimiento de finalización ([formación](../../context/hechos/formacion-ia-por-rol.md)). Hay uso de herramientas y experiencias de aprendizaje: el piloto de abril (n=12, autoseleccionado) incluyó cursos, con 17% de finalización ([piloto](../../context/hechos/encuesta-y-pilotos-ia.md)). La adopción del agente de código difiere entre áreas y está condicionada por los clientes ([uso de IA](../../context/hechos/uso-ia-interno.md)); no prueba por sí sola madurez cultural ni competencias | Programa por rol con seguimiento de finalización y aprendizaje aplicado; suplentes para roles críticos, sujetos al diagnóstico de capacidades |
| Gobernanza y ética | 2 provisional | Política de uso de IA vigente, aprobada según el responsable del caso; el Directorio la ratifica al aprobar el plan y la preparación deja constancia de versión y alcance ([R-07](07-resoluciones.md#gobierno-y-seguridad)). La validación inicial revisa el estado de la matriz de clientes, el inventario de casos, el registro de riesgos y la operación del Council ([gobierno](../../context/hechos/gobierno-y-politica-ia.md)). La certificación de seguridad de la organización no demuestra controles específicos de IA ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) | Aplicación de la política y gobierno operativo con inventario de casos, registro de riesgos, matriz y comité funcionando con evidencia |
| Adopción y valor | 1 en producto, 2 en interno, provisionales | No se documenta IA productiva en la oferta; el harness confirmado no se entrega ni comercializa a clientes ([oferta](../../context/hechos/ia-en-producto-y-oferta.md)). Hay herramientas de harness para el SDLC de uso exclusivamente interno, sin mediciones de tiempo, calidad o costo contra una línea de base para evaluar su impacto, según el responsable del caso ([uso interno](../../context/hechos/uso-ia-interno.md)) | Medir valor y calidad contra una base en los procesos internos; para producto, evidencia de una funcionalidad u oferta de IA con valor medido |

No se promedian dimensiones ni frentes: en Adopción y valor se conserva la
diferencia entre producto e interno. Las fuentes no permiten afirmar ausencia
universal de toda medición. Lo que no hay es valor incremental medido contra una
base: es la premisa del pedido, que financia producir esa medición con rampa 0% en
M1-M3 ([R-01](07-resoluciones.md#autoridad-y-liberaciones)).

El harness del SDLC se clasifica en el frente interno. Su existencia no prueba
por sí sola valor incremental ni eleva el puntaje de producto; otros casos de
IA en la oferta requieren evidencia propia.

El harness existente integra el punto de partida de la medición prospectiva.
La base y el protocolo permiten contrastar mejoras posteriores; no se atribuyen
beneficios retrospectivos sin una comparación válida.

En Talento y cultura, el 2 refleja uso y aprendizaje parciales, sin programa por
rol con seguimiento. No se asignan niveles de madurez por área a partir de la
telemetría de una herramienta; se contrastan competencias y prácticas culturales.

En Datos e infraestructura, la distribución entre sistemas no determina por sí
sola el nivel de madurez. El 2 se conserva como hipótesis provisional hasta
contrastar la plataforma y el gobierno operativo; el inventario existente es un
avance y su cobertura para los casos de IA sigue por verificar.

### Perímetro por conciliar antes de liberar M1-M3

| Dato | Población, unidad y fecha | Qué no permite derivar |
|---|---|---|
| Dotación de 60-70 personas | Nómina y contratistas, septiembre de 2026 ([tamaño](../../context/hechos/tamano-y-estructura.md)) | Personas/FTE disponibles por rol ni la mezcla de nómina y contratistas |
| Utilización 83%-90%, bench <1 FTE | Promedio de toda la empresa en 2026, sin corte por proyecto ([capacidad](../../context/hechos/capacidad-y-utilizacion.md)) | Que haya horas libres en los roles que el plan necesita |
| Concentración 40%-50% | Facturación, agosto de 2026 ([cartera](../../context/hechos/cartera-y-concentracion.md)) | Cuántas personas o proyectos dependen de ese cliente |

**Qué se concilia, en privado y con quien tenga acceso:** el corte común, la
nómina, los contratistas, la conversión personas→FTE y las horas por rol, en la
matriz semanal de [Anexo D](04-personas-cultura.md) ("Capacidad efectiva"). La
supuesta diferencia con una conversación de dotación no está respaldada por
ninguna fuente: no se afirma que el rango esté mal ni se explica la diferencia
como hecho. Sin conciliación no se derivan las horas del
[Anexo E](05-business-case.md) de los agregados; si cambian los insumos, se
recalcula. La matriz la produce Personas con Operaciones y la verifica el CFO
([R-24](07-resoluciones.md#personas)); las personas que ocupan cada rol se nombran
en el acta de la primera liberación ([R-06](07-resoluciones.md#autoridad-y-liberaciones)).

### Validación inicial con autorización propia

El [hito inicial](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial)
resuelve el trabajo que necesita la validación: el Directorio libera la
preparación de 2026 al aprobar el plan
([R-02](07-resoluciones.md#autoridad-y-liberaciones)). Antes de iniciarla,
Operaciones y los managers confirman sus agendas, trabajo desplazado e imputación
presupuestaria. No se exige un diagnóstico ya validado para producir esa evidencia.

Se proponen diez días hábiles, con 4-6 entrevistas de una hora a referentes de
las funciones necesarias, contraste documental y una ronda de conciliación.
El resultado es un diagnóstico revisado por dimensión, con fuentes, cambios de
puntaje, brechas y faltantes explícitos. Las hipótesis abiertas se conservan con
su fuente; una incertidumbre que bloquee el alcance impide liberar esa actividad en
la segunda liberación, que firma el CEO y decide reducir o detener
([R-05](07-resoluciones.md#autoridad-y-liberaciones)).

Son dos preparaciones distintas. La **técnica**, ya costeada, suma 20-40 h:
12-24 h de viabilidad, extracción e historial del [Anexo B](02-arquitectura.md)
y 8-16 h de preparación de facilitación del [Anexo D](04-personas-cultura.md);
techo 3k USD. La **organizativa** es nueva: 60-96 h de entrevistas, padrón y
matriz, restricciones, conciliación económica y verificación; techo 5k USD.
Juntas, la primera liberación totaliza 80-136 h y un techo de 8k USD de tiempo,
sin caja incremental, con el cierre documental incluido
([Anexo E](05-business-case.md), "Primera autorización").

Los solapes de horas entre B, C y D que el costeo supone (DevOps, QA, seniors y
Seguridad) los adopta el Directorio al aprobar el plan
([R-26](07-resoluciones.md#finanzas)). La validación los comprueba: si las
exportaciones no caben en el tope de DevOps se reportan como uso estimado, sin
sumar horas, y si aun así no cabe, el CFO recostea antes de M1 dentro de 71 y firma
el CEO.

**Quién decide y cómo se sale.** El Directorio libera la validación al aprobar el
plan; al cerrarla, el CEO, por delegación del Directorio, decide en un acta
continuar con el alcance validado, reducir/resecuenciar o detener
([R-04 y R-05](07-resoluciones.md#autoridad-y-liberaciones)). Si se detiene, la exposición
es el tiempo efectivamente trabajado, hasta 8k USD, y caja 0; la segunda
liberación de hasta 71k USD no es automática ([Anexo F](06-roadmap-riesgo.md),
"Validación inicial y dos liberaciones").

### Hechos de contexto que condicionan el plan

| Hecho | Valor | Por qué importa | Fuente |
|---|---|---|---|
| Concentración de clientes | El principal pesa 40%-50% de la facturación; los cinco primeros, más del 90% | Lo que se haga con IA sobre un cliente grande es una decisión de riesgo comercial | [Cartera](../../context/hechos/cartera-y-concentracion.md) |
| Capacidad ociosa | Utilización facturable 83%-90%; bench menor a 1 FTE | Todo el plan compite con horas facturables | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md) |
| Gasto de tecnología | De ~2% a ~4% de la facturación entre enero y agosto de 2026 | El OKR 2027 pide bajarlo a menos de 3,5% | [Costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real de IA | ~12 veces lo que se paga por suscripción en el agente de código | Un cambio de precio a consumo pega en el costo | [Costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Regulación de los clientes | El BCRA obliga a bancos y PSP a gobernar la IA propia y de terceros | Acme Labs es tercero: entra en el análisis de riesgo del cliente | [Regulación](../../context/hechos/regulacion-clientes-financieros.md) |
| Situación económica | Facturación mensual con un crecimiento cercano a 35% entre enero y agosto de 2026; EBITDA mensual de 21%-30% | Hay margen para invertir por etapas | [Situación económica](../../context/hechos/situacion-economica.md) |

### Brechas que el plan prioriza

Siguiendo el método de diagnóstico de madurez (paso 6: dos o tres brechas críticas), el CAIO propone:

1. **Gobernanza:** verificar el alcance y la aplicación de la política aprobada,
   revisar la matriz de clientes y completar sus brechas antes de habilitar casos
   de IA en el producto ([Anexo C](03-gobierno-seguridad.md)).
2. **Datos y medición:** revisar y completar el inventario existente para las
   fuentes elegibles, verificar su acceso e integración y producir la línea de
   base de productividad, incidentes y costo. Sin línea de base no hay gates
   ([Anexo B](02-arquitectura.md)).
3. **Adopción y valor:** medir capacidad con calidad contra la base, sabiendo que
   con una cohorte de 15-20 personas solo se distinguen mejoras grandes: el valor
   se lee en el mes 9 ([R-19](07-resoluciones.md#arquitectura-y-medición)); en el
   producto, observar el problema del asistente de integración (tiempo a la
   primera integración exitosa) antes del mes 6. Sin problema, base y señal
   comercial escrita, no se construye ([Anexo F](06-roadmap-riesgo.md)).

Talento y cultura no queda afuera: es el habilitador de las tres
([Anexo D](04-personas-cultura.md)). Como en el caso de referencia del método, no
tiene base sólida sin estrategia y datos confiables.

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El puntaje refleja documentos y no la práctica | Alta | Medio | Contraste documental y 4-6 entrevistas focalizadas en la validación inicial, con el alcance de R-02 | Si la validación mueve dos o más dimensiones, se rehace el orden de prioridades |
| El perímetro de personas mezcla poblaciones y fechas | Alta | Alto para la capacidad | Conciliar corte, nómina, contratistas, personas/FTE y horas por rol dentro de la primera liberación | Sin conciliación no se libera la ejecución de M1-M3 |
| Las cifras del caso son estimadas y no están validadas contra fuentes internas | Alta | Alto | Validar las fuentes que sostienen cada puntaje | Sin validación, el diagnóstico se presenta como hipótesis y no como hecho |
| La telemetría solo mide el agente de código y subestima el uso en staff | Alta | Medio | Medir chat y Workspace en los meses 1-3 ([Anexo D](04-personas-cultura.md)) | — |
| Leer la baja adopción de Operaciones como problema cultural | Media | Medio | Separar lo contractual (el cliente fija herramientas) de lo cultural | — |

## Decisiones

- **Usar las cinco dimensiones del diagnóstico de madurez** y no la variante
  extendida (seis ejes de NovaGob y AIMM): son las del método base y AIMM sigue
  sin validar ([fuentes faltantes](../../material/huecos.md)). Reversible.
- **Puntuar producto e interno por separado** en Adopción y valor. En Talento,
  distinguir competencias y prácticas por área durante la validación, sin
  equiparar uso de una herramienta con madurez. Alternativa descartada: derivar
  subpuntajes de talento solo de la telemetría de adopción. Reversible.
- **Financiar la validación antes de liberar M1-M3:** el primer hito confirma o
  corrige los puntajes con evidencia y conserva los faltantes como hipótesis.
  Quien produce, quien verifica y quien firma: roles distintos, fijados en
  [R-06](07-resoluciones.md#autoridad-y-liberaciones); las personas se nombran en
  el acta de la primera liberación.
  Éxito: puntajes revisados con trazabilidad y alcance ejecutable; si una brecha
  bloquea el alcance, se reduce/resecuencia o se detiene, sin liberación automática.

## Cautelas

- Es un diagnóstico de escritorio, sin entrevistas: se toma como hipótesis.
- La aprobación de la política fue informada por el responsable del caso; el
  respaldo documental es el acta de aprobación del plan, que la ratifica (R-07), y
  la preparación deja constancia de versión y alcance.
- Los niveles 2 y 4 no están descritos en el método; el 2 se usa como intermedio.
- Las cifras de este anexo son estimadas y se validan contra fuentes internas
  durante la validación autorizada, antes de liberar la ejecución de M1-M3.
