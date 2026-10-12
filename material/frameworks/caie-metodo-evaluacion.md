---
type: Concepto
title: CAIE, método de evaluación y scoring en dos etapas
description: Roles, escalas, fórmulas de la Etapa 1 (ZUCS y SZUCS) y de la Etapa 2 (brechas de madurez y superficie estructural) de CAIE.
tags: [evaluacion, scoring, metodologia]
sources:
  - id: caie
    resource: CAI  CAIE - Framework (paper).pdf
    title: "Putnoki y Orosz (2026), secciones 2.2 y 6, pp. 5 y 37-43"
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte de [CAIE](/frameworks/caie.md). Zonas y rasgos en
[caie-zonas](/frameworks/caie-zonas.md).

# Roles y datos de entrada (sección 6.1, p. 39)

| Rol | Variable | Pregunta | Escala |
|---|---|---|---|
| Desarrolladores o arquitectos | Pᵢ (presencia) | ¿Está implementado el rasgo i? | 0 o 1 |
| Desarrolladores o arquitectos | Lᵢˢʸˢᵗᵉᵐ | ¿A qué nivel de madurez opera hoy? | L1 a L5 |
| Usuarios | Vᵢ (desempeño) | ¿Qué tan bien funciona el rasgo? | 1 (pobre) a 10 (excelente) |
| Usuarios | wᵢᵘˢᵉʳ (importancia) | ¿Qué tan importante es para tu experiencia? | 1 a 10 |
| Stakeholders (opcional) | Lᵢᵉˣᵖᵉᶜᵗᵉᵈ | ¿A qué nivel debería llegar? | L1 a L5 |
| Stakeholders (opcional) | wᵢˢᵗᵃᵏᵉʰᵒˡᵈᵉʳ | ¿Qué tan crítico es para el éxito estratégico? | 1 (bajo) a 10 (crítico) |

Los datos también pueden salir de documentación de arquitectura o
especificaciones técnicas en vez de encuestas.[^caie]

# Etapa 1, evaluación por rasgo y por zona (sección 6.2, pp. 39-41)

1. **Puntaje normalizado del rasgo**: fᵢ = Pᵢ · Vᵢ / Vmax, con Vmax típicamente 10.
   Un rasgo no implementado aporta 0 sin importar la opinión del usuario.[^caie]
2. **Peso por importancia**: wᵢ = promedio de las calificaciones de importancia de
   los k usuarios.[^caie]
3. **Puntaje de la zona**: S = Σ wᵢ · fᵢ sobre los rasgos de la zona.[^caie]
4. **Zoned Unified Composite Score**: ZUCSᵢ = Sᵢ / wᵢ_max, normaliza cada zona.[^caie]
5. **System-Zoned Unified Composite Score**: SZUCS, promedio ponderado de los
   ZUCS de las seis zonas (ecuaciones 4 a 6). Es el indicador único para
   benchmark entre sistemas.[^caie]

El perfil Z = {F_A, F_B, F_C, F_D, F_E, F_F} es el "perfil cognitivo" del
sistema.[^caie]

Nota de lectura: la ecuación 6 del texto extraído es ambigua; el paper define
wᵢ_max sin detallarlo más (probablemente el peso máximo posible de la zona).
Para usar el SZUCS en una slide, confirmar la fórmula contra el PDF original
antes de reproducirla.

# Etapa 2, análisis estructural y de brechas (sección 6.3, pp. 41-43)

* **Brecha por rasgo**: Δlᵢ = Lᵢᵉˣᵖᵉᶜᵗᵉᵈ − Lᵢˢʸˢᵗᵉᵐ.[^caie]

| Δlᵢ | Lectura |
|---|---|
| < 0 | El rasgo se activó antes de que se cumplieran sus prerrequisitos |
| = 0 | La madurez coincide con lo esperado |
| > 0 | El rasgo está subdesarrollado respecto de la meta |

* **Brecha por zona**: g = Σ Δlᵢ / |F_j|, promedio de la zona.[^caie]
* **Visualización prevista**: mapas de calor, modelos de terreno 3D y matrices
  de dependencias; el paper dice que se desarrollarán en trabajo futuro.[^caie]
* **Superficie de madurez estructural (SMS)**: grafica cada rasgo contra su nivel,
  su brecha y su peso. Marcadores:[^caie]

| Marcador | Condición |
|---|---|
| Mínimos locales (rasgos críticos subdesarrollados) | Δl > 0, nivel ≤ 2 y peso alto |
| Máximos globales (fortalezas estratégicas) | nivel ≥ 4 y peso > 6 |
| Activaciones prematuras | Fᵢ depende de Fⱼ pero el nivel de i es mayor que el de j |
| Rasgos clave ausentes | Pᵢ = 0 y peso > 6 |

* **Aplicación estratégica**: priorizar los rasgos con mayor Δlᵢ · wᵢ,
  secuenciar el roadmap con lógica "fundaciones primero", alinear la inversión
  con las zonas de mayor retorno cognitivo y validar o ajustar las metas.[^caie]

# Alcance de cada etapa

* La Etapa 1 sola alcanza para comparar sistemas sin definir expectativas
  universales; la Etapa 2 sirve para planificar un sistema específico.[^caie]
* La Etapa 1 se apoya en teoría cognitiva establecida; la Etapa 2 se presenta
  explícitamente como modelo prospectivo, sin validación empírica todavía.[^caie]
* Si faltan los valores esperados, la Etapa 2 se puede usar en forma parcial, y
  la Matriz de Philipp puede aportar niveles esperados de referencia.[^caie]

# Diseño de la encuesta del piloto (sección 2.2, p. 5)

Cada rasgo se midió con tres ejes: estado de implementación (binario),
desempeño percibido (1 a 10) e importancia (1 a 10). Ver
[caso y limitaciones](/frameworks/caie-caso-limitaciones.md).[^caie]

[^caie]: Putnoki y Orosz (2026), *Cognitive and artificial intelligence evaluation framework*, Artif Intell Rev 59:98. Páginas según la numeración impresa.
