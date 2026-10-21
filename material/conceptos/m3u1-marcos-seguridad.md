---
type: Concepto
title: "Marcos de seguridad de IA, para qué sirve cada uno"
description: "Cuándo usar OWASP Top 10 LLM, OWASP Top 10 agéntico, MITRE ATLAS y NIST AI RMF con AI 600-1, según la Clase 9."
tags: [m3, seguridad, marcos, owasp, nist]
sources:
  - id: clase9
    resource: "Hoy atacamos · CAIO Clase 9.pdf"
    title: "Hoy atacamos, CAIO Clase 9, lámina 13"
status: draft
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T14:30:00Z }
---

# Para qué sirve cada marco

Lámina 13, con los nombres tal como figuran:[^clase9]

| Marco | Qué cubre | Lo usás cuando… |
|---|---|---|
| OWASP Top 10 LLM | Los riesgos de la aplicación | revisás una app con LLM antes de salir a producción |
| OWASP Top 10 agéntico 2026 | Los riesgos de los agentes | tu IA ya usa herramientas y toma acciones |
| MITRE ATLAS | Cómo ataca un adversario | armás el plan de red team |
| NIST AI RMF + AI 600-1 | Cómo se gobierna | necesitás políticas, roles y reportes |

# Relación con otras fichas

- La ficha de la [unidad M3U1](/unidades/m3u1-seguridad.md) dice que el curso "no cita
  estándares" y suma OWASP como referencia externa. Eso vale para las 20 slides: esta
  clase sí cita estos cuatro marcos.
- NIST AI RMF ya tiene ficha en [EU AI Act, NIST e ISO](/conceptos/m1u4-eu-ai-act-nist-iso.md);
  el OWASP Top 10 LLM se usa en [prompt injection](/conceptos/m3u1-prompt-injection-jailbreaks.md).
  OWASP agéntico, MITRE ATLAS y NIST AI 600-1 no tienen ficha propia.

# Cautelas

* Ficha nueva, en borrador, sin verificación humana. Cotejo del agente contra la
  lámina 13 el 2026-10-21.
* No se abrieron las fuentes primarias de los cuatro marcos: nombres, ediciones y
  alcance son los de la lámina. Antes de citarlos en el plan, cotejar cada uno contra
  su publicación oficial.

[^clase9]: Hoy atacamos, CAIO Clase 9, lámina 13
