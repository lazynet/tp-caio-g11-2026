---
type: Concepto
title: Microsoft RAI MM, estructura y los 5 niveles
description: Cómo se organizan las 24 dimensiones del RAI Maturity Model en tres categorías, qué significan los niveles Latent a Leading y las reglas para subir de nivel.
tags: [gobierno, madurez, ia-responsable, escala]
status: draft
sources:
  - id: ms-rai
    resource: Microsoft Responsible AI 2023.pdf
    title: "Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1, 17-may-2023; pp. 2, 7-13 del PDF (numeración física; la impresa va uno menos)"
  - id: ms-rai-web
    resource: https://www.microsoft.com/en-us/research/publication/responsible-ai-maturity-model/
    title: Ficha de la publicación en Microsoft Research (MSR-TR-2023-26), consultada 2026-10-11
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [Microsoft RAI Maturity Model](/frameworks/microsoft-rai-maturity.md). Cómo usarlo: [uso](/frameworks/microsoft-rai-uso.md).

# Estructura: 3 categorías, 24 dimensiones

El modelo tiene 24 dimensiones empíricas, cada una con 5 niveles, agrupadas en tres categorías que forman una pirámide: Organizational Foundations es la base, Team Approach el centro y RAI Practice la cima; cada capa depende de las de abajo (p. 9).[^ms-rai]

| Categoría | Qué cubre | Dims. | Detalle |
|---|---|---|---|
| Organizational Foundations | La organización entera; las mueve el liderazgo senior | 5 | [fundamentos](/frameworks/microsoft-rai-dimensiones-fundamentos.md) |
| Team Approach | Cómo, por qué y con quién trabajan los equipos RAI | 10 | [equipo](/frameworks/microsoft-rai-dimensiones-equipo.md) |
| RAI Practice | Cómo se ejecuta el trabajo (identificar, medir, mitigar, monitorear, etc.) | 9 | [práctica](/frameworks/microsoft-rai-dimensiones-practica.md) |

## Las 24 dimensiones

| # | Dimensión | Categoría (subgrupo) | Página PDF |
|---|---|---|---|
| 1 | Leadership and Culture | Foundations | 13-14 |
| 2 | RAI policy | Foundations (Governance) | 16 |
| 3 | RAI compliance processes and infrastructure | Foundations (Governance) | 17 |
| 4 | Knowledge resources | Foundations (Org. Capacity) | 18 |
| 5 | Tooling | Foundations (Org. Capacity) | 19 |
| 6 | Teams valuing RAI | Team Approach | 21 |
| 7 | Timing of RAI within the AI development and deployment lifecycle | Team Approach | 22 |
| 8 | Motivation for AI products | Team Approach | 23 |
| 9 | Sociotechnical approach | Team Approach (cross-discipline) | 24 |
| 10 | Common language | Team Approach (cross-discipline) | 25 |
| 11 | Collaboration within teams | Team Approach (cross-discipline) | 26 |
| 12 | Non-UX disciplines' perceptions of UX | Team Approach (cross-discipline) | 27-28 |
| 13 | UX practitioners' AI readiness | Team Approach (cross-discipline) | 29 |
| 14 | RAI specialists working with product teams | Team Approach (cross-discipline) | 30 |
| 15 | Teams working with RAI specialists | Team Approach (cross-discipline) | 31 |
| 16 | Accountability | RAI Practice | 33 |
| 17 | External transparency | RAI Practice (Transparency) | 34-35 |
| 18 | Internal transparency | RAI Practice (Transparency) | 35-36 |
| 19 | Identifying RAI risks | RAI Practice | 37-38 |
| 20 | Measuring RAI risks | RAI Practice | 38-39 |
| 21 | Mitigating RAI risks | RAI Practice | 40 |
| 22 | Monitoring RAI risks | RAI Practice | 41-42 |
| 23 | AI privacy | RAI Practice (privacy y seguridad) | 43-44 |
| 24 | AI security | RAI Practice (privacy y seguridad) | 44-45 |

La numeración 1-24 es nuestra, para referenciar; el PDF no numera las dimensiones. Se verificó que las listadas en el índice del PDF suman 24 (p. 4-5).[^ms-rai]

# Los 5 niveles

Los niveles van del 1 (Latent) al 5 (Leading) en todas las dimensiones (p. 2).[^ms-rai] El PDF no ofrece una definición genérica de cada nivel: la definición está dentro de cada dimensión. Lo que sigue es una lectura transversal nuestra, a partir de los patrones que se repiten en las tablas, y no una cita del documento.

| Nivel | Nombre | Patrón transversal (síntesis propia) |
|---|---|---|
| 1 | Latent | No existe o no se es consciente; lo que pasa es accidental o reactivo, o lo señalan terceros. |
| 2 | Emerging | Hay conciencia y planes, pero el trabajo es ad hoc, manual y depende de pocas personas. |
| 3 | Developing | Existe una versión inicial, parcial o fragmentada; hay avance en bolsillos pero no es consistente. |
| 4 | Realizing | Práctica sistemática, documentada y valorada, aunque con huecos de integración al ciclo o en profundidad. |
| 5 | Leading | Integrada al negocio habitual, escalable, mejorada continuamente y con influencia hacia afuera (estándares, industria). |

# Consideraciones clave

* **El modelo evoluciona.** RAI es un campo nuevo; el modelo es un artefacto vivo (p. 10).[^ms-rai]
* **Mira hacia adelante.** Captura el estado ideal, no el actual; la mayoría de las organizaciones está en niveles bajos y el nivel 5 es muy aspiracional (p. 10).[^ms-rai]
* **La madurez varía dentro de la organización.** Team Approach y RAI Practice se pueden promediar entre equipos para ver el panorama de una organización, pero mirar las diferencias entre equipos ayuda a enfocar y a que los más maduros compartan prácticas (p. 10).[^ms-rai]
* **La dificultad no es lineal.** Los niveles 1 a 5 no son pasos equidistantes: salir de 1 y 2 suele requerir crear procesos o prácticas nuevos (costoso), mientras que pasar de 3 y 4 puede ser formalizar o integrar lo existente. Además, una dimensión puede quedar bloqueada por la baja madurez de otra (pp. 10-11).[^ms-rai]
* **RAI depende del contexto.** El tipo y dominio del sistema condicionan la práctica; por eso el modelo define cómo encarar con madurez (qué discusiones, qué factores sociotécnicos, qué decisiones) en vez de criterios rígidos (p. 11).[^ms-rai]
* **Las dimensiones son interdependientes.** Se separaron para facilitar el entendimiento y la evaluación, pero es una simplificación (p. 9).[^ms-rai]
* **Cumplir un nivel antes de pasar al siguiente.** Para subir hay que lograr antes las metas deseables del nivel previo; si el nivel 4 dice que los equipos identifican bien los riesgos, se asume que el 5 también lo cumple (p. 12).[^ms-rai]
* **El nivel 5 puede no ser aplicable ni deseable** para toda organización (p. 11).[^ms-rai]

# Origen de las dimensiones

Surgieron de 47 entrevistas con especialistas de RAI y practicantes de IA (internos y externos a Microsoft) y de 23 focus groups, 17 entrevistas y feedback asincrónico con 56 expertos internos que validaron dimensiones, detectaron huecos y definieron niveles; en total más de 80 horas con 90 participantes (pp. 7-8). El paso siguiente declarado era un piloto con equipos de Microsoft.[^ms-rai]

[^ms-rai]: Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1 (17-may-2023), Microsoft Research, PDF pp. 2, 4-5, 7-13 (numeración física).
[^ms-rai-web]: Ficha de la publicación en Microsoft Research: confirma 24 dimensiones, 3 categorías y 5 niveles de Latent a Leading.
