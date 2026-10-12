---
type: Concepto
title: Microsoft RAI MM, dimensiones de RAI Practice
description: Las 9 dimensiones de práctica de RAI (accountability, transparencia externa e interna, identificar, medir, mitigar y monitorear riesgos, privacidad y seguridad de IA) con lo que se pide en cada uno de los 5 niveles.
tags: [gobierno, madurez, ia-responsable, rubrica, riesgo]
status: draft
sources:
  - id: ms-rai
    resource: Microsoft Responsible AI 2023.pdf
    title: "Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1, 17-may-2023; esta nota cubre las pp. 32-45 del PDF (numeración física; la impresa va uno menos)"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [Microsoft RAI Maturity Model](/frameworks/microsoft-rai-maturity.md). Anteriores: [fundamentos](/frameworks/microsoft-rai-dimensiones-fundamentos.md) y [Team Approach](/frameworks/microsoft-rai-dimensiones-equipo.md). Escala: [niveles](/frameworks/microsoft-rai-niveles.md).

# Qué es RAI Practice

Son las dimensiones sobre cómo los equipos hacen trabajo concreto de RAI, normalmente al servicio de objetivos como equidad, inclusión y confiabilidad y seguridad. Cumplirlos exige identificar, medir, mitigar y monitorear riesgos. Son lo más visible, pero están moldeadas por Organizational Foundations y Team Approach; a su vez, la madurez en práctica permite a los practicantes empujar la de su equipo y organización.[^ms-rai]

**Quién evalúa (p. 32):** los equipos; el promedio por departamento sirve por dimensión (no entre dimensiones) y el esfuerzo se adapta al equipo, al tipo de sistema de IA y al dominio de despliegue.[^ms-rai]

# 16. Accountability (p. 33)

Hacerse cargo de mitigar daños en productos, funciones y sistemas de IA. La organización responde ante los usuarios finales y también ante los clientes que usan y despliegan los sistemas que construye. Se evalúa a nivel organización.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | La organización no asume responsabilidad por mitigar daños. |
| 2 Emerging | Responsabilidad mínima: documentación de RAI y descargos superficiales; delega en los usuarios finales vigilar daños o usar el sistema sólo como está aprobado; delega en los clientes que despliegan poner supervisión humana y hacer las pruebas de última milla sin guía adicional. |
| 3 Developing | Asume alguna responsabilidad: reconoce los límites de la supervisión humana y da documentación detallada (p. ej. Transparency Notes); no tiene políticas de accountability de RAI; puede usar compuertas o controles del sistema para limitar y rastrear despliegues y evitar usos dañinos; identifica y documenta a los responsables de resolver problemas, gestionar, operar, supervisar y controlar el sistema durante y después del despliegue. |
| 4 Realizing | Comparte la responsabilidad con usuarios y clientes: da guía y formación sobre supervisión humana para que gestionen daños y fallas; tiene políticas de accountability de RAI; cuando es posible incorpora mitigaciones al sistema y lo diseña para evitar fallas. |
| 5 Leading | Comparte la responsabilidad y además define y documenta los métodos (y métricas) para evaluar si los stakeholders pueden cumplir realistamente las funciones de supervisión (o guía al tercero responsable de evaluarlas); tiene un plan documentado para gestionar fallas previamente desconocidas (rollback de funciones y sistema, procesos de actualización del modelo, aviso a usuarios y clientes). |

# Transparencia (p. 34)

Ser abierto con la información necesaria para entender los sistemas de IA. Desde RAI no es sólo documentar datos técnicos (datasets, modelos, benchmarks) sino también limitaciones conocidas, daños potenciales y usos inapropiados.[^ms-rai]

## 17. External transparency (p. 34-35)

Compartir públicamente información del sistema con usuarios, clientes y stakeholders para comunicar capacidades, limitaciones y riesgos, mediante transparency notes, model o system cards, tutoriales, documentación online, FAQs y textos de UI. Se evalúa a nivel organización y equipo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No comparte información del sistema o sólo documentación técnica; puede no ser obvio que se usa IA. |
| 2 Emerging | Comparte información técnica (funcionalidad, instrucciones) sin información de RAI ni consideraciones sociotécnicas; la información no está integrada a la UI y el usuario debe buscarla; es difícil de encontrar (sólo en documentación aparte). |
| 3 Developing | Comparte información técnica y de RAI, pero la de RAI es genérica y conceptual; en la UI se integra información genérica en unos pocos puntos clave y también está en la documentación. |
| 4 Realizing | Comparte información técnica y consideraciones específicas de RAI (limitaciones conocidas, daños potenciales, uso responsable); en la UI se integra información específica en unos pocos puntos clave; también está en documentación y otros formatos (tutoriales, notebooks, videos) y es fácil de acceder. |
| 5 Leading | Transparencia apropiada: adapta comunicaciones a la audiencia y evalúa su efectividad; la información está integrada a toda la experiencia (p. ej. explicaciones disponibles de los resultados, en lenguaje sencillo); ofrece mecanismos para que cualquier stakeholder dialogue o pregunte; la transparencia es una interacción continua y la información se actualiza a medida que el sistema evoluciona. |

## 18. Internal transparency (p. 35-36)

Documentar sistemáticamente diseño, desarrollo y funcionamiento para asegurar auditabilidad, colaboración, reflexión sobre riesgos y transparencia externa; con código y documentación del sistema, impact assessments, datasheets for datasets, diagramas de arquitectura y model cards. Se evalúa a nivel organización y equipo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Sin requisitos ni guía de qué documentar; algo queda en mails, reuniones, presentaciones; parte depende de la memoria de las personas, y si alguien se va del proyecto se pierde información. |
| 2 Emerging | Sin requisitos ni guía; algo se documenta a nivel equipo, según necesidad y de forma inconsistente en la organización. |
| 3 Developing | Recomienda documentar activos de IA y ofrece plantillas (Impact Assessments, Datasheets for Datasets, Model Cards) pero casi nada es obligatorio; hay documentación estandarizada pero inconsistente, incompleta y difícil de encontrar; se crea hacia el final del ciclo. |
| 4 Realizing | Requisitos, plantillas, guía y recursos claros; hay documentación estandarizada pero no integrada del todo a pipelines, flujos y herramientas; se crea algo a lo largo del ciclo, aún sin consistencia; es suficiente para auditar. |
| 5 Leading | Integra la documentación requerida en pipelines, flujos y herramientas; se documenta de forma consistente y actualizada; captura decisiones de diseño y desarrollo, justificaciones y supuestos, y consideraciones de RAI (limitaciones, usos soportados y no soportados, evaluaciones de equidad); se usa para decidir y facilita la colaboración entre equipos (reuso de modelos, datasets, mitigaciones) y la auditoría; los requisitos y plantillas de la organización son adoptados por otros en la industria e informan estándares y políticas. |

# Identificar, medir, mitigar y monitorear riesgos (p. 37)

"Identify, measure, mitigate" es el marco recomendado para abordar riesgos de RAI; monitorear completa el ciclo.[^ms-rai]

## 19. Identifying RAI risks (p. 37-38)

Determinar riesgos y problemas propios del sistema, sus usos, stakeholders y contextos de despliegue; suele ser el primer paso. Riesgos de equidad, confiabilidad, seguridad, privacidad. Incluye impact assessments, involucramiento de stakeholders y red teaming.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Falta conciencia de qué es un riesgo de RAI; los riesgos o daños los levantan sólo terceros (auditores, prensa, empleados nuevos). |
| 2 Emerging | Identifican riesgos de forma ad hoc, sin investigaciones específicas (alguien tropieza con el problema). |
| 3 Developing | Investigaciones ad hoc (mirar datos "a ojo", especular, hacer impact assessments ocasionales); razonan algo sobre riesgos sin involucrar a los afectados; pueden no poder priorizar riesgos ni gestionar trade-offs, con riesgo de parálisis (como un sistema perfecto es inalcanzable, descartan los requisitos de RAI: pensamiento de todo o nada). |
| 4 Realizing | Investigaciones sistemáticas con prácticas establecidas como el impact assessment, informadas por stakeholders; conocen riesgos, beneficios y requisitos de negocio pero les cuesta priorizar y gestionar trade-offs. |
| 5 Leading | Plan documentado y estructurado (impact assessment) integrado al ciclo; razonamiento basado en compromiso profundo con stakeholders, apoyándose en expertos sociotécnicos (UX research); análisis costo-beneficio profundo y basado en datos para priorizar y balancear riesgos, beneficios y requisitos de negocio; actualizan y revisan el impact assessment al menos una vez por año, al sumar nuevos usos previstos y antes de pasar a una nueva etapa de release (objetivo A1.3 del Microsoft RAI Standard v2). |

## 20. Measuring RAI risks (p. 38-39)

Evaluar la extensión o severidad de los riesgos ya identificados, de forma cuantitativa, cualitativa o mixta; ayuda a entender, priorizar y seguir el progreso de mitigación. Implica recolectar datos, usar herramientas, colaborar con expertos de RAI y del dominio y definir métricas alineadas a producto o función.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No miden riesgos específicos de RAI; usan métricas generales, agregadas y mayormente offline (p. ej. accuracy); consideran a los stakeholders sólo según necesidades básicas de negocio y quizá no a los expuestos a riesgos de RAI. |
| 2 Emerging | Miden sólo algunos riesgos (p. ej. daños de calidad de servicio), ad hoc; usan datos existentes, saben de sus limitaciones (adecuación al propósito, representatividad) pero no pueden cuantificarlas ni resolverlas con más datos; miden fallas predecibles (falsos positivos y negativos) y analizan su impacto en stakeholders. |
| 3 Developing | Miden varios riesgos (fallas conocidas, calidad de servicio, modelado de amenazas de seguridad) y empiezan a reconocer las dificultades (cuantificar daños de representación); a veces recolectan datos adicionales ad hoc e intentan cuantificar o abordar las limitaciones del dataset; usan enfoques que van más allá de lo predecible (evaluación agregada vs. desagregada, herramientas de RAI); se apoyan en literatura pero rara vez validan con expertos de RAI. |
| 4 Realizing | Plan de evaluación documentado con mediciones, métricas y tipos de error, que incluye enfoques cuantitativos y cualitativos de evaluación de daños; recolectan datos adicionales como parte de una estrategia; amplia gama de enfoques (medir sobre varias poblaciones) con foco en reproducibilidad; van a la causa raíz (representatividad de datos vs. límites del modelo); trabajan con expertos de RAI y mejores prácticas (evaluación desagregada, RAI Dashboard y Toolbox) y buscan nuevas formas de medir (tolerancias de error por caso de uso); trabajan con expertos del dominio (p. ej. médicos en salud) y ven cómo varían los factores entre grupos. |
| 5 Leading | Miden riesgos regularmente como parte del monitoreo; tienen un proceso para refrescar y retirar datos (¿sigue siendo representativo ante nuevos stakeholders, cambios de modelo y funciones?); reflexionan y mejoran sus prácticas de medición; trabajan además con miembros de los grupos demográficos identificados para entender riesgos e impactos (p. ej. disparidades de desempeño). |

## 21. Mitigating RAI risks (p. 40)

Elegir la estrategia correcta para abordar riesgos ya identificados y medidos, antes y después del despliegue. Hay mitigaciones técnicas (cambiar parámetros, más datos) y otras como intervenciones de diseño UX/UI o documentación de RAI. Requiere entender trade-offs, emparejar estrategias con riesgos en distintas etapas y priorizar daños.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Pueden aplicar técnicas de mitigación sin medir los riesgos, lo que potencialmente causa más daño. |
| 2 Emerging | Mitigan guiados por una identificación y medición incompletas (p. ej. buscar más representatividad de datos sin considerar los grupos y daños específicos). |
| 3 Developing | La elección está guiada por una identificación y medición más completas, pero no logran emparejar de forma óptima mitigación con riesgo ni aplicarla en la etapa óptima; la estrategia puede no ser la más efectiva pero no genera más daño. |
| 4 Realizing | Elección guiada por comprensión profunda de riesgos y trade-offs entre estrategias; emparejan de forma óptima; el foco se limita a 1-2 etapas del ciclo de ML y/o no tienen monitoreo que les permita identificar riesgos de manera continua. |
| 5 Leading | Igual comprensión profunda y emparejamiento óptimo, considerando mitigaciones en cada etapa del ciclo; sabiendo que no se pueden identificar y mitigar todos los riesgos para todos los grupos, tienen monitoreo y una estrategia de priorización documentada que ajustan periódicamente. |

## 22. Monitoring RAI risks (p. 41-42)

Seguimiento de sistemas y funciones posdespliegue para detectar riesgos de equidad, confiabilidad y seguridad, seguridad informática e interacción humano-IA. Monitorear latencia es común; monitorear RAI exige además definir la postura de seguridad (safety posture), controlar sobredependencia de la IA, usar telemetría extensible y hacer pruebas adversariales continuas.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No monitorean activamente; dependen de señales externas como reportes de usuarios, que quizá no se revisan sistemáticamente. |
| 2 Emerging | Monitoreo ad hoc (si un cliente señala un problema, a veces investigan manualmente); algunas pruebas offline (probing manual, tests del modelo); monitorean sobre todo garantías de desempeño (latencia, disponibilidad, SLAs como latencia < 300 ms). |
| 3 Developing | Enfoque proactivo (telemetría diseñada temprano en el pipeline), revisan redes sociales y reportes de usuarios de forma sistemática; empiezan a discutir riesgos específicos (qué significan confiabilidad y seguridad en su contexto, su postura de seguridad); monitorean sobre todo garantías de desempeño y, en menor medida, algunos daños posteriores (sobredependencia, degradación del modelo, uso fuera de contexto, daños de equidad). |
| 4 Realizing | Enfoque sistemático (marcos de telemetría, formas claras de incorporar aprendizajes del feedback y la telemetría al diseño, procesos de conciencia de fallas); análisis sistemático de riesgos (daños de equidad, data poisoning, sobredependencia), metas de medición claras (p. ej. en las safety specs) y formas de mostrar que se lograron; monitorean no sólo el daño sino también fallas imprevistas (compatibilidad hacia atrás, usos no previstos, vectores de ataque de caja negra). |
| 5 Leading | Enfoque sistemático y escalable con planes predefinidos de falla (apagar o reemplazar componentes de ML), telemetría extensible (medidas nuevas rápido) y nuevas formas de monitoreo específico de IA (p. ej. telemetría "eyes-off"); analizan la superficie de amenaza de RAI y definen la safety spec de forma interdisciplinaria (qué significa seguridad para negocio, cliente y usuario); hacen pruebas internas continuas (testeo adversarial, red teaming, bug bashing) para identificar y mitigar riesgos de forma proactiva. |

# AI privacy and security (p. 43-45)

La IA plantea desafíos propios de privacidad y seguridad; la práctica madura los aborda en lugar de apoyarse en enfoques tradicionales. Ambas dimensiones complementan, no reemplazan, los modelos de madurez existentes de privacidad y seguridad (ver apéndice del PDF); una organización puede ser muy madura en lo tradicional y menos en lo específico de IA, pero la alta madurez en IA exige alta madurez tradicional.[^ms-rai]

## 23. AI privacy (p. 43-44)

Identificar, medir y mitigar riesgos de privacidad propios de la IA, como identificación de miembros por filtrado del modelo, memorización de datos de entrenamiento y aprendizaje federado; complementa frameworks como el Privacy Standard de Microsoft. Se evalúa a nivel organización y equipo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Equipos y personal de privacidad entienden bien la privacidad general pero no los riesgos específicos de IA; los procesos de privacidad (revisiones, modelado de amenazas, respuesta a incidentes) cubren requisitos legales generales pero no los riesgos de IA. |
| 2 Emerging | Conocen riesgos específicos (identificación por filtrado del modelo, memorización, ingeniería inversa de prompts) pero no tienen conocimiento, guía, procesos ni recursos para identificarlos, medirlos y mitigarlos. |
| 3 Developing | Conocen los riesgos y usan algunas mitigaciones (privacidad diferencial, aprendizaje federado, datos sintéticos), pero sin guía clara la elección puede no ser óptima (p. ej. usar privacidad diferencial porque saben que ayuda, sin evidencia de que aborde los riesgos específicos); aparecen bolsillos de expertise en privacidad de IA, pero se maneja caso por caso y depende de los pocos expertos. |
| 4 Realizing | Conocen una amplia gama de medios para identificar, medir y mitigar, y discuten críticamente que haya correspondencia entre metas, riesgos y mitigaciones; la organización empieza a desarrollar políticas, guía y requisitos específicos; aunque no haya procesos formales, documentan sus decisiones, lo que habilita auditoría. |
| 5 Leading | Construye sobre proyectos previos guía y prácticas reutilizables e integra la privacidad de IA a sus procesos de privacidad; sus expertos hacen avanzar el estado del arte (investigación, guía, herramientas); el personal de privacidad anticipa cambios regulatorios y consulta a instituciones y organismos sobre regulaciones de privacidad de IA. |

## 24. AI security (p. 44-45)

Identificar, medir y mitigar riesgos de seguridad propios de la IA (evasión de modelos, ataques adversariales y lo que recogen frameworks específicos como MITRE ATLAS); complementa los frameworks de seguridad existentes. Se evalúa a nivel organización y equipo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Entienden bien los riesgos de seguridad generales pero no los específicos de IA. |
| 2 Emerging | Les preocupan los temas de seguridad de IA pero aplican metodologías tradicionales como el Security Development Lifecycle (SDL). |
| 3 Developing | No dan por supuesto que los procesos existentes (SDL) cubran todo: conocen algunos riesgos adversariales (evasión del modelo) que requieren mitigaciones específicas; pueden dar pasos ad hoc (red teaming para evaluar mitigaciones). |
| 4 Realizing | Procesos para temas de seguridad de IA (el SDL incluye riesgos adversariales; el proceso de respuesta a incidentes incorpora ataques adversariales); empiezan a medir y monitorear su postura (cuántos servicios corren modelos de IA, procedencia de los modelos, cuántos pasaron modelado de amenazas con amenazas adversariales); usan frameworks como MITRE ATLAS para modelar amenazas por etapa. |
| 5 Leading | Pruebas adversariales exhaustivas y modelado de amenazas integrados al pipeline, regulares (p. ej. ante cambios sustanciales del modelo), a escala y con herramientas automáticas (p. ej. Counterfit); entienden la naturaleza evolutiva de las amenazas y las detectan y responden en tiempo razonable; su guía, procesos, frameworks y herramientas son adoptados por otros en la industria e informan estándares y políticas. |

# Cautelas

* La tabla de External transparency salta de página (pp. 34-35) y los textos de varios niveles quedan cortados en el límite; la frase del nivel 5 "explicaciones de... resultados" se reconstruyó uniendo las dos mitades (la palabra que une ambos tramos no es legible en el PDF).
* Mitigating, nivel 4: el original lista las limitaciones del nivel (foco sólo en 1-2 etapas y/o falta de monitoreo continuo) como lo que lo separa del nivel 5.

[^ms-rai]: Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1 (17-may-2023), Microsoft Research, PDF pp. 32-45 (numeración física).
