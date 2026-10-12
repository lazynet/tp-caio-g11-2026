---
type: Concepto
title: EU AI Act, Anexo III de alto riesgo (foco banca y seguros)
description: Los ocho ámbitos del Anexo III con sus casos de uso, y el detalle de los puntos 5.b (scoring crediticio) y 5.c (seguros de vida y salud) que tocan a un proveedor de software financiero.
tags: [compliance, regulacion, alto-riesgo, scoring, eu-ai-act]
sources:
  - id: eu-ai-act
    resource: EU AI Act 2024.pdf
    title: Reg. (UE) 2024/1689, Anexo III (p. 127-129), arts. 6, 12, 17, 18, 19, 26, 27, 43, 49, 72
  - id: eu-ai-act-eurlex
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    title: Reg. (UE) 2024/1689 en EUR-Lex (fuente primaria)
  - id: ai-omnibus
    resource: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
    title: Reg. (UE) 2026/1744, Digital Omnibus on AI, DOUE L de 24.7.2026
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

# Qué es el Anexo III

Es la lista de casos de uso que el art. 6.2 declara de alto riesgo. Es la vía
que aplica al software para banca y seguros. La clasificación depende del
**uso previsto**, no de la tecnología: el mismo modelo es de alto riesgo si se
ofrece "para evaluar solvencia" y no lo es si se ofrece "para detectar
fraude".[^eu-ai-act] Ver las [reglas de clasificación y la excepción del
art. 6.3](/frameworks/eu-ai-act-niveles-riesgo.md).[^eu-ai-act-eurlex]

# Lista completa (p. 127-129)

| Pto. | Ámbito | Casos de uso |
|---|---|---|
| 1 | Biometría (si el derecho lo permite) | a) identificación biométrica remota (excluye verificación 1:1 cuya única finalidad es confirmar que alguien es quien dice); b) categorización biométrica por atributos sensibles; c) reconocimiento de emociones |
| 2 | Infraestructuras críticas | Componentes de seguridad en infraestructuras digitales críticas, tráfico rodado, suministro de agua, gas, calefacción o electricidad |
| 3 | Educación y formación | a) acceso o admisión; b) evaluar resultados de aprendizaje; c) nivel de educación adecuado; d) vigilancia de conductas prohibidas en exámenes |
| 4 | Empleo y gestión de trabajadores | a) reclutamiento y selección (filtrar CV, evaluar candidatos); b) decisiones sobre condiciones laborales, promoción, despido, asignación de tareas por comportamiento o rasgos, y supervisión y evaluación del desempeño |
| 5 | Servicios esenciales, privados y públicos | a) autoridades públicas: elegibilidad a prestaciones; **b) solvencia y calificación crediticia de personas físicas, salvo detección de fraude financiero; c) evaluación de riesgos y fijación de precios en seguros de vida y de salud**; d) clasificación de llamadas de emergencia, despacho y triaje |
| 6 | Cumplimiento del derecho (policía) | a) riesgo de ser víctima; b) polígrafos; c) fiabilidad de pruebas; d) riesgo de delinquir o reincidir; e) perfilado en investigaciones |
| 7 | Migración, asilo y fronteras | a) polígrafos; b) evaluación de riesgo de personas; c) examen de solicitudes de asilo, visado y residencia; d) detección e identificación de personas |
| 8 | Justicia y procesos democráticos | a) asistencia a autoridad judicial; b) influir en el resultado de elecciones o referendos (excluye herramientas logísticas de campaña) |

# Punto 5.b: scoring crediticio

Texto: sistemas "destinados a ser utilizados para evaluar la solvencia de
personas físicas o establecer su calificación crediticia, **salvo** los sistemas
de IA utilizados al objeto de detectar fraudes financieros" (p. 127).[^eu-ai-act]

Cómo leerlo para el plan:

- **Solo personas físicas.** El scoring de empresas (personas jurídicas) no está
  en 5.b.
- **La excepción es por finalidad.** Detección de fraude financiero queda afuera;
  un modelo de fraude que se reutilice para decidir un crédito entra.
- **Elaboración de perfiles = siempre alto riesgo.** El art. 6.3 no deja usar el
  filtro de "no riesgo importante" cuando el sistema perfila personas físicas, y
  un score perfila.[^eu-ai-act]
- **Otros usos bancarios** (AML/KYC, atención al cliente, cobranzas, antifraude)
  no están en la lista salvo que deriven en una decisión de acceso a crédito.
  Cobranzas y cobertura merecen revisión caso a caso: no se verificó que haya
  una interpretación oficial al respecto.

# Punto 5.c: seguros de vida y de salud

"Evaluación de riesgos y la fijación de precios en relación con las personas
físicas en el caso de los seguros de vida y de salud" (p. 127). No cubre seguros
de daños patrimoniales ni de autos.[^eu-ai-act]

# FRIA: evaluación de impacto en derechos fundamentales (art. 27)

Antes del primer uso, deben hacerla los desplegadores que sean organismos
públicos o presten servicios públicos, **y todos los desplegadores de sistemas
5.b y 5.c**, es decir, bancos, financieras y aseguradoras que usen scoring o
pricing de seguros de vida y salud. Contenido mínimo (p. 69):[^eu-ai-act]

1. Procesos en los que se usará el sistema, conforme a su finalidad.
2. Período y frecuencia de uso.
3. Categorías de personas y colectivos afectados.
4. Riesgos de perjuicio específicos para esos grupos (usando la información del
   art. 13 que da el proveedor).
5. Medidas de supervisión humana.
6. Medidas si los riesgos se materializan: gobierno interno y mecanismos de
   reclamación.

Se notifica el resultado a la autoridad de vigilancia del mercado (art. 27.3) y
la FRIA complementa la evaluación de impacto de protección de datos (RGPD art.
35) cuando ya la cubre. El Omnibus permite además referenciar secciones de la
EIPD en vez de duplicarlas.[^eu-ai-act][^ai-omnibus]

**Qué significa para un proveedor:** la FRIA la hace el cliente, pero necesita
del proveedor la documentación del art. 13 (instrucciones de uso con precisión,
límites y riesgos conocidos). Entregar esos insumos bien armados es un
diferencial comercial.

# Facilitaciones para entidades financieras

El Reglamento reconoce que la banca ya tiene gobierno interno regulado y le da
cierto alivio (p. 63-64, 68, 101):[^eu-ai-act]

| Artículo | Alivio |
|---|---|
| 17.4 | El **proveedor** que sea entidad financiera cumple el sistema de gestión de calidad si respeta sus reglas de gobierno interno sectoriales (salvo letras g, h, i del 17.1) |
| 18.3 y 19.2 | Documentación técnica y logs del proveedor que es entidad financiera se conservan dentro de la documentación del derecho financiero |
| 26.5 y 26.6 | El **desplegador** que sea entidad financiera cumple la vigilancia y la conservación de logs al respetar su gobierno interno sectorial |
| 72.4 | El plan de vigilancia poscomercialización de sistemas del Anexo III punto 5 de entidades financieras puede integrarse en sus planes existentes |

**Cautela de lectura:** 17.4, 18.3, 19.2 y 72.4 benefician al *proveedor que es
entidad financiera*, no a un proveedor de software independiente. El que se
beneficia aquí es el banco cliente como desplegador (26.5 y 26.6). Un
proveedor de software tiene el QMS completo.

# Obligaciones que activa el Anexo III

- Registro en la base de datos de la UE antes de comercializar (art. 49.1),
  salvo infraestructuras críticas (punto 2), que se registran a nivel nacional.
- Evaluación de la conformidad por **control interno (Anexo VI)** para los
  puntos 2 a 8, sin organismo notificado (art. 43.2). Solo la biometría (punto
  1) tiene la opción de organismo notificado en ciertos casos. Por lo tanto, el
  scoring y el pricing de seguros se autoevalúan.[^eu-ai-act]
- Certificados, si los hay, valen como máximo cuatro años para el Anexo III
  (art. 44.2).

Detalle de los requisitos y roles en
[proveedor y desplegador](/frameworks/eu-ai-act-proveedor-desplegador.md).

# Cuándo aplica

El Omnibus movió la aplicación del cap. III para los sistemas del Anexo III del
2 de agosto de 2026 al **2 de diciembre de 2027**. Ver el
[calendario](/frameworks/eu-ai-act-calendario-sanciones.md).[^ai-omnibus]
El Omnibus no modificó el texto del Anexo III (el listado de modificaciones del
Reglamento no lo incluye).[^ai-omnibus]

# Cautelas

- El Anexo III puede cambiar por acto delegado (art. 7); revisar la versión
  vigente antes de entregar.
- Falta contrastar con las guías de la Comisión sobre alto riesgo (art. 6.5).

[^eu-ai-act]: Reg. (UE) 2024/1689, texto en español del DOUE; páginas del PDF indicadas en el texto.
[^eu-ai-act-eurlex]: Misma norma en EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[^ai-omnibus]: Reg. (UE) 2026/1744, art. 1 puntos 13 y 40, DOUE L de 24.7.2026.
