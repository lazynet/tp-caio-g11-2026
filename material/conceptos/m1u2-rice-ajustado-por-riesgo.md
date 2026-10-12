---
type: Concepto
title: "RICE ajustado para IA y por riesgo"
description: "Marco RICE (Reach, Impact, Confidence, Effort), por qué el esfuerzo se comprime y la confianza se vuelve más incierta con IA generativa, y el riesgo como factor corrector."
tags: [m1, priorizacion, rice]
sources:
  - id: m1u2
    resource: Módulo 1 — Unidad 2 — Portfolio, priorización y ejecución de los 100 días.pdf
    title: "M1U2, pp. 2, 4 y 8-10"
  - id: rice-productplan
    resource: https://productplan.com/glossary/rice-scoring-model
    title: "ProductPlan, RICE scoring model"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Fórmula

**RICE = (Reach × Impact × Confidence) ÷ Effort**. Produce un puntaje comparable entre iniciativas heterogéneas. Su utilidad no está en la precisión matemática de los inputs sino en "la disciplina de hacer explícitas las suposiciones detrás de cada estimación" y poder debatirlas con el equipo.[^m1u2]

| Componente | Significado |
|---|---|
| Reach | Alcance |
| Impact | Impacto |
| Confidence | Confianza en las estimaciones |
| Effort | Esfuerzo |

[^m1u2]

# Origen

RICE lo desarrolló el equipo de producto de Intercom. En su versión original, el impacto usa niveles discretos (3 masivo, 2 alto, 1 medio, 0,5 bajo, 0,25 mínimo) y la confianza porcentajes (100% alta, 80% media, 50% baja). La fuente consultada es secundaria (ProductPlan); el curso no cita el origen.[^rice-productplan]

# Ajustes para IA generativa (según el curso)

- **Effort se comprime:** herramientas de desarrollo asistido, APIs de modelos y plataformas de agentes permiten prototipos funcionales en días en lugar de semanas. Eso eleva el puntaje RICE de iniciativas que antes parecían costosas y obliga a recalibrar el peso relativo de cada dimensión.
- **Confidence se vuelve más incierta:** los modelos generativos son menos predecibles que el ML clásico, lo que exige más rigor al estimar el impacto esperado.
- **Riesgo como factor corrector:** el RICE clásico no incluye riesgo; debe incorporarse, sobre todo con datos sensibles o decisiones con consecuencias regulatorias.

[^m1u2]

# Qué NO da el curso

El curso **no define una fórmula numérica** para el ajuste por riesgo; solo dice que debe incorporarse "como factor corrector" y que la priorización considera impacto, riesgo, *readiness* y *time-to-value* (título del tema 2).[^m1u2] Cualquier fórmula concreta (por ejemplo, dividir el puntaje RICE por un factor de riesgo regulatorio de 1 a 3) es una propuesta del equipo, no del material.

# Uso en el portfolio

Los 20 a 30 candidatos de la ideación se filtran por factibilidad y se puntúan con "el marco RICE ajustado para IA"; de la lista larga se eligen las 10 mejores. Ver [AI Portfolio 1.0](/conceptos/m1u2-ai-portfolio-1-0.md).[^m1u2]

Relacionado: [matriz factibilidad-impacto](/conceptos/m1u2-matriz-factibilidad-impacto.md) · [pain killer vs vitamina](/conceptos/m1u2-pain-killer-vs-vitamina.md) · unidad [M1U2](/unidades/m1u2-portfolio-100-dias.md).

[^m1u2]: M1U2, pp. 2, 4 y 8-10
[^rice-productplan]: ProductPlan, RICE scoring model
