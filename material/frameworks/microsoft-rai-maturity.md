---
type: Framework
title: Microsoft Responsible AI Maturity Model
description: Modelo de madurez de IA responsable de Microsoft (2023) con 24 dimensiones en 3 categorías y 5 niveles, de Latent a Leading, que no se promedian.
tags: [gobierno, madurez, ia-responsable]
status: draft
resource: https://www.microsoft.com/en-us/research/publication/responsible-ai-maturity-model/
sources:
  - id: ms-rai
    resource: Microsoft Responsible AI 2023.pdf
    title: "Vorvoreanu, Heger, Passi, Dhanorkar, Kahn y Wang (2023), Responsible AI Maturity Model, v1, 17-may-2023, Aether Central UX Research & Education, Microsoft, 51 páginas"
  - id: ms-rai-web
    resource: https://www.microsoft.com/en-us/research/publication/responsible-ai-maturity-model/
    title: Ficha de la publicación en Microsoft Research (MSR-TR-2023-26, mayo de 2023), consultada 2026-10-11
  - id: ms-rai-pdf
    resource: https://www.microsoft.com/en-us/research/wp-content/uploads/2023/05/RAI-MM-for-PDF-printing-PUBLISHED-May-17.pdf
    title: PDF oficial del RAI MM (17-may-2023), enlazado desde la ficha de Microsoft Research
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

# Qué es

Framework de Microsoft Research para que una organización identifique su nivel actual y el deseado de madurez en IA responsable (RAI). Contiene 24 dimensiones derivadas empíricamente, cada una con 5 niveles de menor a mayor madurez: Latent, Emerging, Developing, Realizing, Leading.[^ms-rai]

# Publicación original (verificada)

Autores: Mihaela Vorvoreanu, Amy Heger, Samir Passi, Shipi Dhanorkar, Zoe Kahn y Ruotong Wang, de Aether Central UX Research & Education (Microsoft). Versión 1, 17 de mayo de 2023 (tapa del PDF). La ficha oficial lo registra como informe técnico MSR-TR-2023-26 de mayo de 2023, con el PDF, un resumen ejecutivo con FAQ y un deck de taller.[^ms-rai-web][^ms-rai-pdf] El PDF de la carpeta de la cursada coincide con esa publicación: mismo título, autores y fecha.[^ms-rai]

# Ideas clave

* **Tres categorías** (pirámide): Organizational Foundations (5 dimensiones), Team Approach (10) y RAI Practice (9).[^ms-rai]
* **Mapa, no medición punitiva.** Mirar adónde se puede llegar importa más que el nivel actual; el nivel 5 puede no ser deseable para todos.[^ms-rai]
* **No se promedia entre dimensiones:** un nivel alto no significa lo mismo en dimensiones distintas ni independientes entre sí.[^ms-rai]
* **La colaboración interdisciplinaria es el motor** de la madurez.[^ms-rai]
* **Dificultad no lineal:** los saltos de los niveles bajos cuestan más, y cada nivel exige cumplir el anterior.[^ms-rai]

# Conceptos

| Concepto | Qué contiene |
|---|---|
| [Estructura y niveles](/frameworks/microsoft-rai-niveles.md) | Las 24 dimensiones listadas, los 5 niveles, consideraciones clave y metodología de origen |
| [Organizational Foundations](/frameworks/microsoft-rai-dimensiones-fundamentos.md) | Liderazgo y cultura, política, cumplimiento, conocimiento, herramientas, con tabla por nivel |
| [Team Approach](/frameworks/microsoft-rai-dimensiones-equipo.md) | 10 dimensiones de enfoque y colaboración, con tabla por nivel |
| [RAI Practice](/frameworks/microsoft-rai-dimensiones-practica.md) | Accountability, transparencia, riesgos, privacidad y seguridad, con tabla por nivel |
| [Uso y aplicación](/frameworks/microsoft-rai-uso.md) | Reglas de uso, quién evalúa, hallazgos y lectura para un proveedor de software de bancos |

# Respalda

Gobierno: ver el [mapa](/mapa-plan-fuentes.md). Se complementa con el [AIMM](/frameworks/aimm-gartner.md) (madurez de IA en general) y con el [EU AI Act](/frameworks/eu-ai-act.md) (requisitos regulatorios).

# Cautelas

* La numeración de páginas que se cita es la física del PDF (la impresa va una menos).
* Las tablas por nivel son traducción libre; el PDF corta algunas palabras en el margen derecho de ciertas tablas (ver cautelas de cada concepto).
* El modelo se declara aspiracional y en evolución: no hay umbrales cuantitativos ni validación con organizaciones al momento de la versión 1 (el piloto era un paso futuro).[^ms-rai]

[^ms-rai]: Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1 (17-may-2023), Microsoft Research, PDF pp. 1-2, 7-12.
[^ms-rai-web]: Ficha de la publicación en Microsoft Research, MSR-TR-2023-26.
[^ms-rai-pdf]: PDF oficial del RAI MM publicado en el sitio de Microsoft Research.
