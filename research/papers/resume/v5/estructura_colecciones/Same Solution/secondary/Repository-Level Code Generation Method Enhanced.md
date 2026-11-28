# Repository-Level Code Generation Method Enhanced by Context-Dependent Graph Retrieval

## Identidad
- **paper_id:** provisional `context-dependent-graph-retrieval`; sin ID canónico local.
- **Título:** *Repository-Level Code Generation Method Enhanced by Context-Dependent Graph Retrieval*.
- **Autores:** Hanxiao Zhang, Anqi Li, Zhirui Kuai, Zhao Wei, Li Kuang y Yingjie Xia.
- **Año/venue:** CollaborateCom 2024; proceedings LNICST 626 publicado en 2026; pp. impresas 42–61. DOI del capítulo `10.1007/978-3-031-93257-1_3`; DOI del volumen `10.1007/978-3-031-93257-1`.
- **Fuente de este lote:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/Repository-Level Code Generation Method Enhanced.md`; PDF del volumen homónimo.
- **Cobertura y extracción:** el Markdown contiene el volumen completo de 328 páginas físicas; el artículo pertinente está en PDF pp. 52–71 (impresas 42–61). Se leyó íntegro el artículo objetivo, no las otras contribuciones del volumen. Figuras y páginas pertinentes cotejadas visualmente.
- **Registro canónico:** esta ficha cubre las dos rutas fuente con el mismo título y DOI: `Same Solution/secondary/Repository-Level Code Generation Method Enhanced.md` y `Related/secondary/graph/Repository-Level Code Generation Method Enhanced.md`. La segunda ficha es una referencia de alias; no se cambia la clasificación fuente.
- **Grupo/etiquetas:** Same Solution / secondary como ubicación canónica de la ficha; se conserva `Related/secondary/graph` en la clasificación fuente y como alias.

## Pregunta y contribución
**Hecho:** propone generación de función Python desde firma/docstring usando un grafo dependiente del contexto y recuperación in-file/cross-file.

**Interpretación:** la selección de módulos puede motivar ideas para requisito y reutilización, pero el método operativo recupera entidades/resúmenes de código, no documentación con trazabilidad requisito-API.

## Método
- **Entrada/salida:** firma y docstring de función con repositorio → implementación de función.
- **Grafo RCDG:** archivos, clases y funciones; atributos incluyen tipo, nombre, ubicación, código y resumen semántico; relaciones de importación, invocación y contención. AST Python y lógica de dependencias.
- **Recuperación:** subgrafo in-file, BFS cross-file desde archivo actual con profundidad limitada y nodos similares por HGT; LLM juzga relevancia de entidades.
- **Generación:** prompt combina contexto in-file/cross-file y requisitos, con instrucciones CoT y reutilización.

## Documentos y arquitectura
El paper menciona documentación API e historial entre posibles fuentes de conocimiento, pero método descrito opera sobre código, resúmenes generados y dependencias. No reporta indexación/recuperación trazable de documentos humanos ni generación arquitectónica.

## Evaluación
- **Benchmark:** CoderEval4Python, 230 tareas, 46 repositorios, cerca de 30% standalone y 70% dependientes de contexto.
- **Configuración/métricas:** GPT-3.5-Turbo para resumen, juicio y generación; temperatura 1, n=10; pass@k con n=10, CodeBLEU y recall@k de reutilización de APIs personalizadas.
- **Resultados:** Tabla 1 reporta 51,61/67,63/72,17% pass@1/5/10, CodeBLEU 0,57 y recall@1 0,60. Tabla 2: añadir contexto cross-file a in-file+import eleva pass@1 de 51,43% a 51,61%, mientras recall@1 baja 0,61→0,60. No atribuir esos cambios a una sola causa. Tablas 1–3 en PDF pp. 65–68 (impresas 55–58), cotejadas visualmente; usar orden visual de columnas porque extracción textual altera el orden.
- **Límites:** evaluación solo Python; construcción de grafos y recuperación requieren tiempo/esfuerzo. La definición de recall@k de APIs no queda completamente operacionalizada.

## Artefactos
El artículo declara datos en `github.com/Rinkalin/RCDG`; no se verificaron acceso, contenido, licencia ni ejecución.

## Relación con nuestra tesis
Antecedente para relaciones de dependencia y selección de módulos según contexto; requeriría fijar APIs de RepoScope y añadir asociación explícita API-documento-requisito. No sustituye baseline ni demuestra el efecto de documentación.

## Riesgos
No equiparar recall@k de APIs con API P/R/F1 de la tesis. Control de fuga/ocultación de función objetivo no se verificó en la lectura.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad y DOI | Artículo en PDF/Markdown; portada raster | 52 (42) | Hecho, cotejado visualmente |
| Firma/docstring y grafo | Markdown; §3.1–3.2, Fig. 1 | 56–59 (46–49) | Hecho |
| BFS, HGT y juicio de entidad | Markdown; §3.3, Fig. 2 | 59–61 (49–51) | Hecho |
| Benchmark y parámetros | Markdown; §§4.2–4.4 | 62–64 (52–54) | Hecho |
| Resultados y columnas | Markdown; Tablas 1–3; rasters revisados | 65–68 (55–58) | Hecho reportado |
| Duplicado en ficha Related/secondary/graph | Ficha local con mismo título y DOI | No aplica | Identidad cotejada |
| Diferencia con documentación requerida | Brief frente al método | No aplica | Interpretación |

## Pendientes
No se revisaron las otras contribuciones del volumen, que no forman parte del artículo de esta ficha. No verificar artefactos sin autorización.
