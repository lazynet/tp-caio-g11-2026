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

**Lo que pedimos hoy (G0):** tres meses con techo, el piso de capacidad del año y la regla de gates. No el año. El detalle, en la slide 8.

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

- **Una base común:** gateway neutral al modelo, gobierno ratificado y línea de base congelada.
- **IA en la operación interna:** de uso alto en Tecnología a uso medido en toda la empresa.
- **IA en el producto, diferida hasta la señal de un cliente:** un asistente de integración en la plataforma propia, L1 y sin datos de clientes. Le ganó en RICE a dos alternativas (puntajes propuestos, sin medir).

No se paga con productividad sola: compra la opción de cobertura de precio (se confirma o se descarta en G2), la opción de un ingreso y, si la evidencia contractual de T1 la confirma, licencia para venderles a bancos.

**Decisión:** adoptar la tesis con el producto diferido. Ver [Anexo F — Roadmap ajustado por riesgo](annexes/06-roadmap-riesgo.md).

---

# Arquitectura: un gateway, dos frentes, cero datos de cliente

- Gateway con **≥2 proveedores**, ruteo por nivel de dato y registro de costo.
- Aislamiento por cliente y harness con evals en CI y gate humano.
- 3 de las 4 superficies de IA de hoy pueden no pasar por el gateway: control compensatorio probado en T2.
- Sin fine-tuning ni datos productivos de clientes en los 12 meses.

| Aprobar en G0 | Se libera en G1-G2 | No aprobar todavía |
|---|---|---|
| T1: inventario, línea de base, matriz de superficies, telemetría | Gateway, harness y prueba de portabilidad y costo (T2); piloto de T3 solo con señal | Modelo propio y contratos de más de 12 meses |

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
3. Financiar los controles por gate; la demostración externa (red team externo e ISO ampliada), solo con señal contractual en G3 o si G2 libera el producto.

Ver [Anexo C — Gobierno, seguridad y compliance](annexes/03-gobierno-seguridad.md).

---

# Personas: capacitar y reasignar, no contratar

- En el piloto de abril (n=12, autoseleccionado) el uso fue alto (NPS +42) y la capacitación falló: solo 17% completó los cursos. Es una señal, no una medición de toda la organización: la base de T1 la mide.
- Formación por rol, en horario laboral, con champions con tiempo asignado.
- Se mide **uso real semanal por área**, no seats comprados.
- Ni las metas del plan llegan al 80% combinado del OKR: publicamos Tecnología y Operaciones habilitadas por separado.

**Decisiones:** capacitar en vez de contratar; IA aplicada de T1 con **un** contractor a prueba, que choca con "no contratar", o un rol interno demostrado. Y la postura sobre el empleo: proponemos un compromiso con excepciones.

Ver [Anexo D — Personas y cultura](annexes/04-personas-cultura.md).

---

# Roadmap: cada trimestre se gana el siguiente

| | T1 → G1 | T2 → G2 | T3 → G3 | T4 → G4 |
|---|---|---|---|---|
| Técnico | Inventario, línea de base, telemetría | Gateway, evals, prueba de costo | Caso interno en L2; piloto si hay señal | Go/no-go de modelo propio |
| Gobierno | Política, matriz de clientes | Pasarela, bypass, red team | Cláusula tipo, sin firma | Red team externo, si hay señal |
| Cultural | Básico ≥90%, champions | Operaciones y staff | Casos por rol | Tecnología ≥85% |
| Techo (miles USD, caja / tiempo) | 33 / 62 | 71 / 106 | 59 / 78 | 95 / 69 |
| Pasa si | Base, política, básico ≥90% | Throughput ≥ +3%, Tecnología ≥80% | Throughput ≥ +8% | Camino a ~17% o interés contractual |

- **Espera:** se sigue sin escalar y se vuelve a medir; la de throughput en G2 vence a las 6 semanas y, si no mejora, corta.
- **Corta por frente:** sin política, no hay producto en el año; matriz ambigua al mes 4, sin piloto con ese cliente; debajo de la banda, queda la base mínima (en G3, el corte es del frente interno y de la base común); en G4, no se financia el régimen (~53 por año de base mínima).

**Decisión:** adoptar los gates como regla de liberación de fondos. Ver [Anexo F — Roadmap](annexes/06-roadmap-riesgo.md).

---

# Business case: un año de inversión con salida acotada

| Miles de USD | Año 1, producto diferido |
|---|---|
| Caja, con contingencia | 98-255 (114-314 si G2 libera el producto) |
| Tiempo reasignado, a costo cargado | 115-320 (~3,5 FTE) |
| Cortar en G1 | 73 en el medio; hasta 106 hasta cerrar y 146 en el año |

- ROI a 12 meses negativo en los tres escenarios; beneficio de caja: cero.
- Equilibrio a régimen: **~17% de throughput**, 3 puntos debajo del +20% del OKR: la meta lo cubre en el medio, sin certeza (~23% si se le carga el producto).

**Decisión, el pedido G0 completo:**
1. T1: hasta 33 de caja más 6 de reserva de cierre; hasta 62 de tiempo (1,6 FTE clave y 590 h distribuidas).
2. Piso de capacidad: 1,6 FTE clave en T1; 2,2 / 2,2 / 2,1 en T2-T4 con el replan de T2 (respaldo: 2,5 en T2).
3. Si se corta, base mínima hasta 41 de tiempo; T0, propuesto, hasta 7.

Ver [Anexo E — Business case](annexes/05-business-case.md).

---

# Riesgos: lo irreversible espera a G4

| Escenario | Qué pasa | Resultado del año (miles USD) |
|---|---|---|
| Pesimista con gates | Espera en G2; vence a las 6 semanas y corta | ≈ −262 (≈ −300 si la espera no venciera) |
| Pesimista sin frenar | Todo el año ejecutado | −382; −502 con precio a 12× desde T3 |
| Base | Producto diferido; G4 con el frente interno | ROI económico −84% |
| Optimista | Señal en G2; en G4 se decide el primer contrato | ROI económico −76% |

- A 12× de consumo, 211-267 por año: exposición de la empresa, con o sin plan.

**Irreversibles, decididos en G4 y vigentes después:** datos de cliente a un modelo, contrato de IA con un cliente, L3 en producto, compromisos de más de 12 meses.

**Decisión:** el replan de T2, con la excepción de 0,3 FTE como respaldo. Ver [Anexo F](annexes/06-roadmap-riesgo.md) y [Anexo E](annexes/05-business-case.md).

---

# Equipo y cómo hicimos este plan

Gabriela Temporale · Martin Vago · Pablo Ces · Eduardo Chaparro · Rafael Cioffi · Nicolás Tanos · Luciano De Corso · Maximiliano Zerr Morinigo

Responsables por sección: **pendiente** de acordar en el equipo.

**Usamos el modelo operativo que proponemos:** roles asumidos por agentes, una revisión adversarial del board y chequeos automáticos de fuentes y de fuga de datos. Cada cifra remonta a un anexo; las fichas siguen en borrador, sin verificación humana. El ensayo de la defensa está pendiente.

**Resolución que proponemos:** el Directorio aprueba el G0 de la slide 8 y adopta los gates; el resto del año se gana trimestre a trimestre.
