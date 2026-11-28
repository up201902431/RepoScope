# RepoHYPER

## Identidad
- **paper_id:** provisional `repohyper`; sin ID canónico local.
- **Título:** *RepoHYPER: Search-Expand-Refine on Semantic Graphs for Repository-Level Code Completion*.
- **Autores:** Huy N. Phan, Hoang N. Phan, Tien N. Nguyen y Nghi D. Q. Bui.
- **Versión:** `arXiv:2403.06095v4`, fechado 14-ago-2024. No DOI ni venue indicados en el ejemplar local.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/RepoHyper.md`; PDF homónimo.
- **Alias:** RepoHyper, RepoHYPER y REPOHYPER son variantes tipográficas del mismo sistema en el material consultado.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo, 13 páginas físicas; portada y Tablas 1–4 cotejadas visualmente en rasters selectos.

## Pregunta y contribución
**Hecho:** completa la siguiente línea de código mediante búsqueda, expansión y refinamiento sobre grafo semántico del repositorio.

**Interpretación:** aporta expansión estructural/reranking de fragmentos; no recupera documentación ni prueba selección por requisito.

## Método
- **Entrada/salida:** fragmento incompleto y repositorio Python → código completado.
- **Grafo:** funciones/métodos, clases y nodos script; relaciones de importación, invocación, pertenencia, encapsulación y jerarquía.
- **Recuperación:** kNN busca nodos ancla; BFS exhaustivo o por patrones expande candidatos; predictor de enlaces GraphSAGE los ordena para LLM. Patrones de ruta se aprenden de consultas/contextos oro de entrenamiento.

## Documentos y arquitectura
El grafo representa código y relaciones estructurales, no documentos, arquitectura versionada o historial.

## Evaluación
- **Benchmarks:** RepoBench-R para recuperación y RepoBench-P para completion end-to-end; Cross-File-First y Cross-File-Random.
- **Métricas:** Accuracy@k para retrieval; EM y CodeBLEU para completion.
- **Resultados:** UniXcoder/RepoHyper: RepoBench-R Hard XF-F 25,81/49,51/61,19 acc@1/3/5; Hard XF-R 27,12/51,12/63,23. RepoBench-P con GPT-3.5-Turbo: XF-F EM 52,76/CodeBLEU 61,49; XF-R EM 64,06/CodeBLEU 71,59. Tabla 1 p. 6, Tabla 2 p. 7; visualmente cotejadas. Tabla 4 p. 8 informa ablación de patrón+link predictor frente a kNN.
- **Límites:** solo RepoBench; tipos de rutas se seleccionan manualmente y varían por lenguaje; recursos significativos y uso de modelos propietarios.

## Artefactos
El artículo indica implementación en repositorio anónimo de 4open.science. No se comprobó disponibilidad, contenido, licencia o ejecución.

## Relación con nuestra tesis
Prioridad interpretativa media-alta para ideas de expansión estructural sobre código. Requiere adaptar recuperación a documento asociado a API y requisito, con APIs recuperadas fijas; no adoptar el sistema completo ni tratarlo como generador documental.

## Riesgos
No confundir grafo semántico de código con documentación. No inferir causalidad ni comparar cifras de RepoBench directamente con otras tareas.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---:|---|
| Identidad y versión v4 | Markdown/PDF y raster de portada | 1 | Hecho, cotejado visualmente |
| Nodos y relaciones del RSG | Markdown; §3.1 | 3–4 | Hecho |
| Expansión y predictor | Markdown; §§3.2–3.3 | 4–5 | Hecho |
| Resultados y ablaciones | Markdown; Tablas 1–4; rasters revisados | 6–8 | Hecho reportado |
| Límites | Markdown; §8 | 9 | Hecho |
| Relevancia documental | Brief frente a método | No aplica | Interpretación |

## Pendientes
No se cotejó otra versión externa ni se verificó el repositorio de código.
