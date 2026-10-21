---
type: Concepto
title: Higiene de datos a escala
description: Prácticas automatizadas de limpieza, estructuración y normalización que protegen al modelo de errores sistemáticos.
tags: [m1, datos, calidad]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 13 páginas
status: draft
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Qué es

Conjunto de prácticas sistemáticas para detectar, corregir y prevenir errores en los
datos: faltantes, duplicados, inconsistencias de formato, outliers y esquemas mal
definidos. Es "el punto de partida de cualquier pipeline de IA confiable" (p. 2).[^m1u3]

Importa porque los modelos amplifican los patrones de los datos: **un error
sistemático en el 5% de los registros puede generar un sesgo perceptible** en las
salidas (p. 3).[^m1u3]

# Tres operaciones

| Operación | Qué incluye |
|---|---|
| Limpieza | Nulos (imputación, eliminación o marcado explícito), deduplicación, estandarización de formatos (fechas, monedas, codificaciones), validación de tipos contra un esquema |
| Estructuración | Pasar datos semiestructurados o no estructurados (PDFs, correos, logs, transcripciones) a JSON, Parquet o tablas relacionales |
| Normalización | Reducir redundancia y asegurar consistencia: "Buenos Aires", "Bs. As." y "CABA" se unifican en una representación canónica |

Las transformaciones deben **documentarse y versionarse** para garantizar
reproducibilidad (p. 4).[^m1u3]

# A escala

- Orquestación con Apache Airflow o dbt, y plataformas cloud como Google BigQuery.
- En 2024, BigQuery DataFrames sumó generación de datos sintéticos con LLMs, en un
  workflow único de procesamiento, ML y generación, sin sacar los datos del entorno
  cloud (p. 4).[^m1u3]

# Auditoría y sesgos

La auditoría periódica verifica distribuciones, detecta drift y analiza outliers para
encontrar sesgos antes de que aparezcan en las salidas. La mitigación de sesgos exige
revisar la representatividad (categorías demográficas, idiomas, casos de uso) y no
solo limpiar (p. 6).[^m1u3]

Se formaliza con [data contracts](/conceptos/m1u3-data-contracts.md).

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

# Cautelas

* Cotejada contra M1U3, p. 2-6 (PDF de 13 páginas). Se corrigió la cita de auditoría y
  sesgos: es la p. 6, no la 5-6.
* El "5% de registros con error sistemático genera un sesgo perceptible" (p. 3) es una
  afirmación del curso, sin fuente. No va en una slide como dato.
* La agrupación en limpieza, estructuración y normalización sigue el título del Tema 1
  (p. 3); asignar la estandarización de formatos a "limpieza" es de la ficha.

[^m1u3]: M1U3, Tema 1 (p. 3-4), Tema 3 (p. 5-6) y conceptos clave (p. 2)
