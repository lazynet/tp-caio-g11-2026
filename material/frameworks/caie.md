---
type: Framework
title: CAIE
description: Framework académico (Putnoki y Orosz, 2026) para evaluar sistemas de IA en 6 zonas cognitivas, 5 niveles de madurez y un scoring en dos etapas.
tags: [evaluacion, madurez, rubrica]
resource: https://doi.org/10.1007/s10462-026-11493-x
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), Cognitive and artificial intelligence evaluation framework, Artif Intell Rev 59:98, 52 páginas (el PDF de la carpeta tiene 52 páginas, no 27)"
  - id: crossref-doi
    resource: https://api.crossref.org/works/10.1007/s10462-026-11493-x
    title: Registro Crossref del DOI 10.1007/s10462-026-11493-x (consultado 2026-10-11)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

# Qué es

CAIE (*Cognitive and Artificial Intelligence Evaluation*) es una metodología
independiente del dominio para evaluar la "inteligencia" de sistemas de IA y de
sistemas de información en general. Descompone esa inteligencia en 86 rasgos
cognitivos agrupados en 6 zonas, los puntúa con un modelo en dos etapas y los
ubica en 5 niveles de madurez.[^caie]

El paper es un artículo de acceso abierto (CC BY 4.0) de Attila Márton Putnoki y
Tamás Orosz (ELTE, Budapest), publicado el 2026-01-28 en *Artificial
Intelligence Review* 59, artículo 98. Autores, título, revista y fecha están
confirmados contra el registro Crossref del DOI.[^crossref-doi]

# Para qué sirve

* Diagnosticar fortalezas y debilidades de un sistema por zona cognitiva.[^caie]
* Comparar sistemas distintos con el mismo criterio, incluso AI y no AI.[^caie]
* Priorizar desarrollo: ver brechas entre la madurez actual y la esperada.[^caie]
* No es un estándar ni una regulación: el propio paper lo ubica como herramienta
  de apoyo al desarrollo, no obligatoria.[^caie]

# Mapa de conceptos

* [Zonas, niveles de madurez y Matriz de Philipp](/frameworks/caie-zonas.md)
* [Método de evaluación y scoring en dos etapas](/frameworks/caie-metodo-evaluacion.md)
* Rasgos por zona:
  [A Aprendizaje](/frameworks/caie-rasgos-aprendizaje.md),
  [B Percepción](/frameworks/caie-rasgos-percepcion.md),
  [C Razonamiento](/frameworks/caie-rasgos-razonamiento.md),
  [D Interacción](/frameworks/caie-rasgos-interaccion.md),
  [E Memoria](/frameworks/caie-rasgos-memoria.md),
  [F Optimización](/frameworks/caie-rasgos-optimizacion.md)
* [Caso piloto SAP BTP, limitaciones y lectura crítica](/frameworks/caie-caso-limitaciones.md)
* [Cómo usar CAIE como rúbrica para evaluar agentes y LLMs](/frameworks/caie-uso-como-rubrica.md)

# Motivación y marco teórico

* **Problema**: las herramientas de evaluación priorizan eficiencia o desempeño
  en áreas estrechas (ML, reconocimiento de patrones) y rara vez cubren memoria,
  adaptación o interacción.[^caie]
* **Antecedentes que el paper considera parciales**: la categorización de Russell
  y Norvig, la medida de generalización de Chollet, SOAR, ACT-R, CogPrime de
  OpenCog y el marco de IBM Watson. Son teóricos o de dominio específico y no
  permiten comparar entre dominios ni ponderar según el usuario.[^caie]
* **Base de las zonas**: se parte de las capacidades cognitivas que Kotseruba y
  Tsotsos (2020) extraen de 84 arquitecturas cognitivas, y se consolidan en 5
  zonas; la sexta (Optimización) se agrega porque ninguna de las 13
  arquitecturas comparadas la cubre.[^caie]
* **Comparación con otros enfoques** (Tabla 3 del paper): Gato/AGI (benchmark de
  investigación), NIST AI RMF (gestión de riesgo, voluntario), EU AI Act
  (cumplimiento obligatorio) y CAIE (apoyo a la calidad del desarrollo,
  no obligatorio). CAIE diagnostica madurez; NIST y EU AI Act gobiernan riesgo y
  legalidad. Ver [EU AI Act](/frameworks/eu-ai-act.md).[^caie]
* **Definiciones operativas** (p. 5-6): un sistema "cognitivo" mantiene y aplica
  contexto entre tareas, actualiza representaciones con feedback y adapta sus
  políticas de decisión; un sistema con IA puede incluir varios modelos sin
  coordinarlos con un contexto compartido.[^caie]
* **Preguntas de investigación**: RQ-1 si se pueden comparar sistemas cognitivos
  y de IA con una medida objetiva; RQ-2 si la medición puede adaptarse a las
  preferencias del usuario; RQ-3 si el nivel cognitivo puede ser un factor clave
  del scoring (p. 2).[^caie]

# Datos clave del paper

| Dato | Valor | Página |
|---|---|---|
| Zonas | 6 (A a F) | 34 |
| Rasgos listados (A16, B8, C19, D11, E16, F16) | 86; el texto dice "90" y "más de 90" | 11, 45 |
| Niveles de madurez | 5 (Muy bajo a Muy alto) | 35-36 |
| Etapas de scoring | 2 (rasgo a rasgo, y brechas estructurales) | 38 |
| Revisión de literatura | PRISMA 2020-2024, 189 registros, 118 finales | 4 |
| Caso piloto | SAP BTP, 21 usuarios, SZUCS = 0,244 | 43 |

# Cautelas

* **Es académico: usarlo como rúbrica, no como estándar.** Ningún regulador ni
  organismo de normalización lo adoptó; lo que encontramos es solo el paper.
  Búsqueda hecha: DOI en Crossref (confirma metadatos) y búsqueda web general,
  que no devolvió el artículo ni citas de terceros.
* **Discrepancia de conteo**: el paper afirma "más de 90" rasgos pero enumera 86
  (ver [zonas](/frameworks/caie-zonas.md)). En la slide, decir "86 rasgos
  enumerados" o "~90", no "más de 90".
* **La Etapa 2 no está validada empíricamente**: el propio paper la define como
  modelo prospectivo (p. 38-39, 46).
* **Validación mínima**: un único caso (SAP BTP) con 21 respondientes, solo
  usuarios.[^caie]

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas citadas según la numeración impresa del artículo (1-52).
[^crossref-doi]: Crossref, DOI 10.1007/s10462-026-11493-x: título, autores (Attila Márton Putnoki, Tamás Orosz), revista, volumen 59, artículo 98, publicado online 2026-01-28, licencia CC BY 4.0.
