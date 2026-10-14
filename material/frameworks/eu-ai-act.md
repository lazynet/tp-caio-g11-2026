---
type: Framework
title: EU AI Act
description: Reglamento (UE) 2024/1689 con sus niveles de riesgo, calendario vigente tras el Digital Omnibus (Reg. UE 2026/1744), roles de proveedor y desplegador y sanciones.
tags: [compliance, regulacion, eu-ai-act]
resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
sources:
  - id: eu-ai-act
    resource: EU AI Act 2024.pdf
    title: Reg. (UE) 2024/1689, copia en la carpeta Frameworks Generales (144 p., texto en español del DOUE)
  - id: eu-ai-act-eurlex
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    title: Reg. (UE) 2024/1689 en EUR-Lex (fuente primaria)
  - id: ai-omnibus
    resource: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
    title: Reg. (UE) 2026/1744, Digital Omnibus on AI, DOUE L de 24.7.2026
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

# Qué es

Reglamento de la UE que regula la IA por niveles de riesgo. Se firmó el 13 de
junio de 2024, se publicó el 12 de julio de 2024 y entró en vigor el 1 de agosto
de 2024. Tiene 113 artículos y 13 anexos.[^eu-ai-act][^eu-ai-act-eurlex]

Aplica fuera de la UE cuando el resultado del sistema se usa en la UE (art. 2.1.c),
así que alcanza a un proveedor argentino con clientes que operan en Europa.[^eu-ai-act]

# Mapa del framework

| Tema | Concepto |
|---|---|
| Prácticas prohibidas (art. 5), clasificación (art. 6), transparencia (art. 50), modelos de uso general (cap. V) | [Niveles de riesgo](/frameworks/eu-ai-act-niveles-riesgo.md) |
| Casos de uso de alto riesgo, con scoring crediticio (5.b) y seguros (5.c), y la FRIA (art. 27) | [Anexo III](/frameworks/eu-ai-act-anexo-iii.md) |
| Requisitos arts. 8-15, obligaciones del proveedor y del desplegador, cadena de valor (art. 25), alfabetización (art. 4), incidentes (art. 73) | [Proveedor y desplegador](/frameworks/eu-ai-act-proveedor-desplegador.md) |
| Fechas del art. 113 con el Omnibus y multas del art. 99 | [Calendario y sanciones](/frameworks/eu-ai-act-calendario-sanciones.md) |

# Lo esencial para el plan

- **Para el board:** el paquete completo de alto riesgo para scoring y seguros
  aplica desde el **2 de diciembre de 2027** (antes 2 de agosto de 2026), por
  el Omnibus. Ya rigen hoy la alfabetización, las prohibiciones, las
  obligaciones de GPAI, las sanciones y la transparencia del art. 50.[^ai-omnibus]
- **Rol:** Acme Labs es proveedor en su software (art. 16) y desplegador en
  lo que opera para sí mismo (art. 26). Pasa a ser proveedor si pone su marca a
  un sistema de terceros, lo modifica sustancialmente o cambia su finalidad
  (art. 25).[^eu-ai-act]
- **Cliente bancario:** un banco que usa scoring o pricing de seguros de vida y
  salud es desplegador de alto riesgo y debe hacer una FRIA (art. 27); necesita
  del proveedor las instrucciones de uso del art. 13.[^eu-ai-act]
- **Multas:** hasta 35 M EUR o 7 % por prácticas prohibidas, 15 M o 3 % por
  obligaciones de proveedor, desplegador y transparencia; para PyMEs rige el
  menor de los dos valores.[^eu-ai-act]

# Cautelas

- **Resuelta:** el AI Omnibus que cita [M1U4](/unidades/m1u4-rol-gobernanza.md)
  existe y es el Reg. (UE) 2026/1744 (8 de julio de 2026, DOUE L de 24.7.2026,
  en vigor desde el 27 de julio de 2026). Detalle en el
  [calendario](/frameworks/eu-ai-act-calendario-sanciones.md).[^ai-omnibus]
- **Abierta:** qué fecha rige para la evaluación de conformidad y el registro
  (arts. 43 y 49) tras el Omnibus. Ver el calendario.
- **Abierta:** aplicabilidad concreta a los clientes de Acme Labs (art. 2.1.c)
  y su tamaño como PyME, que condicionan multas y obligaciones. No se resuelve
  con el material de la cursada.

[^eu-ai-act]: Reg. (UE) 2024/1689, texto en español del DOUE.
[^eu-ai-act-eurlex]: Reg. (UE) 2024/1689 en EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[^ai-omnibus]: Reg. (UE) 2026/1744 (Digital Omnibus on AI), DOUE L de 24.7.2026: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
