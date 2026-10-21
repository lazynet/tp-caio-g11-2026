---
type: Concepto
title: AI Council vs AI Center of Excellence
description: Un Council decide y coordina; un CoE habilita y opera. Incluye funciones, temas de cada uno y los anti-patterns de cada diseño.
tags: [m1, gobierno, operating-model]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
status: draft
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Diferencia

| | AI Council | AI Center of Excellence (CoE) |
|---|---|---|
| Naturaleza | Órgano de decisión y coordinación | Capacidad operativa, no solo un comité |
| Participan | AI/Technology, negocio, Security, Legal, Risk, Data y otros según el contexto | Equipo que opera entre reuniones |
| Hace | Políticas y principios comunes, clasificación de riesgo, excepciones relevantes, inversiones transversales, conflictos de ownership, iniciativas de alto impacto, incidentes significativos, cambios regulatorios | Templates, golden paths, estándares, training, herramientas compartidas, métricas, lifecycle y soporte a los equipos |
| Ritmo | Puede reunirse una vez por mes y decidir | Tiene trabajo operativo entre reuniones |
| Nombres alternativos (slide 7) | AI Governance Committee, AI Steering Committee, Responsible AI Council | AI Enablement Team, AI Hub, AI Office |

Fuente: sección 1.3, p. 4; slide 7.[^m1u4-lectura][^m1u4-slides]

El Council "no debería necesitar aprobar cada asistente, prompt o automatización de
bajo riesgo".[^m1u4-lectura] Una organización puede tener ambos, uno solo, o
distribuir esas funciones entre equipos existentes. El nombre importa menos que el
mandato: si principalmente decide, se parece a un Council; si principalmente habilita,
a un CoE (slide 7).[^m1u4-slides]

Microsoft describe **cuatro funciones de un CoE agentic: govern, enable, optimize y
scale**.[^m1u4-lectura]

# Anti-patterns

| Anti-pattern | Qué pasa |
|---|---|
| El gatekeeper | Todo requiere aprobación central y los equipos empiezan a esquivar el proceso |
| El comité fantasma | Existe formalmente, pero sin autoridad, métricas ni decisiones concretas |
| El CoE que construye todo | Quiere ser dueño de cada iniciativa y se vuelve una software factory central |
| El governance perfecto | Se intenta completar toda la política antes de permitir experimentación, y la adopción migra por fuera del sistema oficial |

Microsoft nombra tres de estos (gatekeeper, comité fantasma, governance perfecto) en
su guía de CoE; el CoE que construye todo es una fricción que suma la unidad
(p. 4).[^m1u4-lectura]

"La calidad del operating model se mide menos por cuántos comités existen y más por
si las decisiones ocurren a tiempo, tienen owner y dejan evidencia."[^m1u4-lectura]

# Relación con el plan

Es la pieza central de la sección de Gobierno. Cadencia y registro:
[inventario y operating rhythm](/conceptos/m1u4-inventario-y-operating-rhythm.md).
Mandatos: [decision rights](/conceptos/m1u4-decision-rights.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

# Cautelas

* Cotejada el 2026-10-20 contra M1U4 lectura, p. 4 (sección 1.3) y slides v3, slide 7:
  funciones, temas, nombres alternativos, citas y anti-patterns coinciden. Fiel.
* La slide 7 nombra los anti-patterns con otras palabras y solo tres: "CoE gatekeeper",
  "Consejo que no decide nada" y "Governance tan lento que los equipos lo rodean". La
  tabla de arriba sigue la lectura (cuatro).
* La atribución a Microsoft de las cuatro funciones del CoE y de tres anti-patterns es
  del curso; no se cotejó Microsoft Learn.

[^m1u4-lectura]: M1U4, lectura, sección 1.3 (p. 4)
[^m1u4-slides]: M1U4, slide 7
