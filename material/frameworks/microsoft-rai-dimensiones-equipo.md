---
type: Concepto
title: Microsoft RAI MM, dimensiones de Team Approach
description: Las 10 dimensiones de enfoque de equipo (valoración, timing, motivación y 7 de colaboración interdisciplinaria) con lo que se pide en cada uno de los 5 niveles.
tags: [gobierno, madurez, ia-responsable, rubrica, cultura]
status: draft
sources:
  - id: ms-rai
    resource: Microsoft Responsible AI 2023.pdf
    title: "Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1, 17-may-2023; esta nota cubre las pp. 20-31 del PDF (numeración física; la impresa va uno menos)"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [Microsoft RAI Maturity Model](/frameworks/microsoft-rai-maturity.md). Anterior: [fundamentos organizacionales](/frameworks/microsoft-rai-dimensiones-fundamentos.md); siguiente: [RAI Practice](/frameworks/microsoft-rai-dimensiones-practica.md). Escala: [niveles](/frameworks/microsoft-rai-niveles.md).

# Qué es Team Approach

Son las dimensiones sobre cómo encaran los equipos el trabajo de RAI (cómo, por qué, con quién). Son fundamentales y suelen tener que estar para que haya progreso real en RAI Practice; además están condicionadas por Organizational Capacity y por Leadership and Culture. Gran parte cae bajo la colaboración interdisciplinaria, que se divide en elementos (motivación, timing) y en relaciones concretas (dentro del equipo, especialistas de RAI con equipos de producto).[^ms-rai]

**Quién evalúa (p. 20):** los equipos, porque la madurez refleja sus acciones y decisiones. Combinar evaluaciones de equipos da un promedio del departamento por dimensión (nunca entre dimensiones), pero los equipos de un mismo departamento pueden variar mucho, así que el esfuerzo se adapta por equipo. Una evaluación rápida pero menos robusta es que el jefe del departamento estime el nivel; es menos adecuada para un líder porque no ve de primera mano cosas como la colaboración dentro del equipo o la preparación de UX.[^ms-rai]

# Grupo A. Valoración, timing y motivación

## 6. Teams valuing RAI (p. 21)

Cuánto ven los equipos la necesidad e importancia de RAI. Sin adhesión genuina (creer que RAI es crítica para productos de calidad) hay pocas chances de madurar: la política y el cumplimiento obligan, pero hace falta motivación para ir más allá del mínimo. Una organización puede tener toda la capacidad y no avanzar si los equipos no usan los recursos.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Los equipos creen que RAI es un impedimento que baja la calidad, o ni la conocen / se sorprenden al enterarse. |
| 2 Emerging | Conocen RAI pero la ven como un impuesto que aporta poco valor. |
| 3 Developing | Empiezan a ver valor en RAI y cómo mejora la calidad del producto. |
| 4 Realizing | Creen en su valor y aprenden y refinan activamente su conocimiento. |
| 5 Leading | Aprecian a fondo RAI, se esfuerzan por implementarla en todas las etapas del ciclo y la defienden regularmente. |

## 7. Timing of RAI within the AI development and deployment lifecycle (p. 22)

Qué tan temprano o tarde en el ciclo se hace trabajo de RAI. Si se ignora hasta el final es tarde para mitigar; hay que considerarla desde el inicio, lo que además minimiza trabajo duplicado y pérdida de tiempo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No dedican tiempo a RAI en el ciclo; se topan con requisitos de RAI muy tarde, cuando creían haber terminado. |
| 2 Emerging | No la consideran temprano; le dedican tiempo en algún momento pero no al principio, con tiempo perdido y mucho retrabajo. |
| 3 Developing | La consideran temprano pero no incorporan temprano a las disciplinas de UX. |
| 4 Realizing | La consideran desde el inicio del ciclo y empiezan el trabajo de UX antes del desarrollo del modelo. |
| 5 Leading | La consideran en las etapas tempranas de ideación, antes de tener una idea de producto y antes de que arranque el ciclo; el trabajo previo de UX informa la idea de producto, lo que ahorra tiempo y retrabajo. |

## 8. Motivation for AI products (p. 23)

La inspiración y la razón de ser del desarrollo. Muchos productos de IA nacen del deseo de usar tecnología nueva (centrado en tecnología) en vez de necesidades de personas. El desarrollo maduro se centra en la gente y en el impacto en sociedad y ambiente; "a veces la acción más madura desde RAI es no construir el sistema".[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Centrado en tecnología: se prioriza o motiva por una tecnología nueva (p. ej. un modelo grande nuevo) o por la presión de integrar IA, no por una necesidad demostrada de las personas. |
| 2 Emerging | Motivado sobre todo por la tecnología; considera a las personas tarde o superficialmente, lo que dificulta identificar y abordar problemas de RAI. Si se detectan, se demora su abordaje indefinidamente o hasta un release futuro. |
| 3 Developing | Mismo punto de partida que el nivel 2, pero si se detectan problemas, se demora el lanzamiento para abordar al menos los mayores. |
| 4 Realizing | Centrado en las personas: motivado por sus necesidades y con balances cuidadosos entre negocio, experiencia, tecnología y prioridades de RAI. El resultado de la deliberación puede ser no construir si los daños superan los beneficios. |
| 5 Leading | Se basa en enfoques inclusivos, equitativos y potencialmente innovadores para entender las necesidades y el impacto en personas, sociedad y ambiente (diseño inclusivo, centrado en valores, participativo, design justice). |

# Grupo B. Colaboración interdisciplinaria

La colaboración es indispensable porque RAI no es un problema técnico con soluciones sólo técnicas: trata de impactos en personas y sociedad y exige expertos que entiendan a la gente, la sociedad y el contexto de aplicación (p. 24).[^ms-rai]

## 9. Sociotechnical approach (p. 24)

En qué medida los equipos encaran RAI desde una perspectiva sociotécnica y no sólo técnica; define qué trabajo se considera necesario, cómo, quién y cuándo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | RAI se ve como problema técnico con soluciones técnicas; los técnicos (ciencia de datos, ingeniería, gestión de proyecto) trabajan solos, sin considerar lo social ni traer expertos sociotécnicos (UX research, diseño). |
| 2 Emerging | Igual visión técnica; incorporan a UX muy tarde y sólo para trabajo superficial (p. ej. estética de la interfaz). |
| 3 Developing | RAI se ve en gran parte como técnica con algunas implicancias sociales; los técnicos hacen ellos mismos trabajo sociotécnico perfunctorio, sin involucrar a las disciplinas de UX. |
| 4 Realizing | RAI se ve como problema sociotécnico; se involucra a disciplinas con expertise sociotécnico (UX, antropología, sociología, lingüística) para abordarlo. |
| 5 Leading | RAI se ve como práctica sociotécnica; esas disciplinas participan desde el comienzo y moldean la estrategia de producto (si construir y qué construir). |

## 10. Common language (p. 25)

Que los distintos actores sepan que pueden no compartir vocabulario y construyan uno a propósito. Ejemplo del documento: "feature" es una variable de entrada para un data scientist y una función o capacidad del producto para UX o PM.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No tienen lenguaje común, no entienden el vocabulario de otras disciplinas, clientes ni consultores de RAI y no saben que se malentienden. |
| 2 Emerging | No se comunican bien pero reconocen que carecen de lenguaje común y que no están en la misma página. |
| 3 Developing | Alcanza para entenderse un poco y reconocer lo que no saben; algunas disciplinas se comunican bien (UX y front-end) pero poco entre todas. |
| 4 Realizing | Alcanza para conversaciones útiles; buscan activamente clarificar e invierten paciencia y curiosidad. |
| 5 Leading | Pueden dialogar entre disciplinas y traducir de una disciplina, grupo o cliente a otro; el diálogo respeta la expertise de cada una y no exige que todos sean expertos en todo. |

## 11. Collaboration within teams (p. 26)

Las interacciones entre los miembros de un equipo de producto o servicio al hacer RAI. Suele darse por supuesta, pero los equipos deben reflexionar y crear una cultura que permita trabajar bien juntos.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Falta diversidad de perspectivas; las disciplinas están en silos que no se hablan, mantenidas separadas por razones inválidas ("ahorrarles tiempo"); nadie tiene visión holística del producto, su razón de ser ni del trabajo de otras disciplinas. |
| 2 Emerging | Silos que hablan algo (sólo en hitos o puntos de integración, "tirando por encima del muro", o cuando hay un problema); sin visión holística. |
| 3 Developing | Disciplinas y perspectivas diversas en la sala, pero algunas no son escuchadas; visión parcial del producto y comprensión parcial del trabajo ajeno. |
| 4 Realizing | Discuten y deciden juntas; cada miembro tiene visión holística del producto, su razón de ser y el trabajo de otras disciplinas. |
| 5 Leading | Trabajan juntas desde el comienzo y en las decisiones más importantes (qué construir, roadmap, asignación de recursos); cada miembro tiene visión holística e influye en otras disciplinas, entiende cómo su trabajo impacta al de otras y sabe cuándo buscar su expertise. |

## 12. Non-UX disciplines' perceptions of UX (p. 27-28)

Cómo perciben los practicantes no-UX (ingeniería, gestión de proyecto, ciencia de datos) el rol de las disciplinas de UX (investigación, diseño, estrategia de contenido, redacción). Como RAI es sociotécnica, la participación de UX es crucial y puede ser inmadura si otros no la entienden ni valoran. Influye en Timing, Sociotechnical approach y Motivation, y a su vez depende de la preparación de UX en IA. Hay que mirar las discrepancias entre percepciones de UX y no-UX: indican oportunidades.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No entienden el valor de UX ni lo involucran en proyectos de IA. |
| 2 Emerging | Entendimiento estrecho: ven a UX como entregables reductivos (wireframes y mock-ups; testeo de usabilidad o validar supuestos). No se involucra a UX de forma significativa (investigación, estrategia de producto, arquitectura de información) para aportar nuevos insights o preguntas. Los practicantes de UX deben abogar y educar (p. ej. porque la investigación cualitativa se percibe como anecdótica y poco cuantificable). |
| 3 Developing | Perciben a UX como útil pero su trabajo como lento, así que lo hacen ellos creyendo que es más rápido. |
| 4 Realizing | Perciben a UX como valiosa con un rol amplio (insights cualitativos, nuevas preguntas, identificar riesgos); esos aportes y sus cambios, incluso sustanciales, se aceptan. |
| 5 Leading | Perciben a UX como par indispensable; entienden que incluye moldear estrategia y realizar valores morales y sociales más allá de usuarios y stakeholders inmediatos; respetan su trabajo y saben colaborar. |

## 13. UX practitioners' AI readiness (p. 29)

Qué tan preparados y con qué conocimiento están los practicantes de UX para trabajar con IA. Depende de Knowledge resources, Collaboration within teams y Teams working with RAI specialists; influye en Sociotechnical approach y en las percepciones de los no-UX.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Tratan la IA como un sistema tradicional determinista; usan métodos y herramientas tradicionales sin saber si la singularidad de la IA los vuelve imprecisos. |
| 2 Emerging | Aprecian la singularidad de la IA pero no saben cómo abordarla; no asumen que los métodos tradicionales sirvan y reconocen que necesitan aprender. |
| 3 Developing | Entienden algo su naturaleza probabilística y usan métodos propios de IA de forma ad hoc, no sistemática; pueden pasar por alto fallos y diseñar sólo para el camino feliz ("hero path"). |
| 4 Realizing | Tienen comprensión a nivel sistema, incluidas las implicancias de UX del trabajo de ciencia de datos (datasets de entrenamiento y prueba, recolección, elecciones del modelo, explicabilidad); los métodos específicos de IA están integrados al flujo de trabajo. |
| 5 Leading | Abordan UX de IA de forma sistemática y consistente (p. ej. con frameworks como el HAX Toolkit) e innovan en prácticas, guías, métodos y herramientas. |

## 14. RAI specialists working with product teams (p. 30)

Cómo los especialistas de RAI (expertos, consultores) encaran el trabajo con los equipos de producto cuando los asesoran. Deben fijar bien las expectativas de roles y responsabilidades al inicio, porque las primeras interacciones condicionan la receptividad. Se evalúa de forma independiente por ambas partes y luego se discute: los desacuerdos son oportunidad de mejora.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Fijan expectativas erróneas o irreales (p. ej. "hacemos justo tu sistema en una semana"); son alarmistas sobre los riesgos, con muchas o graves preocupaciones que llevan al pánico o a creer que hay que mitigar todo antes de lanzar. |
| 2 Emerging | Expectativas poco claras sobre quién responde por qué y los resultados (los equipos esperan que los especialistas hagan el trabajo, o asumen que la responsabilidad es sólo suya); abruman con preocupaciones y recomendaciones sin sintetizar, y los equipos pueden rendirse. |
| 3 Developing | Fijan expectativas claras (expertise, intención, naturaleza, resultados y responsabilidades) pero consideran sólo el trabajo de RAI del equipo y no otras presiones externas; muestran empatía y reconocen que RAI es nueva y difícil para todos. |
| 4 Realizing | Además de lo anterior, consideran otras presiones del equipo (se coordinan con otras áreas de cumplimiento, miran sus prioridades y fechas); son conscientes del conocimiento del equipo y hacen las cosas manejables (concisión, un punto de contacto, aclarar que no hace falta abordar cada riesgo). |
| 5 Leading | Documentan expectativas y acuerdos de trabajo y los revisan; interactúan como socios ("estamos del mismo lado"); enmarcan la relación como un recorrido a lo largo del ciclo del producto, no un esfuerzo único. |

## 15. Teams working with RAI specialists (p. 31)

La contracara: cómo interactúan los equipos de producto con los especialistas que los asesoran. También se evalúa en forma independiente por ambas partes y se discute luego.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Adversariales o sin involucrarse; no escuchan el input y comparten poco, sin dar acceso a quienes tienen el conocimiento que se necesita. |
| 2 Emerging | Defensivos o resistentes: rechazan el input y las tareas recomendadas; si se hace trabajo de RAI lo hacen los consultores, no el equipo; comparten muy poca o demasiada información, lo que impide entender la situación. |
| 3 Developing | Indiferentes o a medias: receptivos de forma pasiva (quieren que les digan qué hacer); esperan que les digan qué información compartir, lo que genera idas y vueltas y tiempo perdido. |
| 4 Realizing | Abiertos: abrazan el input, aprenden de RAI e implementan recomendaciones; comparten información adecuada y ponen un punto de contacto que conecta con las personas y recursos correctos (acceso a sistemas, telemetría, incidentes reportados). |
| 5 Leading | Forman verdaderas alianzas: identifican, entienden y abordan juntos los problemas; adaptan la información a la audiencia con el nivel de detalle apropiado y mantienen a los especialistas al día de los cambios. |

# Cautelas

* En Motivation for AI products, los niveles 2 y 3 comparten el primer párrafo en el original (p. 23); sólo difieren en qué pasa si se detectan problemas.
* La traducción es libre; los nombres oficiales de los niveles se mantienen en inglés.

[^ms-rai]: Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1 (17-may-2023), Microsoft Research, PDF pp. 20-31 (numeración física).
