---
type: Concepto
title: Decision rights y mandato del CAIO
description: Definir quién decide qué clase de decisión de IA, en vez de discutir fronteras entre cargos, y qué debe incluir el mandato del CAIO.
tags: [m1, gobierno, operating-model, caio]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: m1u4-slides
    resource: Presentacion - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional v3.pdf
    title: M1U4, slides v3 (24 slides)
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Idea central

El CAIO es una **función organizacional** antes que un título: exista o no una
persona con ese nombre, la organización necesita alguien accountable por que la IA
genere valor sin perder control (p. 1).[^m1u4-lectura] En una empresa de 300
personas la función puede recaer en un CTO, CIO, Chief Digital Officer, Head of AI o
en un modelo compartido entre tecnología y negocio.[^m1u4-lectura]

La pregunta correcta no es "¿toda empresa necesita un CAIO?", sino "¿quién es
accountable por que la IA genere valor sin que la organización pierda control?"
(p. 1).[^m1u4-lectura]

Las fronteras entre CIO, CTO, CDO, CISO, Product, Legal y CAIO varían demasiado:
discutirlas lleva a debates semánticos. Es más útil trabajar con **decision
rights**: dejar explícito quién tiene autoridad para cada clase de decisión
(p. 2).[^m1u4-lectura] "La respuesta puede variar. El problema es que no exista."
(slide 4).[^m1u4-slides]

# Tabla de decision rights (p. 2)

| Decisión | Accountability probable |
|---|---|
| ¿Qué problema de negocio queremos resolver? | Business / Product |
| ¿Qué iniciativas de IA priorizamos? | Business + función de IA / portfolio governance |
| ¿Qué plataformas o modelos están permitidos? | Technology / AI / Security |
| ¿Qué datos puede utilizar una solución? | Data owner + Privacy/Security + negocio |
| ¿Qué nivel de autonomía puede tener un agente? | Business owner + Risk/Security + AI governance |
| ¿Quién define el quality bar? | Product + Domain experts + Business owner |
| ¿Quién decide si el sistema está listo para producción? | Business/Product + Engineering dentro de guardrails definidos |
| ¿Quién aprueba una excepción a una política de alto riesgo? | Órgano de governance / Risk / autoridad designada |
| ¿Quién responde por el resultado de negocio? | Business owner |

El valor no está en que todos los casos tengan la misma respuesta, sino en "que la
respuesta exista antes del incidente".[^m1u4-lectura] Microsoft incorpora la idea en
su modelo de madurez: a más autonomía de los agentes, el operating model debe
explicitar decision rights, accountability y escalamiento, y esos derechos deben
evolucionar.[^m1u4-lectura]

# CIO vs. CTO vs. CAIO en 60 segundos (p. 2-3)

| Rol | Foco típico | Pregunta frecuente |
|---|---|---|
| CIO | Sistemas corporativos, IT, operación tecnológica | ¿Cómo funciona y escala la tecnología que usa la empresa? |
| CTO | Arquitectura, ingeniería, plataformas y, en empresas de producto, la tecnología que diferencia al negocio | ¿Qué tecnología construimos y cómo? |
| CDO / Data | Datos, calidad, acceso, analytics y governance del dato | ¿Cómo convertimos datos en un activo confiable y utilizable? |
| CISO | Riesgo y seguridad de la información | ¿Qué puede salir mal y cómo limitamos la exposición? |
| CAIO | Estrategia de IA, adopción, operating model, portfolio, governance y valor | ¿Cómo convierte la organización la IA en capacidad real sin perder control? |

No hay frontera universal. El objetivo "no es defender territorio sino hacer
explícitas las interfaces y decisiones compartidas".[^m1u4-lectura]

# Qué es y qué no es el CAIO (slide 3)

| NO | SÍ |
|---|---|
| Aprobar cada uso de IA | Estrategia y portfolio |
| Elegir cada modelo | Operating model |
| Construir todos los agentes | Decision rights |
| Responder por cada outcome | Capacidades compartidas |
| Convertirse en el nuevo cuello de botella | Adopción y governance; medición de valor |

"El CAIO diseña el sistema mediante el cual la organización puede usar IA con
velocidad, accountability y control."[^m1u4-slides]

# Mandato mínimo (p. 4-5)

El reporting line importa menos que el mandato real. Sin decision rights, acceso a
los líderes relevantes y capacidad de escalar conflictos, el CAIO queda reducido a
evangelizador.[^m1u4-lectura] Un mandato mínimo aclara:

- qué decisiones puede tomar directamente;
- qué decisiones pertenecen al negocio;
- qué excepciones deben escalarse y a quién;
- qué capacidades compartidas puede financiar o priorizar;
- qué métricas reporta a liderazgo;
- qué áreas participan del governance;
- qué cadencia de revisión mantiene la organización.

Ver también el [inventario de IA y el operating rhythm](/conceptos/m1u4-inventario-y-operating-rhythm.md).

# Ejercicio 1 de la unidad

Empresa SaaS de 400 empleados con CTO, VP Product, Head of Data bajo el CTO, CISO
part-time y 15 iniciativas de IA dispersas; el CEO pide "una persona accountable por
AI". Opciones: A crear un CAIO, B asignar la función al CTO, C crear un AI Council sin
CAIO, D otra estructura. Se pide letra más el problema que se intenta resolver
(p. 6, slide 5).[^m1u4-lectura] El material no da una respuesta correcta: evalúa la
justificación.

# Relación con el plan

Respalda la sección de Gobierno: ver [Council vs CoE](/conceptos/m1u4-council-vs-coe.md),
[RACI](/conceptos/m1u4-raci-ownership.md) y el
[Governance Stack](/conceptos/m1u4-governance-stack.md). Unidad:
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^m1u4-lectura]: M1U4, lectura, secciones 1.1 y 1.4 y ejercicio 1 (p. 1-6)
[^m1u4-slides]: M1U4, slides 3, 4 y 5
