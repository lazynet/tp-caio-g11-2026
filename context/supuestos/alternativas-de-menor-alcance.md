---
type: Supuesto
title: "Alternativas de menor alcance y prueba chica de los meses 1-3"
description: "Composición propuesta de alternativas de gobierno y formación, piloto del agente actual y prueba chica, separadas del paquete mínimo vigente, con protocolo común sin equivalencia demostrada de controles o resultados."
status: draft
verified:
  by: human:lazynet
  at: 2026-10-20
  scope: "Martín confirmó la composición de las tres alternativas como comparación separada del paquete mínimo vigente: medición anual de 0,2 FTE y telemetría de 500-1.500 USD por trimestre; formación de 15-20 personas por 12 h; champions del piloto por 384 h anuales; y prueba con 40-80 h de diseño, 64 h de champions y 16-24 h de lectura. Incluye no presumir equivalencia de controles o resultados, revisar y costear legal antes de habilitar el piloto, conciliar capacidad y solapes antes de extender sin costo adicional, condicionar inicio en semana 5 o 9 a la base congelada y distinguir la rama de 199.000 USD del mínimo vigente. Productividad como hipótesis y prueba inicial de aprendizaje. Confirmado en esta conversación; no acredita disponibilidad, ejecución ni aprobación empresarial."
tags: [supuesto, finanzas, alternativas]
sources:
  - id: finanzas
    resource: "plan/annexes/05-business-case.md"
    title: "Anexo E, composición de las alternativas originales y prueba chica"
  - id: gobierno
    resource: "plan/annexes/03-gobierno-seguridad.md"
    title: "Anexo C, controles aplicables por superficie y compensatorios"
  - id: personas
    resource: "plan/annexes/04-personas-cultura.md"
    title: "Anexo D, formación completa y champions de las alternativas amplias"
  - id: costo-rol
    resource: "context/supuestos/costo-cargado-por-rol.md"
    title: "Supuestos de costo cargado por rol"
  - id: cohorte
    resource: "context/supuestos/desarrolladores-en-equipos-propios.md"
    title: "Supuestos de cohorte de 15-20 desarrolladores y costo cargado"
  - id: ganancia
    resource: "context/supuestos/ganancia-de-productividad.md"
    title: "Ganancia de productividad como hipótesis no medida"
  - id: uso-ia
    resource: "context/hechos/uso-ia-interno.md"
    title: "Uso informado de herramientas actuales y sus cautelas"
  - id: datos
    resource: "context/supuestos/disponibilidad-de-datos.md"
    title: "Disponibilidad de datos y habilitación de repositorios como supuestos"
  - id: resoluciones
    resource: "plan/annexes/07-resoluciones.md"
    title: "Anexo G, resoluciones del Directorio con autoridad, hito y consecuencia"
generated: { by: codex/gpt-6, at: 2026-10-20 }
---
# Supuesto

Estas alternativas se conservan para comparar alcances; no son el paquete
mínimo vigente. Proponen un protocolo común de medición, sin demostrar
equivalencia de controles o resultados.[^finanzas]

Para las comparaciones anuales se supone una base prospectiva congelada en las
semanas 1-4, con la unidad del anexo B; la serie retrospectiva solo estima
tendencia y ruido. Se presupuestan telemetría de herramientas actuales por
500-1.500 USD por trimestre y 0,2 FTE de DevOps/QA durante 12 meses para contar
y leer intervalos: 0,2 × 160 × 12 = 384 h.[^finanzas]

| Componente | Gobierno mínimo y formación | Piloto sobre el agente de código | Prueba chica de los meses 1-3, dentro del paquete |
|---|---|---|---|
| Gobierno | Controles del Anexo C y legal externo; sin presumir que el presupuesto original cubre todos los controles aplicables | Matriz de clientes y política existente; el costo original no incluye legal, cuya necesidad y costo deben revisarse antes de habilitar | Controles aplicables del paquete, sujetos a prueba |
| Formación | La del Anexo D completa (básico, intermedio, avanzado, champions, líder del programa) | Intermedio de la cohorte de 15-20 personas × 12 h = 180-240 h (210 h en el punto medio de 17,5) y 2 champions de Tecnología al 10% durante 12 meses = 384 h | Propone usar el intermedio de Tecnología como vehículo; que no sume horas requiere confirmar agendas y solapes |
| Prácticas sobre el agente de código | Las que traiga la formación | Contrato de agente, skills y guía de revisión: 40-80 h de tech lead | Las mismas 40-80 h, más 2 champions al 10% durante 2 meses (64 h) y 16-24 h de lectura de DevOps/QA al cierre de los meses 1-3 |
| Plataforma, contractor, pasarela, demostración externa | No | No | No se incorpora compra adicional por la prueba; los demás componentes del paquete requieren decisión separada |

La composición proviene de las alternativas del anexo E, la formación del
anexo D y los controles del anexo C. Tener política y matriz no prueba que el
uso esté habilitado.[^finanzas][^personas][^gobierno]

Los costos por hora salen del [costo por rol](/supuestos/costo-cargado-por-rol.md)
sobre 160 h por mes, y las horas de la cohorte, del costo por desarrollador de
[N y costo](/supuestos/desarrolladores-en-equipos-propios.md).[^costo-rol][^cohorte]

En la rama sin señal del paquete completo se propone extender la prueba como
piloto acotado, reutilizando diseño, champions y formación. La extensión sin
costo adicional es una hipótesis: requiere comprobar capacidad, controles y
solapes, incluida la lectura de 16-24 h frente al 0,2 FTE de medición ya
previsto. No se suma ni se absorbe trabajo automáticamente.[^finanzas][^gobierno]

La prueba empieza en semana 5 solo si la base se congela en semana 4; si la
base se extiende a semana 8, empieza en semana 9 y se revisa completitud en M3.
La prueba inicial compra aprendizaje, sin atribuir mejora de productividad.[^finanzas]

Los aproximadamente 199.000 USD del año sin señal corresponden a una rama del
paquete completo anterior, no al presupuesto del mínimo vigente. No son un
techo aprobado ni un costo transferible entre alcances.[^finanzas]

El piloto acotado trabaja solo sobre repositorios que la matriz habilite: sin datos de
clientes ([disponibilidad de datos](/supuestos/disponibilidad-de-datos.md)).
Esa habilitación y los controles deben comprobarse antes de usarlo.[^datos][^gobierno]

Las alternativas ampliadas no se piden: quedan como antecedente. Si una se
reactivara, decide el Directorio con una estimación común del CFO; antes de
iniciarla, Personas confirma champions y agendas y el Responsable de seguridad
habilita repositorios según la matriz. Sin esas dos confirmaciones, no se
ejecuta (R-28).[^resoluciones]

# Por qué es razonable

- Se propone reutilizar el agente de código informado en uso en Tecnología
  (ver [uso de IA](/hechos/uso-ia-interno.md)), sin seats nuevos. Esto no prueba
  suficiencia de licencias ni ausencia de otros costos incrementales.[^uso-ia]
- La [ganancia de productividad](/supuestos/ganancia-de-productividad.md) se
  plantea como hipótesis sobre el uso sistemático del agente con contrato de
  agente, skills y compuertas de calidad; el piloto no acredita esa ganancia.[^ganancia]
- Las piezas del gobierno mínimo y formación son renglones que los Anexos C y D ya costean; acá solo se
  arman de otra forma, sin demostrar equivalencia de controles ni costo
  completo para cada superficie habilitada.[^finanzas][^gobierno][^personas]

# Qué lo invalidaría

- Que medir sin el esfuerzo técnico del Anexo B cueste bastante más que 0,2 FTE
  (por ejemplo, si el historial de PR no alcanza y hay que instrumentarlo).
- Que la matriz no habilite repositorios suficientes para una cohorte de 15
  personas activas: el piloto acotado y la prueba chica se achican o no arrancan.
- Que el intermedio de Tecnología no pueda usarse como vehículo de la prueba y
  las horas de la cohorte se sumen.
- Que extender la prueba en M4-M12 pida champions, controles o lectura por
  encima de lo presupuestado: esa rama debe volver a costearse y autorizarse.

# Cautelas

- No hay dato de qué fracción de la ganancia se logra sin la plataforma: el
  Anexo E la trata como variable de sensibilidad (0 a 1), sin valor puntual.
- Los montos están en el Anexo E; esta ficha fija la composición.
- Las 40-80 h de diseño, 64 h de champions de la prueba (2 × 10% × 160 h ×
  2 meses) y 16-24 h de lectura son supuestos de diseño, sin medición.
- La verificación registra revisión humana de las alternativas, sin aprobar
  presupuesto, agendas, controles, contratación ni ampliación del mínimo.

[^finanzas]: Anexo E, composición de las tres opciones originales, prueba chica y secuencia condicionada a la base; rama sin señal de aproximadamente 199.000 USD, separada del mínimo vigente y sin equivalencia demostrada de alcances.
[^gobierno]: Anexo C, controles aplicables y compensatorios por superficie; su necesidad y costo deben conciliarse antes de habilitar usos o extender la prueba.
[^personas]: Anexo D, formación completa y champions de las alternativas de mayor alcance; si una alternativa se reactivara, Personas confirma champions y agendas antes de iniciarla y, sin esa confirmación, no se ejecuta (R-28).
[^costo-rol]: Costo cargado por rol, rangos supuestos y convención de 160 h mensuales para costear.
[^cohorte]: Cohorte supuesta de 15-20 desarrolladores de equipos propios; el punto medio 17,5 es una convención de cálculo, no una cantidad observada.
[^ganancia]: Ganancia de productividad como hipótesis no medida, sin beneficio atribuible demostrado por el piloto.
[^uso-ia]: Uso informado de herramientas actuales, con las cautelas de población y capacidad de la ficha.
[^datos]: Disponibilidad de datos y repositorios como supuesto de habilitación; el Responsable de seguridad habilita los repositorios según la matriz de restricciones antes de iniciar y, sin habilitación, no se usan (R-28).
[^resoluciones]: Anexo G, registro único de resoluciones del Directorio: qué se decide, autoridad, hito, consecuencia y tipo de cada R-xx.
