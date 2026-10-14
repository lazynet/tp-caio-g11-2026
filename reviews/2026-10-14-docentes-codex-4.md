# Revisión docente cruzada, cuarta corrida (a ciegas)

Fecha: 2026-10-14. Estado: revisión de borrador; no habilita peer review ni entrega.
Versión revisada: rama `chore/anonimizar-acme`, commit `0bae98f`.

## Metodología

Cuarta corrida de la revisión docente cruzada descripta en
[la primera revisión](2026-10-13-docentes-codex.md): Codex CLI con `gpt-6-astra`
(OpenAI), reasoning `high`, en sesión nueva y solo lectura, con el mismo rol y
los mismos ocho criterios. Esta vez fue **a ciegas**: las corridas 2 y 3 veían
las anteriores y cerraban sus propios hallazgos, así que su suba de nota
(5 → 6,5 → 7) tenía anclaje. Para esta corrida se sacaron del worktree
`reviews/` y la nota de `defense/objeciones.md` que citaba las revisiones, y se
le prohibió leer la historia de git, otros worktrees y sesiones previas.
Quedaron dos filas del Anexo E marcadas "(re-revisión docente)"; el revisor
declara no haberlas usado como punto de partida.

Resultado: **5/10**, igual que la primera corrida.

Las correcciones de esta revisión se integraron después, en las rondas 7 a 9
(M3, M5, M8, m1 y m2; M1, M2 y M4; la bifurcación en G1 como decisión humana).
Las líneas citadas abajo corresponden a `0bae98f`, no al estado actual.

---

Fecha: 2026-10-14. Estado evaluado: archivos presentes del worktree `review/docentes-4`, base `0bae98f` indicada por el brief, sin consultar historia de git. Corrección simulada contra la consigna del repositorio; no representa una calificación oficial de UTN.

## 1. Veredicto

**No lo aprobaría hoy como entrega final. Nota orientativa: 5/10.**
Integra las cinco dimensiones del plan y demuestra trabajo sustantivo de arquitectura, gobierno y finanzas, pero todavía no sostiene una decisión ejecutiva verificable.
Faltan validación humana, cierre del riesgo de reidentificación y una defensa con responsables; además, hay brechas entre el contrato de gates, sus titulares y la evidencia de valor.
El PDF cumple cantidad de slides y peso. La extensión de los anexos y el exceso de condiciones perjudican la síntesis.

La escala numérica es un juicio de esta corrección: el programa no publica una rúbrica numérica del TIF (`material/conceptos/programa-evaluacion.md:34`). Los impactos de los hallazgos se superponen; no son descuentos que deban sumarse.

## 2. Tabla por criterio

| Criterio | Estado | Evidencia | Qué falta |
|---|---|---|---|
| 1. Cumplimiento de la consigna | **Parcial** | Arquitectura en `plan/annexes/02-arquitectura.md:60`; gobierno y seguridad en `plan/annexes/03-gobierno-seguridad.md:113`; personas en `plan/annexes/04-personas-cultura.md:107`; finanzas en `plan/annexes/05-business-case.md:98`; integración en `plan/annexes/06-roadmap-riesgo.md:128`. Defensa sin ensayo: `defense/storyline.md:3`. | Las partes existen. Falta probar que el conjunto merece la inversión, asignar responsables humanos y cerrar decisiones que alteran objetivos y capacidad. |
| 2. Formato de entrega | **Cumple** en los límites físicos | `plan/slides.md:22` a `plan/slides.md:164`: diez slides, portada y equipo incluidos. Build observado: `out/entrega.pdf`, **162 páginas, 1.427.065 bytes**, con diez slides, un índice y 151 páginas de anexos. Consigna: `AGENTS.md:21`. | Mantener ese cumplimiento al editar. La síntesis y algunas decisiones escondidas en anexos se penalizan en calidad ejecutiva, no como un límite de páginas inexistente. |
| 3. Uso de la cursada | **Parcial** | Aplicación concreta de harness y datos: `plan/annexes/02-arquitectura.md:297`; Governance Stack: `plan/annexes/03-gobierno-seguridad.md:234`; grafo humano-agente: `plan/annexes/04-personas-cultura.md:140`; RICE: `plan/annexes/06-roadmap-riesgo.md:339`. | Completar selección del portfolio interno, comparación económica build/buy y aprendizaje temprano. La desviación de los primeros 100 días está explicada, pero su alternativa pequeña sigue sin costearse. |
| 4. Trazabilidad de cifras | **Parcial** como borrador; **no apta para entrega** | Las cifras principales tienen recorrido hasta fichas draft y las cuentas centrales cierran. Excepción relevante: `plan/annexes/05-business-case.md:168` contra `context/supuestos/capacidad-de-inversion.md:11`. | Revisar humanamente las **71 fichas citadas que rechaza plan-check**; completar supuestos huérfanos y el desglose de capacidad. No alcanza con cambiar status. |
| 5. Coherencia interna | **Parcial** | Calendario y reservas consistentes: `plan/annexes/06-roadmap-riesgo.md:59`, `plan/annexes/05-business-case.md:574`. Desajustes: `plan/slides.md:113` contra `plan/annexes/06-roadmap-riesgo.md:200`; `plan/annexes/04-personas-cultura.md:186` contra `plan/annexes/05-business-case.md:804`. | Una sola regla operativa de gates, alcance de G0 y bases de medición; retirar indicaciones editoriales que contradicen el texto vigente. |
| 6. Anonimización | **Parcial; publicación no habilitada por esta revisión** | Alias y rangos presentes, pero persisten asociaciones en `context/hechos/cartera-y-concentracion.md:40`, `context/hechos/estructura-de-ingresos.md:20` y `context/hechos/tamano-y-estructura.md:26`. | Revisión humana del conjunto, no solo de cada ficha. La denylist no está disponible y el control estricto no ejecutó el escaneo. Identidad real y ausencia total de datos privados: **no verificadas**. |
| 7. Chequeos automáticos | **Parcial** | Borrador OK; build OK; 91 tests OK con Chrome habilitado. Delivery falla por siete artefactos draft, 48 marcas de pendiente y 71 fichas sin verificar. Véase sección 5. | Cerrar el contenido y su revisión, proveer la denylist por el canal autorizado y repetir los modos de entrega. Distinguir pendientes editoriales de estados futuros legítimos del caso. |
| 8. Calidad ejecutiva | **Parcial** | Todas las slides piden o sostienen una decisión, pero `plan/slides.md:119` concentra presupuesto, reservas, capacidad, contingencias y fórmula; `plan/slides.md:141` mezcla netos y ROI. | Reducir densidad, explicitar qué se decide sobre los OKR, separar datos observados de metas y presentar una comparación económica homogénea. Los 151 folios de anexos necesitan edición sustantiva. |

## 3. Hallazgos priorizados

### Bloqueantes para entregar o publicar

**B1. La entrega no tiene evidencia humana declarada ni responsabilidad humana cerrada.**

Evidencia: `plan/slides.md:160`, `plan/annexes/01-diagnostico.md:22`, `plan/annexes/05-business-case.md:30`, `defense/storyline.md:3` y `defense/evidence/index.md:11`. La regla exige revisión humana en `AGENTS.md:139` y trazabilidad verificada para entrega en `AGENTS.md:145`.

El validador del corpus rechaza 156 fichas; el de la entrega, 71 fichas utilizadas: 33 de context y 38 de material. No significa que haya que verificar todo el corpus para entregar; sí las fuentes realmente utilizadas y las afirmaciones que sostienen.

**Impacto:** impide la aprobación final, aunque el diseño sea discutible como borrador. **Corrección:** asigná integrantes responsables, registrá el alcance real de cada verificación y cerrá el acuerdo del caso. Prepará evidencias anonimizadas de las afirmaciones decisivas y un ensayo con tiempos, roles y preguntas.

**B2. Los alias no eliminan la posibilidad de vincular el caso con una empresa y sus relaciones comerciales.**

Evidencia: oferta dual, antigüedad y sedes en `context/hechos/oferta-y-segmentos.md:18`; tamaño y estructura en `context/hechos/tamano-y-estructura.md:15`; certificaciones en `context/hechos/seguridad-y-certificaciones.md:21`. Los nombres del equipo están en `plan/slides.md:158`.

El conjunto conserva una huella que se detalla abajo. No busqué la empresa real ni afirmo haberla identificado. El chequeo estricto se detuvo antes de escanear por ausencia de denylist; tampoco podría demostrar por sí solo que el conjunto es anónimo.

**Impacto:** bloquea recomendar la publicación como segura. **Corrección:** pedí una revisión autorizada del conjunto; eliminá atributos y asociaciones que no cambian decisiones, y generalizá el resto. No hace falta publicar contratos ni nombres para demostrar concentración, restricciones o capacidad.

### Mayores

**M1. La propuesta financia una base costosa antes de demostrar qué intervención adicional produce el valor.**

Evidencia: `plan/annexes/05-business-case.md:333` asigna el beneficio a productividad; `plan/annexes/02-arquitectura.md:286` define un asistente de conocimiento; su gate es de aprendizaje y no de valor (`plan/annexes/02-arquitectura.md:338`). Tecnología ya usa agentes (`context/hechos/uso-ia-interno.md:49`).

El año base cuesta 394 mil económicos y libera 62 mil de capacidad; el plan no separa el aporte marginal de formación, mejores prácticas del agente existente y nueva plataforma. La alternativa sin contractor cuesta menos, pero su beneficio no se recalcula (`plan/annexes/05-business-case.md:283`, `plan/annexes/05-business-case.md:319`).

**Impacto:** baja fuerte en estrategia y financial storytelling. Un ROI negativo puede ser defendible; lo insuficiente es no comparar alternativas equivalentes para comprar aprendizaje, protección o ingreso.

**Corrección:** compará el paquete recomendado con gobierno mínimo más formación y con un piloto acotado sobre herramientas actuales. Mostrá costo incremental, señal de valor y condición de abandono de cada opción. No inventes una probabilidad de ingresos para volver positivo el ROI.

**M2. Los primeros 100 días postergan valor sin cerrar la comparación que justificaría esa secuencia.**

La cursada pide quick wins medidos y gobierno en paralelo (`material/conceptos/m1u2-plan-100-dias.md:20`). El plan reconoce la desviación y una prueba pequeña desde la semana 5, pero deja su costo sin estimar (`plan/annexes/06-roadmap-riesgo.md:104`).

La justificación de que esa prueba alteraría una base que se estabiliza no termina de encajar con la base ya congelada en la semana 4 y la capacitación desde la semana 5 (`plan/annexes/06-roadmap-riesgo.md:77`). El riesgo de precisión existe, pero afecta también al gate posterior.

**Impacto:** reduce la calidad de aplicación de M1U2; no se exige copiar literalmente una cantidad de iniciativas. **Corrección:** costeá la prueba pequeña y decidí con el mismo criterio que el paquete grande. Si se descarta, explicá qué incertidumbre concreta impide hacerla y qué evidencia la despeja.

**M3. El contrato resumido de gates no coincide con todas las reglas que el board estaría aprobando.**

La slide 7 dice que una espera se mide a las seis semanas y, si no mejora, corta el frente (`plan/slides.md:113`). Sin embargo, adopción en 60%-80% libera T3 y se revisa al cierre del trimestre (`plan/annexes/06-roadmap-riesgo.md:200`); G3 puede mantener base mínima tras la espera (`plan/annexes/06-roadmap-riesgo.md:205`).

G1 tampoco tiene una condición automática de corte del plan: el anexo lo declara expresamente (`plan/annexes/05-business-case.md:840`). El board conserva la facultad de no liberar T2, pero no es lo mismo que una regla de abandono por fracaso.

Además, “el total de B1 es una decisión de G0” (`plan/annexes/04-personas-cultura.md:186`) puede leerse como aprobación anual del contractor, mientras G0 autoriza T1 y las ampliaciones dependen de gates (`plan/annexes/05-business-case.md:806`).

**Impacto:** alto en control financiero y coherencia. **Corrección:** limitá el texto de seis semanas al gate correspondiente; distinguí corte, suspensión, mantenimiento y excepción. Aclará que G0 elige la vía contractual y autoriza su primer tramo, sin liberar automáticamente los nueve meses siguientes.

**M4. La precisión de los gates y la regla de calidad todavía no hacen defendible el caso base.**

Con +3,75% y +9%, pasar exige intervalos mucho más estrechos que el máximo permitido; el propio modelo dice que lo esperable es esperar y cortar (`plan/annexes/05-business-case.md:358`). Se pide una comprobación en T0, pero no existe evidencia de que se haya realizado (`plan/annexes/06-roadmap-riesgo.md:76`).

La base cambia potencialmente a la retrospectiva si la prospectiva resulta demasiado dispersa (`context/supuestos/convenciones-de-calculo.md:16`), mientras el people plan sostiene atribución solo contra la prospectiva (`plan/annexes/04-personas-cultura.md:356`).

La regla de calidad invalida la ganancia solo si el límite inferior del aumento de incidentes/retrabajo es mayor que cero (`plan/annexes/02-arquitectura.md:241`). Un intervalo amplio que cruce cero no demostraría “sin deterioro”: dejaría el resultado incierto.

**Impacto:** alto en la validez de las decisiones y del retorno atribuible. **Corrección:** cerrá antes de G0 un protocolo único de medición, respaldo, calidad y muestra insuficiente. Recalculá las ramas de inversión con la precisión observada; distinguí explícitamente ausencia de evidencia de daño y evidencia de no deterioro.

**M5. El límite de capacidad tiene una cifra sin el respaldo que se le atribuye y una clasificación implícita de horas.**

El anexo E convierte “10%-15% del tiempo de 10-15 personas” en 1-2,25 FTE (`plan/annexes/05-business-case.md:168`). La ficha citada contiene 10%-15% de un “grupo acotado”, **sin fijar 10-15 personas** (`context/supuestos/capacidad-de-inversion.md:11`).

Ese denominador determina si el replan entra y cuánto habría que exceptuar. Además, el supuesto de capacidad separada define horas distribuidas como formación y champions (`context/supuestos/sobre-de-capacidad-separado.md:17`), pero las cifras de E parecen incluir también los ejercicios de incidentes de C.

Reconstrucción: T2 = 1,2 de B + 0,45 de gobierno/seguridad + 0,2 de liderazgo + (30 h de Council + 90 h de bypass + 60 h de red team)/480 = **2,225 FTE**. Si las 24 h del ejercicio de T2 son clave, da **2,275**, por encima de 2,25.

Las 2.790 h distribuidas del año se reconstruyen como 390 + 600 + 600 + 1.152 + 48 de ejercicios. Esto explica las cifras; **no es un error aritmético demostrado**, sino una clasificación no explicitada que altera la lectura del techo. Fuentes: `plan/annexes/03-gobierno-seguridad.md:474`, `plan/annexes/03-gobierno-seguridad.md:478`, `plan/annexes/03-gobierno-seguridad.md:482`, `plan/annexes/04-personas-cultura.md:478`.

**Impacto:** alto en factibilidad. **Corrección:** registrá como supuesto el número de personas clave; adjuntá una conciliación actividad→horas→rol→sobre, sin nombres. Confirmá capacidad real y trabajo desplazado; separar sobres contables no crea horas disponibles.

**M6. El caso de producto tiene usuario y señal comercial, pero todavía no un criterio de éxito de negocio.**

El usuario y el outcome están bien elegidos: integración exitosa y consultas al soporte (`plan/annexes/06-roadmap-riesgo.md:325`). Sin embargo, el SLO sigue pendiente y remite a exactitud, citas y aislamiento (`plan/annexes/06-roadmap-riesgo.md:330`); G3 pide cumplir ese SLO (`plan/annexes/06-roadmap-riesgo.md:208`).

La señal de G2 exige interlocutor con presupuesto y rango de precio de referencia, lo cual mejora la hipótesis, pero no prueba compra ni fija cuánto debe mejorar una integración. Los puntajes RICE están correctamente marcados como juicio del equipo, no como demanda medida.

**Impacto:** alto en estrategia comercial y aplicación del portfolio. **Corrección:** definí antes de liberar P cómo se validarán dolor, outcome, umbral, esfuerzo de soporte y decisión comercial. Mostrá quién obtiene esa señal y con qué capacidad presupuestada; no esperes a G4 para descubrir que la mejora útil nunca estuvo definida.

**M7. El diagnóstico de toda la organización no se traduce en un portfolio interno comparable.**

Se priorizan tres opciones de producto (`plan/annexes/06-roadmap-riesgo.md:339`), pero el asistente interno aparece como caso de referencia técnico (`plan/annexes/02-arquitectura.md:279`), sin una comparación equivalente con procesos de Operaciones, Finanzas o Comercial.

El portfolio de la cursada pide área responsable, inversión, retorno, métricas y próximos hitos por iniciativa (`material/conceptos/m1u2-ai-portfolio-1-0.md:19`). Capacitar a toda la empresa cubre personas; no reemplaza seleccionar dónde conviene intervenir en el negocio.

**Impacto:** medio-alto en el alcance de “organización completa”. **Corrección:** documentá una lista corta de candidatos internos y justificá cuál se prueba, cuál se posterga y cuál se descarta. No agregues casos solo para imitar las diez iniciativas del ejemplo docente.

**M8. Las decisiones sobre los OKR quedan fuera del pedido ejecutivo, y el equilibrio mezcla horizontes en su presentación.**

F propone excluir la inversión del indicador de gasto tecnológico o cambiar su denominador (`plan/annexes/06-roadmap-riesgo.md:401`). También propone reemplazar el OKR combinado de adopción (`plan/annexes/06-roadmap-riesgo.md:404`). La slide 6 reconoce que no llega al 80%, pero no pide explícitamente reformular el objetivo.

En la slide 8, “equilibrio ~17%” no aclara que es **equilibrio operativo anual del régimen del año 2** (`plan/slides.md:128`; `plan/annexes/05-business-case.md:502`). No recupera la inversión inicial; el propio anexo descarta payback dentro de 24 meses con productividad sola (`plan/annexes/05-business-case.md:535`).

**Impacto:** alto en claridad ante el CFO. **Corrección:** llevá al deck la decisión de mantener o cambiar cada objetivo, con el indicador original visible. Rotulá el equilibrio con su horizonte y separalo de ROI y payback. No conviertas una exclusión contable en mejora económica.

**M9. La evidencia procesada se convirtió en un documento demasiado extenso para su función.**

El PDF tiene 151 páginas de anexos: A 5, B 36, C 27, D 21, E 32 y F 30, según los inicios del índice generado. La matriz financiera ocupa varias páginas y el roadmap también; se comprobó visualmente en las páginas físicas 106, 138 y 139.

Las slides 8 y 9 se ven completas, pero obligan a procesar fórmula, múltiples reservas, tres magnitudes de corte, sobres de capacidad y excepciones (`plan/slides.md:121`, `plan/slides.md:141`). La columna “resultado del año (miles USD)” incluye porcentajes de ROI.

**Impacto:** alto en calidad ejecutiva, no incumplimiento formal de páginas. **Corrección:** recortá repeticiones y notas entre autores; mantené un cuadro maestro por decisión. En slides, compará escenarios con las mismas columnas —caja, costo económico, beneficio y neto— y dejá el detalle estadístico y de reservas en anexos navegables.

### Menores

**m1. Adopción del agente de código presentada como adopción de IA general.**
`plan/slides.md:38` dice que 7/10 y 1/10 “usan IA”; la fuente mide solo el agente de código (`context/hechos/uso-ia-interno.md:44`, `context/hechos/uso-ia-interno.md:64`). El anexo D sí aclara la limitación.
**Impacto:** precisión del diagnóstico. **Corrección:** nombrá la herramienta o la superficie medida en la slide.

**m2. Los documentos contienen instrucciones editoriales desactualizadas.**
C dice que F todavía clasifica distinto la política (`plan/annexes/03-gobierno-seguridad.md:289`), aunque F ya la define enmendable (`plan/annexes/06-roadmap-riesgo.md:379`). E afirma que D todavía frena seats (`plan/annexes/05-business-case.md:871`), aunque D ya suspende horas (`plan/annexes/04-personas-cultura.md:393`).
**Impacto:** confianza y claridad. **Corrección:** conservá desacuerdos vigentes; sacá mensajes de propagación que ya no describen el entregable.

**m3. Hay una ilustración de unit economics expresamente sin ficha, y el comparativo build/buy no desarrolla TCO.**
Las tasas de 2 y 4 PR por semana no tienen ficha (`plan/annexes/05-business-case.md:666`); la plataforma imputada queda fuera. B invoca cuatro ejes de decisión, pero su tabla resuelve mayormente control y capacidad sin costos y plazos comparables (`plan/annexes/02-arquitectura.md:382`).
**Impacto:** aplicación parcial, no falsedad: las limitaciones están declaradas. **Corrección:** registrá los supuestos o retiralos de la versión entregable; completá una comparación breve de las alternativas de plataforma relevantes.

**m4. Las fuentes del PDF apuntan a una rama mutable.**
Se observaron enlaces a GitHub `blob/main/`; el default está en `scripts/build-delivery.py:406`. No se verificó que main contenga los mismos bytes que este worktree y no se consultó otra rama.
**Impacto:** auditabilidad futura. **Corrección:** al preparar la entrega, fijá un commit publicado con las fuentes correspondientes mediante `CAIO_PUBLIC_REF`, como indica `README.md:356`, y verificá sus destinos.

### Trazabilidad: todas las cifras de las slides

Se distinguen hechos del caso, supuestos de cálculo y decisiones propuestas. Los números de slide, grupo, unidades y nombres de gates son identificadores, no resultados empíricos. Todas las cadenas siguientes siguen sin verificación humana declarada.

| Slide / cifras | Recorrido contrastado | Resultado |
|---|---|---|
| 1: 2027, tres meses y horizonte anual | `plan/slides.md:22` → `plan/annexes/06-roadmap-riesgo.md:39` → `context/supuestos/convenciones-de-calculo.md:14` | Calendario propuesto consistente. Grupo 11 y ocho nombres coinciden con `README.md:1`. |
| 2: niveles 2 y 1-2; dimensiones M1U1 | `plan/slides.md:34` → `plan/annexes/01-diagnostico.md:41` → `material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md:25` | Puntajes del equipo, correctamente rotulados como propuesta; entrevistas pendientes. |
| 2: 7/10, 1/10, abril 2026, cero IA en producto | `plan/annexes/01-diagnostico.md:45` → `context/hechos/uso-ia-interno.md:49`, `context/hechos/gobierno-y-politica-ia.md:21`, `context/hechos/ia-en-producto-y-oferta.md:21` | Hay origen documental declarado; la generalización de uso es m1. |
| 2: 40%-50%, 83%-90% | `plan/slides.md:42` → `plan/annexes/01-diagnostico.md:56` → `context/hechos/cartera-y-concentracion.md:31`, `context/hechos/capacidad-y-utilizacion.md:23` | Rangos de fuentes internas anonimizadas, no comprobados contra originales. |
| 3: dos frentes, una base, L1, dos alternativas | `plan/slides.md:48` → `plan/annexes/06-roadmap-riesgo.md:321` y `plan/annexes/06-roadmap-riesgo.md:339` → `material/conceptos/m1u2-rice-ajustado-por-riesgo.md:42` | Diseño y puntajes propuestos, no resultados medidos. RICE: 0,60; 0,111…; 0,125, coherentes con la tabla. |
| 4: ≥2 proveedores, 12 meses, T1-T3 y G0-G2 | `plan/slides.md:62` → `plan/annexes/02-arquitectura.md:62`, `plan/annexes/02-arquitectura.md:400` → `context/supuestos/umbrales-tecnicos-propuestos.md:28` y `context/supuestos/disponibilidad-de-datos.md:17` | Restricciones de diseño; no proveedores ya operativos. |
| 5: cinco asientos, tres niveles, cinco días, L1-L2, primer secreto y G3 | `plan/slides.md:77` → `plan/annexes/03-gobierno-seguridad.md:192`, `plan/annexes/03-gobierno-seguridad.md:248`, `plan/annexes/03-gobierno-seguridad.md:118`, `plan/annexes/03-gobierno-seguridad.md:265`, `plan/annexes/03-gobierno-seguridad.md:407` | Reglas propias identificables en el anexo. No son un SLA observado ni un mandato normativo cuantificado. |
| 6: n=12, NPS +42, 17%, abril | `plan/slides.md:93` → `plan/annexes/04-personas-cultura.md:65` → `context/hechos/encuesta-y-pilotos-ia.md:21` | NPS compatible con 6 promotores y 1 detractor sobre 12; 2/12 ≈17%. Cautela de autoselección explícita. |
| 6: 80% y un contractor | `plan/annexes/04-personas-cultura.md:364`, `plan/annexes/04-personas-cultura.md:183` → `context/hechos/okrs-y-objetivos.md:32`, `context/supuestos/costo-cargado-por-rol.md:19` | Meta del OKR y alternativa de contratación; no se oculta su tensión. |
| 7: ≥90%, ≥80%, ≥85%; +3%, +8%, ~17%, seis semanas | `plan/slides.md:109` → `plan/annexes/04-personas-cultura.md:338`, `plan/annexes/06-roadmap-riesgo.md:199`, `plan/annexes/06-roadmap-riesgo.md:205` → `context/supuestos/umbrales-tecnicos-propuestos.md:51`, `context/supuestos/costo-de-regimen-del-ano-2.md:11` | Metas y reglas propuestas. La frase universal de espera no respeta todas las ramas: M3. |
| 7: techos 33/62, 71/106, 59/78, 95/69 | `plan/slides.md:110` → `plan/annexes/06-roadmap-riesgo.md:131`, `plan/annexes/05-business-case.md:837` → `context/supuestos/precios-externos-sin-cotizar.md:13`, `context/supuestos/costo-cargado-por-rol.md:14`, `context/supuestos/convenciones-de-calculo.md:21` | Concuerdan entre slide y anexos; son máximos autorizables con redondeo superior, no medios ni gastos ya hechos. |
| 8: caja 98-255 y 114-314; tiempo 115-320; ~3,5 FTE | `plan/slides.md:123` → `plan/annexes/05-business-case.md:98`, `plan/annexes/05-business-case.md:137` → fichas de precios, costos por rol y `context/supuestos/poblaciones-de-capacitacion.md:13` | Caja base recalculada: 98,1525-255,30 mil antes de redondear. Tiempo consistente con componentes B/C/D y T0. El alcance de los sobres requiere la conciliación de M5. |
| 8: corte 73/106/146; reservas 6/15; base mínima hasta 41; T0 hasta 7 | `plan/slides.md:125`, `plan/slides.md:131` → `plan/annexes/05-business-case.md:554`, `plan/annexes/05-business-case.md:574` → `context/supuestos/costos-de-cierre-por-corte.md:25`, `context/supuestos/base-minima-tras-un-corte.md:13`, `context/supuestos/convenciones-de-calculo.md:21` | Diferencia entre pérdida hasta cierre, costo anual residual y reserva explicitada. 33+6 =39 mil de autorización de caja G0. |
| 8: ROI negativo, caja cero, ~17%/~23%, +20%, 1,20/(1+d)−1−c ≥16,7% | `plan/slides.md:127` → `plan/annexes/05-business-case.md:391`, `plan/annexes/05-business-case.md:489`, `plan/annexes/05-business-case.md:508` → `context/supuestos/desarrolladores-en-equipos-propios.md:13`, `context/supuestos/rampa-de-la-ganancia.md:13`, `context/supuestos/costo-de-regimen-del-ano-2.md:13` | Cálculos coherentes. Con régimen redondeado: g*=16,735% y 23,224%. La fórmula es condicional a d y c medidos, no prueba de que el OKR alcance. |
| 8: 1,6; 2,2/2,2/2,1; 2,5 FTE; 590 h | `plan/slides.md:131` → `plan/annexes/05-business-case.md:178`, `plan/annexes/05-business-case.md:213` → `context/supuestos/sobre-de-capacidad-separado.md:14`, `context/supuestos/poblaciones-de-capacitacion.md:13` | 590 =390 de básico +200 de intermedio según asignación del presupuesto; el sobre máximo de 2,25 carece del denominador en la ficha citada: M5. |
| 9: −262/−300/−382/−502; −84%; −245; −76% | `plan/slides.md:143` → `plan/annexes/05-business-case.md:358`, `plan/annexes/05-business-case.md:489`, `plan/annexes/05-business-case.md:640` → fichas de productividad, rampa, N/costo, cierre y base mínima | ROI base recalculado con presupuesto redondeado: −84,23%; optimista −75,77%. Las ramas de medio T3 son aproximaciones declaradas. |
| 9: 12×, 211-267/año, L3, >12 meses, 0,3 y 0,2 FTE | `plan/slides.md:148` → `plan/annexes/05-business-case.md:411`, `plan/annexes/06-roadmap-riesgo.md:261`, `plan/annexes/06-roadmap-riesgo.md:386` → `context/hechos/costos-tecnologia-e-ia.md:46`, `context/supuestos/umbrales-tecnicos-propuestos.md:62` | Incremental anual: 11×(40×40×12 a 45×45×12) =211,2-267,3 mil. No es factura actual ni ahorro del plan. Las fracciones son alternativas de asignación. |
| 10: equipo y G0 | `plan/slides.md:158` → `README.md:3`; resolución remite a slide 8 y `plan/annexes/06-roadmap-riesgo.md:50` | Ocho integrantes listados; responsabilidades y ensayo pendientes. No se verificó identidad ni participación individual. |

No encontré en estas cifras centrales un error aritmético que revierta el signo del ROI. Tampoco la consistencia aritmética demuestra que los supuestos sean verdaderos: los originales internos y las cotizaciones no se verificaron.

### Aplicación de la cursada: qué está logrado y qué queda incompleto

| Marco / unidad | Juicio docente |
|---|---|
| M1U1, diagnóstico | Se aplican las cinco dimensiones, se explica el nivel 2 y se priorizan brechas. Es un diagnóstico de escritorio declarado; falta la parte de entrevistas del método. `plan/annexes/01-diagnostico.md:22`; `material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md:39`. |
| M1U2, portfolio y RICE | Hay comparación de producto, fórmulas coherentes y riesgo marcado como adaptación. Falta comparación de iniciativas internas y el business case incremental de alternativas. `plan/annexes/06-roadmap-riesgo.md:312`; `material/conceptos/m1u2-ai-portfolio-1-0.md:54`. |
| M1U2, primeros 100 días y kill/scale | Hay reglas detalladas y salidas costeadas. La promesa de aprendizaje temprano y las reglas del deck no quedan resueltas por citar el marco. `plan/annexes/06-roadmap-riesgo.md:90`, `plan/annexes/06-roadmap-riesgo.md:187`. |
| M1U3 y harness | Aplicación sustantiva: fuentes, clasificación, data contract, retrieval, aislamiento, trazas, versionado y rollback. No es solo una lista de tecnologías. `plan/annexes/02-arquitectura.md:297`, `plan/annexes/02-arquitectura.md:340`. |
| M1U4, gobierno | Council/CoE, derechos de decisión, operating rhythm, Governance Stack y registro de riesgos conectan controles con pruebas y residuales. Buen nivel de diseño; faltan responsables humanos y evidencia de operación. `plan/annexes/03-gobierno-seguridad.md:142`, `plan/annexes/03-gobierno-seguridad.md:206`, `plan/annexes/03-gobierno-seguridad.md:224`. |
| NIST / ISO | El mapeo por función de NIST es útil. ISO 42001 es dirección y brecha futura, no un assessment completo: el propio texto declara que no cotejó cláusulas. No corresponde premiarlo como certificación o implementación terminada. `plan/annexes/03-gobierno-seguridad.md:165`. |
| M2U3, trabajo humano-agente | El antes/después de delivery asigna modos y revisión humana. Está correctamente declarado como proceso supuesto; falta validarlo con el proceso real. `plan/annexes/04-personas-cultura.md:131`. |
| M2U4, AIOps y economía | Dataset, evals, release gates, drift y rollback concretos. Tokenomics distingue suscripción de consumo y cobertura de precio de control. Falta convertir unit economics y outcome de producto en criterios completos de negocio. `plan/annexes/02-arquitectura.md:328`; `plan/annexes/05-business-case.md:432`, `plan/annexes/05-business-case.md:654`. |
| M3U1, seguridad | Riesgos y pruebas por superficie, bypass, secretos y respuesta inicial bien desarrollados; los controles futuros no deben confundirse con evidencia actual. `plan/annexes/03-gobierno-seguridad.md:154`. |
| M3U2, cultura | Literacy por nivel/rol, champions con tiempo y barreras contractuales frente a culturales son aplicaciones pertinentes. Falta confirmar tiempo, habilitación real y metas con el equipo. `plan/annexes/04-personas-cultura.md:246`, `plan/annexes/04-personas-cultura.md:296`. |
| Otros marcos del catálogo | No penalizo no usar CAIE, Cisco, AIMM, ADKAR o gemelos digitales por sí mismo. La consigna no pide exhibir todos los frameworks; `material/huecos.md:19` aclara la falta de desarrollo de algunos y `material/conceptos/programa-evaluacion.md:36` impide sustituir la consigna por CAIE. |
| Defensa / M3U4 | Hay storyline y 31 respuestas, pero no ensayo ni fichas de evidencia. Además falta el material de M3U4: es una limitación de acceso declarada, no prueba de que el equipo ignore un contenido específico. `defense/objeciones.md:41`, `defense/evidence/index.md:11`, `material/huecos.md:11`. |

No agregaría más frameworks. Lo que falta es cerrar evidencia, comparaciones y decisiones; lo que sobra son repeticiones, contingencias expresadas varias veces y comentarios de coordinación entre autores.

### Anonimización: combinaciones que facilitan el reconocimiento

| Combinación | Evidencia local | Riesgo y corrección |
|---|---|---|
| Software financiero + plataforma integrable y staffing + más de una década + oficinas en dos países latinoamericanos + certificación de gestión | `context/hechos/oferta-y-segmentos.md:18`, `context/hechos/oferta-y-segmentos.md:27`, `context/hechos/seguridad-y-certificaciones.md:21` | Rasgos públicos genéricos por separado, más discriminantes juntos. Conservá solo los que condicionen el plan. |
| Tamaño 60-70 + áreas casi simétricas de Tecnología/Operaciones + equipo de producto dedicado al principal cliente | `context/hechos/tamano-y-estructura.md:15`, `context/hechos/tamano-y-estructura.md:25` | Refuerza la huella organizacional. El tamaño es útil para cálculos, pero la asociación con el cliente puede eliminarse. |
| Cliente A principal + producto operado por suscripción + participación en ingresos y costos + equipo dedicado | `context/hechos/cartera-y-concentracion.md:31`, `context/hechos/cartera-y-concentracion.md:42`, `context/hechos/estructura-de-ingresos.md:20`, `context/hechos/costos-tecnologia-e-ia.md:37` | El alias persiste entre fichas y permite reconstruir una relación. Desacoplá concentración, línea comercial y centro de costo. |
| Dos productos propios en inversión + uno de medios de pago con habilitación en 2027 + otro con datos de categoría especial | `context/hechos/estructura-de-ingresos.md:35` | Combinación comercial más específica que “software financiero”. Generalizá funciones y calendario si no cambian la decisión. |
| Lo anterior + nombres de integrantes y vinculación del caso con una propuesta al CEO | `plan/slides.md:158`, `README.md:10` | Puede facilitar una asociación por conocimiento público de los integrantes. No afirmo que la asociación esté demostrada. Reducí la huella del caso sin borrar la identificación académica requerida del equipo. |

No se identificó un nombre real de cliente ni una credencial en el texto del entregable examinado. Esto no es un escaneo certificado de todos los archivos ni una validación de que los datos agregados sean suficientemente anónimos.

## 4. Ocho preguntas difíciles del tribunal

1. **Por qué comprar esta plataforma ahora?** Compará los 394 mil económicos del año base con gobierno mínimo más capacitación sobre las herramientas actuales. Qué aprendizaje o resultado incremental justifica la diferencia? (`plan/annexes/05-business-case.md:115`, `plan/annexes/05-business-case.md:283`).
2. **Qué cambia si fracasa T1?** Mostrá qué fondos se bloquean automáticamente, cuáles sigue liberando el modo control y por qué el titular de la slide 7 no dice eso. (`plan/slides.md:104`, `plan/annexes/05-business-case.md:840`).
3. **Puede pasar realmente el escenario base?** Mostrá la dispersión de T0, la cohorte utilizable y el protocolo que permite decidir con +3,75%, sin cambiar la base después de ver el ruido. (`plan/annexes/05-business-case.md:358`, `context/supuestos/convenciones-de-calculo.md:16`).
4. **De dónde salen las personas y las horas?** Justificá las 10-15 personas clave, el segundo sobre y qué trabajo facturable deja de hacerse. Dónde se cuentan los ejercicios de incidentes? (`plan/annexes/05-business-case.md:168`, `plan/annexes/03-gobierno-seguridad.md:482`).
5. **Qué prueba que el producto resuelve un problema por el que alguien pagaría?** Definí el umbral de integración o soporte que haría exitoso el piloto y el criterio comercial de G4. (`plan/annexes/06-roadmap-riesgo.md:327`, `plan/annexes/06-roadmap-riesgo.md:332`).
6. **Qué significa exactamente “equilibrio de 17%”?** Separá beneficio de caja, capacidad, régimen del año 2 y recuperación de lo invertido. Qué decide el board sobre los OKR originales? (`plan/annexes/05-business-case.md:508`, `plan/annexes/06-roadmap-riesgo.md:401`).
7. **Qué evidencia comercial sostiene la licencia para vender y cuánto gobierno hace falta sin esa señal?** Mostrá el agregado verificado, sin contratos ni clientes identificables, y el alcance de las capas M/T/D. (`plan/annexes/03-gobierno-seguridad.md:400`, `plan/annexes/03-gobierno-seguridad.md:431`).
8. **Quién del grupo responde por cada afirmación y por la anonimización?** Elegí una cifra del PDF, seguí su fuente estable y mostrale al tribunal qué verificó una persona y qué sigue siendo un supuesto. (`plan/slides.md:160`, `defense/evidence/index.md:11`).

## 5. Output de los chequeos automáticos

Se activó `.venv/bin/activate` del checkout principal. Se usó `PYTHONDONTWRITEBYTECODE=1` en los chequeos Python y `TMPDIR=$PWD/out` en la ejecución que necesitaba temporales. No se modificó código para hacer pasar pruebas.

### Chequeos de contenido

```text
$ bash scripts/leak-check.sh --all --strict
exit 2
✗ leak-check: denylist ausente o vacía; modo estricto rechazado

$ bash scripts/okf-check.sh
exit 0
✓ okf-check: 159 archivos conformes en borrador; no implica aptitud para slides/entrega

$ bash scripts/okf-check.sh --delivery
exit 1
✗ context/hechos/capacidad-y-utilizacion.md: entrega exige status: verified con revisión humana
[156 fichas rechazadas por ese mismo requisito; salida abreviada]
✗ okf-check: 156 errores

$ python scripts/plan-check.py
exit 0
plan-check (draft): 10 slides; 48 pendientes; 164 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas

$ python scripts/plan-check.py --mode delivery
exit 1
plan-check (delivery): 10 slides; 48 pendientes; 164 referencias locales
ERROR: Entrega rechazada: deck declarado draft
ERROR: Entrega rechazada: anexo declarado draft: plan/annexes/01-diagnostico.md
[los seis anexos están declarados draft]
[48 diagnósticos de pendiente]
[71 fichas utilizadas sin status verified: 33 de context y 38 de material]
✗ okf-check: 71 errores
```

Los 48 son coincidencias del chequeo, no 48 tareas humanas independientes. Por ejemplo, marca que un producto del caso está pendiente de habilitación (`context/hechos/estructura-de-ingresos.md:35`): eso no se resuelve inventando que obtuvo la habilitación.

Para pasar entrega hacen falta deck y seis anexos listos, resolver editorialmente las 48 marcas sin borrar incertidumbre real y declarar revisión humana válida de las 71 fichas utilizadas. El modo global de OKF exige 156; tres índices explican la diferencia con los 159 conformes en borrador.

### Build y PDF

Primer intento restringido: `npm ENOTFOUND registry.npmjs.org`. Intento sin red: `npm ENOTCACHED`. No se atribuyen esos errores al contenido del plan.

Se repitió el build con acceso ampliado para descargar Marp y ejecutar Chrome, con caché npm y temporales en `out/`.

```text
$ bash scripts/build-deck.sh
exit 0
plan-check (draft): 10 slides; 48 pendientes; 164 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas
[  INFO ] plan/slides.md => out/deck-marp.html
[  INFO ] plan/slides.md => out/deck-marp.pdf
[  INFO ] plan/slides.md => out/deck-marp.pptx
out/entrega.pdf: 162 páginas, 1,427,065 bytes

$ pdfinfo out/entrega.pdf
Pages:           162
Page size:       960 x 540 pts
File size:       1427065 bytes
PDF version:     1.7
```

Comprobación independiente con pypdf: deck 10 páginas, anexos 151; índice una página. El índice ubica A/B/C/D/E/F en las páginas de anexos 1/6/42/69/90/122.

Se inspeccionaron visualmente las diez slides, el índice y las páginas físicas 106, 138 y 139. No se observaron recortes en las slides; las tablas de anexos observadas repiten encabezados y muestran numeración al pie. **No se inspeccionaron visualmente las 162 páginas completas.**

### Tests

Primer intento restringido:

```text
Ran 91 tests in 13.540s

FAILED (errors=1)
ERROR: test_index_uses_titles_order_and_actual_destination_pages
SystemExit: Chrome no generó el pdf de los anexos
```

Repetición con acceso ampliado para Chrome:

```text
$ python -m unittest discover -s tests
exit 0
Ran 91 tests in 14.213s

OK
Shell verificado: GNU bash, version 3.2.57(1)-release (arm64-apple-darwin26)
Shell verificado: GNU bash, version 5.3.20(1)-release (aarch64-apple-darwin25.6.0)
```

La suite pasa en esa ejecución; no demuestra la verdad de los supuestos ni la suficiencia del plan. No se hizo mutation testing ni se removieron guards: la tarea prohíbe editar el código.

### Alcance y límites de la revisión

- No se consultaron `reviews/`, historia de git, otras ramas, otros worktrees, fuentes internas originales ni memorias del proyecto. Las menciones a correcciones previas encontradas dentro de anexos no se usaron como autoridad.
- Antes de delimitar la revisión se leyeron instrucciones operativas generales de skills externos al worktree. No contenían evidencia de este caso; Graphify y LazyMind no se ejecutaron. La corrección se apoya en los archivos citados del entregable y la cursada.
- No se buscó la empresa real. Tampoco se cotejó normativa vigente en fuentes externas: las afirmaciones regulatorias quedan **no verificadas** en esta corrección, con las cautelas de `plan/annexes/03-gobierno-seguridad.md:73` y `material/huecos.md:48`.
- La revisión de cifras abarca todas las slides y los cálculos de anexos que sostienen presupuesto, reservas, ROI, equilibrio, exposición, capacidad y gates. No se certifica cada supuesto secundario del corpus.
- No se actualizó PRJ: revisión de solo lectura, sin cambio aplicado al estado del proyecto y con acceso fuera del worktree prohibido por el brief. No se ejecutó `lh metrics record-verify`: la excepción de Codex del skill de verificación lo omite.

