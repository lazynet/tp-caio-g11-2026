---
name: board-review
description: Revisión del plan CAIO desde las miradas de rol y del board. Focalizada (una sección o anexo en borrador, con un revisor pertinente) o integral (cuatro miradas más consolidación del board, antes del peer review y de la entrega). Usalo cuando pidan una revisión del board, una pre-revisión o poner a prueba slides o anexos.
---

# board-review

Uso: `<objetivo> [--rol architect|governance|people|finance|board] [--integral] [--chat]`.

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
  preguntá. Integral: sin argumento es `plan/` y `defense/`, y lo decís. Si el
  pedido limita el alcance, respetalo y marcá lo que queda fuera de evaluación.
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

  Conservá la captura completa en variables del runtime cuando sea posible,
  sin volcarla entera a la conversación. Cada revisor recibe el mismo manifiesto
  de versión y solo los archivos necesarios para su mirada, siempre extraídos
  de esa captura. Con `--chat` o sin escritura, el paquete vive en memoria: ni
  diff ni copias en archivos temporales.
- **Criterios:** la consigna del TIF tal como la resume `.claude/agents/board.md`
  (no un framework de la cursada), la mirada del rol y la rúbrica del Corrector
  IA (`material/frameworks/rubrica-corrector-caio.md`) para puntuar C1 a C7. Una cifra se acepta solo
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

Cada revisor recibe **solo**: las instrucciones del rol y las reglas aplicables
de `AGENTS.md`, el objetivo y su versión, las fuentes pertinentes
(fichas de `context/`, `material/` o `defense/evidence/` que el objetivo cita) y
los criterios. No le pases la justificación del autor, el historial de la
conversación ni los hallazgos de otro revisor: la independencia es un criterio
de esta revisión. Solo `board` en la integral recibe los reportes de los otros
cuatro, y nada más que eso además del objetivo.

Si tu herramienta no puede aislar el contexto (por ejemplo, corrés vos mismo
las miradas), no lo finjas: en el reporte escribí "sin aislamiento de contexto".
Usá una sesión nueva o el equivalente a `fork_turns: none`; una copia de la
conversación del autor no es una revisión independiente. Si el paquete no cabe,
dividí por secciones conservando el manifiesto y declarando las omisiones; no
dejes que un truncamiento silencioso se convierta en un aprobado.

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
   El orquestador lanza las tandas; no dependas de que cada revisor pueda delegar.

## 4. Cada revisor devuelve

Brechas, contradicciones con otras secciones y afirmaciones sin fuente, cada una
con **ubicación** (archivo y slide, sección o línea), **severidad**
(crítica / alta / media / baja), **agente dueño** y **condición de cierre**. Si
no pudo leer algo (archivo ausente, fuente sin acceso), lo reporta aparte como
**limitación de acceso**, no como deficiencia del contenido.

## 4b. Nota orientativa

Solo en la integral, con los siete criterios evaluables y la revisión completa.
Los revisores no la calculan: `board` no ejecuta código. El orquestador toma los
niveles que devolvió `board` y corre:

```bash
python3 -c 'import sys; w=[20,20,15,15,10,10,10]; n=[int(x) for x in sys.argv[1:]]; assert len(n)==7 and all(0<=x<=4 for x in n); s=sum(a*b for a,b in zip(w,n)); assert abs(s/40-s/100*2.5)<1e-9; print(f"S={s} nota={s/40:.1f}/10")' <C1> <C2> <C3> <C4> <C5> <C6> <C7>
```

Con algún NE o una revisión parcial no hay nota: se informa la cobertura (suma
de pesos evaluados sobre 100). Nunca renormalices los pesos.

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

El reporte (guardado o en chat) lleva: SHA base, status y manifiesto de paths y
sha256 de la captura; resumen del diff y de los archivos nuevos (el contenido
completo queda en el paquete, no se repite en cada reporte); criterios usados;
modo, tandas y si hubo
aislamiento o ejecución secuencial; veredicto por sombrero del board (integral o
`board`); tabla de la rúbrica (criterio, peso, nivel o NE, evidencia) y la salida
del cálculo de la nota, o el motivo por el que no se emite; hallazgos ordenados por severidad con ubicación, dueño y condición de
cierre; limitaciones de acceso en sección aparte; y las 5 preguntas más difíciles
para `defense/objeciones.md` a través de `caio`.

## 6. Devolvé al usuario

El veredicto por sombrero (si corrió `board`), los niveles C1 a C7 y la nota
calculada (o el motivo para no emitirla), los 5 hallazgos principales con
su agente dueño, las limitaciones de acceso y el path de la revisión, o "sin
archivo (modo chat)".
