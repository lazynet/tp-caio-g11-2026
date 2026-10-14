---
type: Supuesto
title: "Precios de servicios externos sin cotización y contingencia"
description: "Los costos externos del plan (asesoría legal, red team, auditoría, pasarela, infraestructura y consumo del piloto) son rangos del equipo sin cotización, y una contingencia de 15% sobre la caja cubre el error de precio de lo estimado, dentro del techo aprobado."
status: draft
tags: [supuesto, finanzas, seguridad, arquitectura]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T03:18:00Z }
---
# Supuesto

| Concepto | Rango supuesto (USD) | Lo usa |
|---|---|---|
| Asesoría legal externa (BCRA, Ley 25.326, cláusulas tipo) | 8.000-20.000 en total | Anexo C |
| Red team externo | Ver desacuerdo abajo | Anexos B y C |
| Auditoría para extender ISO 27001 a IA | 800-1.500 por jornada, 2-4 jornadas | Anexo C |
| Pasarela de salida, DLP y logs de acciones | 500-2.000 por mes | Anexo C |
| Infraestructura nueva (gateway, retrieval, trazas, evals) | T1 acotado (T1-b, solo telemetría y registro): 500-1.500 en el trimestre. T1 con gateway en laboratorio (T1-a): 500-1.500 por mes. Después, por mes: 1.500-4.000 en T2; en T3 y T4, 1.500-4.000 sin piloto y 2.000-6.000 con piloto (el incremento, 500-2.000 por mes, es del frente producto) | Anexo B |
| Consumo de modelos del piloto de producto | 1.000-4.000 por mes en T3 y T4 | Anexo B |
| Contingencia sobre la caja | 15% | Anexo E |

La contingencia cubre el error de precio de los renglones estimados. Los
renglones que se nombran pero no se estiman (certificación o curso externo del
nivel avanzado y certificaciones del programa de partners) no tienen cobertura
propia: entran solo con una cotización antes de su gate y dentro del techo
aprobado, usando contingencia no consumida o desplazando otro renglón. Si no
entran, no se hacen; el techo no se mueve. La instrumentación de la medición de
uso ya no está entre ellos: el anexo B la costea como tiempo.

# Desacuerdo a la vista: red team

| Mirada | Rango | Alcance |
|---|---|---|
| Arquitectura (anexo B) | 5.000-15.000 | Un ejercicio sobre el piloto, con un tercero chico |
| Gobierno (anexo C) | 10.000-25.000 | Red team externo de fin de año |

No se elige uno acá: cubren alcances distintos y ninguno tiene cotización.
Lo resuelven `architect` y `governance` con `finance`.

# Por qué es razonable

Son órdenes de magnitud de mercado para una empresa de este tamaño con
infraestructura en AWS (ver [stack](/hechos/stack-y-plataforma.md)); la amplitud
de los rangos refleja que no hay cotización.

# Qué lo invalidaría

- Cualquier cotización real que caiga fuera del rango.
- Que los renglones sin estimar superen la contingencia: la regla del plan es no
  gastar fuera del techo de caja aprobado.

# Cautelas

- Ningún valor tiene cotización: no sirven para una slide de entrega hasta
  reemplazarlos por cotizaciones o marcarlos como supuesto revisado.
- Valores vigentes en los anexos B, C y E al 2026-10-14. El plan recomendado usa
  T1-b; el valor por mes de T1 corresponde a T1-a.
