---
type: Framework
title: AIMM (Gartner)
description: Modelo de madurez de IA en 5 niveles donde el nivel global lo fija la dimensión más débil; la copia de la cursada es una elaboración independiente, no el informe de Gartner.
tags: [diagnostico, madurez]
status: draft
sources:
  - id: aimm
    resource: AIMM (Gartner) 2026.pdf
    title: AIMM (Gartner), documento de referencia de la cursada (3 págs.)
  - id: gartner-ai
    resource: https://www.gartner.com/en/topics/artificial-intelligence
    title: Gartner, página temática de IA (el informe completo requiere suscripción)
  - id: aimm-sec
    resource: https://blogs.bmc.com/ai-maturity-models/
    title: BMC, AI maturity models (fuente secundaria que reproduce la escala de 5 niveles)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

# Qué es

Escala de 5 niveles que describe la trayectoria típica de una organización al incorporar IA. Su valor es el vocabulario común entre dirección, tecnología y negocio, no la sofisticación.[^aimm] Se usa para ubicar dónde está hoy la organización, qué falta para el nivel siguiente y alinear expectativas entre áreas (p. 1).[^aimm]

# Contenido

* [Los 5 niveles](/frameworks/aimm-niveles.md): señal, síntoma, riesgo dominante y qué hace falta para avanzar.
* [Cómo usarlo en un diagnóstico](/frameworks/aimm-uso-diagnostico.md): evaluar por dimensión, evidencia antes que percepción, no saltear niveles, limitaciones y marcos complementarios.

# Cautelas

**Resuelta en parte.** El PDF aclara que es una elaboración independiente, redactada sin acceso al informe de Gartner ni a la web, y que "puede no coincidir con la caracterización oficial" (p. 3).[^aimm] Se buscó la fuente primaria: el informe de Gartner es de pago y no se pudo leer (la [página temática de Gartner](https://www.gartner.com/en/topics/artificial-intelligence) no publica el modelo)[^gartner-ai]. Lo que se confirmó es solo la **escala de 5 niveles y sus nombres**, que circula en resúmenes secundarios.[^aimm-sec] Un resumen lo escribe "Systematic" en vez de "Systemic": el PDF usa "Systemic".[^aimm-sec]

Lo que **no** está confirmado contra Gartner: los síntomas, riesgos y recomendaciones por nivel, la regla de "la dimensión más débil fija el nivel" y las cinco dimensiones sugeridas. Por eso queda en `draft`: el modelo puede nombrarse como escala pública de 5 niveles, pero no atribuirle a Gartner el detalle ni usarlo en una slide como cifra o criterio de Gartner.

# Respalda

Diagnóstico: ver el [mapa](/mapa-plan-fuentes.md). Para el eje de responsabilidad se combina con [Microsoft RAI](/frameworks/microsoft-rai-maturity.md) y el [EU AI Act](/frameworks/eu-ai-act.md).

[^aimm]: AIMM (Gartner), documento de referencia de la cursada, pp. 1-3
[^gartner-ai]: Gartner, página temática de IA
[^aimm-sec]: BMC, AI maturity models
