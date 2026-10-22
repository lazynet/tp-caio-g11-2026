---
type: Concepto
title: EU AI Act, obligaciones de alto riesgo y roles de proveedor y desplegador
description: Requisitos de los arts. 8-15, obligaciones del proveedor (arts. 16-21, 43, 47-49, 72, 73), del desplegador (arts. 26-27), cambio de rol por el art. 25, alfabetización del art. 4 y alcance territorial del art. 2.
tags: [compliance, regulacion, alto-riesgo, proveedor, desplegador, eu-ai-act]
sources:
  - id: eu-ai-act
    resource: EU AI Act 2024.pdf
    title: Reg. (UE) 2024/1689, arts. 2-4 (p. 45-51), 8-27 (p. 55-70), 43 (p. 78), 49 (p. 81), 72-73 (p. 101-102)
  - id: eu-ai-act-eurlex
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    title: Reg. (UE) 2024/1689 en EUR-Lex (fuente primaria)
  - id: ai-omnibus
    resource: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
    title: Reg. (UE) 2026/1744, Ómnibus digital sobre IA, DOUE L de 24.7.2026 (texto español, CELEX_32026R1744_ES_TXT.pdf)
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-21T20:13:00Z }
status: verified
verified:
  by: human:lazynet
  at: 2026-10-22
  scope: "Art. 3.3, art. 25.1 y Anexo III (puntos 3, 4 y 5.b) del Reg. 2024/1689, y art. 4.1 y considerando (8) del Reg. 2026/1744, cotejados contra el DOUE español (Cellar, 2026-10-22); el 2026/1744 no modifica 3.3, 25.1 ni el Anexo III. No cubre el resto de los artículos. Cotejo del agente revisado y confirmado por Martín en esta conversación."
---

# Alcance territorial (art. 2)

Acme Labs está fuera de la UE, pero el Reglamento no mira dónde está la
empresa. Aplica a (p. 45):[^eu-ai-act]

- **Proveedores que comercialicen o pongan en servicio sistemas en la UE**, estén
  donde estén (2.1.a).
- **Desplegadores establecidos en la UE** (2.1.b).
- **Proveedores y desplegadores de terceros países cuando el resultado de salida
  del sistema se use en la UE** (2.1.c). Es la cláusula de extraterritorialidad:
  un score calculado en Argentina cuyo resultado se usa para decidir sobre una
  persona en la UE queda dentro.
- Importadores, distribuidores, fabricantes de producto, representantes
  autorizados y personas afectadas ubicadas en la UE.

Un proveedor de un tercer país de GPAI debe nombrar representante en la UE
(art. 54, [niveles de riesgo](/frameworks/eu-ai-act-niveles-riesgo.md)).

**Cautela:** si los clientes de Acme Labs son bancos locales con clientes
locales, el Reglamento puede no aplicar de forma directa. Aplica si hay clientes
con operación en la UE o si el resultado se usa allá. El ejercicio de
clasificación hay que hacerlo por cliente y por caso de uso. Además, un cliente
que sí esté alcanzado va a trasladar las obligaciones por contrato.

# Proveedor y desplegador (art. 3)

| Rol | Definición | Qué hace |
|---|---|---|
| Proveedor (3.3) | Quien desarrolla un sistema de IA, o lo hace desarrollar, y lo introduce en el mercado o lo pone en servicio con su nombre o marca, pagando o gratis | Diseña y garantiza conformidad |
| Desplegador (3.4) | Quien usa un sistema de IA bajo su propia autoridad (salvo uso personal no profesional) | Opera el sistema conforme a las instrucciones |

Un banco que usa el motor de scoring de un tercero es **desplegador**; el
tercero es **proveedor**.[^eu-ai-act][^eu-ai-act-eurlex]

# Art. 4: alfabetización en IA

**Texto original (p. 51):** proveedores y desplegadores "adoptarán medidas para
garantizar que, en la mayor medida posible," su personal y quienes operan sistemas en
su nombre tengan "un nivel suficiente de alfabetización en materia de IA", según conocimientos,
experiencia, formación y contexto de uso. Aplica desde el 2 de febrero de
2025.[^eu-ai-act]

**Texto vigente tras el Omnibus (art. 4.1, p. 16):** "adoptarán medidas para
**apoyar la promoción** de la alfabetización en materia de IA de su personal y demás
personas que se encarguen en su nombre del funcionamiento y la utilización de
sistemas de IA", con los mismos criterios de conocimientos, experiencia, formación y
contexto de uso. Agrega: "Esta obligación no exige que los proveedores o los
responsables del despliegue garanticen un nivel específico de alfabetización en
materia de IA de ninguna persona en particular". La Comisión y los Estados miembros
apoyan y facilitan, "en particular de las pymes", y la Comisión publica ejemplos
prácticos (4.2); el Consejo de IA adopta recomendaciones según los marcos europeos
de competencias (4.3).[^ai-omnibus] La frase "apoyar el desarrollo" es del
considerando (8), no del artículo. El considerando dice que una obligación
estricta era una carga, en particular para las pequeñas empresas, y que la
alfabetización debe ser prioridad estratégica "independientemente de las
obligaciones reglamentarias y las posibles sanciones" (p. 3).[^ai-omnibus]

Para el plan: es un piso de people plan que ya rige hoy; ver
[M3U2](/unidades/m3u2-cambio-literacy.md).

# Requisitos de los sistemas de alto riesgo (arts. 8-15)

Los exige el proveedor (sección 2 del cap. III):[^eu-ai-act]

| Art. | Requisito | Puntos clave | Pág. |
|---|---|---|---|
| 9 | Gestión de riesgos | Proceso iterativo durante todo el ciclo de vida: identificar y estimar riesgos con uso previsto y mal uso previsible, incorporar datos poscomercialización, medidas de mitigación, pruebas previas a la salida con umbrales definidos; atender a menores de 18 y colectivos vulnerables | 56-57 |
| 10 | Datos y gobierno de datos | Datasets de entrenamiento, validación y prueba pertinentes, representativos y con propiedades estadísticas adecuadas; examinar y mitigar sesgos; origen, preparación y lagunas documentados | 57-58 |
| 11 | Documentación técnica | Elaborada antes de comercializar y actualizada; contenido mínimo del Anexo IV; formulario simplificado para PyMEs | 58 |
| 12 | Registros (logs) | Registro automático de eventos durante toda la vida del sistema, que permita detectar riesgos y vigilar el funcionamiento | 59 |
| 13 | Transparencia | Instrucciones de uso: identidad del proveedor, finalidad, precisión y métricas, solidez, ciberseguridad, riesgos conocidos, supervisión humana, vida útil y mantenimiento | 59-60 |
| 14 | Supervisión humana | Interfaz que permita entender límites, tener conciencia del sesgo de automatización, interpretar resultados, ignorar o revertir la salida y detener el sistema (botón de parada) | 60-61 |
| 15 | Precisión, solidez y ciberseguridad | Niveles declarados en las instrucciones; robustez ante errores; mitigar bucles de retroalimentación; resistencia a envenenamiento de datos y de modelos, ejemplos adversarios y ataques a la confidencialidad | 61 |

El art. 10.5 permitía tratar categorías especiales de datos para detectar
sesgos bajo seis condiciones; el Omnibus suprime el 10.5 y lo reemplaza por un
nuevo **art. 4 bis** (p. 17 y 19) con condiciones equivalentes (sólo si es estrictamente necesario, sin alternativa
sintética o anonimizada, con seudonimización, acceso controlado, sin
transferencia a terceros y borrado una vez corregido el sesgo). El 4 bis.2 extiende
la posibilidad a los desplegadores y a otros sistemas y aclara que "no crea
obligación alguna" de detectar y corregir sesgos.[^eu-ai-act][^ai-omnibus]

# Obligaciones del proveedor (art. 16 y siguientes)

El art. 16 (p. 62) lista doce obligaciones:[^eu-ai-act]

1. Cumplir los requisitos de arts. 8-15.
2. Indicar nombre, marca y dirección de contacto en el sistema o su documentación.
3. Tener un **sistema de gestión de calidad** (art. 17).
4. Conservar documentación (art. 18).
5. Conservar los logs bajo su control (art. 19).
6. Pasar la **evaluación de conformidad** antes de comercializar (art. 43).
7. Redactar la **declaración UE de conformidad** (art. 47).
8. Colocar el **marcado CE** (art. 48).
9. **Registrarse y registrar el sistema** en la base de datos de la UE (art. 49).
10. Adoptar medidas correctoras e informar (art. 20).
11. Demostrar conformidad ante la autoridad que lo pida.
12. Cumplir accesibilidad.

## Sistema de gestión de calidad (art. 17, p. 62-63)

Documentado en políticas, procedimientos e instrucciones. Debe incluir, como
mínimo: estrategia de cumplimiento y gestión de cambios, técnicas de diseño,
desarrollo y control de calidad, procedimientos de prueba y validación, normas
técnicas aplicadas, gestión de datos, gestión de riesgos (art. 9), vigilancia
poscomercialización (art. 72), procedimiento de notificación de incidentes graves
(art. 73), gestión de la comunicación con autoridades, registro documental,
gestión de recursos y un **marco de rendición de cuentas** del personal
directivo. Se aplica en proporción al tamaño del proveedor (17.2), con refuerzo
del Omnibus para PyMEs y small mid-caps.[^eu-ai-act][^ai-omnibus]

## Conservación y cooperación

| Qué | Plazo o regla | Art. |
|---|---|---|
| Documentación técnica, QMS, declaración UE de conformidad | **10 años** desde la comercialización | 18 |
| Logs generados automáticamente (bajo control del proveedor) | Al menos **6 meses**, salvo otra norma (por ejemplo, protección de datos) | 19 |
| Medidas correctoras | Inmediatas si hay no conformidad: corregir, retirar, desactivar o recuperar, e informar | 20 |
| Cooperación con autoridades | Entregar información y accesos a logs ante solicitud motivada | 21 |

## Evaluación de conformidad (art. 43, p. 78)

- Anexo III puntos 2 a 8 (incluye scoring y seguros): **control interno
  (Anexo VI)**, sin organismo notificado.
- Anexo III punto 1 (biometría): control interno o, si no hay normas armonizadas
  o no se las aplicó, evaluación con organismo notificado (Anexo VII).
- Una **modificación sustancial** obliga a repetir la evaluación. Los cambios
  predeterminados y documentados en la evaluación inicial de un sistema que sigue
  aprendiendo no cuentan como sustanciales.[^eu-ai-act]

## Registro (art. 49, p. 81-82)

El proveedor registra el sistema y a sí mismo en la base de datos de la UE antes
de comercializarlo, **incluso cuando concluyó que no es de alto riesgo** por el
art. 6.3 (49.2). Los desplegadores que son autoridades públicas también se
registran (49.3).[^eu-ai-act]

## Vigilancia poscomercialización (art. 72, p. 101)

Sistema proporcional y documentado que recolecta y analiza datos de desempeño
durante toda la vida útil, sobre la base de un plan que forma parte de la
documentación técnica (Anexo IV). El texto de 2024 pedía a la Comisión un acto de
ejecución con el modelo del plan, a más tardar el 2 de febrero de 2026 (p. 101). El
Omnibus cambia el instrumento y la fecha: la Comisión "adoptará orientaciones —que
incluirán un modelo— sobre el plan de seguimiento poscomercialización a más tardar
el **2 de septiembre de 2027**" (art. 1 punto 30, p. 26).[^eu-ai-act][^ai-omnibus]

## Incidentes graves (art. 73, p. 101-102)

Incidente grave (art. 3.49): fallecimiento o daño grave a la salud; alteración
grave e irreversible de infraestructuras críticas; **incumplimiento de
obligaciones del derecho de la UE que protegen derechos fundamentales**; daños
graves a la propiedad o al ambiente.[^eu-ai-act]

| Caso | Plazo de notificación a la autoridad de vigilancia del mercado |
|---|---|
| General | Inmediatamente tras establecer el nexo causal (o su probabilidad razonable) y a más tardar **15 días** desde que se conoce |
| Infracción generalizada o infraestructura crítica | Inmediato y a más tardar **2 días** |
| Fallecimiento | Inmediato y a más tardar **10 días** |

Se permite una notificación inicial incompleta. Hasta investigar, el proveedor
no puede modificar el sistema de un modo que afecte el análisis de causas sin
avisar a la autoridad (73.6). Si el proveedor ya está sujeto a obligaciones de
información equivalentes, solo notifica los incidentes del 3.49.c (73.9). Para
bancos, un fallo de scoring discriminatorio puede configurar justamente el
supuesto c.[^eu-ai-act]

# Cadena de valor (art. 25)

Un distribuidor, importador, desplegador o tercero **pasa a ser proveedor** y
asume el art. 16 cuando (p. 67):[^eu-ai-act]

- (a) **pone su nombre o marca** a un sistema de alto riesgo ya comercializado,
  salvo acuerdo contractual que reparta las obligaciones de otro modo;
- (b) hace una **modificación sustancial** de un sistema de alto riesgo y sigue
  siéndolo;
- (c) **cambia la finalidad prevista** de un sistema (incluido un GPAI) no
  considerado de alto riesgo, de modo que pase a serlo.

Para Acme Labs, el escenario (a) aparece si revende o integra con marca propia
un motor de terceros, y el (c) si toma un modelo genérico o una herramienta y lo
orienta a evaluar solvencia: **un LLM usado para decidir crédito es alto
riesgo**, y quien lo orienta a eso es el proveedor.

El proveedor original deja de serlo para ese sistema y debe cooperar (25.2); el
Omnibus detalla qué entrega: documentación técnica suficiente, límites y modos
de falla conocidos y acceso técnico dirigido para pruebas y validación. No
aplica si indicó claramente que el sistema no debe volverse de alto
riesgo.[^eu-ai-act][^ai-omnibus]

**Acuerdo escrito (25.4):** el proveedor de un sistema de alto riesgo y el
tercero que le suministra sistemas, modelos, herramientas, servicios o
componentes deben especificar por escrito la información, capacidades y acceso
técnico necesarios. No aplica a componentes libres y de código abierto distintos
de modelos GPAI. Aquí entra el contrato con el proveedor del LLM.[^eu-ai-act]

# Obligaciones del desplegador (art. 26, p. 67-69)

| Apartado | Obligación |
|---|---|
| 26.1 | Medidas técnicas y organizativas para usar el sistema conforme a las instrucciones |
| 26.2 | Encomendar la supervisión humana a personas con competencia, formación y autoridad |
| 26.4 | Asegurar datos de entrada pertinentes y representativos, en lo que controle |
| 26.5 | Vigilar el funcionamiento; ante riesgo, informar al proveedor y a la autoridad y **suspender el uso**; ante incidente grave, avisar primero al proveedor |
| 26.6 | Conservar los logs bajo su control al menos 6 meses |
| 26.7 | Si es empleador, informar a trabajadores y representantes antes de usar un sistema de alto riesgo en el lugar de trabajo |
| 26.9 | Usar la información del proveedor (art. 13) para su evaluación de impacto de protección de datos |
| 26.11 | Informar a las personas físicas que están expuestas a un sistema de alto riesgo del Anexo III que toma o ayuda a tomar decisiones sobre ellas |
| 26.12 | Cooperar con las autoridades |

Además, **FRIA** (art. 27, p. 69) para organismos de Derecho público, entidades
privadas que prestan servicios públicos (salvo Anexo III punto 2) y desplegadores de
los puntos 5.b y 5.c del Anexo III: ver
[Anexo III](/frameworks/eu-ai-act-anexo-iii.md).

# Qué cambia para Acme Labs

| Pregunta | Lectura del repo a partir del texto |
|---|---|
| Rol por defecto en software propio para bancos | Proveedor |
| Rol cuando opera el sistema para sí mismo | Desplegador |
| Cuándo se pasa de desplegador o integrador a proveedor | Marca propia, modificación sustancial o cambio de finalidad (art. 25) |
| Quién hace la FRIA | El banco o aseguradora cliente, con insumos del proveedor |
| Qué pide el cliente al proveedor | Instrucciones de uso del art. 13, evidencia de pruebas, logs, soporte para incidentes y contrato del art. 25.4 |

# Cautelas

- Cotejada el 2026-10-20 contra el texto español del Reglamento (UE) 2024/1689 en el
  PDF del curso, p. 45-46 (arts. 2 y 3), 49 (art. 3.49), 51, 56-61, 62-64, 67-69, 78,
  81-82 y 101-102: artículos, apartados, plazos (10 años, 6 meses, 15, 2 y 10 días) y
  las doce obligaciones del art. 16 coinciden. Se corrigieron dos cosas: la cita
  del art. 4, que omitía "en la mayor medida posible", y el alcance de la FRIA, que
  omitía a los organismos públicos. Lo que el Reglamento dice del Anexo III y del
  rol del cliente es texto; las filas sobre Acme Labs (rol por defecto, escenarios
  (a) y (c) del art. 25, "un LLM usado para decidir crédito es alto riesgo") son
  aplicación del repo, y el segundo supuesto vale solo para evaluar la solvencia de
  personas físicas (Anexo III, punto 5.b).
- Las partes basadas en el Reglamento 2026/1744 (Omnibus) se cotejaron el 2026-10-21
  contra el texto español del DOUE L de 24.7.2026 (PDF de EUR-Lex, 41 p.): art. 4
  (p. 16), art. 4 bis (p. 17), art. 10.5 suprimido (p. 19), art. 17.2 y 25.2 y 25.4
  (p. 19-20) y art. 72.3 (p. 26). Coinciden; se corrigió la cita del art. 4 ("apoyar
  la promoción", no "apoyar el desarrollo") y el nombre del art. 4 bis.
- Ese cotejo llegó en el PR #55 (autor en GitHub: edu2020chaparro-ux; herramienta no
  declarada). La revisión del 2026-10-21 (claude-code/claude-opus-5-5) lo repitió
  sobre el PDF/A español del Omnibus bajado de Cellar, el repositorio de la Oficina de
  Publicaciones (41 p.). Las páginas coinciden. Precisó el art. 72.3: el acto de
  ejecución original (p. 101) pasa a ser orientaciones con un modelo (p. 26). La
  ficha queda en `draft` hasta una declaración humana nueva.
- Las entidades financieras tienen reglas propias que la ficha no recoge: arts. 17.4,
  18.3, 19.2, 26.5 (párr. 2) y 26.6 (párr. 2) los remiten a su normativa financiera, y el
  art. 72.4 permite integrar la vigilancia poscomercialización del Anexo III punto 5.
  Conviene mirarlos antes de afirmar qué obligaciones le caen a un banco.
- Aplicabilidad real a clientes locales: depende de si el resultado se usa en la
  UE (art. 2.1.c). Falta decidirlo por cliente; no hay dato en el repo.
- Las normas armonizadas (art. 40) y las especificaciones comunes (art. 41) para
  demostrar conformidad no se relevaron.

# Relacionado

[Overview](/frameworks/eu-ai-act.md),
[niveles de riesgo](/frameworks/eu-ai-act-niveles-riesgo.md),
[Anexo III](/frameworks/eu-ai-act-anexo-iii.md),
[calendario y sanciones](/frameworks/eu-ai-act-calendario-sanciones.md),
[M1U4](/unidades/m1u4-rol-gobernanza.md).

[^eu-ai-act]: Reg. (UE) 2024/1689, texto en español del DOUE; páginas del PDF indicadas en el texto.
[^eu-ai-act-eurlex]: Misma norma en EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[^ai-omnibus]: Reg. (UE) 2026/1744, art. 1 puntos 5, 6, 9, 11, 12 y 30, considerando (8), DOUE L de 24.7.2026; páginas del PDF en español indicadas en el texto.
