---
type: Concepto
title: "Scorecard de seguridad de IA para el directorio"
description: "Los diez controles con madurez de 0 a 3 y los tres indicadores que, según la Clase 9, el CAIO le lleva al directorio."
tags: [m3, seguridad, gobierno, metricas]
sources:
  - id: clase9
    resource: "Hoy atacamos · CAIO Clase 9.pdf"
    title: "Hoy atacamos, CAIO Clase 9, láminas 10, 14 y 15"
status: accepted
accepted:
  by: human:lazynet
  at: 2026-10-21
  scope: "Aceptación documental por instrucción expresa de Martín en esta sesión, incorporación al corpus del TP tras aceptar presentaciones oficiales como material suficiente para cerrar #22; no acredita por sí sola cotejo primario ni verificación normativa. Se acepta la inclusión de esta ficha y sus referencias a U9 o «Hoy atacamos», cuyos originales no fueron localizados; no se afirma su localización ni se verifica su contenido."
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T14:30:00Z }
---

# Qué es

"Lo que el CAIO le lleva al directorio" (lámina 14): un scorecard de diez controles,
cada uno con madurez de 0 a 3, y tres indicadores. La lámina aclara que sus valores
son "datos de ejemplo".[^clase9]

# Escala de madurez

La lámina usa cuatro rótulos: 0 · Ausente, 1 · Inicial, 2 · Definido y
3 · Medido.[^clase9] No define cada nivel.

# Diez controles

| # | Control |
|---|---|
| 1 | Inventario de agentes y permisos |
| 2 | [Regla de dos de tres](/conceptos/m3u1-regla-dos-de-tres.md) |
| 3 | Aprobación humana en acciones críticas |
| 4 | Detección de instrucciones sospechosas |
| 5 | [Política de datos por destino](/conceptos/m3u1-fugas-y-destinos-de-datos.md) |
| 6 | Gestión de secretos |
| 7 | Separación de canales |
| 8 | Red teaming con tasa de éxito |
| 9 | Pruebas de regresión |
| 10 | Controles de aplicación clásicos |

Fuente: lámina 14.[^clase9] Los niveles que muestra la lámina para cada control son
de ejemplo y no se transcriben.

# Tres indicadores

| Indicador | Cómo se lee |
|---|---|
| Tasa de éxito de ataque | Porcentaje de esta ronda contra la anterior |
| Agentes con A+B+C sin humano | Cantidad; meta: 0 |
| Hallazgo crítico más viejo | Días abierto |

Fuente: lámina 14.[^clase9] La tasa de éxito se mide corriendo el mismo ataque
muchas veces (20 en el ejemplo de la lámina 10), no con un solo intento.[^clase9]

El cierre de la clase (lámina 15) le pone ritmo: qué lee el agente, qué puede hacer y
quién aprueba, "medido todos los meses".[^clase9]

# Relación con otras fichas

El [apunte del 2026-10-06](/apuntes/2026-10-06-seguridad-agentes.md) registra cinco
dimensiones de este scorecard, a partir de notas de clase; la lámina trae los diez
controles. Para el gobierno del plan, conecta con el
[Council](/conceptos/m1u4-council-vs-coe.md) y su revisión periódica. Lectura de
esta ficha, no del curso.

# Cautelas

* La aceptación cubre la inclusión de la ficha en el corpus. Los originales de U9
  y «Hoy atacamos» no fueron localizados en la búsqueda local; las referencias a
  cotejos del agente son antecedentes de elaboración, sin verificación humana.

* Ficha aceptada para el corpus, sin verificación humana del contenido. Cotejo del agente contra la
  lámina 14 (leída como imagen) y las láminas 10 y 15, el 2026-10-21.
* Los niveles de madurez y los valores de los indicadores de la lámina son de
  ejemplo: no describen a ninguna organización y no van a una slide como dato.

[^clase9]: Hoy atacamos, CAIO Clase 9, láminas 10, 14 y 15
