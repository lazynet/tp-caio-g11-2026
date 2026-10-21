---
type: Supuesto
title: "Precios de servicios externos sin cotización y contingencia"
description: "Rangos de diseño sin cotización para servicios externos, diferenciados entre el paquete mínimo y las alternativas de mayor alcance, con una reserva propuesta de 15% sobre la caja estimada cuya suficiencia debe comprobarse."
status: draft
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Rangos confirmados por Martín como supuestos de planificación para legal, red team, auditoría, pasarela, infraestructura, consumo del piloto y contingencia de 15%. Incluye distinguir el paquete mínimo de las alternativas de mayor alcance, retirar la atribución a precios de mercado, mantener pendientes de conciliación los alcances de ambos red teams y comprobar la suficiencia de la reserva. Los gastos sin estimar requieren presupuesto y autorización. Confirmado en esta conversación; no acredita cotizaciones, contratación ni aprobación empresarial."
tags: [supuesto, finanzas, seguridad, arquitectura]
sources:
  - id: arquitectura
    resource: "plan/annexes/02-arquitectura.md"
    title: "Anexo B, rangos de infraestructura, red team y consumo del piloto"
  - id: gobierno
    resource: "plan/annexes/03-gobierno-seguridad.md"
    title: "Anexo C, rangos de legal, pasarela, red team y auditoría"
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, contingencia y límites presupuestarios propuestos"
  - id: minimo
    resource: "context/supuestos/paquete-minimo-de-aprendizaje.md"
    title: "Paquete mínimo, legal focalizada y herramientas existentes"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Los siguientes rangos corresponden a alternativas de mayor alcance de los
anexos B y C; no son el presupuesto del paquete mínimo.[^arquitectura][^gobierno]

| Concepto | Rango supuesto (USD) | Lo usa |
|---|---|---|
| Asesoría legal externa (BCRA, Ley 25.326, cláusulas tipo) | 8.000-20.000 en total | Anexo C |
| Red team externo | Ver desacuerdo abajo | Anexos B y C |
| Auditoría propuesta para ampliar el alcance de ISO 27001 a IA | 800-1.500 por jornada, 2-4 jornadas: 1.600-6.000 en total | Anexo C |
| Pasarela de salida, DLP y logs de acciones | 500-2.000 por mes | Anexo C |
| Infraestructura nueva (gateway, retrieval, trazas, evals) | Meses 1-3, alternativa de solo telemetría y registro: 500-1.500 en el tramo de tres meses. Meses 1-3 con gateway en laboratorio: 500-1.500 por mes. Después, por mes: 1.500-4.000 en los meses 4-6; en los meses 7-12, 1.500-4.000 sin piloto y 2.000-6.000 con piloto (el incremento, 500-2.000 por mes, es del frente producto) | Anexo B |
| Consumo de modelos del piloto de producto | 1.000-4.000 por mes en los meses 7-12 | Anexo B |
| Contingencia sobre la caja | 15% | Anexo E |

El paquete mínimo contempla legal focalizada por 2.000-6.000 USD y herramientas
por 0-1.500 USD por trimestre, reutilizando las existentes, sin nueva pasarela
central. La legal focalizada sustituye la porción inicial de la revisión
completa; no se suma dos veces.[^minimo][^gobierno]

La contingencia de 15% es una reserva propuesta sobre la caja estimada para
absorber errores de precio; no garantiza que alcance.[^finanzas] Los renglones
que se nombran, pero no se estiman (certificación o curso externo del nivel
avanzado y certificaciones del programa de partners), no tienen cobertura
propia: requieren presupuesto, cotización y autorización antes de su gate.

Si se aprueba un techo de caja, esos gastos solo entran dentro de él, usando
contingencia no consumida o desplazando otro renglón con autorización. Si no
entran, no se hacen; el techo no aumenta automáticamente. La instrumentación
de la medición de uso se costea como tiempo en el anexo B.[^arquitectura]

# Desacuerdo a la vista: red team

| Mirada | Rango | Alcance |
|---|---|---|
| Arquitectura (anexo B) | 5.000-15.000 | Un ejercicio sobre el piloto, con un tercero chico |
| Gobierno (anexo C) | 10.000-25.000 | Red team externo de fin de año |

Cubren alcances distintos y ninguno tiene cotización. Ninguno entra en el
paquete mínimo. Si el Directorio libera el producto en el gate del mes 6, un
único contrato cubre piloto, reprueba y las superficies que pida el cliente: el
Responsable de seguridad define el alcance con el Responsable de Tecnología y el
CFO verifica la cotización antes de contratar; sin cotización verificada, el
piloto no sale a clientes. No se suman ni se sustituyen los dos renglones
(R-30)[^resoluciones].[^arquitectura][^gobierno]

# Por qué es razonable

Son estimaciones de diseño con revisión humana, para comparar alternativas.
La amplitud expresa incertidumbre por falta de cotizaciones; no acredita
precios de mercado ni acuerdo del equipo o aprobación empresarial.

# Qué lo invalidaría

- Cualquier cotización real que caiga fuera del rango.
- Que el error de precio o los renglones sin estimar superen la reserva no
  consumida: requiere rearmar el presupuesto y su autorización, sin gastar
  fuera del techo de caja que se apruebe.

# Cautelas

- Ningún valor tiene cotización. La verificación registra revisión humana del
  supuesto, sin autorizar la contratación ni confirmar suficiencia financiera.
- Los importes de las alternativas de los anexos B y C se conservan con sus
  alcances; sus etiquetas históricas de recomendado o conservador no definen
  el paquete mínimo actual.
- La auditoría es un costo propuesto; la ficha no acredita ampliación de
  alcance, resultado de auditoría ni nueva certificación.

[^arquitectura]: Anexo B, rangos propuestos de infraestructura, red team, consumo del piloto e instrumentación como tiempo.
[^gobierno]: Anexo C, rangos propuestos de servicios externos y sustitución de la porción inicial de legal por la revisión focalizada.
[^finanzas]: Anexo E, contingencia propuesta de 15% sobre caja y reglas de límites presupuestarios.
[^minimo]: Paquete mínimo de aprendizaje, legal focalizada por 2.000-6.000 USD y herramientas por 0-1.500 USD por trimestre, sin nueva plataforma central.
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
