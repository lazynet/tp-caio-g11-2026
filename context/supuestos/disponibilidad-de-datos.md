---
type: Supuesto
title: "Disponibilidad de datos para casos de IA"
description: "El escenario prioriza fuentes internas como candidatas para IA, sujetas a permisos, clasificación y calidad, y excluye datos productivos de clientes y datos de categoría especial."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Supuesto de diseño confirmado por Martín para los 12 meses: fuentes internas candidatas sujetas a permisos, clasificación y calidad; datos operativos de productos propios anonimizados o sintéticos; exclusión de datos productivos de clientes y datos de categoría especial. Incluye precisar el carácter histórico de la política de abril y reemplazar la afirmación no acreditada sobre pipelines propios y salud de repositorios por telemetría de uso y registros de costos documentados. Se conservan la validación del inventario, accesos e integración y las condiciones que obligan a revisar el supuesto. Confirmado en esta conversación."
tags: [supuesto, datos, arquitectura]
sources:
  - id: gobierno-ia
    resource: "context/hechos/gobierno-y-politica-ia.md"
    title: "Antecedente de política de abril y aprobación informada con sus cautelas"
  - id: uso-ia
    resource: "context/hechos/uso-ia-interno.md"
    title: "Telemetría de uso interno de IA y límites de la medición"
  - id: costos-tecnologia
    resource: "context/hechos/costos-tecnologia-e-ia.md"
    title: "Registros de costos de tecnología e IA por fuente y corte"
  - id: inventario-datos
    resource: "context/hechos/inventario-y-distribucion-de-datos.md"
    title: "Existencia informada del inventario y aspectos por contrastar"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

En los 12 meses del plan, los casos de IA se alimentan de:

- **Fuentes candidatas, sujetas a permisos, clasificación y calidad:**
  repositorios propios, tickets y documentación de proyectos, telemetría de
  ingeniería y de uso de IA, datos financieros operativos internos.
- **Con anonimización o datos sintéticos:** datos operativos de los productos
  propios.
- **Excluidos:** datos productivos de clientes y datos de categoría especial.

# Por qué es razonable

- El antecedente documental de política de abril prohíbe enviar datos personales
  de clientes a IA externa y establece reglas propias para el producto con datos
  de categoría especial. Su correspondencia con la versión aprobada sigue por
  contrastar (ver [gobierno](/hechos/gobierno-y-politica-ia.md)).[^gobierno-ia]
- Hay telemetría de uso de IA y registros de costos documentados (ver
  [uso de IA](/hechos/uso-ia-interno.md) y
  [costos](/hechos/costos-tecnologia-e-ia.md)).[^uso-ia][^costos-tecnologia]

# Qué lo invalidaría

- Que los permisos o la calidad de los datos internos sean insuficientes para
  los casos previstos.
- Que un cliente habilite contractualmente el uso de sus datos.

# Cómo verificarlo

Revisar el [inventario existente](/hechos/inventario-y-distribucion-de-datos.md)
como primer entregable de la fase de diagnóstico: contrastar su vigencia,
cobertura, responsables, clasificación y calidad documentada para las fuentes
elegibles de los casos de IA. Completar las brechas sobre ese inventario y
verificar accesos e integración entre los sistemas que contienen los datos.[^inventario-datos]

# Cautelas

- La elegibilidad efectiva de cada fuente requiere confirmar permisos,
  restricciones contractuales, clasificación y calidad en la validación inicial.
- Se conserva el carácter de supuesto de diseño para el horizonte del plan.

[^gobierno-ia]: Gobierno y política de IA existentes, antecedente documental de abril y límites de la aprobación informada.
[^uso-ia]: Uso actual de IA en la operación interna, telemetría y cautelas de alcance.
[^costos-tecnologia]: Costos de tecnología e IA, registros por fuente y corte temporal.
[^inventario-datos]: Inventario y distribución de datos, existencia informada y validaciones propuestas.
