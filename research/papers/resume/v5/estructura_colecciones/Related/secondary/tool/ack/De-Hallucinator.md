# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *De-Hallucinator: Mitigating LLM Hallucinations in Code Generation Tasks via Iterative Grounding*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/secondary/tool/ack/De-Hallucinator.md`
- PDF local referido por la extracción
- cobertura: Markdown íntegro; tablas/páginas seleccionadas cotejadas

## Pregunta y contribución
Reducir referencias a APIs inexistentes o incorrectas añadiendo iterativamente contexto anclado en el proyecto.

## Tipo de tarea
- completado de código Python
- generación de tests JavaScript
- mitigación de alucinaciones de API

## Método
- entrada: código incompleto/proyecto o paquete JavaScript
- indexación de funciones, clases, atributos y referencias
- recuperación inicial desde prompt
- recuperación iterativa desde predicciones sucesivas
- prompt aumentado con referencias y reconsulta al LLM
- salida: código/tests fundamentados

## Documentos y arquitectura
- no genera documentación humana ni arquitectura
- conserva referencias a APIs y firmas del proyecto
- técnica de grounding candidata para enlazar APIs recuperadas con documentos
- no hay trazabilidad requisito-documento ni selección documental

## Evaluación
- completado: mejoras relativas reportadas 23,3–50,6% en distancia de edición y 23,9–61,0% en API match
- tests JavaScript: mejora relativa reportada de 63,2% en tests con alucinaciones mitigadas
- métricas incluyen edit distance/similarity y API match; la dirección de una etiqueta edit-similarity debe verificarse
- completado usa best@k, no necesariamente Pass@1

## Artefactos
- el texto indica repositorio público
- disponibilidad, licencia, versión y ejecución no verificadas

## Relación con nuestra tesis
Es el antecedente técnico más cercano para grounding iterativo sobre APIs recuperadas. Puede adaptar el mecanismo para añadir documentación enlazada, pero no es el módulo documental ni prueba su aporte.

## Riesgos
- completado retira líneas objetivo/imports asociados según el paper, pero el resto del contexto debe auditarse
- best@k no equivale a Pass@1
- reindexación y refinado pueden incorporar soluciones si no se congela el snapshot

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Iteración y tipos de API indexados | mismo archivo | §§3.1–3.4; físicas 3–5 | Hecho extraído |
| Métricas y tabla | mismo archivo | §5.1.4 y tabla 3; física 7 | Hecho reportado |

## Pendientes
- cotejar tablas y etiqueta edit similarity
- verificar particiones, modelo y artefacto
- diseñar adaptación sin cambiar APIs recuperadas
