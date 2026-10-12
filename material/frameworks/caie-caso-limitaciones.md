---
type: Caso
title: CAIE, caso piloto SAP BTP y limitaciones
description: Resultados del piloto de CAIE sobre SAP BTP (21 usuarios, SZUCS 0,244), validación de las preguntas de investigación y límites del paper.
tags: [evaluacion, caso, limitaciones]
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), secciones 2, 7, 8, 9 y 10, pp. 3-5 y 43-47"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte de [CAIE](/frameworks/caie.md). Método en
[caie-metodo-evaluacion](/frameworks/caie-metodo-evaluacion.md).

# Metodología del paper

* **Revisión PRISMA** (2020-2024) en cinco bases: Google Scholar, PubMed,
  SpringerLink, ScienceDirect y Web of Science. Se refinó por palabras clave en el
  título hasta 189 registros; se eliminaron 71 y quedaron 118 estudios.[^caie]
* **Tendencias**: crecen Interacción y Personalización; decae Optimización y
  Eficiencia. Seleccionados por año: 14, 18, 34, 26 y 26 (2020 a 2024).[^caie]
* **Hallazgo de la revisión**: Optimización está saturada en la literatura y
  Memoria subrepresentada (p. 45).[^caie]
* **Encuesta cuantitativa** sobre SAP Business Technology Platform como caso
  demostrativo; el paper aclara que CAIE no es específico de SAP.[^caie]

# Resultados del piloto SAP BTP (sección 7, pp. 43-44)

Base: 21 respondientes, todos usuarios activos; sin datos de arquitectos.[^caie]

| Zona | ZUCS |
|---|---|
| A Aprendizaje y adaptación | 0,395 |
| B Percepción y conciencia | 0,089 |
| C Razonamiento y decisión | 0,127 |
| D Interacción y personalización | 0,261 |
| E Memoria | 0,171 |
| F Optimización y eficiencia operativa | 0,366 |
| **SZUCS (sistema completo)** | **0,244** |

Lectura del paper: A y F puntúan mejor (aprendizaje general, adaptación del
comportamiento, gobierno, automonitoreo); B y C muestran brechas críticas
porque los usuarios las consideran importantes pero casi ausentes.[^caie]

# Validación de las preguntas de investigación

* RQ-1 y RQ-2: 95,24% de los participantes afirmó que los rasgos cognitivos y de
  IA pueden evaluarse objetivamente y adaptarse a la relevancia definida por el
  usuario (20 de 21).[^caie]
* RQ-3: 90,48% confirmó que la capacidad cognitiva sirve como métrica central
  (19 de 21).[^caie]
* Los porcentajes corresponden a una muestra de 21; son indicativos, no
  estadísticamente robustos (lectura nuestra).

# Limitaciones

Del paper:

* La Etapa 2 no se pudo activar por falta de datos a nivel de arquitectura: no
  hubo brechas de madurez, mapa de dependencias ni diagnóstico de roadmap (p. 46).[^caie]
* La Matriz de Philipp es un andamiaje teórico sin valores de referencia
  empíricos (p. 46).[^caie]
* La Etapa 2 es "prospectiva" y su adecuación final queda pendiente de validación
  y casos adicionales (pp. 38-39).[^caie]
* Trabajo futuro: matriz de dependencias completa y su visualización,
  motor de recomendación cognitiva, Matrices de Philipp por dominio y
  detección automática de presencia (Pᵢ) leyendo documentación (p. 47).[^caie]

Observaciones críticas nuestras (no del paper):

* Un único caso, un único tipo de sistema (plataforma empresarial) y solo
  usuarios; no hay evaluación de LLMs, agentes ni sistemas bancarios.
* Los autores usan su propio marco y el cuestionario no está publicado ("No
  datasets were generated or analysed", p. 47), así que no es reproducible.
* El puntaje depende de la percepción del usuario, sujeto a sesgo; no hay
  pruebas objetivas de capacidad.
* Hay rasgos que no aplican a software (BCI, HRI, habilidades motoras); un
  puntaje total diluye con ceros lo que el sistema no pretende hacer.
* Ningún organismo ni regulador lo adoptó; no hay evidencia de uso fuera del
  paper (búsqueda web sin resultados).

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas según la numeración impresa.
