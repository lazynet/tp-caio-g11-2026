---
owner: caio
status: draft
title: "Anexo A — Diagnóstico y punto de partida"
---

# Anexo A — Diagnóstico y punto de partida

Slide que sustenta: [Slide 2 — Punto de partida](../slides.md). El diagnóstico
también ordena las prioridades de [Slide 3 — Tesis](../slides.md).

> **Borrador sin verificación humana.** Todas las fichas de `context/` que cita
> este anexo están en `draft`; ninguna cifra es apta para el peer review ni para
> la entrega.

## Objetivo

Mostrar dónde está Acme Labs hoy en las cinco dimensiones de madurez de M1U1
([ficha](../../material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md)) y
de ahí sacar las dos o tres brechas que el plan ataca primero.

**El puntaje es una propuesta del CAIO a validar por el equipo, no un hecho.** Sale
de leer las fichas de `context/`, todas en `draft`, sin entrevistas ni encuestas
propias: el paso 2 del método de M1U1 (entrevistas y encuestas por nivel) no se
hizo. Responsable humano de validar el puntaje: **pendiente**.

## Supuestos de partida

| Supuesto | Valor | Fuente o tipo |
|---|---|---|
| Escala | 1 (Inicial) a 5 (Transformacional); el curso describe solo los niveles 1, 3 y 5 | [Ficha M1U1](../../material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md) |
| Cómo se lee un 2 | Entre el nivel 1 y el 3 descriptos: hay piezas del 3, pero sin formalizar ni medir | Criterio del CAIO, porque el curso no describe el 2 |
| Alcance | La organización completa: producto que se vende y operación interna | [Índice del caso](../../context/index.md) |
| Evidencia | Solo fichas de `context/` (hechos y supuestos anonimizados) | [Índice del caso](../../context/index.md) |
| Corte temporal | Datos hasta octubre de 2026; las cifras financieras, del cierre de agosto | [Situación económica](../../context/hechos/situacion-economica.md) |

## Evidencia

### Puntaje propuesto por dimensión

| Dimensión | Propuesta | Evidencia principal | Brecha frente al nivel 3 |
|---|---|---|---|
| Estrategia y liderazgo | 2 | Hay propuestas al Directorio sobre IA y un borrador de OKR 2027 con un objetivo de eficiencia con IA, pero la propuesta de oferta de IA sigue sin decidir y los OKR de la empresa son financieros y comerciales ([OKR](../../context/hechos/okrs-y-objetivos.md), [IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)) | Estrategia de IA aprobada, con dueño y atada a resultados del negocio |
| Datos e infraestructura | 2 | La infraestructura está cerca del 3: AWS en varias cuentas, Kubernetes, GitOps, observabilidad ([stack](../../context/hechos/stack-y-plataforma.md)). Los datos, no: sin inventario formal, y los datos productivos de clientes no se pueden usar ([datos](../../context/supuestos/disponibilidad-de-datos.md)) | Inventario de datos con dueño y calidad, y una capa común para servir casos de IA |
| Talento y cultura | 2 (Tecnología 3, Operaciones 1) | Tecnología: ~7 de cada 10 usan el agente de código. Operaciones: ~1 de cada 10, en buena parte porque el cliente fija las herramientas ([uso de IA](../../context/hechos/uso-ia-interno.md)). El piloto de abril (n=12, autoseleccionado) dio NPS +42, pero solo el 17% completó los cursos ([piloto](../../context/hechos/encuesta-y-pilotos-ia.md)). Capacidades críticas en pocas personas ([estructura](../../context/hechos/tamano-y-estructura.md)) | Capacitación por rol que se complete y suplentes para los roles críticos |
| Gobernanza y ética | 2 | Política de uso con clasificación en cuatro niveles y contrato para agentes de código, pero en borrador desde abril de 2026, sin matriz de clientes, sin inventario de casos ni registro de riesgos ([gobierno](../../context/hechos/gobierno-y-politica-ia.md)). ISO/IEC 27001 de la organización, sin controles específicos de IA verificados ([seguridad](../../context/hechos/seguridad-y-certificaciones.md)) | Política ratificada, inventario, registro de riesgos y comité operando |
| Adopción y valor | 1 en producto, 2 en interno | Cero IA en producción en lo que se vende ([IA en producto](../../context/hechos/ia-en-producto-y-oferta.md)). En lo interno hay uso alto en Tecnología y un piloto con criterios cumplidos, pero sin línea de base de productividad ([productividad](../../context/supuestos/ganancia-de-productividad.md)) | Un caso en producción con valor medido contra una línea de base |

No se promedia: un promedio de 2 esconde que la brecha más grande está en el
producto que se vende y en Operaciones.

### Hechos de contexto que condicionan el plan

| Hecho | Valor | Por qué importa | Fuente |
|---|---|---|---|
| Concentración de clientes | El principal pesa 40%-50% de la facturación; los cinco primeros, más del 90% | Lo que se haga con IA sobre un cliente grande es una decisión de riesgo comercial | [Cartera](../../context/hechos/cartera-y-concentracion.md) |
| Capacidad ociosa | Utilización facturable 83%-90%; bench menor a 1 FTE | Todo el plan compite con horas facturables | [Capacidad](../../context/hechos/capacidad-y-utilizacion.md) |
| Gasto de tecnología | De ~2% a ~4% de la facturación entre enero y agosto de 2026 | El OKR 2027 pide bajarlo a menos de 3,5% | [Costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Consumo real de IA | ~12 veces lo que se paga por suscripción en el agente de código | Un cambio de precio a consumo pega en el costo | [Costos](../../context/hechos/costos-tecnologia-e-ia.md) |
| Regulación de los clientes | El BCRA obliga a bancos y PSP a gobernar la IA propia y de terceros | Acme Labs es tercero: entra en el análisis de riesgo del cliente | [Regulación](../../context/hechos/regulacion-clientes-financieros.md) |
| Situación económica | Facturación mensual con un crecimiento cercano a 35% entre enero y agosto de 2026; EBITDA mensual de 21%-30% | Hay margen para invertir por etapas | [Situación económica](../../context/hechos/situacion-economica.md) |

### Brechas que el plan prioriza

Siguiendo el paso 6 de M1U1 (dos o tres brechas críticas), el CAIO propone:

1. **Gobernanza:** ratificar la política y armar la matriz de clientes. Es la
   condición para cualquier caso de IA en el producto ([Anexo C](03-gobierno-seguridad.md)).
2. **Datos y medición:** inventario de datos y línea de base de productividad,
   incidentes y costo. Sin línea de base no hay gates ([Anexo B](02-arquitectura.md)).
3. **Adopción y valor en el producto:** una hipótesis de producto elegida con
   RICE (un asistente de integración en la plataforma propia), diferida hasta
   que un cliente dé señal en la lectura de impacto del mes 6, con gate de scale o kill
   ([Anexo F](06-roadmap-riesgo.md)).

Talento y cultura no queda afuera: es el habilitador de las tres
([Anexo D](04-personas-cultura.md)). Igual que en el caso resuelto del curso, no
tiene base sólida sin estrategia y datos confiables.

## Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación | Disparador de abandono |
|---|---|---|---|---|
| El puntaje refleja documentos y no la práctica | Alta | Medio | Validar con 2-3 sesiones con referentes de cada área, como propone la versión extendida de M1U1 | Si la validación mueve dos o más dimensiones, se rehace el orden de prioridades |
| Las fichas de `context/` están en `draft` | Alta | Alto para la entrega | Verificación humana de las fichas que sostienen cada puntaje | Sin fichas `verified`, el diagnóstico no va a la versión de peer review como hecho |
| La telemetría solo mide el agente de código y subestima el uso en staff | Alta | Medio | Medir chat y Workspace en los meses 1-3 ([Anexo D](04-personas-cultura.md)) | — |
| Leer la baja adopción de Operaciones como problema cultural | Media | Medio | Separar lo contractual (el cliente fija herramientas) de lo cultural | — |

## Decisiones

- **Usar las cinco dimensiones de M1U1** y no la variante extendida (seis ejes de
  NovaGob y AIMM): son las que pide la cursada y AIMM sigue en `draft`
  ([huecos](../../material/huecos.md)). Reversible.
- **Puntuar producto e interno por separado** en Adopción y valor, y Tecnología y
  Operaciones por separado en Talento. Alternativa descartada: un solo número por
  dimensión, que esconde dónde está la brecha. Reversible.
- **Validar antes del peer review:** el equipo confirma o corrige los puntajes en
  una sesión; quien valida queda **pendiente**. Criterio de éxito: cada puntaje con
  al menos una ficha `verified` detrás.

## Cautelas

- Es un diagnóstico de escritorio, sin entrevistas.
- Los niveles 2 y 4 no están descritos en el curso; el 2 se usa como intermedio.
- Ninguna cifra de este anexo es apta para la entrega hasta que sus fichas pasen a
  `verified`.
