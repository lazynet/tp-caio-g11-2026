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
     cifra viene de un anexo y de una fuente. El pedido completo vive solo en la
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

<p class="fine">Cifras estimadas · validación con autorización propia antes de liberar M1-M3 · sin promesa de repago en el año</p>

---

<p class="eyebrow">01 · Problema</p>

# Uso sin valor medido, y un diagnóstico por conciliar

<div class="grid main-side">
<div class="plain">

| Dimensión | Madurez propuesta | Lo que la explica |
|---|---|---|
| Estrategia | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Hay iniciativas; sin estrategia formal aprobada (supuesto) |
| Datos e infraestructura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 provisional | Inventario existente; datos distribuidos; integración por validar |
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
<span class="body">Autorizar una validación acotada del diagnóstico, las fuentes y las agendas antes de liberar la ejecución de M1-M3.</span>
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
<p>PR aceptados por persona activa contra una base congelada, retrabajo e incidentes primero. Pasa si el límite inferior llega a +3% en el mes 6 y +8% en el 9.</p>
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

<p style="margin-top:14px">El paso no está asegurado: con +3,75% y semiancho de 3 puntos, el límite inferior queda en +0,75%.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar capacidad con calidad como beneficio a medir, sin presupuestar caja ni ingreso.</span>
<span class="ref">

[Anexo B](annexes/02-arquitectura.md) · [Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">03 · Alternativas</p>

# El mínimo compra la medición; lo demás es referencia

<div class="grid main-side">
<div class="card dark">
<span class="tag">Qué compra el mínimo</span>
<h3>Saber si hay valor, con controles probados</h3>
<p>Básico, cohorte, controles por superficie, base y medición, y descubrimiento del asistente, con las herramientas que ya pagamos. Sin plataforma.</p>
<p>Todo el año, si pasan los gates: <strong>≈70 (27-113)</strong>, incluida la validación; proyección no aprobada.</p>
</div>
<div class="plain">

| Referencia, otro alcance | Económico |
|---|---|
| Piloto sobre el agente actual | 47 |
| Gobierno y formación desde el inicio | 161 |
| Rama sin señal, paquete completo | ≈199 |
| Plataforma sin producto | 394 (≈400) |
| Plataforma con producto | 471 |

</div>
</div>

<p class="note">Miles de USD. Alcances distintos, sin comparación homogénea: no prueban que el mínimo sea la mejor compra. El pedido completo (33 + 6 de caja, 72 + 7 de tiempo) queda como alternativa. En el mes 3 se comparan gastos futuros evitables.</p>

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
<h3>Tras la validación inicial</h3>
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
<span class="body">Condicionar la columna izquierda a la validación inicial; ratificar o no las cuatro condiciones.</span>
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

<p class="note" style="margin-top:12px">Sin plataforma, no alcanza la política: cada superficie prueba sus compensatorios (secreto sintético, prueba adversarial, revisión humana) con críticos cerrados y residual aceptado. Lo que no cumple se excluye, y Seguridad puede suspender un uso aunque gasto y adopción cumplan.</p>

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
<p class="eyebrow" style="color:var(--muted)">Reserva propuesta para los meses 1-3</p>
<div class="grid g2" style="margin:6px 0">
<div class="kpi"><div class="num">1,5</div><div class="lbl">FTE clave a reservar (720 h)</div></div>
<div class="kpi"><div class="num">660 h</div><div class="lbl">Formación: máximo del tramo</div></div>
</div>
<p class="note">Supuesto: reserva máxima de 1.380 h; demanda estimada de 970-1.350 h. Confirmar agendas por persona y semana en una matriz privada.</p>
</div>
<div>

- Básico para toda la organización e intermedio para una cohorte de 15-20.
- Piloto de abril (n=12, autoseleccionado): uso alto, 17% completó los cursos.
- **Metas por área:** Tecnología ≥80% en el mes 6 y ≥85% en el 12; Operaciones habilitadas ≥60% en el 12. Cumplir exactamente 85%/60%, con igual peso y toda Operaciones habilitada, da 72,5%; no es un techo ni cumplimiento del OKR combinado.
- **Transición:** formar y reasignar antes que desvincular, con un estudio de un rol crítico y chequeo de equidad por grupo. Sin compensación monetaria nueva en 12 meses.

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

<p class="eyebrow">07 · Roadmap técnico, financiero y cultural</p>

# Validación inicial y fondos por decisión

<p><strong>Preparación 2026:</strong> 10 días hábiles, 80-136 h; techo <strong>0 / 8</strong>. Diagnóstico, agendas y viabilidad antes de decidir continuar, reducir o detener.</p>

| | Meses 1-3 → mes 3 | Meses 4-6 → mes 6 | Meses 7-9 → mes 9 | Meses 10-12 → cierre |
|---|---|---|---|---|
| Técnico | Base, política, controles y prueba de prácticas | Solución según evidencia; medición del asistente | Aplicación; producto solo con señal | Evaluación y traspaso |
| Cultural | Básico para todos; intermedio de la cohorte | Champions; diagnóstico de un rol crítico | Casos por rol; diseño del rol | Evaluación de lo que escala |
| Financiero: techo caja / tiempo | **9 / 59** (segunda autorización) | 2 / 14 | 2 / 11 | 2 / 11 |
| Pasa si | Base, política, controles probados, básico ≥90% | Límite inferior ≥ +3%, sin daño; Tec. ≥80% | Límite inferior ≥ +8% | Tec. ≥85%; Op. habilitadas ≥60% |
| Plataforma | Se evalúa | Se relee | Se relee | Irreversibles, para después |

<p class="note">Miles de USD; los meses 4-12 no se aprueban hoy. El Council puede frenar o cortar cada mes, sin liberar fondos. Un daño corta aunque el throughput pase. Las esperas de los meses 6 y 9 duran 6 semanas, con subtramo aprobado aparte; si no pasa, corta. Base extendida a la semana 8: formación y prueba arrancan en la 9. Cada gate lee adopción, impacto financiero y calidad.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Adoptar estos gates como regla para liberar fondos: primero validar; después decidir hasta 71 adicionales, con reservas. Acumulado máximo: 79.</span>
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
| Antes de M1 | 0 / 8 → **8** | **8**, cierre documental incluido |
| Mes 3 | 10 / 69 → **79** | **85** con núcleo de gobierno |
| Mes 6 | 12 / 83 → **95** | **99** |
| Mes 9 | 14 / 94 → **108** | **110** |
| Mes 12 | 16 / 105 → **121** | **121** |

</div>
<div class="grid" style="gap:8px">
<div class="card"><strong>Caja:</strong> legal y herramientas</div>
<div class="card"><strong>Tiempo:</strong> horas existentes, no nómina nueva</div>
<div class="card rose"><strong>Beneficio presupuestado: 0</strong> (ROI modelado −100%)</div>
<div class="card"><strong>Fuente:</strong> interna, por etapas, sin deuda</div>
</div>
</div>

<p class="note">Miles de USD; suma de techos, sin restar beneficio. Esperar 6 semanas y cortar: 102 en el mes 6, 115 en el 9. El núcleo posterior (accesos, incidentes, permisos) cuesta caja 0 y hasta 6 de tiempo, y se aprueba al salir. Si no actuamos, siguen abiertos los clientes que prohíben modelos externos y el uso sin regla, que el mínimo cubre, y el consumo de modelos, que no cubre: sin montos.</p>

<p class="eyebrow" style="margin-bottom:6px">Irreversibles: en el mes 12 y para después</p>

<div class="chips outline">
<span>Datos de cliente a un modelo</span>
<span>Contrato de IA con un cliente</span>
<span>"Actúa con aprobación" en producto</span>
<span>Compromisos a más de 12 meses</span>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Aceptar una pérdida máxima de aprendizaje de 79 hasta cerrar en M3, sujeta a dos autorizaciones.</span>
<span class="ref">

[Anexo E](annexes/05-business-case.md) · [Anexo F](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<!-- _class: closing -->

<style scoped>h1 { font-size: 54px; }</style>

<p class="eyebrow">Valor medible · seguridad aceptable · fondos por decisión</p>

# Autorizar la validación inicial

<p style="font-size:24px;line-height:1.4;max-width:1000px;color:#f3efe4">Autorizar primero diez días hábiles de validación: hasta 8 de tiempo interno y caja incremental 0, con agendas e imputación 2026 confirmadas. Adoptar los gates de los meses 3, 6, 9 y 12. Con evidencia, decidir hasta 71 adicionales para M1-M3 y reservas: caja 10 y tiempo 61. Pérdida máxima hasta cerrar: 79; la segunda liberación y el año quedan condicionados.</p>

<div class="grid g2" style="margin-top:auto;position:relative">
<div>
<p class="eyebrow">Equipo · Grupo 11</p>
<p>Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
<p class="fine">Responsables por sección y por gate: a designar.</p>
</div>
<div class="fine">
<p>Miles de USD. Sujeto a horas liberadas y controles probados antes de usar; plataforma y producto se vuelven a costear.</p>
<p>Hecho con el modelo que proponemos: roles de IA, revisión adversarial y chequeos de fuentes y fuga. Cifras estimadas, por validar contra fuentes internas; ensayo pendiente.</p>
</div>
</div>
