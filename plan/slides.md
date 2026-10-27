---
marp: true
theme: acme
paginate: true
size: 16:9
lang: es-AR
owner: caio
status: ready
---
<style>
section { font-size: 24px; }
h1 { font-size: 43px; margin-bottom: 26px; }
.lead { font-size: 28px; line-height: 1.4; margin-bottom: 30px; }
.card { padding: 24px; }
.card h3 { font-size: 28px; margin-bottom: 18px; }
.card p { font-size: 24px; line-height: 1.45; }
.ref { margin-top:auto; font-size:15px; color:var(--muted); padding-top:18px; }
.strip { background: var(--mint); border-left: 7px solid var(--green); padding: 15px 22px; margin-top: 26px; font-size: 24px; }
.steps { display:grid; grid-template-columns:repeat(4,1fr); gap:22px; margin:12px 0 24px; }
.steps > div { position:relative; background:var(--sand); padding:22px 18px; border-top:7px solid var(--green); border-radius:8px; }
.steps > div:not(:last-child)::after { content:'→'; position:absolute; right:-21px; top:92px; color:var(--green); font-size:27px; }
.steps h3 { font-size:27px; margin:10px 0 18px; }
.steps p { font-size:21px; line-height:1.4; }
.q { color:var(--rust); font-size:20px; font-weight:700; }
.flow { display:grid; grid-template-columns:repeat(4,1fr); gap:22px; margin:10px 0 25px; }
.flow > div { background:var(--sand); border-radius:8px; padding:23px 17px; font-size:25px; text-align:center; }
.flow b { display:block; color:var(--green); font-size:36px; }
.money { display:grid; grid-template-columns:1fr 60px 1fr 60px 1.3fr; gap:10px; align-items:center; margin:10px 0 20px; }
.money .box { border-top:5px solid var(--green); background:var(--sand); border-radius:8px; padding:17px 18px; min-height:180px; }
.money .box b { display:block; color:var(--rust); font-size:39px; margin-bottom:10px; }
.money .box p { font-size:21px; }
.money .sign { font-size:38px; text-align:center; color:var(--green); }
.later { display:grid; grid-template-columns:repeat(4,1fr); gap:15px; }
.later > div { border-top:2px solid var(--green-soft); padding-top:10px; font-size:20px; }
.small { font-size:19px; }
section.closing .ref { color:#dcd8c9; } section.closing > * { position:relative; z-index:1; } section .ref p { margin:0; }
section.roadmap-v2 h1 { margin-bottom:18px; } section.roadmap-v2 .steps { margin:6px 0 10px; } section.roadmap-v2 .steps > div { padding:18px; } section.roadmap-v2 .steps p { font-size:20px; } section.roadmap-v2 .strip { margin-top:16px; font-size:22px; }
section.roadmap-v3 h1 { margin-bottom:18px; }
section.roadmap-v3 .steps { margin:0 0 4px; }
section.roadmap-v3 .steps > div { padding:14px 16px; }
section.roadmap-v3 .steps h3 { font-size:25px; margin:8px 0 10px; }
section.roadmap-v3 .steps p { font-size:18px; line-height:1.3; }
section.roadmap-v3 .steps .budget { font-size:18px; font-weight:700; border-top:1px solid var(--green-soft); padding-top:8px; margin-top:10px; }
section.roadmap-v3 .strip { font-size:21px; margin-top:10px; padding:12px 18px; }
section.value-v3 .lead { font-size:25px; margin-bottom:14px; }
section.value-v3 .card h3 { font-size:25px; margin-bottom:12px; }
section.value-v3 .card p { font-size:21px; }
section.value-v3 .strip { font-size:20px; margin-top:10px; } section.value-v3 h1 { margin-bottom:18px; } section.value-v3 .card { padding:18px; }
section.closing .vote { font-size:24px; line-height:1.5; margin:15px 0; max-width:1090px; }
</style>

<!-- _class: cover -->
<!-- _paginate: false -->

<span class="chip">Grupo 11 · Diplomatura CAIO · UTN BA</span>

# Plan de Inteligencia Artificial 2027

<p class="sub">Acme Labs</p>

<p style="font-size:34px;max-width:900px;line-height:1.4;margin-top:30px">Mejorar cómo trabajamos y evolucionar lo que ofrecemos.</p>

<div class="ref">

[Anexo H — Cómo se armó el plan](annexes/08-como-se-armo.md)

</div>

---

<p class="eyebrow">El desafío del negocio</p>

# Fortalecer nuestra oferta y las relaciones con nuestros clientes

<p class="lead">Acme desarrolla software para bancos y fintechs. Ya usa IA, pero todavía no demuestra su aporte; las restricciones de los clientes condicionan cómo utilizarla.</p>

<div class="grid g2">
<div class="card dark"><h3>Mejorar lo que tenemos</h3><p>Procesos más eficientes y productos que respondan mejor a nuestros clientes estratégicos.</p></div>
<div class="card"><h3>Explorar nuevas oportunidades</h3><p>Identificar soluciones que fortalezcan la oferta y puedan atraer nuevos clientes.</p></div>
</div>

<p class="strip">Nuestra respuesta: incorporar IA para sostener la competitividad y evolucionar la oferta, protegiendo las entregas actuales.</p>

<div class="ref">

Base: [Anexo A — Diagnóstico](annexes/01-diagnostico.md). Las mejoras y oportunidades son objetivos por validar.

</div>

---

<!-- _class: roadmap-v3 -->

<p class="eyebrow">La propuesta · 12 meses de 2027</p>

# Incorporar IA por etapas, con evidencia para avanzar

<div class="steps">
<div><span class="q">Q1 · Preparar</span><h3>Crear las condiciones</h3><p>Base y controles probados. Básico ≥90%; intermedio de la cohorte.<br><strong>Habilitar Q2:</strong> base, agendas y controles listos.</p><p class="budget">Hasta USD 79 mil acumulados</p></div>
<div><span class="q">Q2 · Validar</span><h3>Probar los usos</h3><p>Medición y estudio de integración. Seguimiento de adopción.<br><strong>Continuar:</strong> uso, costo y controles; todavía no por valor.</p><p class="budget">Tramo: hasta USD 16 mil</p></div>
<div><span class="q">Q3 · Aplicar</span><h3>Comprobar el aporte</h3><p>Mejora positiva en la estimación prudente; sin daño de calidad detectado. Adopción sostenida.<br><strong>Decidir:</strong> aplicar las reglas de valor.</p><p class="budget">Tramo: hasta USD 13 mil</p></div>
<div><span class="q">Q4 · Consolidar</span><h3>Decidir la continuidad</h3><p>Evaluación y traspaso. Revisar adopción y aprendizajes.<br><strong>Decidir año 2:</strong> alcance, capacidad y costos propios.</p><p class="budget">Tramo: hasta USD 13 mil</p></div>
</div>

<p class="strip">Q3 con método viable: mejora prudente positiva → avanzar; si no acredita, estimado ≥5% y sin daño → única espera de 6 semanas; sin condiciones → cortar.</p>

<div class="ref">

[Anexo F — Roadmap y riesgo](annexes/06-roadmap-riesgo.md). Estimación prudente: piso del intervalo del 90%. Medición no viable: beneficio 0, sin expansión; continuidad por adopción, calidad, costo y controles. Techos en Recursos, sin liberación automática. Q2–Q4 sin formación ampliada.

</div>

---

<p class="eyebrow">Las iniciativas</p>

# Por dónde empezamos

<div class="grid g2">
<div class="card dark"><h3>Mejorar nuestra operación</h3><p>Aplicar IA en una tarea real para comprobar si mejoramos la entrega sin perder calidad.</p><p style="margin-top:18px"><strong>Primera prueba:</strong> resolver una falla en software propio y confirmar que la corrección funciona.</p></div>
<div class="card"><h3>Explorar nuevas soluciones</h3><p>Estudiar una ayuda para facilitar la integración de nuestros productos en los clientes.</p><p style="margin-top:18px"><strong>Primero:</strong> comprobar el problema, las alternativas y el interés comercial.</p></div>
</div>

<p class="strip">Primero estas dos: herramientas actuales y una prueba dentro de la capacidad confirmada; estudio comercial acotado, sin construir producto. Plataforma y pagos con IA se postergan.</p>

<div class="ref">

[Anexo B — Arquitectura](annexes/02-arquitectura.md) · [Anexo F](annexes/06-roadmap-riesgo.md). Ambas son propuestas por validar; documentación o soporte pueden reemplazar al asistente.

</div>

---

<p class="eyebrow">El inicio · Q1</p>

# Empezar con las herramientas que ya tenemos

<p class="lead">Con agendas confirmadas, usar las herramientas actuales en tareas habilitadas, con controles probados y revisión humana.</p>

<div class="flow">
<div><b>1</b>Trabajo del equipo</div>
<div><b>2</b>Asistencia de IA</div>
<div><b>3</b>Revisión humana</div>
<div><b>4</b>Entrega validada</div>
</div>

<div class="grid g2">
<div class="card"><h3>Antes de la práctica</h3><p>Congelar la base de comparación y habilitar cada entorno. Después, formación y prueba con las horas asignadas.</p></div>
<div class="card"><h3>Una entrega controlada</h3><p>Información autorizada, permisos acotados y validación humana. Registrar calidad y resultados; nueva plataforma, otra decisión.</p></div>
</div>

<div class="ref">

[Anexo B — Arquitectura](annexes/02-arquitectura.md). Configurar y probar es reversible; construir o ampliar alcance exige nueva aprobación.

</div>

---

<p class="eyebrow">Personas y adopción</p>

# Preparar al equipo para incorporar IA

<div class="grid g3">
<div class="card dark"><h3>Formación aplicada</h3><p>Casos de trabajo por rol, formación básica para todos e intermedia para la cohorte de prueba.</p></div>
<div class="card"><h3>Tiempo asignado</h3><p>Confirmar agendas, el trabajo que se desplaza y cómo cubrirlo antes de comenzar.</p></div>
<div class="card"><h3>Transición responsable</h3><p>Capacitar y reasignar. Durante 12 meses, la mejora por IA no se usa para desvincular.</p></div>
</div>

<p class="strip"><strong>Meta de Q1:</strong> al menos el 90% aprueba la formación básica con un caso práctico.</p>

<div class="ref">

[Anexo D — Personas y cultura](annexes/04-personas-cultura.md). Roles actuales; ampliaciones requieren aprobación propia. La regla laboral excluye causas previas ajenas a la IA; comunicarla es costoso de deshacer.

</div>

---

<p class="eyebrow">Gobierno y seguridad</p>

# Incorporar IA protegiendo la información y a nuestros clientes

<div class="grid g3">
<div class="card"><h3>Comprobar antes de usar</h3><p>Probar los controles de cada herramienta y corregir problemas críticos antes de habilitar nuevos usos.</p></div>
<div class="card dark"><h3>Definir responsabilidades</h3><p>Separar quién produce, quién verifica y quién autoriza. En producto, la persona decide y ejecuta.</p></div>
<div class="card"><h3>Actuar ante riesgos</h3><p>Seguridad puede suspender usos. Desde la aprobación se suspende el uso externo de código de clientes bajo acuerdos de confidencialidad.</p></div>
</div>

<p class="strip">Código y datos de clientes fuera de modelos externos, salvo en el entorno del cliente y con su permiso escrito.</p>

<div class="ref">

[Anexo C — Gobierno y seguridad](annexes/03-gobierno-seguridad.md) · [Anexo G — Condiciones y resoluciones](annexes/07-resoluciones.md). Sin crédito ni evaluación crediticia con IA durante los 12 meses. Transición de los demás usos de código: condiciones de G.

</div>

---

<p class="eyebrow">Recursos · Límites de autorización en USD</p>

# Empezar con tiempo interno y liberar recursos por etapas

<div class="money">
<div class="box"><b>8 mil</b><p>Validación inicial<br><strong>Tiempo interno · Caja 0</strong><br>10 días hábiles en 2026</p></div>
<div class="sign">+</div>
<div class="box"><b>71 mil</b><p>Segunda liberación<br><strong>Condicionada</strong><br>10 caja + 61 tiempo</p></div>
<div class="sign">=</div>
<div class="box"><b>79 mil</b><p>Techo acumulado hasta cerrar Q1<br><strong>10 caja + 69 tiempo</strong><br>Incluye reserva de cierre</p></div>
</div>

<div class="later">
<div><strong>Q2 · +16 mil</strong><br>2 caja + 14 tiempo</div>
<div><strong>Q3 · +13 mil</strong><br>2 caja + 11 tiempo</div>
<div><strong>Q4 · +13 mil</strong><br>2 caja + 11 tiempo</div>
<div><strong>Techo total · 121 mil</strong><br>16 caja + 105 tiempo</div>
</div>

<p class="small" style="margin-top:18px">Son techos, no gasto esperado ni desembolso inicial. El CEO libera cada tramo con verificación del CFO y controles; excesos y ampliaciones vuelven al Directorio.</p>

<p class="small"><strong>Costo estimado si continúa el mínimo todo el año: USD 27–114 mil</strong> entre caja y tiempo valorizado. Incluye preparación previa; sin esperas ni reservas gastadas.</p>

<div class="ref">

[Anexo E — Business case](annexes/05-business-case.md) · [Anexo G](annexes/07-resoluciones.md). Tiempo interno valorizado; no es caja. Excluye contribución facturable desplazada y facilitación externa.

</div>

---

<!-- _class: value-v3 -->

<p class="eyebrow">El valor buscado</p>

# Una decisión estratégica con recursos por etapas

<p class="lead">Incorporar IA es estratégico para sostener la competitividad y evolucionar la oferta. El mínimo compra <strong>controles sobre usos existentes, medición y formación.</strong></p>

<p style="font-size:24px;margin-bottom:16px"><strong>ROI económico modelado: −100% a 12 meses.</strong> Beneficios cuantificados: 0; ahorro de caja e ingreso nuevo presupuestados: 0.</p>

<div class="grid g3">
<div class="card"><h3>Adverso · Frenar</h3><p>Sin viabilidad, no iniciar Q1: hasta USD 8 mil de tiempo interno. Si una prueba falla, frenamos ese tramo; la estrategia sigue vigente.</p></div>
<div class="card dark"><h3>Base · Continuar con límites</h3><p>Sostener el mínimo solo con las condiciones de cada etapa. No financiar producto ni nueva plataforma.</p></div>
<div class="card"><h3>Favorable · Acreditar valor</h3><p>Reconocer solo mejora comprobada y sin daño detectado. Capacidad no es caja; ampliar exige otra decisión.</p></div>
</div>

<p class="strip">El riesgo de precio y consumo del proveedor requiere una evaluación propia; no queda resuelto por este mínimo.</p>

<div class="ref">

[Anexo E — Escenarios y retorno](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md). ROI del mínimo, sin beneficios cuantificados: no es pérdida de caja ni ausencia de valor. Corte o espera según F; el riesgo de no actuar no se monetiza.

</div>

---

<!-- _class: closing -->

<p class="eyebrow">Decisión solicitada</p>

# Aprobar el plan y liberar solo su validación inicial

<p style="font-size:30px;line-height:1.4;margin-top:12px"><strong>Hoy: hasta USD 8 mil de tiempo interno, caja 0.<br>Diez días hábiles de validación en 2026.</strong></p>

<p class="vote">Adoptar las resoluciones del plan y fijar los techos: <strong>USD 79 mil hasta cerrar Q1 y USD 121 mil total</strong>, con los límites por tramo presentados.</p>

<p class="vote">Delegar al CEO las liberaciones condicionadas, con verificación del CFO y dictamen del AI Council. <strong>Excesos o ampliaciones vuelven al Directorio.</strong></p>

<div class="ref">

[Anexo G — Resoluciones y condiciones completas](annexes/07-resoluciones.md). Fijar techos no libera el resto. Construcción de producto y nueva plataforma requieren otra decisión.

</div>

<p style="font-size:17px;line-height:1.5;margin-top:24px">Grupo 11 · Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
