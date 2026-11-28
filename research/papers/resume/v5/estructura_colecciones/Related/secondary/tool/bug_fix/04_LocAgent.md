# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *LocAgent: Graph-Guided LLM Agents for Code Localization*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/secondary/tool/bug_fix/04_LocAgent.md`
- PDF local referido; páginas físicas 3–9 / impresas 8699–8705 según lectura
- cobertura: Markdown íntegro; tablas/páginas seleccionadas cotejadas

## Pregunta y contribución
Localizar archivos, clases y funciones relevantes para tareas de mantenimiento mediante un grafo y herramientas de búsqueda.

## Método
- tarea: code localization, no generación de parches como objetivo principal
- grafo Python: directorios, archivos, clases y funciones
- relaciones: contain, import, invoke, inherit
- índices BM25 y herramientas de búsqueda, recorrido y entidades
- salida: ubicaciones candidatas

## Documentos y arquitectura
- no genera documentación humana ni arquitectura textual
- aporta navegación estructural y trazabilidad a entidades/archivos
- no selecciona documentación por requisito

## Evaluación
- SWE-bench-Lite y Loc-Bench (560 tareas)
- métricas Acc@k de localización
- hasta 92,7% de exactitud file-level Acc@5 con Qwen2.5-Coder-32B afinado, según reporte
- resolución downstream reportada con mejoras

## Artefactos
- repositorio público anunciado
- disponibilidad, licencia, modelo fine-tune y ejecución no comprobados

## Relación con nuestra tesis
Puede informar selección/localización de archivos de API antes de recuperar documentos asociados. No sustituye el experimento central ni demuestra valor documental.

## Riesgos
- posible solapamiento train/test en SWE-bench-Lite; requiere comprobar separación exacta
- Loc-Bench busca reducir contaminación usando issues posteriores a octubre de 2024, pero no garantiza eliminación
- métricas de localización no equivalen a Pass@1/API F1

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Grafo y herramientas | mismo archivo | §§3–5; físicas 3–9 | Hecho extraído |
| Loc-Bench y Acc@k | mismo archivo | tablas físicas referidas 7–8 | Hecho reportado |

## Pendientes
- confirmar split train/test y fechas
- verificar artefacto y modelos
- definir uso de localización separado de recuperación documental
