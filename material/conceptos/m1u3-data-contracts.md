---
type: Concepto
title: Data contracts
description: Acuerdo técnico formal entre productores y consumidores de datos, con esquema, calidad, SLAs y un ejemplo en YAML.
tags: [m1, datos, calidad, gobierno]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 13 páginas
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "M1U3 (PDF de 13 páginas), p. 2, 5, 6 y 10: definición, contenido, uso en Data Mesh, cláusulas de equidad y YAML de ejemplo; herramientas como atribución del curso. Cotejo del agente revisado y confirmado por Martín en esta conversación."
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Qué es

Un Data Contract es un acuerdo técnico formal entre productores y consumidores de
datos que especifica esquema, tipos, restricciones de calidad, semántica y SLAs.
"Funciona como un contrato de API, pero para los datos" (p. 2).[^m1u3]

Se expresa generalmente en YAML o JSON y define qué espera el consumidor y qué
garantiza el productor.[^m1u3]

# Qué incluye

- Esquema: nombres y tipos de columnas.
- Restricciones de calidad: rangos válidos, cardinalidad, unicidad.
- Frecuencia de actualización.
- Propietario del dato.
- Consecuencias de incumplimiento.
- Opcional: cláusulas de equidad (*fairness constraints*) que obligan al productor a
  documentar la distribución de atributos sensibles y a avisar cuando cambia de forma
  significativa (p. 6).[^m1u3]

# Para qué sirve

- En arquitecturas de **Data Mesh**, con equipos que producen y consumen de forma
  descentralizada, previene que un cambio silencioso en un pipeline upstream rompa un
  modelo en producción (p. 5).[^m1u3]
- Con validaciones automáticas en cada etapa del pipeline, baja la probabilidad de que
  datos corruptos lleguen al modelo y alimenten alucinaciones (p. 5-6).[^m1u3]
- Convierte la calidad del dato en "una responsabilidad compartida y auditable, no en
  una tarea puntual del equipo de ML" (p. 6).[^m1u3]

Herramientas citadas (2024): Data Contract CLI, Datahub y Data Mesh Manager, para
definir, versionar, validar y auditar contratos.[^m1u3]

# Ejemplo del curso (p. 10)

Contrato de un dataset sintético de tickets de soporte, con Data Contract CLI:[^m1u3]

```yaml
dataContractSpecification: 0.9.0
id: tickets-sinteticos-v1
models:
  tickets:
    fields:
      id: {type: integer, unique: true}
      descripcion: {type: string, minLength: 20, maxLength: 500}
      categoria: {type: string, enum: [facturacion, conectividad, portabilidad, equipos, consultas]}
      prioridad: {type: string, enum: [alta, media, baja]}
```

El contrato define el esquema del dataset (paso 1) y, al final, valida el resultado
(tipos, enum de `categoria`, largo de `descripcion`, unicidad de `id`). Ver el
[caso completo](/conceptos/m1u3-caso-tickets-sinteticos.md).

# Relación con otros conceptos

- Línea de defensa de la [higiene de datos](/conceptos/m1u3-higiene-de-datos.md).
- En producción aparece dentro de "integración y datos" en los
  [requisitos de M1U4](/conceptos/m1u4-demo-a-produccion.md).

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

# Cautelas

* Cotejada contra M1U3, p. 2, 5, 6 y 10 (PDF de 13 páginas). Se corrigió una
  inferencia: el curso no dice que el contrato "guíe" la generación; el prompt incluye
  el esquema (p. 10) y el contrato se usa para validar (p. 11).
* Las herramientas (Data Contract CLI, Datahub, Data Mesh Manager) son atribuciones del
  curso; la fuente "Data Contracts in Action" no trae URL (p. 12).

[^m1u3]: M1U3, Tema 3 (p. 5-6), conceptos clave (p. 2) y ejemplo aplicado (p. 10)
