---
type: Concepto
title: Verificación del AI Omnibus (Reg. UE 2026/1744) y la guía SIGEN 197/2026
description: Resultado de chequear contra fuentes externas las dos citas que el curso daba sin fuente primaria, con fechas, alcance y diferencias.
tags: [m1, compliance, regulacion, verificacion]
sources:
  - id: m1u4-lectura
    resource: Lectura - Módulo 1 — Unidad 4 — Rol del CAIO, gobernanza y arquitectura organizacional.pdf
    title: M1U4, lectura de 25 páginas
  - id: cooley-omnibus
    resource: https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
    title: Cooley, Digital AI Omnibus delays key deadlines and introduces new rules
  - id: abreu-omnibus
    resource: https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/
    title: Abreu Advogados, Digital Omnibus Regulation on AI, the key amendments to the AI Act
  - id: ertico-omnibus
    resource: https://ertico.com/digital-omnibus-on-ai-enters-into-force
    title: ERTICO, Digital Omnibus on AI enters into force
  - id: sigen-197
    resource: https://www.argentina.gob.ar/normativa/nacional/norma-426859/texto
    title: Infoleg/argentina.gob.ar, Resolución 197/2026 de la SIGEN
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Lectura M1U4 p. 11, 19 y 25 más Cooley, Abreu, ERTICO y la Resolución SIGEN 197/2026 (texto en argentina.gob.ar): fechas y alcance contrastados con fuentes secundarias; EUR-Lex y anexo de SIGEN sin leer. Cotejo del agente revisado y confirmado por Martín en esta conversación."
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Resumen

| Cita del curso | Resultado |
|---|---|
| AI Omnibus, Reg. (UE) 2026/1744 | **Existe y coincide en lo esencial.** Quedan sin cotejar contra el Official Journal el texto de cada artículo y la nota sobre guidelines de la Comisión |
| Guía SIGEN 197/2026 | **Existe y coincide.** Matiz: su carácter obligatorio no surge del texto de la resolución y aplica al sector público nacional, no a empresas privadas |

# AI Omnibus (Reg. UE 2026/1744)

Datos que coinciden entre la lectura y las fuentes secundarias:

- Firmado el 8 de julio de 2026 (fecha del reglamento), publicado en el Official Journal
  el 24 de julio y en vigor el 27 de julio de 2026 (la lectura dice lo mismo, p. 19 y
  25). Cooley da el 29 de junio como adopción del texto final.[^m1u4-lectura][^cooley-omnibus][^ertico-omnibus]
- Modifica el Reglamento (UE) 2024/1689. La modificación de otros dos reglamentos
  (2018/1139 y 2023/1230) no se pudo reconfirmar en Abreu al recotejar el 2026-10-20.[^abreu-omnibus]

Calendario nuevo según Cooley:[^cooley-omnibus]

| Ítem | Fecha original | Fecha nueva |
|---|---|---|
| High-risk Anexo III (empleo, educación, aplicación de la ley, etc.) | 2 de agosto de 2026 | 2 de diciembre de 2027 |
| High-risk en productos regulados, Anexo I (juguetes, dispositivos médicos, maquinaria) | 2 de agosto de 2027 | 2 de agosto de 2028 |
| Art. 50 transparencia para sistemas nuevos | 2 de agosto de 2026 | Sin cambio |
| Art. 50(2) marcado para sistemas ya en el mercado antes del 2 de agosto de 2026 | 2 de agosto de 2026 | 2 de diciembre de 2026 (gracia) |
| High-risk usados por autoridades públicas | 2 de agosto de 2026 | 2 de agosto de 2030 |
| Sandboxes regulatorios de los Estados miembros | 2 de agosto de 2026 | 2 de agosto de 2027 |

Otros cambios que no menciona el curso:[^abreu-omnibus][^ertico-omnibus]

- Dos nuevas prohibiciones en el art. 5 sobre IA generativa (material íntimo no
  consentido y abuso sexual infantil), desde el 2 de diciembre de 2026.
- Más facultades de supervisión para la AI Office sobre modelos de uso general.
- Base legal voluntaria para tratar datos de categorías especiales cuando sea
  estrictamente necesario para detectar y corregir sesgos.

## Diferencia con el curso: art. 4

La lectura dice que el art. 4, modificado, "exige a providers y deployers tomar
medidas para apoyar el desarrollo" de AI literacy (p. 11). Cooley y Abreu describen el cambio con otro énfasis: ya no se exige "asegurar" la competencia del personal, y la Comisión y los
Estados miembros "apoyan y facilitan".[^m1u4-lectura][^cooley-omnibus][^abreu-omnibus] La
ficha [proveedor y desplegador](/frameworks/eu-ai-act-proveedor-desplegador.md) leyó
una copia del DOUE del Reg. 2026/1744 y confirma el cambio: "adoptarán medidas para
apoyar el desarrollo" de la alfabetización, sin exigir un nivel garantizado. Falta
cotejarlo contra el ELI oficial antes de llevarlo a una slide. Ver
[champions y literacy](/conceptos/m1u4-champions-y-literacy.md).

## Qué no se verificó

- Texto de los artículos en EUR-Lex (las búsquedas devolvieron fuentes secundarias).
- Las guidelines de transparencia de la Comisión del 20 de julio de 2026.
- Que "Digital Omnibus on AI" sea el título oficial usado en el Official Journal; dos
  fuentes lo usan como nombre del reglamento.

Qué hacer: usar las fechas de la tabla con cita a Cooley y al Reglamento, y
chequear EUR-Lex antes de ponerlas en una slide. Calendario original:
[EU AI Act](/frameworks/eu-ai-act.md), sin editar acá.

# Guía SIGEN, Resolución 197/2026

- Resolución SIGEN 197/2026, sancionada el 16 de junio de 2026 y publicada en el
  Boletín Oficial el 22 de junio de 2026 (n.º 35934).[^sigen-197]
- Art. 1: aprueba la "Guía de Controles Inteligencia Artificial - SIGEN" como anexo.
  Art. 2: se aplica a todo el Sector Público Nacional (art. 8 de la Ley 24.156).[^sigen-197]
- Enfoque basado en riesgos y control interno; se apoya en las resoluciones SIGEN
  172/2014 y 87/2022.[^sigen-197]
- El anexo con el contenido de la guía no se publica en el texto de la resolución y no
  se leyó. Los considerandos hablan de "orientar"; el texto no usa la palabra
  "obligatoria", aunque el art. 2 dice que "será de aplicación".[^sigen-197]

Consecuencia para el plan: la guía **no es obligatoria para Acme Labs** como
empresa privada. Importa si un cliente es un organismo público o como referencia de
controles. La lectura la presenta como instrumento del sector público
(p. 19).[^m1u4-lectura]

Unidad: [M1U4](/unidades/m1u4-rol-gobernanza.md).

# Cautelas

* Cotejada el 2026-10-20 contra M1U4 lectura, p. 11, 19 y 25 (PDF de 25 páginas), y
  contra Cooley, Abreu, ERTICO y el texto de la Resolución SIGEN 197/2026 en
  argentina.gob.ar. No se abrió EUR-Lex ni el ELI oficial.
* Se corrigió la fecha de adopción: el 8 de julio es la fecha del reglamento (firma,
  según la lectura p. 25 y ERTICO); Cooley da otra para el texto final (29 de junio).
* Se corrigió la cita del art. 4: la lectura ya dice "para apoyar el desarrollo". El
  desacuerdo con el curso es de énfasis ("exige" y "obligación"), no una
  contradicción literal. Cooley y Abreu son descripciones, no el texto del artículo.
* Cotejados con SIGEN: sanción 16-06-2026, Boletín Oficial 22-06-2026 (n.º 35934),
  arts. 1 y 2, resoluciones 172/2014 y 87/2022, y la ausencia de "obligatoria".
* La lectura (p. 19) tiene el calendario del Anexo III (2-dic-2027), del Anexo I
  (2-ago-2028), del art. 50 y las guidelines del 20-jul-2026; coincide con Cooley.
* Fidelidad a fuentes secundarias no es verdad regulatoria: ninguna fecha va a una
  slide sin el ELI oficial. El AI Act no se declara aplicable a Acme Labs.

[^m1u4-lectura]: M1U4, lectura, secciones 4.1, 9.1 y fuentes (p. 11, 19, 25)
[^cooley-omnibus]: Cooley, Digital AI Omnibus (consultado el 2026-10-12)
[^abreu-omnibus]: Abreu Advogados (consultado el 2026-10-12, a partir de un resultado de búsqueda)
[^ertico-omnibus]: ERTICO (consultado el 2026-10-12, a partir de un resultado de búsqueda)
[^sigen-197]: Resolución SIGEN 197/2026, texto en argentina.gob.ar (consultado el 2026-10-12)
