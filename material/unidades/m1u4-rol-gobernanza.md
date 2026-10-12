---
type: Unidad
title: M1U4 Rol, gobernanza y arquitectura org.
description: Decision rights, escala de autonomía, Governance Stack y marco regulatorio del CAIO.
tags: [m1, gobierno, compliance, defensa]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# De qué trata

La pregunta de la unidad: cómo hacer que una organización use IA con velocidad sin
perder accountability. El CAIO es una función antes que un título; su trabajo es
diseñar el sistema que permite moverse rápido con control (p. 1, slide 1).[^m1u4-lectura]

La unidad tiene la lectura previa de 25 páginas y una presentación de 24 slides para
la clase por Zoom de 90 minutos, con seis ejercicios y un caso integrador.[^m1u4-slides]

# Objetivos de aprendizaje (p. 1)

1. Distinguir la función del CAIO de los cargos del organigrama.
2. Diseñar decision rights básicos.
3. Usar un maturity model como herramienta de diagnóstico y planificación.
4. Asignar ownership y accountability con roles claros y RACI.
5. Diferenciar experimentación, validación y producción.
6. Diseñar gobernanza proporcional al riesgo y a la autonomía de un agente.
7. Entender la relación entre políticas, controles, observabilidad y evidencia.
8. Explicar qué aportan el EU AI Act, NIST AI RMF e ISO/IEC 42001.

# Conceptos de la unidad

| Sección de la lectura (p.) | Concepto |
|---|---|
| 1.1 y 1.4 Decision rights y mandato (2-5) | [Decision rights y mandato del CAIO](/conceptos/m1u4-decision-rights.md) |
| 1.2 Centralizada, federada o híbrida (3) | [Arquitectura organizacional](/conceptos/m1u4-arquitectura-organizacional.md) |
| 1.3 Council vs CoE (4) | [AI Council vs CoE](/conceptos/m1u4-council-vs-coe.md) |
| 1.4 Inventario y operating rhythm (5) | [Inventario y operating rhythm](/conceptos/m1u4-inventario-y-operating-rhythm.md) |
| 2 Readiness y maturity (6-8) | [Microsoft Agentic AI Maturity Model](/conceptos/m1u4-microsoft-agentic-maturity.md) |
| 3 Ownership y RACI (8-10) | [Ownership y RACI](/conceptos/m1u4-raci-ownership.md) |
| 4 Champions y literacy (10-11) | [AI Champions y AI literacy](/conceptos/m1u4-champions-y-literacy.md) |
| 5.1-5.2 Demo a producción (11-12) | [De la demo a producción](/conceptos/m1u4-demo-a-produccion.md) |
| 5.3 AI Economics (13) | [Costo por outcome aceptado](/conceptos/m1u4-costo-por-outcome.md) |
| 6.1 Autonomía (13-14) | [Escala L0-L4](/conceptos/m1u4-escala-autonomia-l0-l4.md) |
| 6.2-6.4 HITL, blast radius y cuatro preguntas (14-15) | [Criterios de gobierno agéntico](/conceptos/m1u4-criterios-gobierno-agentico.md) |
| 7 Governance Stack (15-16) | [AI Governance Stack](/conceptos/m1u4-governance-stack.md) |
| 8 Evals, observability, traceability (17-18) | [Evals, observability y traceability](/conceptos/m1u4-evals-observability-traceability.md) |
| 9 EU AI Act, NIST, ISO (18-20) | [EU AI Act, NIST AI RMF e ISO/IEC 42001](/conceptos/m1u4-eu-ai-act-nist-iso.md), más el [framework EU AI Act](/frameworks/eu-ai-act.md) |
| 10 Caso integrador (20-22) | [Caso Mercurio SA](/casos/m1u4-mercurio-sa.md) |

# Ejercicios

Seis ejercicios con su concepto: 1 ¿necesitamos un CAIO? ([decision rights](/conceptos/m1u4-decision-rights.md)),
2 baseline de madurez ([maturity](/conceptos/m1u4-microsoft-agentic-maturity.md)), 3 ¿quién
es Accountable? ([RACI](/conceptos/m1u4-raci-ownership.md)), 4 18 de 20
([demo a producción](/conceptos/m1u4-demo-a-produccion.md)), 5 ¿dónde cambia el governance?
([criterios](/conceptos/m1u4-criterios-gobierno-agentico.md)) y 6 incidente de agente
([evals y traza](/conceptos/m1u4-evals-observability-traceability.md)).[^m1u4-lectura]

# Los 14 takeaways (p. 22-23)

1. El CAIO es una función antes que un título.
2. Diseñar decision rights es más importante que discutir territorios.
3. La arquitectura puede ser centralizada, híbrida o federada, según madurez, riesgo y capacidad de los dominios.
4. No se puede gobernar lo que no se conoce: inventario mínimo de sistemas, owners y riesgo.
5. AI Readiness no es binaria: se evalúa contra el nivel de capacidad y autonomía que se quiere desplegar.
6. Un maturity model sirve para encontrar gaps, no para obtener una medalla.
7. Business mantiene el ownership del outcome.
8. Governance proporcional al riesgo.
9. Human-in-the-loop no es una solución mágica: demasiadas aprobaciones generan fatiga.
10. Limitar el blast radius puede ser más efectivo que intentar predecir todos los errores.
11. Una demo demuestra posibilidad; producción demuestra repetibilidad.
12. Principios sin controles son aspiraciones.
13. Regulación, risk frameworks y management systems cumplen funciones distintas.
14. El rol del CAIO no es controlar toda la IA.[^m1u4-lectura]

# Citas

"El rol del CAIO no es controlar toda la IA. Es diseñar un sistema que permita a la
organización moverse rápido sin perder accountability." (p. 23)[^m1u4-lectura]

Las seis preguntas del cierre (slide 24): ¿qué queremos lograr con AI?, ¿quién decide
qué?, ¿quién responde por el outcome?, ¿qué puede hacer autónomamente la IA?, ¿cómo
sabemos si funciona y qué hizo?, ¿qué capacidades hay que construir para que escale?
"Velocidad sin perder accountability."[^m1u4-slides]

# Glosario de la lectura (p. 23-24)

Accountable, AI Champion, AI Center of Excellence, AI Inventory, AI Readiness, Blast
radius, Decision rights, Evals, Guardrail, Human-in-the-loop, Observability, RACI y
Traceability. Cada término está definido en el concepto que le corresponde.[^m1u4-lectura]

# Cautelas

La lectura incluye datos de 2026 de terceros (Microsoft, OpenAI, Anthropic, NIST) que
no son citas primarias. Resultado del chequeo web:

- **AI Omnibus (Reg. UE 2026/1744) y guía SIGEN 197/2026: existen**, con las fechas
  de la lectura. Detalle, diferencias y qué falta cotejar en
  [Verificación del AI Omnibus y SIGEN](/conceptos/m1u4-ai-omnibus-sigen.md).
- **Corrección pendiente:** el alcance del art. 4 (AI literacy) tras el Omnibus: las
  fuentes secundarias describen una obligación más liviana que la de la lectura.
- Los números de Anthropic (por ejemplo, 93% de permission prompts aprobados) y el
  marco Exploration / Validation / Production de OpenAI son citas de segunda mano, sin
  verificar.
- No va en una slide una cifra o fecha normativa sin chequear el Official Journal.

# Respalda

Gobierno, compliance, arquitectura, people plan, finanzas y defensa: ver el
[mapa](/mapa-plan-fuentes.md).

[^m1u4-lectura]: M1U4, lectura de 25 páginas
[^m1u4-slides]: M1U4, slides v3 (24 slides)
