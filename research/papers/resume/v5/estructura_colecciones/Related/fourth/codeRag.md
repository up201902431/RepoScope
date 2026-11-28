# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion*
- autores, año/venue, DOI: no verificados íntegramente en la extracción local; verificar portada y metadatos.
- fuente original: extracción Markdown local
- PDF/texto/procedencia: `research/papers/text/v5/estructura_colecciones/Related/fourth/codeRag.md`; PDF local referenciado por la extracción bajo `research/papers/pdf/Related/fourth/`
- grupo/etiquetas/aprobación: Related/fourth; retrieval/code completion; sin aprobación en catálogo
- cobertura de lectura: lectura íntegra del Markdown realizada por el lote; PDF no cotejado sistemáticamente

## Pregunta y contribución
¿Qué conocimiento del repositorio es relevante y necesario para completar código sin añadir contexto redundante o insuficiente? Hecho del texto extraído: el método combina consultas guiadas por log-probabilidad, recuperación por múltiples vías y reranking `BESTFIT`.

## Método
- tarea: completado de código a nivel de repositorio
- entrada: contexto de código y consulta derivada del punto de completado
- recuperación: vías múltiples y reranking basado en preferencia ajustada al contexto
- salida: fragmentos contextuales seleccionados y código completado
- unidad/granularidad: fragmentos y símbolos de repositorio; no se documenta como tarea de API-documento-requisito
- dependencias: recuperador/reranker y modelo de generación

## Documentos y arquitectura
- no es sistema de documentación humana ni genera documentos arquitectónicos
- la salida candidata es código y/o contexto de recuperación
- no se evaluaron generación documental, enlaces requisito-documento o procedencia documental

## Evaluación
- benchmarks mencionados: ReccEval y CCEval
- métricas y resultados localizables: la extracción informa mejoras frente a métodos previos, sin cifras completas verificables en esta lectura
- selección/exclusiones: no verificadas en el PDF
- modelos/configuración: no definidos en la síntesis disponible

## Artefactos
- enlace oficial anunciado en el texto; no comprobado aquí
- disponibilidad real, licencia, versión y reproducción: pendientes
- no confundir anuncio con ejecución local

## Relación con nuestra tesis
Puede informar recuperación y reranking de contexto. No demuestra que documentación asociada a APIs recuperadas mejore Pass@1/API F1. Para reutilizarlo habría que aislar el ranking documental del ranking de código y mantener APIs recuperadas fijas.

## Riesgos
- fuga por índices o documentos derivados que contengan el objetivo
- comparabilidad limitada por tareas y métricas distintas
- no se verificó cobertura de historia, particiones ni exclusiones

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Consultas guiadas, vías múltiples y BESTFIT | `research/papers/text/v5/estructura_colecciones/Related/fourth/codeRag.md` | abstract y método; PDF no cotejado sistemáticamente | Hecho extraído |
| Evaluación en ReccEval/CCEval | mismo archivo | secciones de evaluación de la extracción | Hecho extraído |
| Relación con documentación/API: no evaluada | síntesis del lote | interpretación | Interpretación |

## Pendientes
- confirmar título, autores, año/venue, DOI y páginas
- cotejar tablas de resultados y definición de métricas
- verificar artefacto oficial y particiones
