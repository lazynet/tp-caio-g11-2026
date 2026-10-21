---
type: Concepto
title: BAIC, perfiles y selección de tecnología
description: Los tres perfiles organizacionales (usuario, adaptador, desarrollador) y la opción entre herramientas propietarias y open source.
tags: [build-buy, people]
sources:
  - id: baic
    resource: BAIC - Guia GenAi.pdf
    title: BAIC, Guía GenAI, p. 16
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
status: draft
---

Parte de [BAIC, Guía GenAI](/frameworks/baic-guia-genai.md); corresponde a los pasos 3 y 4 de la [metodología](/frameworks/baic-metodologia-7-pasos.md).

# Perfiles según el nivel de implementación

| Perfil | Qué hace |
|---|---|
| Usuario | Usa soluciones existentes, comerciales o propias, en su actividad diaria, bajo políticas de responsabilidad y uso de IA generativa |
| Adaptador | Customiza código abierto (tras analizar políticas de uso y comercialización) en soluciones propias |
| Desarrollador | Evoluciona los modelos fundacionales |

# Selección de tecnología

| Opción | Tradeoff según la guía |
|---|---|
| Herramientas propietarias | Recelos de privacidad por los datos utilizados |
| Desarrollo propio sobre open source | Mayor control de privacidad y seguridad |

La guía solo plantea estas dos opciones; el tercer camino (partner) del plan es criterio propio, no de BAIC.[^baic]

# Cautelas

Cotejada contra la p. 16 de la guía (pasos 3 y 4). Se corrigió la tabla de selección:
la versión anterior atribuía "rapidez" a las herramientas propietarias, y la guía no
lo dice; solo menciona los recelos de privacidad. Los pasos 3 y 4 de la guía
(p. 16) incluyen además presupuesto de cómputo y licencias, y criterios de selección
(caso de uso, tipo y calidad de datos, recursos), que esta ficha no recoge.

[^baic]: BAIC, Guía GenAI, p. 16
