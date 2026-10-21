---
type: Supuesto
title: "Precio de los modelos y dependencia de proveedor"
description: "El plan supone costo estable o menor por unidad comparable de uso o resultado, contempla un escenario de pago por consumo y valida portabilidad y costo de migración sin anticipar cambios de precios."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Hipótesis de diseño confirmadas por Martín: costo por unidad comparable de uso o resultado estable o menor en los 12 meses, escenario de estrés de pago por consumo y migración de costo moderado sujeta a prueba de portabilidad y diseño neutral al modelo. Se retira la tendencia de precios en baja como hecho sin fuente; el múltiplo aproximado de 12 veces a precio de API se conserva como estimación de telemetría, sin demostrar cambio de precios. Incluye revisión mensual por persona activa y resultado, y revisión del supuesto ante aumentos, recortes de límites o acoplamiento exclusivo. Confirmado en esta conversación."
tags: [supuesto, finanzas, arquitectura, riesgo]
sources:
  - id: costos-ia
    resource: "context/hechos/costos-tecnologia-e-ia.md"
    title: "Consumo valorizado a precio de API y límites de la estimación"
  - id: pilotos-ia
    resource: "context/hechos/encuesta-y-pilotos-ia.md"
    title: "Límites de uso y dependencia de proveedor informados en el piloto"
  - id: arquitectura
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, propuestas de ruteo y portabilidad"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

- Se supone que el costo por unidad comparable de uso o resultado se mantiene
  o baja durante los 12 meses, con calidad comparable.
- Se contempla un escenario de estrés de pago por consumo ante cambios de
  suscripción, sin afirmar que el proveedor vaya a cambiar su esquema.
- Se plantea una migración de costo moderado, sujeta a prueba de portabilidad.
  La neutralidad del harness (contratos de agente, skills, telemetría) es un
  objetivo de diseño.[^arquitectura]

# Por qué es razonable

El piloto interno registró límites de uso y preocupación por depender de un
solo proveedor (ver [encuesta](/hechos/encuesta-y-pilotos-ia.md)).[^pilotos-ia]

La telemetría de septiembre estima que el consumo valorizado a precio de API
equivale a unas 12 veces la suscripción de ese mes (ver
[costos](/hechos/costos-tecnologia-e-ia.md)).[^costos-ia]

Ese múltiplo se usa para construir un escenario de estrés; no es una factura
ni demuestra un cambio de precios. La evolución unitaria permanece como
hipótesis de planificación.

# Qué lo invalidaría

- Un aumento de precios o recorte de límites del proveedor principal.
- Que la arquitectura termine acoplada a funciones exclusivas de un proveedor.

# Cómo verificarlo

Revisión mensual de costo por persona activa y por resultado, con un escenario
de pago por consumo en el anexo financiero.

# Cautelas

- La ficha no acredita una tendencia de mercado ni cambios futuros de precio.
- La portabilidad y el costo de migración requieren prueba y medición; el
  diseño neutral al modelo no los garantiza por sí solo.
- Los escenarios se revisan con costos observados por unidad comparable y
  resultado, manteniendo las condiciones de calidad.

[^costos-ia]: Costos de tecnología e IA, valorización de telemetría a precio de API y suscripción de septiembre de 2026.
[^pilotos-ia]: Encuesta y pilotos internos de IA, límites de uso y preocupación por dependencia de proveedor, con sus cautelas de población.
[^arquitectura]: Anexo B, ruteo y portabilidad como objetivos y pruebas propuestas de diseño.
