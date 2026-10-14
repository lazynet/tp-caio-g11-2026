# Storyline de la defensa

Borrador del CAIO a validar por el equipo, sobre un caso propuesto y pendiente
del acuerdo del equipo. Responsable humano de la storyline: **pendiente**. Cada
cifra remonta a un anexo de `plan/annexes/`; ninguna tiene verificación humana.
**No hubo ensayo todavía**: cuando lo haya, se registra con fecha, tiempos, roles
y feedback.

## Tesis en una oración

Acme Labs tiene que poner IA en lo que les vende a bancos y fintechs antes de
que se lo exijan, y la forma de hacerlo sin apostar la empresa es una base común
gobernada y financiada por gates trimestrales, donde cortar a tiempo cuesta poco.

## Acto 1: por qué ahora (slides 1-2)

- La empresa es rentable y crece, pero concentrada: el cliente principal pesa
  40%-50% de la facturación ([Anexo A](../plan/annexes/01-diagnostico.md)).
- La IA ya está adentro: Tecnología la usa mucho y el piloto dio NPS +42. Pero no
  hay nada de IA en el producto que se vende, y la política sigue en borrador.
- Los clientes son bancos y PSP que el BCRA obliga a gobernar la IA de sus
  terceros. Acme Labs es ese tercero: o llega con controles demostrables, o
  queda afuera.
- Y el costo ya se mueve: el consumo real del agente de código es ~12 veces lo que
  se paga por suscripción.

**Cierre del acto:** el riesgo no es invertir en IA; es seguir sin gobierno ni
producto mientras el costo y la exigencia de los clientes suben.

## Acto 2: qué proponemos (slides 3-6)

- Dos frentes sobre una base: el producto que se vende y la operación interna.
- Una arquitectura neutral al modelo y aislada por cliente, sin datos de clientes
  en 12 meses ([Anexo B](../plan/annexes/02-arquitectura.md)).
- Un gobierno liviano que habilita: Council de 5, intake en niveles, política
  ratificada ([Anexo C](../plan/annexes/03-gobierno-seguridad.md)).
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
  no genera caja ([Anexo E](../plan/annexes/05-business-case.md)). Y cumplir la
  meta de +20% de throughput del OKR tampoco cubre el régimen: el equilibrio
  pide ~23%. Lo que compra es cobertura de precio, licencia para venderles a
  bancos y una opción de ingreso.
- Por eso no pedimos el año: pedimos un único G0. T1 con hasta 32 mil USD de
  caja y 1,6 FTE clave, que sí entra en el sobre de tiempo. Cortar en G1 cuesta
  73 mil económicos en el medio y hasta 106 en el máximo.
- Lo que no cierra lo mostramos y lo decidimos hoy, no en marzo: T2-T4 no entra
  en el sobre. O se amplía, o se difiere el producto hasta que un cliente dé
  señal ([Anexo F](../plan/annexes/06-roadmap-riesgo.md)).
- Cada gate dice qué pasa si falla cada condición, y los dos frentes se cortan
  por separado. Lo irreversible se decide en G4 y rige después.

**Cierre:** "Aprueben tres meses con techo. En marzo les traemos la línea de
base congelada, la política ratificada y la matriz de clientes, y deciden si
seguimos."

## Qué no decir

- Que la plataforma o el producto propio A están certificados.
- Porcentajes de ahorro de inferencia o de ROI del curso sin fuente
  ([huecos](../material/huecos.md)).
- Cualquier cifra que no esté en un anexo.
- Que la defensa está ensayada, mientras no haya un ensayo registrado.
- Qué producto o qué cliente podría estar detrás de un alias o un rango.
