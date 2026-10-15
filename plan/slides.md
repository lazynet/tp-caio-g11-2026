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
     cifra viene de un anexo y de fichas en draft. El pedido completo vive solo en la
     slide 10; la 9 muestra su pérdida máxima. Diseño: plan/theme/acme.css; los bloques
     HTML llevan Markdown adentro, separado por líneas en blanco, y los links siguen en
     Markdown. -->

<!-- _class: cover -->
<!-- _paginate: false -->

<div class="sun"></div>

<span class="chip">Grupo 11 · Diplomatura CAIO · UTN BA</span>

# Medir el valor antes de ampliar la inversión

<p class="sub">Plan Maestro CAIO 2027 para <strong>Acme Labs</strong>, software para bancos, fintechs y grandes empresas</p>

<p class="eyebrow">Doce meses de IA en la operación y en el producto, con fondos por decisión</p>

<p style="max-width:820px">Hoy la IA se usa, pero su valor incremental no está medido. Proponemos empezar por lo mínimo que compra esa medición, con controles probados y las herramientas que ya pagamos, y ampliar solo con evidencia.</p>

<p class="fine">Caso propuesto · borrador sin verificación humana · sin promesa de repago en el año</p>

---

<p class="eyebrow">01 · Problema</p>

# Uso sin valor medido, y un diagnóstico por conciliar

<div class="grid main-side">
<div class="plain">

| Dimensión (M1U1) | Madurez propuesta | Lo que la explica |
|---|---|---|
| Estrategia | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Propuestas de IA sin decidir |
| Datos e infraestructura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Buena nube, datos sin inventario |
| Talento y cultura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Agente de código: Tecnología ~7 de 10; Operaciones ~1 de 10 |
| Gobernanza | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Política en borrador; último registro, abril de 2026 |
| Adopción y valor | <span class="dots"><span class="on">●</span><span class="half">●</span><span class="off">●●●</span></span> 1-2 | Sin IA productiva documentada en la oferta; valor interno sin medir |

</div>
<div class="grid">
<div class="card kpi"><div class="num">40-50%</div><div class="lbl">de la facturación viene del cliente principal (agosto)</div></div>
<div class="card kpi"><div class="num">83-90%</div><div class="lbl">de utilización promedio, sin corte por proyecto</div></div>
</div>
</div>

<p class="note">Fuentes de escritorio con poblaciones y fechas distintas: nómina y contratistas a septiembre, utilización de 2026, concentración de agosto. Son hipótesis, no hechos certificados.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Tomar el diagnóstico como hipótesis: antes de comprometer horas, conciliar corte, nómina, contratistas, personas/FTE y horas por rol.</span>
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
<h3>Capacidad con calidad</h3>
<p>PR aceptados por persona activa contra una base congelada, con retrabajo e incidentes primero. Pasa por el límite inferior del intervalo: +3% en el mes 6, +8% en el mes 9.</p>
</div>
<div class="card">
<span class="tag">En el modelo</span>
<h3>Beneficio de caja estimado: 0</h3>
<p>Ingreso nuevo: 0. La capacidad liberada no es caja: solo se convierte si se vende o evita una contratación, con evidencia.</p>
</div>
<div class="card dashed">
<span class="tag">Hipótesis, no beneficio</span>
<h3>Asistente de integración</h3>
<p>Antes del mes 6 medimos el tiempo a la primera integración exitosa con la documentación y el soporte actuales. Sin problema, base y señal comercial escrita, no se construye.</p>
</div>
</div>

<p style="margin-top:14px">El paso no está asegurado: con +3,75% y un semiancho de 3 puntos, el límite inferior queda en +0,75%. Por eso medimos antes de ampliar.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar capacidad con calidad como beneficio a medir, sin presupuestar caja ni ingreso.</span>
<span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">03 · Alternativas</p>

# Costos publicados de alcances distintos, pendientes de homogeneizar

<div class="plain">

| Alcance publicado | Caja / tiempo → económico | Qué compra |
|---|---|---|
| Piloto sobre el agente actual | 5 / 42 → **47** | Cohorte, matriz, prácticas y medición; sin formación general ni legal |
| Gobierno y formación desde el inicio | 21 / 141 → **161** | Política, matriz, inventario, legal y medición |
| Rama sin señal del paquete anterior | ≈39 / ≈160 → **≈199** | Gobierno y formación después de arrancar el paquete, con compensatorios |
| Paquete con plataforma, sin producto | 177 / 217 → **394** (≈400 con prueba) | Plataforma, controles, formación y demostración externa |
| Paquete con producto | 214 / 257 → **471** | Otro alcance; neto optimista ≈ −357 |
| **Paquete mínimo, todo el año** | **≈67 (25-108)**, proyección | Básico, cohorte, controles probados, medición y descubrimiento; sin plataforma |

</div>

<p class="note">Miles de USD. No hay comparación homogénea todavía: controles, población y medición no son iguales. El pedido anterior de 33 + 6 de caja y 72 + 7 de tiempo queda como alternativa. En el mes 3 se comparan gastos futuros evitables, sin costos hundidos.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Empezar por el paquete mínimo, sin llamar presupuesto aprobado a ninguna proyección anual.</span>
<span class="ref">

[Anexo E — Business case](annexes/05-business-case.md)

</span>
</div>

---

<p class="eyebrow">04 · Arquitectura</p>

# La respuesta mínima que pase las pruebas

<div class="chips">
<span>Configurar lo que ya pagamos antes de comprar o ensamblar</span>
<span>Permisos, MCP acotados y escaneo local por superficie</span>
<span>Extracción reproducible de PR, CI, reversiones e incidentes</span>
<span>El gateway no reemplaza controles de IDE, chat ni suite</span>
<span class="hot">Sin datos productivos de clientes en 12 meses</span>
</div>

<div class="grid g3">
<div class="card dark">
<h3>Aprobar hoy</h3>
<p>Meses 1-3 con herramientas existentes: configuración, telemetría, base y prueba de prácticas.</p>
</div>
<div class="card">
<h3>Meses 3, 6 y 9: opción de plataforma</h3>
<p>Regla vigente: una señal de contrato, precio o cliente. Propuesta pendiente de ratificación: además, brecha documentada, alternativas comparables, economía incremental o pérdida aceptada, y capacidad demostrada.</p>
</div>
<div class="card dashed">
<h3>No aprobar todavía</h3>
<p>Gateway, harness central, modelo propio y contratos de más de 12 meses. Nada pasa al año 2 por defecto.</p>
</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aprobar la columna izquierda; ratificar o no las cuatro condiciones.</span>
<span class="ref">

[Anexo B — Arquitectura](annexes/02-arquitectura.md)

</span>
</div>

---

<p class="eyebrow">05 · Gobierno y seguridad</p>

# Controles probados antes de usar

<div class="grid g3">
<div class="kpi"><div class="num">5</div><div class="lbl">asientos en el AI Council, dentro del comité de tecnología: revisión mensual con poder de corte</div></div>
<div class="kpi"><div class="num">3 roles</div><div class="lbl">distintos en cada gate: quien produce la evidencia, quien la verifica y quien firma</div></div>
<div class="kpi"><div class="num" style="font-size:30px">“Prepara, no ejecuta”</div><div class="lbl">techo de autonomía en el producto durante los 12 meses</div></div>
</div>

<p class="note" style="margin-top:12px">Sin plataforma, no alcanza la política: cada superficie prueba sus compensatorios (secreto sintético, prueba adversarial, revisión humana) con críticos cerrados y residual aceptado. Lo que no cumple se excluye. Seguridad puede suspender el uso aunque el gasto o la adopción cumplan.</p>

<div class="decision block">
<div class="decision-head"><span class="pill">Decisiones</span><span class="ref">

[Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md)

</span></div>
<div class="grid g3">
<div><strong>1.</strong> Ratificar la política en los meses 1-3, después de confirmar su estado actual.</div>
<div><strong>2.</strong> Sin crédito ni scoring en 12 meses; el resto, clasificado caso por caso.</div>
<div><strong>3.</strong> Ningún uso nuevo sin prueba previa por superficie; una prohibición contractual se cumple excluyendo el uso.</div>
</div>
</div>

---

<p class="eyebrow">06 · Personas</p>

# Formar, reasignar y decidir una excepción externa

<div class="grid g2">
<div class="card">
<p class="eyebrow" style="color:var(--muted)">Capacidad interna de los meses 1-3</p>
<div class="grid g2" style="margin:6px 0">
<div class="kpi"><div class="num">2,0-2,8</div><div class="lbl">FTE internos en total (referencia 2,4)</div></div>
<div class="kpi"><div class="num">0,9-1,4</div><div class="lbl">FTE clave, dentro del total</div></div>
</div>
<p class="note">Salen de horas facturables: cada hora tiene origen, tarea desplazada y responsable en una matriz privada.</p>
</div>
<div>

- Básico para toda la organización e intermedio para una cohorte de 15-20.
- Piloto de abril (n=12, autoseleccionado): uso alto, 17% completó los cursos.
- **Metas por área:** Tecnología ≥80% en el mes 6, Operaciones habilitadas ≥60%. Cumplir exactamente esas metas da 72,5% combinado: no es un techo; publicamos el combinado y la cobertura.

</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">No contratar. Si falta un facilitador interno, decidir una excepción externa de 16-32 h que lo reemplaza, con cotización. Empleo: compromiso con excepciones.</span>
<span class="ref">

[Anexo D — Personas y cultura](annexes/04-personas-cultura.md)

</span>
</div>

---

<p class="eyebrow">07 · Roadmap</p>

# Doce meses, revisión cada mes, fondos cada tres

| | Meses 1-3 → mes 3 | Meses 4-6 → mes 6 | Meses 7-9 → mes 9 | Meses 10-12 → cierre |
|---|---|---|---|---|
| Qué pasa | Diagnóstico, base, política, controles, formación y prueba | Solución según evidencia; medición del asistente | Aplicación; producto solo con señal | Evaluación y traspaso |
| Techo caja / tiempo | **9 / 58** (aprobar hoy) | 2 / 14 | 2 / 11 | 2 / 11 |
| Pasa si | Base, política, controles probados, básico ≥90% | Límite inferior ≥ +3%, sin daño; Tec. ≥80% | Límite inferior ≥ +8% | Tec. ≥85%; Op. habilitadas ≥60% |
| Plataforma | Se evalúa | Se relee | Se relee | Irreversibles, para después |

<p class="note">Miles de USD; los meses 4-12 no se aprueban hoy. Cada mes el Council puede frenar o cortar, sin liberar fondos. Calidad primero: un daño corta aunque el throughput pase. Espera del mes 6: 6 semanas y, si sigue debajo, corta. Si la base se extiende a la semana 8, básico, intermedio y prueba arrancan en la 9.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Adoptar estos gates como regla para liberar fondos.</span>
<span class="ref">

[Anexo F — Roadmap](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">08 · Costo y riesgo</p>

# Cuánto podemos perder para aprender

<div class="grid main-side">
<div class="plain">

| Si salimos en | Hasta cerrar (caja / tiempo) | Máximo del año |
|---|---|---|
| Mes 3 | 10 / 63 → **73** | **79** con núcleo de gobierno |
| Mes 6 | 12 / 77 → **89** | **93** |
| Mes 9 | 14 / 88 → **102** | **104** |
| Mes 12 | 16 / 99 → **115** | **115** |

</div>
<div class="grid" style="gap:8px">
<div class="card"><strong>Caja:</strong> legal y herramientas</div>
<div class="card"><strong>Tiempo:</strong> horas existentes, no nómina nueva</div>
<div class="card rose"><strong>Beneficio presupuestado: 0</strong> (ROI modelado −100%)</div>
</div>
</div>

<p class="note">Miles de USD; límites por suma de techos, sin restar beneficio. Tras un corte, el núcleo (accesos, incidentes, permisos) cuesta caja 0 y hasta 6 de tiempo. A 12× de consumo, el incremental (211-267 por año) es exposición de la empresa, con o sin plan.</p>

<p class="eyebrow" style="margin-bottom:6px">Irreversibles: en el mes 12 y para después</p>

<div class="chips outline">
<span>Datos de cliente a un modelo</span>
<span>Contrato de IA con un cliente</span>
<span>"Actúa con aprobación" en producto</span>
<span>Compromisos a más de 12 meses</span>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar una pérdida máxima de aprendizaje de 73 al mes 3.</span>
<span class="ref">

[Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<!-- _class: closing -->

<p class="eyebrow">Valor medible · seguridad aceptable · fondos por decisión</p>

# El Directorio autoriza solo el paquete mínimo de los meses 1-3, hasta 9 de caja más 1 de reserva y 58 de tiempo más 3 de preparación y 2 de cierre, y adopta los gates de los meses 3, 6, 9 y 12.

<div class="grid g2" style="margin-top:auto;position:relative">
<div>
<p class="eyebrow">Equipo · Grupo 11</p>
<p>Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
<p class="fine">Responsables por sección y por gate: pendientes de acordar en el equipo.</p>
</div>
<div class="fine">
<p>Miles de USD. Sujeto a horas liberadas por persona y controles probados antes de usar. Plataforma y producto se recostean antes de liberarse.</p>
<p>Usamos el modelo operativo que proponemos: roles asumidos por agentes, revisión adversarial y chequeos de fuentes y de fuga de datos. Las fichas siguen en borrador; el ensayo de la defensa está pendiente.</p>
</div>
</div>
