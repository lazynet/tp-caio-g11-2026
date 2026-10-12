---
type: Concepto
title: Microsoft Agentic AI Adoption Maturity Model y AI readiness
description: Modelo de madurez de Microsoft con 5 pilares y 5 niveles, y el uso que le da la unidad como assessment de los primeros 30 días.
tags: [m1, gobierno, madurez, readiness]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
  - id: ms-maturity
    resource: https://learn.microsoft.com/agents/adoption-maturity-model/
    title: Microsoft Learn, Agentic AI adoption maturity model
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# AI readiness

Capacidad actual de una organización para adoptar y escalar **un determinado nivel**
de uso de IA de forma efectiva, segura y sostenible (p. 6, slide 8).[^m1u4-lectura]
No es binaria: se puede estar listo para un copiloto que resume documentos y no
para un agente con escritura sobre el ERP, delegar decisiones de crédito, automatizar
contratación u operar agentes autónomos con información sensible.[^m1u4-lectura]

No existe un estándar universal. El valor del maturity model "no está en obtener un
número para presentar al directorio, sino en convertir percepciones vagas en
evidencia, gaps y prioridades".[^m1u4-lectura]

# Los 5 pilares y 5 niveles

Confirmado contra la página de Microsoft Learn (`updated_at` 2026-09-30).[^ms-maturity] La lectura dice "publicado en mayo de 2026"; la página muestra
`ms.date` de marzo y actualización de septiembre de 2026, así que esa fecha no se
pudo confirmar (los pilares y niveles sí coinciden).[^ms-maturity]

| Pilar | Qué cubre según Microsoft |
|---|---|
| AI Strategy & Experience | Alinear iniciativas con objetivos de negocio, prioridades de liderazgo, estrategia de largo plazo y experiencia de usuario |
| Business Strategy | Rediseñar procesos de punta a punta para colaboración humano-agente, medir impacto y optimizar la realización de valor |
| AI Governance & Security | Guardrails, controles, supervisión, gestión operativa y governance del ciclo de vida para riesgo y compliance a medida que escala |
| Technology & Data | Fundaciones técnicas escalables y seguras, arquitecturas y patrones de acceso a datos |
| Organization & Culture | Personas, roles, incentivos y formas de trabajo que sostienen la adopción |

| Nivel | Descripción |
|---|---|
| 100, Initial | Iniciativas no planificadas y experimentales; capacidades inconsistentes, aisladas y dependientes de individuos |
| 200, Repeatable | Empiezan patrones y prácticas repetibles, aún informales y desparejas |
| 300, Defined | Capacidades definidas, documentadas y respaldadas por governance, estándares y operating model |
| 400, Capable | Agentes embebidos en planificación y operación; procesos, governance y tecnología soportan la escala |
| 500, Efficient | Organización "agent-first", capacidades optimizadas y mejoradas continuamente |

Microsoft aclara que el modelo se basa en el Capability Maturity Model (CMM) y que
Responsible AI se trata de forma transversal a todos los pilares.[^ms-maturity]

La lectura insiste en lo que Microsoft recomienda: **no usarlo como score único ni
como evaluación de una sola vez**. Cada pilar se evalúa por separado contra
comportamientos observables; una organización puede tener Technology & Data en 400
y Governance en 200 (p. 7).[^m1u4-lectura]

# Cómo se usa en los primeros 30 días

| Paso | Qué hacer |
|---|---|
| 1. Baseline | Evaluar el estado por pilar con evidencia observable: políticas, herramientas desplegadas, procesos reales de aprobación, calidad y acceso a datos, métricas de adopción, incidentes, roles, entrevistas con negocio, tecnología, riesgo y usuarios |
| 2. Target state | No llevar todos los pilares a 500: el target responde a lo que la estrategia necesita (si solo se buscan copilots internos, hace falta menos madurez en autorización de agentes) |
| 3. Gap y roadmap | Identificar qué capacidades bloquean los casos prioritarios y convertirlas en iniciativas |
| 4. Reassessment | Reevaluar periódicamente; en niveles altos, cada vez más apoyada en telemetría operativa y de valor |

Fuente: p. 7-8. Es la misma lógica de los assessments de ciberseguridad: baseline,
gap, target, plan, re-evaluación.[^m1u4-lectura]

Ejemplo de la slide 9: Technology & Data 400 ("integrado"), Governance & Security 150
("muy inicial") y Organization & Culture 200 ("repetible"). Nota: **150 no es un
nivel del modelo** (los niveles son 100, 200, 300, 400, 500); se lee como un valor
intermedio ilustrativo.[^m1u4-slides]

> "El maturity model no sirve para conseguir un score lindo. Sirve para tomar
> decisiones." (slide 9)[^m1u4-slides]

# Fricción real: el assessment como teatro

Los equipos sobreestiman su madurez, discuten horas si son 200 o 300, o intentan
mejorar todos los pilares a la vez. El antídoto es pedir evidencia observable y
vincular cada gap con una ambición concreta. "Si el nivel asignado no cambia ninguna
decisión, el assessment se convirtió en burocracia" (p. 8).[^m1u4-lectura]

Ejemplo de evidencia: "Governance 200, tenemos una política de uso, pero no
inventario central ni owners por sistema".

# Relación con el plan

Respalda el diagnóstico y el punto de partida; complementa el
[AIMM de Gartner](/frameworks/aimm-gartner.md) y el
[Microsoft RAI Maturity Model](/frameworks/microsoft-rai-maturity.md) (son modelos
distintos: este es de adopción agéntica). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, sección 2 (p. 6-8)
[^m1u4-slides]: M1U4, slides 8, 9 y 10
[^ms-maturity]: Microsoft Learn, Agentic AI adoption maturity model (consultado el 2026-10-12)
