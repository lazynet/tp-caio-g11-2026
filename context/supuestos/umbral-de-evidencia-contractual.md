---
type: Supuesto
title: "Umbral de evidencia contractual para la licencia para vender"
description: "Umbrales sin calibrar para distinguir restricciones, exigencias comerciales de controles y demanda de funciones de IA, usados por la regla de plataforma que ratifica el Directorio, sin autorizar inversión ni uso prohibido."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-21
  scope: "Revalidación registrada por instrucción expresa de Martín en la sesión del 21/10/2026 sobre el contenido vigente del PR #52. Regla de plataforma de R-15: señal contractual y cuatro condiciones, ratificadas por el Directorio al aprobar el plan. Se conserva como diseño sin calibrar la restricción en uno de cinco clientes principales y la exigencia de controles en uno de dos o dos de cinco dentro de 18 meses, separadas de demanda de funciones. El Directorio libera fondos y recalibra a propuesta del AI Council; una prohibición contractual no habilita el uso. Se mantiene como Supuesto de diseño: esta declaración no acredita mediciones, contratos, disponibilidad ni ejecución de decisiones futuras."
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
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, R-15: plataforma con señal más cuatro condiciones, ratificada por el Directorio"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21 }
---
# Supuesto

Estos umbrales son supuestos sin calibrar. El Directorio, al aprobar el plan,
ratifica la regla de gate que los usa: liberar plataforma en el mes 3, 6 o 9
exige una señal más cuatro condiciones, y la prohibición pura excluye el uso sin
liberar plataforma (R-15 del Anexo G).
La ratificación es del criterio, no de que exista una señal.[^resoluciones]

Alcance y hito: la evidencia contractual se reúne en M1-M3 y se lee en la
decisión del mes 3, con relectura en los meses 6 y 9. Autoridad: el AI Council
declara la señal; el Directorio libera los fondos de plataforma y es quien
recalibra los umbrales, en un gate, a propuesta del AI Council. Consecuencia: si
no se alcanza un umbral o falta una condición, no se libera plataforma y sigue el
mínimo costeado.[^resoluciones] La expresión "licencia para vender" es
estratégica: no significa licencia regulatoria ni venta confirmada.[^gobierno]

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

- Que el Directorio recalibre el umbral en un gate (por ejemplo, a un solo cliente cualquiera).
- Que la concentración cambie y los cinco primeros dejen de representar la
  mayor parte de la facturación.

# Cautelas

- Los umbrales (uno de dos, dos de cinco, 18 meses) siguen sin calibrar; la
  regla que los usa la ratifica el Directorio y recalibrarlos es decisión suya
  en un gate, a propuesta del AI Council.[^resoluciones]
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
[^resoluciones]: Anexo G, R-15: regla de plataforma con señal y cuatro condiciones, ratificada por el Directorio al aprobar el plan; el Directorio libera fondos y recalibra umbrales a propuesta del AI Council.
[^finanzas]: Anexo E, señal como entrada para evaluar una respuesta, con inversión y ampliación del mínimo sujetas a alcance, costeo y autorización propios, sin ingresos ni repago demostrados.
