# Guion oral de la defensa

Lo que se dice en voz alta, slide por slide. Tope: **12 minutos**, para
dejar 3 de margen sobre el máximo de 15. El texto suma unas 1.040 palabras,
unos 8 minutos a 130 palabras por minuto; el resto absorbe pausas, siete
cambios de voz y señalar la slide. Cada tiempo es un tope: si un bloque se
pasa, se corta, no se acelera.

- **Se dice esto, no se lee la slide.** El board la ve; la voz agrega el por qué.
- **Solo se dicen las cifras de la slide.** Si preguntan más, se responde con
  [el banco de objeciones](objeciones.md) y el anexo, no improvisando.
- **Reparto por rol, sin nombres.** Abajo van ocho voces (P1 a P8) atadas al
  anexo que respalda cada slide. Los nombres se ponen en
  [#21](https://github.com/lazynet/tp-caio-g11-2026/issues/21).
- **Sin ensayo todavía.** Los tiempos son estimados por palabras; se corrigen
  con el cronómetro del primer ensayo.

## Las cinco cifras que nadie puede errar

| Cifra | Qué es | Qué no es |
|---|---|---|
| **8k USD** | Lo que se libera hoy: tiempo propio, caja 0, diez días de validación | No es gasto de caja |
| **+71k USD** | Segunda liberación, la firma el CEO solo si se cumple R-05 | No es automática |
| **79k USD** | Techo acumulado hasta cerrar M3 (10 de caja + 69 de tiempo) | No es gasto esperado |
| **121k USD** | Techo anual: 79 + 16 + 13 + 13, cada tramo con su firma | No está liberado |
| **0** | Beneficio de caja e ingreso nuevo presupuestados | No es "no hay valor" |

Si una sola cosa queda clara, que sea esta: **hoy se aprueba arriesgar 8k de
tiempo, no 121k de caja.**

## Reparto

Ocho voces para diez slides. Criterio: cada voz presenta la slide cuyo anexo
domina, y las dos que repiten lo hacen en slides consecutivas o en la apertura y
el cierre, para no sumar cambios de orador. Siete cambios de voz en total.

| Voz | Rol | Presenta | Responde objeciones | Respaldo de |
|---|---|---|---|---|
| P1 | Coordinación de la defensa | 1 y 10 | Qué se pide hoy (3, 31, 53); deriva el resto | P8 |
| P2 | Diagnóstico (Anexo A) | 2 | 19, 25, 45 | P3 |
| P3 | Material de la cursada | 3 | 21, 22, 47; "dónde se ve la cursada" | P2 |
| P4 | Arquitectura (Anexo B) | 4 y 5 | 1, 4, 26, 28, 48 | P6 |
| P5 | Personas y cultura (Anexo D) | 6 | 2, 8, 9, 14, 15, 40–42, 44 | P7 |
| P6 | Gobierno y seguridad (Anexo C) | 7 | 5, 11, 12, 13, 20, 23, 54, 55 | P4 |
| P7 | Roadmap y riesgo (Anexo F) | 8 | 24, 27, 43, 46, 52 | P5 |
| P8 | Business case (Anexo E) | 9 | 3, 6, 7, 10, 16–18, 29–39, 49–51, 56 | P1 |

- **En las preguntas, P1 modera:** escucha, nombra a la voz que responde y
  corta si una respuesta pasa de un minuto. Si la voz no sabe, contesta su respaldo.
- **Diferencia con la propuesta de [la storyline](storyline.md#reparto-de-presentadores-propuesta-del-equipo-no-acordada):**
  ahí la slide 4 la presentaba Business case; acá la presenta Arquitectura,
  que sigue con la 5 sin cambio de voz. La objeción 4 (asistente) pasa a P4.

## Reloj

| # | Slide | Voz | Tiempo | Acumulado |
|---|---|---|---|---|
| 1 | Portada | P1 | 0:45 | 0:45 |
| 2 | Problema de negocio | P2 | 1:15 | 2:00 |
| 3 | Priorización | P3 | 1:15 | 3:15 |
| 4 | Iniciativas concretas | P4 | 1:30 | 4:45 |
| 5 | Arquitectura | P4 | 1:00 | 5:45 |
| 6 | Personas | P5 | 1:15 | 7:00 |
| 7 | Gobierno y seguridad | P6 | 1:15 | 8:15 |
| 8 | Roadmap | P7 | 1:15 | 9:30 |
| 9 | Dinero y escenarios | P8 | 1:30 | 11:00 |
| 10 | Decisión | P1 | 1:00 | 12:00 |

Control a mitad de camino: **al terminar la slide 5 tiene que ir por 6:00 o
menos.** Si va pasado, en las slides 6 y 7 se dice solo la primera y la última frase.

---

## 1. Portada · P1 · 0:45

> Buenas tardes. Somos el Grupo 11 y venimos a pedirles una decisión sobre
> Acme Labs.
>
> Acme ya usa inteligencia artificial para desarrollar software, pero hoy no
> puede decir cuánto mejora sus entregas. Nuestro plan a doce meses hace dos
> cosas: medir ese aporte con las herramientas que ya tenemos, y estudiar un
> asistente de integración para clientes, sin construirlo todavía.
>
> Lo decimos de entrada: no presupuestamos retorno de caja en el año. Lo que
> pedimos es aprender con un riesgo chico y con frenos en cada etapa.

**Transición:** "Empecemos por el problema."

## 2. Problema de negocio · P2 · 1:15

> Acme desarrolla software para bancos y fintechs. La gente ya usa IA en su
> trabajo, pero nadie comparó los resultados contra una línea de base. No
> sabemos si entregamos mejor o solo escribimos más código.
>
> Hay dos tensiones. La primera es la capacidad: entre el 83 y el 90 por ciento
> de las horas se facturan. Cada hora que le damos al plan puede salir de una
> entrega a un cliente. Y un promedio de utilización no nos dice si hay agendas
> libres.
>
> La segunda es la calidad. Más código no es más valor si trae más retrabajo, y
> cada cliente pone restricciones sobre qué podemos probar con su código.
>
> Por eso lo primero que pedimos no es ejecutar: es validar el diagnóstico y las
> agendas reales.

**Transición:** "Con ese problema, elegimos qué hacer y qué no."

## 3. Priorización de iniciativas · P3 · 1:15

> Evaluamos cuatro iniciativas por impacto, factibilidad y riesgo.
>
> Probamos una: la prueba operativa, porque usa herramientas que ya tenemos.
> Estudiamos otra: el asistente de integración, porque falta validar que el
> cliente tenga el problema y quiera pagar por resolverlo.
>
> Y postergamos dos que suenan mejor en una presentación: IA en pagos, que
> depende de habilitaciones externas, y un servicio de agentes, que nos falta
> certificar y competiría por las mismas personas que hoy entregan.
>
> No pusimos puntajes numéricos. Sin datos, un puntaje sería precisión inventada.

**Transición:** "Bajemos las dos elegidas a tareas concretas."

## 4. Iniciativas concretas · P4 · 1:30

> En operación, el candidato es simple de explicar: corregir con IA un defecto
> real de nuestro propio código. Con una prueba que falla antes y pasa después,
> revisada por otra persona, con integración continua y aceptada por quien lo usa.
> Si sale, tenemos una corrección en uso real dentro de los primeros tres meses.
>
> Ojo con lo que eso no prueba: una corrección no demuestra productividad ni
> retorno. Y no suma horas: reemplaza una tarea que ya estaba costeada. Si no
> entra, se saca.
>
> En la oferta, la hipótesis es un asistente que ayude al desarrollador del
> cliente a integrarse con nuestra plataforma. Antes del mes 6 medimos cuánto
> tarda hoy la primera integración exitosa y buscamos una señal comercial por
> escrito, con presupuesto. Si mejorar la documentación resuelve lo mismo, el
> asistente se descarta.

**Transición:** "Para hacer esto no compramos nada nuevo."

## 5. Arquitectura · P4 · 1:00

> La decisión de arquitectura es configurar lo que ya existe antes de comprar o
> construir.
>
> Tres pasos: configurar, acotando permisos y registrando el uso; medir, con una
> extracción repetible de cambios, fallas e incidentes; y revisar, con una
> persona siempre en el circuito.
>
> Una plataforma central no está en este pedido. Para pedirla vamos a tener que
> mostrar una brecha real, alternativas comparadas y una economía que la
> justifique. Es una decisión reversible y separada.

**Transición:** "Lo más escaso no es la tecnología, es el tiempo de la gente."

## 6. Personas y adopción · P5 · 1:15

> La formación en IA es por rol, en horario laboral y con casos reales. La meta a
> tres meses es que al menos el 90 por ciento apruebe el nivel básico con un caso
> práctico.
>
> Pero la formación sin tiempo protegido es una promesa vacía. Por eso
> operaciones y cada manager confirman por separado las horas, qué trabajo se
> desplaza y cómo se recupera. Si las horas no aparecen, reducimos el plan antes
> de empezar.
>
> Y un compromiso explícito: durante doce meses, la mejora por IA no se usa para
> desvincular. Se reasigna y se capacita. Lo decimos porque, una vez comunicado,
> es muy caro de deshacer.

**Transición:** "Ningún uso se habilita sin controles."

## 7. Gobierno y seguridad · P6 · 1:15

> Cada uso nuevo pasa por tres pasos. Probar: ensayamos fugas con secretos
> falsos y ataques. Autorizar: quien produce, quien verifica y quien firma son
> personas distintas, y el riesgo que queda se acepta por escrito. Y suspender:
> seguridad puede frenar un uso aunque el gasto y la adopción vayan bien.
>
> En producto, la IA prepara y la persona decide y ejecuta. No hay crédito ni
> scoring con IA en el año. Y el código y los datos de clientes no van a modelos
> externos, salvo en el entorno del cliente y con su permiso escrito.

**Transición:** "Todo esto se ordena en etapas, cada una con su firma."

## 8. Roadmap ajustado al riesgo · P7 · 1:15

> El año tiene cuatro etapas y cada una necesita una firma nueva.
>
> En los meses 1 a 3 armamos la base, los controles y la formación. En el 4 al 6
> medimos y estudiamos la integración; en el mes 6 todavía no leemos valor,
> porque la muestra todavía no alcanza. En el mes 9 sí: avanzamos solo si la
> mejora es distinguible de cero y sin daño en la calidad. Del 10 al 12
> decidimos continuidad.
>
> Si en algún punto no hay agenda, la medición no sirve o aparece un daño,
> se corta. Y seguridad puede suspender en cualquier momento.

**Transición:** "Ahora, lo que les importa a ustedes: cuánto y para qué."

## 9. Dinero y escenarios · P8 · 1:30

> Dos números: 79 mil dólares es el techo hasta cerrar el mes 3, de los cuales
> 10 son caja y 69 tiempo de nuestra propia gente. 121 mil es el techo anual,
> y cada tramo necesita pasar su compuerta.
>
> Son techos, no gasto esperado.
>
> En el escenario pesimista, la validación no sostiene el plan y lo reducimos o
> detenemos antes de empezar. Si corta en el mes 3, lo máximo del año es 85 mil.
> En el base, seguimos con el mínimo y beneficio de caja cero. En el optimista,
> medimos mejora sin daño. Pero esa capacidad solo se vuelve plata si el
> contrato lo permite y demostramos ingreso o costo evitado.
>
> Les pedimos que acepten aprender con una exposición acotada, sin prometer
> repago en el año. Preferimos eso a un ROI que no podemos sostener.

**Transición:** "Entonces, qué les pedimos hoy."

## 10. Decisión del Directorio · P1 · 1:00

> Les pedimos aprobar el plan y sus resoluciones.
>
> Hoy son 8 mil dólares de tiempo propio, con caja cero, para diez días hábiles
> de validación. Si la validación cumple las condiciones, el CEO firma la segunda
> liberación de hasta 71 mil. No es automática. El techo anual es 121 mil, y cada
> tramo vuelve a pasar por una firma.
>
> No aprobamos plataforma ni construcción de producto. Cualquier exceso vuelve
> a este Directorio.
>
> Riesgo acotado, frenos en cada etapa y una respuesta honesta sobre el retorno.
> Muchas gracias; quedamos para sus preguntas.

---

## Si el tiempo aprieta

Cortes en este orden, sin tocar las slides 9 y 10:

1. Slide 3: sacar la frase de los puntajes numéricos.
2. Slide 4: sacar el párrafo "Ojo con lo que eso no prueba" (queda para las preguntas).
3. Slide 5: decir solo la primera y la última frase.
4. Slide 7: sacar la línea de crédito y scoring.

## Puente a las preguntas

Las primeras respuestas salen de
[Respuestas para abrir la conversación](objeciones.md#respuestas-para-abrir-la-conversación);
las difíciles, de [las cinco preguntas más difíciles](objeciones.md#las-cinco-preguntas-más-difíciles).
Regla: responder en dos frases, nombrar el anexo y ofrecer el detalle. Si no se
sabe, se dice y se anota; no se inventa una cifra.
