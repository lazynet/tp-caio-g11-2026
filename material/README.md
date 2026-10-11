# material

Índice del material de la cursada: qué documento respalda cada sección del plan.
Los PDFs viven en la carpeta de Drive de Martin y no se copian al repo. La ruta
local está en `private/sources.md` (no versionado).

Los extractos del notebook se pegan acá, cada uno con la unidad de origen.

## Programa

14 semanas. El objetivo final es "elaborar y defender un Plan Maestro a 12 meses frente a un board ejecutivo".

| Módulo | Unidades |
|---|---|
| M1 Estrategia, Visión y Ejecución | U1 Mentalidad CAIO · U2 Portfolio y 100 días · U3 Datos y contexto · U4 Rol, gobernanza y arquitectura org. · U5 TIF · U6 Recuperatorio |
| M2 Tecnología, Coding y Fuerza Laboral Sintética | U1 Vibe coding · U2 Agentes y arquitecturas · U3 Fuerza laboral aumentada · U4 AIOps, observabilidad y economía |
| M3 Seguridad, Cultura, Talento y Futuro | U1 Seguridad y resiliencia · U2 Cambio y AI Literacy · U3 Talento y reestructuración · U4 Cierre y defensa del Plan Maestro |

El programa menciona estos artefactos: AI Constitution 1.0, AI Risk Register, CAIO Operating System (rituales, RACI, cadencias), AI Portfolio con reglas de kill/scale, ADKAR / Kotter / Lean Change.

## Sección del plan → fuentes

| Sección | Fuente principal | Complementos |
|---|---|---|
| Diagnóstico / punto de partida | M1U1: madurez en 5 dimensiones, escala 1-5 | AIMM (nivel = dimensión más débil), Cisco (6 pilares con pesos) |
| Arquitectura | Memoria-Contexto-Harness: Agente = Modelo + Harness, 7 componentes | M1U3 (estrategias de contexto, data contracts), M1U4 (escala L0-L4), M2U3 (grafo humano-agente), M2U4 (evals, versionado, release gates) |
| Build / buy / partner | M1U2: triángulo build / buy / agentificar | BAIC (propietario vs open source) |
| Gobierno | M1U4: decision rights, Council vs CoE, Governance Stack Principles→Evidence | Microsoft RAI Maturity (24 dimensiones), programa (AI Constitution, Risk Register) |
| Compliance | M1U4: EU AI Act + NIST AI RMF + ISO/IEC 42001 | EU AI Act (texto), ver cautelas |
| Seguridad | M3U1: prompt injection, DLP, red teaming | Harness (10 fallas de contexto, gate antes de efectos irreversibles), M1U3 (PII, anonimización) |
| People plan | M3U2: AI Literacy por rol, AI Champions en 4 fases | M2U3 (fuerza laboral sintética), BAIC (perfiles usuario / adaptador / desarrollador), M1U4 (RACI con una sola A) |
| Roadmap cultural | Resumen visual M3U2: frenos a la adopción, Prompt Challenge | M3U2 slides (transparencia, co-diseño, victorias tempranas) |
| Roadmap técnico / 100 días | M1U2: plan en 3 fases (1-30, 31-70, 71-100) | M1U1 (plan de 30 días), M2U4 (ciclo desplegar → evaluar → monitorear) |
| Finanzas / CFO | M1U2: RICE ajustado por riesgo, business case, outputs de negocio | M2U4 (tokenomics), M1U4 (costo por outcome) |
| Risk-adjusted roadmap | M1U2: SLOs y kill/scale gates | M1U1 (kill-fast), M1U4 (autonomía, consecuencia, reversibilidad, blast radius) |
| Defensa | M1U4 lectura (caso Mercurio SA), M3U1 (caso red team) | M3U4: **falta material** |

## Catálogo

### Módulo 1

- **Programa** (`Diplomatura Chief AI Officer (CAIO) 185354.pdf`): temario, objetivos y artefactos.
- **M1U1 Mentalidad CAIO**. Hay dos versiones:
  - `Módulo 1 — Unidad 1 — …pdf`, la extendida: kill-fast, 5 habilitadores, radar de señales, Personal AI OS, 4 anti-patterns del líder, plan de 30 días.
  - `Documento_…_Unidad_1 (2).pdf`, la corta: tres eras del software (determinística, probabilística, agéntica) y diagnóstico de madurez en 5 dimensiones.
  - Cita: "Un experimento que falla en dos semanas es infinitamente más valioso que uno que falla en seis meses."
- **M1U2 Portfolio y 100 días**: matriz factibilidad-impacto, RICE ajustado por riesgo, pain killer vs vitamina, build / buy / agentificar, SLOs y kill/scale gates, 100 días en 3 fases.
  - Cita para el CFO: "La precisión del modelo es un input; la reducción del tiempo de procesamiento de facturas en un 40% es el output que le importa al CFO."
- **M1U3 Datos y contexto** (`Modulo 1 Unidad 3.pdf`): prompt vs RAG vs fine-tuning vs long context, Data Contracts en YAML, context engineering, anonimización en inferencia, higiene de datos.
- **M1U4 Rol, gobernanza y arquitectura org.**: lectura de 25 páginas, más las slides v3.
  - Decision rights (p. 2) y Microsoft Agentic AI Adoption Maturity Model, 5 pilares × 5 niveles (p. 6-7).
  - Escala de autonomía L0-L4 (p. 13-15) y Governance Stack (p. 15-16).
  - EU AI Act / NIST AI RMF / ISO 42001 (p. 18-20). Caso Mercurio SA.
  - Cita: "El rol del CAIO no es controlar toda la IA. Es diseñar un sistema que permita a la organización moverse rápido sin perder accountability." (p. 23)

### Módulos 2 y 3

El número de unidad en el nombre de archivo (7 a 10) no coincide con el del programa. Acá van mapeadas por título.

- **M2U3 Fuerza laboral aumentada y sintética** (`…Modulo_2_Unidad_7.pdf`): grafo humano-agente; tres modos (automatización, aumentación, supervisión); gemelos digitales; multi-agente.
- **M2U4 AIOps, observabilidad y economía** (`…Modulo_2_Unidad_8.pdf`): evals; logs, métricas y trazas; versionado de modelo, datos, código y config; release gates; tokenomics.
- **Memoria, contexto y harness** (`Memoria-Contexto-Harness.pdf`, 16 páginas, "Data Management en Soluciones de Gen IA"; no indica unidad):
  - 10 fallas de contexto (p. 3-12).
  - Agente = Modelo + Harness, con 7 componentes (p. 14); tres capas (p. 15); cinco elementos de diseño (p. 16).
- **M3U1 Seguridad, riesgos y resiliencia** (`…Modulo_3_Unidad_9.pdf`): jailbreaks y prompt injection, DLP, pipeline seguro, proceso de red teaming.
  - Cita: "El modelo no distingue entre instrucciones del sistema y entradas maliciosas del usuario."
- **M3U2 Cambio y AI Literacy**, en dos archivos:
  - `…Modulo_3_Unidad_10.pdf`: literacy en 3 niveles, programa de champions, estrategias de transición.
  - `UTNBA_CAIO_M3_U2_Resumen_visual.pdf`, solo imagen: literacy por rol (ejecutivos, mandos medios, colaboradores), champions en 4 fases, Prompt Challenge de 2 semanas, frenos a la adopción.

### Frameworks generales

- **EU AI Act**, Reg. (UE) 2024/1689:
  - Niveles: prohibidas (art. 5), alto riesgo (art. 6 + Anexo III; el 5.b cubre scoring crediticio salvo fraude), transparencia (art. 50), uso general (cap. V).
  - Aplicación (art. 113): 2025-02-02 caps. I-II · 2025-08-02 uso general y sanciones · 2026-08-02 general · 2027-08-02 art. 6.1.
  - Multas de hasta 35 M EUR o 7% de la facturación mundial.
  - Proveedor (art. 16) vs desplegador (art. 26). Flexibility pasa a ser proveedor si pone su marca a un sistema (art. 25).
- **Microsoft Responsible AI Maturity Model** (2023): 24 dimensiones en 5 niveles (Latent → Leading). No se promedian.
- **Cisco AI Readiness Index 2025**: 6 pilares con peso (Strategy 15, Infrastructure 25, Data 20, Governance 15, Talent 15, Culture 10); 4 perfiles (Pacesetters 13%). Es una encuesta global: sirve como contexto, no como benchmark local.
- **BAIC, Guía GenAI**: metodología de 7 pasos, del business case a la monitorización; perfiles usuario / adaptador / desarrollador.
- **CAIE** (Putnoki y Orosz, 2026): 6 zonas cognitivas y más de 90 rasgos para evaluar sistemas de IA. Es académico: usarlo como rúbrica, no como estándar.
- **AIMM (Gartner)**: 5 niveles (Awareness → Transformational). El nivel global lo fija la dimensión más débil.

## Huecos

- No hay material de M2U1 (vibe coding), M2U2 (agentes y arquitecturas), M3U3 (talento y reestructuración) ni **M3U4 (cierre y defensa del Plan Maestro)**. M3U4 es la que más importa para el TP: hay que buscarla en el notebook o en el aula.
- `Video Clase 1.mp4` no está indexado.

## Cautelas para citar

- **AIMM**: el propio documento dice que se redactó sin acceso al informe de Gartner. Verificar antes de citarlo.
- Dos cifras sin fuente en las slides: "60-80% menos costo de inferencia" (M2U4) y "60% menos resistencia" (M3U2). No van en una slide sin fuente primaria.
- M1U4 menciona el AI Omnibus (Reg. UE 2026/1744) y la guía SIGEN 197/2026. No se verificaron contra fuente primaria.
- M1U2 cita FINMA 08/2024, que es suizo: aclararlo si se usa.
- Hay duplicados idénticos (mismo md5): los "(1)" de M1U2 y de la lectura de M1U4.
