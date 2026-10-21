---
type: Concepto
title: "Kill/scale gates y revisión trimestral"
description: "Puntos de decisión formales para descontinuar, mantener o acelerar iniciativas, con condiciones típicas y ritmo de revisión trimestral."
tags: [m1, gates, portfolio]
sources:
  - id: finma-08-2024
    resource: https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/4dokumentation/finma-aufsichtsmitteilungen/20241218-finma-aufsichtsmitteilung-08-2024.pdf
    title: "FINMA, Guidance 08/2024, Governance and risk management when using artificial intelligence (18-12-2024)"
  - id: m1u2
    resource: Módulo 1 — Unidad 2 — Portfolio, priorización y ejecución de los 100 días.pdf
    title: "M1U2, pp. 2, 8 y 11"
status: draft
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Definición

Punto de decisión formal del ciclo de vida de una iniciativa donde se evalúa, con criterios predefinidos, si se **descontinúa** (kill), se **mantiene** o se **acelera a escala** (scale). Impide que pilotos fallidos consuman recursos indefinidamente.[^m1u2]

# Condiciones típicas

| Gate | Se activa cuando |
|---|---|
| Kill | La iniciativa no alcanza sus métricas de éxito en el piloto; el costo de implementación supera el ROI proyectado; cambia el contexto de negocio que la justificaba |
| Scale | El piloto supera sus métricas; el área de negocio confirma el valor percibido; existe la infraestructura para escalar |

[^m1u2]

Ambos deben ser decisiones **formales, documentadas y comunicadas**, no conversaciones informales. Sin ellos el portfolio acumula "proyectos zombis": pilotos que nunca terminan, sistemas que nadie usa pero nadie se atreve a matar.[^m1u2]

# Ejemplo del curso (clasificación de documentos)

- SLO: precisión ≥ 90% en categorías principales, medida en las primeras 500 transacciones del piloto.
- **Kill gate:** si a las 6 semanas la precisión es inferior al 80% o la implementación supera las 10 semanas, se revisa la decisión de agentificar y se evalúa comprar.
- **Scale gate:** si la precisión supera el 90% y operaciones confirma la reducción de tiempo, se escala al 100% del volumen en la semana 8.

[^m1u2]

# Revisión trimestral

Cada trimestre se revisa cada iniciativa contra sus métricas, se aplican los gates, se incorporan iniciativas nuevas y se actualizan prioridades. También se actualiza el inventario de sistemas de IA que exige el AI Act, para que la clasificación de riesgo refleje el estado actual.[^m1u2]

**Cautela:** el curso atribuye el ciclo trimestral a la FINMA Guidance 08/2024. El texto original no menciona ciclos trimestrales ni de ninguna frecuencia (ver [cautelas](/conceptos/m1u2-cautelas-citas-regulatorias.md)). El ritmo trimestral es una práctica del curso, no un requisito de FINMA.[^finma-08-2024]

# Relacionado

[Kill-fast](/conceptos/m1u1-kill-fast.md) (versión de experimento individual) · [AI Portfolio 1.0](/conceptos/m1u2-ai-portfolio-1-0.md) · [diseño para escalar](/conceptos/m1u2-diseno-para-escalar-slos.md) · unidad [M1U2](/unidades/m1u2-portfolio-100-dias.md). El programa pide un AI Portfolio "con reglas de kill/scale" como artefacto: ver [artefactos](/conceptos/programa-artefactos.md).

# Cautelas

- **Cotejada contra el PDF** (2026-10-20): M1U2, pp. 2 (definición), 8 (Tema 6: condiciones de los gates, proyectos zombis, revisión trimestral) y 11 (Paso 4, ejemplo de clasificación de documentos). Condiciones, umbrales (90%, 80%, 6 y 10 semanas, 100% en la semana 8) coinciden con el texto. La cita anterior incluía la p. 7, que no trata gates (la sección empieza al final de esa página y los gates están en la p. 8).
- **FINMA cotejada contra el PDF primario** (2026-10-20): el comunicado no fija ninguna frecuencia de revisión, trimestral ni de otro tipo; sí menciona controles regulares y monitoreo continuo (sección 2.4). El ritmo trimestral es práctica del curso.
- **"Inventario que exige el AI Act":** es la formulación del curso; no se cotejó contra el articulado. Antes de afirmarlo como obligación, ver [AI Act](/frameworks/eu-ai-act.md).
- **Los umbrales del ejemplo son ilustrativos del curso**, no valores recomendados para ningún caso real.

[^finma-08-2024]: FINMA, Guidance 08/2024, Governance and risk management when using artificial intelligence (18-12-2024)
[^m1u2]: M1U2, pp. 2, 8 y 11
