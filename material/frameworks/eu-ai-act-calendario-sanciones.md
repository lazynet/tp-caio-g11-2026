---
type: Concepto
title: EU AI Act, calendario de aplicación y sanciones
description: Fechas de aplicación del art. 113 con las modificaciones del Digital Omnibus (Reg. UE 2026/1744), régimen transitorio del art. 111 y montos de multas del art. 99 con el tratamiento de PyMEs.
tags: [compliance, regulacion, calendario, sanciones, eu-ai-act]
sources:
  - id: eu-ai-act
    resource: EU AI Act 2024.pdf
    title: Reg. (UE) 2024/1689, arts. 99-101 (p. 115-117), 111-113 (p. 121-123)
  - id: eu-ai-act-eurlex
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    title: Reg. (UE) 2024/1689 en EUR-Lex (fuente primaria)
  - id: ai-omnibus
    resource: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
    title: Reg. (UE) 2026/1744, Ómnibus digital sobre IA, DOUE L de 24.7.2026 (arts. 1.30 y 1.38 a 1.40, art. 4, considerando 40)
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T20:13:00Z }
status: verified
verified:
  by: human:lazynet
  at: 2026-10-22
  scope: "Fechas del art. 113, letra c (i: 2027-12-02 Anexo III; ii: 2028-08-02 Anexo I) y la fecha previa 2026-08-02 (considerando 40), cotejadas contra el texto español del DOUE del Reg. 2026/1744 obtenido de Cellar el 2026-10-22. No cubre sanciones ni la lectura para el plan. Cotejo del agente revisado y confirmado por Martín en esta conversación."
---

# Resolución de la cautela del Omnibus

[M1U4](/unidades/m1u4-rol-gobernanza.md) citaba el "AI Omnibus (Reg. UE
2026/1744)" sin fuente. **Confirmado con la fuente primaria:** es el
*Reglamento (UE) 2026/1744 del Parlamento Europeo y del Consejo, de 8 de julio de
2026, por el que se modifican los Reglamentos (UE) 2024/1689, (UE) 2018/1139 y (UE)
2023/1230 en lo que respecta a la simplificación de la aplicación de normas
armonizadas en materia de inteligencia artificial (Ómnibus digital sobre IA)*, publicado en
el DOUE L de 24.7.2026 y en vigor el tercer día siguiente a su publicación, es
decir, el 27 de julio de 2026.[^ai-omnibus]

El Omnibus **mueve fechas y simplifica**, pero no elimina las obligaciones de
alto riesgo. El motivo declarado (considerando 40) es que las normas
armonizadas, las especificaciones comunes y las autoridades nacionales no
llegaron a tiempo.[^ai-omnibus]

Lo que sigue en la cautela de M1U4: la guía SIGEN 197/2026 **no** se revisó acá
(no es de este Reglamento).

# Calendario vigente

Texto original (art. 113, p. 123) y texto vigente con el Omnibus:[^eu-ai-act][^ai-omnibus]

| Fecha | Qué aplica | Origen |
|---|---|---|
| 2024-08-01 | Entrada en vigor del Reglamento (20 días tras su publicación del 12.7.2024) | Art. 113 original |
| 2025-02-02 | Caps. I y II: objeto, definiciones, **alfabetización (art. 4)** y **prácticas prohibidas (art. 5)** | Art. 113.a |
| 2025-08-02 | Cap. III sección 4 (organismos notificados), **cap. V (GPAI)**, cap. VII (gobernanza), cap. XII (sanciones) y art. 78; excluido el art. 101 | Art. 113.b |
| 2026-07-27 | Entra en vigor el Omnibus; arts. 102-110 aplican desde esa fecha | Omnibus, art. 113.d |
| 2026-08-02 | Fecha general de aplicación: **transparencia (art. 50)**, art. 101 (multas a GPAI) y el resto no diferido | Art. 113 original |
| 2026-12-02 | Nuevas prohibiciones 5.1 (ba) y (bb) y 5.1a y 5.1b; plazo de los sistemas generativos ya en el mercado para cumplir el marcado del art. 50.2 | Omnibus, art. 113.a y art. 111.4 |
| 2027-08-02 | GPAI introducidos antes del 2.8.2025 deben cumplir | Art. 111.3 |
| **2027-12-02** | **Cap. III secciones 1, 2 y 3 (alto riesgo, requisitos y obligaciones) para Anexo III**, incluye scoring (5.b) y seguros (5.c) | Omnibus, art. 113.c.i |
| 2027-09-02 | Orientaciones de la Comisión, con un modelo, sobre el plan de vigilancia poscomercialización (art. 72.3; el texto de 2024 pedía un acto de ejecución para el 2.2.2026) | Omnibus, art. 1 punto 30 |
| **2028-08-02** | Cap. III secciones 1, 2 y 3 para alto riesgo por Anexo I (art. 6.1, productos regulados) | Omnibus, art. 113.c.ii |
| 2030-08-02 | Sistemas de alto riesgo de autoridades públicas ya en el mercado | Art. 111.2 |

Antes del Omnibus, el alto riesgo del Anexo III aplicaba el **2 de agosto de
2026** y el del art. 6.1 el 2 de agosto de 2027.[^eu-ai-act][^eu-ai-act-eurlex]

## Lectura para el plan a 12 meses

- **Hoy (octubre de 2026) ya rigen:** alfabetización (art. 4, en su versión
  suavizada), prohibiciones (art. 5), obligaciones de GPAI, sanciones y
  transparencia del art. 50.
- **Todavía no rige** el paquete completo de requisitos de alto riesgo (arts.
  8-27) para scoring y seguros: queda para el **2 de diciembre de 2027**, unos
  14 meses después de esta fecha. Un plan de 12 meses es la ventana de preparación,
  no de exigibilidad.
- Esa fecha es un **plazo legal, no un permiso para esperar**: la
  documentación, el QMS, los logs y la evaluación de conformidad llevan meses y
  los clientes los van a pedir antes por contrato. Es una decisión reversible
  empezar por lo barato (inventario, clasificación, art. 4) e irreversible
  rediseñar logs y datos tarde.
- Régimen transitorio (art. 111.2): un sistema de alto riesgo ya en el mercado
  antes de la fecha de aplicación sólo queda alcanzado si después sufre
  **cambios significativos de diseño**. Es un incentivo para cerrar bien las
  versiones.[^ai-omnibus]

# Sanciones (art. 99, p. 115-116)

Las fija cada Estado miembro, que deben ser "efectivas, proporcionadas y
disuasorias". Los topes del Reglamento:[^eu-ai-act]

| Infracción | Tope en euros | Tope sobre facturación mundial | Se aplica |
|---|---|---|---|
| Prácticas prohibidas (art. 5) | 35.000.000 | 7 % | El **mayor** de los dos (si es empresa) |
| Obligaciones de proveedores (16), representantes (22), importadores (23), distribuidores (24), desplegadores (26), organismos notificados y transparencia (50) | 15.000.000 | 3 % | El **mayor** |
| Información inexacta, incompleta o engañosa a autoridades u organismos notificados | 7.500.000 | 1 % | El **mayor** |
| Proveedores de GPAI (art. 101, multa de la Comisión) | 15.000.000 | 3 % | El **mayor** |
| Instituciones de la UE (art. 100): prohibidas / resto | 1.500.000 / 750.000 | no aplica | Fijo |

**PyMEs:** para PyMEs, incluidas startups, cada multa es el porcentaje o el
importe, **el que sea menor** (art. 99.6). El Omnibus extiende esa regla a las
*small mid-caps* (art. 99.6a) y agrega al escalón de 15 M las obligaciones del
art. 25.2 y 25.4 (cooperación en la cadena de valor y contratos).[^eu-ai-act][^ai-omnibus]

Factores para graduar la multa (99.7): gravedad, duración y personas afectadas;
tamaño y cuota de mercado; beneficio obtenido; cooperación; si el operador
reportó la infracción; intencionalidad o negligencia; medidas de mitigación.

## Qué tope le importa a un proveedor de software

- El de **15 M / 3 %** es el relevante para incumplir las obligaciones del art. 16
  (si es proveedor) o del art. 26 (si es desplegador) y para transparencia.
- Para una PyME rige el **menor** de los dos, de modo que el tope práctico es
  el 3 % de la facturación mundial anual, no 15 M. Esto es distinto del cliente
  bancario grande, donde el mayor de los dos casi siempre son los 15 M o más.
- La clasificación de PyME (Recomendación 2003/361/CE) depende de los datos
  reales de Acme Labs, que no van en el repo.

# Cautelas

- **Sección 5 del cap. III** (arts. 40-49: normas, evaluación de conformidad,
  certificados, registro; p. 76-81 del texto de 2024): la regla literal del art.
  113 la deja en la fecha general. El párrafo segundo dice "Será aplicable a partir
  del 2 de agosto de 2026" (p. 123), y el Omnibus no lo toca: solo modifica el
  párrafo tercero (art. 1 punto 40, p. 35). Ninguna letra de ese párrafo nombra la
  sección 5, ni en el original (la b) nombra la sección 4) ni en el modificado (la
  c) nombra las secciones 1, 2 y 3). El considerando (40) llama al 2 de agosto de
  2026 la "fecha general de aplicación" (p. 12).[^eu-ai-act][^ai-omnibus]
- Lo que sigue abierto es cómo opera esa fecha para la evaluación de conformidad y
  el registro (arts. 43 y 49) mientras los requisitos de las secciones 1 a 3 están
  diferidos. Es una lectura a decidir, no una conclusión sobre Acme Labs. El
  Omnibus sustituye el art. 43.3: los organismos notificados del Anexo I, sección
  A, piden su designación a más tardar el **2028-01-28** (p. 22). No modifica el
  art. 49; el registro del art. 49.2 se simplifica suprimiendo los puntos 7 y 9 del
  Anexo VIII, sección B (p. 36; considerando 22).
- Cotejado el 2026-10-21 contra el texto español del DOUE L de 24.7.2026, bajado
  de EUR-Lex (CELEX_32026R1744_ES_TXT.pdf, 41 p.): arts. 111 y 113 modificados
  (p. 35), art. 72.3 (p. 26), considerando (40) (p. 12) y art. 4 del Omnibus,
  entrada en vigor (p. 41). Coinciden con la tabla.
- Ese cotejo llegó en el PR #55 (autor en GitHub: edu2020chaparro-ux; herramienta no
  declarada). La revisión del 2026-10-21 (claude-code/claude-opus-5-5) lo repitió
  sobre el PDF/A español del Omnibus bajado de Cellar, el repositorio de la Oficina de
  Publicaciones (41 p.), y sobre el Reg. 2024/1689 en español (art. 113, p. 123;
  art. 72.3, p. 101). Precisó la sección 5 y el art. 72.3, y alineó el título con
  el oficial (p. 1).
- Las fuentes secundarias (estudios jurídicos) coinciden en 2 de diciembre de
  2027 y 2 de agosto de 2028; la primaria lo confirma. Sobre el art. 50.2, un
  resumen secundario lo da como aplicable sin matices; el texto primario fija
  la gracia hasta el 2 de diciembre de 2026 solo para sistemas ya en el mercado.
- Las multas efectivas dependen de la ley nacional de cada Estado miembro; no
  se relevó ninguna.

# Relacionado

[Overview](/frameworks/eu-ai-act.md),
[niveles de riesgo](/frameworks/eu-ai-act-niveles-riesgo.md),
[Anexo III](/frameworks/eu-ai-act-anexo-iii.md),
[proveedor y desplegador](/frameworks/eu-ai-act-proveedor-desplegador.md).

[^eu-ai-act]: Reg. (UE) 2024/1689, texto en español del DOUE; páginas del PDF indicadas en el texto.
[^eu-ai-act-eurlex]: Misma norma en EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[^ai-omnibus]: Reg. (UE) 2026/1744, DOUE L de 24.7.2026: art. 1 puntos 30 y 38 a 40, art. 4 y considerando (40).
