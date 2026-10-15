# Storyline de la defensa

Borrador del CAIO a validar por el equipo, sobre un caso propuesto y pendiente
del acuerdo del equipo. Responsable humano de la storyline: **pendiente**. Cada
cifra remonta a un anexo de `plan/annexes/`; ninguna tiene verificación humana.
**No hubo ensayo todavía**: cuando lo haya, se registra con fecha, tiempos, roles
y feedback. El arco sigue la revisión del 2026-10-15
(`reviews/2026-10-15-comentarios-equipo.md`): problema → beneficio →
alternativas → costo → resolución.

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
  antes de comprometer horas conciliamos corte, nómina, contratistas, personas y
  horas por rol.

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
  un facilitador. El mínimo pide 2,0-2,8 FTE internos en total (0,9-1,4 clave),
  que salen de horas facturables y se concilian por persona
  ([Anexo D](../plan/annexes/04-personas-cultura.md)).
- **Roadmap:** diagnóstico, base, política, controles, formación y prueba en los
  meses 1-3; solución según evidencia en los 4-6; aplicación y producto
  condicional en los 7-9; evaluación y traspaso en los 10-12. El Council revisa
  cada mes y puede cortar; los fondos se liberan en los meses 3, 6, 9 y 12.
- **Pérdida máxima:** salir en el mes 3 cuesta hasta 73 hasta cerrar (10 de caja
  y 63 de tiempo) y 79 en el año con el núcleo de gobierno. Es el precio de
  aprender, sin restar beneficio.

## Cierre: resolución (slide 10)

**Valor medible; seguridad aceptable; fondos por decisión.** "Autoricen solo el
paquete mínimo de los meses 1-3: hasta 9 de caja más 1 de reserva, y 58 de
tiempo más 3 de preparación y 2 de cierre, y adopten los gates. En marzo les
traemos la base congelada, la política, la matriz, los controles probados y lo
que aprendió la prueba, y deciden si sigue, se amplía o se corta."

## Qué no decir

- Que el plan se paga en el año o que genera caja: el modelo presupuesta
  beneficio de caja 0 e ingreso nuevo 0.
- "Caja cero": se confunde con desembolso cero. Decir "beneficio de caja
  estimado: 0".
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
