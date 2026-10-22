---
owner: caio
status: ready
title: "Anexo G. Resoluciones del Directorio"
---

# Anexo G. Resoluciones del Directorio

::: {.annex-summary}
## Síntesis ejecutiva

**El Directorio aprueba un paquete con condiciones y delegaciones delimitadas.**
Las resoluciones R-01 a R-34 del desarrollo conservan su texto y rigen en
autoridad y condiciones. Esta síntesis facilita su lectura.

| Qué se decide | Límite y autoridad |
|---|---|
| Paquete mínimo | Medición, controles y formación; beneficio de caja e ingreso nuevo presupuestados: 0 |
| Primera liberación | Directorio: hasta 8k USD de tiempo y caja 0, diez días hábiles de validación con cargo a 2026 |
| Segunda liberación | CEO: hasta 71k adicionales, exclusivamente con todas las condiciones de R-05 |
| Techos | 79k hasta cerrar M3; después 16k, 13k y 13k por tramo. Total anual 121k; fijarlos no libera fondos |
| Gates | CEO firma dentro de cada tramo; CFO verifica y comité de IA dictamina. Excesos y ampliaciones vuelven al Directorio |
| Alcance excluido | Plataforma, construcción del producto y demás ampliaciones requieren otra decisión y costeo |

**Recomendación:** adoptar el paquete completo sin desprender sus condiciones.
La alternativa de liberar todo hoy anularía el control por evidencia. Martín
coordina la revisión del registro en el TP; las personas de Acme que ocupan cada
rol se nombran en las actas, con producción, verificación y firma separadas.

**Éxito y corte:** cada liberación tiene evidencia, autoridad y reserva suficiente.
Si falta una condición de la segunda liberación, no arranca M1: se reduce,
resecuencia o detiene. Seguridad puede suspender un uso aunque cumpla gasto
y adopción. Sin señal comercial escrita y problema medido, no se construye el
asistente. Las puertas irreversibles quedan para el cierre de M12 y el plan
siguiente.

**Registro por tema:** [autoridad y liberaciones](#autoridad-y-liberaciones),
[gobierno y seguridad](#gobierno-y-seguridad),
[arquitectura y medición](#arquitectura-y-medición), [personas](#personas),
[finanzas](#finanzas), [roadmap y comercial](#roadmap-y-comercial).
La [tabla de evidencia](#quién-produce-verifica-y-firma-cada-decisión) identifica
los roles por entregable.
:::

## Desarrollo y fuentes

Slides que sustenta: el cierre del [deck](../slides.md), "Aprobar el plan y sus
resoluciones", y cada slide que cita una resolución R-xx en su recuadro de
resolución. Montos en k USD (1k USD = 1.000 USD) salvo que se indique otra
unidad. Este anexo no agrega cifras: cada número viene del anexo que se cita al
final de cada resolución.

## Objetivo

Dejar en un registro único qué aprueba el Directorio al aprobar el plan. Cada
resolución dice qué se decide, quién tiene la autoridad, en qué hito, qué pasa si
no se cumple y si es reversible. Lo que depende de un hecho futuro (una medición,
un contrato, un regulador) queda como decisión delegada con autoridad, hito y
consecuencia. Ante una discrepancia con los Anexos A a F, rige este anexo en
autoridad y condiciones; en cifras rige el anexo dueño de la cifra.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Primera liberación | Caja 0; tiempo hasta 8 | [Anexo E](05-business-case.md), [Anexo F](06-roadmap-riesgo.md) |
| Segunda liberación | Hasta 71 (caja 10, tiempo 61) | [Anexo E](05-business-case.md) |
| Techo acumulado hasta cerrar M3 | 79 (caja 10 + tiempo 69); 85 en el año con núcleo de guardia | [Anexo E](05-business-case.md), [Anexo F](06-roadmap-riesgo.md) |
| Techo de tiempo M1-M3 | 59 | [Anexo E](05-business-case.md) |
| Suma de techos del año | 118 sin gastar reservas; 121 con cierre; techos por tramo 16 / 13 / 13 | [Anexo E](05-business-case.md), [Anexo F](06-roadmap-riesgo.md) |
| Beneficio de caja e ingreso nuevo presupuestados | 0 | [Anexo E](05-business-case.md) |
| Gate de valor | El mes 6 no lee valor: sigue por adopción, costo y controles, y corta por daño de calidad o caída demostrada. El mes 9 pasa si el peor caso es mayor que 0, sin daño; espera con estimado ≥ +5% sin pasar; corta con estimado < +5% o daño | [Anexo B](02-arquitectura.md), [Anexo F](06-roadmap-riesgo.md) |
| Roles de Acme que deciden | Directorio, CEO, CFO, AI Council, CAIO, Responsable de seguridad, Responsable de Tecnología, Personas, Producto, Comercial, Operaciones; roles por caso que ocupa una persona de esos roles: Dueño del dato, Dueño de negocio del caso, Dueño de producto (Producto), Responsable comercial del cliente (Comercial). Sin Delivery manager con autoridad propia | [Anexo C](03-gobierno-seguridad.md) |
| Personas que ocupan cada rol | Se nombran en el acta de cada liberación; el plan publica roles | Supuesto del CAIO (R-06) |

## Decisiones

**Al aprobar el plan, el Directorio resuelve:**

### Autoridad y liberaciones

- **R-01 · Paquete mínimo para medir.** El Directorio elige el paquete mínimo:
  financia producir una medición de valor contra una base, porque hoy no hay valor
  incremental medido. Beneficio de caja e ingreso nuevo presupuestados: 0; la rampa
  de ganancia en M1-M3 es 0%.
  *Autoridad:* Directorio. *Hito:* aprobación del plan; se relee en cada gate.
  *Si no se cumple:* si la segunda liberación no reúne sus condiciones (R-05), no se
  libera M1-M3 y rige reducir o detener. *Tipo:* reversible en cada gate.
  *Desarrolla:* [Anexo A](01-diagnostico.md), [Anexo E](05-business-case.md).
- **R-02 · Primera liberación.** Libera hoy hasta 8 de tiempo propio, caja 0, para
  diez días hábiles de validación inicial en la preparación de 2026. Produce el
  CAIO y verifica el CFO.
  *Autoridad:* Directorio. *Hito:* arranca cuando Operaciones y los managers
  confirman agendas e imputación 2026 y el Responsable de Tecnología confirma el
  acceso a las fuentes; el resultado llega al CEO antes de M1.
  *Si no se cumple:* sin agendas la ventana no empieza y M1 no arranca; si el
  resultado no sostiene el alcance, se reduce o resecuencia con recosteo, o se
  detiene con lo trabajado (hasta 8). *Tipo:* reversible.
  *Desarrolla:* [Anexo F](06-roadmap-riesgo.md), [Anexo E](05-business-case.md).
- **R-03 · Techos y reservas.** Fija 79 hasta cerrar M3, 85 en el año con el núcleo
  de guardia aprobado al salir, y 121 como suma de techos del año (118 sin gastar
  reservas), con un techo por tramo: M4-M6 16 (caja 2 + tiempo 14), M7-M9 13 (2 + 11)
  y M10-M12 13 (2 + 11); el techo de tiempo de M1-M3 es 59. Fijar no es liberar: hoy
  se liberan solo 8 (R-02). Las reservas de salida
  del mínimo (caja 1, tiempo 2) integran la segunda liberación y el CFO las
  recalcula en cada gate antes de asumir obligaciones nuevas. Tras un corte, el
  núcleo restringido (108 h, caja 0, tiempo hasta 6) lo firma el CEO en el gate de
  salida, dentro de 85 y con verificación del CFO; la continuidad por superficie
  la autoriza el Responsable de seguridad. Ni la contribución desplazada ni una
  facilitación externa están dentro de 79.
  *Autoridad:* Directorio fija; CFO verifica. *Hito:* aprobación del plan; cada gate.
  *Si no se cumple:* superar el techo de un tramo, aunque el acumulado quede debajo
  de 121, o cualquier camino con espera que supere 121, exige nueva resolución del
  Directorio; sin reserva suficiente, el gate no libera el compromiso nuevo; tras un corte, el uso
  no cubierto se suspende. *Tipo:* reversible.
  *Desarrolla:* [Anexo E](05-business-case.md), [Anexo F](06-roadmap-riesgo.md).
- **R-04 · Delegación en el CEO.** El Directorio delega por acta en el CEO la
  segunda liberación y la firma de los gates de los meses 3, 6, 9 y 12, siempre
  dentro del techo del tramo que corresponde según R-03 (79 hasta M3; 16, 13 y 13
  después). Un gasto de IA fuera del presupuesto que entra en el techo del tramo lo
  firma el CEO; por encima, el Directorio. El CFO fija el tope de costo por PR y de
  consumo como parámetro de control y verifica; no libera fondos. Vuelve al
  Directorio todo lo que supere el techo de un tramo o
  amplíe alcance (plataforma, construcción del producto, exploración comercial
  costeada, compromisos a más de 12 meses, lo irreversible) y los cambios de
  política. El CAIO produce el paquete de cada gate; el CFO verifica cifras, caja y
  reservas y no libera fondos; el AI Council dictamina antes de cada gate y no
  libera fondos.
  *Autoridad:* Directorio delega; CEO firma. *Hito:* acta de delegación antes de la
  segunda liberación. *Si no se cumple:* sin acta, la segunda liberación la decide
  el Directorio en sesión y M1 no empieza hasta entonces. *Tipo:* reversible; la
  delegación se revoca en cualquier sesión.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo E](05-business-case.md),
  [Anexo F](06-roadmap-riesgo.md).
- **R-05 · Segunda liberación.** El CEO libera hasta 71 (acumulado 79) solo con:
  diagnóstico revisado; matriz persona/semana con trabajo desplazado y
  recuperación; acta de viabilidad con método ratificado (R-14); productor,
  verificador y firmante nombrados (R-06); presupuesto 2027 comprobado; solapes
  conciliados (R-26) y facilitación del básico resuelta (R-22). La capacidad se lee
  con sobre separado: la reserva de soporte clave (hasta 720 h) y la de formación
  (540-660 h) se confirman por separado. La contribución comercial desplazada se
  informa, estimada por la matriz, sin umbral.
  *Autoridad:* CEO, por delegación; produce el CAIO; verifican el CFO (costo,
  presupuesto 2027, contribución desplazada) y el Responsable de seguridad (política
  y controles); dictamina el AI Council. *Hito:* antes del inicio de M1, al cierre
  de la validación. *Si no se cumple:* falta un elemento y no se libera M1-M3; se
  reduce o resecuencia con recosteo dentro de 71, o se detiene; excederlo vuelve al
  Directorio. *Tipo:* reversible hasta 79 al cerrar M3.
  *Desarrolla:* [Anexo E](05-business-case.md), [Anexo F](06-roadmap-riesgo.md).
- **R-06 · Quién produce, verifica y firma.** Rige la separación por rol y por
  entregable de la tabla de "Evidencia": ningún rol produce y verifica el mismo
  entregable. Las personas que ocupan cada rol se nombran en el acta de la
  liberación que habilita el entregable. Sin verificador independiente rige excluir
  la superficie; un verificador externo acotado solo entra si está cotizado, cabe en
  el techo y lo autoriza el CEO. El Responsable de Tecnología responde por los hitos
  técnicos y el CFO por cada cifra del business case. Quien produce o verifica un
  entregable no vota su aceptación: al aceptar un residual o ratificar el método de
  medición, ese asiento del AI Council se abstiene; si el dueño del riesgo produjo o
  verificó la prueba de su control, acepta el AI Council. Quórum: tres asientos con
  voto; si no se alcanza, el residual no se acepta y rige la suspensión preventiva.
  Los dictámenes y la declaración de una señal los emite el Council completo y el
  acta registra quién produjo y quién verificó. La suspensión preventiva es
  contención unilateral y no lleva productor ni verificador previos; la reanudación
  sí: Ingeniería produce, verifica el Responsable de seguridad (o el verificador
  senior independiente si Seguridad produjo parte de la evidencia) y acepta la
  autoridad del residual (R-10).
  *Autoridad:* Directorio (regla); CEO valida los nombres en la segunda liberación.
  *Hito:* acta de la primera liberación (preparación) y de la segunda (M1-M3).
  *Si no se cumple:* el entregable no se declara probado y la superficie queda
  excluida; sin nombres no hay segunda liberación; si la exclusión deja sin
  superficies a la cohorte, el tramo se reduce o se detiene. *Tipo:* reversible.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo F](06-roadmap-riesgo.md).

### Gobierno y seguridad

- **R-07 · Política de IA.** Ratifica la política de uso de IA vigente como
  política del plan; el acta de aprobación del plan es su respaldo documental. La
  preparación de 2026 deja constancia de versión y alcance, y el mes 3 verifica que
  se aplique y su alcance aplicable al producto. La mantiene el Responsable de
  seguridad.
  *Autoridad:* Directorio (ratifica y aprueba cambios). *Hito:* hoy; constancia en
  la preparación; aplicación en el mes 3. *Si no se cumple:* sin constancia al
  cierre de la preparación, la segunda liberación no se firma hasta que el
  Directorio la deje asentada; sin aplicación y cobertura demostradas al vencer el
  plazo de 6 semanas del mes 3 (no es la espera de throughput de R-27), no hay frente producto en el año. *Tipo:* reversible, con
  costo de credibilidad. *Desarrolla:* [Anexo C](03-gobierno-seguridad.md).
- **R-08 · Alcance del horizonte.** En los 12 meses el código o los datos de un
  cliente (código, documentación, tickets y datos, productivos o no, que un cliente
  entrega o que se producen para él bajo contrato) no salen hacia un modelo externo,
  salvo dentro del entorno del propio cliente y con su permiso escrito. La única
  excepción es la transitoria de R-09 para código sin NDA, hasta el gate del mes 3.
  Sin crédito ni scoring; la clasificación de riesgo es caso por
  caso, y los datos de categoría especial siguen prohibidos en el intake. Ninguna
  función de IA se asienta en el producto de medios de pago hasta que su entidad
  operadora acredite la habilitación que corresponda; la verifica Producto, con
  Legal externo, en la lectura del mes 6.
  *Autoridad:* Directorio; Producto verifica la habilitación. *Hito:* hoy; la
  habilitación, en el mes 6 (o el 9 si se difiere); reabrir el alcance, solo en el
  cierre del mes 12. *Si no se cumple:* un uso que no encaje no se habilita y, si ya
  corre, rige R-09; sin habilitación acreditada, el piloto usa otro producto o se
  difiere. *Tipo:* reversible hasta firmar un compromiso con un cliente.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md).
- **R-09 · Clientes: uso existente y matriz de restricciones.** El código bajo NDA
  se suspende desde la aprobación del plan: es Restringido en la clasificación de la
  política que R-07 ratifica. El uso que ya corre sobre código sin NDA de un cliente
  sigue, sin ampliarse, como residual transitorio (Media / Alto) que acepta el AI
  Council con informe al CEO, hasta el gate del mes 3; los datos de un cliente no
  entran en esta excepción y lo que el contrato prohíbe se suspende. Comercial
  completa la matriz de restricciones de los clientes principales al cierre de M1-M3
  (produce Operaciones, verifica Seguridad). Un uso nuevo o ampliado sobre un
  cliente exige su fila en la matriz y su permiso escrito; sin fila rige
  *default-deny*, sin excepción caso por caso.
  *Autoridad:* AI Council (residual); Comercial (matriz); Responsable de seguridad
  (suspensión). *Hito:* hoy para el código bajo NDA; gate del mes 3 para el resto;
  mes 4 para los contratos ambiguos. *Si no se cumple:* desde el mes 3 el uso sigue
  solo si encaja en R-08; prohibitivo, ambiguo o no leído, *default-deny*; con más de
  30% ambiguo al mes 4, *default-deny* con revisión legal y sin piloto con ese
  cliente; un incidente confirmado revoca la aceptación para ese cliente. Sostener
  después del mes 3 el uso con la herramienta corporativa, con permiso escrito, es
  una modificación de R-08 que el Directorio decide en ese gate.
  *Tipo:* reversible, cliente por cliente.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo D](04-personas-cultura.md).
- **R-10 · Apetito de riesgo y registro único.** Adopta el criterio de aceptación
  del residual del Anexo C, completado por dominancia (más probabilidad o más
  impacto nunca bajan la autoridad). Acepta el dueño del riesgo: Baja con impacto
  hasta Alto; Media o Alta con Bajo; Media con Medio. Acepta el AI Council, con
  informe al CEO: Media con Medio-alto o Alto; Alta con Medio o Medio-alto; Baja con
  Muy alto. No acepta nadie: Alta con Alto o mayor; Media con Muy alto. El registro
  del Anexo C es el de referencia: datos de un cliente en un modelo externo, Media /
  Alto; "superficies sin control técnico central" es un atributo de las filas de
  datos de cliente y fuga de secretos, sin calificación propia. Hasta probar el
  control rige el inherente, y lo acepta la autoridad que le corresponde por esta
  tabla, con fecha de prueba. Si el inherente cae en "nadie" (capacidad concentrada,
  Alta / Alto), no se dan de alta casos nuevos de nivel 3 del intake hasta que el
  suplente corra el runbook en el ejercicio de mesa de M4-M6. Suplente para
  contener: el Responsable de Tecnología, que suspende pero no reanuda ni acepta
  residuales. El CEO no levanta una suspensión fuera del procedimiento de
  reanudación (R-06) y de esta resolución.
  *Autoridad:* Directorio adopta; el Responsable de seguridad mantiene el registro y
  el AI Council lo revisa cada mes. *Hito:* hoy; recalibración con la base de
  M1-M3. *Si no se cumple:* un residual sin fila no se acepta y rige la suspensión
  preventiva; si la prueba de una superficie no alcanza su residual objetivo, su uso
  sobre clientes se suspende. *Tipo:* reversible.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo F](06-roadmap-riesgo.md).
- **R-11 · Controles: clasificación y calendario.** Adopta la clasificación de
  controles exigibles y opcionales del Anexo C: los exigibles rigen en las dos
  ramas, las opciones se liberan solo por la señal del gate que las lee y cada
  control nombra su motivo y su alternativa de menor costo. Toda superficie que se
  use en M1-M3 prueba sus controles en M1-M3, dentro del techo de 59; si su prueba
  no cabe en las horas validadas, esa superficie no se usa hasta M4-M6. Toda
  afirmación comercial sobre seguridad o IA la valida el Responsable de seguridad
  antes de salir.
  *Autoridad:* Directorio (regla); el Responsable de seguridad decide por superficie
  si está probada y el CFO verifica que cabe; pasar un control de exigible a opción
  lo decide el Directorio en un gate, a propuesta del Responsable de seguridad con
  el AI Council. *Hito:* hoy; dictamen de Legal externo en M1; matriz del mes 3.
  *Si no se cumple:* sin prueba no hay uso; si el dictamen o la matriz agregan un
  requisito, el control sube a exigible en el gate siguiente con su costo
  verificado por el CFO; una afirmación no respaldada se retira y se escala al
  AI Council. *Tipo:* reversible.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo F](06-roadmap-riesgo.md).
- **R-12 · Incidentes de IA.** Es incidente de IA el evento confirmado de un
  disparador del registro de riesgos. Severidad 1: toca código o datos de un
  cliente, producción o una afirmación hecha a un cliente; severidad 2: el resto.
  Contención inmediata; aviso al cliente según su contrato (o, si no fija plazo,
  antes de la reunión semanal siguiente); revisión de causa en la revisión mensual
  del AI Council; informe al CEO en severidad 1. Se preservan ticket, logs, prompts
  y acciones, decisión de contención y acta de reanudación. La ruta se monta sobre
  el circuito de incidentes del SGSI existente, dentro de las horas de "Política e
  intake": 0 USD adicionales en M1-M3. Se conservan los dos ejercicios de mesa
  (M4-M6 y M10-M12).
  *Autoridad:* Directorio (estructura); Responsable de seguridad (contención y
  comunicación). *Hito:* ruta escrita antes de habilitar cualquier uso del mínimo.
  *Si no se cumple:* no se habilita ningún uso nuevo y los existentes quedan bajo la
  suspensión preventiva; si el circuito existente no sirve, la ruta se escribe
  igual dentro de las mismas horas. *Tipo:* reversible.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo E](05-business-case.md).
- **R-13 · Datos de uso por persona y trazas.** El Responsable de seguridad decide
  el tratamiento y la retención de los eventos de uso por persona y de las trazas
  del harness; Personas y Legal externo son consultados (revisión laboral y Ley
  25.326) y el CAIO decide solo qué indicador se reporta. Por defecto: agregados por
  área desde las consolas existentes; ningún evento por persona se extrae ni se
  retiene fuera de las consolas; ninguna métrica evalúa desempeño individual; el
  harness no persiste trazas hasta aprobar clasificación, ubicación y plazo.
  *Autoridad:* Responsable de seguridad. *Hito:* tratamiento aprobado y comunicado
  en la preparación de 2026, antes de extraer cualquier serie: el Responsable de
  seguridad fija la regla por defecto (agregados por área), que no necesita dictamen
  legal; un tratamiento por persona espera la revisión de M1 con Personas y Legal
  externo; trazas, antes del harness v1 (M4-M6, solo con plataforma). *Si no se
  cumple:* no se extrae ninguna serie, esa fuente se publica "sin medir" y la
  lectura usa agregados; si no alcanzan, el indicador se reformula en el mes 3, sin
  ampliar la captura; sin retención aprobada, el caso de referencia queda en
  evaluación offline. *Tipo:* reversible mientras no se retenga el dato; la
  retención hecha es irreversible para esas personas.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo D](04-personas-cultura.md),
  [Anexo B](02-arquitectura.md).
- **R-34 · Supuestos regulatorios sin uso decisorio.** El plan trata como
  supuestos la vigencia posterior y el alcance sobre cada cliente de los textos
  ordenados del BCRA que cita el Anexo C, su traslado a Acme Labs y la
  aplicabilidad del AI Act al caso (art. 2.1.c). Ninguna liberación, gate ni
  resolución depende de verificarlos: las decisiones se apoyan en la evidencia
  contractual de los meses 1-3 (R-09). Las fechas del AI Act cotejadas contra el
  DOUE se usan como contexto del calendario, no como obligación de Acme Labs. La
  revisión jurídica es una actividad de ejecución: el dictamen focalizado de Legal
  externo arranca en M1, dentro del legal focalizado ya costeado en M1-M3. Esta
  resolución no crea obligaciones jurídicas ni reconoce que una norma aplique.
  *Autoridad:* AI Council, con Legal externo; el Responsable de seguridad lleva el
  hallazgo al intake. *Hito:* dictamen focalizado de M1-M3. *Si no se cumple:* sin
  dictamen, los supuestos siguen sin uso decisorio y los casos que podrían caer en
  alto riesgo quedan fuera de la liberación hasta tenerlo; si el dictamen muestra
  que una norma alcanza a un caso, ese caso vuelve al intake y cualquier cambio de
  alcance o techo vuelve al Directorio. *Tipo:* reversible.
  *Registro:* decisión del responsable del caso del 2026-10-22
  ([#56](https://github.com/lazynet/tp-caio-g11-2026/issues/56)).
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo F](06-roadmap-riesgo.md).

### Arquitectura y medición

- **R-14 · Método de medición.** Producen QA/análisis de datos (extracción, base,
  tasas) y DevOps (exportaciones), bajo el Responsable de Tecnología; Arquitectura
  redacta el protocolo. Verifica el verificador senior independiente, fuera de la
  línea de Tecnología: el acta de viabilidad y los indicadores de cada lectura; el
  Responsable de seguridad clasifica la severidad de los incidentes. Los
  indicadores se calculan en totales por área y semana (R-13). El AI Council
  ratifica el método sobre la tabla de operación del acta: estimador,
  sobredispersión, ventanas, muestra mínima, cohorte, extensión de la base y el gate
  de valor del Anexo B (el mes 6 no lee valor; el mes 9 pasa si el peor caso es
  mayor que 0; la calidad es guardia de daño). Quien produjo o verificó se abstiene
  en esa ratificación. La autoridad del gate no ratifica el método.
  *Autoridad:* AI Council. *Hito:* antes de la segunda liberación, sobre el acta de
  la validación. *Si no se cumple:* sin método ratificado no se libera M1-M3; con
  menos de 15 personas activas, o si ni con base de 8 semanas la lectura del mes 9
  distingue con 80% de potencia una ganancia de +25% (techo del rango supuesto), el
  AI Council ratifica que ninguna lectura decide por valor y el beneficio acreditado
  es 0. *Tipo:* reversible; un cambio posterior es un desvío fechado que rige desde
  la ventana siguiente. *Desarrolla:* [Anexo B](02-arquitectura.md).
- **R-15 · Plataforma: señal más cuatro condiciones.** Liberar plataforma en el mes
  3, 6 o 9 exige una señal (contractual, de precio o de producto, con los umbrales
  del Anexo C) y además: (1) brecha documentada, (2) alternativas comparables,
  (3) economía incremental o aprendizaje con pérdida aceptada y límite de pérdida
  declarado y (4) capacidad demostrada. Una prohibición pura excluye el uso y no
  libera plataforma. Producen la evidencia el Responsable de Tecnología (1, 2 y la
  parte técnica de 4), Personas (horas de 4) y el CFO (3); el Responsable de
  seguridad verifica los controles de 1 y 4; el AI Council dictamina.
  *Autoridad:* Directorio: ratifica hoy la regla, libera los fondos y es el único
  que acepta la pérdida de aprendizaje; recalibrar los umbrales también es suyo, a
  propuesta del AI Council. *Hito:* hoy (regla); meses 3, 6 y 9 (aplicación).
  *Si no se cumple:* falta una condición y no se libera plataforma: sigue el mínimo
  costeado y se relee en M6/M9; nada pasa al año 2 por defecto. *Tipo:* reversible;
  la regla se enmienda en cualquier gate y liberar es reversible hasta firmar
  contratos largos. *Desarrolla:* [Anexo B](02-arquitectura.md),
  [Anexo C](03-gobierno-seguridad.md), [Anexo E](05-business-case.md),
  [Anexo F](06-roadmap-riesgo.md).
- **R-16 · Evidencia de plataforma para el mes 3.** La comparación configurar /
  comprar / ensamblar se produce en M1-M3 y se lee en el mes 3: elige alternativa
  el Responsable de Tecnología, habilita datos el Responsable de seguridad según la
  matriz contractual, acepta o restringe el residual la autoridad de R-10 y libera
  fondos el Directorio. El relevamiento técnico de capacidades (gateway,
  inventario de arquitectura, harness interno) lo hace el Responsable de Tecnología
  dentro de las 24-40 h de Arquitectura ya costeadas; el legal lo encarga el
  Responsable de seguridad, y una asesoría externa entra solo con cotización
  verificada por el CFO.
  Después de M1, la provisión de caja de cada tramo (0-1,5 más 15%, techo 2) es única
  para herramientas o consulta legal puntual de hasta 4 h: M4-M6, cláusulas ambiguas
  de la evidencia contractual del gate del mes 6; M7-M9 y M10-M12, incidente o cambio
  contractual. Las dos al máximo no entran (3,45 contra 2): se recostea dentro del
  techo del tramo o vuelve al Directorio. La revisión normativa completa y un
  dictamen nuevo son alcance ampliado (R-28).
  *Autoridad:* las cuatro de arriba. *Hito:* técnico, decisión del mes 3; legal,
  antes de la revisión de ambiguos del mes 4 y de la cláusula tipo de M7-M9.
  *Si no se cumple:* sin comparación completa rige configurar lo existente sin caja
  nueva y la condición 2 de R-15 no se cumple; sin relevamiento técnico no hay
  brecha documentada; si no cabe en las horas, se recostea antes de la segunda
  liberación; sin relevamiento legal, los contratos ambiguos siguen en
  *default-deny*; sin bloqueo probado, la superficie se restringe o se suspende.
  *Tipo:* reversible. *Desarrolla:* [Anexo B](02-arquitectura.md),
  [Anexo C](03-gobierno-seguridad.md), [Anexo E](05-business-case.md).
- **R-17 · Rama con plataforma.** Solo si el Directorio libera plataforma (R-15):
  rige el replan de M4-M6 (Arquitectura 0,4; DevOps/QA 0,8; contractor 0,2), con el
  0,2 confirmado por Personas en su contrato y la excepción de 0,3 FTE solo con
  aprobación previa del Directorio. Cada ruta del gateway la habilita el
  Responsable de Tecnología tras la prueba de portabilidad y costo, con el régimen
  comercial confirmado por escrito con el proveedor y verificado por el CFO. Con
  suscripción que no permite gateway, el Responsable de Tecnología costea M7-M12 y
  el CFO lo verifica; no se publica un año para ese régimen.
  *Autoridad:* Directorio (liberación y excepción); Responsable de Tecnología
  (rutas). *Hito:* mes 3 (o 6 y 9 si la señal llega tarde); antes de activar ruteo;
  antes del gate del mes 6. *Si no se cumple:* sin contractor ni perfil interno
  demostrado al inicio de M4, no se inician los hitos de IA aplicada; una ruta sin
  régimen confirmado queda en laboratorio con tráfico sintético; sin costeo de
  M7-M12, no se libera M7-M9. *Tipo:* reversible hasta firmar contratos largos.
  *Desarrolla:* [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md).
- **R-18 · Calendario de la base y lectura del mes 3.** El camino esperado es la
  base de 8 semanas: con los valores ilustrativos del Anexo B, la de 4 no alcanza la
  potencia del criterio mecánico. Básico, intermedio y prueba se desplazan juntos a
  la semana 9 y la lectura del mes 3 es reducida y declarada (unas 3 semanas de PR
  maduros): informa uso, retrabajo y PR maduros sin atribuir ganancia, y no se corre
  ni atrasa M4. Si el acta, con los valores reales, muestra que la base de 4 semanas
  alcanza, la base se congela en la semana 4 y la formación empieza en la 5.
  *Autoridad:* la oficina del CAIO aplica el disparador y Arquitectura lo verifica;
  el CAIO presenta la lectura, el CFO la verifica y el CEO firma el gate.
  *Hito:* acta de viabilidad (camino esperado), semana 4 (disparo con λ y φ
  observados); cierre del mes 3 (lectura). *Si no se cumple:* la meta del básico del
  mes 3 se revisa con el calendario más corto; la lectura de valor queda en el mes 9
  (R-19); correr la lectura del mes 3 solo si el Directorio lo pide, con su costo.
  *Tipo:* reversible.
  *Desarrolla:* [Anexo B](02-arquitectura.md), [Anexo F](06-roadmap-riesgo.md).
- **R-19 · Ganancia: medir, leer y convertir.** La ganancia de productividad es una
  hipótesis. Tecnología produce los indicadores con el protocolo del Anexo B y el
  verificador senior independiente los verifica; el AI Council lee en los meses 9 y
  12 con el gate de valor del Anexo B, calidad primero; el mes 6 no lee valor.
  Convierte el CFO: se acredita el peor caso de una lectura que pasó, la capacidad
  liberada cuenta como beneficio solo si en el mes 6 hay un destino decidido (vender
  capacidad o evitar una contratación), y se valoriza como horas a costo cargado, no
  como caja. Los meses 3 y 6 no atribuyen ganancia. Las métricas de seguimiento
  (Operaciones habilitadas, destino de la capacidad, Tecnología sostenida, pedidos
  con ejemplos, costo por PR aceptado, residuales revisados) se informan y no liberan
  ni cortan fondos.
  *Autoridad:* Tecnología (produce), verificador senior independiente (verifica),
  AI Council (lee), CFO (convierte). *Hito:* meses 9 y 12. *Si no se cumple:* sin
  pasar, rige la espera única del mes 9 o el corte (R-27); si la medición no
  distingue, o no hay destino, el beneficio es 0. *Tipo:* reversible.
  *Desarrolla:* [Anexo B](02-arquitectura.md), [Anexo E](05-business-case.md),
  [Anexo F](06-roadmap-riesgo.md).

### Personas

- **R-20 · Postura sobre el empleo.** En los 12 meses, la mejora por IA no se usa
  para desvincular: primero se reasigna y se capacita; quedan afuera las causas
  previas ajenas a la IA. El plan no amplía la nómina: toda incorporación externa
  (la facilitación de R-22, el contractor de la rama con plataforma de R-17) es
  excepción del Directorio, con caja propia. Costo incremental 0, porque el plan no
  presupuesta ahorro de nómina ni contratación. El CAIO es un rol existente
  reasignado, distinto del Responsable de Tecnología, del de seguridad, del CFO y del
  CEO; su dedicación se absorbe en el Anexo E (48-96 h en M1-M3; 14-24 h por tramo
  después, dentro de las 36-60 h del tech lead). El estudio de un rol crítico es
  alcance ampliado, con horas y autorización propias del Directorio, después de
  comunicar la postura.
  *Autoridad:* Directorio, con asesoría laboral sobre el texto; comunica el CEO. La
  asesoría laboral va dentro de las 8-16 h del dictamen legal de M1-M3 si su
  cotización deja 2-4 h (la verifica el CFO y la firma el CEO en la segunda
  liberación); si no, 0,575-1,725 de caja fuera de 79, que aprueba el Directorio,
  como R-22. *Hito:* hoy; comunicación en M1, antes de cualquier estudio del rol.
  *Si no se cumple:* sin asesoría aprobada, la postura no se comunica; sin
  comunicación no arranca el estudio del rol. *Tipo:* **costosa de
  deshacer** una vez comunicada. *Desarrolla:* [Anexo D](04-personas-cultura.md),
  [Anexo F](06-roadmap-riesgo.md).
- **R-21 · Formación del mínimo y evaluación del básico.** Rige la alternativa
  vigente: básico de 6 h para 60-70 personas e intermedio de 12 h para la cohorte de
  15-20 (540-660 h); el módulo de uso seguro no se recorta. Completar el básico es
  aprobar un caso permitido para el rol, con datos sintéticos o autorizados y
  evidencia de la revisión del resultado: usa herramienta y superficie permitidas,
  no envía datos prohibidos, revisa el resultado y sabe dónde reportar un incidente.
  Evalúa la facilitación técnica dentro de sus 16-32 h y registra Personas dentro
  de sus 8-16 h. Núcleo con profundización y secuenciar quedan como opciones del
  rediseño del mes 3, costeadas solo si se activa.
  *Autoridad:* el CAIO aprueba el instrumento; si la matriz no confirma horas,
  Personas propone reducir o resecuenciar, el CFO verifica y el CEO lo firma en la
  segunda liberación dentro del techo de 59; el rediseño del mes 3 lo propone el
  CAIO y lo firma el CEO en el gate, con recosteo del CFO. *Hito:* segunda
  liberación (horas); antes de iniciar el básico, semana 5 o 9 (instrumento).
  *Si no se cumple:* la formación no confirmada se resecuencia; sin encaje en las
  horas el básico no se inicia hasta recostear; dictado sin instrumento, el ≥90%
  queda "sin medir", no se da por cumplido y aplica la banda de rediseño.
  *Tipo:* reversible. *Desarrolla:* [Anexo D](04-personas-cultura.md),
  [Anexo E](05-business-case.md).
- **R-22 · Facilitación del básico.** La facilitación es interna. Si en la segunda
  liberación no hay perfil interno demostrado, una intervención externa de 16-32 h
  que reemplaza la fila interna requiere cotización y resolución del Directorio,
  porque su caja queda fuera de 79; el CFO verifica la cotización.
  *Autoridad:* Directorio. *Hito:* segunda liberación. *Si no se cumple:* sin vía
  demostrada ni cotización aprobada, el módulo se difiere, se recostea y la meta del
  básico del mes 3 se revisa. *Tipo:* reversible.
  *Desarrolla:* [Anexo D](04-personas-cultura.md), [Anexo F](06-roadmap-riesgo.md).
- **R-23 · Adopción: definición, metas y brecha del OKR.** "Activo" es quien hace
  al menos una tarea laboral con una herramienta permitida y revisa su resultado en
  la semana. La medición semanal es la lectura oficial para metas, gates y OKR; la
  ventana móvil de cuatro semanas es una serie auxiliar de tendencia, sin efecto
  sobre metas ni aplicación retroactiva. Rigen metas por área, Operaciones sobre
  habilitadas, y el combinado original informado con su denominador completo.
  Operaciones no tiene meta en el mes 6; ≥40% al cierre del mes 9 como meta
  intermedia informada y ≥60% en el mes 12, solo si el Directorio autoriza el
  programa ampliado en el gate del mes 6. La
  brecha contra el OKR 2027 es contractual, no cultural. El programa cultural
  ampliado de los meses 4-12 informa sus metas sin comprarlas; su costeo y
  autorización son del Directorio en el gate del mes 6.
  *Autoridad:* Directorio, a propuesta del Responsable de Tecnología (dueño del OKR)
  y del CAIO, que opera el diccionario de indicadores. *Hito:* diccionario cerrado
  antes de congelar la base (semanas 1-4 de M1); en el mes 3, con base y matriz, el
  Directorio decide si pide revisar el resultado clave. *Si no se cumple:* si el
  diccionario no distingue tarea de conexión, se publica como proxy del agente de
  código y la meta no se declara cumplida; sin matriz en el mes 3, no hay meta en
  Operaciones y el combinado se informa sin declararlo cumplido ni incumplido.
  *Tipo:* reversible antes de congelar la base; después obliga a recalcular la
  serie. *Desarrolla:* [Anexo D](04-personas-cultura.md),
  [Anexo F](06-roadmap-riesgo.md).
- **R-24 · Validación organizativa y matriz de capacidad.** Adopta 60-96 h (1-4,1;
  techo 5) como presupuesto de la validación organizativa, confirmado por Personas
  como estimación de planificación. Quien solo hace el básico se planifica por
  bloque de área o turno; el detalle por persona y semana queda para horas clave,
  la cohorte del intermedio y los roles acumulados. La matriz de capacidad suma tres
  columnas: horas clave y distribuidas por separado, tipo de hora y cliente o
  contrato con identificador privado.
  *Autoridad:* Personas (estimación y matriz); el CFO verifica que entra en el techo.
  *Hito:* día 2 de la ventana, con una prueba de una hora sobre un área y el export
  confirmado. *Si no se cumple:* el día 3 se reduce el detalle a horas clave y
  cohorte, o se recostea dentro del techo de 5; si lo excede, la ventana se detiene
  y vuelve al Directorio; horas sin "cliente o contrato" se tratan como facturables
  desplazadas. *Tipo:* reversible. *Desarrolla:* [Anexo D](04-personas-cultura.md),
  [Anexo E](05-business-case.md).

### Finanzas

- **R-25 · Horas de gobierno y demanda de M1-M3.** El tech lead de gobierno dedica
  22-32 h en M1-M3, la suma de las actividades del Anexo C. La demanda interna de
  M1-M3 queda en 970-1.346 h, con un máximo de tiempo de 58,03 y un margen de 34 h
  sobre la reserva clave (cálculo en "Evidencia"). La verificación de la lectura del
  mes 3 (4-5 h, 0,075-0,234 k USD) es el primer uso declarado del margen de 34 h:
  soporte 434-691 h, total 974-1.351 h, tiempo máximo 58,27, debajo de 59. La
  demanda de actividades (970-1.346 h) no cambia. No cambian los techos de 8, 71,
  79, 59, 118 ni 121. El business case no publica un punto medio del pedido: el
  Directorio aprueba techos, no gasto esperado.
  *Autoridad:* Directorio, a propuesta del Responsable de seguridad; el CFO
  verifica y propaga. *Hito:* hoy; propagación a los anexos y al deck antes de la
  entrega. *Si no se cumple:* donde la propagación no llegue, rige 1.350 h como cota
  prudente, con la diferencia de 0,25 declarada. *Tipo:* reversible.
  *Desarrolla:* [Anexo C](03-gobierno-seguridad.md), [Anexo E](05-business-case.md).
- **R-26 · Solapes de horas.** Adopta los solapes del business case: QA del Anexo B
  contiene la reproducción del Anexo D (8-16 h); las 64 h de seniors contienen la
  revisión del Anexo B (16-24 h); la matriz de seguridad entra en las 24-40 h del
  Anexo B, con Seguridad que verifica y no produce los compensatorios. DevOps 40-64 h
  es el tope de configuración, prueba, corrección y exportaciones de consolas: un
  límite de alcance, no un ahorro. Las 8-16 h de managers en M1-M3 cubren solo la
  actualización semanal de agendas; la validación inicial de agendas se imputa en la
  primera liberación y no se repite.
  *Autoridad:* confirman el Responsable de Tecnología (desglose de DevOps) y el
  Responsable de seguridad; Personas define el alcance de managers; el CFO verifica
  y publica el remanente. *Hito:* durante la validación; antes de la segunda
  liberación. *Si no se cumple:* si las exportaciones no caben en el tope, se
  reportan como uso estimado, sin sumar horas; si aun así no cabe, el CFO recostea
  antes de M1 dentro de 71 y firma el CEO; superar 71 vuelve al Directorio; el techo
  de 59 no sube. *Tipo:* reversible. *Desarrolla:* [Anexo B](02-arquitectura.md),
  [Anexo D](04-personas-cultura.md), [Anexo E](05-business-case.md).
- **R-27 · Espera única, en el mes 9.** Una sola espera de 6 semanas, en el mes 9,
  cuando el estimado es ≥ +5% sin que el peor caso pase de 0; sin expansión ni
  producto, con subtramo propio (64-106 h; techos 1 / 6) dentro del techo de M10-M12
  (2 / 11): el resto del trimestre se recostea contra lo que la espera calculó o
  ejecutó. La reserva de salida se usa una sola vez.
  *Autoridad:* el AI Council recomienda abrirla; el CEO firma el subtramo dentro del
  techo del tramo; el CFO verifica. *Hito:* cierre del mes 9 más 6 semanas.
  *Si no se cumple:* si al vencer no pasa valor y calidad con la versión congelada,
  se corta el frente interno con la precedencia del Anexo F (seguridad,
  dependencias, caja): 115 hasta cerrar y 116 en el año. Caminos: corte en M6 95 /
  99; en M9 108 / 110; espera que vence 115 / 116; sin espera o espera que pasa,
  121. Ningún camino supera 121; superar el techo de un tramo vuelve al Directorio.
  No hay segunda espera ni espera en el mes 6: seis semanas más no compran
  precisión, porque el piso lo pone la base. *Tipo:* reversible.
  *Desarrolla:* [Anexo E](05-business-case.md), [Anexo F](06-roadmap-riesgo.md).
- **R-28 · Alcances no pedidos.** El paquete completo (33+6 / 72+7), su preparación,
  la referencia anual del Anexo C y las alternativas de menor alcance ampliadas
  quedan como antecedente: no se autorizan ni se suman al pedido. Los costos
  publicados de alcances distintos (47 / 161 / ≈199 / 394 / ≈400 / 471) son
  referencia, no comparación.
  *Autoridad:* Directorio; si un gate propone ampliar o usar un renglón anual, el
  CFO presenta antes una estimación común desde ese gate (gasto futuro evitable,
  sin costos hundidos) y decide el Directorio. *Hito:* el gate que proponga ampliar.
  *Si no se cumple:* sin estimación común no hay decisión de ampliación; una
  alternativa reactivada no se ejecuta sin champions y agendas confirmados por
  Personas y repositorios habilitados por el Responsable de seguridad.
  *Tipo:* reversible. *Desarrolla:* [Anexo E](05-business-case.md),
  [Anexo C](03-gobierno-seguridad.md), [Anexo F](06-roadmap-riesgo.md).
- **R-29 · Gasto de tecnología del OKR.** El indicador de gasto de tecnología del
  OKR se mide sin la inversión del plan, y ese gasto se informa igual, aparte.
  *Autoridad:* Directorio, en el presupuesto 2027. *Hito:* segunda liberación, con
  el presupuesto 2027 comprobado. *Si no se cumple:* hasta que el presupuesto 2027
  los separe, el indicador se publica con y sin la inversión del plan.
  *Tipo:* reversible. *Desarrolla:* [Anexo F](06-roadmap-riesgo.md),
  [Anexo E](05-business-case.md).

### Roadmap y comercial

- **R-30 · Producto: captura de valor y construcción.** El mecanismo por defecto es
  la eficiencia de soporte de integración (consultas por integración y tiempo a la
  primera integración exitosa contra la base del descubrimiento), valorizada como
  capacidad liberada a costo cargado, no como caja. Ingreso por función solo se
  modela con señal comercial escrita y rango de precio en el mes 6, y es 0 hasta un
  contrato firmado; la retención no financia. Producto y Comercial acuerdan
  elegibilidad, criterio de éxito y umbral antes del mes 6; los puntajes de
  priorización los valida el AI Council con Producto. Si se libera el producto, un
  único contrato de red team cubre piloto, reprueba y las superficies que pida el
  cliente; ninguno entra en el mínimo. La base operativa del producto la dimensiona
  el Responsable de Tecnología y la verifica el CFO antes de liberar M7-M9.
  *Autoridad:* Producto propone el mecanismo y el CFO verifica su valorización; el
  Responsable de seguridad define con Tecnología el alcance del red team y el CFO
  verifica su cotización; el Directorio libera la construcción. *Hito:* gate del
  mes 6. *Si no se cumple:* sin mecanismo, problema medido o señal escrita, no hay
  construcción en el año y la hipótesis se relee en el mes 12; sin cotización
  verificada, el piloto no sale a clientes. *Tipo:* reversible en el mes 9.
  *Desarrolla:* [Anexo F](06-roadmap-riesgo.md), [Anexo E](05-business-case.md),
  [Anexo B](02-arquitectura.md), [Anexo C](03-gobierno-seguridad.md).
- **R-31 · Exploración comercial.** Es una opción no costeada: ingresos nuevos 0 en
  todos los escenarios. La única actividad comercial financiada es el descubrimiento
  de integración de M4-M6 (36-64 h, ya costeado), que lidera Producto; Comercial
  gestiona la señal y el registro de oportunidades sin costo propio.
  *Autoridad:* Directorio, si se propone ampliarla con alcance costeado. *Hito:*
  gate del mes 6. *Si no se cumple:* sin señal escrita en el mes 6, la oportunidad
  se archiva; ningún ingreso entra al modelo antes de un contrato firmado.
  *Tipo:* reversible. *Desarrolla:* [Anexo E](05-business-case.md),
  [Anexo F](06-roadmap-riesgo.md).
- **R-32 · Puertas de un solo sentido.** Ninguna decisión irreversible se toma
  antes del cierre del mes 12, y las que se toman ahí rigen para el plan siguiente:
  firmar un compromiso contractual de IA con un cliente; enviar código o datos de un
  cliente a un modelo externo fuera del entorno del propio cliente (R-08); subir una
  función del producto a "actúa con aprobación" (nivel 3); el uso interno con code
  review ya opera en ese nivel y no entra en esta puerta; hardware propio o consumo
  comprometido a más de 12 meses. Ajustar un modelo con código o datos de un cliente
  queda fuera del horizonte. El año 2 se decide y se costea aparte
  en el mes 12.
  *Autoridad:* Directorio, con dictamen del AI Council. *Hito:* cierre del mes 12.
  *Si no se cumple:* sin resolución del Directorio, ninguna se ejecuta y el año 2 no
  se financia por defecto. *Tipo:* **irreversible**.
  *Desarrolla:* [Anexo F](06-roadmap-riesgo.md), [Anexo B](02-arquitectura.md),
  [Anexo C](03-gobierno-seguridad.md).
- **R-33 · Destino de la capacidad: caso base intacto.** Se conservan en 0 las
  horas evitadas, el beneficio de caja y el ingreso nuevo presupuestados; no
  cambia ninguna cifra. Más funcionalidades por período con el mismo equipo y
  precio queda como sensibilidad de destino a revisar en el mes 6, sin
  monetizarla ni sumarla a las horas evitadas; por sí sola no acredita el destino
  de R-19, que conserva su alcance junto con los gates. Tres indicadores
  (funcionalidades desplegadas por período, mediana de días de pedido priorizado a
  producción, incidentes productivos y resolución de los críticos) se adoptan como
  seguimiento complementario, sin atribución causal a la IA ni caja; si no se
  extraen dentro de horas costeadas, quedan opcionales o se recostean, sin
  bloquear el gate. Que un cliente reduzca la dotación al renovar es una hipótesis
  de riesgo comercial, sin probabilidad estimada.
  *Autoridad:* CFO convierte la capacidad (R-19); el AI Council lee la
  sensibilidad. *Hito:* gate del mes 6. *Si no se cumple:* sin datos o encaje
  contractual, la sensibilidad se retira y el caso base no cambia; sin destino
  decidido, el beneficio sigue en 0. *Tipo:* reversible.
  *Registro:* decisión del responsable del caso del 2026-10-22
  ([#60](https://github.com/lazynet/tp-caio-g11-2026/issues/60)).
  *Desarrolla:* [Anexo E](05-business-case.md#destino-operativo-de-la-capacidad-sensibilidad-adoptada),
  [Anexo F](06-roadmap-riesgo.md#entrega-al-cliente-sensibilidad-de-destino-adoptada).

## Evidencia

### Quién produce, verifica y firma cada decisión

Modelo de autoridad único (R-04 y R-06). El firmante nunca produce el paquete que
firma, y el CFO verifica sin liberar fondos: solo fija el tope de costo por PR y de
consumo como parámetro de control.

| Decisión | Produce | Verifica | Dictamina | Firma |
|---|---|---|---|---|
| Aprobación del plan, techos, resoluciones y primera liberación | CAIO | CFO | — | Directorio |
| Entregables de la preparación (diagnóstico, padrón, restricciones, conciliación) | CAIO | Verificador senior independiente | — | CEO, en la segunda liberación |
| Segunda liberación (hasta 71) | CAIO | CFO (cifras, caja, reservas, presupuesto 2027); Responsable de seguridad (política y controles) | AI Council | CEO, por delegación |
| Gates de los meses 3, 6, 9 y 12, dentro del techo de cada tramo | CAIO; el Responsable de Tecnología produce los indicadores | CFO (techos y reservas); verificador senior independiente (indicadores); Responsable de seguridad (controles, incidentes) | AI Council; el acta registra quién produjo y verificó | CEO, por delegación |
| Superar el techo de un tramo, ampliar alcance, compromisos a más de 12 meses, decisiones irreversibles, cambios de política | CAIO, con el dueño del dominio | CFO | AI Council | Directorio |
| Método de medición y acta de viabilidad | QA/análisis de datos y DevOps, bajo el Responsable de Tecnología | Verificador senior independiente (acta e indicadores de cada lectura); el Responsable de seguridad clasifica severidad | — | AI Council ratifica, con abstención (R-06) |
| Compensatorios y prueba previa por superficie | Ingeniería (senior DevOps) | Responsable de seguridad, que verifica y no produce | Dueño del riesgo o AI Council aceptan el residual (R-10), con abstención (R-06) | CEO, en el gate |
| Evidencia contractual agregada (señal) | Comercial y Operaciones leen; Responsable de seguridad consolida | Responsable de Tecnología, con Legal externo para lo ambiguo | AI Council declara la señal | CEO firma el gate; la plataforma la libera el Directorio |
| Tratamiento y retención de eventos de uso por persona | Ingeniería | Personas y Legal externo, consultados | — | Responsable de seguridad |
| Suspensión preventiva de un uso | Quien detecta el disparador (Ingeniería o dueño del caso) | Sin verificación previa: es contención; la revisa el AI Council en su revisión mensual | — | Responsable de seguridad; suplente para contener, Responsable de Tecnología |
| Reanudación de un uso suspendido | Ingeniería | Responsable de seguridad, o el verificador senior independiente si Seguridad produjo parte de la evidencia | Autoridad del residual (R-10), con abstención | CEO registra en el gate |
| Tope de costo de IA por PR o por consumo (parámetro de control) | Tecnología | — | AI Council | CFO |
| Gasto de IA fuera del presupuesto | Tecnología | CFO | AI Council | CEO dentro del techo del tramo; Directorio por encima |

### Recálculo de las horas de gobierno (R-25)

| Componente | Antes | Ahora | Cuenta |
|---|---|---|---|
| Tech lead de gobierno (Anexo C) | 22-36 h | 22-32 h | 8-16 + 2-4 + 12 = 22-32 |
| Demanda interna M1-M3 | 970-1.350 h | 970-1.346 h | 1.350 − 4 = 1.346; el extremo bajo no cambia |
| FTE máximo | 2,8125 | 2,8042 | 1.346 / 480 |
| Soporte clave | 430-690 h | 430-686 h | 690 − 4 = 686 |
| Margen sobre la reserva clave | 30 h | 34 h | 720 − 686 = 34 |
| Máximo de tiempo M1-M3 | 58,28 | 58,03 | 58,28125 − 4 × 62,5 / 1.000 = 58,03125 |
| Techo de tiempo M1-M3 | 59 | 59 | 58,03 < 59 |
| Con la verificación de la lectura del mes 3 (4-5 h) | — | 974-1.351 h; soporte 434-691 h; margen 29 h; tiempo máximo 58,27 | 970 + 4 = 974; 1.346 + 5 = 1.351; 720 − 691 = 29; 58,03125 + 5 × 46,875 / 1.000 = 58,265625 < 59 |

### Dónde dos miradas chocaban y qué se eligió

| Tema | Alternativa adoptada | Alternativa descartada y por qué |
|---|---|---|
| Quién libera fondos en los gates | El CEO firma por delegación; el CFO verifica (R-04) | El CFO libera: junta la verificación de las cifras con la firma del gasto. El Directorio firma todo: suma cuatro sesiones sin más control |
| Quién ratifica el método de medición | AI Council (R-14) | Responsable de Tecnología: es quien supervisa a los productores. CFO: verificaría cifras y ratificaría la regla contra la que se mide |
| Valor inherente de datos de cliente en un modelo externo | Media / Alto, sin fila propia para superficies sin control central (R-10) | Media / Muy alto con fila nueva Alta / Alto: obligaría a suspender el uso existente antes de probar compensatorios y a justificar por qué el control baja el impacto |
| Uso existente sobre código de clientes | El código bajo NDA se suspende desde la aprobación; el código sin NDA sigue como residual del AI Council hasta el gate del mes 3, con la matriz leída; sin excepción comercial (R-08, R-09) | Dejar seguir todo el uso hasta el mes 3: contradice la política que R-07 ratifica, que clasifica el código bajo NDA como Restringido. Vencerlo en la segunda liberación: antes de que la matriz pueda estar completa |
| Verificación del acta de viabilidad | Verificador senior independiente, ya costeado para el acta; también verifica los indicadores de cada gate (R-14) | Que la verifique el Responsable de Tecnología: supervisa a quien produce |
| Hasta dónde firma el CEO | Techos fijados hoy y no liberados: 79 hasta M3 y 16 / 13 / 13 por tramo, 121 en el año; el CEO firma dentro del techo de cada tramo (R-03, R-04) | Tope de 79 y cada tramo de M4-M12 al Directorio: suma tres sesiones sin más control. Delegar hasta 121 sin tramos: un cheque en blanco sobre el año |
| Gate del mes 6 | No lee valor: sigue por adopción, costo y controles, y corta por daño o caída demostrada; el valor se lee en el mes 9 si el peor caso es mayor que 0 (R-19, R-27) | Límite inferior ≥ +3% en el mes 6 y ≥ +8% en el mes 9: con 15-20 personas el semiancho es del orden de ±16 puntos con valores ilustrativos y el gate casi no podía pasar ([Anexo B](02-arquitectura.md)) |
| Facilitación externa del básico | La resuelve el Directorio, porque su caja queda fuera de 79 (R-22) | Que la firme el CEO: excede un techo, y eso vuelve al Directorio |
| Ruta de incidentes | Sobre el circuito existente, 0 USD adicionales en M1-M3 (R-12) | No adoptarla por no costeada: el costo ya está dentro de "Política e intake" |
| Política de IA | El Directorio la ratifica hoy y la preparación deja constancia de versión y alcance (R-07) | Solo tomar conocimiento: deja la política sin respaldo documental hasta el mes 3 |
| Lectura del mes 3 con la base de 8 semanas | Reducida y declarada (R-18) | Correrla hasta 4 semanas: atrasa M4 sin mover fondos en el mes 3 |
| Exploración comercial | Opción no costeada; Producto lidera el descubrimiento (R-31) | Financiarla desde el mes 3: compra ingreso que el modelo no cuenta |
| Destino de la capacidad | Caso base intacto; más funcionalidades por período como sensibilidad del mes 6, sin monetizar (R-33) | Monetizar la mayor entrega en el caso base: no hay evidencia de ingreso o costo evitado ni encaje contractual |
| Uso decisorio de BCRA y del AI Act | Supuestos sin uso decisorio; la revisión jurídica es el dictamen focalizado de M1-M3 (R-34) | Condicionar la entrega o una liberación a su verificación previa: traslada a la entrega un dictamen que corresponde a la ejecución |

## Riesgos y mitigación

Probabilidad e impacto son juicio del CAIO.

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El Directorio lee "adopta R-01 a R-34" como un cheque en blanco | Media | Alto | Cada resolución lleva autoridad, hito, consecuencia y tipo; los techos son fijos y lo que los supera vuelve al Directorio | Una resolución se ejecuta sin su condición: el CEO suspende el tramo y lo informa al Directorio |
| La delegación en el CEO concentra la firma | Baja | Alto | El CFO verifica, el AI Council dictamina, los techos son fijos y la delegación se revoca en cualquier sesión | Un gate firmado por encima de un techo: el Directorio revoca la delegación |
| Un gate se firma sin verificador independiente | Media | Alto | R-06: sin verificador, la superficie se excluye; el firmante no produce ni verifica | El entregable no se declara probado |
| Un hecho externo (contrato, habilitación, medición) no llega a su hito | Alta | Medio | Cada resolución que depende de un tercero fija qué rige si en el hito no está: *default-deny*, espera o diferimiento | El frente afectado no se libera |
| Los Anexos A a F quedan desalineados con este registro | Media | Medio | Cada anexo cita la R que aplica; ante una discrepancia rige este anexo en autoridad y condiciones, y el anexo dueño en cifras | La entrega no sale con una cifra o autoridad que contradiga una R |
| La postura sobre el empleo se comunica y después no se sostiene | Baja | Alto | Texto con asesoría laboral y excepciones explícitas; marcada como costosa de deshacer | Cambiarla exige resolución del Directorio y comunicación del CEO |
