---
type: Hueco
title: Huecos del material
description: Qué falta en el material de la cursada, qué quedó sin verificar y qué cifras no pueden ir a una slide.
tags: [pendiente, cursada, cautelas]
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-20T19:40:00Z }
---

# Unidades y clases sin material

* No hay material de M2U1 (vibe coding) ni M2U2 (agentes y arquitecturas).
* M3U3 y M3U4 tienen solo slides, de nivel alto. M3U3 no desarrolla evaluación de
  desempeño en humanos aumentados, Physical AI, Human-Agent Trust ni fronteras
  2026-2030, que el programa lista. M3U4 no desarrolla el roadmap ajustado por
  riesgo (contingencias, reversibilidad) ni la storyline, el banco de objeciones o
  la rúbrica del panel. Esos temas hay que buscarlos en el notebook o en el aula.
* El programa no publica una rúbrica de evaluación del TIF (ver [evaluación del
  programa](/conceptos/programa-evaluacion.md)). La guía docente del Corrector IA
  propone una rúbrica formativa, no oficial: [rúbrica del Corrector IA](/frameworks/rubrica-corrector-caio.md).
* Falta el prompt base del Corrector IA (`Prompt_base_Revisor_CAIO.txt`), que según
  la guía docente conserva los controles críticos y el formato de respuesta. No está
  visible en el aula.
* El Corrector IA cita "M3-U4 Fundamentos para la Presentación de un Plan Maestro"
  como referencia. Según el equipo, es el material de [M3U4](/unidades/m3u4-plan-maestro.md)
  que ya está incluido (`..._Modulo_3_Unidad_12.pdf`); no se cotejó el `.md` del aula.
* Sin apuntes de las clases del 2026-08-25, 2026-09-01, 2026-09-08 y 2026-09-15: las
  notas están vacías.
* `Video Clase 1.mp4` no está indexado.
* El curso no cubre ADKAR, Kotter ni Lean Change, aunque el programa los menciona. Si
  el plan los usa, hay que sumar una fuente propia.

# Cifras que no van en una slide

| Cifra | Dónde | Estado |
|---|---|---|
| "60-80% menos costo de inferencia" | [M2U4](/conceptos/m2u4-tokenomics.md) | Sin fuente primaria. Usar los mecanismos (caché, ruteo) sin porcentaje, o un supuesto marcado |
| "70% más de retención de talento" con reskilling | [M3U3](/conceptos/m3u3-transicion-responsable.md) | Sin fuente primaria y sin base de comparación. No va en una slide |
| "60% menos resistencia" | [M3U2](/conceptos/m3u2-frenos-y-transicion.md) | Sin fuente primaria; solo apareció un resumen secundario de Deloitte con otras cifras |
| ROI 2,8×-4,1× e inversiones en euros | casos de [M1U1](/conceptos/m1u1-caso-diagnostico-rrhh.md) y [M1U2](/conceptos/m1u2-caso-portfolio-financiera.md) | Ilustrativas del curso |
| Cifras de Logística Sur | [Prompt Challenge](/conceptos/m3u2-prompt-challenge.md) | Didácticas |
| 24/7, ~0% y 100% de los empleados sintéticos | [M2U3](/conceptos/m2u3-empleados-sinteticos.md) | Marketing sin fuente |
| "Hasta 50%" de baja de costos y 360 → 7 USD como "66% más barato" | [apunte 29/9](/apuntes/2026-09-29-tokenomics-aiops.md) | Sin fuente; la cuenta da ~98%, no 66% |
| 93% de Anthropic, marco de OpenAI | [M1U4](/unidades/m1u4-rol-gobernanza.md) | Citas de segunda mano |

# Correcciones al contenido del curso

* **FINMA 08/2024** es suiza y no define ciclos trimestrales de revisión: el ritmo
  trimestral es práctica del curso ([verificación](/conceptos/m1u2-cautelas-citas-regulatorias.md)).
* **AI Act:** entró en vigor el 2024-08-01, no en julio.
* **AI Omnibus (Reg. UE 2026/1744):** existe y rige desde el 2026-07-27. Corre el alto
  riesgo del Anexo III al 2027-12-02 y el del Anexo I al 2028-08-02
  ([AI Omnibus y SIGEN](/conceptos/m1u4-ai-omnibus-sigen.md)).
* **SIGEN 197/2026** existe, pero aplica al Sector Público Nacional: no obliga a
  Acme Labs.
* **CAIE** dice "más de 90 rasgos" pero enumera 86.
* **AIMM:** el PDF es una elaboración independiente, no el informe de Gartner. Queda en
  `draft`.

# Pendiente de verificar

* **M3U4:** el roadmap técnico habla de MLOps clásico y no de agentes ni LLMOps; no trae metas ni umbrales para los KPIs. **M3U3:** el programa describe el Deep Research con un plan a 18 meses y las slides no dan plazo.

* **EU AI Act tras el Omnibus:** las fechas y el nuevo art. 4 (AI literacy: "apoyar
  el desarrollo", más liviano que el "exige" del curso) se leyeron de una copia del
  DOUE y coinciden entre las fichas. Falta cotejarlos contra el ELI oficial de
  EUR-Lex, junto con las guidelines del 2026-07-20 y la fecha de los arts. 43 y 49.
* **Alcance del AI Act sobre Acme Labs:** decidir con el equipo si alcanza a sus
  clientes (art. 2.1.c).
* **SIGEN 197/2026:** no se leyó el anexo.
* **AIMM:** el informe de Gartner es de pago; sin acceso no se puede salir de `draft`.
* **CAIE:** falta validación externa, el cuestionario del piloto y confirmar la
  fórmula del SZUCS.
* **Microsoft RAI:** sin umbrales cuantitativos ni casos; el deck de taller no se leyó.
* **Cisco:** falta cotejar con el PDF publicado por Cisco.
* **M1U3:** cuatro fuentes web sin URL (PIIvot, PrivacyShield, Data Contracts in
  Action, Clandestinio) no se identificaron.
* **M1U1:** el AI Maturity Model de Gartner y las listas de NovaGob que cita el curso.
* **M2U4:** no da metodología de evals (datasets, umbrales, LLM-as-judge) ni umbrales
  de release gates. **Harness:** tamaños de ventana, la cita de Harrison Chase y la
  clasificación de productos; los 3 labs de la p. 13 son solo capturas.
* **M2U3:** no trae un proceso de ejemplo con nodos y arcos, ni casos de gemelos
  digitales.
* **Seguridad:** el curso no cita un estándar; se sumó OWASP LLM Top 10. Si el plan
  los necesita, faltan NIST AI RMF (perfil GenAI) y MITRE ATLAS.
* **Apuntes:** "PromptFoo" y "millones de tokens" son lecturas supuestas de las notas.

# Catálogo

Hay duplicados idénticos (mismo md5): los "(1)" de M1U2 y de la lectura de M1U4. Se
tratan como copias.
