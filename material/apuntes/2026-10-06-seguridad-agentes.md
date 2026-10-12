---
type: Apunte de clase
title: Apunte 2026-10-06, seguridad de agentes de IA
description: Notas de la clase sobre inyección directa e indirecta, jailbreaks, marcos de referencia, scorecard de madurez y red teaming continuo.
tags: [apunte, m3, seguridad, red-teaming]
sources:
  - id: apunte-1006
    resource: Apuntes de clase de Martin (LazyMind), 2026-10-06
    title: Notas de la clase del 2026-10-06
    author: human:lazynet
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:10:00Z }
---

# Unidad que respalda

[M3U1 Seguridad, riesgos y resiliencia](/unidades/m3u1-seguridad.md).

# Ideas clave

- **Amenazas:** inyección directa e indirecta, y jailbreaks (DAN,
  personificación). Los modelos viejos son más vulnerables.[^apunte-1006]
- **Pruebas continuas:** hacen falta pruebas de regresión y red teaming continuo,
  no solo reactivo.[^apunte-1006]

# Marcos y herramientas de referencia

OWASP Top 10 LLM, MITRE ATLAS, NIST AI RMF, y herramientas de prueba como
PromptMap, PromptFoo y LangSmith (corridas en CI/CD).[^apunte-1006]

# Scorecard de madurez en seguridad

Dimensiones que se mencionaron:[^apunte-1006]

- Inventario de agentes.
- Permisos.
- Aprobación humana en acciones críticas.
- Gestión de secretos.
- Tasa de éxito en red teaming.

# Casos de estudio mencionados

Finbot, chatbot de McDonald's e inyección en documentos judiciales.[^apunte-1006]

# Ejercicios sugeridos

- Red teaming proactivo en el entorno de desarrollo con repositorios de pruebas.
- Armar un scorecard de madurez en seguridad para la organización.
- Pruebas de regresión en cada cambio de producción.
- Tests automáticos en CI/CD más pruebas manuales.

Todos sugeridos para el conjunto de los alumnos.[^apunte-1006]

# Cautelas

- "Libertas" y "CIVALS" figuran en la nota original y no se pudieron identificar
  con certeza (posible ruido de transcripción); se omiten de la lista de
  herramientas.
- Los casos de estudio se citaron por nombre, sin detalle ni fuente; verificar
  antes de usarlos como evidencia.

# Pistas para el TIF y la defensa

El apunte no registra consignas explícitas del TIF. Lectura nuestra: el
scorecard de cinco dimensiones sirve como métrica de éxito del frente de
seguridad en el roadmap, y el red teaming continuo como control con costo
recurrente en el presupuesto.

[^apunte-1006]: Apuntes de clase de Martin (LazyMind), 2026-10-06
