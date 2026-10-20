---
type: Hecho
title: "Gobierno y política de IA existentes"
description: "Acme Labs tiene una política de uso aceptable de IA aprobada, según el responsable del caso; la aprobación no acredita la implementación de controles ni actualiza por sí sola los pendientes del registro de abril."
status: draft
tags: [caso, gobierno, ia, politicas]
sources:
  - id: confirmacion-caso-2026-10-20
    resource: "Confirmación del responsable del caso, 20/10/2026 (anonimizada)"
    title: "Aprobación de la política de uso de IA"
  - id: interno-politica-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)"
  - id: interno-estandares-ingenieria-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Estándares de ingeniería y contrato organizacional para agentes de código, 2026 (privado, anonimizado)"
  - id: interno-okr-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Política de uso aceptable de IA

El responsable del caso confirmó el 20/10/2026 que la política de uso de IA está
aprobada. La confirmación no identifica una versión, fecha de aprobación, acta ni
autoridad aprobadora revisadas documentalmente.[^confirmacion-caso-2026-10-20]

La aprobación informada no acredita la implementación ni la eficacia de los
controles, la operación de un AI Council ni el cierre de los pendientes del
registro de abril.[^confirmacion-caso-2026-10-20]

## Antecedente documental de abril de 2026

El registro al 21/04/2026 era la versión 1.0 en borrador, con dueño y sponsor
designados dentro de Tecnología. Las definiciones siguientes describen ese
antecedente; su correspondencia con la versión aprobada está por contrastar.[^interno-politica-ia-2026]

**Principios:** usar solo herramientas corporativas; desconfiar del output hasta
revisarlo; el humano es el responsable final; lo que no se mide no se justifica.[^interno-politica-ia-2026]

**Clasificación de datos en cuatro niveles:**

| Nivel | Ejemplos | ¿Se puede usar con IA externa? |
|---|---|---|
| Público | Sitio web, casos publicados | Sí |
| Interno | Organigrama, procesos | Sí, con herramientas aprobadas |
| Confidencial | Código propio, propuestas, reportes financieros operativos | Solo con SSO corporativo y contrato sin entrenamiento sobre los datos |
| Restringido | Datos personales de clientes, credenciales, código bajo NDA, contratos, resultados no divulgados | Nunca |

[^interno-politica-ia-2026]

**Controles definidos:** lista cerrada de lo que nunca se envía (incluye datos de
salud y categorías especiales de la Ley 25.326); validación comercial antes de
usar IA sobre código de un cliente; reglas propias para el producto que maneja
datos de categoría especial; revisión del output según su destino (code review,
responsable del área, dueño del dominio financiero o legal); aprobación de herramientas nuevas
por el comité de tecnología en 2 a 4 semanas; reporte de incidentes en el día,
sin sanción por reportar.[^interno-politica-ia-2026]

**Roles:** dueño de la política, sponsor, administrador técnico de licencias,
comité de tecnología como aprobador y auditoría mensual de uso.[^interno-politica-ia-2026]

# Pendientes históricos declarados en abril de 2026

El registro de abril declaraba los siguientes pendientes. La aprobación fue
informada posteriormente; el resto del estado y la evidencia documental de esa
aprobación quedan por contrastar.[^interno-politica-ia-2026][^confirmacion-caso-2026-10-20]

- Ratificación del Directorio y firma del dueño.
- Matriz de clientes con restricciones contractuales sobre modelos externos;
  hasta tenerla, cada caso se validaba a mano con el área comercial.
- Restricciones específicas de un banco cliente y del producto con datos de
  categoría especial.
- Onboarding formal de usuarios y revisión anual.

[^interno-politica-ia-2026]

# Gobierno técnico de los agentes de código

Existe un contrato organizacional para los agentes de código: reglas de datos,
servidores MCP aprobados (gestión de tickets, mensajería, suite ofimática,
repositorios, automatización de navegador y búsqueda local), permisos y *hooks*,
y la obligación de mencionar en el PR los cambios estructurales generados con
IA.[^interno-estandares-ingenieria-2026]

El alcance y la retención de la telemetría de uso de IA, junto con la excepción
del producto con datos de categoría especial, están pendientes de definir con
Talento como meta de 2027.[^interno-okr-2026]

# Cautelas

- La aprobación informada el 20/10/2026 actualiza el estado de la política, pero
  no convierte el borrador v1.0 en la versión aprobada ni acredita su fecha,
  acta o autoridad aprobadora.[^confirmacion-caso-2026-10-20]
- Los pendientes del 21/04/2026 son históricos y están por contrastar, salvo la
  aprobación informada; no se infiere que la matriz de restricciones, el
  onboarding o la revisión anual estén completos.[^interno-politica-ia-2026][^confirmacion-caso-2026-10-20]
- La evidencia de partida no registra inventario formal de casos de uso ni
  registro de riesgos de IA. La confirmación no acredita su existencia ni la
  operación del Council; su estado actual sigue por contrastar.[^interno-politica-ia-2026][^confirmacion-caso-2026-10-20]
- La ficha conserva `status: draft`: no hay revisión humana declarada contra
  la documentación de aprobación ni prueba de controles implementados.

[^confirmacion-caso-2026-10-20]: Confirmación del responsable del caso, 20/10/2026 (anonimizada), «Aprobación de la política de uso de IA». Aprobación informada; documentación y controles no revisados.
[^interno-politica-ia-2026]: Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)
[^interno-estandares-ingenieria-2026]: Estándares de ingeniería y contrato organizacional para agentes de código, 2026 (privado, anonimizado)
[^interno-okr-2026]: OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)
