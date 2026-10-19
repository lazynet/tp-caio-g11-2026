---
type: Concepto
title: EU AI Act, niveles de riesgo y prácticas prohibidas
description: Las cuatro capas del Reglamento (prohibidas, alto riesgo, transparencia, uso general) con la lista completa del art. 5, las reglas de clasificación del art. 6 y el art. 50.
tags: [compliance, regulacion, riesgo, eu-ai-act]
sources:
  - id: eu-ai-act
    resource: EU AI Act 2024.pdf
    title: Reg. (UE) 2024/1689, texto en español del DOUE (arts. 2-6, 50-55, p. 45-54 y 82-86)
  - id: eu-ai-act-eurlex
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    title: Reg. (UE) 2024/1689 en EUR-Lex (fuente primaria, consultada 2026-10-11)
  - id: ai-omnibus
    resource: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
    title: Reg. (UE) 2026/1744, Digital Omnibus on AI, DOUE L de 24.7.2026
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

# Las cuatro capas

El Reglamento no regula "la IA" en bloque: regula por riesgo. Un mismo producto
puede caer en más de una capa (un chatbot de un banco es de transparencia, y el
scoring que lo alimenta puede ser de alto riesgo).[^eu-ai-act][^eu-ai-act-eurlex]

| Capa | Dónde | Consecuencia |
|---|---|---|
| Prohibida | art. 5 | No se puede ofrecer ni usar en la UE |
| Alto riesgo | art. 6 + Anexo III (y Anexo I) | Requisitos de los arts. 8-15 y obligaciones de [proveedor y desplegador](/frameworks/eu-ai-act-proveedor-desplegador.md) |
| Transparencia | art. 50 | Avisar que es IA, marcar contenido sintético |
| Uso general (GPAI) | cap. V, arts. 51-56 | Obligaciones del proveedor del modelo; más fuertes con riesgo sistémico |

Lo que no entra en ninguna capa queda sin obligaciones específicas, salvo el
art. 4 de [alfabetización en IA](/frameworks/eu-ai-act-proveedor-desplegador.md), que aplica a todos.

# Prácticas prohibidas (art. 5)

Lista completa del art. 5.1 (p. 51-52):[^eu-ai-act]

| Letra | Práctica prohibida |
|---|---|
| a | Técnicas subliminales o manipuladoras/engañosas que alteran sustancialmente el comportamiento y causan o pueden causar perjuicio considerable |
| b | Explotar vulnerabilidades por edad, discapacidad o situación social o económica específica, con perjuicio considerable |
| c | Puntuación ciudadana (social scoring): evaluar o clasificar personas por comportamiento social o características personales, con trato perjudicial en contextos no relacionados con el origen de los datos, o injustificado o desproporcionado |
| d | Evaluar el riesgo de que una persona cometa un delito basándose únicamente en su perfil o rasgos de personalidad (con excepción de apoyo a una valoración humana basada en hechos objetivos) |
| e | Crear o ampliar bases de reconocimiento facial con extracción no selectiva de imágenes de internet o de CCTV |
| f | Inferir emociones en el trabajo y en centros educativos (salvo motivos médicos o de seguridad) |
| g | Categorización biométrica para deducir raza, opiniones políticas, afiliación sindical, creencias, vida u orientación sexual |
| h | Identificación biométrica remota "en tiempo real" en espacios públicos con fines policiales, salvo excepciones tasadas (víctimas, amenaza inminente, delitos graves) y con autorización previa |

Para un proveedor de software a bancos y fintechs, las que más cerca pasan son
**c** (un score que reutiliza datos de un contexto en otro para perjudicar al
cliente), **b** (explotar vulnerabilidad económica en cobranzas o venta
dirigida), **a** (patrones oscuros en venta de productos financieros) y **f**
(analítica de emociones de empleados o de agentes de call center).[^eu-ai-act]

Las prohibiciones aplican desde el 2 de febrero de 2025 y su multa es la más alta
(ver [calendario y sanciones](/frameworks/eu-ai-act-calendario-sanciones.md)).

## Novedades del Omnibus en el art. 5

El Reg. (UE) 2026/1744 agrega dos prohibiciones: **(ba)** sistemas que generan o
manipulan imágenes, video o audio realistas de partes íntimas o actividad
sexualmente explícita de una persona identificable sin su consentimiento, y
**(bb)** material de abuso sexual infantil. Aplican desde el 2 de diciembre de
2026 y tienen reglas de alcance propias (art. 5.1a y 5.1b).[^ai-omnibus] No
afectan a un software bancario típico.

# Alto riesgo: cómo se clasifica (art. 6)

Dos vías (p. 53-54):[^eu-ai-act]

1. **Art. 6.1, producto regulado (Anexo I):** el sistema es componente de
   seguridad de un producto cubierto por la legislación de armonización del
   Anexo I (o es el producto) y ese producto requiere evaluación de conformidad
   de terceros. Aplica más tarde que la otra vía.
2. **Art. 6.2, casos de uso del Anexo III:** ver [Anexo III](/frameworks/eu-ai-act-anexo-iii.md).
   Es la vía relevante para banca y seguros.

## Excepción del art. 6.3 (el "filtro de salida")

Un sistema del Anexo III **no** es de alto riesgo si no plantea un riesgo
importante para salud, seguridad o derechos fundamentales, incluso por no
influir sustancialmente en el resultado de la decisión, y cumple alguna de estas
condiciones (p. 54):[^eu-ai-act]

- (a) hace una tarea de procedimiento limitada;
- (b) mejora el resultado de una actividad humana ya realizada;
- (c) detecta patrones o desviaciones de decisiones previas, sin sustituir ni
  influir la valoración humana sin revisión humana adecuada;
- (d) hace una tarea preparatoria para una evaluación del Anexo III.

**Contraexcepción:** si el sistema **elabora perfiles de personas físicas**,
siempre es de alto riesgo. Un scoring crediticio perfila a la persona, así que
este filtro casi nunca lo salva.[^eu-ai-act]

Si el proveedor concluye que su sistema del Anexo III no es de alto riesgo,
tiene que **documentar la evaluación antes de comercializarlo** y **registrarlo**
(art. 6.4 y art. 49.2), y entregarla a la autoridad si se la piden.[^eu-ai-act]

El art. 7 permite a la Comisión modificar el Anexo III por acto delegado, y el
art. 112 le exige evaluar la lista una vez al año (p. 54-55 y 122).[^eu-ai-act]

# Transparencia (art. 50)

Aplica a **proveedores** y a **desplegadores** según el caso (p. 82-83):[^eu-ai-act]

| Apartado | Quién | Obligación |
|---|---|---|
| 50.1 | Proveedor | Los sistemas que interactúan con personas deben informar que es una IA, salvo que sea evidente |
| 50.2 | Proveedor (incluye GPAI) | Marcar en formato legible por máquina el contenido sintético de audio, imagen, video o texto, de modo detectable |
| 50.3 | Desplegador | Informar a las personas expuestas a un sistema de reconocimiento de emociones o de categorización biométrica |
| 50.4 | Desplegador | Revelar las ultrasuplantaciones (deepfakes) y el texto generado por IA publicado para informar al público (salvo revisión editorial humana) |

La información se da de forma clara a más tardar en la primera interacción
(50.5). Para un asistente conversacional de un banco, el 50.1 es la obligación
operativa; para cualquier producto que genere texto o imágenes para terceros, el
50.2.[^eu-ai-act]

**Cambio del Omnibus:** los proveedores de sistemas generativos ya puestos en el
mercado antes del 2 de agosto de 2026 tienen hasta el **2 de diciembre de 2026**
para cumplir el 50.2. El resto de los apartados no se movió.[^ai-omnibus]

# Modelos de uso general (cap. V)

Distinguir **modelo** de uso general (art. 3.63) y **sistema** de uso general
(art. 3.66, un sistema construido sobre un modelo). El cap. V regula al
proveedor del **modelo**.[^eu-ai-act]

| Nivel | Qué obliga | Artículo |
|---|---|---|
| Todo modelo GPAI | Documentación técnica (Anexo XI), información para quienes lo integran (Anexo XII), política de derechos de autor, resumen público del contenido de entrenamiento | 53.1 |
| GPAI de código abierto | Eximido de documentación técnica y de información a integradores, **salvo** que tenga riesgo sistémico | 53.2 |
| Proveedor de tercer país | Debe nombrar representante autorizado en la UE | 54 |
| Riesgo sistémico | Evaluación con pruebas adversarias, mitigación de riesgos, reporte de incidentes graves a la Oficina de IA, ciberseguridad | 55 |

**Riesgo sistémico (art. 51):** se presume cuando el cómputo acumulado de
entrenamiento supera **10^25 operaciones de coma flotante**, o por decisión de la
Comisión según el Anexo XIII. Se notifica a la Comisión en menos de dos semanas
(art. 52). Los códigos de buenas prácticas del art. 56 sirven para demostrar
cumplimiento hasta que haya normas armonizadas.[^eu-ai-act]

Para Acme Labs lo relevante es la figura de **proveedor posterior** (art.
3.68): quien integra un modelo de terceros en su sistema. No es proveedor del
modelo, pero el art. 53.1.b obliga al proveedor del modelo a darle documentación
para que cumpla, y el art. 25.4 exige un acuerdo escrito entre ambos (ver
[cadena de valor](/frameworks/eu-ai-act-proveedor-desplegador.md)).[^eu-ai-act]

# Cautelas

- La lista del art. 5 y el Anexo III se pueden modificar por acto delegado
  (arts. 7 y 97); chequear la versión consolidada antes de citar en una slide.
- No se verificó el contenido de los códigos de buenas prácticas de GPAI ni las
  guías de la Comisión sobre el art. 6 (previstas para el 2 de febrero de 2026,
  art. 6.5); no se buscaron en esta pasada.

# Relacionado

[Overview del EU AI Act](/frameworks/eu-ai-act.md),
[Anexo III](/frameworks/eu-ai-act-anexo-iii.md),
[proveedor y desplegador](/frameworks/eu-ai-act-proveedor-desplegador.md),
[calendario y sanciones](/frameworks/eu-ai-act-calendario-sanciones.md),
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^eu-ai-act-eurlex]: Misma norma en EUR-Lex, fuente primaria contra la que se cotejaron números de artículo y fechas: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[^eu-ai-act]: Reg. (UE) 2024/1689, texto en español del DOUE; páginas del PDF indicadas en el texto.
[^ai-omnibus]: Reg. (UE) 2026/1744, art. 1 puntos 7 y 39.b y art. 113 modificado, DOUE L de 24.7.2026.
