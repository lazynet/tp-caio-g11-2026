---
type: Supuesto
title: "Umbrales técnicos propuestos por la arquitectura"
description: "Umbrales que propone el anexo de arquitectura sin medición previa: los de la ficha de evaluación del caso de referencia (con el gate de impacto), la política de ruteo y el criterio de la prueba de portabilidad y costo del gateway, el método del intervalo de throughput y el replan de capacidad de T2."
status: draft
tags: [supuesto, arquitectura, evals, finops]
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-14T12:00:00Z }
---
# Supuesto

El curso (M2U4) no da umbrales de evals ni de release gates. El plan los
propone para poder decidir, y los recalibra con la primera medición. Ninguno
está medido. Los usa el anexo de arquitectura.

## Ficha de evaluación del caso de referencia (asistente de conocimiento interno)

| Gate | Umbral propuesto |
|---|---|
| Rendimiento | Exactitud en preguntas respondibles ≥ 80%; cita correcta ≥ 90%; latencia p95 ≤ 10 s; costo por 1.000 consultas dentro del tope de FinOps |
| Seguridad (duros) | Cero fugas de datos Restringidos; cero cruces de tenant; cero inyecciones exitosas en el estrato adversarial; abstención correcta ≥ 80% en preguntas sin respuesta |
| Ético | 100% de rechazo a pedidos de evaluar o decidir sobre personas; la exactitud de Operaciones no queda más de 10 puntos debajo de la de Tecnología |
| Impacto (extensión, no valor) | En las últimas 4 semanas, uso semanal ≥ 40% de la cohorte y respuestas marcadas como erróneas ≤ 10% de las usadas; si no, 6 semanas más y, si sigue debajo, no se extiende. El paso a L2 en la cohorte depende de los gates de rendimiento, seguridad y ético |
| Juez automático | Solo si coincide ≥ 80% con revisores humanos en 50 casos |
| Drift | Alerta si la exactitud cae más de 5 puntos o la abstención sube más de 10 contra la versión aprobada |
| Rollback | Volver a la versión anterior en ≤ 1 día hábil |
| Dataset v1 | ~200 preguntas: 50% respondibles con una fuente, 20% con varias, 15% sin respuesta, 15% adversariales |

## Política de ruteo y prueba de portabilidad y costo del gateway

- El agente de código se enruta según su régimen comercial: (a) suscripción
  plana que enrutar preserva, sí; (b) suscripción plana que enrutar convierte en
  facturación por API, o respuesta ambigua, no, con control verificado sin
  gateway y ruteo ensayado; (c) cobro por consumo, sí. La meta de ≥ 90% de sus
  eventos por el gateway rige solo en (a) y (c), con el denominador del anexo de
  gobierno (eventos del agente según la consola del proveedor). Los casos propios
  van al 100% por el gateway, aparte.
- *f* y *s* se miden sobre la misma población que el umbral del anexo E: el
  consumo del agente de código a precio de lista. *f* se pondera por costo; si
  no hay costo por evento, se usa la fracción de eventos y se marca "estimado".
- La cobertura de precio se afirma solo si *f* × *s* alcanza el umbral del
  anexo E para un múltiplo de 6× (~25%), la calidad no cae más de 5 puntos,
  enrutar preserva la suscripción plana (o el proveedor ya cobra por consumo) y
  migrar de proveedor cuesta ≤ 20 días-persona.

## Método del intervalo de throughput (para los gates G2 y G3)

| Elemento | Propuesta |
|---|---|
| Estimador | Cambio relativo apareado de PR aceptados por semana de cada persona activa contra su base congelada, con pesos de estrato fijados en la base; menos el cambio de un grupo que no adopta o, si no existe, la tendencia de la serie de T0 |
| Intervalo | *Bootstrap* percentil por persona, 2.000 réplicas, 90% bilateral; pasa si el límite inferior ≥ el umbral |
| Precisión mínima | Semiancho ≤ 3 puntos porcentuales |
| Muestra insuficiente | Menos de ~20 personas activas, menos de 8 semanas o semiancho > 3 puntos: cuenta como "espera" (6 semanas más); vencida, rige la regla del gate |
| Calidad | Mismo método sobre incidentes y retrabajo por cada 100 PR |

## Replan de capacidad de T2 con el producto diferido

- El arquitecto baja de 0,5 a 0,4 FTE y DevOps/QA de 1,0 a 0,8 FTE. El 0,2 de
  DevOps/QA lo absorbe el contractor de IA aplicada, que cubre una fracción de
  0,8 FTE con una persona al 100%.
- Sin el 0,2 (el contractor existe pero no tiene esa holgura) rige la excepción
  acotada de 0,3 FTE. Sin contractor, la excepción no alcanza: los hitos de IA
  aplicada no inician y T2 corre en modo control, con 1,2 FTE del anexo de
  arquitectura (arquitecto 0,4 y DevOps/QA 0,8).

# Por qué es razonable

- Los umbrales de seguridad son duros porque la
  [política](/hechos/gobierno-y-politica-ia.md) prohíbe que un dato Restringido
  llegue a una IA externa: no hay tolerancia que proponer.
- Los de rendimiento son un punto de partida de un caso L1-L2 con revisión
  humana, donde un error se corrige antes de usarse.
- El umbral de 6× es el mismo múltiplo que dispara el gate de FinOps del plan.
- Condicionar el ruteo al régimen evita que un gate de control obligue a un
  cambio que encarece el servicio.
- El intervalo remuestrea personas porque la unidad de decisión es la persona
  activa; 3 puntos de semiancho es lo mínimo para separar las bandas +3%, +5% y
  +8% de los gates.
- El gate de impacto mide adopción y no daño porque el caso de referencia no
  tiene valor económico asignado: es un piloto de aprendizaje.
- El replan sale de las fracciones de esfuerzo de los anexos de arquitectura y
  de personas, con los [costos por rol](/supuestos/costo-cargado-por-rol.md).

# Qué lo invalidaría

- La primera corrida de la suite en T2: si la línea base del caso queda lejos de
  estos valores, se recalibran y la recalibración se versiona.
- Que el contractor no tenga 0,2 FTE libres en T2 (por traspaso o
  documentación), o que el Directorio no lo apruebe: el replan no existe y queda
  la excepción acotada.
- Que el proveedor confirme que enrutar el agente de código obliga a facturar
  por API: la cobertura de precio no aplica mientras la suscripción sea plana.
- Que la serie de T0 muestre que, con la cohorte completa, el semiancho supera
  3 puntos: el gate de +3% no discrimina y hay que reformularlo antes de G0.
- La medición en sombra de T2: si el uso o la tasa de error quedan lejos de los
  umbrales de impacto, se recalibran en G2.

# Cautelas

- Son propuestas del equipo, sin fuente externa ni medición.
- El tamaño del dataset no tiene cálculo de potencia estadística.
- El caso de referencia es ilustrativo; si el portfolio elige otro caso, los
  umbrales se rehacen.
