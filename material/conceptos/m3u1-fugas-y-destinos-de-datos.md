---
type: Concepto
title: "Tres fugas de datos y destino permitido por tipo de dato"
description: "Las vías por las que se escapan datos en sistemas de IA, del usuario, del modelo y operativa, y a qué destino puede ir cada tipo de dato según la Clase 9."
tags: [m3, seguridad, datos, dlp]
sources:
  - id: clase9
    resource: "Hoy atacamos · CAIO Clase 9.pdf"
    title: "Hoy atacamos, CAIO Clase 9, láminas 07, 08 y 09"
  - id: m3u1-doc
    resource: Documento_Chief_AI_Officer_CAIO_Modulo_3_Unidad_9.pdf
    title: "M3U1, documento de lectura (Unidad 9), pp. 4-6"
status: draft
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T14:30:00Z }
---

# Tres fugas, no dos

El documento de lectura describe dos vías: del lado del usuario y del lado del
modelo (p. 4).[^m3u1-doc] La Clase 9 suma una tercera (lámina 07):[^clase9]

| Fuga | Qué pasa |
|---|---|
| Del usuario | "Pega un contrato en un chat público" (Samsung, 2023) |
| Del modelo | "Devuelve lo que vio" |
| Operativa | "Secretos en logs, prompts, repos y capturas. Nadie la pega, se escurre" |

# Dato → destino permitido

Lámina 07:[^clase9]

| Destino | Dato que puede ir |
|---|---|
| LLM público | Información ya pública |
| Enterprise con contrato | Datos internos del negocio |
| Privado | Datos de clientes y pacientes |
| Ninguno | Secretos y credenciales |

# Controles

- **DLP en un sistema real (lámina 08):** anonimización (datos médicos enmascarados
  antes de salir, con revisión humana), compartimentación ("lo de un cliente habla
  solo de ese cliente"), separación de canales (el PIN de un voucher nunca viaja con
  la imagen del voucher) y cifrado y monitoreo ("lo que IT ya tenía").[^clase9]
- **Secretos (lámina 09):** "Los secretos nunca pasan por el chat"; "todo lo que está
  en el contexto del modelo se puede descubrir"; una clave commiteada no se arregla
  borrándola: hay que rotarla.[^clase9]
- **Marco de DLP del documento (pp. 5-6):** clasificación y descubrimiento, política
  de uso, gateway de IA, sandboxing, modelos privados, capacitación, y monitoreo y
  respuesta.[^m3u1-doc]

# Relación con otras fichas

Amplía [DLP en sistemas de IA](/conceptos/m3u1-dlp-datos-en-riesgo.md), que sigue la
presentación de 20 slides. La política de datos por destino es el control 5 del
[scorecard](/conceptos/m3u1-scorecard-seguridad-directorio.md), y la gestión de
secretos, el 6.

# Cautelas

* Ficha nueva, en borrador, sin verificación humana. Cotejo del agente contra las
  láminas 07 a 09 (07 y 08 leídas como imagen) y las pp. 4-6 del documento, el
  2026-10-21.
* El caso Samsung (2023) se cita por nombre, sin fuente; no se cotejó.
* La tabla de destinos es un criterio del curso, no una clasificación legal. Para Acme
  Labs manda su propia política de clasificación de datos.

[^clase9]: Hoy atacamos, CAIO Clase 9, láminas 07 a 09
[^m3u1-doc]: M3U1, documento de lectura (Unidad 9), pp. 4-6
