---
type: Concepto
title: Microsoft RAI MM, cómo se usa y qué aplica a un proveedor de software para bancos
description: Reglas de uso del RAI Maturity Model (mapa, no medición punitiva; no se promedia entre dimensiones), quién evalúa, hallazgos de la investigación base y lectura para un proveedor de software de bancos.
tags: [gobierno, madurez, ia-responsable, diagnostico]
status: draft
sources:
  - id: ms-rai
    resource: Microsoft Responsible AI 2023.pdf
    title: "Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1, 17-may-2023; pp. 2, 7-13 del PDF (numeración física; la impresa va uno menos)"
  - id: ms-rai-web
    resource: https://www.microsoft.com/en-us/research/publication/responsible-ai-maturity-model/
    title: Ficha de la publicación en Microsoft Research (MSR-TR-2023-26), consultada 2026-10-11
  - id: ms-rai-exec
    resource: https://www.microsoft.com/en-us/research/wp-content/uploads/2023/05/RAI-MM-Exec-Summary-PUBLISHED-Sept-23.pdf
    title: Executive summary y FAQ del RAI MM (versión de septiembre de 2023), consultado 2026-10-11
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [Microsoft RAI Maturity Model](/frameworks/microsoft-rai-maturity.md). Escala y estructura: [niveles](/frameworks/microsoft-rai-niveles.md).

# Para qué sirve

Es un mapa del territorio de RAI: ayuda a una organización a identificar su nivel actual y el deseado. Mirar hacia los niveles altos, para ver qué es posible y deseable, importa más que medir el nivel actual; el campo no es maduro, así que hay que esperar niveles bajos. Se lo está usando "bien" si dispara aprendizaje sobre RAI y conversaciones sobre cambio organizacional (p. 2).[^ms-rai]

El resumen ejecutivo lo presenta como herramienta de planificación estratégica para armar el programa de RAI (políticas, infraestructura) y los cambios culturales y de colaboración. Tiene dos audiencias: líderes y tomadores de decisión, y equipos que trabajan en productos de IA. Usos: **orientación** (leer la dimensión para entender qué hace falta para crecer) y **definición de metas** (elegir dimensiones relevantes, discutir el nivel al que apuntar y planificar los pasos).[^ms-rai-exec]

# Reglas de uso (pp. 10-12)

| Regla | Qué dice el documento |
|---|---|
| Mapa, no medición punitiva | Sirve para ubicarse y decidir adónde ir; identificar el nivel al que apuntar y qué costaría llegar. El nivel 5 puede no ser aplicable ni deseable.[^ms-rai] |
| No promediar entre dimensiones | No se recomienda un puntaje global ni comparar puntajes entre dimensiones: unas pesan más que otras o dependen de otras. Un 5 en Tooling no tiene el impacto de un 5 en Leadership and Culture.[^ms-rai] |
| Sí se puede promediar entre equipos | Dentro de una dimensión de Team Approach o RAI Practice, se puede combinar lo de varios equipos para ver el promedio de un departamento, cuidando las diferencias entre equipos.[^ms-rai] |
| Suplemento, no reemplazo | No cubre toda la IA, datos o tecnología; usarlo con otros modelos de madurez (IA, seguridad, privacidad).[^ms-rai] |
| Evalúan líderes y equipos | Los equipos son mejores para juzgar su enfoque y práctica; el liderazgo y los especialistas de RAI, las prioridades y la capacidad organizacional. Todos deberían evaluar todas las dimensiones; la divergencia de percepciones es señal de que hay espacio para madurar.[^ms-rai] |
| Cumplir el nivel antes de subir | Hay que satisfacer los criterios del nivel previo antes de pasar al siguiente.[^ms-rai] |

## Quién evalúa cada categoría

| Categoría | Evalúa | Matiz |
|---|---|---|
| Organizational Foundations | Liderazgo senior y equipos | Contrastar cómo se viven las decisiones del liderazgo; las disparidades son oportunidad (p. 13). |
| Team Approach | Los equipos | Una estimación rápida del jefe de departamento es posible pero menos robusta (p. 20). |
| RAI Practice | Los equipos | Adaptar el esfuerzo al equipo, tipo de sistema y dominio (p. 32). |
| Accountability | Nivel organización | Ídem (p. 33). |
| Transparencia externa e interna, AI privacy, AI security | Organización y equipo | Se evalúan en ambos niveles (pp. 34-35, 43-44). |
| Relación especialistas de RAI y equipos (dim. 14 y 15) | Ambas partes por separado | Después se discuten juntas; el desacuerdo se usa para armar un plan de mejora (pp. 30-31). |

El material de la publicación incluye además un deck para facilitar talleres ("Introducing the RAI MM Workshop"), enlazado desde la ficha de Microsoft Research; no se leyó, así que acá no se describe el formato del taller.[^ms-rai-web]

# Relación con políticas y regulación

Según el resumen ejecutivo, las políticas y marcos como el EU AI Act, el NIST AI RMF o el Responsible AI Standard de Microsoft fijan los objetivos que cada producto de IA debe lograr, mientras que el RAI MM es una herramienta para decidir qué inversiones hacen falta para gobernar y sostener el trabajo de RAI.[^ms-rai-exec] Ver [EU AI Act](/frameworks/eu-ai-act.md).

# Hallazgos de la investigación base

El PDF no trae resultados por organización estudiada ni casos de empresas: el modelo se construyó con entrevistas a especialistas y practicantes (internos y externos a Microsoft), no con un benchmark de empresas. Lo que sí informa como hallazgos de esa investigación es:[^ms-rai]

* **La colaboración es el motor central** de la madurez en las 90 personas consultadas. Es un trabajo invisible, poco valorado, y ninguna organización debería esperar alcanzar niveles altos sin madurar antes la colaboración interdisciplinaria (p. 8).
* **Los principios solos no alcanzan:** traducirlos a práctica es difícil; muchas herramientas y checklists están pensadas para practicantes individuales y no para organizaciones, y son parciales (p. 7).
* **No había un modelo de madurez específico de RAI:** los de IA/ML revisados la trataban de forma insuficiente (p. 7).
* **Las dimensiones son interdependientes**, y el avance en una puede depender del nivel de otras (p. 9).
* **La mayoría de las organizaciones está en niveles bajos** y salir de los niveles 1-2 es lo más costoso (p. 10).

# Lectura para un proveedor de software de bancos

Lectura propia del equipo, no del documento. Sirve para el [plan CAIO](/mapa-plan-fuentes.md) como andamio de diagnóstico y de metas a 12 meses, y se complementa con otros modelos de madurez como el [AIMM](/frameworks/aimm-gartner.md).

* **Elegir dimensiones, no medir las 24.** El documento invita a escoger las dimensiones que importan; para una empresa que construye software para bancos tienen peso inmediato Leadership and Culture, RAI policy, RAI compliance, Accountability, las dos de Transparency, Identifying/Measuring/Monitoring y AI security.
* **Accountability depende de ser proveedor.** El nivel 2 describe a quien delega en el cliente que despliega la supervisión humana y las pruebas de última milla; los niveles 4-5 piden compartir responsabilidad, dar guía y formación sobre supervisión humana y tener un plan de rollback y aviso a clientes. Para un proveedor, la frontera entre su responsabilidad y la del banco es la dimensión más cercana a su contrato.
* **Transparencia externa e interna** equivalen a lo que los bancos piden en due diligence: transparency notes, limitaciones conocidas, documentación obligatoria integrada al pipeline (nivel 4-5).
* **Cumplimiento regulatorio.** El modelo no trae requisitos legales: usarlo para decidir inversiones y mapear aparte las exigencias (EU AI Act, regulación local, requisitos que llegan desde los clientes).
* **No hay metas en cifras.** Ninguna dimensión trae umbrales cuantitativos; las metas de nivel se tienen que traducir a indicadores propios (ver la regla de no promediar).
* **Meta realista.** Dado que el nivel 5 es aspiracional y salir de los niveles 1-2 es lo más caro, un objetivo a 12 meses razonable es subir pocas dimensiones prioritarias uno o dos niveles, no todas a la vez; es una hipótesis a validar, no una recomendación del documento.

# Cautelas

* El PDF es la versión 1 del 17-may-2023 y el modelo se declara en evolución (p. 10); la ficha de Microsoft Research también publica un resumen ejecutivo con fecha posterior (septiembre de 2023).
* Los hallazgos acá listados son los que el propio PDF declara sobre su metodología y uso; no hay datos de organizaciones evaluadas.

[^ms-rai]: Vorvoreanu et al. (2023), Responsible AI Maturity Model, v1 (17-may-2023), Microsoft Research, PDF pp. 2, 7-13, 20, 30-35, 43-44 (numeración física).
[^ms-rai-web]: Ficha de la publicación en Microsoft Research (MSR-TR-2023-26), con enlaces al PDF, al resumen ejecutivo y al deck de taller.
[^ms-rai-exec]: Executive summary y FAQ del Responsible AI Maturity Model, Microsoft Research (versión de septiembre de 2023), pp. 2-3.
