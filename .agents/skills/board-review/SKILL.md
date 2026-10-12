---
name: board-review
description: Revisión del plan CAIO desde las miradas de rol y del board. Focalizada (una sección o anexo en borrador, con un revisor pertinente) o integral (cuatro miradas más consolidación del board, antes del peer review y de la entrega). Usalo cuando pidan una revisión del board, una pre-revisión o poner a prueba slides o anexos.
argument-hint: "<objetivo> [--rol architect|governance|people|finance|board] [--integral] [--chat]"
---

# board-review

Dos modos. Elegí el más chico que sirva: el borrador de una sección no necesita
cinco revisiones antes del feedback humano (ver "Revisiones proporcionales" en
`AGENTS.md`).

| Modo | Cuándo | Revisores |
|---|---|---|
| **Focalizada** (default) | Borrador de una sección o anexo | Un revisor pertinente: el rol dueño de esa mirada, o `board` si la duda es contra la consigna |
| **Integral** (`--integral`) | Antes del peer review y de la entrega | `architect`, `governance`, `people` y `finance`, y después `board` consolida |

## 1. Fijá objetivo y versión

Antes de lanzar a nadie, dejá por escrito:

- **Objetivo:** paths exactos. Focalizada: el argumento es obligatorio; si falta,
  preguntá. Integral: sin argumento es `plan/`, y lo decís.
- **Versión (captura inmutable):** los revisores leen una copia capturada, nunca
  paths vivos que otro revisor o el equipo pueda tocar. Capturá en memoria:
  1. SHA base (`git rev-parse HEAD`) y `git status --short -- <objetivo>`.
  2. Tracked: `git diff HEAD -- <objetivo>` completo (junta staged y unstaged,
     también con staging parcial; un `git diff` sin `HEAD` pierde lo staged).
  3. Nuevos sin trackear: `git ls-files --others --exclude-standard -- <objetivo>`
     y, por cada uno, los bytes completos y su sha256. Un hash solo no reconstruye
     el texto.
  4. Los bytes completos de cada archivo revisado (tracked y nuevo) y de las
     fuentes que cita, cada uno con su sha256.
  5. Verificación: repetí `git status` y los hashes. Si algo cambió durante la
     captura, descartá el paquete y reintentá; no revises una mezcla de versiones.

  Todo revisor recibe exactamente ese paquete. Con `--chat` o sin escritura, el
  paquete vive en memoria: ni diff ni copias en archivos temporales.
- **Criterios:** la consigna del TIF tal como la resume `.claude/agents/board.md`
  (no un framework de la cursada) y la mirada del rol. Una cifra se acepta solo
  si remonta a una ficha `verified` con bloque `verified:`. Distinguí dos
  niveles:
  - **Focalizada sobre un borrador:** una cifra trazable a una ficha `draft` o a
    un supuesto marcado se discute como **supuesto de borrador**; el revisor
    nombra la verificación pendiente. Eso no la aprueba para entrega.
  - **Integral (peer review y entrega):** exige ficha `verified` con el bloque
    `verified:` que pide `AGENTS.md`; que el texto sea consistente consigo mismo
    no la aprueba.
- **Evaluable:** si el objetivo es un setup o un esqueleto provisional (por
  ejemplo, títulos de `plan/slides.md` sin contenido ni acuerdo del equipo),
  no lo revises como si fuera un plan. Devolvé "no evaluable" con lo que falta.

## 2. Armá el paquete de cada revisor

Cada revisor recibe **solo**: el objetivo y su versión, las fuentes pertinentes
(fichas de `context/`, `material/` o `defense/evidence/` que el objetivo cita) y
los criterios. No le pases la justificación del autor, el historial de la
conversación ni los hallazgos de otro revisor: la independencia es un criterio
de esta revisión. Solo `board` en la integral recibe los reportes de los otros
cuatro, y nada más que eso además del objetivo.

Si tu herramienta no puede aislar el contexto (por ejemplo, corrés vos mismo
las miradas), no lo finjas: en el reporte escribí "sin aislamiento de contexto".

## 3. Planificá las tandas

1. Averiguá cuántos subagentes concurrentes permite el runtime. Tu sesión
   consume un slot: tandas de `slots - 1`.
2. Integral con 4 o más slots libres (ya descontado el tuyo): los cuatro roles en una tanda, después
   `board`. Con menos (1 a 3): tandas parciales en ese orden fijo (`architect`,
   `governance`, `people`, `finance`), y `board` siempre al final.
3. Si no hay slots libres o no podés saberlo, corré las miradas en **secuencia**,
   una por vez, sin mezclar hallazgos entre ellas, y marcá el reporte como
   "ejecución secuencial".
4. Lanzá solo tipos de agente que existan en tu herramienta. Si no podés elegir
   el tipo (por ejemplo, Codex), lanzá un subagente genérico y pasale como
   instrucciones el contenido de `.claude/agents/<rol>.md`; si no podés lanzar
   subagentes, adoptá el rol vos mismo. No inventes nombres de agente ni corras
   comandos slash.
5. Al trasladar un rol, respetá las herramientas reales: los revisores no
   editan nada; `board` solo escribe en `reviews/` y solo si la sección 5 lo permite.

## 4. Cada revisor devuelve

Brechas, contradicciones con otras secciones y afirmaciones sin fuente, cada una
con **ubicación** (archivo y slide, sección o línea), **severidad**
(crítica / alta / media / baja), **agente dueño** y **condición de cierre**. Si
no pudo leer algo (archivo ausente, fuente sin acceso), lo reporta aparte como
**limitación de acceso**, no como deficiencia del contenido.

## 5. Salida

- **`--chat`** (o la herramienta sin escritura): devolvé la revisión en la
  conversación y no escribas ningún archivo. Si lanzás `board`, pedile que
  responda en texto y no use `Write`.
- **Guardado:** `reviews/AAAA-MM-DD-<objetivo>.md`, solo si el pedido lo
  autoriza. Si hay duda, modo chat y ofrecé guardar. Cualquier prohibición de
  escritura del usuario prevalece sobre este skill y sobre el contrato de `board`.
- No commitees la revisión: eso lo decide el equipo.
- **Datos privados:** nunca se copian a `reviews/` ni se publican; el reporte
  los anonimiza (ver "Datos privados" en `AGENTS.md`). Un snapshot crudo con
  datos privados, si el usuario autoriza conservarlo, va solo en `private/`.

El reporte (guardado o en chat) lleva: SHA base, status, `git diff HEAD` del
objetivo y lista de archivos nuevos con su sha256 (y su contenido, salvo que
sea dato privado); paths revisados; criterios usados; modo, tandas y si hubo
aislamiento o ejecución secuencial; veredicto por sombrero del board (integral o
`board`); hallazgos ordenados por severidad con ubicación, dueño y condición de
cierre; limitaciones de acceso en sección aparte; y las 5 preguntas más difíciles
para `defense/objections.md`.

## 6. Devolvé al usuario

El veredicto por sombrero (si corrió `board`), los 5 hallazgos principales con
su agente dueño, las limitaciones de acceso y el path de la revisión, o "sin
archivo (modo chat)".
