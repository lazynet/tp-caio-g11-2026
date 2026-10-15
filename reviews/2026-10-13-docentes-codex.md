# Revisión docente cruzada — Plan Maestro CAIO (Acme Labs)

Fecha: 2026-10-13. Estado: revisión de borrador; no habilita peer review ni entrega.
Versión revisada: rama `chore/anonimizar-acme`, commit `3ed2875` sobre `main` (`1ba9c2e`).

## Metodología: auditar con otro tipo de agente

El plan lo produjeron agentes de Claude (Anthropic) con roles del repo
(`caio`, `architect`, `governance`, `people`, `finance`) y lo revisó `board`,
también Claude. Un revisor de la misma familia de modelos comparte sesgos con
quien escribió: estilo, supuestos implícitos, puntos ciegos y tendencia a
validar argumentos que él mismo generaría.

Para limitarlo, esta auditoría la hizo **un agente de otro proveedor y otro
harness**: Codex CLI con `gpt-6-astra` (OpenAI), reasoning `high`. Además se le
dio **otro rol**: no el board de la empresa, sino el equipo docente de la
diplomatura que corrige el TIF contra la consigna y lo enseñado en la cursada.

Cómo se corrió:

- **Aislamiento:** solo lectura sobre un commit fijo; podía generar `out/`
  (fuera de git) y correr los chequeos. No editó, no commiteó ni pusheó: el
  árbol quedó limpio al terminar.
- **Brief autocontenido:** contrato del repo (`AGENTS.md`), fuentes de la
  consigna (`material/programa.md`, índices y huecos de `material/`) y ocho
  criterios: consigna, formato, uso de la cursada, trazabilidad de cifras,
  coherencia interna, anonimización, chequeos automáticos y calidad ejecutiva.
  Salida pedida: veredicto, tabla por criterio, hallazgos priorizados con
  `path:línea`, preguntas del tribunal y output de los chequeos.
- **Sin acceso a datos privados:** no leyó `private/` ni la denylist, y tenía
  prohibido buscar la empresa real.
- **Control del orquestador:** antes de guardar, se reprodujeron dos hallazgos
  por fuera del revisor: los 321 vínculos `file://` del PDF (B2) y que la regla
  de G2 manda a esperar, no a cortar, entre 0% y +3% (M1).

Límites:

- Sigue siendo una revisión de IA. No reemplaza la verificación humana que
  exige `AGENTS.md`, y ninguna ficha pasa a `verified` por ella.
- La nota es juicio del revisor, no una rúbrica oficial de UTN.
- Fue una sola corrida. Los logs y capturas que cita en `out/` son locales y no
  se versionan; se regeneran con los mismos comandos.

Para la cursada: el mismo patrón sirve a cualquier CAIO. Las conclusiones de un
sistema de IA las audita un sistema distinto (otro proveedor, otro rol, otras
instrucciones), con alcance y evidencia explícitos y con una persona que
reproduce lo crítico antes de actuar.

## Reporte del revisor

### 1. Veredicto

**Hoy no lo aprobaría como entrega final. Nota orientativa: 5/10.** Hay un borrador sustantivo, con integración de las cinco miradas, costos explícitos y decisiones por etapas. La nota es juicio de esta revisión, no una rúbrica oficial de UTN.

La entrega falla por evidencia humana pendiente, trazabilidad que se rompe al exportar el PDF y contradicciones entre escenarios y gates. El caso de producto que justifica parte de la inversión todavía no está definido. La versión pública necesita otra revisión de anonimización antes de publicarse.

El ROI negativo no es por sí mismo motivo de desaprobación: reconocerlo es una fortaleza. El problema es que las otras razones para invertir —protección comercial, cobertura de precios y opción de producto— todavía no tienen una prueba decisoria suficiente (`plan/annexes/05-business-case.md:167`, `plan/annexes/06-roadmap-riesgo.md:225`).

**Versión y alcance.** Rama `chore/anonimizar-acme`, HEAD `3ed2875`, base `1ba9c2e`; árbol de trabajo limpio al inicio y después del build. Revisión del 2026-10-13, contra el contrato del repo y el material disponible. No hubo cambios a fuentes, commits, push ni búsquedas de la empresa real.

Leí las diez slides, los seis anexos, las 32 fichas de contexto, storyline y objeciones, programa, mapa, huecos y fichas pertinentes de la cursada. Usé el checklist de board como referencia, sin ejecutar su workflow. Inspeccioné las diez slides renderizadas y las 92 páginas de anexos en hojas de contacto; no fue una lectura visual ampliada de cada página.

### 2. Tabla por criterio

| Criterio | Estado | Evidencia | Qué falta |
|---|---|---|---|
| 1. Consigna e integración | Parcial | Arquitectura y alternativas: `plan/annexes/02-arquitectura.md:49`, `:208`; gobierno: `plan/annexes/03-gobierno-seguridad.md:122`; personas: `plan/annexes/04-personas-cultura.md:94`; finanzas: `plan/annexes/05-business-case.md:68`; roadmap: `plan/annexes/06-roadmap-riesgo.md:86` | Elegir una apuesta de negocio concreta, resolver capacidad por trimestre, asignar responsables y demostrar que los escenarios ejecutan sus gates. |
| 2. Formato | Cumple el límite formal | `plan/slides.md:21`, `:149`; `scripts/build-deck.sh:30`; `out/revision-build-escalated.log:13`; PDF regenerado: 10 slides + 92 páginas de anexos, 1.000.229 bytes | Corregir navegación y trazabilidad del PDF. Las 92 páginas de anexos no violan un tope documentado, pero sí perjudican la consulta ejecutiva. |
| 3. Uso de la cursada | Parcial | M1U1 aplicado: `plan/annexes/01-diagnostico.md:39`; harness: `plan/annexes/02-arquitectura.md:57`; literacy: `plan/annexes/04-personas-cultura.md:156`; RICE diferido: `plan/annexes/06-roadmap-riesgo.md:227` | Portfolio priorizado, quick win con valor en los primeros 100 días, proceso humano-agente concreto y diseño mínimo de evals/unit economics. |
| 4. Trazabilidad y cifras | No cumple para entrega | `out/revision-okf-delivery.log:155`; `plan/annexes/05-business-case.md:351`; `context/supuestos/rampa-de-la-ganancia.md:17` | Verificación humana, reconciliar fichas y anexos, corregir la rampa y hacer que las fuentes sean consultables desde el PDF. |
| 5. Coherencia interna | Parcial | Espera en G2: `plan/annexes/06-roadmap-riesgo.md:119`; corte pesimista: `:150`; G0 económico: `plan/annexes/05-business-case.md:413`; portada: `plan/slides.md:27` | Unificar gates, escenario elegido, capacidad y autorización de cierre; retirar referencias a versiones superadas. |
| 6. Anonimización | No cumple el cierre requerido para publicar | `context/hechos/oferta-y-segmentos.md:21`, `:27`; `context/hechos/estructura-de-ingresos.md:35`; historia Git (ver B3) | Reducir la huella identificable del conjunto y revisar también la historia Git. El scanner sin hallazgos no prueba anonimato. |
| 7. Chequeos automáticos | Parcial | Logs `out/revision-leak.log:1`, `out/revision-okf.log:1`, `out/revision-plan.log:1`, `out/revision-tests.log:3`, `out/revision-plan-delivery.log:1` | Borrador y 84 tests pasan; entrega no. Además, el detector confunde el español «todo» con TODO (`scripts/plan-check.py:328`). |
| 8. Calidad ejecutiva y defensa | Parcial | Pedido temprano: `plan/slides.md:27`; cierre: `defense/storyline.md:63`; evidencia vacía: `defense/evidence/index.md:11` | Menos repetición, hacer visible el pedido G0 completo, anexo de consulta breve y ensayo con evidencia y responsables. |

### 3. Hallazgos priorizados

Los impactos en la nota son cualitativos y no se suman como penalidades independientes: varios hallazgos afectan el mismo criterio.

#### Bloqueantes

**B1. Ninguna cadena de cifras está habilitada para entrega.**

Evidencia: `AGENTS.md:130`, `:137`; `out/revision-okf-delivery.log:155` registra 154 fichas sin revisión humana: 32 de contexto y 122 de material. El recorrido de `plan-check --mode delivery` requiere 62 fichas directas —28 de contexto y 34 de material—, además del deck y seis anexos todavía `draft`.

Impacto: bloquea la aprobación final y el peer review bajo las reglas acordadas. No implica que las cifras sean falsas; implica que todavía no existe la revisión exigida. Corrección: asigná revisores humanos, verificá fuentes y supuestos, registrá alcance y fecha, y reconciliá los faltantes antes de declarar `ready`. No alcanza con cambiar etiquetas.

**B2. El PDF no permite seguir la evidencia fuera de la computadora que lo generó.**

Evidencia: `scripts/build-delivery.py:38` concatena los cuerpos; `:90` los imprime desde HTML temporal; `:159` agrega deck y anexos. La inspección de anotaciones de `out/entrega.pdf` contó **321 URI `file://`, 3 URI web y 6 destinos internos**. Por ejemplo, en la página 11 los enlaces a slide y ficha de madurez son rutas locales; la fuente Markdown está en `plan/annexes/01-diagnostico.md:9`, `:18`.

Impacto: hay trazabilidad en el repositorio, pero el único entregable deja de ser auditable por el tribunal. También expone rutas locales. Corrección: convertí vínculos entre slides/anexos a destinos internos y agregá referencias públicas estables o evidencia procesada autocontenida; para las fuentes privadas, identificador anonimizado y constancia de validación humana, nunca el original.

**B3. Cambiar el nombre no anonimiza el conjunto ni su historia.**

Evidencia: la combinación pública de las tres ofertas, las dos sedes, antigüedad y sello de certificación es muy específica (`context/hechos/oferta-y-segmentos.md:21`, `:27`). Se le agregan tamaño y estructura (`context/hechos/tamano-y-estructura.md:15`, `:20`), mezcla y concentración comercial (`context/hechos/cartera-y-concentracion.md:29`, `:40`) y dos productos en inversión con características singulares (`context/hechos/estructura-de-ingresos.md:35`).

No identifiqué ni busqué la empresa real. La combinación que facilita reconocerla junta los nombres comerciales de la oferta pública, las ciudades de las sedes, la antigüedad exacta, el organismo del sello de certificación y la escala de la dotación. *(Valores concretos redactados el 2026-10-13 al corregir B3: este archivo es público.)* Una vez reconocida, los alias y los productos en inversión permiten vincular información interna. Los índices mensuales y métricas exactas del piloto agregan una huella innecesaria (`context/hechos/situacion-economica.md:15`, `context/hechos/encuesta-y-pilotos-ia.md:25`).

La comparación de la rama mostró además que se retiró del scanner un patrón con dominio corporativo real, pero sigue recuperable en un commit anterior de la historia publicada, en el scanner y en su test. *(Commit y líneas redactados el 2026-10-13 al corregir B3.)* No lo reproduzco. El chequeo del árbol actual no escanea ni anonimiza esa historia.

Impacto: bloquea considerar cerrada la preparación para publicación, independientemente de la nota académica. Corrección: generalizá sedes, antigüedad, rasgos de oferta y cruces que no cambian decisiones; revisá el conjunto con alguien autorizado. Tratá la historia como una exposición separada: un commit nuevo no borra lo ya publicado (`README.md:234`). No se propone reescribirla automáticamente.

#### Mayores

**M1. El escenario pesimista no ejecuta el gate que dice ejecutar.**

Evidencia: `context/supuestos/rampa-de-la-ganancia.md:14`, `:17`; `plan/annexes/05-business-case.md:324`; `plan/annexes/06-roadmap-riesgo.md:119`, `:150`; slide 9 en `plan/slides.md:137`.

El objetivo pesimista de 5% multiplicado por la rampa de T2 de 10% da **+0,5%**. G2 manda a espera entre 0% y +3%, libera T3 sin escalado y vuelve a medir seis semanas después. No ordena cortar en G2 por no llegar a +3%. La ausencia de cliente corta P, no automáticamente I. Tampoco se declara más retrabajo en ese escenario.

Impacto: la protección de pérdida «−245 frente a −481» no está demostrada por la política vigente. Corrección: especificá la causa adicional que dispara el corte, o simulá la espera y su costo hasta el gate realmente aplicable; recalculá slides 8-9, E, F y objeción 17. Separá los costos de base, interno y producto para no cargar el techo entero a una falla de un solo frente.

**M2. Se aprueba una arquitectura antes de seleccionar el problema de producto.**

Evidencia: `plan/annexes/06-roadmap-riesgo.md:231` tiene pendientes usuario, problema, outcome y SLO; `:242` solo enumera tipos de candidato. RICE aparece como trabajo futuro en `:227`; no hay comparación puntuada. El método pide business case por iniciativa y prioridad relativa (`material/conceptos/m1u2-ai-portfolio-1-0.md:19`, `:54`).

Impacto: debilita la tesis «IA que se vende» y la aplicación de M1U2. La aceptación no vinculante de evaluar un piloto (`plan/annexes/06-roadmap-riesgo.md:239`) prueba interés exploratorio, no disposición a pagar.

Corrección: elegí al menos un candidato como hipótesis explícita, comparalo con dos alternativas y con hacer solo gobierno/eficiencia, y fijá usuario, tarea, outcome, datos, SLO y señal comercial. No hace falta inventar diez iniciativas ni ingreso del año 1; hace falta justificar por qué esta opción merece la inversión.

**M3. La capacidad no queda resuelta al separar sobres, y el pedido en slides es incompleto.**

Evidencia: `plan/annexes/05-business-case.md:116` distingue 1,6 FTE clave y 1,2 distribuidos; `:136` admite que incluso difiriendo producto T2 queda en 2,5 FTE clave frente al máximo de 2,25. `context/supuestos/sobre-de-capacidad-separado.md:39` reconoce que separar no crea horas.

La portada pide 1,6 FTE (`plan/slides.md:27`) y la slide financiera agrega 61 de tiempo (`:122`), pero las **590 horas distribuidas**, su autorización separada y la ratificación de **T0 hasta 7 mil** quedan solo en anexos (`plan/annexes/05-business-case.md:415`). Son decisiones, no mero sustento. Tampoco está confirmado el extremo disponible del rango 1-2,25: 1,6 no entra en su extremo inferior.

Impacto: no permite concluir que T1 sea ejecutable ni que el plan recomendado entre en T2. Corrección: llevá a slides el pedido completo, el piso de capacidad requerido y el trabajo desplazado por rol. Cerrá un cronograma y presupuesto para la opción recomendada de diferir producto; hoy el cuadro base todavía financia el piloto (`plan/annexes/05-business-case.md:78`).

**M4. La rampa tiene dos significados y cambia los beneficios.**

Evidencia: la ficha define rampa como fracción del objetivo de throughput (`context/supuestos/rampa-de-la-ganancia.md:17`), pero la fórmula multiplica la capacidad ya convertida por esa fracción (`plan/annexes/05-business-case.md:351`). Si el throughput trimestral es `g × r`, las horas evitadas son `g × r / (1 + g × r)`, no `g / (1 + g) × r`.

Con los mismos N=17,5 y costo mensual=4.750, el recálculo da beneficios anuales, en miles de USD: **base 62,131 frente a 60,175; pesimista 12,189 frente a 11,875; optimista 114,108 frente a 109,725** (`out/revision-numeric.log:2`, `:3`, `:4`). La fórmula actual es conservadora, pero no representa la rampa declarada. No cambia el signo del ROI.

Impacto: resta confiabilidad al modelo reproducible y a sus sensibilidades. Corrección: elegí una definición única y propagala a beneficios, escenarios y condiciones de gate; no cambies silenciosamente la ficha para justificar el resultado.

**M5. La pérdida máxima comunicada no es todo el desembolso posterior al corte.**

Evidencia: slide 8 (`plan/slides.md:123`) y objeciones 2/17 (`defense/objeciones.md:12`, `:27`) destacan 106 como máximo en G1. E sí separa ejecución+cierre de la base posterior: **106 hasta cerrar, pero 146 en el año si se conserva la base mínima** (`plan/annexes/05-business-case.md:281`).

Además, G0 autoriza 32 de caja y un corte en G1 requiere hasta 38 de caja con cierre (`plan/annexes/05-business-case.md:413`, `:281`); no queda explícita la autorización de esa reserva cuando G1 rechaza continuar. Impacto: el CFO puede interpretar un techo de pérdida que no cubre los compromisos efectivos. Corrección: mostrale ambos máximos y autorizá desde G0 el cierre y la base residual, o explicá qué autoridad los libera.

**M6. «Cobertura de precio» y «licencia para vender» están más afirmadas que demostradas.**

Evidencia: `plan/slides.md:53`; `defense/storyline.md:21`; gateway condicionado a endpoint configurable en `plan/annexes/02-arquitectura.md:97`; cobertura no verificada en `:92`. El estrés de 12× está bien diferenciado de una factura (`context/hechos/costos-tecnologia-e-ia.md:48`, `:60`), pero no hay comparación económica del gateway bajo suscripción y bajo API, conservando calidad.

La obligación de gobierno del cliente no demuestra que comprar IA al proveedor sea requisito de continuidad comercial. El propio apetito contractual es supuesto (`context/supuestos/apetito-de-riesgo-de-clientes.md:11`). Impacto: las dos palancas que justifican el ROI negativo quedan sin comparación contra una alternativa de controles mínimos.

Corrección: pedí evidencia contractual anonimizada y una prueba de portabilidad/costo antes de financiar el componente relevante. Mostrá qué riesgo reduce cada alternativa y cuánto cuesta. El texto de la [Comunicación A 7777 del BCRA](https://www.bcra.gob.ar/pdfs/comytexord/A7777.pdf), sección 4.6, respalda gestión del uso de IA; no prueba la exigencia comercial específica de este caso. Vigencia consolidada 2026: no verificada en esta revisión.

**M7. Persisten contradicciones entre fuentes de cálculo, hitos y decisiones.**

| Tema | Evidencia en conflicto | Corrección propuesta |
|---|---|---|
| Base de productividad | T0 en `context/supuestos/convenciones-de-calculo.md:13`, `context/supuestos/ganancia-de-productividad.md:34`; prospectiva de T1 en `plan/annexes/02-arquitectura.md:327` y F `:74` | Elegí una base, con regla de respaldo, y actualizá la fuente del cálculo y la comparación contra el OKR. |
| T0 supuesto versus realizado | E dice «se ejecuta» y autorización pendiente (`plan/annexes/05-business-case.md:94`); el pedido lo llama «ya ejecutado» (`:417`) y F igual (`plan/annexes/06-roadmap-riesgo.md:56`) | Presentalo como costo previo propuesto hasta contar con evidencia de ejecución. No hay acta o registro que permita afirmarlo como hecho. |
| T1 de infraestructura | Ficha: 500-1.500 **por mes** (`context/supuestos/precios-externos-sin-cotizar.md:17`); T1-b: 500-1.500 **por trimestre** (`plan/annexes/02-arquitectura.md:398`) | Registrá T1-b como variante de la ficha; hoy seguir el enlace triplica ese renglón. |
| Contingencia | La ficha dice que cubre no estimados (`context/supuestos/precios-externos-sin-cotizar.md:21`); E los excluye del techo y exige desplazar otro gasto (`plan/annexes/05-business-case.md:362`) | Una sola regla presupuestaria y sus exclusiones. |
| G1/matriz | Slide 7 corta producto por ausencia de matriz (`plan/slides.md:107`); F admite revisión hasta mes 4 y corte por cliente (`plan/annexes/06-roadmap-riesgo.md:116`) | Sintetizá sin alterar el alcance del corte. |
| G4 | E: «No se renueva el régimen» (`plan/annexes/05-business-case.md:430`); F y slide: sigue frente interno con controles (`plan/annexes/06-roadmap-riesgo.md:128`, `plan/slides.md:110`) | Definí alcance, costo y autorización del frente que queda en el año 2. |

Impacto: penaliza integración; no se soluciona solo con más detalle. Dueño integrador: `caio`, con confirmación de cada dueño de anexo.

**M8. El plan cita más madurez operativa de la que muestra.**

Evidencia: NIST se presenta como taxonomía utilizada (`plan/annexes/03-gobierno-seguridad.md:80`, `:225`), pero el registro R1-R9 no mapea funciones, responsable por riesgo, riesgo residual ni prueba del control (`:104`). Los cuatro release gates se nombran (`plan/annexes/02-arquitectura.md:65`), pero datasets, evaluación, umbrales y respuesta a drift siguen sin aplicación concreta (`:185`, `:347`).

Impacto: debilita M1U4/M2U4 y la defensa frente a una falla del modelo. Corrección: agregá un ejemplo completo de riesgo→control→prueba→evidencia→aceptación residual, y una ficha de evaluación de un caso con dataset sintético, criterio de aceptación, revisión humana, versión y rollback. El curso no provee los umbrales: corresponde proponerlos y marcarlos, no inventar que ya se midieron (`material/conceptos/m2u4-evals.md:39`).

**M9. La defensa está preparada en texto, pero no probada.**

Evidencia: `defense/storyline.md:6`, `defense/evidence/index.md:11`, `plan/slides.md:153`; acuerdo de caso y alcance pendientes en `README.md:397`. El banco de veinte objeciones es útil, pero remite a borradores y repite respuestas generales sobre valor comercial.

Impacto: no permite evaluar dominio humano, tiempos, respuestas espontáneas ni reparto de responsabilidad. Corrección: acordá el caso y los responsables, ensayá las ocho preguntas del punto 4 y registrá evidencia anonimizada, tiempos y correcciones. No se exige haber ejecutado el plan 2027; sí poder defender sus decisiones en 2026.

#### Menores

**m1. El detector automático sobredimensiona los pendientes.** `scripts/plan-check.py:328` busca `TODO` con `re.IGNORECASE` y rechaza el español «todo». Ejemplo observado: «sobre todo la terminal» en `context/hechos/encuesta-y-pilotos-ia.md:62`. De las 76 coincidencias, 30 aparecen solo por «todo», sin otra expresión de la regex en esa línea. No son 76 tareas independientes. Corregí el detector y agregá una regresión cuando se autorice editar; no borres cautelas verdaderas para poner el checker en verde.

**m2. Hay restos de coordinación entre agentes en el entregable.** B dice que D solo tiene contractor desde T2 (`plan/annexes/02-arquitectura.md:262`) y que Finanzas lo cuenta doble (`:275`), cuando E ya lo sustituyó desde T1 (`plan/annexes/05-business-case.md:55`). F pide alinear una base que B ya alineó (`plan/annexes/06-roadmap-riesgo.md:83`, B `:287`). E afirma que faltan fichas que sí existen (`:490`; `context/supuestos/costos-de-cierre-por-corte.md:9`). Quitá estados de rondas anteriores y conservá solo alternativas vigentes.

**m3. Redondeos y unidades necesitan una regla.** G0 máximo calculado es `(16,5 + 10 + 1,5) × 1,15 = 32,2`, frente a techo 32 (`plan/annexes/05-business-case.md:413`). El avanzado usa 13×40=520 h trimestrales (`plan/annexes/04-personas-cultura.md:168`), mientras Finanzas usa 480 (`plan/annexes/05-business-case.md:31`). Redondeá techos hacia arriba o recortá componentes y distinguí horas calendario de la convención de costeo.

**m4. La expresión del piloto sobreextiende la muestra.** Slide 6 habla de «la gente» (`plan/slides.md:92`), mientras la ficha y D advierten n=12 autoseleccionado (`context/hechos/encuesta-y-pilotos-ia.md:61`, `plan/annexes/04-personas-cultura.md:76`). Conservá NPS y finalización como señal de ese piloto, con muestra visible; no como prueba de toda la organización ni causalidad demostrada del formato.

**m5. La forma es legible, pero poco ejecutiva.** No observé desbordes evidentes en las diez slides. Predominan tablas y bullets, sin un flujo de arquitectura ni cronograma que haga visible la integración (`plan/slides.md:59`, `:103`). Las tablas usan 18 px (`:10`), con menor legibilidad proyectadas. El pedido G0 se repite en varias slides y la última termina sin una resolución sintética.

Los anexos repiten supuestos, riesgos, tensiones e insumos del deck. En el PDF, el diagnóstico ocupa pp. 11-15, B 16-35, C 36-52, D 53-68, E 69-86 y F 87-102. Hay filas partidas entre páginas y columnas estrechas: inversión pp. 70-72, gates pp. 81-83 y 91-94 (`plan/annexes/05-business-case.md:75`, `:424`; `plan/annexes/06-roadmap-riesgo.md:110`). Recortá duplicaciones y remaquetá tablas; no achiques más la tipografía. Falta numeración visible de anexos e índice de consulta.

#### Aplicación de la cursada: balance explícito

| Unidad/framework | Juicio docente |
|---|---|
| M1U1, cinco dimensiones | Aplicación buena como diagnóstico de escritorio: puntajes justificados, dimensiones separadas y tres brechas. Falta la validación por entrevistas, reconocida (`plan/annexes/01-diagnostico.md:22`; método en `material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md:39`). |
| M1U2, build/buy/agentificar y kill/scale | Hay decisiones por capacidad y razones (`plan/annexes/02-arquitectura.md:216`). Los gates son una aplicación real, aunque M1 y M7 muestran fallas. |
| M1U2, portfolio/RICE y 100 días | RICE solo se promete. T1 se concentra en habilitadores (`plan/annexes/06-roadmap-riesgo.md:91`), sin quick win de negocio medido dentro de los 100 días, a diferencia de `material/conceptos/m1u2-plan-100-dias.md:20`. Justificá la adaptación o agregá uno factible. |
| M1U3 y harness | Buena traducción a inventario, contratos de datos, memoria, aislamiento y controles (`plan/annexes/02-arquitectura.md:57`). Falta un recorrido de datos aplicado a un caso; el inventario de componentes no lo sustituye. |
| M1U4, Council/CoE, RACI y Governance Stack | Es de lo mejor aplicado: derechos, cadencias, intake y controles propuestos (`plan/annexes/03-gobierno-seguridad.md:145`, `:163`, `:171`). AI Constitution está cubierta funcionalmente por principios/política/prohibiciones; no corresponde exigir otro documento solo por el nombre. |
| NIST/ISO/OWASP | Se distingue correctamente voluntario de obligatorio y alinear de certificar (`plan/annexes/03-gobierno-seguridad.md:73`, `:218`). OWASP se traduce a amenazas; NIST/ISO necesitan mapeo y evidencia, no solo mención. |
| M2U3, fuerza laboral y grafo humano-agente | Hay transformación de roles (`plan/annexes/04-personas-cultura.md:107`), pero falta el antes/después de un proceso, sus handoffs y puntos de decisión humana (`material/conceptos/m2u3-grafo-humano-agente.md:22`). Es una mejora sustantiva esperable, no una nueva obligación formal de formato. |
| M2U4, tokenomics y AIOps | Bien separar telemetría de factura y evitar porcentajes de ahorro sin fuente. Falta costo por outcome aplicado y ciclo de evals/observación/rollback concreto (`plan/annexes/05-business-case.md:293`; `material/conceptos/programa-artefactos.md:23`). |
| M3U2, literacy/champions/cambio | Bien separar freno contractual de cultural, formar por rol y asignar tiempo (`plan/annexes/04-personas-cultura.md:156`, `:189`, `:203`). El compromiso de empleo y las métricas de comportamiento necesitan resolución. |
| ADKAR, Kotter, Lean Change, AIMM, CAIE | No descontaría puntos por no acumular frameworks. ADKAR/Kotter/Lean Change no están desarrollados en el corpus; AIMM tiene cautelas; CAIE no es rúbrica del TIF (`material/huecos.md:19`, `:45`; `material/conceptos/programa-evaluacion.md:36`). |

M2U1, M2U2, M3U3 y M3U4 faltan en las fuentes disponibles (`material/huecos.md:11`). No es evidencia de que no se hayan enseñado ni de que el equipo incumpla actividades: la corrección se limita al corpus accesible. Evitá suplir esos huecos con exigencias inventadas.

#### Auditoría de todas las cifras visibles en slides

Cada fila cubre números de negocio y umbrales; G0-G4, T1-T4, L1-L2 y A-F son identificadores. Año, horizonte, grupo y nombres del equipo son metadatos/alcance, no estimaciones financieras. Ninguna cadena de abajo está verificada por un humano.

| Slide y cifras | Cadena comprobada | Resultado |
|---|---|---|
| 1: 2027, Grupo 11; 32 mil y 1,6 FTE; T1/T2-T4 (`plan/slides.md:21`) | Calendario: `context/supuestos/convenciones-de-calculo.md:14`; G0: E `:120`, `:413`; equipo: `README.md:1` | Trazables como propuesta. Pedido incompleto sin horas distribuidas/T0. 32 es redondeo menor al cálculo máximo de 32,2. |
| 2: puntajes 2 y 1-2; ~7/10 y ~1/10; abril 2026; cero producción; 40%-50% y 83%-90% (`plan/slides.md:33`) | A `:43` a `:47`, `:56`; fichas `uso-ia-interno.md:49`, `gobierno-y-politica-ia.md:21`, `ia-en-producto-y-oferta.md:21`, `cartera-y-concentracion.md:31`, `capacidad-y-utilizacion.md:23`; escala M1U1 `:21` | Puntajes son propuesta, no medición. Ratificación actual no confirmada desde el corte de abril. Porcentajes tienen fuente privada anonimizada, no validada. |
| 3: dos frentes/una base, G0 (`plan/slides.md:47`) | F `:19`, `:47` | Conteo del diseño. Sin cifra económica nueva. |
| 4: ≥2 proveedores; 3 de 4 superficies; 12 meses y contratos >12 (`plan/slides.md:61`) | B `:59`, `:95`, `:234`; `context/hechos/uso-ia-interno.md:24` | ≥2 es objetivo del equipo; 3/4 es hipótesis técnica explícita, no capacidad de proveedor verificada. Plazos son restricciones propuestas. |
| 5: 5 asientos; 3 niveles; 5 días; primer secreto; L1-L2 y 12 meses (`plan/slides.md:76`) | C `:113`, `:131`, `:187`, `:199` | Decisiones propuestas con soporte local. No benchmarks externos. Umbrales sin ficha OKF específica; deben quedar como propuesta aprobable y trazable. |
| 6: NPS +42, 17%, 80% combinado y un contractor (`plan/slides.md:92`) | D `:65`, `:269`, `:149`; `context/hechos/encuesta-y-pilotos-ia.md:25`; `context/hechos/okrs-y-objetivos.md:32`; costo: `context/supuestos/costo-cargado-por-rol.md:19` | NPS 50%-8%≈42 y 2/12≈17% cierran por redondeo; muestra pequeña. 85% y 60% con igual peso dan 72,5%, consistente con no alcanzar 80%. Contractor es propuesta. |
| 7: 90%, 6 semanas, +3%, 80%, 0/+3%, 60%-80%, +8%, +5%, ~23% (`plan/slides.md:107`) | F `:114` a `:129`; E `:428`, `:429`, `:253`; D `:243`; régimen/N en fichas respectivas | Umbrales locales explícitos, sin calibración. ~23% recalcula a 23,224%. Las bandas se solapan en extremos si se leen literalmente: fijá intervalos no superpuestos y precedencia del «pasa». M1 invalida el corte pesimista automático. |
| 8: 114-314; 150-408; ~4,5 FTE; 32/61; 73/106 y 27/38; 12 meses, 3 escenarios, cero caja; ~23% vs +20%; 12× y 211-267 (`plan/slides.md:120`) | E `:75`, `:240`, `:279`, `:219`; costos de B `:383`, C `:330`, D `:347`; fichas `costo-cargado-por-rol.md:14`, `precios-externos-sin-cotizar.md:11`, `costos-de-cierre-por-corte.md:11`, `base-minima-tras-un-corte.md:13`, `costo-de-regimen-del-ano-2.md:11`, `desarrolladores-en-equipos-propios.md:11` | Totales redondeados consistentes con la tabla, salvo ajustes de M4/m3. FTE promedio de 2,8/6,1/4,9/4,0≈4,45. Suscripción 40-45 seats×40-45 USD×12×11 da 211,2-267,3 mil incrementales. Cierre no equivale al costo total del año. |
| 9: −245 vs −481; G4; >12 meses; ~3,7 FTE (`plan/slides.md:137`) | E `:286`, `:136`; F `:150`, `:215`, `:257` | −481≈12−493; −245≈beneficio residual−247. Se reproducen como escenarios de gasto, pero no como resultado de ejecutar el gate vigente. 3,7 es demanda de capacidad, no capacidad confirmada. |
| 10: ocho integrantes, A-F (`plan/slides.md:149`) | `README.md:3`; seis anexos presentes | Coinciden equipo y cantidad de anexos. Responsabilidades y ensayo pendientes. |

**Muestra adicional de cálculos decisorios.** ROI con costos medios de 493 y beneficios 12/60/110 da aproximadamente −98%/−88%/−78%, como E `:240`. Umbral de ventas: 114/3%=3,8 millones y 314/3%≈10,47 millones, como E `:99`. Riesgo evitado: 1%/(50%×30%)≈6,7 puntos y 1%/(40%×21%)≈11,9, como E `:203`. Son cálculos correctos sobre supuestos; no prueban liquidez, probabilidad de pérdida ni viabilidad del plan.

### 4. Ocho preguntas del tribunal

1. Si la razón principal para aprobarlo es vender IA, mostranos el usuario, el problema, el outcome y la comparación que hizo ganar a ese caso. Qué alternativa descartaron y por qué? (`plan/annexes/06-roadmap-riesgo.md:231`).
2. En el pesimista G2 da +0,5%. Su regla dice esperar. Por qué la slide dice cortar y cómo cambia la pérdida si cumplen las seis semanas de espera? (`plan/annexes/06-roadmap-riesgo.md:119`, `:150`).
3. Qué trabajo facturable dejan de hacer para liberar 1,6 FTE más 590 horas en T1, y cómo entra T2 incluso sin producto? (`plan/annexes/05-business-case.md:126`, `:139`).
4. Si rechazo G1, autorizo 106 o 146 mil económicos en el año? Quién paga la salida que lleva caja de 32 a 38? (`plan/annexes/05-business-case.md:281`, `:413`).
5. Qué prueba demuestra que el gateway reduce la exposición a precios, sin perder la suscripción plana ni degradar la calidad, y qué pasa con las superficies que no enrutan? (`plan/annexes/02-arquitectura.md:95`; `plan/annexes/05-business-case.md:214`).
6. Por qué medir más PR aceptados demostraría valor al cliente y no fragmentación de trabajo? Cómo separan el efecto de IA de la mezcla de tareas y de la capacitación? (`plan/annexes/02-arquitectura.md:151`).
7. Qué cláusula o señal verificable prueba que perderían negocio sin este plan, y por qué no alcanza una alternativa de gobierno mínimo más barata? (`plan/annexes/05-business-case.md:177`, `:203`, `:403`).
8. Qué verificó cada integrante, cómo seguiría yo una cifra desde el PDF sin su computadora y qué revisión evita reconocer la organización a partir del conjunto público? (`plan/slides.md:153`; `defense/evidence/index.md:11`; `context/hechos/oferta-y-segmentos.md:27`).

### 5. Output de chequeos y evidencia de ejecución

Entorno: `.venv` del repo principal activado como pide el brief; sin modificar código para ejecutar tests. Logs de esta revisión en `out/`, fuera de Git. Los resultados verdes prueban la ejecución observada, no una auditoría de la sensibilidad de cada test: no removí guards porque el brief exige solo lectura.

```text
$ bash scripts/leak-check.sh --all --strict
exit 0
✓ leak-check: revisión COMPLETA; sin hallazgos

$ bash scripts/okf-check.sh
exit 0
✓ okf-check: 157 archivos conformes en borrador; no implica aptitud para slides/entrega

$ bash scripts/okf-check.sh --delivery
exit 1
✗ okf-check: 154 errores
# Todos por revisión humana ausente: context 32; material 122.

$ python scripts/plan-check.py
exit 0
plan-check (draft): 10 slides; 76 pendientes; 162 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas

$ python scripts/plan-check.py --mode delivery
exit 1
plan-check (delivery): 10 slides; 76 pendientes; 162 referencias locales
ERROR: Entrega rechazada: deck declarado draft
# Seis anexos declarados draft.
# 76 coincidencias de pendientes, incluidas falsos positivos por «todo».
# okf-check invocado sobre las 62 fichas usadas directamente:
✗ okf-check: 62 errores

$ python -m unittest discover -s tests
exit 0
....................................................................................
----------------------------------------------------------------------
Ran 84 tests in 16.932s

OK
Shell verificado: GNU bash, version 3.2.57(1)-release (arm64-apple-darwin26)
Shell verificado: GNU bash, version 5.3.20(1)-release (aarch64-apple-darwin25.6.0)
```

Logs completos: `out/revision-leak.log:1`, `out/revision-okf.log:1`, `out/revision-okf-delivery.log:1`, `out/revision-plan.log:1`, `out/revision-plan-delivery.log:1`, `out/revision-tests.log:1`. En el bloque, líneas con `#` son síntesis de esta revisión, no salida literal del CLI.

**Cuánto falta para pasar entrega.** El chequeo global exige revisar 154 fichas; el recorrido directo del deck exige 62. No son cantidades sumables. Para ese recorrido faltan 62 verificaciones humanas, cerrar el estado del deck y seis anexos, resolver pendientes sustantivos y corregir la clasificación falsa de «todo». Las cuatro fichas de contexto fuera del recorrido directo no quedan dispensadas si sostienen cifras por enlaces transitivos. El checker se detiene al encontrar una ficha de evidencia (`scripts/plan-check.py:315`), por lo que pasar ese recorrido no certifica toda la cadena.

**Build y artefacto.** Primer intento restringido: falló por DNS al resolver npm (`out/revision-build.log:3`). Segundo intento, mismo script con acceso ampliado aprobado por el runtime: exit 0. No hubo rechazo del revisor automático.

```text
$ source /Users/lazynet/repos/lazy/tp-caio-g11-2026/.venv/bin/activate
$ bash scripts/build-deck.sh
out/entrega.pdf: 102 páginas, 1,000,229 bytes

$ pdfinfo out/entrega.pdf
Producer:        pypdf
Pages:           102
Page size:       960 x 540 pts
File size:       1000229 bytes
PDF version:     1.7
```

La medida de página anterior corresponde al deck; los anexos se generan A4 (`scripts/build-delivery.py:17`). Confirmé con pypdf el número de páginas y bytes y recorrí anotaciones. Evidencia visual: `out/revision-slides-1.png`, `out/revision-slides-6.png` y seis hojas `out/revision-contact-*.png`; inventario de páginas: `out/revision-pdf-pages.log:1`; cuentas: `out/revision-numeric.log:1`.

**Límites de la revisión.** No leí fuentes privadas originales ni la denylist, no validé contratos o nómina y no hice búsquedas de la empresa real. Los PDFs originales de la cursada no se cotejaron: usé su corpus procesado, como permite el brief. El programa no contiene rúbrica numérica oficial (`material/conceptos/programa-evaluacion.md:36`).

Para evitar cuestionar fechas con memoria desactualizada, consulté la [página oficial de la Comisión Europea](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai): respalda el calendario 2/12/2027 y 2/8/2028 citado en el corpus. El [ELI del Reglamento 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) no devolvió texto legible en esta consulta. No afirmo haber verificado el consolidado ni el alcance contractual del caso; ninguna ficha pasó a `verified`.

**Verificación independiente del reporte.** Un subagente aislado revisó cumplimiento, citas, logs y cuentas principales. Confirmó la discrepancia del gate pesimista, los costos de corte, la conversión de rampa y los enlaces locales; dictaminó «aprobado con ajuste menor de citas». Se completaron esas referencias. Esa segunda lectura valida el reporte, no otorga verificación humana al plan ni a sus fuentes.
