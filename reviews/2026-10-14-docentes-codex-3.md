# Revisión docente cruzada, tercera corrida

Fecha: 2026-10-14. Estado: revisión de borrador; no habilita peer review ni entrega.
Versión revisada: rama `chore/anonimizar-acme`, commit `5c73fe7`.

## Metodología

Tercera corrida de la revisión docente cruzada descripta en
[la primera revisión](2026-10-13-docentes-codex.md): Codex CLI con `gpt-6-astra`
(OpenAI), reasoning `high`, en sesión nueva y solo lectura, con el rol del
equipo docente de la diplomatura. Esta vez se le pidió además contrastar la
versión corregida contra las dos revisiones anteriores (5/10 y 6,5/10), sin anclarse en ella: primero corrige desde
cero y después cierra cada hallazgo anterior (cerrado, parcial, abierto o empeoró).

Entre corridas, los agentes de rol del repo corrigieron sus anexos con un
orquestador que integró, corrió el gate y reprodujo los hallazgos críticos.
Los logs que cita en `out/` son locales y no se versionan.

## Reporte del revisor

Fecha: 2026-10-14. Rama: `chore/anonimizar-acme`. Versión evaluada: `5c73fe76b9b8f52d5251d8779c3f13e8a8b0b94b`.
Evaluación del trabajo académico; la nota es orientativa, no una calificación oficial de UTN.

Se revisó primero el estado actual y después se contrastó con los informes de `3ed2875` y `74ebece`. Los nombres A–F designan los seis anexos, en su orden.
Las referencias corresponden a esta versión. Los logs nuevos están en `out/review-3/`, fuera de git.

### 0. Cierre de las revisiones anteriores

#### Segunda revisión: R1–R10

| ID y problema anterior | Estado | Evidencia actual y juicio |
|---|---|---|
| R1 — La excepción no cubría la ausencia del contractor | **Parcial** | El error cuantitativo está corregido: sin contractor, la alternativa interna requiere 3,325 FTE clave en T2; el respaldo de 0,3 cubre únicamente la falta del 0,2 adicional. Hay modo control sin hitos de IA aplicada, y la slide lo explica. `plan/annexes/06-roadmap-riesgo.md:185`; `plan/slides.md:132`; `plan/slides.md:152`; `out/review-3/numeric.log:17`. Quedan una cautela ambigua sobre aprobación del contractor en `context/supuestos/umbrales-tecnicos-propuestos.md:94` y la incompatibilidad de documentación del replan, desarrollada en N3. |
| R2 — Reserva de cierre insuficiente después de G1 | **Cerrado** | Reserva de 6 en G0, ampliación a 15 antes del contractor al 100% y a 17 antes del tenant de P. F vincula su aprobación con la liberación de compromisos. `plan/slides.md:131`; `plan/annexes/06-roadmap-riesgo.md:186`; `plan/annexes/06-roadmap-riesgo.md:192`; `defense/objeciones.md:29`. Los cierres sin P de 6/15/15 se reproducen en `out/review-3/numeric.log:8`. |
| R3 — Corte de un frente sin sostener las dependencias del otro | **Cerrado** | La precedencia seguridad → dependencias → caja resuelve el corte mixto. E incorpora 0,1 FTE de arquitecto a la base de P: costo anual medio 433 frente a 471 sin corte. G1 ya no ordena un corte global automático. `plan/annexes/05-business-case.md:601`; `plan/annexes/05-business-case.md:825`; `plan/annexes/06-roadmap-riesgo.md:193`. Hay redondeos menores nuevos, no una reapertura de la solución de fondo. |
| R4 — Ruteo incompatible con suscripción y denominadores mezclados | **Cerrado** | B distingue suscripción preservada, suscripción que se pierde al enrutar y pago por consumo; F y C adoptan la distinción. Cobertura de eventos y fracción de costo elegible son métricas distintas. `plan/annexes/02-arquitectura.md:111`; `plan/annexes/02-arquitectura.md:122`; `plan/annexes/02-arquitectura.md:175`; `plan/annexes/06-roadmap-riesgo.md:189`; `plan/annexes/03-gobierno-seguridad.md:347`. |
| R5 — OKR y equilibrio comparados con bases distintas | **Parcial** | Se agregó el puente T0–T1 y el umbral de mejora previa de ~2,8%; la cuenta de rebasing es correcta. No se incorporó el ajuste por control o tendencia que ahora define la ganancia atribuible. `plan/annexes/05-business-case.md:504`; `plan/annexes/02-arquitectura.md:237`; `plan/slides.md:128`. El condicional de la slide sigue siendo insuficiente; ver N2. |
| R6 — Señal de evaluación presentada como disposición a pagar | **Cerrado** | G2 exige interlocutor con presupuesto y aceptación de un rango de precio, además de la evaluación; se aclara que no hay compromiso de compra y que la disposición a pagar sigue sin probarse. `plan/annexes/06-roadmap-riesgo.md:323`; `plan/annexes/06-roadmap-riesgo.md:344`; `defense/objeciones.md:31`. Cierre del diseño académico, no validación comercial real. |
| R7 — Gate de impacto sin umbral e intervalo sin método | **Parcial** | El gate de impacto ahora decide la extensión a Operaciones; rendimiento, seguridad y ética habilitan previamente L2 en Tecnología. Hay estimador, remuestreo por persona, confianza y criterio de precisión. `plan/annexes/02-arquitectura.md:237`; `plan/annexes/02-arquitectura.md:338`; `plan/annexes/02-arquitectura.md:343`. La incorporación del intervalo no se propagó al escenario base de Finanzas: N1. |
| R8 — Promesa de bloqueo universal de secretos | **Cerrado** | La slide diferencia bloqueo técnico de controles compensatorios y residual aceptado por el Council. El primer secreto expuesto activa contención. `plan/slides.md:79`; `plan/annexes/03-gobierno-seguridad.md:118`; `plan/annexes/03-gobierno-seguridad.md:330`. |
| R9 — Decisión y enlace recortados en la slide 7 | **Cerrado** | El render nuevo muestra completos tabla, aclaración sobre el intervalo, decisión y enlace. Fuente: `plan/slides.md:104`; evidencia visual: `out/review-3/slide-007.png`. Se inspeccionaron las diez slides, no solo el conteo del PDF. |
| R10 — Defensa sin responsables ni prueba humana | **Abierto** | Responsables por sección y ensayo siguen pendientes; el bundle de evidencia no contiene fichas. `plan/slides.md:160`; `plan/slides.md:162`; `defense/objeciones.md:4`; `defense/evidence/index.md:11`. Más respuestas escritas no sustituyen la defensa del equipo. |

#### Ocho menores de la segunda revisión

Se asignan S1–S8 solo para identificarlos en este informe; el anterior los enumeraba sin ID.

| ID / asunto | Estado | Evidencia actual |
|---|---|---|
| S1 — Ahorro pesimista atribuido a una cifra vieja | **Cerrado** | El puente ahora dice 218 = 120 por gates + 98 por diferir P, con alcances comparables. `plan/annexes/05-business-case.md:644`. |
| S2 — Restos de coordinación | **Abierto** | E sigue diciendo que D y F cubren la falta total del contractor con la excepción, y que F/C no adoptaron denominadores que ya adoptaron. `plan/annexes/05-business-case.md:856`; `plan/annexes/05-business-case.md:860`. |
| S3 — Exigencia comercial de los bancos presentada como certeza | **Parcial** | C distingue bien obligación del banco e hipótesis contractual del proveedor, pero la frase para el CFO vuelve a afirmar que compra controles que los bancos piden. `plan/annexes/03-gobierno-seguridad.md:91`; `plan/annexes/05-business-case.md:875`; `context/supuestos/base-minima-tras-un-corte.md:42`. |
| S4 — Medios de P rotulados como máximos | **Cerrado** | La ficha separa medios/rangos y los gates autorizan techos de 38/34 y 21/23. `plan/annexes/06-roadmap-riesgo.md:322`; `plan/annexes/06-roadmap-riesgo.md:192`; `plan/annexes/06-roadmap-riesgo.md:130`. |
| S5 — Frenar una expansión de seats no presupuestada | **Parcial** | F ahora identifica ~13 mil de tiempo de formación/champions que suspende. D conserva la instrucción anterior de frenar expansión de licencias. `plan/annexes/06-roadmap-riesgo.md:188`; `plan/annexes/04-personas-cultura.md:388`. |
| S6 — Comparación injusta de alternativas de 100 días | **Parcial** | Ya compara igual provisión de IA aplicada y reconoce que ambas variantes caben en el sobre clave. La rampa supuesta de cero en T1 no demuestra que cualquier resultado posterior a congelar la base sea ruido. `plan/annexes/06-roadmap-riesgo.md:97`; `plan/annexes/06-roadmap-riesgo.md:106`. |
| S7 — Enlaces públicos a `main` | **Abierto** | Se observaron 268 URI a una referencia mutable. La opción para fijar un commit publicado ya existe. `out/review-3/pdf-audit.log:3`; `README.md:356`. No se verificó acceso externo a cada destino. |
| S8 — Anexos demasiado extensos | **Empeoró** | La entrega pasó de 140 a 163 páginas: diez slides, un índice y 152 páginas de anexos. `out/review-3/pdf-audit.log:2`. No infringe un límite de anexos; sí agrava la falta de síntesis. La slide 7, evaluada aparte, mejoró. |

#### Primera revisión: hallazgos que seguían abiertos o parciales

| ID original | Estado actual | Evidencia y relación con esta revisión |
|---|---|---|
| B1 — Evidencia no habilitada para entrega | **Abierto** | 156 fichas fallan la revisión humana global; 71 están en el alcance directo del chequeo de entrega del plan. `out/review-3/okf-delivery.log:1`; `out/review-3/plan-delivery.log:58`. |
| B3 — Anonimización conjunta e historia | **Parcial** | Se mantienen generalizaciones, pero subsisten asociaciones de cliente, producto y características internas. La defensa afirma una desvinculación mayor que la observable. `context/hechos/estructura-de-ingresos.md:35`; `plan/annexes/02-arquitectura.md:226`; `defense/objeciones.md:32`. Historia pública no revalidada. |
| M2 — Producto sin selección defendible | **Cerrado** | Candidato, usuario, comparación RICE, señal con presupuesto/precio y condición de abandono explícitos. `plan/annexes/06-roadmap-riesgo.md:311`; `plan/annexes/06-roadmap-riesgo.md:323`; `plan/annexes/06-roadmap-riesgo.md:332`. |
| M3 — Capacidad y pedido G0 incompletos | **Parcial** | G0 y las contingencias cuantitativas están completos; queda el conflicto documental del replan. `plan/slides.md:130`; `plan/annexes/04-personas-cultura.md:210`; `plan/annexes/02-arquitectura.md:364`. |
| M5 — Pérdida máxima y reserva | **Cerrado** | Se distingue hasta cerrar y año completo con base mínima; reserva escalonada con autoridad del gate. `defense/objeciones.md:29`; `defense/objeciones.md:36`. |
| M6 — Cobertura de precio y licencia comercial | **Parcial** | Ruteo y denominador resueltos (R4); quedan frases que presentan las dos opciones como beneficios ya asegurados. `plan/annexes/05-business-case.md:875`, frente a `plan/slides.md:54`. |
| M7 — Inconsistencias entre fuentes y decisiones | **Parcial** | Mejoró G1 y el corte mixto; nuevas inconsistencias del intervalo y la atribución impiden cerrarlo. `plan/annexes/05-business-case.md:358`; `plan/annexes/05-business-case.md:508`; `plan/annexes/06-roadmap-riesgo.md:159`. |
| M8 — Madurez operativa solo enunciada | **Parcial** | El caso, los controles y los release gates ya están aplicados como diseño; falta integrar la política estadística con los escenarios que financia. `plan/annexes/02-arquitectura.md:297`; `plan/annexes/02-arquitectura.md:335`; N1. |
| M9 — Defensa sin evidencia humana | **Abierto** | Mismo pendiente de R10. `defense/objeciones.md:4`; `defense/evidence/index.md:11`. |
| m2 — Restos editoriales | **Abierto** | Persisten reglas competidoras de adopción, capacidad y gasto. `plan/annexes/02-arquitectura.md:212`; `plan/annexes/04-personas-cultura.md:161`; `plan/annexes/04-personas-cultura.md:388`. |
| m5 — Densidad ejecutiva | **Parcial** | El recorte de la slide 7 está cerrado; la extensión de anexos empeoró. `plan/slides.md:104`; `out/review-3/pdf-audit.log:2`. |

No reaparecieron los defectos ya cerrados de links locales, doble interpretación de rampa, extrapolación del piloto y falso positivo de TODO.
Los redondeos nuevos del corte mixto son menores y se identifican abajo; no invalidan los techos trimestrales reproducidos. `out/review-3/numeric.log:1`; `out/review-3/numeric.log:12`; `out/review-3/plan.log:1`.

### 1. Veredicto

**No aprobaría esta versión como entrega final; como borrador avanzado, 7/10 orientativo**, frente a 5/10 y 6,5/10 anteriores.
Mejoraron de manera comprobable las contingencias, la reserva, la señal comercial, el ruteo y la legibilidad del deck.
La mejora no alcanza para cerrar la integración: el escenario base promete gates que su nueva regla estadística no garantiza, y el replan desplaza evidencia exigida en G2.
Siguen pendientes la verificación humana, la defensa del equipo y la revisión conjunta de anonimización. La nota no surge de una rúbrica oficial con pesos, ausente en `material/conceptos/programa-evaluacion.md:36`.

### 2. Evaluación por los ocho criterios

| Criterio | Estado | Evidencia y faltante |
|---|---|---|
| 1. Consigna integral | **Parcial** | Están estrategia, arquitectura, gobierno, seguridad, personas, finanzas y roadmap de 12 meses. Hay opciones reversibles, cierres y frentes separados. Falta demostrar que las decisiones de cada gate son ejecutables con la capacidad y evidencia presupuestadas. `plan/slides.md:48`; `plan/annexes/06-roadmap-riesgo.md:135`; `plan/annexes/06-roadmap-riesgo.md:175`. |
| 2. Formato | **Cumple** | PDF único de 163 páginas y 1.426.710 bytes, diez slides incluidas portada/equipo. Índice y vínculos internos correctos en la auditoría. `out/review-3/pdf-audit.log:2`; `out/review-3/index-audit.log:1`. La longitud de los anexos afecta calidad, no el límite formal. |
| 3. Aplicación de la cursada | **Parcial** | Hay aplicación concreta de RICE, build/buy, harness/data contracts, gobierno, grafo humano-agente y cambio. Quedan débiles la validación del diagnóstico, la evidencia de valor de los primeros 100 días y costo por outcome. `plan/annexes/01-diagnostico.md:22`; `plan/annexes/06-roadmap-riesgo.md:97`; `plan/annexes/05-business-case.md:651`. |
| 4. Trazabilidad de cifras | **Parcial** | Las cifras de slides tienen cadena hacia anexos/fichas o propuestas identificadas. Techos, rampa, ROI y cierres principales se reproducen. Trazabilidad no equivale a validación humana; fallan 71 fichas directas. `out/review-3/numeric.log:1`; `out/review-3/plan-delivery.log:58`. N1/N2 afectan interpretación, no solo cuentas. |
| 5. Coherencia interna | **Parcial** | Hay una política integrada para reservas, ruteo y corte mixto. Permanecen diferencias E/B/F sobre intervalos y atribución, y B/D sobre documentación. `plan/annexes/05-business-case.md:358`; `plan/annexes/02-arquitectura.md:237`; `plan/annexes/04-personas-cultura.md:214`. |
| 6. Anonimización | **Parcial** | El chequeo textual estricto no encuentra patrones, y hay generalizaciones. No demuestra que el conjunto no permita reidentificar; siguen asociaciones comerciales y de producto, y una afirmación demasiado amplia en defensa. `out/review-3/leak.log:1`; `defense/objeciones.md:32`; B3 abajo. |
| 7. Chequeos automáticos | **Parcial** | Build, suite de 91 tests, leak y draft pasan. Los dos modos delivery rechazan el estado actual. Los primeros intentos de build/test tuvieron limitaciones de entorno; las repeticiones autorizadas pasaron. `out/review-3/tests-retry.log:1`; `out/review-3/build-retry.log:13`; sección 5. |
| 8. Calidad ejecutiva | **Parcial** | Storyline y G0 son claros; las diez slides tienen función de decisión o soporte. No observé recortes en los renders actuales. Slide 8 sigue densa; 152 páginas de anexos, repeticiones y notas de coordinación dificultan identificar la decisión vigente. `plan/slides.md:119`; `plan/annexes/05-business-case.md:854`; `out/review-3/slide-008.png`. |

#### Aplicación de la cursada: qué está aplicado y qué falta

| Contenido | Evaluación docente |
|---|---|
| M1U1: diagnóstico de madurez | Escala, dimensiones y evidencia están explicadas, pero es juicio de escritorio. No tiene entrevistas ni validación de quienes operan la empresa. No se exige sumar otro marco por nombre: falta validar el elegido. `plan/annexes/01-diagnostico.md:22`; `plan/annexes/01-diagnostico.md:91`. |
| M1U2: portfolio, RICE y build/buy | Aplicación real: alternativas, puntajes propuestos, no abrir P como opción y señal de cliente proporcionada a la etapa. RICE reproduce 0,60 / 0,11 / 0,13; no es evidencia de demanda. `plan/annexes/06-roadmap-riesgo.md:326`; `plan/annexes/02-arquitectura.md:376`; `out/review-3/numeric.log:16`. |
| M1U2: 100 días y kill/scale | La adaptación explicita qué entrega al día 90, compara capacidades equivalentes y evita inventar un quick win. Debe justificar el costo de esperar con una alternativa pequeña posterior a congelar la base; fijar rampa cero no demuestra imposibilidad. Las reglas de kill/scale mejoraron, pero necesitan N1/N3. `plan/annexes/06-roadmap-riesgo.md:97`; `plan/annexes/06-roadmap-riesgo.md:113`; `material/mapa-plan-fuentes.md:23`. |
| M1U3: contexto, harness y contratos de datos | Aplicado como diseño: fuentes, clasificación, acceso, trazas, abstención, evaluación y operación de un caso concreto. No se confunde con una implementación probada. `plan/annexes/02-arquitectura.md:297`; `plan/annexes/02-arquitectura.md:330`. |
| M1U4: Council/CoE, derechos de decisión y Governance Stack | Roles, cadencias, decisiones y capas de inversión están desarrollados. Falta asignar humanos, no otro organigrama conceptual. `plan/annexes/03-gobierno-seguridad.md:222`; `plan/annexes/03-gobierno-seguridad.md:243`; `material/mapa-plan-fuentes.md:18`. |
| M1U4 y M3U1: NIST, seguridad y compliance | Mapeo de riesgos a funciones, controles, residual y ejemplo operativo. El EU AI Act se usa condicionalmente; no se declara aplicable por defecto. ISO 42001 queda como opción, no certificación lograda. Las cautelas regulatorias deben permanecer visibles. `plan/annexes/03-gobierno-seguridad.md:73`; `plan/annexes/03-gobierno-seguridad.md:139`; `plan/annexes/03-gobierno-seguridad.md:330`. |
| M2U3: grafo humano-agente | Hay proceso antes/después y handoffs; constituye aplicación, no una cita decorativa. `plan/annexes/04-personas-cultura.md:140`; `material/mapa-plan-fuentes.md:21`. |
| M2U4: tokenomics, evals y AIOps | El modelo de costo y la prueba de portabilidad son concretos. Hay suite, versionado, degradación y rollback; el gate de impacto ya tiene acción. El costo por outcome sigue como fórmula futura, sin ejemplo numérico del caso ni un tope de FinOps cerrado. `plan/annexes/02-arquitectura.md:151`; `plan/annexes/02-arquitectura.md:335`; `plan/annexes/05-business-case.md:651`; `material/mapa-plan-fuentes.md:24`. |
| M3U2: literacy, champions y cambio | Se identifican poblaciones, horas, costo y conductas. Se reconoce que no se alcanza el OKR combinado. La postura laboral es una propuesta con excepciones, cuya aprobación y costo no están demostrados. `plan/annexes/04-personas-cultura.md:246`; `plan/annexes/04-personas-cultura.md:369`; `plan/annexes/04-personas-cultura.md:421`. |
| Defensa y evidencia | Storyline y objeciones preparadas; falta prueba humana. No corresponde penalizar la ausencia de un framework de una unidad cuyo material el propio corpus declara faltante. `material/mapa-plan-fuentes.md:27`; `defense/objeciones.md:4`; `defense/evidence/index.md:11`. |

Lo que sobra es coordinación histórica mezclada con decisión vigente y repetición de las mismas cifras en varios anexos.
Lo que falta no es una lista adicional de acrónimos: son validación humana, compatibilidad entre regla y escenario, y una unidad económica del caso aplicada. `plan/annexes/05-business-case.md:854`; `plan/annexes/05-business-case.md:651`.

#### Trazabilidad de todas las cifras de las slides

Se revisaron también cantidades de diseño, horizontes y niveles, además de los montos. No se halló una cifra material sin cadena de soporte; eso no certifica su verdad.
Se evita repetir combinaciones de datos comerciales del caso que no hacen falta para explicar un hallazgo.

| Slide / fuente | Cifras y soporte | Resultado |
|---|---|---|
| 1 — `plan/slides.md:22` | Año 2027, 12 meses, G0 por tres meses; equipo académico. `plan/annexes/06-roadmap-riesgo.md:50`; `plan/annexes/05-business-case.md:36`. | Horizonte coherente. No confundir aprobación inicial con autorización de todo el año. |
| 2 — `plan/slides.md:34` | Cinco puntajes de madurez, proporciones de adopción, ausencia de IA productiva, fecha de política, rangos de concentración/utilización. `plan/annexes/01-diagnostico.md:43`; `plan/annexes/01-diagnostico.md:56`; `context/hechos/uso-ia-interno.md:49`; `context/hechos/gobierno-y-politica-ia.md:21`. | Puntajes propuestos; hechos sin verificación humana. La combinación tiene riesgo residual de anonimización. |
| 3 — `plan/slides.md:48` | Dos frentes, un caso L1 y dos alternativas RICE. `plan/annexes/06-roadmap-riesgo.md:311`; `plan/annexes/06-roadmap-riesgo.md:332`. | Propuesta trazable. Cobertura de precio e ingreso se presentan como opciones, correctamente. |
| 4 — `plan/slides.md:60` | Al menos dos proveedores, T1/T2/T3, cero datos productivos de clientes, 12 meses y contratos mayores a 12 meses diferidos. `plan/annexes/02-arquitectura.md:90`; `plan/annexes/02-arquitectura.md:111`; `plan/annexes/02-arquitectura.md:396`. | Decisiones de arquitectura, no hechos observados. Ruteo ya condicionado a la modalidad comercial. |
| 5 — `plan/slides.md:75` | Cinco asientos, tres niveles de intake, cinco días hábiles, L1–L2 y gates T1/G2/G3. `plan/annexes/03-gobierno-seguridad.md:192`; `plan/annexes/03-gobierno-seguridad.md:243`; `plan/annexes/03-gobierno-seguridad.md:257`; `plan/annexes/03-gobierno-seguridad.md:118`. | Diseño trazable. Bloqueo y residual ahora se distinguen. |
| 6 — `plan/slides.md:91` | Piloto n=12, NPS +42, 17% de cursos, objetivo combinado 80%, un contractor. `context/hechos/encuesta-y-pilotos-ia.md:21`; `plan/annexes/04-personas-cultura.md:65`; `plan/annexes/04-personas-cultura.md:369`. | El piloto se delimita; no se extrapola a la empresa. El NPS es compatible con proporciones redondeadas de esa muestra. |
| 7 — `plan/slides.md:104` | Cuatro techos 33/62, 71/106, 59/78, 95/69; básico 90%, uso de Tecnología 80% y 85%; throughput 3%, 8%, régimen ~17%; espera seis semanas. `plan/annexes/05-business-case.md:98`; `plan/annexes/06-roadmap-riesgo.md:135`; `plan/annexes/06-roadmap-riesgo.md:187`; `plan/annexes/06-roadmap-riesgo.md:193`. | Techos reproducidos. La slide adopta límite inferior; E no lo aplica a su escenario base. |
| 8 — `plan/slides.md:119` | Caja 98–255/114–314; tiempo 115–320; ~3,5 FTE; G1 73/106/146; ROI negativo/caja cero; equilibrio 17%/23%; puente 2,8%; reserva 6/15; 590 h; pisos 1,6/2,2/2,2/2,1 y respaldo 2,5; base mínima 41 y T0 7. `plan/annexes/05-business-case.md:112`; `plan/annexes/05-business-case.md:203`; `plan/annexes/05-business-case.md:496`; `plan/annexes/05-business-case.md:825`; `out/review-3/numeric.log:1`. | Totales y techos principales correctos. FTE es equivalencia de tiempo reasignado, no disponibilidad demostrada. N2 invalida la suficiencia del puente; N3 condiciona el piso de T2. |
| 9 — `plan/slides.md:139` | Pesimistas −262/−300/−382/−502; base −84%; optimista −76%; shock 12× y 211–267; G4, L3, contratos >12 meses; excepción 0,3 frente al 0,2. `plan/annexes/05-business-case.md:622`; `plan/annexes/05-business-case.md:644`; `plan/annexes/06-roadmap-riesgo.md:238`; `out/review-3/numeric.log:5`; `out/review-3/numeric.log:15`. | Aritmética reproducida. El escenario base completo es condicional al paso de gates; la afirmación de que llega a G4 no está demostrada con el intervalo nuevo. |
| 10 — `plan/slides.md:156` | Ocho integrantes, G0 y referencia a slide 8; revisión y ensayo pendientes. `README.md:3`; `README.md:406`; `defense/objeciones.md:4`. | Identificación académica y estado explícito. Los roles sintéticos no reemplazan responsables humanos. |

#### Recálculo independiente de decisiones financieras

Cifras en miles de USD salvo indicación. Se recalcularon a partir de fracciones de dedicación, rangos de costo, gastos y contingencia; no se usó el total publicado como valor esperado.
Los logs conservan decimales; las cifras de presentación se redondean.

| Cuenta | Resultado reproducido | Juicio |
|---|---|---|
| Caja T1–T4, extremos | 12,9375–32,2 / 27,025–70,15 / 22,425–58,65 / 35,765–94,3 → techos 33/71/59/95 | Coincide. `out/review-3/numeric.log:1`. |
| Tiempo T1–T4, extremos | 22,3375–61,3125 / 33,7708–105,9042 / 30,0208–77,3292 / 26,8958–68,8292 → 62/106/78/69 | Coincide. `out/review-3/numeric.log:2`. |
| Año base, con T0 | Caja 98,1525–255,3; tiempo 114,825–320,075; costo económico medio 394,17625 | Coincide con rangos 98–255/115–320. Los rangos redondeados descriptivos no son los techos por gate. `out/review-3/numeric.log:3`. |
| Incremento de P | Caja 16,1–58,65; tiempo 22,5–56,25; costo medio 76,75 | Año con P: 470,92625. `out/review-3/numeric.log:4`. |
| Beneficio por escenario | Usando g × r / (1 + g × r): 12,18937 / 62,13132 / 114,10795 | ROI base −84,23768%; optimista con P −75,76946%. Son capacidad valorizada, no ingreso de caja. `out/review-3/numeric.log:5`. |
| Cierre G1/G2/G3, sin P | Cierre máximo 6/15/15; máximos hasta cerrar 106,2125 / 291,2667 / 427,2458; con base residual anual 146,45 / 330,0917 / 446,6583 | Reproduce la presentación 106/291/427 y 146/330/447. `out/review-3/numeric.log:8`. |
| Pesimista, espera que vence | Costo 264,6625; beneficio 3,08334; neto −261,57916 | Reproduce ~−262 bajo el supuesto de medio T3 usado para aproximar las seis semanas. `out/review-3/numeric.log:11`; `plan/annexes/05-business-case.md:622`. |
| Corte mixto G3 | Caja anual 204,6075; tiempo 228,5875; total 433,195; ahorro frente a P sin corte 37,73125 | Total 433 y ahorro 38 correctos. Tiempo debe redondear 229, no 228; ver m1. `out/review-3/numeric.log:12`. |
| Equilibrio de régimen | 142,5 / 997,5 = 14,2857% de horas; g = x/(1−x) = 16,6667%. Con 187,5 de régimen: 23,1481% | Correcto en la lectura de capacidad valorizada. El problema es inferirlo de un OKR observado sin descontar el control. `out/review-3/numeric.log:13`. |
| Cobertura a 6× y shock a 12× | Umbral de ahorro ponderado ~25,2874%; exposición anual a 12×: 211,2–267,3 | Coincide con ~25% y 211–267. No prueba que el proveedor o el gateway consigan ese ahorro. `out/review-3/numeric.log:15`. |
| Esfuerzo sin contractor y replan | 3,325 frente a 2,225 FTE clave de T2 | El respaldo de 0,3 nunca fue sustituto del contractor. La nueva contingencia lo reconoce. `out/review-3/numeric.log:17`. |
| Horas distribuidas de D | 2.620–2.860 h, valorizadas en 26,2–100,1 | Reproducido; no sumar estas personas de nuevo como si fueran una dotación disponible adicional. `out/review-3/numeric.log:20`. |

### 3. Hallazgos priorizados y correcciones propuestas

No se aplicó ninguna corrección al plan.

#### Bloqueantes de entrega o de liberación pública

**B1 — Sigue faltando validación humana de evidencia y responsabilidad académica.**

El chequeo global rechaza 156 fichas: 34 de contexto y 122 de material. El plan recorre 71 fichas directas sin verificar: 33 de contexto y 38 de material.
Además rechaza deck y seis anexos en draft y 48 coincidencias de pendientes. `out/review-3/okf-delivery.log:1`; `out/review-3/plan-delivery.log:1`.

Las 48 coincidencias no son 48 tareas independientes: incluyen cautelas, repetición de estados y expresiones como “sin evidencia”.
Tampoco se deben sumar las 71 fichas a las 156: son alcances superpuestos.

**Impacto:** impide aceptar esta versión como final bajo el contrato del repo, aunque el borrador sea valioso. El acuerdo del caso, responsables y ensayo siguen abiertos. `README.md:406`; `plan/slides.md:160`.
**Corrección:** responsables humanos revisan fuente y alcance, registran `verified` legítimo y resuelven pendientes sustantivos; luego se evalúan las marcas que el checker trata de forma textual. No corresponde reemplazar palabras o estados para hacerlo pasar.

**B3 — La revisión conjunta de anonimización sigue sin cierre, y la defensa exagera lo que se desvinculó.**

Persisten categorías de datos que, cruzadas, pueden reducir el anonimato: especialización comercial, estructura de oferta propia, madurez/estado de productos, relaciones cliente-producto y rasgos internos de operación.
No se afirma que identifiquen inequívocamente a una empresa ni se buscó la identidad real.

Evidencia de las categorías: `context/hechos/oferta-y-segmentos.md:24`; `context/hechos/estructura-de-ingresos.md:35`; `context/hechos/cartera-y-concentracion.md:40`; `context/hechos/stack-y-plataforma.md:43`.
Los anexos aún enlazan aliases de clientes con productos: `plan/annexes/02-arquitectura.md:226`; `plan/annexes/05-business-case.md:753`.

Eso contradice la respuesta “los anexos no asocian clientes con productos ni con calendarios” de `defense/objeciones.md:32`.
El antecedente sobre exposición histórica existe en `reviews/2026-10-13-docentes-codex.md:100`; **no se revalidó la historia publicada ni los remotos en esta corrida**.

**Impacto:** queda pendiente un criterio de liberación pública; leak-check en verde no lo resuelve.
**Corrección:** una persona autorizada revisa el conjunto, elimina asociaciones no necesarias para el razonamiento y corrige la respuesta de defensa. Tratar por separado el árbol actual y lo ya publicado; no publicar una receta de reidentificación en otro reporte.

#### Mayores

**N1 — El escenario base sigue decidiendo por estimado puntual, aunque los gates ahora deciden por límite inferior.**

E dice que +3,75% en T2 y +9% en T3 hacen pasar G2 y G3. F exige límites inferiores de +3% y +8%, con confianza 90% y semiancho máximo de 3 puntos.
`plan/annexes/05-business-case.md:355`; `plan/annexes/05-business-case.md:358`; `plan/annexes/06-roadmap-riesgo.md:159`; `plan/annexes/06-roadmap-riesgo.md:187`.

Contraejemplo compatible con esa precisión: 3,75 ± 3 da límite inferior 0,75; 9 ± 3 da 6. Ninguno pasa.
Para pasar con esos estimados e intervalos simétricos se necesitan semianchos ≤0,75 y ≤1, respectivamente. `out/review-3/numeric.log:18`.

No se afirma que esos sean los intervalos reales: todavía no existen. El contraejemplo prueba que el escenario base no puede presentarse como paso asegurado.
Además, la cohorte supuesta es de 15–20 personas y la regla pide aproximadamente 20; agregar seis semanas no agrega personas independientes. `context/supuestos/desarrolladores-en-equipos-propios.md:13`; `plan/annexes/02-arquitectura.md:240`.

**Impacto:** afecta presupuesto ejecutado, probabilidad de cierre y ROI del escenario que el board ve como base. E conserva también gates económicos expresados solo en puntos. `plan/annexes/05-business-case.md:827`; `plan/slides.md:145`.
**Corrección:** incorporar supuestos explícitos de dispersión/cohorte y simular espera/corte con la misma regla de F. Si no hay datos para calibrarlos, presentar el año completo como condicional y una sensibilidad de paso, sin inventar potencia ni precisión. Definir antes de G0 qué significa “~20”.

**N2 — El puente del OKR corrige la base temporal, pero todavía confunde crecimiento observado con atribuible.**

El puente `(1 + OKR) = (1 + d) × (1 + crecimiento contra T1)` es correcto para crecimiento observado.
B/F definen el estimador atribuible restando el cambio de un grupo no adoptante o la tendencia de T0. `plan/annexes/05-business-case.md:508`; `plan/annexes/02-arquitectura.md:237`; `plan/annexes/06-roadmap-riesgo.md:161`.

Contraejemplo ilustrativo, no dato del caso: con d = 0, OKR observado +20% y cambio del control +5 puntos, la resta definida por B deja +15% atribuible.
Cumple d <2,8% y el OKR, pero no el equilibrio de 16,67%. Por eso la condición de `plan/slides.md:128` y `defense/objeciones.md:42` no alcanza.

**Impacto:** el titular financiero puede prometer cobertura de régimen aun cuando la medición atribuible del propio plan no la logra.
**Corrección:** separar cambio observado, rebasing y ajuste contrafactual. Con la resta propuesta, exigir `1,20/(1+d) − 1 − c ≥ 0,1667`, definiendo c en la misma unidad. Si se elige otro estimador, actualizar fórmula, fichas, slide y defensa de manera consistente.

**N3 — El replan libera capacidad postergando documentación que B exige para aceptar los entregables de G2.**

D asigna el 0,2 del contractor a documentación/traspaso/coordinación, lo mueve a evals en CI y portabilidad en T2, y dice que la documentación se hace en T3–T4.
B dispone que un entregable de T2 sin documentación reproducible no cuenta para G2. `plan/annexes/04-personas-cultura.md:198`; `plan/annexes/04-personas-cultura.md:210`; `plan/annexes/02-arquitectura.md:364`.

No está definida una documentación mínima incluida dentro del 0,8 que permita satisfacer ambas instrucciones.
La excepción prevista si se descubre el faltante al cierre de T2 tampoco recupera automáticamente el trabajo que faltó en el trimestre. `plan/annexes/04-personas-cultura.md:222`.

**Impacto:** el piso de 2,2 FTE de T2 depende de una simultaneidad no resuelta entre producción de entregables y evidencia de aceptación; afecta continuidad y gate.
**Corrección:** distinguir documentación mínima reproducible para G2 de manuales/traspaso posteriores, con horas y responsables. Si esa carga no entra, activar el respaldo durante T2 con disparador anticipado, o quitar un entregable y propagarlo al gate.

**R10 vigente — El trabajo está preparado por agentes, pero todavía no defendido por el equipo.**

Las respuestas son más precisas y hay 30 objeciones, pero el documento afirma que no hubo ensayo, y no hay evidencia de validación individual ni responsables acordados.
`defense/objeciones.md:4`; `defense/objeciones.md:42`; `plan/slides.md:160`; `defense/evidence/index.md:11`.

**Impacto:** no se puede dar por satisfecha la preparación de defensa y apropiación académica.
**Corrección:** ensayo cronometrado y cruzado; cada integrante explica una cadena cifra–supuesto–decisión y responde una objeción de otra sección. Registrar observaciones y correcciones, sin fabricar consenso o verificaciones.

#### Menores y remanentes con impacto ejecutivo

| ID | Evidencia e impacto | Corrección propuesta |
|---|---|---|
| m1 — Redondeos nuevos del corte mixto | Tiempo anual 228,5875 debe presentarse como 229, no 228; tiempo de base mínima de P en T4 19,625 → 20, no 19. Ahorro de tiempo 28,2375 → ~28, no ~29. Total 433 y ahorro total ~38 están bien. `plan/annexes/05-business-case.md:613`; `plan/annexes/05-business-case.md:618`; `defense/objeciones.md:41`; `out/review-3/numeric.log:12`. Resta prolijidad y confianza, no cambia la decisión. | Recalcular desde componentes y redondear una sola vez; actualizar E, F y objeciones. |
| m2 — Reglas antiguas mezcladas con acuerdos nuevos | B mantiene ≥80% combinado como resultado esperado, mientras slide/D explicitan que no se alcanza; D atribuye a B 0,5 FTE en T1 donde B plantea alternativa interna de 0,3; D conserva el gate de licencias. E describe como pendientes integraciones ya hechas. `plan/annexes/02-arquitectura.md:212`; `plan/annexes/04-personas-cultura.md:161`; `plan/annexes/02-arquitectura.md:431`; `plan/annexes/04-personas-cultura.md:388`; `plan/annexes/05-business-case.md:856`. | Dejar una decisión vigente por concepto; distinguir objetivo organizacional, meta del plan y alternativa. Retirar coordinación histórica del entregable. |
| m3 — Beneficios opcionales vuelven a presentarse como certezas | E recomienda decir que se compra un tope de precio y controles pedidos por bancos, aunque slide 3 y C los condicionan a pruebas y contratos. `plan/annexes/05-business-case.md:875`; `plan/slides.md:54`; `plan/annexes/03-gobierno-seguridad.md:91`. | Uniformar el carácter de opción/hipótesis en todas las frases de defensa y fichas. |
| m4 — Adaptación de 100 días todavía argumentada con su propio supuesto | Rampa cero en T1 no prueba que un experimento después de semana 4 sea ruido. La comparación de capacidad ya es justa. `plan/annexes/06-roadmap-riesgo.md:97`; `plan/annexes/06-roadmap-riesgo.md:106`. | Comparar una prueba pequeña con herramientas existentes y datos habilitados, o reconocer expresamente que se posterga el aprendizaje de valor por preferencia de secuencia. No inventar un quick win para cumplir una etiqueta. |
| m5 — Costo por outcome sin aplicación numérica del caso | E define costo por PR aceptado, pero no lo calcula; B deja el tope de FinOps para más adelante. `plan/annexes/05-business-case.md:651`; `plan/annexes/02-arquitectura.md:335`. El contenido central está mencionado y diseñado, aún no aplicado económicamente. | Agregar una sensibilidad ilustrativa de volumen y aceptación, marcada como supuesto, y quién fija el tope antes del piloto. No presentar una cifra inventada como observada. |
| m6 — Síntesis y estabilidad de fuentes | 163 páginas y 268 enlaces a `main`; tablas de gates muy largas y reiteradas. `out/review-3/pdf-audit.log:2`; `plan/annexes/05-business-case.md:823`; `README.md:356`. | Reducir duplicación, conservar cálculo/evidencia útil y fijar un SHA publicado al generar la versión final; probar vínculos fuera del entorno local. |

### 4. Las ocho preguntas más difíciles del tribunal

1. Con +3,75% y un intervalo de ±3 puntos, G2 no pasa. Qué escenario presupuestario presentan y cuántas personas independientes les permiten esperar un intervalo suficientemente estrecho? `plan/annexes/05-business-case.md:358`; `plan/annexes/02-arquitectura.md:240`.
2. Si cumplen +20% contra T0 y el control mejora cinco puntos, cuánto queda atribuible a IA? Por qué el umbral d <2,8% sería suficiente? `plan/slides.md:128`; `plan/annexes/02-arquitectura.md:237`.
3. Quién documenta reproduciblemente los entregables de T2 antes de G2 si el mismo 0,2 FTE se reasignó a construirlos? Cuándo se activa el respaldo sin esperar al incumplimiento? `plan/annexes/04-personas-cultura.md:201`; `plan/annexes/02-arquitectura.md:364`.
4. Si el contractor no se contrata, qué evidencia de valor o de cobertura de precio puede llevar el modo control a G2, y qué condición justificaría seguir financiándolo? `plan/annexes/06-roadmap-riesgo.md:185`.
5. Si P sigue y el frente interno corta, por qué el ahorro es apenas ~38 frente a 471? Qué inversión realmente queda protegida por el gate y cuál depende del producto? `plan/annexes/05-business-case.md:601`; `plan/annexes/05-business-case.md:619`.
6. Qué observación de un cliente invalidaría el asistente elegido, aun después de aceptar un rango de precio? Quién puede cerrar el experimento y cómo evitan convertir interés en ingreso supuesto? `plan/annexes/06-roadmap-riesgo.md:323`; `plan/annexes/06-roadmap-riesgo.md:344`.
7. Si en el régimen de suscripción no conviene enrutar, qué prueba demuestra control compensatorio suficiente y qué afirmación de cobertura de precio retiran del board? `plan/annexes/02-arquitectura.md:111`; `plan/annexes/06-roadmap-riesgo.md:190`.
8. Qué integrante verificó qué fuente, quién aprobó el caso y qué evidencia permite afirmar que el conjunto publicado no expone relaciones internas? Cómo responderían sin apoyarse en que los agentes o leak-check dijeron que estaba bien? `plan/slides.md:160`; `defense/objeciones.md:32`; `defense/evidence/index.md:11`.

### 5. Chequeos ejecutados, evidencia y límites

Se activó la venv compartida indicada en el brief antes de usar Python y del build.
Estos son resultados de esta corrida; no se infirió el éxito a partir del historial.

#### Salidas resumidas

```text
$ bash scripts/leak-check.sh --all --strict
exit 0
✓ leak-check: revisión COMPLETA; sin hallazgos

$ bash scripts/okf-check.sh
exit 0
✓ okf-check: 159 archivos conformes en borrador; no implica aptitud para slides/entrega

$ bash scripts/okf-check.sh --delivery
exit 1
156 fichas rechazadas por revisión humana ausente:
34 context + 122 material.

$ python scripts/plan-check.py
exit 0
plan-check (draft): 10 slides; 48 pendientes; 164 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas

$ python scripts/plan-check.py --mode delivery
exit 1
plan-check (delivery): 10 slides; 48 pendientes; 164 referencias locales
ERROR: Entrega rechazada: deck declarado draft
[seis anexos declarados draft; 48 coincidencias de pendientes]
[71 fichas directas sin revisión humana: 33 context + 38 material]

$ python -m unittest discover -s tests
[repetición con Chrome habilitado]
...........................................................................................
----------------------------------------------------------------------
Ran 91 tests in 13.237s

OK
Shell verificado: GNU bash, version 3.2.57(1)-release (arm64-apple-darwin26)
Shell verificado: GNU bash, version 5.3.20(1)-release (aarch64-apple-darwin25.6.0)

$ bash scripts/build-deck.sh
[repetición autorizada]
out/entrega.pdf: 163 páginas, 1,426,710 bytes
```

Las líneas entre corchetes y los totales por carpeta son resúmenes del revisor, no citas literales del checker.
Salidas completas: `out/review-3/leak.log:1`; `out/review-3/okf.log:1`; `out/review-3/okf-delivery.log:1`; `out/review-3/plan.log:1`; `out/review-3/plan-delivery.log:1`; `out/review-3/tests-retry.log:1`; `out/review-3/build-retry.log:13`.

El primer intento de tests ejecutó 91 y terminó con un error al generar PDF con Chrome; el primer build falló al acceder a npm y su caché dentro de las restricciones.
Las repeticiones con permisos concedidos pasaron. No se atribuyen esos fallos iniciales a una regresión del repo. `out/review-3/tests.log:1`; `out/review-3/build.log:1`.

#### PDF y revisión visual

```text
PDF: 163 paginas; 1426710 bytes; deck 10
Links: 311 internos; 271 URI; file=0; private=0; main=268
Índice: destinos absolutos 12 / 17 / 52 / 79 / 100 / 132
Páginas de anexos correspondientes: 1 / 6 / 41 / 68 / 89 / 121
```

Evidencia: `out/review-3/pdf-audit.log:2`; `out/review-3/index-audit.log:1`.
Los seis destinos del índice coinciden con el inicio de los anexos. El PDF tiene enlaces internos reales; no depende de rutas locales para esa navegación.

Se abrieron los renders de las diez slides y las páginas absolutas 11, 107, 123 y 138 del PDF.
No observé texto recortado en las slides; la muestra de anexos es legible, aunque las tablas se fragmentan y ocupan varias páginas.

Evidencia visual: `out/review-3/slide-001.png` a `slide-010.png`, `out/review-3/page-11.png`, `page-107.png`, `page-123.png`, `page-138.png`.
No se inspeccionaron visualmente las 163 páginas; no se certifica ausencia de defectos en cada página de anexos.

#### Alcance de la verificación normativa

La [A 7777 del BCRA, sección 4.6](https://www.bcra.gob.ar/pdfs/comytexord/A7777.pdf) respalda obligaciones de identificar y gobernar IA usada por la entidad o terceros.
No demuestra que un cliente concreto compre IA o imponga una certificación al proveedor; C ahora separa esas afirmaciones. `plan/annexes/03-gobierno-seguridad.md:75`; `plan/annexes/03-gobierno-seguridad.md:91`.

La [página oficial de la Comisión Europea sobre el AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) consultada informa las fechas de diciembre de 2027 y agosto de 2028 para categorías de alto riesgo.
Esto es un contraste acotado de calendario, no revisión legal integral ni cotejo del texto consolidado de todas las normas. Las cautelas de `plan/annexes/03-gobierno-seguridad.md:79` siguen vigentes.

#### Límites y cierre del alcance

- Se revisó el material de cursada disponible en el repo; no se accedió al Notebook ni se pretendió que fichas draft sustituyan fuentes originales verificadas.
- No se buscó la empresa real, no se imprimió la denylist y no se transcribieron fuentes privadas.
- Los tests prueban la ejecución observada de la suite. No se hizo mutation testing: quitar guards requeriría editar fuentes, prohibido por este brief.
- No había un grafo Graphify disponible; se usó lectura y búsqueda textual dirigida. No se generó uno.
- No se editó el plan, scripts ni fichas; se generó `out/` y este reporte. No se hizo commit, push, PR, cambio de rama ni otra acción sobre publicación.
- En Codex se omite `lh metrics record-verify`, como indica el skill: no hay session id de Claude. La verificación se conserva en los logs y en este informe.

