# Storyline de la defensa

Borrador del CAIO a validar por el equipo, sobre un caso propuesto y pendiente
del acuerdo del equipo. Responsable humano de la storyline: **pendiente**. Cada
cifra remonta a un anexo de `plan/annexes/`; ninguna tiene verificación humana.
**No hubo ensayo todavía**: cuando lo haya, se registra con fecha, tiempos, roles
y feedback. El arco sigue la revisión del 2026-10-15
(`reviews/2026-10-15-comentarios-equipo.md`): problema → beneficio →
alternativas → costo → resolución.

## Qué tiene que demostrar la defensa

El [capstone ante un panel ejecutivo](../material/conceptos/m3u4-capstone-panel-ejecutivo.md)
evalúa cuatro competencias. Este es dónde las sostiene el plan, sin cambiar el
orden de los actos:

| Competencia | Dónde se demuestra | Cómo se prepara |
|---|---|---|
| Visión estratégica | Tesis y acto 1: medir el valor antes de ampliar | Síntesis ejecutiva: la tesis y la slide 10, dichas en menos de un minuto |
| Justificación de inversiones | Actos 2 y 3: beneficio medido, pérdida máxima por salida, narrativa financiera | Cada cifra con su anexo; ninguna fuera del deck o de un anexo |
| Gestión de objeciones | [Banco de objeciones](objeciones.md), con respuesta y evidencia por objeción | Mapeo de objeciones probables por tema, con quien responde cada una a designar |
| Comunicación ejecutiva | Una decisión por slide y el cierre con el pedido | Ensayo con tiempos y preguntas bajo presión: todavía no se hizo |

**Bajo presión:** responder con la cifra y el anexo; si no se sabe, decir qué se
mide y en qué gate; no estimar en vivo ni cambiar el pedido en la sala.

## Tesis en una oración

Acme Labs ya usa IA sin saber cuánto vale: proponemos medir el valor antes de
ampliar la inversión, con un paquete mínimo sobre las herramientas que ya paga,
controles probados antes de usar y fondos que se liberan solo por decisión en
cada gate.

## Acto 1: el problema (slides 1-2)

- La empresa es rentable y crece, pero concentrada: el cliente principal pesa
  40%-50% de la facturación ([Anexo A](../plan/annexes/01-diagnostico.md)).
- La IA ya está adentro: Tecnología usa mucho el agente de código; Operaciones,
  poco, en buena parte porque el cliente fija las herramientas. No hay IA
  productiva documentada en la oferta, y la política estaba en borrador en el
  último registro, de abril.
- Lo que falta es valor incremental medido contra una base. Y el propio
  diagnóstico es una hipótesis: las fuentes mezclan poblaciones y fechas, así que
  financiamos primero una validación acotada para conciliar corte, nómina,
  contratistas, personas y horas por rol antes de liberar M1-M3.

**Cierre del acto:** el riesgo no es invertir poco; es ampliar sin saber qué compra.

## Acto 2: qué beneficio buscamos y qué alternativas hay (slides 3-4)

- El beneficio principal es capacidad con calidad: PR aceptados contra una base
  congelada, con retrabajo e incidentes primero. **Beneficio de caja estimado: 0;
  ingreso nuevo: 0** en el modelo ([Anexo E](../plan/annexes/05-business-case.md)).
- El paso no está asegurado: con el caso base y un semiancho de 3 puntos, el
  límite inferior queda debajo de los umbrales. Por eso medimos primero
  ([Anexo F](../plan/annexes/06-roadmap-riesgo.md)).
- El asistente de integración es una hipótesis de producto: antes del mes 6
  medimos el tiempo a la primera integración exitosa con la documentación y el
  soporte actuales. Sin problema, base y señal comercial escrita, no se construye.
- Las alternativas publicadas (47, 161, ≈199, 394, ≈400, 471) son costos de
  alcances distintos, pendientes de homogeneizar. No las comparamos como si
  fueran equivalentes. El pedido anterior (33 + 6 de caja, 72 + 7 de tiempo)
  queda como alternativa.

**Cierre del acto:** elegimos lo mínimo que compra la medición, no la opción más
barata por el ROI de un paquete que no medimos.

## Acto 3: cuánto cuesta y cómo se controla (slides 5-9)

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
  formación: máximo 1.380 h, con demanda costeada de 970-1.350 h. Son supuestos;
  Operaciones confirma agendas y trabajo desplazado por persona y semana
  ([Anexo D](../plan/annexes/04-personas-cultura.md)).
- **Roadmap:** diagnóstico, base, política, controles, formación y prueba en los
  meses 1-3, después de diez días hábiles de validación autorizada en 2026;
  solución según evidencia en los 4-6; aplicación y producto
  condicional en los 7-9; evaluación y traspaso en los 10-12. El Council revisa
  cada mes y puede cortar; a las dos liberaciones iniciales les siguen los gates
  de los meses 3, 6, 9 y 12.
- **Primera liberación:** 80-136 h y hasta 8 de tiempo, sin caja incremental;
  agendas e imputación 2026 confirmadas antes de empezar. Incluye diagnóstico,
  matriz privada, viabilidad, verificación y cierre documental. Sin despliegues
  ni dictamen externo; el alcance y la cotización legal preparan la decisión.
- **Pérdida máxima:** el resto de M1-M3 y las reservas requiere una
  segunda autorización de hasta 71; el acumulado es 79 (10 de caja y 69 de
  tiempo), no 79 nuevos. Si se corta antes de M1, el límite es 8; si se sale en
  M3, es 79 hasta cerrar y 85 en el año con núcleo aprobado al salir. Es el
  precio de aprender, sin restar beneficio. Esperar seis semanas en M6 y cortar
  tiene techo 102; cortar sin esperar, 95.
- **Narrativa financiera, datos → narrativa → decisión** ([Anexo E](../plan/annexes/05-business-case.md#insumos-para-el-deck)):
  *datos*, beneficio de caja 0 y un mínimo que cuesta hasta 79; *narrativa*, sin
  retorno prometido se compra información, y si el board dice que no siguen
  abiertas tres exposiciones sin monto: clientes que prohíben modelos externos y
  uso sin regla, que el mínimo cubre, y consumo de modelos, que no cubre;
  *decisión*, la primera autorización y los criterios de la segunda. La plata es
  interna, por etapas y sin deuda.
- **Personas, sin eludir el empleo:** formar y reasignar antes que desvincular,
  con un estudio de un rol crítico que no decide desvinculaciones, chequeo de
  equidad por grupo y sin compensación monetaria nueva en 12 meses
  ([Anexo D](../plan/annexes/04-personas-cultura.md)).

## Cierre: resolución (slide 10)

**Valor medible; seguridad aceptable; fondos por decisión.** "Autoricen primero
diez días hábiles de validación con agenda propia: hasta 8 de tiempo y caja
incremental 0. Con diagnóstico, capacidad y viabilidad revisados, decidan continuar,
reducir/resecuenciar o detener. Continuar requiere autorizar hasta 71 adicionales
para M1-M3 y reservas, con presupuesto 2027 comprobado: acumulado 79. La aprobación
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
- Un monto para el costo de no actuar: son exposiciones sin probabilidad ni
  pérdida estimada.
- Un VPN: no hay tasa en el caso ni flujos positivos que descontar.
- Que el reskilling retiene un porcentaje del talento: la cifra del curso no
  tiene fuente.
- Que el estudio del rol crítico decide recortes o que la postura sobre el
  empleo ya está aprobada: es propuesta, la decide el Directorio con asesoría laboral.
