---
type: Supuesto
title: "Desarrolladores en equipos propios y su costo"
description: "El caso de negocio supone entre 15 y 20 desarrolladores en equipos propios (valor de cálculo 17,5) con un costo cargado de USD 2.500-7.000 por mes (valor de cálculo 4.750)."
status: draft
tags: [supuesto, finanzas, productividad]
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-14T20:00:00Z }
---
# Supuesto

| Insumo | Rango | Valor de cálculo |
|---|---|---|
| Desarrolladores en equipos propios (N) | 15-20 personas | 17,5 |
| Costo cargado por desarrollador | USD 2.500-7.000 por mes | 4.750 |
| Mínimo de personas activas para decidir un gate por valor (propuesta) | — | 15 |

Equipos propios son los que trabajan en modo producto, donde la organización
controla las herramientas; el staffing no se cuenta, porque el uso de IA ahí
depende de cada cliente (ver [ganancia de productividad](/supuestos/ganancia-de-productividad.md)).

El mínimo de 15 reemplaza el "~20" del método de los gates: con una cohorte de
15-20, un mínimo de 20 dejaría el gate en "muestra insuficiente" casi siempre.
Es el piso de la cohorte, necesario pero no suficiente: decide el semiancho.

# Por qué es razonable

- Tecnología es cerca del 40% de una dotación de 60-70 personas (ver
  [tamaño y estructura](/hechos/tamano-y-estructura.md)); N descuenta
  plataforma, seguridad y soporte.
- El costo se ubica entre semisenior y senior del
  [costo por rol](/supuestos/costo-cargado-por-rol.md).

# Qué lo invalidaría

- Un inventario por equipo que dé menos de 15 desarrolladores en equipos propios.
- Una mezcla de seniority muy distinta de la supuesta.
- Que la serie de la preparación previa muestre que con 15 personas el semiancho supera 3 puntos:
  entonces el mínimo no alcanza y el gate se reformula antes de la aprobación de hoy.

# Cautelas

- No está calibrado contra la nómina: N × costo **no** es la nómina de
  Tecnología ni debe usarse como tal.
- Es el valor vigente en el anexo E
  al 2026-10-14; si su dueño lo cambia, se actualiza esta ficha primero.
