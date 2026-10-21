---
type: Supuesto
title: "Metas culturales y de adopción propuestas por el plan"
description: "El plan propone metas de adopción por tramo, sin respaldo de benchmark: el básico ≥90% en el mes 3 es un criterio del mínimo, medido por aprobación de un caso práctico por rol, y las de Tecnología, Operaciones, prompts y staff de los meses 4-12 son del programa completo, con costeo y autorización adicionales."
status: draft
tags: [supuesto, personas, adopcion, metas]
sources:
  - id: okr
    resource: "context/hechos/okrs-y-objetivos.md"
    title: "Borrador de OKR de Tecnología 2027, resultado clave de uso activo semanal"
  - id: paquete-minimo
    resource: "context/supuestos/paquete-minimo-de-aprendizaje.md"
    title: "Poblaciones del mínimo y objetivo de completitud del básico para dimensionar horas"
  - id: pilotos
    resource: "context/hechos/encuesta-y-pilotos-ia.md"
    title: "Calidad de uso en el piloto de abril, ejemplos del resultado esperado"
  - id: poblaciones
    resource: "context/supuestos/poblaciones-de-capacitacion.md"
    title: "Poblaciones del programa completo y reparto supuesto de horas de Operaciones"
  - id: umbrales
    resource: "context/supuestos/umbrales-tecnicos-propuestos.md"
    title: "Umbral técnico de uso de la cohorte para extender la lectura"
  - id: ganancia
    resource: "context/supuestos/ganancia-de-productividad.md"
    title: "Hipótesis de throughput, distinta de las metas de adopción"
  - id: tamano
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Dotación y peso aproximado de Operaciones y Tecnología"
  - id: personas
    resource: "plan/annexes/04-personas-cultura.md"
    title: "Anexo D, hitos culturales, criterios de éxito y condiciones de abandono"
  - id: roadmap
    resource: "plan/annexes/06-roadmap-riesgo.md"
    title: "Anexo F, gates y disparadores de adopción"
  - id: negocio
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, continuación condicional del mínimo sin nuevas cohortes"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio R-13, R-21 y R-23"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21 }
---
# Supuesto

El plan propone las metas siguientes como **objetivos internos**. No son un hecho
de la organización ni un benchmark externo. El básico ≥90% del mes 3 es un
criterio del **mínimo**; las de los meses 4-12 son del **programa completo** y no
están incluidas en el presupuesto del mínimo. Cada una se lee con numerador y
denominador, por área y agregada, sin dato individual.[^personas]

| Meta | Período | Denominador | Origen |
|---|---|---|---|
| Básico completado ≥90%, con evaluación práctica por rol | Cierre de los meses 1-3 | Dotación del básico, 60-70 personas (referencia ~65)[^tamano] | El 90% aparece en la ficha del mínimo solo como objetivo para dimensionar horas (se reservan 360-420 h para toda la población, no para el 90%);[^paquete-minimo] el instrumento lo define el Anexo D: aprobar un caso permitido del rol con revisión del resultado, aplicado antes del inicio del básico[^resoluciones] |
| Tecnología, uso activo semanal ≥80% | Meses 4-6 y sostenido en 7-9 | Personas de Tecnología según el padrón por área, con cobertura publicada | El 80% sale del resultado clave del OKR, que lo fija para **Operaciones y Tecnología juntas**;[^okr] aplicarlo a Tecnología por separado es una decisión del plan[^personas] |
| Tecnología, uso activo semanal ≥85% | Meses 10-12 | Ídem | Meta interna del Anexo D, sin ficha previa[^personas] |
| Operaciones habilitadas, uso activo ≥40% | Mes 6 (meta intermedia) | Personas de Operaciones **habilitadas** por la matriz de restricciones por cliente; se informa también sobre el total | Meta interna del Anexo D, sin ficha previa[^personas] |
| Operaciones habilitadas, uso activo ≥60% | Meses 10-12 | Ídem | Meta interna del Anexo D, sin ficha previa[^personas] |
| Pedidos con ejemplos del resultado esperado ≥30% | Meses 7-9 | Muestra agregada de prompts del chat | La base de ≤5% viene del análisis del piloto (n=12, solo chat);[^pilotos] el 30% es meta interna[^personas] |
| Staff, uso activo ≥50% | Meses 10-12 | Personas de staff según el padrón | Meta solo del Anexo D; hoy no hay fuente que mida chat ni Gemini[^personas] |

# Alcance: programa completo y mínimo

- **Básico ≥90% en el mes 3.** El mínimo reserva el básico para toda la población
  (60-70 personas, 360-420 h) y el plan lo lee en el mes 3.[^paquete-minimo] Se
  mide con el instrumento que fija R-21 del Anexo G:
  el CAIO lo aprueba antes de iniciar el básico (semana 5, o 9 si se amplía la
  base); dictado sin instrumento, el ≥90% queda «sin medir» y no se da por
  cumplido.[^resoluciones]
- **Metas de los meses 4-12 (programa completo).** Estas metas suponen intermedio ampliado (~50 personas),
  avanzado y champions con tiempo asignado,[^poblaciones] además de costeo y
  autorización adicionales a los del mínimo.[^personas]
- **Mínimo.** La continuación condicional de E no incluye nuevas cohortes,
  avanzado ni formación general adicional presupuestada,[^negocio] y el mínimo
  reserva básico para 60-70 personas e intermedio para 15-20, sin avanzado ni
  champions al 10%.[^paquete-minimo] En el mínimo las metas de los meses 4-12 se
  informan; no se prometen con ese techo.

# Qué no se debe confundir

- El **40% de Operaciones** de la ficha de poblaciones es el reparto supuesto de
  horas de básico e intermedio, no una meta de uso.[^poblaciones]
- El **40% de la cohorte** de los umbrales técnicos es el criterio de uso para
  extender la lectura de la prueba, otra métrica y otro denominador.[^umbrales]
- El **72,5%** del OKR combinado es el resultado aritmético de 85% y 60% con toda
  Operaciones habilitada: no es un máximo ni una predicción.[^personas]
- El **combinado original** del OKR se informa con su denominador completo, sin
  declararlo cumplido por el plan; si se revisa el resultado clave lo decide el
  Directorio en el mes 3 (R-23 del Anexo G).[^resoluciones]
- Las metas de adopción no equivalen a la hipótesis de throughput de la ficha de
  ganancia, que no es una meta.[^ganancia]

# Disparadores existentes

Las lecturas del Anexo F ya usan estos umbrales; esta ficha no los cambia ni
automatiza liberaciones.[^roadmap]

- Mes 3: básico ≥90% con evaluación práctica pasa; ≥50% y <90% se rediseña el
  formato; <50% se cambia el formato.
- Mes 6: Tecnología ≥80% mantiene; ≥60% y <80% rediseña la formación; <60% frena
  las horas de formación que no sean rediseño.

**En el mínimo**, esas lecturas llevan a rediseñar y recostear antes de comprometer
horas nuevas: la continuidad del mínimo no incluye formación general de los meses
4-12, no se usan sus horas para cubrir una remediación que no se costeó, y no hay
horas de formación M4-M12 que frenar. **Cortar o suspender horas de formación
ampliada** aplica solo si ese alcance fue costeado y autorizado aparte.

Los umbrales de 50% (básico) y 60% (Tecnología) son **propuestas del Anexo F y del
Anexo D**, que se citan entre sí: esa referencia cruzada no los valida. No hay
benchmark externo ni ficha humana firmada que los respalde; se ajustan con la línea
de base de los meses 1-3.

# Dependencias

- Línea de base prospectiva congelada en las semanas 1-4 (hasta 8 si se extiende)
  y definición de «activo» fijada por el Directorio, con el diccionario cerrado
  antes de congelarla; la medición semanal es la lectura oficial
  (R-23 del Anexo G).[^resoluciones]
- Matriz de restricciones por cliente, que da el denominador de Operaciones
  habilitadas: la completa Comercial para los clientes principales al cierre de
  los meses 1-3; sin ella no hay meta en Operaciones.[^resoluciones]
- Capacidad por persona y semana, y costeo del tramo, validados antes de
  comprometer horas.
- Tratamiento y retención de los eventos de uso por persona: los decide el
  Responsable de seguridad, con Personas y Legal externo consultados, antes de
  congelar la base (semana 1 de M1); sin esa decisión, la fuente queda «sin
  medir» (R-13 del Anexo G).[^resoluciones]

# Qué lo invalidaría

- Una línea de base que no permita medir uso activo con cobertura suficiente: la
  meta queda «sin medir» y no se convierte en inactividad.
- Que la matriz deje habilitada una fracción tan chica de Operaciones que el
  denominador pierda sentido.
- Que no haya capacidad ni autorización para el intermedio ampliado, el avanzado
  y los champions.

# Cautelas

- Es un supuesto de diseño del plan, escrito por un agente. Una revisión humana
  futura lo confirmaría como propuesta; no lo convierte en hecho ni en benchmark.
- Las metas de los meses 4-12 no están incluidas en el presupuesto ni en los
  techos del mínimo. El básico del mes 3 sí tiene horas costeadas en el mínimo y
  su instrumento está definido en el Anexo D; falta aplicarlo, antes del inicio
  del básico.[^resoluciones]
- La telemetría actual solo mide el agente de código: Tecnología se publica como
  proxy y no se extrapola a staff ni a Operaciones.
- El piloto de abril (n=12, autoseleccionado) da la base de ejemplos al pedir
  solo para el chat y no representa a la organización.[^pilotos]
- Las cifras son rangos y metas, no mediciones; se ajustan con la base de los
  meses 1-3.

[^okr]: Borrador de OKR de Tecnología 2027, objetivo de eficiencia operativa con IA: 80% o más de las personas de Operaciones y Tecnología con uso activo semanal.
[^paquete-minimo]: Paquete mínimo de aprendizaje, poblaciones del mínimo y reserva de horas del básico.
[^pilotos]: Encuesta y pilotos internos de IA, análisis de prompts del chat: ejemplos del resultado esperado en 5% o menos.
[^poblaciones]: Poblaciones y tiempos de capacitación en IA, programa completo y reparto supuesto de horas de Operaciones.
[^umbrales]: Umbrales técnicos propuestos por la arquitectura, impacto de extensión de la prueba.
[^ganancia]: Ganancia de productividad por IA en ingeniería, supuesto de throughput de 10% a 25%.
[^tamano]: Tamaño y estructura de la organización, dotación y pesos aproximados de las áreas.
[^personas]: Anexo D, hitos culturales, criterios de éxito, métricas de comportamiento y condiciones de abandono, como propuestas de diseño.
[^resoluciones]: Anexo G, resoluciones del Directorio: R-13 (datos de uso por persona), R-21 (formación del mínimo y evaluación del básico) y R-23 (definición de activo, metas y brecha del OKR).
[^roadmap]: Anexo F, gates de los meses 3 y 6 y sus disparadores de adopción.
[^negocio]: Anexo E, continuación condicional sin plataforma, no aprobada hoy.
