---
type: Supuesto
title: "Costo mensual cargado por rol"
description: "Para costear el plan se usan rangos de mercado argentinos de costo cargado mensual en dólares por rol, no la nómina real de Acme Labs."
status: draft
tags: [supuesto, finanzas, personas]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Supuesto

Costo mensual cargado (sueldo, cargas y beneficios, o factura de contractor),
en USD, para perfiles con base en Argentina:

| Rol | Rango supuesto |
|---|---|
| Desarrollador semisenior | 2.000 - 5.000 |
| Desarrollador senior, QA automation o DevOps | 3.000 - 7.500 |
| Tech lead o arquitecto | 4.500 - 10.000 |
| Especialista en IA o ML aplicado | 4.500 - 11.000 |
| Analista funcional o de negocio | 2.000 - 5.500 |
| Rol de staff (finanzas, talento, comercial) | 1.500 - 5.000 |

# Por qué es razonable

La empresa trabaja con personal mixto (nómina y contractors) y factura servicios
en dólares a clientes de la región (ver [tamaño y estructura](/hechos/tamano-y-estructura.md)).
Los rangos son amplios a propósito: cubren esa mezcla y no están calibrados
contra la nómina real, para que el producto dotación × costo no permita
reconstruirla.

# Qué lo invalidaría

- Que la nómina real quede fuera de los rangos en los roles que el plan usa.
- Un salto cambiario o de inflación en dólares que mueva el costo local más de
  20% durante los 12 meses del plan.

# Cómo verificarlo

Quien tenga acceso a la nómina contrasta los rangos en `private/` y ajusta el
anexo financiero sin publicar el dato real.
