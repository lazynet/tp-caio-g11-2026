# Revisión focalizada del board — roadmap tridimensional (PR #32)

Fecha: 2026-10-20. Modo: **focalizada**, una sola mirada (`board`, con sus tres
sombreros), sin tandas. La corrió un agente en sesión nueva que adoptó el rol
`board`; no recibió la justificación del autor ni el historial de #32, pero no es
un subagente aislado: **sin aislamiento de contexto formal**. Revisión de
borrador: las cifras trazables a fichas `draft` se discuten como supuestos de
borrador, no se aprueban para entrega.

El skill `board-review` dice "no commitees la revisión"; el pedido de la sesión
orquestadora (issue #20) autoriza guardar este archivo, commitearlo y abrir PR.

## Objetivo y versión

- **Objetivo:** slides 7, 8 y 9 de `plan/slides.md` (numeración por página del
  render; sus eyebrows dicen 06, 07 y 08), `plan/annexes/06-roadmap-riesgo.md`
  completo y las objeciones 37-44 de `defense/objeciones.md`.
- **Fuera de evaluación:** slides 1-6 y 10, los Anexos A-E salvo como fuente de
  contraste, las objeciones 1-36 y 45, y `defense/storyline.md` (también tocado
  por #32).
- **SHA base:** `4c9c26431bb736180d8195a059f3c424343d3aa2`, rama `docs/board-f`.
  `git status --short -- plan defense`: limpio.

| Archivo | Rol en la revisión | sha256 |
|---|---|---|
| `plan/slides.md` | Revisado (slides 7-9) | `b46a1cddc1c7b8600c9da59eeb4dec861ac27115147b76d82063152d87cb517f` |
| `plan/annexes/06-roadmap-riesgo.md` | Revisado | `8e259cc0bfdbce3fbae024cc03c53d9acb0210544b9734d98a58f6b04dd94be0` |
| `defense/objeciones.md` | Revisado (37-44) | `934e09fdc96dc4dd53ccaeb04895933fd18f07e13cf91c0251ede64455b43faa` |
| `plan/annexes/05-business-case.md` | Fuente de contraste | `f283ef4305923f14c2db1dc96927628efe233c53d9cc1c4e19f88424ba996ab8` |
| `plan/annexes/04-personas-cultura.md` | Fuente de contraste | `f9eeb764acb4bf433300fda4a363bdb6f9a8c3c69e22c60686fae1a758bb9353` |
| `context/supuestos/paquete-minimo-de-aprendizaje.md` | Fuente (`Supuesto`, `draft`) | `1e3aa300db9979b4faafc5c2c6af84c2778d86367bc08955d1538f99db4428b5` |
| `context/hechos/costos-tecnologia-e-ia.md` | Fuente (`Hecho`, `draft`) | `55ac8edf6d282f18e404b804959c3e3e4f3ac3c4a16a2f59852597ec443bfa37` |
| `material/conceptos/m3u4-roadmap-tridimensional.md` | Fuente (`draft`) | `68cae0ee9c482e77f46191d0977541968d7b619f1a139ba842da1aa69cb7cb8c` |
| `material/conceptos/m3u4-estrategia-12-meses.md` | Fuente (`draft`) | `e911b6712da162f71fc2d7e948a86490639d0bb6ee9a2fc6d028f54a37a474ae` |
| `material/conceptos/m3u4-financial-storytelling.md` | Fuente (`draft`) | `ebd4d4971cf24b2f1ed9684af9ab8aacd84063256fff988bfc67de78034f55bd` |
| `material/conceptos/m3u4-capstone-panel-ejecutivo.md` | Fuente (`draft`) | `166af3ea54423ffb37c290d5dba04909b81d8835c75aae68afc687b884aee1f7` |

**Criterios:** la consigna del TIF tal como la resume `.claude/agents/board.md`
y las reglas de `AGENTS.md` ("todo número tiene fuente", "los totales se
recalculan"). Las cuatro fichas `m3u4-*` que sostienen la estructura de F
(F:244, F:314, F:461) y el bloque de panel ejecutivo de las objeciones
(`objeciones.md:78-80`) están en `draft`: son conceptos del curso sin cifras, así
que lo pendiente es verificación humana contra el PDF de la unidad, no un número.

## Recálculos

| Total | Componentes | Recalculado | Declarado | Estado |
|---|---|---|---|---|
| Demanda M1-M3, mínimo | 146+44+48+8+34+64+60+26+360+180 (ficha, tabla de horas) | 970 h | 970 h | Cierra |
| Demanda M1-M3, máximo | 276+72+72+16+54+64+96+40+420+240 | 1.350 h | 1.350 h | Cierra |
| Clave / distribuida | 8 primeras filas: 430-690; básico+intermedio: 540-660 | 0,8958-1,4375 / 1,125-1,375 FTE a 480 h | F:80 | Cierra |
| Reserva de capacidad | 720 + 660 | 1.380 h; margen 720−690 = 30 h | Slide 7, F:84-93 | Cierra |
| Segunda liberación | caja 9+1 = 10; tiempo 59+2 = 61 | 71 | Slide 8 y 10, F:96 | Cierra |
| Acumulado hasta cerrar M3 | caja 10 + tiempo (59+3+5+2 = 69) | 79 | Slides 8-10, F:97 | Cierra |
| Salida M3 en el año | 79 + núcleo 6 (108 h, 2 por tramo × 3) | 85 | Slide 9, F:393 | Cierra |
| Salida M6 | caja 10+2 = 12; tiempo 69+14 = 83 → 95; +2 tramos de núcleo (4) | 95 / 99 | Slide 9, F:394 | Cierra |
| Espera M6 | 12+1 / 83+6 → 102; +~1,5 tramos de núcleo (3) | 102 / 105 | Slide 9, F:395; E:1329 | Cierra (prorrateo de E) |
| Salida M9 | 12+2 / 83+11 → 108; +1 tramo (2) | 108 / 110 | Slide 9, F:396 | Cierra |
| Espera M9 | 14+1 / 94+6 → 115; +~0,5 tramo (1) | 115 / 116 | Slide 8 nota, F:397; E:1330 | Cierra (prorrateo de E) |
| Año completo | caja 16 / tiempo 105 | 121 | Slide 9, F:398 | Cierra |

La aritmética del deck y de F es consistente. Los hallazgos de abajo no son de
suma: son de qué se muestra como condición, qué se omite y qué se afirma sin
costeo.

## Revisión visual (render)

`scripts/build-deck.sh html` y export PNG con la misma versión de Marp
(`@marp-team/marp-cli@4.1.2`) y el tema `plan/theme`. Lo que vi en las páginas
7-9:

- **Página 7 (Personas):** sin desborde. La tarjeta izquierda ("Reserva propuesta
  para los meses 1-3") ocupa media altura con más de la mitad vacía debajo de la
  nota; la columna derecha carga cuatro viñetas largas, la de metas con cinco
  renglones. Espacio mal repartido, no roto.
- **Página 8 (Roadmap):** sin desborde. Tabla de 5 filas × 4 tramos legible; la
  nota al pie va en cuerpo chico, tres renglones densos, pegada a la barra de
  decisión. Ahí vive información de decisión (esperas, extensión de base).
- **Página 9 (Costo y riesgo):** sin desborde. Tabla de salidas y cuatro
  tarjetas legibles; queda una franja vacía entre los chips de irreversibles y
  la barra de decisión.

## Veredicto por sombrero

- **Miembro del board: aprobado con cambios.** La decisión que se pide es clara
  (8 primero, hasta 71 después, 79 acumulado) y el "qué pasa si decimos que no"
  está. Pero la fila "Pasa si" de la página 8 promete condiciones de pase que F
  no aplica así (H1).
- **CFO escéptico: aprobado con cambios.** La plata, el techo y cómo se frena
  cierran. Lo que no cierra: el único costo de no actuar monetizado del plan
  (211-267 al año a 12×) se presenta como "sin montos" (H3); el "79 máximo" tiene
  dos salidas de caja no contadas (H4); y el upside si los gates pasan no aparece
  en ninguna forma (H5).
- **Corrector de la cursada: aprobado con cambios.** Hay roadmap en tres
  dimensiones con hitos, gates, contingencias, escenarios de salida e
  irreversibles. Faltan criterios de éxito financieros en la slide (H2), la
  dimensión de gobierno se funde en "Técnico" (H6) y los escenarios son solo de
  pérdida (H5).

## Hallazgos

Todos tienen dueño `caio` (único editor de `plan/slides.md`, dueño de F y de
`defense/`); donde la fuente es de otro anexo, se nombra el dueño a consultar.

### H1 — Alta. "Pasa si" de la página 8 no es la regla de F

- **Ubicación:** `plan/slides.md:259`; contraste con F:344 y F:350.
- **Evidencia:** la slide pone "Tec. ≥80%" como condición de pase del mes 6 y
  "Tec. ≥85%; Op. habilitadas ≥60%" como pase del mes 12. En F, la adopción del
  mes 6 solo define el destino de las horas de formación M7-M9 (≥60% y <80% es
  "mantenimiento"; <60% "suspensión" de formación), y la del mes 12 no corta
  nada: "Se informa contra el OKR". El pase que libera M7-M9 es el throughput.
- **Por qué importa:** el board va a preguntar "throughput pasa y adopción da
  70%: seguimos o no?". La slide dice que no pasa; F dice que el frente sigue.
  Una de las dos está mal, y es la que el board lee.
- **Condición de cierre:** la fila separa "libera fondos" (throughput y calidad,
  controles, base) de "se informa" (adopción), o F convierte la adopción en
  condición de pase con su consecuencia. No las dos versiones a la vez.

### H2 — Media. La dimensión financiera de la página 8 no tiene criterio de éxito

- **Ubicación:** `plan/slides.md:258-259`; F:341, F:351, F:318-323.
- **Evidencia:** el eyebrow dice "Roadmap técnico, financiero y cultural", pero la
  fila financiera solo lista techos. Los criterios financieros de F no llegan a
  la slide: "consumo dentro de los techos" (mes 3), "costo por PR aceptado que no
  sube" (mes 9) y "trayectoria al equilibrio o interés contractual" (mes 12, el
  único criterio que decide el año 2).
- **Condición de cierre:** cada tramo de la slide muestra al menos un criterio
  financiero de pase, o la nota dice explícitamente dónde está.

### H3 — Media. Costo de no actuar: "sin montos", pero el plan sí tiene uno

- **Ubicación:** `plan/slides.md:300`; `defense/objeciones.md:87` (objeción 38);
  F:419; E:436-441.
- **Evidencia:** la slide y la objeción 38 dicen que el costo de no actuar va
  "sin montos". E y F cuantifican la exposición a consumo: a 12×, 211-267 al año
  de incremental, "del orden de toda la caja del plan" (E:438) y mayor que el
  techo anual de 121. Ese número cuelga de `context/hechos/costos-tecnologia-e-ia.md`
  (~12×, telemetría, no factura), ficha `Hecho` en `draft`.
- **Por qué importa:** el CFO va a encontrar el número en E y preguntar por qué
  la exposición más grande del plan, que el mínimo no cubre, no está en la slide
  de riesgo. Además, E dice que es exposición "con o sin plan"; listarla bajo
  "si no actuamos" la confunde con un costo evitable.
- **Condición de cierre:** la slide y la objeción 38 dicen qué se cuantificó
  (exposición de consumo, rango, con o sin plan) y qué no (clientes y uso sin
  regla, sin probabilidad), o justifican por qué ese rango no va. Pendiente de
  verificación humana de la ficha de costos (dueño: `finance`).

### H4 — Media. El "máximo 79" tiene salidas de caja no contadas

- **Ubicación:** `plan/slides.md:238`, `:313`; F:420, F:239, F:554;
  `plan/annexes/04-personas-cultura.md:233`.
- **Evidencia:** (a) la excepción externa de facilitación (16-32 h) es pago
  externo, pero la caja M1-M3 es "sin contractor" (F:75) y su precio "requiere
  cotización" (F:420): si se activa, el 79 deja de ser máximo. (b) El mapeo del
  rol crítico va en M1-M3 (F:239) sin horas propias; D:233 supone que "lo absorbe
  el 20% del líder ya computado", cuando el margen de la reserva clave es 30 h
  (F:91) con utilización 83-90%.
- **Condición de cierre:** la página 9 o su nota dice que la excepción externa
  se suma al 79 y con qué tope, y el mapeo tiene horas estimadas dentro de las
  146-276 h del líder o se pasa a M4-M6. Consultar a `finance` y `people`.

### H5 — Media. No hay escenario de éxito: el CFO no ve qué compra si sale bien

- **Ubicación:** página 9 (`plan/slides.md:278-319`); F:390-399, F:460-461.
- **Evidencia:** la tabla de la página 9 y los escenarios de F son solo puntos de
  salida con pérdida máxima. F decide no mostrar equilibrio ni ROI (F:460-461) y
  lo justifica bien (beneficio de caja 0). Pero tampoco muestra qué representa
  pasar los gates: F:60 dice que el throughput "se valúa como horas evitadas a
  output fijo", y ese valor nunca aparece, ni como rango ni como orden de
  magnitud de horas.
- **Por qué importa:** la consigna pide escenarios y financial storytelling para
  un CFO escéptico; el material del curso (`m3u4-financial-storytelling`, draft)
  pide caso de negocio. "ROI −100%" en rojo sin un "si pasa +8%, equivale a X
  horas" deja al board con una sola cara de la moneda. El corrector puede leerlo
  como escenarios incompletos.
- **Condición de cierre:** un escenario "pasan los gates" con la capacidad
  liberada en horas (no caja), marcada como supuesto, o una línea explícita en
  la slide de por qué no se muestra.

### H6 — Media/baja. Gobierno desaparece del roadmap de la slide

- **Ubicación:** `plan/slides.md:254-260`; F:236-242, F:244-247.
- **Evidencia:** F tiene columna "Gobierno y seguridad" y dice que los
  principios éticos del roadmap tridimensional "viven acá en la columna de
  gobierno". La slide la funde en "Técnico" ("Base, política, controles…"). En
  M4-M12, lo de gobierno de F (residuales con vencimiento, cláusula tipo,
  revisión de residuales) no aparece.
- **Condición de cierre:** la slide nombra gobierno en alguna fila, o la nota
  remite a la columna de F.

### H7 — Media/baja. Esperas presentadas como regla cuando una es propuesta

- **Ubicación:** `plan/slides.md:262`; F:347, F:397.
- **Evidencia:** la slide dice "Las esperas de los meses 6 y 9 duran 6 semanas";
  F marca la espera del mes 9 como "propuesta a ratificar". La página 9 repite
  "115 en el 9" sin la marca.
- **Condición de cierre:** la slide marca la espera del mes 9 como propuesta, o
  F la adopta.

### H8 — Baja. F declara que la tabla de familias "no agrega umbrales", y agrega

- **Ubicación:** F:316, F:321-322, F:555-556.
- **Evidencia:** la tabla de familias de indicadores trae "Operaciones
  habilitadas ≥40%" (mes 6), "Tecnología ≥80% sostenido", "pedidos con ejemplos
  ≥30%" y "costo por PR aceptado que no sube" (mes 9). Vienen del Anexo D
  (D:566-567), pero no están en la tabla de gates de F (F:332-351). F:316 dice
  que "las condiciones de la tabla ya las cubren" y la cautela F:555-556 dice que
  no agrega umbrales.
- **Condición de cierre:** o se suman a los gates con su consecuencia, o la tabla
  dice que son métricas de seguimiento de D sin efecto en fondos.

### H9 — Baja. Referencias de F a las slides con títulos viejos

- **Ubicación:** F:9-12.
- **Evidencia:** "Slide 8 — Roadmap a doce meses", "Slide 9 — Compromiso,
  pérdida y escenarios", "Slide 3 — Beneficio principal y captura", "Slide 10 —
  Resolución propuesta" no son los títulos actuales. F numera por página (slide
  8 = eyebrow "07 · Roadmap"); el deck numera los eyebrows desde la primera
  slide de contenido. En la defensa, "slide 7" va a significar dos cosas.
- **Condición de cierre:** títulos actualizados y una sola convención de número.

### H10 — Baja. La objeción 44 no responde lo que pregunta

- **Ubicación:** `defense/objeciones.md:93`.
- **Evidencia:** pregunta "si se atrasa la formación"; la respuesta habla de
  base congelada, cohorte activa y horas liberadas. Lo que pasa si la formación
  se atrasa está en F:339 (básico <90% al mes 3: rediseño; <50%: cambio de
  formato) y no se cita.
- **Condición de cierre:** la respuesta empieza por la regla del básico en el
  mes 3 y después la cadena de dependencias.

### H11 — Baja. Página 7: espacio vacío y metas comprimidas

- **Ubicación:** `plan/slides.md:217-234` (render, página 7).
- **Evidencia:** ver "Revisión visual". La meta intermedia de Operaciones (≥40%
  en el mes 6, D:566) no aparece, mientras la explicación del 72,5% ocupa cinco
  renglones.
- **Condición de cierre:** decisión de diseño de `caio`; no bloquea.

## Checklist de la consigna (solo lo que toca esta sección)

| Ítem | Estado | Comentario |
|---|---|---|
| Roadmap técnico con hitos y criterios de éxito | Cumple | Página 8 y F:236-242 |
| Roadmap cultural con hitos y criterios de éxito | Cumple con cambios | Criterios mezclados con pase (H1) |
| Roadmap financiero con hitos y criterios de éxito | No cumple en la slide | Solo techos (H2); en F sí |
| Escenarios | Cumple parcial | Solo de salida y pérdida (H5) |
| Contingencias | Cumple | F:412-429 |
| Decisiones reversibles e irreversibles | Cumple | Página 9 y catálogo F:494-521 |
| Storytelling para el CFO | Cumple con cambios | Sin upside (H5); costo de no actuar (H3) |
| Preparación de la defensa | Cumple con cambios | Objeciones 37-44 presentes; 38 y 44 a corregir |
| Gobierno en el roadmap integral | Cumple en F, no en la slide | H6 |
| Máximo de 10 slides | Cumple | `plan-check`: 10 slides |

## Limitaciones de acceso

- No leí los PDFs de M3U4: las fichas `m3u4-*` están en `draft` y no pude
  contrastarlas contra la fuente.
- No hay fuentes internas en este worktree (`private/` no se usó). Ninguna cifra
  revisada tiene ficha `verified`; todas son supuestos de borrador.
- No revisé `defense/storyline.md`, que #32 también tocó.

## Las 5 preguntas más difíciles (para `defense/objeciones.md`, vía `caio`)

1. "Si el throughput pasa en el mes 6 pero Tecnología da 70% de adopción, el
   tramo siguiente se libera o no? Su slide dice una cosa y su anexo otra."
2. "Su propio anexo dice que el consumo a 12× nos expone a 211-267 mil por año,
   más que todo el plan. Por qué la slide de riesgo dice 'sin montos', y qué hace
   el plan por esa exposición en estos doce meses?"
3. "Me piden aceptar 79 de pérdida máxima. Si la facilitación tiene que ser
   externa, cuánto pasa a ser? Quién firma ese exceso?"
4. "Si todo sale bien y pasan los cuatro gates, qué tengo en la mano en
   diciembre de 2027, en horas o en algo que pueda contar?"
5. "El estudio del rol crítico arranca en M1-M3 con horas que no están en el
   costeo y antes de que el Directorio decida la postura sobre el empleo. Qué
   pasa si el equipo lo lee como un recorte?"
