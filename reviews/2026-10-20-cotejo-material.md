# Cotejo de material para la verificación humana — 20/10/2026

Paquete para que Martín declare la verificación humana de las 45 fichas de `material/`
que exige el gate de entrega (`plan-check.py --mode delivery`, campo `evidence`).

## Cómo se hizo

- Cuatro agentes (`claude-code/claude-sonnet-5-5`) cotejaron 44 fichas contra los PDF de la
  cursada, página por página, y contra las fuentes web accesibles. La sesión orquestadora
  consolidó `huecos.md` e `index.md` y repitió, contra el PDF, un cotejo de muestra por bloque.
- **Ninguna ficha está `verified`.** Todas quedan en `status: draft` hasta la declaración humana.
  El cotejo del agente no reemplaza esa declaración.
- Lo que no se pudo abrir quedó como "no cotejable" y está anotado en `# Cautelas` o en
  [huecos](/material/huecos.md).

## Qué tiene que confirmar Martín

Por ficha o por bloque: que acepta las correcciones y el alcance (`verified.scope`) propuesto.
Las filas en **negrita** traen una decisión o una corrección que cambia el contenido.

## Bloque m1a: M1U1 y M1U2

| Ficha | Resultado | Qué confirmar | `verified.scope` propuesto |
|---|---|---|---|
| [`conceptos/m1u1-diagnostico-madurez-5-dimensiones.md`](/material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md) | **corregida (parcialmente cotejable: Gartner/NovaGob no cotejados).** | que acepta los niveles 2 y 4 como "sin definir" y la cita a pp. 6-10. | M1U1 corta pp. 6-10 y extendida pp. 8-10 cotejadas contra el PDF; atribuciones a Gartner y NovaGob del curso sin cotejar; no acredita madurez de Acme Labs. |
| [`conceptos/m1u1-kill-fast.md`](/material/conceptos/m1u1-kill-fast.md) | corregida (solo citas y marcado de inferencias). | que las relaciones marcadas como del bundle quedan así. | M1U1 extendida pp. 2-4, 8 y 10 cotejadas contra el PDF; las relaciones con otros conceptos son lectura del bundle. |
| [`conceptos/m1u2-build-buy-agentificar.md`](/material/conceptos/m1u2-build-buy-agentificar.md) | **corregida.** | la redacción de FINMA (observación de supervisión, no obligación). | M1U2 pp. 2, 5-6 y 10 y FINMA 08/2024 (2.2 y 2.7) cotejadas; ejes de decisión y clasificación AI Act del ejemplo son atribución del curso; ejemplos ilustrativos. |
| [`conceptos/m1u2-kill-scale-gates.md`](/material/conceptos/m1u2-kill-scale-gates.md) | corregida (solo citas y cautelas). | que el ritmo trimestral queda como práctica del curso. | M1U2 pp. 2, 8 y 11 y FINMA 08/2024 cotejadas; el ritmo trimestral es práctica del curso, el inventario del AI Act es afirmación del curso sin cotejar; umbrales ilustrativos. |
| [`conceptos/m1u2-plan-100-dias.md`](/material/conceptos/m1u2-plan-100-dias.md) | corregida (solo citas). | nada fuera de la cita. | M1U2 pp. 1-2, 7 y 10-11 cotejadas contra el PDF; método del curso, no estándar ni cronograma de Acme Labs. |
| [`conceptos/m1u2-rice-ajustado-por-riesgo.md`](/material/conceptos/m1u2-rice-ajustado-por-riesgo.md) | corregida (solo citas). | nada fuera de la cita. | M1U2 pp. 2, 4-5 y 8 cotejadas contra el PDF y origen de RICE cotejado con ProductPlan (secundaria); la fórmula de ajuste por riesgo no existe en el curso. |

## Bloque m1b: M1U3 y M1U4

| Ficha | Resultado | Qué confirmar | `verified.scope` propuesto |
|---|---|---|---|
| [`conceptos/m1u3-anonimizacion-inferencia.md`](/material/conceptos/m1u3-anonimizacion-inferencia.md) | fiel | que el patrón de cuatro pasos y la tabla entrenamiento/inferencia reflejan la p. 6; que las herramientas se tratan como atribución del curso. | M1U3 (PDF de 13 páginas), p. 2, 6 y 12: PII, estrategias de entrenamiento e inferencia, patrón de enmascarar y revertir; herramientas como atribución del curso sin cotejo. |
| [`conceptos/m1u3-caso-tickets-sinteticos.md`](/material/conceptos/m1u3-caso-tickets-sinteticos.md) | **corregida (parcialmente cotejable en lo externo)** | que se acepta no usar "balanceado" ni "sin PII" mientras el PDF se contradiga; que la ficha se lea como receta del curso. | M1U3 (PDF de 13 páginas), p. 8-11 más blogs de Google Cloud de Gretel y BigQuery DataFrames: seis pasos y parámetros fieles al texto; contradicción texto/gráfico documentada; Gemini en BigQuery sin cotejar. |
| [`conceptos/m1u3-data-contracts.md`](/material/conceptos/m1u3-data-contracts.md) | **corregida** | que el YAML transcripto coincide con la p. 10. | M1U3 (PDF de 13 páginas), p. 2, 5, 6 y 10: definición, contenido, uso en Data Mesh, cláusulas de equidad y YAML de ejemplo; herramientas como atribución del curso. |
| [`conceptos/m1u3-estrategias-de-contexto.md`](/material/conceptos/m1u3-estrategias-de-contexto.md) | **corregida** | la tabla de cuatro estrategias contra la p. 7. | M1U3 (PDF de 13 páginas), p. 2, 7 y 8: las cuatro estrategias de contexto con ventajas y límites cualitativos; cifras de ventana como dato del curso 2024-2025. |
| [`conceptos/m1u3-higiene-de-datos.md`](/material/conceptos/m1u3-higiene-de-datos.md) | **corregida** | que el 5% no se use como dato en una slide. | M1U3 (PDF de 13 páginas), p. 2 a 6: prácticas de higiene, estructuración, normalización, escala y auditoría; la cifra del 5% como afirmación del curso sin fuente. |
| [`conceptos/m1u4-ai-omnibus-sigen.md`](/material/conceptos/m1u4-ai-omnibus-sigen.md) | **corregida (parcialmente cotejable)** | que se acepta citar fechas con Cooley hasta cotejar EUR-Lex, y la aclaración de que el AI Act no se declara aplicable a Acme Labs (ver `huecos.md`). | Lectura M1U4 p. 11, 19 y 25 más Cooley, Abreu, ERTICO y la Resolución SIGEN 197/2026 (texto en argentina.gob.ar): fechas y alcance contrastados con fuentes secundarias; EUR-Lex y anexo de SIGEN sin leer. |
| [`conceptos/m1u4-champions-y-literacy.md`](/material/conceptos/m1u4-champions-y-literacy.md) | **corregida** | la atribución de la cita a la slide 14. | Lectura M1U4 p. 10-11 y slide 14 de las slides v3: champions, condiciones de funcionamiento y AI literacy; art. 4 contrastado solo con Cooley y Abreu. |
| [`conceptos/m1u4-costo-por-outcome.md`](/material/conceptos/m1u4-costo-por-outcome.md) | fiel | nada fuera de la lectura contra la ficha. | Lectura M1U4 p. 12-13: costo por outcome aceptado, cinco ejemplos y cadena cost, adoption, outcome, value. |
| [`conceptos/m1u4-council-vs-coe.md`](/material/conceptos/m1u4-council-vs-coe.md) | fiel | que seguir la lectura y no la slide para los anti-patterns es lo que querés. | Lectura M1U4 p. 4 y slide 7: diferencias entre Council y CoE, funciones, nombres alternativos y anti-patterns; atribución a Microsoft como del curso. |
| [`conceptos/m1u4-criterios-gobierno-agentico.md`](/material/conceptos/m1u4-criterios-gobierno-agentico.md) | **corregida (parcialmente cotejable)** | que el 93% queda como atribución del curso, sin ir a una slide. | Lectura M1U4 p. 14-15 y 25, slides 17-19: cuatro variables, blast radius y límites del human-in-the-loop; cifras de Anthropic como atribución del curso, sin cotejo primario. |
| [`conceptos/m1u4-escala-autonomia-l0-l4.md`](/material/conceptos/m1u4-escala-autonomia-l0-l4.md) | fiel | que la tabla sigue la lectura y no la slide. | Lectura M1U4 p. 13-14 y slide 17: escala pedagógica L0-L4, definiciones y aclaración de que no es un estándar oficial. |
| [`conceptos/m1u4-eu-ai-act-nist-iso.md`](/material/conceptos/m1u4-eu-ai-act-nist-iso.md) | **corregida (parcialmente cotejable)** | si abrís ISO a mano para cerrar la edición vigente; el alcance del AI Act sobre Acme Labs. | Lectura M1U4 p. 18-20 y 23, slide 22, página de NIST AI RMF: función de los tres marcos y contenido del curso; ISO y EUR-Lex sin recotejar. |
| [`conceptos/m1u4-raci-ownership.md`](/material/conceptos/m1u4-raci-ownership.md) | fiel | el ejemplo RACI del copiloto contra la p. 9. | Lectura M1U4 p. 8-10 y slides 11-13: cinco roles de ownership, RACI con una sola A, ejemplo del copiloto comercial y ejercicio de refunds. |

## Bloque m2h: Harness, M2U3, M2U4, apunte y frameworks

| Ficha | Resultado | Qué confirmar | `verified.scope` propuesto |
|---|---|---|---|
| [`conceptos/harness-agente-modelo-mas-harness.md`](/material/conceptos/harness-agente-modelo-mas-harness.md) | fiel | que la definición, los siete componentes y la fórmula coinciden con las p. 14-15. | Memoria-Contexto-Harness.pdf, p. 14-15 (definición, siete componentes y fórmula Agente = Modelo + Harness); el párrafo 'Por qué importa' queda fuera, es lectura del repo. |
| [`conceptos/harness-cinco-elementos-diseno.md`](/material/conceptos/harness-cinco-elementos-diseno.md) | fiel | que los cinco elementos y su texto coinciden con la p. 16. | Memoria-Contexto-Harness.pdf, p. 16 (los cinco elementos de diseño); la tabla de relación con las fallas queda fuera, es lectura del repo. |
| [`conceptos/harness-diez-fallas-contexto.md`](/material/conceptos/harness-diez-fallas-contexto.md) | **corregida (menor)** | las diez fichas contra p. 3-12; mirar la p. 13 a mano si quiere precisar los labs. | Memoria-Contexto-Harness.pdf, p. 3-13 (diez fallas y labs) y las tres fuentes externas (Chroma 2025, Liu et al. 2023, Kurfali y Östling EMNLP 2025) abiertas el 2026-10-20. |
| [`conceptos/harness-tres-capas.md`](/material/conceptos/harness-tres-capas.md) | fiel | tabla, cita y recuadro contra la p. 15. | Memoria-Contexto-Harness.pdf, p. 15 (tabla de tres capas, cita atribuida a Harrison Chase y recuadro de dónde se construye el harness); atribución y productos no cotejados con fuente primaria. |
| [`unidades/memoria-contexto-harness.md`](/material/unidades/memoria-contexto-harness.md) | **corregida** | el mapa de páginas de la tabla (2, 3-12, 13, 14, 15, 16). | Memoria-Contexto-Harness.pdf, p. 1-16: estructura por páginas, tesis y ausencia de número de unidad. |
| [`conceptos/m2u3-grafo-humano-agente.md`](/material/conceptos/m2u3-grafo-humano-agente.md) | **corregida** | nodos y arcos (slide 14), cuatro objetivos (15), beneficios (17), cita (18). | M2U3 (archivo 'Unidad 7'), slides 13-18: definición de nodos y arcos, cuatro objetivos, beneficios y cita de cierre; la sección 'Cómo lo usa el plan' queda fuera, es lectura del repo. |
| [`conceptos/m2u3-tres-modos-ia.md`](/material/conceptos/m2u3-tres-modos-ia.md) | **corregida (menor)** | los tres textos de la slide 16. | M2U3 (archivo 'Unidad 7'), slide 16: las tres opciones de intervención de la IA y su descripción; la columna 'Quién decide' es lectura del repo. |
| [`conceptos/m2u4-evals.md`](/material/conceptos/m2u4-evals.md) | fiel | definición y tres dimensiones (slide 3), tres métricas (slide 17), y que el deck no tiene metodología de evals. | M2U4 (archivo 'Unidad 8'), slides 3 y 17: definición de evals, tres dimensiones y tres métricas del caso; la ausencia de metodología se verificó recorriendo las 20 slides. |
| [`conceptos/m2u4-tokenomics.md`](/material/conceptos/m2u4-tokenomics.md) | fiel | token ¾ palabra, costos, tres palancas y 60-80% (slides 12-15); que no usa el 60-80% en slides. | M2U4 (archivo 'Unidad 8'), slides 11-15, más el resumen de FrugalGPT y los multiplicadores de prompt caching de Anthropic consultados el 2026-10-20; el rango 60-80% se declara sin fuente. |
| [`conceptos/m2u4-versionado-release-gates.md`](/material/conceptos/m2u4-versionado-release-gates.md) | **corregida (menor)** | lista de la slide 8 y los cuatro gates de la slide 10 (están en una imagen). | M2U4 (archivo 'Unidad 8'), slides 7-10: versionado, qué se versiona (según slide 8) y los cuatro tipos de release gates. |
| [`apuntes/2026-09-29-tokenomics-aiops.md`](/material/apuntes/2026-09-29-tokenomics-aiops.md) | parcialmente cotejable | si asiste y sostiene el contenido del resumen, y si `author` y el título de la fuente están bien. Las cifras ya figuran como dudosas (360→7 ≈ 98%, no 66%). | Nota de clase del 2026-09-29 en LazyMind (resumen automático, sin transcripción): la ficha reproduce sus ideas; las cifras quedan declaradas sin fuente primaria. |
| [`frameworks/baic-perfiles-tecnologia.md`](/material/frameworks/baic-perfiles-tecnologia.md) | **corregida** | tres perfiles y las dos opciones de tecnología contra la p. 16. | BAIC, Guía GenAI, p. 16 (pasos 3 y 4): tres perfiles y las dos opciones de selección de tecnología; se omiten presupuesto, licencias y criterios de selección. |
| [`frameworks/eu-ai-act-proveedor-desplegador.md`](/material/frameworks/eu-ai-act-proveedor-desplegador.md) | **corregida; parcialmente cotejable (Omnibus no cotejable: fuente inaccesible)** | abrir EUR-Lex 2026/1744 a mano para el Omnibus; decidir si pide sumar las reglas de entidades financieras a la ficha. | Reglamento (UE) 2024/1689, texto español del DOUE (EU AI Act 2024.pdf), arts. 2, 3.3, 3.4, 3.49, 4, 9-21, 25-27, 43, 49, 72 y 73; las modificaciones del Reglamento 2026/1744 no se cotejaron. |

## Bloque m3: M3U1 a M3U4

| Ficha | Resultado | Qué confirmar | `verified.scope` propuesto |
|---|---|---|---|
| [`conceptos/m3u1-prompt-injection-jailbreaks.md`](/material/conceptos/m3u1-prompt-injection-jailbreaks.md) | **corregida (un matiz).** | que las siete defensas de la sección "Complemento OWASP" sirvan como complemento y no como contenido del curso (ya está rotulado así). | M3U1 (archivo Unidad 9) slides 3-6 y OWASP LLM01:2025 Prompt Injection leída el 2026-10-20; fidelidad al curso, no eficacia de las defensas. |
| [`unidades/m3u1-seguridad.md`](/material/unidades/m3u1-seguridad.md) | fiel (se agregaron citas de páginas). | que "el curso no cita estándares" se lea como afirmación sobre estas 20 slides. | M3U1 (archivo Unidad 9), 20 slides, estructura, cita y síntesis en tres capas; IDs OWASP LLM01/02/06/07 contra el Top 10 2025 leído el 2026-10-20. |
| [`conceptos/m3u2-ai-literacy-niveles.md`](/material/conceptos/m3u2-ai-literacy-niveles.md) | fiel. | que los dos ejes (profundidad y rol) no se crucen en una matriz del curso; eso ya está dicho en la ficha. | M3U2 (archivo Unidad 10) slides 3-6 y resumen visual pág. 1; fidelidad al curso, no el nivel de literacy de ninguna organización. |
| [`conceptos/m3u2-frenos-y-transicion.md`](/material/conceptos/m3u2-frenos-y-transicion.md) | fiel (cifra del 60% fiel a la slide, sin fuente primaria). | que el 60% siga fuera de las slides (ya figura en `huecos.md`). | M3U2 (archivo Unidad 10) slides 11-14 y resumen visual pág. 3; la cifra del 60% es afirmación del curso sin fuente primaria. |
| [`conceptos/m3u2-programa-champions.md`](/material/conceptos/m3u2-programa-champions.md) | fiel. | nada más que la lectura. | M3U2 (archivo Unidad 10) slides 7-10 y 18-19 y resumen visual pág. 2; fidelidad al curso, no la necesidad de una red de champions en Acme Labs. |
| [`conceptos/m3u3-compensacion-futuro-sintetico.md`](/material/conceptos/m3u3-compensacion-futuro-sintetico.md) | **corregida.** | la corrección de tres modelos más un principio (la versión anterior contaba cuatro). El Anexo D (`plan/annexes/04-personas-cultura.md`, fila de compensación) usa tres de los modelos con nombre y no cuenta "cuatro", así que no necesita cambio. | M3U3 (archivo Unidad 11) slides 11-14: tres modelos de compensación y el principio de transparencia y equidad salarial; son modelos prospectivos sin cifras. |
| [`conceptos/m3u3-deep-research-rol-critico.md`](/material/conceptos/m3u3-deep-research-rol-critico.md) | fiel. | que el horizonte de 18 meses del programa se adapte a 12 meses como decisión propia del plan. | M3U3 (archivo Unidad 11) slides 15-19 y programa del curso pág. 12 (plazo de 18 meses); fidelidad al curso. |
| [`conceptos/m3u3-perfil-talento-ai-ready.md`](/material/conceptos/m3u3-perfil-talento-ai-ready.md) | fiel. | nada más que la lectura. | M3U3 (archivo Unidad 11) slides 3-5: cuatro habilidades y tres pilares de adaptabilidad; marco sin niveles ni métricas. |
| [`conceptos/m3u3-transicion-responsable.md`](/material/conceptos/m3u3-transicion-responsable.md) | fiel (cifra del 70% fiel a la slide, sin fuente primaria). | que el 70% siga fuera de las slides (ya figura en `huecos.md`). | M3U3 (archivo Unidad 11) slides 6-10; la cifra del 70% de retención es afirmación del curso sin fuente primaria ni base de comparación. |
| [`conceptos/m3u4-estrategia-12-meses.md`](/material/conceptos/m3u4-estrategia-12-meses.md) | **corregida (un matiz).** | ninguna decisión; solo la lectura. | M3U4 (archivo Unidad 12) slides 2-5 y 18 y programa del curso pág. 11; sin metas ni umbrales de KPI en la fuente. |
| [`conceptos/m3u4-financial-storytelling.md`](/material/conceptos/m3u4-financial-storytelling.md) | fiel. | nada más que la lectura. | M3U4 (archivo Unidad 12) slides 12-14 y 18; sin fórmulas ni ejemplo numérico en la fuente. |
| [`conceptos/m3u4-roadmap-tridimensional.md`](/material/conceptos/m3u4-roadmap-tridimensional.md) | fiel. | nada más que la lectura. | M3U4 (archivo Unidad 12) slides 6-11: tres dimensiones, componentes y principios; sin hitos, fechas ni criterios de éxito. |

## `material/huecos.md`

Consolidado por la sesión orquestadora con las propuestas de los cuatro bloques.
Propuesta de `verified.scope`: "Estado del corpus al 2026-10-20 tras el cotejo de las 44 fichas
exigidas por la entrega; describe faltantes y cautelas, no acredita su contenido."
