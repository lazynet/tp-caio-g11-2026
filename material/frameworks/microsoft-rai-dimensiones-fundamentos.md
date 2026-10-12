---
type: Concepto
title: Microsoft RAI MM, dimensiones de Organizational Foundations
description: Las 5 dimensiones de fundamentos organizacionales (liderazgo y cultura, política, procesos de cumplimiento, recursos de conocimiento y herramientas) con lo que se pide en cada uno de los 5 niveles.
tags: [gobierno, madurez, ia-responsable, rubrica]
status: draft
sources:
  - id: ms-rai
    resource: Microsoft Responsible AI 2023.pdf
    title: "Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1, 17-may-2023; esta nota cubre las pp. 13-19 del PDF (numeración física; la impresa va uno menos)"
  - id: ms-rai-web
    resource: https://www.microsoft.com/en-us/research/publication/responsible-ai-maturity-model/
    title: Ficha de la publicación en Microsoft Research (MSR-TR-2023-26), consultada 2026-10-11
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [Microsoft RAI Maturity Model](/frameworks/microsoft-rai-maturity.md). Los niveles se leen según [la escala](/frameworks/microsoft-rai-niveles.md); la ficha oficial de la publicación está en Microsoft Research;[^ms-rai-web] las otras categorías están en [Team Approach](/frameworks/microsoft-rai-dimensiones-equipo.md) y [RAI Practice](/frameworks/microsoft-rai-dimensiones-practica.md).

# Qué son los fundamentos organizacionales

Son las dimensiones que atañen a la empresa entera y dependen de decisiones del liderazgo senior, que muchas veces es el único que puede moverlas. Suelen tener que estar en su lugar para que avancen Team Approach y RAI Practice.[^ms-rai] Se subdividen en Leadership and Culture y Organizational Capacity (que agrupa Governance —política y cumplimiento—, Knowledge resources y Tooling).[^ms-rai]

**Quién evalúa:** el equipo de liderazgo senior y los equipos, para ver cómo se vive en el terreno cada decisión del liderazgo; las diferencias de percepción son una señal de oportunidad de mejora (p. 13).[^ms-rai]

**Organizational Capacity** reúne lo que le da a los equipos la capacidad de hacer trabajo de RAI. Las tres dimensiones suelen depender entre sí: la política facilita crear recursos de conocimiento, los recursos de conocimiento ayudan a las herramientas, y las herramientas habilitan los procesos de cumplimiento (p. 15).[^ms-rai]

**Governance** es la existencia de políticas formales (RAI Policy, p. ej. el RAI Standard de Microsoft) más la infraestructura y las prácticas para cumplirlas (RAI compliance). Da a los equipos guía, procesos y sistemas para implementar las dimensiones de RAI Practice y habilita la madurez en Accountability (p. 15).[^ms-rai]

# 1. Leadership and Culture (p. 13-14)

Mide cuánto priorizan RAI el liderazgo y la cultura, es decir, hasta dónde los valores de RAI se traducen en recursos e incentivos. Las acciones de los líderes señalan qué se valora y se premia; su priorización en las decisiones habilita a los equipos a practicar RAI con madurez.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Puede haber mensajes generales sobre RAI, pero: la cúpula (C-suite) no la considera al decidir ni le asigna recursos (sin presupuesto para herramientas, consultoría con expertos, formación, datos representativos ni headcount); no se incentiva el trabajo de RAI; la gerencia no adhiere (no cambia decisiones ni conducta para alinearse con los valores de RAI). |
| 2 Emerging | La organización declara que valora RAI (mensajes, principios), pero: la cúpula no la considera ni asigna presupuesto o headcount; no hay incentivos; la gerencia no reserva tiempo de RAI en el ciclo de desarrollo y despliegue; el trabajo, si existe, lo empujan pocas personas apasionadas. |
| 3 Developing | Declara que valora RAI, y: la cúpula prioriza algunos aspectos (p. ej. equidad, transparencia) pero no otros (confiabilidad y seguridad, accountability); hay algunos recursos para arrancar; se alienta pero no se incentiva; la gerencia invoca valores en competencia y presión por entregar para justificar no priorizar; el trabajo lo empujan equipos apasionados en "bolsillos" de la organización. |
| 4 Realizing | RAI se valora y prioriza: la cúpula la considera en decisiones y asignación de recursos (formación, gobierno, infraestructura, expertos); hay inversión planificada a largo plazo (headcount y presupuesto para práctica, investigación y educación); algunos equipos están incentivados, posiblemente con compromisos explícitos, indicadores de desempeño y reconocimiento gerencial. |
| 5 Leading | RAI está integrada plenamente: es parte del negocio habitual y requisito de los sistemas de IA. No se lanzan productos si no se atienden al menos los riesgos mayores conocidos (p. ej. daños de equidad). La cúpula fija compromisos e indicadores claros de RAI; la organización incentiva a todos los equipos de IA a priorizarla. |

# 2. RAI policy (p. 16)

Son los requisitos y lineamientos de cumplimiento para los productos de IA. Una política bien definida habilita accountability al formalizar requisitos y dar un punto de referencia para detectar desvíos; además es buen punto de partida para quien tiene pocas prácticas.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No hay políticas internas de RAI. |
| 2 Emerging | Se está armando una política interna unificada. Pueden existir políticas para algunos aspectos (equidad, privacidad) pero fragmentadas. |
| 3 Developing | Hay una política interna de RAI, apoyada en alguna documentación que explica la política y cómo implementarla; la documentación es de alto nivel y no cubre todo lo necesario. |
| 4 Realizing | La política es rigurosa (basada en evidencia empírica e investigación), integral y auditable; se actualiza continuamente según lo aprendido al aplicarla; la documentación es completa pero puede faltar profundidad para implementar (p. ej. prácticas detalladas para medir algunos daños). |
| 5 Leading | La política es tan avanzada que informa políticas externas (estándares, leyes, regulaciones); se concilia con el resto de las políticas y procesos de gobierno de la empresa (RAI, privacidad, seguridad se integran y se eliminan redundancias); la documentación está integrada en procesos y herramientas, con mecanismos para mantenerla al día e incorporar conocimiento nuevo. |

# 3. RAI compliance processes and infrastructure (p. 17)

Prácticas, procedimientos y estructuras internas para facilitar el cumplimiento de la política: guías para evaluaciones de riesgo (p. ej. impact assessments), plantillas de documentación obligatoria (transparency notes) y procesos para reportar y revisar usos de alto riesgo.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No hay proceso ni infraestructura de cumplimiento específicos de RAI. Ejemplo: no hay proceso estructurado para que los empleados reporten daños. |
| 2 Emerging | Procesos en planificación; el trabajo de cumplimiento (p. ej. revisiones de RAI) es manual, ad hoc y sin infraestructura. Ejemplo: proceso informal de reporte de daños. |
| 3 Developing | Los procesos varían mucho entre unidades; la infraestructura es fragmentada. Ejemplo: proceso estructurado de reporte de daños (p. ej. para usos de alto riesgo, a nivel empresa). |
| 4 Realizing | Procesos aceptados y homogéneos en toda la organización; la infraestructura existe pero está desconectada del ciclo de desarrollo y despliegue de los equipos. Ejemplo: proceso estructurado de reporte y de difusión del daño al personal relevante, con procesos para abordar daños caso por caso. |
| 5 Leading | Procesos escalables, extensibles y en mejora continua; infraestructura profundamente integrada al ciclo de los equipos; se automatiza donde corresponde. Proceso de reporte integrado al ciclo y un proceso de respuesta de RAI plenamente operativo que atiende sistemáticamente distintos tipos de daño. |

# 4. Knowledge resources (p. 18)

Disponibilidad de expertos y de conocimiento, formación y educación específicos de RAI. Son fundamentales para madurar en casi todas las demás dimensiones y el medio principal para educar a practicantes y equipos.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | Recursos de formación propios inexistentes o limitados; mucho conocimiento de RAI sin documentar; acceso limitado a expertos. |
| 2 Emerging | Igual redacción de recursos que en el nivel 1; los equipos tienen acceso a algunos expertos pero insuficientes; empiezan a surgir bolsillos de expertise desde abajo. |
| 3 Developing | Parte del conocimiento está codificado en formación, pero incompleta o poco accionable (demasiado genérica o difícil de aplicar); los equipos acceden a expertos internos. |
| 4 Realizing | El conocimiento está codificado en buenas prácticas, guías y formación efectiva (casos de estudio, talleres interdisciplinarios); hay una biblioteca actualizada de guía accionable; los expertos forman parte de una comunidad externa reconocida que genera y comparte conocimiento. |
| 5 Leading | La organización abstrae y generaliza sus aprendizajes en conocimiento utilizable por otros; sus expertos participan públicamente en crear y compartir conocimiento (conferencias profesionales y académicas). |

# 5. Tooling (p. 19)

Acceso y desarrollo de herramientas que facilitan el trabajo de RAI. Sirven para escalar su implementación en el terreno (identificar y medir riesgos) al servicio de principios como confiabilidad, seguridad y equidad. La mera existencia de herramientas no alcanza sin incentivos y requisitos de cumplimiento que lleven a usarlas. Influyen la asistencia a lo largo del ciclo de IA, la integración en los flujos de trabajo y la diversidad y personalización de capacidades.[^ms-rai] El documento remite a las herramientas de Microsoft (HAX Toolkit, RAI Toolbox, aka.ms/rai) del apéndice.[^ms-rai]

| Nivel | Qué se pide / cómo se ve |
|---|---|
| 1 Latent | No se da a los equipos acceso a herramientas específicas de RAI. |
| 2 Emerging | Hay algunas herramientas, pero fragmentadas y no interoperables, y sólo abordan aspectos limitados (p. ej. equidad) o etapas limitadas (p. ej. pruebas del modelo). |
| 3 Developing | Hay algunas herramientas, pero no están integradas a los flujos e infraestructura de los equipos y no manejan los tipos de datos o la escala de algunos modelos. |
| 4 Realizing | Las herramientas están integradas a los procesos, son personalizables y dan soporte de punta a punta; tienen tipos y ubicación de datos centralizados, infraestructura común y automatización; manejan muchos escenarios. |
| 5 Leading | Ecosistema extensible y personalizable en el que los equipos pueden aportar herramientas nuevas; soporta documentación y auditoría de punta a punta. |

# Cautelas

* El PDF corta algunas palabras en el margen derecho de la tabla de RAI policy (p. 16, nivel 5, "policies an[d]", "priv[acy]", "ar[e]"); acá se reponen sólo para que la frase sea legible.
* En Knowledge resources, el nivel 2 repite textualmente el primer párrafo del nivel 1 (p. 18); es así en el original, no un error de transcripción.
* La redacción es traducción libre al español; los términos oficiales (Latent, Emerging, Developing, Realizing, Leading) se conservan en inglés.

[^ms-rai]: Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1 (17-may-2023), Microsoft Research, PDF pp. 13-19 (numeración física).
[^ms-rai-web]: Ficha de la publicación en Microsoft Research, MSR-TR-2023-26.
