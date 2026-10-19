---
type: Hecho
title: "Gobierno y política de IA existentes"
description: "Acme Labs tiene una política de uso aceptable de IA con clasificación de datos y matriz de herramientas, pero sigue en borrador y con pendientes clave, como la matriz de restricciones de clientes."
status: draft
tags: [caso, gobierno, ia, politicas]
sources:
  - id: interno-politica-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)"
  - id: interno-estandares-ingenieria-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Estándares de ingeniería y contrato organizacional para agentes de código, 2026 (privado, anonimizado)"
  - id: interno-okr-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Política de uso aceptable de IA

Versión 1.0 en borrador desde abril de 2026, con dueño y sponsor designados
dentro de Tecnología.[^interno-politica-ia-2026]

**Principios:** usar solo herramientas corporativas; desconfiar del output hasta
revisarlo; el humano es el responsable final; lo que no se mide no se justifica.

**Clasificación de datos en cuatro niveles:**

| Nivel | Ejemplos | ¿Se puede usar con IA externa? |
|---|---|---|
| Público | Sitio web, casos publicados | Sí |
| Interno | Organigrama, procesos | Sí, con herramientas aprobadas |
| Confidencial | Código propio, propuestas, reportes financieros operativos | Solo con SSO corporativo y contrato sin entrenamiento sobre los datos |
| Restringido | Datos personales de clientes, credenciales, código bajo NDA, contratos, resultados no divulgados | Nunca |

**Controles definidos:** lista cerrada de lo que nunca se envía (incluye datos de
salud y categorías especiales de la Ley 25.326); validación comercial antes de
usar IA sobre código de un cliente; reglas propias para el producto que maneja
datos de categoría especial; revisión del output según su destino (code review,
responsable del área, dueño del dominio financiero o legal); aprobación de herramientas nuevas
por el comité de tecnología en 2 a 4 semanas; reporte de incidentes en el día,
sin sanción por reportar.[^interno-politica-ia-2026]

**Roles:** dueño de la política, sponsor, administrador técnico de licencias,
comité de tecnología como aprobador y auditoría mensual de uso.[^interno-politica-ia-2026]

# Pendientes declarados por la propia política

- Ratificación del Directorio y firma del dueño.
- Matriz de clientes con restricciones contractuales sobre modelos externos;
  hasta tenerla, cada caso se valida a mano con el área comercial.
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

- El estado de los pendientes es al 2026-04-21; no hay registro posterior de la
  ratificación.
- No hay inventario formal de casos de uso de IA ni registro de riesgos de IA.

[^interno-politica-ia-2026]: Política de uso aceptable de IA, versión 1.0 en borrador, abril de 2026 (privado, anonimizado)
[^interno-estandares-ingenieria-2026]: Estándares de ingeniería y contrato organizacional para agentes de código, 2026 (privado, anonimizado)
[^interno-okr-2026]: OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)
