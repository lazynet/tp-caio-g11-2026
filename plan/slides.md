---
owner: caio
status: ready
marp: true
theme: acme
paginate: true
size: 16:9
lang: es-AR
---
<style>
section table th { background: var(--green); }
section .note { font-size: 19px; line-height: 1.4; }
section .card p { font-size: 22px; line-height: 1.4; }
section .card h3 { font-size: 28px; }
section .decision { font-size: 20px; }
section .decision .pill { font-size: 17px; }
section .decision .ref { font-size: 16px; }
section .decision .ref a::after { content: " →"; }
section .card.dashed .tag { color: #5e574e; }
.lead { font-size: 28px; line-height: 1.4; margin: 0 0 24px; }
.steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin: 20px 0; }
.steps > div { background: var(--sand); border-top: 7px solid var(--green-soft); border-radius: 8px; padding: 20px 16px; }
.steps h3 { font-size: 29px; margin: 10px 0 14px; }
.steps p { font-size: 22px; line-height: 1.4; margin: 0; }
.steps .month { font-size: 18px; font-weight: 700; color: var(--green); }
.roadmap table { font-size: 20px; line-height: 1.35; }
.roadmap th, .roadmap td { padding: 11px 13px; }
.roadmap td:first-child { width: 125px; }
section .kpi .num { font-size: 60px; }
section .kpi .lbl { font-size: 22px; line-height: 1.35; }
.money { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin: 20px 0; }
.money > div { border-top: 3px solid var(--green-soft); padding-top: 14px; }
.money strong { font-family: "Caprasimo", Georgia, serif; font-size: 58px; font-weight: 400; color: var(--rust); }
.money p { font-size: 22px; line-height: 1.4; }
section.closing .money strong { color: #fff; }
section.closing .money > div { border-top-color: #8b9d6d; }
section.closing .fine, section.cover .fine { font-size: 18px; color: #dcd8c9; }
</style>

<!-- Fuente única del deck. Las condiciones completas rigen en el Anexo G.
     Una decisión por slide; los anexos conservan la evidencia y las excepciones. -->

<!-- _class: cover -->
<!-- _paginate: false -->

<div class="sun"></div>

<span class="chip">Grupo 11 · Diplomatura CAIO · UTN BA</span>

# IA para mejorar las entregas

<p class="sub"><strong>Acme Labs · Plan Maestro 2027</strong></p>

<p style="font-size:30px;line-height:1.4;max-width:850px">Medir el aporte de la IA en la operación y estudiar un asistente de integración para clientes.</p>

<p style="font-size:25px;max-width:820px">Herramientas actuales, controles probados y fondos por etapa.</p>

<p class="fine">Propuesta al Directorio · 12 meses · Cifras estimadas, sujetas a validación.</p>

<div class="fine">

Pedido: aprobar el plan y las resoluciones del [Anexo G](annexes/07-resoluciones.md). Beneficio de caja e ingreso nuevo presupuestados: 0.

</div>

---

<p class="eyebrow">Problema de negocio</p>

# La IA ya se usa y falta medir su aporte

<p class="lead">Acme desarrolla software para bancos y fintechs. El uso interno de IA todavía no demuestra cuánto mejora la entrega frente a una base comparable.</p>

<div class="grid g2">
<div class="card dark">
<h3>Proteger las entregas</h3>
<p><strong>83–90% de las horas se facturan.</strong> Reservar personas para el plan puede desplazar entregas. El promedio de utilización no demuestra agendas disponibles.</p>
</div>
<div class="card">
<h3>La calidad protege el negocio</h3>
<p>Necesitamos distinguir capacidad útil de más código y más retrabajo. Las restricciones de cada cliente condicionan qué usos podemos probar.</p>
</div>
</div>

<p class="note">Diagnóstico de madurez en cinco dimensiones, de escritorio y a validar. La mejora todavía debe demostrarse.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Validar diagnóstico y agendas antes de comprometer la ejecución.</span>
<span class="ref">

[Anexo A](annexes/01-diagnostico.md)

</span>
</div>

---

<p class="eyebrow">Priorización de iniciativas</p>

# Elegimos impacto viable con riesgo acotado

<div class="roadmap">

| Iniciativa | Impacto buscado | Factibilidad y riesgo | Prioridad |
|---|---|---|---|
| Prueba operativa | Capacidad con calidad | Herramientas existentes; controles por probar | **Probar** |
| Asistente de integración | Mejor soporte al cliente | Documentación propia; falta validar problema y señal | **Estudiar**, sin construir |
| IA en pagos | Nueva función de producto | Habilitación externa y seguridad pendientes | Postergar |
| Servicio de agentes | Nueva oferta | Faltan certificaciones; compite con entregas | Postergar |

</div>

<p class="note">Matriz factibilidad–impacto y RICE ajustado por riesgo. Puntajes de producto hipotéticos, a validar; operación sin puntaje nuevo.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Elegir el mínimo y un estudio acotado. Construir producto requiere otra decisión.</span>
<span class="ref">

[Anexo F](annexes/06-roadmap-riesgo.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>

---

<p class="eyebrow">Iniciativas concretas</p>

# Dos tareas para poner a prueba el valor

<div class="grid g2">
<div class="card dark">
<h3>Operación: corrección útil</h3>
<p><strong>Candidato a quick win:</strong> corregir con IA un defecto real de código propio usado. Regresión que falla antes y pasa después, revisión de otra persona, CI y aceptación del usuario.</p>
<p><strong>Resultado propuesto:</strong> corrección integrada y en uso real dentro de la prueba de M3, tras base, formación y controles. Sin capacidad confirmada, se retira de M3.</p>
</div>
<div class="card">
<h3>Oferta: asistente de integración</h3>
<p><strong>Hipótesis:</strong> ayudar al desarrollador del cliente a encontrar funciones, preparar llamadas y entender errores en un sandbox.</p>
<p><strong>Estudiamos antes de M6:</strong> tiempo a la primera integración exitosa, consultas de soporte y señal comercial escrita con presupuesto y rango de precio.</p>
</div>
</div>

<p class="note">Candidato no aprobado ni observado: sustituye una tarea de la prueba costeada, sin horas nuevas ni productividad o ROI demostrados. El asistente usa documentación propia y datos sintéticos; mejor documentación o soporte pueden reemplazarlo.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Operación primero; asistente como hipótesis que puede descartarse.</span>
<span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">Arquitectura proporcional</p>

# Empezamos con las herramientas actuales

<p class="lead">Build / buy / agentificar: primero configuramos lo existente y probamos controles por herramienta.</p>

<div class="grid g3">
<div class="card dark">
<h3>Configurar</h3>
<p>Acotar permisos y conectores. Escanear secretos y registrar el uso.</p>
</div>
<div class="card">
<h3>Medir</h3>
<p>Repetir la extracción de cambios aceptados, fallas, reversiones e incidentes.</p>
</div>
<div class="card">
<h3>Revisar</h3>
<p>Mantener revisión humana y probar los controles de cada herramienta antes de habilitar un uso nuevo.</p>
</div>
</div>

<p class="note">Una plataforma central requiere señal, brecha demostrada, alternativas comparables, economía incremental o aprendizaje con pérdida aceptada y límite declarado, y capacidad demostrada.</p>

<div class="decision">
<span class="pill">Decisión reversible</span>
<span class="body">Configurar lo existente. Nueva agentificación, plataforma y modelo propio: otra decisión.</span>
<span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>

---

<p class="eyebrow">Personas y adopción</p>

# La formación necesita tiempo protegido

<div class="grid g2">
<div class="card dark">
<h3>AI literacy por rol</h3>
<p>Formación básica para toda la organización e intermedia para la cohorte de prueba. Casos por rol, en horario laboral.</p>
<p><strong>Meta M3:</strong> al menos 90% aprueba el básico con un caso práctico.</p>
</div>
<div class="card">
<h3>Confirmar agendas reales</h3>
<p>Operaciones y managers confirman por separado las horas de soporte y de formación, el trabajo desplazado y cómo recuperarlo.</p>
<p>Sin capacidad o facilitación demostrada, se reduce o resecuencia antes de liberar M1.</p>
</div>
</div>

<p style="font-size:25px;margin-top:22px"><strong>Compromiso por 12 meses:</strong> la mejora por IA no se usa para desvincular. Se reasigna y se capacita. Comunicarlo es costoso de deshacer.</p>

<p class="note">La regla de empleo excluye causas previas ajenas a la IA. El mínimo usa roles existentes; incorporaciones y formación ampliada requieren decisión y caja propias.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Reservar tiempo verificable y sostener la transición acordada.</span>
<span class="ref">

[Anexo D](annexes/04-personas-cultura.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>

---

<p class="eyebrow">Gobierno y seguridad</p>

# Cada uso se habilita con evidencia

<div class="grid g3">
<div class="card">
<h3>Probar</h3>
<p>Ensayar fugas con secretos falsos, ataques y revisión humana. Corregir problemas críticos.</p>
</div>
<div class="card dark">
<h3>Autorizar</h3>
<p>Separar quién produce, quién verifica y quién firma. Aceptar el riesgo restante por escrito.</p>
</div>
<div class="card">
<h3>Suspender</h3>
<p>Seguridad puede frenar un uso aunque el gasto y la adopción cumplan.</p>
</div>
</div>

<p style="font-size:25px;margin-top:24px"><strong>Human-in-the-loop:</strong> en producto, tope de autonomía 2: la IA prepara; la persona decide y ejecuta.</p>

<p class="note">Sin crédito ni scoring con IA por 12 meses. Código y datos de clientes: fuera de modelos externos, salvo en su entorno y con permiso escrito. Código bajo NDA: se suspende al aprobar; transición completa en G.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Ratificar la política y exigir controles antes de cada uso nuevo o ampliado.</span>
<span class="ref">

[Anexo C](annexes/03-gobierno-seguridad.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>

---

<p class="eyebrow">Roadmap integrado · Kill/scale gates</p>

# Cada etapa necesita una nueva firma

<div class="roadmap">

| | Meses 1–3 | Meses 4–6 | Meses 7–9 | Meses 10–12 |
|---|---|---|---|---|
| Trabajo | Base, controles y formación | Medición y estudio de integración | Lectura de valor y seguimiento de uso | Evaluación y traspaso |
| Compuerta | Base y controles probados | Adopción, costo y controles; no lee valor | Piso del intervalo >0 y sin daño | Decidir continuidad y año 2 |
| Techo<br>k USD | **79 acumulados**, con preparación y cierre | **+16** | **+13** | **+13** |

</div>

<p style="font-size:24px;margin-top:20px">Kill-fast: sin agenda o viabilidad, se reduce o detiene antes de M1. Kill/scale gates: decidir por etapa; valor en M9.</p>

<p class="note">El CEO firma dentro de cada tramo, el CFO verifica y el comité dictamina. Seguridad puede suspender siempre. M9 acredita el piso del intervalo de 90%; si no es viable medir: beneficio 0, sin expansión. Condiciones completas en F.</p>

<div class="decision">
<span class="pill">Decisión reversible</span>
<span class="body">Fondos por compuerta. Superar un tramo o ampliar alcance vuelve al Directorio.</span>
<span class="ref">

[Anexo F](annexes/06-roadmap-riesgo.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>

---

<p class="eyebrow">Dinero y escenarios</p>

# El límite de recursos no promete retorno

<div class="grid g2" style="margin:10px 0 18px">
<div class="kpi"><div class="num">79k USD</div><div class="lbl">techo hasta cerrar M3<br><strong>10 caja + 69 tiempo propio</strong></div></div>
<div class="kpi"><div class="num">121k USD</div><div class="lbl">techo anual, sujeto a gates<br><strong>16 caja + 105 tiempo propio</strong></div></div>
</div>

<div class="grid g3">
<div class="card">
<h3>Pesimista</h3>
<p>La validación no sostiene el alcance: se reduce o detiene antes de M1. Si corta en M3, el máximo anual con guardia aprobada es 85k.</p>
</div>
<div class="card">
<h3>Base</h3>
<p>Continuidad condicionada del mínimo. Beneficio de caja e ingreso nuevo presupuestados: <strong>0</strong>.</p>
</div>
<div class="card dark">
<h3>Optimista</h3>
<p>Mejora medible sin daño. La capacidad genera dinero solo si el contrato lo permite y se demuestra ingreso o costo evitado.</p>
</div>
</div>

<p class="note">Techos de autorización, no gasto esperado. Excluyen contribución facturable desplazada y facilitación externa. Un cambio de precio del proveedor exige respuesta propia; el mínimo no resuelve ese riesgo. Puertas irreversibles: decisión al cierre de M12 para el plan siguiente.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar aprendizaje con exposición presupuestaria limitada, sin presupuestar repago en el año.</span>
<span class="ref">

[Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<!-- _class: closing -->

<p class="eyebrow">Decisión del Directorio</p>

# Aprobar el plan y sus resoluciones

<p style="font-size:26px;line-height:1.4">Adoptar las resoluciones R-01 a R-32 del Anexo G: paquete mínimo, límites, techos y delegación condicionada.</p>

<div class="money">
<div><strong>8k USD</strong><p><b>Hoy, tiempo propio y caja 0.</b> Diez días hábiles de validación, con cargo a 2026.</p></div>
<div><strong>+71k USD</strong><p><b>Segunda liberación.</b> Firma el CEO solo con las condiciones de R-05. No es automática.</p></div>
<div><strong>121k USD</strong><p><b>Techo anual.</b> 79k hasta M3 y tramos de 16k, 13k y 13k. Cada gate requiere firma.</p></div>
</div>

<div class="fine">

Sin aprobación de plataforma ni construcción de producto. Todo exceso de tramo o ampliación de alcance vuelve al Directorio. Autoridad y condiciones completas: [Anexo G](annexes/07-resoluciones.md).

</div>

<div style="margin-top:auto;position:relative">
<p class="eyebrow">Equipo · Grupo 11</p>
<p style="font-size:20px;max-width:1100px">Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
<p class="fine">Plan elaborado con asistentes de IA por rol, revisión adversarial simulada y chequeos automáticos.</p>
</div>
