---
type: Concepto
title: Tres capas que se confunden con el harness
description: Distinción entre framework o SDK, runtime de orquestación y harness, con los ejemplos que da el curso.
tags: [arquitectura, agentes, harness, build-buy]
sources:
  - id: harness
    resource: Memoria-Contexto-Harness.pdf
    title: Data Management en Soluciones de Gen IA, 16 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Memoria-Contexto-Harness.pdf, p. 15 (tabla de tres capas, cita atribuida a Harrison Chase y recuadro de dónde se construye el harness); atribución y productos no cotejados con fuente primaria. Cotejo del agente revisado y confirmado por Martín en esta conversación."
---

# Las tres capas (p. 15)

El curso advierte que "harness" se confunde con tres capas distintas, y propone
separarlas:[^harness]

| Capa | Qué es | Ejemplos del curso |
|---|---|---|
| Framework / SDK | Piezas para armar el agente | LangChain, CrewAI, OpenAI Agents SDK, Strands |
| Runtime / orquestación | Cómo corre el grafo, los retries y el estado | LangGraph, Temporal |
| Harness | El entorno ya armado alrededor del modelo | Deep Agents, Claude Code, Codex, Grok Build, Microsoft HarnessAgent |

# Notas de la slide

- **LangGraph + Deep Agents** es "el stack más citado".
- **Microsoft Agent Framework** aparece con HarnessAgent.
- **Strands Agents** se vende literalmente como "build an agent harness".
- **Grok Build** es el harness de coding de xAI: TUI, tools, sandbox y loop.
- La frase más citada, atribuida a Harrison Chase (LangChain): "LangGraph es el
  runtime. LangChain es la abstracción. Deep Agents es el harness."[^harness]

# Cautelas

La atribución a Harrison Chase y la clasificación de productos concretos (Grok Build,
HarnessAgent, Strands) son del PDF y no se verificaron con la fuente primaria. Los
productos cambian rápido; para una decisión de build, buy o partner hay que
reverificar cada uno. Cotejada contra el PDF, p. 15 (tabla, cita y recuadro "Dónde se
construye el harness hoy"). Strands figura como framework en la tabla y, en el
recuadro, como producto que se vende "literal" como "build an agent harness": la
ambigüedad es del PDF. Ver [Agente = Modelo + Harness](/conceptos/harness-agente-modelo-mas-harness.md).

[^harness]: Data Management en Soluciones de Gen IA (Memoria-Contexto-Harness.pdf), p. 15.
