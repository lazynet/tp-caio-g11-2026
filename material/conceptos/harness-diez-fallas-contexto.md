---
type: Concepto
title: Las diez fallas de contexto
description: Catálogo de diez fallas de un chatbot sin harness, cada una con qué es, por qué ocurre y la solución agéntica.
tags: [arquitectura, seguridad, contexto, harness]
sources:
  - id: harness
    resource: Memoria-Contexto-Harness.pdf
    title: Data Management en Soluciones de Gen IA, 16 páginas
  - id: chroma-rot
    resource: https://research.trychroma.com/context-rot
    title: Hong, Troynikov, Huber (Chroma). Context Rot, informe técnico, 14-07-2025
  - id: liu-lost-middle
    resource: https://arxiv.org/abs/2307.03172
    title: Liu et al. Lost in the Middle, TACL 2023, arXiv 2307.03172
  - id: kurfali-needles
    resource: https://aclanthology.org/2025.emnlp-main.1742/
    title: Kurfali y Östling. Conflicting Needles in a Haystack, EMNLP 2025
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:05:00Z }
---

# Idea central

El PDF muestra diez formas en que un chatbot falla con el contexto, y a cada una le
opone una "solución agéntica" que vive en el
[harness](/conceptos/harness-agente-modelo-mas-harness.md), no en el modelo. Cada
ficha tiene tres partes: qué es, por qué ocurre y tres medidas. El lema del deck:
"El chatbot solo demuestra. La solución es el harness."[^harness]

La ventana de contexto en sí (qué entra, límites de entrada y salida) está en
[ventana de contexto](/conceptos/harness-ventana-de-contexto.md).

# Resumen

| # | Falla | En una línea |
|---|---|---|
| 1 | Context rot | La calidad cae antes de llenar la ventana |
| 2 | Lost in the middle | El dato del medio no se recupera |
| 3 | Silent truncation | El runtime corta sin avisar |
| 4 | Tool-output bloat | El volcado de una tool tapa la decisión |
| 5 | Retrieval noise | Gana lo parecido, no lo vigente |
| 6 | Conflicting needles | Dos hechos incompatibles, y el modelo elige uno sin avisar |
| 7 | Compaction loss | El resumen pierde la excepción |
| 8 | Indirect prompt injection | Texto no confiable se trata como orden |
| 9 | Context cost and latency | Contexto lleno cuesta más y no responde mejor |
| 10 | Instruction drift | El contrato del turno 1 deja de regir |

# Las diez fichas

## 1. Context rot (p. 3)

- **Qué es:** a medida que crece el contexto, el modelo usa peor lo que ya estaba. La calidad cae antes de que la ventana se llene: olvida una regla, duda un hecho, se contradice.
- **Por qué ocurre:** la atención se diluye entre más tokens y lo temprano pesa menos. No es un corte duro sino una degradación, y el runtime no avisa. El PDF cita a Chroma, 2025.
- **Solución:** (1) un hilo por tarea, sin "append forever"; (2) presupuesto de working set, y si la calidad baja, cortar; (3) compactar a un *ledger* (decisión, constraint, excepción) y seguir con eso, no con el hilo entero; la regla fija se reinyecta, no se espera que sobreviva.[^harness]

## 2. Lost in the middle (p. 4)

- **Qué es:** el dato está en la ventana y aun así no se recupera si quedó en el medio. Ganan el inicio y el final (Liu et al., 2023).
- **Por qué ocurre:** la atención de un transformer privilegia el principio (primacía) y el final (recencia).
- **Solución:** (1) el hecho crítico y la regla van al inicio del working set y se repiten al final; (2) no enterrar política en el cuerpo de un documento recuperado; (3) el rerank también posiciona: "estar en el contexto" no alcanza.[^harness]

## 3. Silent truncation (p. 5)

- **Qué es:** el runtime corta el inicio o el medio para entrar en la ventana, y el modelo sigue como si el contrato estuviera entero. Nadie dice qué se comió.
- **Por qué ocurre:** la ventana es un límite duro; SDKs y apps recortan tokens viejos o del medio, a menudo sin error visible.
- **Solución:** (1) presupuesto explícito, y si no entra, fallar en voz alta; (2) si se compacta, registrar qué se bajó, nunca un clip silencioso del SDK; (3) la regla vigente vive fuera del blob recortado y se reinyecta después de cualquier corte.[^harness]

## 4. Tool-output bloat (p. 6)

- **Qué es:** una tool devuelve un volcado (JSON, HTML, log) que se come el contexto y tapa la decisión que importaba.
- **Por qué ocurre:** las tools devuelven el payload crudo y el loop del agente lo appendea en el mismo canal que el plan; la atención se va al dump.
- **Solución:** (1) la tool devuelve un resumen y un id, y el archivo vive afuera; (2) tope de tokens de salida, y si hace falta más, se pide un slice; (3) la decisión (por ejemplo RECHAZAR y el motivo) queda en el ledger, no dentro del JSON.[^harness]

## 5. Retrieval noise (p. 7)

- **Qué es:** el retrieval trae varios pasajes parecidos y el modelo elige el familiar o el repetido, no el vigente ni el que tiene autoridad.
- **Por qué ocurre:** la búsqueda semántica rankea similitud, no validez, y los casi-duplicados compiten. Sin un campo de autoridad, "el más parecido" le gana a "el que rige".
- **Solución:** (1) pocos pasajes, rerank y metadata (fecha, estado, fuente); (2) evaluar el retrieval aparte de la respuesta y citar el documento; (3) "vigente" es un campo, y staging e histórico no entran al working set.[^harness]

## 6. Conflicting needles (p. 8)

- **Qué es:** dos hechos incompatibles conviven en el contexto y el modelo elige uno sin decir que hay conflicto. Sesgo de posición y de repetición (EMNLP 2025).
- **Por qué ocurre:** el modelo predice el siguiente token y no es un store versionado. Si el harness no versiona, la repetición y la recencia le ganan a "esto reemplazó a aquello".
- **Solución:** (1) una verdad vigente, con timestamp, y lo viejo se reemplaza, no se apila; (2) la escritura va a memoria externa con versión, y el chat no acumula precios; (3) ante conflicto, el agente lo marca y para, no promedia (ni 12 ni 26 si la corrección dijo 40).[^harness]

## 7. Compaction loss (p. 9)

- **Qué es:** al resumir el hilo para que entre, el resumen cuenta la historia y pierde la excepción, el número, el constraint. El turno siguiente aplica la política y se la salta.
- **Por qué ocurre:** el resumen optimiza lo que suena a relato, y la excepción es un token raro. El modelo no sabe qué no puede perder.
- **Solución:** (1) compactar a ledger, no a ensayo: decisión, constraint, excepción, con el número; (2) schema del resumen, y un constraint que gatea una acción no se cae; (3) el resto se reconstruye, la excepción no.[^harness]

## 8. Indirect prompt injection (p. 10)

- **Qué es:** un texto no confiable que entra al contexto (documento, página, resultado de tool) trae una orden y el modelo la trata como instrucción.
- **Por qué ocurre:** la ventana no tiene tipos. Una línea de un PDF y una línea del usuario son el mismo tipo de token; dato e instrucción comparten canal.
- **Solución:** (1) lo recuperado y lo que devuelve una tool es dato, marcado, nunca una orden; (2) las órdenes solo vienen del usuario o del system, con el canal separado; (3) **gate humano antes de un efecto** (enviar, pagar, borrar). En clase, la señal es una palabra que no estaba en el pedido.[^harness]

## 9. Context cost and latency (p. 11)

- **Qué es:** la misma pregunta cuesta más y tarda más cuando el contexto está lleno, y no responde mejor. En un agente, eso es plata y un prefix cache roto.
- **Por qué ocurre:** cada turno reprocesa cada token, y reenviar el mundo cambia el prefijo y anula el cache. Decirle "ignorá lo anterior" no saca tokens de la ventana.
- **Solución:** (1) working set corto y prefijo estable (system + tools) para que el cache pegue; (2) no reenviar el mundo en cada turno, pedir un slice; (3) medir tokens y latencia del loop, no solo la calidad de la respuesta.[^harness]

Ver [tokenomics](/conceptos/m2u4-tokenomics.md).

## 10. Instruction drift (p. 12)

- **Qué es:** el contrato del turno 1 deja de regir. El modelo optimiza el último tono, no el objetivo.
- **Por qué ocurre:** nada reinyecta la instrucción vigente, así que la recencia gana. Unos turnos amables pisan el contrato, y sin harness no hay quién lo reafirme.
- **Solución:** (1) objetivo y reglas en el working set de cada turno, no "acordate de lo que dije"; (2) si cambia la tarea, sesión nueva, porque el tono nuevo no reescribe el contrato; (3) gate: la salida se chequea contra el contrato antes de salir, con humano en lo irreversible.[^harness]

# Labs

La p. 13 propone tres labs de chatbot tradicional "fáciles de entender y probar", con
capturas de pantalla de conversaciones, sin texto explicativo. Los enunciados no se
pueden extraer del PDF.[^harness]

# Verificación externa

Tres atribuciones del PDF se chequearon contra la fuente primaria:

| Atribución del PDF | Resultado |
|---|---|
| Chroma, 2025 (context rot) | Confirmada: informe técnico "Context Rot: How Increasing Input Tokens Impacts LLM Performance", 14-07-2025, de Hong, Troynikov y Huber; evalúa 18 LLM y concluye que la confiabilidad cae al crecer la entrada, incluso en tareas simples.[^chroma-rot] |
| Liu et al., 2023 (lost in the middle) | Confirmada: arXiv 2307.03172, TACL 2023; patrón en U, mejor al inicio y al final, peor en el medio, y la precisión cae con el largo de entrada.[^liu-lost-middle] |
| EMNLP 2025 (conflicting needles) | Confirmada: Kurfali y Östling, EMNLP 2025; con tres "needles" mutuamente excluyentes, los modelos casi nunca señalan el conflicto y muestran sesgo por repetición y recencia.[^kurfali-needles] |

Las soluciones del PDF (ledger, gates, presupuesto de working set) son el criterio de
diseño de la cátedra, no resultados de esos papers.

[^harness]: Data Management en Soluciones de Gen IA (Memoria-Contexto-Harness.pdf), p. 3-13; las páginas figuran entre paréntesis en cada ficha.
[^chroma-rot]: Chroma, Context Rot: https://research.trychroma.com/context-rot
[^liu-lost-middle]: Liu et al., Lost in the Middle: https://arxiv.org/abs/2307.03172
[^kurfali-needles]: Kurfali y Östling, Conflicting Needles in a Haystack: https://aclanthology.org/2025.emnlp-main.1742/
