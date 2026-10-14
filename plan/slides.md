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
     viene de un anexo y de fichas en draft. -->

<!-- _class: lead -->

# Plan Maestro CAIO 2027: IA que se vende y se gobierna

**Acme Labs** · software para bancos, fintechs y grandes empresas

Grupo 11 · Diplomatura CAIO · UTN BA · caso propuesto, borrador sin verificación humana

**Lo que pedimos hoy (G0):** T1 con techo de 32 mil USD de caja y 1,6 FTE clave, el marco de gates y la elección de cómo se cubre T2-T4. No el año.

---

# Punto de partida: rentable, concentrada y sin IA en lo que vende

| Dimensión (M1U1) | Propuesta | Lo que la explica |
|---|---|---|
| Estrategia | 2 | Propuestas de IA sin decidir |
| Datos e infraestructura | 2 | Buena nube, datos sin inventario |
| Talento y cultura | 2 | Tecnología ~7 de 10 usan IA; Operaciones ~1 de 10 |
| Gobernanza | 2 | Política en borrador desde abril de 2026 |
| Adopción y valor | 1-2 | Cero IA en producción en el producto |

El cliente principal pesa 40%-50% de la facturación y la utilización es 83%-90%.

**Decisión:** validar el diagnóstico como base del plan. Ver [Anexo A — Diagnóstico](annexes/01-diagnostico.md).

---

# Tesis: dos frentes sobre una base, financiados por etapas

- **IA en el producto** que se vende a bancos y fintechs: un piloto acotado, solo con señal de un cliente.
- **IA en la operación interna:** de uso alto en Tecnología a uso medido en toda la empresa.
- **Una base común:** gateway neutral al modelo, gobierno ratificado y línea de base congelada.

No se paga con productividad sola: compra cobertura de precio, licencia para venderles a bancos y la opción de un ingreso.

**Decisión:** el pedido G0 único (T1, techos, gates y capacidad de T2-T4). Ver [Anexo F — Roadmap ajustado por riesgo](annexes/06-roadmap-riesgo.md) y [Anexo E — Business case](annexes/05-business-case.md).

---

# Arquitectura: un gateway, dos frentes, cero datos de cliente

- Gateway con **≥2 proveedores**, ruteo por nivel de dato y registro de costo.
- Aislamiento por cliente y harness con evals en CI y gate humano.
- 3 de las 4 superficies de IA de hoy pueden no pasar por el gateway: control compensatorio probado en T2.
- Sin fine-tuning ni datos productivos de clientes en los 12 meses.

| Aprobar en G0 | Se libera en G1-G2 | No aprobar todavía |
|---|---|---|
| T1: inventario, línea de base, matriz de superficies, telemetría | Gateway y harness (T2); piloto de T3 con matriz, política y señal | Modelo propio y contratos de más de 12 meses |

**Decisión:** solo la columna de la izquierda. Ver [Anexo B — Arquitectura](annexes/02-arquitectura.md).

---

# Gobierno que habilita, no que frena

- **AI Council de 5 asientos** dentro del comité de tecnología, con CoE virtual.
- Intake en 3 niveles: respuesta en 5 días hábiles para el riesgo medio.
- Secretos y datos prohibidos, siempre bloqueados; el primer secreto expuesto ya dispara la contención.
- Autonomía en el producto: L1-L2 en los 12 meses.

**Decisiones:**
1. Ratificar la política de IA en T1: compromiso interno, enmendable.
2. Sin crédito ni scoring en 12 meses; el resto, clasificado caso por caso.
3. Financiar los controles por gate.

Ver [Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md).

---

# Personas: capacitar y reasignar, no contratar

- El piloto mostró que la gente valora la IA (NPS +42) y que falló la capacitación: 17% completó los cursos.
- Formación por rol, en horario laboral, con champions con tiempo asignado.
- Se mide **uso real semanal por área**, no seats comprados.
- Ni las metas del plan llegan al 80% combinado del OKR: publicamos Tecnología y Operaciones habilitadas por separado.

**Decisiones:** capacitar en vez de contratar; IA aplicada de T1 con **un** contractor a prueba, que choca con "no contratar", o un rol interno demostrado. Y si hay compromiso sobre el empleo.

Ver [Anexo D — Personas y cultura](annexes/04-personas-cultura.md).

---

# Roadmap: cada trimestre se gana el siguiente

| Gate | Pasa si… | Espera | Corta |
|---|---|---|---|
| G1 | Base congelada, política, matriz, básico ≥90% | 6 semanas para completar | Sin política o matriz: no hay producto en el año |
| G2 | Throughput ≥ +3%; Tecnología ≥80%; señal de cliente | 0 a +3% o 60%-80%: T3 sin escalado | Sin mejora: base mínima. Sin señal: producto diferido |
| G3 | Throughput ≥ +8%; SLO del piloto, si sigue | +5% a +8%: solo base mínima | Menos de +5%: corte del frente interno |
| G4 | Camino a ~23% de throughput o interés contractual | — | Queda solo el frente interno |

**Decisión:** adoptar los gates por condición como regla de liberación de fondos. Ver [Anexo F — Roadmap](annexes/06-roadmap-riesgo.md).

---

# Business case: un año de inversión con salida acotada

| | Año 1 (miles de USD) |
|---|---|
| Caja incremental, con contingencia | 114-314 |
| Tiempo reasignado, a costo cargado | 150-408 (~4,5 FTE) |
| Pedido G0 (T1) | hasta 32 de caja y 61 de tiempo |
| Cortar en G1 | 73 en el medio, hasta 106 (caja: 27, hasta 38) |

- ROI a 12 meses negativo en los tres escenarios; beneficio de caja: cero.
- Equilibrio a régimen: **~23% de throughput, por encima** del +20% del OKR. Cumplir la meta no alcanza.
- A 12× de consumo, 211-267 por año: exposición de la empresa, con o sin plan.

**Decisión:** el pedido G0 y el resto por gates. Ver [Anexo E — Business case](annexes/05-business-case.md).

---

# Riesgos: lo irreversible espera a G4

| Escenario | Qué pasa |
|---|---|
| Pesimista con gates | Corte en G2: ≈ −245 (sin frenar: −481) |
| Base | G4 con frente interno y piloto evaluado |
| Optimista | En G4 se decide el primer contrato, que rige después |

**Irreversibles, decididos en G4 y vigentes después:** datos de cliente a un modelo, contrato de IA con un cliente, L3 en producto, compromisos de más de 12 meses.

**Abierto:** T2-T4 no entra en el sobre de tiempo. Ampliarlo a ~3,7 FTE clave o diferir el producto hasta la señal de cliente.

**Decisión:** elegirlo en G0; proponemos diferir, con ampliación condicionada en G2. Ver [Anexo F](annexes/06-roadmap-riesgo.md) y [Anexo E](annexes/05-business-case.md).

---

# Equipo y cómo hicimos este plan

Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo

Responsables por sección: **pendiente** de acordar en el equipo.

**Usamos el modelo operativo que proponemos:** roles (CAIO, arquitectura, gobierno, personas, finanzas) asumidos por agentes, una revisión adversarial del board y chequeos automáticos de fuentes y de fuga de datos.

**Trazabilidad:** cada cifra remonta a un anexo; las fichas siguen en borrador, sin verificación humana. Defensa: storyline y banco de objeciones; el ensayo está pendiente.

**Decisión:** ninguna; es el equipo que responde. Anexos A a F.
