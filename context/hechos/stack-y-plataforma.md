---
type: Hecho
title: "Stack y plataforma de delivery"
description: "Acme Labs desarrolla sobre Node/TypeScript, Java y Python, despliega en AWS con Kubernetes y GitOps, y gestiona el trabajo en GitHub y en la suite de Atlassian."
status: draft
tags: [caso, arquitectura, plataforma]
sources:
  - id: interno-estandares-ingenieria-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Estándares de ingeniería y contrato organizacional para agentes de código, 2026 (privado, anonimizado)"
  - id: interno-okr-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)"
  - id: interno-propuestas-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Diseño del sistema de propuestas comerciales, septiembre de 2026 (privado, anonimizado)"
  - id: interno-costos-tech-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Reportes mensuales de costos de tecnología, febrero a septiembre de 2026 (privado, anonimizado)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Lenguajes y prácticas

- Lenguajes principales: Node (JavaScript y TypeScript), Java, Python y Bash;
  .NET solo en proyectos legados o por pedido del cliente.
- Desarrollo *trunk-based*, commits chicos, CI corporativa obligatoria y code
  review estándar también para código generado con IA.[^interno-estandares-ingenieria-2026]

# Plataforma

| Capa | Herramientas |
|---|---|
| Nube | AWS, organizado en varias cuentas (compartidas, red, seguridad, laboratorio y una por proyecto) |
| Ejecución y despliegue | Kubernetes administrado, despliegue GitOps, contenedores en un registro privado |
| Observabilidad y soporte | Grafana y una mesa de servicio con alertas y ruteo por niveles |
| Código y calidad | GitHub, análisis estático y auditoría periódica de vulnerabilidades de código e imágenes |
| Gestión y colaboración | Jira, Confluence, Slack y Google Workspace |

[^interno-okr-2026] [^interno-estandares-ingenieria-2026] [^interno-costos-tech-2026]

# Estado de la base técnica

- El producto del Cliente A es un producto maduro, en producción y con
  compromisos de disponibilidad.[^interno-propuestas-2026]
- Formalizar dueño y runbook de cada workload productivo es una meta técnica
  de 2027.[^interno-okr-2026]
- La nube concentra cerca del 80% del gasto de tecnología (ver
  [costos de tecnología e IA](/hechos/costos-tecnologia-e-ia.md)).

# Cautelas

- Los equipos asignados a clientes (staffing) trabajan con el stack y las
  herramientas de cada cliente, no con las de Acme Labs.
- La lista de herramientas surge de documentos internos; no hay un inventario
  formal de arquitectura.

[^interno-estandares-ingenieria-2026]: Estándares de ingeniería y contrato organizacional para agentes de código, 2026 (privado, anonimizado)
[^interno-okr-2026]: OKR organizacionales 2026 y borrador de OKR de Tecnología 2027 (privado, anonimizado)
[^interno-propuestas-2026]: Diseño del sistema de propuestas comerciales, septiembre de 2026 (privado, anonimizado)
[^interno-costos-tech-2026]: Reportes mensuales de costos de tecnología, febrero a septiembre de 2026 (privado, anonimizado)
