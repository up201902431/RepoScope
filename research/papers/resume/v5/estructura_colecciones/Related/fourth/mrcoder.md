# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título extraído: *MRCoder: An Efficient Context Selecting Approach for Repository-Level Code Generation*
- autores/año/venue/DOI: no cerrar metadatos; la referencia extraída contiene DOI/campos inconsistentes
- fuente: `research/papers/text/v5/estructura_colecciones/Related/fourth/mrcoder.md`
- PDF: ruta referenciada localmente bajo `research/papers/pdf/Related/fourth/mrcoder.pdf`, pendiente de cotejo bibliográfico
- cobertura: Markdown leído íntegramente; tablas y páginas no cotejadas visualmente

## Pregunta y contribución
Seleccionar contexto eficientemente para generación de código a nivel de repositorio, reduciendo tokens e inferencia sin perder precisión.

## Método
- entrada: requisito/función incompleta y contexto del repositorio
- fase Map: borradores sobre contextos particionados
- señales de selección: consistencia de API y similitud lógica
- fase Reduce: agrega contexto refinado
- verificación paralela: valida candidatos antes de la salida
- salida: implementación de código
- tarea: generación a nivel de repositorio

## Documentos y arquitectura
- no genera documentación humana ni establece enlaces requisito-documento
- produce contexto de código recuperado y seleccionado
- no hay origen documental etiquetado ni procedencia de afirmaciones

## Evaluación
- benchmarks reportados: CoderEval y DevEval
- modelos reportados: Qwen2.5-Coder y DeepSeek-Coder
- resultados de la extracción: mejoras de precisión y reducción de tokens del 30–50%, con hasta 52% menos tiempo de inferencia
- estos valores deben cotejarse con tablas y configuraciones originales

## Artefactos
- extracción declara código y datos disponibles
- disponibilidad, licencia, versión y ejecución: no comprobadas

## Relación con nuestra tesis
Puede inspirar un selector de contexto. Pero su selección está orientada a código y consistencia de APIs, no a documentación asociada según requisito. No usar sus cifras como comparativas hasta fijar el protocolo común.

## Riesgos
- ahorro reportado puede depender de modelos/benchmarks concretos
- selección Map/Reduce puede filtrar el objetivo si no se congela la vista
- la métrica de precisión no está definida ni vinculada a API P/R/F1

## Evidencia
| Afirmación | Fuente/archivo | Sección/página | Tipo |
|---|---|---|---|
| Selección Map/Reduce y verificación | `research/papers/text/v5/estructura_colecciones/Related/fourth/mrcoder.md` | método de extracción, PDF pp. 2–23 referidas | Hecho extraído |
| CoderEval/DevEval y modelos | mismo archivo | evaluación de la extracción | Hecho extraído |
| Ahorro 30–50%/52% | mismo archivo | resumen extraído; cotejo pendiente | Declaración reportada |

## Pendientes
- verificar metadatos, DOI y año
- cotejar tablas y fórmulas
- comprobar artefactos, particiones y fuga
