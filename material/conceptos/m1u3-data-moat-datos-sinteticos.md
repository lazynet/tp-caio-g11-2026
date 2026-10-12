---
type: Concepto
title: Data moat y datos sintéticos
description: Cómo los datos propietarios son un foso defensivo y cómo el dato sintético con privacidad diferencial permite circularlos sin exponer PII.
tags: [m1, datos, estrategia, privacidad]
sources:
  - id: m1u3
    resource: Modulo 1 Unidad 3.pdf
    title: M1U3, documento de 14 páginas
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-12T01:00:00Z }
---

# Data moat

Ventaja competitiva sostenible construida con datos propietarios, únicos o difíciles
de replicar (p. 2).[^m1u3] A diferencia de los modelos, que se pueden replicar o
licenciar, los datos propietarios de alta calidad son una barrera de entrada: "nadie
puede entrenar un modelo con datos que no tiene" (p. 5).[^m1u3]

Fuentes típicas: comportamiento de usuarios, datos de dominio especializado
(registros médicos, transacciones financieras, sensores) o datos generados por
procesos únicos del negocio.

**Cautela del propio material:** acumular sin criterio no es un foso. Calidad,
cobertura y relevancia importan más que el volumen bruto (p. 5).[^m1u3]

# Dato sintético

Dato generado artificialmente (modelos estadísticos, GANs o LLMs) que imita la
distribución y estructura de datos reales sin contener PII. Permite entrenar, testear
y compartir sin comprometer privacidad (p. 2).[^m1u3]

Rol estratégico doble (p. 5):[^m1u3]

1. **Aumentar** datasets existentes cuando los reales son escasos o caros de etiquetar.
2. **Compartir** con socios, auditores o reguladores sin exponer información sensible.

# Privacidad diferencial

Técnica que añade ruido estadístico calibrado a los datos o al entrenamiento. Es el
mecanismo matemático que impide reconstruir registros individuales del dataset
original a partir del sintético. Así el dato sintético circula y genera valor "sin
erosionar el foso defensivo" (p. 5).[^m1u3]

Herramienta citada: Gretel, integrada en BigQuery desde octubre de 2024 (p. 9). En el
caso práctico se usa con presupuesto ε = 1.0 (p. 11).[^m1u3]

Que Gemini más Gretel sea "el estado del arte" es una afirmación del documento, sin
cita primaria.

Flujo completo en el [caso de tickets sintéticos](/conceptos/m1u3-caso-tickets-sinteticos.md).

Unidad: [M1U3](/unidades/m1u3-datos-contexto.md).

[^m1u3]: M1U3, Tema 2 (p. 4-5), conceptos clave (p. 2) y caso práctico (p. 9-11)
