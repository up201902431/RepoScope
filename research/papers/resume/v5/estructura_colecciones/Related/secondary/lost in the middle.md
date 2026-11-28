# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título canónico: *Lost in the Middle: How Language Models Use Long Contexts*
- ruta fuente: `research/papers/text/v5/estructura_colecciones/Related/secondary/lost in the middle.md`
- **Registro canónico:** esta ficha cubre también la copia local `Related/secondary/full_text.md`; esa ruta de resumen es una referencia de alias.
- PDF local referenciado: `research/papers/pdf/Related/secondary/lost in the middle.pdf`
- **Cobertura:** Markdown íntegro revisado; ambas rutas fuente contienen la misma extracción del artículo. PDF visualmente no auditado página por página.

## Pregunta y contribución
Estudiar cómo cambia el rendimiento al mover evidencia relevante dentro de un contexto largo.

## Método
- QA multodocumento con posición controlada
- clave-valor sintético con varios pares y longitud variable
- medición de respuesta frente a recall del recuperador
- comparación de posiciones/arquitecturas según el estudio

## Documentos y arquitectura
- no es documentación de repositorios ni arquitectura
- aporta un principio metodológico para ordenar contextos recuperados
- no establece trazabilidad requisito-código-documento

## Evaluación
- observación principal: forma de U, con peor desempeño en el medio
- QA abierto: el lector puede saturar antes que el recall del recuperador
- cifras detalladas pendientes de cotejo visual de tablas/figuras

## Artefactos
- código/datos anunciados por el paper
- disponibilidad real no comprobada

## Relación con nuestra tesis
Aplicable al diseño de pruebas de posición de documentos/API references. Debe tratarse como control metodológico, no como evidencia de que documentos mejoren código.

## Riesgos
- extrapolar de NLP a software puede ser engañoso
- no prueba generación ni API awareness
- el orden puede interactuar con límites de ventana y modelo

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Extracto íntegro coincide con ruta alias | `secondary/lost in the middle.md` y `secondary/full_text.md` | PDF físicas 1–17 / impresas 157–173 | Hecho de alias |
| Posición de evidencia | ambos archivos | §§2–5; físico 5–10 | Hecho del paper |

## Pendientes
- confirmar la canonicalización y metadatos
- conservar ambas rutas como alias
