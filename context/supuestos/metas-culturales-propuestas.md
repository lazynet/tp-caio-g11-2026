---
type: Supuesto
title: "Metas culturales y de adopción propuestas por el plan"
description: "El plan propone metas de adopción por tramo, sin respaldo de benchmark: el básico ≥90% en el mes 3 es un criterio del mínimo, medido por aprobación de un caso práctico por rol, y las de Tecnología, Operaciones, prompts y staff de los meses 4-12 son del programa completo, con costeo y autorización adicionales."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-21
  scope: "Revalidación registrada por instrucción expresa de Martín en la sesión del 21/10/2026 sobre el contenido vigente del PR #52. Metas de diseño: básico de 60-70 personas con aprobación práctica por rol de al menos 90% en M3; Tecnología con uso semanal de al menos 80% en M6 y 85% en M12; Operaciones habilitadas con 40% en M9 y 60% en M12 solo con programa ampliado autorizado en M6, sin meta en M6. R-13, R-19, R-21 y R-23 fijan agregación, instrumento, responsables, denominadores y consecuencias; ninguna meta de adopción libera fondos por sí sola. Se declara la brecha frente al OKR conjunto de 80%. Se mantiene como Supuesto de diseño: esta declaración no acredita mediciones, contratos, disponibilidad ni ejecución de decisiones futuras."
tags: [supuesto, personas, adopcion, metas]
sources:
  - id: okr
    resource: "context/hechos/okrs-y-objetivos.md"
    title: "Borrador de OKR de Tecnología 2027 (uso activo semanal) y meta de utilización facturable del Directorio"
  - id: uso
    resource: "context/hechos/uso-ia-interno.md"
    title: "Adopción por área medida por la telemetría del agente de código y uso detectado de Gemini"
  - id: pilotos
    resource: "context/hechos/encuesta-y-pilotos-ia.md"
    title: "Calidad de uso en el piloto de abril, ejemplos del resultado esperado"
  - id: tamano
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Dotación y peso aproximado de Operaciones y Tecnología"
  - id: politica
    resource: "context/hechos/gobierno-y-politica-ia.md"
    title: "Política de IA vigente; la matriz de restricciones por cliente no consta"
  - id: poblaciones
    resource: "context/supuestos/poblaciones-de-capacitacion.md"
    title: "Poblaciones del programa completo y reparto supuesto de horas de Operaciones"
  - id: umbrales
    resource: "context/supuestos/umbrales-tecnicos-propuestos.md"
    title: "Umbral técnico de uso de la cohorte para extender la lectura"
  - id: ganancia
    resource: "context/supuestos/ganancia-de-productividad.md"
    title: "Hipótesis de throughput, distinta de las metas de adopción"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio R-13, R-19, R-21 y R-23 (autoridad y definiciones, no origen de las cifras)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21 }
---
# Supuesto

Las metas siguientes son **supuestos de diseño del plan**: objetivos internos que
parten de hechos verificados del caso (el borrador de OKR 2027 y la adopción
medida hoy), no un hecho de la organización ni un benchmark externo. El básico
≥90% del mes 3 es un criterio del **mínimo**; las de los meses 7-12 son del
**programa ampliado** y no están en el presupuesto del mínimo. Cada una se lee con
numerador y denominador, por área y agregada, sin dato individual.[^okr]

| Meta | Período | Denominador | De qué hecho parte y qué es diseño |
|---|---|---|---|
| Básico completado ≥90%, con evaluación práctica por rol | Cierre de los meses 1-3 | Dotación del básico, 60-70 personas (referencia ~65)[^tamano] | Hoy no hay formación por rol con seguimiento y en el piloto de abril solo 17% completó los cursos.[^pilotos] El 90% es diseño: deja un 10% para ausencias e ingresos del tramo. El instrumento (aprobar un caso permitido del rol, no asistir) lo fija R-21[^resoluciones] |
| Tecnología, uso activo semanal ≥80% | Cierre de los meses 4-6 y sostenido en 7-9 | Personas de Tecnología según el padrón por área, con cobertura publicada | El OKR fija 80% para **Operaciones y Tecnología juntas**;[^okr] hoy Tecnología está en ~7 de cada 10 con el agente de código.[^uso] Aplicar la cifra del OKR a Tecnología sola, unos 10 puntos sobre el proxy actual, es diseño |
| Tecnología, uso activo semanal ≥85% | Meses 10-12 | Ídem | Diseño: 5 puntos sobre la cifra del OKR. Con Tecnología en 85% y áreas de peso parecido,[^tamano] el 80% combinado del OKR exige 75% de Operaciones sobre su total (aritmética: (85 + 75) / 2 = 80) |
| Operaciones habilitadas, uso activo ≥40% | Cierre de los meses 7-9, **solo si el gate del mes 6 autoriza el programa ampliado**; en el mes 6 Operaciones no tiene meta | Personas de Operaciones **habilitadas** por la matriz de restricciones por cliente; se informa también sobre el total | Hoy Operaciones está en ~1 de cada 10 sobre su total y trabaja con las herramientas que permite cada cliente;[^uso] la matriz de restricciones no consta.[^politica] Diseño: 40% es dos tercios de la meta final, informado sin efecto de gate (R-19)[^resoluciones] |
| Operaciones habilitadas, uso activo ≥60% | Meses 10-12, solo con programa ampliado | Ídem | Diseño: por debajo del nivel actual de Tecnología (~7 de cada 10),[^uso] porque Operaciones parte de ~1 de cada 10 y su intermedio llega recién en los meses 7-9 |
| Pedidos con ejemplos del resultado esperado ≥30% | Cierre de los meses 7-9 | Muestra agregada de prompts del chat | La base de 5% o menos viene del análisis del piloto (n=12, solo chat);[^pilotos] el 30% es diseño |
| Staff, uso activo ≥50% | Meses 10-12 | Personas de staff según el padrón | No hay fuente que mida su uso frecuente: la telemetría no capta chat ni Gemini, y el ~60% de Gemini es detección, no uso semanal.[^uso] El 50% es diseño, por debajo de esa detección |

# Alcance: mínimo y programa ampliado

- **Básico ≥90% en el mes 3.** El mínimo reserva el básico de 6 h para toda la
  población (60-70 personas, 360-420 h) y el plan lo lee en el mes 3 con el
  instrumento de R-21: el CAIO lo aprueba antes de iniciar el básico (semana 5, o
  9 si se amplía la base); dictado sin instrumento, el ≥90% queda «sin medir» y no
  se da por cumplido.[^resoluciones]
- **Tecnología ≥80% en el mes 6.** Se lee con la formación del mínimo (básico para
  todos e intermedio de la cohorte, ambos en los meses 1-3, desde la semana 9 en
  el camino esperado de base de 8 semanas, R-18), con más de un tramo de margen.
  El gate del mes 6 decide por adopción, costo y controles; el valor se lee en el
  mes 9.[^resoluciones]
- **Metas de los meses 7-12 (programa ampliado).** Suponen intermedio ampliado
  (~50 personas), avanzado y champions con tiempo asignado,[^poblaciones] que el
  Directorio autoriza o no en el gate del mes 6 (R-23).[^resoluciones] Sin esa
  autorización se informan; no se prometen con los techos del mínimo.

# Qué no se debe confundir

- El **40% de Operaciones** de la ficha de poblaciones es el reparto supuesto de
  horas de básico e intermedio, no una meta de uso.[^poblaciones]
- El **40% de la cohorte** de los umbrales técnicos es el criterio de uso para
  extender la lectura de la prueba, otra métrica y otro denominador.[^umbrales]
- El **72,5%** es el resultado aritmético de 85% y 60% con toda Operaciones
  habilitada y áreas de igual peso, (85 + 60) / 2: no es un máximo ni una
  predicción.
- El **combinado original** del OKR se informa con su denominador completo, sin
  declararlo cumplido por el plan; si se revisa el resultado clave lo decide el
  Directorio en el mes 3 (R-23).[^resoluciones]
- Las metas de adopción no equivalen a la hipótesis de throughput de la ficha de
  ganancia, que no es una meta.[^ganancia]

# Bandas de lectura

Supuestos de diseño, no benchmarks; se ajustan con la línea de base de los meses
1-3:

- Mes 3: básico ≥90% con evaluación práctica pasa; ≥50% y <90% se rediseña el
  formato; <50% se cambia el formato (R-21).[^resoluciones] El 50% es la mitad de
  la dotación.
- Mes 6: Tecnología ≥80% mantiene; ≥60% y <80% rediseña la formación; <60% frena
  las horas de formación que no sean rediseño. El 60% está por debajo del proxy
  actual de Tecnología (~7 de cada 10),[^uso] así que una lectura bajo ese valor
  señala una caída contra hoy, no solo una meta incumplida.

**En el mínimo**, esas lecturas llevan a rediseñar y recostear antes de comprometer
horas nuevas: la continuidad del mínimo no incluye formación general de los meses
4-12 y no hay horas de formación M4-M12 que frenar. **Cortar o suspender horas de
formación ampliada** aplica solo si ese alcance fue costeado y autorizado. Ninguna
meta de adopción libera ni corta fondos por sí sola (R-19).[^resoluciones]

# Dependencias

- Tratamiento y retención de los eventos de uso por persona: el Responsable de
  seguridad fija en la preparación de 2026, antes de extraer cualquier serie, la
  regla por defecto (agregados por área desde las consolas existentes); un
  tratamiento por persona espera la revisión de M1, con Personas y Legal externo
  consultados, y sin ella la fuente queda «sin medir» (R-13).[^resoluciones]
- Línea de base prospectiva congelada en las semanas 1-4 (hasta 8 si se extiende)
  y definición de «activo» fijada por el Directorio, con el diccionario cerrado
  antes de congelarla; la medición semanal es la lectura oficial (R-23).[^resoluciones]
- Matriz de restricciones por cliente, que da el denominador de Operaciones
  habilitadas: la completa el Responsable comercial del cliente para los clientes
  principales al cierre de los meses 1-3; sin ella no hay meta en Operaciones
  (R-23).[^resoluciones]
- Capacidad por persona y semana, y costeo del tramo, validados antes de
  comprometer horas.

# Qué lo invalidaría

- Una línea de base que no permita medir uso activo con cobertura suficiente: la
  meta queda «sin medir» y no se convierte en inactividad.
- Que la matriz deje habilitada una fracción tan chica de Operaciones que el
  denominador pierda sentido.
- Que el Directorio no autorice el programa ampliado en el gate del mes 6: las
  metas de los meses 7-12 quedan como seguimiento informado.

# Cautelas

- Es un supuesto de diseño escrito por un agente. Una revisión humana futura lo
  confirmaría como propuesta; no lo convierte en hecho ni en benchmark.
- Cada cifra parte de un hecho verificado (OKR, adopción por área, piloto,
  dotación) y el resto es diseño, dicho fila por fila. Los anexos del plan
  aplican estas metas; no son su fuente.
- La telemetría actual solo mide el agente de código: Tecnología se publica como
  proxy y no se extrapola a staff ni a Operaciones.[^uso]
- El piloto de abril (n=12, autoseleccionado) da la base de ejemplos al pedir
  solo para el chat y no representa a la organización.[^pilotos]
- Las cifras son rangos y metas, no mediciones; se ajustan con la base de los
  meses 1-3.

[^okr]: OKR y objetivos: borrador de OKR de Tecnología 2027, objetivo de eficiencia operativa con IA (80% o más de las personas de Operaciones y Tecnología con uso activo semanal; ratios con numerador y denominador).
[^uso]: Uso de IA interno: personas con actividad del agente de código por área (Tecnología ~7 de cada 10, Operaciones ~1 de cada 10), uso detectado de Gemini y cautela de que Operaciones usa lo que permite cada cliente.
[^pilotos]: Encuesta y pilotos internos de IA: completitud de cursos del piloto de abril y ejemplos del resultado esperado en 5% o menos.
[^tamano]: Tamaño y estructura de la organización, dotación y pesos aproximados de las áreas.
[^politica]: Gobierno y política de IA: la política vigente no acredita que exista la matriz de restricciones por cliente.
[^poblaciones]: Poblaciones y tiempos de capacitación en IA, programa completo y reparto supuesto de horas de Operaciones.
[^umbrales]: Umbrales técnicos propuestos por la arquitectura, impacto de extensión de la prueba.
[^ganancia]: Ganancia de productividad por IA en ingeniería, supuesto de throughput de 10% a 25%.
[^resoluciones]: Anexo G, resoluciones del Directorio: R-13 (datos de uso por persona), R-19 (las métricas de seguimiento no liberan ni cortan fondos), R-21 (formación del mínimo y evaluación del básico) y R-23 (definición de activo, metas, brecha del OKR y autorización del programa ampliado en el gate del mes 6).
