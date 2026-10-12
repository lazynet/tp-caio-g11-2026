---
type: Concepto
title: "Tres eras del software"
description: "Software determinístico, probabilístico y agéntico: lógica de cada era, ejemplos e implicancias estratégicas para el CAIO."
tags: [m1, eras-software, agentes]
sources:
  - id: m1u1-corta
    resource: Documento_Chief_AI_Officer_CAIO_Modulo_1_Unidad_1 (2).pdf
    title: "M1U1 corta, pp. 4-6 y 9"
  - id: m1u1-extendida
    resource: Módulo 1 — Unidad 1 — Mentalidad CAIO y liderazgo en la era IA.pdf
    title: "M1U1 extendida, p. 5"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Cuadro comparativo

| Era | Lógica | Ejemplo del curso | Implicancia estratégica |
|---|---|---|---|
| Determinística | Si X, entonces Y (reglas explícitas) | Procesamiento de nóminas por horas trabajadas y tasa fija | Eficiencia y fiabilidad; el software es un activo que se construye y mantiene[^m1u1-corta] |
| Probabilística | Según los datos, lo más probable es Z (patrones) | Recomendaciones de Netflix | Personalización y predicción; los datos son el activo principal[^m1u1-corta] |
| Agéntica | Para lograr A, ejecuto B, C y D (autonomía) | Agente que planifica y reserva un viaje completo vía APIs | Automatización y escala; la estrategia es diseñar sistemas de agentes y gobernar su autonomía[^m1u1-corta] |

# Detalle por era

**Determinística.** Misma entrada, misma salida; reglas codificadas, comportamiento predecible y auditable. Domina los ERP y CRM actuales. Fortaleza: confiabilidad; limitación: rigidez, no maneja lo no anticipado. Ideal para problemas bien estructurados, como sistemas bancarios o control industrial.[^m1u1-extendida][^m1u1-corta]

**Probabilística.** Machine learning y LLMs: se entrena con datos para que "aprendan" patrones y el sistema ofrece la respuesta más probable, no una única correcta. El líder ya no puede exigir certeza: trabaja con probabilidades, umbrales de confianza y mecanismos de validación. La evaluación deja de ser binaria (funciona / no funciona) y pasa a ser estadística.[^m1u1-extendida][^m1u1-corta]

**Agéntica.** Se consolida en 2024-2025. Los agentes planifican, ejecutan acciones, llaman herramientas externas, coordinan con otros agentes y ajustan su comportamiento según resultados intermedios. Ejemplos de frameworks citados: LangGraph, AutoGen, Salesforce Einstein, Microsoft Copilot Studio.[^m1u1-extendida] Se pasa de crear herramientas a orquestar equipos híbridos de humanos y agentes.[^m1u1-corta]

# Riesgo nuevo de la era agéntica

Un agente mal configurado no solo da una respuesta incorrecta: puede **ejecutar acciones incorrectas en sistemas reales**. La gobernanza exige nuevas capas de supervisión, límites de acción explícitos e intervención humana en puntos críticos.[^m1u1-extendida]

# Diferencia probabilístico vs. agéntico (autoevaluación)

El software probabilístico predice, clasifica o genera y entrega un output para que un humano u otro sistema decida (ej. probabilidad de fraude en una transacción). El agéntico decide y ejecuta acciones para alcanzar un objetivo, a menudo sin intervención humana directa (ej. trading algorítmico que compra y vende según reglas y objetivos).[^m1u1-corta]

# Ejercicio del curso

Clasificar tres iniciativas propias: ¿en qué era encaja cada una?, ¿talento, infraestructura y métricas están alineados con la lógica de esa era?, ¿hay oportunidad de evolucionar a la siguiente y qué haría falta?[^m1u1-corta]

# Relacionado

[Mandato del CAIO](/conceptos/m1u1-mandato-caio.md) · [cinco habilitadores](/conceptos/m1u1-cinco-habilitadores.md) · unidad [M1U1](/unidades/m1u1-mentalidad-caio.md).

[^m1u1-corta]: M1U1 corta, pp. 4-6 y 9
[^m1u1-extendida]: M1U1 extendida, p. 5
