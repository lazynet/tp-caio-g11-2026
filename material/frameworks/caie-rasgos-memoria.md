---
type: Concepto
title: CAIE zona E, Memoria (16 rasgos)
description: Los 16 rasgos de la zona E de CAIE, con definición, nivel de madurez esperado y el modelo combinado de memoria.
tags: [evaluacion, taxonomia, memoria]
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), sección 3.2.5, pp. 25-30; niveles de la Tabla 5, p. 37"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Zona E de [CAIE](/frameworks/caie.md); ver [zonas y niveles](/frameworks/caie-zonas.md).
Mide cómo el sistema almacena, recupera y aplica conocimiento en el tiempo.
Es clave donde las decisiones dependen de interacciones pasadas.[^caie]

| Id | Rasgo | Definición | Nivel |
|---|---|---|---|
| E1 | Memoria sensorial y DSBM | Captura y estabiliza brevemente la entrada cruda (milisegundos a segundos); el DSBM (Data Short Buffer Memory) la preprocesa antes de pasarla a memoria de corto plazo, sin ser un tipo de memoria aparte | 3 |
| E2 | Memoria icónica, ecoica y háptica | Canales por modalidad (visual, auditivo, táctil) dentro de la memoria sensorial | 3 |
| E3 | Memoria buffer de acción de comportamiento (ABM) | Capa de control que convierte memoria corta y larga en salidas listas para actuar y sincroniza la ejecución en tiempo real | 3 |
| E4 | Memoria de corto plazo (de trabajo) | Retener y manipular información por segundos o pocos minutos; puerta entre memoria sensorial y de largo plazo | 3 |
| E5 | Recuperación de memoria de largo plazo para tareas complejas | Retener información por períodos largos y aplicar experiencias pasadas a situaciones nuevas | 3 |
| E6 | Memoria avanzada y de modelo del mundo | Almacenar y actualizar representaciones del entorno para predecir estados futuros | 5 |
| E7 | Memoria procedimental | Retener rutinas y cómo se hacen las tareas para ejecutarlas sin reaprender | 3 |
| E8 | Habilidades motoras y coordinación | Recordar y refinar la ejecución física de tareas (robótica, automatización) | 4 |
| E9 | Memoria declarativa | Hechos y conocimiento explícito; abarca episódica y semántica | 4 |
| E10 | Memoria episódica | Eventos y experiencias específicas; personaliza interacciones y decisiones | 5 |
| E11 | Memoria semántica | Hechos y conceptos generales; grafos de conocimiento y ontologías | 5 |
| E12 | Memoria contextual (incl. espacial) | Combina datos espaciales y temporales con conciencia situacional (ubicación, hora, actividad) | 4 |
| E13 | Inteligencia instructiva y control de tareas | Interfaz entre memoria y ejecución: genera instrucciones priorizadas y resuelve conflictos entre tareas | 4 |
| E14 | Soporte de memoria y recuperación de información | Memoria externa para el usuario: bases de datos, repositorios y búsqueda | 3 |
| E15 | Representación y organización del conocimiento | Estructurar información para recuperación y razonamiento; incluye memoria asociativa (ej. AtomSpace) | 4 |
| E16 | Mecanismos de olvido (optimización selectiva) | Podar, decaer o borrar por heurística lo obsoleto o redundante, conservando lo crítico | 5 |

Fuente: sección 3.2.5 (pp. 25-30) y Tabla 5 (p. 37).[^caie]

# Modelo combinado de memoria (Fig. 1, p. 28)

Parte del modelo modal de Atkinson y Shiffrin (1968): memoria sensorial, de corto
plazo y de largo plazo, refinado por Baddeley y Hitch y con el búfer episódico de
Baddeley (2000). La de largo plazo se divide en explícita (declarativa:
episódica, semántica, contextual) e implícita (procedimental). CAIE agrega la
memoria avanzada de modelo del mundo y la capa de control ABM.[^caie]

Notas del paper: tecnologías citadas son RNN y LSTM, redes con memoria
aumentada, grafos de conocimiento, SPAUN, AtomSpace, InfluxDB y Elasticsearch
(p. 30). La revisión PRISMA encontró la memoria subrepresentada en la
literatura (p. 45).[^caie]

Para agentes basados en LLM, E4 y E5 equivalen a ventana de contexto y memoria
persistente; esa lectura es nuestra, no del paper (ver
[uso como rúbrica](/frameworks/caie-uso-como-rubrica.md)).

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas según la numeración impresa.
