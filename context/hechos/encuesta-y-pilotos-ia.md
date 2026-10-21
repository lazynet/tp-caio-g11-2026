---
type: Hecho
title: "Encuesta y pilotos internos de IA"
description: "El piloto de IA de abril de 2026 superó sus criterios de valor y falló en capacitación: alta frecuencia de uso y NPS de +42, pero la mitad no hizo ningún curso y casi nadie usa ejemplos al pedir."
status: verified
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Ficha completa cotejada con la encuesta y autoevaluación del piloto de abril de 2026, el análisis de prompts de abril y el diseño del sistema de propuestas comerciales de septiembre: indicadores, frenos, criterios del piloto, calidad de uso y experiencia de delivery. Se conservan los límites de la muestra autoseleccionada de 12 participantes, del análisis de chat y del resultado de delivery de la primera semana, sin extrapolación. Confirmado por Martín en esta conversación."
tags: [caso, ia, adopcion, cultura]
sources:
  - id: interno-encuesta-ia-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Encuesta y autoevaluación del piloto de IA, abril de 2026, n=12 (privado, agregado)"
  - id: interno-poc-prompting-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Análisis de prompts del piloto de IA, abril de 2026 (privado, agregado)"
  - id: interno-propuestas-2026
    resource: "Documento interno de Acme Labs (privado, no publicado)"
    title: "Diseño del sistema de propuestas comerciales, septiembre de 2026 (privado, anonimizado)"
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-13T23:00:00Z }
---
# Encuesta del piloto (abril de 2026)

Respondieron los 12 participantes del piloto, de distintas áreas.[^interno-encuesta-ia-2026]

| Indicador | Resultado |
|---|---|
| NPS | +42 (50% promotores, 8% detractores) |
| Usan la herramienta 3 o más días por semana | 92% |
| Chocaron con el límite de uso del plan | 58% |
| Completaron los tres cursos obligatorios | 17% |
| No hicieron ningún curso | 50% |

**Frenos y pedidos:** el primer freno es la falta de tiempo para capacitarse (dos
de cada tres); más de la mitad pide casos prácticos por rol en lugar de cursos
genéricos; hubo fallas de comunicación sobre la capacitación asignada. Parte
de los participantes advierte sobre la dependencia de un solo proveedor de
modelos y propone consumo multimodelo.[^interno-encuesta-ia-2026]

**Criterios del piloto:** cumplió con holgura los umbrales de adopción (uso
frecuente) y de casos de valor (casos que las otras herramientas no
resolvían); no cumplió la capacitación obligatoria al primer
mes.[^interno-encuesta-ia-2026]

# Calidad de uso (análisis de prompts, abril de 2026)

Sobre más de un centenar de conversaciones del chat corporativo:[^interno-poc-prompting-2026]

- Casi nadie da ejemplos del resultado esperado (*few-shot* en 5% o menos).
- Las buenas prácticas se copian como plantilla, sin internalizarse.
- No hay una regla explícita sobre el uso personal del seat corporativo.
- Pocos usuarios piden contraargumentos o advierten sobre alucinaciones.

# Piloto de delivery con IA

Un equipo que trabajó con agentes de código desde el inicio construyó un lote
chico de endpoints en menos de dos días, comparado con un grupo de control del
equipo convencional, con umbrales de cobertura y de *mutation testing* como
compuertas de calidad.[^interno-propuestas-2026]

# Cautelas

- n=12 y autoseleccionado: no representa a la organización.
- El análisis de prompts cubre solo el chat; los perfiles técnicos usan sobre
  todo la terminal.
- El resultado del piloto de delivery vale solo para la primera semana; la propia
  fuente advierte que no se puede extrapolar.
- Se publican solo agregados: ni citas ni resultados por persona.

[^interno-encuesta-ia-2026]: Encuesta y autoevaluación del piloto de IA, abril de 2026, n=12 (privado, agregado)
[^interno-poc-prompting-2026]: Análisis de prompts del piloto de IA, abril de 2026 (privado, agregado)
[^interno-propuestas-2026]: Diseño del sistema de propuestas comerciales, septiembre de 2026 (privado, anonimizado)
