# Storyline de la defensa

Borrador del CAIO a validar por el equipo, sobre el caso Acme Labs y el alcance
de toda la organización (producto y operación interna), acordados en comisión
([acuerdo de alcance informado por Martín](https://github.com/lazynet/tp-caio-g11-2026/issues/15)).
Coordina la defensa (storyline, objeciones y quién presenta cada slide) Lucho,
según el reparto del `README.md`. Quién presenta cada slide y quién responde
cada objeción **todavía no se acordó** (#21). Cada cifra remonta a un anexo de
`plan/annexes/`. Las 84 fichas de fuente que exigía el chequeo de entrega al
20/10/2026 están `verified`, con declaración humana de Martín de esa fecha.
Después se sumó un supuesto de metas culturales, en borrador y sin verificación
humana, que citan los Anexos D y F; cuántas fichas exige hoy la entrega se dice
cuando el chequeo vuelva a ser válido. La declaración del 20/10 acredita el
cotejo de cada ficha con la fuente declarada, no la validación de los supuestos
con datos internos de Acme Labs, ni el acuerdo del equipo, ni una aprobación
empresarial. La anonimización todavía necesita la revisión de un humano
autorizado. **No hubo ensayo todavía**: cuando lo haya, se registra con fecha,
tiempos, roles y feedback. El arco sigue la revisión del 2026-10-15
(`reviews/2026-10-15-comentarios-equipo.md`): problema → beneficio →
alternativas → costo → resolución. Montos en k USD (miles de dólares).

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
| Visión estratégica | Tesis y acto 1: medir el valor antes de ampliar | Síntesis ejecutiva: la tesis y el cierre del deck, dichos en menos de un minuto (propuesta del equipo, no del curso) |
| Justificación de inversiones | Actos 2 y 3: beneficio medido, exposición presupuestaria por punto de salida, narrativa financiera | Cada cifra con su anexo; ninguna fuera del deck o de un anexo |
| Gestión de objeciones | [Banco de objeciones](objeciones.md), con respuesta y evidencia por objeción | Mapeo de objeciones probables por tema, con quien responde cada una a designar |
| Comunicación ejecutiva | Una decisión por slide y el cierre con el pedido | Ensayo con tiempos y preguntas bajo presión (propuesta del equipo): todavía no se hizo |

**Bajo presión:** responder con la cifra y el anexo; si no se sabe, decir qué se
mide y en qué gate; no estimar en vivo ni cambiar el pedido en la sala.

## Tesis en una oración

Acme Labs ya usa IA sin saber cuánto vale: proponemos medir el valor antes de
ampliar la inversión, con un paquete mínimo sobre las herramientas que ya paga,
controles probados antes de usar y fondos que se liberan solo por decisión en
cada gate.

## Acto 1: el problema (portada y Problema)

- La empresa es rentable y crece, pero concentrada: el cliente principal pesa
  40%-50% de la facturación ([Anexo A](../plan/annexes/01-diagnostico.md)).
- La IA ya está adentro: Tecnología usa mucho el agente de código; Operaciones,
  poco, en buena parte porque el cliente fija las herramientas. Hay herramientas
  de harness para el SDLC de uso exclusivamente interno; no se cuentan como IA
  productiva de la oferta. La política de IA está aprobada según
  el responsable del caso; su versión, acta y alcance se revisan antes de
  liberar M1-M3, y el gate del mes 3 comprueba su aplicación y su alcance para
  el producto; los controles siguen por verificar.
- No hay medición del impacto del harness contra una base, según el responsable
  del caso ([uso interno](../context/hechos/uso-ia-interno.md)). El propio
  diagnóstico es una hipótesis: las fuentes mezclan poblaciones y fechas, así que
  financiamos primero una validación acotada para conciliar corte, nómina,
  contratistas, personas y horas por rol antes de liberar M1-M3.

**Cierre del acto:** el riesgo no es invertir poco; es ampliar sin saber qué compra.

## Acto 2: qué beneficio buscamos y qué alternativas hay (Beneficio y Alternativas)

- El beneficio principal es capacidad con calidad: PR aceptados contra una base
  congelada, con retrabajo e incidentes primero. **Beneficio de caja estimado: 0;
  ingreso nuevo: 0** en el modelo ([Anexo E](../plan/annexes/05-business-case.md)).
- El paso no está asegurado: con el caso base y un semiancho de 3 puntos, el
  límite inferior queda debajo de los umbrales. Pasa solo con calidad sin
  deterioro demostrado; una calidad incierta espera y un daño corta. Y con la
  cohorte y los datos reales la medición puede no distinguir la mejora: la
  validación lo estima y, si no alcanza, el método se reformula antes de la
  segunda liberación o el caso se presenta como espera y corte. Por eso medimos
  primero ([Anexo F](../plan/annexes/06-roadmap-riesgo.md); [Anexo B](../plan/annexes/02-arquitectura.md), "Viabilidad").
- El asistente de integración es una hipótesis de producto: antes del mes 6
  medimos el tiempo a la primera integración exitosa con la documentación y el
  soporte actuales. Sin problema, base y señal comercial escrita, no se construye.
- Las alternativas publicadas (47, 161, ≈199, 394, ≈400, 471) son costos de
  alcances distintos, pendientes de homogeneizar. No las comparamos como si
  fueran equivalentes. El pedido anterior (33 + 6 de caja, 72 + 7 de tiempo)
  queda como alternativa.

**Cierre del acto:** elegimos lo mínimo que compra la medición, no la opción más
barata por el ROI de un paquete que no medimos.

## Acto 3: cuánto cuesta y cómo se controla (de Arquitectura a Costo y riesgo)

- **Arquitectura proporcional:** configurar lo que ya pagamos antes de comprar o
  ensamblar. La plataforma se relee en los meses 3, 6 y 9: la regla vigente pide
  una señal; la propuesta, pendiente de ratificación, suma cuatro condiciones.
  Nada pasa al año 2 por defecto ([Anexo B](../plan/annexes/02-arquitectura.md)).
- **Seguridad antes de usar:** sin plataforma no alcanza la política; cada
  superficie prueba sus compensatorios, con críticos cerrados y residual
  aceptado. Seguridad puede suspender el uso aunque el gasto o la adopción
  cumplan, y quien produce la evidencia no es quien la verifica ni quien firma
  ([Anexo C](../plan/annexes/03-gobierno-seguridad.md)).
- **Personas:** formar, reasignar y decidir una excepción externa solo si falta
  un facilitador. Se propone reservar 720 h clave (1,5 FTE) más 540-660 h de
  formación: máximo 1.380 h, con demanda estimada de 970-1.350 h si se
  confirman uniones de horas de B, C y D que sus dueños no ratificaron. La
  reserva es propuesta, no disponibilidad: Operaciones confirma agendas y
  trabajo desplazado por persona y semana, o se recostea antes del mes 1. Si se
  cuenta todo junto o la formación aparte (el sobre de capacidad) lo proponemos
  decidir al liberar los 71k USD ([Anexo D](../plan/annexes/04-personas-cultura.md),
  [Anexo F](../plan/annexes/06-roadmap-riesgo.md#decisiones-pendientes-para-el-board-o-el-equipo)).
- **Roadmap:** diagnóstico, base, política, controles, formación y prueba en los
  meses 1-3, después de diez días hábiles de validación autorizada en 2026;
  en los 4-12, controles, medición y, en los 4-6, el estudio del asistente sin
  construirlo; evaluación y traspaso en los 10-12. Producto, plataforma,
  referentes y cursos nuevos no entran en esos techos: necesitan otra decisión y
  costeo, sin fecha prometida, y no pasan al año 2 por defecto. El Council revisa
  cada mes y puede cortar; a las dos liberaciones iniciales les siguen los gates
  de los meses 3, 6, 9 y 12.
- **Primera liberación:** 80-136 h y hasta 8k USD de tiempo, sin caja
  incremental; agendas e imputación 2026 confirmadas antes de empezar. La
  autoriza el Directorio o una autoridad formalmente delegada. Incluye
  diagnóstico, matriz privada, viabilidad, verificación y cierre documental. Sin
  despliegues ni dictamen externo; el alcance y la cotización legal preparan la
  decisión. Si no sostiene el alcance, se reduce o se detiene con lo trabajado,
  hasta 8k USD.
- **Exposición presupuestaria máxima autorizada del tramo:** el resto de M1-M3 y
  las reservas requiere una segunda autorización de hasta 71k USD; el acumulado
  propuesto es 79k USD (10 de caja y 69 de tiempo), no 79 nuevos. Si se corta
  antes de M1, el límite es 8; si se sale en M3, es 79 hasta cerrar y 85 en el
  año con núcleo aprobado al salir. Son techos de recursos, sin restar beneficio:
  no es pérdida económica incremental ni salida de caja, y no incluyen la
  contribución del trabajo facturable que puedan desplazar, que sigue sin medir. Esperar seis semanas en M6 y
  cortar tiene techo 102; cortar sin esperar, 95.
- **Si sale bien:** pasan los gates y el mínimo sigue todo el año sin
  plataforma, con costo proyectado ≈70k USD (27-113) y techos de 118k USD sin
  gastar reservas, 121k USD con cierre. Lo que
  queda en la mano es base, lecturas de throughput y calidad con su intervalo,
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
  consumo facturado ni pronóstico, y es de la empresa con o sin plan; *decisión*, la primera
  autorización y los criterios de la segunda. La plata es interna, por etapas y
  sin deuda.
- **Personas, sin eludir el empleo:** formar y reasignar antes que desvincular.
  El estudio de un rol crítico no decide desvinculaciones y no está en el
  mínimo: es alcance ampliado, con postura comunicada, horas y autorización
  propias. Además, chequeo de
  equidad por grupo y sin compensación monetaria nueva en 12 meses
  ([Anexo D](../plan/annexes/04-personas-cultura.md)).

## Cierre: resolución (Autorizar la validación inicial)

**Valor medible; seguridad aceptable; fondos por decisión.** "Les pedimos
autorizar primero diez días hábiles de validación con agenda propia: hasta 8k USD
de tiempo y caja incremental 0. Con diagnóstico, capacidad y viabilidad
revisados, decidan continuar, reducir/resecuenciar o detener. Continuar requiere
otra decisión de hasta 71k USD adicionales para M1-M3 y reservas, con
presupuesto 2027 comprobado: acumulado propuesto 79k USD. La aprobación
económica no habilita prácticas sin controles. En marzo traemos base, política,
matriz, pruebas y aprendizajes para decidir el siguiente tramo. El año sigue
condicionado. Y adopten los gates de los meses 3, 6, 9 y 12 como regla para
liberar fondos."

## Qué no decir

- Que el plan se paga en el año o que genera caja: el modelo presupuesta
  beneficio de caja 0 e ingreso nuevo 0.
- "Caja cero": se confunde con desembolso cero. Decir "beneficio de caja
  estimado: 0".
- Que los 79 se autorizan de una vez, que la preparación está ejecutada o que
  elegir el supuesto libera agendas: son dos decisiones y falta autorización
  empresarial. Para la primera, decir "caja incremental 0", junto con sus horas.
- Que 47/161/394 son alternativas equivalentes: son alcances distintos.
- Que las cuatro condiciones de plataforma ya rigen: son una propuesta pendiente.
- Que la plataforma pasa al año 2: se relee en los meses 3, 6 y 9.
- Que el 72,5% es un techo de adopción: es el resultado de cumplir exactamente
  las metas por área.
- Que el escenario base pasa las lecturas de los meses 6 y 9.
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
- Que el estudio del rol crítico decide recortes o que la postura sobre el
  empleo ya está aprobada: es propuesta, la decide el Directorio con asesoría laboral.
