---
type: Hecho
title: "Seguridad de la información y certificaciones"
description: "La organización tiene un sistema de gestión de seguridad certificado; el producto propio de medios de pago todavía no tiene su propio sistema de gestión certificado."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Ficha completa cotejada con el sitio institucional, los documentos de OKR y el diseño del sistema de propuestas comerciales de septiembre de 2026: certificación de la organización, estado del sistema de gestión del producto de pagos, auditoría prevista, capacitación, indicadores y concentración de capacidades. Incluye la precisión de auditorías anuales de seguimiento en lugar de renovación anual y conserva la falta de evidencia de controles específicos de IA adicionales a la política. Confirmado por Martín en esta conversación."
tags: [caso, seguridad, compliance]
sources:
  - id: web-empresa
    resource: "Sitio web institucional de la empresa (URL en private/sources.md)"
    title: "Sitio web de Acme Labs, accedido el 2026-10-13"
  - id: interno-okr-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)"
  - id: interno-propuestas-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Diseño del sistema de propuestas comerciales, septiembre de 2026 (privado, anonimizado)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Dos hechos que no se mezclan

1. **La organización** tiene certificación ISO/IEC 27001 vigente, con auditorías
   anuales de seguimiento; el sitio muestra el sello de la certificación.[^web-empresa] [^interno-propuestas-2026]
2. **El producto propio A** (medios de pago) está construyendo su propio sistema
   de gestión de seguridad, que todavía no está certificado: no debe presentarse
   como plataforma certificada.[^interno-propuestas-2026]

# Ciclo de mejora

- Hay una auditoría externa prevista para 2027 dentro del ciclo de la certificación.
- Un plan de capacitación en seguridad de la información corre de octubre de 2026
  a enero de 2027 para todo el personal.
- Los indicadores de seguridad se miden por trimestre desde septiembre de 2026.

[^interno-okr-2026]

# Capacidad

Las capacidades de seguridad y gobierno de IA están concentradas en pocas
personas.[^interno-okr-2026]

# Cautelas

- El sitio no nombra la norma del sello; la mención a ISO/IEC 27001 sale de
  fuentes internas. No se nombra el organismo certificador para no sumar un rasgo
  identificatorio.
- No hay evidencia de controles específicos de IA (red teaming, DLP sobre
  prompts) más allá de la política de uso.

[^web-empresa]: Sitio web de Acme Labs, accedido el 2026-10-13
[^interno-okr-2026]: OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)
[^interno-propuestas-2026]: Diseño del sistema de propuestas comerciales, septiembre de 2026 (privado, anonimizado)
