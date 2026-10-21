# Handoff de verificación — 20/10/2026

## Mandato para retomar

Martín pidió cerrar esta sesión con commit, push y PR. Para la continuación
indicó: «Lo que resta quiero que lo hagas en forma autónoma».

Avanzá con cotejos, correcciones, conciliaciones, chequeos y preparación de
entregables sin pedir confirmaciones de rutina. Conservá las decisiones
empresariales y los acuerdos del equipo que todavía no existen como tales.
No atribuyas a `human:lazynet` una verificación de material que no presentó y
confirmó: la autonomía operativa no reemplaza la declaración humana de OKF.

## Resultado de esta sesión

- Rama: `docs/verificacion-fuentes-caso`; base de trabajo `9d4566a`.
- Las 40 fichas de `context/` tienen verificación humana declarada: 17 `Hecho`
  y 23 `Supuesto`, confirmados individualmente o por bloques por Martín.
- Cada declaración registra `human:lazynet`, fecha 2026-10-20 y alcance.
  Los supuestos no se convirtieron en hechos ni en autorizaciones empresariales.
- Se corrigieron fuentes, cifras y cautelas antes de registrar cada confirmación:
  regulación, certificaciones, capacidad, rampas, costos, salidas y señales.
- No se modificaron slides, anexos, material ni defensa en esta rama.
- No se generó un nuevo PDF de entrega ni se verificó su disposición visual.

## Evidencia al cerrar el bloque de contexto

```text
.venv/bin/python scripts/okf-check.py --delivery --path context
✓ okf-check: 41 archivos conformes en entrega; solo estructura y declaración humana
```

Son 40 fichas más el índice. El chequeo de borrador del plan devuelve diez
slides y cero errores. El de entrega devuelve 119 errores: siete estados
`draft` (deck y seis anexos), 111 marcas de pendiente y un error agregado de
OKF por 45 fichas citadas de `material/` sin verificación humana.

Las 111 marcas no son 111 tareas independientes. El detector también alcanza
frontmatter, cautelas y condiciones futuras del plan. Clasificá faltantes
reales y condiciones de ejecución; conservá sus diferencias semánticas.
No suprimas cautelas ni declares evidencia inexistente para hacer pasar el gate.

Diagnósticos locales reproducibles, no versionados:

```sh
.venv/bin/python scripts/plan-check.py --mode draft --json > tmp/draft-check-verificacion-contexto.json
.venv/bin/python scripts/plan-check.py --mode delivery --json > tmp/delivery-check-verificacion-contexto.json
```

## Próximo bloque: fuentes citadas de la cursada

El backlog de fuentes es [#22](https://github.com/lazynet/tp-caio-g11-2026/issues/22).
Priorizá las 45 fichas que exige la entrega actual; el corpus completo tiene
132 fichas leídas como `draft`. El alcance necesario se obtiene del campo
`evidence` de `plan-check --mode delivery --json`, sin verificar todo el corpus
por navegación de índices.

La siguiente ficha preparada para revisar es
`material/conceptos/m1u1-diagnostico-madurez-5-dimensiones.md`, todavía `draft`.
Se cotejaron M1U1 corta, páginas 6-10, y extendida, páginas 8-9. También se abrió
el render de la página 7 corta, con dimensiones y pasos. Las fuentes originales
siguen fuera del repo; su ubicación se consulta en `private/sources.md`.

Correcciones que debe incorporar esa revisión:

- La respuesta completa del caso de supermercados termina en la página 10,
  por lo que la cita corta de páginas 6-9 queda incompleta.
- Las cinco dimensiones y los niveles 1, 3 y 5 pertenecen al marco didáctico.
  Los niveles 2 y 4 requieren criterio explícito; no hay una regla de promedio
  validada en esas páginas para producir un puntaje organizacional único.
- La variante extendida usa otras dimensiones. Su mención de Gartner y NovaGob
  es una atribución del curso, sin cotejo de esas fuentes primarias.
- Verificar la fidelidad al curso no acredita la madurez real de Acme Labs.

No se presentó este bloque para confirmación humana en la sesión: Martín
pidió primero un estado y luego cerrar. Prepará la revisión autónomamente y
mantené identificado el requisito humano que reste.

## Conciliaciones que siguen en los anexos

Respetá el dueño de cada archivo y los responsables de `README.md`. La lista
siguiente es contexto de continuidad, no reemplaza el backlog de GitHub.

- B, [#16](https://github.com/lazynet/tp-caio-g11-2026/issues/16): la cuenta de E
  es 1.068 h / 480 = 2,225 FTE; contra 2,25 quedan 0,025 FTE / 12 h trimestrales.
  B todavía declara 0,05 de holgura. La diferencia quedó explícita en la ficha
  `umbrales-tecnicos-propuestos.md`.
- D, [#18](https://github.com/lazynet/tp-caio-g11-2026/issues/18): todavía imputa
  toda la documentación mínima del contractor al 0,8; B y la ficha revisada la
  imputan a la fracción que produce cada entregable, 0,8 o 0,2. También revisar
  las afirmaciones de capacidad aceptada y absorción automática de horas.
- E, [#19](https://github.com/lazynet/tp-caio-g11-2026/issues/19): alinear el
  tratamiento de capacitación interna como tiempo y gastos externos como caja;
  los pisos 1,6-1,8 FTE pertenecen a alternativas amplias, no al mínimo vigente.
- B/C, [#16](https://github.com/lazynet/tp-caio-g11-2026/issues/16) y
  [#17](https://github.com/lazynet/tp-caio-g11-2026/issues/17): conciliar los
  alcances distintos de red team, sin elegir un precio ni sumar ambos por defecto.
- B/E: el umbral central del gateway a 6× es 33.000 / (6 × 21.500) = 25,581395…%,
  no un corte exacto de 25%. Con tarifa plana no hay ahorro de precio.
- B/F, [#20](https://github.com/lazynet/tp-caio-g11-2026/issues/20): ±3 pp y N≥15
  no garantizan paso de productividad. El ejemplo base necesita semianchos
  ≤0,75 pp en M6 y ≤1 pp en M9; decide el límite inferior real del bootstrap.

## Secuencia de continuación

1. Cotejar las 45 fuentes necesarias, corregir atribuciones y números, y separar
   cotejo del agente de declaración humana. Revisar `material/huecos.md` antes
   de usar cifras y fuentes regulatorias vigentes antes de afirmar su alcance.
2. Conciliar los anexos con las fichas revisadas. Recalcular componentes y
   mantener separados mínimo, paquete completo y continuidad del producto.
3. Clasificar las marcas del gate y resolver los faltantes de entrega. Un plan
   sometido al board puede contener decisiones futuras sin afirmar que ocurrieron.
   Cualquier cambio del validador exige justificar el criterio y probar que no
   habilita borradores o evidencia sin revisión.
4. Completar las revisiones de sección; solo el dueño cambia cada anexo y `caio`
   edita el deck. No asignar responsables humanos nuevos ni inventar consenso.
5. Ejecutar `board-review` integral, después los chequeos y
   `CAIO_PYTHON=.venv/bin/python scripts/build-deck.sh entrega --delivery`.
   Abrir el render antes de afirmar que no hay desbordes; comprobar diez slides
   y PDF único menor de 10 MB. Registrar lo que continúe sin cumplir.

El PR de esta sesión entrega el bloque de contexto y este handoff; no cierra
la revisión integral ni habilita entrega. No se pidió merge en esta sesión.

## Particularidades del entorno

- No usar heredocs ad hoc: fallaron al crear temporales en este sandbox.
  Para chequeos cortos, `.venv/bin/python -c`; para scripts, `tmp/`, autorizado.
- Antes de editar, confirmar la rama: otra sesión trabajó sobre el mismo checkout.
  Para tareas concurrentes, usar worktree propio y coordinar por issue.
- Los PDFs originales no se copian al repo. Nada de datos internos, rutas
  corporativas o credenciales debe entrar en el handoff ni en el PR.
- El PRJ se actualiza con `vaultkit`, con diff previo, sin commitear el vault.
  El aviso de más de 5.000 palabras no autoriza archivar el historial por cuenta propia.
