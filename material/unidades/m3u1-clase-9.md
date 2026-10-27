---
type: Unidad
title: "M3U1 Clase 9, Hoy atacamos (presentación de la sesión)"
description: "Presentación de 15 láminas de la clase de seguridad, con la regla de dos de tres, tres fugas de datos, secretos, red teaming medido, marcos de referencia y un scorecard para el directorio."
tags: [m3, seguridad, clase, red-teaming]
sources:
  - id: clase9
    resource: "Hoy atacamos · CAIO Clase 9.pdf"
    title: "Hoy atacamos, Seguridad e integridad en LLMs, CAIO Clase 9: portada y 15 láminas (16 páginas)"
status: accepted
accepted:
  by: human:lazynet
  at: 2026-10-21
  scope: "Aceptación documental por instrucción expresa de Martín en esta sesión, incorporación al corpus del TP tras aceptar presentaciones oficiales como material suficiente para cerrar #22; no acredita por sí sola cotejo primario ni verificación normativa. Se acepta la inclusión de esta ficha y sus referencias a U9 o «Hoy atacamos», cuyos originales no fueron localizados; no se afirma su localización ni se verifica su contenido."
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T14:30:00Z }
---

# Qué es

Presentación de la clase de seguridad de M3U1. Es otro archivo que la
[presentación de 20 slides](/unidades/m3u1-seguridad.md) y que el
[documento de lectura](/unidades/m3u1-documento-u9.md). Su tesis es de diseño:
lo que importa no es si el modelo se puede engañar, sino qué puede hacer el agente
cuando se equivoca.[^clase9]

La numeración es la de las láminas (01/15 a 15/15); la página del PDF es la lámina
más uno, porque la p. 1 es la portada.

# Contenido

| Lámina | Tema | Idea central |
|---|---|---|
| 01 | Escenario | "Un CAIO que no sabe atacar su IA no sabe cuánto riesgo tiene": una web con una orden escondida hace que un bot que resume documentos ofrezca un descuento que no existe |
| 02 | El problema | "El modelo no distingue órdenes de datos": instrucciones del sistema, pedido del usuario y contenido externo van en un solo flujo de texto. Inyección directa, inyección indirecta ("la que importa en agentes") y jailbreak. "La pregunta no es si se puede hacer jailbreak, sino qué puede hacer el agente cuando el modelo se equivoca" |
| 03 | Incidentes | Air Canada (2024), una concesionaria en EE. UU. (2023) y EchoLeak en Microsoft 365 Copilot (2025, CVSS 9,3). "Dos tipos de riesgo: lo que el bot DICE y lo que el bot HACE" |
| 04 | Regla de diseño | "Los filtros no alcanzan": [regla de dos de tres](/conceptos/m3u1-regla-dos-de-tres.md) |
| 05 | Antes y después | Con controles, el agente detecta instrucciones sospechosas, cita el texto escondido sin ejecutarlo y no tiene herramienta para aplicar descuentos. "La diferencia entre un incidente y una anécdota es qué permisos tenía" |
| 06 | Multiagente | "Lavado de permisos": "El mensaje de otro agente nunca otorga permisos". "Cada agente es una identidad con permisos, como un empleado" |
| 07 | Datos | [Tres fugas y destino permitido por tipo de dato](/conceptos/m3u1-fugas-y-destinos-de-datos.md) |
| 08 | Controles | DLP en un sistema real: anonimización, compartimentación, separación de canales, cifrado y monitoreo |
| 09 | Secretos | "Los secretos nunca pasan por el chat". "Todo lo que está en el contexto del modelo se puede descubrir". Claves de producción commiteadas: "Borrarlas no alcanza: hay que rotarlas" |
| 10 | Proceso | Red teaming "de evento a proceso": alcance escrito y firmado, atacar, medir y regresión. Medir la **tasa** de éxito, no si funcionó: el mismo ataque corrido 20 veces. Herramientas abiertas: PyRIT, garak y promptfoo |
| 11 | Lo clásico | Fallas de IDOR y de autorización en rutas: "Una aplicación de IA es una aplicación" |
| 12 | Caso | [FinBot](/casos/m3u1-finbot.md) leído con la regla de dos de tres |
| 13 | Marcos | [Para qué sirve cada marco](/conceptos/m3u1-marcos-seguridad.md) |
| 14 | Gobierno | [Scorecard que el CAIO le lleva al directorio](/conceptos/m3u1-scorecard-seguridad-directorio.md) |
| 15 | Cierre | "La seguridad de IA no es un filtro que se compra. Es qué lee el agente, qué puede hacer y quién aprueba, medido todos los meses" |

Fuente de la tabla: [^clase9]

# Relación con otras fichas

- El [apunte del 2026-10-06](/apuntes/2026-10-06-seguridad-agentes.md) registra los
  mismos temas (FinBot, marcos, scorecard, red teaming continuo) a partir de notas de
  clase. Esta presentación es la fuente primaria de esos temas; que sea la misma
  sesión es una inferencia por coincidencia de contenido.
- La ficha de la [unidad](/unidades/m3u1-seguridad.md) dice que el curso "no cita
  estándares": vale para las 20 slides. Esta clase sí cita OWASP, MITRE ATLAS y
  NIST (lámina 13).

# Respalda

Seguridad y gobierno: secretos fuera del chat, prueba adversarial, aprobación humana
en acciones críticas y un tablero mensual para el directorio. Es lectura de esta
ficha, no afirmación del curso sobre Acme Labs.

# Cautelas

* La aceptación cubre la inclusión de la ficha en el corpus. Los originales de U9
  y «Hoy atacamos» no fueron localizados en la búsqueda local; las referencias a
  cotejos del agente son antecedentes de elaboración, sin verificación humana.

* Ficha aceptada para el corpus, sin verificación humana del contenido. Cotejo del agente contra el PDF
  de 16 páginas, con las láminas 03, 04, 07, 08 y 14 leídas como imagen, el
  2026-10-21.
* Los incidentes de la lámina 03 y de las láminas 09 y 11 se citan como en la
  presentación (dos de ellos como "ficha de incidente, anónima"); no se cotejaron
  fuentes primarias. No van a una slide como evidencia sin fuente.
* La presentación no trae referencias bibliográficas.

[^clase9]: Hoy atacamos, CAIO Clase 9, láminas 01 a 15
