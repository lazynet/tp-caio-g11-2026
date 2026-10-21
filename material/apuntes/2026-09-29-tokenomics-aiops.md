---
type: Apunte de clase
title: Apunte 2026-09-29, costos de modelos, tokenomics y AIOps
description: Notas de la clase sobre costos medidos en tokens, enrutamiento entre modelos, evals con release gate y cambio del modelo de facturación.
tags: [apunte, m2, tokenomics, aiops, evals]
sources:
  - id: apunte-0929
    resource: Apuntes de clase de Martin (LazyMind), 2026-09-29
    title: Notas de la clase del 2026-09-29
    author: human:lazynet
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:10:00Z }
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Nota de clase del 2026-09-29 en LazyMind (resumen automático, sin transcripción): la ficha reproduce sus ideas; las cifras quedan declaradas sin fuente primaria. Cotejo del agente revisado y confirmado por Martín en esta conversación."
---

# Unidad que respalda

[M2U4 AIOps, observabilidad y economía](/unidades/m2u4-aiops.md).

# Ideas clave

- **Costos en tokens, no en hardware:** los modelos nuevos bajaron costos hasta
  un 50%.[^apunte-0929]
- **Evals antes de producción:** usar evals automáticos con casos reales de la
  empresa antes de poner un modelo nuevo en producción.[^apunte-0929]
- **Modelo liviano como router:** si la confianza es baja, deriva a un modelo más
  potente; si es alta, clasifica directo.[^apunte-0929]
- **LLMOps / AgentOps:** evaluación automática con release gate, y métricas como
  TTFT (latencia al primer token) y consumo en millones de
  tokens.[^apunte-0929]
- **Modelo de negocio:** pasa de facturar por hora o perfil a facturar por costo
  de tokens o por outcome.[^apunte-0929]

# Herramientas mencionadas

LangSmith, LangFuse, LiteLLM y PromptFoo (observabilidad y
evaluación).[^apunte-0929]

# Demos

- Router con un modelo liviano y uno potente: el costo de un caso bajó de 360 a 7
  dólares.[^apunte-0929]
- Clasificación de ironía y urgencia en tickets: el modelo clasificó con alta
  confianza, a diferencia del humano (así lo dice la nota).[^apunte-0929]

# Cautelas

- Las notas dicen "~66% más barato" junto a 360 → 7 dólares, pero esa baja es de
  cerca del 98%. Una de las dos cifras está mal anotada; no usar ninguna en
  slides sin la fuente.
- "Hasta un 50%" de baja de costos de los modelos nuevos: sin fuente primaria.
- La nota de LazyMind es un resumen automático (wrapup) de la sesión grabada, con la
  transcripción vacía; no son apuntes escritos a mano. Cotejada el 2026-10-20: cada
  idea de la ficha figura en el resumen, pero no hay transcripción contra la cual
  verificar el resumen mismo. La nota dice "PromptFu"; la ficha lo normaliza a
  PromptFoo por inferencia. Nombra además el modelo liviano de la demo; la ficha no.
- "mtoc" en la nota original es casi seguro un error de transcripción de MTok
  (millones de tokens); no se verificó.

# Pistas para el TIF y la defensa

El apunte no registra consignas explícitas del TIF. Lectura nuestra: el release
gate con evals sobre casos reales y el pasaje a facturación por outcome son
argumentos para el CFO escéptico; cualquier cifra de ahorro tiene que salir con
supuesto y fuente.

[^apunte-0929]: Apuntes de clase de Martin (LazyMind), 2026-09-29
