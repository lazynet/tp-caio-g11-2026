---
owner: caio
status: draft
marp: true
theme: acme
paginate: true
size: 16:9
---

<!-- Fuente única del deck. Nunca edites un deck generado: corré scripts/build-deck.sh.
     Una slide por `---`, con un título `#` cada una. Máximo 10 slides. Cada slide dice
     qué decisión le pide al board y apunta a su anexo. Borrador del CAIO: toda cifra
     viene de un anexo y de fichas en draft. El pedido de hoy completo vive solo en la
     slide 8; las demás piden su parte. Diseño: plan/theme/acme.css; los bloques HTML
     llevan Markdown adentro, separado por líneas en blanco, y los links siguen en
     Markdown. -->

<!-- _class: cover -->
<!-- _paginate: false -->

<div class="sun"></div>

<span class="chip">Grupo 11 · Diplomatura CAIO · UTN BA</span>

# IA que se vende y se gobierna

<p class="sub">Plan Maestro CAIO 2027 para <strong>Acme Labs</strong>, software para bancos, fintechs y grandes empresas</p>

<p class="eyebrow">Lo que pedimos hoy: los primeros tres meses, no el año</p>

<div class="grid g3" style="max-width:820px;margin:8px 0 14px">
<div class="card kpi"><div class="num">33</div><div class="lbl">mil USD de caja para los meses 1-3, con una prueba chica</div></div>
<div class="card kpi"><div class="num">~1,8</div><div class="lbl">FTE clave como piso de capacidad</div></div>
<div class="card kpi"><div class="num">Mes 3</div><div class="lbl">una señal libera la plataforma: la regla de decisión</div></div>
</div>

<p class="fine">Caso propuesto · borrador sin verificación humana · el pedido completo, en la slide 8</p>

---

<p class="eyebrow">01 · Punto de partida</p>

# Rentable, concentrada y sin IA en lo que vende

<div class="grid main-side">
<div class="plain">

| Dimensión (M1U1) | Madurez propuesta | Lo que la explica |
|---|---|---|
| Estrategia | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Propuestas de IA sin decidir |
| Datos e infraestructura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Buena nube, datos sin inventario |
| Talento y cultura | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Agente de código: Tecnología ~7 de 10; Operaciones ~1 de 10 |
| Gobernanza | <span class="dots"><span class="on">●●</span><span class="off">●●●</span></span> 2 | Política en borrador desde abril de 2026 |
| Adopción y valor | <span class="dots"><span class="on">●</span><span class="half">●</span><span class="off">●●●</span></span> 1-2 | Cero IA en producción en el producto |

</div>
<div class="grid">
<div class="card kpi"><div class="num">40-50%</div><div class="lbl">de la facturación viene del cliente principal</div></div>
<div class="card kpi"><div class="num">83-90%</div><div class="lbl">de utilización: poco margen para sumar trabajo</div></div>
</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Validar el diagnóstico como base del plan.</span>
<span class="ref">

[Anexo A — Diagnóstico](annexes/01-diagnostico.md)

</span>
</div>

---

<p class="eyebrow">02 · Tesis</p>

# Gobierno y formación primero; la plataforma, con una señal

<div class="grid g3">
<div class="card dark">
<span class="tag">Siempre · desde hoy</span>
<h3>La base</h3>
<p>Gobierno ratificado, línea de base congelada, formación para toda la empresa y una prueba chica con el agente de código que ya se usa.</p>
</div>
<div class="card">
<span class="tag">Solo con señal en el mes 3</span>
<h3>La plataforma</h3>
<p>Gateway neutral al modelo, controles con bloqueo, harness y evals. La señal puede ser de precio, de contrato o de un cliente.</p>
</div>
<div class="card dashed">
<span class="tag">Con señal de un cliente · mes 6</span>
<h3>IA en el producto</h3>
<p>Un asistente de integración en la plataforma propia, que solo asiste y sin datos de clientes. Le ganó en RICE a dos alternativas (puntajes propuestos, sin medir).</p>
</div>
</div>

<p style="margin-top:14px">Con productividad sola, las opciones baratas ganan el año 1. La plataforma compra opciones (cobertura de precio, un ingreso y licencia para venderles a bancos, si los meses 1-3 la confirman) y se paga solo si una prende.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Adoptar la tesis: la plataforma se gana en el mes 3 y el producto, en el mes 6.</span>
<span class="ref">

[Anexo F — Roadmap ajustado por riesgo](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">03 · Arquitectura</p>

# Un gateway si hay señal, cero datos de cliente

<div class="chips">
<span>Gateway con ≥2 proveedores, ruteo por nivel de dato</span>
<span>Registro de costo</span>
<span>Aislamiento por cliente</span>
<span>Harness con evals en CI y gate humano</span>
<span>Fuera del gateway: control compensatorio probado en los meses 4-6</span>
<span>El agente de código entra solo si no rompe la suscripción</span>
<span class="hot">Sin fine-tuning ni datos productivos de clientes en 12 meses</span>
</div>

<div class="grid g3">
<div class="card dark">
<h3>Aprobar hoy</h3>
<p>Meses 1-3: inventario, línea de base, matriz de superficies, telemetría, prueba chica.</p>
</div>
<div class="card">
<h3>Meses 3 y 6, solo con señal</h3>
<p>Gateway, harness y prueba de portabilidad y costo (meses 4-6); piloto de los meses 7-9.</p>
</div>
<div class="card dashed">
<h3>No aprobar todavía</h3>
<p>Modelo propio y contratos de más de 12 meses.</p>
</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Solo la columna de la izquierda.</span>
<span class="ref">

[Anexo B — Arquitectura](annexes/02-arquitectura.md)

</span>
</div>

---

<p class="eyebrow">04 · Gobierno</p>

# Gobierno que habilita, no que frena

<div class="grid g3">
<div class="kpi"><div class="num">5</div><div class="lbl">asientos en el AI Council, dentro del comité de tecnología y con CoE virtual: revisión mensual con poder de corte</div></div>
<div class="kpi"><div class="num">5 días</div><div class="lbl">hábiles de respuesta para el riesgo medio, con intake en 3 niveles</div></div>
<div class="kpi"><div class="num" style="font-size:30px">“Prepara, no ejecuta”</div><div class="lbl">techo de autonomía en el producto durante los 12 meses</div></div>
</div>

<p class="note" style="margin-top:12px">Secretos y datos prohibidos: bloqueo técnico en la pasarela (con señal en el mes 3) y en el equipo; en chat, IDE y suite, solo control compensatorio, con residual que acepta el Council. El primer secreto expuesto dispara la contención.</p>

<div class="decision block">
<div class="decision-head"><span class="pill">Decisiones</span><span class="ref">

[Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md)

</span></div>
<div class="grid g3">
<div><strong>1.</strong> Ratificar la política de IA en los meses 1-3: compromiso interno, enmendable.</div>
<div><strong>2.</strong> Sin crédito ni scoring en 12 meses; el resto, clasificado caso por caso.</div>
<div><strong>3.</strong> Financiar los controles por decisión: gobierno mínimo siempre; controles técnicos de la plataforma si en el mes 3 hay señal; la demostración externa (red team externo e ISO ampliada), solo con señal contractual en el mes 9 o si en el mes 6 se libera el producto.</div>
</div>
</div>

---

<p class="eyebrow">05 · Personas</p>

# Capacitar y reasignar, no contratar

<div class="grid g2">
<div class="card">
<p class="eyebrow" style="color:var(--muted)">Piloto de abril · n=12, autoseleccionado</p>
<div class="grid g2" style="margin:6px 0">
<div class="kpi"><div class="num">+42</div><div class="lbl">NPS: el uso fue alto</div></div>
<div class="kpi"><div class="num">17%</div><div class="lbl">completó los cursos</div></div>
</div>
<p class="note">Es una señal, no una medición de toda la organización: la base de los meses 1-3 la mide.</p>
</div>
<div>

- Formación por rol, en horario laboral, con champions con tiempo asignado.
- Se mide **uso real semanal por área**, no seats comprados.
- **OKR 2027, con el presupuesto, no hoy.** El 80% combinado no se alcanza ni con las metas del plan (72,5% como mucho): proponemos Tecnología ≥80% y Operaciones habilitadas, cada una con su denominador. El gasto de tecnología bajo 3,5% de la facturación: mantenerlo y recortar el plan, o medirlo sin la inversión del plan. Cambia cómo se mide, no lo que se gasta.

</div>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Capacitar en vez de contratar. IA aplicada de los meses 1-3 con <strong>un</strong> contractor a prueba (los meses 4-12, solo con señal en el mes 3), que choca con "no contratar", o un rol interno demostrado. Empleo: un compromiso con excepciones.</span>
<span class="ref">

[Anexo D — Personas y cultura](annexes/04-personas-cultura.md)

</span>
</div>

---

<p class="eyebrow">06 · Roadmap</p>

# Revisión cada mes, fondos cada tres

<p><strong>Cada mes, el Council revisa el tablero y puede frenar o cortar. Los fondos se liberan en los meses 3, 6, 9 y 12.</strong></p>

| | Meses 1-3 → mes 3 | Meses 4-6 → mes 6 | Meses 7-9 → mes 9 | Meses 10-12 → cierre |
|---|---|---|---|---|
| Técnico y gobierno | Base, política, matriz, prueba chica | Con señal: gateway, evals, red team | Caso interno: prepara, no ejecuta | Go/no-go de modelo propio |
| Cultural | Básico ≥90% | Operaciones y staff | Casos por rol | Tecnología ≥85% |
| Techo caja / tiempo | **33 / 72** | **71 / 106** | **59 / 78** | **95 / 69** |
| Pasa si | Base y política; **una señal libera la plataforma** | Throughput ≥ +3%; Tec. ≥80% | Throughput ≥ +8% | Camino a ~17% o interés contractual |

<p class="note">Miles de USD; meses 4-12, rama con señal. <strong>El mes 3 no corta: decide la plataforma.</strong> Sin señal, gobierno mínimo y formación (≈ 199 en el año); los meses 6 y 9 releen. Throughput por límite inferior del intervalo; calidad incierta cuenta como espera. Espera en el mes 6: se remide a las 6 semanas y, si sigue en la banda, corta el frente interno; en el mes 9, base mínima.</p>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Adoptar esta regla para liberar fondos.</span>
<span class="ref">

[Anexo F — Roadmap](annexes/06-roadmap-riesgo.md)

</span>
</div>

---

<p class="eyebrow">07 · Business case</p>

# Lo barato gana el año 1; la plataforma, con señal

<div class="grid main-side">
<div class="plain">

| Miles de USD | Sin señal en el mes 3 | Con señal en el mes 3 |
|---|---|---|
| Costo económico del año | **≈ 199** | **≈ 400** (216-584) |
| Caja, con contingencia | ≈ 39 | 98-255 (114-314 si en el mes 6 se libera el producto) |
| Tiempo reasignado, a costo cargado | ≈ 160 | 115-320 (~3,5 FTE), más ~6 de la prueba |

</div>
<div class="grid" style="gap:8px">
<div class="card"><strong>Gobierno mínimo y formación</strong><br>161 · neto −161 a −99</div>
<div class="card"><strong>Piloto sobre el agente actual</strong><br>47 · neto −47 a +15</div>
<div class="card rose"><strong>Paquete completo</strong><br>394 · neto −332</div>
</div>
</div>

<p class="note">ROI a 12 meses negativo y caja cero: <strong>en el año 1 ganan las alternativas baratas</strong>, y por eso pedimos solo los meses 1-3.</p>

<div class="decision block">
<div class="decision-head"><span class="pill">Decisión: el pedido de hoy completo</span><span class="ref">

[Anexo E — Business case](annexes/05-business-case.md)

</span></div>
<div class="grid g2">
<div><strong>1.</strong> Meses 1-3 con la prueba chica: 33 de caja (contractor hasta 16,5) y 6 de reserva de cierre; 72 de tiempo (~1,8 FTE clave, ~654 h).</div>
<div><strong>2.</strong> Piso: ~1,8 FTE clave; con señal, 2,2 / 2,2 / 2,1 en los meses 4-12 con el replan (respaldo: 2,5 en los meses 4-6).</div>
<div><strong>3.</strong> El mes 3 libera la plataforma y amplía la reserva a 15 solo con señal. Cortar en el mes 3: 79 en el medio, 115 hasta cerrar, 155 en el año.</div>
<div><strong>4.</strong> Base mínima tras un corte: hasta 41 de tiempo; preparación previa: hasta 7.</div>
</div>
</div>

---

<p class="eyebrow">08 · Riesgos</p>

# Sin señal, el año cuesta la mitad; lo irreversible, al cierre

<div class="plain">

| Escenario | Qué pasa | Costo | Capacidad | Neto 12 m | ROI 12 m |
|---|---|---|---|---|---|
| Sin señal en el mes 3 | Sin plataforma en los meses 4-12 | ≈ 199 | ≥ φ × 62 | −199 a −137 | −100% a −69% |
| Pesimista, con la regla | Espera en el mes 6, vence y corta | 265 | ~3 | ≈ −262 | ≈ −99% |
| Pesimista, sin frenar | Sin la regla | 394 | 12 | −382 | −97% |
| Base | Pasan los meses 6 y 9 (o la espera vence) | 394 (265) | 62 (~19) | −332 (≈ −245) | −84% (≈ −93%) |
| Optimista | Producto en los meses 7-12 | 471 | 114 | −357 | −76% |

</div>

<p class="note">Miles de USD; salvo la primera fila, con señal y sin la prueba. φ: ganancia sin plataforma, sin dato (0 a 1). A 12× de consumo, 211-267 por año, con o sin plan (−502 sin frenar).</p>

<p class="eyebrow" style="margin-bottom:6px">Irreversibles: en el mes 12 y para después</p>

<div class="chips outline">
<span>Datos de cliente a un modelo</span>
<span>Contrato de IA con un cliente</span>
<span>"Actúa con aprobación" en producto</span>
<span>Compromisos a más de 12 meses</span>
</div>

<div class="decision">
<span class="pill">Decisión</span>
<span class="body">Con señal, el replan de los meses 4-6; la excepción de 0,3 FTE cubre solo el 0,2 faltante del contractor.</span>
<span class="ref">

[Anexo F](annexes/06-roadmap-riesgo.md) · [Anexo E](annexes/05-business-case.md)

</span>
</div>

---

<!-- _class: closing -->

<p class="eyebrow">Resolución que proponemos</p>

# El Directorio aprueba el pedido de hoy de la slide 8, los meses 1-3 con la prueba chica, y adopta la regla de decisión: el Council revisa el riesgo cada mes y puede cortar; la plataforma se gana con una señal en el mes 3, y los fondos del resto del año se liberan en los meses 6, 9 y 12.

<div class="grid g2" style="margin-top:auto;position:relative">
<div>
<p class="eyebrow">Equipo · Grupo 11</p>
<p>Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo</p>
<p class="fine">Responsables por sección: pendiente de acordar en el equipo.</p>
</div>
<div class="fine">
<p>Usamos el modelo operativo que proponemos: roles asumidos por agentes, una revisión adversarial del board y chequeos automáticos de fuentes y de fuga de datos.</p>
<p>Cada cifra remonta a un anexo; las fichas siguen en borrador, sin verificación humana. El ensayo de la defensa está pendiente.</p>
</div>
</div>
