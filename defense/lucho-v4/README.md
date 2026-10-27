# Alternativa ejecutiva V4 de Lucho

Propuesta para revisar con el equipo, vinculada con [#27](https://github.com/lazynet/tp-caio-g11-2026/issues/27) y [#21](https://github.com/lazynet/tp-caio-g11-2026/issues/21). Mantiene el alcance del plan y presenta su argumento en diez diapositivas. No reemplaza el deck canónico de `plan/slides.md` ni modifica los anexos.

## Abrir la propuesta

- [PDF integrado: presentación, anexos completos, defensa, speech y reporte del board](https://github.com/lazynet/tp-caio-g11-2026/releases/download/defensa-lucho-v4-20261027/defensa-lucho-v4-integrado.pdf).
- [Descarga y alcance de esta versión](https://github.com/lazynet/tp-caio-g11-2026/releases/tag/defensa-lucho-v4-20261027).
- [Guion de defensa: respaldo y objeciones](guion-defensa.md).
- [Speech: relato por diapositiva y transiciones](speech-presentacion.md).
- [Resultado completo de la revisión interna](board-review.md).
- [Fuente congelada de la alternativa](slides.md) y [tema](acme.css).

El PDF abre con las diez diapositivas; después incluye los anexos A–G completos y el material de apoyo. Sus 308 páginas y aproximadamente 1,9 MB corresponden a ese respaldo completo, no a un deck de 308 diapositivas. Los marcadores permiten saltar por sección.

## Resultado de revisión

El agente Board del repo hizo una revisión focalizada e independiente de la presentación y del guion de defensa V4, con las miradas de directorio, CFO y corrector. Resultado: **4/4 en los siete criterios**, sin observaciones textuales sustantivas pendientes dentro del alcance revisado:

| Criterio | Nivel |
|---|---:|
| Estrategia y alcance | 4/4 |
| Arquitectura, gobierno, seguridad y personas | 4/4 |
| Roadmap integrado | 4/4 |
| Finanzas | 4/4 |
| Escenarios y reversibilidad | 4/4 |
| Preparación de la defensa | 4/4 |
| Síntesis y trazabilidad | 4/4 textual |

Se abrieron las diez diapositivas del PDF final para comprobar su lectura. La revisión interna del borrador no es una nota oficial del aula ni una aprobación de un directorio real. No se calculó nota global. El speech se preparó después como apoyo de exposición; no se lo presenta como un objetivo adicional de aquella revisión.

## Versión y conservación

- Respaldo de anexos y criterios: commit `9c3a879c3f0f4d3225e5602b1b3bc1a5ab8efb91`.
- Las fuentes copiadas aquí conservan los bytes de la V4 local aprobada. [snapshot.json](snapshot.json) registra sus hashes.
- El guion de defensa y el speech son archivos separados.
- Los anexos siguen en [su versión de respaldo](https://github.com/lazynet/tp-caio-g11-2026/tree/9c3a879c3f0f4d3225e5602b1b3bc1a5ab8efb91/plan/annexes); no se duplican ni editan en esta propuesta.
- El PDF generado se publica como adjunto de esta propuesta. No se agregan PDF, ZIP, PowerPoint ni mensajes de WhatsApp al historial Git.

Para reproducir las diez diapositivas, usá Marp con este `slides.md` y `acme.css`, con salida en `out/`. Las referencias remiten deliberadamente al commit fijo que respaldó la revisión.

## Pendientes del equipo

- Revisar y acordar la alternativa con los responsables, o registrar su descarte (#27).
- Confirmar presentadores y responsables de respuestas; ensayar con fecha, tiempos y feedback (#21).
- Mantener las validaciones de fuentes y de entrega del plan. Ningún acuerdo de esos puntos se da por cumplido por publicar esta propuesta.
