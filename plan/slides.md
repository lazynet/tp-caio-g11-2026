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
/* Legibilidad proyectada y contraste WCAG AA, sin tocar el tema. */
section table th { background: var(--green); }
section .note { font-size: 16px; }
section .decision.block .grid { font-size: 17px; }
.cuenta { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 0 0 12px; }
.cuenta div { background: var(--sand); border-radius: 10px; padding: 6px 12px; font-size: 15px; line-height: 1.25; display: flex; align-items: center; gap: 10px; }
.cuenta b { font-family: "Caprasimo", Georgia, serif; font-weight: 400; font-size: 28px; color: var(--rust); }
.cuenta .total { background: var(--green); color: #f3efe4; }
.cuenta .total b { color: #fff; }
.cuenta .cap { grid-column: 1 / -1; display: block; background: transparent; padding: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; color: var(--muted); }
/* Estado de un punto de decisión. Ratios WCAG: pasa 6,25:1, espera 4,67:1, corta 6,23:1. */
.st { display: inline-block; border-radius: 999px; padding: 2px 10px; font-size: 15px; font-weight: 700; white-space: nowrap; }
.st.pasa { background: var(--green); color: #fff; }
.st.espera { background: var(--orange); color: var(--ink); }
.st.corta { background: var(--rust); color: #fff; }
.semaforo table { font-size: 16px; }
.semaforo td:first-child { width: 110px; }
.pedido { font-size: 22px; color: #f3efe4; margin: 4px 0 0; }
/* Tamaños mínimos del texto clave y contraste no-texto (WCAG 1.4.11). */
section .card.dashed .tag { color: #5e574e; }
section .dots .on { color: var(--rust); }
section .dots .off { color: var(--muted); }
section .decision .ref a::after { content: " →"; }
.alts tbody tr:first-child td, .alts tbody tr:first-child td:first-child { background: var(--mint); font-weight: 700; }
.alts td:last-child { white-space: nowrap; }
section .alts table { font-size: 16px; }
section .alts table td, section .alts table td:first-child { padding: 6px 12px; }
.roadmap table { font-size: 14.5px; }
.roadmap tbody tr:nth-child(3) td { font-size: 17px; line-height: 1.3; }
.roadmap tbody tr:nth-child(4) td { font-size: 15.5px; line-height: 1.25; }
.roadmap td:first-child { width: 112px; }
.escalera-wrap { display: grid; grid-template-columns: 1.75fr 1fr; gap: 26px; align-items: end; margin: 0 0 10px; }
.leyenda { display: flex; gap: 18px; font-size: 15px; margin: 0 0 6px; color: var(--ink); }
.leyenda i { display: inline-block; width: 16px; height: 14px; vertical-align: -2px; margin-right: 6px; }
.sw-hoy { background: var(--green); }
.sw-no { background: var(--sand); border: 2px solid var(--muted); }
.sw-g { background: var(--rust); }
.escalera { display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; align-items: end; }
.escalera .col { display: flex; flex-direction: column; text-align: center; }
.escalera .v { font-size: 17px; line-height: 1.15; margin: 0 0 4px; white-space: nowrap; }
.escalera .v b { font-family: "Caprasimo", Georgia, serif; font-weight: 400; font-size: 26px; color: var(--rust); }
.escalera .bar { margin: 0 22px; display: flex; flex-direction: column; }
.escalera .g { background: var(--rust); border-bottom: 2px solid var(--cream); }
.escalera .t { background: var(--green); }
.escalera .no .t { background: var(--sand); border: 2px solid var(--muted); border-bottom: 0; }
.escalera .x { border-top: 2px solid var(--ink); padding-top: 5px; font-size: 16px; line-height: 1.25; height: 46px; }
.pedido b { font-family: "Caprasimo", Georgia, serif; font-weight: 400; font-size: 34px; color: #fff; }
</style>

<!-- Fuente única del deck. Nunca edites un deck generado: corré scripts/build-deck.sh.
     Una slide por `---`, con un título `#` cada una. Máximo 10 slides. Arco:
     propósito → oportunidad → plan → ejecución → recursos → decisión. Borrador del CAIO: toda
     cifra viene de un anexo y de una fuente. El pedido completo se resume en la
     slide 10; la 9 muestra su exposición presupuestaria máxima autorizada. Diseño: plan/theme/acme.css; los bloques
     HTML llevan Markdown adentro, separado por líneas en blanco, y los links siguen en
     Markdown. -->

<!-- _class: cover -->
<!-- _paginate: false -->

<div class="sun"></div>

<span class="chip">Grupo 11 · Diplomatura CAIO · UTN BA</span>

# Plan de Inteligencia Artificial 2027

<p class="sub"><strong>Acme Labs</strong></p>

<p style="font-size:30px;line-height:1.35;max-width:850px">Incorporación progresiva de IA en la operación y en los productos</p>

<p style="max-width:820px">Preparar a la organización, probar aplicaciones y avanzar según sus resultados.</p>

<p class="fine">Propuesta al Directorio · 12 meses · Cifras estimadas, sujetas a validación</p>

<p class="fine">El pedido: aprobar el plan y sus resoluciones R-01 a R-32 del Anexo G. No presupuestamos repago en el año. Montos en k USD (miles de dólares).</p>

---

<p class="eyebrow">01 · Oportunidad de negocio</p>

# Mejorar la entrega y evolucionar la oferta

<p style="font-size:26px;line-height:1.4">Acme desarrolla software para bancos y fintechs. Proponemos aplicar IA en dos frentes: <strong>mejorar la capacidad y calidad de sus entregas</strong> y <strong>evaluar nuevas funcionalidades para sus clientes</strong>.</p>

<div class="plain" style="margin-top:18px">

Ya utiliza IA en desarrollo interno, pero no mide su aporte contra una base. El plan ratifica la política vigente; su aplicación debe verificarse.

<strong>83–90% de las horas ya se facturan:</strong> el plan debe mejorar la entrega sin desplazar trabajo a ciegas. <strong>40–50% de la facturación depende de un cliente:</strong> cuidar sus restricciones es parte de proteger el negocio.

</div>

<p class="note">Rangos anonimizados del diagnóstico, a confirmar en la validación. Competitividad es el objetivo; la mejora y su conversión en ingresos todavía deben demostrarse.</p>

<div class="decision">
<span class="pill">Propósito</span>
<span class="body">Fortalecer la competitividad: mejorar cómo trabajamos y decidir dónde evolucionar lo que vendemos.</span>
<span class="ref">

[Anexo A — Diagnóstico](annexes/01-diagnostico.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>


---

<p class="eyebrow">02 · Propuesta</p>

# Cuatro etapas para incorporar IA

<p><strong>Resultado buscado:</strong> demostrar mejoras de capacidad con calidad y decidir qué aplicaciones conviene continuar o ampliar.</p>

<style scoped>
.phase-flow { display:flex; align-items:stretch; gap:0; margin:24px 0 18px; }
.phase { flex:1; min-width:0; background:#eadbc6; border-top:7px solid #8b9d6d; border-radius:8px; padding:18px 16px; box-sizing:border-box; }
.phase:nth-of-type(3) { border-top-color:#738654; }
.phase:nth-of-type(5) { border-top-color:#56683d; }
.phase:nth-of-type(7) { border-top-color:#3d472b; }
.phase-month { font-size:16px; font-weight:700; text-transform:uppercase; color:#56683d; margin:0 0 9px; }
.phase h3 { font-size:27px; line-height:1.1; margin:0 0 14px; color:#3d472b; }
.phase p { font-size:20px; line-height:1.38; margin:0; }
.phase-arrow { align-self:center; width:30px; flex:0 0 30px; text-align:center; font-size:31px; font-weight:700; color:#56683d; }
</style>

<div class="phase-flow">
<div class="phase">
<div class="phase-month">Meses 1–3</div>
<h3>Preparar</h3>
<p>Base de comparación, controles, formación y prueba con las herramientas actuales.</p>
</div>
<div class="phase-arrow">→</div>
<div class="phase">
<div class="phase-month">Meses 4–6</div>
<h3>Validar</h3>
<p>Medir mejoras internas y estudiar una necesidad de cliente. Construir producto requiere otra decisión.</p>
</div>
<div class="phase-arrow">→</div>
<div class="phase">
<div class="phase-month">Meses 7–9</div>
<h3>Aplicar</h3>
<p>Continuar usos con evidencia. Producto solo con necesidad validada, señal comercial, solución costeada y nueva autorización.</p>
</div>
<div class="phase-arrow">→</div>
<div class="phase">
<div class="phase-month">Meses 10–12</div>
<h3>Consolidar</h3>
<p>Evaluar resultados y adopción. Definir qué continúa, se transfiere o se detiene.</p>
</div>
</div>

<p class="note"><strong>Antes de iniciar:</strong> diez días hábiles de validación del diagnóstico, las agendas y la viabilidad, con liberación propia en 2026 (R-02). No se presupuestan ahorros de caja ni ingresos nuevos; el producto no está garantizado.</p>

<div class="decision">
<span class="pill">Criterio</span>
<span class="body">El paso a cada etapa requiere evidencia, seguridad aceptable y autorización de recursos.</span>
<span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo E](annexes/05-business-case.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>


---

<p class="eyebrow">03 · Iniciativas y prioridad</p>

# Mejorar la operación y validar una oportunidad de producto

<div class="grid g2">
<div class="card dark">
<h3>Operación: primera aplicación</h3>
<p>Formación aplicada, controles y mejores prácticas con las herramientas actuales. Medir cambios de código aceptados por el equipo, en agregados por área y semana contra su base; revisar primero retrabajo e incidentes.</p>
<p>Capacidad liberada no equivale a caja: solo se convierte en dinero si se vende o evita una contratación y eso se demuestra.</p>
</div>
<div class="card">
<h3>Oferta: una hipótesis a investigar</h3>
<p>El asistente de integración ayudaría al cliente a conectar con la plataforma: encontrar funciones, preparar llamadas y entender errores con documentación y datos sintéticos.</p>
<p>Antes del mes 6: problema medido y un cliente con presupuesto que acepte por escrito evaluar en sandbox y un rango de precio, sin compra comprometida. El mínimo financia el estudio; construir requiere nuevo costeo y autorización.</p>
</div>
</div>

<p class="note">El Anexo F compara además funciones en medios de pago, servicios de agentes de código y continuar solo con eficiencia. Son alternativas de respaldo, no proyectos aprobados ni exploración amplia financiada. El mínimo anual se estima en ≈71 mil USD (27–114); los otros alcances no son precios equivalentes (R-28).</p>

<p class="note">M6 no lee valor. M9 pasa con el piso del intervalo de 90% >0 y sin daño: se acredita ese piso. Calidad es guardia de daño. Con menos de 15 personas o medición no viable según B/R-14, ninguna lectura decide por valor: beneficio 0, sin expansión; continuidad por adopción, calidad, costo y controles.</p>

<div class="decision"><span class="pill">Prioridad</span><span class="body">Primero capacidad con calidad; producto solo si la necesidad y la viabilidad justifican una decisión propia.</span><span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md) · [Anexo G](annexes/07-resoluciones.md)

</span></div>

---

<p class="eyebrow">Arquitectura</p>

# Empezar con la tecnología que ya tenemos

<p style="font-size:17px">Llamamos <strong>herramienta</strong> a cada lugar donde se usa IA: editor de código, agente de código, chat y suite de oficina. Cada una prueba sus propios controles.</p>

<div class="chips">
<span>Configurar lo que ya pagamos antes de comprar o construir</span>
<span>Acotar permisos y conectores de IA, y escanear secretos en cada herramienta</span>
<span>Medir de forma repetible: cambios aceptados, fallas de prueba automática, reversiones e incidentes</span>
<span>Mantener los controles de cada herramienta, aunque haya pasarela central</span>
<span class="hot">Código o datos de un cliente: fuera de modelos externos, salvo en su entorno y con su permiso escrito</span>
</div>

<div class="grid g3">
<div class="card dark">
<h3>Meses 1-3, tras la validación</h3>
<p>Con las herramientas actuales: configuración, registro de uso, base de medición y prueba de prácticas de trabajo con IA.</p>
</div>
<div class="card">
<h3>Plataforma: condiciones</h3>
<p>Señal contractual, de precio o producto, más: <strong>1</strong> brecha documentada, <strong>2</strong> alternativas comparables, <strong>3</strong> economía incremental o aprendizaje con pérdida aceptada y límite declarado, <strong>4</strong> capacidad demostrada.</p>
</div>
<div class="card dashed">
<h3>No se aprueba todavía</h3>
<p>Pasarela central, plataforma para agentes, modelo propio y contratos de más de 12 meses. Nada pasa al año 2 por defecto.</p>
</div>
</div>

<div class="decision">
<span class="pill">Resoluciones R-08 · R-11 · R-15 · R-16</span>
<span class="body">M1-3 tras la validación, con controles probados por herramienta. Plataforma: señal y condiciones 1-4; dictamina el comité de IA, libera el Directorio.</span>
<span class="ref">

[Anexo B — Arquitectura](annexes/02-arquitectura.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>

---

<p class="eyebrow">Personas</p>

# De uso individual a capacidad de equipo

<div class="grid g2">
<div>
<div class="card">
<p class="eyebrow" style="color:var(--muted)">Tiempo que pedimos reservar en los meses 1-3</p>
<div class="grid g2" style="margin:6px 0">
<div class="kpi"><div class="num">720 h</div><div class="lbl">de personas clave para sostener el plan (1,5 personas a tiempo completo)</div></div>
<div class="kpi"><div class="num">660 h</div><div class="lbl">de formación, como máximo</div></div>
</div>
<p style="font-size:17px">Demanda de actividades: 970-1.346 h; con verificación M3: 974-1.351 h (R-25). Solapes adoptados (R-26), sujetos a validación real. La reserva no es disponibilidad: confirmar agendas y recostear antes de la segunda liberación, sin subir el techo.</p>
</div>
<div class="card dashed" style="margin-top:12px">
<span class="tag">Resolución R-20 · costosa de deshacer una vez comunicada</span>
<p><strong>Empleo:</strong> en 12 meses la mejora por IA no se usa para desvincular; primero se reasigna y se capacita. Quedan afuera causas previas ajenas a la IA.</p>
</div>
</div>
<div>

- **Formación:** básica para todos; intermedia para un grupo de 15-20.
- **Por qué casos por rol:** en el piloto de abril de 2026 (12 voluntarios), el 92% usó la herramienta 3 o más días por semana y el índice de recomendación (NPS) dio +42, pero solo 2 de 12 (17%) terminaron los cursos. El freno fue el tiempo: formamos con casos reales, en horario laboral.
- **Metas de uso (R-23):** Tecnología ≥80% en M6 y ≥85% en M12. Operaciones: sin meta M6; ≥40% en M9 y ≥60% en M12 sobre personas habilitadas, solo con programa ampliado costeado y autorizado por el Directorio en M6. El combinado original se informa aparte: no llega al 80% del borrador 2027; en M3 el Directorio decide si revisa ese objetivo.

</div>
</div>

<div class="decision">
<span class="pill">Resoluciones R-20 · R-22</span>
<span class="body">No ampliar nómina; toda incorporación externa es excepción del Directorio, con caja propia. Si no hay perfil interno para el curso básico: una intervención de 16-32 h que reemplaza esas horas, con cotización.</span>
<span class="ref">

[Anexo D — Personas y cultura](annexes/04-personas-cultura.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>


---

<p class="eyebrow">Gobierno y seguridad</p>

# Cada uso tiene límites y alguien que responde

<style scoped>.decision.block { margin-top: 16px; }</style>

<div class="grid g3">
<div class="kpi"><div class="num">5</div><div class="lbl">miembros en el comité de IA, dentro del comité de tecnología: revisa todos los meses y puede cortar</div></div>
<div class="kpi"><div class="num">Separados</div><div class="lbl">producir la evidencia, verificarla y firmar cada punto de decisión; quien produjo o verificó no vota su aceptación</div></div>
<div class="kpi"><div class="num">Autonomía 2</div><div class="lbl">tope de la IA en el producto por 12 meses (escala de autonomía 0-4: 0 sin IA, 4 autónoma): prepara, y una persona decide y ejecuta</div></div>
</div>

<p class="eyebrow" style="margin:18px 0 6px">Cada control responde a un contrato, un riesgo o una evidencia que falta: así se habilita cada herramienta</p>

<div class="grid g3">
<div class="card"><h3>1 · Probar</h3><p>Mandamos un secreto falso para ver si se filtra, simulamos un ataque y exigimos revisión humana.</p></div>
<div class="card"><h3>2 · Habilitar</h3><p>Con los problemas graves corregidos y el riesgo restante aceptado por escrito por quien corresponde. Lo que no pasa, no se usa.</p></div>
<div class="card"><h3>3 · Vigilar</h3><p>Seguridad puede suspender un uso en cualquier momento, aunque gasto y adopción vayan bien.</p></div>
</div>

<div class="decision block">
<div class="decision-head"><span class="pill">Resoluciones R-07 · R-08 · R-09 · R-11</span><span class="ref">

[Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md) · [Anexo G](annexes/07-resoluciones.md)

</span></div>
<div class="grid g3">
<div><strong>1.</strong> Ratificar la política; versión y alcance asentados antes de la segunda liberación, aplicación verificada en M3. Cambios: Directorio. Uso nuevo o ampliado: prueba previa en su herramienta.</div>
<div><strong>2.</strong> Sin crédito ni scoring con IA por 12 meses: límite del plan mientras maduran los controles. La clasificación normativa se hace caso por caso.</div>
<div><strong>3.</strong> Al aprobar: suspender código bajo NDA y usos prohibidos por contrato. Solo código sin NDA ya en uso: residual del comité hasta M3, sin ampliar; datos excluidos. Nuevo uso: matriz y permiso escrito. Desde M3 rige R-08.</div>
</div>
</div>


---

<p class="eyebrow">Roadmap técnico, financiero y cultural</p>

# Un recorrido con resultados y recursos por etapa

<div class="cuenta">
<div class="cap">Lo que pedimos liberar por etapa, en k USD</div>
<div><b>8k</b><span>Hoy: validación en 2026, 10 días hábiles. Caja 0 + tiempo 8</span></div>
<div><b>68k</b><span>Segunda liberación, con evidencia: meses 1-3. Caja 9 + tiempo 59</span></div>
<div><b>3k</b><span>En esa decisión: reservas para cerrar si cortamos. Caja 1 + tiempo 2</span></div>
<div class="total"><b>79k</b><span>Techo hasta el mes 3, fijado hoy. Caja 10 + tiempo 69</span></div>
</div>

<div class="roadmap">

| | Meses 1-3 | Meses 4-6 | Meses 7-9 | Meses 10-12 |
|---|---|---|---|---|
| Técnico y gobierno | Base de medición, política y controles | Controles y medición; estudio del asistente, sin construirlo | Controles y medición; producto solo con otra decisión y costeo | Evaluación y traspaso |
| Cultural | Básico (≥90% aprobado con caso práctico); intermedio, 15-20 | Seguimiento de uso, sin cursos nuevos | Seguimiento de uso | Metas propuestas, informadas |
| Techo, k USD | **caja 9 · tiempo 59** | **16**: caja 2 · tiempo 14 | **13**: caja 2 · tiempo 11 | **13**: caja 2 · tiempo 11 |
| Punto de decisión | <span class="st pasa">Pasa</span> base, política y controles probados; gasto dentro del techo | <span class="st pasa">Sigue</span> adopción, costo y controles; no lee valor<br><span class="st corta">Corta</span> daño o caída demostrada | <span class="st pasa">Pasa</span> peor caso >0%, sin daño<br><span class="st espera">Espera</span> Estimado ≥+5%, sin pasar | Año 2: otra decisión, con costeo propio; no pasa por defecto |

</div>

<p class="note" style="margin-top:2px">Caja: legal/herramientas; tiempo: personas propias. Producto, plataforma y cursos nuevos: otro costeo y decisión. Espera única M9: 6 semanas sin ampliar, firma el CEO; daño o estimado &lt;+5% sin pasar, o espera vencida sin pasar: corta. Medición no viable: B/R-14 y F. Adopción sola no libera fondos.</p>

<div class="decision">
<span class="pill">R-03 · R-04 · R-05 · R-27</span>
<span class="body">Hoy: fijar techos y liberar 8k. Bajo R-05, el CEO libera hasta 71k más (68 + 3) y firma gates dentro de cada tramo: 79k, +16k, +13k, +13k = 121k. Superar un tramo vuelve al Directorio.</span>
<span class="ref">

[Anexo F — Roadmap](annexes/06-roadmap-riesgo.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>


---

<p class="eyebrow">Costo y riesgo</p>

# Cuánto arriesgamos como máximo, y dónde frenamos

<p style="font-size:17px;margin:0 0 8px"><strong>Techo:</strong> máximo autorizado. <strong>Costo estimado:</strong> gasto esperado. Hoy se liberan 8k USD; el CEO libera hasta 71k más bajo R-05 (ver Roadmap). Si todo pasa: mínimo sin plataforma, estimado <span style="white-space:nowrap">≈71k USD (27-114)</span>, techo anual 121k (118k sin usar reservas). Financia base, medición y controles para decidir el año 2; ingreso presupuestado 0.</p>

<div class="escalera-wrap">
<div>
<div class="leyenda"><span><strong>k USD</strong></span><span><i class="sw-hoy"></i>Se fija y se libera hoy</span><span><i class="sw-no"></i>Techo fijado hoy, no se libera hoy</span><span><i class="sw-g"></i>Guardia hasta el mes 12</span></div>
<div class="escalera">
<div class="col"><div class="v"><b>8</b></div><div class="bar"><div class="t" style="height:10px"></div></div><div class="x"><strong>La validación</strong><br>caja 0</div></div>
<div class="col no"><div class="v"><b>79</b> +6 = 85</div><div class="bar"><div class="g" style="height:9px"></div><div class="t" style="height:95px"></div></div><div class="x"><strong>Mes 3</strong><br>caja 10</div></div>
<div class="col no"><div class="v"><b>95</b> +4 = 99</div><div class="bar"><div class="g" style="height:6px"></div><div class="t" style="height:114px"></div></div><div class="x"><strong>Mes 6</strong><br>caja 12</div></div>
<div class="col no"><div class="v"><b>108</b> +2 = 110</div><div class="bar"><div class="g" style="height:3px"></div><div class="t" style="height:130px"></div></div><div class="x"><strong>Mes 9</strong><br>caja 14</div></div>
<div class="col no"><div class="v"><b>121</b> +0 = 121</div><div class="bar"><div class="t" style="height:146px"></div></div><div class="x"><strong>Mes 12</strong><br>caja 16</div></div>
</div>
</div>
<div>

<p class="note" style="margin:0 0 8px"><strong>Cortes inmediatos M3/M6/M9:</strong> techo hasta cerrar + guardia = exposición anual. Guardia: accesos, incidentes y permisos, caja 0 y tiempo 2k por trimestre restante; se aprueba al cortar.</p>

<p class="note" style="margin:0">Caja estimada hasta M3: 2,3-8,6k USD. El resto es tiempo propio, sin nómina nueva ni deuda; puede desplazar trabajo facturable, cuya contribución está sin medir. Con beneficio 0, ROI a 12 meses = (capacidad liberada − caja − tiempo) / (caja + tiempo) = −100%, por construcción.</p>

</div>
</div>

<p class="note" style="margin:0 0 8px"><strong>Espera M9 que vence:</strong> 108 + 7 = 115 hasta cerrar; +1 de guardia = <strong>116 anual</strong>. Subtramo: caja 1 + tiempo 6, sustituye continuidad dentro de M10–M12; reserva de cierre usada una sola vez (R-27).</p>

<p style="font-size:17px;margin:0 0 10px"><strong>Irreversibles, no aprobados (desde M12):</strong> código/datos de clientes a modelos externos; contratos de IA con clientes; IA que ejecuta en producto, aun con aprobación humana; compromisos >12 meses. <strong>No actuar:</strong> septiembre: agente de código ~12× lo pagado a precio API, no facturado. Con cobro por consumo e igual uso: 211-267k USD extra/año, con o sin plan. Escenario, no pronóstico; mínimo y pasarela sola no lo cubren.</p>

<div class="decision">
<span class="pill">Resolución R-03</span>
<span class="body">Techos: 79k hasta M3 (8 + 71), 85k con guardia; anual 121k (+16, +13, +13). Estimado hasta M3: 18-73k USD. Excluye contribución facturable desplazada y facilitación externa.</span>
<span class="ref">

[Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md) · [Anexo G](annexes/07-resoluciones.md)

</span>
</div>


---

<!-- _class: closing -->

<style scoped>h1 { font-size: 50px; } .fine, .fine p { color: #dcd8c9; }</style>

<p class="eyebrow">Mejorar la entrega · evolucionar la oferta · avanzar con evidencia</p>

# Aprobar el plan y sus resoluciones

<p style="font-size:22px;line-height:1.4;max-width:1100px;color:#f3efe4">Al aprobar el plan, el Directorio adopta las resoluciones R-01 a R-32 del Anexo G. Libera hoy 8k USD de tiempo de personas propias, sin caja: 10 días hábiles de validación en 2026, con cargo al presupuesto 2026. Fija los techos: 79k USD hasta el mes 3 y 121k USD en el año, con 16k, 13k y 13k por tramo. Delega en el CEO la segunda liberación, de hasta 71k USD, solo con las condiciones de R-05, y la firma de los puntos de decisión de los meses 3, 6, 9 y 12 dentro del techo de cada tramo. Lo que supere el techo de un tramo o amplíe el alcance vuelve al Directorio.</p>

<p class="pedido"><b>8k</b> hoy &nbsp;→&nbsp; <b>+71k</b> con la segunda liberación &nbsp;→&nbsp; <b>79k</b> de techo hasta el mes 3 &nbsp;·&nbsp; USD (ver Roadmap)</p>

<div class="grid g2" style="margin-top:auto;position:relative">
<div>
<p class="eyebrow">Equipo · Grupo 11</p>
<p>Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
<div class="fine">

Quién produce, verifica y firma cada punto de decisión, por rol: [Anexo G — Resoluciones del Directorio](annexes/07-resoluciones.md).

</div>
</div>
<div class="fine" style="max-width:340px">
<p>79k USD es un techo de autorización, no gasto esperado ni salida de caja, y no incluye la contribución del trabajo facturable que pueda desplazar, sin medir. Plataforma y producto se vuelven a costear antes de decidirlos. Cifras estimadas, a confirmar con fuentes internas.</p>
<p>Hicimos este plan con IA: un asistente por rol, una revisión adversarial simulada y chequeos automáticos de fuentes y de datos privados.</p>
</div>
</div>
