---
okf_version: "0.2"
---

Caso propuesto, pendiente del acuerdo del equipo: **Acme Labs, la organización completa** (empresa argentina de
software para bancos, fintechs y grandes empresas). El plan cubre la IA en lo que
se vende a clientes y en la operación interna. Solo hay datos públicos, con su
URL, o datos internos anonimizados (alias, rangos, ratios, índices base 100); los
datos reales viven en `private/`.

# Hechos

Hechos sobre el caso en los que se apoya el plan (`type: Hecho`), uno por archivo.

* [Capacidad, utilización y bench](/hechos/capacidad-y-utilizacion.md) - La utilización facturable ronda el 83% con bench casi nulo: no hay capacidad ociosa, así que cualquier iniciativa de IA compite con horas facturables.
* [Cartera de clientes y concentración](/hechos/cartera-y-concentracion.md) - La facturación está muy concentrada: el cliente principal pesa entre 40% y 50%, los dos primeros cerca del 70% y los cinco primeros más del 90%, contra una meta interna de menos del 30% por cliente.
* [Costos de tecnología e IA](/hechos/costos-tecnologia-e-ia.md) - El gasto de tecnología se duplicó entre febrero y septiembre de 2026 y pasó de cerca de 2% a 4% de la facturación; la nube es la mayor parte, y el consumo real de IA equivale a unas doce veces lo que se paga por suscripción.
* [Encuesta y pilotos internos de IA](/hechos/encuesta-y-pilotos-ia.md) - El piloto de IA de abril de 2026 superó sus criterios de valor y falló en capacitación: alta frecuencia de uso y NPS de +42, pero la mitad no hizo ningún curso y casi nadie usa ejemplos al pedir.
* [Estructura de ingresos por línea de negocio](/hechos/estructura-de-ingresos.md) - Cerca del 40% de la facturación sale de un producto operado bajo suscripción para un solo cliente y otro tanto de staffing; el margen más alto está en el soporte a la plataforma propia.
* [Gobierno y política de IA existentes](/hechos/gobierno-y-politica-ia.md) - Acme Labs tiene una política de uso aceptable de IA con clasificación de datos y matriz de herramientas, pero sigue en borrador y con pendientes clave, como la matriz de restricciones de clientes.
* [IA en el producto y en la oferta a clientes](/hechos/ia-en-producto-y-oferta.md) - Acme Labs no tiene hoy IA en producción dentro de lo que vende; su posicionamiento en IA está en evaluación y depende de los productos propios.
* [Qué hace Acme Labs y para quién](/hechos/oferta-y-segmentos.md) - Acme Labs vende una plataforma de funcionalidades financieras y equipos de desarrollo a bancos, fintechs y grandes empresas, con oficinas en dos países de Latinoamérica.
* [OKR y objetivos de la organización y de Tecnología](/hechos/okrs-y-objetivos.md) - Los OKR de la empresa son financieros y comerciales; Tecnología prepara para 2027 objetivos de productos recurrentes, eficiencia con IA y una base técnica segura.
* [Regulación argentina que pesa sobre los clientes financieros](/hechos/regulacion-clientes-financieros.md) - Los bancos y proveedores de servicios de pago clientes de Acme Labs están obligados por el BCRA a gobernar el uso de IA propio y de terceros, y por ley a guardar secreto financiero y proteger datos personales.
* [Seguridad de la información y certificaciones](/hechos/seguridad-y-certificaciones.md) - La organización tiene un sistema de gestión de seguridad certificado; el producto propio de medios de pago todavía no tiene su propio sistema de gestión certificado.
* [Situación económica 2026](/hechos/situacion-economica.md) - La facturación creció cerca de 35% entre enero y agosto de 2026, con margen EBITDA de 21-30% mensual.
* [Stack y plataforma de delivery](/hechos/stack-y-plataforma.md) - Acme Labs desarrolla sobre Node/TypeScript, Java y Python, despliega en AWS con Kubernetes y GitOps, y gestiona el trabajo en GitHub y en la suite de Atlassian.
* [Tamaño y estructura de la organización](/hechos/tamano-y-estructura.md) - Acme Labs tiene entre 60 y 70 personas, con un modelo mixto de nómina y contractors, y cerca del 80% en Operaciones y Tecnología.
* [Uso actual de IA en la operación interna](/hechos/uso-ia-interno.md) - Acme Labs usa tres herramientas de IA generativa con licencia corporativa; la adopción es alta en Tecnología y baja en Operaciones y en las áreas de staff.

# Supuestos

Lo que el plan da por cierto sin una fuente que lo pruebe (`type: Supuesto`).
Cada uno dice por qué es razonable y qué lo invalidaría.

* [Apetito de riesgo de los clientes financieros frente a la IA](/supuestos/apetito-de-riesgo-de-clientes.md) - Se asume que los bancos y PSP clientes no van a permitir que su código ni sus datos pasen por modelos externos sin una cláusula contractual explícita y controles demostrables.
* [Base mínima que queda después de un corte](/supuestos/base-minima-tras-un-corte.md) - Si el plan se corta en un gate, se supone que la empresa conserva el resto del año un núcleo de gobierno (fracciones de liderazgo y seguridad más el comité) y la pasarela de salida si ya está instalada.
* [Capacidad de inversión para el plan de IA](/supuestos/capacidad-de-inversion.md) - El plan a 12 meses se diseña para una inversión incremental de entre 1% y 3% de la facturación anual, financiada con margen operativo y reasignación de tiempo, sin contrataciones masivas.
* [Capacidades que el plan da por ausentes](/supuestos/capacidades-ausentes.md) - El plan supone que hoy no existen un gateway de modelos, un inventario formal de arquitectura ni una función legal interna dedicada a IA, y presupuesta construirlos o contratarlos.
* [Continuidad de los clientes principales](/supuestos/continuidad-de-clientes-principales.md) - El plan da por hecho que los dos clientes principales siguen durante los 12 meses con un volumen similar; la concentración se trata como riesgo y no como escenario base.
* [Convenciones de calendario y de cálculo del plan](/supuestos/convenciones-de-calculo.md) - El plan usa T0 = cuarto trimestre de 2026, T1-T4 = los trimestres de 2027, la base de atribución congelada en las semanas 1-4 de T1, 480 horas de costeo por persona-trimestre, costo horario = costo mensual del rol / 160 y techos redondeados hacia arriba.
* [Costo de régimen del año 2](/supuestos/costo-de-regimen-del-ano-2.md) - Para evaluar el equilibrio más allá de los 12 meses se supone un costo de régimen anual de cerca de 63 mil USD de caja de la base común (infraestructura y pasarela), 30 mil más de consumo si el producto sigue, y 1,5 FTE de mantenimiento a costo de senior.
* [Costo mensual cargado por rol](/supuestos/costo-cargado-por-rol.md) - Para costear el plan se usan rangos de mercado argentinos de costo cargado mensual en dólares por rol, no la nómina real de Acme Labs.
* [Costos de cierre al cortar el plan en un gate](/supuestos/costos-de-cierre-por-corte.md) - Si el plan se corta en un gate, el cierre suma un mes de dedicación del contractor por preaviso y un mes de infraestructura de laboratorio, y legal y red team no comprometen gasto más allá del gate vigente.
* [Desarrolladores en equipos propios y su costo](/supuestos/desarrolladores-en-equipos-propios.md) - El caso de negocio supone entre 15 y 20 desarrolladores en equipos propios (valor de cálculo 17,5) con un costo cargado de USD 2.500-7.000 por mes (valor de cálculo 4.750).
* [Disponibilidad de datos para casos de IA](/supuestos/disponibilidad-de-datos.md) - Los datos utilizables a corto plazo son los internos de Acme Labs (código propio, tickets, documentación, telemetría y finanzas); los datos productivos de clientes no están disponibles para IA.
* [Ganancia de productividad por IA en ingeniería](/supuestos/ganancia-de-productividad.md) - El caso de negocio supone entre 10% y 25% más de throughput por desarrollador al cabo de 12 meses en los equipos propios, no en los equipos asignados a clientes.
* [Poblaciones y tiempos de capacitación en IA](/supuestos/poblaciones-de-capacitacion.md) - El people plan supone cerca de 65 personas en el nivel básico (6 h), 50 en el intermedio (12 h), unas 10 en el avanzado y una red de 8 champions con 10% de su jornada.
* [Precio de los modelos y dependencia de proveedor](/supuestos/precio-y-dependencia-de-modelos.md) - Se asume que el costo por unidad de capacidad de los modelos no sube en 12 meses, pero que el precio de las suscripciones planas puede ajustarse hacia el consumo real.
* [Precios de servicios externos sin cotización y contingencia](/supuestos/precios-externos-sin-cotizar.md) - Los costos externos del plan (asesoría legal, red team, auditoría, pasarela, infraestructura y consumo del piloto) son rangos del equipo sin cotización, y una contingencia de 15% sobre la caja cubre el error de precio de lo estimado, dentro del techo aprobado.
* [Rampa de la ganancia de productividad](/supuestos/rampa-de-la-ganancia.md) - La ganancia de throughput llega por tramos: en el escenario base, 0% del objetivo en T1, 25% en T2, 60% en T3 y 100% en T4; en el pesimista 0/10/30/60% y en el optimista 0/40/80/100%.
* [Sobre de capacidad separado en tiempo clave y distribuido](/supuestos/sobre-de-capacidad-separado.md) - Propuesta de Finanzas, todavía no aprobada: el tiempo de las personas clave se mide contra el sobre de 1 a 2,25 FTE, y las horas repartidas en toda la dotación forman un segundo sobre que el board aprueba en G0.
* [Umbral de evidencia contractual para la licencia para vender](/supuestos/umbral-de-evidencia-contractual.md) - Se propone que la licencia para vender IA a bancos cuente como señal solo si uno de los dos primeros clientes, o dos de los cinco primeros, piden evidencia de controles de IA como condición o puntaje de contratación o renovación dentro de 18 meses.
