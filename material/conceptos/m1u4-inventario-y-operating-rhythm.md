---
type: Concepto
title: Inventario de IA y operating rhythm
description: Registro mínimo de sistemas y usos de IA, y la cadencia semanal, mensual y trimestral con la que se gobierna.
tags: [m1, gobierno, operating-model, inventario]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: nist-airmf
    resource: https://www.nist.gov/itl/ai-risk-management-framework
    title: NIST, AI Risk Management Framework
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# AI inventory

"No se puede gobernar lo que no se conoce": una de las primeras capacidades de
governance es un inventario de sistemas y usos de IA. No hace falta una plataforma
sofisticada, alcanza una tabla (p. 5).[^m1u4-lectura]

| Campo |
|---|
| Nombre y propósito |
| Business owner |
| Proveedor y modelo |
| Datos utilizados |
| Usuarios afectados |
| Nivel de [autonomía](/conceptos/m1u4-escala-autonomia-l0-l4.md) |
| Sistemas a los que accede |
| Risk tier |
| Estado del lifecycle |
| Responsable técnico |
| Fecha de última revisión |

**Incluir la IA embebida en software de terceros.** El caso más frecuente no es
construir un agente propio, sino que el CRM, ERP, suite de productividad o sistema de
RRHH active una función de IA. Que la organización no haya construido el modelo no
elimina la necesidad de decidir quién aprueba su activación, qué datos usa, qué
acciones ejecuta y quién responde.[^m1u4-lectura]

NIST AI RMF incluye el inventario dentro de la función **Govern** (GOVERN 1.6),
porque permite responder tanto por un sistema como por el parque completo.[^m1u4-lectura]
La página principal de NIST confirma la versión AI RMF 1.0 de enero de 2023; el
subcontrol GOVERN 1.6 no se verificó en el playbook.[^nist-airmf]

# Operating rhythm

Una política que nadie revisa y un dashboard que nadie mira no son un sistema de
gestión. Ejemplo de la lectura, "no como receta universal" (p. 5):[^m1u4-lectura]

| Cadencia | Temas |
|---|---|
| Semanal | Incidentes, health, nuevos casos y bloqueos |
| Mensual | Portfolio, excepciones, adopción, riesgo y decisiones ejecutivas |
| Trimestral | Valor, maturity, roadmap, inversión, sistemas a escalar o retirar |

Microsoft propone un patrón similar para sus CoE agentic y recomienda integrarlo a
reuniones existentes en vez de crear burocracia paralela.[^m1u4-lectura]

# Fricción real (p. 5-6)

La arquitectura organizacional falla muchas veces por razones poco sofisticadas:
reuniones sin preparación, roles voluntarios sin tiempo asignado, sponsors que dejan
de participar, decisiones que se postergan, comités que revisan temas pero no pueden
resolverlos. Por eso el CAIO diseña también rituales, expectativas y
follow-up.[^m1u4-lectura]

Ver [Council vs CoE](/conceptos/m1u4-council-vs-coe.md) y la unidad
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 1.4 (p. 4-6)
[^nist-airmf]: NIST, AI RMF (consultado el 2026-10-12)
