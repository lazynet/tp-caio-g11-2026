---
owner: caio
status: draft
title: "Anexo A — Diagnóstico y punto de partida"
---

# Anexo A — Diagnóstico y punto de partida

Slide que sustenta: [Slide 2 — Problema y diagnóstico por conciliar](../slides.md).
El diagnóstico también ordena el beneficio que se mide en la
[Slide 3 — Beneficio principal y captura](../slides.md).

> **Cifras estimadas, todavía sin validar contra fuentes internas.** Se validan
> antes de liberar la ejecución de M1-M3. La validación tiene una autorización propia.

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
por nivel) no se hizo. Responsable de validar el puntaje: a designar.

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
| Datos e infraestructura | 2 | La infraestructura está cerca del 3: AWS en varias cuentas, Kubernetes, GitOps, observabilidad ([stack](../../context/hechos/stack-y-plataforma.md)). Los datos, no: sin inventario formal, y los datos productivos de clientes no se pueden usar ([datos](../../context/supuestos/disponibilidad-de-datos.md)) | Inventario de datos con dueño y calidad, y una capa común para servir casos de IA |
| Talento y cultura | 2 (Tecnología 3, Operaciones 1) | Tecnología: ~7 de cada 10 usan el agente de código. Operaciones: ~1 de cada 10, en buena parte porque el cliente fija las herramientas ([uso de IA](../../context/hechos/uso-ia-interno.md)). El piloto de abril (n=12, autoseleccionado) dio NPS +42, pero solo el 17% completó los cursos ([piloto](../../context/hechos/encuesta-y-pilotos-ia.md)). Capacidades críticas en pocas personas ([estructura](../../context/hechos/tamano-y-estructura.md)) | Capacitación por rol que se complete y suplentes para los roles críticos |
| Gobernanza y ética | 2 | Política de uso con clasificación en cuatro niveles y contrato para agentes de código, en borrador según el último registro, del 21 de abril de 2026; no hay constancia posterior de su ratificación, y su estado actual se confirma antes de pedirla, sin matriz de clientes, sin inventario de casos ni registro de riesgos ([gobierno](../../context/hechos/gobierno-y-politica-ia.md)). ISO/IEC 27001 de la organización, sin controles específicos de IA verificados ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) | Política ratificada, inventario, registro de riesgos y comité operando |
| Adopción y valor | 1 en producto, 2 en interno | Sin IA productiva documentada en la oferta ([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)). En lo interno hay uso alto en Tecnología y un piloto con criterios cumplidos, pero sin línea de base de productividad ([productividad](../../context/supuestos/ganancia-de-productividad.md)) | Un caso en producción con valor medido contra una línea de base |

No se promedia: un promedio de 2 esconde que la brecha más grande está en el
producto que se vende y en Operaciones. Las fuentes no permiten afirmar ausencia
universal de toda medición: lo que falta es valor incremental medido contra una base.

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
recalcula. Responsables (Talento, Operaciones, Finanzas, Seguridad): a designar.

### Validación inicial con autorización propia

El [hito inicial](../../context/supuestos/paquete-minimo-de-aprendizaje.md#validación-inicial)
resuelve el trabajo que necesita la validación: el Directorio o una autoridad
formalmente delegada autoriza primero la preparación de 2026. Antes de iniciarla,
Operaciones y los managers confirman sus agendas, trabajo desplazado e imputación
presupuestaria. No se exige un diagnóstico ya validado para producir esa evidencia.

Se proponen diez días hábiles, con 4-6 entrevistas de una hora a referentes de
las funciones necesarias, contraste documental y una ronda de conciliación.
El resultado es un diagnóstico revisado por dimensión, con fuentes, cambios de
puntaje, brechas y faltantes explícitos. Las hipótesis pendientes se conservan;
una incertidumbre que bloquee el alcance impide liberar esa actividad.

La validación organizativa suma 60-96 h internas nuevas; junto con las 20-40 h
técnicas existentes, la primera liberación totaliza 80-136 h y un techo de 8 mil
USD de tiempo, sin caja incremental. Incluye participantes, verificación y cierre
documental. Son supuestos para el borrador, elegidos por Martín; falta el acuerdo
del equipo y la autorización empresarial. El [Anexo E](05-business-case.md)
costea las tareas y el [Anexo F](06-roadmap-riesgo.md) define el segundo pase:
continuar, reducir/resecuenciar o detener antes de ejecutar M1-M3.

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

1. **Gobernanza:** ratificar la política y armar la matriz de clientes. Es la
   condición para cualquier caso de IA en el producto ([Anexo C](03-gobierno-seguridad.md)).
2. **Datos y medición:** inventario de datos y línea de base de productividad,
   incidentes y costo. Sin línea de base no hay gates ([Anexo B](02-arquitectura.md)).
3. **Adopción y valor:** medir capacidad con calidad contra la base y, en el
   producto, observar el problema del asistente de integración (tiempo a la
   primera integración exitosa) antes del mes 6. Sin problema, base y señal
   comercial escrita, no se construye ([Anexo F](06-roadmap-riesgo.md)).

Talento y cultura no queda afuera: es el habilitador de las tres
([Anexo D](04-personas-cultura.md)). Como en el caso de referencia del método, no
tiene base sólida sin estrategia y datos confiables.

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El puntaje refleja documentos y no la práctica | Alta | Medio | Contraste documental y 4-6 entrevistas focalizadas en el hito inicial, supuesto de alcance a ratificar | Si la validación mueve dos o más dimensiones, se rehace el orden de prioridades |
| El perímetro de personas mezcla poblaciones y fechas | Alta | Alto para la capacidad | Conciliar corte, nómina, contratistas, personas/FTE y horas por rol dentro de la primera liberación | Sin conciliación no se libera la ejecución de M1-M3 |
| Las cifras del caso son estimadas y no están validadas contra fuentes internas | Alta | Alto | Validar las fuentes que sostienen cada puntaje | Sin validación, el diagnóstico se presenta como hipótesis y no como hecho |
| La telemetría solo mide el agente de código y subestima el uso en staff | Alta | Medio | Medir chat y Workspace en los meses 1-3 ([Anexo D](04-personas-cultura.md)) | — |
| Leer la baja adopción de Operaciones como problema cultural | Media | Medio | Separar lo contractual (el cliente fija herramientas) de lo cultural | — |

## Decisiones

- **Usar las cinco dimensiones del diagnóstico de madurez** y no la variante
  extendida (seis ejes de NovaGob y AIMM): son las del método base y AIMM sigue
  sin validar ([fuentes faltantes](../../material/huecos.md)). Reversible.
- **Puntuar producto e interno por separado** en Adopción y valor, y Tecnología y
  Operaciones por separado en Talento. Alternativa descartada: un solo número por
  dimensión, que esconde dónde está la brecha. Reversible.
- **Financiar la validación antes de liberar M1-M3:** el primer hito confirma o
  corrige los puntajes con evidencia y conserva los faltantes como hipótesis.
  Quien produce, quien verifica y quien firma: personas distintas, a designar.
  Éxito: puntajes revisados con trazabilidad y alcance ejecutable; si una brecha
  bloquea el alcance, se reduce/resecuencia o se detiene, sin liberación automática.

## Cautelas

- Es un diagnóstico de escritorio, sin entrevistas: se toma como hipótesis.
- El estado de la política es al 2026-04-21; no hay registro posterior.
- Los niveles 2 y 4 no están descritos en el método; el 2 se usa como intermedio.
- Las cifras de este anexo son estimadas y se validan contra fuentes internas
  durante la validación autorizada, antes de liberar la ejecución de M1-M3.
