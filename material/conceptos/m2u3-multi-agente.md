---
type: Concepto
title: Colaboración multi-agente
description: Cómo varios agentes especializados se coordinan, qué ventajas declara el curso y cómo se reparten el trabajo con las personas.
tags: [m2, arquitectura, agentes]
sources:
  - id: m2u3
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_2_Unidad_7.pdf
    title: M2U3 (el archivo dice Unidad 7), 20 slides
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Cómo funciona

Múltiples agentes especializados coordinan sus acciones para resolver problemas
"inabordables para un individuo o un agente único". Tres rasgos:[^m2u3]

- **Especialización:** cada agente domina una función del proceso.
- **Coordinación:** comparten información y sincronizan acciones en tiempo real.
- **Autonomía distribuida:** toman decisiones locales sin depender de un controlador central.

# Ventajas declaradas

| Ventaja | Detalle |
|---|---|
| Mayor eficiencia | Ejecución en paralelo, con menores tiempos de ciclo |
| Distribución inteligente | La carga se asigna dinámicamente según capacidad y disponibilidad |
| Decisiones descentralizadas | Se eliminan cuellos de botella jerárquicos |
| Resiliencia | Si un agente falla, los demás siguen operando |

# Reparto humano-agente

| Los agentes aportan | Las personas aportan |
|---|---|
| Velocidad y precisión en tareas estructuradas | Juicio ético y contextual complejo |
| Disponibilidad continua sin fatiga | Creatividad e innovación disruptiva |
| Procesamiento de datos a gran escala | Empatía y gestión de relaciones |

# Cautelas

El curso solo presenta ventajas. La autonomía distribuida choca con los riesgos de
contexto del [harness](/conceptos/harness-diez-fallas-contexto.md), en particular la
inyección indirecta de prompts: un agente que lee la salida de otro hereda su
contexto. Esto es lectura del repo, no del PDF.

[^m2u3]: M2U3 (Unidad 7), slides 9-12.
