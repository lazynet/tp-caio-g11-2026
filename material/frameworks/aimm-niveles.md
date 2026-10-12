---
type: Concepto
title: AIMM, los 5 niveles
description: Descripción de cada nivel de madurez (Awareness a Transformational) con señal, síntoma, riesgo dominante y qué hace falta para avanzar.
tags: [diagnostico, madurez]
status: draft
sources:
  - id: aimm
    resource: AIMM (Gartner) 2026.pdf
    title: AIMM (Gartner), documento de referencia de la cursada, pp. 1-2
  - id: aimm-sec
    resource: https://blogs.bmc.com/ai-maturity-models/
    title: BMC, AI maturity models (confirma nombres y señal de cada nivel)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [AIMM](/frameworks/aimm-gartner.md). Los nombres y la señal característica coinciden con resúmenes públicos;[^aimm-sec] síntomas, riesgos y recomendaciones son elaboración del documento de la cursada, no de Gartner.[^aimm]

| Nivel | Denominación | Señal característica |
|---|---|---|
| 1 | Awareness (Conciencia) | Se habla de IA. No hay nada implementado. |
| 2 | Active (Activo) | Pruebas de concepto y pilotos aislados. |
| 3 | Operational (Operacional) | Al menos un sistema en producción generando valor. |
| 4 | Systemic (Sistémico) | IA transversal a procesos y productos, con plataforma común. |
| 5 | Transformational (Transformacional) | La IA es parte del modelo de negocio, no un apoyo. |

# Detalle por nivel

| Nivel | Síntoma típico | Riesgo dominante | Para avanzar |
|---|---|---|---|
| 1 Awareness | Se discute qué hacer con IA sin conocer el estado de los propios datos | Expectativas infladas que luego se leen como fracaso | Inventario de datos y 2 o 3 casos de uso acotados y medibles |
| 2 Active | Varios pilotos exitosos y ninguno en producción | "Purgatorio de pilotos": demos que no escalan porque nadie se hace cargo del salto a operaciones | Criterios de qué pasa a producción y responsable explícito del ciclo de vida del modelo |
| 3 Operational | Hay que responder qué pasa cuando el modelo se degrada | Deuda técnica y de gobernanza acumulada en la etapa de pilotos | Plataforma compartida, estándares de documentación, marco de gestión de riesgos formal |
| 4 Systemic | Un equipo nuevo lanza una solución reutilizando infraestructura y controles | Concentración: dependencias críticas de sistemas poco explicables | Integrar la IA en la planificación estratégica, no solo en la ejecución |
| 5 Transformational | Decisiones estratégicas imposibles sin las capacidades de IA instaladas | Rigidez: el modelo de negocio queda atado a supuestos tecnológicos | No es objetivo universal |

Características por nivel según el documento:[^aimm]

* **Nivel 1:** sin iniciativas ni presupuesto; es la etapa de mayor distancia entre expectativa y capacidad real.
* **Nivel 2:** iniciativas de equipos individuales, sin coordinación central; cada una arranca de cero.
* **Nivel 3:** sistema en producción sostenido con valor atribuible; aparecen roles dedicados, versionado de modelos y datos, monitoreo y MLOps incipiente.
* **Nivel 4:** plataforma común, componentes reutilizables y función de gobernanza formal; las decisiones dejan de ser caso por caso.
* **Nivel 5:** redefine qué hace la organización y cómo compite. Pocas lo sostienen y menos aún de forma homogénea. "Para la mayoría, el nivel 3 o 4 sostenido vale más que un 5 aspiracional" (p. 2).

[^aimm]: AIMM (Gartner), documento de referencia de la cursada, pp. 1-2
[^aimm-sec]: BMC, AI maturity models
