---
type: Supuesto
title: "Umbral de evidencia contractual para la licencia para vender"
description: "Se propone que la licencia para vender IA a bancos cuente como señal solo si uno de los dos primeros clientes, o dos de los cinco primeros, piden evidencia de controles de IA como condición o puntaje de contratación o renovación dentro de 18 meses."
status: draft
tags: [supuesto, compliance, clientes, gobierno]
sources:
  - id: bcra-a7777
    resource: https://www.bcra.gob.ar/pdfs/comytexord/A7777.pdf
    title: 'BCRA, Comunicación "A" 7777 (01-06-2023), texto ordenado de "Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información", versión 1a'
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T03:00:00Z }
---
# Supuesto

La "licencia para vender" IA a bancos y fintechs se trata como señal, y no como
hipótesis, solo si la evidencia contractual del primer trimestre del plan cumple
alguno de estos umbrales, propuestos por el equipo:

| Señal | Umbral |
|---|---|
| Restricción | Al menos un contrato de los cinco primeros clientes prohíbe o condiciona la IA de terceros |
| Licencia para vender | Uno de los dos primeros clientes, o dos de los cinco primeros, piden evidencia de controles de IA del proveedor como condición o puntaje de contratación o renovación dentro de 18 meses |
| Demanda | Un cliente pide una función de IA (es otra señal: pedir controles no es pedir IA) |

Las preguntas de un cuestionario sin consecuencia sobre la contratación no
cuentan. La evidencia sale de contratos vigentes, cuestionarios de evaluación de
proveedores, RFP, pedidos de renovación e informes de auditoría de clientes; se
registra documento por documento solo en `private/` y fuera de ahí sale solo el
agregado, sin alias ni textos.

# Por qué es razonable

- La normativa obliga al banco a identificar y documentar el uso de IA propio o
  "por terceros"; no fija qué le exige al proveedor, así que la exigencia hay que
  buscarla en los contratos.[^bcra-a7777]
- Los cinco primeros clientes concentran más del 90% de la facturación y los dos
  primeros cerca del 70% (ver [cartera](/hechos/cartera-y-concentracion.md)): un
  umbral sobre ellos cubre casi todo el ingreso en juego.
- El supuesto de partida sobre el [apetito de riesgo](/supuestos/apetito-de-riesgo-de-clientes.md)
  dice cómo verificarse (la matriz por cliente); este umbral dice cuándo esa
  verificación alcanza para financiar la capa que demuestra controles.

# Qué lo invalidaría

- Que el board fije otro umbral (por ejemplo, un solo cliente cualquiera).
- Que la concentración cambie y los cinco primeros dejen de representar la
  mayor parte de la facturación.

# Cautelas

- Los umbrales (uno de dos, dos de cinco, 18 meses) son una propuesta de
  `governance`, sin calibrar; los decide el equipo con el board.
- Se leyó la sección 4.6 de la versión 1a de la norma; la versión vigente en
  2026 y la sección de terceras partes no se cotejaron.
- Ningún cliente ni cláusula real se describe acá: el resultado se registra como
  hecho anonimizado cuando exista y lo verifique una persona del equipo.

[^bcra-a7777]: BCRA, Comunicación "A" 7777, versión 1a (vigencia 06/09/2023), sección 4.6
