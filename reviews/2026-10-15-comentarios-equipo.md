# Revisión del board: siete comentarios del equipo

Fecha: 2026-10-15. Caso anonimizado: Acme Labs. Rol adoptado: `board`, sin delegación ni edición del plan o la defensa.

Dictamen sobre una propuesta de rediseño; no constituye aprobación humana de presupuesto, hechos empresariales ni entrega.

## Versión, independencia y alcance

Base: `f7e7b0e8f8036090617cecc9f9febca3443e2395`, rama `chore/anonimizar-acme`. Captura de 213 archivos, con status limpio, `diff_HEAD` vacío y ningún archivo nuevo en el alcance.

Paquete local de la sesión, sin versionar: `tmp/review-lucho-20261015/`; integridad contrastada contra su `manifest.json`. Las referencias al plan corresponden a la captura de la base Git indicada arriba, no al árbol vivo; esa base permite recuperar las fuentes versionadas.

Según el brief del orquestador, los cuatro roles trabajaron aislados: primera tanda `architect`/`governance`/`people`, después `finance`; `caio` integró y este board consolida al final.

El brief informa Codex GPT-6.1-Sol high para roles y board, y Opus 5.5 para caio. Esta lane recibió los originales y los cinco reportes, sin historial del orquestador; no repitió las miradas con contexto compartido.

Referencias: **S** = `plan/slides.md`; **A** = `plan/annexes/01-diagnostico.md`; **B** = `plan/annexes/02-arquitectura.md`; **C** = `plan/annexes/03-gobierno-seguridad.md`; **D** = `plan/annexes/04-personas-cultura.md`; **E** = `plan/annexes/05-business-case.md`; **F** = `plan/annexes/06-roadmap-riesgo.md`. `S:29` significa archivo y línea de la captura.

Revisados: contrato y rol `board`; S completo; A completo y secciones pertinentes de B-F; fichas de tamaño, utilización, concentración, uso interno, oferta y política; supuestos de datos, productividad, cohorte/costo, rampas, alternativas y señal contractual.

Se consultaron `material/index.md`, `material/mapa-plan-fuentes.md` y `material/huecos.md`, y los reportes `report-architect.md`, `report-governance.md`, `report-people.md`, `report-finance.md` y `report-caio.md` del paquete. No se usó una revisión anterior como evidencia.

## Dictamen por sombrero y cumplimiento del encargo

| Sombrero | Veredicto | Alcance de la decisión |
|---|---|---|
| Board | **Aprobado con cambios**, como dirección propuesta | Priorizar valor y comparar respuestas proporcionales es defendible. Corregir comparación, presupuesto inicial y postergación temporal antes de elevar una resolución. No se aprueba construir plataforma. |
| CFO escéptico | **Rechazado**, como autorización de gasto o justificación de retorno | El paquete no recupera su costo económico en 12 meses; faltan costo incremental comparable, horas realmente liberadas y evidencia comercial. Un experimento acotado puede proponerse con pérdida máxima explícita. |
| Corrector | **Aprobado con cambios**, como estructura de borrador; **rechazado para entrega** | Diez slides y horizonte integral de doce meses son viables en la propuesta corregida. Las fichas siguen `draft`, faltan responsables y ensayo; no se certifican formato visual ni PDF. |

**Criterio del encargo: cumplido por este informe.** Los siete puntos tienen veredicto, evidencia, matiz, cambio, dueño y cierre; se propone una estructura revisable de diez slides con los cinco pilares y doce meses.

**Integración de caio: cumplimiento parcial en su versión recibida.** Su tabla presenta 47/161/394 «con el mismo piso» sin recosteo (`report-caio.md:45`), conserva el pedido viejo tras elegir una base distinta (`:53`) y desplaza plataforma al año 2 (`:94`) sin justificar eliminar M6/M9. Se corrigen abajo; el plan sigue sin modificar.

Prioridad de hallazgos: **alta** en evidencia/capacidad (2 y 5), inversión incremental (4 y 6), demanda (3) y viabilidad de gates (7); **media** en orden narrativo (1). La falta de verificación es bloqueante para entrega, aunque esté bien declarada como cautela de borrador (A:12-25; E:30-32).

## Respuesta punto por punto

### 1. Pedido antes del problema y beneficio — parcialmente válido; media

**Evidencia y matiz:** S:29-35 abre con 33 de caja, ~1,8 FTE y señal M3 antes del diagnóstico. S:29 ya limita el pedido a tres meses; S:255-261 reconoce alternativas menores y ROI negativo del paquete. No oculta todo el problema económico ni pide aprobar ~400 hoy.

**Cambio concreto:** portada «Medir el valor antes de ampliar la inversión»; después problema, beneficio, alternativas y resolución. Usar «beneficio de caja estimado: 0», porque «caja cero» (S:261) puede confundirse con desembolso cero (E:392-399).

**Dueño:** `caio`, cifras de `finance`. **Dependencia:** elegir alcance y conciliación de cifras. **Responsable humano:** pendiente; proponer Directorio/CFO, sin asignación acordada.

**Éxito:** la solicitud final distingue caja, reserva, tiempo y preparación, y se entiende qué aprendizaje compra. **Abandono:** sin caja y capacidad confirmadas, no iniciar ese alcance; reducirlo y recostearlo.

**Alternativa:** conservar una línea de decisión en portada mejora orientación inmediata del board, pero consume espacio para fundamentar. Recomiendo una tesis breve y el monto completo al cierre.

### 2. Diagnóstico, dotación y verificación — parcialmente válido; alta

**Evidencia:** `context/hechos/tamano-y-estructura.md:15-16` incluye nómina y contratistas a septiembre; `context/hechos/capacidad-y-utilizacion.md:23-26` informa utilización y bench, y `:40` aclara que no hay corte por proyecto. Concentración corresponde a agosto (`context/hechos/cartera-y-concentracion.md:27-33`). Son poblaciones, unidades y fechas diferentes.

**Matiz:** A:12-25 y A:97-106 ya reconocen diagnóstico de escritorio y verificación pendiente. Hay fuentes documentales declaradas; no son hechos certificados. La supuesta diferencia con una conversación es **no respaldada en este paquete**: no se puede afirmar que el rango esté mal ni explicar su diferencia como hecho.

**Cambio concreto en S:65 y A:** «Tomar el diagnóstico como hipótesis. Antes de comprometer horas, conciliar corte, nómina, contratistas, personas/FTE y horas por rol; verificar las fichas para peer review y entrega». Actualizar el estado de política: la ficha advierte falta de registro posterior a abril (`context/hechos/gobierno-y-politica-ia.md:72-74`).

**Dueño:** `caio` en A/S; apoyo `people`, `finance` y `governance`. **Dependencia:** padrón, asignaciones y fuentes actuales revisadas por quienes tengan acceso. **Responsables humanos:** Talento/Operaciones/Finanzas/Seguridad, todos pendientes de asignación nominal.

**Éxito:** perímetro conciliado y asignación 2027 por rol suficiente para el compromiso; para entrega, fichas `verified` con bloque humano. Son exigencias distintas: una etiqueta `verified` no libera agendas, y una agenda aprobada no sustituye la trazabilidad de entrega.

**Abandono:** sin conciliación no derivar factibilidad de los agregados; si cambian insumos, recalcular. Si se mueven dos dimensiones de madurez, revisar prioridades (A:84). Mantener rangos con cautelas permite diseñar; retirarlos reduce precisión y riesgo de sobreafirmar.

### 3. Demanda del asistente — parcialmente válido; alta antes de producto

**Evidencia y matiz:** F:410-417 ya define usuario, tarea, dos outcomes y señal comercial con interlocutor de presupuesto y rango de referencia. F:412 mide la base recién en M7-M9, después de liberar; F:439-444 aclara que la señal no prueba disposición a pagar. E:332 imputa ingresos nuevos 0; oferta pendiente y precios sin validar en `context/hechos/ia-en-producto-y-oferta.md:42-45`.

**Cambio concreto:** antes de M6, observar el problema y medir tiempo a primera integración exitosa; dejar consultas de soporte por integración como secundaria propuesta. Elegir si se captura eficiencia, ingreso por función o retención y cómo. No convertir mejora de servicio en ingreso ni sumar toda la facturación protegida.

**Dueño:** `caio` integra F/S; `architect` mide; `finance` conecta beneficio económico. **Dependencia:** Comercial/producto, usuario elegible, sandbox permitido y esfuerzo de descubrimiento costeado. **Responsables humanos:** pendientes, incluidos dueño de producto e interlocutor comercial.

**Éxito:** dolor observado, base, beneficio principal y umbral acordado antes de financiar construcción; conservar señal proporcional de F:417. No inventar porcentaje de mejora ni precio. **Abandono:** sin problema, base o señal suficiente, diferir; documentación o soporte que resuelvan mejor la tarea desplazan al asistente.

**Alternativas:** mejorar documentación/soporte, configurar un asistente o integrarlo al producto. La integración compra aprendizaje técnico, pero exige más ingeniería; no demuestra ingreso dentro del año. La dependencia actual de plataforma M3 para producto M7-M9 sigue en F:273; una ruta técnica distinta necesita diseño y costeo.

### 4. Plataforma frente a herramientas existentes — parcialmente válido; alta

**Evidencia y matiz:** S:128-136 autoriza inventario/base/matriz/telemetría/prueba, y condiciona gateway. B:100-116 y C:366-397 reconocen superficies fuera de pasarela y protección de la suscripción. B:401-407 ya tiene decisiones buy/build; falta comparación probada de configuración actual, compra y ensamblado con cobertura y TCO equivalentes.

**Brecha:** una señal M3 libera plataforma (F:265; F:461), aunque no demuestra necesidad de esa implementación. C:494 solo cuenta restricción que condiciona el uso, mientras `context/supuestos/umbral-de-evidencia-contractual.md:21` admite prohibición o condicionamiento; F:496 deja la elección abierta.

**Cambio concreto:** «La señal habilita evaluar la respuesta mínima: brecha documentada, alternativas comparables, economía incremental o aprendizaje con pérdida aceptada y capacidad demostrada». Son condiciones nuevas propuestas, no una interpretación de la regla vigente; decide una persona. Una prohibición pura se cumple excluyendo el uso afectado.

**Controles previos propuestos:** fuentes y repositorios habilitados, datos propios/sintéticos, permisos/MCP acotados, sin credenciales productivas, escaneo local, prueba adversarial, revisión humana y aceptación del residual según autoridad. Probar antes de ejecutar/ampliar; adelantar el calendario de C:540-558 necesita validar horas y costo.

**Contradicción a cerrar:** B:625 y B:638 y F:180 dicen «solo política»; C:540-541 y F:270 exigen compensatorios probados. No sumar componentes para tapar esa diferencia textual. El gateway tampoco reemplaza controles de IDE, chat y suite.

**Dueños:** `architect` en B; `governance` en C; `caio` en F/S; `finance` costea. **Dependencias:** requisitos efectivos, configuración/pruebas, operación y régimen comercial. **Responsables humanos:** dirección técnica, Seguridad, Council y Directorio, pendientes.

**Éxito:** en M3, matriz requisito→superficie→prueba→residual→alternativa→costo y una única definición de señal. **Abandono:** sin brecha incremental, diferir plataforma y reevaluar M6/M9; control obligatorio incumplido suspende el uso afectado. Configurar ahorra integración; comprar reduce operación; ensamblar adapta controles, con mayor mantenimiento. Ninguna gana sin prueba.

### 5. Capacidad, contratación y adopción — parcialmente válido; alta

**Evidencia y matiz:** S:59, S:196, S:203 y S:270 ya muestran tensión de utilización, OKR y contractor. El promedio 83-90% y bench <1 FTE no prueban que el complemento esté libre ni disponible en los roles necesarios (`context/hechos/capacidad-y-utilizacion.md:23-26`, `:40`). Separar sobres no crea tiempo (E:174-197).

**Cuenta contrastada:** con la prueba, ~1,8 FTE clave + 654/480 = **~3,16 FTE internos totales en M1-M3**, usando el redondeo clave publicado (E:901-906). En M4-M6, 1.068/480 = 2,225 clave y 1.208/480 = 2,517 distribuidos: **4,742 internos**, más contractor externo; margen clave de apenas 12 h contra 2,25 (E:210-219).

**Cambio concreto:** matriz semanal por rol que concilie ambas bolsas sobre las mismas personas en privado: horas disponibles, trabajo desplazado, recuperación y efecto en ingresos/contribución. Mostrar el total además del piso clave. No financiar las horas iniciales con ganancias futuras ni sumar costo cargado y contribución perdida dos veces.

**Contratación:** reemplazar el título S:181 por «Formar, reasignar y decidir una excepción externa». La restricción literal es no contratar (`context/hechos/capacidad-y-utilizacion.md:35-36`); el contractor consume caja aunque no amplíe nómina. D:190 lo costea; E:307-320 distingue falta de holgura de 0,2 y ausencia completa de especialista. La excepción de 0,3 no reemplaza al especialista.

**Adopción:** D:414-422 calcula correctamente **72,5% al cumplir exactamente 85%/60%, con pesos iguales y toda Operaciones habilitada**. Es el mejor resultado de esa tabla bajo esos supuestos, no un máximo teórico de adopción. Las metas son mínimos y pueden superarse; si ambas áreas fueran 100% activas, el combinado sería 100%.

Con fracción habilitada `e`, y suponiendo que solo ese grupo aporta uso contado, el combinado es `(85% + 60% × e)/2`: 50%, 57,5%, 72,5% para e=25/50/100%. Con Tecnología en 85% y pesos iguales, llegar a 80% exige Operaciones total en 75%. No generalizar a otro padrón ni confundir el proxy de agente de código con toda IA (`context/hechos/uso-ia-interno.md:64-68`).

**Cambio de OKR propuesto:** conservar metas de D:360-362 por área y publicar combinado original, habilitados/total y cobertura. Definir «activo» antes de medir; ventana de cuatro semanas sugerida por `people` sigue sin aprobar. Corregir D:544 a 384 h del líder en sobre clave; D:320 debe decir que formación *puede* desplazar facturación. D:568 quedó desactualizado: E:120-121 y E:230-234 ya costean el avanzado como rango, sin sumar otra corrección.

**Dueños:** `people` y `finance`, con `architect` para replan y `caio` para integración. **Dependencias:** agendas, contratos, padrón y decisión de OKR. **Responsables humanos:** Operaciones/managers, Talento, Finanzas y Directorio, pendientes.

**Éxito:** cada hora tiene origen, tarea desplazada y responsable; denominadores reproducibles y excepción externa explícita. **Abandono:** bajo 1,6 FTE clave no entra ninguna versión publicada; entre 1,6 y ~1,8 retirar prueba y revisar metas/costeo (E:904-910). Sin perfil demostrado no iniciar sus hitos. Reasignar preserva caja, pero desplaza delivery; contratar cambia esa presión por caja y dependencia.

### 6. Piloto 47, paquete 394 y retorno — parcialmente válido; alta en elección

**Evidencia y matiz:** E:792-821 y S:255-261 ya comparan alternativas y admiten que las menores ganan el neto cuantificado. E:810-817 atribuye g a prácticas sobre el agente, sin mecanismo directo demostrado de throughput de plataforma/contractor. El cuestionamiento incremental es correcto; no es un descubrimiento ausente del borrador.

**Cambio concreto:** comparación a doce meses desde la misma fecha con controles aplicables equivalentes, costo de medir y beneficios incrementales. Rotular los montos siguientes como **costos publicados de alcances distintos, pendientes de homogeneizar**; no presentar la comparación corregida como realizada.

| Alcance publicado | Caja / tiempo y costo económico, miles de USD | Qué significa |
|---|---|---|
| Piloto independiente | 5 / 42 → **47** | Cohorte, matriz, prácticas y medición; sin formación general ni legal. Neto ilustrativo −47 a +15; el extremo positivo supone capturar toda la ganancia base sin plataforma. |
| Gobierno y formación desde el inicio | 21 / 141 redondeados; total publicado **161** | Formación general, política/matriz/inventario/legal y medición. Neto −161 a −99; sin compensatorios añadidos a la rama posterior. No forzar 162 a partir de sumandos redondeados. |
| Rama sin señal después de arrancar paquete | ~39 / ~160 → **~199** | ~69 de previa/arranque +6 prueba +114 continuación +4 cierre +6 compensatorios. Continúa gobierno/formación; no es el piloto de 47 ni un corte total en M3. |
| Paquete con señal, sin producto ni prueba chica | 177 / 217 → **394** | Plataforma, controles, formación y demostración externa condicional como cota superior; capacidad base ~62 y neto ~−332. |
| Mismo paquete con prueba chica | Suma ~6 de tiempo → **~400** | Cabecera de la rama con señal del borrador; no es caja ni techo anual aprobado. |
| Paquete con producto, sin prueba chica | 214 / 257 → **471** | Otro alcance: optimista ~114 de capacidad, neto ~−357. No comparar ese ROI como si costara 394. |

Fuentes: E:99-153, E:490-499, E:792-801 y E:871-881; C:586-588 confirma que los compensatorios se agregan a ~199, no a la alternativa original de 161. F:532-534 reconoce que ~199 no tiene rango ni techos propios por tramo.

**Lectura económica:** caja son pagos externos incrementales; tiempo es valuación de recursos a costo cargado, sin demostrar nueva nómina. Su suma es el costo económico publicado. El costo de oportunidad real exige conocer trabajo/contribución desplazados; capacidad liberada no es caja y solo se convierte por venta o contratación evitada con evidencia (E:392-399). No sumar dos veces las mismas horas como ahorro e ingreso.

**Recálculo independiente:** base 62,131−394=−331,869, ROI −84,231%; optimista sin producto 114,108−394=−279,892, ROI −71,039%; con producto, −356,892 y −75,773%. El paquete sigue negativo incluso optimista. El posible +15 del piloto es sensibilidad hipotética, no resultado ni retorno de caja demostrado.

Los diferenciales 394−161=233, 394−47=347 y 400−199=201 responden comparaciones diferentes. En M3 hay que comparar gastos futuros evitables desde un historial común, sin atribuir al siguiente tramo los costos ya hundidos.

**Señal no es repago:** E:457-472 solo cubre infraestructura del gateway: ejemplo medio 33/(6×21,5)=25,6%. Cubrir diferencial anual de 233 a 12× requiere 90,3% ponderado; son bases y costos distintos (E:824-825). Ni anuncio de consumo ni exigencia genérica de cliente prueban ahorro suficiente o compra.

**Dueños:** `finance` recostea; `architect`/`governance` fijan mínimos y `people` capacidad; `caio` integra. **Dependencias:** alcance, controles, evidencia comercial/precios y horas. **Responsables humanos:** Directorio/CFO y dueños de evidencia, pendientes.

**Éxito:** el board distingue qué compra cada opción y justifica el compromiso incremental. **Abandono:** si una solución menor cubre el objetivo y controles, no liberar paquete. Mantener la opción de reevaluación M6/M9; diferir al año 2 exige una decisión adicional justificada, no se deduce de elegir hoy la opción menor.

### 7. Datos, gates y claridad en diez minutos — parcialmente válido; alta en medición, media narrativa

**Evidencia y matiz:** B:228-252 y F:228-248 sí tienen protocolo, cohorte, estimador, intervalos y calidad. Disponibilidad de fuentes sigue como supuesto (`context/supuestos/disponibilidad-de-datos.md:13`, `:35`); telemetría cubre solo agente de código (`context/hechos/uso-ia-interno.md:64-65`). Tener diseño y herramientas no prueba una serie utilizable.

**Cuenta contrastada:** con estimados base +3,75% y +9% y semiancho simétrico de 3 pp, los límites inferiores son +0,75% y +6%, debajo de gates +3%/+8%. Para esos estimados harían falta semianchos ≤0,75/1 pp (B:252; F:244-248). Es aproximación de planificación; el bootstrap percentil real puede ser asimétrico y se evalúa su límite inferior.

**Cambio concreto:** acta de viabilidad antes de ratificar método: extracción reproducible, diccionario, enlace PR/CI/reversiones/tickets/incidentes, cohorte elegible, precisión y lectura simulada de pasa/espera/corta. Cada indicador declara fuente, numerador, denominador, ventana, maduración de 14/30 días, cobertura y responsable (B:228-232).

Resolver base que no resuelve antes del tratamiento (F:495): si se extiende a semana 8, desplazar también básico y prueba que empezarían en semana 5; mover solo intermedio no protege la base. Precisar precedencia de daño sobre no inferioridad en B:249, consistente con F:253; definir tratamiento de tasas base cero sin inventar datos.

**Narrativa propuesta:** «Valor medible; seguridad aceptable; fondos por decisión». Mantener bandas y acciones exactas en F; reducir la oración de S:322 a solicitud y condiciones. No borrar escenarios, riesgos ni decisiones irreversibles para ganar tiempo.

**Dueños:** `architect` en datos/protocolo, `people` en actividad/denominadores, `governance` en controles y telemetría, `finance` en valuación, `caio` integra. **Dependencias:** fuentes, cohorte, protocolo congelado y ensayo humano. **Responsables humanos:** productor de evidencia, verificador y autoridad de gate, pendientes y diferenciados.

**Éxito:** otro operador reproduce tasas y acciones con los mismos datos; ensayo real ≤10 minutos. **Abandono:** sin datos/precisión no atribuir ganancia ni liberar por valor; aplicar espera/corte o reformular antes de comenzar. Encuesta puede describir uso, pero no reemplaza medición de throughput/calidad. S:332 ya declara el ensayo pendiente.

## Tabla corregida de diez slides propuesta al CAIO

| # | Título y decisión central | Sustento y cautela |
|---|---|---|
| 1 | Medir valor antes de ampliar inversión | Portada, caso propuesto, borrador y tesis de doce meses; sin prometer repago. |
| 2 | Problema y diagnóstico por conciliar | Uso sin valor incremental medido y sin IA productiva documentada en la oferta; A y fichas. No afirmar ausencia universal de toda medición. |
| 3 | Beneficio principal y captura | Capacidad con calidad; beneficio de caja estimado 0 e ingreso nuevo 0 en el modelo; asistente como hipótesis, no beneficio validado. B/E/F. |
| 4 | Alternativas de alcances distintos | 47/161/394 publicados, pendientes de igualar controles; ~199 es rama posterior y ~400 incluye prueba. Elegir qué recostear, sin llamarlo presupuesto listo. E/C. |
| 5 | Arquitectura proporcional | Configurar/comprar/ensamblar con pruebas equivalentes; plataforma ante brecha y cuatro condiciones propuestas. B. |
| 6 | Gobierno y seguridad antes de usar | Autoridades, controles mínimos por superficie, residual y poder de suspensión; producto prepara, no ejecuta. C. |
| 7 | Personas y capacidad efectivas | Total interno por tramo, trabajo desplazado, excepción externa y OKR por área sin declarar cumplido el combinado. D/E. |
| 8 | Roadmap integral a doce meses | M1-M3 diagnóstico/base/política/formación/prueba; M4-M6 solución según evidencia; M7-M9 aplicación/producto condicional; M10-M12 evaluación/traspaso. Riesgo mensual; gates M3/6/9/12; releer señales M6/M9. F. |
| 9 | Compromiso, pérdida y escenarios | Separar costo económico, caja, tiempo y beneficio; escenarios de corte y reserva. Montos del pedido vigente solo si se conserva exactamente su alcance. E/F. |
| 10 | Resolución propuesta y equipo | Autorizar únicamente el tramo costeado y su marco de decisión, sujeto a evidencia; equipo incluido, responsables pendientes. Irreversibles se deciden al cierre para después. F:458-481. |

**Pedido vigente del borrador**, si se mantiene su alcance: hasta 33 de caja +6 de reserva, hasta 72 de tiempo M1-M3 y hasta 7 de preparación; también explicitar núcleo mínimo tras corte, hasta 41 de tiempo, y los máximos de salida de E:883-916. No confundir esos techos con los medios anuales.

**Si se elige empezar por otro paquete mínimo**, la solicitud cambia: presupuesto, capacidad, reserva, secuencia y salidas quedan **pendientes de costeo**. No hereda 33+6/72+7 ni se llama «base común» sin definir entregables. La resolución puede pedir completar ese costeo, sin autorizar ejecución del paquete indefinido.

Checklist contra consigna: estrategia integral **cumple como cobertura propuesta** (slides 3 y 5-7); roadmap técnico/financiero/cultural **cumple como diseño** (8-9); storytelling CFO **cumple con las correcciones económicas** (3-4/9); riesgo, contingencias y reversibilidad **cumple como diseño** (6/8-10); defensa **no cumple aún su validación humana**; máximo diez incluyendo portada/equipo **cumple en esta tabla**, sin render comprobado.

El reparto de caio suma 600 segundos (`report-caio.md:98-102`), pero sumar tiempos propuestos no prueba exposición clara ni duración real. Fusionar arquitectura/gobierno libera una slide para riesgos, con menor espacio para explicar responsabilidades; conservar ambas exige sintetizar los escenarios sin perder su trazabilidad.

## Gates medibles para someter a decisión humana

Todos son propuestas o reglas del borrador que necesitan ratificación; no son resultados observados. Mantener seguridad antes que dependencias y caja (F:220-225).

| Momento | Evidencia exigible y decisión propuesta | Si falta o falla |
|---|---|---|
| Antes de iniciar | Alcance/presupuesto definidos; horas por rol liberadas; vía de IA aplicada demostrada; viabilidad del protocolo y decisión de calendario; controles aplicables probados antes de usar. | Reducir/diferir y recostear; no afirmar que el presupuesto libera tiempo. |
| M3 | Base fechada, política ratificada, matriz habilitante y básico ≥90% según F:259-264. Para plataforma: señal/brecha + comparación + economía incremental o pérdida de aprendizaje aceptada + capacidad; reserva y contrato para nuevo compromiso. | Aplicar acciones de cada condición, sin convertirlas en un pase global; sin justificación incremental, continuar variante mínima costeada y releer M6/M9. |
| M6, valor y adopción | Límite inferior throughput ≥+3%, calidad sin daño según protocolo; Tecnología ≥80%, cobertura y denominador publicados (F:268-269). | Estimado ≤0 o daño: corte del frente interno; estimado >0 insuficiente: espera una vez, 6 semanas, y corte al vencer si no pasa. Adopción tiene acciones propias, sin equipararla a valor. |
| M6, controles y plataforma | Pruebas de cobertura por superficie, críticos cerrados, residual aceptado; ruteo solo si preserva régimen comercial. Si se declara cobertura de precio: fc×s contra umbral, calidad y portabilidad de B:189-194. | Superficie no cubierta se declara y escala; sin prueba económica retirar beneficio de precio. Conservar gateway exige justificar control frente a alternativa menor, no cambiar automáticamente la promesa. |
| M6, producto | Problema/base y métrica principal antes de liberar, comparación menor y señal escrita con presupuesto/rango de F:417; ampliar horas y costear descubrimiento. | Sin evidencia, diferir; sin plataforma M3 no prometer M7-M9 bajo la secuencia vigente (F:273). |
| M9 | Límite inferior ≥+8%; si estimado ≥+5% sin pasar, mantenimiento/base mínima y relectura a 6 semanas; <+5% corta. Producto: SLO acordado, cero cruces de tenant y críticos cerrados. | Aplicar F:274-277 y precedencia si sigue otro frente; una filtración cancela función. Señal tardía de plataforma se evalúa con calendario/costo nuevos, no con promesa del itinerario original. |
| M12 | Tecnología ≥85%, Operaciones habilitadas ≥60%, ambos denominadores y combinado informados; decisión de continuidad y trayectoria al equilibrio o interés contractual según F:278-279. | Sin fundamento, no financiar régimen completo. Contratos externos, datos productivos, mayor autonomía y compromisos largos requieren decisión explícita para después del horizonte. |

N≥15, ocho semanas y precisión mínima no garantizan pasar: demostrar límite inferior y calidad en cada lectura (B:243-252). Datos faltantes se reportan «sin medir»; distinguir causa del fallo y aplicar la regla congelada, sin inventar nuevas bandas después del resultado.

## Decisiones y evidencia humanas pendientes

1. Registrar acuerdo del equipo sobre el caso y responsables nominales por sección/gate (S:328; F:42). Los dueños agentes anteriores son autores, no personas que comprometieron recursos.
2. Conciliar perímetros y vigencia de fuentes; verificar hechos/supuestos para entrega con bloque `verified` humano. Para asignar horas, exigir además matriz de agendas y trabajo desplazado validada por managers/Operaciones/Finanzas; la conversación faltante solo es necesaria para resolver aquella comparación específica.
3. Elegir paquete inicial y pérdida máxima de aprendizaje; validar caja, costo cargado, contribución desplazada y reservas en privado; publicar únicamente rangos/modelos autorizados. Si cambia alcance, recostear antes de aprobar.
4. Ratificar nueva regla de cuatro condiciones y lectura restringida de señal, o conservar la vigente como apuesta de aprendizaje explícita. Decidir cómo se prueba y quién acepta cada residual; la aceptación no sustituye permiso contractual.
5. Aprobar excepción externa y sobres de capacidad; distinguir replan de respaldo sin contractor. Aprobar OKR por área, definición de actividad/cobertura/ventana y tratamiento del dato ausente, sin presentar metas nuevas como resultados.
6. Demostrar fuentes/precisión y congelar método/calendario antes del tratamiento; decidir base insuficiente. Comercial/producto deben validar problema y beneficio principal del asistente, y luego señal proporcional, precio y eventual compra, sin inferir consenso.

**Éxito del rediseño:** propuestas editables por sus dueños, cifras con alcance y fuente exactos, decisiones humanas identificadas y problema→beneficio→alternativas→costo→resolución entendibles en ensayo de diez minutos. Para entrega se agregan verificación humana y controles de artefacto; este informe no los reemplaza.

**Abandono/revisión:** sin datos, horas o controles, reducir/diferir; si basta una alternativa menor, no ampliar plataforma. Mantener reevaluaciones M6/M9 de E:880 y F:461. Pasar toda plataforma al año 2 sería cambiar esa opción y debe justificarse por secuencia, costo o evidencia, sin asumir una postergación permanente.

## Cinco preguntas más difíciles de defensa

1. Si el agente ya está pago y el piloto publicado cuesta 47, qué brecha verificable justifica el siguiente gasto de plataforma, después de igualar controles y descontar costos hundidos?
2. Qué personas liberan las ~3,16 FTE internas iniciales y el pico de ~4,74, qué entrega/contribución se desplaza y por qué separar sobres no oculta doble asignación?
3. Si el caso base de productividad puede esperar y cortar, qué pérdida máxima acepta el Directorio para aprender, qué fondos quedan comprometidos al salir y qué controles deben sobrevivir?
4. Qué problema observado del cliente mejora el asistente frente a documentación/soporte, quién tiene presupuesto y cómo pasa de interés a margen o compra sin contar dos veces el mismo beneficio?
5. Qué extracción y pruebas permiten decidir los gates, cómo tratarán incertidumbre y daño, y quién puede suspender el uso aunque el gasto o la adopción parezcan cumplir?

## Verificación y limitaciones

Salida local observada al contrastar captura y recalcular en Python, sin modificar el plan:

```text
files=213; mismatches=[]; status=''; diff_HEAD=''; untracked=[]
base: capacity=62.131; net=-331.869; ROI=-84.231%
pessimistic: capacity=12.189; net=-381.811; ROI=-96.906%
optimistic_product: capacity=114.108; net=-356.892; ROI=-75.773%
optimistic_no_product: capacity=114.108; net=-279.892; ROI=-71.039%
branches: with_trial=400; no_signal=199; differences=233,347,201
Q1 FTE approx=3.1625; Q2 key=2.225; Q2 total=4.7417; Q2 key margin hours=12.0
adoption: equal_weights_targets=72.5%; theoretical_all_active=100.0%; operations_needed=75%
gate lower bounds: 0.75, 6; max symmetric semispans: 0.75, 1
Context statuses: 36 draft; 0 verified
```

Capacidad calculada como `17,5×4.750×3×Σ[g×r/(1+g×r)]/1.000`, con g=15/5/25% y las rampas de las fichas `desarrolladores-en-equipos-propios.md:11-14` y `rampa-de-la-ganancia.md:11-15`. Consistencia matemática sobre supuestos; no auditoría completa de todos los renglones ni verificación empírica de costos/beneficios.

**Limitaciones de acceso:** no se consultaron fuentes privadas, conversación original de dotación, credenciales, Notebook ni normativa externa. El material declara huecos, incluido cierre/defensa (`material/huecos.md:11-15`). Esta revisión documental no certifica obligaciones legales actuales ni vigencia de fuentes empresariales.

**Deficiencias de contenido separadas:** ausencia de comparación recosteada, responsables, evidencia ejecutable de datos/controles y demanda validada; contradicción de rama «solo política» y compensatorios; decisiones de señal/base/OKR sin cerrar. Esas sí están documentadas arriba y no se excusan por falta de acceso.

Control adicional del informe guardado; las referencias se verificaron por existencia/rango y se contrastaron semánticamente durante la lectura. El control de patrones es parcial y no certifica ausencia de información privada:

```text
seven_points=7; Slide rows=10; defense_questions=5
Reference bounds: checked=101; errors=[]
Fixed privacy patterns: hits=0; private denylist not consulted; partial check
Snapshot: files=213; mismatches=[]
Protected scope diff bytes=0
```

No hubo revisión visual, generación/inspección del PDF ni ensayo de defensa. No se ejecuta build del plan porque no se editó; no hay build estricto definido para este informe. Verificación acotada a integridad, recálculo, referencias y lectura del artefacto.

Se aplica `verify-before-done` con esos límites; no se delega verificador porque el encargo lo prohíbe. En Codex se omite `lh metrics record-verify` según el skill. Sin commit, push, PR ni cambios del vault/PRJ: el brief autoriza exclusivamente este reporte.
