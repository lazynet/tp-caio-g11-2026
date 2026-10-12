---
type: Concepto
title: DLP en sistemas de IA
description: Qué datos hay que proteger en un sistema de IA y las cuatro estrategias de prevención de fuga de datos.
tags: [m3, seguridad, dlp, datos]
sources:
  - id: m3u1
    resource: Presentacion_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: M3U1 (el archivo dice Unidad 9), 20 slides
    pages: slides 7-9
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:09:00Z }
---

# Definición

Los sistemas de IA procesan grandes volúmenes de datos, lo que amplifica el
riesgo de exposición. La prevención de fuga de datos (DLP) reúne las estrategias
y herramientas para que la información sensible no sea expuesta, robada o mal
usada.[^m3u1]

# Datos en riesgo

*"La clasificación de datos es la base de toda estrategia DLP efectiva."*
Cualquier dato que fluya por un sistema de IA puede ser un vector de
exposición.[^m3u1]

| Categoría | Ejemplos de la slide |
|---|---|
| PII (información de identificación personal) | Nombres, direcciones, números de identificación |
| Datos empresariales confidenciales | Estrategias, finanzas, contratos internos |
| Propiedad intelectual | Algoritmos, modelos entrenados, código fuente propietario |

# Estrategias clave

| Estrategia | En qué consiste |
|---|---|
| Anonimización | Eliminar o enmascarar identificadores personales antes del procesamiento |
| Cifrado | Proteger datos en tránsito y en reposo con estándares robustos |
| Control de acceso | Restringir quién consulta o modifica datos sensibles |
| Monitoreo continuo | Auditar la actividad en los pipelines para detectar anomalías |

Fuente de las dos tablas: [^m3u1]

# Relacionado

- [Pipeline de datos seguro](/conceptos/m3u1-pipeline-datos-seguro.md)
- [Capas de seguridad](/conceptos/m3u1-capas-seguridad.md)
- Anonimización en inferencia: [M1U3](/unidades/m1u3-datos-contexto.md)

[^m3u1]: M3U1, slides 7-9.
