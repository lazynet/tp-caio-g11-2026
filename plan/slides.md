---
owner: caio
status: draft
marp: true
theme: acme
paginate: true
size: 16:9
---

<!-- Fuente única del deck. Nunca edites un deck generado: corré scripts/build-deck.sh.
     Una slide por `---`, con un título `#` cada una. Máximo 10 slides. Arco:
     problema → beneficio → alternativas → costo → resolución. Borrador del CAIO: toda
     cifra viene de un anexo y de una fuente. La cuenta del pedido (preparación +
     meses 1-3 + reservas = 79) vive completa solo en la slide 8; la 9 (salidas) y la 10
     (cierre) la citan: si cambia, cambian las tres. Código de estado: .st pasa (verde),
     espera (naranja de fondo) y corta (óxido), siempre con la palabra escrita. Escrito para un board que no leyó el caso: sin jerga ni
     siglas sin explicar. Diseño: plan/theme/acme.css; los ajustes de legibilidad del
     bloque <style> de abajo valen para todo el deck. Los bloques HTML llevan Markdown
     adentro, separado por líneas en blanco, y los links siguen en Markdown. -->

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
.st { display: inline-block; border-radius: 999px; padding: 2px 10px; font-size: 13.5px; font-weight: 700; white-space: nowrap; }
.st.pasa { background: var(--green); color: #fff; }
.st.espera { background: var(--orange); color: var(--ink); }
.st.corta { background: var(--rust); color: #fff; }
.semaforo table { font-size: 16px; }
.semaforo td:first-child { width: 110px; }
.pedido { font-size: 22px; color: #f3efe4; margin: 4px 0 0; }
.pedido b { font-family: "Caprasimo", Georgia, serif; font-weight: 400; font-size: 34px; color: #fff; }
</style>

<!-- _class: cover -->
<!-- _paginate: false -->

<div class="sun"></div>

<span class="chip">Grupo 11 · Diplomatura Chief AI Officer (CAIO) · UTN BA</span>

# Medir el valor antes de ampliar la inversión

<p class="sub">Plan Maestro del CAIO, el responsable de IA, para <strong>Acme Labs</strong>, software para bancos, fintechs y grandes empresas</p>

<p class="eyebrow">Plan 2027: doce meses de IA en la operación y en el producto, con la plata liberada por etapas</p>

<p style="max-width:820px">Hoy la IA se usa, pero nadie midió cuánto valor agrega. Proponemos empezar por lo mínimo que permite medirlo, con controles de seguridad probados y las herramientas que ya pagamos, y ampliar solo con evidencia.</p>

<p class="fine">Cifras estimadas, a confirmar con datos internos en una validación de 10 días hábiles que se hace en 2026, antes de que arranque el plan. No presupuestamos repago en el año: pedimos lo que estamos dispuestos a arriesgar para medir, no lo que esperamos ganar.</p>

---

<p class="eyebrow">01 · Problema</p>

# Usamos IA, pero no sabemos cuánto rinde

<div class="grid main-side">
<div class="plain">

| Dimensión (escala 1 a 5) | Nivel estimado | Lo que lo explica |
|---|---|---|
| Estrategia | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Hay iniciativas, sin estrategia formal aprobada |
| Datos e infraestructura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Hay inventario; datos repartidos; integración sin validar |
| Talento y cultura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Uso y cursos sueltos; sin formación por rol con seguimiento |
| Gobierno | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Política aprobada; falta verificar que se aplique |
| Adopción y valor | Interno: 2<br>Producto: 1 | IA en el desarrollo interno, no en el producto; nada medido contra una base |

</div>
<div class="grid" style="gap:10px">
<div class="card kpi"><div class="num">40-50%</div><div class="lbl">de la facturación viene de un solo cliente: usar IA con sus datos es un riesgo comercial, no solo técnico</div></div>
<div class="card kpi"><div class="num">83-90%</div><div class="lbl">de las horas ya se facturan: cada hora que el plan use compite con trabajo vendido</div></div>
</div>
</div>

<p style="font-size:17px;margin-top:6px">1 = inicial, 3 = operacional, 5 = transformacional; 2 = hay piezas del 3 sin formalizar ni medir. Los niveles y las cifras salen de fuentes con fechas distintas: son estimaciones que la validación confirma o corrige. Lo que no está en duda es que el valor no se mide.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Autorizar 10 días hábiles para confirmar diagnóstico, cifras y agendas antes de arrancar los meses 1-3 del plan.</span>
<span class="ref">

[Anexo A — Diagnóstico](annexes/01-diagnostico.md)

</span>
</div>

---

<p class="eyebrow">02 · Beneficio</p>

# Lo que compramos es capacidad con calidad, medida

<div class="grid g3">
<div class="card dark">
<span class="tag">Beneficio principal</span>
<h3>Más trabajo entregado, sin perder calidad</h3>
<p>Cambios de código aceptados por persona, contra una base tomada antes de empezar. Retrabajo e incidentes se miran primero.</p>
</div>
<div class="card">
<span class="tag">En el presupuesto</span>
<h3>Beneficio de caja: 0, por diseño</h3>
<p>La capacidad liberada es plata solo si se vende o evita una contratación, y eso se demuestra, no se supone.</p>
</div>
<div class="card dashed">
<span class="tag">Hipótesis, no beneficio</span>
<h3>Asistente para integrar clientes</h3>
<p>Sin un problema medido antes del mes 6 y sin interés escrito de un cliente, no se construye.</p>
</div>
</div>

<p class="eyebrow" style="margin:14px 0 2px">Cómo se lee la mejora medida en los meses 6 y 9</p>

<div class="semaforo">

| | Mes 6 | Mes 9 |
|---|---|---|
| <span class="st pasa">Pasa</span> | ≥ +3% en el peor caso, sin daño | ≥ +8% en el peor caso, sin daño |
| <span class="st espera">Espera</span> | Estimado > 0%, sin pasar | Estimado ≥ +5%, sin pasar (a ratificar) |
| <span class="st corta">Corta</span> | Estimado ≤ 0%, o daño | Estimado < +5%, o daño |

</div>

<p class="note">Estimado: la mejora medida. Peor caso: el piso de su margen estadístico. Espera: seis semanas más, sin ampliar; si no pasa, se corta. Daño: más retrabajo o más incidentes. Es exigente a propósito: con la mejora que estimamos (+3,75%, ±3 puntos) el peor caso da +0,75% y no pasa.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar capacidad con calidad como el beneficio a medir, sin presupuestar caja ni ingreso.</span>
<span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">03 · Alternativas</p>

# Empezamos por lo mínimo que permite medir

<div class="grid main-side">
<div class="card dark">
<span class="tag">El paquete mínimo</span>
<h3>Saber si hay valor, con controles probados</h3>
<p>Formación básica para todos e intermedia para un grupo de 15-20, controles de seguridad por herramienta, medición contra una base y estudio del asistente para clientes. Con lo que ya pagamos, sin plataforma nueva.</p>
<p><strong>Lo que se pide hoy no es el año:</strong> son 8 para validar y, con evidencia, un techo de 79 hasta el mes 3 (slide 8). Si todo pasa, el año completo tiene un costo estimado de ≈70 (27-113) y un techo de 121 (slide 9); no se aprueba hoy.</p>
</div>
<div class="plain">

| Otros alcances | Miles de USD |
|---|---|
| Piloto sobre el agente de código actual, sin formación general ni revisión legal | 47 |
| Gobierno y formación desde el inicio | 161 |
| Paquete completo si no aparece interés de clientes | ≈199 |
| Plataforma, sin producto | 394 |
| Plataforma, con producto | 471 |

</div>
</div>

<p style="font-size:17px;margin-top:4px">No es una comparación de precios: cada alcance compra cosas distintas. El piloto de 47 es más barato porque deja afuera la formación general y la revisión legal.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Empezar por el paquete mínimo. Ninguna proyección anual queda aprobada como presupuesto.</span>
<span class="ref">

[Anexo E — Business case](annexes/05-business-case.md)

</span>
</div>

---

<p class="eyebrow">04 · Arquitectura</p>

# Lo mínimo que pase las pruebas, con lo que ya pagamos

<p style="font-size:17px">Llamamos <strong>herramienta</strong> a cada lugar donde se usa IA: editor de código, agente de código, chat y suite de oficina. Cada una prueba sus propios controles.</p>

<div class="chips">
<span>Configurar lo que ya pagamos antes de comprar o construir</span>
<span>Permisos y conectores de IA acotados, y escaneo de secretos en cada herramienta</span>
<span>Medición repetible: cambios aceptados, fallas de prueba automática, reversiones e incidentes</span>
<span>Una pasarela central no reemplaza los controles de cada herramienta</span>
<span class="hot">Sin datos reales de clientes en los modelos durante 12 meses</span>
</div>

<div class="grid g3">
<div class="card dark">
<h3>Meses 1-3, tras la validación</h3>
<p>Con las herramientas actuales: configuración, registro de uso, base de medición y prueba de prácticas de trabajo con IA.</p>
</div>
<div class="card">
<h3>Meses 3, 6 y 9: ¿plataforma?</h3>
<p>Hoy alcanza con una señal: un contrato, un cambio de precio del proveedor o un cliente interesado. Proponemos exigir además: <strong>1</strong> brecha documentada, <strong>2</strong> alternativas comparables, <strong>3</strong> números que cierren o pérdida aceptada, <strong>4</strong> capacidad demostrada.</p>
</div>
<div class="card dashed">
<h3>No se aprueba todavía</h3>
<p>Pasarela central, plataforma para agentes, modelo propio y contratos de más de 12 meses. Nada pasa al año 2 por defecto.</p>
</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Arrancar los meses 1-3 solo después de la validación. Decidir si la plataforma exige, además de una señal, las condiciones 1 a 4.</span>
<span class="ref">

[Anexo B — Arquitectura](annexes/02-arquitectura.md)

</span>
</div>

---

<p class="eyebrow">05 · Gobierno y seguridad</p>

# Controles probados antes de usar

<div class="grid g3">
<div class="kpi"><div class="num">5</div><div class="lbl">miembros en el comité de IA, dentro del comité de tecnología: revisa todos los meses y puede cortar</div></div>
<div class="kpi"><div class="num">3 roles</div><div class="lbl">distintos en cada punto de decisión: quien produce la evidencia, quien la verifica y quien firma</div></div>
<div class="kpi"><div class="num">Nivel 2</div><div class="lbl">tope de la IA en el producto por 12 meses, en una escala de autonomía de 0 (sin IA) a 4 (autónoma): prepara, y una persona decide y ejecuta</div></div>
</div>

<p class="eyebrow" style="margin:18px 0 6px">Sin plataforma central, la política sola no alcanza: así se habilita cada herramienta</p>

<div class="grid g3">
<div class="card"><h3>1 · Probar</h3><p>Mandamos un secreto falso para ver si se filtra, simulamos un ataque y exigimos revisión humana.</p></div>
<div class="card"><h3>2 · Habilitar</h3><p>Con los problemas graves corregidos y el riesgo restante aceptado por escrito por quien corresponde. Lo que no pasa, no se usa.</p></div>
<div class="card"><h3>3 · Vigilar</h3><p>Seguridad puede suspender un uso en cualquier momento, aunque gasto y adopción vayan bien.</p></div>
</div>

<div class="decision block">
<div class="decision-head"><span class="pill">Decisiones</span><span class="ref">

[Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md)

</span></div>
<div class="grid g3">
<div><strong>1.</strong> Aplicar la política de IA ya aprobada desde el mes 1. Cambiarla lo decide la dirección de Acme Labs, no este plan.</div>
<div><strong>2.</strong> Nada de IA en crédito ni en scoring durante 12 meses: como vendemos a bancos y fintechs, son los usos de mayor riesgo regulatorio. El resto se clasifica caso por caso.</div>
<div><strong>3.</strong> Ningún uso nuevo sin prueba previa en su herramienta. Si un contrato con un cliente prohíbe un uso, ese uso queda afuera.</div>
</div>
</div>

---

<p class="eyebrow">06 · Personas</p>

# Formar y reasignar, sin contratar

<div class="grid g2">
<div>
<div class="card">
<p class="eyebrow" style="color:var(--muted)">Tiempo que pedimos reservar en los meses 1-3</p>
<div class="grid g2" style="margin:6px 0">
<div class="kpi"><div class="num">720 h</div><div class="lbl">de personas clave para sostener el plan (1,5 personas a tiempo completo)</div></div>
<div class="kpi"><div class="num">660 h</div><div class="lbl">de formación, como máximo</div></div>
</div>
<p style="font-size:17px">Estimamos usar entre 970 y 1.350 h de las 1.380 h reservadas. Operaciones y los managers confirman las agendas, persona por persona, en la validación.</p>
</div>
<div class="card dashed" style="margin-top:12px">
<span class="tag">Propuesta, la decide el Directorio con asesoría laboral</span>
<p><strong>Empleo:</strong> en 12 meses la mejora por IA no se usa para desvincular; primero se reasigna y se capacita. Quedan afuera causas previas ajenas a la IA.</p>
</div>
</div>
<div>

- **Formación:** básica para todos; intermedia para un grupo de 15-20.
- **Por qué casos por rol:** en el piloto de abril de 2026 (12 voluntarios) la IA se usó mucho, pero solo 17% terminó los cursos. El freno fue el tiempo: formamos con casos reales, en horario laboral.
- **Metas de uso:** Tecnología ≥80% en el mes 6 y ≥85% en el 12; Operaciones ≥60% en el 12, entre quienes tengan uso permitido. Juntas no alcanzan por sí solas el 80% del objetivo de la empresa: lo informamos aparte.

</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">No contratar. Si nadie interno puede dictar el curso básico, contratar en su lugar 16-32 h de un facilitador externo, con cotización previa.</span>
<span class="ref">

[Anexo D — Personas y cultura](annexes/04-personas-cultura.md)

</span>
</div>

---

<p class="eyebrow">07 · Roadmap técnico, financiero y cultural</p>

# Primero validar; después, fondos por etapa

<div class="cuenta">
<div class="cap">Lo que se libera por etapa, en miles de USD</div>
<div><b>8</b><span>Hoy: validación en 2026, 10 días hábiles. Caja 0 + tiempo 8</span></div>
<div><b>68</b><span>Con evidencia: meses 1-3. Caja 9 + tiempo 59</span></div>
<div><b>3</b><span>Con evidencia: reservas para cerrar si cortamos. Caja 1 + tiempo 2</span></div>
<div class="total"><b>79</b><span>Máximo hasta el mes 3. Caja 10 + tiempo 69</span></div>
</div>

| | Meses 1-3 | Meses 4-6 | Meses 7-9 | Meses 10-12 |
|---|---|---|---|---|
| Técnico | Base de medición, política y controles; prueba de prácticas | Solución según evidencia; estudio del asistente | Aplicación; producto solo con interés de un cliente | Evaluación y traspaso |
| Cultural | Básico para todos (≥90%); grupo intermedio | Referentes internos; Tecnología ≥80% | Casos por rol | Tecnología ≥85%; Operaciones ≥60% |
| Techo, miles de USD | **caja 9 · tiempo 59** | caja 2 · tiempo 14 | caja 2 · tiempo 11 | caja 2 · tiempo 11 |
| Punto de decisión | <span class="st pasa">Pasa</span> base, política y controles probados; gasto dentro del techo | <span class="st pasa">Pasa</span> ≥ +3% en el peor caso, sin daño<br><span class="st espera">Espera</span> Estimado > 0%, sin pasar | <span class="st pasa">Pasa</span> ≥ +8% en el peor caso, sin daño<br><span class="st espera">Espera</span> Estimado ≥ +5%, sin pasar (a ratificar) | Año 2: camino al equilibrio o interés de un cliente |

<p class="note" style="margin-top:2px">Caja: legal y herramientas. Tiempo: horas de gente de Acme Labs, a su costo. Meses 4-12: no se aprueban hoy. Lo que no pasa ni espera, corta (slide 3).</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Adoptar estos puntos de decisión como la regla para liberar fondos: hoy, 8 para validar; con evidencia, hasta 71 más (68 + 3). Máximo acumulado: 79.</span>
<span class="ref">

[Anexo F — Roadmap](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">08 · Costo y riesgo</p>

# Cuánto arriesgamos como máximo, y dónde frenamos

<p style="font-size:17px;margin:0 0 6px">Dos cifras distintas: el <strong>techo</strong> es lo máximo autorizado; el <strong>costo estimado</strong> es lo que esperamos gastar. Hoy se liberan 8; el resto hasta 79 se libera con evidencia (slide 8). Si todo pasa, el año completo tiene un costo estimado de ≈70 (27-113) y un techo de 121.</p>

| Si cortamos en | Techo hasta cerrar, miles de USD | Guardia hasta el mes 12 | Máximo del año | ¿Se decide hoy? |
|---|---|---|---|---|
| La validación | **8** (caja 0) | — | **8** | Sí: se liberan 8 |
| El mes 3 | **79** (caja 10) | +6 | **85** | Sí, el techo de 79; se libera con evidencia |
| El mes 6 | **95** (caja 12) | +4 | **99** | No |
| El mes 9 | **108** (caja 14) | +2 | **110** | No |
| El mes 12 | **121** (caja 16) | 0 | **121** | No |

<p class="note">Caja que sale de verdad hasta el mes 3: 2,3 a 8,6 estimado; el resto es tiempo de personas que ya están, sin nómina nueva ni deuda. Guardia mínima: accesos, incidentes y permisos hasta el mes 12, con caja 0 y 2 de tiempo por trimestre que falte; se aprueba al cortar. Sin beneficio presupuestado, el retorno modelado es −100%.</p>

<p style="font-size:17px;margin:0 0 10px"><strong>Sin vuelta atrás, no se aprueba nada hoy</strong> (se evalúan en el mes 12 o después): datos de clientes a un modelo · contratos de IA con clientes · IA que ejecuta acciones en el producto, aun con aprobación humana · compromisos de más de 12 meses.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar 79 como máximo autorizado hasta cerrar en el mes 3, en dos autorizaciones. Es un techo de presupuesto, no una pérdida ni una salida de caja.</span>
<span class="ref">

[Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<!-- _class: closing -->

<style scoped>h1 { font-size: 50px; } .fine, .fine p { color: #dcd8c9; }</style>

<p class="eyebrow">Valor medible · seguridad aceptable · fondos por etapa</p>

# Autorizar la validación inicial

<p style="font-size:22px;line-height:1.4;max-width:1100px;color:#f3efe4">Hoy pedimos 8 (miles de USD): diez días hábiles de tiempo de personas propias, sin caja, en 2026, antes de que arranque el plan 2027, con cargo al presupuesto 2026 a confirmar junto con las agendas. Con esa evidencia, decidir hasta 71 más para los meses 1-3 y las reservas. Y adoptar los puntos de decisión de los meses 3, 6, 9 y 12.</p>

<p class="pedido"><b>8</b> hoy &nbsp;→&nbsp; <b>+71</b> con evidencia &nbsp;→&nbsp; <b>79</b> como máximo hasta el mes 3 &nbsp;·&nbsp; miles de USD (slide 8)</p>

<div class="grid g2" style="margin-top:auto;position:relative">
<div>
<p class="eyebrow">Equipo · Grupo 11</p>
<p>Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
<p class="fine">Quienes producen, verifican y firman cada punto de decisión en Acme Labs se designan como condición de la primera autorización.</p>
</div>
<div class="fine" style="max-width:340px">
<p>79 es un techo, no salida de caja. Plataforma y producto se vuelven a costear antes de decidirlos. Cifras estimadas, a confirmar con fuentes internas.</p>
<p>Hicimos este plan con IA: un asistente por rol, una revisión adversarial simulada y chequeos automáticos de fuentes y de datos privados.</p>
</div>
</div>
