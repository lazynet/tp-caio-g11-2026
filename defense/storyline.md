# Storyline de la defensa

Borrador del CAIO a validar por el equipo, sobre el caso Acme Labs y el alcance
de toda la organización (producto y operación interna), acordados en comisión
([acuerdo de alcance informado por Martín](https://github.com/lazynet/tp-caio-g11-2026/issues/15)).
Coordina la defensa (storyline, objeciones y quién presenta cada slide) Lucho,
según el reparto del `README.md`. Quién presenta cada slide y quién responde
cada objeción **todavía no se acordó** (#21): al final va una propuesta para que el
equipo la discuta. El pedido es aprobar el plan y sus resoluciones R-01 a R-32
([Anexo G](../plan/annexes/07-resoluciones.md)). Cada cifra remonta a un anexo de
`plan/annexes/`. Esta síntesis editorial conserva las decisiones de A–G y
reorganiza su exposición alrededor de tareas, evidencia y liberaciones.
Los supuestos modificados por G fueron revalidados por instrucción de Martín
el 21/10, según README; conservan su tipo `Supuesto`.
Las cuatro fichas de #55 siguen `draft`, sin declaración humana nueva;
#56 conserva el bloqueo regulatorio de entrega. Una revisión de fuentes no
valida los supuestos con datos internos ni acredita acuerdo del equipo o
aprobación empresarial. La anonimización todavía necesita la revisión de un humano
autorizado. **No hubo ensayo todavía**: cuando lo haya, se registra con fecha,
tiempos, roles y feedback. El arco propuesto conserva el propósito empresarial:
oportunidad → cuatro etapas → iniciativas → ejecución → recursos → resolución.
El deck es la única fuente; este texto prepara su defensa. Montos en k USD.

## Apertura propuesta y relato en tres actos

**Apertura oral breve, todavía sin ensayar:**

> Acme ya usa IA para desarrollar software, pero todavía no mide cuánto mejora
> sus entregas. Priorizamos una prueba con las herramientas actuales, formación
> aplicada por rol y controles probados. Medimos cambios aceptados con calidad y
> estudiamos un asistente de integración para clientes, sin construirlo todavía.
> Hoy pedimos aprobar el plan y sus resoluciones: liberar hasta 8k USD de tiempo,
> caja 0, para diez días hábiles de validación en 2026. Los 71k adicionales los
> libera el CEO solo con las condiciones cumplidas. El techo es 79k hasta M3 y
> 121k anual, por tramos. No presupuestamos repago. Si falta capacidad, falla la
> seguridad o la evidencia no alcanza, reducimos o cortamos.

| Acto | Slides | Pregunta que resolvemos |
|---|---|---|
| 1. Problema y propuesta | 1–4 | Qué tarea queremos mejorar y cómo vamos a demostrar su aporte? |
| 2. Capacidad de ejecutar | 5–7 | Con qué herramientas, tiempo y límites podemos probarla? |
| 3. Recursos y decisión | 8–10 | Quién libera cada tramo y cuándo conviene detenerse? |

**Candidato operativo, no aprobado ni observado:** resolver un defecto real de
código propio usado, con regresión que falla antes y pasa después, revisión
independiente del autor, CI, aceptación del usuario interno, integración y uso
real comprobados. Sustituye una tarea dentro de la prueba restante de M3, tras
base, formación y controles y con todas sus horas confirmadas. Si no cabe, se
retira de M3; M4 solo con continuidad autorizada y capacidad existente. No demuestra
ganancia de productividad ni retorno. El asistente de integración es una
hipótesis distinta: documentación propia y datos sintéticos, con base del problema
y señal comercial antes de decidir su construcción.

**Respuesta adversa que no se omite:** el escenario pesimista puede terminar
antes de M1; si corta en M3, el techo hasta cerrar es 79 y el anual con guardia
aprobada es 85. El optimista acredita solo capacidad medible sin daño: venderla
o evitar una contratación requiere evidencia propia. Un cambio de precio del
proveedor conserva exposición con o sin este plan; el mínimo no la elimina.

**Uso del detalle siguiente:** consultar la regla y el anexo ante una objeción.
El guion ejecutivo ordena la exposición; las condiciones completas del Anexo G
siguen rigiendo. Presentadores, respuestas y ensayo quedan pendientes de acuerdo.

## Qué tiene que demostrar la defensa

El [capstone ante un panel ejecutivo](../material/conceptos/m3u4-capstone-panel-ejecutivo.md)
pide demostrar cuatro competencias. Este es dónde las sostiene el plan, sin
cambiar el orden de los actos.

> **Alcance de la atribución.** Martín confirmó el cotejo de la ficha del
> capstone (M3U4, pp. 15-20) el 21/10. La fuente pide *demostrar* las cuatro
> competencias, pero no da rúbrica ni criterios de evaluación: no se presentan
> como criterio de evaluación del panel. Los tiempos, el ensayo y el diseño del
> panel son propuesta del equipo, no del curso.

| Competencia | Dónde se demuestra | Cómo se prepara |
|---|---|---|
| Visión estratégica | Tesis y acto 1: mejorar la entrega y evaluar la oferta, avanzando con evidencia | Síntesis ejecutiva: la tesis y el cierre del deck, dichos en menos de un minuto (propuesta del equipo, no del curso) |
| Justificación de inversiones | Actos 2 y 3: beneficio medido, exposición presupuestaria por punto de salida, narrativa financiera | Cada cifra con su anexo; ninguna fuera del deck o de un anexo |
| Gestión de objeciones | [Banco de objeciones](objeciones.md), con respuesta y evidencia por objeción | Mapeo de objeciones probables por tema, con una propuesta de quién responde cada una al final, no acordada |
| Comunicación ejecutiva | Una decisión por slide y el cierre con el pedido | Ensayo con tiempos y preguntas bajo presión (propuesta del equipo): todavía no se hizo |

**Bajo presión:** responder con la cifra y el anexo; si no se sabe, decir qué se
mide y en qué gate; no estimar en vivo ni cambiar el pedido en la sala.

## Tesis en una oración

Proponemos medir capacidad con calidad en las entregas de Acme Labs y estudiar
un asistente de integración, con herramientas actuales, controles probados y
recursos liberados por evidencia antes de ampliar.

## Respaldo del acto 1: problema, propuesta e iniciativas (slides 1–4)

- La empresa es rentable y crece, pero concentrada: el cliente principal pesa
  40%-50% de la facturación ([Anexo A](../plan/annexes/01-diagnostico.md)).
- La IA ya está adentro: Tecnología usa mucho el agente de código; Operaciones,
  poco, en buena parte porque el cliente fija las herramientas. Hay herramientas
  de harness para el SDLC de uso exclusivamente interno; no se cuentan como IA
  productiva de la oferta. La política de IA vigente la ratifica el Directorio
  al aprobar el plan (R-07); la preparación deja constancia de versión y alcance,
  y el gate del mes 3 comprueba su aplicación y su alcance para el producto; los
  controles se prueban por superficie antes de usar.
- No hay medición del impacto del harness contra una base, según el responsable
  del caso ([uso interno](../context/hechos/uso-ia-interno.md)). El propio
  diagnóstico es una hipótesis: las fuentes mezclan poblaciones y fechas, así que
  financiamos primero una validación acotada para conciliar corte, nómina,
  contratistas, personas y horas por rol antes de liberar M1-M3.

**Cierre del acto:** mejorar la entrega y evolucionar la oferta exige comprobar
capacidad, calidad y restricciones antes de ampliar.

### Priorización y etapas que sostienen la propuesta

- **Factibilidad–impacto y RICE ajustado por riesgo:** el mínimo prueba la
  operación con herramientas existentes. En producto, el estudio del asistente
  queda antes que pagos y el servicio de agentes por documentación propia y
  menor dependencia externa. Pagos requiere habilitación y seguridad; agentes,
  certificaciones y horas que compiten con entregas. Los puntajes son hipótesis
  del CAIO, no resultados ([Anexo F](../plan/annexes/06-roadmap-riesgo.md#de-los-conceptos-de-la-cursada-a-la-decisión-del-caso)).

- **Preparar → Validar → Contrastar → Consolidar:** primero base, controles,
  formación y prueba; después validación interna y estudio acotado de producto;
  aplicación con evidencia y evaluación de continuidad al cierre. La validación
  inicial de 2026 tiene liberación propia; construir producto exige otra decisión
  y costeo (B, E, F y G, R-02/R-30/R-31).

- El beneficio principal es capacidad con calidad: PR aceptados contra una base
  congelada, en agregados por área y semana, con retrabajo e incidentes primero.
  **Beneficio de caja estimado: 0;
  ingreso nuevo: 0** en el modelo ([Anexo E](../plan/annexes/05-business-case.md)).
- El paso no está asegurado: con 15-20 personas, la medición solo distingue con
  buena probabilidad una mejora cercana al +25%. Por eso el mes 6 no lee valor
  (sigue por adopción, costo y controles, y corta por daño o caída demostrada) y
  el mes 9 pide solo que la mejora se distinga de cero, sin daño de calidad. Si
  no se distingue, el beneficio acreditado es 0 y no se amplía: el año compra
  aprendizaje con techo, no una promesa de retorno
  ([Anexo F](../plan/annexes/06-roadmap-riesgo.md#gates-por-condición-pasa-espera-corta); [Anexo B](../plan/annexes/02-arquitectura.md), «Gate de valor»).
- El asistente de integración es una hipótesis de producto: antes del mes 6
  medimos el tiempo a la primera integración exitosa con la documentación y el
  soporte actuales. Sin problema, base y señal comercial escrita, no se construye.
- Las alternativas publicadas (47, 161, ≈199, 394, ≈400, 471) son costos de
  alcances distintos: referencia, no comparación de precios (R-28). Ninguna
  resolución depende de compararlas; si un gate propone ampliar, Finanzas arma
  antes una estimación común. El pedido anterior (33 + 6 de caja, 72 + 7 de
  tiempo) queda como antecedente.

**Cierre del acto:** operación primero y asistente como hipótesis; el mínimo
financia la evidencia para decidir qué continuar o ampliar.

## Respaldo de los actos 2 y 3: ejecución, recursos y control (slides 5–10)

- **Build / buy / agentificar:** configurar lo que ya pagamos antes de comprar o
  ensamblar. La plataforma se relee en los meses 3, 6 y 9 con la regla que
  ratifica el Directorio: una señal y además cuatro condiciones (R-15). La libera
  el Directorio. Nada pasa al año 2 por defecto ([Anexo B](../plan/annexes/02-arquitectura.md)).
- **Human-in-the-loop y seguridad antes de usar:** en producto el tope L2
  permite preparar acciones, pero la persona decide y ejecuta. La escala es
  pedagógica del curso. Sin plataforma no alcanza la política; cada
  superficie prueba sus compensatorios, con críticos cerrados y residual
  aceptado. Seguridad puede suspender el uso aunque el gasto o la adopción
  cumplan, y quien produce la evidencia no es quien la verifica ni quien firma
  ([Anexo C](../plan/annexes/03-gobierno-seguridad.md)).
  R-08 excluye código y datos de clientes de modelos externos, salvo en su entorno
  y con permiso escrito. R-09 suspende código bajo NDA desde la aprobación; solo
  código sin NDA ya en uso admite residual del comité hasta M3, no datos.
- **AI literacy por rol:** formar, reasignar y decidir una excepción externa solo si falta
  un facilitador. Se propone reservar 720 h clave (1,5 FTE) más 540-660 h de
  formación: máximo 1.380 h, con demanda de actividades de 970-1.346 h; con
  verificación M3, 974-1.351 h. Se adoptan los solapes
  de horas entre áreas adoptados (R-25, R-26). La reserva no es disponibilidad:
  Operaciones confirma agendas y trabajo desplazado por persona y semana, o se
  recostea antes del mes 1 sin subir el techo. La capacidad se lee con sobre
  separado: soporte clave y formación se confirman por separado en la segunda
  liberación (R-05) ([Anexo D](../plan/annexes/04-personas-cultura.md),
  [Anexo F](../plan/annexes/06-roadmap-riesgo.md#resoluciones-del-directorio-y-decisiones-delegadas)).
  Operaciones no tiene meta M6: ≥40% M9 y ≥60% M12 sobre habilitadas, solo si el
  Directorio autoriza y costea el programa ampliado en M6 (R-23).
- **Roadmap:** diagnóstico, base, política, controles, formación y prueba en los
  meses 1-3, después de diez días hábiles de validación autorizada en 2026;
  en los 4-12, controles, medición y, en los 4-6, el estudio del asistente sin
  construirlo; evaluación y traspaso en los 10-12. Producto, plataforma,
  referentes y cursos nuevos no entran en esos techos: necesitan otra decisión y
  costeo, sin fecha prometida, y no pasan al año 2 por defecto. El Council revisa
  cada mes y puede cortar; a las dos liberaciones iniciales les siguen los gates
  de los meses 3, 6, 9 y 12.
- **Kill-fast y kill/scale gates:** aplicar señales y plazos de inviabilidad
  temprana evita mantener una prueba inviable. Los gates formales autorizan cada
  tramo; no se confunde cortar a tiempo con exigir retorno antes de poder
  medirlo. El valor se lee en M9, con los criterios vigentes, sin modificación
  por el candidato de corrección puntual.
- **Primera liberación:** 80-136 h y hasta 8k USD de tiempo, sin caja
  incremental; agendas e imputación 2026 confirmadas antes de empezar. La
  libera el Directorio al aprobar el plan (R-02). Incluye
  diagnóstico, matriz privada, viabilidad, verificación y cierre documental. Sin
  despliegues ni dictamen externo; el alcance y la cotización legal preparan la
  decisión. Si no sostiene el alcance, se reduce o se detiene con lo trabajado,
  hasta 8k USD.
- **Exposición presupuestaria máxima autorizada del tramo:** el resto de M1-M3 y
  las reservas requiere la segunda liberación, de hasta 71k USD, que firma el CEO
  por delegación y solo con las condiciones de R-05; el acumulado
  propuesto es 79k USD (10 de caja y 69 de tiempo), no 79 nuevos. Si se corta
  antes de M1, el límite es 8; si se sale en M3, es 79 hasta cerrar y 85 en el
  año con núcleo aprobado al salir. Son techos de recursos, sin restar beneficio:
  no es pérdida económica incremental ni salida de caja, y no incluyen la
  contribución del trabajo facturable que puedan desplazar, que sigue sin medir.
  Después, el Directorio fija hoy techos por tramo de 16k, 13k y 13k USD (121k en
  el año) y no los libera: el CEO firma cada gate dentro del techo de su tramo.
  Cortes inmediatos M6/M9: 95/108 hasta cerrar y 99/110 anual con guardia.
  Espera única M9 vencida: 108 + 7 = 115 hasta cerrar; +1 de guardia = 116 anual.
  El subtramo caja 1/tiempo 6 sustituye continuidad de M10–M12; la reserva de
  cierre se usa una sola vez. No hay espera por medición M6 (E, R-27).
  Ningún camino supera 121; superar un tramo vuelve al Directorio.
- **Si sale bien:** pasan los gates y el mínimo sigue todo el año sin
  plataforma, con costo proyectado ≈71k USD (27-114) dentro de un techo anual de
  121k USD (118k sin gastar las reservas de cierre). Lo que
  queda en la mano es base, la lectura de valor del mes 9 con su intervalo,
  controles probados y la decisión del año 2 con evidencia; no un ingreso
  ([Anexo F](../plan/annexes/06-roadmap-riesgo.md#escenarios)).
- **Narrativa financiera, datos → narrativa → decisión** ([Anexo E](../plan/annexes/05-business-case.md#insumos-para-el-deck)):
  *datos*, beneficio de caja 0 y un mínimo con techo de 79k USD; *narrativa*, sin
  retorno prometido se compra información, y si el board dice que no siguen
  abiertas tres exposiciones, sin monetizar daños ni probabilidades: clientes que
  prohíben modelos externos y uso sin regla, que el mínimo cubre, y consumo de
  modelos, que el mínimo no cubre; si una plataforma lo cubriría depende del
  régimen del proveedor. El consumo es la única modelada: 211-267k USD
  incrementales al año a 12× si el proveedor cobrara por consumo y el uso de
  septiembre, valorizado a precio de API, se mantuviera. Es un escenario, no
  consumo facturado ni pronóstico, y es de la empresa con o sin plan; *decisión*,
  aprobar el plan y sus resoluciones: la primera liberación, los techos y la
  delegación de la segunda con sus condiciones. La plata es interna, por etapas y
  sin deuda.
- **Personas, sin eludir el empleo:** formar y reasignar antes que desvincular.
  El estudio de un rol crítico no decide desvinculaciones y no está en el
  mínimo: es alcance ampliado, con postura comunicada, horas y autorización
  propias. Además, chequeo de
  equidad por grupo y sin compensación monetaria nueva en 12 meses
  ([Anexo D](../plan/annexes/04-personas-cultura.md)).

## Cierre: resolución (Aprobar el plan y sus resoluciones)

**Valor medible; seguridad aceptable; fondos por decisión.** "Les pedimos aprobar
el plan y, con él, las resoluciones R-01 a R-32 del Anexo G. Hoy liberan diez días
hábiles de validación con agenda propia: hasta 8k USD de tiempo y caja incremental
0. Fijan los techos: 79k USD hasta el mes 3 y 121k en el año, con 16k, 13k y 13k
por tramo. Delegan en el CEO la segunda
liberación, de hasta 71k USD, solo con diagnóstico, capacidad, método ratificado,
roles nombrados y presupuesto 2027 comprobado; si falta algo, reduce o detiene.
También delegan en el CEO la firma de los gates de los meses 3, 6, 9 y 12, siempre
dentro del techo de cada tramo: todo lo que supere el techo de un tramo o amplíe
el alcance vuelve a este Directorio. La aprobación económica no habilita prácticas sin controles. En
marzo traemos base, política, matriz, pruebas y aprendizajes. El año sigue
condicionado."

## Qué no decir

- Que el plan se paga en el año o que genera caja: el modelo presupuesta
  beneficio de caja 0 e ingreso nuevo 0.
- "Caja cero": se confunde con desembolso cero. Decir "beneficio de caja
  estimado: 0".
- Que los 79 se liberan de una vez, que la preparación está ejecutada o que
  aprobar el plan libera agendas: son dos liberaciones, la segunda con
  condiciones (R-05), y las agendas se confirman antes de empezar. Para la primera, decir "caja incremental 0", junto con sus horas.
- Que 47/161/394 son alternativas equivalentes: son alcances distintos.
- Que una señal sola libera plataforma: rige la señal más cuatro condiciones (R-15),
  y los fondos los libera el Directorio.
- Que la plataforma pasa al año 2: se relee en los meses 3, 6 y 9.
- Que el 72,5% es un techo de adopción: es el resultado de cumplir exactamente
  las metas por área.
- Que el escenario base pasa la lectura del mes 9, o que el mes 6 lee valor: el
  mes 6 decide por adopción, costo y controles.
- Que se mide a cada persona: los indicadores son totales por área y semana (R-13).
- Que hay horas libres porque la utilización promedio lo sugiere.
- Que los secretos están bloqueados en toda superficie: hay compensatorios
  probados y residual aceptado, no bloqueo universal.
- Que la señal del mes 6 prueba disposición a pagar.
- Cualquier cifra que no esté en un anexo, o qué cliente o producto hay detrás
  de un alias o un rango.
- Que la defensa está ensayada, mientras no haya un ensayo registrado.
- Un monto de daño evitado o de pérdida esperada por no actuar: no hay
  probabilidad ni pérdida estimada. Sí se puede citar la exposición modelada a
  consumo (211-267k USD incrementales al año a 12×), aclarando que es un
  escenario a precio de API, no consumo facturado ni pronóstico, que es de la
  empresa con o sin plan y que el mínimo no la cubre.
- Que la falta de pasarela causa el consumo o que tenerla lo cubre: depende del
  régimen del proveedor y del ahorro medido.
- Que el mínimo compra producto, plataforma, referentes, cohortes nuevas o el
  estudio del rol, o que llega al "equilibrio": ese umbral es del paquete
  completo.
- Que los 79k USD son "lo que se puede perder": son un techo de recursos y no
  incluyen la contribución del trabajo facturable que puedan desplazar.
- Que los 12 voluntarios del piloto valoraron la herramienta: hubo 8% de
  detractores. Decir 92% de uso 3 o más días por semana y NPS +42.
- Que crédito y scoring son de alto riesgo regulatorio por vender a bancos: es
  un límite que nos ponemos, no una clasificación normativa.
- Que las cuatro competencias del capstone son la rúbrica del curso: la fuente
  dice "demostrar", no "evaluar", y no da rúbrica ni criterios.
- Un VPN: no hay tasa en el caso ni flujos positivos que descontar.
- Que el reskilling retiene un porcentaje del talento: la cifra del curso no
  tiene fuente.
- Que el estudio del rol crítico decide recortes, o que la postura sobre el
  empleo no tiene excepciones: el Directorio la adopta con asesoría laboral (R-20),
  con las causas previas ajenas a la IA afuera, y es costosa de deshacer una vez
  comunicada.
- Que el CEO puede subir un techo o compensar entre tramos: firma dentro del techo
  de cada tramo (79k hasta el mes 3; 16k, 13k y 13k después); lo demás vuelve al
  Directorio (R-03, R-04).
- Que "no contratamos" sin matiz: el plan no amplía la nómina, y toda incorporación
  externa es excepción del Directorio con caja propia (R-20).

## Reparto de presentadores: propuesta del equipo, no acordada

**Propuesta para discutir en #21; no está acordada.** El `README.md` dice que el
reparto de slides se acuerda en la tarea de defensa. Criterio: cada responsable
presenta la slide de su anexo y Lucho, que coordina la defensa, abre y cierra.
Son diez slides para ocho personas, así que dos integrantes presentan dos.

| Slide | Presenta | Responde objeciones | Respaldo en preguntas |
|---|---|---|---|
| Portada | Lucho | Storyline | Martín |
| Problema de negocio | Martín (Anexo A) | 19, 25, 45 | Eduardo |
| Priorización de iniciativas | Eduardo | 21, 22, 47 | Nico |
| Iniciativas concretas | Gabriela (Anexo E) | 6, 7, 37, 39, 50, 51 | Maxi |
| Arquitectura | Nico (Anexo B) | 1, 26, 28 | Rafa |
| Personas | Pablo (Anexo D) | 8, 9, 14, 15, 40-42, 44 | Gabriela |
| Gobierno y seguridad | Rafa (Anexo C) | 11, 12, 13, 20, 23 | Nico |
| Roadmap | Maxi (Anexo F) | 21, 24, 27, 43, 46 | Lucho |
| Dinero y escenarios | Gabriela (Anexo E) | 3, 10, 18, 29-36, 38, 49 | Maxi |
| Cierre | Lucho | "Qué estamos pidiendo hoy" (3, 31) | Martín |

- **Adaptación propuesta:** Eduardo presenta la priorización de iniciativas;
  Gabriela conecta operación, producto y alcance financiado. Reutiliza la propuesta
  anterior sin dar por acordados los mensajes nuevos. Una alternativa de reparto
  queda pendiente de definición por el equipo en #21/#27.
- **Dependencia:** revisión de mensajes por los responsables y acuerdo o descarte
  de esta estructura en #27; cualquier cambio de orden rehace el reparto por mensaje.
- **Qué falta para darlo por acordado:** la conformidad de los ocho en #21 y un
  ensayo registrado con fecha, tiempos y correcciones.
