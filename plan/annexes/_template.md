---
owner: finance
status: draft
title: Anexo X — Nombre del tema
---

<!-- Plantilla de anexo. Copiala como plan/annexes/NN-tema.md (el número fija el
     orden en el PDF de entrega), cambiá owner por el agente dueño y borrá estos
     comentarios. Los archivos que empiezan con _ no se validan ni se entregan.

     Un anexo es evidencia procesada, no datos crudos: el CFO o el board lo lee para
     entender de dónde salió cada número de la slide y qué tan sólido es el
     razonamiento. Todo dato interno va anonimizado (ver "Datos privados" en
     AGENTS.md). En el PDF los links no navegan: nombrá el anexo en la slide
     ("ver Anexo B — Finanzas") además de enlazarlo. -->

# Anexo X — Nombre del tema

Slide que sustenta: [Slide N — Título](../slides.md).

## Objetivo

Qué afirmación o decisión de las slides sustenta este anexo, en una o dos oraciones.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Costo por consulta humana | USD X | [Fuente](/context/ejemplo.md) o "supuesto del equipo" |
| Volumen mensual | N consultas | ... |

## Evidencia

Prueba de concepto, benchmark o caso comparable que respalda los supuestos.

| Métrica | Hoy | Esperado | Fuente |
|---|---|---|---|
| Latencia | | | |
| Resolución al primer contacto | | | |
| Precisión | | | |

Un gráfico simple si ayuda (por ejemplo, la curva de costos a 12 meses), generado
desde los datos de este anexo.

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| Alucinaciones del modelo | | | Guardrails y supervisión humana sobre un % de interacciones | |

## Decisiones

Qué se eligió y por qué, contra qué alternativas (por ejemplo, RAG frente a
fine-tuning) y con qué criterio de costo-beneficio. Indicá si la decisión es
reversible o no.
