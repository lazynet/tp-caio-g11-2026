---
type: Concepto
title: "Build / Buy / Agentificar"
description: "Triángulo de decisión de cómo construir cada iniciativa, con cuatro ejes de análisis, criterio de diferenciación y dimensión de compliance."
tags: [m1, build-buy, arquitectura]
sources:
  - id: finma-08-2024
    resource: https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/4dokumentation/finma-aufsichtsmitteilungen/20241218-finma-aufsichtsmitteilung-08-2024.pdf
    title: "FINMA, Guidance 08/2024, Governance and risk management when using artificial intelligence (18-12-2024)"
  - id: m1u2
    resource: Módulo 1 — Unidad 2 — Portfolio, priorización y ejecución de los 100 días.pdf
    title: "M1U2, pp. 2, 5 y 9-10"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Las tres opciones

| Opción | Qué implica |
|---|---|
| Build | Desarrollo propio |
| Buy | Adquirir una solución existente |
| Agentificar | Categoría emergente: orquestar capacidades de IA (modelos, APIs, herramientas, bases de conocimiento internas) con agentes autónomos, sin construir desde cero ni comprar una solución cerrada |

[^m1u2]

La agentificación reduce el esfuerzo de construcción sin sacrificar control: en vez de entrenar un modelo propio o comprar una caja cerrada, se diseña un flujo donde agentes usan APIs y herramientas existentes.[^m1u2]

# Cuatro ejes (frameworks desde 2025)

1. Costo total de propiedad (TCO).
2. Tiempo hasta el primer valor (time-to-value).
3. Capacidad interna disponible.
4. Nivel de control requerido sobre el sistema.

La decisión "no puede delegarse a criterios puramente técnicos".[^m1u2]

# Criterio de diferenciación

- Si la IA replica algo que cualquier competidor puede comprar, el argumento para construir se debilita.
- Si el caso requiere datos propietarios, lógica de negocio específica o integración profunda con legacy único, construir o agentificar puede ser la única opción viable.
- Si el proceso es un diferenciador competitivo clave, perder control sobre el modelo es un riesgo estratégico.

[^m1u2]

# Compliance

El AI Act exige que los sistemas de alto riesgo sean auditables, trazables y gobernables. Una caja negra puede ser incompatible, sobre todo si el proveedor no da transparencia ni permite revisión independiente. Por eso el control es también un criterio legal: hay que poder demostrar que se entiende, monitorea e interviene el comportamiento del sistema.[^m1u2] El curso respalda la exigencia de revisión independiente en la FINMA Guidance 08/2024; esa guía es suiza y sí pide revisión independiente para aplicaciones materiales (ver [cautelas](/conceptos/m1u2-cautelas-citas-regulatorias.md)).[^finma-08-2024]

# Ejemplos del caso del curso

| Iniciativa | Decisión | Fundamento |
|---|---|---|
| Clasificación de documentos de onboarding | Agentificar | Modelo de extracción de entidades sobre PDF |
| Resumen de llamadas | Buy | Herramienta de transcripción y resumen con API existente |
| Detección de anomalías en transacciones internas | Build | Sensibilidad de los datos y requisitos del AI Act para sistemas de alto riesgo financiero |

[^m1u2]

Ver el [caso completo](/conceptos/m1u2-caso-portfolio-financiera.md). Unidad: [M1U2](/unidades/m1u2-portfolio-100-dias.md).

[^finma-08-2024]: FINMA, Guidance 08/2024, Governance and risk management when using artificial intelligence (18-12-2024)
[^m1u2]: M1U2, pp. 2, 5 y 9-10
