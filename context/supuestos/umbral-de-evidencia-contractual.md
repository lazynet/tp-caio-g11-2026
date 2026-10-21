---
type: Supuesto
title: "Umbral de evidencia contractual para la licencia para vender"
description: "Criterios propuestos para distinguir restricciones, exigencias comerciales de controles y demanda de funciones de IA, sin autorizar inversión ni uso prohibido y con evidencia contractual real pendiente."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Martín confirmó los criterios como propuesta pendiente de ratificación y evidencia real: restricción en al menos uno de los cinco principales; exigencia de controles con consecuencia contractual en uno de los dos principales o dos de los cinco, dentro de 18 meses; y demanda de función como señal distinta. Incluye excluir el uso ante prohibición pura, separar señal de autorización de inversión o ampliación del mínimo, aclarar que licencia para vender no es licencia regulatoria ni venta, no inferir ingresos o repago, limitar concentración a agosto de 2026 y no presumir que todos los clientes sean bancos o PSP. Confirma actualizar BCRA al texto ordenado consultado y publicar solo agregados sin alias ni cláusulas. No acredita contratos revisados, señales observadas ni aprobación empresarial. Confirmado en esta conversación."
tags: [supuesto, compliance, clientes, gobierno]
sources:
  - id: bcra-tecnologia
    resource: https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rmgcti.pdf
    title: 'BCRA, texto ordenado de tecnología y seguridad al 13/02/2026, última comunicación incorporada "A" 8401, secciones 1.1, 4.6 y 10.3; consultado el 20/10/2026'
  - id: cartera
    resource: "context/hechos/cartera-y-concentracion.md"
    title: "Concentración de la cartera en agosto de 2026 y cautelas"
  - id: apetito
    resource: "context/supuestos/apetito-de-riesgo-de-clientes.md"
    title: "Apetito de riesgo y matriz de restricciones por cliente como supuestos"
  - id: gobierno
    resource: "plan/annexes/03-gobierno-seguridad.md"
    title: "Anexo C, señales y exclusión del uso ante prohibición pura"
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, decisiones separadas de inversión y paquete mínimo vigente"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Estos criterios son propuestas sin calibrar, pendientes de ratificación y de
reunir evidencia contractual real durante el primer trimestre. La expresión
"licencia para vender" es estratégica: no significa licencia regulatoria ni
venta confirmada. Verificar esta ficha no acredita que exista una señal.[^gobierno]

| Señal | Umbral |
|---|---|
| Restricción | Al menos un contrato de los cinco primeros clientes prohíbe o condiciona la IA de terceros |
| Licencia para vender | Uno de los dos primeros clientes, o dos de los cinco primeros, piden evidencia de controles de IA del proveedor como condición o puntaje de contratación o renovación dentro de 18 meses |
| Demanda | Un cliente pide una función de IA (es otra señal: pedir controles no es pedir IA) |

Las preguntas de un cuestionario sin consecuencia sobre la contratación no
cuentan. La consecuencia debe estar documentada. Se propone reunir evidencia
en contratos vigentes, cuestionarios de evaluación de proveedores, RFP,
pedidos de renovación e informes de auditoría; esta ficha no acredita que
esos documentos hayan sido inspeccionados.[^gobierno]

El registro documento por documento queda solo en `private/`. Fuera de ahí se
publica únicamente el agregado, sin alias ni cláusulas.[^gobierno]

Una prohibición pura se cumple excluyendo el uso afectado; contarla como
restricción no justifica comprar plataforma. Si hay condicionamiento o una
exigencia comercial, la señal permite evaluar una respuesta y presupuestarla,
sin autorizar automáticamente inversión ni ampliación del mínimo.[^gobierno][^finanzas]

Los 18 meses son el horizonte comercial propuesto para el criterio, no una
promesa de ingresos dentro de los doce meses del plan. Pedir controles no
equivale a pedir una función de IA; ninguna señal demuestra repago ni
probabilidad de perder clientes.[^gobierno][^finanzas]

# Por qué es razonable

- El texto ordenado del BCRA consultado incluye entidades financieras y PSP
  registrados. Su sección 4.6 contempla IA propia o de terceros y la 10.3
  establece requisitos de formalización de la tercerización. Ese marco no
  demuestra la exigencia de un cliente concreto: debe verificarse el sujeto,
  el servicio y su evidencia contractual.[^bcra-tecnologia]
- Los cinco primeros clientes concentran más del 90% de la facturación y los dos
  primeros cerca del 70% en agosto de 2026 (ver
  [cartera](/hechos/cartera-y-concentracion.md)). Eso prioriza la revisión de
  cartera, sin medir ingreso protegido ni riesgo de pérdida. No se presume
  que todos esos clientes sean bancos o PSP.[^cartera]
- El supuesto de partida sobre el [apetito de riesgo](/supuestos/apetito-de-riesgo-de-clientes.md)
  propone verificar la matriz por cliente. Los umbrales de esta ficha
  organizan la lectura de señales, sin financiar por sí solos una capa de
  demostración ni acreditar que la matriz esté completa.[^apetito][^gobierno]

# Qué lo invalidaría

- Que el board fije otro umbral (por ejemplo, un solo cliente cualquiera).
- Que la concentración cambie y los cinco primeros dejen de representar la
  mayor parte de la facturación.

# Cautelas

- Los umbrales (uno de dos, dos de cinco, 18 meses) son una propuesta de
  `governance`, sin calibrar; los decide el equipo con el board.
- Se reemplaza la referencia histórica aislada por el texto ordenado BCRA al
  13/02/2026, consultado el 20/10/2026, con secciones 1.1, 4.6 y 10.3.
  Corresponde revisar cambios posteriores antes de entregar.[^bcra-tecnologia]
- Ningún cliente ni cláusula real se describe acá: el resultado se registra como
  hecho anonimizado cuando exista y lo verifique una persona del equipo.
- Los umbrales no provienen de la norma ni acreditan consecuencias
  comerciales; su verificación humana no los convierte en hechos observados
  ni en una autorización empresarial.

[^bcra-tecnologia]: BCRA, texto ordenado al 13/02/2026, última comunicación incorporada "A" 8401, secciones 1.1, 4.6 y 10.3; consultado el 20/10/2026. Marco por sujeto y servicio, sin acreditar cláusulas de clientes concretos.
[^cartera]: Cartera y concentración, agosto de 2026: más de 90% en los cinco primeros y cerca del 70% en los dos primeros; fotografía de un mes, sin identificar segmentos de cada cliente.
[^apetito]: Apetito de riesgo de clientes, verificación propuesta de restricciones y matriz, sin presumir disponibilidad de evidencia contractual.
[^gobierno]: Anexo C, umbrales propuestos de señal, consecuencias documentadas, evidencia privada y exclusión del uso ante prohibición pura; no acredita señales observadas ni ratificación.
[^finanzas]: Anexo E, señal como entrada para evaluar una respuesta, con inversión y ampliación del mínimo sujetas a alcance, costeo y autorización propios, sin ingresos ni repago demostrados.
