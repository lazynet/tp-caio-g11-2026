---
type: Concepto
title: "Diagnóstico de madurez IA en 5 dimensiones"
description: "Marco de diagnóstico con cinco dimensiones y escala de 1 (Inicial) a 5 (Transformacional), con los pasos para aplicarlo y un caso resuelto."
tags: [m1, diagnostico, madurez]
sources:
  - id: m1u1-corta
    resource: Documento_Chief_AI_Officer_CAIO_Modulo_1_Unidad_1 (2).pdf
    title: "M1U1 corta, pp. 6-10"
  - id: m1u1-extendida
    resource: Módulo 1 — Unidad 1 — Mentalidad CAIO y liderazgo en la era IA.pdf
    title: "M1U1 extendida, pp. 8-10"
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "M1U1 corta pp. 6-10 y extendida pp. 8-10 cotejadas contra el PDF; atribuciones a Gartner y NovaGob del curso sin cotejar; no acredita madurez de Acme Labs. Cotejo del agente revisado y confirmado por Martín en esta conversación."
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:30:00Z }
---
# Para qué sirve

Es el punto de partida de cualquier estrategia seria: sin diagnóstico, las iniciativas se lanzan sobre supuestos desconectados de la realidad y se hacen "inversiones costosas en experimentos inconexos con un retorno poco claro". Responde si la cultura está preparada, si los datos son confiables y accesibles y si hay talento para escalar.[^m1u1-corta]

# Escala

De 1 (Inicial, ad-hoc) a 5 (Transformacional, optimizado), con el nivel 3 como Operacional (definido).[^m1u1-corta]

# Las cinco dimensiones

| Dimensión | Nivel 1: Inicial | Nivel 3: Operacional | Nivel 5: Transformacional |
|---|---|---|---|
| 1. Estrategia y liderazgo | Uso experimental, sin estrategia central ni apoyo claro del directorio | Estrategia de IA definida y alineada al negocio; roles y responsabilidades claros | La IA es central en la estrategia corporativa; el liderazgo impulsa la reinvención de modelos de negocio |
| 2. Datos e infraestructura | Silos, baja calidad, difícil acceso; infraestructura no preparada | Plataforma de datos centralizada y gobernanza de datos; cloud soporta proyectos de IA | Arquitectura moderna y ágil (ej. Data Mesh); escalado rápido; MLOps industrializado |
| 3. Talento y cultura | Conocimiento escaso y concentrado; resistencia al cambio | Programas de capacitación; cultura de experimentación y colaboración técnica-negocio | Atrae y retiene talento de élite; aprendizaje continuo y simbiosis humano-IA |
| 4. Gobernanza y ética | Sin políticas de uso ético; riesgos no gestionados formalmente | Principios de IA responsable y comité de ética; auditorías de sesgo en modelos clave | Ética y gobernanza integradas en todo el ciclo de vida; cumplimiento proactivo |
| 5. Adopción y valor | PoC aisladas sin impacto medible | IA integrada en procesos clave con valor medible (eficiencia, personalización) | Procesos core transformados y nuevas líneas de negocio; ROI monitoreado y optimizado |

[^m1u1-corta]

El curso describe solo los niveles 1, 3 y 5. Los niveles 2 y 4 no tienen descriptor en la tabla (el caso resuelto asigna nivel 2 sin definirlo), así que su criterio hay que fijarlo explícitamente al aplicar el marco. Tampoco hay una regla para promediar o combinar las cinco dimensiones en un puntaje organizacional único.

# Pasos para realizar el diagnóstico

1. **Formar un equipo multidisciplinario:** tecnología, negocio, legal y RRHH.
2. **Entrevistas y encuestas** a distintos niveles sobre las cinco dimensiones.
3. **Mapear la evidencia:** no basarse solo en opiniones (documentos de estrategia, arquitecturas de datos, políticas de gobernanza).
4. **Puntuar cada dimensión** (1-5) justificando el puntaje.
5. **Visualizar** con un gráfico de radar o scoreboard.
6. **Definir la hoja de ruta:** las 2-3 brechas más críticas con plan de acción para subir al siguiente nivel.

No es un evento único: es un proceso continuo que lidera el CAIO.[^m1u1-corta]

# Variante de la versión extendida

La versión extendida estructura el diagnóstico en otras dimensiones, tomadas de listas de verificación de NovaGob (2024) y del AI Maturity Model de Gartner: disponibilidad y calidad de datos, talento interno, procesos con potencial de automatización, infraestructura tecnológica, cultura frente al cambio y cumplimiento normativo. Una versión inicial puede completarse en 2-3 sesiones con los referentes del área, sin semanas de consultoría.[^m1u1-extendida] En el [caso de RRHH](/conceptos/m1u1-caso-diagnostico-rrhh.md) se aplicaron cinco: datos, talento, procesos candidatos, cultura y cumplimiento.

La dimensión cultural suele subestimarse: con excelente infraestructura y talento, si la cultura penaliza el error o los mandos medios ven la IA como amenaza, la adopción será superficial. Se evalúa con conversaciones directas entre niveles, mejor que con encuestas formales.[^m1u1-extendida]

# Caso resuelto del curso (supermercados)

| Dimensión | Nivel | Observación |
|---|---|---|
| Estrategia y liderazgo | 2 | Hay conciencia, pero la estrategia no está formalizada |
| Datos e infraestructura | 2 | Datos de ventas accesibles; inventario y clientes en silos y baja calidad |
| Talento y cultura | 1 | Conocimiento casi nulo fuera del equipo de TI |
| Gobernanza y ética | 1 | Sin políticas |
| Adopción y valor | 1 | Un solo piloto (demanda de manzanas) |

[^m1u1-corta]

**Respuesta del curso, dos prioridades para 6 meses:** (1) formalizar la estrategia y asegurar apoyo del liderazgo, con 2-3 casos de uso de alto impacto atados a KPIs; (2) plan de gobernanza y calidad de datos en inventario y clientes. Talento y gobernanza son importantes pero no tienen base sólida sin estrategia y datos fiables.[^m1u1-corta]

# Relacionado

[Plan de 30 días](/conceptos/m1u1-plan-30-dias.md) · [marcos de madurez del bundle](/frameworks/microsoft-rai-maturity.md), [Cisco AI Readiness](/frameworks/cisco-ai-readiness.md) y [AIMM](/frameworks/aimm-gartner.md) · unidad [M1U1](/unidades/m1u1-mentalidad-caio.md).

# Cautelas

- **Cotejada contra el PDF** (2026-10-20): M1U1 corta, pp. 6-10 (marco y niveles 1, 3 y 5, p. 6-7; pasos, p. 7; proceso continuo, p. 8; caso de supermercados, p. 9; respuesta del curso, pp. 9-10) y M1U1 extendida, pp. 8-10 (dimensiones alternativas y cultura, pp. 8-9; ejemplo de RRHH con sus cinco dimensiones, p. 10). La tabla y los pasos se leyeron de la capa de texto del PDF.
- **Cita corregida:** la respuesta completa del caso de supermercados termina en la p. 10; la cita anterior, pp. 6-9, quedaba incompleta.
- **Marco didáctico, no estándar:** las cinco dimensiones y los niveles 1, 3 y 5 son el marco del curso. Los niveles 2 y 4 no están definidos y el curso no da una regla de promedio; no se debe presentar un puntaje único como resultado del marco.
- **Variante extendida:** usa otras dimensiones y atribuye su estructura a NovaGob (2024) y al AI Maturity Model de Gartner. Es atribución del curso: no se cotejaron esas fuentes primarias (ver [AIMM](/frameworks/aimm-gartner.md) y [huecos](/huecos.md)).
- **Fidelidad al curso no es madurez de Acme Labs:** verificar que la ficha refleja el curso no acredita ningún nivel de madurez real de la organización.

[^m1u1-corta]: M1U1 corta, pp. 6-10
[^m1u1-extendida]: M1U1 extendida, pp. 8-10
