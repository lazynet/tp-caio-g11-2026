---
type: Concepto
title: AI Champions y AI literacy
description: Por qué una red de champions no se activa sola, qué hace falta para que funcione y qué es AI literacy, con la corrección sobre el artículo 4 del AI Act.
tags: [m1, people, adopcion, literacy]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
  - id: cooley-omnibus
    resource: https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
    title: Cooley, Digital AI Omnibus delays key deadlines and introduces new rules
  - id: abreu-omnibus
    resource: https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/
    title: Abreu Advogados, Digital Omnibus Regulation on AI, the key amendments to the AI Act
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# AI Champions

Los casos valiosos aparecen cerca del trabajo (ventas, operaciones, finanzas,
soporte, logística, RRHH, producto). El champion conecta el dominio con la capacidad
de IA de la organización. El nombre no es estándar; la función sí (p. 10).[^m1u4-lectura]

Un champion efectivo puede detectar oportunidades reales, traducir problemas del
área, acompañar la adopción, compartir patrones que funcionaron, identificar riesgos
o fricciones antes que un equipo central y llevar feedback a Product, Platform o AI
governance. No necesita ser especialista en ML ni reportar al CAIO.[^m1u4-lectura]

## Teoría vs. realidad

Experiencia del docente: designó champions, se reunieron, y "algunos no preparan
material, otros no vienen, cada uno está absorbido por sus prioridades y las
reuniones fácilmente se convierten en status meetings" (p. 10, slide 14).[^m1u4-lectura][^m1u4-slides]
Nombrar champions no crea capacidad por sí solo.

Qué hace falta para que funcione:

- tiempo explícitamente asignado por sus managers;
- una expectativa concreta de qué traer a cada encuentro;
- problemas o experimentos reales para compartir, no solo novedades;
- ownership rotativo de demos o aprendizajes;
- un canal entre reuniones para pedir ayuda y reutilizar soluciones;
- reconocimiento o incentivos, aunque no sean monetarios;
- alguien que opere la comunidad y haga follow-up.

La slide 14 lo resume como "mandato explícito, sponsor y un deliverable concreto".[^m1u4-slides]

Microsoft incluye champions y comunidades de práctica como mecanismos de madurez, y
advierte que depender de pocos champions sin un sistema de enablement es un
antipatrón. OpenAI, con entrevistas a BBVA, Philips, JetBrains y Scania, destaca
cultura antes que tooling, governance como habilitador, ownership local y calidad
definida antes de escalar (p. 11). Ambas son citas de segunda mano de la lectura.[^m1u4-lectura]

# AI literacy

No debería reducirse a enseñar prompts. A medida que los sistemas ganan autonomía, la
persona necesita criterio para (p. 11):[^m1u4-lectura]

- saber qué puede delegar;
- comprender qué información no debería compartir;
- reconocer outputs que requieren verificación;
- entender límites y fuentes de error;
- decidir cuándo aplicar juicio humano;
- supervisar agentes sin caer en aprobación mecánica;
- reportar incidentes o comportamientos inesperados.

La madurez cultural aparece cuando la organización deja de medir "usuarios con
licencia" y mide si las personas incorporan IA de manera útil y responsable.

## Corrección sobre el artículo 4 del AI Act

La lectura afirma que el art. 4, modificado por el Reglamento (UE) 2026/1744, "exige a
providers y deployers tomar medidas" para desarrollar AI literacy, y la slide 14 lo
presenta como obligación.[^m1u4-lectura][^m1u4-slides] **Las fuentes secundarias
consultadas dicen lo contrario en el matiz:** tras el Omnibus, la obligación deja de
exigir que providers y deployers "aseguren" la competencia del personal; pasa a que la
Comisión y los Estados miembros "apoyen y faciliten" el desarrollo de AI literacy. El
artículo se mantiene, pero la carga sobre cada organización baja.[^cooley-omnibus][^abreu-omnibus]

Tratalo como **no resuelto**: no se leyó el texto consolidado del Official Journal.
Para una slide, no afirmar que el art. 4 "obliga" a Acme Labs a capacitar; sí que
la AI literacy es una práctica recomendada y está en el texto. Ver
[AI Omnibus y SIGEN](/conceptos/m1u4-ai-omnibus-sigen.md).

# Relación con el plan

Respalda el people plan y el roadmap cultural. Ver también
[M3U2](/unidades/m3u2-cambio-literacy.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 4 (p. 10-11)
[^m1u4-slides]: M1U4, slide 14
[^cooley-omnibus]: Cooley, sobre Reg. (UE) 2026/1744 (consultado el 2026-10-12)
[^abreu-omnibus]: Abreu Advogados, sobre Reg. (UE) 2026/1744 (consultado el 2026-10-12)
