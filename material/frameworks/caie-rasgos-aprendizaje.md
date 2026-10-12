---
type: Concepto
title: CAIE zona A, Aprendizaje y adaptación (16 rasgos)
description: Los 16 rasgos de la zona A de CAIE, con definición, nivel de madurez esperado y cómo medirlos.
tags: [evaluacion, taxonomia, aprendizaje]
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), sección 3.2.1, pp. 12-15; niveles de la Tabla 5, p. 37"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Zona A de [CAIE](/frameworks/caie.md); ver [zonas y niveles](/frameworks/caie-zonas.md).
Evalúa si el sistema adquiere conocimiento nuevo, generaliza desde la experiencia
y se adapta a entornos y tareas cambiantes.[^caie]

| Id | Rasgo | Definición | Nivel |
|---|---|---|---|
| A1 | Aprendizaje general | Refinar procesos y mejorar el desempeño procesando datos y feedback. Se mide con mejora de precisión, tasa de aprendizaje, reducción de errores y generalización entre tareas | 3 |
| A2 | Adquisición de habilidades | Velocidad y efectividad con que adquiere habilidades nuevas (Chollet 2019) | 3 |
| A3 | Aprendizaje por chunking | Descomponer tareas complejas en unidades manejables y reutilizar lo aprendido | 3 |
| A4 | Aprendizaje supervisado, no supervisado y semisupervisado | Usar datos etiquetados, no etiquetados o ambos para adaptarse a distintos entornos de datos | 2 |
| A5 | Aprendizaje por refuerzo | Aprender acciones óptimas por recompensas y castigos del entorno | 4 |
| A6 | Optimización de la tasa de aprendizaje | Ajustar la velocidad de aprendizaje a la complejidad de la tarea sin sobre ni subajuste | 3 |
| A7 | Aprendizaje por imitación de la cognición humana | Capacidades generativas (NLU y NLG) que simulan comunicación y pensamiento humanos | 4 |
| A8 | Generalización | Aplicar lo aprendido a situaciones nuevas; indicador central de inteligencia | 3 |
| A9 | Adaptación del comportamiento | Modificar la conducta según el feedback y los cambios del entorno; se mide por tiempo de respuesta y efectividad del cambio | 5 |
| A10 | Transfer learning | Usar conocimiento de un dominio para mejorar en otro relacionado | 4 |
| A11 | Zero-shot learning | Reconocer y categorizar patrones o situaciones nuevas sin exposición previa | 2 |
| A12 | Inteligencia multidominio | Aprender y operar en varios dominios; se mide por consistencia de desempeño entre tareas | 5 |
| A13 | Autonomía | Operar y decidir sin intervención humana; se mide por tareas completadas sin input externo y exactitud sin supervisión | 5 |
| A14 | Aprendizaje por autojuego | Refinar estrategias en entornos simulados sin input externo (Silver et al. 2016) | 5 |
| A15 | Desarrollo cognitivo por interacción humano-computadora | Crecimiento cognitivo mutuo: el usuario aprende del sistema y el sistema del usuario; se mide con encuestas y análisis de comportamiento | 4 |
| A16 | Ejercicio cognitivo, apoyo al envejecimiento y habilidades digitales | Apoyar el desarrollo de habilidades cognitivas en distintas edades y géneros, con inclusividad | 5 |

Fuente de la tabla: secciones 3.2.1 (pp. 12-15) y Tabla 5 (p. 37).[^caie]

Notas del paper: la zona se vincula con redes neuronales (RNN, LSTM), RL como
AlphaZero, meta-aprendizaje (MAML), AutoML y arquitecturas como SOAR, ACT-R y
OpenCog (p. 15).[^caie] El nivel de A11 (zero-shot) figura en 2 aunque el texto
lo llama "marcador de inteligencia verdadera"; es un dato tal cual de la
Tabla 5.[^caie]

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas según la numeración impresa.
