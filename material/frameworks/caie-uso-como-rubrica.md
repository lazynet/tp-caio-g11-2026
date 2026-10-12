---
type: Concepto
title: CAIE, uso como rúbrica para evaluar agentes y LLMs de un proveedor para bancos
description: Propuesta del equipo para adaptar CAIE como rúbrica de evaluación de agentes y modelos, qué zonas pesan más en banca y qué no cubre.
tags: [evaluacion, rubrica, banca, propuesta]
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), secciones 4 a 6, pp. 34-43"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Este concepto es **una propuesta del equipo**, no figura en el paper: CAIE no
trae una versión para LLMs ni para banca. Fuente del método:
[CAIE](/frameworks/caie.md) y [caie-metodo-evaluacion](/frameworks/caie-metodo-evaluacion.md).

# Qué se puede tomar del paper

* El paper permite evaluar un sistema con solo la Etapa 1 y pesos del usuario,
  sin expectativas universales.[^caie]
* Los pesos de importancia los define quien evalúa: en banca, el comité de
  riesgo o el cliente. Eso permite reflejar prioridades regulatorias sin cambiar
  el marco.[^caie]
* Admite también datos extraídos de documentación técnica en lugar de encuestas.[^caie]

# Propuesta de adaptación

1. **Elegir rasgos relevantes** (subconjunto) y ponderar de 1 a 10 con el cliente.
   Los rasgos de robótica y BCI se excluyen (C17, D11, E8) en vez de puntuar cero.
2. **Medir P y V con pruebas** (golden sets, red teaming), no con opinión: así se
   reduce la dependencia de la percepción del usuario.
3. **Fijar L esperado** con la Matriz de Philipp como piso y las exigencias del
   cliente como techo.
4. **Reportar el perfil por zona**, no solo el SZUCS: un promedio esconde que
   una zona crítica (por ejemplo, F) esté en rojo.

# Zonas y rasgos con más peso en banca (criterio nuestro)

| Prioridad | Rasgos CAIE | Por qué |
|---|---|---|
| Alta | [D6](/frameworks/caie-rasgos-interaccion.md) confianza y explicabilidad | Auditabilidad de decisiones |
| Alta | [F11, F12, F13, F14](/frameworks/caie-rasgos-optimizacion.md) seguridad, riesgo, cumplimiento, auditoría | Exigencias del cliente bancario |
| Alta | [C5, C10, C11](/frameworks/caie-rasgos-razonamiento.md) ética, pensamiento crítico, falacias | Riesgo de decisiones sesgadas o circulares |
| Alta | [D7, D8](/frameworks/caie-rasgos-interaccion.md) resiliencia y robustez | Continuidad operativa |
| Media | [E4, E5, E16](/frameworks/caie-rasgos-memoria.md) memoria de trabajo, larga y olvido | Contexto de agentes y retención de datos |
| Media | [A1, A8](/frameworks/caie-rasgos-aprendizaje.md) aprendizaje y generalización | Calidad en casos nuevos |
| Media | [F7, F15](/frameworks/caie-rasgos-optimizacion.md) automonitoreo y evaluación de desempeño | Monitoreo en producción |
| Baja | B4 a B6, C17, D11, E8 | Percepción física, BCI, robots: no aplican |

# Qué no cubre CAIE (límites para el uso bancario)

* **No es evaluación de cumplimiento**: no reemplaza el análisis de riesgo del
  [EU AI Act](/frameworks/eu-ai-act.md) ni del [Microsoft RAI](/frameworks/microsoft-rai-maturity.md).
  El propio paper lo diferencia de NIST y del EU AI Act (Tabla 3).[^caie]
* **No hay benchmark de exactitud, alucinación, sesgo ni privacidad**: CAIE
  puntúa capacidades, no corrección de las respuestas.
* **Los rasgos F11 a F14 miden si el sistema automatiza esos controles**, no si
  el proveedor cumple.
* **No existen puntos de corte** que digan "apto" o "no apto".

# Cómo citarlo en el plan

Como "rúbrica de referencia académica adaptada" para ordenar la conversación
sobre capacidades y brechas, nunca como estándar. Si va una cifra en una slide
(por ejemplo, "86 rasgos en 6 zonas"), debe llevar `verified` en este concepto
antes de usarse.

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas según la numeración impresa.
