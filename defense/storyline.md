# Storyline de la defensa

Borrador del CAIO a validar por el equipo, sobre un caso propuesto y pendiente
del acuerdo del equipo. Responsable humano de la storyline: **pendiente**. Cada
cifra remonta a un anexo de `plan/annexes/`; ninguna tiene verificación humana.
**No hubo ensayo todavía**: cuando lo haya, se registra con fecha, tiempos, roles
y feedback.

## Tesis en una oración

Acme Labs tiene que gobernar y aprender la IA que ya usa antes de que sus
clientes se lo exijan, y pagar la plataforma para venderla solo cuando una señal
de contrato, de precio o de cliente la justifique: el riesgo se revisa cada mes,
la plata se libera cada tres, diferir es la regla y cortar a tiempo cuesta poco.

## Acto 1: por qué ahora (slides 1-2)

- La empresa es rentable y crece, pero concentrada: el cliente principal pesa
  40%-50% de la facturación ([Anexo A](../plan/annexes/01-diagnostico.md)).
- La IA ya está adentro: Tecnología la usa mucho, y en el piloto de abril (12
  personas que se anotaron solas) el NPS fue +42. Pero no hay nada de IA en el
  producto que se vende, y la política sigue en borrador.
- Los clientes son bancos y PSP que el BCRA obliga a gobernar la IA propia y de
  terceros. Acme Labs es ese tercero. Si eso se traduce en exigencias
  contractuales, lo dice la evidencia que se junta en los meses 1-3, no lo
  suponemos.
- Y el costo ya se mueve: el consumo real del agente de código es ~12 veces lo que
  se paga por suscripción.

**Cierre del acto:** el riesgo no es invertir en IA; es seguir sin gobierno ni
producto mientras el costo y la exigencia de los clientes suben.

## Acto 2: qué proponemos (slides 3-6)

- Dos frentes sobre una base: la operación interna y el producto que se vende.
  El producto tiene un caso elegido con RICE, un asistente de integración en la
  plataforma propia, sin datos de clientes, y **está diferido** hasta que un
  cliente dé señal en la lectura de impacto del mes 6
  ([Anexo F](../plan/annexes/06-roadmap-riesgo.md)).
- Gobierno, base y formación van siempre, con una prueba chica sobre el agente
  de código que Tecnología ya usa. La plataforma (arquitectura neutral al modelo,
  aislada por cliente, sin datos de clientes en 12 meses) se gana con una señal
  en la decisión de plataforma del mes 3; la cobertura de precio es una opción
  que la prueba de los meses 4-6 confirma o descarta
  ([Anexo B](../plan/annexes/02-arquitectura.md)).
- Un gobierno liviano que habilita: Council de 5, intake en niveles, política
  ratificada y una revisión mensual con poder de corte
  ([Anexo C](../plan/annexes/03-gobierno-seguridad.md)).
- Personas: capacitar y reasignar, medir uso real, un solo contractor a prueba
  ([Anexo D](../plan/annexes/04-personas-cultura.md)).
- **Dogfooding:** este plan se hizo con el modelo operativo que proponemos:
  roles asumidos por agentes, una revisión adversarial del board y chequeos
  automáticos de fuentes y fugas. No decimos que todas las herramientas invoquen
  los agentes de punta a punta: eso no está probado.

**Cierre del acto:** no es una lista de iniciativas; es un sistema con dueños,
controles y métricas.

## Acto 3: cómo se protege la plata (slides 7-10)

- Lo decimos primero: con productividad sola, el plan no se paga en 12 meses y
  no genera caja ([Anexo E](../plan/annexes/05-business-case.md)). El
  equilibrio operativo anual del año 2 pide ~17% de throughput atribuible
  contra la base del plan (~23% si el régimen carga el producto); no recupera la
  inversión del año 1 ni es ROI ni payback. El OKR, que se mide contra el cuarto
  trimestre de 2026, lo cubre solo si, descontadas la mejora previa (d, medida
  en el mes 3) y la del grupo que no adopta (c, desde el mes 6), queda al menos
  16,7%. Lo que compra es la opción de cobertura de precio, una opción de
  ingreso y, si la evidencia contractual de los meses 1-3 la confirma, licencia
  para venderles a bancos.
- Y lo decimos segundo: en el año 1, gobierno mínimo y formación (161) o un
  piloto sobre el agente actual (47) le ganan al paquete completo (394). Por eso
  la plataforma no se compra hoy: **la decisión del mes 3 la libera solo con una
  señal** contractual, de precio por consumo o de cliente. Sin señal, el año
  cuesta ≈ 199 en lugar de ≈ 400, y las lecturas de los meses 6 y 9 vuelven a
  leer. No es un corte: es diferir.
- Hacemos un único pedido hoy: los meses 1-3 con la prueba chica, hasta 33 mil
  USD de caja (del contractor, solo su tramo de los meses 1-3) más 6 de reserva
  de cierre, que se amplía a 15 en el mes 3 solo si se libera la plataforma, y
  hasta 72 de tiempo (~1,8 FTE clave y ~654 h distribuidas). Cortar en el mes 3
  cuesta 79 mil económicos en el medio, hasta 115 hasta cerrar y 155 en el año si
  se conserva la base mínima.
- Con señal, los meses 4-12 entran en el sobre sin holgura, con el producto
  diferido y el replan de arquitectura; la excepción de los meses 4-6 es el
  respaldo si falta el 0,2 del contractor, y sin contractor los meses 4-6 corren
  en modo control. El producto amplía el sobre solo si un cliente da una señal
  comercial con presupuesto.
- **El riesgo se mira cada mes; la plata se libera cada tres.** El Council revisa
  cada mes un tablero con caja, uso, incidentes y señales: puede frenar, cortar,
  activar una contingencia o escalar una señal, pero no libera fondos. Eso queda
  en los meses 3, 6, 9 y 12, y la revisión mensual no suma costo.
- Cada decisión dice qué pasa si falla cada condición, y los dos frentes se
  cortan por separado. La espera del mes 6 vence a las 6 semanas y corta el
  frente interno; la del mes 9 mantiene la base mínima, y el mes 3 no corta:
  decide la plataforma. En el pesimista, el plan corta en los meses 7-9 y pierde
  ≈ 262 mil, contra 382 sin frenar. Lo irreversible se decide en el cierre del
  mes 12 y rige después.

**Cierre:** "Aprueben los primeros tres meses, con techo. Cada mes les mostramos
el tablero de riesgo. En marzo les traemos la línea de base congelada, la
política ratificada, la matriz, la evidencia de clientes y lo que aprendió la
prueba chica, y deciden si la plataforma se ganó su lugar."

## Qué no decir

- Que la plataforma o el producto propio A están certificados.
- Que el gateway ya cubre el precio, o que los bancos ya exigen IA: son
  hipótesis: la primera se prueba en los meses 4-6 y la segunda, en los
  meses 1-3.
- Que el OKR de +20% cubre el equilibrio: se miden contra bases distintas.
- Que el escenario base pasa las lecturas de los meses 6 y 9: con la regla del
  límite inferior, es condicional a la precisión del intervalo, y si la calidad
  queda incierta cuenta como espera.
- Que la revisión mensual libera fondos o decide por el throughput: lo muestra
  como tendencia; la lectura sigue a las 6 semanas y en los gates.
- Que la plataforma se paga con productividad: en el año 1 las opciones baratas
  ganan; la plataforma se paga solo con una señal.
- Que los secretos están bloqueados en toda superficie: en chat, IDE y suite
  hay prohibición y control compensatorio, no bloqueo.
- Que la señal del mes 6 prueba disposición a pagar: prueba interés con
  presupuesto y un rango de precio aceptado como referencia.
- Porcentajes de ahorro de inferencia o de ROI del curso sin fuente
  ([huecos](../material/huecos.md)).
- Cualquier cifra que no esté en un anexo.
- Que la defensa está ensayada, mientras no haya un ensayo registrado.
- Qué producto o qué cliente podría estar detrás de un alias o un rango.
