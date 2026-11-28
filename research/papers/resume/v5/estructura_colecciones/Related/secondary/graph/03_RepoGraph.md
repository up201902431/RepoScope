# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *REPOGRAPH: Enhancing AI Software Engineering with Repository-Level Code Graph*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/secondary/graph/03_RepoGraph.md`
- PDF local referido por la extracción, pendiente de cotejo completo
- cobertura: Markdown íntegro; páginas/figuras seleccionadas visualmente

## Pregunta y contribución
Representar repositorios como grafos de líneas/entidades para mejorar ingeniería asistida por IA y resolución de issues.

## Método
- tarea: localización/contextualización para resolución de issues y completado cross-file
- construcción AST/tree-sitter
- nodos: definiciones/referencias a nivel de línea
- relaciones: invocación y contención
- recuperación: ego-grafos k-hop desde términos de consulta
- salida: contexto gráfico para agentes o flujos existentes

## Documentos y arquitectura
- representa arquitectura/código como grafo, no documentación humana
- no genera documentos ni enlaces requisito-documento
- la trazabilidad va entre términos, líneas, archivos y relaciones

## Evaluación
- benchmarks: SWE-bench-Lite y CrossCodeEval
- SWE-bench-Lite: resolve rate mejora en los cuatro métodos; ejemplo Agentless de 27,33% a 29,67%
- CrossCodeEval: mejoras reportadas en coincidencia de código e identificadores
- métricas completas y fórmulas pendientes

## Artefactos
- extracción indica repositorio público
- disponibilidad, licencia, código y ejecución no verificadas

## Relación con nuestra tesis
Fuente de contexto estructural y dependencia para recuperar módulos/APIs. No demuestra documentación vinculada o selección por requisito.

## Riesgos
- plugin gráfico puede incluir soluciones/archivos futuros si la vista no se restringe
- no se encontró auditoría explícita de fuga en la lectura
- métricas downstream no equivalen a Pass@1/API F1

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Grafo AST y ego-grafos | `03_RepoGraph.md` | §§3–4; páginas físicas referidas 4–9 | Hecho extraído |
| SWE-bench/CrossCodeEval | mismo archivo | tablas físicas referidas 7 y 9 | Hecho reportado |

## Pendientes
- verificar título, autores, versión y DOI
- auditar tablas y particiones
- comprobar artefacto y control de fuga
