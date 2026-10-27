---
type: Supuesto
title: "Desarrolladores en equipos propios y su costo"
description: "El caso de negocio supone entre 15 y 20 desarrolladores en equipos propios (valor de cálculo 17,5) con un costo cargado de USD 2.500-7.000 por mes (valor de cálculo 4.750)."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-21
  scope: "Revalidación registrada por instrucción expresa de Martín en la sesión del 21/10/2026 sobre el contenido vigente del PR #52. Cohorte supuesta de 15-20 personas, punto medio 17,5 y costo cargado mensual de USD 2.500-7.000, punto medio 4.750. Se adopta el protocolo agregado por área del Anexo B. Se mantiene el piso propuesto de 15 personas de la cohorte; ese N no garantiza precisión ni paso del gate, y se retira el semiancho fijo de 3 puntos como criterio de precisión. R-14 exige ratificación del método y cohorte por el AI Council antes de la segunda liberación. Se mantiene como Supuesto de diseño: esta declaración no acredita mediciones, contratos, disponibilidad ni ejecución de decisiones futuras."
tags: [supuesto, finanzas, productividad]
sources:
  - id: tamano-estructura
    resource: "context/hechos/tamano-y-estructura.md"
    title: "Dotación y peso de Tecnología, con límites del dimensionamiento"
  - id: ganancia-productividad
    resource: "context/supuestos/ganancia-de-productividad.md"
    title: "Alcance propuesto de productividad en equipos propios"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Rangos supuestos de costo cargado por rol"
  - id: umbrales-tecnicos
    resource: "context/supuestos/umbrales-tecnicos-propuestos.md"
    title: "Muestra y precisión propuestas para los gates de impacto"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, R-14 (método de medición) y R-06 (quién produce, verifica y firma)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21 }
---
# Supuesto

| Insumo | Rango | Valor de cálculo |
|---|---|---|
| Desarrolladores en equipos propios (N) | 15-20 personas | 17,5 |
| Costo cargado por desarrollador | USD 2.500-7.000 por mes | 4.750 |
| Mínimo de personas activas para decidir un gate por valor (propuesta) | — | 15 |

Equipos propios son los que trabajan en modo producto, donde la organización
controla las herramientas; el staffing no se cuenta, porque el uso de IA ahí
depende de cada cliente (ver [ganancia de productividad](/supuestos/ganancia-de-productividad.md)).[^ganancia-productividad]

El mínimo propuesto de 15 es el piso de la cohorte para que una lectura decida
por valor. No garantiza precisión: con 15-20 personas, la lectura del mes 9 solo
distingue de cero, con buena probabilidad, una mejora cercana al techo del rango
de la ganancia supuesta; la cuenta de potencia y el gate de valor están en la
ficha de umbrales técnicos.[^umbrales-tecnicos] La cohorte la identifica el Responsable de Tecnología en el acta de la validación
inicial; el CFO verifica el costo, y la precisión y el método los ratifica el AI
Council antes de la segunda liberación (R-14). Sin ratificación no se libera
M1-M3.[^resoluciones]

# Por qué es razonable

- Tecnología es cerca del 40% de una dotación de 60-70 personas (ver
  [tamaño y estructura](/hechos/tamano-y-estructura.md)).[^tamano-estructura]
  Esos agregados no determinan N: el rango de 15-20 es una hipótesis que requiere
  identificar la cohorte y distinguir plataforma, seguridad y soporte.
- El costo se ubica entre semisenior y senior del
  [costo por rol](/supuestos/costo-cargado-por-rol.md), como rango de diseño.[^costo-rol]

# Qué lo invalidaría

- Un inventario por equipo que dé menos de 15 desarrolladores en equipos propios.
- Una mezcla de seniority muy distinta de la supuesta.
- Que la serie de la preparación previa muestre que, con la cohorte real, ni con
  base de 8 semanas la lectura del mes 9 distingue el techo del rango: el AI
  Council ratifica antes de la segunda liberación, previa a M1, que ninguna lectura
  decida por valor (R-14).[^resoluciones]

# Cautelas

- No está calibrado contra la nómina: N × costo **no** es la nómina de
  Tecnología ni debe usarse como tal.
- Los cambios de cohorte, costo o precisión requieren actualizar esta ficha y
  recalcular el caso de negocio correspondiente.

[^tamano-estructura]: Tamaño y estructura de la organización, dotación y peso aproximado de Tecnología al corte de septiembre de 2026.
[^ganancia-productividad]: Ganancia de productividad con agentes de código, alcance en equipos propios y exclusión de staffing.
[^costo-rol]: Costo mensual cargado por rol, rangos supuestos sin calibración contra nómina.
[^resoluciones]: Anexo G, R-14 (el AI Council ratifica estimador, muestra mínima, cohorte elegible y reformulación antes de la segunda liberación) y R-06 (el CFO responde por cada cifra del business case).
[^umbrales-tecnicos]: Umbrales técnicos propuestos, muestra mínima de 15 personas activas, cuenta de potencia y gate de valor, sujetos a validación previa.
