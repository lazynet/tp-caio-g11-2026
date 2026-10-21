---
type: Supuesto
title: "Costo mensual cargado por rol"
description: "Para costear el plan se usan rangos supuestos de planificación de costo cargado mensual en dólares por rol, sujetos a contraste privado con los costos reales."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Rangos mensuales de planificación confirmados por Martín, en USD: semisenior 2.000-5.000; senior, QA automation o DevOps 3.000-7.500; tech lead o arquitecto 4.500-10.000; IA/ML aplicado 4.500-11.000; analista funcional o de negocio 2.000-5.500; staff 1.500-5.000. Incluye sueldo, cargas y beneficios o factura de contractor, contraste privado y revisión si costos reales quedan fuera de rango o si cambios cambiarios o inflación en dólares alteran costos más de 20% en los 12 meses. Se retiran las atribuciones no acreditadas de precios de mercado y facturación en dólares. Confirmado en esta conversación."
tags: [supuesto, finanzas, personas]
sources:
  - id: tamano-estructura
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Modelo mixto de nómina y contratistas y roles documentados"
generated: { by: codex/gpt-6, at: 2026-10-20 }
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

La empresa trabaja con un modelo mixto de nómina y contratistas (ver
[tamaño y estructura](/hechos/tamano-y-estructura.md)).[^tamano-estructura]
Los rangos se adoptan como supuestos amplios para presupuestar esa mezcla,
sujetos a contraste privado con los costos reales.

# Qué lo invalidaría

- Que la nómina real quede fuera de los rangos en los roles que el plan usa.
- Un salto cambiario o de inflación en dólares que mueva el costo local más de
  20% durante los 12 meses del plan.

# Cómo verificarlo

Quien tenga acceso a la nómina contrasta los rangos en `private/` y ajusta el
anexo financiero sin publicar el dato real.

# Cautelas

- Son rangos supuestos de planificación, sin fuente de mercado ni cotización
  que acredite precios vigentes.
- No están calibrados contra la nómina real y no deben usarse para
  reconstruirla a partir de la dotación.
- El umbral de variación del 20% es un disparador propuesto de revisión.

[^tamano-estructura]: Tamaño y estructura de la organización, modelo mixto de nómina y contratistas y roles al corte de septiembre de 2026.
