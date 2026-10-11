---
name: board-review
description: Revisión multi-agente del plan CAIO antes de que llegue al equipo o al equipo de peer review. Los cuatro agentes de rol (architect, governance, people, finance) revisan en paralelo, cada uno con su mirada, y después el agente board consolida una revisión con fecha en reviews/. Usalo cuando pidan una revisión del board, una pre-revisión o poner a prueba slides o anexos.
argument-hint: "[path a revisar; por defecto plan/]"
---

# board-review

Objetivo de la revisión: el path que se pase como argumento; si no hay, `plan/`.

1. Lanzá en paralelo los subagentes `architect`, `governance`, `people` y
   `finance`. Cada uno revisa el objetivo solo con su mirada y devuelve brechas,
   contradicciones con otras secciones y afirmaciones sin fuente. No editan archivos.
2. Lanzá el subagente `board` con el objetivo y los cuatro reportes. Escribe la
   revisión con fecha en `reviews/AAAA-MM-DD-<objetivo>.md`.
3. Devolvé el veredicto del board por sombrero, los 5 hallazgos principales con
   su agente dueño y el path de la revisión.

Si tu herramienta no puede elegir el tipo de subagente (por ejemplo, Codex),
lanzá subagentes genéricos y pasale a cada uno, como instrucciones, el
contenido de `.claude/agents/<rol>.md`. Si no puede lanzar subagentes, corré
las cinco miradas en secuencia vos mismo, sin mezclar los hallazgos de cada una.
