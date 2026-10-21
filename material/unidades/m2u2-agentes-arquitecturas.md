---
type: Unidad
title: M2U2 Agentes de IA y arquitecturas modernas
description: Taxonomías y patrones de agentes, uso de herramientas, recuperación de contexto y evaluación del recorrido hasta el resultado.
status: draft
tags: [m2, agentes, arquitectura, herramientas, evaluacion]
sources:
  - id: m2u2-presentacion
    resource: Módulo 2 — Unidad 2 — Agentes de IA y arquitecturas modernas.pdf
    title: "Presentación oficial, M2U2: Agentes de IA y arquitecturas modernas (15 páginas)"
  - id: m2u2-u6
    resource: Documento_Chief_AI_Officer_CAIO_Modulo_2_Unidad_6.pdf
    title: "Documento de lectura, Unidad 6: Agentes de IA y arquitecturas modernas (10 páginas)"
generated: { by: codex/gpt-6, at: 2026-10-21 }
---

# De qué trata

M2U2 corresponde a la Unidad 6 en la numeración corrida. La presentación y el
documento cubren agentes y sus arquitecturas; el documento desarrolla ReAct y
el uso de herramientas, y la presentación agrega recuperación de contexto,
memoria y evaluación del recorrido.[^m2u2-presentacion][^m2u2-u6]

| Tema | Alcance del material |
|---|---|
| Taxonomías | La presentación distingue chatbots, workflows, agentes simples y swarms (p. 3); el documento recorre agentes reactivos, basados en modelos, objetivos, utilidad y aprendizaje (pp. 3-4).[^m2u2-presentacion][^m2u2-u6] |
| Arquitecturas | Planificador/ejecutor, supervisor/especialistas y grafos en la presentación (p. 4); modelo, memoria, herramientas, bucle de orquestación y ReAct en el documento (pp. 4-5).[^m2u2-presentacion][^m2u2-u6] |
| Herramientas | El modelo propone la llamada y sus argumentos; el runtime o backend ejecuta y devuelve el resultado (presentación p. 5; documento pp. 5-6).[^m2u2-presentacion][^m2u2-u6] |
| Contexto e integración | RAG, memoria vectorial, grafos de conocimiento y Model Context Protocol (presentación pp. 6-7, 10-11); caso de orquestador y especialistas de soporte (documento pp. 6-7).[^m2u2-presentacion][^m2u2-u6] |
| Evaluación | Calidad de la respuesta, latencia, costo y calidad de la trayectoria, con un caso de conexión a herramientas (presentación pp. 12-14).[^m2u2-presentacion] |

# Relación con el plan

Como aplicación al plan, permite justificar el patrón de coordinación, separar
la decisión del modelo de la ejecución y evaluar las herramientas utilizadas
además del resultado final. Complementa [Modelo + Harness](/conceptos/harness-agente-modelo-mas-harness.md),
[estrategias de contexto](/conceptos/m1u3-estrategias-de-contexto.md) y
[evals](/conceptos/m2u4-evals.md).[^m2u2-presentacion][^m2u2-u6]

# Cautelas

- La ficha sigue en `draft`: leer e indexar los PDFs no constituye verificación humana.
- La presentación se acepta como material oficial de la unidad por decisión de Martin del 21/10/2026; el documento de lectura se conserva como complemento.
- Son dos taxonomías pedagógicas diferentes; no se presume equivalencia entre sus categorías (presentación p. 3; documento pp. 3-4).[^m2u2-presentacion][^m2u2-u6]
- El documento usa la sigla MCP tanto para «Multi-Agent Conversation Patterns» como para «Model Context Protocol» (pp. 6-7). La presentación la usa para el protocolo (p. 10). La ficha conserva esa distinción y no usa la primera expansión como definición del protocolo.[^m2u2-u6][^m2u2-presentacion]
- Las capacidades y ventajas atribuidas a productos y frameworks no se verificaron contra documentación técnica vigente. La expresión de costo de la presentación (p. 12) no se toma como fórmula del business case.[^m2u2-presentacion]

[^m2u2-presentacion]: Módulo 2 — Unidad 2 — Agentes de IA y arquitecturas modernas.pdf, presentación oficial, páginas indicadas en cada referencia; alcance general en pp. 2-15.
[^m2u2-u6]: Documento_Chief_AI_Officer_CAIO_Modulo_2_Unidad_6.pdf, documento de lectura, páginas indicadas en cada referencia; introducción y objetivos en pp. 1-2.
