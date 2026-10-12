---
type: Caso
title: "Caso: AI Portfolio inicial en una financiera de 350 empleados"
description: "Ejemplo aplicado del curso: 24 candidatos, 3 pain killers, business cases, SLOs y gates, y presentación del portfolio en el día 95."
tags: [m1, caso, portfolio]
sources:
  - id: m1u2
    resource: Módulo 1 — Unidad 2 — Portfolio, priorización y ejecución de los 100 días.pdf
    title: "M1U2, pp. 9-11"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Contexto

Empresa de servicios financieros con operaciones en España. El responsable de transformación digital asume el rol de CAIO interno y tiene 100 días para presentar el AI Portfolio 1.0 al comité de dirección.[^m1u2] Montos y ROI son ilustrativos del curso, no benchmarks verificados.

# Pasos

**Paso 1, diagnóstico (días 1-30).** Entrevistas con los directores de cinco áreas (operaciones, riesgos, atención al cliente, finanzas, tecnología). 24 candidatos. Tres fuentes de datos bien estructuradas (CRM, ERP, gestión de riesgos) y dos caóticas (correo y documentos no estructurados). Ya existían dos iniciativas sin coordinación: un chatbot de atención (piloto sin métricas) y un scoring de crédito (en producción sin SLOs); ambas entran al inventario del AI Act con su clasificación.[^m1u2]

**Paso 2, filtrado y priorización (días 31-45).** Matriz factibilidad-impacto: se descartan 8 por baja factibilidad; los 16 restantes se puntúan con RICE; se identifican 3 pain killers:[^m1u2]

| Pain killer | Dolor actual | Decisión |
|---|---|---|
| Clasificación de documentos de onboarding | 4 horas por cliente, estimado 45 minutos | Agentificar |
| Resumen de llamadas | 12 agentes dedican 20% del tiempo a documentar | Buy |
| Detección de anomalías en transacciones | Finanzas revisa 300 transacciones semanales a mano | Build |

[^m1u2]

**Paso 3, business case de las 3 prioritarias.**

| Iniciativa | Inversión estimada | ROI a 12 meses | Riesgo AI Act | Time-to-value |
|---|---|---|---|---|
| Clasificación de documentos | 15.000 € + 2 meses de equipo | 3,2× | Bajo | 6 semanas |
| Resumen de llamadas | 8.400 €/año (SaaS) | 2,8× | Bajo | 3 semanas |
| Detección de anomalías | 45.000 € + 4 meses de equipo | 4,1× | Alto (requiere inventario AI Act) | 16 semanas |

[^m1u2]

**Paso 4, SLOs y gates.** Ver [kill/scale gates](/conceptos/m1u2-kill-scale-gates.md): precisión ≥ 90%; kill gate a las 6 semanas si baja de 80% o la implementación pasa de 10 semanas; scale gate al superar 90%, con escala total en la semana 8.[^m1u2]

**Paso 5, presentación (día 95).** El comité recibe las 10 iniciativas, los 3 quick wins con resultados preliminares (el resumen de llamadas ya en producción con métricas positivas), el inventario de IA para el AI Act, el modelo de ownership con responsables por área y el calendario de revisión trimestral. Aprueba presupuesto para las 7 iniciativas restantes y fija la primera revisión en el mes 4.[^m1u2]

# Lecciones

- Las decisiones build/buy/agentificar varían por caso según sensibilidad de datos y riesgo regulatorio, no hay una respuesta única.
- El inventario del AI Act empieza en el diagnóstico, incluso con iniciativas ya existentes.
- Nota de lectura: el ROI de 4,1× corresponde a la iniciativa de mayor riesgo y mayor tiempo (16 semanas), lo que contradice que los quick wins sean la fuente principal de retorno; el curso no lo discute.

Conceptos: [build/buy/agentificar](/conceptos/m1u2-build-buy-agentificar.md), [plan de 100 días](/conceptos/m1u2-plan-100-dias.md), [AI Portfolio 1.0](/conceptos/m1u2-ai-portfolio-1-0.md). Unidad: [M1U2](/unidades/m1u2-portfolio-100-dias.md).

[^m1u2]: M1U2, pp. 9-11
