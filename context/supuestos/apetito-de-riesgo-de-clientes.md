---
type: Supuesto
title: "Apetito de riesgo de los clientes financieros frente a la IA"
description: "El plan adopta como supuesto una restricción por defecto para usar modelos externos sobre código y datos de clientes financieros, hasta contar con habilitación contractual y controles demostrables."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Supuesto de diseño confirmado por Martín: restricción por defecto para usar modelos externos sobre código y datos de clientes financieros y mínimos propuestos de habilitación contractual, inventario, ubicación, no entrenamiento y controles. Incluye revisar el supuesto ante contratos permisivos o demanda activa de IA y relevar y completar la matriz con Comercial. Se precisa que la matriz figuraba pendiente en abril y su estado actual sigue por contrastar; la restricción por defecto se conserva como supuesto del plan. Confirmado en esta conversación."
tags: [supuesto, compliance, clientes]
sources:
  - id: regulacion-clientes
    resource: "context/hechos/regulacion-clientes-financieros.md"
    title: "Regulación por sujeto y actividad, IA de terceros y datos personales"
  - id: gobierno-ia
    resource: "context/hechos/gobierno-y-politica-ia.md"
    title: "Antecedente de política de abril y estado de la matriz por contrastar"
  - id: oferta-ia
    resource: "context/hechos/ia-en-producto-y-oferta.md"
    title: "Propuesta comercial y elección de herramientas en consultoría"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Para diseñar el plan, se adopta una restricción por defecto sobre el uso de
modelos externos con código y datos de clientes financieros. Los mínimos
propuestos para habilitarlo son cláusula contractual, inventario del uso,
ubicación de los datos, no entrenamiento con sus datos y evidencia de controles
(registro, revisión humana, gestión de incidentes).

# Por qué es razonable

- El BCRA obliga a las entidades a documentar y gestionar el uso de IA propio y
  de terceros (ver [regulación](/hechos/regulacion-clientes-financieros.md)).[^regulacion-clientes]
- El secreto financiero y la protección de datos imponen condiciones según el
  sujeto y la actividad.[^regulacion-clientes]
- El antecedente de política de abril contemplaba validación cliente por cliente
  y registraba la matriz de restricciones como pendiente. Su estado actual sigue
  por contrastar (ver [gobierno](/hechos/gobierno-y-politica-ia.md)).[^gobierno-ia]
- La propuesta comercial indica que en consultoría el cliente elige las
  herramientas (ver [IA en producto](/hechos/ia-en-producto-y-oferta.md)).[^oferta-ia]

# Qué lo invalidaría

- Que los contratos vigentes resulten permisivos al armar la matriz.
- Que los clientes pidan activamente IA a su proveedor como condición.

# Cómo verificarlo

Relevar el estado actual y completar la matriz de restricciones contractuales
por cliente con el área comercial, y registrar el resultado con su fuente
anonimizada.

# Cautelas

- La restricción por defecto es un supuesto de diseño. El apetito real de cada
  cliente se valida con sus contratos, autorizaciones y requisitos aplicables.

[^regulacion-clientes]: Regulación argentina que pesa sobre los clientes financieros, alcance por sujeto y actividad.
[^gobierno-ia]: Gobierno y política de IA existentes, antecedente de abril y pendientes históricos por contrastar.
[^oferta-ia]: IA en el producto y en la oferta a clientes, propuesta comercial y elección de herramientas en consultoría.
