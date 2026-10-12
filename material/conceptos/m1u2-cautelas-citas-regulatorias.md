---
type: Concepto
title: "Verificación de citas regulatorias de M1U1 y M1U2"
description: "Qué es cada norma o fuente que citan las unidades M1U1 y M1U2, qué se confirmó contra la fuente primaria y qué dijo mal el curso."
tags: [m1, cautelas, compliance, verificacion]
sources:
  - id: ai-act-comision
    resource: https://commission.europa.eu/news/ai-act-enters-force-2024-08-01_en
    title: 'Comisión Europea, "AI Act enters into force" (01-08-2024)'
  - id: ai-act-eurlex
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    title: "Reglamento (UE) 2024/1689, DOUE L, 12-07-2024"
  - id: es-ia-2024
    resource: https://digital.gob.es/comunicacion/notas-prensa/secretaria-digitalizacion-e-inteligencia-artificial/2024/05/2024-05-14
    title: "Gobierno de España, nota de prensa sobre la Estrategia de IA 2024 (14-05-2024)"
  - id: finma-08-2024
    resource: https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/4dokumentation/finma-aufsichtsmitteilungen/20241218-finma-aufsichtsmitteilung-08-2024.pdf
    title: "FINMA, Guidance 08/2024, Governance and risk management when using artificial intelligence (18-12-2024)"
  - id: finma-mll
    resource: https://www.mll-news.com/finma-guidance-08-2024-governance-and-risk-management-when-using-artificial-intelligence?lang=en
    title: "MLL Legal, resumen de la FINMA Guidance 08/2024 (10-01-2025)"
  - id: iso-42001
    resource: https://webstore.iec.ch/publication/90574
    title: "IEC Webstore, ISO/IEC 42001:2023"
  - id: m1u1-extendida
    resource: Módulo 1 — Unidad 1 — Mentalidad CAIO y liderazgo en la era IA.pdf
    title: "M1U1 extendida, pp. 1-2"
  - id: m1u2
    resource: Módulo 1 — Unidad 2 — Portfolio, priorización y ejecución de los 100 días.pdf
    title: "M1U2, pp. 1, 5-8 y 12"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Resumen

| Cita del curso | Resultado | Detalle |
|---|---|---|
| FINMA Guidance 08/2024 | Confirmada, es **suiza**; el curso le atribuye algo que no dice | Ver abajo |
| Reglamento (UE) 2024/1689 "aprobado en junio de 2024" (M1U2) | Parcialmente correcto | Se firmó en junio y se publicó el 12-07-2024 |
| Reglamento "en vigor desde julio de 2024" (M1U1) | **Incorrecto** | Entró en vigor el 1-08-2024 |
| ISO/IEC 42001 | Confirmada | Estándar de sistema de gestión de IA, diciembre de 2023 |
| Estrategia de IA 2024 de España | Confirmada | Aprobada el 14-05-2024 |
| RICE | Confirmado | Origen en Intercom |
| AI Maturity Model de Gartner, NovaGob (2024) | Sin verificar | Ver [AIMM (Gartner)](/frameworks/aimm-gartner.md) |

# FINMA Guidance 08/2024

**Qué es.** Comunicado de supervisión de la FINMA, la autoridad suiza de supervisión de los mercados financieros, publicado el **18 de diciembre de 2024**, titulado "Governance and risk management when using artificial intelligence". Aplica a instituciones supervisadas en Suiza; no es norma de la UE ni de Argentina.[^finma-08-2024]

**Qué dice.** Suiza no tiene legislación específica de IA; los requisitos de gobernanza y gestión de riesgos ya vigentes, neutrales en tecnología y basados en principios, cubren los riesgos de la IA. Las observaciones de supervisión se agrupan en siete áreas: gobernanza; inventario y clasificación de riesgo; calidad de datos; pruebas y monitoreo continuo; documentación; explicabilidad; y revisión independiente.[^finma-08-2024] Hay un inventario gestionado centralmente con clasificación de riesgo, definición de responsabilidades, requisitos de testeo, estándares de documentación y capacitación amplia.[^finma-08-2024]

**Lo que el curso afirma y el texto no respalda.** M1U2 dice que FINMA "establece ciclos de revisión trimestrales o según criticidad para la gestión de portafolios de IA".[^m1u2] En el texto primario completo no aparece ninguna frecuencia de revisión, y tampoco una gestión de "portafolios". Lo más cercano es que el riesgo se pondera por materialidad y probabilidad, y que los tests y el monitoreo son continuos y definidos de antemano; ninguna frecuencia es trimestral.[^finma-08-2024] Un resumen jurídico independiente tampoco menciona ciclos trimestrales.[^finma-mll]

**Cómo usarla en el plan.** Citarla como referencia suiza de buenas prácticas para entidades financieras (inventario con clasificación de riesgo, independencia de la revisión, monitoreo de deriva de datos), nunca como obligación para Flexibility ni como fuente del ritmo trimestral. Los clientes argentinos o internacionales de Flexibility no están sujetos a ella salvo que operen en Suiza (a verificar caso a caso).

# Reglamento (UE) 2024/1689 (AI Act)

- Publicado en el Diario Oficial el **12 de julio de 2024**.[^ai-act-eurlex]
- Entró en vigor el **1 de agosto de 2024**, según la Comisión Europea.[^ai-act-comision]
- M1U1 dice "en vigor desde julio de 2024", lo que es incorrecto; M1U2 dice "aprobación ... en junio de 2024", que alude a la firma del acto, no a su entrada en vigor.[^m1u1-extendida][^m1u2]
- El calendario de aplicación escalonada (2025-02-02, 2025-08-02, 2026-08-02 y siguientes) está en [EU AI Act](/frameworks/eu-ai-act.md). El AI Omnibus (Reg. UE 2026/1744) modificó ese calendario: ver [calendario y sanciones](/frameworks/eu-ai-act-calendario-sanciones.md). Antes de citar fechas en una slide, chequear el texto consolidado en EUR-Lex.[^ai-act-eurlex]

# ISO/IEC 42001 y Estrategia de IA 2024 de España

- ISO/IEC 42001:2023 es el primer estándar internacional de sistema de gestión de IA (AIMS): requisitos para establecer, operar, mantener y mejorar un sistema de gestión de IA. Es certificable de forma voluntaria.[^iso-42001]
- La Estrategia de IA 2024 la aprobó el Consejo de Ministros el 14-05-2024: 3 ejes, 8 palancas y 1.500 millones de euros adicionales para 2024-2025 según el comunicado oficial.[^es-ia-2024] Es una referencia española; no aplica a Argentina.

# Relacionado

[Kill/scale gates](/conceptos/m1u2-kill-scale-gates.md) · [build/buy/agentificar](/conceptos/m1u2-build-buy-agentificar.md) · [diseño para escalar](/conceptos/m1u2-diseno-para-escalar-slos.md) · unidad [M1U2](/unidades/m1u2-portfolio-100-dias.md).

[^ai-act-comision]: Comisión Europea, "AI Act enters into force" (01-08-2024)
[^ai-act-eurlex]: Reglamento (UE) 2024/1689, DOUE L, 12-07-2024
[^es-ia-2024]: Gobierno de España, nota de prensa sobre la Estrategia de IA 2024 (14-05-2024)
[^finma-08-2024]: FINMA, Guidance 08/2024, Governance and risk management when using artificial intelligence (18-12-2024)
[^finma-mll]: MLL Legal, resumen de la FINMA Guidance 08/2024 (10-01-2025)
[^iso-42001]: IEC Webstore, ISO/IEC 42001:2023
[^m1u1-extendida]: M1U1 extendida, pp. 1-2
[^m1u2]: M1U2, pp. 1, 5-8 y 12
