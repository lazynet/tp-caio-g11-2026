---
type: Hecho
title: "Regulación argentina que pesa sobre los clientes financieros"
description: "Los bancos y proveedores de servicios de pago clientes de Acme Labs están obligados por el BCRA a gobernar el uso de IA propio y de terceros, y por ley a guardar secreto financiero y proteger datos personales."
status: draft
tags: [caso, compliance, regulacion, bcra]
sources:
  - id: bcra-a7777
    resource: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7777.pdf
    title: 'BCRA, Comunicación "A" 7777 (01-06-2023), texto ordenado de "Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información"'
  - id: bcra-a7783
    resource: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7783.pdf
    title: 'BCRA, Comunicación "A" 7783 (02-06-2023), requisitos para servicios financieros digitales'
  - id: bcra-a6885
    resource: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf
    title: 'BCRA, Comunicación "A" 6885 (30-01-2020), proveedores de servicios de pago que ofrecen cuentas de pago'
  - id: ley-21526
    resource: https://www.argentina.gob.ar/normativa/nacional/ley-21526-16071/texto
    title: "Ley 21.526 de Entidades Financieras, arts. 39 y 40"
  - id: ley-25326
    resource: https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto
    title: "Ley 25.326 de Protección de los Datos Personales (2000)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Gestión de riesgos de tecnología e IA (BCRA)

El texto ordenado de requisitos mínimos de tecnología y seguridad de la
información, que reúne lo dispuesto por la Comunicación "A" 7724, dedica una
sección a inteligencia artificial y aprendizaje automático. Las entidades
financieras tienen que:[^bcra-a7777]

- identificar y documentar el objetivo del uso de software con IA, **propio o de
  terceros**;
- asignar roles para definir el contexto, los modelos, los datos y métricas y
  umbrales de confiabilidad;
- analizar riesgos de modelos, datos de entrenamiento, privacidad y madurez de
  las pruebas;
- evitar sesgos, documentar transparencia y explicabilidad, revisar resultados
  contra la tolerancia al riesgo y **avisar al cliente** cuando un servicio usa IA.

El mismo texto pide que el gobierno de la entidad asegure evaluaciones de impacto
y defina el apetito de riesgo para el uso de IA, e incluye la relación con
terceras partes y la adopción de tecnología emergente entre los riesgos a
gestionar.[^bcra-a7777]

La Comunicación "A" 7783 extiende requisitos equivalentes a los servicios
financieros digitales y alcanza también a los proveedores de servicios de pago
(PSP); define explicabilidad y aprendizaje automático.[^bcra-a7783] Los PSP que
ofrecen cuentas de pago tienen además su propio régimen y registro ante el
BCRA.[^bcra-a6885]

# Secreto financiero

Las entidades financieras no pueden revelar las operaciones que realizan ni la
información que reciben de sus clientes, salvo excepciones taxativas (jueces,
BCRA, organismos recaudadores), y su personal debe guardar absoluta
reserva.[^ley-21526]

# Datos personales

La Ley 25.326 define los datos sensibles (entre ellos, los de salud), establece
que nadie puede ser obligado a proporcionarlos y prohíbe transferir datos
personales a países u organismos que no den niveles de protección
adecuados.[^ley-25326] Esto condiciona el envío de datos a modelos alojados en
el exterior.

# Qué implica para Acme Labs

Acme Labs no es una entidad financiera, pero es **tercero** de bancos y PSP:
lo que construya u opere con IA para ellos entra en el análisis de riesgos de
terceros del cliente, y su producto propio de medios de pago quedaría alcanzado
de forma directa si obtiene la habilitación.

# Cautelas

- El texto ordenado tuvo versiones posteriores (la sección de tecnología
  figura actualizada en 2026); antes de citarlo en una slide, verificar la
  versión vigente en bcra.gob.ar.
- Las citas son resúmenes de la fuente primaria, no transcripciones completas.
- A 6885: verificada solo por encabezado y alcance; leer el texto ordenado
  vigente antes de citar detalles.
- No se verificó la normativa UIF ni las comunicaciones específicas que los
  documentos internos asocian al producto de medios de pago.

[^bcra-a7777]: BCRA, Comunicación "A" 7777 (01-06-2023), secciones 2, 3 y 4.6
[^bcra-a7783]: BCRA, Comunicación "A" 7783 (02-06-2023), destinatarios y glosario
[^bcra-a6885]: BCRA, Comunicación "A" 6885 (30-01-2020), alcance
[^ley-21526]: Ley 21.526, arts. 39 y 40
[^ley-25326]: Ley 25.326, arts. 2, 7 y 12
