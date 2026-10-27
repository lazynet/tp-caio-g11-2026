---
type: Unidad
title: "M3U1 Seguridad, documento de lectura (Unidad 9)"
description: "Documento de lectura de 9 páginas de M3U1, con inyección directa e indirecta, tácticas avanzadas, un marco de DLP con gateway y sandboxing, y el caso FinBot."
tags: [m3, seguridad, lectura]
sources:
  - id: m3u1-doc
    resource: Documento_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: "M3U1, documento de lectura (el archivo dice Unidad 9), 9 páginas"
status: accepted
accepted:
  by: human:lazynet
  at: 2026-10-21
  scope: "Aceptación documental por instrucción expresa de Martín en esta sesión, incorporación al corpus del TP tras aceptar presentaciones oficiales como material suficiente para cerrar #22; no acredita por sí sola cotejo primario ni verificación normativa. Se acepta la inclusión de esta ficha y sus referencias a U9 o «Hoy atacamos», cuyos originales no fueron localizados; no se afirma su localización ni se verifica su contenido."
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T14:30:00Z }
---

# Qué es

Documento de lectura de la unidad de seguridad. Es otro archivo que la
[presentación de 20 slides](/unidades/m3u1-seguridad.md) que usa el resto del
corpus: cubre los mismos cuatro bloques (prompt injection y jailbreaks, DLP, red
teaming y un caso práctico) con más desarrollo y con otro caso.[^m3u1-doc]

# Contenido

| Bloque | Páginas | Qué trae |
|---|---|---|
| Introducción y objetivos | 1-2 | Cuatro objetivos: distinguir prompt injection de jailbreaking, aplicar DLP para LLMs, entender el red teaming de IA y analizar un caso de red teaming sobre un agente |
| Prompt injection y jailbreaks | 3 | Distingue **inyección directa** (el atacante modifica el prompt) de **inyección indirecta** (la instrucción va en una web, un documento o un correo que el modelo procesa, sin que el usuario final lo sepa). El jailbreaking es una técnica específica de prompt injection; ejemplo DAN ("Do Anything Now") |
| DLP en IA | 4 | Dos vías de fuga: del lado del usuario (pega contratos, datos de clientes o código en un LLM público) y del lado del modelo (revela información con la que fue entrenado). Estrategias: clasificación, enmascaramiento o redacción antes de enviar, modelos privados y monitoreo en tiempo real |
| Red teaming corporativo | 4 | A diferencia del pentest tradicional, se enfoca en el comportamiento, la lógica y los datos del modelo |
| Tácticas avanzadas | 4-5 | Inyección de múltiples pasos, ataques basados en roles y ofuscación de instrucciones; ejercicio con tres prompts para forzar un descuento no autorizado |
| Marco de DLP para IA | 5-6 | Clasificación y descubrimiento de datos; política de uso de IA; controles técnicos (**gateway de IA** que centraliza el tráfico y monitorea, filtra y redacta datos sensibles; **sandboxing**; modelos privados u on-premise); capacitación; monitoreo y respuesta a incidentes |
| Caso práctico | 6-7 | [FinBot](/casos/m3u1-finbot.md): inyección indirecta con texto oculto en un blog |
| Resumen y autoevaluación | 7-9 | Tres preguntas con respuesta. La del análisis de caso propone reforzar las instrucciones del sistema, validar la salida con un filtro o un segundo modelo y hacer fine-tuning adversarial |

Fuente de la tabla: [^m3u1-doc]

# Relación con otras fichas

- La distinción directa/indirecta (p. 3) es parte del curso, no solo de OWASP: ver
  [prompt injection y jailbreaks](/conceptos/m3u1-prompt-injection-jailbreaks.md),
  cuya sección "Complemento OWASP" la presenta como ajena al curso.
- Las dos vías de fuga (p. 4) se amplían a tres en la
  [Clase 9](/unidades/m3u1-clase-9.md): ver
  [fugas y destinos de datos](/conceptos/m3u1-fugas-y-destinos-de-datos.md).

# Respalda

Seguridad: el gateway de IA, la política de uso y el sandboxing del marco de DLP
(p. 5-6) son controles que el plan discute en los Anexos B y C. Es lectura de esta
ficha, no afirmación del curso sobre Acme Labs.

# Cautelas

* La aceptación cubre la inclusión de la ficha en el corpus. Los originales de U9
  y «Hoy atacamos» no fueron localizados en la búsqueda local; las referencias a
  cotejos del agente son antecedentes de elaboración, sin verificación humana.

* Ficha aceptada para el corpus, sin verificación humana del contenido. Cotejo del agente contra el PDF
  de 9 páginas, página por página, el 2026-10-21.
* Las mitigaciones del documento (afinar el modelo para que sea "más escéptico",
  fine-tuning adversarial, p. 7 y 9) son controles sobre el comportamiento del
  modelo. La [Clase 9](/unidades/m3u1-clase-9.md) pone el peso en limitar lo que el
  agente puede hacer. No se contradicen, pero no tienen el mismo efecto.
* La p. 7 dice que el ataque "permitió la exfiltración de información
  confidencial"; la Clase 9 lo lee de otra forma (ver [FinBot](/casos/m3u1-finbot.md)).
* Referencias de la p. 9 (IBM, Kiteworks, Palo Alto Networks, Trend Micro, OpenAI,
  NeuralTrust): se listan sin URL y no se cotejaron.

[^m3u1-doc]: M3U1, documento de lectura (Unidad 9), pp. 1-9
