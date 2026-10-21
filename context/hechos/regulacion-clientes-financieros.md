---
type: Hecho
title: "Regulación argentina que pesa sobre los clientes financieros"
description: "El BCRA exige gobierno de tecnología e IA a entidades financieras y PSP registrados; el secreto financiero y la protección de datos condicionan los servicios de Acme Labs según el sujeto y la actividad."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Versión corregida de la ficha completa cotejada con los textos ordenados oficiales del BCRA de tecnología al 13/02/2026 y PSP al 02/10/2026, las leyes 21.526 y 25.326 actualizadas y la información de la AAIP sobre transferencias internacionales, consultados el 20/10/2026. Incluye alcance por sujeto y actividad, IA y terceros, registro PSP, operaciones pasivas y reserva, y excepciones y mecanismos de transferencia. Se conserva sin verificar la normativa UIF y los requisitos específicos de habilitación del producto de pagos. Confirmado por Martín en esta conversación."
tags: [caso, compliance, regulacion, bcra]
sources:
  - id: bcra-tecnologia
    resource: https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rmgcti.pdf
    title: 'BCRA, requisitos mínimos de tecnología y seguridad, texto ordenado al 13/02/2026, última comunicación incorporada "A" 8401; consultado el 20/10/2026'
  - id: bcra-psp
    resource: https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-psp.pdf
    title: 'BCRA, proveedores de servicios de pago, texto ordenado al 02/10/2026, última comunicación incorporada "A" 8488; consultado el 20/10/2026'
  - id: ley-21526
    resource: https://www.argentina.gob.ar/normativa/nacional/ley-21526-16071/actualizacion
    title: "Ley 21.526 de Entidades Financieras, texto actualizado, arts. 39 y 40; consultado el 20/10/2026"
  - id: ley-25326
    resource: https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/actualizacion
    title: "Ley 25.326 de Protección de los Datos Personales, texto actualizado, arts. 2, 7 y 12; consultado el 20/10/2026"
  - id: aaip-transferencias
    resource: https://www.argentina.gob.ar/transferencias-internacionales
    title: "AAIP, transferencias internacionales y mecanismos de protección; consultado el 20/10/2026"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Gestión de riesgos de tecnología e IA (BCRA)

El texto ordenado consultado el 20/10/2026 está actualizado al 13/02/2026
(Comunicación "A" 8401). Su alcance incluye entidades financieras y PSP
registrados en el BCRA; la sección 4.6 exige:[^bcra-tecnologia]

- documentar objetivos de uso de IA propia o de terceros;
- definir responsables, modelos, datos, métricas y umbrales;
- evaluar riesgos de modelos, entrenamiento, privacidad y pruebas;
- prevenir sesgos, documentar explicabilidad, revisar resultados e informar
  al cliente cuando use servicios soportados por IA.

La gestión de riesgos de IA se integra al gobierno de tecnología de la entidad.
La sección 10 exige evaluar y formalizar la relación con terceros, conservando
la responsabilidad de la entidad que terceriza.[^bcra-tecnologia]

El régimen de PSP consultado está actualizado al 02/10/2026 (Comunicación
"A" 8488). La sección 2 exige inscripción según la función desempeñada;
incluye a quienes ofrecen cuentas de pago.[^bcra-psp]

# Secreto financiero

El art. 39 de la Ley 21.526 actualizado protege las **operaciones pasivas** de
las entidades alcanzadas, con las excepciones legales. También impone reserva
a su personal; el art. 40 regula la información que recibe el BCRA.[^ley-21526]

# Datos personales

La Ley 25.326 define datos sensibles, incluidos los de salud, y restricciones
para su obtención y tratamiento. El art. 12 restringe las transferencias
internacionales sin protección adecuada y contempla excepciones.[^ley-25326]

La AAIP describe mecanismos para transferir a destinos sin legislación
adecuada, incluidas cláusulas contractuales modelo y normas corporativas
vinculantes. El envío a un modelo externo exige evaluar destino, datos y
mecanismo aplicable.[^aaip-transferencias]

# Qué implica para Acme Labs

En el escenario del plan, Acme Labs actúa como proveedor tecnológico de bancos
y PSP: sus servicios de IA deben contemplarse en la evaluación y las condiciones
de tercerización del cliente.[^bcra-tecnologia]

Para el producto propio de pagos, el alcance directo depende de la entidad
operadora y de su función y registro como PSP. No se atribuye una obligación
directa a la empresa solo por desarrollar el software.[^bcra-psp][^bcra-tecnologia]

# Cautelas

- Se identifican los textos ordenados disponibles en el sitio oficial al
  20/10/2026; corresponde revisar cambios posteriores antes de la entrega.
- Las citas son resúmenes de la fuente primaria, no transcripciones completas.
- Se reemplazan las comunicaciones históricas aisladas por los textos
  ordenados consultados para tecnología y PSP.
- El alcance del secreto financiero, la protección de datos y las obligaciones
  BCRA se distingue según sujeto y actividad; no se equipara un PSP a un banco.
- No se verificó la normativa UIF ni las comunicaciones específicas que los
  documentos internos asocian al producto de medios de pago.

[^bcra-tecnologia]: BCRA, texto ordenado al 13/02/2026, secciones 1.1, 4.6 y 10; consultado el 20/10/2026.
[^bcra-psp]: BCRA, texto ordenado al 02/10/2026, secciones 1 y 2; consultado el 20/10/2026.
[^ley-21526]: Ley 21.526, texto actualizado, arts. 39 y 40; consultado el 20/10/2026.
[^ley-25326]: Ley 25.326, texto actualizado, arts. 2, 7 y 12; consultado el 20/10/2026.
[^aaip-transferencias]: AAIP, transferencias internacionales: excepciones y mecanismos de protección, incluidas cláusulas contractuales modelo y normas corporativas vinculantes; consultado el 20/10/2026.
