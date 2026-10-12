---
type: Concepto
title: "Diseño para escalar: métricas, ownership, SLOs y compliance"
description: "Los cuatro elementos que hay que definir desde el día uno para que un piloto pueda escalar, con ejemplo de SLO y mapeo de compliance."
tags: [m1, slo, escalado]
sources:
  - id: m1u2
    resource: Módulo 1 — Unidad 2 — Portfolio, priorización y ejecución de los 100 días.pdf
    title: "M1U2, pp. 2 y 6"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Principio

Un piloto exitoso que no puede escalar es "en el mejor de los casos, un aprendizaje; en el peor, un costo hundido". El diseño para escalar empieza el primer día.[^m1u2]

# Los cuatro elementos

| Elemento | Qué define |
|---|---|
| Métricas de éxito | Qué se mide y cómo; **métricas de negocio**, no solo técnicas. "La precisión del modelo es un input; la reducción del tiempo de procesamiento de facturas en un 40% es el output que le importa al CFO." |
| Ownership | Quién responde por el sistema en producción, con responsable en el área de negocio, no solo en el equipo de IA. Sin eso los sistemas se degradan sin que nadie lo note o se abandonan al cambiar el sponsor |
| SLOs | Umbrales de desempeño aceptables |
| Modelo de compliance | Cómo se garantiza el cumplimiento a medida que crece el sistema |

[^m1u2]

# SLO (Service Level Objective)

Objetivo cuantificable de desempeño de un sistema de IA en producción (precisión mínima, latencia máxima, tasa de falsos positivos aceptable). Es "el puente entre la promesa técnica y el contrato operativo con el negocio".[^m1u2]

**Ejemplo del curso (clasificador de documentos):** precisión superior al 92% medida semanalmente y respuesta inferior a 2 segundos en el percentil 95; si cae por debajo del umbral se activa un protocolo de revisión.[^m1u2]

# Mapeo de compliance

El compliance se mapea al AI Act (sistemas desplegados en la UE), al NIST AI RMF y a marcos sectoriales cuando aplican. Las herramientas de gobernanza de IA pueden automatizar la recolección de evidencias y mapear controles a varios marcos a la vez. La ISO/IEC 42001 y la Estrategia de IA 2024 de España enfatizan ownership documentado y métricas alineadas con los objetivos estratégicos.[^m1u2] Ambas referencias existen (ver [cautelas](/conceptos/m1u2-cautelas-citas-regulatorias.md)).

Relacionado: [kill/scale gates](/conceptos/m1u2-kill-scale-gates.md) · unidad [M1U2](/unidades/m1u2-portfolio-100-dias.md).

[^m1u2]: M1U2, pp. 2 y 6
