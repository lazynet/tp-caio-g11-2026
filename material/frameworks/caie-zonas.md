---
type: Concepto
title: CAIE, zonas, niveles de madurez y Matriz de Philipp
description: Las 6 zonas cognitivas de CAIE, la escala de 5 niveles de madurez y la matriz que asigna cada rasgo a un nivel esperado.
tags: [evaluacion, madurez, taxonomia]
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), secciones 3.1, 4 y 5, pp. 7-11 y 34-37"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte de [CAIE](/frameworks/caie.md). Método de scoring en
[caie-metodo-evaluacion](/frameworks/caie-metodo-evaluacion.md).

# Las 6 zonas

| Zona | Nombre | Qué evalúa | Rasgos | Detalle |
|---|---|---|---|---|
| A | Learning and Adaptation (Aprendizaje y adaptación) | Adquirir, generalizar y adaptar conocimiento en el tiempo | 16 | [A](/frameworks/caie-rasgos-aprendizaje.md) |
| B | Perception and Awareness (Percepción y conciencia) | Interpretar señales de entrada y mantener conciencia del contexto | 8 | [B](/frameworks/caie-rasgos-percepcion.md) |
| C | Reasoning and Decision-Making (Razonamiento y decisión) | Inferencia lógica, planificación y ejecución autónoma de decisiones | 19 | [C](/frameworks/caie-rasgos-razonamiento.md) |
| D | Interaction and Personalization (Interacción y personalización) | Interacción humano-máquina, respuestas a medida y comunicación | 11 | [D](/frameworks/caie-rasgos-interaccion.md) |
| E | Memory (Memoria) | Almacenar, recuperar y usar conocimiento de corto y largo plazo | 16 | [E](/frameworks/caie-rasgos-memoria.md) |
| F | Optimization and Operational Efficiency (Optimización y eficiencia operativa) | Optimizar con bucles de feedback, autoevaluación y eficiencia de recursos | 16 | [F](/frameworks/caie-rasgos-optimizacion.md) |

Fuente de las definiciones: sección 4, p. 34.[^caie] Los conteos salen de la
numeración de las secciones 3.2.1 a 3.2.6 y de la Tabla 5 (86 en total; el
paper dice "90" y "más de 90", ver cautela en [CAIE](/frameworks/caie.md)).[^caie]

# Cómo se armaron las zonas

* Kotseruba y Tsotsos (2020) revisaron 84 arquitecturas cognitivas y 900
  proyectos; extrajeron percepción, atención, selección de acción, motivación,
  actuación, memoria, aprendizaje, razonamiento, metarrazonamiento, interacción
  social y creatividad.[^caie]
* CAIE las consolidó: el metarrazonamiento queda dentro de C y la atención dentro
  de B, para reducir redundancia.[^caie]
* La zona F no aparece en ninguna de las 13 arquitecturas de la Tabla 2 (ACT-R,
  ART, SOAR, HTM, Leabra, CLARION, RCS, SPA, EPIC, IMPRINT, LIDA, Disciple,
  CogPrime); la D la cubren solo ACT-R, SOAR, CLARION, LIDA, Disciple y
  CogPrime. El paper la añade porque la eficiencia es "una dimensión implícita
  pero rara vez formalizada".[^caie]
* Criterio de inclusión de un rasgo: debe mapearse a al menos un escenario
  realista o caso de uso empresarial (validación por pipeline: percepción,
  acceso a memoria, razonamiento, salida).[^caie]

# Los 5 niveles de madurez

| Nivel | Nombre | Descripción |
|---|---|---|
| 1 | Muy bajo | Ausente o de reglas fijas; sin adaptación ni aprendizaje |
| 2 | Bajo | Comportamiento básico y reactivo; feedback mínimo para ajustes locales |
| 3 | Medio | Predictivo y analítico; anticipa o optimiza con datos estructurados, lógica histórica o probabilística |
| 4 | Alto | Razonamiento adaptativo e integrado; integra dimensiones contextuales, multimodales o éticas |
| 5 | Muy alto | Autoperfeccionamiento e inteligencia generalizada; transfiere entre dominios y reorganiza sus procesos |

Fuente: sección 5, pp. 35-36. Los niveles no están atados a una tecnología; describen
integración y complejidad crecientes.[^caie]

## Progresión por zona (Tabla 4, p. 36)

| Zona | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|
| A | Sin aprendizaje ni adaptación | Aprendizaje básico por feedback | Generalización predictiva y adquisición de habilidades | Aprendizaje autónomo consciente del contexto | Autooptimización plena y adaptación entre dominios |
| B | Sin interpretación de señales | Procesamiento básico de entradas | Percepción contextual y priorización | Coordinación e integración multimodal | Seguimiento situacional pleno y conciencia predictiva |
| C | Sin razonamiento ni planificación | Respuestas basadas en reglas | Razonamiento analítico y previsión | Resolución ética y contextual de problemas | Decisión autónoma y colaborativa |
| D | Sin interacción ni personalización | Interacción reactiva y estática | Diálogo adaptativo al contexto | Interacción personalizada en tiempo real | Interacción plenamente colaborativa y con conciencia emocional |
| E | Sin memoria | Buffer de datos de corto plazo | Recuerdo histórico y uso predictivo | Integración de memoria-contexto y reflexión | Memoria autorreforzada con aprendizaje de por vida |
| F | Sin optimización | Bucle de feedback básico | Optimización estructurada y refinamiento | Automonitoreo y adaptación contextual | Autooptimización dinámica y mejora continua |

Fuente: Tabla 4.[^caie]

# Matriz de Philipp (Tabla 5, p. 37)

Asigna cada rasgo al nivel en el que "típicamente" aparece en el desarrollo de un
sistema. Se basa en el trabajo de Molnár y Mattyasovszky-Philipp (2023) y sirve
como referencia de madurez esperada (Lᵉˣᵖᵉᶜᵗᵉᵈ) cuando no hay metas propias del
dominio. No define dependencias específicas entre rasgos.[^caie]

| Zona | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|
| A | ninguno | A4, A11 | A1, A2, A3, A6, A8 | A5, A7, A10, A15 | A9, A12, A13, A14, A16 |
| B | ninguno | B1, B8 | B2, B3 | B4, B6, B7 | B5 |
| C | ninguno | C1 | C2, C3, C6, C14, C15, C18 | C5, C7, C9, C11, C19 | C4, C8, C10, C12, C13, C16, C17 |
| D | ninguno | ninguno | D2, D3, D4, D5 | D1, D6, D7, D8 | D9, D10, D11 |
| E | ninguno | ninguno | E1, E2, E3, E4, E5, E7, E14 | E8, E9, E12, E13, E15 | E6, E10, E11, E16 |
| F | ninguno | F1 | F2, F4, F15 | F5, F6, F7, F9, F16 | F3, F8, F10, F11, F12, F13, F14 |

Fuente: Tabla 5.[^caie] El nivel de cada rasgo también figura en las tablas por zona.

Observaciones útiles para el plan:

* Ningún rasgo está en el nivel 1 (que es "ausente").[^caie]
* Un rasgo de nivel 5 (por ejemplo C4 Probabilístico, E6 Memoria de modelo del
  mundo, F3 Simulación de escenarios) no se espera en un sistema recién
  desplegado; exigirlo sería un error de rúbrica.[^caie]
* La matriz es un andamiaje teórico: el paper admite que su aplicación empírica
  está limitada sin valores de referencia ni dependencias estructurales (p. 46).[^caie]

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas según la numeración impresa.
