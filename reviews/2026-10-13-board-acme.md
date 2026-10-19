# Revisión integral del board — Acme Labs

Fecha: 2026-10-13. Estado: revisión de borrador; no habilita peer review ni entrega.

## Objetivo, versión y procedimiento

Alcance: `plan/slides.md`, los seis `plan/annexes/0*.md` y todo `defense/`.
Contraste: las 21 fichas de `context/`, sus índices, `material/programa.md`,
mapa de fuentes, huecos y conceptos pertinentes; consigna resumida en `AGENTS.md`.

- SHA base: `43eb843e669a09e0f037462790a2d7e5cf11ff71`, rama `docs/board-review`.
- `git status --short` del objetivo y las fuentes: vacío.
- `git diff HEAD` del objetivo y las fuentes: vacío.
- Archivos nuevos del paquete: ninguno.
- Captura en memoria: bytes completos y SHA-256 de 164 archivos Markdown del objetivo, fuentes y roles. Dos comprobaciones de hashes: sin cambios.
- Modo integral, ejecución secuencial: architect → governance → people → finance → consolidación del board.
- **Sin aislamiento de contexto**: las cinco miradas las ejecutó el mismo agente, por instrucción del brief. No constituyen cuatro revisiones independientes.
- Criterios: estrategia integral, roadmap técnico/financiero/cultural, relato financiero, riesgo y reversibilidad, defensa y formato. Para peer review/entrega, toda cifra exige ficha `verified` con revisión humana.
- No se editó el plan. Los montos de diseño son supuestos; no se reprodujeron datos privados originales.

El plan es evaluable como propuesta. No es un esqueleto, aunque mantiene decisiones
y responsables humanos pendientes. La contradicción sobre el caso acordado está en H18.

## Veredictos por sombrero

| Sombrero | Veredicto | Motivo |
|---|---|---|
| Board | **Rechazado para aprobar hoy** | T1 tampoco tiene capacidad demostrada; la autorización solicitada cambia entre slides y los gates no cierran todas las rutas |
| CFO escéptico | **Rechazado** | La pérdida publicitada usa el punto medio, no el techo autorizado; escenarios de corte sin flujo recostado; beneficios sin puente a caja |
| Corrector de la cursada | **Rechazado para peer review/entrega** | Cobertura temática amplia, pero faltan evidencia humana, consistencia operativa y comprobación del entregable |

Recomendación: conservar el borrador y corregir los bloqueantes antes de pedir fondos.
Alternativa: aprobar sólo un diagnóstico acotado, con capacidad y techo propios
demostrados en G0; implica diferir plataforma y producto.

El responsable humano de resolver cada hallazgo sigue pendiente: no se asigna
a integrantes del grupo ni se inventa acuerdo del Directorio.

## Miradas secuenciales

| Mirada | Hallazgos propios que consolida el board |
|---|---|
| architect | H04: cobertura del gateway; H07: límites de datos/autonomía; H11: recursos; H12: línea de base; H13: caso de producto |
| governance | H03: anonimización; H04 y H15: controles; H05: decisión de gates; H07: irreversibilidad; H08: alcance regulatorio |
| people | H02 y H11: capacidad; H12: T0/T1; H14: adopción; H16: defensa y responsables |
| finance | H02: sobre de tiempo; H06: autorización; H09: productividad/caja; H10: costo de salida y escenarios; H17: modelo y contingencia |

## Hallazgos ordenados por severidad

### H01 — Crítica: ninguna cifra está habilitada para peer review o entrega

**Ubicación:** `plan/slides.md:17`; `plan/annexes/05-business-case.md:23`;
`plan/annexes/04-personas-cultura.md:317`; `context/hechos/costos-tecnologia-e-ia.md:5`.
**Dueños:** caio y cada dueño de anexo/fuente.

Las 21 fichas del caso están en draft. Además, fracciones de esfuerzo, poblaciones,
rampas, contingencia, régimen del año 2 y umbrales sólo viven en anexos: no tienen
ficha propia revisada. Una cadena de links no equivale a revisión humana.

**Corrección y cierre:** crear las fichas Supuesto faltantes con método e invalidez;
el humano revisa el alcance y declara `verified` sin convertir supuestos en hechos.
Cada cifra entregada debe resolver esa cadena y pasar los validadores de entrega.

### H02 — Crítica: se financia T1 antes de demostrar que T1 entra en la capacidad

**Ubicación:** `plan/annexes/05-business-case.md:84`, `:94`, `:260`;
`plan/annexes/06-roadmap-riesgo.md:58`, `:103`.
**Dueños:** caio, finance, architect y people.

El promedio anual de 5,2 FTE ya está identificado, pero **T1 pide 3,5 FTE** contra
un sobre máximo de 2,25 FTE bajo las mismas hipótesis: aproximadamente 1,56 veces.
G0 sólo confirma caja; el replan se posterga a G1, cuando T1 ya fue ejecutado.

**Corrección y cierre:** llevar a G0 la aprobación de capacidad, solapes y trabajo
desplazado por rol/trimestre. Presentar una versión ejecutable de T1 y recostear
el año, o ampliar explícitamente el sobre; sin eso, no arrancar la plataforma.

### H03 — Alta: alias y rangos no eliminan las combinaciones reidentificables

**Ubicación:** `context/hechos/cartera-y-concentracion.md:40`;
`context/supuestos/continuidad-de-clientes-principales.md:16`;
`context/hechos/estructura-de-ingresos.md:33`;
`plan/annexes/06-roadmap-riesgo.md:33`, `:145`.
**Dueño:** governance; caio integra la versión pública.

El paquete vincula una empresa identificada con perfiles de relación comercial,
historia contractual y estado/calendario de iniciativas internas. Cruzadas con
la oferta pública, esas características pueden identificar clientes o proyectos.

Es **riesgo de reidentificación**, no una identidad reconstruida en esta revisión.
No se hallaron nombres directos de clientes, empleados del caso, credenciales
ni montos reales en USD dentro del objetivo; no se intentó identificar los alias.

**Corrección y cierre:** revisar el conjunto completo con un humano autorizado;
generalizar cronologías y vínculos singulares o moverlos a `private/`.
Documentar qué conserva valor decisorio sin permitir esa asociación; el scanner no cierra este hallazgo.

### H04 — Alta: el control del 90% de seats no tiene una ruta técnica demostrada

**Ubicación:** `plan/annexes/02-arquitectura.md:57`, `:141`;
`plan/annexes/03-gobierno-seguridad.md:249`;
`context/hechos/uso-ia-interno.md:24`.
**Dueños:** architect y governance.

El gateway propuesto enruta llamadas de modelos, mientras la operación usa tres
productos corporativos distintos. No hay diseño o prueba que demuestre cómo sus
superficies de uso pasan por la pasarela, ni cómo se cuentan las que quedan afuera.

Además, si cae el uso semanal, la pasarela pasa a monitoreo sin distinguir datos
prohibidos. Esa salida puede quitar el bloqueo que sustenta la promesa de control.

**Corrección y cierre:** matriz superficie→control→telemetría, prueba de integración
y bypass por herramienta, presupuesto de migración y denominador del 90%.
Mantener bloqueo de secretos/datos prohibidos aunque se ajuste la fricción de usos permitidos.

### H05 — Alta: los gates no definen todas las fallas ni separan los frentes

**Ubicación:** `plan/annexes/06-roadmap-riesgo.md:53`, `:59`, `:60`, `:61`;
`plan/annexes/05-business-case.md:229`, `:262`.
**Dueños:** caio y los cuatro dueños de condiciones.

Se exige cumplir todo, pero G1 no dice qué pasa sin política o básico ≥90%.
En G2, la meta es ≥80% de adopción y la acción sólo cubre <60%: queda un intervalo
sin decisión. La señal de cliente aparece en la acción, pero no en las condiciones.

G3 exige SLO y red team del piloto incluso si producto se difirió en G2. Tampoco
coincide el corte económico de <+5% de T3 con la condición de +8% para liberar T4.

**Corrección y cierre:** tabla por condición con pass/hold/kill, dueño que decide,
fondos afectados, plazo de corrección y tratamiento de «no aplica». Separar gates
del frente interno y producto; recorrer casos 70% de adopción, +6% de throughput y producto diferido.

### H06 — Alta: la autorización cambia entre slides

**Ubicación:** `plan/slides.md:27`, `:55`, `:68`, `:70`;
`plan/annexes/02-arquitectura.md:239`;
`plan/annexes/05-business-case.md:239`.
**Dueños:** caio y architect.

Portada y Finanzas piden sólo T1; la slide 4 pide aprobar plataforma e hitos T1-T2
y señala como decisión esa columna. No distingue aceptar una dirección de diseño
de autorizar trabajo, gasto o compromiso para T2.

**Corrección y cierre:** un único pedido G0, con caja máxima, capacidad máxima,
entregables y decisiones delegadas. T2 debe quedar expresamente condicionado a G1
en slide 4 y anexo B.

### H07 — Alta: reversibilidad, datos y autonomía se contradicen

**Ubicación:** `plan/annexes/06-roadmap-riesgo.md:122`, `:126`, `:129`, `:131`;
`plan/slides.md:64`, `:140`;
`plan/annexes/03-gobierno-seguridad.md:189`, `:200`, `:201`, `:209`, `:250`.
**Dueños:** caio, governance y architect.

F declara irreversible ratificar la política en T1 y luego dice que ninguna
decisión irreversible ocurre antes de G4. La slide prohíbe datos productivos
durante el año, mientras otras filas habilitan datos con cláusula y matriz.

C pide cláusula acordada con cliente en T3, aunque el compromiso contractual espera
a G4. F contempla subir a L3/L4 con efectos externos en G4, mientras C restringe
L4 a sandbox y sólo contempla L3 en producto. Crédito también se reabre en T4.

**Corrección y cierre:** catálogo único de decisiones con ámbito, fecha mínima,
autoridad, condición y compromiso exacto. Separar aprobación interna, negociación
no vinculante y firma; ninguna excepción debe contradecir una prohibición del horizonte.

### H08 — Alta: una fecha cae dentro del plan y la exclusión regulatoria es excesiva

**Ubicación:** `plan/annexes/03-gobierno-seguridad.md:94`, `:207`;
`plan/annexes/06-roadmap-riesgo.md:28`.
**Dueño:** governance; caio corrige el relato.

El anexo C ubica el 2027-12-02 «fuera» del plan, aunque T4 termina en diciembre
de 2027. Además, excluir scoring/crédito no demuestra por sí solo ausencia de
alto riesgo: hay otros usos, por ejemplo empleo y educación.

La [Comisión Europea](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
enumera esos usos y publica esa fecha para Anexo III. Su calendario confirma la
contradicción temporal; no demuestra la aplicabilidad a Acme Labs.

La [Com. A 7777, sección 4.6](https://www.bcra.gob.ar/pdfs/comytexord/A7777.pdf)
requiere identificar usos de IA por la entidad o terceros, no sólo scoring.
Ese documento histórico no prueba por sí solo la versión vigente de 2026.

**Corrección y cierre:** corregir la ventana; sustituir «única forma» por exclusión
del caso crediticio y clasificación caso por caso. Legal confirma alcance, versión,
rol y excepciones. No dar por verificada una ficha por esta lectura del agente.

### H09 — Alta: throughput se valúa como capacidad sin definir su conversión

**Ubicación:** `plan/annexes/05-business-case.md:108`, `:149`, `:165`, `:181`;
`context/supuestos/ganancia-de-productividad.md:11`.
**Dueños:** finance y architect.

La fórmula multiplica costo por ganancia de throughput y llama al resultado
capacidad liberada. A output fijo, +15% de throughput implica liberar 15/115
≈13,04% de horas; con la rampa publicada da ~62,1 mil, frente a ~69,2 mil por equivalencia de output.

Ambas valuaciones pueden modelarse, pero responden preguntas distintas. No hay
unidad estable de throughput, normalización de dificultad ni destino probado
para monetizar la capacidad. El «ROI sobre la caja» usa beneficio que no es caja.

**Corrección y cierre:** definir unidad, cohorte, calidad y fórmula; elegir output
adicional o horas evitadas. Separar ROI de capacidad y retorno de caja, con un
puente verificable hacia ventas/contratación evitada. Recalcular equilibrio y sensibilidad.

### H10 — Alta: «cortar barato» usa medios y el escenario kill mantiene costos del año

**Ubicación:** `plan/slides.md:122`;
`plan/annexes/05-business-case.md:154`, `:242`, `:260`;
`plan/annexes/06-roadmap-riesgo.md:76`;
`defense/objeciones.md:9`.
**Dueños:** finance y caio.

La respuesta a «cuánto pierdo» da ~12 de caja y ~57 de tiempo, valores medios.
G0 autoriza hasta 17 y 82: hasta 99 mil económicos, antes de compromisos de salida.
No hay plazo de cancelación, mantenimiento residual o transferencia cuantificados.

El pesimista de E conserva 342 mil de tiempo y agrega consumo desde T3; F anuncia
kill en G2/G3. Falta distinguir estrés sin frenar de flujo ejecutado con kill.

**Corrección y cierre:** mostrar punto medio y máximo, gasto/compromiso devengado,
costo de cierre y base mínima que queda. Rehacer flujos por gate fallido; conservar
el estrés sin mitigación como comparación explícita.

### H11 — Alta: el recurso de IA de T1 no está cubierto y el contractor tiene dos lecturas

**Ubicación:** `plan/annexes/02-arquitectura.md:218`, `:219`;
`plan/annexes/04-personas-cultura.md:104`, `:252`;
`plan/annexes/05-business-case.md:279`.
**Dueños:** architect, people y finance.

B necesita 0,5 FTE de IA aplicada en T1; D sólo dispone el perfil externo desde T2.
No identifica cómo se cubre T1. Desde T2, el modelo suma esfuerzo interno de IA
y contractor: el solape está reconocido, pero no resuelto en la capacidad autorizable.

**Corrección y cierre:** asignación por rol, vía y trimestre, sin nombres internos;
capacidad ya disponible o formación previa demostrada para T1. Decidir si el
contractor reemplaza o complementa el esfuerzo técnico; recostear cada alternativa.

### H12 — Alta: T0 financia prerrequisitos que otros anexos prometen en T1

**Ubicación:** `plan/annexes/04-personas-cultura.md:209`;
`plan/annexes/02-arquitectura.md:193`;
`plan/annexes/06-roadmap-riesgo.md:41`, `:42`;
`context/supuestos/ganancia-de-productividad.md:34`.
**Dueños:** caio, people, architect y finance.

D pone línea de base, ratificación y estudio de matriz en T0. B/C/F trasladan
varias de esas tareas a T1. T0 no tiene presupuesto ni capacidad en el consolidado,
y medir la base mientras comienza formación/plataforma puede contaminar la comparación.

**Corrección y cierre:** un calendario único: qué existe antes de G0, quién lo
verifica y cuánto cuesta; distinguir reconstrucción retrospectiva de medición
prospectiva y congelar una base comparable antes de atribuir la ganancia.

### H13 — Media: «IA en lo que vende» todavía puede terminar en un asistente interno

**Ubicación:** `plan/slides.md:49`;
`plan/annexes/06-roadmap-riesgo.md:144`, `:148`;
`plan/annexes/02-arquitectura.md:200`.
**Dueño:** caio, con architect y finance.

La hipótesis principal es soporte interno de una plataforma. Puede tener valor,
pero no demuestra una funcionalidad vendida ni disposición a pagar. «Señal de
cliente», SLO y outcome del piloto no tienen definición concreta.

**Corrección y cierre:** ficha de experimento elegida en G1: usuario, problema,
datos permitidos, outcome, SLO, costo máximo y evidencia comercial exigida.
Distinguir eficiencia de soporte de producto vendible y contingencia sin cliente.

### H14 — Media: las metas propuestas tampoco alcanzan el 80% combinado

**Ubicación:** `plan/annexes/04-personas-cultura.md:213`, `:251`;
`plan/annexes/06-roadmap-riesgo.md:164`;
`context/hechos/okrs-y-objetivos.md:32`.
**Dueños:** people y caio.

Con áreas de igual peso, Tecnología 85% y Operaciones 60% dan 72,5%, incluso
si toda Operaciones estuviera habilitada. Con habilitación parcial, el resultado
sobre el total es menor. DP5 propone además Tecnología 80%, frente al 85% de T4.

**Corrección y cierre:** decidir si se reemplaza el OKR combinado; publicar ambas
métricas y sus denominadores sin presentar la nueva meta como cumplimiento del
80%. Unificar 80%/85% por trimestre.

### H15 — Media: el disparador de secretos tolera el primer incidente

**Ubicación:** `plan/annexes/03-gobierno-seguridad.md:110`, `:153`, `:236`.
**Dueño:** governance.

R4 bloquea el envío automático recién con más de un secreto expuesto por trimestre.
La tabla de amenazas indica rotación inmediata, pero no exige contención ni
revisión del canal en la primera exposición: permite repetirla antes del bloqueo.

**Corrección y cierre:** primer secreto confirmado → revocar/rotar, contener el
canal afectado y decidir reanudación con evidencia. Separar umbral de escalamiento
del indicador de recurrencia; ejercitar esa ruta en el tabletop de T2.

### H16 — Media: la defensa declara ensayo sin evidencia y su bundle está vacío

**Ubicación:** `plan/slides.md:156`; `defense/evidence/index.md:11`;
`defense/storyline.md:36`; `defense/objeciones.md:3`;
`AGENTS.md:187`.
**Dueño:** caio; board aporta las preguntas.

El deck dice «defensa ensayada», pero el objetivo sólo contiene respuestas para
ensayar y ninguna ficha Evidencia. El índice aún espera elegir caso. El uso de
roles no acredita que todas las herramientas invoquen agentes de punta a punta.

**Corrección y cierre:** retirar el claim o registrar ensayo fechado, tiempos,
participantes/roles autorizados y feedback. Incorporar evidencia procesada para
objeciones críticas; distinguir rol adoptado de invocación automática probada.

### H17 — Media: faltan el modelo recalculable y límites de los costos sin estimar

**Ubicación:** `plan/annexes/05-business-case.md:47`, `:50`, `:154`, `:161`;
`plan/annexes/04-personas-cultura.md:286`.
**Dueño:** finance, con architect y people.

El árbol versionado no contiene el modelo financiero que genera tablas. La rampa
base es explícita, pero las rampas numéricas pesimista/optimista no lo son.
Un tercero no puede reproducir los tres ROI y paybacks con todos sus inputs.

La contingencia del 15% cubre varios renglones sin cotización ni cantidades.
Nombrarlos no demuestra que entren en el techo de caja.

**Corrección y cierre:** versionar un modelo con inputs públicos/supuestos, fórmulas
y tablas generadas; valores reales sólo en private. Cotizar o excluir lo faltante,
con regla de no gastar fuera del techo y sensibilidad por renglón.

### H18 — Media: el contrato y el corpus discrepan sobre el acuerdo del caso

**Ubicación:** `AGENTS.md:20`; `context/index.md:5`;
`defense/evidence/index.md:11`.
**Dueño:** caio, con el equipo que mantiene el contrato.

AGENTS mantiene Acme Labs como candidato pendiente; context dice caso elegido
y la defensa conserva un índice que espera la elección. El brief autoriza revisar
este plan, pero no constituye evidencia del acuerdo de los ocho integrantes.

**Corrección y cierre:** el equipo confirma el caso y alcance; registrar el acuerdo
y reconciliar las tres declaraciones. Si sólo está autorizado como borrador para
validar, rotularlo así en vez de declarar consenso.

## Checklist de la consigna

«Cumple» significa que el contenido requerido existe; no reemplaza los bloqueantes
de evidencia y consistencia. No se usa CAIE como rúbrica del TIF.

| Requisito | Estado | Evidencia / brecha |
|---|---|---|
| Estrategia integral: arquitectura, gobierno, seguridad, personas y finanzas | **Cumple en cobertura** | Anexos A–F, alternativas y riesgos explícitos; no aprobable por H01–H12 |
| Roadmap técnico, financiero y cultural con hitos y criterios de éxito | **No cumple integralmente** | Tracks presentes; capacidad, calendario y rutas de falla inconsistentes |
| Financial storytelling para CFO escéptico | **No cumple para decisión** | Se reconoce ROI negativo; falta costo máximo de salida y conversión a caja |
| Escenarios, contingencias, reversibles e irreversibles | **No cumple integralmente** | Existen, pero no son ejecutables de manera coherente entre anexos |
| Preparación de la defensa con evidencia | **No cumple** | Storyline y objeciones presentes; ensayo sin registro y bundle vacío |
| Máximo diez slides, incluyendo portada/equipo | **Cumple estructuralmente** | plan-check cuenta 10; portada y equipo incluidos |
| Un PDF de menos de 10 MB con anexos | **No demostrado** | No se generó ni inspeccionó un entregable durante esta revisión |
| Cifras entregadas respaldadas por revisión humana | **No cumple** | Fuentes del caso draft; validadores de entrega rechazan |

El programa no agrega una rúbrica de notas al enunciado. Constitution/Portfolio/
Operating System son insumos: no se exige adoptar un framework de cambio que el
material declara ausente sólo para completar una lista.

## Las cinco preguntas más difíciles para la defensa

1. Si T1 ya necesita más capacidad que la disponible, qué trabajo concreto dejamos de hacer, y por qué la aprobación de capacidad espera hasta marzo?
2. Cuál es la pérdida máxima autorizada y el costo de cierre en G1/G2, incluyendo obligaciones y mantenimiento, y dónde está el flujo después del kill?
3. Cómo prueban que los tres productos de IA pasan por sus controles, y qué sigue bloqueado si la pasarela pasa a monitoreo?
4. Qué señal comercial verificable justifica financiar producto, si el primer caso puede ser soporte interno y no se cuenta ingreso durante el año?
5. Qué fuentes y supuestos revisó un humano, y cómo demuestran que la combinación de alias, cronologías y relaciones no identifica clientes o proyectos?

Destino existente para incorporarlas: `defense/objeciones.md`.
No se escribió allí: el brief prohíbe editar la defensa.

## Evidencia de verificación observada

```text
python3 scripts/plan-check.py --mode draft
plan-check (draft): 10 slides; 52 pendientes; 152 referencias locales
OK: estructura válida; evidencia humana y madurez no certificadas

python3 scripts/plan-check.py --mode delivery
plan-check (delivery): 10 slides; 52 pendientes; 152 referencias locales
ERROR: Entrega rechazada: deck declarado draft
[entre otros errores, seis anexos draft y pendientes]
✗ okf-check: 55 errores

scripts/okf-check.sh
✓ okf-check: 147 archivos conformes en borrador; no implica aptitud para slides/entrega

scripts/okf-check.sh --delivery
✗ okf-check: 144 errores

scripts/leak-check.sh --all --strict
✓ leak-check: revisión COMPLETA; sin hallazgos

scripts/leak-check.sh --strict (sólo la revisión staged)
✓ leak-check: revisión COMPLETA; sin hallazgos

Comprobación SHA-256 contra captura
Captura: 164 archivos; cambios detectados: 0
```

La salida de errores se extracta: los conteos corresponden a los comandos
observados, no a una certificación de verdad ni a 144 problemas independientes.
Los chequeos de entrega fallan; eso confirma el estado y no invalida esta revisión.

Se recompuso el beneficio base de E: 17,5 × 4.750 × 12 × 15% ×
(0 + 25% + 60% + 100%)/4 = 69.201,56. No se presenta el cálculo como
evidencia de retorno de caja ni como validación de los supuestos.

## Limitaciones de acceso y del procedimiento

- Fuentes internas originales no consultadas; se leyeron sus fichas anonimizadas. No se certifica su fidelidad ni la anonimización frente a quien conoce el caso.
- PDFs originales de la cursada y notebook no consultados; se usó el corpus local y sus huecos. La consigna completa original no está en el paquete.
- EUR-Lex devolvió una verificación antirrobot al abrir los dos ELI. Se consultó la página oficial de la Comisión para H08; no se cotejó íntegramente el texto consolidado.
- El BCRA leído es A 7777 de 2023: no se afirma vigencia actual del texto ordenado ni validación de todas las normas de C.
- Sin prueba de proveedores, medición real de throughput, cotizaciones, contratos ni ensayo humano.
- No se generó PDF/HTML/PPTX: el brief limita escrituras a la revisión y el reporte. La maquetación y el peso final quedan sin verificar.
- No hay revisión por subagente: la instrucción explícita de ejecutar solo prevalece sobre el paso de delegación de verify-before-done.
- No se ejecutó `lh metrics record-verify`: el skill lo excluye para Codex por falta del session id que necesita.
- `vaultkit status`: «sin PRJ para board — no se crea ninguno, es decision humana». No se modificó LazyMind; el brief limita las escrituras a estos dos archivos.
- No hay `graphify-out/graph.json` en esta worktree. Se usó contraste textual dirigido; no se creó un grafo fuera del alcance.

## Huellas del objetivo y del contexto

Las fuentes y roles adicionales también fueron capturados en memoria. Estas
huellas identifican el objetivo y contexto principal; el SHA base permite recuperar
el paquete completo porque status y diff estaban vacíos.

| Archivo | SHA-256 |
|---|---|
| `AGENTS.md` | `72e58ef1f75dae61b6794bd1530ba2a22ab8221be16f80654aeadfa1588b2184` |
| `context/hechos/capacidad-y-utilizacion.md` | `9e104bdea2c36843b0872a666c09b227ab29c6c53c1117b42b9be737b0a097f6` |
| `context/hechos/cartera-y-concentracion.md` | `dc9533ffb3179c8e3940a33d0fbb9ccce035fd4c1c06ed083b87fccc6385d6d8` |
| `context/hechos/costos-tecnologia-e-ia.md` | `00924b2af175100b4c683b23e5019e6f66532cdd58678e6a065802f4f90e243e` |
| `context/hechos/encuesta-y-pilotos-ia.md` | `40ef47c7034abc59c44eecfe35f240f857e116ca220c3046203608ac72951cf5` |
| `context/hechos/estructura-de-ingresos.md` | `8d363d17440b11c22e4db095f9b556578916bc8150e7d0985958ac8a99fc6672` |
| `context/hechos/gobierno-y-politica-ia.md` | `2b10c8b41aa7a477bce48ebc34b28a7fe635a479f3d301a531ef245b586d0eb1` |
| `context/hechos/ia-en-producto-y-oferta.md` | `0a1bd400029a3cc59e6cde3160213ebcb8ce573482946cf33d036ad46cb6fa7a` |
| `context/hechos/oferta-y-segmentos.md` | `d72308027e28d08d2353a7a6aac29d7e94a3a5414c1f8942144ddd277a659fa4` |
| `context/hechos/okrs-y-objetivos.md` | `94e4bf9e999e8d033b588ead51d6a0c0753168e4dff337025a520e395b75339c` |
| `context/hechos/regulacion-clientes-financieros.md` | `db7c9117b5061fa0da4c51b64fbe1f891a1ebae2115b0a5b350f6d2ef2dee82f` |
| `context/hechos/seguridad-y-certificaciones.md` | `4d76a699e57f3bd2cd269ddb447306e0f2932e63164a65ae5b466c16629ef698` |
| `context/hechos/situacion-economica.md` | `0cd1171c05e9bca797ac79fecad33f7542d430c06252b7c0ff9c6cacdadd86f0` |
| `context/hechos/stack-y-plataforma.md` | `c248f56c64a1c07779f5580644a630534fcd9224bd598b688f36833d9ec009df` |
| `context/hechos/tamano-y-estructura.md` | `e0efbd460d99ab2044f6c11b534e239fdbf59ab3d9c368cf490a35f70c01d98f` |
| `context/hechos/uso-ia-interno.md` | `17756b4b00d1e0ef7868fe5fcfdc11f1684a0e5aebdd368f7ae614c49edf0d7d` |
| `context/index.md` | `7b46461a885e04b89d298bebec31710a5ce1fd256c03eda798564d5f06456e05` |
| `context/supuestos/apetito-de-riesgo-de-clientes.md` | `1c89ba358a57d3b6837495d121ba9dd24627ec6fa423727b372d400996374e3a` |
| `context/supuestos/capacidad-de-inversion.md` | `28746630a48563789c949e22c647a94157829a6f8f0b6da342c7bbb52502c5cd` |
| `context/supuestos/continuidad-de-clientes-principales.md` | `df7e4e31c664a5b88f21ea068fc2571ff6297be513ecb0e674e59d89488e9046` |
| `context/supuestos/costo-cargado-por-rol.md` | `6b1191c705b8e48b55c1476d5c240d0ffcd25b5cbbd510a2950797f21e2def3f` |
| `context/supuestos/disponibilidad-de-datos.md` | `17c652e2d4e7e88d210e657d0c40c7ea6c880566a08ad7f616f4f6c346b0048c` |
| `context/supuestos/ganancia-de-productividad.md` | `fc3331f7a585b658618733cb003413e849cae72c4e4fb23d328df617b2bf1dca` |
| `context/supuestos/precio-y-dependencia-de-modelos.md` | `39f8c93afd3e74bb3922ac54c4048cd84d07ece07956629e4d43f072371939e5` |
| `defense/evidence/index.md` | `4f2e2592a722b62f70aabea2ed8ce664ea6488c09f9f994aa383bf6da9ae8a21` |
| `defense/objeciones.md` | `732cf2d4b664858a68a26b553fb9fb75918a58750dec3bad01586a30cd889ce7` |
| `defense/storyline.md` | `85c50b5514445164cb3ea683eee7808e28b79d3c6d8161f6a73f6e0bd9fd6bec` |
| `material/huecos.md` | `472289f621405dc2819a29d775cfacc7ec4916b82074ad78b247415e26069321` |
| `material/index.md` | `754a69ee8f36abfa654f95df04275a5afcb63a87fd858a0211d5d3e64ce21888` |
| `material/mapa-plan-fuentes.md` | `64a6aea17f3d2908160c24446a385c34862a3734f38b90db4c959a519e48afa9` |
| `material/programa.md` | `13ee3e6befba068171e15a6f3fd71a5506a12523e37f2295abbb36f2de82caf6` |
| `plan/annexes/01-diagnostico.md` | `0dc63ceeeeadaf68860d96ecc0280d9452e8682991bfe733beb7bf675c2b0da4` |
| `plan/annexes/02-arquitectura.md` | `c4940256ed41ec0f5d187850cbf85cc27af9c87f472720c5a6e8ef45a936a16d` |
| `plan/annexes/03-gobierno-seguridad.md` | `5fc9508384e1a3b5220859c6338527f2463732c87b2970587bd1be1ea2748f37` |
| `plan/annexes/04-personas-cultura.md` | `522b75c311e697af3a075ba62e3eba74db5b528e713a444edf59d0411fd4ee72` |
| `plan/annexes/05-business-case.md` | `f009cb35ee20a7706289f2d6c003802b9d9666b2d4bee2500eaa784a11aa18b4` |
| `plan/annexes/06-roadmap-riesgo.md` | `04c66215491734138bc430cf4b791e4691dca4fde2d7614fa32b438094eafed6` |
| `plan/slides.md` | `dcce12e8453e4bc1f5f5ed8c4f9d3a6baec0235b56d11a98283df26062c402aa` |

