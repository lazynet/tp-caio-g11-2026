---
type: Framework
title: Rúbrica del Corrector IA del TP Final (guía docente v2)
description: Rúbrica formativa propuesta por el equipo docente para el Corrector IA del Plan Maestro, con siete criterios ponderados, escala 0-4, anclas por nivel, controles de revisión y fórmula de la nota orientativa.
tags: [evaluacion, rubrica, tif, plan-maestro, defensa]
status: draft
sources:
  - id: guia
    resource: GUIA_CORRECCION_CAIO_v2.md
    title: "Guía docente de referencia para el Revisor del Plan Maestro CAIO, versión de funcionamiento 2.0, rúbrica propuesta v1.0 (aula virtual UTN BA, actividad 'Corrector IA TP Final :: Plan Maestro')"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-20T23:45:00Z }
---

# Qué es

La guía la escribió el equipo docente para configurar el **Corrector IA del TP
Final**, el asistente del aula virtual que devuelve feedback orientativo sobre el
Plan Maestro.[^guia] Se usa junto con un prompt base
(`Prompt_base_Revisor_CAIO.txt`) que no está accesible para el equipo (ver
[huecos](/huecos.md)).

La rúbrica es una **propuesta formativa**, no la regla oficial de aprobación: una
rúbrica oficial del docente la reemplaza, y la evaluación final es de los
docentes.[^guia] Igual es la mejor aproximación disponible a cómo se va a leer el
plan, y por eso la usan `board` y el skill `board-review`.

# Criterios y pesos

| Criterio | Peso | Qué observa |
|---|---|---|
| C1. Alcance, estrategia y aplicación al caso | 20% | Alcance y objetivos comprensibles; relación entre necesidad de negocio y plan; aplicación pertinente de los contenidos |
| C2. Arquitectura, gobierno, seguridad y people plan | 20% | Las cuatro dimensiones desarrolladas, coherentes entre sí y con el alcance y la estrategia |
| C3. Roadmap integrado a 12 meses | 15% | Recorrido técnico, financiero y cultural; hitos, dependencias y criterios de éxito; consistencia con capacidades y recursos |
| C4. Finanzas y financial storytelling | 15% | Costos, beneficios, supuestos y respaldo; cálculos consistentes; decisión clara para el CFO |
| C5. Escenarios, contingencias y reversibilidad | 10% | Riesgos aplicados; escenarios que cambian el plan; respuestas; reversible e irreversible justificados |
| C6. Preparación de la defensa | 10% | Storyline, objeciones relevantes, evidencia para abordarlas; qué se quiere que el board decida |
| C7. Síntesis ejecutiva y trazabilidad a anexos | 10% | Presentación centrada en decisiones; legibilidad funcional; anexos separados y vinculados |

Fuente de la tabla: [^guia], sección M03.

# Escala

* **0, sin evidencia:** el componente está ausente, y solo se asigna después de revisar el TP completo y los anexos.
* **1, inicial:** hay menciones o fragmentos, pero no alcanzan para comprender una propuesta aplicada.
* **2, en desarrollo:** propuesta aplicada, con vacíos, contradicciones o respaldo insuficiente.
* **3, logrado:** comprensible, coherente y respaldada en lo necesario para el alcance.
* **4, integrado:** el nivel 3 más relaciones explícitas entre componentes y razonamiento sobre alternativas, restricciones o consecuencias.
* **NE, no evaluable:** faltan archivos, materiales o acceso. No es 0 ni penaliza.[^guia]

# Anclas por criterio

| | Nivel 1 | Nivel 2 | Nivel 3 | Nivel 4 |
|---|---|---|---|---|
| C1 | Objetivos genéricos o alcance confuso | Caso definido, conexión parcial entre necesidad, objetivos y estrategia | Alcance, objetivos y estrategia conectados por aplicación pertinente | Además justifica elecciones y restricciones con evidencia y consecuencias |
| C2 | Lista términos sin explicar su uso | Algunas dimensiones débiles o desconectadas | Las cuatro dimensiones aplicadas y compatibles | Además explicita cómo dependencias y decisiones sostienen estrategia y roadmap |
| C3 | Calendario o lista sin recorrido integrado | Faltan vínculos, hitos o criterios de éxito | Tres recorridos integrados con hitos, dependencias y criterios coherentes | Además explica cómo evidencia y restricciones orientan avanzar o ajustar |
| C4 | Cifras o promesas sin lógica | Estimaciones interpretables con respaldo o argumento incompleto | Costos, beneficios y supuestos trazables; cálculos coherentes; decisión clara | Además conecta supuestos y limitaciones con roadmap, riesgos y decisión |
| C5 | Riesgos genéricos o escenarios sin consecuencias | Contingencias o reversibilidad parciales | Escenarios, contingencias y reversibilidad justificados y conectados | Además muestra qué señales llevan a cada respuesta y su impacto en el recorrido |
| C6 | Narrativa sin objeciones ni respaldo | Storyline y alguna objeción, con evidencia o decisión débiles | Argumento coherente, objeciones pertinentes, evidencia localizable | Además prioriza la conversación ejecutiva y explicita límites o alternativas |
| C7 | Acumulación que esconde las decisiones | Comprensible con sobrecarga o vínculos débiles | Síntesis centrada en decisiones, anexos vinculados y localizables | Además cada parte aporta a la decisión con respaldo fácil de consultar |

Fuente: [^guia], sección M03. Las anclas no agregan marcos, cantidades ni
entregables obligatorios.

# Nota orientativa

`Nota / 10 = Σ(peso × nivel) / 40`, con pesos 20, 20, 15, 15, 10, 10 y 10. Con
`S = Σ(peso × nivel)` entre 0 y 400, se comprueba que `S / 40` coincida con
`(S / 100) × 2,5`. Todos 2 da 5,0; todos 3 da 7,5; `S = 270` da 6,8.[^guia]

* Solo se emite con los siete criterios evaluables, revisión completa y un cálculo
  determinista (código). Sin eso, van los niveles fundamentados sin nota.
* Con un criterio NE o una revisión parcial no hay nota global ni se renormalizan
  los pesos: se informa la cobertura (suma de pesos evaluados sobre 100).
* No hay umbral de aprobación ni se traduce a aprobado o desaprobado.[^guia]

# Controles de revisión que exige la guía

* **Antes de declarar una ausencia**, buscar sinónimos en slides y anexos (costos,
  presupuesto, inversión; beneficio, ahorro, capacidad, ROI; escenario,
  sensibilidad; reversible, costoso de deshacer, salida). Si está pero es débil,
  se dice qué no queda demostrado; no se declara ausente.[^guia]
* **Números:** suma de partidas contra el total y los tramos; porcentajes con el
  denominador correcto (de 8 a 6 es -25%; de 6 a 8 es +33,3%); ROI simple =
  beneficio neto / costo en el mismo período; escenario adverso que puede dar
  negativo; capacidad liberada, gasto evitado, margen y valor esperado no son
  caja automáticamente.[^guia]
* **Contradicciones:** se localizan los dos pasajes (promesa ejecutiva y anexo,
  gate y cronograma, control declarado y operación, defensa y escenarios).[^guia]
* **Clasificación de hallazgos:** error verificable, contradicción interna,
  evidencia insuficiente, aclaración necesaria, sugerencia opcional y contenido
  inaccesible se mantienen separados. Una sugerencia no es un error.[^guia]
* **Prioridades:** máximo tres en la devolución, por impacto en la decisión, el
  presupuesto, la habilitación o la defensa; sin inventar problemas para
  completar tres.[^guia]

# Qué no premia ni exige (M10)

* No exige herramienta, metodología, comité, organigrama, cantidad de champions
  ni formato de roadmap salvo que la consigna lo pida.[^guia]
* No premia cantidad de tecnologías, iniciativas, presupuesto ni diseño vistoso.[^guia]
* Admite caso ficticio y cifras estimadas si se entiende su origen y lógica.[^guia]
* El límite de 10 slides es un máximo y no excluye la portada del cómputo.[^guia]

# Cautelas

* Es la versión 2.0 de la guía y la v1.0 de la rúbrica; los docentes pueden
  cambiarla. Una rúbrica oficial la reemplaza.
* Falta el prompt base, que según la guía conserva los controles críticos y el
  formato de respuesta.
* El Corrector IA cita también "M3-U4 Fundamentos para la Presentación de un Plan
  Maestro", que no está en `material/` (ver [huecos](/huecos.md)).
* La regla del repo es más estricta que la guía: para entrega, toda cifra remonta
  a una ficha `verified`. La guía acepta estimaciones con lógica comprensible.
* Extracto de la guía docente; el texto completo no se versiona.

[^guia]: Equipo docente, *GUIA_CORRECCION_CAIO_v2*, Diplomatura CAIO UTN BA, 2026. Secciones M02 a M12.
