---
type: Concepto
title: Arquitectura organizacional de IA, centralizada, federada o híbrida
description: Tres patrones para decidir dónde vive la capacidad de IA y cómo se relaciona con los equipos de negocio.
tags: [m1, gobierno, operating-model]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Los tres patrones

Definir [decision rights](/conceptos/m1u4-decision-rights.md) resuelve una parte; la
otra es decidir dónde vive la capacidad de IA. "No existe una arquitectura
universal" (p. 3).[^m1u4-lectura]

| Patrón | Cómo funciona | Cuándo sirve | Riesgo |
|---|---|---|---|
| Centralizada | Un equipo central concentra plataforma, expertise, delivery y governance | Organización que empieza, con pocos casos de uso, o que necesita recuperar control sobre una adopción dispersa; facilita estandarizar herramientas y seguridad | El equipo central se vuelve cuello de botella y se aleja del contexto operativo |
| Federada | Las unidades de negocio construyen y operan sus soluciones dentro de estándares comunes; el centro mantiene políticas, plataformas, patrones, monitoreo y governance por excepción | Cuando hay capacidades maduras en los dominios | Duplicación, calidad desigual, herramientas incompatibles y shadow AI si los estándares centrales son débiles |
| Híbrida (hub-and-spoke) | Un núcleo central mantiene plataforma, security, evals, identity, observability y standards; equipos embebidos en los dominios responden por los casos de uso y outcomes | El caso más frecuente en la práctica | Requiere definir con claridad qué es del centro y qué del dominio |

Fuente: sección 1.2, p. 3; resumen en slide 6.[^m1u4-lectura][^m1u4-slides]

# Matices

- Muchas organizaciones no eligen un único modelo para todo: un copiloto para
  empleados puede gobernarse de forma relativamente centralizada, y los agentes que
  transforman procesos core pueden requerir ownership federado en el negocio.
- Microsoft propone elegir la estructura según el patrón de transformación y la
  madurez del dominio.[^m1u4-lectura]

# Síntesis

> Centralizar capacidades compartidas y guardrails; empujar las decisiones de negocio
> al nivel más cercano que pueda tomarlas de forma segura.

"Ese principio no determina un organigrama: ayuda a diseñarlo" (p. 3).[^m1u4-lectura]
La slide 6 lo resume como "centralizar capacidades compartidas, federar decisiones de
negocio donde sea seguro hacerlo".[^m1u4-slides]

# Relación con el plan

Respalda arquitectura organizacional y gobierno. Las capacidades que conviene
centralizar están en [de demo a producción](/conceptos/m1u4-demo-a-produccion.md)
(identity, conectores, evals, observability). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 1.2 (p. 3)
[^m1u4-slides]: M1U4, slide 6
