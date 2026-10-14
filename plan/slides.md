---
owner: caio
status: draft
marp: true
paginate: true
size: 16:9
style: |
  section { font-size: 23px; padding: 48px 60px; }
  h1 { font-size: 36px; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 46px; }
---

<!-- Fuente única del deck. Nunca edites un deck generado: corré scripts/build-deck.sh.
     Una slide por `---`, con un título `#` cada una. Máximo 10 slides. Cada slide dice
     qué decisión le pide al board y apunta a su anexo. Borrador del CAIO: toda cifra
     viene de un anexo y de fichas en draft. El pedido G0 completo vive solo en la
     slide 8; las demás piden su parte. -->

<!-- _class: lead -->

# Plan Maestro CAIO 2027: IA que se vende y se gobierna

**Acme Labs** · software para bancos, fintechs y grandes empresas

Grupo 11 · Diplomatura CAIO · UTN BA · caso propuesto, borrador sin verificación humana

**Lo que pedimos hoy (G0):** tres meses con techo y una prueba chica, el piso de capacidad y la regla de gates. No el año: la plataforma se gana con una señal en G1. El detalle, en la slide 8.

---

# Punto de partida: rentable, concentrada y sin IA en lo que vende

| Dimensión (M1U1) | Propuesta | Lo que la explica |
|---|---|---|
| Estrategia | 2 | Propuestas de IA sin decidir |
| Datos e infraestructura | 2 | Buena nube, datos sin inventario |
| Talento y cultura | 2 | Agente de código: Tecnología ~7 de 10; Operaciones ~1 de 10 |
| Gobernanza | 2 | Política en borrador desde abril de 2026 |
| Adopción y valor | 1-2 | Cero IA en producción en el producto |

El cliente principal pesa 40%-50% de la facturación y la utilización es 83%-90%.

**Decisión:** validar el diagnóstico como base del plan. Ver [Anexo A — Diagnóstico](annexes/01-diagnostico.md).

---

# Tesis: gobierno y formación primero; la plataforma, con una señal

- **Siempre:** gobierno ratificado, línea de base congelada, formación para toda la empresa y una prueba chica con el agente de código que ya se usa.
- **Solo con una señal en G1:** la plataforma (gateway neutral al modelo, controles con bloqueo, harness y evals), por precio, contrato o cliente.
- **IA en el producto, diferida hasta la señal de un cliente:** un asistente de integración en la plataforma propia, L1 y sin datos de clientes. Le ganó en RICE a dos alternativas (puntajes propuestos, sin medir).

Con productividad sola, las opciones baratas ganan el año 1. La plataforma compra opciones (cobertura de precio, un ingreso y licencia para venderles a bancos, si T1 la confirma) y se paga solo si una prende.

**Decisión:** adoptar la tesis: la plataforma se gana en G1 y el producto, en G2. Ver [Anexo F — Roadmap ajustado por riesgo](annexes/06-roadmap-riesgo.md).

---

# Arquitectura: un gateway si hay señal, cero datos de cliente

- Gateway con **≥2 proveedores**, ruteo por nivel de dato y registro de costo.
- Aislamiento por cliente y harness con evals en CI y gate humano.
- Fuera del gateway, control compensatorio probado en T2; el agente de código entra solo si no rompe la suscripción.
- Sin fine-tuning ni datos productivos de clientes en los 12 meses.

| Aprobar en G0 | Se libera en G1-G2, solo con señal | No aprobar todavía |
|---|---|---|
| T1: inventario, línea de base, matriz de superficies, telemetría, prueba chica | Gateway, harness y prueba de portabilidad y costo (T2); piloto de T3 | Modelo propio y contratos de más de 12 meses |

**Decisión:** solo la columna de la izquierda. Ver [Anexo B — Arquitectura](annexes/02-arquitectura.md).

---

# Gobierno que habilita, no que frena

- **AI Council de 5 asientos** dentro del comité de tecnología, con CoE virtual.
- Intake en 3 niveles: respuesta en 5 días hábiles para el riesgo medio.
- Secretos y datos prohibidos: bloqueo técnico en la pasarela (con señal en G1) y en el equipo; en chat, IDE y suite, solo control compensatorio, con residual que acepta el Council. El primer secreto expuesto dispara la contención.
- Autonomía en el producto: L1-L2 en los 12 meses.

**Decisiones:**
1. Ratificar la política de IA en T1: compromiso interno, enmendable.
2. Sin crédito ni scoring en 12 meses; el resto, clasificado caso por caso.
3. Financiar los controles por gate: gobierno mínimo siempre; controles técnicos de la plataforma si G1 encuentra una señal; la demostración externa (red team externo e ISO ampliada), solo con señal contractual en G3 o si G2 libera el producto.

Ver [Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md).

---

# Personas: capacitar y reasignar, no contratar

- En el piloto de abril (n=12, autoseleccionado) el uso fue alto (NPS +42) y la capacitación falló: solo 17% completó los cursos. Es una señal, no una medición de toda la organización: la base de T1 la mide.
- Formación por rol, en horario laboral, con champions con tiempo asignado.
- Se mide **uso real semanal por área**, no seats comprados.

**Decisiones:** capacitar en vez de contratar; IA aplicada de T1 con **un** contractor a prueba (T1 en G0; T2-T4, solo con señal en G1), que choca con "no contratar", o un rol interno demostrado. La postura sobre el empleo: un compromiso con excepciones.

**OKR 2027, con el presupuesto, no en G0:** (1) el 80% combinado no se alcanza ni con las metas del plan (72,5% como mucho): proponemos reemplazarlo por Tecnología ≥80% y Operaciones habilitadas, cada una con su denominador y el 80% combinado informado al lado. (2) Gasto de tecnología bajo 3,5% de la facturación: mantenerlo y recortar el plan, o medirlo sin la inversión del plan o por persona activa. Cambia cómo se mide, no lo que se gasta.

Ver [Anexo D — Personas y cultura](annexes/04-personas-cultura.md).

---

# Roadmap: la plataforma se gana con una señal en G1

| | T1 → G1 | T2 → G2 | T3 → G3 | T4 → G4 |
|---|---|---|---|---|
| Técnico y gobierno | Base, política, matriz, prueba chica | Con señal: gateway, evals, red team | Caso interno en L2 | Go/no-go de modelo propio |
| Cultural | Básico ≥90% | Operaciones y staff | Casos por rol | Tecnología ≥85% |
| Techo (caja / tiempo) | 33 / 72 | 71 / 106 | 59 / 78 | 95 / 69 |
| Pasa si | Base y política; **una señal libera la plataforma** | Throughput ≥ +3%; Tec. ≥80% | Throughput ≥ +8% | Camino a ~17% o interés contractual |

Miles de USD; T2-T4, rama con señal. **G1 no corta: decide la plataforma.** Sin señal de contrato, de precio por consumo o de cliente, T2-T4 sigue como gobierno mínimo y formación (≈ 199 en el año) y G2-G3 releen. Throughput: límite inferior del intervalo; calidad incierta cuenta como espera. G2 en espera: nueva medición a las 6 semanas y, si sigue en la banda, corta el frente interno. G3 en espera: T4 con la base mínima.

**Decisión:** adoptar los gates como regla de liberación de fondos. Ver [Anexo F — Roadmap](annexes/06-roadmap-riesgo.md).

---

# Business case: lo barato gana el año 1; la plataforma, con señal

| Miles de USD | Sin señal en G1 | Con señal en G1 |
|---|---|---|
| Costo económico del año | ≈ 199 | ≈ 400 (216-584) |
| Caja, con contingencia | ≈ 39 | 98-255 (114-314 si G2 libera el producto) |
| Tiempo reasignado, a costo cargado | ≈ 160 | 115-320 (~3,5 FTE), más ~6 de la prueba |

ROI a 12 meses negativo y caja cero. **En el año 1 ganan las alternativas baratas:** gobierno mínimo y formación, 161 (neto −161 a −99); piloto sobre el agente actual, 47 (−47 a +15); paquete, 394 (−332).

**Decisión, el pedido G0 completo:**
1. T1 con la prueba chica: 33 de caja (contractor, solo T1: hasta 16,5) y 6 de reserva de cierre; 72 de tiempo (~1,8 FTE clave, ~654 h).
2. Piso: ~1,8 FTE clave en T1; con señal, 2,2 / 2,2 / 2,1 en T2-T4 con el replan (respaldo: 2,5 en T2).
3. G1 libera la plataforma solo con señal, y solo entonces amplía la reserva a 15 (sin señal, queda en 6). Cortar en G1: 79 en el medio, 115 hasta cerrar, 155 en el año.
4. Si se corta, base mínima hasta 41 de tiempo; T0, propuesto, hasta 7.

Ver [Anexo E — Business case](annexes/05-business-case.md).

---

# Riesgos: sin señal, el año cuesta la mitad; lo irreversible espera a G4

| Escenario | Qué pasa | Costo económico | Capacidad liberada | Neto 12 m | ROI 12 m |
|---|---|---|---|---|---|
| Sin señal en G1 | Sin plataforma en T2-T4 | ≈ 199 | ≥ φ × 62 | −199 a −137 | −100% a −69% |
| Pesimista, gates | Espera en G2, vence y corta | 265 | ~3 | ≈ −262 | ≈ −99% |
| Pesimista, sin frenar | Sin gates | 394 | 12 | −382 | −97% |
| Base | G2 y G3 pasan (o la espera vence) | 394 (265) | 62 (~19) | −332 (≈ −245) | −84% (≈ −93%) |
| Optimista | Producto en T3-T4 | 471 | 114 | −357 | −76% |

Miles de USD; salvo la primera fila, rama con señal y sin la prueba. φ: parte de la ganancia sin plataforma, sin dato (0 a 1). A 12× de consumo, 211-267 por año, con o sin plan (−502 sin frenar).

**Irreversibles, en G4 y vigentes después:** datos de cliente a un modelo, contrato de IA con un cliente, L3 en producto, compromisos de más de 12 meses.

**Decisión:** con señal, el replan de T2; la excepción de 0,3 FTE cubre solo la falta del 0,2 del contractor. Ver [Anexo F](annexes/06-roadmap-riesgo.md) y [Anexo E](annexes/05-business-case.md).

---

# Equipo y cómo hicimos este plan

Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo

Responsables por sección: **pendiente** de acordar en el equipo.

**Usamos el modelo operativo que proponemos:** roles asumidos por agentes, una revisión adversarial del board y chequeos automáticos de fuentes y de fuga de datos. Cada cifra remonta a un anexo; las fichas siguen en borrador, sin verificación humana. El ensayo de la defensa está pendiente.

**Resolución que proponemos:** el Directorio aprueba el G0 de la slide 8, T1 con la prueba chica, y adopta los gates: la plataforma se gana con una señal en G1 y el resto del año, trimestre a trimestre.
