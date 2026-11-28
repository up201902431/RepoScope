# RepoMind

## Identidad
- **paper_id:** no asignado en el catálogo local; identificador provisional: `RepoMind`.
- **Título:** *RepoMind: Enhancing Repository-Level Code Generation via LLM Reasoning over Structured Repository Documentation*.
- **Autores:** Songwen Gong, Mengzhen Wang, Jiexin Wang y Yi Cai.
- **Año/venue:** ICPC ’26, 12–13-abr-2026. DOI `10.1145/3794763.3794823`. PDF de 12 páginas, impresas 355–366.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/primary/RepoMind.md`; PDF: `research/papers/pdf/Same Solution/primary/RepoMind.pdf`.
- **Procedencia/cobertura:** lectura íntegra del Markdown declarada por el especialista; portada y rasters de páginas físicas 7–9 revisados. PDF completo no inspeccionado visualmente. Extracción automática local.
- **Grupo/etiquetas:** se conserva `Same Solution/primary`, sin afirmar aprobación formal.

## Pregunta y contribución
**Hecho del paper:** RepoDocsAgent construye documentación jerárquica de repositorios y un agente de recuperación razona sobre ella para localizar APIs funcionalmente relevantes.

**Interpretación:** es un antecedente cercano a documentación generada y recuperación condicionada por requisito, pero no prueba el enlace a documentación humana preexistente.

## Método
- **Entrada/salida/tarea:** requisito y código/contexto del repositorio; salida, función Python.
- **Documentación generada:** RepoDocsAgent produce API-Doc, File-Doc y Module-Doc bottom-up. DocsWriter genera descripciones; DocsVerifier las evalúa y recomienda revisión.
- **Recuperación:** UniXcoder vectorial obtiene APIs similares como guía inicial. Un Reasoning-Retrieval Agent explora directorios/módulos y archivos top-down mediante herramientas, selecciona APIs funcionalmente relevantes y valida sus rutas. Combina selección razonada y similar; el paper describe un conjunto final de cinco APIs.
- **Generación:** contexto API combinado con requisito/contexto de archivo. La documentación es insumo de recuperación, no producto final evaluado.
- **Granularidad:** función/API, archivo y directorio/módulo Python. No genera diagramas ni modelo arquitectónico.

## Documentos y arquitectura
API-Doc, File-Doc y Module-Doc son descripciones generadas jerárquicamente desde el repositorio. El artículo no establece aquí procedencia a nivel de afirmación ni distingue esos documentos de documentación humana. No presenta arquitectura visual.

## Evaluación
- **Benchmarks/subconjuntos:** subconjunto Python de CoderEval: 207 tareas tras exclusiones; DevEval: 1.742 muestras tras exclusiones.
- **Modelos/métrica:** GPT-4o-Mini, DeepSeek-V3 y Qwen3-235B-A22B, accesibles por API; Pass@1.
- **Resultados reportados:** Tabla 1, CoderEval: 47,34/56,04/52,17; DevEval: 37,37/48,34/44,89 para los tres modelos, respectivamente. Tabla 2 contiene ablaciones en CoderEval.
- **Cautela comparativa:** la nota de Tabla 1 dice que RepoScope se tomó del paper original porque RepoMind no había liberado código y no se realizaron las comparaciones de RQ con ese método. RepoScope anuncia paquete de réplica en su artículo. La discrepancia no se resolvió externamente.
- **Límites:** evaluación en los subconjuntos descritos y modelos remotos; sin reproducción local.

## Artefactos
El paper dice que el código “will be released” en `https://github.com/ABigTrouble/RepoMind`. Es una promesa del artículo, no comprobación de disponibilidad actual ni reproducción. No se verificaron licencia ni contenido.

## Relación con nuestra tesis
**Interpretación acotada:** antecedente para documentación generada y recuperación requirement-aware. Para adaptarlo habría que separar documentación humana de generada, registrar origen/commit, impedir que la documentación derive de la solución objetivo y evaluar el enlace documental–API. Sus API-Docs no deben tratarse como documentación humana.

## Riesgos
- El paper reconoce posible contaminación de repositorios en entrenamiento de modelos.
- Documentación generada desde el repositorio puede incorporar cuerpo, comentarios o derivados de la función objetivo. La lectura no verificó una política suficiente de ocultación antes de construir RepoDocs.
- La comparación de RepoScope citada tiene una discrepancia documental sobre disponibilidad de código que queda sin resolver.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Identidad y publicación | PDF/Markdown; raster portada | 1 | 355 | Metadato |
| Pipeline de RepoDocs y recuperación | PDF/Markdown local | §§3.1–3.5, 4–6 | 358–360 | Método |
| Tablas 1–3 y ablaciones | PDF y rasters locales | 7–9 | 361–363 | Resultados reportados |

## Pendientes
Auditar ocultación de objetivo/derivados antes de indexación y generación; aclarar exclusiones de evaluación; verificar disponibilidad y versión del paquete en una tarea autorizada.
