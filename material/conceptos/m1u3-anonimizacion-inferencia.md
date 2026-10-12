---
type: Concepto
title: Anonimización de PII en entrenamiento e inferencia
description: Dónde aparece el riesgo de PII, qué técnicas y herramientas cita el curso y el patrón de enmascarar y revertir en la inferencia.
tags: [m1, datos, seguridad, privacidad, pii]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 14 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Qué es PII

Cualquier dato que permita identificar directa o indirectamente a una persona:
nombre, DNI, correo, teléfono, dirección IP. Su protección es obligatoria en marcos
como el GDPR y la **Ley 25.326** argentina (p. 2).[^m1u3]

# Dos momentos, dos estrategias

| Momento | Riesgo | Técnicas |
|---|---|---|
| Entrenamiento | El modelo memoriza datos sensibles y los reproduce | Anonimizar el dataset antes de usarlo, privacidad diferencial durante el fine-tuning, auditoría post-entrenamiento para detectar memorización |
| Inferencia | El usuario mete PII en el prompt, que viaja a APIs externas o queda en logs | Interceptar el prompt, detectar y enmascarar PII, enviar el prompt anonimizado y, si hace falta, revertir la anonimización en la respuesta |

Fuente: Tema 4, p. 6.[^m1u3]

# Patrón de inferencia

1. Interceptar el prompt del usuario antes del LLM.
2. Detectar y enmascarar la PII.
3. Enviar el prompt anonimizado al modelo.
4. Si es necesario, revertir la anonimización en la respuesta para que sea coherente
   para el usuario.

Es especialmente relevante en aplicaciones empresariales, donde los usuarios incluyen
datos de clientes, empleados o pacientes sin ser conscientes del riesgo
(p. 6).[^m1u3]

# Herramientas citadas (2024)

| Herramienta | Qué hace |
|---|---|
| PIIvot | Librería Python con NER ajustado: reemplaza PII por sustitutos realistas que preservan la coherencia semántica del texto, en vez de borrar |
| PrivacyShield | FastAPI + spaCy + Microsoft Presidio; pipeline completo de detección y anonimización que corre en local, con reversión post-inferencia |
| Clandestinio | IA generativa para pseudonimizar datos en entornos de test, detectando columnas sensibles según principios del GDPR |

El documento lista estas tres herramientas entre las fuentes web sin sus URLs
(p. 12): no se verificaron.[^m1u3]

# Relación con el plan

Es el soporte técnico de la sección de seguridad. Complementa el DLP de
[M3U1](/unidades/m3u1-seguridad.md) y las
[estrategias de contexto](/conceptos/m1u3-estrategias-de-contexto.md). Alternativa
para compartir datos sin PII: [datos sintéticos](/conceptos/m1u3-data-moat-datos-sinteticos.md).

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

[^m1u3]: M1U3, Tema 4 (p. 6), conceptos clave (p. 2) y fuentes web (p. 12)
