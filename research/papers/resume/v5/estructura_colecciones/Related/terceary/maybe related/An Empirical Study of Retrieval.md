# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/terceary/maybe related/An Empirical Study of Retrieval.md`
- cobertura: Markdown íntegro; tablas/paginación no cotejadas visualmente

## Pregunta y contribución
Estudiar recuperación y fusión de contexto para generación de código y sus limitaciones.

## Método
- modelos: CodeGen, UniXcoder y CodeT5
- benchmarks: CONCODE, CoNaLa y HearthStone
- recuperación: BM25 y alternativas
- integración: Sequential Integration Fusion y Sketch Filling Fusion
- salida: código generado

## Documentos y arquitectura
- recuperación de ejemplos/código, no documentación humana
- no hay trazabilidad requisito-documento-API
- no genera documentación o arquitectura

## Evaluación
- compara recuperación y estrategias de fusión
- concluye mejoras con recuperación en su configuración
- recomienda BM25 y SIF por conveniencia/resultados
- resultados específicos a modelos/datasets/particiones

## Artefactos
- extracción no permite confirmar disponibilidad reproducible

## Relación con nuestra tesis
Antecedente metodológico para diseño de recuperación y fusión. No demuestra que documentación humana/generada mejore el baseline.

## Riesgos
- benchmarks antiguos y tareas distintas
- posible solapamiento entre datos y particiones no auditado
- métricas no son API P/R/F1/Pass@1 del protocolo actual

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Modelos/datasets y fusión | mismo archivo | método/evaluación; páginas impresas 188:1–188:28 según extracción | Hecho extraído |
| Conclusiones sobre recuperación | mismo archivo | conclusión | Hecho reportado |

## Pendientes
- verificar autoría, year/venue y DOI
- cotejar tablas y particiones
- verificar artefacto y fuga
