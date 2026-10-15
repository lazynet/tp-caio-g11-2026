# Revisión docente cruzada, segunda corrida

Fecha: 2026-10-14. Estado: revisión de borrador; no habilita peer review ni entrega.
Versión revisada: rama `chore/anonimizar-acme`, commit `74ebece`.

## Metodología

Segunda corrida de la revisión docente cruzada descripta en
[la primera revisión](2026-10-13-docentes-codex.md): Codex CLI con `gpt-6-astra`
(OpenAI), reasoning `high`, en sesión nueva y solo lectura, con el rol del
equipo docente de la diplomatura. Esta vez se le pidió además contrastar la
versión corregida contra la revisión anterior (5/10), sin anclarse en ella: primero corrige desde
cero y después cierra cada hallazgo anterior (cerrado, parcial, abierto o empeoró).

Entre corridas, los agentes de rol del repo corrigieron sus anexos con un
orquestador que integró, corrió el gate y reprodujo los hallazgos críticos.
Los logs que cita en `out/` son locales y no se versionan.

## Reporte del revisor

Fecha: 2026-10-14. Árbol revisado: `74ebece8f30c787662cf4213446ed74c2824e9b2`, rama `chore/anonimizar-acme`. Revisión de solo lectura: no se corrigieron fuentes, no se crearon commits y no se modificó el estado de publicación.

Se examinó primero la versión actual y después el reporte anterior, sobre `3ed2875`. Las referencias `path:línea` corresponden al árbol actual, salvo las que apuntan al reporte anterior. Los logs y renders de esta revisión están en `out/re-review-*`, fuera del versionado.

### 0. Cierre de la revisión anterior

«Cerrado» significa que se resolvió el defecto señalado, no que se ejecutó el plan ni que una ficha quedó verificada por un humano. «Parcial» distingue avances concretos de condiciones todavía incumplidas.

#### Hallazgos anteriores

| ID | Estado | Evidencia actual y evaluación |
|---|---|---|
| B1 — Evidencia no habilitada para entrega | **Abierto** | Siguen sin revisión humana 156 fichas en el chequeo global: 34 de contexto y 122 de material. La entrega recorre 71 fichas directas sin verificar, además de deck y seis anexos en `draft`. `out/re-review-okf-delivery.log:1`; `out/re-review-plan-delivery.log:1`. Las dos fichas adicionales mejoran trazabilidad; no empeoran por sí mismas la calidad. |
| B2 — Enlaces locales del PDF | **Cerrado** | El PDF regenerado tiene 279 enlaces internos y 269 URI; ninguna URI `file://` ni destino a `private/`. El índice lleva a los seis anexos correctos. Queda la recomendación de fijar un commit publicado para los vínculos públicos, sin reabrir este defecto técnico. `out/re-review-pdf.log:4`; `README.md:359`. |
| B3 — Anonimización conjunta e historia | **Parcial** | Se generalizaron rasgos públicos y se retiró la serie mensual identificatoria. Persisten cruces de información comercial y de producto que requieren evaluación conjunta autorizada. No se revalidó la historia publicada ni se investigó la organización real. `context/hechos/oferta-y-segmentos.md:24`; `context/hechos/estructura-de-ingresos.md:35`; `context/hechos/cartera-y-concentracion.md:42`; `context/hechos/situacion-economica.md:37`. |
| M1 — Pesimista que no ejecutaba el gate | **Cerrado** | Ahora se simula la espera de seis semanas y su vencimiento: costo medio 265, capacidad liberada cercana a 3 y neto −262. Se distingue de cortar directamente en G2 y de esperar hasta G3. El supuesto de costo durante la espera es explícito. `plan/annexes/05-business-case.md:447`; `plan/annexes/06-roadmap-riesgo.md:157`. Hay otros conflictos entre gates, detallados abajo. |
| M2 — Producto sin selección | **Parcial** | Hay candidato, usuario, tarea y comparación RICE con dos alternativas y con no abrir P. Los puntajes se reproducen. La señal sigue siendo aceptación de una evaluación, insuficiente para afirmar disposición a pagar. `plan/annexes/06-roadmap-riesgo.md:263`; `:278`; `:283`; `:292`; `:304`. |
| M3 — Capacidad y pedido incompleto | **Parcial** | El pedido G0 ya expone caja, cierre, tiempo, horas distribuidas, piso de capacidad, base mínima y T0. El replan identifica tareas desplazadas y People lo reconoce como condicional. El respaldo de 2,5 FTE no cubre la ausencia total del contractor. `plan/slides.md:132`; `plan/annexes/02-arquitectura.md:408`; `plan/annexes/04-personas-cultura.md:198`; `plan/annexes/06-roadmap-riesgo.md:211`. |
| M4 — Dos significados de rampa | **Cerrado** | Se aplica `g × r / (1 + g × r)`. Beneficios anuales recalculados: 12,189 / 62,131 / 114,108 miles de USD. ROI base cercano a −84% y optimista con P cercano a −76%. `plan/annexes/05-business-case.md:275`; `out/re-review-numeric.log:8`. |
| M5 — Pérdida máxima y reserva | **Parcial** | G1 comunica 106 hasta cerrar y 146 en el año; G0 autoriza 6 de reserva y la base residual. El problema reaparece en G2/G3: el cierre llega a 15, mientras F dice que todo corte se paga con la reserva de G0. `plan/slides.md:127`; `plan/annexes/05-business-case.md:430`; `:609`; `plan/annexes/06-roadmap-riesgo.md:218`. |
| M6 — Cobertura de precio y licencia comercial | **Parcial** | Se comparan suscripción/API, se diseña una prueba y se condiciona la capa D a evidencia comercial o producto. Quedan incompatibilidades entre no enrutar bajo suscripción y exigir 90% de ruteo, denominadores distintos y una frase contractual categórica. `plan/annexes/02-arquitectura.md:151`; `:176`; `plan/annexes/06-roadmap-riesgo.md:159`; `plan/annexes/03-gobierno-seguridad.md:91`; `:401`. |
| M7 — Inconsistencias entre fuentes y decisiones | **Parcial** | Se aclaran T0 propuesto, infraestructura trimestral, contingencia, base prospectiva y continuidad mínima de G4. Persisten divergencias G1 entre E/F; la comparación del equilibrio con el OKR usa bases diferentes. `context/supuestos/convenciones-de-calculo.md:16`; `plan/annexes/05-business-case.md:633`; `plan/annexes/06-roadmap-riesgo.md:151`; `plan/slides.md:130`. |
| M8 — Madurez operativa solo enunciada | **Parcial** | Hay matriz NIST con responsables y residual, ejemplo completo de secreto, dataset de evals, versionado, drift y rollback. El gate de impacto carece de umbral, aunque habilita el paso a L2 junto con los otros tres. `plan/annexes/03-gobierno-seguridad.md:137`; `:151`; `plan/annexes/02-arquitectura.md:296`; `:300`; `:305`. |
| M9 — Defensa sin prueba humana | **Abierto** | El banco creció a 28 objeciones y la advertencia sobre herramientas es más honesta. Siguen pendientes responsables humanos, acuerdo y ensayo; el bundle de evidencia permanece vacío. `plan/slides.md:162`; `:164`; `defense/storyline.md:3`; `defense/evidence/index.md:11`. |
| m1 — Falso positivo de TODO | **Cerrado** | El modo borrador pasa con diez slides y el chequeo no vuelve a confundir el uso corriente en español con el marcador. La suite completa pasa. Esto acredita la ejecución observada, no resistencia a mutaciones del código. `out/re-review-plan.log:1`; `out/re-review-tests-escalated.log:1`. |
| m2 — Restos editoriales y coordinación | **Abierto** | Siguen cifras viejas del gateway, preferencias ya reemplazadas y notas que dicen que faltan fichas existentes. Algunas afectan decisiones, además de la edición. `plan/annexes/02-arquitectura.md:143`; `:564`; `plan/annexes/05-business-case.md:232`; `plan/annexes/04-personas-cultura.md:515`. |
| m3 — Redondeos y horas/FTE | **Cerrado** | Queda fijada la persona-trimestre de 480 h y se distinguen redondeos de estimaciones de techos autorizados. Los techos trimestrales de caja y tiempo se reproducen desde los componentes. `context/supuestos/convenciones-de-calculo.md:19`; `:21`; `out/re-review-numeric.log:1`. |
| m4 — Extrapolación de encuesta | **Cerrado** | La slide identifica `n=12`; D trata la muestra como piloto, sin extenderla a toda la organización. `plan/slides.md:93`; `plan/annexes/04-personas-cultura.md:65`. |
| m5 — Densidad y calidad ejecutiva | **Empeoró** | Mejora el contenido del pedido G0, pero la slide 7 corta la decisión y su enlace en el render. La entrega crece de 102 a 140 páginas; no viola un tope de anexos, aunque aumenta la carga de lectura. `plan/slides.md:106`; `:117`; `out/re-review-pdf.log:2`; `:6`; antecedente en `reviews/2026-10-13-docentes-codex.md:68`. |

#### Diez filas de aplicación de la cursada

| Fila / instrumento | Estado | Evaluación de aplicación, no de mera mención |
|---|---|---|
| M1U1 — Diagnóstico de madurez | **Parcial** | Se explica la escala, el juicio y sus fuentes, sin exigir AIMM además del marco elegido. Sigue siendo diagnóstico de escritorio, sin entrevistas ni validación humana. `plan/annexes/01-diagnostico.md:22`; `:31`; `:91`. |
| M1U2 — Build/buy y kill/scale | **Parcial** | Alternativas y bandas ahora son concretas. La independencia de frentes y el ruteo obligatorio todavía producen instrucciones incompatibles. `plan/annexes/02-arquitectura.md:330`; `plan/annexes/06-roadmap-riesgo.md:138`; `:159`; `:163`. |
| M1U2 — Portfolio, RICE y 100 días | **Parcial** | RICE está aplicado y el plan de 100 días declara una adaptación sin quick win de producto. Falta sustentar la señal de pago; la justificación de capacidad compara variantes con distinta provisión de IA aplicada. `plan/annexes/06-roadmap-riesgo.md:90`; `:96`; `:283`; `:292`. |
| M1U3 — Harness y data contracts | **Cerrado** | Se desarrolla un caso con flujo, contrato de datos, fuentes, acceso, abstención y operación. Es un diseño propuesto suficientemente aplicado para el trabajo, no una implementación probada. `plan/annexes/02-arquitectura.md:239`; `:281`; `material/conceptos/m1u3-data-contracts.md:24`. |
| M1U4 — Council, CoE, RACI y Governance Stack | **Cerrado** | Se asignan derechos de decisión, cadencias y capas de control, con presupuesto y alternativa mínima. Quedan decisiones humanas pendientes explícitas. `plan/annexes/03-gobierno-seguridad.md:187`; `:203`; `:223`; `:381`. |
| NIST / ISO / OWASP y seguridad | **Cerrado** | El registro mapea funciones y responsables; R4 recorre control, prueba, evidencia, residual y aceptación. C no presenta la correspondencia como certificación o auditoría de cláusulas. La generalización de la slide sobre bloqueo sigue siendo un defecto propio. `plan/annexes/03-gobierno-seguridad.md:137`; `:151`; `:160`. |
| M2U3 — Grafo humano-agente | **Cerrado** | Hay antes/después, seis pasos, handoffs, responsables y outcomes. Satisface el uso del método como propuesta; no demuestra beneficios medidos. `plan/annexes/04-personas-cultura.md:131`; `material/conceptos/m2u3-grafo-humano-agente.md:22`. |
| M2U4 — Tokenomics, evals y AIOps | **Parcial** | Mejoran sustancialmente datasets, métricas, versionado, drift y rollback. Falta una decisión de impacto y el cálculo económico del gateway mezcla denominadores; el costo por outcome queda como fórmula a instrumentar. `plan/annexes/02-arquitectura.md:151`; `:296`; `plan/annexes/05-business-case.md:473`; `material/conceptos/m2u4-versionado-release-gates.md:37`. |
| M3U2 — Literacy, champions y cambio | **Parcial** | Se concretan poblaciones, horas, costo, conducta y postura laboral. Se reconoce que no se alcanza el OKR combinado. La reubicación depende de un contractor aún no acordado y la postura laboral no tiene costo propio estimado. `plan/annexes/04-personas-cultura.md:203`; `:236`; `:351`; `:402`; `:416`; `:426`. |
| Marcos adicionales — ADKAR, AIMM, CAIE | **Cerrado** | No corresponde exigir acumulación de siglas ni convertir artefactos de certificación individual en requisitos del TIF. La decisión de usar los marcos que tienen aplicación y fuente es defendible. `plan/annexes/01-diagnostico.md:91`; `material/huecos.md:19`; `material/conceptos/programa-evaluacion.md:36`. |

### 1. Veredicto

**6,5/10 orientativo, frente a 5/10 en la revisión anterior.** Hay mejora sustancial: producto elegido, cálculo corregido, G0 visible, controles aplicados y PDF navegable.

**Sigue siendo un borrador; no está listo para peer review ni entrega bajo el contrato del repo.** Faltan revisión humana y ensayo, y permanecen contradicciones que cambian capacidad, desembolsos y decisiones de los gates.

El principal problema ya no es la falta de desarrollo: es la integración. Sumar anexos no resuelve las decisiones incompatibles, y la slide 7 pierde parte de su resolución en el PDF.

### 2. Evaluación por criterio

Las notas por criterio son diagnósticas; no constituyen una rúbrica oficial ni un promedio aritmético de aprobación.

| Criterio | Nota orientativa | Evaluación |
|---|---:|---|
| Consigna | 8/10 | Plan de doce meses para toda la organización, con estrategia, arquitectura, gobierno, personas, finanzas y defensa. El alcance está cubierto; el acuerdo humano sigue pendiente. `plan/slides.md:22`; `:162`; `material/programa.md:18`. |
| Formato | 6/10 | Diez slides y un PDF de 1.308.187 bytes: cumple límites formales. La slide 7 desborda; hay 129 páginas de anexos más un índice. `out/re-review-pdf.log:2`; `:3`; `:6`. |
| Aplicación de la cursada | 7,5/10 | RICE, governance, harness, evals y grafo humano-agente ya tienen desarrollo propio. Impacto y economía por outcome todavía no cierran como criterios operables. `plan/annexes/06-roadmap-riesgo.md:292`; `plan/annexes/02-arquitectura.md:300`; `plan/annexes/05-business-case.md:475`. |
| Trazabilidad y cifras | 6,5/10 | Las cuentas principales cierran y el PDF enlaza la evidencia. Ninguna de las fichas exigidas por delivery tiene verificación humana; hay una comparación económica con bases diferentes. `out/re-review-numeric.log:1`; `out/re-review-plan-delivery.log:1`; `plan/slides.md:130`. |
| Coherencia del plan | 5/10 | Mejoran rampa, T0 y G4. Siguen mal definidos el respaldo sin contractor, el cierre tardío, la dependencia B/P y el ruteo bajo suscripción. `plan/annexes/06-roadmap-riesgo.md:159`; `:163`; `:211`; `:218`. |
| Anonimización | 6/10 provisional | Hay generalización real y el scanner estricto no encuentra patrones. Eso no certifica anonimización por combinación ni remedia la historia publicada. `out/re-review-leak.log:1`; `context/hechos/estructura-de-ingresos.md:35`; `reviews/2026-10-13-docentes-codex.md:100`. |
| Chequeos y reproducibilidad | 8/10 | Borrador válido, 91 tests aprobados y build completo reproducido con Chrome fuera del sandbox. Delivery falla por condiciones reales pendientes. Los chequeos no detectaron el desborde ni las contradicciones de negocio. `out/re-review-tests-escalated.log:1`; `out/re-review-build-escalated.log:13`; `out/re-review-pdf.log:6`. |
| Calidad ejecutiva y defensa | 5,5/10 | El board ya ve el pedido G0 y la pérdida anual de G1. Se mantiene densidad excesiva, afirmaciones más fuertes que la evidencia y ausencia de ensayo humano. `plan/slides.md:127`; `:132`; `:164`; `defense/evidence/index.md:11`. |

### 3. Hallazgos actuales y correcciones propuestas, no aplicadas

#### Bloqueantes para entrega o publicación

##### B1 vigente — La entrega todavía no tiene evidencia revisada por humanos

**Evidencia:** `out/re-review-okf-delivery.log:1` registra 156 fichas sin revisión; `out/re-review-plan-delivery.log:1` falla por deck/anexos `draft`, 45 ocurrencias pendientes y 71 fichas directas sin verificar. `plan/slides.md:162` mantiene dueños humanos pendientes.

Las 45 ocurrencias no equivalen a 45 tareas independientes: incluyen advertencias como «sin evidencia». No corresponde borrarlas para que el chequeo quede verde ni cambiar `status` sin revisar fuentes y alcance.

**Impacto en la nota:** impide considerar aprobado el entregable final conforme a las reglas acordadas. No demuestra que cada cifra sea falsa; demuestra que falta la revisión requerida.

**Corrección:** asignar revisores, verificar las fichas que sostienen la entrega y registrar persona, fecha y alcance reales. Resolver las decisiones abiertas antes de declarar el deck listo. Responsabilidad: equipo humano, coordinado por CAIO.

##### B3 vigente, parcial — No está cerrado el tratamiento de anonimización e historia

**Evidencia:** se generalizaron atributos en `context/hechos/oferta-y-segmentos.md:24` y la serie mensual en `context/hechos/situacion-economica.md:37`. Permanecen relaciones entre cartera, características de productos, hitos y estructura en `context/hechos/cartera-y-concentracion.md:42`, `context/hechos/estructura-de-ingresos.md:35` y `context/hechos/tamano-y-estructura.md:25`.

El antecedente sobre exposición histórica está en `reviews/2026-10-13-docentes-codex.md:100`. Esta revisión no volvió a inspeccionar valores sensibles de commits antiguos ni verificó remotos, forks o caches. No se identificó ni buscó a la organización real.

**Impacto en la nota:** la generalización merece crédito, pero no permite afirmar que el caso esté anonimizado de punta a punta. Sigue pendiente una condición de publicación responsable, distinta de la calidad del business case.

**Corrección:** revisión conjunta por una persona autorizada, suprimiendo relaciones innecesarias para la decisión; registrar el riesgo residual de lo ya publicado por separado. No reescribir historia ni publicar detalles sensibles desde este reporte.

#### Mayores

##### R1 — La contingencia sin contractor subestima la capacidad necesaria

**Evidencia:** B requiere 0,8 FTE de IA aplicada en T2–T4 y dice que el contractor los reemplaza (`plan/annexes/02-arquitectura.md:384`). Sin él, B solo ya demanda 2,3 FTE en T2 (`:408`). F, sin embargo, promete resolver su ausencia con 2,5 FTE totales y una excepción de 0,3 (`plan/annexes/06-roadmap-riesgo.md:211`); D repite esa conclusión (`plan/annexes/04-personas-cultura.md:218`).

El recálculo con los demás roles da aproximadamente **3,325 FTE clave en T2 sin contractor**, antes de cualquier compensación por caja ahorrada: 2,3 de B más 0,45 de gobierno, 0,375 de actividades clave y 0,2 de liderazgo de cambio. Evidencia del cálculo: `out/re-review-numeric.log:17`.

La excepción de 2,5 puede respaldar que el contractor exista, pero no ceda el 0,2 para evals/portabilidad. No cubre que falte también su 0,8 principal. People ya advierte correctamente que ese 0,2 tiene tareas asignadas (`plan/annexes/04-personas-cultura.md:198`).

**Impacto en la nota:** afecta ejecutabilidad y credibilidad del pedido G0; el board cree aprobar un respaldo que no alcanza.

**Corrección:** separar contingencias «sin 0,2 adicional» y «sin contractor». Para la segunda, recalcular alcance, roles, caja y tiempo; o convertir la contratación en condición de no inicio de esos hitos. Integrar B/D/E/F y la slide 8.

##### R2 — La reserva de cierre solo cubre el primer corte

**Evidencia:** G0 autoriza 6 de caja para cierre (`plan/annexes/05-business-case.md:609`). Los costos de cierre de G2 y G3 llegan a 15; F manda pagarlos con esa misma reserva (`plan/annexes/06-roadmap-riesgo.md:218`). El recálculo reproduce 2,417–6 en G1 y 6–15 en G2/G3 (`out/re-review-numeric.log:14`; `:15`; `:16`).

**Impacto en la nota:** queda una brecha de autorización de hasta **9 mil de caja** en un corte posterior. Los techos de ejecución no demuestran por sí mismos que esa reserva esté disponible cuando se rechaza continuar.

**Corrección:** autorizar y mantener una reserva de cierre actualizada antes de asumir cada nuevo compromiso, con renglón y autoridad explícitos. Distinguirla del gasto operativo y de la base mínima. El máximo de G1 ya está bien comunicado; no volver a mezclarlo con el máximo anual.

##### R3 — E y F no resuelven qué pasa cuando falla un frente y otro puede continuar

**Evidencia:** F declara independencia de frentes (`plan/annexes/06-roadmap-riesgo.md:138`), pero el fallo de throughput en G3 corta I **y B** (`:163`), mientras P puede continuar si supera su SLO (`:166`). P utiliza servicios comunes definidos por B. No hay presupuesto ni regla de precedencia para ese escenario mixto.

Además, E resume como corte el incumplimiento de G1 (`plan/annexes/05-business-case.md:633`), mientras F permite espera por falta de base, revisión contractual hasta mes 4 y restricciones específicas por frente (`plan/annexes/06-roadmap-riesgo.md:151`). La referencia a F no elimina la orden contradictoria del cuadro económico.

**Impacto en la nota:** afecta integración y roadmap ajustado por riesgo. Un CFO y un responsable técnico pueden ejecutar decisiones diferentes leyendo anexos distintos.

**Corrección:** fijar precedencia de seguridad, dependencias y caja; definir el mínimo de B que necesita P cuando se corta I; costear ese escenario y hacer que E sea una proyección fiel de la tabla de F.

##### R4 — La prueba económica del gateway y el gate de ruteo no usan la misma política

**Evidencia:** B dispone no enrutar el agente mientras la suscripción sea plana y rechaza hacerlo si rompe esa suscripción (`plan/annexes/02-arquitectura.md:176`). F exige que al menos 90% de sus eventos pasen por gateway (`plan/annexes/06-roadmap-riesgo.md:159`); C mantiene esa exigencia (`plan/annexes/03-gobierno-seguridad.md:351`).

También difieren los denominadores: B mide `f` sobre eventos de cuatro superficies, y `s` sobre costo de tareas del agente de código (`plan/annexes/02-arquitectura.md:151`). E calcula el umbral con el gasto del agente, no con el costo conjunto ponderado de las cuatro superficies (`plan/annexes/05-business-case.md:352`). Multiplicarlos no estima automáticamente ahorro monetario sobre esa base.

B conserva además umbrales viejos de 55% / 37% / 18% (`plan/annexes/02-arquitectura.md:143`), aunque E ya adopta aproximadamente 38% / 25% / 13% para 4× / 6× / 12×. La cifra de 25% a 6× sí se reproduce: `33 / (6 × 21,75)`.

**Impacto en la nota:** puede forzar un cambio que encarezca el servicio para cumplir un gate, o declarar cobertura económica con una medición no comparable.

**Corrección:** condicionar el ruteo del agente al régimen comercial y separar controles de superficies que no enrutan. Calcular ahorro sobre gasto elegible, con la misma población y precios que el modelo financiero; sincronizar umbrales y reglas B/C/E/F.

##### R5 — El equilibrio de 17% está bien calculado; la comparación con el OKR no está demostrada

**Evidencia:** la convención distingue línea de base prospectiva de T1 y OKR contra T0 (`context/supuestos/convenciones-de-calculo.md:16`). La slide afirma que el equilibrio está tres puntos por debajo del OKR y que la meta lo cubre (`plan/slides.md:130`); E y defensa repiten la inferencia (`plan/annexes/05-business-case.md:398`; `defense/storyline.md:56`).

El cálculo financiero da 16,67% sin P y 23,15% con P. Pero comparar esos porcentajes directamente con +20% requiere igualar o convertir las bases; esa relación no está medida ni declarada como supuesto. La cautela sobre tamaño/costo de cohorte no resuelve esta diferencia.

**Impacto en la nota:** debilita una de las pocas afirmaciones favorables del financial storytelling. La resta de puntos porcentuales es aritméticamente simple, pero conceptualmente no está habilitada.

**Corrección:** expresar meta y equilibrio sobre una misma base, mostrando el puente T0→T1; hasta entonces, presentar el umbral como exigencia económica independiente. No atribuir al plan mejoras previas a la intervención.

##### R6 — La hipótesis de producto está elegida, pero todavía no prueba disposición a pagar

**Evidencia:** el candidato y las alternativas se describen en `plan/annexes/06-roadmap-riesgo.md:263`; los RICE de 0,60 / 0,11 / 0,13 son reproducibles (`:292`). La señal G2 consiste en aceptar evaluar un piloto sin compromiso vinculante (`:283`), pero el texto dice que la opción «prueba disposición a pagar» (`:304`).

**Impacto en la nota:** el avance respecto de M2 es real, pero la tesis de producto sigue sobrevalorada. Aceptar una evaluación acredita interés exploratorio; no valida precio, presupuesto ni comprador.

**Corrección:** definir una señal comercial proporcional a la etapa —por ejemplo, interlocutor con presupuesto y aceptación de un rango de precio sujeto a resultados— o cambiar el claim a interés exploratorio. Mantener el costo de aprendizaje y el criterio de abandono visibles; no inventar ventas del año 1.

##### R7 — El cuarto release gate no decide, y el gate económico carece de precisión estadística definida

**Evidencia:** el caso de referencia tiene dataset, umbrales técnicos, seguridad, ética, revisión humana y rollback. El gate de impacto dice que se mide, pero no tiene umbral de salida (`plan/annexes/02-arquitectura.md:300`); la escalera exige pasar los cuatro para L2 (`:305`). El material distingue cuatro decisiones de release (`material/conceptos/m2u4-versionado-release-gates.md:37`).

Para throughput se proponen estratos y controles de calidad (`plan/annexes/02-arquitectura.md:199`), pero F decide según si un intervalo cruza +3% o +8% sin fijar método, confianza o precisión mínima (`plan/annexes/06-roadmap-riesgo.md:143`). Un promedio de escenario superior al umbral no garantiza pasar el gate.

**Impacto en la nota:** permite aprobar «cuatro gates» cuando uno carece de regla y dificulta ejecutar los económicos de forma repetible. No se exige una medición real en un plan futuro; sí especificar cómo decidir con los resultados.

**Corrección:** definir criterio de impacto o reconocer formalmente que es un piloto de aprendizaje sin escalado por valor demostrado. Proponer método y calidad mínima del intervalo de throughput, con respuesta a muestra insuficiente. Validarlos con los responsables humanos antes de G0/G2, según corresponda.

##### R8 — La slide promete un bloqueo que el propio anexo declara inexistente en algunas superficies

**Evidencia:** `plan/slides.md:79` presenta secretos siempre bloqueados. C registra que las superficies sin pasarela no bloquean y considera ese resultado esperado, sujeto a aceptación residual (`plan/annexes/03-gobierno-seguridad.md:155`).

**Impacto en la nota:** el board puede interpretar una prohibición de uso como una garantía técnica. La transparencia del anexo es buena, pero queda desmentida por la síntesis ejecutiva.

**Corrección:** distinguir prohibición, bloqueo técnico y controles compensatorios por superficie. Llevar el riesgo residual relevante a la decisión del board, sin afirmar cobertura preventiva total.

##### R9 — La slide 7 pierde su decisión en el único entregable

**Evidencia:** al abrir el render de las diez slides, la 7 muestra cortada la decisión final y su enlace inferior. Fuente: `plan/slides.md:106` y `:117`; artefacto: `out/re-review-slide-007.png`; registro: `out/re-review-pdf.log:6`.

**Impacto en la nota:** defecto de entrega, además de calidad ejecutiva. Que Marp cuente diez páginas y que los enlaces existan en las anotaciones no hace visible el texto cortado.

**Corrección:** reducir el contenido de esa slide a decisiones e hitos principales y trasladar detalle al anexo existente. Regenerar y abrir el PDF; no resolverlo solo bajando tipografía. No se propone una undécima slide.

##### R10 — La defensa humana continúa pendiente

**Evidencia:** `defense/evidence/index.md:11` no contiene ensayo; `plan/slides.md:162` no asigna dueños humanos; `defense/storyline.md:3` conserva cautelas. El uso de herramientas en el repo no prueba que los seis roles funcionen de punta a punta ni que el equipo domine el plan (`plan/slides.md:164`).

**Impacto en la nota:** limita la evaluación de dominio, síntesis, manejo de contradicciones y respuesta al CFO. No se exige haber implementado el plan 2027; sí defender sus decisiones.

**Corrección:** acordar alcance y responsables, ensayar con tiempos y registrar respuestas/correcciones anonimizadas. Resolver primero R1–R8 para no entrenar respuestas incompatibles.

#### Menores y remanentes editoriales

| Hallazgo | Evidencia | Impacto en la nota | Corrección propuesta |
|---|---|---|---|
| Atribución vieja del ahorro pesimista | `plan/annexes/05-business-case.md:465` dice 120 por gates, pero `:468` conserva «~180» y atribuye la mayor parte a diferir producto. Con los escenarios actuales, 480−262≈218: 120 por gates y 98 por diferir P. | Resta confianza al relato, aunque la tabla principal está corregida. | Rehacer el puente entre escenarios con idéntico alcance. |
| Restos de coordinación | B dice que no se actualizaron fichas de precios que ya contemplan la variante; E conserva la preferencia interna reemplazada por contractor; D dice que faltan fichas de poblaciones existentes. `plan/annexes/02-arquitectura.md:564`; `plan/annexes/05-business-case.md:232`; `plan/annexes/04-personas-cultura.md:515`. | Hace difícil saber cuál decisión manda. | Barrido editorial por afirmación y concepto, después de integrar las decisiones. |
| Interés contractual presentado como certeza | `plan/annexes/03-gobierno-seguridad.md:91` afirma lo que pedirán los bancos; `:401` establece correctamente que hay que buscar esa evidencia. | Debilita la prudencia de la tesis comercial. | Usar hipótesis condicionada a evidencia contractual; separar requisito regulatorio del cliente y exigencia comercial al proveedor. |
| Costo «máximo» con valor medio | `plan/annexes/06-roadmap-riesgo.md:282` rotula como máximo 37 y 39 con rangos cuyos extremos superiores son mayores. | Ambigüedad para quien aprueba el tramo de P. | Rotular medio/rango y separar techos autorizados. |
| Gate sobre seats sin expansión financiada | `plan/annexes/06-roadmap-riesgo.md:158` frena una expansión; E dice que el plan no suma seats (`plan/annexes/05-business-case.md:455`). | La condición puede carecer de efecto presupuestario. | Identificar gasto o acción que realmente se frena, sin cortar controles necesarios. |
| Justificación incompleta de la adaptación de 100 días | F compara T1-a con carga interna frente a T1-b con contractor (`plan/annexes/06-roadmap-riesgo.md:96`); B distingue ambas provisiones (`plan/annexes/02-arquitectura.md:392`; `:463`). | No prueba que toda alternativa de quick win sea inviable. | Comparar alternativas con igual capacidad y costo; se puede justificar la adaptación sin prometer un quick win ficticio. |
| Vínculos públicos dependientes de `main` | El PDF tiene 266 vínculos a esa referencia mutable (`out/re-review-pdf.log:4`); README ya permite fijar un SHA (`README.md:359`). | La evidencia puede cambiar después de entregar. | Para la versión final, construir con un commit publicado y comprobar acceso desde fuera del entorno. |
| Anexos excesivamente extensos | 140 páginas: diez slides, índice y 129 páginas de anexos (`out/re-review-pdf.log:2`). La muestra visual de tablas es legible, pero larga. | Penalización de síntesis, no infracción de un límite formal de páginas de anexos. | Concentrar evidencia procesada y decisiones; retirar instrucciones editoriales resueltas. |

#### Auditoría de cifras de las diez slides

Esta tabla distingue consistencia numérica de validación del dato. Las cifras de contexto y los umbrales propuestos siguen en `draft`; un vínculo correcto o una cuenta que cierra no los convierte en hechos verificados.

| Slide / referencia | Cifras y recorrido | Resultado |
|---|---|---|
| 1 — `plan/slides.md:22` | Horizonte 2027, doce meses; G0 libera tres meses. `plan/annexes/05-business-case.md:36`; `plan/annexes/06-roadmap-riesgo.md:50`. | Coherente con T1–T4 y el pedido por tramo. Grupo/equipo es identificación académica. |
| 2 — `plan/slides.md:34` | Puntajes de madurez, adopción por área, ausencia de IA productiva, concentración y utilización. `plan/annexes/01-diagnostico.md:43`; `:56`; `context/hechos/uso-ia-interno.md:49`; `context/hechos/ia-en-producto-y-oferta.md:21`. | Trazabilidad presente; madurez propuesta y datos sin verificación humana. No se reproducen acá combinaciones comerciales innecesarias. |
| 3 — `plan/slides.md:50` | Dos frentes, nivel L1 y alternativas de producto. `plan/annexes/06-roadmap-riesgo.md:263`; `:292`. | RICE 0,60 / 0,11 / 0,13 reproducido; selección razonable como hipótesis, no validación de pago. |
| 4 — `plan/slides.md:62` | Dos proveedores, cuatro superficies, tres sin ruta general por gateway, horizonte sin fine-tuning/datos de clientes y contratos largos. `plan/annexes/02-arquitectura.md:90`; `:138`; `:350`. | Son decisiones de diseño propuestas. Falta condicionar coherentemente la cobertura al régimen comercial. |
| 5 — `plan/slides.md:77` | Council de cinco, tres niveles, intake de cinco días, L1/L2, capa D condicional. `plan/annexes/03-gobierno-seguridad.md:187`; `:243`; `:257`; `:388`. | Estructura trazable; el claim de bloqueo universal excede los controles disponibles. |
| 6 — `plan/slides.md:93` | Muestra de 12, NPS 42 y 17% con curso; metas de adopción y contractor. `context/hechos/encuesta-y-pilotos-ia.md:21`; `:25`; `:28`; `plan/annexes/04-personas-cultura.md:351`. | NPS consistente con porcentajes redondeados; muestra correctamente delimitada. Se reconoce que no se alcanza 80% combinado. |
| 7 — `plan/slides.md:106` | Techos caja/tiempo por trimestre, metas de formación/adopción, gates +3%/+8%, espera de seis semanas y base anual 53. `plan/annexes/05-business-case.md:98`; `:630`; `plan/annexes/06-roadmap-riesgo.md:147`. | Techos reproducidos. Subsisten conflictos de decisión R3/R4; la decisión inferior queda cortada en el PDF. |
| 8 — `plan/slides.md:125` | Caja 98–255 o 114–314 con P; tiempo 115–320; corte G1 73/106/146; equilibrio 17%/23%; G0 33+6, 62, 590 h, pisos y T0. `plan/annexes/05-business-case.md:112`; `:140`; `:203`; `:398`; `:430`; `:603`. | Totales y redondeos principales correctos. R1/R2 afectan contingencias; R5 afecta comparación con OKR. Los ~3,5 FTE son equivalencia media de costo/tiempo, no personas adicionales disponibles. |
| 9 — `plan/slides.md:145` | Pesimista −262, alternativa −300, estrés −382/−502, ROI −84%/−76% y shock anual 211–267. `plan/annexes/05-business-case.md:326`; `:379`; `:447`. | Coherencia aritmética verificada; el shock anual no debe confundirse con el incremental desde T3. La clasificación de decisiones se desarrolla en F. |
| 10 — `plan/slides.md:160` | Ocho integrantes y responsables pendientes; dogfooding. `README.md:1`; `defense/storyline.md:3`; `defense/evidence/index.md:11`. | Identificación de equipo, no evidencia de asignación de dueños ni de ensayo. El texto ya reconoce límites de las pruebas de herramientas. |

#### Recálculo independiente del modelo

Unidades monetarias: miles de USD. Se usaron componentes, fracciones por rol y convenciones del repo; no se cotizaron precios nuevos ni se incorporaron datos privados. Resultados detallados en `out/re-review-numeric.log:1`.

| Magnitud | Resultado recalculado | Evaluación |
|---|---|---|
| Caja T1–T4, rangos | 12,9375–32,2; 27,025–70,15; 22,425–58,65; 35,765–94,3 | Techos 33 / 71 / 59 / 95 correctos. |
| Tiempo T1–T4, rangos | 22,3375–61,3125; 33,7708–105,9042; 30,0208–77,3292; 26,8958–68,8292 | Techos 62 / 106 / 78 / 69 correctos. |
| Caja anual base | 98,1525–255,3 | 98–255 es rango estimado redondeado; no confundirlo con suma de techos autorizados. |
| Tiempo anual, incluido T0 | 114,825–320,075 | 115–320 correcto. |
| Costo económico medio base | 394,17625 | ~394 correcto; no es todo caja. |
| Incremental P | Caja 16,1–58,65; tiempo 22,5–56,25 | Medios ~37 y ~39 correctos para P diferido; los extremos no son esos medios. |
| Beneficio pesimista/base/optimista | 12,1894 / 62,1313 / 114,1080 | Conversión de rampa corregida. Son capacidad valorizada, no caja. |
| ROI base y optimista con P | −84,24% / −75,77% | Titulares −84% / −76% correctos. |
| G1, hasta cerrar / año completo, máximos | 106,2125 / 146,45 | Estimaciones 106 / 146 conformes a convención de redondeo; autorización separada de reserva necesaria. |
| G2, hasta cerrar / año completo, máximos | 291,2667 / 330,0917 | Valores de E reproducidos. Cierre máximo 15 no cubierto por reserva 6. |
| G3, hasta cerrar / año completo, máximos | 427,2458 / 446,6583 | Valores de E reproducidos. Misma brecha de reserva. |
| Pesimista con espera vencida | Costo ~265, beneficio ~3, neto ~−262 | Compatible con el supuesto explícito de financiar medio T3 sin P y conservar la base mínima. |
| Equilibrio a régimen | 16,67% sin P; 23,15% con P | Matemática correcta; comparación contra OKR pendiente de convertir bases. |
| Gateway, umbral medio a 6× | 25,29% | E/F usan ~25%; B conserva otro valor y mezcla denominadores en la prueba. |
| Shock 12× incremental anual | 211,2–267,3 | Rango 211–267 correcto; representa exposición anual, no factura observada. |
| FTE T2 sin contractor | ~3,325 | Refuta el respaldo total de 2,5 FTE para esa contingencia. |

La suma de componentes no prueba cotizaciones ni disponibilidad de personas. Los rangos económicos y las fracciones son supuestos pendientes de verificación; las restricciones humanas siguen siendo condiciones de G0.

### 4. Ocho preguntas difíciles para la defensa

1. **CFO:** Si el contractor no se aprueba, B solo pide 2,3 FTE en T2. Cómo llegan a 2,5 sumando gobierno y cambio, y qué dejan de hacer si el total es ~3,3? (`plan/annexes/02-arquitectura.md:408`; `plan/annexes/06-roadmap-riesgo.md:211`).
2. **CFO:** Quién autoriza los 9 mil adicionales si G2 corta y el cierre cuesta 15, cuando G0 reservó 6? Qué obligación queda contraída antes de esa decisión? (`plan/annexes/05-business-case.md:609`; `plan/annexes/06-roadmap-riesgo.md:218`).
3. **Board:** Si el piloto pasa su SLO y el frente interno queda por debajo de +5%, continúan P o cortan B? Con qué infraestructura, personas y presupuesto? (`plan/annexes/06-roadmap-riesgo.md:138`; `:163`; `:166`).
4. **Arquitectura y Finanzas:** Si la suscripción sigue siendo plana y el endpoint propio obliga a pagar por consumo, cumplen el 90% de ruteo o respetan la prohibición de enrutar? Cómo miden el ahorro sin mezclar eventos y gasto de poblaciones distintas? (`plan/annexes/02-arquitectura.md:151`; `:176`; `plan/annexes/06-roadmap-riesgo.md:159`).
5. **CFO:** Por qué dicen que el OKR cubre el equilibrio si uno se mide contra T0 y el otro contra la base de T1? Cuál es el puente numérico y qué ocurre si no coincide? (`context/supuestos/convenciones-de-calculo.md:16`; `plan/slides.md:130`).
6. **Producto:** Qué evidencia distinguiría un cliente dispuesto a evaluar gratis de un comprador con presupuesto? Qué resultado les haría abandonar el candidato aunque el RICE siga siendo el mayor? (`plan/annexes/06-roadmap-riesgo.md:283`; `:304`).
7. **Gobierno:** Qué significa «secretos siempre bloqueados» en las superficies donde la prueba espera ausencia de bloqueo? Quién acepta ese residual y qué evento revoca la autorización? (`plan/slides.md:79`; `plan/annexes/03-gobierno-seguridad.md:155`).
8. **Docentes:** Qué evidencia presentarían para pasar el gate de impacto a L2 y para demostrar que un +3,75% supera G2 si el intervalo cruza +3%? Quién del equipo humano defiende esas decisiones? (`plan/annexes/02-arquitectura.md:300`; `plan/annexes/06-roadmap-riesgo.md:143`; `plan/slides.md:162`).

### 5. Chequeos ejecutados, evidencia y límites

#### Resultados resumidos

| Chequeo | Resultado observado | Evidencia |
|---|---|---|
| Árbol y versión | `HEAD` indicado al comienzo; `git status --short` vacío al control de trabajo. | `out/re-review-pdf.log:1`; consulta directa a Git durante la revisión. |
| `scripts/leak-check.sh --all --strict` | Exit 0: «revisión COMPLETA; sin hallazgos». No se imprimió la denylist. | `out/re-review-leak.log:1`. |
| `scripts/okf-check.sh` | Exit 0: 159 archivos conformes en borrador. | `out/re-review-okf.log:1`. |
| `scripts/okf-check.sh --delivery` | Exit 1: 156 errores de verificación humana ausente; 34 contexto y 122 material. | `out/re-review-okf-delivery.log:1`. |
| `scripts/plan-check.py --mode draft` | Exit 0: diez slides, 45 ocurrencias pendientes, 164 referencias locales. | `out/re-review-plan.log:1`. |
| `scripts/plan-check.py --mode delivery` | Exit 1: deck y seis anexos `draft`, pendientes y 71 fichas directas sin verificar. | `out/re-review-plan-delivery.log:1`. |
| Suite de tests | Primer intento: 91 tests, un error al generar PDF con Chrome bajo sandbox. Reejecución autorizada fuera del sandbox: 91 tests, **OK**, 13,343 s; Bash 3.2 y 5.3 verificados. | `out/re-review-tests.log:1`; `out/re-review-tests-escalated.log:1`. |
| `scripts/build-deck.sh` | Build completo con Chrome fuera del sandbox; produjo formatos del deck y entrega de 140 páginas, 1.308.187 bytes. | `out/re-review-build-escalated.log:13`. |
| PDF: estructura y anotaciones | Diez páginas de deck; 279 enlaces internos, 269 URI, cero `file://`, cero destinos a `private/`. Índice a páginas absolutas 12, 17, 47, 72, 92 y 117. | `out/re-review-pdf.log:2`. |
| QA visual | Abiertas las diez slides; desborde en la 7. Abiertos índice y muestra de tablas de finanzas/gates; sin recortes observados en esa muestra. | `out/re-review-pdf.log:6`; `out/re-review-slide-007.png`. |
| Recálculo | Componentes trimestrales, anualización, P, rampa, ROI, cierres, RICE, equilibrio, precio y capacidad. | `out/re-review-numeric.log:1`. |

#### Qué no acreditan estos resultados

- El scanner revisa el árbol y sus patrones; no certifica anonimización semántica, historia publicada, forks ni ausencia de toda información sensible. No se buscó a la organización real ni se reprodujeron valores de la denylist.
- Los tests y el build exitosos prueban las ejecuciones observadas. No se hicieron pruebas de mutación ni se retiró código protegido para observar fallas: el encargo fue de solo lectura. Tampoco se ejecutaron los seis agentes del repo de punta a punta.
- Se verificaron anotaciones y destinos del índice, pero no se abrieron por HTTP las 269 URI ni se comprobó disponibilidad remota de todos los archivos en `main`. No hubo QA visual página por página de los 129 folios de anexos.
- La revisión fue realizada por un solo revisor sintético, sin subagentes independientes ni simulación de consenso humano. `board-review` sirvió como orientación proporcional; no se corrió una ronda integral atribuida a seis roles.
- Los estados `draft`, los supuestos y las advertencias se conservaron. Ningún resultado automático autoriza marcar fichas `verified`.

#### Contraste regulatorio acotado

La sección 4.6 de la [Comunicación A 7777 del BCRA](https://www.bcra.gob.ar/pdfs/comytexord/A7777.pdf) respalda exigencias de gestión del uso de IA en las entidades alcanzadas. No demuestra por sí misma una obligación contractual de comprar IA a este proveedor ni la vigencia consolidada de todos los requisitos en 2026. La cautela corresponde al claim de `plan/annexes/03-gobierno-seguridad.md:91`.

La [página oficial de la Comisión Europea sobre el marco de IA](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) es consistente con la fecha indicada en `plan/annexes/03-gobierno-seguridad.md:94`; esa fecha cae dentro de T4 de 2027. No se detectó allí el error temporal de excluirla del horizonte. No se emitió una opinión de aplicabilidad jurídica al caso.

#### Cierre del alcance

No se modificaron fuentes ni se borraron archivos versionados; solo se generaron artefactos de revisión en `out/` y este reporte en la ruta pedida. El build y los chequeos no cambian el estado académico de aprobación.

