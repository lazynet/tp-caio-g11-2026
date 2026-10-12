---
type: Concepto
title: EU AI Act, NIST AI RMF e ISO/IEC 42001 según la cursada
description: Qué función cumple cada marco (ley, marco de riesgo, sistema de gestión), qué dice el curso de cada uno y qué se verificó contra fuentes primarias.
tags: [m1, compliance, regulacion, nist, iso]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
  - id: nist-airmf
    resource: https://www.nist.gov/itl/ai-risk-management-framework
    title: NIST, AI Risk Management Framework
  - id: iso-42001
    resource: https://www.iso.org/standard/81230.html
    title: ISO, ISO/IEC 42001:2023
  - id: cooley-omnibus
    resource: https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
    title: Cooley, Digital AI Omnibus delays key deadlines and introduces new rules
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Tres marcos, tres funciones

"Los tres aparecen juntos, pero responden preguntas diferentes" (p. 18). Se pueden
mapear controles entre ellos, pero conviene entender primero qué función cumple cada
uno.[^m1u4-lectura]

| Marco | Qué es | Pregunta práctica |
|---|---|---|
| EU AI Act | Regulación con fuerza legal en su ámbito de aplicación (**LAW**) | ¿Qué obligaciones legales aplican a este sistema y a nuestro rol? |
| NIST AI RMF | Framework voluntario de gestión de riesgo (**RISK FRAMEWORK**) | ¿Cómo identificamos, medimos y administramos riesgos de IA? |
| ISO/IEC 42001 | Standard de management system (**MANAGEMENT SYSTEM**) | ¿Cómo institucionalizamos procesos repetibles para gestionar IA? |

Fuente: sección 9, p. 18-20; slide 22. Takeaway 13: "se pueden complementar, pero no
son intercambiables" (p. 22-23).[^m1u4-lectura][^m1u4-slides]

# EU AI Act, lo que vale la pena saber como CAIO

Reglamento (UE) 2024/1689, marco legal europeo basado en riesgo, en vigor desde el 1
de agosto de 2024, con obligaciones por etapas (p. 19). Texto y calendario original en
[EU AI Act](/frameworks/eu-ai-act.md).[^m1u4-lectura]

La pregunta temprana del lifecycle: "¿Qué rol tenemos bajo la norma, en qué categoría
cae el sistema y qué obligaciones se activan?" Dos ejemplos: un FAQ interno de
políticas tiene un perfil regulatorio muy distinto al de un sistema que decide sobre
personas; la IA para filtrar CVs cae en empleo y gestión de trabajadores
(high-risk), con documentación, oversight, logging y risk management mucho más
pesados. "La lección no es evitar casos regulados; es identificar temprano cuándo la
regulación cambia el costo y el diseño del sistema."[^m1u4-lectura]

## Calendario según la lectura, contrastado con la web

| Obligación | Lo que dice la lectura | Verificación |
|---|---|---|
| Art. 50 transparencia | Aplica desde el 2 de agosto de 2026 | Coincide: sin cambios con el Omnibus.[^cooley-omnibus] Existe un período de gracia hasta el 2 de diciembre de 2026 para el marcado del art. 50(2) de sistemas ya en el mercado |
| High-risk Anexo III (empleo, educación, biometría, infraestructura crítica, migración) | Desde el 2 de diciembre de 2027 | Coincide con Cooley (antes: 2 de agosto de 2026) |
| IA integrada en productos regulados (Anexo I) | Se extendió al 2 de agosto de 2028 | Coincide con Cooley (antes: 2 de agosto de 2027) |
| Guidelines de transparencia de la Comisión | Publicadas el 20 de julio de 2026 | **No verificado** |

Detalle y fuentes en [AI Omnibus y SIGEN](/conceptos/m1u4-ai-omnibus-sigen.md). Cautela
para el plan: el Anexo III 5.b (scoring crediticio) es lo que toca a clientes
bancarios; en el calendario de arriba aplica desde 2027, no desde 2026.

## Contexto argentino

No existe un régimen general equivalente, pero siguen vigentes la **Ley 25.326** de
Protección de los Datos Personales, su reglamentación y las normas sectoriales; el
sector público nacional ya tiene la guía SIGEN de controles de IA; y para empresas con
impacto en la UE debe analizarse el alcance extraterritorial (p. 19).[^m1u4-lectura]
La slide 22 dice: "Argentina no tiene todavía una ley específica de IA. Para empresas
locales, el EU AI Act importa sobre todo por extraterritorialidad y operaciones en la
UE".[^m1u4-slides]

# NIST AI RMF

- AI RMF 1.0, publicado en 2023, sigue vigente "aunque NIST informa que está en
  proceso de revisión" (p. 19).[^m1u4-lectura] **Confirmado:** la página de NIST dice
  "AI RMF 1.0 is being revised as part of the White House AI Action Plan"; fecha de
  lanzamiento 26 de enero de 2023.[^nist-airmf]
- Voluntario. Core en cuatro funciones (p. 20):[^m1u4-lectura]

| Función | Qué hace |
|---|---|
| Govern | Definir políticas, roles, cultura y accountability para administrar riesgo (incluye el inventario de sistemas, GOVERN 1.6) |
| Map | Entender contexto, propósito, stakeholders, impactos y riesgos posibles |
| Measure | Evaluar y monitorear riesgos y características relevantes con métricas y métodos apropiados |
| Manage | Priorizar, tratar, monitorear y responder a los riesgos identificados |

Orden mnemotécnico de la slide 22: Govern → Map → Measure → Manage.[^m1u4-slides]
"El valor de NIST no es funcionar como checklist mecánico": el Playbook aclara que las
acciones sugeridas se adaptan al contexto.[^m1u4-lectura]

# ISO/IEC 42001

Define requisitos para establecer, implementar, mantener y mejorar continuamente un
**Artificial Intelligence Management System (AIMS)**. Su lógica es la de ISO 27001:
políticas, objetivos, responsabilidades, gestión de riesgos y oportunidades,
procesos, monitoreo y mejora continua (p. 20).[^m1u4-lectura]

**Confirmado:** ISO/IEC 42001:2023, Edición 1, publicada en diciembre de 2023, aplica a
organizaciones de cualquier tamaño que provean o usen sistemas de IA. Fuente: listado
oficial de ISO. La afirmación de la lectura "vigente a agosto de 2026" no se pudo
contrastar con una fuente que lo diga explícitamente; el listado no muestra una edición
posterior.[^iso-42001]

# Relación con el plan

Respalda la sección de Compliance. El stack operativo está en el
[Governance Stack](/conceptos/m1u4-governance-stack.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md). Caso de aplicación:
[Mercurio SA](/casos/m1u4-mercurio-sa.md), parte 5.

[^m1u4-lectura]: M1U4, lectura, sección 9 (p. 18-20)
[^m1u4-slides]: M1U4, slide 22
[^nist-airmf]: NIST, AI RMF (consultado el 2026-10-12)
[^iso-42001]: ISO, ISO/IEC 42001:2023 (consultado el 2026-10-12)
[^cooley-omnibus]: Cooley, Digital AI Omnibus (consultado el 2026-10-12)
